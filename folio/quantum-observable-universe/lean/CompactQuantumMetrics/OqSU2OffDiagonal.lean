import CompactQuantumMetrics.OqSU2Coproduct

/-!
# Off-diagonal left-invariant vector fields on `O_q(SU(2))` and their twist

Bean `qou-q3dc`, option B. `OqSU2Coproduct.lean` gives the coproduct and shows that a
functional `φ` with `φ(xy) = φ(x)χ(y) + ε(x)φ(y)` for a character `χ` yields a
left-invariant operator `X_φ = (id ⊗ φ)Δ` with the one-sided Leibniz rule
`X_φ(fg) = X_φ f · R_χ g + f · X_φ g`. Only the diagonal (Cartan) field was built there.
This file builds the off-diagonal ones and pins down their twist. Everything is over a
generic commutative ring `R` with `q : Rˣ` (§7c).

Call `φ` a `χ_u`-twisted derivation when
`φ(xy) = φ(x) χ_u(y) + ε(x) φ(y)` for the diagonal character `χ_u = (u, 0, 0, u⁻¹)`.

## Results (sorry-free)

* `twistedDeriv_constraints`: every `χ_u`-twisted derivation satisfies
  `φ(β)(1 − qu) = 0`, `φ(γ)(1 − qu) = 0` and `φ(δ) = −u⁻¹ φ(α)`.
  So off-diagonal components force `qu = 1` up to torsion: the twist is `χ_{q⁻¹}`.
* `twistedDeriv_offDiag_eq_zero`: if `1 − qu` is not a zero divisor, `φ(β) = φ(γ) = 0`;
  no off-diagonal field exists at any other diagonal twist.
* `triRep`: for `s0 sp sm : R` the upper-triangular representation
  `α ↦ [[1, s0], [0, q⁻¹]]`, `β ↦ [[0, sp], [0, 0]]`, `γ ↦ [[0, sm], [0, 0]]`,
  `δ ↦ [[1, −q s0], [0, q]]`. Its corner `triFun` is a `χ_{q⁻¹}`-twisted derivation
  (`triFun_twisted`).
* `twistedDeriv_eq_triFun`: every `χ_{q⁻¹}`-twisted derivation is `triFun (φ α) (φ β) (φ γ)`.
  The `χ_{q⁻¹}`-twisted derivations are exactly a free 3-parameter family: a
  three-dimensional tangent space.
* `field_leibniz`: the field `X_s = (id ⊗ triFun s)Δ` satisfies
  `X(fg) = Xf · R g + f · Xg` with `R = (q⁻¹α, qβ, q⁻¹γ, qδ)`, one-sided, for all three
  directions at once.
* `field_alpha`, …, `field_delta`: on generators
  `X α = s0α + smβ`, `X β = spα − q s0β`, `X γ = s0γ + smδ`, `X δ = spγ − q s0δ`.
  So `X₊ = X_{(0,1,0)}` sends `(α, β, γ, δ) ↦ (0, α, 0, γ)` and `X₋ = X_{(0,0,1)}` sends
  `(α, β, γ, δ) ↦ (β, 0, δ, 0)`: right-acting raising and lowering operators.

## Not established

* Whether this basis is Woronowicz's normalization of the 3D calculus. Woronowicz (1987)
  is not in `library/`. In particular his Cartan direction may use a twist other than
  `χ_{q⁻¹}`; here `X₀ = X_{(1,0,0)}` is the Cartan field with the same twist as `X₊, X₋`.
  `OqSU2Coproduct.cartanField` covers Cartan fields at any `u`.
* Twists by non-diagonal characters, and twists by a matrix of characters (non-split
  bimodule structure).
* Anything about Part A of `conj:regularity-breakdown` (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group* (1987).
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open TensorProduct

variable {R : Type*} [CommRing R] (q : Rˣ)

/-! ## 1. Constraints on twisted derivations -/

section Constraints

variable {q}

theorem twistedDeriv_map_one (u : Rˣ) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y) :
    φ 1 = 0 := by
  have h := hφ 1 1
  simp only [mul_one, map_one, one_mul] at h
  linear_combination -h

/-- **Constraints on a `χ_u`-twisted derivation.** -/
theorem twistedDeriv_constraints (u : Rˣ) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y) :
    φ (β q) * (1 - (q : R) * u) = 0 ∧ φ (γ q) * (1 - (q : R) * u) = 0 ∧
      φ (δ q) = -(((u⁻¹ : Rˣ) : R)) * φ (α q) := by
  refine ⟨?_, ?_, ?_⟩
  · have h := congrArg φ (rel_ab q)
    rw [map_smul, hφ, hφ] at h
    simp [counit, diagCharAlgHom] at h
    linear_combination h
  · have h := congrArg φ (rel_ag q)
    rw [map_smul, hφ, hφ] at h
    simp [counit, diagCharAlgHom] at h
    linear_combination h
  · have h := congrArg φ (rel_det_left q)
    rw [map_sub, map_smul, hφ, hφ, twistedDeriv_map_one u φ hφ] at h
    simp [counit, diagCharAlgHom] at h
    linear_combination h

/-- **No off-diagonal field away from `u = q⁻¹`.** If `1 − qu` is not a zero divisor,
a `χ_u`-twisted derivation vanishes on `β` and `γ`. -/
theorem twistedDeriv_offDiag_eq_zero (u : Rˣ) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y)
    (hreg : ∀ r : R, r * (1 - (q : R) * u) = 0 → r = 0) :
    φ (β q) = 0 ∧ φ (γ q) = 0 :=
  ⟨hreg _ (twistedDeriv_constraints u φ hφ).1, hreg _ (twistedDeriv_constraints u φ hφ).2.1⟩

/-- A `χ_u`-twisted derivation vanishing on `α, β, γ` is zero. -/
theorem twistedDeriv_eq_zero (u : Rˣ) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * diagCharAlgHom q u y + counit q x * φ y)
    (hα : φ (α q) = 0) (hβ : φ (β q) = 0) (hγ : φ (γ q) = 0) : φ = 0 := by
  have hδ : φ (δ q) = 0 := by
    rw [(twistedDeriv_constraints u φ hφ).2.2, hα, mul_zero]
  have h1 := twistedDeriv_map_one u φ hφ
  ext x
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective R (OqSU2Rel q) x
  induction y using FreeAlgebra.induction with
  | grade0 r =>
    rw [AlgHom.commutes, Algebra.algebraMap_eq_smul_one, map_smul, h1, smul_zero]; rfl
  | grade1 i =>
    fin_cases i
    · exact hα
    · exact hβ
    · exact hγ
    · exact hδ
  | mul a b ha hb =>
    simp only [LinearMap.zero_apply] at ha hb ⊢
    rw [map_mul, hφ, ha, hb]; ring
  | add a b ha hb =>
    simp only [LinearMap.zero_apply] at ha hb ⊢
    rw [map_add, map_add, ha, hb, add_zero]

end Constraints

/-! ## 2. The upper-triangular representation and its corner functional -/

theorem q_mul_mul_inv (x : R) : (q : R) * x * (((q⁻¹ : Rˣ) : R)) = x := by
  rw [mul_comm (q : R), mul_assoc, Units.mul_inv, mul_one]

/-- The upper-triangular representation with diagonal `(ε, χ_{q⁻¹})` and off-diagonal
corner `(α, β, γ, δ) ↦ (s0, sp, sm, −q s0)`. -/
noncomputable def triRep (s0 sp sm : R) : OqSU2 R q →ₐ[R] Matrix (Fin 2) (Fin 2) R :=
  liftQuadruple q
    (Matrix.of ![![1, s0], ![0, (((q⁻¹ : Rˣ) : R))]])
    (Matrix.of ![![0, sp], ![0, 0]])
    (Matrix.of ![![0, sm], ![0, 0]])
    (Matrix.of ![![1, -((q : R) * s0)], ![0, (q : R)]])
    { ab := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two]
        rw [← mul_assoc, q_mul_mul_inv]
      ag := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two]
        rw [← mul_assoc, q_mul_mul_inv]
      bd := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two, mul_comm]
      gd := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two, mul_comm]
      bg := by
        ext i j
        fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
      det_left := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two]
        ring
      det_right := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two]
        ring_nf; simp [mul_assoc] }

/-- The representation is upper triangular with diagonal `(ε, χ_{q⁻¹})`. -/
theorem triRep_shape (s0 sp sm : R) (x : OqSU2 R q) :
    triRep q s0 sp sm x 1 0 = 0 ∧ triRep q s0 sp sm x 0 0 = counit q x ∧
      triRep q s0 sp sm x 1 1 = diagCharAlgHom q q⁻¹ x := by
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective R (OqSU2Rel q) x
  induction y using FreeAlgebra.induction with
  | grade0 r =>
    simp only [Algebra.algebraMap_eq_smul_one]
    simp
  | grade1 i =>
    have hi : RingQuot.mkAlgHom R (OqSU2Rel q) (FreeAlgebra.ι R i) = gen q i := rfl
    rw [hi]
    fin_cases i <;> simp [triRep, counit, diagCharAlgHom]
  | mul a b ha hb =>
    simp only [map_mul, Matrix.mul_apply, Fin.sum_univ_two]
    rw [ha.1, hb.1, ha.2.1, hb.2.1, ha.2.2, hb.2.2]
    refine ⟨by ring, by ring, by ring⟩
  | add a b ha hb =>
    simp only [map_add, Matrix.add_apply]
    rw [ha.1, hb.1, ha.2.1, hb.2.1, ha.2.2, hb.2.2]
    exact ⟨by ring, rfl, rfl⟩

/-- The corner functional `x ↦ triRep(x)₀₁`. -/
noncomputable def triFun (s0 sp sm : R) : OqSU2 R q →ₗ[R] R where
  toFun x := triRep q s0 sp sm x 0 1
  map_add' x y := by simp
  map_smul' r x := by simp

theorem triFun_apply (s0 sp sm : R) (x : OqSU2 R q) :
    triFun q s0 sp sm x = triRep q s0 sp sm x 0 1 := rfl

@[simp] theorem triFun_alpha (s0 sp sm : R) : triFun q s0 sp sm (α q) = s0 := by
  simp [triFun_apply, triRep]
@[simp] theorem triFun_beta (s0 sp sm : R) : triFun q s0 sp sm (β q) = sp := by
  simp [triFun_apply, triRep]
@[simp] theorem triFun_gamma (s0 sp sm : R) : triFun q s0 sp sm (γ q) = sm := by
  simp [triFun_apply, triRep]
@[simp] theorem triFun_delta (s0 sp sm : R) :
    triFun q s0 sp sm (δ q) = -((q : R) * s0) := by
  simp [triFun_apply, triRep]

/-- **The corner is a `χ_{q⁻¹}`-twisted derivation.** -/
theorem triFun_twisted (s0 sp sm : R) (x y : OqSU2 R q) :
    triFun q s0 sp sm (x * y) =
      triFun q s0 sp sm x * diagCharAlgHom q q⁻¹ y + counit q x * triFun q s0 sp sm y := by
  have hx := triRep_shape q s0 sp sm x
  have hy := triRep_shape q s0 sp sm y
  simp only [triFun_apply, map_mul, Matrix.mul_apply, Fin.sum_univ_two]
  rw [hx.2.1, hy.2.2]
  ring

/-- **Classification at twist `χ_{q⁻¹}`.** Every `χ_{q⁻¹}`-twisted derivation is the corner
functional with parameters `(φ α, φ β, φ γ)`. -/
theorem twistedDeriv_eq_triFun (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x y, φ (x * y) = φ x * diagCharAlgHom q q⁻¹ y + counit q x * φ y) :
    φ = triFun q (φ (α q)) (φ (β q)) (φ (γ q)) := by
  have h := twistedDeriv_eq_zero q⁻¹ (φ - triFun q (φ (α q)) (φ (β q)) (φ (γ q)))
    (fun x y => by
      simp only [LinearMap.sub_apply, hφ, triFun_twisted]; ring)
    (by simp) (by simp) (by simp)
  exact sub_eq_zero.mp h

/-! ## 3. The left-invariant fields and their Leibniz twist -/

/-- The left-invariant field `X_s = (id ⊗ triFun s) Δ`. -/
noncomputable def field (s0 sp sm : R) : OqSU2 R q →ₗ[R] OqSU2 R q :=
  leftInvOp q (triFun q s0 sp sm)

/-- **Leibniz twist of the off-diagonal fields.** All three directions share the one-sided
twist `R = (q⁻¹α, qβ, q⁻¹γ, qδ)`, right translation by `χ_{q⁻¹}`. -/
theorem field_leibniz (s0 sp sm : R) (f₁ f₂ : OqSU2 R q) :
    field q s0 sp sm (f₁ * f₂) =
      field q s0 sp sm f₁ * torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ f₂ + f₁ * field q s0 sp sm f₂ := by
  rw [field, leftInvOp_leibniz q _ (diagCharAlgHom q q⁻¹) (triFun_twisted q s0 sp sm),
    rightTrans_diagChar]

theorem field_twist_generators :
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (α q) = (((q⁻¹ : Rˣ) : R)) • α q ∧
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (β q) = (q : R) • β q ∧
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (γ q) = (((q⁻¹ : Rˣ) : R)) • γ q ∧
    torusScaleAlgHom q q⁻¹ q⁻¹⁻¹ (δ q) = (q : R) • δ q := by
  simp [torusScaleAlgHom]

theorem field_alpha (s0 sp sm : R) : field q s0 sp sm (α q) = s0 • α q + sm • β q := by
  simp [field, leftInvOp]
theorem field_beta (s0 sp sm : R) :
    field q s0 sp sm (β q) = sp • α q - ((q : R) * s0) • β q := by
  simp [field, leftInvOp, sub_eq_add_neg]
  exact neg_smul (R := R) (M := OqSU2 R q) _ _
theorem field_gamma (s0 sp sm : R) : field q s0 sp sm (γ q) = s0 • γ q + sm • δ q := by
  simp [field, leftInvOp]
theorem field_delta (s0 sp sm : R) :
    field q s0 sp sm (δ q) = sp • γ q - ((q : R) * s0) • δ q := by
  simp [field, leftInvOp, sub_eq_add_neg]
  exact neg_smul (R := R) (M := OqSU2 R q) _ _

/-- The raising field `X₊ : (α, β, γ, δ) ↦ (0, α, 0, γ)`. -/
noncomputable abbrev fieldPlus : OqSU2 R q →ₗ[R] OqSU2 R q := field q 0 1 0
/-- The lowering field `X₋ : (α, β, γ, δ) ↦ (β, 0, δ, 0)`. -/
noncomputable abbrev fieldMinus : OqSU2 R q →ₗ[R] OqSU2 R q := field q 0 0 1

theorem fieldPlus_generators :
    fieldPlus q (α q) = 0 ∧ fieldPlus q (β q) = α q ∧
      fieldPlus q (γ q) = 0 ∧ fieldPlus q (δ q) = γ q := by
  simp [fieldPlus, field_alpha, field_beta, field_gamma, field_delta]

theorem fieldMinus_generators :
    fieldMinus q (α q) = β q ∧ fieldMinus q (β q) = 0 ∧
      fieldMinus q (γ q) = δ q ∧ fieldMinus q (δ q) = 0 := by
  simp [fieldMinus, field_alpha, field_beta, field_gamma, field_delta]

end QOU.AlgebraicSubstrate.OqSU2
