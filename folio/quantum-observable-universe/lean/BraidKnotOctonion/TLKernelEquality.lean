import BraidKnotOctonion.TLKernelConvention
import BraidKnotOctonion.JimboKernelGeneric

/-!
# The Hecke trace radical IS the Temperley–Lieb kernel, after the twist `θ`

`TLKernelConvention` showed that the pulled-back Temperley–Lieb kernel `tlKernelPulled` is
**not** contained in `rad(wtrace)` (`tlKernelPulled_not_le_rad`), and defined the involution
`θ : σ_i ↦ (q - q⁻¹) - σ_i = -σ_i⁻¹`.  This file proves that the two ideals agree exactly up
to `θ`:

    x ∈ rad(wtrace)  ↔  θ x ∈ tlKernelPulled           (`theta_mem_tlKernelPulled_iff`)
    y ∈ tlKernelPulled  ↔  θ y ∈ rad(wtrace)           (`mem_tlKernelPulled_iff`)

over any field of characteristic zero, for `q ≠ 0` not a root of unity.

## Route

No new mathematics: the corpus already has `H/rad ≃ₐ TL`
(`JimboKernelGeneric.traceQuotTLEquiv`, from a dimension count), and its composite with the
quotient map, `heckeToTLGeneric`, sends `σ_i ↦ q - e_i`.  The skein quotient map twisted by
`θ` sends `σ_i ↦ (q - q⁻¹) - (e_i - q⁻¹) = q - e_i` as well (`skeinToTL_theta_σ`).  Two algebra
maps out of `H` that agree on generators are equal (`skeinToTL_comp_theta`), so their kernels
coincide, and the kernel of `heckeToTLGeneric` is `rad(wtrace)` because the second factor is an
isomorphism.

So the convention collision recorded in `rem:hecke-radical-is-temperley-lieb` is resolved: the
corpus's `H/rad ≅ TL` is the `e_i ↦ q - σ_i` presentation, which is the `θ`-twist of the
`U_i = T_i + 1` presentation used by `HeckeToTemperleyLieb` and `TLCarrierBridge`.

Purely algebraic.
-/

namespace QOU.IwahoriHecke.TLKernelEquality

open QOU.SchurWeyl QOU.SchurWeyl.JimboKernelGeneric
open QOU.MathlibExt.HeckeToTemperleyLieb QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.CoxeterCarrier
open QOU.IwahoriHecke.TLCarrierBridge QOU.IwahoriHecke.TLKernelConvention
open QOU.QBeta.TemperleyLiebTower

variable {K : Type*} [Field K]

/-- The skein quotient map sends `σ_i` to `e_i - q⁻¹`. -/
theorem skeinToTL_σ {q : K} (hq0 : q ≠ 0) (n : ℕ) (i : Fin n) :
    skeinToTL hq0 n (δ := q + q⁻¹) (by field_simp) (Hecke.σ K q q⁻¹ n i)
      = e K (q + q⁻¹) adjFin i - algebraMap K _ q⁻¹ := by
  show heckeToTL _ (isTypeADiagram_AMat n) (skeinCoxeterEquiv q hq0 n (Hecke.σ K q q⁻¹ n i)) = _
  rw [skeinCoxeterEquiv_σ, map_smul, heckeToTL_T, u, smul_sub, smul_smul, inv_mul_cancel₀ hq0,
    one_smul, Algebra.algebraMap_eq_smul_one]

/-- **After `θ`, the skein quotient map sends `σ_i` to `q - e_i`** — the generator image of
`heckeToTLGeneric`. -/
theorem skeinToTL_theta_σ {q : K} (hq0 : q ≠ 0) (n : ℕ) (i : Fin n) :
    skeinToTL hq0 n (δ := q + q⁻¹) (by field_simp) (theta q hq0 n (Hecke.σ K q q⁻¹ n i))
      = algebraMap K _ q - e K (q + q⁻¹) adjFin i := by
  rw [theta_σ, map_sub, map_smul, map_one, skeinToTL_σ, Algebra.algebraMap_eq_smul_one,
    Algebra.algebraMap_eq_smul_one]
  module

variable [CharZero K]

/-- **The `θ`-twisted skein quotient map is `heckeToTLGeneric`.** -/
theorem skeinToTL_comp_theta {q : K} (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) :
    (skeinToTL hq0 n (δ := q + q⁻¹) (by field_simp)).comp (theta q hq0 n)
      = heckeToTLGeneric hq0 hq2 n := by
  apply Hecke.hom_ext
  intro i
  rw [AlgHom.comp_apply, skeinToTL_theta_σ, heckeToTLGeneric_σ]

/-- `heckeToTLGeneric x = 0` exactly on the trace radical. -/
theorem heckeToTLGeneric_eq_zero_iff {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    heckeToTLGeneric hq0 hq2 n x = 0
      ↔ x ∈ traceRadical (⇑(SeminormalRep.wtrace q hq0 hq2 n)) := by
  rw [← proj_eq_zero_iff hq0 hq2 n x]
  show (traceQuotTLEquiv hq0 hq2 n) (proj q hq0 hq2 n x) = 0 ↔ _
  exact map_eq_zero_iff _ (traceQuotTLEquiv hq0 hq2 n).injective

/-- **`x ∈ rad(wtrace) ↔ θ x ∈ tlKernelPulled`**, for every `δ` with `q δ = q² + 1`. -/
theorem theta_mem_tlKernelPulled_iff {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {δ : K} (hδ : q * δ = q ^ 2 + 1) (n : ℕ)
    (x : Hecke K q q⁻¹ n) :
    theta q hq0 n x ∈ tlKernelPulled hq0 n hδ
      ↔ x ∈ traceRadical (⇑(SeminormalRep.wtrace q hq0 hq2 n)) := by
  obtain rfl : δ = q + q⁻¹ := by
    field_simp
    linear_combination hδ
  rw [tlKernelPulled, TwoSidedIdeal.mem_ker, ← heckeToTLGeneric_eq_zero_iff hq0 hq2 n x,
    ← skeinToTL_comp_theta hq0 hq2 n]
  rfl

/-- **`tlKernelPulled = θ(rad(wtrace))`**: `y` is in the pulled-back Temperley–Lieb kernel
exactly when `θ y` is in the trace radical. -/
theorem mem_tlKernelPulled_iff {q : K} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {δ : K} (hδ : q * δ = q ^ 2 + 1) (n : ℕ)
    (y : Hecke K q q⁻¹ n) :
    y ∈ tlKernelPulled hq0 n hδ
      ↔ theta q hq0 n y ∈ traceRadical (⇑(SeminormalRep.wtrace q hq0 hq2 n)) := by
  rw [← theta_mem_tlKernelPulled_iff hq0 hq2 hδ n, theta_theta]

/-- **`θ(tlKernelPulled) ⊆ rad(wtrace)`** — the twisted inclusion, as a corollary. -/
theorem theta_mem_rad {q : K} (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {δ : K} (hδ : q * δ = q ^ 2 + 1) (n : ℕ) {x : Hecke K q q⁻¹ n}
    (hx : x ∈ tlKernelPulled hq0 n hδ) :
    theta q hq0 n x ∈ traceRadical (⇑(SeminormalRep.wtrace q hq0 hq2 n)) :=
  (mem_tlKernelPulled_iff hq0 hq2 hδ n x).mp hx

end QOU.IwahoriHecke.TLKernelEquality
