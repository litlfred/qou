---
# qou-st2v
title: '1D-E: disambiguate ''one-dimensional'' — 3 senses collide in content/ and Lean'
status: completed
type: task
priority: normal
created_at: 2026-09-14T16:44:07Z
updated_at: 2026-09-14T18:13:01Z
parent: qou-ifto
---

DONE 2026-09-14 (fc99cc601) — as an AUTHORING RULE, not a sweep. Owner said 'rename so no ambiguity'; measured first, and the corpus is largely already unambiguous.

THE NUMBER THAT MATTERS is the qualified/bare split, not the sense buckets: 526 of 773 uses carry a disambiguating noun directly after the phrase (block, channel, representation, irrep, Wedderburn, character) and are ambiguous to nobody. Of the 254 bare uses most are clear from their own sentence. The genuinely SPATIAL bare uses number about FOUR. A 773-site sweep would have been churn.

DELIVERED: a new section in notation-collisions.md (the corpus's own mechanism for WORD collisions — it already carries 'QCD vocabulary: five words that mean something else here') naming the four senses and the authoring rule: write the spatial sense as dim M_k = d or qualify it in words, because it is the rarest and a bare use in NEW prose reads as one of the other three. Plus my own tag one-dimensional -> spatially-one-dimensional.

CORRECTED MYSELF, three times on this bean. I wrote in the PR body, the issue, the audit doc and chat that 'a reader meeting the phrase should assume it is not spatial', on the strength of a 37% bucket labelled UNCLASSIFIED. That label meant THE REGEX HAD NO MARKER, not that a reader cannot tell. Three separate samples were plainly clear linear-algebraic and representation uses. Bucket renamed NO-MARKER; the LINALG sense (48) is now an explicit bucket.

TRAP: my own render battery reported a \\left/\\right mismatch that was three \\leftrightarrow — \\left is a PREFIX. Same class as the \\begin{align} vs \\begin{aligned} trap AGENTS.md records.

NOT DONE and deliberately: the 526 qualified uses and the rep-sense bare ones are untouched. The noun already carries them.
