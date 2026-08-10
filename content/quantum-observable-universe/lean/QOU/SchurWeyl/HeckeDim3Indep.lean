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

Base ring `ℝ` (seminormal rep is archimedean, §7c).
-/

namespace QOU.SchurWeyl

open Hecke Matrix

section Indep

variable (q : ℝ)

local notation3 "t₀" => σ ℝ q q⁻¹ 2 0
local notation3 "t₁" => σ ℝ q q⁻¹ 2 1

theorem sixWords_indep (hq : q ≠ 0)
    (c₁ c₂ c₃ c₄ c₅ c₆ : ℝ)
    (h : c₁ • (1 : Hecke ℝ q q⁻¹ 2) + c₂ • t₀ + c₃ • t₁ + c₄ • (t₀ * t₁)
        + c₅ • (t₁ * t₀) + c₆ • (t₀ * t₁ * t₀) = 0) :
    c₁ = 0 ∧ c₂ = 0 ∧ c₃ = 0 ∧ c₄ = 0 ∧ c₅ = 0 ∧ c₆ = 0 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  -- Apply the trivial and sign representations (algebra homs to ℝ).
  have et := congrArg (rhoTriv ℝ q q⁻¹ 2) h
  have es := congrArg (rhoSign ℝ q q⁻¹ 2) h
  simp only [map_add, map_smul, map_mul, map_one, map_zero, rhoTriv_σ, rhoSign_σ,
    smul_eq_mul] at et es
  -- Apply the (2,1) seminormal representation and read off matrix entries.
  have hm := congrArg (seminormalRep21 q hq) h
  simp only [map_add, map_smul, map_mul, map_one, map_zero, seminormalRep21_σ0,
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
  -- and the `c₃` relation.
  have h36 : c₃ = c₆ - c₄ * (q - q⁻¹) := by linear_combination hC - q⁻¹ * h45
  -- GAP: the final closure `c₁=c₂=c₄=c₆=0` (then `c₃=c₅=0` via `h45`,`h36`) comes from the
  --   two seminormal DIAGONAL entries `m00`,`m11` (coefficients `c00=-1/(q³+q)`, `c11=q³/(q²+1)`)
  --   together with `et` (triv) and `es` (sign): a 4×4 system that clears to a polynomial
  --   identity in `q`.  The explicit `linear_combination` coefficients remain to be computed.
  --   Tracked as bean `qou-pymd` (parent `qou-0h5k`, epic `qou-59vq`).
  -- Ref: [kassel1995] Ch. XII — `dim H_n(q) = n!`.
  sorry

end Indep

end QOU.SchurWeyl
