# Prompts Used — Task 1: Client Brief → Dev Task Breakdown Skill

## Prompt 1 (initial — to skill-creator)
I am a freelance web developer. I build Next.js apps, mobile apps, WordPress sites, Shopify
stores, and custom web projects. Build me a skill that takes a messy client project description
and turns it into a structured development task list grouped by Frontend, Backend, Database,
Integrations, Auth, Deployment, and Testing — with checkboxes I can paste into GitHub or Trello.
Always end with 3-6 questions I should ask the client before starting.

## Prompt 2 (refinement)
Also: detect the project type automatically (Next.js/WordPress/Shopify/Flutter etc.), add a
one-line complexity estimate, flag any assumptions I am making that the client didn't specify
with "(assumed)", and add a warning if the brief is too short to produce a reliable task list.

## Prompt 3 (trigger test — fresh chat, skill name NOT mentioned)
"Client wants an online clothing store, they want to list products, customers can add to cart and
checkout, payment via JazzCash and Easypaisa, admin can add/remove products, they also want an
order tracking page. Mobile-friendly. Budget and deadline not discussed yet."

## Prompt 4 (second trigger test — different phrasing)
"New project brief: WordPress site for a doctor's clinic, they need appointment booking, a blog,
contact form, and the doctor wants to add his own services from a dashboard."
