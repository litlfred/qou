/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.TemperleyLiebDimCatalan
import QOU.SchurWeyl.TraceQuotGeneric

/-!
# `ker(Jimbo) = rad(wtrace)` and `H_{m+1}(q)/rad ≃ₐ TL_{m+1}(q + q⁻¹)` over a generic field

`JimboActionKernel.ker_jimbo_eq_traceRadicalIdeal` identifies the kernel of the Jimbo action
`H_{m+1}(q) → End(V^{⊗(m+1)})`, `dim V = 2`, with the trace radical of the Ocneanu trace — but
only over a **linearly ordered** field: its step `rad ⊆ ker` is positivity of the weighted
trace form `X ↦ Tr(K^{⊗N} X Xᵀ)`.  This file removes the order.  Everything here holds over any
field `K` of characteristic zero, for `q ≠ 0` not a root of unity — in particular over `ℂ`.

## Results

With `π : H_{m+1}(q) →ₐ H_{m+1}(q)/rad(wtrace)` the quotient map and `e_i` the
Temperley–Lieb generators:

* `tlTraceQuotEquiv : TL_{m+1}(q + q⁻¹) ≃ₐ[K] H_{m+1}(q)/rad(wtrace)`, `e_i ↦ π(q − σ_i)`;
  its inverse `traceQuotTLEquiv` sends `π(σ_i) ↦ q − e_i` (`traceQuotTLEquiv_σ`).
  **This is `H/rad ≅ TL`.**
* `ker_jimbo_eq_traceRadicalIdeal_generic` — `ker(jimbo) = rad(wtrace)` as two-sided ideals.
* `jimbo_eq_comp` — the Jimbo action factors as `tlRep ∘ (H/rad ≃ TL) ∘ π`.
* `tlRep_injective` — the Temperley–Lieb representation on `V^{⊗(m+1)}` is **faithful**.
* `finrank_tl_eq_catalan_generic` — `dim TL_{m+1}(q + q⁻¹) = catalan (m+1)`.
* `finrank_range_jimbo_eq_catalan_generic` — `dim (image of jimbo) = catalan (m+1)`.
* `_complex` instances of the three statements over `ℂ`.

## Route (no positivity)

1. `ker ⊆ rad` is formal: `wtrace(x y) = (1+q²)^{-(m+1)} · Tr(K ρ(x) ρ(y))`
   (`jimboTrace_eq_wtrace`, valid over any field), so `ρ(x) = 0` kills every pairing.
2. Hence any relation that holds after applying `ρ` holds in `H/rad`.  The elements
   `q − ρ(σ_i)` are `tlRep (e_i)` (`strandBraid_eq`), and they satisfy the Temperley–Lieb
   relations because `tlRep` is an algebra map out of `TL`.  So `e_i ↦ π(q − σ_i)` defines
   `ψ : TL → H/rad`, and `ψ` is surjective since `π(σ_i) = q − ψ(e_i)`.
3. `dim TL ≤ catalan (m+1)` (Jones normal forms span, any commutative ring) and
   `dim H/rad = catalan (m+1)` (`TraceQuotGeneric`, any `CharZero` field).  A surjection from a
   space of dimension `≤ C` onto one of dimension `C` is bijective.
4. `jimbo = tlRep ∘ ψ⁻¹ ∘ π` on generators, hence everywhere; so `rad = ker π ⊆ ker jimbo`.

The ordered-field argument of `JimboActionKernel` is not used anywhere: its positivity step is
replaced by the dimension count of step 3.

## Scope

* Hypotheses: `[Field K] [CharZero K]`, `q ≠ 0`, `NotRootOfUnity q`.  Steps 1–2
  (`ker ⊆ rad`, the surjection `tlToQuot`) need only `[Field K]`; `CharZero` enters only
  through the dimension of `H/rad`.  `CharZero` is inherited
  from `TraceQuotGeneric.finrank_traceQuot_eq_catalan` (via `heckeProduct`); `q² + 1 ≠ 0` and
  `(q²)^k ≠ 1` are implied by `NotRootOfUnity q`.
* Convention D (`z = q³/(q²+1)`) for `wtrace`, as in `TraceQuotGeneric`.
* At a root of unity nothing is claimed.

-- Ref: [jimbo1986]; [leitner2026] bean qou-cf3m
-/

namespace QOU.SchurWeyl.JimboKernelGeneric

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebDimCatalan
open QOU.SchurWeyl QOU.SchurWeyl.JimboActionKernel
open QOU.QBeta.MarkovTraceQuotient QOU.QBeta.TemperleyLiebTower
open QOU.SchurWeyl.TraceQuotGeneric (hgen_of_notRootOfUnity hq21_of_notRootOfUnity)

/-! ## Step 1: `ker(jimbo) ⊆ rad(wtrace)`, over any field -/

section Formal

variable {K : Type*} [Field K]

/-- **An element acting by zero in the Jimbo representation lies in the trace radical.**
Any field; no ordering. -/
theorem mem_traceRadical_of_jimbo_eq_zero {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) {x : Hecke K q q⁻¹ m}
    (h : jimbo q hq m x = 0) :
    x ∈ traceRadical (⇑(SeminormalRep.wtrace q hq hq2 m)) := by
  intro y
  rw [← jimboTrace_eq_wtrace q hq hq2 (hq21_of_notRootOfUnity hq2)
    (hgen_of_notRootOfUnity hq2), jimboTrace_apply, map_mul, h, zero_mul, qtr_zero, mul_zero]

/-- The two-sided-ideal form of `mem_traceRadical_of_jimbo_eq_zero`. -/
theorem ker_jimbo_le_traceRadicalIdeal {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    TwoSidedIdeal.ker (jimbo q hq m)
      ≤ traceRadicalIdeal (SeminormalRep.wtrace q hq hq2 m)
          (SeminormalRep.wtrace_cyclic q hq hq2 m) := by
  intro x hx
  rw [TwoSidedIdeal.mem_ker] at hx
  rw [mem_traceRadicalIdeal]
  exact mem_traceRadical_of_jimbo_eq_zero hq hq2 m hx

/-- The quotient by the trace radical of the Ocneanu trace. -/
abbrev Quot (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :=
  TraceQuot (SeminormalRep.wtrace q hq hq2 m) (SeminormalRep.wtrace_cyclic q hq hq2 m)

/-- The quotient map `H → H/rad`. -/
noncomputable abbrev proj (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Hecke K q q⁻¹ m →ₐ[K] Quot q hq hq2 m :=
  quotMk (SeminormalRep.wtrace q hq hq2 m) (SeminormalRep.wtrace_cyclic q hq hq2 m)

theorem proj_eq_zero_iff {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (x : Hecke K q q⁻¹ m) :
    proj q hq hq2 m x = 0 ↔ x ∈ traceRadical (⇑(SeminormalRep.wtrace q hq hq2 m)) :=
  quot_eq_zero_iff _ _ x

/-- **Relations that hold after the Jimbo action hold in `H/rad`.** -/
theorem proj_eq_of_jimbo_eq {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) {a b : Hecke K q q⁻¹ m} (h : jimbo q hq m a = jimbo q hq m b) :
    proj q hq hq2 m a = proj q hq hq2 m b := by
  rw [← sub_eq_zero, ← map_sub, proj_eq_zero_iff]
  exact mem_traceRadical_of_jimbo_eq_zero hq hq2 m (by rw [map_sub, h, sub_self])

/-- The Temperley–Lieb element `q − σ_i` of the Hecke algebra. -/
noncomputable def tlE (q : K) (m : ℕ) (i : Fin m) : Hecke K q q⁻¹ m :=
  algebraMap K _ q - Hecke.σ K q q⁻¹ m i

/-- `ρ(q − σ_i) = tlRep(e_i)`. -/
theorem jimbo_tlE {q : K} (hq : q ≠ 0) (m : ℕ) (i : Fin m) :
    jimbo q hq m (tlE q m i)
      = tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq) (e K (q + q⁻¹) adjFin i) := by
  rw [tlE, map_sub, AlgHom.commutes, jimbo_σ, strandBraid_eq (mul_inv_cancel₀ hq), map_add,
    map_smul, AlgHom.commutes, neg_one_smul]
  abel

end Formal

/-! ## Steps 2–4, over a `CharZero` field -/

section Generic

variable {K : Type*} [Field K] [CharZero K]

/-- **The Temperley–Lieb algebra maps onto `H/rad`**, `e_i ↦ π(q − σ_i)`. -/
noncomputable def tlToQuot {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : TLFin K (q + q⁻¹) m →ₐ[K] Quot q hq hq2 m :=
  lift K (q + q⁻¹) adjFin (fun i => proj q hq hq2 m (tlE q m i))
    (fun i => by
      rw [← map_mul, ← AlgHom.commutes (proj q hq hq2 m), ← map_mul]
      apply proj_eq_of_jimbo_eq hq hq2 m
      rw [map_mul, map_mul, AlgHom.commutes, jimbo_tlE, ← map_mul, e_sq, map_mul,
        AlgHom.commutes])
    (fun i j h => by
      rw [← map_mul, ← map_mul]
      apply proj_eq_of_jimbo_eq hq hq2 m
      rw [map_mul, map_mul, jimbo_tlE, jimbo_tlE, ← map_mul, ← map_mul, e_adjacent h])
    (fun i j h => by
      rw [← map_mul, ← map_mul]
      apply proj_eq_of_jimbo_eq hq hq2 m
      rw [map_mul, map_mul, jimbo_tlE, jimbo_tlE, ← map_mul, ← map_mul, e_farCommute h])

omit [CharZero K] in
@[simp] theorem tlToQuot_e {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (i : Fin m) :
    tlToQuot hq hq2 m (e K (q + q⁻¹) adjFin i) = proj q hq hq2 m (tlE q m i) :=
  lift_e _ _ _ _ _ _ _ _

omit [CharZero K] in
/-- Every class `π(x)` lies in the image of `tlToQuot`. -/
theorem proj_mem_range {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (x : Hecke K q q⁻¹ m) :
    proj q hq hq2 m x ∈ AlgHom.range (tlToQuot hq hq2 m) := by
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective K (HeckeRel K q q⁻¹ m) x
  let φ := (proj q hq hq2 m).comp (RingQuot.mkAlgHom K (HeckeRel K q q⁻¹ m))
  have hle : Algebra.adjoin K (Set.range (FreeAlgebra.ι K))
      ≤ (AlgHom.range (tlToQuot hq hq2 m)).comap φ := by
    refine Algebra.adjoin_le ?_
    rintro _ ⟨i, rfl⟩
    show proj q hq hq2 m (Hecke.σ K q q⁻¹ m i) ∈ AlgHom.range (tlToQuot hq hq2 m)
    refine ⟨algebraMap K _ q - e K (q + q⁻¹) adjFin i, ?_⟩
    show tlToQuot hq hq2 m (algebraMap K _ q - e K (q + q⁻¹) adjFin i) = _
    rw [map_sub, AlgHom.commutes, tlToQuot_e, tlE, map_sub, AlgHom.commutes, sub_sub_cancel]
  rw [FreeAlgebra.adjoin_range_ι] at hle
  exact hle (Algebra.mem_top : y ∈ ⊤)

omit [CharZero K] in
theorem proj_surjective {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Surjective (proj q hq hq2 m) := by
  rintro ⟨x⟩
  exact ⟨x, rfl⟩

omit [CharZero K] in
theorem tlToQuot_surjective {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Surjective (tlToQuot hq hq2 m) := by
  intro z
  obtain ⟨x, rfl⟩ := proj_surjective hq hq2 m z
  exact proj_mem_range hq hq2 m x

theorem finrank_quot_eq_catalan {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Module.finrank K (Quot q hq hq2 m) = catalan (m + 1) := by
  exact_mod_cast TraceQuotGeneric.finrank_traceQuot_eq_catalan hq hq2 m

/-- **`dim TL_{m+1}(q + q⁻¹) = catalan (m+1)`** over any `CharZero` field, `q ≠ 0` not a root
of unity. -/
theorem finrank_tl_eq_catalan_generic {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Module.finrank K (TLFin K (q + q⁻¹) m) = catalan (m + 1) := by
  haveI := finite_tlFin (q + q⁻¹) m
  refine le_antisymm (QOU.MathlibExt.TemperleyLiebNormalFormSpanning.finrank_le_catalan _ m) ?_
  rw [← finrank_quot_eq_catalan hq hq2 m, ← finrank_top K (Quot q hq hq2 m),
    ← (LinearMap.range_eq_top (f := (tlToQuot hq hq2 m).toLinearMap)).mpr
      (tlToQuot_surjective hq hq2 m)]
  exact LinearMap.finrank_range_le _

theorem tlToQuot_injective {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Injective (tlToQuot hq hq2 m) := by
  haveI := finite_tlFin (q + q⁻¹) m
  haveI : Module.Finite K (Quot q hq hq2 m) :=
    Module.Finite.of_surjective (tlToQuot hq hq2 m).toLinearMap (tlToQuot_surjective hq hq2 m)
  have h := (LinearMap.injective_iff_surjective_of_finrank_eq_finrank
    (f := (tlToQuot hq hq2 m).toLinearMap)
    (by rw [finrank_tl_eq_catalan_generic hq hq2, finrank_quot_eq_catalan hq hq2])).mpr
    (tlToQuot_surjective hq hq2 m)
  exact h

/-- **`TL_{m+1}(q + q⁻¹) ≃ₐ[K] H_{m+1}(q)/rad(wtrace)`**, `e_i ↦ π(q − σ_i)`, over any
`CharZero` field, `q ≠ 0` not a root of unity. -/
noncomputable def tlTraceQuotEquiv {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    TLFin K (q + q⁻¹) m ≃ₐ[K] Quot q hq hq2 m :=
  AlgEquiv.ofBijective (tlToQuot hq hq2 m)
    ⟨tlToQuot_injective hq hq2 m, tlToQuot_surjective hq hq2 m⟩

/-- **`H_{m+1}(q)/rad(wtrace) ≃ₐ[K] TL_{m+1}(q + q⁻¹)`** (`H/rad ≅ TL`). -/
noncomputable def traceQuotTLEquiv {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Quot q hq hq2 m ≃ₐ[K] TLFin K (q + q⁻¹) m :=
  (tlTraceQuotEquiv hq hq2 m).symm

/-- The isomorphism `H/rad ≃ TL` sends the class of `σ_i` to `q − e_i`. -/
theorem traceQuotTLEquiv_σ {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (i : Fin m) :
    traceQuotTLEquiv hq hq2 m (proj q hq hq2 m (Hecke.σ K q q⁻¹ m i))
      = algebraMap K _ q - e K (q + q⁻¹) adjFin i := by
  rw [traceQuotTLEquiv, AlgEquiv.symm_apply_eq]
  show proj q hq hq2 m (Hecke.σ K q q⁻¹ m i)
    = tlToQuot hq hq2 m (algebraMap K _ q - e K (q + q⁻¹) adjFin i)
  rw [map_sub, AlgHom.commutes, tlToQuot_e, tlE, map_sub, AlgHom.commutes, sub_sub_cancel]

/-- The composite `H → H/rad ≃ TL`: the Temperley–Lieb quotient map `σ_i ↦ q − e_i`. -/
noncomputable def heckeToTLGeneric {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] TLFin K (q + q⁻¹) m :=
  (traceQuotTLEquiv hq hq2 m).toAlgHom.comp (proj q hq hq2 m)

@[simp] theorem heckeToTLGeneric_σ {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (i : Fin m) :
    heckeToTLGeneric hq hq2 m (Hecke.σ K q q⁻¹ m i)
      = algebraMap K _ q - e K (q + q⁻¹) adjFin i :=
  traceQuotTLEquiv_σ hq hq2 m i

/-- **The Jimbo action factors through the Temperley–Lieb algebra**:
`jimbo = tlRep ∘ heckeToTLGeneric`. -/
theorem jimbo_eq_comp {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) :
    jimbo q hq m
      = (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq)).comp (heckeToTLGeneric hq hq2 m) := by
  apply Hecke.hom_ext
  intro i
  rw [AlgHom.comp_apply, heckeToTLGeneric_σ, map_sub, AlgHom.commutes, ← jimbo_tlE hq m i,
    tlE, map_sub, AlgHom.commutes, sub_sub_cancel]

/-- **`ker(jimbo) = rad(wtrace)`** as two-sided ideals, over any `CharZero` field, for
`q ≠ 0` not a root of unity.  Removes the ordered-field hypothesis of
`JimboActionKernel.ker_jimbo_eq_traceRadicalIdeal`. -/
theorem ker_jimbo_eq_traceRadicalIdeal_generic {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    TwoSidedIdeal.ker (jimbo q hq m)
      = traceRadicalIdeal (SeminormalRep.wtrace q hq hq2 m)
          (SeminormalRep.wtrace_cyclic q hq hq2 m) := by
  refine le_antisymm (ker_jimbo_le_traceRadicalIdeal hq hq2 m) ?_
  intro x hx
  rw [mem_traceRadicalIdeal, ← proj_eq_zero_iff hq hq2 m] at hx
  rw [TwoSidedIdeal.mem_ker, jimbo_eq_comp hq hq2 m, AlgHom.comp_apply, heckeToTLGeneric,
    AlgHom.comp_apply, hx, map_zero, map_zero]

/-- Pointwise form: `ρ(x) = 0 ↔ x ∈ rad(wtrace)`. -/
theorem jimbo_eq_zero_iff_wtrace_generic {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo q hq m x = 0 ↔ ∀ y, SeminormalRep.wtrace q hq hq2 m (x * y) = 0 := by
  rw [← TwoSidedIdeal.mem_ker, ker_jimbo_eq_traceRadicalIdeal_generic hq hq2 m,
    mem_traceRadicalIdeal]
  rfl

/-- **The Temperley–Lieb representation on `V^{⊗(m+1)}` is faithful.** -/
theorem tlRep_injective {q : K} (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) : Function.Injective (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq)) := by
  rw [injective_iff_map_eq_zero]
  intro t ht
  obtain ⟨z, rfl⟩ := (traceQuotTLEquiv hq hq2 m).surjective t
  obtain ⟨x, rfl⟩ := proj_surjective hq hq2 m z
  have hj : jimbo q hq m x = 0 := by
    rw [jimbo_eq_comp hq hq2 m]; exact ht
  have hx := (ker_jimbo_le_traceRadicalIdeal hq hq2 m) ((TwoSidedIdeal.mem_ker _).mpr hj)
  rw [mem_traceRadicalIdeal, ← proj_eq_zero_iff hq hq2 m] at hx
  rw [hx, map_zero]

/-- **`dim (image of the Jimbo action) = catalan (m+1)`** over any `CharZero` field. -/
theorem finrank_range_jimbo_eq_catalan_generic {q : K} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Module.finrank K (LinearMap.range (jimbo q hq m).toLinearMap) = catalan (m + 1) := by
  have hsurj : Function.Surjective (heckeToTLGeneric hq hq2 m) := fun t => by
    obtain ⟨z, rfl⟩ := (traceQuotTLEquiv hq hq2 m).surjective t
    obtain ⟨x, rfl⟩ := proj_surjective hq hq2 m z
    exact ⟨x, rfl⟩
  have hrange : LinearMap.range (jimbo q hq m).toLinearMap
      = LinearMap.range (tlRep (R := K) q q⁻¹ m (mul_inv_cancel₀ hq)).toLinearMap := by
    rw [jimbo_eq_comp hq hq2 m, AlgHom.comp_toLinearMap, LinearMap.range_comp_of_range_eq_top]
    exact LinearMap.range_eq_top.mpr hsurj
  rw [hrange, LinearMap.finrank_range_of_inj (tlRep_injective hq hq2 m),
    finrank_tl_eq_catalan_generic hq hq2 m]

end Generic

/-! ## The complex instances -/

theorem ker_jimbo_eq_traceRadicalIdeal_complex {q : ℂ} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    TwoSidedIdeal.ker (jimbo q hq m)
      = traceRadicalIdeal (SeminormalRep.wtrace q hq hq2 m)
          (SeminormalRep.wtrace_cyclic q hq hq2 m) :=
  ker_jimbo_eq_traceRadicalIdeal_generic hq hq2 m

/-- `H_{m+1}(q)/rad ≃ₐ[ℂ] TL_{m+1}(q + q⁻¹)` at complex `q ≠ 0` not a root of unity. -/
noncomputable def traceQuotTLEquivComplex {q : ℂ} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Quot q hq hq2 m ≃ₐ[ℂ] TLFin ℂ (q + q⁻¹) m :=
  traceQuotTLEquiv hq hq2 m

theorem finrank_tl_eq_catalan_complex {q : ℂ} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    Module.finrank ℂ (TLFin ℂ (q + q⁻¹) m) = catalan (m + 1) :=
  finrank_tl_eq_catalan_generic hq hq2 m

end QOU.SchurWeyl.JimboKernelGeneric
