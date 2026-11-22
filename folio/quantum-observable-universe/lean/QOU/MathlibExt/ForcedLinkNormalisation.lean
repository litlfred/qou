import QOU.MathlibExt.MonotoneWordTraceFactorizes
import Mathlib.Tactic

/-!
# The link-invariant normalisation of a Markov trace is forced, and it equalises the two crossings

A Markov trace `tr` on the Hecke tower is not a link invariant of the closure: the two Markov
moves `β ↦ β σₙ` and `β ↦ β σₙ⁻¹` change it by `z` and `z'`. The standard repair is the
HOMFLY-type normalisation `X(β̂) = μ^{n−1} ν^{e} tr(β)` (braid index `n`, exponent sum `e`),
and the point of this file is that **`μ` and `ν` are not free**: invariance under the two
moves is two equations in two unknowns,

    μ ν z = 1,      μ ν⁻¹ z' = 1,

whose solution is `ν² = z'/z`, `μ = 1/(ν z)`. Nothing is chosen. Two consequences, both exact:

* **The normalised weight of a crossing does not depend on its sign.** `ν z = ν⁻¹ z'`
  (`normalised_weights_equal`): a positive and a negative crossing contribute the same factor
  `√(z z')` once the writhe normalisation is applied. Hence any *branch mixture* of `σ` and `σ⁻¹`
  at one generator — the production superposition letters `(σ + σ⁻¹)/2` and the colour-weighted
  `(½+δ/4)σ + (½−δ/4)σ⁻¹` included — has normalised weight `(cp + cm)·ν z`, and every
  production letter (`cp + cm = 1`) has the **same** normalised weight (`normalised_mixture`).
* **At convention D** (`z = q³/(q²+1)`, and `z' = z − h = 1/(q³+q)` by
  `MarkovTrace.markovParam_inv_eq_sub`) the solution is `ν = q⁻²`, `μ = (q²+1)/q = [2]_q`, and
  the common crossing weight is `q/(q²+1)` (`convD_nu`, `convD_mu`, `convD_weight`).

## Why this matters for the binding law

Under the additive law of #6611, `B = E₀ · ln(tr(free)/tr(atom))`, the monotone factorization
(`MonotoneWordTraceFactorizes.tr_affineWord`) makes `B` a sum over the inter-nucleon bond letters
alone — the nucleon runs cancel between the free and the atom word. Applying the forced
normalisation: the strand-count factor `μ^{n−1}` cancels too (both words have `n = 3A`), and
each bond letter's factor becomes the sign-independent `q/(q²+1)`. So

    B_norm = (A − 1) · E₀ · ln((q²+1)/q) = (A − 1) · E₀ · ln [2]_q,

pure bond counting with one derived bond energy (`bondCounting_of_uniform`). The un-normalised
law's bond energies `−ln b_pp ≠ −ln b_pn ≠ −ln b_nn` — and with them the `(N−Z)` asymmetry
that #6611 measured to have the wrong sign against the data — are the writhe term `ν^e` that the
un-normalised trace leaves in. This does **not** touch the scale question (`E₀`).

## What is and is not claimed

* The forcing is Markov-move invariance, per `σ^{±1}` branch. The atom word is not a braid
  (`2A+1` averaged letters), so `X` is applied branch-wise through linearity — that is exactly
  what `normalised_mixture` states — and no single writhe is ever needed.
* No production number moves. Whether the normalised trace is the *right* functional is the
  question the audit poses; this file settles only what the normalisation is and what it does.

## Base ring (§7c)

The forcing and the weight identities are over a generic `Field K` (division is needed);
convention D is the same field with `q ≠ 0`, `q² + 1 ≠ 0`. The Markov-trace-level letter
statement is over the `MarkovTrace` structure with `CommRing R`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403 — the normalised trace and the two Markov moves.
-- Ref: [leitner2026] docs/audits/2026-09-04-binding-law-options-decision-frame.md §3
-/

namespace QOU.MathlibExt.ForcedLinkNormalisation

open QOU.MathlibExt.OcneanuTrace

section Forcing

variable {K : Type*} [Field K]

/-- **The two Markov moves force `ν² = z'/z`.** -/
theorem nu_sq_forced (μ ν z z' : K) (hν : ν ≠ 0) (hz : z ≠ 0)
    (h₁ : μ * ν * z = 1) (h₂ : μ * ν⁻¹ * z' = 1) : ν ^ 2 = z' / z := by
  have e2 : μ * z' = ν := by
    have := h₂
    field_simp at this
    linear_combination this
  have key : ν ^ 2 * z = z' := by
    linear_combination (-(ν * z)) * e2 + z' * h₁
  rw [← key]
  field_simp

/-- **`μ` is forced too:** `μ = 1/(ν z)`. -/
theorem mu_forced (μ ν z : K) (hν : ν ≠ 0) (hz : z ≠ 0) (h₁ : μ * ν * z = 1) :
    μ = (ν * z)⁻¹ := by
  field_simp
  linear_combination h₁

/-- **The normalised crossing weights are sign-independent.** With `ν² = z'/z`,
`ν z = ν⁻¹ z'`: a positive crossing (weight `z`, writhe `+1`) and a negative crossing (weight
`z'`, writhe `−1`) contribute the same factor once normalised. -/
theorem normalised_weights_equal (ν z z' : K) (hν : ν ≠ 0) (hz : z ≠ 0)
    (hνsq : ν ^ 2 = z' / z) : ν * z = ν⁻¹ * z' := by
  have : z' = ν ^ 2 * z := by rw [hνsq]; field_simp
  rw [this]
  field_simp

/-- **Any branch mixture of the two crossings has normalised weight `(cp + cm)·ν z`.** The
production letters are `cp σ + cm σ⁻¹` with `cp + cm = 1`, so every one of them — `σ`, `σ⁻¹`,
`(σ+σ⁻¹)/2`, the colour-weighted average — has the *same* normalised weight `ν z`. -/
theorem normalised_mixture (ν z z' cp cm : K) (hν : ν ≠ 0) (hz : z ≠ 0)
    (hνsq : ν ^ 2 = z' / z) :
    cp * (ν * z) + cm * (ν⁻¹ * z') = (cp + cm) * (ν * z) := by
  rw [← normalised_weights_equal ν z z' hν hz hνsq]
  ring

/-- The `(c, d)` form `c σ + d·1` of a production letter is the branch form
`(c + d/h) σ − (d/h) σ⁻¹` (using `1 = (σ − σ⁻¹)/h`), so its branch weights sum to `c`. -/
theorem branch_weights_sum (c d h : K) : (c + d / h) + (-(d / h)) = c := by
  ring

end Forcing

section ConventionD

variable {K : Type*} [Field K]

/-- At convention D the negative Markov parameter is `z' = z − h = 1/(q³+q)`. -/
theorem convD_zinv (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹) = 1 / (q ^ 3 + q) := by
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h2
  field_simp
  ring

/-- **`ν = q⁻²` is the forced writhe normalisation at convention D:** `ν² = z'/z`. -/
theorem convD_nu (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (q⁻¹ ^ 2) ^ 2 = (1 / (q ^ 3 + q)) / (q ^ 3 / (q ^ 2 + 1)) := by
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h2
  field_simp

/-- **`μ = [2]_q = (q²+1)/q` is the forced strand normalisation at convention D:** `μ ν z = 1`. -/
theorem convD_mu (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ((q ^ 2 + 1) / q) * (q⁻¹ ^ 2) * (q ^ 3 / (q ^ 2 + 1)) = 1 := by
  field_simp

/-- **The common normalised crossing weight at convention D is `q/(q²+1)`**, for both signs:
`ν z = q⁻² · q³/(q²+1)` and `ν⁻¹ z' = q² · 1/(q³+q)`. -/
theorem convD_weight (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (q⁻¹ ^ 2) * (q ^ 3 / (q ^ 2 + 1)) = q / (q ^ 2 + 1)
      ∧ (q⁻¹ ^ 2)⁻¹ * (1 / (q ^ 3 + q)) = q / (q ^ 2 + 1) := by
  have h3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h2
  constructor
  · field_simp
  · field_simp

/-- **The normalised bond energy is `ln [2]_q`**: `−ln(q/(q²+1)) = ln((q²+1)/q)` for real `q > 0`. -/
theorem convD_bondEnergy (q : ℝ) (hq : 0 < q) :
    -Real.log (q / (q ^ 2 + 1)) = Real.log ((q ^ 2 + 1) / q) := by
  have h2 : 0 < q ^ 2 + 1 := by positivity
  rw [← Real.log_inv, inv_div]

end ConventionD

section BondCounting

/-- **Pure bond counting.** If every one of the `A − 1` bond letters has the same normalised
weight `w`, the additive law `B = E₀ · Σ_bonds (−ln w_k)` is `(A − 1) · E₀ · (−ln w)`. -/
theorem bondCounting_of_uniform (E₀ w : ℝ) (A : ℕ) (wk : Fin (A - 1) → ℝ)
    (huni : ∀ k, wk k = w) :
    E₀ * ∑ k, -Real.log (wk k) = ((A - 1 : ℕ) : ℝ) * (E₀ * -Real.log w) := by
  simp [huni, Finset.sum_const, Finset.card_univ, Fintype.card_fin]
  ring

end BondCounting

section OnTheTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- On the trace itself: a branch-mixture letter `cp • g m + cm • ginv m` stabilises `H m` with
constant `cp z + cm z'`, so the normalised weight statement above is about exactly this letter
class. (Its normalised value is then `normalised_mixture` with `z' = T.zinv`.) -/
theorem tr_mul_branchMixture (m : ℕ) (cp cm : R) (x : A) (hx : x ∈ T.H m) :
    T.tr (x * (cp • T.g m + cm • T.ginv m)) = (cp * T.z + cm * T.zinv) * T.tr x := by
  rw [mul_add, mul_smul_comm, mul_smul_comm, map_add, map_smul, map_smul,
    T.markov m x hx, T.markov_inv m x hx, smul_eq_mul, smul_eq_mul]
  ring

end OnTheTrace

end QOU.MathlibExt.ForcedLinkNormalisation
