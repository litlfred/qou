import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.ParticleInteractions.parity_regime_selection

Canonical declaration for content block `thm:parity-regime-selection`.

## What is proved

The **sign identity**: if both per-nucleon channel sums are negative,
`a < 0` and `b < 0`, and `N ≥ 1`, then the spectator product
`a^Z · b^(N−1)` has sign `(−1)^(A−1)` with `A = Z + N`. Stated as
`0 < (−1)^(Z+N−1) · (a^Z · b^(N−1))` over any strictly ordered field.

## What is NOT proved here (owner ruling 2026-11-16)

The three Q-value regimes (odd `A ≥ 3`, even `A`, `A = 1`) were
previously carried as class fields and projected back out, so the
"theorem" assumed its own conclusion. They are a per-case dispatch
and are not derived; they now live in the remark
`rem:parity-regime-dispatch`, with no Lean claim.
-/

namespace QOU.ParticleInteractions

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Parity regime selection — sign identity**
    ([`thm:parity-regime-selection`]).

    For `a < 0`, `b < 0` and `N ≥ 1`, the spectator product
    `a^Z · b^(N−1)` has sign `(−1)^(Z+N−1)`, i.e.
    `(−1)^(A−1) · a^Z · b^(N−1) > 0`. -/
theorem parity_regime_selection (a b : R) (ha : a < 0) (hb : b < 0)
    (Z N : ℕ) (hN : 1 ≤ N) :
    0 < (-1 : R) ^ (Z + N - 1) * (a ^ Z * b ^ (N - 1)) := by
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  have hexp : Z + (M + 1) - 1 = Z + M := by omega
  rw [hexp, show M + 1 - 1 = M by omega]
  have ha' : 0 < -a := neg_pos.mpr ha
  have hb' : 0 < -b := neg_pos.mpr hb
  have key : (-1 : R) ^ (Z + M) * (a ^ Z * b ^ M) = (-a) ^ Z * (-b) ^ M := by
    rw [neg_pow a, neg_pow b, pow_add]
    ring
  rw [key]
  positivity

/-- The sign identity in the form `sign(a^Z · b^(N−1)) = (−1)^(A−1)`:
    the product equals `(−1)^(A−1)` times a positive number. -/
theorem parity_regime_selection_sign (a b : R) (ha : a < 0) (hb : b < 0)
    (Z N : ℕ) (hN : 1 ≤ N) :
    ∃ r : R, 0 < r ∧ a ^ Z * b ^ (N - 1) = (-1 : R) ^ (Z + N - 1) * r := by
  refine ⟨(-1 : R) ^ (Z + N - 1) * (a ^ Z * b ^ (N - 1)),
    parity_regime_selection a b ha hb Z N hN, ?_⟩
  rw [← mul_assoc, ← pow_add, ← two_mul, pow_mul]
  simp

/-- **Spectator-amplitude asymmetry numerator is positive for `q > 1`.**
    `a − b = (q² − 1)(3(q² + 1)² − 2q²) / (4q³)`, so this numerator fixes
    `|b| > |a|` (used by `rem:parity-regime-dispatch`). Lemma taken from the
    group-8 batch port (PR #8761), restated over a generic ordered field. -/
theorem spectator_asymmetry_num_pos {q : R} (hq : 1 < q) :
    0 < (q ^ 2 - 1) * (3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hq2 : 1 < q ^ 2 := by nlinarith
  have h1 : 0 < q ^ 2 - 1 := by linarith
  have h2 : 0 < 3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2 := by
    have : 3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2 = 3 * q ^ 4 + 4 * q ^ 2 + 3 := by ring
    rw [this]
    positivity
  exact mul_pos h1 h2

end QOU.ParticleInteractions
