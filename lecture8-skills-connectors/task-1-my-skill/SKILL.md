# Skill: Client Brief → Dev Task Breakdown

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
- [ ] Task name — brief explanation (e.g. payment gateway, email service, maps)

### 🔐 Auth & Security
- [ ] Task name — brief explanation

### 🚀 Deployment & Hosting
- [ ] Task name — brief explanation

### 🧪 Testing & QA
- [ ] Task name — brief explanation

**Complexity estimate:** Low / Medium / High (one word with one-line reason)

---

### Step 4 — Flag Missing Information
After the task list, add a section called:

### ❓ Questions to Ask Client Before Starting
List 3–6 specific questions whose answers would change the task list or the estimate. Make them
concrete, not generic. Example: "Do you need the admin panel in English only, or also in Urdu?"
not just "What languages do you need?"

### Step 5 — Tone and Format Rules
- Always use the checkbox list format (`- [ ]`) for tasks so they can be copy-pasted into GitHub Issues, Notion, or Trello immediately.
- Keep task names short (under 10 words) but the explanation can be one sentence.
- Never invent features the client did not hint at — mark assumptions clearly with "(assumed)".
- If the brief is extremely short (under 2 sentences), add a note at the top: "⚠️ Brief is very short — task list based on typical projects of this type. Verify with client before using."
- Always end with the "Questions to Ask Client" section — never skip it.
