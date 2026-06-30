# Prompts Used — Project 3: The Books Don't Match

## Prompt 1 (initial)
I expect Rs 45,000 total from 9 people at Rs 5,000 each. Here is the messy payment export with
inconsistent sender notes. Write a Python script to total it up and tell me the gap between what
I expect and what was actually received.

## Prompt 2 (refinement)
The sender notes don't match real names directly — let me give you a manual mapping (e.g. 'Ali
bhai trip' = Ali Raza) in a separate JSON rules file, and have the script use that mapping to
group payments by actual person, then flag who's short and who overpaid.

## Prompt 3 (fix)
What happens if a memo doesn't match any rule in my mapping? Right now it looks like it just gets
silently dropped from the totals. Add a section that explicitly lists any unmapped payments so I
never lose track of money.
