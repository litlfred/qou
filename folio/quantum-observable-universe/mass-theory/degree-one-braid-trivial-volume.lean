import Mathlib.LinearAlgebra.Span.Basic

/-!
# QOU.Photon — degree-one braid words have trivial volume; volume is not linear

The narrative lemma is word-level: every braid word of crossing length
at most one closes to an unlink, which is non-hyperbolic, so its volume
is `0`.  That is a topological fact about closures and is not encoded
here.

This file encodes the obstruction that forced the restatement
(2026-11-16).  The earlier version added the two cases "by linearity of
the volume map on the Hecke algebra" and carried a structure whose
fields *assumed* an additive `vol` vanishing on each summand, then
summed them — a tautology over hypothesised values.  No such linear
volume exists: a linear map that vanishes on a set vanishes on its
span (`linearVol_eq_zero_of_mem_span`, below).  The six positive
permutation braids span `H_3(q)` and close to non-hyperbolic links, so
a linear map agreeing with `Vol` on them would vanish on all of
`H_3(q)`, including on the figure-eight braid, whose closure has
`Vol(4₁) = 2.0299… ≠ 0`.

Base ring: generic (§7c); nothing archimedean is used.

LaTeX label: `lem:degree-one-braid-trivial-volume`

## References

- [kashaev1997] https://doi.org/10.1023/A:1007364912784 (volume of a
  non-hyperbolic link is zero by convention).
- [leitner2026] mass-theory / degree-one-braid-trivial-volume
-/

namespace QOU.Photon

/-- **A linear functional vanishing on a set vanishes on its span.**

    Applied with `M = H_n(q)`, `S` the positive permutation braids and
    `vol` any linear candidate for the hyperbolic volume, this shows the
    candidate is identically zero on `H_n(q)`; it therefore cannot equal
    `Vol` on a hyperbolic closure such as `4₁`. -/
-- Ref: [leitner2026] lem:degree-one-braid-trivial-volume
theorem linearVol_eq_zero_of_mem_span {R M : Type*} [CommRing R]
    [AddCommGroup M] [Module R M] (vol : M →ₗ[R] R) (S : Set M)
    (h : ∀ s ∈ S, vol s = 0) {x : M} (hx : x ∈ Submodule.span R S) :
    vol x = 0 :=
  LinearMap.mem_ker.mp
    ((Submodule.span_le (p := LinearMap.ker vol)).mpr
      (fun s hs => LinearMap.mem_ker.mpr (h s hs)) hx)

/-- **No linear volume.**  If `S` spans `M`, a linear functional that
    vanishes on `S` cannot take a nonzero value anywhere.  This is the
    contrapositive form used in the narrative: since the figure-eight
    element has nonzero volume, `Vol` is not linear on `H_3(q)`. -/
theorem no_linear_vol_of_span_top {R M : Type*} [CommRing R]
    [AddCommGroup M] [Module R M] (vol : M →ₗ[R] R) (S : Set M)
    (hS : Submodule.span R S = ⊤) (h : ∀ s ∈ S, vol s = 0) (x : M) :
    vol x = 0 :=
  linearVol_eq_zero_of_mem_span vol S h (hS ▸ Submodule.mem_top)

end QOU.Photon
