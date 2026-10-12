import QOU.Mass.KZHolonomy.FlatTransport
import QOU.Mass.KZHolonomy.GaudinCommute
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Comp

/-!
# The Knizhnik–Zamolodchikov connection is flat

Let `A` be a normed `ℂ`-algebra, `ρ : Sₙ → A` a representation of the symmetric group,
and `κ, c ∈ ℂ`.  On the configuration space of `n` distinct points of `ℂ`,
`confSet n = {z : Fin n → ℂ | z injective}` (an open subset of `ℂⁿ`), the
*KZ connection form* is

  `ω_κ(z)(u) = κ · Σ_{a,b} (u_a - u_b)/(z_a - z_b) · (ρ(s_ab) - c)`,

where `s_ab` is the transposition of `a` and `b` (the diagonal terms vanish).  We regard
`ω_κ(z)` as a real-linear map of the tangent vector `u ∈ ℂⁿ`, so that it fits the real
framework of flat transport in `FlatTransport.lean`.

We prove:

* `kzForm_isFlatOn`: `ω_κ` is continuously differentiable on `confSet n`, with explicit
  derivative `kzForm'`, and its curvature vanishes: `∂_δ ω(u) - ∂_u ω(δ) = [ω(δ), ω(u)]`.
  The derivative is symmetric in `(δ, u)`, so the left side is zero; the right side is zero
  because the components `ω(u)`, `ω(v)` commute (`kzOp_commute`, the Arnold relation).
* `kzForm_equivariant`: `ρ(π) ω(z∘π)(u∘π) = ω(z)(u) ρ(π)` for every permutation `π`.
* `IsTransport.comp_perm`: consequently, if `U` is the transport along a path `γ`, then
  `ρ(π)⁻¹ U ρ(π)` is the transport along the permuted path `γ ∘ π`.
-/

open Equiv Finset

namespace QOU.Mass.KZHolonomy

variable {n : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]

/-- Configurations of `n` distinct points of `ℂ`. -/
def confSet (n : ℕ) : Set (Fin n → ℂ) := {z | Function.Injective z}

theorem isOpen_confSet (n : ℕ) : IsOpen (confSet n) := by
  have h : confSet n = ⋂ p ∈ {p : Fin n × Fin n | p.1 ≠ p.2}, {z | z p.1 ≠ z p.2} := by
    ext z
    simp only [confSet, Set.mem_setOf_eq, Set.mem_iInter, Function.Injective]
    constructor
    · intro hz p hp h; exact hp (hz h)
    · intro hz a b hab
      by_contra hne
      exact hz (a, b) hne hab
  rw [h]
  exact (Set.toFinite _).isOpen_biInter fun p _ =>
    isOpen_ne_fun (continuous_apply _) (continuous_apply _)

/-- The real-linear form `u ↦ u_a - u_b`. -/
noncomputable def pairDiff (a b : Fin n) : (Fin n → ℂ) →L[ℝ] ℂ :=
  ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℂ) a -
    ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℂ) b

@[simp] lemma pairDiff_apply (a b : Fin n) (u : Fin n → ℂ) : pairDiff a b u = u a - u b := rfl

@[simp] lemma pairDiff_self (a : Fin n) : pairDiff a a = 0 := sub_self _

/-- The residue `ρ(s_ab) - c`. -/
noncomputable def resid (ρ : Equiv.Perm (Fin n) →* A) (c : ℂ) (a b : Fin n) : A :=
  ρ (Equiv.swap a b) - algebraMap ℂ A c

/-- `u ↦ (u_a - u_b) • (ρ(s_ab) - c)`. -/
noncomputable def kzL (ρ : Equiv.Perm (Fin n) →* A) (c : ℂ) (a b : Fin n) :
    (Fin n → ℂ) →L[ℝ] A :=
  (pairDiff a b).smulRight (resid ρ c a b)

@[simp] lemma kzL_apply (ρ : Equiv.Perm (Fin n) →* A) (c : ℂ) (a b : Fin n)
    (u : Fin n → ℂ) :
    kzL ρ c a b u = (u a - u b) • resid ρ c a b := rfl

/-- The KZ connection form `ω_κ(z)(u) = κ Σ_{a,b} (u_a-u_b)/(z_a-z_b) (ρ(s_ab) - c)`,
as a real-linear map in `u`. -/
noncomputable def kzForm (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (z : Fin n → ℂ) :
    (Fin n → ℂ) →L[ℝ] A :=
  ∑ a, ∑ b, (κ * (z a - z b)⁻¹) • kzL ρ c a b

/-- The coefficient `-κ/(z_a - z_b)²` of the derivative of `kzForm`. -/
noncomputable def kzCoeff' (κ : ℂ) (z : Fin n → ℂ) (a b : Fin n) : ℂ :=
  -(κ * ((z a - z b) ^ 2)⁻¹)

/-- The derivative of `kzForm` in `z`:
`ω'(z)(δ)(u) = -κ Σ_{a,b} (δ_a-δ_b)(u_a-u_b)/(z_a-z_b)² (ρ(s_ab) - c)`. -/
noncomputable def kzForm' (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (z : Fin n → ℂ) :
    (Fin n → ℂ) →L[ℝ] (Fin n → ℂ) →L[ℝ] A :=
  ∑ a, ∑ b, (kzCoeff' κ z a b • pairDiff a b).smulRight (kzL ρ c a b)

theorem kzForm_apply (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (z u : Fin n → ℂ) :
    kzForm ρ κ c z u = κ • kzOp ρ c z u := by
  simp only [kzForm, kzOp, ContinuousLinearMap.coe_sum', Finset.sum_apply,
    ContinuousLinearMap.coe_smul', Pi.smul_apply, kzL_apply, Finset.smul_sum, smul_smul,
    dlogPair, resid]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  congr 1
  rw [div_eq_mul_inv]
  ring

lemma kzForm'_apply (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (z δ u : Fin n → ℂ) :
    kzForm' ρ κ c z δ u =
      ∑ a, ∑ b, (kzCoeff' κ z a b * (δ a - δ b) * (u a - u b)) • resid ρ c a b := by
  simp only [kzForm', ContinuousLinearMap.coe_sum', Finset.sum_apply,
    ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.coe_smul', Pi.smul_apply,
    pairDiff_apply, kzL_apply, smul_smul, smul_eq_mul]

lemma kzForm'_symm (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (z δ u : Fin n → ℂ) :
    kzForm' ρ κ c z δ u = kzForm' ρ κ c z u δ := by
  rw [kzForm'_apply, kzForm'_apply]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  rw [mul_right_comm]

lemma hasFDerivAt_kzTerm (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) {y : Fin n → ℂ}
    (a b : Fin n) (hab : a ≠ b → y a ≠ y b) :
    HasFDerivAt (fun z : Fin n → ℂ => (κ * (z a - z b)⁻¹) • kzL ρ c a b)
      ((kzCoeff' κ y a b • pairDiff a b).smulRight (kzL ρ c a b)) y := by
  by_cases h : a = b
  · subst h
    have h0 : (kzCoeff' κ y a a • pairDiff a a).smulRight (kzL ρ c a a) = 0 := by
      ext δ u; simp
    have hf : (fun z : Fin n → ℂ => (κ * (z a - z a)⁻¹) • kzL ρ c a a) = fun _ => 0 :=
      funext fun z => ContinuousLinearMap.ext fun u => by simp
    rw [h0, hf]
    exact hasFDerivAt_const (𝕜 := ℝ) (0 : (Fin n → ℂ) →L[ℝ] A) y
  · have hy : y a - y b ≠ 0 := sub_ne_zero.2 (hab h)
    have hg : HasFDerivAt (fun z : Fin n → ℂ => z a - z b) (pairDiff a b) y :=
      (pairDiff a b).hasFDerivAt
    have hinv : HasFDerivAt (fun z : Fin n → ℂ => κ * (z a - z b)⁻¹)
        ((κ * -((y a - y b) ^ 2)⁻¹) • pairDiff a b) y :=
      HasDerivAt.comp_hasFDerivAt (f := fun z : Fin n → ℂ => z a - z b)
        (h₂ := fun w : ℂ => κ * w⁻¹) y ((hasDerivAt_inv hy).const_mul κ) hg
    have := hinv.smul_const (kzL ρ c a b)
    rwa [mul_neg] at this

/-- Decomposing a complex coefficient into real and imaginary parts. -/
lemma smulRight_smul_eq (w : ℂ) (P : (Fin n → ℂ) →L[ℝ] ℂ)
    (L : (Fin n → ℂ) →L[ℝ] A) :
    (w • P).smulRight L = w.re • P.smulRight L + w.im • (Complex.I • P).smulRight L := by
  refine ContinuousLinearMap.ext fun δ => ContinuousLinearMap.ext fun u => ?_
  simp only [ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.coe_smul',
    Pi.smul_apply, ContinuousLinearMap.add_apply, smul_eq_mul]
  rw [← Complex.coe_smul, ← Complex.coe_smul,
    smul_smul, smul_smul, ← add_smul]
  congr 1
  have := Complex.re_add_im w
  linear_combination (-(P δ)) * this

lemma continuousOn_kzTerm (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (a b : Fin n) :
    ContinuousOn
      (fun z : Fin n → ℂ => (kzCoeff' κ z a b • pairDiff a b).smulRight (kzL ρ c a b))
      (confSet n) := by
  haveI : ContinuousAdd ((Fin n → ℂ) →L[ℝ] (Fin n → ℂ) →L[ℝ] A) :=
    (SeminormedAddCommGroup.toIsTopologicalAddGroup
      (E := (Fin n → ℂ) →L[ℝ] (Fin n → ℂ) →L[ℝ] A)).toContinuousAdd
  have hg : ContinuousOn (fun z : Fin n → ℂ => kzCoeff' κ z a b) (confSet n) := by
    by_cases h : a = b
    · subst h
      simpa [kzCoeff'] using
        (continuousOn_const : ContinuousOn (fun _ : Fin n → ℂ => (0 : ℂ)) _)
    · refine (continuousOn_const.mul (ContinuousOn.inv₀ ?_ ?_)).neg
      · exact (((continuous_apply a).sub (continuous_apply b)).pow 2).continuousOn
      · intro z hz
        exact pow_ne_zero 2 (sub_ne_zero.2 fun he => h (hz he))
  have hfun :
      (fun z : Fin n → ℂ => (kzCoeff' κ z a b • pairDiff a b).smulRight (kzL ρ c a b)) =
      fun z => (kzCoeff' κ z a b).re • (pairDiff a b).smulRight (kzL ρ c a b) +
        (kzCoeff' κ z a b).im • (Complex.I • pairDiff a b).smulRight (kzL ρ c a b) :=
    funext fun z => smulRight_smul_eq _ _ _
  rw [hfun]
  exact ((Complex.continuous_re.comp_continuousOn hg).smul continuousOn_const).add
    ((Complex.continuous_im.comp_continuousOn hg).smul continuousOn_const)

theorem kzForm_isFlatOn (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) :
    IsFlatOn (kzForm ρ κ c) (kzForm' ρ κ c) (confSet n) where
  hasFDerivAt y hy := by
    have : kzForm ρ κ c = fun z => ∑ a, ∑ b, (κ * (z a - z b)⁻¹) • kzL ρ c a b := by
      funext z; rfl
    rw [this]
    exact HasFDerivAt.fun_sum fun a _ => HasFDerivAt.fun_sum fun b _ =>
      hasFDerivAt_kzTerm ρ κ c a b fun h he => h (hy he)
  continuousOn := by
    haveI : ContinuousAdd ((Fin n → ℂ) →L[ℝ] (Fin n → ℂ) →L[ℝ] A) :=
      (SeminormedAddCommGroup.toIsTopologicalAddGroup
      (E := (Fin n → ℂ) →L[ℝ] (Fin n → ℂ) →L[ℝ] A)).toContinuousAdd
    have : kzForm' ρ κ c =
        fun z => ∑ a, ∑ b, (kzCoeff' κ z a b • pairDiff a b).smulRight (kzL ρ c a b) := by
      funext z; rfl
    rw [this]
    exact continuousOn_finset_sum _ fun a _ => continuousOn_finset_sum _ fun b _ =>
      continuousOn_kzTerm ρ κ c a b
  flat y hy u v := by
    rw [kzForm'_symm ρ κ c y u v, sub_self, kzForm_apply, kzForm_apply,
      smul_mul_smul_comm, smul_mul_smul_comm, kzOp_commute ρ c hy u v, sub_self]

theorem kzForm_zero (ρ : Equiv.Perm (Fin n) →* A) (c : ℂ) (z u : Fin n → ℂ) :
    kzForm ρ 0 c z u = 0 := by
  rw [kzForm_apply, zero_smul]

lemma kzOp_equivariant (ρ : Equiv.Perm (Fin n) →* A) (c : ℂ) (π : Equiv.Perm (Fin n))
    (z u : Fin n → ℂ) :
    ρ π * kzOp ρ c (z ∘ π) (u ∘ π) = kzOp ρ c z u * ρ π := by
  have hsw : ∀ a b, ρ π * ρ (Equiv.swap a b) = ρ (Equiv.swap (π a) (π b)) * ρ π := by
    intro a b
    rw [Equiv.swap_apply_apply, ← map_mul, ← map_mul]
    congr 1
    group
  simp only [kzOp, Finset.mul_sum, Finset.sum_mul]
  conv_rhs => rw [← Equiv.sum_comp π]
  refine Finset.sum_congr rfl fun a _ => ?_
  conv_rhs => rw [← Equiv.sum_comp π]
  refine Finset.sum_congr rfl fun b _ => ?_
  have hd : dlogPair (z ∘ π) (u ∘ π) a b = dlogPair z u (π a) (π b) := rfl
  rw [hd, mul_smul_comm, smul_mul_assoc, mul_sub, sub_mul, hsw,
    (Algebra.commutes c (ρ π)).symm]

theorem kzForm_equivariant (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (π : Equiv.Perm (Fin n))
    (z u : Fin n → ℂ) :
    ρ π * kzForm ρ κ c (z ∘ π) (u ∘ π) = kzForm ρ κ c z u * ρ π := by
  rw [kzForm_apply, kzForm_apply, mul_smul_comm, smul_mul_assoc, kzOp_equivariant]

lemma kzForm_comp_perm (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) (π : Equiv.Perm (Fin n))
    (z u : Fin n → ℂ) :
    kzForm ρ κ c (z ∘ π) (u ∘ π) = ρ π⁻¹ * kzForm ρ κ c z u * ρ π := by
  have h1 : ρ π⁻¹ * ρ π = 1 := by rw [← map_mul, inv_mul_cancel, map_one]
  rw [mul_assoc, ← kzForm_equivariant, ← mul_assoc, h1, one_mul]

theorem IsTransport.comp_perm {ρ : Equiv.Perm (Fin n) →* A} {κ c : ℂ}
    (π : Equiv.Perm (Fin n)) {γ γ' : ℝ → Fin n → ℂ} {U : ℝ → A}
    (hU : IsTransport (kzForm ρ κ c) γ γ' U) :
    IsTransport (kzForm ρ κ c) (fun t => γ t ∘ π) (fun t => γ' t ∘ π)
      (fun t => ρ π⁻¹ * U t * ρ π) := by
  have h1 : ρ π⁻¹ * ρ π = 1 := by rw [← map_mul, inv_mul_cancel, map_one]
  have h2 : ρ π * ρ π⁻¹ = 1 := by rw [← map_mul, mul_inv_cancel, map_one]
  refine ⟨?_, fun t ht => ?_⟩
  · simp only [hU.1, mul_one, h1]
  · refine (((hU.2 t ht).const_mul (ρ π⁻¹)).mul_const (ρ π)).congr_deriv ?_
    show ρ π⁻¹ * (kzForm ρ κ c (γ t) (γ' t) * U t) * ρ π =
      kzForm ρ κ c (γ t ∘ π) (γ' t ∘ π) * (ρ π⁻¹ * U t * ρ π)
    rw [kzForm_comp_perm]
    symm
    calc ρ π⁻¹ * kzForm ρ κ c (γ t) (γ' t) * ρ π * (ρ π⁻¹ * U t * ρ π)
        = ρ π⁻¹ * kzForm ρ κ c (γ t) (γ' t) * (ρ π * ρ π⁻¹) * U t * ρ π := by
          simp only [mul_assoc]
      _ = ρ π⁻¹ * (kzForm ρ κ c (γ t) (γ' t) * U t) * ρ π := by
          rw [h2, mul_one]; simp only [mul_assoc]

end QOU.Mass.KZHolonomy
