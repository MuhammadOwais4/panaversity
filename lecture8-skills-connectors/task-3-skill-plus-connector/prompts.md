# Prompts Used — Task 3: Skill + Connector Combined

## The Main Prompt (single sentence trigger)
Check my Gmail for the most recent client project email and break it down into a dev task list.

## Follow-up (verification)
In the task list you just made — did the client mention anything about a deadline or budget?
Show me exactly what the email said about that.

## Fix Prompt (after email headers caused noise)
The task list included some items that came from email headers and quoted reply text, not from
the actual client request. Update the skill instructions to ignore email headers, "On [date]
so-and-so wrote:" quoted sections, and email footers when extracting requirements.
