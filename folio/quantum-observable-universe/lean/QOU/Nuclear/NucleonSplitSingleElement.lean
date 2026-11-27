import QOU.Nuclear.DecayConjectures
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# What can discharge C1–C3: the single-element theorem for the nucleon split

Bean `qou-myts` (compute-accuracy epic), item C1; beans `qou-99qc`, `qou-wxhi`.

`QOU.QBeta.DecayConjectures` states the three undischarged inputs of the scored
`Q_β = |ε_flavour(V³)|·E₀`: C1 (the decay functional is the `T³` weight trace), C2 (both
nucleons carry the γγ base `V³`), C3 (the posited scale, `Q_β = |ε|·E₀`). The natural way
to discharge C3 is energy conservation, `Q_β = m_n − m_p − m_e`, with each nucleon mass read
off a trace. This file proves what that route can and cannot give, for **every** element of
the braid algebra, not only `V³`.

## The key fact: one element cannot tell `W_n` from `W_p` except through `K`

The neutron weight-space representation is the proton one with `σ₁ ↔ σ₂`
(`B₁ = A₂`, `B₂ = A₁`), and the matrix `P` intertwines them (`intertwine₁`, `intertwine₂`,
and their inverses). We extend the intertwining from positive words (`intertwine_word`) to the
whole free algebra on `σ₁^{±1}, σ₂^{±1}`: every linear combination of braid words, so every
photon product `γ(φ)·γ(ψ)` with `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` and every inverse letter
(`intertwine_rho`). Hence the plain traces agree on every element (`trace_rhoB_eq_trace_rhoA`).

On a weight space, `K^{⊗3}` and the all-pairs charge insertion are scalars (`Kp = q`,
`Kn = q⁻¹`, `QPairP = 0`, `QPairN = −1/3`). So for the owner-ruled two-term trace
`τ_N(X) = tr((K_N + c·Q_pair,N)·ρ_N(X))` with any coupling `c`:

    τ_p(X) = q·t(X),    τ_n(X) = (q⁻¹ − c/3)·t(X),    t(X) = tr ρ_p(X).

(`tauP_eq`, `tauN_eq`.) The element enters only through the common factor `t(X)`.

## Consequences

1. **Linear energy map: wrong sign, for every element (scope (b), invariant `q⁻¹ < q`).**
   If `m_N = S·τ_N − c₀` with `S > 0` and the proton mass positive (`τ_p > 0`), then for
   `q > 1` and `c ≥ 0`, `m_n < m_p` (`linear_mass_neutron_lighter`). Energy conservation then
   gives `Q_β < 0`, so C3 (`Q_β = |ε|·E₀ ≥ 0`) cannot be discharged this way
   (`not_decayEnergyScale_of_linear`). This is a theorem form of the owner's working conjecture
   of 2026-11-21, *"Q_beta I don't think is a linear map"*, for the case of one element used for
   both nucleons. It needs no value of `c`, `S`, `c₀` or `m_e ≥ 0`.
2. **Gibbs (log) energy map: right sign, for every element.** If `m_N = −E·log τ_N + c₀`
   (`F = −k_BT·log Z`, the route-T reading with `k_BT_q = E₀`), then
   `m_n − m_p = E·(2·log q − log(1 − c·q/3))` (`gibbs_mass_split_eq`), positive for `q > 1`,
   `0 ≤ c`, `c·q < 3` (`gibbs_mass_split_pos`). At `c = 0` this is the corpus's route-T cell
   `2E₀·log q` (`docs/audits/2026-11-21-qbeta-energy-map-spectator.md`); the two-term matter
   term only adds `−E·log(1 − c·q/3) ≥ 0`.

## What this says about discharging C1–C3

With one element for both nucleons, the split is **word-independent**: no choice of word,
photon weights, power of `V`, or inverse letters can move it. A discharge of C1–C3 through
energy conservation therefore needs at least one of:

* a non-linear energy map (the Gibbs map above is one; its scale `E` and the coupling `c` are
  not derived here), or
* nucleon elements that are **not** related by the `σ₁ ↔ σ₂` intertwiner (C2 replaced, e.g. a
  proton and a neutron built from different words), or
* a lepton / spectator factor that is not a weight-space scalar.

Nothing here assigns a value to `c` or `E`, and nothing is compared to data. The numbers at the
proton `q₀` are in `computations/probes/nucleon_split_single_element_probe.py`.

-- Ref: [leitner2026] docs/audits/2026-11-27-nucleon-split-single-element-theorem.md
-- Ref: [leitner2026] docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md
-/

namespace QOU.QBeta.NucleonSplitSingleElement

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

section Generic

variable {R : Type*} [Field R]

/-- The four letters `σ₁, σ₂, σ₁⁻¹, σ₂⁻¹` on the proton weight space `W_p`. -/
def genA (q : R) : Fin 4 → Matrix (Fin 3) (Fin 3) R :=
  ![A₁ q, A₂ q, A₁Inv q, A₂Inv q]

/-- The same four letters on the neutron weight space `W_n`. -/
def genB (q : R) : Fin 4 → Matrix (Fin 3) (Fin 3) R :=
  ![B₁ q, B₂ q, B₁Inv q, B₂Inv q]

/-- The proton representation of the free algebra on the four letters: every finite linear
combination of braid words, inverse letters included. -/
noncomputable def rhoA (q : R) : FreeAlgebra R (Fin 4) →ₐ[R] Matrix (Fin 3) (Fin 3) R :=
  FreeAlgebra.lift R (genA q)

/-- The neutron representation of the same free algebra. -/
noncomputable def rhoB (q : R) : FreeAlgebra R (Fin 4) →ₐ[R] Matrix (Fin 3) (Fin 3) R :=
  FreeAlgebra.lift R (genB q)

theorem intertwine_gen (q : R) (hq : q ≠ 0) (i : Fin 4) :
    P q * genA q i = genB q i * P q := by
  fin_cases i
  · exact intertwine₁ q hq
  · exact intertwine₂ q hq
  · exact intertwine₁Inv q hq
  · exact intertwine₂Inv q hq

/-- `P` intertwines the two representations on the whole free algebra. -/
theorem intertwine_rho (q : R) (hq : q ≠ 0) (x : FreeAlgebra R (Fin 4)) :
    P q * rhoA q x = rhoB q x * P q := by
  induction x using FreeAlgebra.induction with
  | grade0 r =>
    simp only [AlgHom.commutes]
    exact (Algebra.commutes r (P q)).symm
  | grade1 i =>
    simp only [rhoA, rhoB, FreeAlgebra.lift_ι_apply]
    exact intertwine_gen q hq i
  | mul a b ha hb =>
    rw [map_mul, map_mul, ← mul_assoc, ha, mul_assoc, hb, mul_assoc]
  | add a b ha hb =>
    rw [map_add, map_add, mul_add, add_mul, ha, hb]

theorem isUnit_det_P (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : IsUnit (P q).det := by
  rw [det_P q hq]
  exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))

/-- **The plain trace is the same on both nucleons, for every element of the algebra.** -/
theorem trace_rhoB_eq_trace_rhoA (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (x : FreeAlgebra R (Fin 4)) : trace (rhoB q x) = trace (rhoA q x) := by
  have hu := isUnit_det_P q hq hq2
  have hB : rhoB q x = P q * (rhoA q x * (P q)⁻¹) := by
    rw [← mul_assoc, intertwine_rho q hq x, mul_assoc, Matrix.mul_nonsing_inv _ hu, mul_one]
  rw [hB, Matrix.trace_mul_comm, mul_assoc, Matrix.nonsing_inv_mul _ hu, mul_one]

/-- Two-term weighted trace on the proton weight space, coupling `c`. -/
noncomputable def tauP (q c : R) (x : FreeAlgebra R (Fin 4)) : R :=
  trace ((Kp q + c • QPairP) * rhoA q x)

/-- Two-term weighted trace on the neutron weight space, coupling `c`. -/
noncomputable def tauN (q c : R) (x : FreeAlgebra R (Fin 4)) : R :=
  trace ((Kn q + c • QPairN) * rhoB q x)

theorem tauP_eq (q c : R) (x : FreeAlgebra R (Fin 4)) :
    tauP q c x = q * trace (rhoA q x) := by
  simp [tauP, Kp, QPairP, Matrix.trace_smul]

theorem tauN_eq (q c : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (x : FreeAlgebra R (Fin 4)) :
    tauN q c x = (q⁻¹ - c / 3) * trace (rhoA q x) := by
  simp only [tauN, Kn, QPairN, smul_smul, ← add_smul, Matrix.smul_mul, Matrix.one_mul,
    Matrix.trace_smul, smul_eq_mul, trace_rhoB_eq_trace_rhoA q hq hq2 x]
  ring

/-- The `n − p` difference of the two-term trace is the common trace times a scalar that does
not depend on the element. -/
theorem tau_diff_eq (q c : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (x : FreeAlgebra R (Fin 4)) :
    tauN q c x - tauP q c x = (q⁻¹ - q - c / 3) * trace (rhoA q x) := by
  rw [tauN_eq q c hq hq2, tauP_eq]
  ring

end Generic

section Archimedean

/-- **Linear energy map: the neutron is lighter, for every element.** If both nucleon masses are
the same positive multiple `S` of the two-term trace of one element, shifted by the same `c₀`,
and the proton trace is positive, then on `q > 1` with `c ≥ 0` the neutron is lighter. -/
theorem linear_mass_neutron_lighter {q c S c₀ : ℝ} (hq1 : 1 < q) (hc : 0 ≤ c) (hS : 0 < S)
    (x : FreeAlgebra ℝ (Fin 4)) (hp : 0 < tauP q c x) :
    S * tauN q c x - c₀ < S * tauP q c x - c₀ := by
  have hq0 : q ≠ 0 := by positivity
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have ht : 0 < trace (rhoA q x) := by
    rw [tauP_eq] at hp
    exact pos_of_mul_pos_right hp (by linarith)
  have hinv : q⁻¹ < q := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  have hd : tauN q c x - tauP q c x < 0 := by
    rw [tau_diff_eq q c hq0 hq2]
    exact mul_neg_of_neg_of_pos (by linarith) ht
  nlinarith

open QOU.QBeta.DecayConjectures in
/-- **C3 cannot be discharged by linear energy conservation on one element.** With the masses of
`linear_mass_neutron_lighter` and `Q_β := m_n − m_p − m_e`, `m_e ≥ 0`, no positive scale `E₀`
and no `ε` make C3 hold. -/
theorem not_decayEnergyScale_of_linear {q c S c₀ mₑ E₀ ε : ℝ} (hq1 : 1 < q) (hc : 0 ≤ c)
    (hS : 0 < S) (hme : 0 ≤ mₑ) (x : FreeAlgebra ℝ (Fin 4)) (hp : 0 < tauP q c x) :
    ¬ DecayEnergyScale E₀ ((S * tauN q c x - c₀) - (S * tauP q c x - c₀) - mₑ) ε := by
  intro h
  have h1 := linear_mass_neutron_lighter (c₀ := c₀) hq1 hc hS x hp
  have h2 := h.qbeta_eq
  have h3 : 0 ≤ |ε| * E₀ := mul_nonneg (abs_nonneg ε) h.scale_pos.le
  linarith

/-- **Gibbs (log) energy map: the split is element-independent.** If `m_N = −E·log τ_N + c₀`,
then `m_n − m_p = E·(2·log q − log(1 − c·q/3))` for every element with positive proton trace. -/
theorem gibbs_mass_split_eq {q c E c₀ : ℝ} (hq1 : 1 < q) (hcq : c * q < 3)
    (x : FreeAlgebra ℝ (Fin 4)) (hp : 0 < tauP q c x) :
    (-E * Real.log (tauN q c x) + c₀) - (-E * Real.log (tauP q c x) + c₀) =
      E * (2 * Real.log q - Real.log (1 - c * q / 3)) := by
  have hq0 : q ≠ 0 := by positivity
  have hqpos : 0 < q := by linarith
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have ht : 0 < trace (rhoA q x) := by
    rw [tauP_eq] at hp
    exact pos_of_mul_pos_right hp hqpos.le
  have hk : 0 < 1 - c * q / 3 := by linarith
  have hN : tauN q c x = q⁻¹ * (1 - c * q / 3) * trace (rhoA q x) := by
    rw [tauN_eq q c hq0 hq2]
    field_simp
  rw [hN, tauP_eq, Real.log_mul (by positivity) ht.ne', Real.log_mul (by positivity) hk.ne',
    Real.log_mul hq0 ht.ne', Real.log_inv]
  ring

/-- The Gibbs split is positive (neutron heavier) on `q > 1`, `0 ≤ c`, `c·q < 3`, `E > 0`. -/
theorem gibbs_mass_split_pos {q c E c₀ : ℝ} (hq1 : 1 < q) (hc : 0 ≤ c) (hcq : c * q < 3)
    (hE : 0 < E) (x : FreeAlgebra ℝ (Fin 4)) (hp : 0 < tauP q c x) :
    0 < (-E * Real.log (tauN q c x) + c₀) - (-E * Real.log (tauP q c x) + c₀) := by
  rw [gibbs_mass_split_eq (E := E) (c₀ := c₀) hq1 hcq x hp]
  have hlq : 0 < Real.log q := Real.log_pos hq1
  have hk : Real.log (1 - c * q / 3) ≤ 0 :=
    Real.log_nonpos (by nlinarith) (by nlinarith)
  have : 0 < 2 * Real.log q - Real.log (1 - c * q / 3) := by linarith
  positivity

end Archimedean

end QOU.QBeta.NucleonSplitSingleElement
