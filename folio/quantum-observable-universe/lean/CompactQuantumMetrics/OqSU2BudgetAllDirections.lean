import CompactQuantumMetrics.OqSU2BudgetSquare
import CompactQuantumMetrics.OqSU2OffDiagonal

/-!
# The budget integrand in the off-diagonal directions

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`).

`OqSU2BudgetSquare` showed that for the Cartan field `X` of the 3D calculus the
budget integrand `φ(X a · X a)` is minus a twisted square `-φ(w* w)` whenever `a`
is self-adjoint and `φ` is torus-invariant. This file extends the identity to the
two off-diagonal directions of Woronowicz's calculus, using the fields
`field q s0 sp sm` of `OqSU2OffDiagonal` (twist `T_{q⁻¹,q}`).

## Results (sorry-free, over a generic `CommRing R`)

* `field_one`, `field_algebraMap`: the fields kill scalars.
* `field_compactStar`: the star swaps the two off-diagonal slots,
  `(X_{s0,sp,sm} a)* = -T_{q,q⁻¹}(X_{s0,sm,sp}(a*))`.
* `mul_eq_smul_square_of_star`: if `(Y a)* = c·T_{s⁻²,s²}(Y'(a*))`, then for
  self-adjoint `a` and `T_{s⁻¹,s}`-invariant `φ`,
  `φ(Y a · Y' a) = c · φ(w* w)` with `w = T_{s⁻¹,s}(Y' a)`.
* `field_pair_eq_neg_square`: for `s² = q⁻¹`,
  `φ(X_{s0,sp,sm} a · X_{s0,sm,sp} a) = -φ(w* w)`.
* `fieldPlusMinus_eq_neg_square`: the case `X₊ · X₋`.

## Consequence, conditional

With the Haar state `h` (PR #9599: torus-invariant for all scalings) and Haar
positivity `h(w* w) ≥ 0` (open in that thread), `h(X₊ a · X₋ a) ≤ 0`, given a
square root `s` of `q⁻¹` in `R`. Woronowicz's `χ₂` is `-q·X₋`, so the
Woronowicz-normalised pairing `h(χ₀ a · χ₂ a)` picks up the factor `-q`.

## Not established here

* Which pairing of the three directions is the budget in the transport
  equation of the q-NS model.
* Haar positivity, and so any sign statement.
* Part A itself (bean `qou-pa7n`) stays open.

Ref: [woronowicz1987-twisted-su2] S. L. Woronowicz, Twisted SU(2) group. An
example of a non-commutative differential calculus, Publ. RIMS 23 (1987),
117–181, §2 (star structure) and §4 (3D calculus).
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {R : Type*} [CommRing R] (q : Rˣ)

set_option linter.unusedSimpArgs false in
/-- Normalise a generator case of `field_compactStar`. -/
local macro "gen_star_simp" : tactic => `(tactic| (
  simp [field_alpha, field_beta, field_gamma, field_delta, torusScaleAlgHom, smul_smul,
    q_mul_mul_inv, sub_eq_add_neg, smul_add, smul_neg, mul_comm, mul_left_comm] <;> abel))

theorem field_one (s0 sp sm : R) : field q s0 sp sm (1 : OqSU2 R q) = 0 := by
  have h := field_leibniz q s0 sp sm 1 1
  simp only [mul_one, one_mul, map_one] at h
  exact add_left_cancel (h.symm.trans (add_zero _).symm)

theorem field_algebraMap (s0 sp sm r : R) :
    field q s0 sp sm (algebraMap R (OqSU2 R q) r) = 0 := by
  rw [Algebra.algebraMap_eq_smul_one, map_smul, field_one, smul_zero]

/-- **Star of the off-diagonal fields.** `(X_{s0,sp,sm} a)* = −T_{q,q⁻¹}(X_{s0,sm,sp}(a*))`. -/
theorem field_compactStar (s0 sp sm : R) (a : OqSU2 R q) :
    compactStar q (field q s0 sp sm a) =
      (-1 : R) • torusScaleAlgHom q q q⁻¹ (field q s0 sm sp (compactStar q a)) := by
  induction a using induction_gen with
  | hα => gen_star_simp
  | hβ => gen_star_simp
  | hγ => gen_star_simp
  | hδ => gen_star_simp
  | halg r => rw [field_algebraMap, compactStar_algebraMap, field_algebraMap]; simp
  | hadd x y hx hy => rw [map_add, map_add, hx, hy, map_add, map_add, map_add, smul_add]
  | hmul x y hx hy =>
    have hT : ∀ z, torusScaleAlgHom q q q⁻¹ (torusScaleAlgHom q q⁻¹ q z) = z := by
      intro z; simpa using torusScale_inv_comp q q⁻¹ z
    rw [field_leibniz, map_add, compactStar_mul, compactStar_mul, hx, hy, compactStar_mul,
      field_leibniz, map_add, map_mul, map_mul, inv_inv, hT, compactStar_torusScale, inv_inv]
    simp only [smul_mul_assoc, mul_smul_comm, smul_add]
    abel

/-- **Abstract square identity.** Let `Y, Y'` be linear operators with
`(Y a)* = c • T_{u⁻¹,u}(Y'(a*))`, where `u = s²`. For self-adjoint `a` and a functional `φ`
invariant under `T_{s⁻¹,s}`, `φ(Ya · Y'a) = c · φ(w* w)` with `w = T_{s⁻¹,s}(Y'a)`. -/
theorem mul_eq_smul_square_of_star (Y Y' : OqSU2 R q →ₗ[R] OqSU2 R q) (s : Rˣ) (c : R)
    (hY : ∀ a, compactStar q (Y a) = c • torusScaleAlgHom q (s ^ 2)⁻¹ (s ^ 2) (Y' (compactStar q a)))
    (a : OqSU2 R q) (ha : compactStar q a = a) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x, φ (torusScaleAlgHom q s⁻¹ s x) = φ x) :
    φ (Y a * Y' a) =
      c * φ (compactStar q (torusScaleAlgHom q s⁻¹ s (Y' a)) * torusScaleAlgHom q s⁻¹ s (Y' a)) := by
  set w := torusScaleAlgHom q s⁻¹ s (Y' a)
  have h1 : Y a = c • torusScaleAlgHom q s s⁻¹ (compactStar q w) := by
    have h := congr_arg (compactStar q) (hY a)
    rw [compactStar_involutive, ha, map_smul, torusScale_sq, compactStar_torusScale,
      inv_inv] at h
    exact h
  have key : φ (torusScaleAlgHom q s s⁻¹ (compactStar q w) * Y' a) =
      φ (compactStar q w * w) := by
    rw [← hφ, map_mul, torusScale_inv_comp]
  rw [h1, smul_mul_assoc, map_smul, key, smul_eq_mul]

/-- **Off-diagonal budget pairing.** For `s² = q⁻¹`, self-adjoint `a` and `T_{s⁻¹,s}`-invariant
`φ`, `φ(X_{s0,sp,sm} a · X_{s0,sm,sp} a) = −φ(w* w)` with `w = T_{s⁻¹,s}(X_{s0,sm,sp} a)`. -/
theorem field_pair_eq_neg_square (s0 sp sm : R) (s : Rˣ) (hs : s ^ 2 = q⁻¹)
    (a : OqSU2 R q) (ha : compactStar q a = a) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x, φ (torusScaleAlgHom q s⁻¹ s x) = φ x) :
    φ (field q s0 sp sm a * field q s0 sm sp a) =
      -φ (compactStar q (torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) *
        torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) := by
  have hY : ∀ b, compactStar q (field q s0 sp sm b) =
      (-1 : R) • torusScaleAlgHom q (s ^ 2)⁻¹ (s ^ 2) (field q s0 sm sp (compactStar q b)) := by
    intro b; rw [hs, inv_inv]; exact field_compactStar q s0 sp sm b
  rw [mul_eq_smul_square_of_star q _ _ s (-1) hY a ha φ hφ, neg_one_mul]

/-- The raising/lowering pair: `φ(X₊a · X₋a) = −φ(w* w)`, `w = T_{s⁻¹,s}(X₋ a)`. -/
theorem fieldPlusMinus_eq_neg_square (s : Rˣ) (hs : s ^ 2 = q⁻¹)
    (a : OqSU2 R q) (ha : compactStar q a = a) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x, φ (torusScaleAlgHom q s⁻¹ s x) = φ x) :
    φ (fieldPlus q a * fieldMinus q a) =
      -φ (compactStar q (torusScaleAlgHom q s⁻¹ s (fieldMinus q a)) *
        torusScaleAlgHom q s⁻¹ s (fieldMinus q a)) :=
  field_pair_eq_neg_square q 0 1 0 s hs a ha φ hφ

end QOU.AlgebraicSubstrate.OqSU2
