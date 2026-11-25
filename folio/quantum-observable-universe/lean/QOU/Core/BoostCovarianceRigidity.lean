import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity

/-!
# Boost covariance of a traced Dirac square is rigid in `q` (bean `qou-2k68`, route 2b)

Write the two-rate Dirac operator as `D = Ω_H • ∇ + Ω_R • ι` (horizontal and Reeb components),
and its traced square as

    Q(Ω_R, Ω_H) = A Ω_R² + B Ω_R Ω_H + C Ω_H²,   A = τ(ι²), B = τ(∇ι + ι∇), C = τ(∇²).

`QOU.Core.AffineCausalityCone` fixes the boost-invariant form on the contact affine chart:
`coneForm c Ω_R Ω_H = c² Ω_R² - Ω_H²`, with `c = c_q = 1/(q - 1)`. "The traced Lagrangian is
boost-covariant" is the statement `Q = k · coneForm c_q` for some scalar `k`.

* `covariant_iff`: `Q = k · coneForm c` for all arguments iff `B = 0`, `C = -k` and `A = k c²`.
  Eliminating `k`, this is `B = 0` and `A = -c² C`.
* `covariant_at_two_speeds_trivial`: if the traces `A, B, C` do not depend on `q`, covariance at
  two cone speeds `c₁² ≠ c₂²` forces `A = C = 0`. A non-degenerate, `q`-independent Dirac datum is
  boost-covariant for at most one value of `c_q`, i.e. at most one `q > 1`.

Consequence, recorded in `qou-2k68`: for the corpus's concrete Dirac operator `substrateDirac`
(`ChenMultiplicativeIntegralBridge.lean`), whose data `Ω, M, N` do not depend on `q`, imposing
covariance at `q₀` would determine `q₀` from substrate data. The owner ruling of 2026-08-02
forbids that. So route 2b needs a Dirac datum whose traces scale with `q` as
`A/C = -1/(q - 1)²`; this file does not construct one.
-/

namespace QOU.Core.BoostCovarianceRigidity

variable {K : Type*} [Field K]

/-- The traced Dirac square as a binary quadratic form. -/
def tracedSq (A B C ΩR ΩH : K) : K := A * ΩR ^ 2 + B * ΩR * ΩH + C * ΩH ^ 2

/-- **Covariance criterion.** `tracedSq A B C = k · (c² Ω_R² - Ω_H²)` for all arguments iff
`B = 0`, `C = -k` and `A = k c²`. -/
theorem covariant_iff (A B C k c : K) :
    (∀ ΩR ΩH : K, tracedSq A B C ΩR ΩH = k * (c ^ 2 * ΩR ^ 2 - ΩH ^ 2)) ↔
      (B = 0 ∧ C = -k ∧ A = k * c ^ 2) := by
  constructor
  · intro h
    have h10 := h 1 0
    have h01 := h 0 1
    have h11 := h 1 1
    simp only [tracedSq] at h10 h01 h11
    refine ⟨?_, ?_, ?_⟩
    · linear_combination h11 - h10 - h01
    · linear_combination h01
    · linear_combination h10
  · rintro ⟨hB, hC, hA⟩ ΩR ΩH
    simp only [tracedSq, hA, hB, hC]
    ring

/-- Eliminating `k`: covariance means `B = 0` and `A = -c² C`. -/
theorem covariant_iff' (A B C c : K) :
    (∃ k : K, ∀ ΩR ΩH : K, tracedSq A B C ΩR ΩH = k * (c ^ 2 * ΩR ^ 2 - ΩH ^ 2)) ↔
      (B = 0 ∧ A = -(c ^ 2) * C) := by
  constructor
  · rintro ⟨k, hk⟩
    obtain ⟨hB, hC, hA⟩ := (covariant_iff A B C k c).mp hk
    exact ⟨hB, by rw [hA, hC]; ring⟩
  · rintro ⟨hB, hA⟩
    refine ⟨-C, (covariant_iff A B C (-C) c).mpr ⟨hB, by ring, by rw [hA]; ring⟩⟩

/-- **Rigidity.** If `q`-independent traces are boost-covariant at two cone speeds with
`c₁² ≠ c₂²`, then `A = C = 0`: the datum is degenerate. -/
theorem covariant_at_two_speeds_trivial {A B C c₁ c₂ : K} (hc : c₁ ^ 2 ≠ c₂ ^ 2)
    (h₁ : ∃ k : K, ∀ ΩR ΩH : K, tracedSq A B C ΩR ΩH = k * (c₁ ^ 2 * ΩR ^ 2 - ΩH ^ 2))
    (h₂ : ∃ k : K, ∀ ΩR ΩH : K, tracedSq A B C ΩR ΩH = k * (c₂ ^ 2 * ΩR ^ 2 - ΩH ^ 2)) :
    A = 0 ∧ C = 0 := by
  obtain ⟨-, hA₁⟩ := (covariant_iff' A B C c₁).mp h₁
  obtain ⟨-, hA₂⟩ := (covariant_iff' A B C c₂).mp h₂
  have hC : (c₁ ^ 2 - c₂ ^ 2) * C = 0 := by linear_combination hA₁ - hA₂
  have hC0 : C = 0 := by
    rcases mul_eq_zero.mp hC with h | h
    · exact absurd (sub_eq_zero.mp h) hc
    · exact h
  exact ⟨by rw [hA₁, hC0]; ring, hC0⟩

/-- For the categorical cone speed `c_q = 1/(q - 1)`, distinct `q₁, q₂ > 1` give `c₁² ≠ c₂²`.
Stated over an ordered field. -/
theorem lightconeSpeed_sq_injective {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]
    {q₁ q₂ : L} (h₁ : 1 < q₁) (h₂ : 1 < q₂) (hne : q₁ ≠ q₂) :
    (1 / (q₁ - 1)) ^ 2 ≠ (1 / (q₂ - 1)) ^ 2 := by
  have p₁ : 0 < q₁ - 1 := sub_pos.mpr h₁
  have p₂ : 0 < q₂ - 1 := sub_pos.mpr h₂
  intro h
  have hpos₁ : 0 < 1 / (q₁ - 1) := by positivity
  have hpos₂ : 0 < 1 / (q₂ - 1) := by positivity
  have heq : 1 / (q₁ - 1) = 1 / (q₂ - 1) := by
    have := (sq_eq_sq₀ hpos₁.le hpos₂.le).mp h
    exact this
  apply hne
  have : q₁ - 1 = q₂ - 1 := by
    have := congrArg (fun x => 1 / x) heq
    simpa [one_div, inv_inv] using this
  linarith

end QOU.Core.BoostCovarianceRigidity
