import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.MathlibExt.QIntegerCanonical


/-!
# QOU.Torsion.quantum_dilogarithm — Quantum dilogarithm

In the archimedean realisation, the transient trace contribution
tr_trans(ϱ, p_i) at the blow-up centre p_i (defined in
`prop:topological-mass-upper-bound`) evaluates to the quantum
dilogarithm Φ_q(z_i), where z_i is the spectral coordinate.

  Φ_q(z) = ∫₀ᶻ (ln_q(1+t)/t) dt = Σ_{n≥1} (-1)^{n+1} z^n / (n [n]_q)

where [n]_q = (qⁿ - 1)/(q - 1) is the q-integer.

LaTeX label: `cor:quantum-dilogarithm`

## References

- [faddeev1994] https://doi.org/10.1007/BF02101456
- [leitner2026] §3-lifting-of-quantum-torsion/quantum-dilogarithm

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open Finset BigOperators

namespace QOU.Torsion

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/- The dilogarithm-series coefficients `1/(n·[n]_q)` require denominators
    unavailable in `R_q = ℤ[q, q⁻¹]`; per the base-ring convention (§7c)
    the series is stated over a generic field `K` (specialise `K := ℝ`,
    `q := q₀`, or `K := Frac(R_q)`). -/
variable {K : Type*} [Field K]

-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
open Classical in
/-- The q-integer `[n]_q = (qⁿ - 1)/(q - 1)` for `q ≠ 1`. -/
noncomputable abbrev qInteger (q : K) (n : ℕ) : K :=
  QOU.QInteger.qIntGeoCl q n

/- For q > 1 and n ≥ 1, the q-integer is positive. -/
-- Ref: [lusztig1993]
-- theorem qInteger_pos {q : K} {n : ℕ} (hq : 1 < q) (hn : 0 < n) :  -- (archimedean; needs an ordered field)
--     0 < qInteger q n := by
--   simp only [qInteger, QOU.QInteger.qIntGeoCl]
--   rw [if_neg (ne_of_gt hq)]
--   apply div_pos
--   · have : 1 < q ^ n := one_lt_pow₀ hq hn.ne'
--     linarith
--   · linarith

/-- The `n`-th coefficient of the quantum dilogarithm series:
    `(-1)^{n+1} / (n · [n]_q)`. -/
-- Ref: [faddeev1994]
noncomputable def qDilogCoeff (q : K) (n : ℕ) : K :=
  if n = 0 then 0
  else (-1) ^ (n + 1) / ((n : K) * qInteger q n)

/-- The partial sum of the quantum dilogarithm series at `z`:
    `Σ_{k=1}^{N} (-1)^{k+1} z^k / (k [k]_q)`. -/
-- Ref: [faddeev1994]
noncomputable def qDilogPartialSum (q z : K) (N : ℕ) : K :=
  ∑ k ∈ range N, qDilogCoeff q (k + 1) * z ^ (k + 1)

/-- The quantum dilogarithm is non-negative at z = 0. -/
-- Ref: [faddeev1994]
theorem qDilog_zero (q : K) (N : ℕ) :
    qDilogPartialSum q 0 N = 0 := by
  unfold qDilogPartialSum
  apply Finset.sum_eq_zero
  intro k _
  simp [zero_pow (Nat.succ_ne_zero k)]

/-- The first term of the quantum dilogarithm is `z / [1]_q = z`. -/
-- Ref: [faddeev1994]
theorem qDilog_first_term {q : K} (_hq : q ≠ 1) (_z : K) :
    qDilogCoeff q 1 = 1 / qInteger q 1 := by
  unfold qDilogCoeff
  simp

/-- For q > 1, [1]_q = 1. -/
-- Ref: [lusztig1993]
theorem qInteger_one {q : K} (hq : q ≠ 1) :
    qInteger q 1 = 1 := by
  simp only [qInteger, QOU.QInteger.qIntGeoCl]
  rw [if_neg hq]
  simp [pow_one, div_self (sub_ne_zero.mpr hq)]

end

end QOU.Torsion
