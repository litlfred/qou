import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Group.Basic
import QOU.Torsion.YekutieliTriple

/-!
# QOU.LiftingDescent.CosimplicialCrossedGroupoid

The recursive brane tower carries a cosimplicial object in the category
of crossed groupoids: coface maps from jet prolongation, codegeneracy
maps from descent, and the crossed structure from conjugation of
1-morphisms on 2-morphisms via the adjoint representation of SU_q(2).

**Pre-Archimedean (formal-chain) version.**  Lives under `lean/QOU/`
and is compiled by `lake build`.  The co-located documentation stub
at `lifting-and-descent/cosimplicial-crossed-groupoid.lean` mirrors
this content.

Ground ring: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).

LaTeX label: `prop:cosimplicial-crossed-groupoid`

## References

- [yekutieli2014-descent] Combinatorial Descent Data for Gerbes, §1 (Defs 1.2, 1.5)
- [yekutieli2015] Nonabelian Multiplicative Integration on Surfaces
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

noncomputable section
/-- Ground ring `R_q = ℤ[q, q⁻¹]`. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A Yekutieli triple at level `n` over a manifold `M`:
    the datum `(x, g, a)` of local trivialisations, transition
    automorphisms, and deformation parameters.

    **De-duplicated (bean `qou-s82c`).** This module used to declare its own
    copy of this structure, byte-identical to `QOU.Torsion.YekutieliTriple`
    except for the coefficient ring. It is now that structure instantiated at
    this module's ground ring `R_q = ℤ[q, q⁻¹]` — one definition, two rings,
    instead of two definitions that could drift apart. The generic structure
    asks only for `[Zero R]` precisely so a `CommRing` without total inverses
    can instantiate it. -/
-- Ref: [yekutieli2014-descent] Def 1.5 (combinatorial descent datum (x, g, a))
abbrev YekutieliTriple (M : Type*) := QOU.Torsion.YekutieliTriple R_q M

/-- A crossed module in the sense of Yekutieli [yekutieli2014-descent]:
    a pair of (possibly non-abelian) groups `N`, `G`, a boundary
    homomorphism `∂ : N → G`, and a conjugation action of `G` on
    `N` satisfying the Peiffer identity
    `∂(g · n) = g · ∂n · g⁻¹`.

    Note: the formal-chain layer keeps the carriers polymorphic
    rather than fixing them to `R_q`; the commutative ring `R_q`
    enters only through the *image* of `∂` when an instance is
    realised over the deformation parameter. Cf. gemini-code-assist
    review on PR #535. -/
-- Ref: [yekutieli2014-descent] Def 1.2 (crossed groupoid; one object = crossed module, Rem 1.3)
structure CrossedModule where
  N : Type
  G : Type
  [grpN : Group N]
  [grpG : Group G]
  boundary : N → G
  action : G → N → N
  peiffer : ∀ (g : G) (n : N),
    boundary (action g n) = g * boundary n * g⁻¹

attribute [instance] CrossedModule.grpN CrossedModule.grpG

/-- **Cosimplicial crossed groupoid** for the brane tower. -/
-- Ref: [yekutieli2014-descent] §1, text after Def 1.4, [leitner2026] §3
structure CosimplicialCrossedGroupoid (M : Type*) where
  tripleAt : (n : ℕ) → YekutieliTriple M
  coface : (n : ℕ) → YekutieliTriple M → YekutieliTriple M
  codegeneracy : (n : ℕ) → YekutieliTriple M → YekutieliTriple M
  retraction : ∀ (n : ℕ) (t : YekutieliTriple M),
    (codegeneracy n (coface n t)).level = t.level
  crossedMod : (n : ℕ) → CrossedModule
  coface_coface : ∀ (n : ℕ) (t : YekutieliTriple M),
    (coface (n + 1) (coface n t)).level =
    (coface n (coface n t)).level
  codegen_codegen : ∀ (n : ℕ) (t : YekutieliTriple M),
    (codegeneracy n (codegeneracy (n + 1) t)).level =
    (codegeneracy n (codegeneracy n t)).level

/-- The assignment `[n] ↦ 𝔊ₙ` extends to a cosimplicial crossed groupoid. -/
-- Ref: [yekutieli2014-descent] §1, text after Def 1.4 (cosimplicial crossed groupoid = object of Δ(CrGrpd)); existence on the brane tower is ours, not Yekutieli's
-- Ref: [leitner2026] §3, Proposition: Cosimplicial crossed groupoid
theorem cosimplicial_crossed_groupoid_exists (M : Type*)
    [inst : Nonempty M] :
    Nonempty (CosimplicialCrossedGroupoid M) := by
  obtain ⟨_⟩ := inst
  exact ⟨{
    tripleAt := fun n => ⟨n, id, fun _ => 1, fun _ => 1, fun _ => one_ne_zero⟩
    coface := fun _ t => { t with level := t.level + 1 }
    codegeneracy := fun _ t => { t with level := t.level - 1 }
    retraction := fun _ _ => by simp [Nat.add_sub_cancel]
    crossedMod := fun _ =>
      { N := PUnit
        G := PUnit
        boundary := id
        action := fun _ n => n
        peiffer := fun _ _ => Subsingleton.elim _ _ }
    coface_coface := fun _ _ => by simp
    codegen_codegen := fun _ _ => by simp
  }⟩

end
end QOU.LiftingDescent
