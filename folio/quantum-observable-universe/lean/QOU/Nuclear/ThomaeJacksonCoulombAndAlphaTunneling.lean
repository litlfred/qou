import QCalculus.ThomaeJacksonCalculus
import Mathlib.Data.Real.Sqrt
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Thomae–Jackson Proper-Time Scaling, Mirror Coulomb Pairs, and Gamow–Geiger–Nuttall Tunneling

This module connects discrete Thomae–Jackson `q`-calculus on the proper-time lattice
`τ_j = τ₀ * (q²)^j` to nuclear Coulomb pair counting and heavy-nucleus `α`-decay Gamow
tunneling (§7c generic + `_real` archimedean specialization pattern):

1. **Telescoping Thomae–Jackson `q`-Calculus & `q⁻²` Proper-Time Prefactor:**
   Instantiates forward/backward Fundamental Theorems of `q`-Calculus on `t_k = t₀ * r^k` and
   proves `jackson_bwd_eq_q_inv_sq_mul_fwd`: on `τ_j = τ₀ * (q²)^j`, backward step weights
   satisfy `(1 - (q²)⁻¹) * τ_j = q⁻¹ ^ 2 * ((q² - 1) * τ_j)`, so every backward Jackson sum
   carries the exact horizontal `q⁻²` Hodge diffusion prefactor of `d_q = q⁻¹ d + ...`.
2. **Mirror Pair-Count Identity (`mirror_pair_count_diff`):**
   `(Z + 1) * Z / 2 - Z * (Z - 1) / 2 = Z`, giving `1` unordered proton–proton pair for
   `Z = 1` (`³H`–`³He`).
3. **`α`-Decay Conservation, Coulomb Pair Drop, and Geiger–Nuttall Law:**
   - `alpha_decay_Q_value_identity`: `Q_α = B_daughter + B_α - B_parent` (`B_parent + Q_α = B_daughter + B_α`),
     `(Z - 2) + 2 = Z`, `(A - 4) + 4 = A`, and exact proton-pair release
     `Z * (Z - 1) / 2 - (Z - 2) * (Z - 3) / 2 - 1 = 2 * (Z - 2) = Z_α * Z_daughter`.
   - `geigerNuttallSubbarrier` & `geigerNuttallSubbarrier_real` (`geiger_nuttall_linear_in_inv_sqrt_Q`):
     `2 * G_leading(Z_d, Q) = C_GN * Z_d / √Q - D_GN * √(Z_d * R_touch)` together with strict
     monotonicity `0 < Q₁ < Q₂ → C / √Q₂ < C / √Q₁` (`geiger_nuttall_monotone_in_Q_real`).

Historical credits:
- Johannes Thomae (1869), *Beiträge zur Theorie der durch die Heinesche Reihe darstellbaren Functionen*
- Frank Hilton Jackson (1910), *On q-definite integrals*
- Hans Geiger & John Mitchell Nuttall (1911), *The ranges of the α particles from various radioactive substances and a relation between range and period of transformation*
- George Gamow (1928), *Zur Quantentheorie des Atomkernes*
- Ronald W. Gurney & Edward U. Condon (1928), *Wave mechanics and radioactive disintegration*

-- Ref: [gamow1928]
-/

namespace QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling

open BigOperators
open QOU.MathlibInfra.ThomaeJacksonCalculus

/-! ## 1. Thomae–Jackson Fundamental Theorems and `q⁻²` Proper-Time Scaling -/

section ProperTimeJackson

variable {K : Type*} [Field K]

/-- Telescoping Fundamental Theorems of `q`-Calculus on `geomGrid t0 r k = t0 * r^k` for both
forward step `(r - 1) * t_k` and backward step `(1 - r⁻¹) * t_k`. -/
theorem thomae_jackson_ftc_fwd_and_bwd {t0 r : K} (ht0 : t0 ≠ 0) (hr : r ≠ 0) (hr1 : r ≠ 1)
    (N : ℕ) (F : K → K) :
    qIntegralFwd t0 r N (qDerivFwd r F) = F (t0 * r ^ N) - F t0 ∧
      qIntegralBwd (r * t0) r N (qDerivBwd r F) = F (t0 * r ^ N) - F t0 := by
  exact ⟨qIntegral_fwd_qDeriv_fwd ht0 hr hr1 N F,
    qIntegral_bwd_qDeriv_bwd ht0 hr hr1 N F⟩

/-- **Backward-to-Forward `q⁻²` Proper-Time Lattice Scaling:**
On the proper-time lattice `τ_j = τ₀ * (q²)^j` (`q ≠ 0`), each backward Jackson step weight
equals `q⁻²` times the forward step weight, and every finite backward Thomae–Jackson sum
satisfies `I_bwd = q⁻² * I_fwd`. -/
theorem jackson_bwd_eq_q_inv_sq_mul_fwd (τ0 : K) {q : K} (hq : q ≠ 0) (j N : ℕ)
    (f : K → K) :
    (1 - (q ^ 2)⁻¹) * (τ0 * (q ^ 2) ^ j) =
        q⁻¹ ^ 2 * ((q ^ 2 - 1) * (τ0 * (q ^ 2) ^ j)) ∧
      qIntegralBwd τ0 (q ^ 2) N f = q⁻¹ ^ 2 * qIntegralFwd τ0 (q ^ 2) N f := by
  refine ⟨?_, qIntegral_bwd_qSq_eq_q_inv_sq_mul_fwd τ0 hq N f⟩
  field_simp

end ProperTimeJackson

/-! ## 2. Mirror Coulomb Pair Difference and `α`-Decay Pair Release -/

section NuclearPairAlgebra

variable {K : Type*} [Field K] [CharZero K]

/-- **Mirror Nucleus Proton-Pair Difference:**
`(Z + 1) * Z / 2 - Z * (Z - 1) / 2 = Z` (giving `1` unordered proton–proton pair at `Z = 1`
for the `³H`–`³He` mirror pair). -/
theorem mirror_pair_count_diff (Z : K) :
    (Z + 1) * Z / 2 - Z * (Z - 1) / 2 = Z ∧
      ((1 : K) + 1) * 1 / 2 - (1 : K) * (1 - 1) / 2 = 1 := by
  refine ⟨by ring, by ring⟩

/-- **`α`-Decay `Q`-Value, Nucleon/Charge Conservation, and `2 (Z - 2)` Coulomb Pair Drop:**
In parent `(Z, A) →` daughter `(Z - 2, A - 4) + α (2, 4)`:
1. `Q_α = B_daughter + B_α - B_parent` satisfies `B_parent + Q_α = B_daughter + B_α`,
2. `(Z - 2) + 2 = Z` and `(A - 4) + 4 = A`,
3. Subtracting the internal daughter pairs `(Z - 2)(Z - 3)/2` and internal `⁴He` pair `1` from
   the parent proton pairs `Z(Z - 1)/2` leaves **exact** inter-fragment Coulomb pair count
   `2 * (Z - 2) = Z_α * Z_daughter`. -/
theorem alpha_decay_Q_value_identity (B_parent B_daughter B_alpha Z A : K) :
    let Q_alpha := B_daughter + B_alpha - B_parent
    B_parent + Q_alpha = B_daughter + B_alpha ∧
      (Z - 2) + 2 = Z ∧
      (A - 4) + 4 = A ∧
      Z * (Z - 1) / 2 - (Z - 2) * (Z - 3) / 2 - 1 = 2 * (Z - 2) := by
  refine ⟨by ring, by ring, by ring, by ring⟩

end NuclearPairAlgebra

/-! ## 3. Sub-Barrier Gamow Exponent and Affine Geiger–Nuttall Law (`§7c` Generic + `_real`) -/

section GeigerNuttall

/-- Generic field form of the sub-barrier Gamow–Gurney–Condon WKB exponent `G_leading` in terms
of square-root witnesses `sqrtQ` and `sqrtZR`. -/
def geigerNuttallSubbarrier {K : Type*} [Field K] (C_GN D_GN Z_d sqrtQ sqrtZR : K) : K :=
  (C_GN * Z_d / sqrtQ - D_GN * sqrtZR) / 2

/-- Generic affine Geiger–Nuttall relation over any `[Field K]` (`CharZero K`):
`2 * geigerNuttallSubbarrier = C_GN * Z_d / sqrtQ - D_GN * sqrtZR`. -/
theorem geiger_nuttall_linear_generic {K : Type*} [Field K] [CharZero K]
    (C_GN D_GN Z_d sqrtQ sqrtZR : K) :
    2 * geigerNuttallSubbarrier C_GN D_GN Z_d sqrtQ sqrtZR =
      C_GN * Z_d / sqrtQ - D_GN * sqrtZR := by
  unfold geigerNuttallSubbarrier
  ring

/-- Archimedean `ℝ` specialization `G_leading(Z_d, Q)` using `Real.sqrt Q` and
`Real.sqrt (Z_d * R_touch)` (§7c `_real` pair for `geigerNuttallSubbarrier`). -/
noncomputable def geigerNuttallSubbarrier_real (C_GN D_GN Z_d Q R_touch : ℝ) : ℝ :=
  geigerNuttallSubbarrier C_GN D_GN Z_d (Real.sqrt Q) (Real.sqrt (Z_d * R_touch))

/-- **Affine Geiger–Nuttall Law & Monotonicity in `Q`:**
1. `2 * geigerNuttallSubbarrier_real C_GN D_GN Z_d Q R_touch = C_GN * Z_d / √Q - D_GN * √(Z_d * R_touch)`.
2. For `0 < C` and `0 < Q₁ < Q₂`, `C / √Q₂ < C / √Q₁` (hence larger `Q_α` strictly decreases
   the Gamow barrier integral `2 G`). -/
theorem geiger_nuttall_linear_in_inv_sqrt_Q (C_GN D_GN Z_d Q R_touch : ℝ) :
    2 * geigerNuttallSubbarrier_real C_GN D_GN Z_d Q R_touch =
      C_GN * Z_d / Real.sqrt Q - D_GN * Real.sqrt (Z_d * R_touch) := by
  unfold geigerNuttallSubbarrier_real
  exact geiger_nuttall_linear_generic C_GN D_GN Z_d (Real.sqrt Q) (Real.sqrt (Z_d * R_touch))

theorem geiger_nuttall_monotone_in_Q_real {C Q1 Q2 : ℝ}
    (hC : 0 < C) (hQ1 : 0 < Q1) (hQ12 : Q1 < Q2) :
    C / Real.sqrt Q2 < C / Real.sqrt Q1 := by
  have hQ2 : 0 < Q2 := lt_trans hQ1 hQ12
  have hs1 : 0 < Real.sqrt Q1 := Real.sqrt_pos.mpr hQ1
  have hs2 : 0 < Real.sqrt Q2 := Real.sqrt_pos.mpr hQ2
  have hslt : Real.sqrt Q1 < Real.sqrt Q2 := Real.sqrt_lt_sqrt (le_of_lt hQ1) hQ12
  have hprod_pos : 0 < Real.sqrt Q1 * Real.sqrt Q2 := mul_pos hs1 hs2
  have hdiff_pos : 0 < (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) := by
    have hsimp :
        (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) =
          C * (Real.sqrt Q2 - Real.sqrt Q1) := by
      have hs1_ne : Real.sqrt Q1 ≠ 0 := ne_of_gt hs1
      have hs2_ne : Real.sqrt Q2 ≠ 0 := ne_of_gt hs2
      field_simp
    rw [hsimp]
    exact mul_pos hC (sub_pos.mpr hslt)
  by_contra hle
  push_neg at hle
  have hnonpos : (C / Real.sqrt Q1 - C / Real.sqrt Q2) * (Real.sqrt Q1 * Real.sqrt Q2) ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hle) (le_of_lt hprod_pos)
  linarith

end GeigerNuttall

end QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling
