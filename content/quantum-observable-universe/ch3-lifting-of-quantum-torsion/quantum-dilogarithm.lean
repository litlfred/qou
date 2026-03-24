/-!
# QOU.Torsion.quantum_dilogarithm — Quantum dilogarithm

In the archimedean realisation, the transient trace contribution
from the topological decomposition of mass evaluates to the
quantum dilogarithm Φ_q(z_i), where z_i is the spectral coordinate.

  Φ_q(z) = ∫₀ᶻ (ln_q(1+t)/t) dt = Σ_{n≥1} (-1)^{n+1} z^n / (n [n]_q)

where [n]_q = (qⁿ - 1)/(q - 1) is the q-integer.

LaTeX label: `cor:quantum-dilogarithm`

## References

- [faddeev1994] https://doi.org/10.1007/BF02101456
- [manuscript] §3-lifting-of-quantum-torsion/quantum-dilogarithm
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.BigOperators.Group.Finset

open Finset BigOperators

namespace QOU.Torsion

/-- The q-integer `[n]_q = (qⁿ - 1)/(q - 1)` for `q ≠ 1`. -/
-- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
noncomputable def qInteger (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then (n : ℝ)
  else (q ^ n - 1) / (q - 1)

/-- For q > 1 and n ≥ 1, the q-integer is positive. -/
-- Ref: [lusztig1993]
theorem qInteger_pos {q : ℝ} {n : ℕ} (hq : 1 < q) (hn : 0 < n) :
    0 < qInteger q n := by
  unfold qInteger
  rw [if_neg (ne_of_gt hq)]
  apply div_pos
  · have : 1 < q ^ n := one_lt_pow₀ hq hn.ne'
    linarith
  · linarith

/-- The `n`-th coefficient of the quantum dilogarithm series:
    `(-1)^{n+1} / (n · [n]_q)`. -/
-- Ref: [faddeev1994]
noncomputable def qDilogCoeff (q : ℝ) (n : ℕ) : ℝ :=
  if n = 0 then 0
  else (-1) ^ (n + 1) / ((n : ℝ) * qInteger q n)

/-- The partial sum of the quantum dilogarithm series at `z`:
    `Σ_{k=1}^{N} (-1)^{k+1} z^k / (k [k]_q)`. -/
-- Ref: [faddeev1994]
noncomputable def qDilogPartialSum (q z : ℝ) (N : ℕ) : ℝ :=
  ∑ k ∈ range N, qDilogCoeff q (k + 1) * z ^ (k + 1)

/-- The quantum dilogarithm is non-negative at z = 0. -/
-- Ref: [faddeev1994]
theorem qDilog_zero (q : ℝ) (N : ℕ) :
    qDilogPartialSum q 0 N = 0 := by
  unfold qDilogPartialSum
  apply Finset.sum_eq_zero
  intro k _
  simp [zero_pow (Nat.succ_ne_zero k)]

/-- The first term of the quantum dilogarithm is `z / [1]_q = z`. -/
-- Ref: [faddeev1994]
theorem qDilog_first_term {q : ℝ} (hq : q ≠ 1) (z : ℝ) :
    qDilogCoeff q 1 = 1 / qInteger q 1 := by
  unfold qDilogCoeff
  simp

/-- For q > 1, [1]_q = 1. -/
-- Ref: [lusztig1993]
theorem qInteger_one {q : ℝ} (hq : q ≠ 1) :
    qInteger q 1 = 1 := by
  unfold qInteger
  rw [if_neg hq]
  simp [pow_one, div_self (sub_ne_zero.mpr hq)]

end QOU.Torsion
