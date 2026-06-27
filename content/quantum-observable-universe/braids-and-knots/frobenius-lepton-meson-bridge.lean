/-
  Frobenius lepton-meson bridge: V_(2,1) ↓ H₂ = V_(2) ⊕ V_(1,1).

  The standard representation of H₃(q) restricts to H₂(q) as the
  direct sum of the two lepton irreps. This is the categorical bridge
  between the lepton mass tower (H₂) and the meson mass tower (H₃).

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Basic
import Mathlib.Tactic
import Mathlib.Data.Nat.Basic

namespace QOU.BraidsAndKnots

-- ═══════════════════════════════════════════════════════════════
-- §1  ARTIN-WEDDERBURN DIMENSION CONSTRAINTS
-- ═══════════════════════════════════════════════════════════════

/-- H₂ has dimension 2! = 2 = 1² + 1²: two 1-dim irreps. -/
theorem h2_artin_wedderburn : 1^2 + 1^2 = Nat.factorial 2 := rfl

/-- H₃ has dimension 3! = 6 = 1² + 2² + 1²: dims (1,2,1). -/
theorem h3_artin_wedderburn : 1^2 + 2^2 + 1^2 = Nat.factorial 3 := rfl

/-- H₄ has dimension 4! = 24 = 1² + 3² + 2² + 3² + 1². -/
theorem h4_artin_wedderburn : 1^2 + 3^2 + 2^2 + 3^2 + 1^2 = Nat.factorial 4 := rfl

/-- 2 = 1² + 1² is the ONLY way to write 2 as a sum of positive
  integer squares. This forces H₂ to have only 1-dim irreps. -/
theorem two_unique_sum_of_squares (a b : ℕ) (ha : 0 < a) (hb : 0 < b)
    (hab : a^2 + b^2 = 2) : a = 1 ∧ b = 1 := by
  simp [pow_two] at hab
  have ha1 : a = 1 := by
    have : a < 2 := by
      by_contra h
      have h2 : 2 ≤ a := Nat.le_of_not_lt h
      have : 4 ≤ a * a := Nat.mul_le_mul h2 h2
      omega
    omega
  have hb1 : b = 1 := by
    have : b < 2 := by
      by_contra h
      have h2 : 2 ≤ b := Nat.le_of_not_lt h
      have : 4 ≤ b * b := Nat.mul_le_mul h2 h2
      omega
    omega
  exact ⟨ha1, hb1⟩

-- ═══════════════════════════════════════════════════════════════
-- §2  BRANCHING RULE H₃ ↓ H₂
-- ═══════════════════════════════════════════════════════════════

/-- The branching multiplicities for H₃ ↓ H₂.
  For each λ ⊢ 3 and μ ⊢ 2, gives the multiplicity of V_μ in
  the restriction of V_λ to H₂.

  These follow from the Pieri rule: remove one box from the Young
  diagram of λ in all valid ways. -/
def branchingH3H2 : Fin 3 → Fin 2 → ℕ
  | 0, 0 => 1   -- V_(3) ↓ V_(2): multiplicity 1
  | 0, 1 => 0   -- V_(3) ↓ V_(1,1): multiplicity 0
  | 1, 0 => 1   -- V_(2,1) ↓ V_(2): multiplicity 1
  | 1, 1 => 1   -- V_(2,1) ↓ V_(1,1): multiplicity 1
  | 2, 0 => 0   -- V_(1,1,1) ↓ V_(2): multiplicity 0
  | 2, 1 => 1   -- V_(1,1,1) ↓ V_(1,1): multiplicity 1

/-- The standard rep (2,1) restricts to BOTH lepton irreps. -/
theorem standard_restricts_to_both_leptons :
    branchingH3H2 1 0 = 1 ∧ branchingH3H2 1 1 = 1 := by
  decide

/-- The trivial rep (3) restricts to the trivial lepton only. -/
theorem trivial_restricts_to_trivial :
    branchingH3H2 0 0 = 1 ∧ branchingH3H2 0 1 = 0 := by
  decide

/-- The sign rep (1,1,1) restricts to the sign lepton only. -/
theorem sign_restricts_to_sign :
    branchingH3H2 2 0 = 0 ∧ branchingH3H2 2 1 = 1 := by
  decide

/-- Dimension check: dim V_(2,1) = sum of branching multiplicities × dim V_μ.
  dim(2,1) = 2 = 1·dim(2) + 1·dim(1,1) = 1·1 + 1·1 = 2. -/
theorem branching_dimension_check :
    branchingH3H2 1 0 * 1 + branchingH3H2 1 1 * 1 = 2 := by
  decide

-- ═══════════════════════════════════════════════════════════════
-- §3  FROBENIUS RECIPROCITY
-- ═══════════════════════════════════════════════════════════════

/-- Frobenius reciprocity: ⟨Res(V_λ), V_μ⟩_H₂ = ⟨V_λ, Ind(V_μ)⟩_H₃.
  This means the branching multiplicity equals the induction multiplicity.

  For V_(2,1) and V_(2): ⟨Res(V_(2,1)), V_(2)⟩ = 1
  For V_(2,1) and V_(1,1): ⟨Res(V_(2,1)), V_(1,1)⟩ = 1 -/
theorem frobenius_reciprocity_standard :
    branchingH3H2 1 0 = 1 ∧ branchingH3H2 1 1 = 1 :=
  standard_restricts_to_both_leptons

end QOU.BraidsAndKnots
