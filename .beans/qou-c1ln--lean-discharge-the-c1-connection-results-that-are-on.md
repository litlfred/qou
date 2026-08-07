---
# qou-c1ln
title: 'LEAN: discharge the C1 connection results that are only numerical'
status: in-progress
type: task
priority: high
created_at: 2026-08-07T22:20:00Z
updated_at: 2026-08-07T23:40:00Z
---

**Claimed** by session on branch `pr4672` → `claude/c1-theta-canonical-solutions-2026-08-07`.
Step 1 **done** (2026-08-07); steps 2–6 open.

Everything load-bearing in the C1 connection arc (bean `qou-wgnx`) rests on
**numerics**, not derivation. The Lean that exists covers only the easy
algebraic layer. This bean tracks closing that gap, in dependency order.

| # | claim | today | needs |
|---|---|---|---|
| 1 | `qThetaC` holomorphic on `ℂ*` | ✅ **PROVED** `differentiableOn_qThetaC` | done 2026-08-07 — see below |
| 2 | Jacobi triple product ⇒ **exact** zero locus (converse of `qTheta_neg_zpow_eq_zero`) | ⊇ only | `tprod` ✓ in Mathlib; the Liouville step needs elliptic theory on `ℂ*/p^ℤ` — **absent**. Wants a formalisation-friendly JTP proof (Gasper–Rahman §1.6, Andrews–Askey–Roy ch.10). |
| 3 | 0-side series radius 1; ∞-side entire | not proved | recursion bounds; feasible, tedious |
| 4 | `Y₀`, `Y_∞`, inverse, meromorphy; `P(pz)=P(z)` | not proved | matrix-valued meromorphic functions; `Analysis/Meromorphic/*` partial |
| 5 | pole divisor + completeness (residue thm) | numerical | **argument principle — absent from Mathlib** |
| 6 | `χ` = the closed form, `α = t₂/T`, order 2 | numerical (12 pts, `5.3e-63`) | all of 1–5 |

**Confirmed absent** in Mathlib: `DifferentiableOn.tsum`,
`differentiableOn_tsum_of_summable_norm`, the argument principle, elliptic
function theory on the multiplicative torus.

## 2026-08-07 — step 1 done: `θ_P` is holomorphic on `ℂ*`

`differentiableOn_qThetaC (P : ℝ) (hP : 1 < P) : DifferentiableOn ℂ (qThetaC P) {(0:ℂ)}ᶜ`
in `content/quantum-observable-universe/lean/QOU/QBeta/C1ConnectionPoles.lean`.
Sorry-free, axioms `[propext, Classical.choice, Quot.sound]`.

Shape of the proof, and the three places it had to route around Mathlib:

* **`DifferentiableOn.tsum` does not exist**, so the limit is taken by hand:
  `tendstoUniformlyOn_tsum` (M-test) → `.tendstoLocallyUniformlyOn` →
  `TendstoLocallyUniformlyOn.differentiableOn`. Partial sums are handled by
  `DifferentiableOn.sum` + `differentiableAt_zpow`.
* The majorant is on an **open annulus** `r < ‖w‖ < R` around each point
  (`r = ‖w₀‖/2`, `R = 2‖w₀‖`), dominated by `qThetaTerm P R n + qThetaTerm P r n`
  — the two-sided bound is what makes one series cover both tails of `ℤ`.
  Summability of the majorant is the *existing* `summable_qThetaTerm`, so the
  completed-square estimate was reused, not redone (new lemma
  `norm_le_annulus`).
* **`zpow` monotonicity in the base is missing** for the `‖w‖ⁿ ≤ Rⁿ + rⁿ`
  step at negative `n`, so it goes through `exp`/`log`: `zpow_eq_exp` +
  `Real.log_le_log` + `Real.exp_le_exp`, splitting on `0 ≤ n`.
* Required adding `import Mathlib.Analysis.Complex.LocallyUniformLimit` to the
  file.

**What this does and does not buy.** It makes `θ_P` a genuine analytic object
rather than a formal `tsum` — the prerequisite for it having a divisor at all,
and exactly the hypothesis the argument-principle route (#5) would otherwise
have to assume. It does **not** move #2: holomorphy plus the functional
equation still does not give "no other zeros" without the argument principle
or JTP. So the pole *locations* are still ⊇-only; what changed is that the
analytic setup underneath them is now derived rather than asserted.

**Next**: #3 (0-side radius 1 / ∞-side entire) is the only other item that
needs nothing absent from Mathlib — recursion bounds, tedious but unblocked.
#2 and #5 are both gated on infrastructure Mathlib does not have.

Blocks/relates: `qou-wgnx`.
