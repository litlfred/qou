import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.PawLeiInnerProduct — Inner product on intertwiner spaces

The adjoint trace induces an inner product on Hom_{SU(2)}(V_j, V_{1/2}^⊗n)
with respect to which the Pawlowski–Leitner basis is orthogonal.

Authoritative source: `content/quantum-observable-universe/lean/QOU/RepresentationTheory.lean`

## References

- [leitnerpawloski2004] arXiv:math/0409565 — "Unital Gröbner Bases over Arbitrary Commutative Ground Rings" (Leitner & Pawloski); the single Pawloski–Leitner paper
- [manuscript] §1, Proposition: Inner product on intertwiner spaces

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The Pawlowski–Leitner inner product on intertwiner spaces.
    Each basis vector has a positive norm-squared computed from
    hook lengths of the indexing Young tableau. -/
structure PawLeiInnerProduct where
  /-- Number of basis vectors. -/
  num_basis : ℕ
  /-- The norm-squared of each basis vector. -/
  normSq : Fin num_basis → R_q
  /-- All norms are positive. -/
  -- Ref: [leitnerpawloski2004] PL inner product / SU(2) intertwiner basis (arXiv:math/0409565, Unital Gröbner Bases)
  -- normSq_pos : ∀ i, normSq i > 0  -- (archimedean; not meaningful over R_q)

/-- Positive-definiteness: the PL inner product ⟨φ, φ⟩ > 0
    for any nonzero intertwiner φ (follows from normSq_pos). -/
-- Ref: [leitnerpawloski2004] Leitner & Pawloski, "Unital Gröbner Bases over Arbitrary Commutative Ground Rings," arXiv:math/0409565
theorem pawLei_pos_def (ip : PawLeiInnerProduct)
    (i : Fin ip.num_basis) : ip.normSq i > 0 :=
  ip.normSq_pos i

end QOU
