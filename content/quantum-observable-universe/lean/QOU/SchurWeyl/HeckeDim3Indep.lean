import QOU.SchurWeyl.BurnsideSpan
import QOU.SchurWeyl.HeckeDim3

/-!
# QOU.SchurWeyl.HeckeDim3Indep — the six T_w words are linearly independent (SW-7, dim ≥ 6)

Lower bound `dim_ℝ H_3(q) ≥ 6`: the six words `{1,σ₀,σ₁,σ₀σ₁,σ₁σ₀,σ₀σ₁σ₀}` are
linearly independent over `ℝ` (`q ≠ 0`), proved by applying the three irreducible
representations `rhoTriv, rhoSign, seminormalRep21` to a linear relation and
solving the resulting `6×6` system.  Combined with `HeckeDim3.span_sixWords_eq_top`
(dim ≤ 6) this gives `dim H_3(q) = 6` and, since the three reps then jointly
biject, the Wedderburn isomorphism `H_3(q) ≅ ℝ × ℝ × M₂(ℝ)` (R2-inst at n=3).

The solving is factored into a **component core** `sixCoeffs_zero`, whose
hypotheses are the three representation images of `Σ cᵢ wᵢ` being zero.  This is
exactly what is available both from a genuine linear relation `Σ cᵢ wᵢ = 0`
(⇒ `sixWords_indep`) and from `ρ (Σ cᵢ wᵢ) = 0` for the product map
`ρ = (rhoTriv, rhoSign, seminormalRep21)` (⇒ injectivity of `ρ`, used for the
Wedderburn iso).  Factoring avoids re-deriving the `6×6` solve.

Base ring `ℝ` (seminormal rep is archimedean, §7c).
-/

namespace QOU.SchurWeyl

open Hecke Matrix

section Indep

variable (q : ℝ)

local notation3 "t₀" => σ ℝ q q⁻¹ 2 0
local notation3 "t₁" => σ ℝ q q⁻¹ 2 1

/-- **Component core.** Given that the three representations `rhoTriv, rhoSign,
seminormalRep21` each send `c₁·1 + c₂σ₀ + c₃σ₁ + c₄σ₀σ₁ + c₅σ₁σ₀ + c₆σ₀σ₁σ₀`
to zero, all six coefficients vanish (`q ≠ 0`).  This is the `6×6` solve; both the
linear-independence statement and the injectivity of the product representation
reduce to it. -/
theorem sixCoeffs_zero (hq : q ≠ 0)
    (c₁ c₂ c₃ c₄ c₅ c₆ : ℝ)
    (hT : rhoTriv ℝ q q⁻¹ 2
        (c₁ • (1 : Hecke ℝ q q⁻¹ 2) + c₂ • t₀ + c₃ • t₁ + c₄ • (t₀ * t₁)
          + c₅ • (t₁ * t₀) + c₆ • (t₀ * t₁ * t₀)) = 0)
    (hS : rhoSign ℝ q q⁻¹ 2
        (c₁ • (1 : Hecke ℝ q q⁻¹ 2) + c₂ • t₀ + c₃ • t₁ + c₄ • (t₀ * t₁)
          + c₅ • (t₁ * t₀) + c₆ • (t₀ * t₁ * t₀)) = 0)
    (hM : seminormalRep21 q hq
        (c₁ • (1 : Hecke ℝ q q⁻¹ 2) + c₂ • t₀ + c₃ • t₁ + c₄ • (t₀ * t₁)
          + c₅ • (t₁ * t₀) + c₆ • (t₀ * t₁ * t₀)) = 0) :
    c₁ = 0 ∧ c₂ = 0 ∧ c₃ = 0 ∧ c₄ = 0 ∧ c₅ = 0 ∧ c₆ = 0 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  -- Trivial and sign representations (algebra homs to ℝ).
  have et := hT
  have es := hS
  simp only [map_add, map_smul, map_mul, map_one, rhoTriv_σ, rhoSign_σ,
    smul_eq_mul] at et es
  -- The (2,1) seminormal representation: read off matrix entries.
  have hm := hM
  simp only [map_add, map_smul, map_mul, map_one, seminormalRep21_σ0,
    seminormalRep21_σ1] at hm
  have m01 := congrFun (congrFun hm 0) 1
  have m10 := congrFun (congrFun hm 1) 0
  have m00 := congrFun (congrFun hm 0) 0
  have m11 := congrFun (congrFun hm 1) 1
  simp only [S0, S1, Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply,
    Matrix.mul_apply, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.of_apply, Matrix.zero_apply, smul_eq_mul,
    Fin.reduceEq, reduceIte, mul_zero, zero_mul, add_zero, zero_add,
    mul_one] at m01 m10 m00 m11
  -- Clean facts from the off-diagonal `M₂` entries.
  have hqi_ne : q + q⁻¹ ≠ 0 := by
    intro hh
    have h2 : q * q + 1 = 0 := by
      have hc := congrArg (· * q) hh
      simp only [zero_mul, add_mul, inv_mul_cancel₀ hq] at hc; linarith [hc]
    nlinarith [mul_self_nonneg q, h2]
  have hK : (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 ≠ 0 := by positivity
  -- `m10 = K·(c₃ - c₄q⁻¹ + c₅q - c₆) = 0`, so the bracket vanishes.
  have hD : c₃ - c₄ * q⁻¹ + c₅ * q - c₆ = 0 := by
    have hfac : (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2
        * (c₃ - c₄ * q⁻¹ + c₅ * q - c₆) = 0 := by
      linear_combination m10 + c₆ * ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) * hqi
    rcases mul_eq_zero.mp hfac with h | h
    · exact absurd h hK
    · exact h
  -- `m01` with `q·q⁻¹ = 1`.
  have hC : c₃ + c₄ * q - c₅ * q⁻¹ - c₆ = 0 := by linear_combination m01 + c₆ * hqi
  -- Off-diagonals ⇒ `c₄ = c₅`.
  have h45 : c₄ = c₅ := by
    have hfac : (c₄ - c₅) * (q + q⁻¹) = 0 := by linear_combination hC - hD
    rcases mul_eq_zero.mp hfac with h | h
    · linarith [h]
    · exact absurd h hqi_ne
  -- Eliminate `c₅` (= c₄) throughout.
  subst c₅
  have h36 : c₃ = c₆ - c₄ * (q - q⁻¹) := by linear_combination hC
  -- Nonzero denominators / factors.
  have hq3q : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq (by positivity)
  have hnum : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hq21 : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  -- `et - m00` cancels c₁,c₂ (both carry `c₁ + c₂ q`); factor out `q⁴+q²+1 ≠ 0`.
  have hPz : c₃ + q * (c₄ + c₄) + q ^ 2 * c₆ = 0 := by
    have h1 : (q ^ 4 + q ^ 2 + 1) * (c₃ + q * (c₄ + c₄) + q ^ 2 * c₆) = 0 := by
      linear_combination (norm := (field_simp; ring)) (q ^ 3 + q) * et - (q ^ 3 + q) * m00
    exact (mul_eq_zero.mp h1).resolve_left hnum
  -- `es - m11` cancels c₁,c₂ (both carry `c₁ - c₂ q⁻¹`); clear q⁻¹ (×q³(q²+1), hqi).
  have hQz : c₃ * q ^ 2 - q * (c₄ + c₄) + c₆ = 0 := by
    have h1 : (q ^ 4 + q ^ 2 + 1) * (c₃ * q ^ 2 - q * (c₄ + c₄) + c₆) = 0 := by
      linear_combination (norm := (field_simp; ring)) q ^ 3 * (q ^ 2 + 1) * m11 - q ^ 3 * (q ^ 2 + 1) * es
    exact (mul_eq_zero.mp h1).resolve_left hnum
  -- c₃ + c₆ = 0.
  have hS' : c₃ + c₆ = 0 := by
    have hR : (1 + q ^ 2) * (c₃ + c₆) = 0 := by linear_combination hPz + hQz
    exact (mul_eq_zero.mp hR).resolve_left (by positivity)
  -- q⁻¹-free relations, then `c₆·(q²+1)² = 0`.
  have hU : 2 * q * c₄ + c₆ * (q ^ 2 - 1) = 0 := by linear_combination hPz - hS'
  have hTt : c₄ * (q ^ 2 - 1) - 2 * c₆ * q = 0 := by
    linear_combination q * h36 - q * hS' + c₄ * hqi
  have hc6 : c₆ = 0 := by
    have hV : c₆ * (q ^ 2 + 1) ^ 2 = 0 := by
      linear_combination (q ^ 2 - 1) * hU - 2 * q * hTt
    exact (mul_eq_zero.mp hV).resolve_right (by positivity)
  have hc4 : c₄ = 0 := by
    have : 2 * q * c₄ = 0 := by linear_combination hU - (q ^ 2 - 1) * hc6
    have h2q : (2 : ℝ) * q ≠ 0 := by simp [hq]
    exact (mul_eq_zero.mp this).resolve_left h2q
  have hc3 : c₃ = 0 := by linear_combination hS' - hc6
  -- c₁, c₂ from et, es with c₃ = c₄ = c₆ = 0.
  have hc2 : c₂ = 0 := by
    have h2 : c₂ * (q + q⁻¹) = 0 := by
      linear_combination et - es
        - hc3 * (q - -q⁻¹) - hc4 * (q * q - -q⁻¹ * -q⁻¹) - hc4 * (q * q - -q⁻¹ * -q⁻¹)
        - hc6 * (q * q * q - -q⁻¹ * -q⁻¹ * -q⁻¹)
    exact (mul_eq_zero.mp h2).resolve_right hqi_ne
  have hc1 : c₁ = 0 := by
    linear_combination et - hc2 * q - hc3 * q - hc4 * (q * q) - hc4 * (q * q) - hc6 * (q * q * q)
  exact ⟨hc1, hc2, hc3, hc4, hc4, hc6⟩

/-- **The six words `{1,σ₀,σ₁,σ₀σ₁,σ₁σ₀,σ₀σ₁σ₀}` are linearly independent over `ℝ`**
(`q ≠ 0`), so `dim_ℝ H_3(q) ≥ 6`. -/
theorem sixWords_indep (hq : q ≠ 0)
    (c₁ c₂ c₃ c₄ c₅ c₆ : ℝ)
    (h : c₁ • (1 : Hecke ℝ q q⁻¹ 2) + c₂ • t₀ + c₃ • t₁ + c₄ • (t₀ * t₁)
        + c₅ • (t₁ * t₀) + c₆ • (t₀ * t₁ * t₀) = 0) :
    c₁ = 0 ∧ c₂ = 0 ∧ c₃ = 0 ∧ c₄ = 0 ∧ c₅ = 0 ∧ c₆ = 0 :=
  sixCoeffs_zero q hq c₁ c₂ c₃ c₄ c₅ c₆
    (by rw [h, map_zero]) (by rw [h, map_zero]) (by rw [h, map_zero])

end Indep

end QOU.SchurWeyl
