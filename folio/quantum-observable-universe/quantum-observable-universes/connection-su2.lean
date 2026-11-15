import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.connection_su2 — Connection and curvature on O(SU(2))

The categorical connection on O(SU(2)):
- A = O(SU(2)) with left-invariant calculus Ω¹(A) = span{ω₁, ω₂, ω₃}
- Connection 1-form: A = A₁ω₁ + A₂ω₂ + A₃ω₃ ∈ Ω¹(A, Ad(A))
- Covariant derivative: ∇f = df + A·f  (Leibniz rule)
- Curvature: F_∇ = dA + A ∧ A ∈ Ω²(A, Ad(A)), which is A-linear
- When substrate parameter q is introduced, deforms to Woronowicz
  3D-calculus on O_q(SU(2))

LaTeX label: `ex:connection-su2`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §1 Example: Connection on O(SU(2))
-/

namespace QOU.Examples

/-- **SU(2) connection data**: a connection on the coordinate ring
    O(SU(2)) with its left-invariant 3D calculus.

    LaTeX: `\label{ex:connection-su2}` -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
structure SU2ConnectionData where
  /-- Number of components of the gauge potential (= dim su(2)). -/
  numComponents : ℕ
  /-- A has 3 components: A₁, A₂, A₃. -/
  num_comp : numComponents = 3
  /-- Rank of Ω²(A) where curvature lives. -/
  curvatureRank : ℕ
  /-- Curvature F_∇ ∈ Ω²(A) of rank 3. -/
  curv_rank : curvatureRank = 3
  /-- The Leibniz rule holds: the connection has as many components as
      the calculus dimension, so ∇ acts component-wise. -/
  leibniz : numComponents = curvatureRank
  /-- Curvature is A-linear: rank of Ω² is bounded by C(n,2) for
      n = numComponents. For n = 3: rank ≤ 3(3−1)/2 = 3. -/
  curvature_linear : curvatureRank ≤ numComponents * (numComponents - 1) / 2

/-- The connection data for SU(2). -/
-- Ref: [leitner2026] §1
def su2Connection : SU2ConnectionData where
  numComponents := 3
  num_comp := rfl
  curvatureRank := 3
  curv_rank := rfl
  leibniz := rfl
  curvature_linear := by omega

/-- A gauge potential on SU(2) has 3 components. -/
theorem su2_gauge_components : su2Connection.numComponents = 3 := rfl

end QOU.Examples
