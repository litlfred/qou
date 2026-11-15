/-
# The Q_β element `Δ_S` is the weak vertex summed over the two crossings

Bean `qou-99qc` (owner card 2026-11-15, "Both, word-level first"). The single-wrap
element of the decay channel is
`Δ_S = (h²/2)·1 − (h/2)(σ₁ + σ₂)`, `h = q − q⁻¹`
(`QOU/QBeta/DeltaSTwoRowCharacterVanishes.lean`). This file proves, for any two
elements `s₁ s₂` of a `K`-algebra:

1. `deltaS_eq_grading_sum`: `Δ_S = −(h·[2]/4)·(J₁ + J₂)`, with `J_i = P₊ − P₋` the
   chirality grading of `s_i` (`OneSidedWeakVertex.grading`). No letter relation is used.
2. `deltaS_eq_weakVertex_sum`: if both `s_i` are Hecke letters, then
   `Δ_S = −(q·h·[2]/4)·(W₁ + W₂)`, with `W_i = oneSidedL q s_i = q⁻¹ J_i`, the
   one-sided flip on the line where `s_i` acts by `q`.

So the corpus's Q_β element is a multiple of the sum of the one-sided flavour flips
over its two crossings.

## Scope

`W_i` is the one-sided-flip ansatz; for `|q| > 1` it is the corpus weak vertex of
`prop:weak-vertex-left-projector` (`LeftLineDefinition.lean`). This file does not say
which functional `ε` should be applied to `Δ_S`, and it does not identify `W_i` with the
physical weak coupling (scope (a)).

Base ring (§7c): generic `[Field K] [Ring A] [Algebra K A]`. No `ℝ`, no `sorry`, no axiom.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.OneSidedWeakVertex

namespace QOU.QuarkState.DeltaSIsWeakVertexSum

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K}

/-- The single-wrap element `Δ_S = (h²/2)·1 − (h/2)(s₁ + s₂)`. -/
noncomputable def deltaS (q : K) (s₁ s₂ : A) : A :=
  ((q - q⁻¹) ^ 2 / 2) • (1 : A) - ((q - q⁻¹) / 2) • (s₁ + s₂)

/-- **`Δ_S` is a multiple of the sum of the two chirality gradings.** -/
theorem deltaS_eq_grading_sum (h2 : (2 : K) ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (s₁ s₂ : A) :
    deltaS q s₁ s₂ =
      (-((q - q⁻¹) * (q + q⁻¹) / 4)) • (grading q s₁ + grading q s₂) := by
  -- J_i = (2/[2]) • (s_i − (h/2)·1)
  have inv : ∀ s : A, grading q s =
      (2 / (q + q⁻¹)) • (s - ((q - q⁻¹) / 2) • (1 : A)) := by
    intro s
    rw [ud_letter_eq_grading h2 hq2, smul_smul, div_mul_div_comm, mul_comm (2 : K),
      div_self (mul_ne_zero hq2 h2), one_smul]
  have hc : -((q - q⁻¹) * (q + q⁻¹) / 4) * (2 / (q + q⁻¹)) = -((q - q⁻¹) / 2) := by
    generalize q - q⁻¹ = t
    generalize q + q⁻¹ = B at hq2 ⊢
    have h4 : (4 : K) ≠ 0 := by
      rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
    field_simp
    ring
  rw [inv s₁, inv s₂, ← smul_add, smul_smul, hc]
  unfold deltaS
  generalize q - q⁻¹ = t
  match_scalars
  all_goals field_simp
  all_goals ring

/-- **`Δ_S` is the weak vertex summed over the two crossings** (both `s_i` letters). -/
theorem deltaS_eq_weakVertex_sum (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    {s₁ s₂ : A} (hs₁ : IsLetter q s₁) (hs₂ : IsLetter q s₂) :
    deltaS q s₁ s₂ =
      (-(q * (q - q⁻¹) * (q + q⁻¹) / 4)) • (oneSidedL q s₁ + oneSidedL q s₂) := by
  rw [deltaS_eq_grading_sum h2 hq2, oneSidedL_eq hq hq2 hs₁, oneSidedL_eq hq hq2 hs₂,
    ← smul_add, smul_smul]
  congr 1
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  linear_combination ((q - q⁻¹) * (q + q⁻¹) / 4) * hqq

end QOU.QuarkState.DeltaSIsWeakVertexSum
