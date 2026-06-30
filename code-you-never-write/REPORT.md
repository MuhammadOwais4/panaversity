# Final Report — Code You Never Write (Lecture 7)

**Student:** Muhammad Owais
**GitHub:** MuhammadOwais4
**AI Tools Used:** Claude (Anthropic)

---

## Project 1 — Money Detective

**Problem:** Find spending leaks (forgotten subscriptions, duplicates) in transaction history.

**AI Tool:** Claude

**Initial Prompt:** "Here is my transaction history as a CSV (date, description, amount). Write a
Python script that finds recurring charges, possible forgotten subscriptions, and duplicate or
repeated payments within a couple of days of each other."

**Improved Prompt:** Added request to calculate total spend/income and sort recurring charges by
total amount.

**Verification:** Hand-summed all negative amounts in the CSV = Rs 61,850. Script output matched
exactly.

**What worked/didn't:** Grouping by (description, amount) worked well. Had to refine because plain
grocery repeats were flagged the same as real subscriptions — sorting by total spend fixed the
visual confusion.

**Result:** Found 9 recurring charges; flagged two overlapping streaming subscriptions
(Netflix + Disney+ = Rs 6,900/month combined) as a candidate to cancel one.

---

## Project 2 — What's My Grade, Really

**Problem:** Calculate true current grade using my teacher's exact policy (weights, dropped
lowest quiz score) and find the score needed on the final to hit a target grade.

**AI Tool:** Claude

**Initial Prompt:** "Here are my scores by category and my teacher's grading policy... Write a
script to calculate my current grade."

**Improved Prompt:** Added target-grade solver for the final exam.

**Verification:** Hand-calculated quizzes average (dropping lowest score of 60) = 85.0, matched
script exactly. Hand-verified the weighted sum (48.45) and needed final score (78.9) — matched.

**What worked/didn't:** "Drop lowest" logic via sort-and-slice was simple and verifiable. Had to
fix an early bug where the in-progress grade was normalized against the full 100% weight
including the not-yet-graded final, making it look artificially low.

**Result:** Current grade 80.75 across completed categories; need 78.9 on the final to hit a
target of 80.

---

## Project 3 — The Books Don't Match

**Problem:** Reconcile a hand-counted trip fund total (Rs 45,000 from 9 people) against a messy
digital payment export with ambiguous memos.

**AI Tool:** Claude

**Initial Prompt:** "I expect Rs 45,000 total from 9 people... Write a script to total it up and
tell me the gap."

**Improved Prompt:** Added a separate name-mapping rules file to resolve ambiguous memos into
real names.

**Verification:** Known fact: 9 confirmed people × Rs 5,000 = Rs 45,000 expected. Hand-summed the
raw CSV = Rs 42,000, matched script's "Total received" output exactly.

**What worked/didn't:** Keeping name-mapping rules in a separate JSON file made the personal
knowledge explicit and easy to audit. Had to add an "unmapped payments" warning after noticing
memos with no matching rule were silently disappearing from totals.

**Result:** Rs 3,000 gap found. Usman and Hina haven't paid at all (Rs 5,000 each owed); Sara
Ahmed overpaid by Rs 2,000.

---

## Project 4 — Organize the Mess

**Problem:** Find duplicate and large files in a messy folder safely, without risking real files.

**AI Tool:** Claude

**Initial Prompt:** "Write a script that scans a folder, finds duplicate files by content, flags
large files, and groups by type — but show me a full plan first and wait for approval."

**Improved Prompt:** Required execute mode to only ever copy (never delete/overwrite originals)
and require typing YES to confirm.

**Verification:** Deliberately created exactly 2 duplicate files and one file padded to exactly
200 KB. Script's "Duplicates found" reported exactly 2; "Large files flagged" reported exactly
200.0 KB — both matched known facts. Confirmed originals were byte-for-byte unchanged after
running --execute.

**What worked/didn't:** SHA-256 content hashing correctly distinguished true duplicates from
same-named-but-different files. First draft deleted duplicates directly from the source folder —
rewrote to copy-only with a typed confirmation gate before trusting it on real data.

**Result:** 2 duplicates found, 1 large file flagged, 6 unique files organized into type folders —
all in a new output folder with originals completely untouched.

---

## Overall Reflection

Across all four projects, the single most useful discipline was the **verification step**: in
every case, I had one number I already knew to be true (a hand-summed total, a manually
calculated category average, a known file count) and checked the AI-generated script's output
against it before trusting anything else it reported. In Project 4 specifically, the dry-run-first
workflow meant that even if the script had a bug, no real file would ever be at risk before I had
a chance to review the full plan.
