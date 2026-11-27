import HeckeTemperleyLieb.IwahoriHecke

/-!
# QOU.Hecke.HeckeLanglandsDual — `H_n(q) ≅ H_n(q⁻¹)` for every `n`

The type-`A` core of `conj:quantum-langlands-dual`, for **every** strand count.
Until now the corpus proved it only for `H_3`, in normal-form coordinates
(`QOU.Conjectures.langlandsDualH3UnitsInvEquiv`).  Here it is proved on the
presentation `IwahoriHecke K q n` (`σ_i² = (q - 1)σ_i + q`, braid, far
commutation), over any commutative ring `K` in which `q` is a unit.

## What is proved

* `liftFamily` / `algHom_ext` — the universal property of the presentation: a
  family in a `K`-algebra satisfying the three relations defines a unique
  algebra map out of `H_n(q)`.
* `isHeckeFamily_rescale` — if `s` satisfies the relations at `q` and
  `a * q = 1`, then `-(a • s)` satisfies them at `a`.
* `isHeckeFamily_σInv` — the inverses `σ_i⁻¹` satisfy the relations at `q⁻¹`.
* `rescaleEquiv : H_n(q⁻¹) ≃ₐ[K] H_n(q)`, `σ_i ↦ -q⁻¹ σ_i`.
* `inverseEquiv : H_n(q⁻¹) ≃ₐ[K] H_n(q)`, `σ_i ↦ σ_i⁻¹`.
* `theta : H_n(q) ≃ₐ[K] H_n(q)`, `σ_i ↦ (q - 1) - σ_i`, the composite
  `rescale ∘ inverse⁻¹`; it is an involution (`theta_involutive`).
* `indexChar`, `signChar : H_n(q) →ₐ[K] K` (`σ_i ↦ q`, `σ_i ↦ -1`), and
  `indexChar_comp_theta` — `theta` exchanges them.
* `theta_ne_refl` — **the `ℤ/2` is non-trivial**: for `n ≥ 1` and `q + 1 ≠ 0`
  over a nontrivial ring, `theta` is not the identity.
* `not_algHom_of_inverts_param` — **distinct from the bar involution**: a ring
  endomorphism of `H_n(q)` sending `q·1 ↦ q⁻¹·1` is not `K`-linear unless
  `q = q⁻¹`.  The bar involution is of that kind; every map above is `K`-linear.

All statements are algebraic: no analysis, no limits, no numerical input.

## What is not claimed

The conjecture's two other items — agreement with the reverse limit `q → ∞` and
the non-simply-laced folding — are not touched.  Type `A` is self-dual, so the
algebra-level content of item 3 is exactly the isomorphisms above.
-/

namespace QOU.Hecke.IwahoriHecke

open FreeAlgebra

variable {K : Type*} [CommRing K]

/-! ## The universal property of the presentation -/

section Lift

variable {A : Type*} [Ring A] [Algebra K A]

/-- A family `s : Fin n → A` satisfying the defining relations of `H_n(q)`. -/
structure IsHeckeFamily (q : K) (n : ℕ) (s : Fin n → A) : Prop where
  quadratic : ∀ i, s i * s i = (q - 1) • s i + q • (1 : A)
  braid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
    s i * s ⟨(i : ℕ) + 1, hi⟩ * s i = s ⟨(i : ℕ) + 1, hi⟩ * s i * s ⟨(i : ℕ) + 1, hi⟩
  commute : ∀ i j : Fin n, (j : ℕ) + 2 ≤ (i : ℕ) → s i * s j = s j * s i

theorem lift_rel {q : K} {n : ℕ} {s : Fin n → A} (hs : IsHeckeFamily q n s)
    {x y : FreeAlgebra K (Fin n)} (h : HeckeRel K q n x y) :
    FreeAlgebra.lift K s x = FreeAlgebra.lift K s y := by
  induction h with
  | quadratic i =>
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
      exact hs.quadratic i
  | braid i hi =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hs.braid i hi
  | commute i j hij =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hs.commute i j hij

/-- The algebra map `H_n(q) → A` determined by a Hecke family. -/
noncomputable def liftFamily (q : K) (n : ℕ) (s : Fin n → A) (hs : IsHeckeFamily q n s) :
    IwahoriHecke K q n →ₐ[K] A :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K s, fun _ _ h => lift_rel hs h⟩

@[simp] theorem liftFamily_σ (q : K) (n : ℕ) (s : Fin n → A) (hs : IsHeckeFamily q n s)
    (i : Fin n) : liftFamily q n s hs (σ K q n i) = s i := by
  have h := RingQuot.liftAlgHom_mkAlgHom_apply (S := K)
    (FreeAlgebra.lift K s) (fun _ _ hr => lift_rel hs hr) (FreeAlgebra.ι K i)
  rw [FreeAlgebra.lift_ι_apply] at h
  exact h

/-- Two algebra maps out of `H_n(q)` agreeing on the generators are equal. -/
theorem algHom_ext {q : K} {n : ℕ} {f g : IwahoriHecke K q n →ₐ[K] A}
    (h : ∀ i, f (σ K q n i) = g (σ K q n i)) : f = g := by
  apply RingQuot.ringQuot_ext' (S := K) (s := HeckeRel K q n) f g
  apply FreeAlgebra.hom_ext
  funext i
  exact h i

end Lift

/-! ## Two ways to move the parameter from `q` to `q⁻¹` -/

section Families

variable {A : Type*} [Ring A] [Algebra K A]

/-- **Rescaling.**  If `s` is a Hecke family at `q` and `a * q = 1`, then
    `-(a • s)` is a Hecke family at `a`. -/
theorem isHeckeFamily_rescale {q a : K} {n : ℕ} {s : Fin n → A}
    (hs : IsHeckeFamily q n s) (haq : a * q = 1) :
    IsHeckeFamily a n (fun i => -(a • s i)) where
  quadratic i := by
    have h1 : a * a * (q - 1) = -((a - 1) * a) := by linear_combination a * haq
    have h2 : a * a * q = a := by linear_combination a * haq
    simp only [neg_mul_neg, smul_mul_smul_comm, hs.quadratic i, smul_add, smul_smul, h1,
      h2, smul_neg, neg_smul]
  braid i hi := by
    simp only [neg_mul, mul_neg, neg_neg, smul_mul_smul_comm, hs.braid i hi]
  commute i j hij := by
    simp only [neg_mul_neg, smul_mul_smul_comm, hs.commute i j hij]

/-- The generators of `H_n(q)` form a Hecke family at `q`. -/
theorem isHeckeFamily_σ (q : K) (n : ℕ) : IsHeckeFamily q n (σ K q n) where
  quadratic i := σ_quadratic K q n i
  braid i hi := σ_braid K q n i hi
  commute i j hij := σ_commute K q n i j hij

variable (q : K) [Invertible q] (n : ℕ)

/-- **Inversion.**  The inverses `σ_i⁻¹` form a Hecke family at `q⁻¹`. -/
theorem isHeckeFamily_σInv : IsHeckeFamily (⅟q) n (σInv K q n) where
  quadratic i := by
    -- `(σσ)(yy) = 1`, then expand `σσ` by the quadratic relation.
    set x := σ K q n i
    set y := σInv K q n i
    have hxy : x * y = 1 := σ_mul_σInv K q n i
    have hxxyy : x * x * (y * y) = 1 := by
      rw [mul_assoc, ← mul_assoc x y y, hxy, one_mul, hxy]
    rw [σ_quadratic, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul, ← mul_assoc, hxy,
      one_mul] at hxxyy
    -- `hxxyy : (q - 1) • y + q • (y * y) = 1`
    have hyy : y * y = ⅟q • (1 : IwahoriHecke K q n) - (⅟q * (q - 1)) • y := by
      have := congrArg (fun z => ⅟q • z) hxxyy
      simp only [smul_add, smul_smul, invOf_mul_self, one_smul] at this
      rw [← this]; abel
    have hc : -(⅟q * (q - 1)) = ⅟q - 1 := by
      have := invOf_mul_self q; linear_combination -this
    rw [hyy, sub_eq_add_neg, ← neg_smul, hc, add_comm]
  braid i hi := by
    have hb : σUnit K q n i * σUnit K q n ⟨(i : ℕ) + 1, hi⟩ * σUnit K q n i
        = σUnit K q n ⟨(i : ℕ) + 1, hi⟩ * σUnit K q n i * σUnit K q n ⟨(i : ℕ) + 1, hi⟩ :=
      Units.ext (σ_braid K q n i hi)
    have := congrArg (fun u : (IwahoriHecke K q n)ˣ => ((u⁻¹ : (IwahoriHecke K q n)ˣ) :
      IwahoriHecke K q n)) hb
    simpa only [mul_inv_rev, Units.val_mul, mul_assoc] using this
  commute i j hij := by
    have hc : σUnit K q n i * σUnit K q n j = σUnit K q n j * σUnit K q n i :=
      Units.ext (σ_commute K q n i j hij)
    have := congrArg (fun u : (IwahoriHecke K q n)ˣ => ((u⁻¹ : (IwahoriHecke K q n)ˣ) :
      IwahoriHecke K q n)) hc
    simpa only [mul_inv_rev, Units.val_mul] using this.symm

end Families

/-! ## The isomorphisms -/

section Equivs

variable (q : K) [Invertible q] (n : ℕ)

/-- `H_n(q⁻¹) → H_n(q)`, `σ_i ↦ -q⁻¹ σ_i`. -/
noncomputable def rescaleHom : IwahoriHecke K (⅟q) n →ₐ[K] IwahoriHecke K q n :=
  liftFamily (⅟q) n _ (isHeckeFamily_rescale (isHeckeFamily_σ q n) (invOf_mul_self q))

/-- `H_n(q) → H_n(q⁻¹)`, `σ_i ↦ -q σ_i`. -/
noncomputable def rescaleHomInv : IwahoriHecke K q n →ₐ[K] IwahoriHecke K (⅟q) n :=
  liftFamily q n _ (isHeckeFamily_rescale (isHeckeFamily_σ (⅟q) n) (mul_invOf_self q))

/-- **Quantum Langlands dual, rescaling form.**  `H_n(q⁻¹) ≃ₐ[K] H_n(q)` for every
    `n`, sending `σ_i ↦ -q⁻¹ σ_i`. -/
noncomputable def rescaleEquiv : IwahoriHecke K (⅟q) n ≃ₐ[K] IwahoriHecke K q n :=
  AlgEquiv.ofAlgHom (rescaleHom q n) (rescaleHomInv q n)
    (algHom_ext fun i => by
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, rescaleHomInv, rescaleHom,
        liftFamily_σ, map_neg, map_smul, smul_neg, neg_neg, smul_smul,
        mul_invOf_self, one_smul])
    (algHom_ext fun i => by
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, rescaleHomInv, rescaleHom,
        liftFamily_σ, map_neg, map_smul, smul_neg, neg_neg, smul_smul, invOf_mul_self,
        one_smul])

@[simp] theorem rescaleEquiv_σ (i : Fin n) :
    rescaleEquiv q n (σ K (⅟q) n i) = -(⅟q • σ K q n i) := by
  simp [rescaleEquiv, rescaleHom]

/-- An algebra map sending `x` to `y` sends a two-sided inverse of `x` to the
    two-sided inverse of `y`. -/
private theorem map_inverse_of {B C : Type*} [Ring B] [Ring C] [Algebra K B] [Algebra K C]
    (f : B →ₐ[K] C) {x x' : B} {y y' : C} (hx : x' * x = 1) (hy : y * y' = 1)
    (hfx : f x = y) : f x' = y' := by
  calc f x' = f x' * (y * y') := by rw [hy, mul_one]
    _ = f (x' * x) * y' := by rw [map_mul, hfx, mul_assoc]
    _ = y' := by rw [hx, map_one, one_mul]

/-- `H_n(q⁻¹) → H_n(q)`, `σ_i ↦ σ_i⁻¹`. -/
noncomputable def inverseHom : IwahoriHecke K (⅟q) n →ₐ[K] IwahoriHecke K q n :=
  liftFamily (⅟q) n _ (isHeckeFamily_σInv q n)

/-- `H_n(q) → H_n(q⁻¹)`, `σ_i ↦ σ_i⁻¹`. -/
noncomputable def inverseHomInv : IwahoriHecke K q n →ₐ[K] IwahoriHecke K (⅟q) n :=
  liftFamily q n _ ((invOf_invOf q) ▸ isHeckeFamily_σInv (⅟q) n)

theorem inverseHomInv_σ (i : Fin n) :
    inverseHomInv q n (σ K q n i) = σInv K (⅟q) n i := by
  simp [inverseHomInv]

/-- **Quantum Langlands dual, inversion form.**  `H_n(q⁻¹) ≃ₐ[K] H_n(q)` for every
    `n`, sending `σ_i ↦ σ_i⁻¹`. -/
noncomputable def inverseEquiv : IwahoriHecke K (⅟q) n ≃ₐ[K] IwahoriHecke K q n :=
  AlgEquiv.ofAlgHom (inverseHom q n) (inverseHomInv q n)
    (algHom_ext fun i => by
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq]
      rw [inverseHomInv_σ]
      exact map_inverse_of (inverseHom q n) (σInv_mul_σ K (⅟q) n i) (σInv_mul_σ K q n i)
        (by simp [inverseHom]))
    (algHom_ext fun i => by
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, inverseHom, liftFamily_σ]
      exact map_inverse_of (inverseHomInv q n) (σInv_mul_σ K q n i)
        (σInv_mul_σ K (⅟q) n i) (inverseHomInv_σ q n i))

@[simp] theorem inverseEquiv_σ (i : Fin n) :
    inverseEquiv q n (σ K (⅟q) n i) = σInv K q n i := by
  simp [inverseEquiv, inverseHom]

/-! ## The non-trivial involution `θ` -/

/-- `-(q • σ_i⁻¹) = (q - 1) - σ_i`. -/
theorem neg_smul_σInv (i : Fin n) :
    -(q • σInv K q n i) = (q - 1) • (1 : IwahoriHecke K q n) - σ K q n i := by
  simp only [σInv, smul_smul, mul_invOf_self, one_smul, neg_sub]

/-- `σ_i ↦ (q - 1) - σ_i` is a Hecke family at `q`. -/
theorem isHeckeFamily_theta :
    IsHeckeFamily q n (fun i => (q - 1) • (1 : IwahoriHecke K q n) - σ K q n i) := by
  have h := isHeckeFamily_rescale (isHeckeFamily_σInv q n) (mul_invOf_self q)
  simp only [neg_smul_σInv] at h
  exact h

/-- `θ : H_n(q) → H_n(q)`, `σ_i ↦ (q - 1) - σ_i`. -/
noncomputable def thetaHom : IwahoriHecke K q n →ₐ[K] IwahoriHecke K q n :=
  liftFamily q n _ (isHeckeFamily_theta q n)

@[simp] theorem thetaHom_σ (i : Fin n) :
    thetaHom q n (σ K q n i) = (q - 1) • (1 : IwahoriHecke K q n) - σ K q n i := by
  simp [thetaHom]

theorem thetaHom_involutive : (thetaHom q n).comp (thetaHom q n) = AlgHom.id K _ :=
  algHom_ext fun i => by
    rw [AlgHom.comp_apply, thetaHom_σ, map_sub, map_smul, map_one, thetaHom_σ,
      AlgHom.id_apply, sub_sub_cancel]

/-- **The `ℤ/2` duality as an automorphism of `H_n(q)`.**  `θ` is an involutive
    algebra automorphism, `σ_i ↦ (q - 1) - σ_i`. -/
noncomputable def theta : IwahoriHecke K q n ≃ₐ[K] IwahoriHecke K q n :=
  AlgEquiv.ofAlgHom (thetaHom q n) (thetaHom q n) (thetaHom_involutive q n)
    (thetaHom_involutive q n)

@[simp] theorem theta_σ (i : Fin n) :
    theta q n (σ K q n i) = (q - 1) • (1 : IwahoriHecke K q n) - σ K q n i :=
  thetaHom_σ q n i

/-- `θ` is the composite of the two dualities: `rescale ∘ inverse⁻¹`. -/
theorem theta_eq_trans :
    theta q n = (inverseEquiv q n).symm.trans (rescaleEquiv q n) := by
  apply AlgEquiv.coe_algHom_injective
  apply algHom_ext
  intro i
  change theta q n (σ K q n i) = rescaleEquiv q n ((inverseEquiv q n).symm (σ K q n i))
  have hinv : (inverseEquiv q n).symm (σ K q n i) = σInv K (⅟q) n i := by
    rw [AlgEquiv.symm_apply_eq]
    exact (map_inverse_of (inverseEquiv q n).toAlgHom (x := σ K (⅟q) n i)
      (x' := σInv K (⅟q) n i) (y := σInv K q n i) (y' := σ K q n i)
      (σInv_mul_σ K (⅟q) n i) (σInv_mul_σ K q n i) (inverseEquiv_σ q n i)).symm
  have hr := map_inverse_of (rescaleEquiv q n).toAlgHom (x := σ K (⅟q) n i)
    (x' := σInv K (⅟q) n i) (y := -(⅟q • σ K q n i)) (y' := -(q • σInv K q n i))
    (σInv_mul_σ K (⅟q) n i)
    (by rw [neg_mul_neg, smul_mul_smul_comm, invOf_mul_self, one_smul, σ_mul_σInv])
    (rescaleEquiv_σ q n i)
  rw [hinv, theta_σ, ← neg_smul_σInv]
  exact hr.symm

end Equivs

/-! ## Characters, and why `θ` is not the identity -/

section Characters

variable (q : K) (n : ℕ)

/-- The index character `σ_i ↦ q`. -/
noncomputable def indexChar : IwahoriHecke K q n →ₐ[K] K :=
  liftFamily q n (fun _ => q) {
    quadratic := fun _ => by simp only [smul_eq_mul, mul_one]; ring
    braid := fun _ _ => rfl
    commute := fun _ _ _ => rfl }

/-- The sign character `σ_i ↦ -1`. -/
noncomputable def signChar : IwahoriHecke K q n →ₐ[K] K :=
  liftFamily q n (fun _ => -1) {
    quadratic := fun _ => by simp only [smul_eq_mul, mul_one]; ring
    braid := fun _ _ => rfl
    commute := fun _ _ _ => rfl }

@[simp] theorem indexChar_σ (i : Fin n) : indexChar q n (σ K q n i) = q := by
  simp [indexChar]

@[simp] theorem signChar_σ (i : Fin n) : signChar q n (σ K q n i) = -1 := by
  simp [signChar]

/-- **`θ` exchanges the index and sign characters.** -/
theorem indexChar_comp_theta [Invertible q] :
    (indexChar q n).comp (theta q n).toAlgHom = signChar q n :=
  algHom_ext fun i => by
    change indexChar q n (theta q n (σ K q n i)) = signChar q n (σ K q n i)
    rw [theta_σ, map_sub, map_smul, map_one, indexChar_σ, signChar_σ, smul_eq_mul, mul_one]
    ring

/-- **The `ℤ/2` duality is non-trivial.**  For `n ≥ 1` and `q + 1 ≠ 0`, `θ` is not
    the identity. -/
theorem theta_ne_refl [Invertible q] (hn : 0 < n) (hq : q + 1 ≠ 0) :
    theta q n ≠ AlgEquiv.refl := by
  intro h
  have := congrArg (fun e : IwahoriHecke K q n ≃ₐ[K] IwahoriHecke K q n =>
    indexChar q n (e (σ K q n ⟨0, hn⟩))) h
  have hr : (AlgEquiv.refl : IwahoriHecke K q n ≃ₐ[K] IwahoriHecke K q n)
      (σ K q n ⟨0, hn⟩) = σ K q n ⟨0, hn⟩ := rfl
  simp only [theta_σ, map_sub, map_smul, map_one, indexChar_σ, smul_eq_mul, mul_one, hr] at this
  exact hq (by linear_combination -this)

/-- **Distinct from the bar involution.**  A ring endomorphism of `H_n(q)` that
    sends `q • 1` to `q⁻¹ • 1` — as the bar involution does — is not `K`-linear
    unless `q = q⁻¹`.  Every isomorphism in this file is `K`-linear. -/
theorem not_algHom_of_inverts_param [Invertible q]
    (φ : IwahoriHecke K q n →+* IwahoriHecke K q n)
    (hφ : φ (q • (1 : IwahoriHecke K q n)) = ⅟q • (1 : IwahoriHecke K q n))
    (hq : q ≠ ⅟q) :
    ¬ ∃ f : IwahoriHecke K q n →ₐ[K] IwahoriHecke K q n, f.toRingHom = φ := by
  rintro ⟨f, rfl⟩
  have h1 : f (q • (1 : IwahoriHecke K q n)) = q • 1 := by rw [map_smul, map_one]
  have h2 : (q • (1 : IwahoriHecke K q n)) = ⅟q • 1 := h1.symm.trans hφ
  have := congrArg (indexChar q n) h2
  simp only [map_smul, map_one, smul_eq_mul, mul_one] at this
  exact hq this

end Characters

end QOU.Hecke.IwahoriHecke

