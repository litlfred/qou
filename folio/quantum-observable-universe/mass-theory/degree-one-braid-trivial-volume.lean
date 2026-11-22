import Mathlib.LinearAlgebra.Span.Basic
import QOU.Photon

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

**Photon (2026-11-20).** The photon is `def:photon`, `QOU.Photon.photon`,
`γ(φ) = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (owner ruling, bean `qou-99qc`). Its
support words are `𝟙, σ₀, σ₁, σ₀σ₁⁻¹`, and the last closes to the unknot, so the
word-level volume statement covers the four-term photon too; the degree-one
element is the named specialisation `φ₀₁ = 0` (photon-usage audit, C10).
`photon_mem_span_support` places the photon in the span of those four words,
and `linearVol_photon_eq_zero` shows that "the volume of the photon by
linearity" is the same vacuous move the obstruction below rules out.

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

open QOU.Photon in
/-- The photon lies in the `R`-span of its four support words
    `𝟙, σ₀, σ₁, σ₀σ₁⁻¹`. -/
theorem photon_mem_span_support {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (σ₀ : A) (σ₁ : Aˣ) (c : Colour R) :
    photon σ₀ σ₁ c ∈ Submodule.span R ({1, σ₀, (σ₁ : A), vertex σ₀ σ₁} : Set A) := by
  unfold photon
  refine Submodule.add_mem _ (Submodule.add_mem _ (Submodule.add_mem _ ?_ ?_) ?_) ?_
  · exact Submodule.subset_span (by simp)
  · exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp))
  · exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp))
  · exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp))

open QOU.Photon in
/-- A linear functional vanishing on the four support words vanishes on every
    photon: a "volume of the photon by linearity" would be zero whatever the
    colour weights, so it carries no information (cf. `no_linear_vol_of_span_top`). -/
-- Ref: [leitner2026] lem:degree-one-braid-trivial-volume; def:photon
theorem linearVol_photon_eq_zero {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (vol : A →ₗ[R] R) (σ₀ : A) (σ₁ : Aˣ)
    (h : ∀ s ∈ ({1, σ₀, (σ₁ : A), vertex σ₀ σ₁} : Set A), vol s = 0) (c : Colour R) :
    vol (photon σ₀ σ₁ c) = 0 :=
  linearVol_eq_zero_of_mem_span vol _ h (photon_mem_span_support σ₀ σ₁ c)

end QOU.Photon
