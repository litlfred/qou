---
# qou-qbs4
title: 'S3: extract the two Stokes multipliers U in C^2 for C1 (RSZ-wild core; gated on S1+S2)'
status: scrapped
type: task
priority: normal
created_at: 2026-08-08T08:05:00Z
updated_at: 2026-08-08T11:35:00Z
---

The residual proper. Sector-dependent q-Borel/Laplace summation of the ramified
series, then cohomological / Birkhoff-Guenther normal-form extraction of the two
multipliers `U in C^2` (RSZ §4-5, q-analog of Birkhoff-Malgrange-Sibuya).
`F(P1,P2) = Matr_{1,1}(C)^2 = C^2` since `r1 = r2 = 1`, `d = 2`.

**Deliverable:** the two multipliers, PLUS an independent cross-check -- the
theta/elliptic ratio structure is available via `QCharacter.ratio_qInvariant`
(ratio of same-multiplier q-characters is elliptic), which constrains the answer's
shape.

**ANTI-FIT (hard).** `U` must be DERIVED. Two constants tuned so a downstream
number lands is a fit, must be labelled one, and may NOT be wired as canonical.
The Q_beta `Phi_2` precedent -- the forbidden seventh ansatz -- applies directly.

**GATED on `qou-qbg2` (S1) + `qou-qbr3` (S2).** Genuinely multi-session; the
08-01 audit's own words: "not a session brick." Do not open this without S1
settled.

Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md` (stage S3).

## VOID 2026-08-08 — see docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md

The target `U in C^2` was derived from `F(P1,P2) = Mat_{1,1}(C)^2`, which does not
apply: C1 is pure isoclinic at infinity, and Thm 3.3.5 gives dimension 0 at k=1.
The work moves to ALIEN CALCULUS, which needs no slope filtration -- the corpus
already has that route (`OneInstantonNormalization.lean`, PR #4246). Re-open only
if a two-slope structure is exhibited somewhere it actually exists.
