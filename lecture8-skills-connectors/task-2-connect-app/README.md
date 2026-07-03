# Task 2 — Connect One App, Read-Only: Gmail

## App Connected
**Gmail** (Google) — via Claude's built-in Google connector

## What I Did
1. Connected Gmail through Claude's connector settings (read-only OAuth permission)
2. Asked Claude: *"Find my most recent email thread that looks like a client project inquiry
   and give me a summary of what the client is asking for"*
3. Claude fetched the thread via the connector — no copy-pasting required
4. I confirmed the summary matched the actual email I could see in my Gmail inbox

## What the AI Fetched
Claude retrieved the most recent unread email thread from a contact asking about a Shopify
store customization project — the client wanted a custom product filter, a modified checkout
page, and asked about timeline and cost.

Claude's summary:
> "A client is inquiring about three Shopify customizations: (1) a custom product filter by
> fabric type and occasion, (2) modifications to the checkout page layout, and (3) asked for
> a timeline and rough cost estimate. No deadline was mentioned. The email was sent two days ago
> and has not been replied to yet."

## Verification
I opened the same thread in Gmail and confirmed the summary was accurate — all three requests
were present and the "no deadline mentioned" note was correct.

## Permission Granted (one sentence)
I granted Gmail read-only access — Claude can see and read my emails but cannot send, delete,
or modify anything — and I do not need write permission for this workflow since I only want
to read and summarize incoming client requests.

## Would I Ever Need Write Permission?
Potentially yes — if I wanted the AI to draft and send a reply automatically. But for this task
(reading and summarizing) read-only is exactly right. Write permission would be a larger trust
decision and should only be granted for a specific, limited purpose.

## Safety Note
No email content, sender names, or personal data are committed to this repository.
Screenshots have been taken with sender names and email addresses blurred.
