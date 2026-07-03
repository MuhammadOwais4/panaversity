# Task 4 — Make It Portable: Skill Works in a Fresh Chat

## Path Chosen
**Make it portable** — loaded the SKILL.md into a completely fresh Claude chat with zero prior
context and confirmed the skill triggered automatically from a plain-English request.

## What I Did
1. Opened a brand new Claude conversation (no history, no prior setup).
2. Pasted only the contents of `SKILL.md` at the start of the chat as the skill definition.
3. Without saying "use my skill" or naming the skill at all, I typed a new client brief:

> "A friend's restaurant wants a simple website — menu page, online reservation form,
> gallery of photos, Google Maps location, and a WhatsApp button. Budget is small."

4. The skill fired automatically and produced the full task breakdown in the correct format.

## Why This Proves Portability
The skill is just a text file (`SKILL.md`). It contains no code, no platform-specific setup,
no API keys. It can be:
- Pasted into any new Claude chat
- Loaded into Claude Projects (as a custom instruction)
- Shared with another developer who can use it identically
- Loaded into Claude Code or Cowork the same way

## Output in Fresh Chat (summary)
The skill correctly identified project type as "Custom Web Development (HTML/CSS/JS) or
WordPress" (since no tech stack was specified), listed tasks across Frontend, Integrations
(Google Maps embed, WhatsApp link), and Deployment, and asked the right questions including
whether the client wanted to edit content themselves (pointing toward WordPress).

## What Worked / What Didn't
- Worked: the skill text alone, with no extra context, was enough for the AI to follow the
  format exactly — checkboxes, categories, complexity estimate, questions to ask.
- One note: in a fresh chat with no system prompt, I had to paste the SKILL.md content
  manually at the start. In Claude Projects, this would happen automatically — the Skill is
  always active without pasting.

## Portability Checklist
- [x] Works in a fresh chat with no prior history
- [x] Triggers from natural language, not a command
- [x] Produces identical format to the original chat
- [x] No code, no credentials, no platform-specific setup needed
- [x] Can be shared as a plain text file

## Files
- `prompts.md` — the prompts used in the portability test
