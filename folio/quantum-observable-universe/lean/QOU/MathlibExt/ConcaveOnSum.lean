import Mathlib.Analysis.Convex.Function
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.MathlibExt.ConcaveOnSum — a `Finset`-indexed sum of concave functions is concave

Bean `qou-mlgp` **Gap 3**, second piece.

## The gap

Mathlib has the **binary** results — `ConvexOn.add`, `ConcaveOn.add`,
`StrictConcaveOn.add_concaveOn`, `ConcaveOn.add_strictConcaveOn` — and it has Jensen
(`ConvexOn.map_sum_le`, which is the *different* statement `f (Σ wᵢ xᵢ) ≤ Σ wᵢ f xᵢ`).
It does **not** have the `Finset`-indexed sum of functions. Measured against the pinned
revision (`f897ebcf`): `grep -rn "ConvexOn.sum\|ConcaveOn.sum\|convexOn_sum\|concaveOn_sum"`
over all of `Mathlib` returns **no hits**.

## Why the corpus needs it

The hyperbolic volume of an ideal *triangulation* is a sum over its tetrahedra,

    `Vol(θ) = Σ_{i ∈ tetrahedra} ( Λ(αᵢ) + Λ(βᵢ) + Λ(γᵢ) )`,

and Rivin's theorem is that this is strictly concave on the angle-structure polytope.
`QOU.Knot.RivinConcavitySimplex` supplies the single-tetrahedron factor; the sum lemma
is what turns one tetrahedron into a triangulation.

## The shape the strict version has to take, and why

`StrictConcaveOn.sum_of_mem` asks for **one** strictly concave summand and lets the rest
be merely concave. That asymmetry is forced, not a convenience. Each per-tetrahedron
volume, read as a function of the *whole* polytope, is constant in every other
tetrahedron's angles — so it is concave but never strictly concave there. What rescues
strictness is that a nonzero direction in the polytope must move *some* tetrahedron's
angles, and that one summand is then strictly concave along it.

A symmetric "all summands strictly concave" lemma would be true and useless here.

## Scope

Pure convexity API — no knots, no volume, no `Λ`. Written to be upstreamable unchanged,
at the same generality as the binary lemmas it iterates.
-/

namespace QOU.MathlibExt

open Finset

-- `Module 𝕜 β` rather than the `DistribMulAction 𝕜 β` that the binary `add` lemmas
-- carry: the empty case of the induction is `concaveOn_const`, and that is where
-- Mathlib itself asks for a module.
variable {𝕜 E β ι : Type*} [Semiring 𝕜] [PartialOrder 𝕜] [AddCommMonoid E]
  [AddCommMonoid β] [PartialOrder β] [IsOrderedCancelAddMonoid β]
  [SMul 𝕜 E] [Module 𝕜 β] {s : Set E}

/-- **A `Finset`-indexed sum of concave functions is concave.**

Stated with the hypothesis as an arrow so that `induction t` needs no manual
generalisation — the family hypothesis mentions `t`, so it has to travel with it. -/
theorem ConcaveOn.sum (t : Finset ι) {f : ι → E → β} (hs : Convex 𝕜 s) :
    (∀ i ∈ t, ConcaveOn 𝕜 s (f i)) → ConcaveOn 𝕜 s (fun x => ∑ i ∈ t, f i x) := by
  classical
  induction t using Finset.induction_on with
  | empty => intro _; simpa using concaveOn_const (0 : β) hs
  | @insert a t ha ih =>
      intro h
      simp only [Finset.sum_insert ha]
      exact (h a (Finset.mem_insert_self _ _)).add
        (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

/-- **A `Finset`-indexed sum of convex functions is convex.** The dual of
`ConcaveOn.sum`. -/
theorem ConvexOn.sum (t : Finset ι) {f : ι → E → β} (hs : Convex 𝕜 s) :
    (∀ i ∈ t, ConvexOn 𝕜 s (f i)) → ConvexOn 𝕜 s (fun x => ∑ i ∈ t, f i x) := by
  classical
  induction t using Finset.induction_on with
  | empty => intro _; simpa using convexOn_const (0 : β) hs
  | @insert a t ha ih =>
      intro h
      simp only [Finset.sum_insert ha]
      exact (h a (Finset.mem_insert_self _ _)).add
        (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

/-- **One strictly concave summand makes the whole sum strictly concave**, provided the
others are concave.

This is the form the triangulation argument needs: see the module docstring for why
asking all summands to be strictly concave would be the wrong hypothesis. -/
theorem StrictConcaveOn.sum_of_mem [DecidableEq ι] {t : Finset ι} {f : ι → E → β} {j : ι}
    (hj : j ∈ t) (hs : Convex 𝕜 s) (hjs : StrictConcaveOn 𝕜 s (f j))
    (h : ∀ i ∈ t, i ≠ j → ConcaveOn 𝕜 s (f i)) :
    StrictConcaveOn 𝕜 s (fun x => ∑ i ∈ t, f i x) := by
  have hsplit : ∀ x : E, ∑ i ∈ t, f i x = f j x + ∑ i ∈ t.erase j, f i x := fun x =>
    (Finset.add_sum_erase t (fun i => f i x) hj).symm
  simp only [hsplit]
  exact hjs.add_concaveOn
    (ConcaveOn.sum (t.erase j) hs fun i hi =>
      h i (Finset.mem_of_mem_erase hi) (Finset.ne_of_mem_erase hi))

end QOU.MathlibExt
