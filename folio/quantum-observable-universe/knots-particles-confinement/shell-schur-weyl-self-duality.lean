import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.ShellSchurWeylSelfDuality

`prop:shell-schur-weyl-self-duality`, corrected 2026-11-15.

**What was wrong.** The old statement said transposition `λ ↦ λ*` is the
image of representation duality `V ↦ V*` on `U_q(gl_k)`-modules, so that
`V(λ*) ≅ V(λ)*`. That is false: for `k = 2`, `λ = (2)`, `V(2)` has
dimension 3 and `V(1,1)` (the determinant) has dimension 1. The old Lean
proved `x_λ = x_{λ*}` by `rfl`, with the transpose replaced by the
identity.

**What is true and proved here.** Transposition comes from the algebra
automorphism `#` of `H_n(q)`, `σ_i ↦ −σ_i⁻¹ = h − σ_i` with
`h = q − q⁻¹`:

* `hashGen_quadratic`, `hashGen_braid`: `h − σ` again satisfies the Hecke
  quadratic and the braid relation, so `#` is well defined on generators.
* `fixed_iff_coeff_symm`: if an automorphism permutes a linearly independent
  family of idempotents `e_λ` by an involution `τ`, then
  `Σ x_λ e_λ` is fixed iff `x_λ = x_{τ λ}` for all `λ`.

That `#` sends the central idempotent `e_λ` to `e_{λ*}` in the split
semisimple case is the standard twist `(S^λ)^# ≅ (S^{λ*})^⊛`; it is cited,
not proved here.
-- Ref: [mathas1999] Iwahori–Hecke algebras and Schur algebras, Ch. 3
-- Ref: [dipper-james1986]
-/

namespace QOU.BraidKnot.ShellSchurWeylSelfDuality

section Generator
variable {k A : Type*} [CommRing k] [Ring A] [Algebra k A]

/-- The image of a Hecke generator under `#`: `σ ↦ −σ⁻¹ = h − σ`. -/
def hashGen (h : k) (a : A) : A := algebraMap k A h - a

theorem hashGen_quadratic (h : k) (a : A) (ha : a * a = h • a + 1) :
    hashGen h a * hashGen h a = h • hashGen h a + 1 := by
  simp only [hashGen, Algebra.algebraMap_eq_smul_one]
  rw [sub_mul, mul_sub, mul_sub, ha]
  simp only [smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, smul_sub]
  abel

theorem hashGen_braid (h : k) (a b : A) (ha : a * a = h • a + 1)
    (hb : b * b = h • b + 1) (hab : a * b * a = b * a * b) :
    hashGen h a * hashGen h b * hashGen h a
      = hashGen h b * hashGen h a * hashGen h b := by
  simp only [hashGen, Algebra.algebraMap_eq_smul_one]
  have key : ((h • (1 : A)) - a) * (h • 1 - b) * (h • 1 - a)
      - (h • 1 - b) * (h • 1 - a) * (h • 1 - b)
      = (h * h) • (b - a) + h • (a * a - b * b) - (a * b * a - b * a * b) := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
      smul_smul, smul_sub]
    noncomm_ring
  rw [ha, hb, hab] at key
  rw [← sub_eq_zero, key]
  simp only [add_sub_add_right_eq_sub, ← smul_sub, smul_smul, sub_self]
  rw [sub_zero, ← smul_add]; simp
end Generator

section Fixed
variable {k A ι : Type*} [CommRing k] [Ring A] [Algebra k A] [Fintype ι]

theorem fixed_iff_coeff_symm (φ : A →ₐ[k] A) (e : ι → A) (he : LinearIndependent k e)
    (τ : ι ≃ ι) (hτ : ∀ i, τ (τ i) = i) (hφ : ∀ i, φ (e i) = e (τ i)) (x : ι → k) :
    φ (∑ i, x i • e i) = ∑ i, x i • e i ↔ ∀ i, x i = x (τ i) := by
  have hmap : φ (∑ i, x i • e i) = ∑ j, x (τ j) • e j := by
    rw [map_sum]
    simp only [map_smul, hφ]
    exact Fintype.sum_equiv τ _ _ fun i => by rw [hτ]
  rw [hmap]
  constructor
  · intro hfix
    have h0 : ∑ j, (x (τ j) - x j) • e j = 0 := by
      simp only [sub_smul, Finset.sum_sub_distrib, hfix, sub_self]
    intro i
    have := Fintype.linearIndependent_iff.mp he _ h0 i
    exact (sub_eq_zero.mp this).symm
  · intro hx
    exact Finset.sum_congr rfl fun j _ => by rw [← hx j]
end Fixed
end QOU.BraidKnot.ShellSchurWeylSelfDuality
