---
# qou-5r17
title: 'Corpus audit: where does the paper say ''derived'' about something axiomatised?'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:23:28Z
updated_at: 2026-08-15T00:45:18Z
---


## Why

Landed after a retraction (#5044). The Ch9 §1 intro said the pairwise result was
"forced by the braiding rather than assumed" when the hexagon is a CLASS FIELD of
Mathlib's `BraidedCategory` — an axiom. The claim survived a one-voice pass, a
render-QA pass, a written PR Verification section, and Copilot. The author caught
it with a five-word question.

The house style guide (`one-voice-style-guide.md` §Sentence patterns) lists
**"Not assumed; derived"** as a sanctioned idiom. That makes the phrase available
corpus-wide to attach to claims that have not earned it, which is exactly the
failure mode that just occurred once.

## Scope — this is NOT a grep

Every hit has to be checked against what actually discharges the claim:
is the thing said to be "derived" (a) proved from stated axioms, (b) a
rearrangement of an axiom, (c) an axiom itself, or (d) conditional on a
class-axiomatised conjecture? Only (a) earns the word. Start from
`grep -rn "derived\|not assumed\|forced by" content/` and expect most hits to
be legitimate.

## Known instance already fixed
`interactions-are-pairwise-intro.md` — fixed in #5044. Do not re-report.
