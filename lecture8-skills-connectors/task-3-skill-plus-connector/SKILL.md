# Skill: Client Brief → Dev Task Breakdown
# (Same SKILL.md as task-1-my-skill/SKILL.md — copied here to show it is self-contained)

## Name
client-dev-breakdown

## Description
Use this skill whenever a client or someone else gives a rough description of a website, web app,
mobile app, WordPress site, Shopify store, or any custom software project — and the user needs it
turned into a clear, structured development task list. Trigger phrases include: "break this down",
"make a task list", "what do I need to build", "scope this project", "client wants", "new project
brief", "estimate tasks for", "plan this project", or any message that contains a rough client
requirement or project idea. This skill is especially useful for freelance developers who receive
vague client requests and need to clarify and structure them before estimating or starting work.

## Instructions

When this skill fires, follow these steps in order:

### Step 1 — Identify the Project Type
Detect which type of project is being described and label it clearly at the top:
- Web Application (Next.js / React / Node.js)
- Mobile Application (Flutter / React Native)
- WordPress Website or Plugin
- Shopify Store or Custom Theme
- Custom Web Development (HTML/CSS/JS)
- API / Backend Only
- Mixed / Full-Stack

### Step 2 — Extract the Core Requirements
Read the client brief carefully and pull out:
- The main purpose of the project (one sentence)
- Key features mentioned (even vaguely)
- Any tech stack preferences the client mentioned (or note "not specified")
- Any deadline or budget hints (or note "not mentioned")

### Step 3 — Build the Structured Task Breakdown
Group all tasks into these fixed categories. Only include a category if it actually applies.
Use this exact format:

---
## Project: [Project Name or short description]
**Type:** [Project Type from Step 1]
**Core Purpose:** [One sentence]

### 🎨 Frontend / UI Tasks
- [ ] Task name — brief explanation

### ⚙️ Backend / API Tasks
- [ ] Task name — brief explanation

### 🗄️ Database Tasks
- [ ] Task name — brief explanation

### 🔌 Integrations & Third-Party
- [ ] Task name — brief explanation

### 🔐 Auth & Security
- [ ] Task name — brief explanation

### 🚀 Deployment & Hosting
- [ ] Task name — brief explanation

### 🧪 Testing & QA
- [ ] Task name — brief explanation

**Complexity estimate:** Low / Medium / High (one word with one-line reason)

---

### Step 4 — Flag Missing Information

### ❓ Questions to Ask Client Before Starting
List 3–6 specific questions whose answers would change the task list or the estimate.

### Step 5 — Tone and Format Rules
- Always use checkbox list format (`- [ ]`) for tasks.
- Never invent features the client did not hint at — mark assumptions with "(assumed)".
- If the brief is under 2 sentences, add: "⚠️ Brief is very short — verify with client."
- Always end with the "Questions to Ask Client" section.
