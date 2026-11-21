import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# The per-quark flavour split: what the pivot can and cannot give

Target: Step 2 of `prf:flavor-split-substrate`
(`mass-theory/flavor-split-substrate-proof.md`), which sets

    (μ_d − μ_u) / μ_avg  ≈  h² · ħ_q / √q,      h = q − q⁻¹,  ħ_q = (q − 1)/q,

as a fitted ansatz (selection against the target). This file asks whether the
corpus already derives that quantity. It does **not**; the file records why, in
three exact statements. No measured number appears.

Setting (all on main):

* Proton and neutron are the `T³ = ±½` weight spaces of `(ℂ²)^{⊗3}`, u = e₁
  (orientation forced, PR #7971).
* `NucleonIsospinExclusions.restrictedTrace_ratio`: for **every** braid word
  `w`, the quantum trace restricted to the weight spaces obeys
  `T_p(w) = q² · T_n(w)`. `commutant_restrictedTrace_ratio` extends this to the
  `U_q(sl₂)` commutant. So inside the Schur–Weyl class the only p/n
  differentiator is the pivot power `q²`.

## What is proved here

1. `perQuark_split_of_nucleon_ratio` — **inversion.** If the nucleon masses are
   additive over strands (`m_p = 2μ_u + μ_d`, `m_n = μ_u + 2μ_d`) and
   `m_p = ρ · m_n`, then `(μ_d − μ_u)/μ_avg = 6(1 − ρ)/(1 + ρ)` exactly.
   With the pivot ratio `ρ = q^{±2}` this is `∓6 (q² − 1)/(q² + 1)`.
2. `pivotSplit_bar_odd` — that split is **exactly** bar-odd, `g(q⁻¹) = −g(q)`.
   `ansatz_bar` — the ansatz is not: `f(q⁻¹) = −q² f(q)` (in `t = √q`:
   `f(t⁻¹) = −t⁴ f(t)`). This settles condition (a) of Step 2 in Lean.
3. `ansatz_ne_pivotSplit` — **no pivot power gives the ansatz.** For every
   `c ≠ 0` and every `m ≥ 1`, the rational functions `c (t^m − 1)/(t^m + 1)`
   and `f(t) = (t⁴ − 1)²(t² − 1)/t⁷` differ. Reason: the ansatz has a triple
   zero at `t = 1`, every pivot split a simple one. This covers ρ = q^{±k} for
   every `k ≥ 1` (m = 2k, c = ±6), the per-strand K-weight reading (c = ±2), and
   any power-law mass map `m ∝ T^s` with `s ≠ 0` integer (ρ = q^{2s}).

## Scope

(b) for the class stated: additive strands, a nucleon ratio that is a nonzero
power of q. It says nothing about an object that breaks `U_q(sl₂)` symmetry;
the 2026-11-16 Bridge B audit records that the corpus contains none. The
Step-1 relation of the same proof is in the excised convention C and is not
touched here.
-/

namespace QOU.FlavorDressing.PivotSplitOrder

open Polynomial

/-! ## 1. Inverting the strand sum -/

/-- From a nucleon ratio `m_p = ρ · m_n` and additive strands, the per-quark
split is `6(1 − ρ)/(1 + ρ)`. -/
theorem perQuark_split_of_nucleon_ratio {K : Type*} [Field K] [CharZero K]
    (U D A ρ : K) (hp : 2 * U + D = ρ * A) (hn : U + 2 * D = A)
    (hA : A ≠ 0) (hρ : 1 + ρ ≠ 0) :
    (D - U) / ((U + D) / 2) = 6 * (1 - ρ) / (1 + ρ) := by
  have hDU : D - U = A * (1 - ρ) := by linear_combination hn - hp
  have hS : U + D = A * (1 + ρ) / 3 := by
    field_simp
    linear_combination hp + hn
  rw [hDU, hS]
  field_simp
  ring

/-- The pivot split `g(q) = 6(1 − q²)/(1 + q²)` (proton heavier by `q²`). -/
noncomputable def pivotSplit {K : Type*} [Field K] (q : K) : K :=
  6 * (1 - q ^ 2) / (1 + q ^ 2)

/-- Pivot ratio `ρ = q²` substituted into the inversion. -/
theorem perQuark_split_pivot {K : Type*} [Field K] [CharZero K]
    (U D A q : K) (hp : 2 * U + D = q ^ 2 * A) (hn : U + 2 * D = A)
    (hA : A ≠ 0) (hq2 : 1 + q ^ 2 ≠ 0) :
    (D - U) / ((U + D) / 2) = pivotSplit q :=
  perQuark_split_of_nucleon_ratio U D A (q ^ 2) hp hn hA hq2

/-! ## 2. Bar parity -/

/-- The pivot split is exactly bar-odd. -/
theorem pivotSplit_bar_odd {K : Type*} [Field K] (q : K) (hq : q ≠ 0)
    (hq2 : 1 + q ^ 2 ≠ 0) : pivotSplit q⁻¹ = -pivotSplit q := by
  have hq2' : q ^ 2 + 1 ≠ 0 := by rwa [add_comm]
  unfold pivotSplit
  field_simp
  ring

/-- The Step-2 ansatz in `t = √q`: `h² ħ_q /√q = (t⁴ − 1)²(t² − 1)/t⁷`. -/
noncomputable def ansatz {K : Type*} [Field K] (t : K) : K :=
  (t ^ 4 - 1) ^ 2 * (t ^ 2 - 1) / t ^ 7

/-- The ansatz written from its factors: `h = (t⁴−1)/t²`, `ħ_q = (t²−1)/t²`. -/
theorem ansatz_eq_factors {K : Type*} [Field K] (t : K) (ht : t ≠ 0) :
    ansatz t = ((t ^ 4 - 1) / t ^ 2) ^ 2 * ((t ^ 2 - 1) / t ^ 2) / t := by
  unfold ansatz
  field_simp

/-- Condition (a) of Step 2 fails: the ansatz is bar-odd only up to `t⁴ = q²`. -/
theorem ansatz_bar {K : Type*} [Field K] (t : K) (ht : t ≠ 0) :
    ansatz t⁻¹ = -(t ^ 4) * ansatz t := by
  unfold ansatz
  field_simp
  ring

/-! ## 3. Order of vanishing at `t = 1` -/

/-- A double root at 1 kills the derivative at 1. -/
theorem derivative_eval_one_of_sq_dvd {p : ℚ[X]} (h : (X - 1) ^ 2 ∣ p) :
    (derivative p).eval 1 = 0 := by
  obtain ⟨g, rfl⟩ := h
  simp [derivative_mul, derivative_pow]

/-- The ansatz numerator has `(t − 1)³` as a factor. -/
theorem ansatz_numerator_factor :
    ((X : ℚ[X]) ^ 4 - 1) ^ 2 * (X ^ 2 - 1) =
      (X - 1) ^ 3 * ((X ^ 3 + X ^ 2 + X + 1) ^ 2 * (X + 1)) := by
  ring

/-- **No pivot power reproduces the ansatz.** Cleared of denominators
(`t⁷ (t^m + 1)`, nonzero near `t = 1`), the identity
`c (t^m − 1)/(t^m + 1) = (t⁴ − 1)²(t² − 1)/t⁷` is false for every `c ≠ 0`,
`m ≥ 1`. -/
theorem ansatz_ne_pivotSplit (c : ℚ) (hc : c ≠ 0) (m : ℕ) (hm : 1 ≤ m) :
    C c * ((X : ℚ[X]) ^ m - 1) * X ^ 7 ≠
      ((X : ℚ[X]) ^ 4 - 1) ^ 2 * (X ^ 2 - 1) * (X ^ m + 1) := by
  intro heq
  have hdvd : (X - 1) ^ 2 ∣ C c * ((X : ℚ[X]) ^ m - 1) * X ^ 7 := by
    rw [heq, ansatz_numerator_factor]
    exact ⟨(X - 1) * ((X ^ 3 + X ^ 2 + X + 1) ^ 2 * (X + 1)) * (X ^ m + 1), by ring⟩
  have h0 := derivative_eval_one_of_sq_dvd hdvd
  simp [derivative_mul, derivative_X_pow, hc] at h0
  omega

end QOU.FlavorDressing.PivotSplitOrder
