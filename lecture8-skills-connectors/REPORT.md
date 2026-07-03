# Final Report — Skills & Connectors (Lecture 8)

**Student:** Muhammad Owais
**AI Tools Used:** Claude (Anthropic)
**Apps Connected:** Gmail (Google) — read-only

---

## Task 1 — My Daily-Life Skill: Client Brief → Dev Task Breakdown

**What it does:** Converts a messy client project description into a structured development task
list grouped by Frontend, Backend, Database, Integrations, Auth, Deployment, and Testing — with
GitHub/Trello-ready checkboxes, a complexity estimate, and a list of questions to ask the client.

**Why I chose it:** I am a freelance developer working on Next.js apps, mobile apps, WordPress
sites, and Shopify stores. Every new project starts with a vague client description. I do this
structuring manually and inconsistently every time. This skill makes the AI do it my exact way,
automatically, from a plain sentence.

**AI Tool:** Claude. Built using the skill-creator approach: described my task in plain English,
answered clarifying questions, let it generate the SKILL.md.

**Prompts used:**
- Initial: described my dev stack and output format requirements
- Refined: added project type auto-detection, "(assumed)" tagging, complexity estimate, and
  the short-brief warning

**Testing:** Typed a realistic client brief (online clothing store with JazzCash/Easypaisa
payments) without naming the skill. Skill fired automatically. Verified the output matched my
actual approach to structuring similar projects.

**What worked:** The trigger description in the SKILL.md was specific enough that phrases like
"client wants", "new project brief", and "break this down" all fired it reliably.

**What didn't:** First version did not flag assumptions, so if a client didn't mention auth
the AI either added a login system silently or skipped it. The "(assumed)" tag in the
instructions fixed this.

---

## Task 2 — Connect One App, Read-Only: Gmail

**What it does:** Connected Gmail via Claude's built-in Google connector and pulled a real
client email thread for summarization — no copy-pasting required.

**AI Tool + App:** Claude + Gmail (read-only OAuth)

**Prompts:** Asked Claude to find the most recent client project inquiry and summarize it.
Follow-up: checked if the email was unread and whether budget/deadline was mentioned.

**Verification:** Opened the same thread in Gmail and confirmed the summary was accurate — all
three client requests were present and the "no deadline" note matched.

**Permission granted:** Read-only access to Gmail — Claude can read emails but cannot send,
delete, or modify anything. Write permission not needed for this workflow.

---

## Task 3 — Skill + Connector: One Sentence, Live Data, Formatted Result

**What it does:** A single sentence ("Check my Gmail for the most recent client project email
and break it down into a dev task list") fetches live email data via the Gmail connector and
immediately formats it with the Task 1 skill — no manual steps.

**AI Tool + App:** Claude + Gmail connector + client-dev-breakdown skill

**The single sentence used:**
> "Check my Gmail for the most recent client project email and break it down into a dev task list."

**Verification:** Spot-checked one specific detail (client's "filter by fabric type and occasion"
phrasing) against the original email — it appeared correctly in the Frontend task list.

**Problem encountered:** The connector returned full raw email including headers and quoted
reply text. The skill initially treated "On 28 May, client@example.com wrote:" as a requirement.
Fixed by adding a note to the skill instructions to ignore email headers and quoted threads.

---

## Task 4 — Make It Portable

**What I did:** Opened a fresh Claude chat with zero history, pasted only the SKILL.md content,
and typed a new client brief (restaurant website) without naming the skill. The skill fired
automatically and produced the correct format identically to the original chat.

**Proof:** The skill is a plain text file with no code, no credentials, no platform-specific
setup. It works in any Claude chat, Claude Projects, Claude Code, or Cowork — anywhere you can
paste or load a text instruction. The format was identical across the original and fresh chats.

---

## Task 5 — Skill Audit: web-search skill

**Skill audited:** The built-in web-search skill (searches the web for current information).

**Plain-English explanation:** Sends search queries to an external search engine and returns
current results with citations. Gives the AI access to information beyond its training cutoff.

**Sensitive areas found:**
- Contacts external servers: Yes (search queries are sent out)
- Handles credentials: No
- Reads connected apps / files: No
- Can modify anything: No

**Safety verdict:** Safe to enable. The only caution is that search queries leave the
conversation — do not type sensitive personal or business information as search terms.
For my use case (searching tech docs, npm packages, Shopify/WordPress APIs) this is
perfectly appropriate.

**What I learned:** The *query itself* is what leaves the system, not just the result.
Auditing made this explicit in a way I had not consciously thought about before.

---

## Overall Reflection

The most valuable thing this assignment taught me was the **Skill as a reusable asset** idea.
Before this, every time I wanted the AI to help with a client project, I would re-explain my
format and preferences from scratch. Now I have a SKILL.md I can load into any chat and it
behaves consistently, in my format, every time. Combined with the Gmail connector, it means
I can go from "new client email arrives" to "structured task list ready" in one sentence.
The safety audit (Task 5) added the discipline of asking "what does this actually touch?" before
enabling any skill — a habit worth keeping.
