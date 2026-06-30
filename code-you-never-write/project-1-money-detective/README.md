# Project 1 — Money Detective

## Problem
Find hidden spending leaks (forgotten subscriptions, duplicate charges, recurring costs) in real
transaction history — rules that are personal to me, which no generic budgeting app would catch.

## AI Tool Used
Claude (Anthropic)

## Initial Prompt
> "Here is my transaction history as a CSV (date, description, amount). Write a Python script that
> finds recurring charges, possible forgotten subscriptions, and duplicate or repeated payments
> within a couple of days of each other."

## Improved Prompt
> "Also calculate total spend and total income for the period, and sort recurring charges by total
> amount spent so the biggest leaks show up first."

## How I Verified
I manually summed all negative amounts in `sample_transactions.csv` by hand:
`-1500-4500-650-...-4500 = Rs 61,850`. The script's "Total spend this period" output matched
exactly: **Rs 61,850**. Since this known total matched, I trusted the rest of the script's logic
(recurring charge detection, duplicate detection).

## Result
- Total spend: Rs 61,850 | Total income: Rs 100,000
- Found **9 recurring charges**, the biggest being Grocery Store (Rs 9,000 total) and Gym
  Membership (Rs 6,000 total).
- Notably found **two streaming subscriptions running simultaneously** (Netflix + Disney+,
  Rs 4,500 + Rs 2,400 = Rs 6,900/month combined) — a candidate to cancel one.
- No exact duplicate billing (same charge within 2 days) was found in this sample period.

## What Worked / What Didn't
- Worked: grouping by (description, amount) cleanly caught all subscription-style charges.
- Didn't work initially: first version flagged *every* repeated grocery trip as "recurring" even
  though groceries aren't a subscription — improved prompt to sort by total spent so I could
  visually separate genuine subscriptions from normal repeat shopping.

## Files
- `money_detective.py` — the script
- `sample_transactions.csv` — sample data (dummy values; real bank data not committed)
