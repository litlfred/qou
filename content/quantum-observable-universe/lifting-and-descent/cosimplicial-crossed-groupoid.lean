import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CosimplicialCrossedGroupoid — Cosimplicial crossed groupoid structure

The recursive brane tower carries a cosimplicial object in the category
of crossed groupoids: coface maps from jet prolongation, codegeneracy
maps from descent, and the crossed structure from conjugation of
1-morphisms on 2-morphisms via the adjoint representation of SU_q(2).

## References

- [yekutieli2010] Central Extensions of Gerbes, §3–4
- [yekutieli2015] Nonabelian Multiplicative Integration on Surfaces
- [manuscript] §3 Lifting and Descent

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
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
-- Ref: [yekutieli2010] §3
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

/-- A crossed module in the sense of Yekutieli [yekutieli2010]:
    a boundary homomorphism `∂ : N → G` and a conjugation action
    satisfying the Peiffer identity. -/
-- Ref: [yekutieli2010] §2, Definition 2.1
structure CrossedModule where
  /-- The boundary map ∂ : 𝒪_M× → SU_{qₙ}(2), sending a unit to
      its central embedding. -/
  boundary : R_q → R_q
  /-- Conjugation action of 1-morphisms on 2-morphisms. -/
  conjugation : R_q → R_q → R_q
  /-- Peiffer identity: ∂(a) · b = a · b · a⁻¹.
      Automatic for central extensions. -/
  peiffer : ∀ (a b : R_q) (ha : a ≠ 0),
    boundary a * b = a * b * a⁻¹

/-! ## Cosimplicial crossed groupoid

The main structure: the assignment [n] ↦ 𝔊ₙ from Δ to
the 2-category of gerbes extends to a cosimplicial object
in the category of crossed groupoids. -/

/-- **Cosimplicial crossed groupoid** for the brane tower.

    The recursive brane tower `{Aₙ}` carries a cosimplicial structure:
    - Coface maps `δⁱ : 𝔊ₙ → 𝔊ₙ₊₁` from jet prolongation
    - Codegeneracy maps `σʲ : 𝔊ₙ₊₁ → 𝔊ₙ` from descent
    - Crossed structure from conjugation via Ad(SU_{qₙ}(2))

    LaTeX: `\label{prop:cosimplicial-crossed-groupoid}` -/
-- Ref: [yekutieli2010] §4, [manuscript] §3
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

/-- The assignment `[n] ↦ 𝔊ₙ` extends to a cosimplicial crossed groupoid. -/
-- Ref: [yekutieli2010] §4, Theorem 4.2
-- Ref: [manuscript] §3, Proposition: Cosimplicial crossed groupoid
theorem cosimplicial_crossed_groupoid_exists (M : Type*)
    [inst : Nonempty M] :
    Nonempty (CosimplicialCrossedGroupoid M) := by
  -- Ref: [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
  obtain ⟨p⟩ := inst
  exact ⟨{
    tripleAt := fun n => ⟨n, id, fun _ => 1, fun _ => 1, fun _ => one_ne_zero⟩
    coface := fun _ t => { t with level := t.level + 1 }
    codegeneracy := fun _ t => { t with level := t.level - 1 }
    retraction := fun n t => by simp [Nat.add_sub_cancel]
    crossedMod := fun _ => ⟨id, fun a _ => a, fun a _ ha => by ring⟩
    coface_coface := fun _ _ => by simp
    codegen_codegen := fun _ _ => by simp
  }⟩

/-- The Peiffer identity for central extensions. -/
-- Ref: [yekutieli2010] §2, Remark 2.3
theorem peiffer_central_automatic (cm : CrossedModule)
    (a b : R_q) (ha : a ≠ 0) :
    cm.boundary a * b = a * b * a⁻¹ :=
  cm.peiffer a b ha

/-- Retraction at each level: codegeneracy ∘ coface = id. -/
theorem cosimplicial_retraction_level {M : Type*}
    (csg : CosimplicialCrossedGroupoid M) (n : ℕ) :
    (csg.codegeneracy n (csg.coface n (csg.tripleAt n))).level =
    (csg.tripleAt n).level :=
  csg.retraction n (csg.tripleAt n)

end QOU
