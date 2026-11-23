import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases

/-!
# Woronowicz's `O_q(SU(2))` Modular Twist, `S²`, Haar Identity, and CPT Invert-Commutation

Over an arbitrary commutative base ring `R` and unit `q : Rˣ` (§7c generic base-ring
discipline, no `ℝ`), this module constructs Woronowicz's coordinate algebra `O_q(SU(2))`
universally as the `RingQuot` of `FreeAlgebra R (Fin 4)` (generators `α, β, γ, δ`) modulo
all 7 defining relations:

  `α β = q β α`, `α γ = q γ α`, `β δ = q δ β`, `γ δ = q δ γ`, `β γ = γ β`,
  `α δ - q β γ = 1`, `δ α - q⁻¹ β γ = 1`.

## Main declarations and results

1. **Non-vacuity & Genuine Non-Commutativity:**
   - `diagCharAlgHom` — diagonal `U(1)` character `(α, β, γ, δ) ↦ (u, 0, 0, u⁻¹)`, proving
     `Nontrivial (OqSU2 R q)` over any `[Nontrivial R]`, `α ≠ 0`, and `ν_q(α) ≠ α` when
     `q² ≠ 1` (`nuAlgEquiv_alpha_ne_alpha`).
   - `borel2AlgHom` — explicit `2 × 2` Borel matrix representation proving `β ≠ 0` and
     `α * β ≠ β * α` whenever `(q : R) ≠ 1` (`alpha_mul_beta_ne_beta_mul_alpha`).
2. **Modular Twist `ν_q`, Squared Antipode `S²`, and Pure-`T₃` Cartan Extraction:**
   - `nuAlgEquiv` — `O_q(SU(2)) ≃ₐ[R] O_q(SU(2))` scaling `(α, β, γ, δ) ↦ (q² α, β, γ, q⁻² δ)`.
   - `antipodeSqAlgEquiv` — `O_q(SU(2)) ≃ₐ[R] O_q(SU(2))` scaling
     `(α, β, γ, δ) ↦ (α, q⁻² β, q² γ, δ)`.
   - `nu_trans_antipodeSq_generators` — `(ν_q ∘ S²)(α, β, γ, δ) = (q² α, q⁻² β, q² γ, q⁻² δ)`.
   - `nuAlgEquiv_fixes_cartan` — `ν_q` fixes `α * δ`, `δ * α`, and `β * γ` pointwise.
3. **Exact Generator Commutator & Haar Modular Identity:**
   - `alpha_delta_sub_delta_alpha` — `α * δ - δ * α = (q - q⁻¹) • (β * γ)` inside `OqSU2 R q`.
   - `haar_cleared_alpha_delta` & `haar_modular_swap_alpha_delta` — for any linear functional
     `h : OqSU2 R q →ₗ[R] R` satisfying Woronowicz's rank-1 Haar relation
     `(1 + q²) * h(β * γ) = -q * h(1)`, `(1 + q²) * h(α * δ) = h(1)` and
     `(1 + q²) * h(δ * α) = q² * h(1)`, whence `h(δ * α) = q² * h(α * δ) = h(ν_q(α) * δ)` and
     `h(α * δ) = h(δ * ν_q⁻¹(α))`.
4. **Modular–CPT Invert-Commutation on All of `O_q(SU(2))`:**
   - `qInvOpAlgEquiv` (`OqSU2 R q ≃ₐ[R] (OqSU2 R q⁻¹)ᵐᵒᵖ`) and `qInvBar` — `q ↔ q⁻¹`
     bar anti-isomorphism satisfying
     `qInvBar q (nuAlgEquiv q x) = (nuAlgEquiv q⁻¹).symm (qInvBar q x)` for **every**
     `x : OqSU2 R q` (`qInvBar_nu_comm`).
   - `compactStarOpAlgEquiv` (`OqSU2 R q ≃ₐ[R] (OqSU2 R q)ᵐᵒᵖ`) and `compactStar` —
     Woronowicz's compact `∗`-anti-involution `(α, β, γ, δ) ↦ (δ, -q γ, -q⁻¹ β, α)` satisfying
     `compactStar q (compactStar q x) = x` and
     `compactStar q (nuAlgEquiv q x) = (nuAlgEquiv q).symm (compactStar q x)` for **every**
     `x : OqSU2 R q` (`compactStar_nu_comm`).

References: Stanisław Lech Woronowicz (1987), Anatoli Klimyk & Konrad Schmüdgen (1997) §4.1–4.2.
-- Ref: [woronowicz1987]
-/

namespace QOU.AlgebraicSubstrate

/-! ## 1. Universal Presentation of `O_q(SU(2))` -/

section Presentation

variable {R : Type*} [CommRing R]

/-- Free-algebra generator `i : Fin 4` (`0 = α, 1 = β, 2 = γ, 3 = δ`). -/
abbrev oqFreeGen (R : Type*) [CommRing R] (i : Fin 4) : FreeAlgebra R (Fin 4) :=
  FreeAlgebra.ι R i

/-- Woronowicz's 7 defining relations for `O_q(SU(2))` on `FreeAlgebra R (Fin 4)`. -/
inductive OqSU2Rel (q : Rˣ) : FreeAlgebra R (Fin 4) → FreeAlgebra R (Fin 4) → Prop
  | ab : OqSU2Rel q (oqFreeGen R 0 * oqFreeGen R 1) ((q : R) • (oqFreeGen R 1 * oqFreeGen R 0))
  | ag : OqSU2Rel q (oqFreeGen R 0 * oqFreeGen R 2) ((q : R) • (oqFreeGen R 2 * oqFreeGen R 0))
  | bd : OqSU2Rel q (oqFreeGen R 1 * oqFreeGen R 3) ((q : R) • (oqFreeGen R 3 * oqFreeGen R 1))
  | gd : OqSU2Rel q (oqFreeGen R 2 * oqFreeGen R 3) ((q : R) • (oqFreeGen R 3 * oqFreeGen R 2))
  | bg : OqSU2Rel q (oqFreeGen R 1 * oqFreeGen R 2) (oqFreeGen R 2 * oqFreeGen R 1)
  | det_left :
      OqSU2Rel q (oqFreeGen R 0 * oqFreeGen R 3 - (q : R) • (oqFreeGen R 1 * oqFreeGen R 2)) 1
  | det_right :
      OqSU2Rel q
        (oqFreeGen R 3 * oqFreeGen R 0 - (((q⁻¹ : Rˣ) : R)) • (oqFreeGen R 1 * oqFreeGen R 2)) 1

/-- Woronowicz's coordinate algebra `O_q(SU(2))` over `R` at unit parameter `q : Rˣ`. -/
abbrev OqSU2 (R : Type*) [CommRing R] (q : Rˣ) : Type _ :=
  RingQuot (OqSU2Rel (R := R) q)

namespace OqSU2

/-- Indexed generator `0 ↦ α, 1 ↦ β, 2 ↦ γ, 3 ↦ δ` in `OqSU2 R q`. -/
noncomputable def gen (q : Rˣ) (i : Fin 4) : OqSU2 R q :=
  RingQuot.mkAlgHom R (OqSU2Rel q) (oqFreeGen R i)

/-- Generator `α` of `OqSU2 R q`. -/
noncomputable def α (q : Rˣ) : OqSU2 R q := gen q 0
/-- Generator `β` of `OqSU2 R q`. -/
noncomputable def β (q : Rˣ) : OqSU2 R q := gen q 1
/-- Generator `γ` of `OqSU2 R q`. -/
noncomputable def γ (q : Rˣ) : OqSU2 R q := gen q 2
/-- Generator `δ` of `OqSU2 R q`. -/
noncomputable def δ (q : Rˣ) : OqSU2 R q := gen q 3

theorem rel_ab (q : Rˣ) : α (R := R) q * β q = (q : R) • (β q * α q) := by
  unfold α β gen
  rw [← map_mul, RingQuot.mkAlgHom_rel R OqSU2Rel.ab, map_smul, map_mul]

theorem rel_ag (q : Rˣ) : α (R := R) q * γ q = (q : R) • (γ q * α q) := by
  unfold α γ gen
  rw [← map_mul, RingQuot.mkAlgHom_rel R OqSU2Rel.ag, map_smul, map_mul]

theorem rel_bd (q : Rˣ) : β (R := R) q * δ q = (q : R) • (δ q * β q) := by
  unfold β δ gen
  rw [← map_mul, RingQuot.mkAlgHom_rel R OqSU2Rel.bd, map_smul, map_mul]

theorem rel_gd (q : Rˣ) : γ (R := R) q * δ q = (q : R) • (δ q * γ q) := by
  unfold γ δ gen
  rw [← map_mul, RingQuot.mkAlgHom_rel R OqSU2Rel.gd, map_smul, map_mul]

theorem rel_bg (q : Rˣ) : β (R := R) q * γ q = γ q * β q := by
  unfold β γ gen
  rw [← map_mul, ← map_mul, RingQuot.mkAlgHom_rel R OqSU2Rel.bg]

theorem rel_det_left (q : Rˣ) : α (R := R) q * δ q - (q : R) • (β q * γ q) = 1 := by
  unfold α β γ δ gen
  rw [← map_mul, ← map_mul, ← map_smul, ← map_sub,
    RingQuot.mkAlgHom_rel R OqSU2Rel.det_left, map_one]

theorem rel_det_right (q : Rˣ) :
    δ (R := R) q * α q - (((q⁻¹ : Rˣ) : R)) • (β q * γ q) = 1 := by
  unfold α β γ δ gen
  rw [← map_mul, ← map_mul, ← map_smul, ← map_sub,
    RingQuot.mkAlgHom_rel R OqSU2Rel.det_right, map_one]

/-- Exact universal commutator identity inside `OqSU2 R q`:
`α * δ - δ * α = (q - q⁻¹) • (β * γ)`. -/
theorem alpha_delta_sub_delta_alpha (q : Rˣ) :
    α (R := R) q * δ q - δ q * α q =
      ((q : R) - (((q⁻¹ : Rˣ) : R))) • (β q * γ q) := by
  have hL := rel_det_left (R := R) q
  have hR := rel_det_right (R := R) q
  have hdiff : (α (R := R) q * δ q - (q : R) • (β q * γ q)) -
      (δ q * α q - (((q⁻¹ : Rˣ) : R)) • (β q * γ q)) = 0 := by
    rw [hL, hR, sub_self]
  have hsub : ((q : R) - (((q⁻¹ : Rˣ) : R))) • (β (R := R) q * γ q) =
      (q : R) • (β q * γ q) - (((q⁻¹ : Rˣ) : R)) • (β q * γ q) := by
    simp only [Algebra.smul_def, map_sub, sub_mul]
  rw [hsub]
  calc
    α (R := R) q * δ q - δ q * α q
        = (α (R := R) q * δ q - (q : R) • (β q * γ q)) -
            (δ q * α q - (((q⁻¹ : Rˣ) : R)) • (β q * γ q)) +
            ((q : R) • (β q * γ q) - (((q⁻¹ : Rˣ) : R)) • (β q * γ q)) := by abel
    _ = 0 + ((q : R) • (β q * γ q) - (((q⁻¹ : Rˣ) : R)) • (β q * γ q)) := by rw [hdiff]
    _ = (q : R) • (β q * γ q) - (((q⁻¹ : Rˣ) : R)) • (β q * γ q) := zero_add _

/-- Predicate saying a quadruple `(a, b, g, d)` in an `R`-algebra `B` satisfies Woronowicz's
7 `O_q(SU(2))` relations. -/
structure IsOqSU2Quadruple {B : Type*} [Ring B] [Algebra R B] (q : Rˣ) (a b g d : B) : Prop where
  ab : a * b = (q : R) • (b * a)
  ag : a * g = (q : R) • (g * a)
  bd : b * d = (q : R) • (d * b)
  gd : g * d = (q : R) • (d * g)
  bg : b * g = g * b
  det_left : a * d - (q : R) • (b * g) = 1
  det_right : d * a - (((q⁻¹ : Rˣ) : R)) • (b * g) = 1

/-- Universal lifting property of `OqSU2 R q`: any quadruple satisfying `IsOqSU2Quadruple`
determines an `R`-algebra homomorphism `OqSU2 R q →ₐ[R] B`. -/
noncomputable def liftQuadruple {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) : OqSU2 R q →ₐ[R] B :=
  RingQuot.liftAlgHom R
    ⟨FreeAlgebra.lift R ![a, b, g, d], by
      intro x y hrel
      cases hrel with
      | ab => simp [oqFreeGen, h.ab]
      | ag => simp [oqFreeGen, h.ag]
      | bd => simp [oqFreeGen, h.bd]
      | gd => simp [oqFreeGen, h.gd]
      | bg => simp [oqFreeGen, h.bg]
      | det_left => simp [oqFreeGen, h.det_left]
      | det_right => simp [oqFreeGen, h.det_right]⟩

@[simp]
theorem liftQuadruple_gen {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) (i : Fin 4) :
    liftQuadruple q a b g d h (gen q i) = (![a, b, g, d] : Fin 4 → B) i := by
  unfold gen liftQuadruple oqFreeGen
  rw [RingQuot.liftAlgHom_mkAlgHom_apply, FreeAlgebra.lift_ι_apply]

@[simp]
theorem liftQuadruple_alpha {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) :
    liftQuadruple q a b g d h (α q) = a :=
  liftQuadruple_gen q a b g d h 0

@[simp]
theorem liftQuadruple_beta {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) :
    liftQuadruple q a b g d h (β q) = b :=
  liftQuadruple_gen q a b g d h 1

@[simp]
theorem liftQuadruple_gamma {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) :
    liftQuadruple q a b g d h (γ q) = g :=
  liftQuadruple_gen q a b g d h 2

@[simp]
theorem liftQuadruple_delta {B : Type*} [Ring B] [Algebra R B] (q : Rˣ)
    (a b g d : B) (h : IsOqSU2Quadruple (R := R) q a b g d) :
    liftQuadruple q a b g d h (δ q) = d :=
  liftQuadruple_gen q a b g d h 3

/-- Universal uniqueness: two `R`-algebra homomorphisms out of `OqSU2 R q` are equal iff they
agree on `(α, β, γ, δ)`. -/
theorem algHom_ext {B : Type*} [Ring B] [Algebra R B] {q : Rˣ}
    {f₁ f₂ : OqSU2 R q →ₐ[R] B}
    (hα : f₁ (α q) = f₂ (α q)) (hβ : f₁ (β q) = f₂ (β q))
    (hγ : f₁ (γ q) = f₂ (γ q)) (hδ : f₁ (δ q) = f₂ (δ q)) :
    f₁ = f₂ := by
  have hfree : f₁.comp (RingQuot.mkAlgHom R (OqSU2Rel q)) =
      f₂.comp (RingQuot.mkAlgHom R (OqSU2Rel q)) := by
    apply (FreeAlgebra.lift R).symm.injective
    funext i
    simp only [FreeAlgebra.lift_symm_apply, AlgHom.coe_comp, Function.comp_apply]
    fin_cases i
    · exact hα
    · exact hβ
    · exact hγ
    · exact hδ
  apply AlgHom.ext
  intro x
  obtain ⟨y, hy⟩ := RingQuot.mkAlgHom_surjective R (OqSU2Rel q) x
  rw [← hy]
  exact AlgHom.congr_fun hfree y

/-! ## 2. Concrete Non-Vacuity & Non-Commutativity Witnesses -/

/-- Diagonal `U(1)` character `(α, β, γ, δ) ↦ (u, 0, 0, u⁻¹)` into `R`. -/
noncomputable def diagCharAlgHom (q u : Rˣ) : OqSU2 R q →ₐ[R] R :=
  liftQuadruple q (u : R) 0 0 (((u⁻¹ : Rˣ) : R))
    { ab := by simp
      ag := by simp
      bd := by simp
      gd := by simp
      bg := by simp
      det_left := by simp [Units.mul_inv]
      det_right := by simp [Units.inv_mul] }

/-- `OqSU2 R q` is nontrivial over every nontrivial commutative ring `R`. -/
instance instNontrivial [Nontrivial R] (q : Rˣ) : Nontrivial (OqSU2 R q) := by
  refine ⟨⟨1, 0, fun h10 => ?_⟩⟩
  have hval := congr_arg (diagCharAlgHom (R := R) q 1) h10
  simp only [map_one, map_zero] at hval
  exact one_ne_zero hval

/-- Generator `α` is nonzero over every nontrivial commutative ring `R`. -/
theorem alpha_ne_zero [Nontrivial R] (q : Rˣ) : α (R := R) q ≠ 0 := by
  intro h0
  have hval := congr_arg (diagCharAlgHom (R := R) q 1) h0
  simp only [diagCharAlgHom, liftQuadruple_alpha, Units.val_one, map_zero] at hval
  exact one_ne_zero hval

/-- `2 × 2` Borel matrix representation `(α, β, γ, δ) ↦ (diag(q, 1), E₀₁, 0, diag(q⁻¹, 1))`,
witnessing both `β ≠ 0` and genuine `q`-noncommutativity `α * β ≠ β * α` when `q ≠ 1`. -/
noncomputable def borel2AlgHom (q : Rˣ) : OqSU2 R q →ₐ[R] Matrix (Fin 2) (Fin 2) R :=
  liftQuadruple q
    (Matrix.of ![![(q : R), 0], ![0, 1]])
    (Matrix.of ![![0, (1 : R)], ![0, 0]])
    0
    (Matrix.of ![![(((q⁻¹ : Rˣ) : R)), 0], ![0, 1]])
    { ab := by
        ext i j
        fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
      ag := by simp
      bd := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two, Units.mul_inv]
      gd := by simp
      bg := by simp
      det_left := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two, Units.mul_inv]
      det_right := by
        ext i j
        fin_cases i <;> fin_cases j <;>
          simp [Matrix.mul_apply, Fin.sum_univ_two, Units.inv_mul] }

/-- Generator `β` is nonzero over every nontrivial commutative ring `R`. -/
theorem beta_ne_zero [Nontrivial R] (q : Rˣ) : β (R := R) q ≠ 0 := by
  intro h0
  have hmat := congr_fun (congr_fun (congr_arg (borel2AlgHom (R := R) q) h0) 0) 1
  simp [borel2AlgHom] at hmat

/-- Genuine `q`-noncommutativity: whenever `(q : R) ≠ 1`, `α * β ≠ β * α` in `OqSU2 R q`. -/
theorem alpha_mul_beta_ne_beta_mul_alpha {q : Rˣ} (hq : (q : R) ≠ 1) :
    α (R := R) q * β q ≠ β q * α q := by
  intro heq
  have hmat := congr_fun (congr_fun (congr_arg (borel2AlgHom (R := R) q) heq) 0) 1
  simp only [map_mul, borel2AlgHom, liftQuadruple_alpha, liftQuadruple_beta,
    Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one, mul_one, mul_zero, add_zero, zero_add] at hmat
  exact hq hmat

/-! ## 3. Torus Automorphisms, Modular Twist `ν_q`, and Squared Antipode `S²` -/

/-- General two-parameter torus `R`-algebra endomorphism scaling
`(α, β, γ, δ) ↦ (u • α, b • β, b⁻¹ • γ, u⁻¹ • δ)` for `u, b : Rˣ`. -/
noncomputable def torusScaleAlgHom (q u b : Rˣ) : OqSU2 R q →ₐ[R] OqSU2 R q :=
  liftQuadruple q
    ((u : R) • α q)
    ((b : R) • β q)
    ((((b⁻¹ : Rˣ) : R)) • γ q)
    ((((u⁻¹ : Rˣ) : R)) • δ q)
    { ab := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_ab,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul]
        congr 1
        ring
      ag := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_ag,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul]
        congr 1
        ring
      bd := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_bd,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul]
        congr 1
        ring
      gd := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_gd,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul]
        congr 1
        ring
      bg := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_bg,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul, mul_comm (b : R)]
      det_left := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul, Units.mul_inv, one_smul]
        exact rel_det_left q
      det_right := by
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul, Units.inv_mul, Units.mul_inv, one_smul]
        exact rel_det_right q }

theorem torusScaleAlgHom_comp (q u₁ b₁ u₂ b₂ : Rˣ) :
    (torusScaleAlgHom (R := R) q u₁ b₁).comp (torusScaleAlgHom q u₂ b₂) =
      torusScaleAlgHom q (u₂ * u₁) (b₂ * b₁) := by
  apply algHom_ext <;>
    simp [torusScaleAlgHom, smul_smul, mul_inv_rev, Units.val_mul, mul_comm]

/-- Two-parameter torus `R`-algebra automorphism `(α, β, γ, δ) ↦ (u α, b β, b⁻¹ γ, u⁻¹ δ)`. -/
noncomputable def torusScaleAlgEquiv (q u b : Rˣ) : OqSU2 R q ≃ₐ[R] OqSU2 R q :=
  AlgEquiv.ofAlgHom
    (torusScaleAlgHom q u b)
    (torusScaleAlgHom q u⁻¹ b⁻¹)
    (by
      rw [torusScaleAlgHom_comp, inv_mul_cancel, inv_mul_cancel]
      apply algHom_ext <;> simp [torusScaleAlgHom])
    (by
      rw [torusScaleAlgHom_comp, mul_inv_cancel, mul_inv_cancel]
      apply algHom_ext <;> simp [torusScaleAlgHom])

/-- **Woronowicz Haar Modular Automorphism `ν_q`:**
`(α, β, γ, δ) ↦ (q² α, β, γ, q⁻² δ)`. -/
noncomputable def nuAlgEquiv (q : Rˣ) : OqSU2 R q ≃ₐ[R] OqSU2 R q :=
  torusScaleAlgEquiv q (q ^ 2) 1

/-- **Woronowicz Squared Antipode `S²`:**
`(α, β, γ, δ) ↦ (α, q⁻² β, q² γ, δ)`. -/
noncomputable def antipodeSqAlgEquiv (q : Rˣ) : OqSU2 R q ≃ₐ[R] OqSU2 R q :=
  torusScaleAlgEquiv q 1 (q⁻¹ ^ 2)

@[simp] theorem nuAlgEquiv_alpha (q : Rˣ) :
    nuAlgEquiv (R := R) q (α q) = ((q : R) ^ 2) • α q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_beta (q : Rˣ) :
    nuAlgEquiv (R := R) q (β q) = β q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_gamma (q : Rˣ) :
    nuAlgEquiv (R := R) q (γ q) = γ q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_delta (q : Rˣ) :
    nuAlgEquiv (R := R) q (δ q) = ((((q⁻¹ : Rˣ) : R)) ^ 2) • δ q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_symm_alpha (q : Rˣ) :
    (nuAlgEquiv (R := R) q).symm (α q) = ((((q⁻¹ : Rˣ) : R)) ^ 2) • α q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_symm_beta (q : Rˣ) :
    (nuAlgEquiv (R := R) q).symm (β q) = β q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_symm_gamma (q : Rˣ) :
    (nuAlgEquiv (R := R) q).symm (γ q) = γ q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem nuAlgEquiv_symm_delta (q : Rˣ) :
    (nuAlgEquiv (R := R) q).symm (δ q) = ((q : R) ^ 2) • δ q := by
  simp [nuAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem antipodeSqAlgEquiv_alpha (q : Rˣ) :
    antipodeSqAlgEquiv (R := R) q (α q) = α q := by
  simp [antipodeSqAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem antipodeSqAlgEquiv_beta (q : Rˣ) :
    antipodeSqAlgEquiv (R := R) q (β q) = ((((q⁻¹ : Rˣ) : R)) ^ 2) • β q := by
  simp [antipodeSqAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

@[simp] theorem antipodeSqAlgEquiv_gamma (q : Rˣ) :
    antipodeSqAlgEquiv (R := R) q (γ q) = ((q : R) ^ 2) • γ q := by
  simp [antipodeSqAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom, inv_pow]

@[simp] theorem antipodeSqAlgEquiv_delta (q : Rˣ) :
    antipodeSqAlgEquiv (R := R) q (δ q) = δ q := by
  simp [antipodeSqAlgEquiv, torusScaleAlgEquiv, torusScaleAlgHom]

/-- Whenever `(q : R)² ≠ 1`, `ν_q(α) ≠ α` (hence `nuAlgEquiv q ≠ AlgEquiv.refl`). -/
theorem nuAlgEquiv_alpha_ne_alpha {q : Rˣ} (hq2 : (q : R) ^ 2 ≠ 1) :
    nuAlgEquiv (R := R) q (α q) ≠ α q := by
  intro heq
  have hval := congr_arg (diagCharAlgHom (R := R) q 1) heq
  simp only [nuAlgEquiv_alpha, map_smul, diagCharAlgHom, liftQuadruple_alpha,
    Units.val_one, smul_eq_mul, mul_one] at hval
  exact hq2 hval

/-- **Canonical Pure-`T₃` Cartan Grading (`ν_q ∘ S²`):**
Composing `nuAlgEquiv q` with `antipodeSqAlgEquiv q` scales `(α, β, γ, δ)` by
`(q², q⁻², q², q⁻²)`, cancelling the right-regular weight and isolating the left `T₃`
eigenvalues `(+1/2, -1/2, +1/2, -1/2)`. -/
theorem nu_trans_antipodeSq_generators (q : Rˣ) :
    ((nuAlgEquiv (R := R) q).trans (antipodeSqAlgEquiv q)) (α q) = ((q : R) ^ 2) • α q ∧
    ((nuAlgEquiv (R := R) q).trans (antipodeSqAlgEquiv q)) (β q) =
      ((((q⁻¹ : Rˣ) : R)) ^ 2) • β q ∧
    ((nuAlgEquiv (R := R) q).trans (antipodeSqAlgEquiv q)) (γ q) = ((q : R) ^ 2) • γ q ∧
    ((nuAlgEquiv (R := R) q).trans (antipodeSqAlgEquiv q)) (δ q) =
      ((((q⁻¹ : Rˣ) : R)) ^ 2) • δ q := by
  simp [AlgEquiv.trans_apply]

/-- **`ν_q` Fixes the Neutral Cartan Elements Pointwise:**
`ν_q(α * δ) = α * δ`, `ν_q(δ * α) = δ * α`, and `ν_q(β * γ) = β * γ`. -/
theorem nuAlgEquiv_fixes_cartan (q : Rˣ) :
    nuAlgEquiv (R := R) q (α q * δ q) = α q * δ q ∧
    nuAlgEquiv (R := R) q (δ q * α q) = δ q * α q ∧
    nuAlgEquiv (R := R) q (β q * γ q) = β q * γ q := by
  have hq : ((q : R) ^ 2) * ((((q⁻¹ : Rˣ) : R)) ^ 2) = 1 := by
    rw [← mul_pow, Units.mul_inv, one_pow]
  have hq' : ((((q⁻¹ : Rˣ) : R)) ^ 2) * ((q : R) ^ 2) = 1 := by
    rw [mul_comm, hq]
  refine ⟨?_, ?_, ?_⟩
  · rw [map_mul, nuAlgEquiv_alpha, nuAlgEquiv_delta, Algebra.smul_mul_assoc,
      Algebra.mul_smul_comm, smul_smul, hq, one_smul]
  · rw [map_mul, nuAlgEquiv_delta, nuAlgEquiv_alpha, Algebra.smul_mul_assoc,
      Algebra.mul_smul_comm, smul_smul, hq', one_smul]
  · rw [map_mul, nuAlgEquiv_beta, nuAlgEquiv_gamma]

/-! ## 4. Woronowicz Haar Modular Identity on `(α, δ)` -/

/-- Cleared Woronowicz Haar evaluation on `α * δ` and `δ * α`: for any `R`-linear functional
`h : OqSU2 R q →ₗ[R] R` satisfying `(1 + q²) * h(β * γ) = -(q * h(1))`, we have
`(1 + q²) * h(α * δ) = h(1)` and `(1 + q²) * h(δ * α) = q² * h(1)`. -/
theorem haar_cleared_alpha_delta (q : Rˣ) (h : OqSU2 R q →ₗ[R] R)
    (hbg : (1 + (q : R) ^ 2) * h (β q * γ q) = -(q : R) * h 1) :
    (1 + (q : R) ^ 2) * h (α q * δ q) = h 1 ∧
      (1 + (q : R) ^ 2) * h (δ q * α q) = (q : R) ^ 2 * h 1 := by
  have hL : h (α q * δ q) - (q : R) * h (β q * γ q) = h 1 := by
    have := congr_arg h (rel_det_left (R := R) q)
    simpa [map_sub, map_smul, smul_eq_mul] using this
  have hR : h (δ q * α q) - (((q⁻¹ : Rˣ) : R)) * h (β q * γ q) = h 1 := by
    have := congr_arg h (rel_det_right (R := R) q)
    simpa [map_sub, map_smul, smul_eq_mul] using this
  have hqi : (((q⁻¹ : Rˣ) : R)) * (q : R) = 1 := Units.inv_mul q
  refine ⟨?_, ?_⟩
  · linear_combination (1 + (q : R) ^ 2) * hL + (q : R) * hbg
  · linear_combination
      (1 + (q : R) ^ 2) * hR + (((q⁻¹ : Rˣ) : R)) * hbg - h 1 * hqi

/-- **Haar Modular Asymmetry & Swap Law (`h(δ α) = q² h(α δ)`):**
Whenever `u = 1 + q²` is invertible, Woronowicz's rank-1 Haar value
`h(β * γ) = -(q * u⁻¹ * h(1))` forces:
1. `h(δ * α) = q² * h(α * δ)`,
2. `h(δ * α) = h(ν_q(α) * δ)`,
3. `h(α * δ) = h(δ * ν_q⁻¹(α))`. -/
theorem haar_modular_swap_alpha_delta (q u : Rˣ) (hu : (u : R) = 1 + (q : R) ^ 2)
    (h : OqSU2 R q →ₗ[R] R)
    (hbg : h (β q * γ q) = -((q : R) * (((u⁻¹ : Rˣ) : R)) * h 1)) :
    h (δ q * α q) = (q : R) ^ 2 * h (α q * δ q) ∧
    h (δ q * α q) = h (nuAlgEquiv q (α q) * δ q) ∧
    h (α q * δ q) = h (δ q * (nuAlgEquiv q).symm (α q)) := by
  have hbg_cleared : (1 + (q : R) ^ 2) * h (β q * γ q) = -(q : R) * h 1 := by
    rw [← hu, hbg]
    have hui : (u : R) * (((u⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv u
    linear_combination -(q : R) * h 1 * hui
  obtain ⟨hAD, hDA⟩ := haar_cleared_alpha_delta q h hbg_cleared
  rw [← hu] at hAD hDA
  have hui : (((u⁻¹ : Rˣ) : R)) * (u : R) = 1 := Units.inv_mul u
  have had_eq : h (α q * δ q) = (((u⁻¹ : Rˣ) : R)) * h 1 := by
    linear_combination (((u⁻¹ : Rˣ) : R)) * hAD - h (α q * δ q) * hui
  have hda_eq : h (δ q * α q) = (q : R) ^ 2 * (((u⁻¹ : Rˣ) : R)) * h 1 := by
    linear_combination (((u⁻¹ : Rˣ) : R)) * hDA - h (δ q * α q) * hui
  have hratio : h (δ q * α q) = (q : R) ^ 2 * h (α q * δ q) := by
    rw [hda_eq, had_eq, mul_assoc]
  refine ⟨hratio, ?_, ?_⟩
  · rw [nuAlgEquiv_alpha, Algebra.smul_mul_assoc, map_smul, smul_eq_mul, hratio]
  · rw [nuAlgEquiv_symm_alpha, Algebra.mul_smul_comm, map_smul, smul_eq_mul, hratio]
    have hq2 : ((((q⁻¹ : Rˣ) : R)) ^ 2) * ((q : R) ^ 2) = 1 := by
      rw [← mul_pow, Units.inv_mul, one_pow]
    linear_combination -h (α q * δ q) * hq2

/-! ## 5. Opposite-Algebra `q ↔ q⁻¹` Bar Map and Compact `∗`-Involution -/

/-- Lift an `R`-algebra homomorphism `f : A →ₐ[R] B` to opposite algebras `Aᵐᵒᵖ →ₐ[R] Bᵐᵒᵖ`. -/
def algHomOp {A B : Type*} [Ring A] [Algebra R A] [Ring B] [Algebra R B]
    (f : A →ₐ[R] B) : Aᵐᵒᵖ →ₐ[R] Bᵐᵒᵖ where
  toFun x := MulOpposite.op (f (MulOpposite.unop x))
  map_one' := by simp
  map_mul' x y := by simp [← MulOpposite.op_mul, map_mul]
  map_zero' := by simp
  map_add' x y := by simp [← MulOpposite.op_add, map_add]
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, MulOpposite.unop_smul, MulOpposite.unop_one,
      map_smul, map_one, MulOpposite.op_smul, MulOpposite.op_one]

/-- Turn `g : B →ₐ[R] Aᵐᵒᵖ` into `Bᵐᵒᵖ →ₐ[R] A`. -/
def algHomFromOp {A B : Type*} [Ring A] [Algebra R A] [Ring B] [Algebra R B]
    (g : B →ₐ[R] Aᵐᵒᵖ) : Bᵐᵒᵖ →ₐ[R] A where
  toFun x := MulOpposite.unop (g (MulOpposite.unop x))
  map_one' := by simp
  map_mul' x y := by
    change MulOpposite.unop (g (MulOpposite.unop y * MulOpposite.unop x)) = _
    rw [map_mul, MulOpposite.unop_mul]
  map_zero' := by simp
  map_add' x y := by simp [map_add]
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one, MulOpposite.unop_smul, MulOpposite.unop_one,
      map_smul, map_one]

/-- Cast-free opposite-algebra homomorphism `OqSU2 R q →ₐ[R] (OqSU2 R p)ᵐᵒᵖ` for any inverse
unit pair `q * p = 1`, sending `(α, β, γ, δ) ↦ (op α', op β', op γ', op δ')`. -/
noncomputable def qInvPairToOpAlgHom (q p : Rˣ) (hqp : q * p = 1) :
    OqSU2 R q →ₐ[R] (OqSU2 R p)ᵐᵒᵖ :=
  have hp_eq : p = q⁻¹ := eq_inv_of_mul_eq_one_right hqp
  have hq_eq : q = p⁻¹ := eq_inv_of_mul_eq_one_left hqp
  liftQuadruple q
    (MulOpposite.op (α (R := R) p))
    (MulOpposite.op (β (R := R) p))
    (MulOpposite.op (γ (R := R) p))
    (MulOpposite.op (δ (R := R) p))
    { ab := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [rel_ab p, smul_smul, ← Units.val_mul, hqp, Units.val_one, one_smul]
      ag := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [rel_ag p, smul_smul, ← Units.val_mul, hqp, Units.val_one, one_smul]
      bd := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [rel_bd p, smul_smul, ← Units.val_mul, hqp, Units.val_one, one_smul]
      gd := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [rel_gd p, smul_smul, ← Units.val_mul, hqp, Units.val_one, one_smul]
      bg := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, rel_bg p]
      det_left := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul,
          ← MulOpposite.op_sub, ← MulOpposite.op_one]
        congr 1
        rw [← rel_bg p, hq_eq]
        exact rel_det_right (R := R) p
      det_right := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul,
          ← MulOpposite.op_sub, ← MulOpposite.op_one]
        congr 1
        rw [← rel_bg p, ← hp_eq]
        exact rel_det_left (R := R) p }

/-- **Exact `q ↔ q⁻¹` Opposite-Algebra Isomorphism (`OqSU2 R q ≃ₐ[R] (OqSU2 R q⁻¹)ᵐᵒᵖ`).** -/
noncomputable def qInvOpAlgEquiv (q : Rˣ) : OqSU2 R q ≃ₐ[R] (OqSU2 R q⁻¹)ᵐᵒᵖ :=
  let fwd := qInvPairToOpAlgHom (R := R) q q⁻¹ (mul_inv_cancel q)
  let bwd := algHomFromOp (qInvPairToOpAlgHom (R := R) q⁻¹ q (inv_mul_cancel q))
  have hbwd_fwd : bwd.comp fwd = AlgHom.id R (OqSU2 R q) := by
    apply algHom_ext <;> simp [fwd, bwd, qInvPairToOpAlgHom, algHomFromOp]
  have hfwd_bwd_inner :
      (algHomFromOp fwd).comp (qInvPairToOpAlgHom (R := R) q⁻¹ q (inv_mul_cancel q)) =
        AlgHom.id R (OqSU2 R q⁻¹) := by
    apply algHom_ext <;> simp [fwd, qInvPairToOpAlgHom, algHomFromOp]
  AlgEquiv.ofAlgHom fwd bwd
    (by
      ext x
      have h := AlgHom.congr_fun hfwd_bwd_inner (MulOpposite.unop x)
      exact MulOpposite.unop_injective h)
    hbwd_fwd

/-- Underlying `R`-linear `q ↔ q⁻¹` bar anti-isomorphism `(·)^‡ : OqSU2 R q →ₗ[R] OqSU2 R q⁻¹`. -/
noncomputable def qInvBar (q : Rˣ) : OqSU2 R q →ₗ[R] OqSU2 R q⁻¹ where
  toFun x := MulOpposite.unop (qInvOpAlgEquiv q x)
  map_add' x y := by simp [map_add]
  map_smul' r x := by simp [map_smul]

theorem qInvBar_mul (q : Rˣ) (x y : OqSU2 R q) :
    qInvBar q (x * y) = qInvBar q y * qInvBar q x := by
  simp only [qInvBar, LinearMap.coe_mk, AddHom.coe_mk, map_mul, MulOpposite.unop_mul]

/-- **Modular–CPT Invert-Commutation for the `q ↔ q⁻¹` Bar Anti-Isomorphism:**
For **every** `x : OqSU2 R q`, `(ν_q x)^‡ = ν_{q⁻¹}⁻¹ (x^‡)`. -/
theorem qInvBar_nu_comm (q : Rˣ) (x : OqSU2 R q) :
    qInvBar q (nuAlgEquiv q x) = (nuAlgEquiv q⁻¹).symm (qInvBar q x) := by
  let lhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q⁻¹)ᵐᵒᵖ :=
    (qInvOpAlgEquiv q).toAlgHom.comp (nuAlgEquiv q).toAlgHom
  let rhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q⁻¹)ᵐᵒᵖ :=
    (algHomOp (nuAlgEquiv q⁻¹).symm.toAlgHom).comp (qInvOpAlgEquiv q).toAlgHom
  have heq : lhsHom = rhsHom := by
    apply algHom_ext <;>
      simp [lhsHom, rhsHom, qInvOpAlgEquiv, qInvPairToOpAlgHom, algHomOp]
  have hx := AlgHom.congr_fun heq x
  exact congr_arg MulOpposite.unop hx

/-- **Woronowicz's Compact `∗`-Anti-Homomorphism (`OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ`):**
Sends `(α, β, γ, δ) ↦ (op δ, op(-q • γ), op(-q⁻¹ • β), op α)`. -/
noncomputable def compactStarToOpAlgHom (q : Rˣ) : OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
  liftQuadruple q
    (MulOpposite.op (δ (R := R) q))
    (MulOpposite.op (-(q : R) • γ (R := R) q))
    (MulOpposite.op (-(((q⁻¹ : Rˣ) : R)) • β (R := R) q))
    (MulOpposite.op (α (R := R) q))
    { ab := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_gd q, smul_smul]
        simp only [smul_smul]
        congr 1
        ring
      ag := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_bd q]
        simp only [smul_smul, neg_mul, Units.inv_mul, Units.mul_inv, mul_neg]
      bd := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [Algebra.mul_smul_comm, Algebra.smul_mul_assoc, rel_ag q]
        simp only [smul_smul]
        congr 1
        ring
      gd := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul]
        congr 1
        rw [Algebra.mul_smul_comm, Algebra.smul_mul_assoc, rel_ab q]
        simp only [smul_smul, neg_mul, mul_neg, Units.inv_mul, Units.mul_inv]
      bg := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul]
        congr 1
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm,
          Algebra.smul_mul_assoc, Algebra.mul_smul_comm, rel_bg q]
        simp only [smul_smul, neg_mul, mul_neg, neg_neg, Units.inv_mul, Units.mul_inv]
      det_left := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul,
          ← MulOpposite.op_sub, ← MulOpposite.op_one]
        congr 1
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul, neg_mul, mul_neg, neg_neg, Units.inv_mul, mul_one]
        exact rel_det_left q
      det_right := by
        rw [← MulOpposite.op_mul, ← MulOpposite.op_mul, ← MulOpposite.op_smul,
          ← MulOpposite.op_sub, ← MulOpposite.op_one]
        congr 1
        rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm]
        simp only [smul_smul, neg_mul, mul_neg, neg_neg, Units.inv_mul, mul_one]
        exact rel_det_right q }

/-- **Woronowicz Compact `∗`-Anti-Isomorphism (`OqSU2 R q ≃ₐ[R] (OqSU2 R q)ᵐᵒᵖ`).** -/
noncomputable def compactStarOpAlgEquiv (q : Rˣ) : OqSU2 R q ≃ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
  let fwd := compactStarToOpAlgHom (R := R) q
  let bwd := algHomFromOp fwd
  have hcomp : bwd.comp fwd = AlgHom.id R (OqSU2 R q) := by
    apply algHom_ext <;>
      simp [fwd, bwd, compactStarToOpAlgHom, algHomFromOp, smul_smul,
        Units.inv_mul, Units.mul_inv]
  AlgEquiv.ofAlgHom fwd bwd
    (by
      ext x
      have h := AlgHom.congr_fun hcomp (MulOpposite.unop x)
      exact MulOpposite.unop_injective h)
    hcomp

/-- Underlying involutive `R`-linear anti-automorphism `(·)^∗ : OqSU2 R q →ₗ[R] OqSU2 R q`. -/
noncomputable def compactStar (q : Rˣ) : OqSU2 R q →ₗ[R] OqSU2 R q where
  toFun x := MulOpposite.unop (compactStarOpAlgEquiv q x)
  map_add' x y := by simp [map_add]
  map_smul' r x := by simp [map_smul]

theorem compactStar_mul (q : Rˣ) (x y : OqSU2 R q) :
    compactStar q (x * y) = compactStar q y * compactStar q x := by
  simp only [compactStar, LinearMap.coe_mk, AddHom.coe_mk, map_mul, MulOpposite.unop_mul]

theorem compactStar_involutive (q : Rˣ) (x : OqSU2 R q) :
    compactStar q (compactStar q x) = x :=
  (compactStarOpAlgEquiv q).symm_apply_apply x

/-- **Modular–Star Invert-Commutation on All of `O_q(SU(2))`:**
For **every** `x : OqSU2 R q`, `(ν_q x)^∗ = ν_q⁻¹ (x^∗)`. -/
theorem compactStar_nu_comm (q : Rˣ) (x : OqSU2 R q) :
    compactStar q (nuAlgEquiv q x) = (nuAlgEquiv q).symm (compactStar q x) := by
  let lhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
    (compactStarOpAlgEquiv q).toAlgHom.comp (nuAlgEquiv q).toAlgHom
  let rhsHom : OqSU2 R q →ₐ[R] (OqSU2 R q)ᵐᵒᵖ :=
    (algHomOp (nuAlgEquiv q).symm.toAlgHom).comp (compactStarOpAlgEquiv q).toAlgHom
  have heq : lhsHom = rhsHom := by
    apply algHom_ext <;>
      simp [lhsHom, rhsHom, compactStarOpAlgEquiv, compactStarToOpAlgHom, algHomOp]
  have hx := AlgHom.congr_fun heq x
  exact congr_arg MulOpposite.unop hx

end OqSU2

end Presentation

end QOU.AlgebraicSubstrate
