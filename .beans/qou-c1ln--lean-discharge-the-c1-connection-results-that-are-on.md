---
# qou-c1ln
title: 'LEAN: discharge the C1 connection results that are only numerical'
status: todo
type: task
priority: high
created_at: 2026-08-07T22:20:00Z
updated_at: 2026-08-07T22:20:00Z
---

Everything load-bearing in the C1 connection arc (bean `qou-wgnx`) rests on
**numerics**, not derivation. The Lean that exists covers only the easy
algebraic layer. This bean tracks closing that gap, in dependency order.

| # | claim | today | needs |
|---|---|---|---|
| 1 | `qThetaC` holomorphic on `ℂ*` | not proved | **entry point found**: `TendstoLocallyUniformlyOn.differentiableOn` (`Mathlib.Analysis.Complex.LocallyUniformLimit`) + Weierstrass M-test on compact annuli, reusing the completed-square bound from `summable_qThetaTerm`. **No new literature needed.** |
| 2 | Jacobi triple product ⇒ **exact** zero locus (converse of `qTheta_neg_zpow_eq_zero`) | ⊇ only | `tprod` ✓ in Mathlib; the Liouville step needs elliptic theory on `ℂ*/p^ℤ` — **absent**. Wants a formalisation-friendly JTP proof (Gasper–Rahman §1.6, Andrews–Askey–Roy ch.10). |
| 3 | 0-side series radius 1; ∞-side entire | not proved | recursion bounds; feasible, tedious |
| 4 | `Y₀`, `Y_∞`, inverse, meromorphy; `P(pz)=P(z)` | not proved | matrix-valued meromorphic functions; `Analysis/Meromorphic/*` partial |
| 5 | pole divisor + completeness (residue thm) | numerical | **argument principle — absent from Mathlib** |
| 6 | `χ` = the closed form, `α = t₂/T`, order 2 | numerical (12 pts, `5.3e-63`) | all of 1–5 |

**Confirmed absent** in Mathlib: `DifferentiableOn.tsum`,
`differentiableOn_tsum_of_summable_norm`, the argument principle, elliptic
function theory on the multiplicative torus.

**Start with #1** — self-contained, needs nothing new, and makes the *pole
locations* fully derived rather than ⊇-only.

Blocks/relates: `qou-wgnx`.
