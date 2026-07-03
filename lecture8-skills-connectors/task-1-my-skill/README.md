# Task 1 — My Daily-Life Skill: Client Brief → Dev Task Breakdown

## The Problem It Solves
As a freelance web/mobile developer, I receive client requirements in messy, incomplete
sentences every week. Before I can estimate time or start building, I need to convert those vague
descriptions into a structured task list I can paste into GitHub Issues, Notion, or Trello.

Normally I do this manually every time, inconsistently. This skill makes the AI do it my exact
way every time, automatically, just from a normal message.

## Why I Chose This
This is genuinely something I do for every project — WordPress sites, Shopify stores, Next.js
apps, Flutter apps. The output format I designed (grouped by Frontend/Backend/DB/Integrations etc.
with checkboxes and a "Questions to Ask Client" section) directly matches how I manage my real
freelance projects.

## AI Tool Used
Claude (Anthropic)

## Initial Prompt to Build the Skill
> "I am a freelance web developer. I build Next.js apps, mobile apps, WordPress sites, Shopify
> stores, and custom web projects. Build me a skill that takes a messy client project description
> and turns it into a structured development task list grouped by Frontend, Backend, Database,
> Integrations, Auth, Deployment, and Testing — with checkboxes I can paste into GitHub or
> Trello. Always end with 3-6 questions I should ask the client before starting."

## Refined Prompt (after first version)
> "Also: detect the project type automatically (Next.js/WordPress/Shopify etc.), add a
> one-line complexity estimate, flag any assumptions I am making that the client didn't specify,
> and add a warning if the brief is too short to work from."

## How I Verified It
I tested the skill with a realistic client brief (see `sample-output.md`): an online clothing
store with JazzCash/Easypaisa payments. I confirmed:
- The skill triggered automatically without me naming it
- All task categories matched my real project structure
- The "Questions to Ask Client" section flagged the JazzCash merchant account issue — a real
  blocker I have encountered on actual projects — confirming the output is genuinely useful

## Files
- `SKILL.md` — the skill itself
- `sample-output.md` — test input and verified output
- `prompts.md` — all prompts used to build and refine the skill
