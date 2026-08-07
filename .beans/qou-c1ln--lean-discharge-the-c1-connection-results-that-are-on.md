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
| 2 | **exact** zero locus (converse of `qTheta_neg_zpow_eq_zero`) | ⊇ only; **all inputs but one now proved** | ~~JTP~~ **the argument principle, and nothing else** — rescoped 2026-08-07, see below |
| 3 | 0-side series radius 1; ∞-side entire | not proved | recursion bounds; feasible, tedious |
| 4 | `Y₀`, `Y_∞`, inverse, meromorphy; `P(pz)=P(z)` | not proved | matrix-valued meromorphic functions; `Analysis/Meromorphic/*` partial |
| 5 | pole divisor + completeness (residue thm) | numerical | argument principle — same single gap as #2. **But: nothing consumes it** (below) |
| 6 | `χ` = the closed form, `α = t₂/T`, order 2 | numerical (12 pts, `5.3e-63`) | all of 1–5 |

**Confirmed absent** in Mathlib (name scan at HEAD, 2026-08-07):
`DifferentiableOn.tsum`, `differentiableOn_tsum_of_summable_norm`, the argument
principle, any winding number, any complex residue (every `residue` hit is
`IsLocalRing`), elliptic function theory on the multiplicative torus.
**Present and usable**: the full `circleIntegral` API, including
`Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable`,
`HasProd`/`Multipliable`/`tprod`, `Analysis/Meromorphic/{Divisor, IsolatedZeros, Order}`.

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
and exactly the hypothesis the argument-principle route would otherwise have to
assume. The pole *locations* are still ⊇-only. What changed is that the analytic
setup underneath them is now derived rather than asserted — and, as it turned
out, that unlocked the rescope below.

## 2026-08-07 — row 2 RESCOPED: the Jacobi triple product is not needed

I had this wrong, and the table said so for a day: row 2 claimed the converse
zero locus needs JTP, and that the Liouville step needs elliptic theory on
`ℂ*/p^ℤ`. It doesn't. The converse follows from three facts **all now proved in
Lean**, plus the argument principle:

| input | Lean |
|---|---|
| `θ_p` holomorphic on `ℂ*` | `differentiableOn_qThetaC` ✅ (today) |
| `θ_p(pw) = w·θ_p(w)` | `qThetaC_functional_equation` ✅ (today, complex version) |
| `θ_p(−p^k) = 0` | `qTheta_neg_zpow_eq_zero` ✅ |

Differentiating the functional equation — legitimate *only* because holomorphy
is now available — and dividing by `θ_p(pw) = wθ_p(w)`:

    p·θ'(pw)/θ(pw) = 1/w + θ'(w)/θ(w)

which is `logDeriv_qThetaC_functional_equation`, also proved today. Substituting
`w ↦ pw` in `∮_{|w|=ρ} θ'/θ dw` turns that `1/w` into `2πi`, so the winding
number on `|w| = pρ` is **exactly one more** than on `|w| = ρ`. The argument
principle reads that off as *exactly one zero, with multiplicity, per
fundamental annulus*; `qTheta_neg_zpow_eq_zero` supplies that zero at `−p^k`,
which therefore is simple and is the only one. Zero set `= −p^ℤ`. ∎

So JTP is **strictly more work** (it additionally needs Liouville on `ℂ*/p^ℤ`)
and is off the critical path. What remains is **one named lemma**: the argument
principle on an annulus. Mathlib does not have it — but it does have the whole
`circleIntegral` layer under it, so this is a lemma-sized job, not a theory
build-out. That is a materially different estimate from "formalise JTP", and
the distinction was being lost.

**And the contour step is proved too, not just sketched.** `qTheta_winding_step`:

    ∮_{|z| = pρ} θ'/θ dz = 2πi + ∮_{|z| = ρ} θ'/θ dz

for any `ρ > 0` on whose circle `θ_P` does not vanish — the exact form the
argument principle consumes. Getting there needed two `θ`-free lemmas Mathlib
does not have, both stated reusably:

* `circleIntegral_scale` — change of variables for `circleIntegral`,
  `∮_{|z|=aR} f = ∮_{|z|=R} a·f(a·z)`. Mathlib has no substitution rule for
  `circleIntegral` at all; this falls straight out of the definition via
  `deriv_circleMap`, but someone has to write it.
* `winding_step` — a `1/z` in the integrand is a `2πi` in the integral, given
  circle-integrability (`circleIntegral.integral_sub_center_inv` supplies the
  `2πi`; `circleIntegrable_sub_zpow_iff` the integrability of `z⁻¹`).

The specialisation to `θ_P` also needed `deriv (qThetaC P)` to be continuous on
the circle, i.e. `DifferentiableOn → AnalyticOnNhd → .deriv → .differentiableOn`,
then `ContinuousOn.div` against the non-vanishing hypothesis and
`ContinuousOn.circleIntegrable`.

New Lean today (all sorry-free, `[propext, Classical.choice, Quot.sound]`):
`qThetaC_functional_equation`, `deriv_qThetaC_functional_equation`,
`logDeriv_qThetaC_functional_equation`, `circleIntegral_scale`, `winding_step`,
`qTheta_winding_step` — plus `differentiableOn_qThetaC` from step 1, seven in
all.

Numerical corroboration at our substrate:
`computations/qbeta/c3_w2_c1_theta_zero_count.py` — the two new identities
reproduce to full working precision (which is what catches a wrong power of `p`
or a `P`-vs-`p` mismatch against this directory's `theta()`), one simple zero
per fundamental annulus at exactly `−p^k`, and exactly 9 across a
`p^-4.5 < |w| < p^4.5` sweep, excluding zeros hiding between orbit points.

## 2026-08-07 — row 5: settled, NOTHING consumes it

Owner asked whether anything consumes the pole divisor + completeness result.
Corpus grep (`content/**/*.ts` for connection matrix / pole divisor /
theta-canonical / connection invariant / `C1ConnectionPoles`):

* **One** content block mentions this arc at all:
  `conj:qdifference-kernel-prolongation-symbol`, consumed in turn by
  `schwinger-measure-computational-time.ts` and listed in `mass-theory.ts`.
* What it actually consumes is route **(B) "numeric connection-matrix
  theta-growth `q^{m²/4}`"** — a *growth rate* — and the isoclinicity result.
  **Not** the divisor, not `χ`, not the closed form, not `α = t₂/T`.
* Outside `computations/`, `lean/` and `.beans/`, nothing references the
  divisor at all.

**So row 5 has zero consumers**, and it is the item gated on the same missing
argument principle as row 2 while being strictly downstream of rows 3–4 as
well. It should not be worked. If the divisor is ever wanted, row 2 is the
cheaper thing to buy and it delivers the same missing ingredient.

## 2026-08-07 — RSZ citations checked against the source, they hold

The corpus note on `conj:qdifference-kernel-prolongation-symbol` (2026-07-20)
cites RSZ Thm 2.2.1 / 2.2.4 / 5.5.7 for "C1 pure isoclinic ⇒ Stokes data
trivial". Text-extracted `uploads/0903.0853v3.pdf` (Astérisque 355) and read
them. All three say what is claimed:

* **2.2.1** — the Newton polygon is well defined, additive, multiplicative,
  and **(iv)** gives its behaviour under **ramification** `z′ := z^{1/ℓ}`.
  That is the "invariant under ramified pullback" leg.
* **2.2.4** — every module over `ℂ({z})` has a *unique* filtration with **pure
  isoclinic** quotients; it is strictly functorial and `gr` is exact, faithful
  and ⊗-compatible. That is the "permanent invariant preserved by every module
  transform" leg.
* **5.5.7 (Stokes phenomenon)** — `St_{λ₀}(λ; A) = Id` for some/all generic
  `λ` ⟺ `A = A₀`, and each `St_{λ₀}(λ; A)` is an **upper-triangular unipotent**
  matrix-valued function. The unipotent blocks are the `U_{i,j}` of 2.2.4's
  normal form, which exist only *between distinct slopes* — so for a pure
  isoclinic (single-slope) module there are none, `A = A₀` outright, and the
  Stokes data is trivial. That is the "unipotent part trivial, U→I" leg, and
  it is why C1 has no Stokes multipliers to find.

So the session's independent re-derivation agrees with the source and with the
prior corpus note. Nothing to revise.

**Next**, in order: #3 (0-side radius 1 / ∞-side entire) — the only item
needing nothing absent from Mathlib, tedious but unblocked; then #2, if and
only if someone is willing to prove the argument principle. #5 and #6 are not
worth starting. See `qou-c1wr` for the separate question of whether any of this
should become authored content in the first place.

Blocks/relates: `qou-wgnx`, `qou-c1wr`.
