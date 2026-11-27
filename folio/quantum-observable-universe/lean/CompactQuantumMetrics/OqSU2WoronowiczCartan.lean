import CompactQuantumMetrics.OqSU2Coproduct
import Mathlib.Tactic.FieldSimp

/-!
# Woronowicz's Cartan vector field on `O_q(SU(2))`

Bean `qou-q3dc`. Woronowicz (1987) builds the 3D left-covariant calculus on
`SU_ν(2)` from functionals `χ₀, χ₁, χ₂` and characters `f₀, f₁, f₂`
(Section 2, eqs. (2.1)–(2.8)). The Cartan direction is `χ₁`, with

* `χ₁(α) = 1`, `χ₁(α*) = −ν²`, and `χ₁` vanishing on `γ`, `γ*` (2.3);
* `f₁(α) = ν⁻²`, `f₁(α*) = ν²`, `f₁(γ) = f₁(γ*) = 0` (2.2);
* `χ₁(ab) = χ₁(a) f₁(b) + e(a) χ₁(b)` (2.7);
* `f₁ = e + ((1 − ν²)/ν²) χ₁` (2.5).

The vector field is `a ↦ χ₁ * a = (id ⊗ χ₁)Φ(a)`, as in his computation of
`χᵢ * α*` in the proof of Thm. 2.1.

**Dictionary.** Woronowicz's fundamental matrix is `((α, −νγ*), (γ, α*))`. In the
corpus presentation `((α, β), (γ, δ))` this is `β = −νγ*`, `δ = α*`, and
`q = ν`. With these, the seven corpus relations are Woronowicz's.

## Results (sorry-free)

* `woronowiczChi1` is `(1 − q⁻²)⁻¹ (ε − f₁)`, with `f₁ = diagCharAlgHom q (q⁻²)`.
  (2.5) solved for `χ₁` gives exactly this.
* `woronowiczChi1_alpha`, `_delta`, `_beta`, `_gamma`: its values match (2.3),
  i.e. `1`, `−q²`, `0`, `0`.
* `woronowiczChi1_leibniz`: (2.7).
* `woronowiczCartanField`: the vector field is the one-sided difference
  `f ↦ (1 − q⁻²)⁻¹ (f − R f)`, where `R` scales `(α, β, γ, δ)` by
  `(q⁻², q², q⁻², q²)`. It obeys `X(fg) = Xf · R g + f · Xg`.

So `u = q⁻²` and `c = 1 − q⁻²`. For Woronowicz's range `0 < ν < 1` the step `c`
is negative. For `q > 1` it is positive.

## Not established

* The sign of the energy budget `−c·φ(Du·Du)`: that needs positivity and the
  `*`-structure, neither used here.
* The off-diagonal fields `χ₀`, `χ₂`.
* Part A of `conj:regularity-breakdown` (bean `qou-pa7n`).

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group. An example of a
  non-commutative differential calculus*, Publ. RIMS 23 (1987) 117–181,
  Section 2, eqs. (2.1)–(2.8), pp. 131–133.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {K : Type*} [Field K] (q : Kˣ)

/-- Woronowicz's character `f₁ = (q⁻², 0, 0, q²)`. -/
noncomputable abbrev woronowiczF1 : OqSU2 K q →ₐ[K] K := diagCharAlgHom q (q⁻¹ ^ 2)

/-- Woronowicz's Cartan functional `χ₁ = (1 − q⁻²)⁻¹ (ε − f₁)`, from his (2.5). -/
noncomputable def woronowiczChi1 : OqSU2 K q →ₗ[K] K :=
  (1 - ((q⁻¹ ^ 2 : Kˣ) : K))⁻¹ • ((counit q).toLinearMap - (woronowiczF1 q).toLinearMap)

variable {q}

theorem one_sub_qinv_sq_ne_zero (hq : (q : K) ^ 2 ≠ 1) : (1 - ((q⁻¹ ^ 2 : Kˣ) : K)) ≠ 0 := by
  intro h
  apply hq
  have h1 : ((q⁻¹ ^ 2 : Kˣ) : K) = 1 := by linear_combination -h
  have h2 : ((q ^ 2 : Kˣ) : K) * ((q⁻¹ ^ 2 : Kˣ) : K) = 1 := by
    rw [← Units.val_mul, ← mul_pow, mul_inv_cancel, one_pow, Units.val_one]
  rw [h1, mul_one] at h2
  simpa using h2

theorem woronowiczChi1_alpha (hq : (q : K) ^ 2 ≠ 1) : woronowiczChi1 q (α q) = 1 := by
  simp only [woronowiczChi1, LinearMap.smul_apply, LinearMap.sub_apply,
    AlgHom.toLinearMap_apply, smul_eq_mul]
  simp [counit, woronowiczF1, diagCharAlgHom]
  have hne := one_sub_qinv_sq_ne_zero hq
  simp only [Units.val_pow_eq_pow_val, Units.val_inv_eq_inv_val, inv_pow] at hne
  exact inv_mul_cancel₀ hne

theorem woronowiczChi1_delta (hq : (q : K) ^ 2 ≠ 1) :
    woronowiczChi1 q (δ q) = -((q : K) ^ 2) := by
  simp only [woronowiczChi1, LinearMap.smul_apply, LinearMap.sub_apply,
    AlgHom.toLinearMap_apply, smul_eq_mul]
  simp [counit, woronowiczF1, diagCharAlgHom]
  have hne := one_sub_qinv_sq_ne_zero hq
  simp only [Units.val_pow_eq_pow_val, Units.val_inv_eq_inv_val, inv_pow] at hne ⊢
  have hq0 : (q : K) ^ 2 ≠ 0 := pow_ne_zero 2 q.ne_zero
  rw [inv_mul_eq_iff_eq_mul₀ hne]
  field_simp
  ring

theorem woronowiczChi1_beta : woronowiczChi1 q (β q) = 0 := by
  simp [woronowiczChi1, counit, woronowiczF1, diagCharAlgHom]

theorem woronowiczChi1_gamma : woronowiczChi1 q (γ q) = 0 := by
  simp [woronowiczChi1, counit, woronowiczF1, diagCharAlgHom]

variable (q)

/-- Woronowicz's (2.7) for `χ₁`. -/
theorem woronowiczChi1_leibniz (x y : OqSU2 K q) :
    woronowiczChi1 q (x * y) =
      woronowiczChi1 q x * woronowiczF1 q y + counit q x * woronowiczChi1 q y :=
  oneSided_twisted q (woronowiczF1 q) _ x y

/-- **Woronowicz's Cartan vector field is a one-sided `q`-difference.** -/
theorem woronowiczCartanField (f₁ f₂ : OqSU2 K q) :
    (∀ f, leftInvOp q (woronowiczChi1 q) f =
        (1 - ((q⁻¹ ^ 2 : Kˣ) : K))⁻¹ • (f - torusScaleAlgHom q (q⁻¹ ^ 2) (q⁻¹ ^ 2)⁻¹ f)) ∧
    leftInvOp q (woronowiczChi1 q) (f₁ * f₂) =
      leftInvOp q (woronowiczChi1 q) f₁ * torusScaleAlgHom q (q⁻¹ ^ 2) (q⁻¹ ^ 2)⁻¹ f₂ +
        f₁ * leftInvOp q (woronowiczChi1 q) f₂ :=
  cartanField q (q⁻¹ ^ 2) _ f₁ f₂

end QOU.AlgebraicSubstrate.OqSU2
