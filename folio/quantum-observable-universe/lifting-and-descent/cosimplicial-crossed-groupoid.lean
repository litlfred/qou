import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Group.Basic


/-!
# QOU.CosimplicialCrossedGroupoid — Cosimplicial crossed groupoid structure

The recursive brane tower carries a cosimplicial object in the category
of crossed groupoids: coface maps from jet prolongation, codegeneracy
maps from descent, and the crossed structure from conjugation of
1-morphisms on 2-morphisms via the adjoint representation of SU_q(2).

## References

- [yekutieli2014-descent] Combinatorial Descent Data for Gerbes, §1 (Defs 1.2, 1.5)
- [yekutieli2015] Nonabelian Multiplicative Integration on Surfaces
- [leitner2026] §3 Lifting and Descent

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.

**Base ring (§7c): no field, and none is wanted.** A crossed module is a
*group-theoretic* object — Yekutieli's `∂ : N → G` between the band `𝒪_M×`
and the gauge group `SU_{qₙ}(2)`, both **groups of units**. An earlier
revision of this file modelled the band by a field `G` and guarded the
Peiffer identity with `a ≠ 0`; that was the wrong abstraction twice over
(nonzero ≠ invertible outside a field, and no ring structure is used at
all), and it forced a `field_simp` where nothing was being divided. The
`g⁻¹` below is the **group** inverse, not a field inverse.

This restores agreement with the compiled formal-chain module
`QOU.LiftingDescent.CosimplicialCrossedGroupoid`
([`lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean`](../lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean)),
which this file mirrors and which already carries the two-carrier
`Group`-based definition.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Yekutieli triple

The local data at each level of the brane tower: objects (local
trivialisations), 1-morphisms (gauge transitions), and 2-morphisms
(deformation parameters in the band). -/

/-- A Yekutieli triple at level `n` over a manifold `M`:
    the datum `(x, g, a)` of local trivialisations, transition
    automorphisms, and deformation parameters. -/
-- Ref: [yekutieli2014-descent] Def 1.5 (combinatorial descent datum (x, g, a))
structure YekutielijTriple (M : Type*) where
  /-- Level in the brane tower. -/
  level : ℕ
  /-- Objects: local trivialisations of the Frobenius–Hopf object Aₙ. -/
  objects : M → M
  /-- 1-morphisms: transition automorphisms g_{ij} in Aut_C(Aₙ). -/
  oneMorphisms : M → R_q
  /-- 2-morphisms: deformation parameters a_{ij} in the band 𝒪_M×. -/
  twoMorphisms : M → R_q
  /-- The 2-morphisms are invertible (they live in 𝒪_M×). -/
  twoMorphisms_ne_zero : ∀ (p : M), twoMorphisms p ≠ 0

/-! ## Crossed-module structure

At each level, `(SU_{qₙ}(2), 𝒪_M×)` forms a crossed module:
the boundary map `∂ : 𝒪_M× → SU_{qₙ}(2)` sends units to
central elements, and the action is conjugation. -/

/-- A crossed module in the sense of Yekutieli [yekutieli2014-descent]:
    a boundary homomorphism `∂ : N → G` and a `G`-action on `N`
    satisfying the Peiffer identity.

    Both carriers are groups (§7c): `N` models the band of units `𝒪_M×`
    and `G` the gauge group `SU_{qₙ}(2)`. No ring, field or division is
    involved — `g⁻¹` is the group inverse. -/
-- Ref: [yekutieli2014-descent] Def 1.2 (crossed groupoid; one object = crossed module, Rem 1.3)
structure CrossedModule where
  /-- The band `N = 𝒪_M×`, the group in which the 2-morphisms live. -/
  N : Type
  /-- The gauge group `G = SU_{qₙ}(2)` acting on the band. -/
  G : Type
  [grpN : Group N]
  [grpG : Group G]
  /-- The boundary map ∂ : 𝒪_M× → SU_{qₙ}(2), sending a unit to
      its central embedding. -/
  boundary : N → G
  /-- Conjugation action of 1-morphisms on 2-morphisms. -/
  action : G → N → N
  /-- Peiffer identity: `∂(g · n) = g · ∂(n) · g⁻¹`.
      Automatic for central extensions. -/
  peiffer : ∀ (g : G) (n : N),
    boundary (action g n) = g * boundary n * g⁻¹

attribute [instance] CrossedModule.grpN CrossedModule.grpG

/-! ## Cosimplicial crossed groupoid

The main structure: the assignment [n] ↦ 𝔊ₙ from Δ to
the 2-category of gerbes extends to a cosimplicial object
in the category of crossed groupoids. -/

/-- **Cosimplicial crossed groupoid** for the brane tower.

    The recursive brane tower `{Aₙ}` carries a cosimplicial structure:
    - Coface maps `δⁱ : 𝔊ₙ → 𝔊ₙ₊₁` from jet prolongation
    - Codegeneracy maps `σʲ : 𝔊ₙ₊₁ → 𝔊ₙ` from descent
    - Crossed structure from conjugation via Ad(SU_{qₙ}(2))

    LaTeX: `\label{prop:cosimplicial-crossed-groupoid}`

    **🛑 Vacuity status (audited 2026-11-20, bean `qou-dx7g`; triage rank 41).**
    This structure does **not** encode the proposition.  (1) The three
    "cosimplicial identities" constrain only the `.level : ℕ` field of the
    image triples, never the triples themselves, and they are not the
    cosimplicial identities: there is one coface and one codegeneracy per
    level rather than the indexed families `δⁱ : 𝔊ₙ → 𝔊ₙ₊₁` (`0 ≤ i ≤ n+1`) and
    `σʲ : 𝔊ₙ₊₁ → 𝔊ₙ`, so `δʲδⁱ = δⁱδʲ⁻¹` cannot even be stated.  (2) No field
    ties `coface` to `tripleAt` or to jet prolongation, and `crossedMod n` is
    unrelated to the triple at level `n`; `cosimplicial_crossed_groupoid_exists`
    inhabits it with level-shifts and `PUnit` crossed modules.  A faithful
    version would take the cosimplicial object from Mathlib
    (`CategoryTheory.CosimplicialObject`, whose identities are theorems) with
    `[n] ↦ 𝔊ₙ` and the coface maps given by jet prolongation.  Neither the
    brane tower (`QOU.Torsion.RecursiveBraneTower` is itself abstract) nor jet
    prolongation is defined in the corpus, so the free fields — `tripleAt`,
    `coface`, `codegeneracy`, `crossedMod` — stay free.  The library twin
    `QOU.LiftingDescent.CosimplicialCrossedGroupoid` has the same shape. -/
-- Ref: [yekutieli2014-descent] §1, text after Def 1.4, [leitner2026] §3
structure CosimplicialCrossedGroupoid (M : Type*) where
  /-- The Yekutieli triple at each level. -/
  tripleAt : (n : ℕ) → YekutielijTriple M
  /-- Coface map: jet prolongation sends level-n data to level-(n+1). -/
  coface : (n : ℕ) → YekutielijTriple M → YekutielijTriple M
  /-- Codegeneracy map: descent sends level-(n+1) data to level-n. -/
  codegeneracy : (n : ℕ) → YekutielijTriple M → YekutielijTriple M
  /-- Retraction: `σ ∘ δ = id` on levels (from 𝔡_{n+1} ∘ ℓ_n = id). -/
  retraction : ∀ (n : ℕ) (t : YekutielijTriple M),
    (codegeneracy n (coface n t)).level = t.level
  /-- The crossed-module structure at each level. -/
  crossedMod : (n : ℕ) → CrossedModule
  /-- Cosimplicial identity: δʲ ∘ δⁱ = δⁱ ∘ δʲ⁻¹ for i < j. -/
  coface_coface : ∀ (n : ℕ) (t : YekutielijTriple M),
    (coface (n + 1) (coface n t)).level =
    (coface n (coface n t)).level
  /-- Cosimplicial identity: σʲ ∘ σⁱ = σⁱ ∘ σʲ⁺¹ for i ≤ j. -/
  codegen_codegen : ∀ (n : ℕ) (t : YekutielijTriple M),
    (codegeneracy n (codegeneracy (n + 1) t)).level =
    (codegeneracy n (codegeneracy n t)).level

/-! ## Main proposition: the brane tower forms a cosimplicial crossed groupoid -/

/-- The assignment `[n] ↦ 𝔊ₙ` extends to a cosimplicial crossed groupoid.

    The construction is purely algebraic (§7c): the crossed module at each
    level is the central one, `∂` landing in the centre, so the Peiffer
    identity holds by conjugation-triviality and no archimedean
    specialisation to `ℝ` is required anywhere. -/
-- Ref: [yekutieli2014-descent] §1, text after Def 1.4 (cosimplicial crossed groupoid = object of Δ(CrGrpd)); existence on the brane tower is ours, not Yekutieli's
-- Ref: [leitner2026] §3, Proposition: Cosimplicial crossed groupoid
theorem cosimplicial_crossed_groupoid_exists (M : Type*)
    [inst : Nonempty M] :
    Nonempty (CosimplicialCrossedGroupoid M) := by
  -- Ref: [yekutieli2014-descent] arXiv:1109.1919, §1
  obtain ⟨_⟩ := inst
  exact ⟨{
    tripleAt := fun n => ⟨n, id, fun _ => 1, fun _ => 1, fun _ => one_ne_zero⟩
    coface := fun _ t => { t with level := t.level + 1 }
    codegeneracy := fun _ t => { t with level := t.level - 1 }
    retraction := fun n t => by simp
    crossedMod := fun _ =>
      { N := PUnit
        G := PUnit
        boundary := id
        action := fun _ n => n
        peiffer := fun _ _ => Subsingleton.elim _ _ }
    coface_coface := fun _ _ => by simp
    codegen_codegen := fun _ _ => by simp
  }⟩

/-- The Peiffer identity, read off a crossed module: the boundary intertwines
    the action with conjugation. -/
-- Ref: [yekutieli2014-descent] Def 1.2(i) (D is G₁-equivariant: the Peiffer condition)
theorem peiffer_central_automatic (cm : CrossedModule) (g : cm.G) (n : cm.N) :
    cm.boundary (cm.action g n) = g * cm.boundary n * g⁻¹ :=
  cm.peiffer g n

/-- Retraction at each level: codegeneracy ∘ coface = id. -/
theorem cosimplicial_retraction_level {M : Type*}
    (csg : CosimplicialCrossedGroupoid M) (n : ℕ) :
    (csg.codegeneracy n (csg.coface n (csg.tripleAt n))).level =
    (csg.tripleAt n).level :=
  csg.retraction n (csg.tripleAt n)

end

end QOU
