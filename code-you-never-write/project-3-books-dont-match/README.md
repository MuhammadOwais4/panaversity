# Project 3 — The Books Don't Match

## Problem
I hand-counted a known total for a group trip fund (9 people × Rs 5,000 = Rs 45,000), but the
digital payment app's transaction memos are messy and ambiguous (nicknames, partial payments,
no consistent format). I needed to find exactly who is short and by how much.

## AI Tool Used
Claude (Anthropic)

## Initial Prompt
> "I expect Rs 45,000 total from 9 people at Rs 5,000 each. Here is the messy payment export with
> inconsistent sender notes. Write a script to total it up and tell me the gap."

## Improved Prompt
> "The sender notes don't match real names directly — let me give you a manual mapping (e.g. 'Ali
> bhai trip' = Ali Raza) and have the script use that mapping to group payments by actual person,
> then flag who's short and who overpaid."

## How I Verified
I knew up front, from manually counting who confirmed coming, that **9 people** were expected to
pay **Rs 5,000 each = Rs 45,000 total** — this was my known fact. The script's "Expected total"
correctly echoed Rs 45,000 (since I fed it directly), and I independently summed the raw CSV
(`digital_payments.csv`) amounts by hand: 5000+5000+3000+5000+5000+2000+5000+5000+2000+5000 =
**Rs 42,000**, which matched the script's "Total received" output exactly.

## Result
- Gap: **Rs 3,000** between expected and received.
- **Usman and Hina have not paid at all** (Rs 5,000 each still owed).
- **Sara Ahmed overpaid by Rs 2,000** (sent in two installments adding up to Rs 7,000).
- Everyone else (Ali Raza, Bilal, Hassan, Fawad, Asad Khan, Zainab) is fully paid.

## What Worked / What Didn't
- Worked: keeping the name-mapping rules in a separate JSON file made it easy to update without
  touching the script, and made the "personal knowledge" part of the process explicit and auditable.
- Didn't work initially: first version assumed memo text would always exactly match a name, so any
  slightly different memo silently vanished into the total without being attributed to anyone. Fixed
  by adding an "Unmapped Payments" section that loudly flags any memo with no matching rule.

## Files
- `reconcile.py` — the script
- `digital_payments.csv` — sample messy payment export (dummy data)
- `reconciliation_rules.json` — known total + my personal name-mapping rules
