---
# qou-h7w4
title: 'CORRECTION: the 2026-08-30 Stokes audit imports Yekutieli''s 1-dim bad-set statement (singular points of the map sigma, :2280) into the 2-dim case, where the kite map is linear by definition and the bad set is the singular locus of the connection FORMS (Def 4.4.12); a_1 is a length not a count; smooth forms give no bad set at all'
status: completed
type: task
priority: normal
created_at: 2026-09-06T10:11:57Z
updated_at: 2026-09-06T10:25:01Z
---

## Resolved 2026-09-06 on PR #6936 — dated correction blocks added to §2 and §3 of the 08-30 audit

The audit's §2 quoted Yekutieli's `|bad(k)| <= m`, m = singular points of sigma — the 1-DIM string
case (held text :2280) — as the 2-dim statement. In 2-dim: the kite map is linear by definition
(Def 4.1.1, :3278); an index is good iff the connection FORMS alpha|Z_i, beta|Z_i are smooth
(Def 4.4.12, :3964); a_0 := 2m for m segments covering the forms' singular locus and
a_1 := 2*sum len(Z_j), a LENGTH (Lemma 4.4.13 proof, :3969-3976). Consequences recorded in both
blocks: the bad set is the connection's singular locus, not the surface map's; a_1 is not a count;
smooth forms give no surface term at all; the corpus has no (alpha, beta) as forms (qou-20bk); the
§3 "checkable against the N=Z chain" prediction is conditional on H1 of
QOU/Mass/StokesSingularCountAffine.lean. The original text is left in place as the record of the
reading corrected, per the repo's practice for dated audits. The same misreading in my own #6929
HyperbolicSurfaceLaw header is corrected on the same PR.

Not changed: the audit's §0/§1 (what is held), §4 (the purged per-cell lambda_Y gate) and §5
(open items) — none of them depends on the map-vs-forms reading.
