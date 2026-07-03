# Task 3 — Skill + Connector: One Sentence, Live Data, Formatted Result

## The Workflow
Combined the Task 1 skill (Client Brief → Dev Task Breakdown) with the Task 2 Gmail connector
to create a single workflow: one natural sentence pulls a real client email and immediately
formats it into a structured task list, with no manual copy-pasting at any step.

## The Single Sentence I Used
> "Check my Gmail for the most recent client project email and break it down into a dev task list."

## What Happened Step by Step
1. The Gmail **Connector** fetched the most recent client project email automatically.
2. The email content (a Shopify customization request) was fed directly into the workflow.
3. The **Skill** (`client-dev-breakdown`) triggered automatically on the fetched content.
4. The formatted task breakdown was produced — Frontend/Backend/etc. categories, checkboxes,
   complexity estimate, and questions to ask the client — all in one response.

No copying, no pasting, no manually typing the client's requirements.

## The Output Produced (summary)
The combined workflow produced a task breakdown for the Shopify customization project including:
- Frontend tasks: custom product filter UI, modified checkout layout
- Backend/API tasks: filter logic, Shopify storefront API calls
- Integrations: Shopify API
- Complexity: Medium
- Questions: asked about Shopify plan tier, whether client has theme source access, and deadline

## How I Verified
I spot-checked one part of the result against the original email: the client's specific mention
of "filter by fabric type and occasion" — I confirmed this appeared correctly as a checkbox task
in the Frontend section. The "Questions to Ask Client" section also correctly flagged that no
deadline had been given, which matched the email.

## What Worked / What Didn't
- Worked: the skill fired without me naming it — the fetched email content alone was enough to
  trigger the "client wants" detection in the skill description.
- Initially the connector returned the full raw email including headers and quoted reply threads,
  which confused the skill into listing email formatting artifacts as tasks. Fixed by adding
  "ignore email headers and quoted reply threads" to the skill's Step 2 instructions.

## Files
- `SKILL.md` — the skill used in this workflow (same as Task 1)
- `prompts.md` — the prompts used
