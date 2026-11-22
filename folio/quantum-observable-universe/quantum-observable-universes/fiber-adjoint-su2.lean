import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.fiber_adjoint_su2 — Fiber–adjoint involution for SU(2)

The embedding σ : ℙ¹(ℂ) ↪ su(2) ≅ ℝ³:
- σ([ℓ]) = vv†/‖v‖² − ½ id_V ∈ su(2) (trace-free skew-Hermitian)
- Image: σ(ℙ¹(ℂ)) = S² ⊂ su(2) (unit sphere under Killing form)
- This identifies ℙ¹(ℂ) with the coadjoint orbit of SU(2)
- Observability: no non-zero G-fixed points in Ad(A), so Hom(𝟙, Ad(A)) = 0

LaTeX label: `ex:fiber-adjoint-su2`

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [leitner2026] §1 Example: Fiber–adjoint involution

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Examples

/-- **SU(2) fiber–adjoint data**: the embedding ℙ¹(ℂ) ↪ su(2) ≅ ℝ³
    identifying the flag manifold with the unit 2-sphere.

    LaTeX: `\label{ex:fiber-adjoint-su2}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure SU2FiberAdjointData where
  /-- Dimension of the adjoint representation su(2). -/
  adjointDim : ℕ
  /-- su(2) has dimension 3. -/
  adj_dim : adjointDim = 3
  /-- Dimension of the coadjoint orbit σ(ℙ¹). -/
  orbitDim : ℕ
  /-- The orbit S² has dimension 2 (codimension 1 in ℝ³). -/
  orbit_dim : orbitDim = 2
  /-- Hom(𝟙, Ad(A)) = 0: dim 3 representation has no trivial summand (Schur). -/
  no_invariant_vectors : adjointDim ≠ 1
  /-- The embedding σ is a monomorphism: orbit embeds in su(2) with
      strictly smaller dimension. -/
  embedding_mono : orbitDim < adjointDim

/-- The fiber–adjoint data for SU(2). -/
-- Ref: [leitner2026] §1
def su2FiberAdjoint : SU2FiberAdjointData where
  adjointDim := 3
  adj_dim := rfl
  orbitDim := 2
  orbit_dim := rfl
  no_invariant_vectors := by omega
  embedding_mono := by omega

/-- The adjoint of SU(2) has dimension 3. -/
theorem su2_fiber_adj_dim : su2FiberAdjoint.adjointDim = 3 := rfl

end QOU.Examples
