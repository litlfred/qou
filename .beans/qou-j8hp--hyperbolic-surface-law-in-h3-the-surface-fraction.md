---
# qou-j8hp
title: 'Hyperbolic surface law: in H^3 the surface fraction tends to a CONSTANT, so the framework''s own geometry predicts no A^(-1/3) term — formalize, test against AME, connect to the Stokes/kite surface'
status: completed
type: task
priority: normal
created_at: 2026-09-06T09:01:07Z
updated_at: 2026-09-06T09:27:40Z
---

## Resolved 2026-09-06 — the framework's own geometry fits BETTER than the Euclidean import, against a pre-registered expectation of worse

Lean `QOU/Mass/HyperbolicSurfaceLaw.lean` (14 decls, sorry-free, axiom-clean) + probe
`computations/probes/hyperbolic_surface_law_probe.py` (21/21). Audit:
`docs/audits/2026-09-06-hyperbolic-surface-law.md`.

**The fact (proved).** In H^3, S - 2V = 2 pi (e^(-2R) + 2R - 1) >= 0 by e^(-x) >= 1 - x alone, so
S/V >= 2 for every R. The surface fraction never vanishes: a hyperbolic-ball cluster fails HasBulk
under ANY radius assignment (hyperbolic_not_hasBulk), its "surface term" is a constant shift of the
volume coefficient, and the residual A-dependence is of order (ln A)/A. The volume is Bolyai's
formula and it is HELD (horvath2010 §3.1, library/arxiv-1010.5321v3); the area is its derivative
(hasDerivAt_hypVol), so nothing had to be ingested.

**The finding (measured, scope-(a)).** Pre-registered: (ln A)/A fits WORSE than A^(-1/3). It fits
BETTER — RSS 31.44 vs 38.53 (ratio 0.816), and beats the best pure power at any exponent (38.19).
Not generic: 0 of 9 alternative shapes beat the Euclidean import and (ln A)/A beats all 9; within
(ln A)^m/A^p at m = 1 the optimum is p* = 0.912, within 0.09 of the hyperbolic p = 1. Two cautions:
the exact ball's best v0 puts every nucleus at R < 2 (near-Euclidean) and the asymptotic SHAPE beats
the ball itself, so the data prefer the shape, not a literal ball; and a free (m, p) search keeps
improving with m, so the hyperbolic point is the best PREDICTED shape, not a global optimum.
**The surface coefficient stays free — nothing derives a_S.**

**Stokes / kites.** The surface of kites is the BULK of Yekutieli's estimate (the 4^k area count);
the surface term is the singular locus, one dimension down. Bridged to HasBulk as StokesSurfaceTerm;
affine_over_affine_not_surfaceTerm shows an affine singular count over an affine kite count tends to
a nonzero constant — the same volume-renormalisation the hyperbolic ball gives. The A-scaling of the
singular count is computed NOWHERE; opened as qou-yc1m.

**Literature.** Nothing needed. Optional: Martelli (arXiv:1610.02592, free) for a held area /
isoperimetry statement; Bezdek-Reid (arXiv:1210.5756) to make #6886's contact-number citations held.

## Next (my judgement, overrule freely)

qou-yc1m — compute the Stokes singular count's A-scaling on the spanning surface of the canonical
closure, starting from YekutieliTrefoilDiscretization.lean. The only route on the board whose
COEFFICIENT could be derived rather than fitted; both outcomes are useful.
