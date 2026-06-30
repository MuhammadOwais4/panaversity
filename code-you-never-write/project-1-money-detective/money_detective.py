"""
Money Detective — finds recurring charges, possible forgotten subscriptions,
and duplicate/repeated payments in a transaction history CSV.

Input CSV columns: date, description, amount
Usage: python money_detective.py sample_transactions.csv
"""

import csv
import sys
from collections import defaultdict
from datetime import datetime


def load_transactions(path):
    transactions = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            row["date"] = datetime.strptime(row["date"], "%Y-%m-%d")
            transactions.append(row)
    return transactions


def find_recurring_charges(transactions, min_occurrences=2):
    """Group by description+amount to find charges that repeat (likely subscriptions)."""
    groups = defaultdict(list)
    for t in transactions:
        if t["amount"] < 0:
            key = (t["description"], t["amount"])
            groups[key].append(t["date"])

    recurring = []
    for (desc, amount), dates in groups.items():
        if len(dates) >= min_occurrences:
            dates.sort()
            recurring.append({
                "description": desc,
                "amount": abs(amount),
                "occurrences": len(dates),
                "dates": [d.strftime("%Y-%m-%d") for d in dates],
                "total_spent": abs(amount) * len(dates),
            })
    recurring.sort(key=lambda x: -x["total_spent"])
    return recurring


def find_duplicate_payments(transactions, max_days_apart=2):
    """Flag same description+amount charged within a couple of days (possible duplicate billing)."""
    groups = defaultdict(list)
    for t in transactions:
        if t["amount"] < 0:
            key = (t["description"], t["amount"])
            groups[key].append(t["date"])

    duplicates = []
    for (desc, amount), dates in groups.items():
        dates.sort()
        for i in range(1, len(dates)):
            gap = (dates[i] - dates[i - 1]).days
            if gap <= max_days_apart:
                duplicates.append({
                    "description": desc,
                    "amount": abs(amount),
                    "date_1": dates[i - 1].strftime("%Y-%m-%d"),
                    "date_2": dates[i].strftime("%Y-%m-%d"),
                    "days_apart": gap,
                })
    return duplicates


def total_spend(transactions):
    return sum(t["amount"] for t in transactions if t["amount"] < 0)


def total_income(transactions):
    return sum(t["amount"] for t in transactions if t["amount"] > 0)


def main():
    if len(sys.argv) < 2:
        print("Usage: python money_detective.py <transactions.csv>")
        sys.exit(1)

    path = sys.argv[1]
    transactions = load_transactions(path)

    print("=" * 60)
    print("MONEY DETECTIVE REPORT")
    print("=" * 60)

    spend = total_spend(transactions)
    income = total_income(transactions)
    print(f"\nTotal spend this period: Rs {abs(spend):,.0f}")
    print(f"Total income this period: Rs {income:,.0f}")

    print("\n--- Likely Recurring Charges / Subscriptions ---")
    recurring = find_recurring_charges(transactions)
    if not recurring:
        print("None found.")
    for r in recurring:
        print(f"  {r['description']:<25} Rs {r['amount']:>8,.0f}  x{r['occurrences']}  "
              f"= Rs {r['total_spent']:>8,.0f} total  (dates: {', '.join(r['dates'])})")

    print("\n--- Possible Duplicate / Repeated Charges (within 2 days) ---")
    duplicates = find_duplicate_payments(transactions)
    if not duplicates:
        print("None found.")
    for d in duplicates:
        print(f"  {d['description']:<25} Rs {d['amount']:>8,.0f}  on {d['date_1']} and {d['date_2']} "
              f"({d['days_apart']} day(s) apart)")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
