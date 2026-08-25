---
# qou-c1ln
title: 'LEAN: discharge the C1 connection results that are only numerical'
status: todo
type: task
priority: high
created_at: 2026-08-07T22:20:00Z
updated_at: 2026-08-08T13:00:00Z
---

> **⏸ PAUSED by owner, 2026-08-08.** Rows 1–3 are proved; rows 4, 5 and 6 are
> open but every one of them is explicitly recorded as having **no downstream
> consumer**. The axis is finished as far as anything needs it. Kept as a bean
> for the record; do not start rows 4/6 without checking back.

**Claimed** by session on branch `pr4672` → `claude/c1-theta-canonical-solutions-2026-08-07`.
Rows 1 and **3 done**; row 2 rescoped to one missing lemma; row 5 dropped
(nothing consumes it); rows 4 and 6 open.

Everything load-bearing in the C1 connection arc (bean `qou-wgnx`) rests on
**numerics**, not derivation. The Lean that exists covers only the easy
algebraic layer. This bean tracks closing that gap, in dependency order.

| # | claim | today | needs |
|---|---|---|---|
| 1 | `qThetaC` holomorphic on `ℂ*` | ✅ **PROVED** `differentiableOn_qThetaC` | done 2026-08-07 — see below |
| 2 | **exact** zero locus (converse of `qTheta_neg_zpow_eq_zero`) | ✅ **PROVED** `qThetaC_eq_zero_iff` | done 2026-08-08 via #4770 — the argument principle landed too (`qou-argp`) |
| 3 | 0-side series radius 1; ∞-side entire | ✅ **PROVED** (radius `≥ 1`; entire) | done 2026-08-07 — see below |
| 4 | `Y₀`, `Y_∞`, inverse, meromorphy; `P(pz)=P(z)` | not proved | matrix-valued meromorphic functions; `Analysis/Meromorphic/*` partial |
| 5 | pole divisor + completeness (residue thm) | numerical | ~~argument principle~~ — **that gap closed** (#4770). Still **not worth working: nothing consumes it** (below) |
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
trivial". Text-extracted `library/arxiv-0903.0853v3/0903.0853v3.pdf` (Astérisque 355) and read
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

## 2026-08-07 — row 3 done: both series converge where they are used

New file `content/quantum-observable-universe/lean/QOU/QBeta/C1SeriesConvergence.lean`,
namespace `QOU.QBeta.C1Series`. Five theorems, sorry-free,
`[propext, Classical.choice, Quot.sound]`.

* `summable_zeroSideCoeff` — the `0`-side `∑ g_k z^k` converges for every
  `‖z‖ < 1`. The ratio `g_{k+2}/g_k` tends to `1` like `1 + O(‖p‖^{-k})`, so the
  coefficients are **bounded**, which is all radius `≥ 1` needs.
* `summable_infSideCoeff` — the `∞`-side is **entire**.

Three of the five are `θ`-free sequence lemmas Mathlib does not have, and are
the reusable part:

* `norm_le_of_ratio_le_one_add_geometric` — a two-step recursion whose ratio is
  `1 + O(geometric)` has bounded terms. `∏(1 + Cρᵏ) ≤ exp(C∑ρᵏ) ≤ exp(C/(1−ρ))`.
* `summable_of_norm_coeff_le` — bounded coefficients ⇒ radius `≥ 1`.
* `summable_of_two_step_geometric` — a two-step recursion with geometrically
  vanishing coefficients gives an **entire** series. The majorant is
  `M ∏_{j<k}(cσʲ)` with **`σ = √ρ`**: the two-step lag costs exactly a square
  root (the naive `∏(cρʲ)` ansatz provably fails), and `σ² = ρ` is what lets the
  induction close with a constant `c` rather than a `k`-dependent one.

All three take the recursion hypothesis only for `k ≥ K` and absorb the first
`K+2` terms into the constant — necessary in both applications, since the
estimates only hold once the geometric tail overtakes the constant term, and
for the `∞`-side that is also what keeps the denominator away from zero.

**Not proved, deliberately**: sharpness of the `0`-side radius (proved `≥ 1`,
not `= 1`). The mirror estimate `‖ratio‖ ≥ 1 − Cρᵏ` plus `1 − x ≥ exp(−2x)`
would give it; nothing downstream uses it, because the singularity's *location*
is pinned by the `θ_p` zeros rather than by this radius. Also not proved: that
these recursions are the ones the operator forces — they are *defined* here to
match the computation, so the file certifies convergence of the stated
sequences, not that `Y₀`/`Y_∞` are solutions. That is row 4.

Two `positivity`/`isDefEq` heartbeat timeouts appeared once the majorant
constants were `set`-bound; `clear_value` on the four definitions plus explicit
`mul_nonneg`/`div_nonneg` terms fixed it. Worth remembering: `set` leaves a
let-binding that `positivity` will unfold.

**Next**: row 4 (`Y₀`, `Y_∞`, inverse, meromorphy) is now the only open item
with a path — and it is the expensive one (matrix-valued meromorphic functions,
`Analysis/Meromorphic/*` only partial). Row 2 needs the argument principle and
nothing else. Rows 5 and 6 are not worth starting — see the row-5 note above.
See `qou-c1wr` for the separate question of whether any of this should become
authored content in the first place.

Blocks/relates: `qou-wgnx`, `qou-c1wr`.

## 2026-08-08 — claim released; rows 4 and 6 still open

The claim line above names branch `pr4672` →
`claude/c1-theta-canonical-solutions-2026-08-07`, which merged as #4672. Rows
1, 2, 3 and 5 are settled there. **Rows 4 and 6 were deliberately not started**
— `Y_0`/`Y_∞` meromorphy and the closed form for `χ` — on the ground recorded in
`qou-c1wr` that nothing downstream consumes the divisor.

Unclaimed. Status moved `in-progress` → `todo`; the claim is stale, not active.

## 2026-08-08 (later) — row 2 CLOSED; and the axis has no remaining work worth doing

**Row 2 was stale in this table.** It read *"⊇ only … needs the argument
principle, and nothing else"*. Both halves landed in #4770 and are on `main`:

* `QOU.Mathlib.ArgumentPrinciple.argument_principle`, plus the annulus forms
  `argumentPrinciple_annulus_{single,filter,finset}` in `C1ConnectionPoles.lean`
  — the named lemma the 08-07 rescope said was the only gap;
* `QOU.QBeta.C1ThetaZeroLocus.qThetaC_eq_zero_iff` —
  `qThetaC P w = 0 ↔ ∃ k : ℤ, w = −P^{2k}`, the exact converse, plus every zero
  simple.

Row 5's stated blocker was *the same* argument principle, so that gap is closed
too — but row 5 keeps its **do-not-work** marker for the independent reason
recorded above: nothing consumes it.

### Resulting state of this bean

| row | state |
|---|---|
| 1 holomorphy | ✅ proved |
| 2 exact zero locus | ✅ proved (#4770) |
| 3 series convergence | ✅ proved |
| 4 `Y₀`/`Y_∞` meromorphy | open — expensive, **no consumer** |
| 5 pole divisor | unblocked but **no consumer**; explicitly not to be worked |
| 6 `χ` closed form | open — needs 4; **no consumer** |

**Everything still open on this axis is explicitly recorded as having no
downstream consumer.** Rows 4 and 6 were "deliberately not started" on that
ground (08-08 entry), row 5 likewise. So the honest reading is not "three rows
remain" but **"the axis is finished as far as anything needs it"**; what is left
is optional completeness work with a known-empty consumer set.

### Third instance of the same staleness failure in two days

`qou-wgnx`'s top summary said the Stokes multipliers were open while its own
entries 21–23 said trivial; this table said row 2 needed a lemma that had
already landed. Both are *summaries that went stale against work recorded
elsewhere in the same corpus*, and both were read as current by a later agent
(PR #4790, then this one). The per-bean fixes are in; the pattern is worth a
systemic look — a stale-summary check has no owner today.
