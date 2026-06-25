import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
# Ground Ring: ℤ[q, q⁻¹]

All formal proofs in the Descartes universe are conducted over the
Laurent polynomial ring `ℤ[q, q⁻¹]`.  This is an integral domain
with no zero divisors.  Results do NOT require ℝ.

**Note to reader**: all Lean proofs in this module work exclusively
over `ℤ[q, q⁻¹]`.  Numerical evaluations at the substrate parameter
`q₀ ≈ 1.1098` appear only in Chapter 7 (Physical Observations) and
are NOT part of the formal chain.

## References

- [lusztig1993] G. Lusztig, *Introduction to quantum groups*, 1993.
-/

namespace QOU.Archimedean

/-! ## §1  The Laurent polynomial ring -/

/-- The ground ring for QOU formal proofs.
    `R_q := ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).

    In Lean 4 / Mathlib, this is `LaurentPolynomial ℤ`.
    We use `q` as the indeterminate. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The indeterminate `q` in `ℤ[q, q⁻¹]`. -/
noncomputable def q : R_q := LaurentPolynomial.T 1

/-- The inverse `q⁻¹` in `ℤ[q, q⁻¹]`. -/
noncomputable def q_inv : R_q := LaurentPolynomial.T (-1)

/-- `q · q⁻¹ = 1` in `ℤ[q, q⁻¹]`. -/
-- Ref: [lusztig1993]
theorem q_mul_q_inv : q * q_inv = 1 := by
  unfold q q_inv
  rw [← LaurentPolynomial.T_add]
  simp

/-! ## §2  Quantum integers -/

/-- The quantum integer `[n]_q = (qⁿ − q⁻ⁿ) / (q − q⁻¹)` as an
    element of `ℤ[q, q⁻¹]`.  For `n ≥ 0`, this is a polynomial
    in `q` and `q⁻¹` (the denominator divides the numerator). -/
noncomputable def qInt (n : ℤ) : R_q :=
  -- [n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}
  -- = Σ_{k=0}^{|n|-1} q^{n-1-2k}
  if n = 0 then 0
  else if n > 0 then
    (Finset.range n.toNat).sum fun k =>
      LaurentPolynomial.T (n - 1 - 2 * ↑k)
  else
    -((Finset.range (-n).toNat).sum fun k =>
      LaurentPolynomial.T (-n - 1 - 2 * ↑k))

/-- `[1]_q = 1`. -/
theorem qInt_one : qInt 1 = 1 := by
  unfold qInt
  simp

/-- `[2]_q = q + q⁻¹`. -/
theorem qInt_two : qInt 2 = q + q_inv := by
  unfold qInt q q_inv
  simp [Finset.sum_range_succ]

/-! ## §3  The Hecke amplitude and quantum Planck constant -/

/-- The Hecke amplitude `HA = q − q⁻¹`.  This is the coefficient
    in the Hecke relation `σ² = HA · σ + 1`. -/
noncomputable def HA : R_q := q - q_inv

/-- The quantum Planck constant `ℏ_q = (q − 1)/q = 1 − q⁻¹`.
    This is the action quantum per exceptional divisor step. -/
noncomputable def hbar_q : R_q := 1 - q_inv

/-- The crossing energy `E_cross = ½(q − q⁻¹)`.

    **Note**: the factor ½ takes us outside ℤ[q, q⁻¹] into
    ℤ[½][q, q⁻¹].  For formal proofs we work with `2 · E_cross = HA`
    to stay in the ground ring.  The ½ is a presentation convenience. -/
noncomputable def two_E_cross : R_q := HA

/-- `2 · E_cross = q − q⁻¹ = HA`. -/
theorem two_E_cross_eq_HA : two_E_cross = HA := rfl

/-- Build a Laurent polynomial from a list of `(exponent, coefficient)`
    pairs: `Σᵢ cᵢ · T^{kᵢ}`.  Folding over a flat `List (ℤ × ℤ)` lets Lean
    elaborate the `•`/`+` operations **once** (in the fold body) instead of
    building a deep `HAdd`/`HSMul` expression tree per definition — the latter
    does not finish elaborating within practical time/heartbeat budgets for
    these hecke-engine witness polynomials.

    Shared helper for the `QOU.Archimedean.PauliWitness` modules; centralised
    here from the previously per-file `private` copies. -/
noncomputable def ofPairs (l : List (ℤ × ℤ)) : LaurentPolynomial ℤ :=
  l.foldl (fun acc p => acc + p.2 • LaurentPolynomial.T p.1) 0

end QOU.Archimedean
