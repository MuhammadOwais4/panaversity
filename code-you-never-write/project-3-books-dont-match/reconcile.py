"""
The Books Don't Match — reconciles a known hand-counted total against a messy
digital payment record, using personal name-mapping rules to resolve ambiguous memos.

Usage: python reconcile.py digital_payments.csv reconciliation_rules.json
"""

import csv
import json
import sys
from collections import defaultdict


def load_payments(path):
    payments = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            payments.append(row)
    return payments


def main():
    if len(sys.argv) < 3:
        print("Usage: python reconcile.py <payments.csv> <rules.json>")
        sys.exit(1)

    payments = load_payments(sys.argv[1])
    with open(sys.argv[2], encoding="utf-8") as f:
        rules = json.load(f)

    expected_total = rules["expected_total"]
    amount_per_person = rules["amount_per_person"]
    members = rules["members_who_should_pay"]
    mapping = rules["name_mapping_rules"]

    by_person = defaultdict(float)
    unmapped = []

    for p in payments:
        note = p["sender_note"]
        person = mapping.get(note)
        if person is None:
            unmapped.append(p)
            continue
        by_person[person] += p["amount"]

    total_received = sum(p["amount"] for p in payments)

    print("=" * 60)
    print("RECONCILIATION REPORT")
    print("=" * 60)
    print(f"\nExpected total (hand-counted): Rs {expected_total:,.0f}")
    print(f"Total received (all digital payments): Rs {total_received:,.0f}")
    print(f"Gap: Rs {expected_total - total_received:,.0f}")

    print("\n--- Per-Person Breakdown ---")
    shortfalls = []
    overpayments = []
    not_paid = []

    for member in members:
        paid = by_person.get(member, 0.0)
        diff = paid - amount_per_person
        status = "OK"
        if diff < 0:
            status = f"SHORT by Rs {abs(diff):,.0f}"
            shortfalls.append((member, abs(diff)))
            if paid == 0:
                not_paid.append(member)
        elif diff > 0:
            status = f"OVERPAID by Rs {diff:,.0f}"
            overpayments.append((member, diff))
        print(f"  {member:<35} paid Rs {paid:>7,.0f}  -> {status}")

    if unmapped:
        print("\n--- Unmapped Payments (no rule matched this memo) ---")
        for p in unmapped:
            print(f"  {p['date']}  '{p['sender_note']}'  Rs {p['amount']:,.0f}  <-- needs a name mapping rule")

    print("\n--- Follow-up Needed ---")
    if not_paid:
        print(f"  Has not paid at all: {', '.join(not_paid)}")
    if shortfalls:
        for name, amt in shortfalls:
            if name not in not_paid:
                print(f"  {name} still owes Rs {amt:,.0f}")
    if overpayments:
        for name, amt in overpayments:
            print(f"  {name} overpaid by Rs {amt:,.0f} (refund or carry forward)")
    if not shortfalls and not overpayments:
        print("  None — books match exactly.")

    print("=" * 60)


if __name__ == "__main__":
    main()
