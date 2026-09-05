---
# qou-glji
title: Does the surface exponent in B/A = a - b*A^(-p) measure the coordination graph's dimension, and what does the AME chart say about the production chain's p = 1?
status: completed
type: task
priority: normal
created_at: 2026-09-05T07:44:21Z
updated_at: 2026-09-05T08:10:01Z
---

## Resolved 2026-09-05 — chain REJECTED, inverse-dimension reading NOT established

Lean `QOU/Mass/SurfaceExponentIsDimension.lean` (sorry-free, 7 decls axiom-clean) + probe
`computations/probes/surface_exponent_is_dimension_probe.py` (19/19). Audit:
`docs/audits/2026-09-05-surface-exponent-is-dimension.md`.

**Positive, robust.** The production braid word's coordination graph is the path P_A (two
endpoints of bond-degree 1, interior degree 2, A_surf = 2 constant), so it is the p = 1 member of
`a - b*A^(-p)`. Profiling p against 2548 AME nuclides with Coulomb/asymmetry/pairing carried
separately: RSS(1) = 147.0 against RSS(p*) = 38.2, p = 1 outside the 1 %-RSS interval, and no
analysis variant's p* exceeds 0.583. **The production chain cannot supply the surface term**, and
the obstruction is dimensional, not a matter of tuning eps, k or k'.

**Negative against my own reading, and it is the finding worth carrying.** A pre-registered
expectation that the analysis variants would agree FAILED. All five constrain p (1 %-RSS widths
0.062 .. 0.134) and they disagree anyway: p* = 0.364 (d = 2.75) on all nuclides against 0.582
(d = 1.72) at A >= 40, with **disjoint** intervals [0.331, 0.397] vs [0.542, 0.624]. So no single
power-law exponent describes the whole chart. Genericity by qou-rav3's method: 17.66 % of the
window [0, 2], against 67.9 % for qou-kqdn's ratio and 73.7 % for qou-rav3's k — far less generic,
but not a clean one-number measurement. **Do not quote d = 2.75 as a measured dimension.**

**Scoping owed to prior work (path 0 was unavailable — grep-open, not graph-open).** The chain's
A^(-1) SCALING is a corpus fact predating this:
`QOU.MassTheory.ChainBindingNoSaturationPeak.chainPerNucleon_eq_hyperbola` proves B/A = c1 + c2/A
by `ring`. New here is the derivation from the boundary DEGREE; the corpus carries the same deficit
only as a bond count. `QOU.Mass.AffineCountIsNotASurfaceTerm` reaches the same exclusion for affine
counts by an independent scope-(b) route, and A-1 is affine. Bean qou-7e67's "not dimension"
negative is on the RADIUS exponent over A <= 4 and does not transfer.

**Sharpest objection, met in the Lean:** the corpus's only derived 3-D coordination object is the
deltahedron contact graph with E = 3A - 6 — still affine, so also A^(-1). A convex deltahedron is
d = 3 with every nucleon on the boundary, i.e. no bulk, which is exactly where A_surf ~ c*A^((d-1)/d)
fails.

## Next (my judgement, overrule freely)

Avenue 2 is sharpened differently from #6761. It asked "what fixes 1 - k'/k?"; the prior question is
now **"what edge set has a bulk at all?"** — both derived candidates on main (A-1 and 3A-6) are
affine and both give A^(-1), and an affine count can never be a surface term. Deciding whether the
substrate emits any non-affine coordination object is decidable by a proved invariant rather than by
a fit, and a negative would close Avenue 2 outright.
