# Project 4 — Organize the Mess (The Files You Forgot)

## Problem
My folders accumulate duplicate files, forgotten downloads, and screenshots saved in multiple
places. This involves real file operations, so the priority was **safety**: never let the script
touch or delete an original file without an approved, reviewed plan first.

## AI Tool Used
Claude (Anthropic)

## Initial Prompt
> "Write a script that scans a folder, finds duplicate files (by content, not just filename), flags
> large files, and groups files by type — but show me a full plan of every action first and wait for
> my approval before changing anything."

## Improved Prompt
> "Make sure the execute step only ever copies files into a new output folder, never deletes or
> overwrites anything in the original folder, and require me to literally type YES to confirm."

## Safety Steps Followed
1. **Copy first.** Worked entirely on a sample folder (`sample_messy_folder/`), never the real
   Downloads/Documents folder, until the script earned trust.
2. **Wrote the brief.** "Clean" = find exact duplicate files by content hash, flag files ≥ 50 KB
   (threshold lowered for this demo; in real use I'd set 100MB+), group remaining files by extension.
3. **Demanded a dry run.** `python organize_mess.py --scan sample_messy_folder` prints the full
   plan and saves it to `plan.json` — **zero files are touched** in this mode.
4. **Reviewed the plan** printed to the screen before running execute.
5. **Approved and executed.** `--execute` re-prints the same plan and requires typing `YES` before
   copying anything — and it only ever **copies into a new `organized_output/` folder**, never
   deletes or modifies the source.
6. **Verified and kept.** Confirmed `sample_messy_folder` was byte-for-byte unchanged after running.

## How I Verified
I deliberately created **exactly 2 duplicate files** in the sample folder (`report_copy.pdf` as a
copy of `report.pdf`, and `IMG_001_copy.jpg` as a copy of `IMG_001.jpg`) — a known fact since I
made them myself. The script's "Duplicates found" section reported **exactly 2 duplicate files**,
matching. I also created one file padded to exactly 200 KB (`bigfile.zip`); the script's "Large
files flagged" section reported it as **200.0 KB**, matching the known size exactly. After running
`--execute`, I ran `ls` on the original folder and confirmed all 8 original files were still present
and unchanged — none were deleted, renamed, or modified.

## Result
- Found 2 duplicate files (saving redundant storage).
- Flagged 1 large file (200 KB) for review.
- Organized 6 unique files into type-based folders (pdf/, png/, jpg/, zip/, txt/) inside a brand
  new `organized_output/` folder — originals untouched the entire time.

## What Worked / What Didn't
- Worked: content-hash-based duplicate detection (SHA-256) correctly ignored filename differences
  and caught true duplicates, not just same-named files.
- Didn't work initially: first draft of the script deleted duplicates directly from the original
  folder. I explicitly asked the AI to change this to copy-only with a typed confirmation gate
  before trusting it on anything beyond the sample folder.

## Files
- `organize_mess.py` — the script (scan / execute modes)
- `sample_messy_folder/` — sample messy folder with intentional duplicates (dummy data, not real files)
