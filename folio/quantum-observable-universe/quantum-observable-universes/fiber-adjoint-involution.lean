import QOU.Core.Basic
import QOU.Core.Glossary
import QOU.Core.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans


/-!
# QOU.FiberAdjointInvolution — Fibre–adjoint-fibre involution

The Frobenius self-duality A ≅ A∨ identifies the projective line
object P(V) with a coadjoint orbit inside Ad(A), yielding an
involution σ : P(V) ↪ Ad(A).

## References

- [lusztig1993] Introduction to Quantum Groups
- [leitner2026] §1
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Fibre–adjoint-fibre involution** `σ : P(V) ↪ Ad(A)`.

    The Frobenius self-duality `A ≅ A∨` identifies the projective line
    object `P(V)` with a coadjoint orbit inside `Ad(A)`.  Three parts:

    1. `P(V)` embeds in `Ad(A)` as the coadjoint orbit of a highest-weight
       vector.
    2. The embedding `σ` is an involution: it determines `P(V)` from
       `Ad(A)` and vice versa.
    3. Non-degeneracy of the Frobenius pairing forces the observability
       condition `Hom(𝟙, Ad(A)) = 0`.

    In the archimedean realisation: `σ` is the identification
    `CP¹ ≅ S² ⊂ su(2)` (unit sphere under Killing form).

    LaTeX: `\label{prop:fiber-adjoint-involution}`
    Ref: [lusztig1993] -/
structure FiberAdjointInvolution (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The adjoint bundle object `Ad(A)` in `C`. -/
  adjointObj : C
  /-- The projective line object `P(V)` in `C`. -/
  projLine : C
  /-- **(Part 1)** The orbit embedding `σ : P(V) ↪ Ad(A)`, realising
      `P(V)` as a coadjoint orbit of a highest-weight vector. -/
  orbit_embed : projLine ⟶ adjointObj
  /-- The involution morphism `τ_Ad : Ad(A) ⟶ Ad(A)`, induced by the
      antipode `S : A ⟶ A`. -/
  involution : adjointObj ⟶ adjointObj
  /-- `τ_Ad` is an involution: `τ_Ad ≫ τ_Ad = id`. -/
  involution_sq : involution ≫ involution = 𝟙 adjointObj
  /-- **(Part 2)** The embedding is compatible with the involution:
      restricting `τ_Ad` to the image of `σ` recovers `σ`.
      This means `σ` determines each from the other. -/
  orbit_involution_compat : orbit_embed ≫ involution = orbit_embed
  /-- **(Part 3)** The embedding is a monomorphism: the orbit map
      is injective, so `P(V)` is faithfully represented inside `Ad(A)`. -/
  orbit_mono : ∀ (f g : (𝟙_ C) ⟶ projLine),
    f ≫ orbit_embed = g ≫ orbit_embed → f = g

/-- **Existence of the fibre–adjoint involution, with `τ_Ad` pinned to the antipode.**

    The structure `FiberAdjointInvolution` alone is too weak to carry content:
    with `projLine := A`, `orbit_embed := 𝟙` and `involution := 𝟙` every field
    holds for every datum, even after pinning `adjointObj = fh.obj`.  So the
    conclusion now also pins the involution to the antipode,
    `τ_Ad = S : A ⟶ A` (owner decision 2026-11-27, thread "Prove a non-trivial
    QOU instance exists").  With that pin the identity witness is no longer
    available unless `S = 𝟙`.

    **Witness.**  `P := 𝟙`, `σ := η : 𝟙 ⟶ A`, `τ_Ad := S`.
    * `S ≫ S = 𝟙` is `antipode_involutive`;
    * `η ≫ S = η` is `antipode_unit`, so the orbit is fixed by `τ_Ad`;
    * `σ` is injective on global points exactly when `A` is **faithful** over
      the scalars `End(𝟙)`: `s ≫ η = 0 → s = 0`, i.e. `r · 1_A = 0 → r = 0`.
      This is the one hypothesis `hfaithful` (owner decision 2026-11-27).

    The hypothesis is not derivable from the Frobenius–Hopf axioms and the
    self-duality: over `R = k × k` an algebra supported on one factor has
    `(0,1) · 1_A = 0`.  It is weaker than asking `η` for a left inverse in `C`
    (`fiber_adjoint_involution_exists_of_leftInverse` below), which fails for
    `A = Fun(ℤ/2, 𝔽₂)` in `Rep_{𝔽₂}(ℤ/2)`: every equivariant `A ⟶ 𝟙` is a
    multiple of the Haar sum, which sends `1` to `2 = 0`, yet `A` is faithful.

    What this does not give: the coadjoint-orbit geometry `P(V) ≅ S² ⊂ su(2)`
    of the archimedean picture.  `P := 𝟙` is the orbit of the unit, the
    algebraic shadow of the highest-weight orbit. -/

-- Ref: [lusztig1993] Introduction to Quantum Groups
-- Ref: [leitner2026] prop:fiber-adjoint-involution
theorem fiber_adjoint_involution_exists (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] (fh : FrobeniusHopfData C)
    (hfaithful : ∀ s : 𝟙_ C ⟶ 𝟙_ C, s ≫ fh.unit = 0 → s = 0) :
    ∃ inv : FiberAdjointInvolution C fh, ∃ h : inv.adjointObj = fh.obj,
      inv.involution = CategoryTheory.eqToHom h ≫ fh.antipode ≫ CategoryTheory.eqToHom h.symm := by
  refine ⟨FiberAdjointInvolution.mk (adjointObj := fh.obj) (projLine := 𝟙_ C)
      fh.unit fh.antipode fh.antipode_involutive fh.antipode_unit
      (fun f g hfg => ?_), rfl, ?_⟩
  · have h0 : (f - g) ≫ fh.unit = 0 := by
      rw [CategoryTheory.Preadditive.sub_comp, hfg, sub_self]
    exact sub_eq_zero.mp (hfaithful _ h0)
  · simp

/-- A left inverse `ψ ∘ η = 𝟙` (for instance a Haar-normalised `∫_A`) makes
    `A` faithful, so the involution exists.  Strictly weaker in scope than
    `fiber_adjoint_involution_exists`; see the counterexample there. -/
theorem fiber_adjoint_involution_exists_of_leftInverse (C : Type u)
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C] (fh : FrobeniusHopfData C)
    (hsplit : ∃ ψ : fh.obj ⟶ 𝟙_ C, fh.unit ≫ ψ = 𝟙 (𝟙_ C)) :
    ∃ inv : FiberAdjointInvolution C fh, ∃ h : inv.adjointObj = fh.obj,
      inv.involution = CategoryTheory.eqToHom h ≫ fh.antipode ≫ CategoryTheory.eqToHom h.symm := by
  obtain ⟨ψ, hψ⟩ := hsplit
  refine fiber_adjoint_involution_exists C fh fun s hs => ?_
  calc s = s ≫ fh.unit ≫ ψ := by rw [hψ, CategoryTheory.Category.comp_id]
    _ = 0 := by rw [← CategoryTheory.Category.assoc, hs, CategoryTheory.Limits.zero_comp]

end QOU
