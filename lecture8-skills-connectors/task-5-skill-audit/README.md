# Task 5 — Audit a Skill Before Trusting It

## Skill Audited
**Skill name:** `web-search` skill (from the official Claude skills directory)

A skill that gives the AI the ability to search the web for current information and return
results with citations.

## Plain-English Explanation (what the skill does)
When this skill is active, any question that needs up-to-date information — news, prices,
recent events, current documentation — triggers a live web search. The AI searches, reads
the top results, and incorporates the findings into its answer with source links. Without
this skill, the AI only uses its training data, which has a knowledge cutoff. With it, the
AI can pull today's results.

## Sensitive Areas Checked

### Does it contact any external server?
**Yes — by design.** This is the entire purpose of the skill. Every search sends your query
to a search engine (Bing or a similar provider). You should assume every search query you
type while this skill is active is sent to an external server. This is not hidden or
unexpected — it is what the skill is for — but it means your queries are not private.

### Does it handle credentials or API keys?
**No.** The web search skill uses Claude's built-in search infrastructure. It does not ask
you to provide an API key, and you do not give it any credentials. Claude handles the
connection internally.

### Does it send your personal data anywhere unexpected?
**Partially.** The search query itself — whatever words you type — is sent externally. If
your question contains personal information (e.g. "find my doctor's address" or "search for
my company's financials"), those words leave the conversation. The skill does not read your
files, emails, or other connected apps and send those — it only sends what you type as a
search query.

### Can it modify anything?
**No.** This skill is read-only by nature. It searches and returns results; it does not post,
submit, purchase, or change anything on any website.

## Safety Verdict

**Safe to enable — with one condition.**

The web search skill is safe for general use. It does exactly what it says, it does not
access credentials or connected apps, and it cannot modify anything. The only thing to
be aware of: **search queries are sent to an external server**, so do not type sensitive
personal information (passwords, private addresses, confidential business data) as search
queries while this skill is active.

For my use case (searching for tech documentation, npm packages, WordPress plugin APIs,
Shopify developer docs), this skill is completely appropriate and useful. I would enable it.

## What I Learned from This Audit
The audit process revealed something I had not thought about before: the *query itself* is
the data that leaves the system, not just the "result". This is obvious in hindsight, but
auditing the skill made it explicit. Going forward I will treat any search query as
semi-public and avoid typing private business or personal details into search prompts.

## Prompts Used in the Audit

### Prompt 1
Explain in plain English exactly what the web-search skill does, step by step, as if you
were explaining it to someone who does not know how search engines work.

### Prompt 2
Does this skill contact any external server? What exactly gets sent outside this conversation?

### Prompt 3
Can this skill read my emails, files, or other connected apps? Can it modify or post anything
anywhere?

### Prompt 4
Based on everything you just told me, is this skill safe to enable? What is the one thing
someone should be careful about when using it?
