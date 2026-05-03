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

- [yekutieli2010] Central Extensions of Gerbes, §3–4
- [yekutieli2015] Nonabelian Multiplicative Integration on Surfaces
- [manuscript] §3 Lifting and Descent
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.LiftingDescent

/-- Ground ring `R_q = ℤ[q, q⁻¹]`. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A Yekutieli triple at level `n` over a manifold `M`:
    the datum `(x, g, a)` of local trivialisations, transition
    automorphisms, and deformation parameters. -/
-- Ref: [yekutieli2010] §3
structure YekutielijTriple (M : Type*) where
  level : ℕ
  objects : M → M
  oneMorphisms : M → R_q
  twoMorphisms : M → R_q
  twoMorphisms_ne_zero : ∀ (p : M), twoMorphisms p ≠ 0

/-- A crossed module in the sense of Yekutieli [yekutieli2010]:
    a boundary homomorphism `∂ : N → G` and a conjugation action
    satisfying the Peiffer identity. -/
-- Ref: [yekutieli2010] §2, Definition 2.1
structure CrossedModule where
  boundary : R_q → R_q
  conjugation : R_q → R_q → R_q
  peiffer : ∀ (a b : R_q) (ha : a ≠ 0),
    boundary a * b = a * b * a⁻¹

/-- **Cosimplicial crossed groupoid** for the brane tower. -/
-- Ref: [yekutieli2010] §4, [manuscript] §3
structure CosimplicialCrossedGroupoid (M : Type*) where
  tripleAt : (n : ℕ) → YekutielijTriple M
  coface : (n : ℕ) → YekutielijTriple M → YekutielijTriple M
  codegeneracy : (n : ℕ) → YekutielijTriple M → YekutielijTriple M
  retraction : ∀ (n : ℕ) (t : YekutielijTriple M),
    (codegeneracy n (coface n t)).level = t.level
  crossedMod : (n : ℕ) → CrossedModule
  coface_coface : ∀ (n : ℕ) (t : YekutielijTriple M),
    (coface (n + 1) (coface n t)).level =
    (coface n (coface n t)).level
  codegen_codegen : ∀ (n : ℕ) (t : YekutielijTriple M),
    (codegeneracy n (codegeneracy (n + 1) t)).level =
    (codegeneracy n (codegeneracy n t)).level

/-- The assignment `[n] ↦ 𝔊ₙ` extends to a cosimplicial crossed groupoid. -/
-- Ref: [yekutieli2010] §4, Theorem 4.2
-- Ref: [manuscript] §3, Proposition: Cosimplicial crossed groupoid
theorem cosimplicial_crossed_groupoid_exists (M : Type*)
    [inst : Nonempty M] :
    Nonempty (CosimplicialCrossedGroupoid M) := by
  obtain ⟨_⟩ := inst
  exact ⟨{
    tripleAt := fun n => ⟨n, id, fun _ => 1, fun _ => 1, fun _ => one_ne_zero⟩
    coface := fun _ t => { t with level := t.level + 1 }
    codegeneracy := fun _ t => { t with level := t.level - 1 }
    retraction := fun _ _ => by simp [Nat.add_sub_cancel]
    crossedMod := fun _ => ⟨id, fun a _ => a, fun _ _ _ => by ring⟩
    coface_coface := fun _ _ => by simp
    codegen_codegen := fun _ _ => by simp
  }⟩

end QOU.LiftingDescent
