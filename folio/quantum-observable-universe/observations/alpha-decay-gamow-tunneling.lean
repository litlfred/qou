import Mathlib.Data.Real.Sqrt
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.Observations.alpha_decay_gamow_tunneling

Zero-parameter Gamow–Gurney–Condon `α`-decay sub-barrier tunneling, Coulomb pair
release, Mayer–Jensen `N = 126` (`1h_{9/2}² ⊗ 3p_{1/2}⁻²`) pair-projection overlap,
and the exterior `q_local(r) → 1` WKB discriminator (`prop:alpha-decay-gamow-tunneling`).

Follows AGENTS.md §7c: purely algebraic conservation, Coulomb pair-drop, affine
Geiger–Nuttall, and Mayer–Jensen degeneracy identities are proved over a generic
field `K` (`CharZero K`), paired with the archimedean `ℝ` specialisation for
`Real.sqrt` monotonicity and the strict `1 < q₀` sub-barrier inequality.

Historical credits:
- Hans Geiger & John Mitchell Nuttall (1911)
- George Gamow (1928)
- Ronald W. Gurney & Edward U. Condon (1928)
- Maria Goeppert Mayer (1949); Otto Haxel, J. Hans D. Jensen & Hans E. Suess (1949)
- John P. Perdew, Robert G. Parr, Mel Levy & Jose L. Balduz Jr. (1982)

-- Ref: [gamow1928]
-- Ref: [mayer1949]
-/

namespace QOU.Observations

section GenericField

variable {K : Type*} [Field K] [CharZero K]

/-- Generic-field `α`-decay `Q`-value, nucleon conservation, and inter-fragment
Coulomb proton-pair drop `Z(Z-1)/2 - (Z-2)(Z-3)/2 - 1 = 2(Z-2) = Z_α Z_d`. -/
theorem alpha_decay_pair_and_qvalue_generic (B_p B_d B_a Z A : K) :
    let Q_a := B_d + B_a - B_p
    B_p + Q_a = B_d + B_a ∧
      (Z - 2) + 2 = Z ∧
      (A - 4) + 4 = A ∧
      Z * (Z - 1) / 2 - (Z - 2) * (Z - 3) / 2 - 1 = 2 * (Z - 2) := by
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- Mayer–Jensen quenched-BCS `J = 0` proton-neutron pair-projection factor at magic
`N = 126` (`²¹⁰Po`: `π(1h_{9/2})²` with `j_p = 9/2`, `ν(3p_{1/2})⁻²` with `j_n = 1/2`):
`1 / ((2 j_p + 1) * (2 j_n + 1)) = 1 / 20`. -/
def mayerJensenPairOverlap (j_p j_n : K) : K :=
  1 / ((2 * j_p + 1) * (2 * j_n + 1))

theorem mayerJensenPairOverlap_po210_generic :
    mayerJensenPairOverlap ((9 : K) / 2) ((1 : K) / 2) = 1 / 20 := by
  unfold mayerJensenPairOverlap
  norm_num

/-- Generic-field affine Geiger–Nuttall sub-barrier exponent in terms of square-root
witnesses `sqrtQ` and `sqrtZR`. -/
def geigerNuttallExponentGeneric (C_GN D_GN Z_d sqrtQ sqrtZR : K) : K :=
  (C_GN * Z_d / sqrtQ - D_GN * sqrtZR) / 2

theorem two_mul_geigerNuttallExponentGeneric (C_GN D_GN Z_d sqrtQ sqrtZR : K) :
    2 * geigerNuttallExponentGeneric C_GN D_GN Z_d sqrtQ sqrtZR =
      C_GN * Z_d / sqrtQ - D_GN * sqrtZR := by
  unfold geigerNuttallExponentGeneric
  ring

end GenericField

section ArchimedeanReal

/-- Archimedean `ℝ` Geiger–Nuttall sub-barrier exponent `G_GN(Z_d, Q, R_touch)`. -/
noncomputable def alpha_decay_geiger_nuttall_G (C_GN D_GN Z_d Q R_touch : ℝ) : ℝ :=
  geigerNuttallExponentGeneric C_GN D_GN Z_d (Real.sqrt Q) (Real.sqrt (Z_d * R_touch))

/-- **Zero-parameter Gamow–Gurney–Condon `α`-decay theorem (`prop:alpha-decay-gamow-tunneling`):**
1. Inter-fragment Coulomb proton-pair release equals `2(Z - 2)` and Mayer–Jensen
   `1h_{9/2}² ⊗ 3p_{1/2}⁻²` `J = 0` pair overlap equals `1 / 20`.
2. Affine Geiger–Nuttall relation `2 G_GN = C_GN Z_d / √Q - D_GN √(Z_d R_touch)` with
   strict barrier decrease `C / √Q₂ < C / √Q₁` for `0 < C` and `0 < Q₁ < Q₂`.
3. Exterior-vacuum `q_local(r) → 1` discriminator: if `1 < q₀` and `0 < G`, scaling the
   exterior wavenumber by `q₀⁻¹` strictly lowers the Gamow barrier `2 G / q₀ < 2 G`. -/
theorem alpha_decay_gamow_tunneling
    (C_GN D_GN Z Z_d Q1 Q2 R_touch G q0 : ℝ)
    (hC : 0 < C_GN) (hQ1 : 0 < Q1) (hQ12 : Q1 < Q2)
    (hG : 0 < G) (hq0 : 1 < q0) :
    (Z * (Z - 1) / 2 - (Z - 2) * (Z - 3) / 2 - 1 = 2 * (Z - 2) ∧
      mayerJensenPairOverlap ((9 : ℝ) / 2) ((1 : ℝ) / 2) = 1 / 20) ∧
    (2 * alpha_decay_geiger_nuttall_G C_GN D_GN Z_d Q1 R_touch =
        C_GN * Z_d / Real.sqrt Q1 - D_GN * Real.sqrt (Z_d * R_touch) ∧
      C_GN / Real.sqrt Q2 < C_GN / Real.sqrt Q1) ∧
    2 * G / q0 < 2 * G := by
  refine ⟨⟨by ring, mayerJensenPairOverlap_po210_generic⟩, ⟨?_, ?_⟩, ?_⟩
  · unfold alpha_decay_geiger_nuttall_G
    exact two_mul_geigerNuttallExponentGeneric C_GN D_GN Z_d (Real.sqrt Q1) (Real.sqrt (Z_d * R_touch))
  · have hQ2 : 0 < Q2 := lt_trans hQ1 hQ12
    have hs1 : 0 < Real.sqrt Q1 := Real.sqrt_pos.mpr hQ1
    have hs2 : 0 < Real.sqrt Q2 := Real.sqrt_pos.mpr hQ2
    have hslt : Real.sqrt Q1 < Real.sqrt Q2 := Real.sqrt_lt_sqrt (le_of_lt hQ1) hQ12
    have hprod : 0 < Real.sqrt Q1 * Real.sqrt Q2 := mul_pos hs1 hs2
    have hdiff : 0 < (C_GN / Real.sqrt Q1 - C_GN / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) := by
      have hsimp :
          (C_GN / Real.sqrt Q1 - C_GN / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) =
            C_GN * (Real.sqrt Q2 - Real.sqrt Q1) := by
        have hs1_ne : Real.sqrt Q1 ≠ 0 := ne_of_gt hs1
        have hs2_ne : Real.sqrt Q2 ≠ 0 := ne_of_gt hs2
        field_simp
      rw [hsimp]
      exact mul_pos hC (sub_pos.mpr hslt)
    by_contra hle
    push_neg at hle
    have hnonpos :
        (C_GN / Real.sqrt Q1 - C_GN / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hle) (le_of_lt hprod)
    linarith
  · exact div_lt_self (by linarith) hq0

end ArchimedeanReal

end QOU.Observations
