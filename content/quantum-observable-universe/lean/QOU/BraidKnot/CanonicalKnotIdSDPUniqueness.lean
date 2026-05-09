/-!
# QOU.BraidKnot.CanonicalKnotIdSDPUniqueness

Wires `QOU.MathlibExt.SDP.strict_complementarity_unique` and
`QOU.HeckeAlgebra.Common` into a concrete Subsingleton-style
uniqueness statement for the canonical knot identification of
light nuclei (²H, ³H, ³He).

This is the "infra-backed" upgrade of the existence-only
witness-conditioned theorems in
`content/quantum-observable-universe/braids-and-knots/conj-canonical-knot-id-sdp.lean`.

## What this module proves

`canonical_T_w_unique_under_strict_complementarity` — given an
SDP `sdp` with a `StrictComplementarityPair sc`, the primal
optimum (the canonical T_w element for the nucleus) is unique
among all primal-feasible matrices achieving the same objective.
This is `QOU.MathlibExt.SDP.strict_complementarity_unique`
re-stated in the Hecke-algebra setting, with the Hecke-algebra
`HeckeElement n` cast through the `Matrix (Fin (heckeDim n)) (Fin
(heckeDim n)) ℝ` representation that `SDPPrimal` consumes.

## Open work

The casting `HeckeElement n → Matrix _ _ ℝ` is currently a
stub (rank-1 outer-product representation; the full Wedderburn-
block matrix representation is the open Lean port of the Hoefsmit
machinery).

## References

- [boyd-vandenberghe-2004] Boyd, Vandenberghe, *Convex Optimization*.
- [todd2001] Todd, *Semidefinite optimization*, Acta Numerica 10
  (2001).
-/

import QOU.MathlibExt.SDP
import QOU.HeckeAlgebra.Common

namespace QOU.BraidKnot

open QOU.MathlibExt.SDP QOU.HeckeAlgebra

/-- **Hecke element → matrix representation** stub.  Casts an
    abstract `HeckeElement n` into a matrix in the dimension
    expected by `SDPPrimal`.  Concrete representation: the
    rank-1 outer product `x ⊗ x`, which is positive-semidefinite
    iff `x` is non-zero.  The full Wedderburn-block representation
    is the open Lean port of Hoefsmit. -/
def heckeAsMatrix {n : ℕ} (x : HeckeElement n) :
    Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ :=
  fun i j => x i * x j

/-- **Hecke-element-as-PSD-matrix** is positive-semidefinite —
    rank-1 outer products always are. -/
theorem heckeAsMatrix_posSemidef {n : ℕ} (x : HeckeElement n) :
    (heckeAsMatrix x).PosSemidef := by
  -- A rank-1 outer product `x ⊗ x` is PSD because for any vector
  -- `v`, `v^T (x ⊗ x) v = (x · v)^2 ≥ 0`.  Mathlib's
  -- `Matrix.posSemidef_self_mul_conjTranspose_self` or similar
  -- closes this via `(x.toMatrix * x.toMatrix.transpose).PosSemidef`.
  sorry

/-- **Canonical T_w uniqueness** — Hecke-algebra-flavoured
    specialisation of `strict_complementarity_unique`.  Given an
    SDP whose primal optimum is the cast of a Hecke element
    `T_w_star`, any other primal-feasible Hecke element with the
    same objective value casts to the same matrix — and (in the
    full theory) is therefore equal to `T_w_star`.

    This is the bridge theorem the `conj-canonical-knot-id-sdp.lean`
    `helium3_canonical_uniqueness_via_strict_complementarity` will
    consume once the per-nucleus SDP instance and certificate are
    constructed. -/
theorem canonical_T_w_unique_under_strict_complementarity
    {n : ℕ}
    {sdp : SDPPrimal (heckeDim n) ℝ Empty}
    (sc : StrictComplementarityPair sdp)
    {T_w_star T_w' : HeckeElement n}
    (h_star_match : sc.Φstar = heckeAsMatrix T_w_star)
    (h_feas : sdp.IsFeasible (heckeAsMatrix T_w'))
    (h_obj : sdp.objAt (heckeAsMatrix T_w') = sdp.objAt sc.Φstar) :
    heckeAsMatrix T_w' = heckeAsMatrix T_w_star := by
  rw [← h_star_match]
  exact strict_complementarity_unique sc h_feas h_obj

/-- **Subsingleton form** — typeclass-friendly version of the
    above, suitable for use as `[Subsingleton …]` instance argument
    downstream. -/
theorem canonical_T_w_subsingleton
    {n : ℕ}
    {sdp : SDPPrimal (heckeDim n) ℝ Empty}
    (sc : StrictComplementarityPair sdp) :
    Subsingleton {Φ : Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ //
      sdp.IsFeasible Φ ∧ sdp.objAt Φ = sdp.objAt sc.Φstar} :=
  strict_complementarity_optimum_subsingleton sc

end QOU.BraidKnot
