import CompactQuantumMetrics.OqSU2Coproduct

/-!
# The `*`-structure of `O_q(SU(2))`

Bean `qou-q3dc`. The corpus already has Woronowicz's involution as an `R`-linear
anti-automorphism `compactStar` (`OqSU2ModularNakayama.lean`), proved involutive
and anti-multiplicative. This file checks it against Woronowicz (1987) and proves
how it interacts with the coproduct, the torus, the characters and the Cartan
field of `OqSU2Coproduct.lean`.

The star is `R`-linear, so scalars are fixed. This is the real form: take `R`
real (or any ring with trivial conjugation). A conjugate-linear star over `ℂ` is
not built here.

## Results (sorry-free)

* `compactStar_alpha`, `_beta`, `_gamma`, `_delta`: the star is
  `α* = δ`, `β* = −qγ`, `γ* = −q⁻¹β`, `δ* = α`. Under the dictionary of
  `OqSU2WoronowiczCartan.lean` (`β = −νγ*`, `δ = α*`, `q = ν`) this is
  Woronowicz's `*` on his generators.
* `coprod_compactStar`: `Δ(x*) = (* ⊗ *)Δx` for every `x`. With the fact that
  `*` is an involutive anti-automorphism, this makes `(O_q(SU(2)), Δ, *)` a
  `*`-bialgebra (real form).
* `compactStar_torusScale`: `(T_{u,b} x)* = T_{u⁻¹,b⁻¹}(x*)`.
* `diagChar_compactStar`: `χ_u(x*) = χ_{u⁻¹}(x)`. So `ε` commutes with `*`, and
  `χ_u` is a `*`-character only when `u = u⁻¹`. Woronowicz's `f₁` (`u = q⁻²`) is
  not one, matching his (2.2).
* `cartanField_compactStar`: for the Cartan field `X = (id ⊗ (ε − χ_u)/c)Δ`,
  `(Xa)* = −T_{u⁻¹,u}(X(a*))`. The field is not `*`-preserving: the star turns it
  into minus itself, followed by the inverse right translation.
* `cartanField_selfAdjoint`: for `a* = a`, `(Xa)* = −T_{u⁻¹,u}(Xa)`.
* `cartanField_sq_selfAdjoint`: for `a* = a`, `Xa · Xa = −(T_{u⁻¹,u}(Xa))* · Xa`.

## What this says about the energy budget

The budget of `q_ns_twisted_transport.lean` is `−c·φ(Du·Du)`. For self-adjoint
`u`, `Du·Du = −(T_{u⁻¹,u}(Du))* · Du`, so it is minus a twisted square, not a
square. Positivity of `φ` alone does not sign it. Signing it needs the modular
property of the Haar state, `h(xy) = h(y σ(x))`, to move the twist across. That
step is not done here.

## Not established

* A conjugate-linear star over `ℂ`.
* The antipode and its relation `S(S(x)*)* = x`.
* The sign of the budget (above), and Part A of `conj:regularity-breakdown`
  (bean `qou-pa7n`).

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group. An example of a
  non-commutative differential calculus*, Publ. RIMS 23 (1987) 117–181,
  Section 1, Thm. 1.4 (pp. 126–127: `Φ` is a `*`-homomorphism, eqs. (1.11)–(1.13)),
  and eq. (2.2).
-/

open TensorProduct

namespace QOU.AlgebraicSubstrate.OqSU2

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- Generator induction on `O_q(SU(2))`. -/
theorem induction_gen {P : OqSU2 R q → Prop}
    (hα : P (α q)) (hβ : P (β q)) (hγ : P (γ q)) (hδ : P (δ q))
    (halg : ∀ r : R, P (algebraMap R (OqSU2 R q) r))
    (hadd : ∀ x y, P x → P y → P (x + y)) (hmul : ∀ x y, P x → P y → P (x * y))
    (x : OqSU2 R q) : P x := by
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective R (OqSU2Rel q) x
  induction y using FreeAlgebra.induction with
  | grade0 r => rw [AlgHom.commutes]; exact halg r
  | grade1 i =>
    fin_cases i
    · exact hα
    · exact hβ
    · exact hγ
    · exact hδ
  | mul x y hx hy => rw [map_mul]; exact hmul _ _ hx hy
  | add x y hx hy => rw [map_add]; exact hadd _ _ hx hy

@[simp] theorem compactStar_alpha : compactStar q (α (R := R) q) = δ q := by
  simp [compactStar, compactStarOpAlgEquiv, compactStarToOpAlgHom]

@[simp] theorem compactStar_beta : compactStar q (β (R := R) q) = -(q : R) • γ q := by
  simp [compactStar, compactStarOpAlgEquiv, compactStarToOpAlgHom]

@[simp] theorem compactStar_gamma :
    compactStar q (γ (R := R) q) = -(((q⁻¹ : Rˣ) : R)) • β q := by
  simp [compactStar, compactStarOpAlgEquiv, compactStarToOpAlgHom]

@[simp] theorem compactStar_delta : compactStar q (δ (R := R) q) = α q := by
  simp [compactStar, compactStarOpAlgEquiv, compactStarToOpAlgHom]

/-- **Torus scalings and the star.** `(T_{u,b} x)* = T_{u⁻¹,b⁻¹}(x*)`. -/
theorem compactStar_torusScale (u b : Rˣ) (x : OqSU2 R q) :
    compactStar q (torusScaleAlgHom q u b x) =
      torusScaleAlgHom q u⁻¹ b⁻¹ (compactStar q x) := by
  let lhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
    (compactStarOpAlgEquiv q).toAlgHom.comp (torusScaleAlgHom q u b)
  let rhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
    (algHomOp (torusScaleAlgHom q u⁻¹ b⁻¹)).comp (compactStarOpAlgEquiv q).toAlgHom
  have heq : lhsHom = rhsHom := by
    apply algHom_ext <;>
      simp [lhsHom, rhsHom, compactStarOpAlgEquiv, compactStarToOpAlgHom, algHomOp,
        torusScaleAlgHom, smul_smul, mul_comm] <;>
      exact MulOpposite.unop_injective (by simp)
  exact congr_arg MulOpposite.unop (AlgHom.congr_fun heq x)

/-- **Diagonal characters and the star.** `χ_u(x*) = χ_{u⁻¹}(x)`. -/
theorem diagChar_compactStar (u : Rˣ) (x : OqSU2 R q) :
    diagCharAlgHom q u (compactStar q x) = diagCharAlgHom q u⁻¹ x := by
  let lhsHom : OqSU2 R q →ₐ[R] R :=
    ((AlgEquiv.toOpposite R R).symm.toAlgHom.comp (algHomOp (diagCharAlgHom q u))).comp
      (compactStarOpAlgEquiv q).toAlgHom
  have heq : lhsHom = diagCharAlgHom q u⁻¹ := by
    apply algHom_ext <;>
      simp [lhsHom, compactStarOpAlgEquiv, compactStarToOpAlgHom, algHomOp, diagCharAlgHom]
  exact AlgHom.congr_fun heq x

theorem counit_compactStar (x : OqSU2 R q) : counit q (compactStar q x) = counit q x := by
  simpa using diagChar_compactStar q 1 x

/-- `* ⊗ *` on `O_q(SU(2)) ⊗ O_q(SU(2))`. -/
noncomputable def starTensor : OqSU2 R q ⊗[R] OqSU2 R q →ₗ[R] OqSU2 R q ⊗[R] OqSU2 R q :=
  TensorProduct.map (compactStar q) (compactStar q)

theorem compactStar_one : compactStar q (1 : OqSU2 R q) = 1 := by
  simp [compactStar]

theorem compactStar_algebraMap (r : R) :
    compactStar q (algebraMap R (OqSU2 R q) r) = algebraMap R (OqSU2 R q) r := by
  rw [Algebra.algebraMap_eq_smul_one, map_smul, compactStar_one]

/-- `* ⊗ *` reverses products, like `*`. -/
theorem starTensor_mul (S T : OqSU2 R q ⊗[R] OqSU2 R q) :
    starTensor q (S * T) = starTensor q T * starTensor q S := by
  induction S using TensorProduct.induction_on with
  | zero => simp
  | add S₁ S₂ h₁ h₂ => simp only [add_mul, mul_add, map_add, h₁, h₂]
  | tmul x y =>
    induction T using TensorProduct.induction_on with
    | zero => simp
    | add T₁ T₂ h₁ h₂ => simp only [add_mul, mul_add, map_add, h₁, h₂]
    | tmul x' y' =>
      simp [starTensor, Algebra.TensorProduct.tmul_mul_tmul, compactStar_mul]

theorem starTensor_algebraMap (r : R) :
    starTensor q (algebraMap R (OqSU2 R q ⊗[R] OqSU2 R q) r) =
      algebraMap R (OqSU2 R q ⊗[R] OqSU2 R q) r := by
  rw [Algebra.algebraMap_eq_smul_one, map_smul, Algebra.TensorProduct.one_def]
  simp [starTensor, compactStar_one]

/-- **The coproduct is a `*`-map.** `Δ(x*) = (* ⊗ *)Δx`. -/
theorem coprod_compactStar (x : OqSU2 R q) :
    coprod q (compactStar q x) = starTensor q (coprod q x) := by
  induction x using induction_gen with
  | hα => simp [starTensor, smul_tmul', tmul_smul, smul_smul, add_comm]
  | hβ =>
    simp [starTensor, smul_tmul', tmul_smul, add_comm]
    congr 2; exact (neg_smul _ _).symm
  | hγ =>
    simp [starTensor, smul_tmul', tmul_smul, add_comm]
    congr 2; exact (neg_smul _ _).symm
  | hδ => simp [starTensor, smul_tmul', tmul_smul, smul_smul, add_comm]
  | halg r => rw [compactStar_algebraMap, AlgHom.commutes, starTensor_algebraMap]
  | hadd x y hx hy => rw [map_add, map_add, map_add, hx, hy, map_add]
  | hmul x y hx hy => rw [compactStar_mul, map_mul, map_mul, hx, hy, starTensor_mul]

/-- **The star of the Cartan field.** For `X = (id ⊗ (ε − χ_u)/c)Δ`,
`(Xa)* = −T_{u⁻¹,u}(X(a*))`. -/
theorem cartanField_compactStar (u : Rˣ) (cinv : R) (a : OqSU2 R q) :
    compactStar q
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a) =
      -torusScaleAlgHom q u⁻¹ u
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap))
          (compactStar q a)) := by
  rw [(cartanField q u cinv a a).1, (cartanField q u cinv a a).1]
  have hcomp : ∀ y, torusScaleAlgHom q u⁻¹ u (torusScaleAlgHom q u u⁻¹ y) = y := by
    intro y
    have h := AlgHom.congr_fun (torusScaleAlgHom_comp (R := R) q u⁻¹ u u u⁻¹) y
    rw [AlgHom.comp_apply] at h
    rw [h, mul_inv_cancel, inv_mul_cancel]
    have hid : torusScaleAlgHom (R := R) q 1 1 = AlgHom.id R (OqSU2 R q) := by
      apply algHom_ext <;> simp [torusScaleAlgHom]
    rw [hid]; rfl
  rw [map_smul, map_sub, compactStar_torusScale, inv_inv, map_smul, map_sub, hcomp,
    smul_sub, smul_sub, neg_sub]

/-- For self-adjoint `a`, `(Xa)* = −T_{u⁻¹,u}(Xa)`. -/
theorem cartanField_selfAdjoint (u : Rˣ) (cinv : R) (a : OqSU2 R q)
    (ha : compactStar q a = a) :
    compactStar q
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a) =
      -torusScaleAlgHom q u⁻¹ u
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a) := by
  rw [cartanField_compactStar, ha]

/-- **The budget integrand is a twisted square, not a square.** For self-adjoint `a`,
`Xa · Xa = −(T_{u⁻¹,u}(Xa))* · Xa`. -/
theorem cartanField_sq_selfAdjoint (u : Rˣ) (cinv : R) (a : OqSU2 R q)
    (ha : compactStar q a = a) :
    leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a *
        leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a =
      -(compactStar q (torusScaleAlgHom q u⁻¹ u
          (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a)) *
        leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a) := by
  set X := leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q u).toLinearMap)) a
  have h : X = -compactStar q (torusScaleAlgHom q u⁻¹ u X) := by
    have h1 := congr_arg (compactStar q) (cartanField_selfAdjoint q u cinv a ha)
    rw [compactStar_involutive, map_neg] at h1
    exact h1
  exact (congrArg (· * X) h).trans (by exact neg_mul (α := OqSU2 R q) _ _)

end QOU.AlgebraicSubstrate.OqSU2
