import Mathlib.Analysis.Convex.Deriv
import Mathlib.Analysis.Convex.Function

/-!
# QOU.MathlibExt.StrictConcaveOnSegments — strict concavity, tested one segment at a time

Bean `qou-mlgp` **Gap 3**.

## The gap, stated precisely

Mathlib can prove strict concavity in **one variable** — `strictConcaveOn_of_deriv2_neg`
turns `f'' < 0` on an interval into `StrictConcaveOn ℝ D f`. It has nothing that
promotes that to a set in a higher-dimensional space. Measured against the pinned
revision (`f897ebcf`):

* `grep -rn "StrictConvexOn.*fderiv\|ConvexOn_of_hasFDeriv"` over all of `Mathlib` —
  **no hits**. There is no multi-dimensional convexity-from-second-derivative test.
* `ConvexOn.comp_affineMap` and `ConcaveOn.comp_affineMap` exist; the **strict**
  versions do not.

## Why this is the piece the corpus is actually missing

`QOU.Knot.RivinConcavity` proves `strictConcaveOn_tetVolLine`: the tetrahedron volume
`Λ(α)+Λ(β)+Λ(γ)` is strictly concave **along a line** in the angle simplex. Its own
docstring then says

> strict concavity on a convex set *is* strict concavity along every segment

which is true, and was asserted in prose rather than proved. `strictConcaveOn_of_segments`
below is that sentence as a theorem. Without it the line result cannot be promoted, and
Rivin concavity — hence the variational characterisation of the hyperbolic structure,
hence everything the volume conjecture work stands on — stops at one dimension.

## Why the affine-slice phrasing is not needed

Gap 3 was recorded as wanting "negative-definite Hessian **on the tangent space of an
affine constraint** ⟹ strictly concave on that slice", and that framing suggests
machinery for affine subspaces, tangent spaces and restricted Hessians. It turns out
none of that is required, because the constraint set is already carried by `S`:

*every segment between two points of `S` has its direction in the directions of `S`.*

So a hypothesis quantified over pairs `x, y ∈ S` is *automatically* a hypothesis about
tangent directions only. For an `S` inside the affine slice `{Σθ = π}`, the direction
`y − x` automatically satisfies `Σ(y−x) = 0` — which is exactly the tangency condition
`u + v + w = 0` that `RivinConcavity.cot_quadratic_pos` consumes. The affine structure
never has to be mentioned.

This is worth recording because the survey's framing overstated the cost: the general
lemma is nine lines and needs no geometry.

## Scope

These are statements about `StrictConcaveOn` and nothing else — no knots, no volume, no
`Λ`. They belong upstream, and are written so they could be moved there unchanged.

Archimedean (ℝ), but `strictConcaveOn_of_segments` is stated over an arbitrary real
module.
-/

namespace QOU.MathlibExt

open Set

section Segments

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- **Strict concavity is a segment-wise property.**

If for every pair of distinct points `x, y ∈ S` the one-variable restriction
`t ↦ f (x + t • (y − x))` is strictly concave on `[0,1]`, then `f` is strictly concave
on `S`.

This is the promotion Mathlib lacks: it turns any number of *one-dimensional* strict
concavity facts — each provable by `strictConcaveOn_of_deriv2_neg` — into a single
statement about a set in a space of any dimension.

The proof is the two-point evaluation. The segment hypothesis at `(x, y)`, applied at
the endpoints `0` and `1` of `[0,1]`, gives exactly the defining inequality of
`StrictConcaveOn` after identifying `x + 0•(y−x) = x`, `x + 1•(y−x) = y`, and
`x + b•(y−x) = a•x + b•y` when `a + b = 1`. -/
theorem strictConcaveOn_of_segments {S : Set E} (hS : Convex ℝ S) {f : E → ℝ}
    (h : ∀ x ∈ S, ∀ y ∈ S, x ≠ y →
      StrictConcaveOn ℝ (Icc (0 : ℝ) 1) (fun t : ℝ => f (x + t • (y - x)))) :
    StrictConcaveOn ℝ S f := by
  refine ⟨hS, fun x hx y hy hxy a b ha hb hab => ?_⟩
  have key := (h x hx y hy hxy).2 (left_mem_Icc.mpr zero_le_one)
    (right_mem_Icc.mpr zero_le_one) zero_ne_one ha hb hab
  have e0 : x + (0 : ℝ) • (y - x) = x := by rw [zero_smul, add_zero]
  have e1 : x + (1 : ℝ) • (y - x) = y := by rw [one_smul]; abel
  have hc : a • (0 : ℝ) + b • (1 : ℝ) = b := by
    rw [smul_eq_mul, smul_eq_mul, mul_zero, mul_one, zero_add]
  have e2 : x + (a • (0 : ℝ) + b • (1 : ℝ)) • (y - x) = a • x + b • y := by
    rw [hc, smul_sub, show a = 1 - b by linarith, sub_smul, one_smul]
    abel
  -- `key` still has the restriction as an unapplied lambda, so `rw … at key`
  -- finds nothing to rewrite. Move the endpoint identities onto the *goal* with
  -- `calc` instead and let beta-reduction close the middle step definitionally.
  calc a • f x + b • f y
      = a • f (x + (0 : ℝ) • (y - x)) + b • f (x + (1 : ℝ) • (y - x)) := by
        rw [e0, e1]
    _ < f (x + (a • (0 : ℝ) + b • (1 : ℝ)) • (y - x)) := key
    _ = f (a • x + b • y) := by rw [e2]

end Segments

section Deriv

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- **The second-derivative test, in any dimension.**

`f` is strictly concave on the convex set `S` as soon as, along every segment of `S`,
it is continuous and its second derivative is negative on the open segment.

This is `strictConcaveOn_of_deriv2_neg` lifted out of `ℝ` by `strictConcaveOn_of_segments`.
Note what the hypotheses do *not* mention: no Fréchet derivative, no Hessian as a
bilinear form, no affine subspace. The direction of the segment is `y − x` with both
endpoints in `S`, so the second-derivative hypothesis is only ever asked about
directions tangent to `S` — which is what makes this usable on a constraint set where
the ambient Hessian is *not* negative definite.

That last point is the whole reason the corpus needs it. `Λ″ = −cot` is negative on
`(0, π/2)` and **positive** on `(π/2, π)`, so `Λ(α)+Λ(β)+Λ(γ)` is not concave on the
open cube. It is concave on the slice `α+β+γ = π`, and only there. -/
theorem strictConcaveOn_of_deriv2_neg_along_segments {S : Set E} (hS : Convex ℝ S)
    {f : E → ℝ}
    (hcont : ∀ x ∈ S, ∀ y ∈ S,
      ContinuousOn (fun t : ℝ => f (x + t • (y - x))) (Icc (0 : ℝ) 1))
    (hneg : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → ∀ t ∈ Ioo (0 : ℝ) 1,
      deriv^[2] (fun s : ℝ => f (x + s • (y - x))) t < 0) :
    StrictConcaveOn ℝ S f := by
  refine strictConcaveOn_of_segments hS fun x hx y hy hxy => ?_
  refine strictConcaveOn_of_deriv2_neg (convex_Icc 0 1) (hcont x hx y hy) fun t ht => ?_
  rw [interior_Icc] at ht
  exact hneg x hx y hy hxy t ht

end Deriv

section AffineMap

-- The typeclass block is copied from Mathlib's own `OrderedRing` section of
-- `Analysis/Convex/Function.lean`, where `ConvexOn.comp_affineMap` lives, so this
-- sits at exactly the generality of the non-strict version it completes.
-- (`OrderedSemiring` / `OrderedAddCommMonoid` are deprecated at the pinned rev and
-- no longer resolve as instance binders.)
variable {𝕜 E F β : Type*} [Field 𝕜] [LinearOrder 𝕜] [AddCommGroup E] [AddCommGroup F]
  [AddCommMonoid β] [PartialOrder β] [Module 𝕜 E] [Module 𝕜 F] [SMul 𝕜 β]

/-- **Strict concavity survives precomposition by an *injective* affine map.**

Mathlib has `ConvexOn.comp_affineMap` and `ConcaveOn.comp_affineMap` but not the strict
versions, and injectivity is exactly what the strict versions need: the defining
inequality is quantified over `x ≠ y`, and without injectivity `g x = g y` is possible,
where the strict inequality is false.

Useful for reading a concavity statement off a *parametrisation* of a constraint set —
give the slice `{Σθ = π}` a linear coordinate system and this transports concavity
between the two descriptions. -/
theorem StrictConcaveOn.comp_affineMap {f : F → β} (g : E →ᵃ[𝕜] F)
    (hg : Function.Injective g) {s : Set F} (hf : StrictConcaveOn 𝕜 s f) :
    StrictConcaveOn 𝕜 (g ⁻¹' s) (f ∘ g) := by
  refine ⟨hf.1.affine_preimage _, fun x hx y hy hxy a b ha hb hab => ?_⟩
  have hcomb : (f ∘ g) (a • x + b • y) = f (a • g x + b • g y) := by
    show f (g (a • x + b • y)) = _
    rw [Convex.combo_affine_apply hab]
  rw [hcomb]
  exact hf.2 hx hy (fun hgxy => hxy (hg hgxy)) ha hb hab

end AffineMap

section Restrict

variable {E : Type*} [AddCommGroup E] [Module ℝ E] [NoZeroSMulDivisors ℝ E]

/-- **The converse of `strictConcaveOn_of_segments`**: a strictly concave function
restricts to a strictly concave function on each of its segments.

Together the two say strict concavity on a convex set *is* segment-wise strict
concavity — which is the sentence `QOU.Knot.RivinConcavity` asserts in prose.

The proof is `StrictConcaveOn.comp_affineMap` above applied to `AffineMap.lineMap x y`,
which is injective exactly because `x ≠ y` (`NoZeroSMulDivisors` is what turns that into
injectivity of `t ↦ t • (y − x)`). This is the direction that needs the *strict*
`comp_affineMap`, and hence the reason it is worth having. -/
theorem StrictConcaveOn.restrict_segment {S : Set E} {f : E → ℝ}
    (hf : StrictConcaveOn ℝ S f) {x y : E} (hx : x ∈ S) (hy : y ∈ S) (hxy : x ≠ y) :
    StrictConcaveOn ℝ (Icc (0 : ℝ) 1) (fun t : ℝ => f (x + t • (y - x))) := by
  -- Not `hf.comp_affineMap`: `StrictConcaveOn` is a `def` unfolding to an `And`, so dot
  -- notation resolves against `And` and looks for `And.comp_affineMap`.
  have hcomp := StrictConcaveOn.comp_affineMap (AffineMap.lineMap x y)
    (AffineMap.lineMap_injective ℝ hxy) hf
  have hsub : Icc (0 : ℝ) 1 ⊆ AffineMap.lineMap x y ⁻¹' S := by
    intro t ht
    exact hf.1.lineMap_mem hx hy ht
  have hfun : (f ∘ AffineMap.lineMap x y) = fun t : ℝ => f (x + t • (y - x)) := by
    funext t
    simp only [Function.comp_apply, AffineMap.lineMap_apply_module']
    rw [add_comm]
  rw [hfun] at hcomp
  exact hcomp.subset hsub (convex_Icc 0 1)

end Restrict

end QOU.MathlibExt
