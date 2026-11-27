import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# Three calibration inputs (conjecture carrier)

`conj:three-calibration-inputs`: every canonical observable `O` of the
framework factors as

  `O = Ô(q₀) · m_e^a · m_π^b`,  `Ô ∈ ℤ[q₀^{±1/2}]`,  `a, b ∈ ℤ`,  `a + b ∈ {0, 1}`,

where `m_e`, `m_π` and `q₀` are the three calibration inputs of
`def:three-calibration-discipline` (`QOU.Observations.CalibrationTriple`).

The class `ThreeCalibrationFactorisation` carries this as its one open field.
No instance exists. The field is content-bearing: for fixed `m_e`, `m_π`,
`q₀` the admissible values form a countable set, so a generic real number is
excluded.

`dimensionless_scale_invariant` is derived, not assumed: an observable with
`a + b = 0` does not change when both mass scales are rescaled by the same
factor.

Until 2026-11-20 this file stated the claim as
`∃ f : ℝ → ℝ → ℝ → ℝ, obs = f q₀ m_e Q_β`, which every `obs` satisfies
(take `f` constant), and it listed `Q_β` rather than `m_π` as the third input
(bean qou-tm3c).

**Ground ring**: `ℝ` (ordering; AGENTS.md §7c). The square root of `q₀` is a
symbol `s` with `s > 0`, `s² = q₀`, not `Real.sqrt` (bean `qou-dk7p`).

## References

- [leitner2026] mass-theory/three-calibration-inputs
-/

namespace QOU.BraidKnot

/-- The realised value of a Laurent polynomial in `q^{1/2}` with integer
    coefficients, written as `s^{-k} · P(s)`, where `s` is the square-root
    symbol (`s² = q₀`). -/
noncomputable def halfLaurentEval (s : ℝ) (k : ℕ) (P : Polynomial ℤ) : ℝ :=
  s⁻¹ ^ k * P.eval₂ (Int.castRingHom ℝ) s

/-- The factorisation formula `Ô(q₀) · m_e^a · m_π^b`, with `s² = q₀`. -/
noncomputable def factorValue (s m_e m_pi : ℝ) (k : ℕ) (P : Polynomial ℤ)
    (a b : ℤ) : ℝ :=
  halfLaurentEval s k P * m_e ^ a * m_pi ^ b

/-- **Conjecture carrier** for `conj:three-calibration-inputs`.
    `Obs` indexes the canonical observables and `value` gives their values. -/
class ThreeCalibrationFactorisation (Obs : Type*) where
  m_e : ℝ
  m_pi : ℝ
  q0 : ℝ
  m_e_pos : 0 < m_e
  m_pi_pos : 0 < m_pi
  one_lt_q0 : 1 < q0
  /-- The square root of `q₀` as a symbol: `s > 0`, `s² = q₀`. -/
  sqrt_q0 : ℝ
  sqrt_q0_pos : 0 < sqrt_q0
  sqrt_q0_sq : sqrt_q0 ^ 2 = q0
  value : Obs → ℝ
  /-- The conjecture: each observable has the factorised form, with
      dimension `a + b ∈ {0, 1}`. -/
  factorises : ∀ O : Obs, ∃ (k : ℕ) (P : Polynomial ℤ) (a b : ℤ),
    (a + b = 0 ∨ a + b = 1) ∧ value O = factorValue sqrt_q0 m_e m_pi k P a b

/-- A dimensionless factorised value (`a + b = 0`) is unchanged when both
    mass scales are rescaled by the same non-zero factor. -/
theorem dimensionless_scale_invariant (s m_e m_pi lam : ℝ) (k : ℕ)
    (P : Polynomial ℤ) (a b : ℤ) (hlam : lam ≠ 0) (hab : a + b = 0) :
    factorValue s (lam * m_e) (lam * m_pi) k P a b
      = factorValue s m_e m_pi k P a b := by
  unfold factorValue
  rw [mul_zpow, mul_zpow]
  have hb : b = -a := by omega
  have : lam ^ a * lam ^ b = 1 := by
    rw [hb, zpow_neg, mul_inv_cancel₀ (zpow_ne_zero a hlam)]
  calc halfLaurentEval s k P * (lam ^ a * m_e ^ a) * (lam ^ b * m_pi ^ b)
      = halfLaurentEval s k P * m_e ^ a * m_pi ^ b * (lam ^ a * lam ^ b) := by ring
    _ = halfLaurentEval s k P * m_e ^ a * m_pi ^ b := by rw [this, mul_one]

end QOU.BraidKnot
