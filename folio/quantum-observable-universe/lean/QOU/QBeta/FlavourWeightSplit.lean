import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic

/-!
# The flavour split of the convention-D trace on the nucleon weight spaces

Owner ruling 2026-11-20 (Carl): derive the `n ≠ p` flavour ingredient on the `U_q` / weight
side, and score `Q_β` on the γγ base `V³` with that `ε`. Beans `qou-99qc`, `qou-ales`.

## The functional, and where each piece comes from

* Convention D's Markov trace is the `U_q(sl₂)` quantum trace `Tr(K^{⊗n} ·) / [2]^n` on
  `(C²)^{⊗n}` with `K = diag(q, q⁻¹)` (bean `qou-99qc`, 2026-11-19 05:10Z: the check
  `Tr(K⊗K Ř)/[2]² = q³/(q²+1) = z_D`). `K` commutes with the braid action, so the trace is a sum
  over weight spaces, and on a weight space `K^{⊗3}` is a scalar: `q` on the proton-type `(2,1)`
  space `W_p`, `q⁻¹` on the neutron-type `(1,2)` space `W_n`
  (`NucleonWeightSpaceTwoTerm.trace_Kp_word`, `trace_Kn_word`).
* The `T³ = ±½` components of the ruled `ε` on an element `X` are therefore
  `ε_p(X) = q·tr_{W_p}(X)/[2]³` and `ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³`, and the flavour functional
  is their difference `ε_flavour(X) = ε_n(X) − ε_p(X)`. Nothing here is a new choice: the
  normalisation `[2]³` is the one that makes the whole-space trace equal the `z_D` Markov trace.
* The element is the γγ base `V³ = (σ₁σ₂⁻¹)³` of PR #8564 (generators numbered from 1 here).
  With the photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` and the corpus-derived colour weights
  `(0, 0, q h)` and `(0, 0, −q⁻¹ h)`, it is the two-photon product
  (`NucleonWeightSpaceTwoTerm.borromeanV3A_eq_switched_photon_product`).

## What is proved

1. `epsFlavour_V3_eq`: `ε_flavour(V³) = (q²−1)·P(q) / (q⁴ (q²+1)³)` over any field,
   `P(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1`.
2. `epsP_bar_eq_epsN`: the bar involution `q ↦ q⁻¹` carries the proton component to the
   neutron one. Hence `epsFlavour_V3_bar_odd`: `ε_flavour(V³)` is exactly bar-odd.
3. `epsFlavour_V3_ne_zero`: on `1 < q ≤ 23/20` (the range of PR #8564's selection theorem) it is
   non-zero, in fact negative.
4. `normalised_split_V3_eq_zero`: the other normalisation (each weight space divided by its own
   dimension, i.e. the plain trace) gives zero. Scope (b) for that functional; the invariant is
   the intertwiner `P(q)` of `NucleonWeightSpaceTraces`.
5. `trace_mirror_V3A`, `trace_inv_V3A`: on the weight space the mirror word `(σ₁⁻¹σ₂)³` (image of
   `V³` under the antipode `σ ↦ σ⁻¹`) and the inverse `V⁻³` have the same trace as `V³`. So the
   antipode-odd projection of every weight-space trace of `V³` vanishes.
6. `trace_commutator_eq_zero`: two photons in either order give the same trace on every weight
   space, so photon ORDER cannot carry flavour for any trace functional.

## What is NOT claimed

* That `Q_β = |ε_flavour(V³)|·E₀`. That is the reader's step, identical to the ruled form
  `Q_β = |ε(Δ)|·E₀`; the probe computes it. The identification of `ε_flavour` with `ε(Δ)` is the
  owner's ruling of 2026-11-20, not a theorem here.
* Anything about the sign of `m_n − m_p` (see the audit, §5).
* No numerical value enters. Generic `[Field R]` except item 3, which needs an order (§7c).
-/

namespace QOU.QBeta.FlavourWeightSplit

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

section Generic

variable {R : Type*} [Field R]

/-- The quantum dimension `[2]_q = q + q⁻¹` of one strand. -/
def qd2 (q : R) : R := q + q⁻¹

/-- Proton (`T³ = +½`) component of the convention-D trace: `K^{⊗3}` acts by `q`. -/
def epsP (q : R) (M : Matrix (Fin 3) (Fin 3) R) : R := q * trace M / qd2 q ^ 3

/-- Neutron (`T³ = −½`) component of the convention-D trace: `K^{⊗3}` acts by `q⁻¹`. -/
def epsN (q : R) (M : Matrix (Fin 3) (Fin 3) R) : R := q⁻¹ * trace M / qd2 q ^ 3

/-- The flavour functional on the γγ base: `ε_n(V³) − ε_p(V³)`. -/
def epsFlavourV3 (q : R) : R := epsN q (borromeanV3B q) - epsP q (borromeanV3A q)

/-- The palindromic polynomial in `tr(V³) = −P(q)/q⁶`. -/
def polyP (q : R) : R := q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1

/-- The closed form of `ε_flavour(V³)`. -/
def fV3 (q : R) : R := (q ^ 2 - 1) * polyP q / (q ^ 4 * (q ^ 2 + 1) ^ 3)

theorem qd2_ne_zero (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : qd2 q ≠ 0 := by
  unfold qd2
  intro h
  apply hq2
  have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [← this, h, mul_zero]

/-- **The flavour functional on `V³`, closed form.** -/
theorem epsFlavour_V3_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    epsFlavourV3 q = fV3 q := by
  unfold epsFlavourV3 epsN epsP fV3 polyP qd2
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp; try ring
  rw [e2]
  field_simp
  ring

/-- **Bar involution swaps the two flavour components.** The proton component evaluated at
`q⁻¹` is the neutron component at `q`. -/
theorem epsP_bar_eq_epsN (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    epsP q⁻¹ (borromeanV3A q⁻¹) = epsN q (borromeanV3B q) := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  unfold epsP epsN qd2
  rw [trace_borromeanV3A q⁻¹ hqi, trace_borromeanV3B q hq, inv_inv]
  have e1 : q⁻¹ + q = (q ^ 2 + 1) / q := by field_simp; try ring
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp; try ring
  rw [e1, e2]
  field_simp
  ring

/-- **`ε_flavour(V³)` is exactly bar-odd.** -/
theorem fV3_bar_odd (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : fV3 q⁻¹ = -fV3 q := by
  unfold fV3 polyP
  have e : (q⁻¹) ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; try ring
  rw [e]
  field_simp
  ring

theorem epsFlavour_V3_bar_odd (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq2' : (q⁻¹) ^ 2 + 1 ≠ 0) : epsFlavourV3 q⁻¹ = -epsFlavourV3 q := by
  rw [epsFlavour_V3_eq q⁻¹ (inv_ne_zero hq) hq2', epsFlavour_V3_eq q hq hq2, fV3_bar_odd q hq hq2]

/-- **The per-sector normalised split vanishes** (scope (b) for that functional): dividing each
weight space by its own dimension leaves the plain traces, which are equal. -/
theorem normalised_split_V3_eq_zero (q : R) (hq : q ≠ 0) :
    trace (borromeanV3B q) / 3 - trace (borromeanV3A q) / 3 = 0 := by
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq, sub_self]

/-- The antipode image `σ ↦ σ⁻¹` of `V = σ₁σ₂⁻¹` on `W_p`: `σ₁⁻¹σ₂`. -/
def mirrorVA (q : R) : Matrix (Fin 3) (Fin 3) R := A₁Inv q * A₂ q

/-- `V⁻¹ = σ₂σ₁⁻¹` on `W_p`. -/
def invVA (q : R) : Matrix (Fin 3) (Fin 3) R := A₂ q * A₁Inv q

/-- **The mirror of `V³` has the same weight-space trace.** -/
theorem trace_mirror_V3A (q : R) (hq : q ≠ 0) :
    trace (mirrorVA q * mirrorVA q * mirrorVA q) = trace (borromeanV3A q) := by
  rw [trace_borromeanV3A q hq]
  simp [mirrorVA, A₁Inv, A₂, Matrix.trace_fin_three]
  field_simp
  ring

/-- **`V⁻³` has the same weight-space trace as `V³`.** -/
theorem trace_inv_V3A (q : R) (hq : q ≠ 0) :
    trace (invVA q * invVA q * invVA q) = trace (borromeanV3A q) := by
  rw [trace_borromeanV3A q hq]
  simp [invVA, A₁Inv, A₂, Matrix.trace_fin_three]
  field_simp
  ring

/-- The four-term photon `γ(φ) = 1 + φ₀σ₁ + φ₁σ₂ + φ₀₁·σ₁σ₂⁻¹` on the proton weight space
(generators numbered from 1; the fourth term is the chiral vertex `V`). -/
def photonA (q φ₀ φ₁ φ₀₁ : R) : Matrix (Fin 3) (Fin 3) R :=
  1 + φ₀ • A₁ q + φ₁ • A₂ q + φ₀₁ • borromeanVA q

/-- **Photon order carries no trace information**: on every weight space (and so in every
`K`-weighted trace) `γ(φ)γ(ψ)` and `γ(ψ)γ(φ)` have equal trace. -/
theorem trace_commutator_eq_zero (q φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R) :
    trace (photonA q φ₀ φ₁ φ₀₁ * photonA q ψ₀ ψ₁ ψ₀₁) -
      trace (photonA q ψ₀ ψ₁ ψ₀₁ * photonA q φ₀ φ₁ φ₀₁) = 0 := by
  rw [Matrix.trace_mul_comm, sub_self]

end Generic

/-! ## Archimedean: non-vanishing on the selection range -/

theorem polyP_neg {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) : polyP q < 0 := by
  set t := q ^ 2 - 1 with ht
  have ht0 : 0 < t := by nlinarith
  have ht1 : t ≤ 1 / 2 := by nlinarith
  have hP : polyP q = t ^ 6 + 3 * t ^ 5 + 3 * t ^ 4 - 3 * t ^ 3 - 9 * t ^ 2 - 9 * t - 3 := by
    unfold polyP
    have : q ^ 2 = t + 1 := by rw [ht]; ring
    have e : ∀ n : ℕ, q ^ (2 * n) = (t + 1) ^ n := fun n => by rw [pow_mul, this]
    rw [show q ^ 12 = q ^ (2 * 6) by norm_num, show q ^ 10 = q ^ (2 * 5) by norm_num,
      show q ^ 8 = q ^ (2 * 4) by norm_num, show q ^ 6 = q ^ (2 * 3) by norm_num,
      show q ^ 4 = q ^ (2 * 2) by norm_num, e, e, e, e, e, this]
    ring
  rw [hP]
  have h4 : t ^ 4 ≤ 1 / 16 := by
    have := pow_le_pow_left₀ ht0.le ht1 4
    norm_num at this ⊢; linarith
  have hb : t ^ 6 + 3 * t ^ 5 + 3 * t ^ 4 = t ^ 4 * (t ^ 2 + 3 * t + 3) := by ring
  have hc : t ^ 2 + 3 * t + 3 ≤ 5 := by nlinarith
  have hpos : 0 ≤ t ^ 4 := by positivity
  nlinarith [mul_le_mul h4 hc (by positivity) (by norm_num : (0:ℝ) ≤ 1 / 16),
    pow_pos ht0 3, pow_pos ht0 2]

/-- **`ε_flavour(V³)` is negative, hence non-zero, on `1 < q ≤ 23/20`.** -/
theorem epsFlavour_V3_neg {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) : epsFlavourV3 q < 0 := by
  have hq : q ≠ 0 := by positivity
  have hq2' : q ^ 2 + 1 ≠ 0 := by positivity
  rw [epsFlavour_V3_eq q hq hq2']
  unfold fV3
  apply div_neg_of_neg_of_pos
  · exact mul_neg_of_pos_of_neg (by nlinarith) (polyP_neg hq1 hq2)
  · positivity

theorem epsFlavour_V3_ne_zero {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) : epsFlavourV3 q ≠ 0 :=
  (epsFlavour_V3_neg hq1 hq2).ne

end QOU.QBeta.FlavourWeightSplit
