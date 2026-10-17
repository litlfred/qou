---
# qou-b5yi
title: 'ROUTE 2: settle the crossing-number minimisation crux (qou-a9li) — decide whether the Freedman-He asymptotic crossing number for a Borromean PAIR is (a) unconstrained, giving inf = 0 since the pair is an unlink, hence the route is DEAD, or (b) constrained to the complement of the third component, where Brunnian-ness holds it up and the computed ACN=1.643 is a genuine upper bound on a positive quantity. This is a definitional question about Freedman-He''s construction, answerable from the Khesin exposition + the corpus''s own Brunnian machinery, and it decides whether qou-0hdx stays open'
status: completed
type: task
priority: normal
created_at: 2026-08-01T21:33:59Z
updated_at: 2026-09-02T21:41:57Z
---

## BODY BACKFILLED 2026-09-02 — this bean was `completed` with no body for a month

Same defect and same answer as its sibling `qou-a9li`: closed 2026-08-01T21:47:37Z
with the conclusion written nowhere.

**The definitional question is answered, and the framing it inherits is wrong.**

Option (a) *(unconstrained, pair is an unlink, inf = 0, route DEAD)* and option (b)
*(constrained to the complement of the third component, so `ACN = 1.643` is a genuine
upper bound on a positive quantity)* both presuppose a **pair** minimisation. Verified
against `library/arxiv-0808.1533v1/sections/sec-002-energy-bound.md:203-216`
(Komendarczyk eq. 43): the object in the Freedman–He link bound is `ac(L_k, L)`,
per-component against the whole link, summed over components. There is no pair index
in either source.

Answering the question behind the framing: the complement constraint is **real** —
eq. (43) bounds `ac(L_k, L)` below by a smallest genus of a surface in
`R^3 \ {other components}` — so Brunnian-ness does hold the value up, which is the
substance of (b). But it does so for a single-component genus, so `1.643` is not the
quantity it bounds. Correctly indexed: `1 <= ac(L_k, L) <= 3.285` per component.

This bean's closing line — *"and it decides whether qou-0hdx stays open"* — is now
decided: `qou-0hdx` is **scrapped** (2026-09-02), on two verified corrections rather
than on this one. Its body carries the full record.
