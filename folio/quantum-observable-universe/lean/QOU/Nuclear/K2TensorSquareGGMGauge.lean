/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.MassTheory.ThetaSlopeArithmetic
import QCalculus.QDifferenceConfluentObstruction
import HeckeTemperleyLieb.KnotFactorFrobeniusPairing
import BraidKnotOctonion.MarkovTraceInstance

/-!
# Algebraic Symmetric-Square Recursion, Newton Slope Profile, and Sign-Alternation Gauge (`qou-otet`)

Formalizes the algebraic parts of `NF-P3` (bean `qou-otet`) over a generic field `K` (§7c):

1. **Bar-parity sign-alternation gauge (`(-1)^m` twist) on the GGM Stokes recursion `𝒢`.**
   Twisting `z m = (-1)^m * y m` is an involution (`parityTwist_involutive`) that intertwines
   the positive-middle-sign recurrence `z_{m+2} + (2 - q^{m+1}) z_{m+1} + z_m = 0` and the
   standard GGM Stokes recurrence `y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m = 0`
   (`ggmStepPlus_parityTwist`, `parityTwist_solves_plus_iff_minus`).

2. **Exact 3rd-order symmetric-square `q`-difference recursion for `𝒦^{\otimes 2}`.**
   For any two solutions `u, v` of a 2nd-order linear recurrence `u_{m+2} = α_m u_{m+1} + β_m u_m`,
   their tensor-product diagonal `w_m = u_m v_m` satisfies an exact 3rd-order linear recurrence
   (`sym2_third_order_recurrence`). Specializing to the normalized binding `q`-lift recursion `𝒦`
   (`[m+2]_q b_{m+2} = b_{m+1} + b_m`, `QDifferenceConfluentObstruction.qint`) gives the cleared
   3rd-order `q`-difference relation
   `[m+2]_q [m+3]_q^2 w_{m+3} = (1 + [m+2]_q)([m+2]_q w_{m+2} + w_{m+1}) - w_m`
   (`binding_sym2_third_order`).

3. **Tropical / Newton slope degree profile `{+1, 0, -1}` containing `𝒢`'s `{-1, +1}` pair.**
   Combining `ThetaSlopeArithmetic.c1Slope` (`1/2`) with its bar-conjugate `bar c1Slope` (`-1/2`),
   the symmetric-square slope profile is `{+1, 0, -1}` (`k_bar_sym2_profile_eq`), which decomposes
   as `newtonSlopes ggmAtInfinity + {0}` (`k_bar_sym2_eq_ggm_add_zero`) and contains `𝒢`'s
   `{-1, +1}` Newton slope multiset (`ggm_slopes_le_k_bar_sym2`). On explicit `K[X]` operator
   coefficients at `∞`, Ore-composing `(σ̃ - 1)` with `L_GGM` yields `natTrailingDegree` quadruple
   `(1, 0, 0, 1)` (`extGgm_valuations`) and strictly convex Newton slopes `{-1, 0, +1}`
   (`newtonSlopes3_extGgm_eq_sym2`).

4. **Convention-D `KnotFactorFrobeniusPairing.ofHecke` wiring.**
   Pulling back the proved Convention-D Ocneanu trace `SeminormalRep.wtrace` (`z_D = q^3/(q^2+1)`)
   along a Hecke algebra homomorphism supplies the cyclic linear trace required by
   `QOU.BraidKnot.ofHecke` (`ofHeckeConventionD`).

No `ℝ`, no empirical literals, no `sorry`.

-- Ref: [leitner2026] beans qou-otet, qou-qzvs
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §2.2 (Newton polygon of q-difference modules)
-/

namespace QOU.Nuclear.K2TensorSquareGGMGauge

open Polynomial
open QOU.Mass.ThetaSlopeArithmetic
open QOU.Mass.QDifferenceConfluentObstruction
open QOU.BraidKnot
open QOU.SchurWeyl

section ParityTwist

variable {R : Type*} [CommRing R]

/-- Residual of the GGM Stokes recurrence `𝒢`: `y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m`. -/
def ggmStepMinus (q : R) (y : ℕ → R) (m : ℕ) : R :=
  y (m + 2) - (2 - q ^ (m + 1)) * y (m + 1) + y m

/-- Residual of the positive-sign partner recurrence: `z_{m+2} + (2 - q^{m+1}) z_{m+1} + z_m`. -/
def ggmStepPlus (q : R) (z : ℕ → R) (m : ℕ) : R :=
  z (m + 2) + (2 - q ^ (m + 1)) * z (m + 1) + z m

/-- Bar-parity sign-alternation gauge transform `(parityTwist y)_m = (-1)^m y_m`. -/
def parityTwist (y : ℕ → R) (m : ℕ) : R :=
  (-1 : R) ^ m * y m

/-- `(-1)^m * (-1)^m = 1` in any commutative ring. -/
theorem neg_one_pow_mul_self (m : ℕ) : (-1 : R) ^ m * (-1 : R) ^ m = 1 := by
  rw [← mul_pow]
  norm_num

/-- **The `(-1)^m` parity twist is an exact involution.** -/
theorem parityTwist_involutive (y : ℕ → R) (m : ℕ) :
    parityTwist (parityTwist y) m = y m := by
  unfold parityTwist
  rw [← mul_assoc, neg_one_pow_mul_self, one_mul]

/-- **Exact operator intertwining under `(-1)^m`:** applying `ggmStepPlus` to `(-1)^m y_m`
produces `(-1)^m` times `ggmStepMinus` of `y_m`. -/
theorem ggmStepPlus_parityTwist (q : R) (y : ℕ → R) (m : ℕ) :
    ggmStepPlus q (parityTwist y) m = (-1 : R) ^ m * ggmStepMinus q y m := by
  unfold ggmStepPlus ggmStepMinus parityTwist
  have h1 : (-1 : R) ^ (m + 1) = -((-1 : R) ^ m) := by rw [pow_succ]; ring
  have h2 : (-1 : R) ^ (m + 2) = (-1 : R) ^ m := by rw [pow_add]; norm_num
  rw [h1, h2]
  ring

/-- Symmetric partner: applying `ggmStepMinus` to `(-1)^m z_m` produces `(-1)^m` times
`ggmStepPlus` of `z_m`. -/
theorem ggmStepMinus_parityTwist (q : R) (z : ℕ → R) (m : ℕ) :
    ggmStepMinus q (parityTwist z) m = (-1 : R) ^ m * ggmStepPlus q z m := by
  unfold ggmStepMinus ggmStepPlus parityTwist
  have h1 : (-1 : R) ^ (m + 1) = -((-1 : R) ^ m) := by rw [pow_succ]; ring
  have h2 : (-1 : R) ^ (m + 2) = (-1 : R) ^ m := by rw [pow_add]; norm_num
  rw [h1, h2]
  ring

/-- **Sign-alternation gauge equivalence:** `(-1)^m y_m` solves
`z_{m+2} + (2 - q^{m+1}) z_{m+1} + z_m = 0` for all `m` if and only if `y_m` solves
the GGM Stokes recurrence `y_{m+2} - (2 - q^{m+1}) y_{m+1} + y_m = 0` for all `m`. -/
theorem parityTwist_solves_plus_iff_minus (q : R) (y : ℕ → R) :
    (∀ m, ggmStepPlus q (parityTwist y) m = 0) ↔ (∀ m, ggmStepMinus q y m = 0) := by
  constructor
  · intro h m
    have hm := h m
    rw [ggmStepPlus_parityTwist] at hm
    have hmul := congrArg ((-1 : R) ^ m * ·) hm
    simpa [← mul_assoc, neg_one_pow_mul_self] using hmul
  · intro h m
    rw [ggmStepPlus_parityTwist, h m, mul_zero]

end ParityTwist

section TensorSquareRecursion

/-- **General 3rd-order symmetric-square recurrence.**
For any two solutions `u, v` of `u_{m+2} = α_m u_{m+1} + β_m u_m` over a commutative ring `R`,
their pointwise product `w_m = u_m v_m` satisfies the cleared 3rd-order linear recurrence
eliminating the off-diagonal cross-term `u_{m+1} v_m + u_m v_{m+1}`. -/
theorem sym2_third_order_recurrence {R : Type*} [CommRing R]
    (α β u v : ℕ → R)
    (hu : ∀ m, u (m + 2) = α m * u (m + 1) + β m * u m)
    (hv : ∀ m, v (m + 2) = α m * v (m + 1) + β m * v m) (m : ℕ) :
    α m * (u (m + 3) * v (m + 3)) =
      α (m + 1) * (α m * α (m + 1) + β (m + 1)) * (u (m + 2) * v (m + 2))
        + α m * β (m + 1) * (α m * α (m + 1) + β (m + 1)) * (u (m + 1) * v (m + 1))
        - α (m + 1) * β (m + 1) * β m ^ 2 * (u m * v m) := by
  have hu3 : u (m + 3) = α (m + 1) * u (m + 2) + β (m + 1) * u (m + 1) := hu (m + 1)
  have hv3 : v (m + 3) = α (m + 1) * v (m + 2) + β (m + 1) * v (m + 1) := hv (m + 1)
  rw [hu3, hv3, hu m, hv m]
  ring

/-- **3rd-order `q`-difference recurrence for the symmetric square of the binding kernel `𝒦`.**
Over a field `K`, if `b₁, b₂ : ℕ → K` both satisfy the proved normalized binding recursion
`[m+2]_q b_{m+2} = b_{m+1} + b_m` (`QDifferenceConfluentObstruction.qint`), then `w_m = b₁_m b₂_m`
satisfies `[m+2]_q [m+3]_q^2 w_{m+3} = (1 + [m+2]_q)([m+2]_q w_{m+2} + w_{m+1}) - w_m`. -/
theorem binding_sym2_third_order {K : Type*} [Field K] (q : K) (b₁ b₂ : ℕ → K)
    (hb₁ : ∀ m, qint q (m + 2) * b₁ (m + 2) = b₁ (m + 1) + b₁ m)
    (hb₂ : ∀ m, qint q (m + 2) * b₂ (m + 2) = b₂ (m + 1) + b₂ m)
    (hq : ∀ k, 2 ≤ k → qint q k ≠ 0) (m : ℕ) :
    qint q (m + 2) * qint q (m + 3) ^ 2 * (b₁ (m + 3) * b₂ (m + 3)) =
      (1 + qint q (m + 2)) * (qint q (m + 2) * (b₁ (m + 2) * b₂ (m + 2)) + b₁ (m + 1) * b₂ (m + 1))
        - b₁ m * b₂ m := by
  have hq2 : qint q (m + 2) ≠ 0 := hq (m + 2) (by omega)
  have hq3 : qint q (m + 3) ≠ 0 := hq (m + 3) (by omega)
  have u2 : b₁ (m + 2) = (b₁ (m + 1) + b₁ m) / qint q (m + 2) := by
    rw [eq_div_iff hq2]; linear_combination hb₁ m
  have v2 : b₂ (m + 2) = (b₂ (m + 1) + b₂ m) / qint q (m + 2) := by
    rw [eq_div_iff hq2]; linear_combination hb₂ m
  have u3 : b₁ (m + 3) = (b₁ (m + 2) + b₁ (m + 1)) / qint q (m + 3) := by
    rw [eq_div_iff hq3]; linear_combination hb₁ (m + 1)
  have v3 : b₂ (m + 3) = (b₂ (m + 2) + b₂ (m + 1)) / qint q (m + 3) := by
    rw [eq_div_iff hq3]; linear_combination hb₂ (m + 1)
  rw [u3, v3, u2, v2]
  field_simp
  ring

end TensorSquareRecursion

section TropicalNewtonProfile

/-- Symmetric-square Newton slope multiset `{2s₁, s₁ + s₂, 2s₂}` built from
`ThetaSlopeArithmetic.prodSlope`. -/
def sym2SlopeProfile (s₁ s₂ : ℚ) : Multiset ℚ :=
  {prodSlope s₁ s₁, prodSlope s₁ s₂, prodSlope s₂ s₂}

/-- Full rank-4 tensor-square slope multiset `{2s₁, s₁ + s₂, s₂ + s₁, 2s₂}`. -/
def tensor2SlopeProfile (s₁ s₂ : ℚ) : Multiset ℚ :=
  {prodSlope s₁ s₁, prodSlope s₁ s₂, prodSlope s₂ s₁, prodSlope s₂ s₂}

/-- **Symmetric-square slope profile of `(𝒦, 𝒦̄)` is `{+1, 0, -1}`.** -/
theorem k_bar_sym2_profile_eq :
    sym2SlopeProfile c1Slope (bar c1Slope) = {(1 : ℚ), 0, -1} := by
  simp only [sym2SlopeProfile, prodSlope, bar, c1Slope]
  norm_num

/-- **`𝒦 ⊗ 𝒦̄` symmetric-square profile equals `𝒢`'s Newton slopes `{-1, +1}` plus `{0}`.** -/
theorem k_bar_sym2_eq_ggm_add_zero :
    sym2SlopeProfile c1Slope (bar c1Slope) = newtonSlopes ggmAtInfinity + {(0 : ℚ)} := by
  rw [k_bar_sym2_profile_eq, newtonSlopes_ggm]
  decide

/-- **`𝒢`'s Newton slope multiset `{-1, +1}` is a submultiset of `{+1, 0, -1}`.** -/
theorem ggm_slopes_le_k_bar_sym2 :
    newtonSlopes ggmAtInfinity ≤ sym2SlopeProfile c1Slope (bar c1Slope) := by
  rw [k_bar_sym2_eq_ggm_add_zero]
  exact Multiset.le_add_right _ _

/-- Valuation quadruple `(v₀, v₁, v₂, v₃)` of an order-3 `q`-difference operator
`a₃ σ̃³ + a₂ σ̃² + a₁ σ̃ + a₀` at `w = 1/x`. -/
structure Order3Valuations where
  v0 : ℤ
  v1 : ℤ
  v2 : ℤ
  v3 : ℤ

/-- Convexity predicate on `Order3Valuations`: the four points `(i, vᵢ)` all sit on the lower
convex hull, so the three unit-width edge slopes `v₁ - v₀ ≤ v₂ - v₁ ≤ v₃ - v₂` are exact. -/
def Order3Valuations.IsLowerConvex (d : Order3Valuations) : Prop :=
  d.v1 - d.v0 ≤ d.v2 - d.v1 ∧ d.v2 - d.v1 ≤ d.v3 - d.v2

/-- Edge-slope multiset of a lower-convex order-3 `q`-difference polygon. -/
def newtonSlopes3Convex (d : Order3Valuations) : Multiset ℚ :=
  {((d.v1 - d.v0 : ℤ) : ℚ), ((d.v2 - d.v1 : ℤ) : ℚ), ((d.v3 - d.v2 : ℤ) : ℚ)}

/-- Explicit `K[X]` coefficients at `w = 1/x` of the order-3 operator `(σ̃ - 1) ∘ L_GGM`,
built directly from `ThetaSlopeArithmetic.ggmA0`, `ggmA1`, `ggmA2` under `σ̃(w) = q w`:
`L₃ = q² w σ̃³ + (1 - (2q² + q) w) σ̃² + (-1 + (q² + 2q) w) σ̃ - q w`. -/
noncomputable def extGgmA0 {K : Type*} [Field K] (q : K) : K[X] := -ggmA0 q
noncomputable def extGgmA1 {K : Type*} [Field K] (q : K) : K[X] := -1 + C (q ^ 2 + 2 * q) * X
noncomputable def extGgmA2 {K : Type*} [Field K] (q : K) : K[X] := 1 - C (2 * q ^ 2 + q) * X
noncomputable def extGgmA3 {K : Type*} [Field K] (q : K) : K[X] := C (q ^ 2) * X

/-- **Ore-product identity at `w = 1/x`:** the coefficients `(extGgmA0..extGgmA3)` equal the
left Ore composition `(σ̃ - 1) ∘ (ggmA2 σ̃² + ggmA1 σ̃ + ggmA0)` under `w ↦ q w`. -/
theorem extGgm_ore_factorization {K : Type*} [Field K] (q : K) :
    extGgmA3 q = (ggmA2 q).comp (C q * X) ∧
    extGgmA2 q = (ggmA1 q).comp (C q * X) - ggmA2 q ∧
    extGgmA1 q = (ggmA0 q).comp (C q * X) - ggmA1 q ∧
    extGgmA0 q = -ggmA0 q := by
  refine ⟨?_, ?_, ?_, rfl⟩
  · simp [extGgmA3, ggmA2]; ring
  · simp [extGgmA2, ggmA1, ggmA2]; ring
  · simp [extGgmA1, ggmA0, ggmA1]; ring

/-- **The order-3 extended GGM operator has exact `w`-adic valuation quadruple `(1, 0, 0, 1)`.** -/
theorem extGgm_valuations {K : Type*} [Field K] (q : K) (hq : q ≠ 0) :
    ((extGgmA0 q).natTrailingDegree, (extGgmA1 q).natTrailingDegree,
      (extGgmA2 q).natTrailingDegree, (extGgmA3 q).natTrailingDegree) = (1, 0, 0, 1) := by
  have h0 : (extGgmA0 q).natTrailingDegree = 1 := by
    unfold extGgmA0 ggmA0
    rw [natTrailingDegree_neg, natTrailingDegree_mul (by simpa using hq) X_ne_zero]
    simp
  have h1 : (extGgmA1 q).natTrailingDegree = 0 := by
    refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
    simp [extGgmA1]
  have h2 : (extGgmA2 q).natTrailingDegree = 0 := by
    refine natTrailingDegree_eq_zero_of_constantCoeff_ne_zero ?_
    simp [extGgmA2]
  have h3 : (extGgmA3 q).natTrailingDegree = 1 := by
    unfold extGgmA3
    have hc : (C (q ^ 2) : K[X]) ≠ 0 := C_ne_zero.mpr (pow_ne_zero 2 hq)
    rw [natTrailingDegree_mul hc X_ne_zero, natTrailingDegree_C, natTrailingDegree_X]
  rw [h0, h1, h2, h3]

/-- Newton valuation quadruple `(1, 0, 0, 1)` computed in `extGgm_valuations`. -/
def extGgmAtInfinity : Order3Valuations := ⟨1, 0, 0, 1⟩

theorem extGgmAtInfinity_isLowerConvex : extGgmAtInfinity.IsLowerConvex := by
  dsimp [Order3Valuations.IsLowerConvex, extGgmAtInfinity]
  omega

/-- **Exact match of order-3 Newton slopes with the `(𝒦, 𝒦̄)` symmetric-square profile.** -/
theorem newtonSlopes3_extGgm_eq_sym2 :
    newtonSlopes3Convex extGgmAtInfinity = sym2SlopeProfile c1Slope (bar c1Slope) := by
  rw [k_bar_sym2_profile_eq]
  decide

end TropicalNewtonProfile

section ConventionDKnotFactor

variable {K : Type*} [Field K]

/-- Pullback of the proved Convention-D Ocneanu trace `SeminormalRep.wtrace` (`z_D = q^3/(q^2+1)`)
along any `K`-algebra homomorphism `B : IwahoriHecke K q m →ₐ[K] SchurWeyl.Hecke K q q⁻¹ n`. -/
noncomputable def pullbackConventionDTrace {q : K} {m n : ℕ}
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (B : QOU.Hecke.IwahoriHecke K q m →ₐ[K] QOU.SchurWeyl.Hecke K q q⁻¹ n) :
    QOU.Hecke.IwahoriHecke K q m →ₗ[K] K :=
  (SeminormalRep.wtrace q hq0 hq2 n).comp B.toLinearMap

theorem pullbackConventionDTrace_cyclic {q : K} {m n : ℕ}
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (B : QOU.Hecke.IwahoriHecke K q m →ₐ[K] QOU.SchurWeyl.Hecke K q q⁻¹ n)
    (x y : QOU.Hecke.IwahoriHecke K q m) :
    pullbackConventionDTrace hq0 hq2 B (x * y) = pullbackConventionDTrace hq0 hq2 B (y * x) := by
  simp only [pullbackConventionDTrace, LinearMap.comp_apply, AlgHom.toLinearMap_apply, map_mul]
  exact SeminormalRep.wtrace_cyclic q hq0 hq2 n (B x) (B y)

/-- **`KnotFactorFrobeniusPairing` instantiated at Convention D (`z_D = q^3/(q^2+1)`) via `ofHecke`.**
Given a Wedderburn splitting `E` of `IwahoriHecke K q m` and a Hecke-model homomorphism `B` into
`SchurWeyl.Hecke`, the Convention-D Ocneanu trace factors uniquely as `τ(x · κ_D)`. -/
noncomputable def ofHeckeConventionD {q : K} {m n : ℕ}
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (E : QOU.Hecke.IwahoriHecke K q m ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i)
    (B : QOU.Hecke.IwahoriHecke K q m →ₐ[K] QOU.SchurWeyl.Hecke K q q⁻¹ n) :
    KnotFactorFrobeniusPairing K (QOU.Hecke.IwahoriHecke K q m) :=
  ofHecke hq0 E a (pullbackConventionDTrace hq0 hq2 B) (pullbackConventionDTrace_cyclic hq0 hq2 B)

theorem ofHeckeConventionD_factors {q : K} {m n : ℕ}
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
    (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (E : QOU.Hecke.IwahoriHecke K q m ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i)
    (B : QOU.Hecke.IwahoriHecke K q m →ₐ[K] QOU.SchurWeyl.Hecke K q q⁻¹ n)
    (x : QOU.Hecke.IwahoriHecke K q m) :
    SeminormalRep.wtrace q hq0 hq2 n (B x) =
      (ofHeckeConventionD hq0 hq2 E a B).pairingTrace
        (x * (ofHeckeConventionD hq0 hq2 E a B).knotFactor) :=
  (ofHeckeConventionD hq0 hq2 E a B).factorisation_holds x

end ConventionDKnotFactor

end QOU.Nuclear.K2TensorSquareGGMGauge
