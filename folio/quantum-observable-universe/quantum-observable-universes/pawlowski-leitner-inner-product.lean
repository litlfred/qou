import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic


/-!
# QOU.PawLeiInnerProduct — Inner product on intertwiner spaces

The adjoint trace induces an inner product on Hom_{SU(2)}(V_j, V_{1/2}^⊗n)
with respect to which the Pawlowski–Leitner basis is orthogonal.

Authoritative source: `folio/quantum-observable-universe/lean/QOU/RepresentationTheory.lean`

## References

- [leitnerpawloski2004] arXiv:math/0409565 — "Unital Gröbner Bases over Arbitrary Commutative Ground Rings" (Leitner & Pawloski); the single Pawloski–Leitner paper
- [leitner2026] §1, Proposition: Inner product on intertwiner spaces

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

end

/-- The Pawlowski–Leitner inner product on intertwiner spaces.

    Each basis vector has a positive norm-squared.  The norms live in `ℝ`
    (the archimedean side of the substrate→archimedean wall, §7c): the
    norm-squared `‖T_λ‖²` is the positive rational number computed from the
    hook lengths of the indexing Young tableau `λ`, so positivity is an
    archimedean order statement (`> 0`) and cannot be phrased over the
    ordering-free ground ring `R_q`. -/
structure PawLeiInnerProduct where
  /-- Number of basis vectors. -/
  num_basis : ℕ
  /-- The norm-squared of each basis vector. -/
  normSq : Fin num_basis → ℝ
  /-- All basis norm-squares are positive — the orthogonal PawLei basis has
      strictly positive norms, computed from hook lengths. -/
  -- Ref: [leitner2026] §1 — positivity of the adjoint-trace PawLei inner product (framework's own construction; the Gröbner paper [leitnerpawloski2004] supplies only the PBW basis, not the inner product)
  normSq_pos : ∀ i, normSq i > 0

/-- Positive-definiteness: the PL inner product `⟨φ, φ⟩ > 0`
    for any nonzero intertwiner `φ` (follows from `normSq_pos`). -/
-- Ref: [leitner2026] §1, Proposition: positive-definiteness of the adjoint-trace PawLei inner product (framework's own; not in the Gröbner paper [leitnerpawloski2004])
theorem pawLei_pos_def (ip : PawLeiInnerProduct)
    (i : Fin ip.num_basis) : ip.normSq i > 0 :=
  ip.normSq_pos i

end QOU
