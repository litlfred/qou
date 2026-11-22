import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.PhotonWeightsForced

/-!
# `1, V, V²` are linearly independent on the proton weight space, for every `q ≠ 0`

Bean `qou-99qc`. Owner 2026-11-22: "Try independence first".

`QOU.PhotonWeightsForced.vOnly_factorisation_forced` takes the linear independence of
`1, V, V²` as a hypothesis. Here it is discharged on the proton `(2,1)` weight space, where
`V = σ₀σ₁⁻¹` is `borromeanVA q`. Three matrix entries suffice: `(0,0)`, `(0,1)` and `(1,0)`.
Their coefficient matrix is triangular with determinant `1`, so the only hypothesis is `q ≠ 0`.

Consequence (`borromeanVA_photon_weights_forced`): on the proton weight space, a factorisation
`V³ = (c + eV)(d + fV)` forces `cd = 1`, and for norm-1 photons `{e, f} = {qh, −q⁻¹h}`, with no
hypothesis beyond `q ≠ 0`.
-/

namespace QOU.BraidsAndKnots.PhotonWeightsForcedProton

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.PhotonWeightsForced

variable {R : Type*} [Field R]

/-- **`1, V, V²` are linearly independent on the proton weight space.** -/
theorem linearIndependent_one_V_Vsq (q : R) (hq : q ≠ 0) :
    LinearIndependent R ![(1 : Matrix (Fin 3) (Fin 3) R), borromeanVA q,
      borromeanVA q * borromeanVA q] := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  have e00 := congrFun (congrFun hg 0) 0
  have e01 := congrFun (congrFun hg 0) 1
  have e10 := congrFun (congrFun hg 1) 0
  simp [Fin.sum_univ_three, borromeanVA, A₁, A₂Inv] at e00 e01 e10
  field_simp at e00 e01 e10
  have h2 : g 2 = 0 := by
    rcases e10 with h | h
    · exact h
    · exact absurd h hq
  rw [h2] at e01 e00
  have h1 : g 1 = 0 := by
    simp at e01
    rcases e01 with h | h
    · exact absurd h hq
    · exact h
  rw [h1] at e00
  have h0 : g 0 = 0 := by simpa using e00
  intro i; fin_cases i <;> simp [h0, h1, h2]

/-- **The V-only factorisation of the proton `V³` is forced, for every `q ≠ 0`.** -/
theorem borromeanVA_photon_weights_forced (q : R) (hq : q ≠ 0) (c d e f : R)
    (hprod : (c • (1 : Matrix (Fin 3) (Fin 3) R) + e • borromeanVA q) *
        (d • (1 : Matrix (Fin 3) (Fin 3) R) + f • borromeanVA q) = borromeanV3A q) :
    c * d = 1 ∧
      (c = 1 → d = 1 →
        ((e = q * (q - q⁻¹) ∧ f = -q⁻¹ * (q - q⁻¹)) ∨
          (e = -q⁻¹ * (q - q⁻¹) ∧ f = q * (q - q⁻¹)))) := by
  have hcube : borromeanVA q * borromeanVA q * borromeanVA q =
      (1 : Matrix (Fin 3) (Fin 3) R) + (q - q⁻¹) ^ 2 • borromeanVA q +
        (-(q - q⁻¹) ^ 2) • (borromeanVA q * borromeanVA q) := by
    have := borromeanV3A_eq_one_add_h_sq_V_sub_V_sq q hq
    rw [borromeanV3A] at this
    rw [this, neg_smul, sub_eq_add_neg]
  exact vOnly_factorisation_forced (borromeanVA q) q hq
    (linearIndependent_one_V_Vsq q hq) hcube c d e f (by rw [hprod]; rfl)

end QOU.BraidsAndKnots.PhotonWeightsForcedProton
