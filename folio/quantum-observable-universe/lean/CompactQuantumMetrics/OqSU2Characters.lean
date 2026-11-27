import CompactQuantumMetrics.OqSU2HaarState

/-!
# Characters of `O_q(SU(2))`: the points of `Aut⊗(τ)` are the torus

Over a commutative ring `R`, a point of the tensor-automorphism group `Aut⊗(τ)` of the
fibre functor of `Rep(SU_q(2))` is an `R`-algebra character
`χ : O_q(SU(2)) →ₐ[R] R` (Tannaka–Krein: `O_q(SU(2))` is the coend of `τ`, and a
monoidal natural automorphism of `τ` is a group-like element of its dual, i.e. a
character). Group law: convolution `χ₁ ⋆ χ₂ = μ ∘ (χ₁ ⊗ χ₂) ∘ Δ`.

This file proves, with no analysis and no empirical input:

* `char_eq_diagChar`: if `q² − 1` is a unit of `R`, **every** character is diagonal,
  `χ = χ_u : (α, β, γ, δ) ↦ (u, 0, 0, u⁻¹)` for a unique `u ∈ Rˣ`.
* `diagChar_injective`, `charConv_diagChar`: `u ↦ χ_u` is injective and turns
  multiplication in `Rˣ` into convolution.
* `charEquivUnits`: hence `(O_q(SU(2)) →ₐ[R] R) ≃ Rˣ`, the group `G_m(R)` of the
  maximal torus. So for `q² ≠ 1` the group `Aut⊗(τ)(R)` is the torus, **not**
  `SL₂(R)`: the map `Aut⊗(τ) → G` is the inclusion of the maximal torus, and the whole
  quantum group exists only as the Hopf algebra (the coend), not as a group of points.
* `exists_nondiag_char_at_one`: the hypothesis is sharp. At `q = 1` the algebra is
  commutative and has the non-diagonal character `(1, 1, 0, 1)` (a unipotent point of
  `SL₂`), recovering classical Tannaka, `Aut⊗(τ)(R) = SL₂(R)`.
* `haarState_rightTrans_char`, `haarState_leftTrans_char`: over a field with `q² ≠ 1`,
  the Haar state is invariant under left and right translation by **every** point of
  `Aut⊗(τ)`, not only the diagonal ones it was built to respect.

## Not established

* `Aut⊗(τ)` itself as a category-theoretic object: `QuantumUniverse.fibreFunctor`
  is a bare functor to `Type` and `QuantumUniverse.gaugeGroup` is `τ ≅ τ` with no monoidal
  constraint. The identification "points of `Aut⊗(τ)` = characters of the coend" is the
  Tannaka–Krein dictionary, which the corpus still carries as an axiom
  (`tannaka_krein_reconstruction`). The theorems here are about characters.
* Haar as the projection onto the trivial Peter–Weyl block (needs coends).

References: S. L. Woronowicz (1987); A. Klimyk & K. Schmüdgen (1997) §4.1.
-- Ref: [woronowicz1987]
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open TensorProduct

variable {R : Type*} [CommRing R]

section classification

variable {q : Rˣ}

/-- If `q² − 1` is a unit then so is `q − 1`. -/
theorem isUnit_sub_one_of_sq (hq : IsUnit ((q : R) ^ 2 - 1)) : IsUnit ((q : R) - 1) := by
  have h : (q : R) ^ 2 - 1 = ((q : R) - 1) * ((q : R) + 1) := by ring
  rw [h] at hq
  exact isUnit_of_mul_isUnit_left hq

/-- The values of a character on the generators satisfy the commutative shadow of the
seven relations. -/
private theorem char_rels (χ : OqSU2 R q →ₐ[R] R) :
    χ (α q) * χ (β q) = (q : R) * (χ (β q) * χ (α q)) ∧
    χ (α q) * χ (γ q) = (q : R) * (χ (γ q) * χ (α q)) ∧
    χ (α q) * χ (δ q) - (q : R) * (χ (β q) * χ (γ q)) = 1 ∧
    χ (δ q) * χ (α q) - ((q⁻¹ : Rˣ) : R) * (χ (β q) * χ (γ q)) = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · have := congrArg χ (rel_ab (R := R) q)
    simpa [map_mul, map_smul, smul_eq_mul] using this
  · have := congrArg χ (rel_ag (R := R) q)
    simpa [map_mul, map_smul, smul_eq_mul] using this
  · have := congrArg χ (rel_det_left (R := R) q)
    simpa [map_mul, map_sub, map_smul, smul_eq_mul] using this
  · have := congrArg χ (rel_det_right (R := R) q)
    simpa [map_mul, map_sub, map_smul, smul_eq_mul] using this

/-- **Classification of characters.** If `q² − 1` is a unit, every character `χ` kills
`β` and `γ`, and `χ(α) χ(δ) = 1`. -/
theorem char_offdiag_zero (hq : IsUnit ((q : R) ^ 2 - 1)) (χ : OqSU2 R q →ₐ[R] R) :
    χ (β q) = 0 ∧ χ (γ q) = 0 ∧ χ (α q) * χ (δ q) = 1 := by
  obtain ⟨hab, hag, hdl, hdr⟩ := char_rels χ
  set a := χ (α q)
  set b := χ (β q)
  set c := χ (γ q)
  set d := χ (δ q)
  have hqq : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := by simp
  -- `(q − q⁻¹) b c = 0`, and `q (q − q⁻¹) = q² − 1` is a unit, so `b c = 0`.
  have hbc0 : ((q : R) ^ 2 - 1) * (b * c) = 0 := by
    linear_combination (-(q : R)) * (hdl - hdr) + (b * c) * hqq
  have hbc : b * c = 0 := (hq.mul_right_eq_zero).mp hbc0
  have had : a * d = 1 := by rw [← hdl, hbc]; ring
  have hq1 := isUnit_sub_one_of_sq hq
  -- `(q − 1) a b = 0`, so `a b = 0`, so `b = d a b = 0`.
  have hab0 : ((q : R) - 1) * (a * b) = 0 := by
    have : ((q : R) - 1) * (a * b) = (q : R) * (b * a) - a * b := by ring
    rw [this, ← hab]; ring
  have hac0 : ((q : R) - 1) * (a * c) = 0 := by
    have : ((q : R) - 1) * (a * c) = (q : R) * (c * a) - a * c := by ring
    rw [this, ← hag]; ring
  have hab' : a * b = 0 := (hq1.mul_right_eq_zero).mp hab0
  have hac' : a * c = 0 := (hq1.mul_right_eq_zero).mp hac0
  refine ⟨?_, ?_, had⟩
  · calc b = (a * d) * b := by rw [had, one_mul]
      _ = d * (a * b) := by ring
      _ = 0 := by rw [hab', mul_zero]
  · calc c = (a * d) * c := by rw [had, one_mul]
      _ = d * (a * c) := by ring
      _ = 0 := by rw [hac', mul_zero]

/-- The unit `u = χ(α)` of a character, when `q² − 1` is a unit. -/
noncomputable def charUnit (hq : IsUnit ((q : R) ^ 2 - 1)) (χ : OqSU2 R q →ₐ[R] R) : Rˣ :=
  Units.mkOfMulEqOne (χ (α q)) (χ (δ q)) (char_offdiag_zero hq χ).2.2

@[simp] theorem charUnit_val (hq : IsUnit ((q : R) ^ 2 - 1)) (χ : OqSU2 R q →ₐ[R] R) :
    (charUnit hq χ : R) = χ (α q) := rfl

/-- **Every character is diagonal** when `q² − 1` is a unit:
`χ = χ_u` with `u = χ(α)`. -/
theorem char_eq_diagChar (hq : IsUnit ((q : R) ^ 2 - 1)) (χ : OqSU2 R q →ₐ[R] R) :
    χ = diagCharAlgHom q (charUnit hq χ) := by
  obtain ⟨hb, hc, had⟩ := char_offdiag_zero hq χ
  have hd : χ (δ q) = (((charUnit hq χ)⁻¹ : Rˣ) : R) := by
    calc χ (δ q)
        = ((((charUnit hq χ)⁻¹ : Rˣ) : R) * ((charUnit hq χ : Rˣ) : R)) * χ (δ q) := by
            rw [Units.inv_mul, one_mul]
      _ = (((charUnit hq χ)⁻¹ : Rˣ) : R) * (χ (α q) * χ (δ q)) := by
            rw [charUnit_val, mul_assoc]
      _ = (((charUnit hq χ)⁻¹ : Rˣ) : R) := by rw [had, mul_one]
  apply algHom_ext <;> simp [diagCharAlgHom, hb, hc, hd]

end classification

/-- `u ↦ χ_u` is injective (over any commutative ring, any `q`). -/
theorem diagChar_injective (q : Rˣ) : Function.Injective (diagCharAlgHom (R := R) q) := by
  intro u v h
  have := congrArg (fun χ : OqSU2 R q →ₐ[R] R => χ (α q)) h
  simp only [diagCharAlgHom, liftQuadruple_alpha] at this
  exact Units.ext this

/-- Convolution of characters, `χ₁ ⋆ χ₂ = μ ∘ (χ₁ ⊗ χ₂) ∘ Δ`: the group law of the points
of `Aut⊗(τ)`. -/
noncomputable def charConv (q : Rˣ) (χ₁ χ₂ : OqSU2 R q →ₐ[R] R) : OqSU2 R q →ₐ[R] R :=
  (Algebra.TensorProduct.lift χ₁ χ₂ (fun _ _ => Commute.all _ _)).comp (coprod q)

/-- `u ↦ χ_u` is a group homomorphism `Rˣ → (characters, ⋆)`. -/
theorem charConv_diagChar (q u v : Rˣ) :
    charConv q (diagCharAlgHom q u) (diagCharAlgHom q v) = diagCharAlgHom (R := R) q (u * v) := by
  apply algHom_ext <;> simp [charConv, diagCharAlgHom, mul_comm]

/-- **Points of `Aut⊗(τ)` are the torus.** When `q² − 1` is a unit, the characters of
`O_q(SU(2))` are in bijection with `Rˣ = G_m(R)` via `u ↦ (u, 0, 0, u⁻¹)`, and the bijection
carries multiplication to convolution (`charConv_diagChar`). -/
noncomputable def charEquivUnits (q : Rˣ) (hq : IsUnit ((q : R) ^ 2 - 1)) :
    (OqSU2 R q →ₐ[R] R) ≃ Rˣ where
  toFun χ := charUnit hq χ
  invFun u := diagCharAlgHom q u
  left_inv χ := (char_eq_diagChar hq χ).symm
  right_inv u := by
    apply Units.ext
    simp [charUnit_val, diagCharAlgHom]

/-- **Sharpness at `q = 1`.** The classical coordinate ring has the non-diagonal character
`(α, β, γ, δ) ↦ (1, 1, 0, 1)`, a unipotent point of `SL₂(R)`; so the torus conclusion needs
`q² ≠ 1`, and at `q = 1` classical Tannaka gives the whole group. -/
theorem exists_nondiag_char_at_one [Nontrivial R] :
    ∃ χ : OqSU2 R (1 : Rˣ) →ₐ[R] R, χ (β 1) ≠ 0 := by
  refine ⟨liftQuadruple (1 : Rˣ) (1 : R) 1 0 1
    { ab := by simp
      ag := by simp
      bd := by simp
      gd := by simp
      bg := by simp
      det_left := by simp
      det_right := by simp }, ?_⟩
  simp

section haar

variable {K : Type*} [Field K] (q : Kˣ)

/-- **Haar is invariant under every point of `Aut⊗(τ)`** (right translation), for
`q² ≠ 1`. -/
theorem haarState_rightTrans_char (hq : (q : K) ^ 2 ≠ 1) (χ : OqSU2 K q →ₐ[K] K)
    (x : OqSU2 K q) : haarState q (rightTrans q χ x) = haarState q x := by
  have hu : IsUnit ((q : K) ^ 2 - 1) := (sub_ne_zero.mpr hq).isUnit
  rw [char_eq_diagChar hu χ]
  exact haarState_rightTrans_diagChar q _ x

/-- **Haar is invariant under every point of `Aut⊗(τ)`** (left translation), for
`q² ≠ 1`. -/
theorem haarState_leftTrans_char (hq : (q : K) ^ 2 ≠ 1) (χ : OqSU2 K q →ₐ[K] K)
    (x : OqSU2 K q) : haarState q (leftTrans q χ x) = haarState q x := by
  have hu : IsUnit ((q : K) ^ 2 - 1) := (sub_ne_zero.mpr hq).isUnit
  rw [char_eq_diagChar hu χ]
  exact haarState_leftTrans_diagChar q _ x

/-- **The modular automorphism is a point of `Aut⊗(τ)` acting on both sides.**
Woronowicz's `σ = (q⁻²α, β, γ, q²δ)` of `haarState_modular` is left translation by the
diagonal character `χ_{q⁻¹}` composed with right translation by the same character:
`σ(x) = χ_{q⁻¹} ⋆ x ⋆ χ_{q⁻¹}`. -/
theorem modularAut_eq_twoSided :
    modularAut q = (leftTrans q (diagCharAlgHom q q⁻¹)).comp
      (rightTrans q (diagCharAlgHom q q⁻¹)) := by
  rw [leftTrans_diagChar, rightTrans_diagChar]
  apply algHom_ext <;> simp [modularAut, torusScaleAlgHom, smul_smul] <;> ring_nf

end haar

end QOU.AlgebraicSubstrate.OqSU2
