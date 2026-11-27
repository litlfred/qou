import QOU.Nuclear.ECatLPDualRadical
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Fin
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Explicit Solver-Free Shadow-Price Evaluation on the 6D `H₃(q)` Normal-Form Basis

Bean `qou-udad`. Completes the formalize-first programme opened by
`QOU.QBeta.ECatLPDualRadical` on the **6-dimensional Coxeter normal-form operator basis**
of `H₃(q)`:

    b = (1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀),     ℓ(wᵢ) = (0, 1, 1, 2, 2, 3).

Recall what `qbeta_ecat_lp_radical_pairing_probe` established on the 3D Wedderburn block
basis: because the diagonal Gram `diag(y_λ dim_λ)` and any `y_λ`-weighted per-block cost
`t_λ = y_λ f(λ)` share the vanishing Convention-D weight `y_(1³) = 0`, `<t, v> = 0` holds
by construction (`ECatLPDualRadical.diagonal_gram_kills_every_cost_on_its_diagonal`).
That left open the 6D operator-basis LP, where the Convention-D Markov Gram
`G_{D,ij} = tr_M(bᵢ bⱼ)` (`z_D = q³ / (q² + 1)`) has rank 5 with 1D radical spanned by
the `q`-antisymmetriser

    v_(1³) = (1, -q⁻¹, -q⁻¹, q⁻², q⁻², -q⁻³),     vᵢ = (-q⁻¹)^{ℓ(wᵢ)},

and polynomial rescale `ṽ_(1³) = (-q³) • v_(1³) = (-q³, q², q², -q, -q, 1)`.

## Main Results (all `sorry`-free, generic field `F` per §7c)

1. **Closed-form normalisation `<1, v_(1³)>` (`ECatLPDualRadical`'s hypothesis `hone`):**
   - `inner_one_radicalPoly3`: `∑ i, 1 * ṽᵢ = -(q - 1) * (q² - q + 1)`.
   - `inner_one_radicalVec3`: `∑ i, 1 * vᵢ = (q - 1) * (q² - q + 1) / q³` for `q ≠ 0`.
   - `cyclotomic6_pos` & `inner_one_radicalVec3_ne_zero`: over any ordered field,
     `q² - q + 1 > 0` everywhere, so `<1, v_(1³)> ≠ 0` for all `q ≠ 0, q ≠ 1`.

2. **Exact non-orthogonality criterion on the 6D Coxeter basis:**
   - `inner_coxeterSymmetric_radicalVec3` & `inner_coxeterSymmetric_ne_zero_iff`: for any
     generator-symmetric cost `t = (c₀, c₁, c₁, c₂, c₂, c₃)` on `H₃(q)`,
     `<t, v_(1³)> = (c₀ q³ - 2 c₁ q² + 2 c₂ q - c₃) / q³`, which is nonzero iff
     `c₀ q³ - 2 c₁ q² + 2 c₂ q - c₃ ≠ 0`.
   - `inner_heckeTraceCost_radicalVec3_eq_zero`: the Convention-D Markov trace vector
     `(1, z_D, z_D, z_D², z_D², h z_D² + z_D)` satisfies `<t_Hecke, v_(1³)> = 0`
     identically over any field (`q ≠ 0, q² + 1 ≠ 0`), recovering the recorded collapse.
   - `inner_ecatPairCyclicCost_radicalVec3` & `ecatPairCyclic_shadowPrice_ne_zero`: the
     separation-weighted `ECatProbeAssertions` cyclic pair kernel `(0, 0, 0, z_D², z_D²,
     2 z_D² + h z_D + 1)` has exact pairing
     `<t_pair, v_(1³)> = (2 q⁷ - 3 q⁶ - q⁴ - q² - 1) / (q³ (q² + 1)²)`, which is strictly
     negative on `0 < q ≤ 3/2` (`1 < q₀ < 3/2`), forcing a **nonzero** solver-free dual
     shadow price `y₀`!
   - `inner_thomaeJacksonCrossing_radicalVec3` & `thomaeJacksonCrossing_shadowPrice_ne_zero`:
     any nonzero step-weighted Coxeter crossing-count cost `tᵢ = w * ℓ(wᵢ)` (including the
     backward Thomae–Jackson `w = q⁻²` proper-time step) has
     `<t_len, v_(1³)> = -w * (2 q² - 4 q + 3) / q³`, which is strictly nonzero for every
     `q ≠ 0` over any ordered field (`2 q² - 4 q + 3 = 2 (q - 1)² + 1 > 0`).
   - `inner_thomaeJacksonGeom_radicalVec3`: cumulative backward Thomae–Jackson cost has
     `<t_TJ,geom, v_(1³)> = -(q - 1) * (q⁵ - q⁴ + q³ + q² - q + 1) / q⁵`.

3. **Scale invariance, residual orthogonality, and 1-parameter dual feasibility affine line:**
   - `shadowPrice_scale_invariant`: replacing `v` by `c • v` (`c ≠ 0`) leaves
     `<t, v> / <1, v>` unchanged.
   - `residual_orthogonal_to_radical`: setting `y₀ = <t, v> / <1, v>` forces
     `<t - y₀ • 1, v> = 0` identically (landing `t - y₀ • 1` inside `v⊥ = Im(G_D)`).
   - `dual_equality_shift_along_radical`: shifting any dual equality solution `y` along
     the radical (`yᵢ + α * vᵢ`) preserves `y₀ • 1 + G y = t` identically.
-/

namespace QOU.Nuclear.ECatRadicalShadowPriceEvaluation

open BigOperators
open QOU.QBeta.ECatLPDualRadical

/-! ### 1. Six-element Coxeter basis of `H₃(q)` and the `(1³)` `q`-antisymmetriser -/

section GenericField

variable {F : Type*} [Field F]

/-- Unroll a sum over `Fin 6` into its six explicit terms `(0, 1, 2, 3, 4, 5)`. -/
theorem sum_fin6 {M : Type*} [AddCommMonoid M] (f : Fin 6 → M) :
    (∑ i : Fin 6, f i) = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 := by
  simpa [add_assoc] using Fin.sum_univ_six f

/-- Coxeter word lengths `(0, 1, 1, 2, 2, 3)` of the standard `H₃(q)` normal-form basis
`(1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀)`. -/
def coxeterLen3 : Fin 6 → ℕ
  | ⟨0, _⟩ => 0
  | ⟨1, _⟩ => 1
  | ⟨2, _⟩ => 1
  | ⟨3, _⟩ => 2
  | ⟨4, _⟩ => 2
  | ⟨5, _⟩ => 3

/-- Constant all-ones vector `1` on `Fin 6`. -/
def allOnes6 : Fin 6 → F := fun _ => 1

/-- The `(1³)` `q`-antisymmetriser `vᵢ = (-q⁻¹)^{ℓ(wᵢ)} = (1, -q⁻¹, -q⁻¹, q⁻², q⁻², -q⁻³)`
spanning the Convention-D Markov Gram radical on `H₃(q)` (`pyhecke.gram.radical_mp`). -/
def radicalVec3 (q : F) : Fin 6 → F :=
  fun i => (-q⁻¹) ^ coxeterLen3 i

/-- Polynomial normalisation `ṽ_(1³) = (-q³, q², q², -q, -q, 1)` of the `H₃(q)` radical
(`operator_selection_lp.lean`). -/
def radicalPoly3 (q : F) : Fin 6 → F
  | ⟨0, _⟩ => -q ^ 3
  | ⟨1, _⟩ => q ^ 2
  | ⟨2, _⟩ => q ^ 2
  | ⟨3, _⟩ => -q
  | ⟨4, _⟩ => -q
  | ⟨5, _⟩ => 1

/-- `radicalPoly3 q` equals `(-q³)` times `radicalVec3 q` componentwise whenever `q ≠ 0`. -/
theorem radicalPoly3_eq_neg_q_cube_mul {q : F} (hq : q ≠ 0) (i : Fin 6) :
    radicalPoly3 q i = (-q ^ 3) * radicalVec3 q i := by
  fin_cases i <;> simp [radicalPoly3, radicalVec3, coxeterLen3] <;> field_simp

/-- **Closed-form `<1, ṽ_(1³)>` (polynomial normalisation):**
`∑ i, 1 * ṽᵢ = -(q - 1) * (q² - q + 1)`. -/
theorem inner_one_radicalPoly3 (q : F) :
    (∑ i : Fin 6, allOnes6 i * radicalPoly3 q i) = -(q - 1) * (q ^ 2 - q + 1) := by
  rw [sum_fin6]
  change (1 : F) * (-q ^ 3) + 1 * q ^ 2 + 1 * q ^ 2 + 1 * (-q) + 1 * (-q) + 1 * 1 =
    -(q - 1) * (q ^ 2 - q + 1)
  ring

/-- **Closed-form `<1, v_(1³)>` (`(-q⁻¹)^{ℓ(w)}` normalisation):**
`∑ i, 1 * vᵢ = (q - 1) * (q² - q + 1) / q³` for `q ≠ 0`. -/
theorem inner_one_radicalVec3 {q : F} (hq : q ≠ 0) :
    (∑ i : Fin 6, allOnes6 i * radicalVec3 q i) = (q - 1) * (q ^ 2 - q + 1) / q ^ 3 := by
  rw [sum_fin6]
  change (1 : F) * (-q⁻¹) ^ 0 + 1 * (-q⁻¹) ^ 1 + 1 * (-q⁻¹) ^ 1 +
      1 * (-q⁻¹) ^ 2 + 1 * (-q⁻¹) ^ 2 + 1 * (-q⁻¹) ^ 3 =
    (q - 1) * (q ^ 2 - q + 1) / q ^ 3
  field_simp
  ring

/-! ### 2. Exact pairing and non-orthogonality criteria on `H₃(q)` -/

/-- A 6D cost vector `(c₀, c₁, c₁, c₂, c₂, c₃)` symmetric under swapping the two braid
generators `σ₀ ↔ σ₁` (hence depending only on Coxeter length on `H₃(q)`). -/
def coxeterSymmetricCost (c0 c1 c2 c3 : F) : Fin 6 → F
  | ⟨0, _⟩ => c0
  | ⟨1, _⟩ => c1
  | ⟨2, _⟩ => c1
  | ⟨3, _⟩ => c2
  | ⟨4, _⟩ => c2
  | ⟨5, _⟩ => c3

/-- Closed-form inner product `<t, v_(1³)> = (c₀ q³ - 2 c₁ q² + 2 c₂ q - c₃) / q³`. -/
theorem inner_coxeterSymmetric_radicalVec3 {q : F} (hq : q ≠ 0) (c0 c1 c2 c3 : F) :
    (∑ i : Fin 6, coxeterSymmetricCost c0 c1 c2 c3 i * radicalVec3 q i) =
      (c0 * q ^ 3 - 2 * c1 * q ^ 2 + 2 * c2 * q - c3) / q ^ 3 := by
  rw [sum_fin6]
  change c0 * (-q⁻¹) ^ 0 + c1 * (-q⁻¹) ^ 1 + c1 * (-q⁻¹) ^ 1 +
      c2 * (-q⁻¹) ^ 2 + c2 * (-q⁻¹) ^ 2 + c3 * (-q⁻¹) ^ 3 =
    (c0 * q ^ 3 - 2 * c1 * q ^ 2 + 2 * c2 * q - c3) / q ^ 3
  field_simp
  ring

/-- **Exact non-orthogonality criterion** (`ECatLPDualRadical`'s escape bar `<t, v> ≠ 0`):
for `q ≠ 0`, `coxeterSymmetricCost c0 c1 c2 c3` is non-orthogonal to `radicalVec3 q`
if and only if the cubic alternating polynomial `c₀ q³ - 2 c₁ q² + 2 c₂ q - c₃ ≠ 0`. -/
theorem inner_coxeterSymmetric_ne_zero_iff {q : F} (hq : q ≠ 0) (c0 c1 c2 c3 : F) :
    (∑ i : Fin 6, coxeterSymmetricCost c0 c1 c2 c3 i * radicalVec3 q i) ≠ 0 ↔
      c0 * q ^ 3 - 2 * c1 * q ^ 2 + 2 * c2 * q - c3 ≠ 0 := by
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  have hq3 : q ^ 3 ≠ 0 := pow_ne_zero 3 hq
  exact div_ne_zero_iff.trans (and_iff_left hq3)

/-- Convention-D Markov parameter `z_D(q) = q³ / (q² + 1)`. -/
def markovZ_D (q : F) : F := q ^ 3 / (q ^ 2 + 1)

/-- Hecke quadratic-relation parameter `h(q) = q - q⁻¹`. -/
def heckeH (q : F) : F := q - q⁻¹

/-- Control cost C0: the Convention-D Markov trace vector
`t_Hecke = (1, z_D, z_D, z_D², z_D², h z_D² + z_D)`. -/
def heckeTraceCost (q : F) : Fin 6 → F :=
  let z := markovZ_D q
  let h := heckeH q
  coxeterSymmetricCost 1 z (z ^ 2) (h * z ^ 2 + z)

/-- **Structural collapse check:** `<t_Hecke, v_(1³)> = 0` identically over any field
whenever `q ≠ 0` and `q² + 1 ≠ 0`. -/
theorem inner_heckeTraceCost_radicalVec3_eq_zero {q : F} (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    (∑ i : Fin 6, heckeTraceCost q i * radicalVec3 q i) = 0 := by
  unfold heckeTraceCost markovZ_D heckeH
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  field_simp
  ring

/-- Candidate cost C1a (`ECatProbeAssertions` cyclic separation-weighted pair kernel on
each Coxeter basis word `wᵢ` of `H₃(q)`):
`(0, 0, 0, z_D², z_D², 2 z_D² + h z_D + 1)`. -/
def ecatPairCyclicCost (q : F) : Fin 6 → F :=
  let z := markovZ_D q
  let h := heckeH q
  coxeterSymmetricCost 0 0 (z ^ 2) (2 * z ^ 2 + h * z + 1)

/-- **Closed-form `<t_pair,cyc, v_(1³)>`:**
`<t_pair,cyc, v_(1³)> = (2 q⁷ - 3 q⁶ - q⁴ - q² - 1) / (q³ (q² + 1)²)`. -/
theorem inner_ecatPairCyclicCost_radicalVec3 {q : F} (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    (∑ i : Fin 6, ecatPairCyclicCost q i * radicalVec3 q i) =
      (2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1) / (q ^ 3 * (q ^ 2 + 1) ^ 2) := by
  unfold ecatPairCyclicCost markovZ_D heckeH
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  field_simp
  ring

/-- Candidate cost C1b (open-word separation `d_open(a,b) = b - a` pair kernel on `H₃(q)`):
`(0, 0, 0, z_D², z_D², 2 z_D² + (h z_D + 1) / 4)`. -/
def ecatPairOpenCost (q : F) : Fin 6 → F :=
  let z := markovZ_D q
  let h := heckeH q
  coxeterSymmetricCost 0 0 (z ^ 2) (2 * z ^ 2 + (h * z + 1) / 4)

/-- **Closed-form `<t_pair,open, v_(1³)>` (over `[CharZero F]` so `4 ≠ 0`):**
`<t_pair,open, v_(1³)> = (8 q⁷ - 9 q⁶ - q⁴ - q² - 1) / (4 q³ (q² + 1)²)`. -/
theorem inner_ecatPairOpenCost_radicalVec3 [CharZero F] {q : F} (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) :
    (∑ i : Fin 6, ecatPairOpenCost q i * radicalVec3 q i) =
      (8 * q ^ 7 - 9 * q ^ 6 - q ^ 4 - q ^ 2 - 1) / (4 * q ^ 3 * (q ^ 2 + 1) ^ 2) := by
  unfold ecatPairOpenCost markovZ_D heckeH
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  have h4 : (4 : F) ≠ 0 := by norm_num
  field_simp
  ring

/-- Candidate cost C2a: step-weighted Coxeter crossing-count cost `tᵢ = w * ℓ(wᵢ)`
(specialising at `w = q⁻²` to the backward Thomae–Jackson proper-time step cost). -/
def thomaeJacksonCrossingCost (w : F) : Fin 6 → F :=
  coxeterSymmetricCost 0 w (2 * w) (3 * w)

/-- **Closed-form `<t_len, v_(1³)>`:**
`<t_len, v_(1³)> = -w * (2 q² - 4 q + 3) / q³`. -/
theorem inner_thomaeJacksonCrossing_radicalVec3 {q : F} (hq : q ≠ 0) (w : F) :
    (∑ i : Fin 6, thomaeJacksonCrossingCost w i * radicalVec3 q i) =
      -w * (2 * q ^ 2 - 4 * q + 3) / q ^ 3 := by
  unfold thomaeJacksonCrossingCost
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  field_simp
  ring

/-- Candidate cost C2b: cumulative backward Thomae–Jackson geometric-lattice cost
`tᵢ = q⁻² * ((q²)^{ℓ(wᵢ)} - 1) = (0, 1 - q⁻², 1 - q⁻², q² - q⁻², q² - q⁻², q⁴ - q⁻²)`. -/
def thomaeJacksonGeomCost (q : F) : Fin 6 → F :=
  coxeterSymmetricCost 0 (1 - q⁻¹ ^ 2) (q ^ 2 - q⁻¹ ^ 2) (q ^ 4 - q⁻¹ ^ 2)

/-- **Closed-form `<t_TJ,geom, v_(1³)>`:**
`<t_TJ,geom, v_(1³)> = -(q - 1) * (q⁵ - q⁴ + q³ + q² - q + 1) / q⁵`. -/
theorem inner_thomaeJacksonGeom_radicalVec3 {q : F} (hq : q ≠ 0) :
    (∑ i : Fin 6, thomaeJacksonGeomCost q i * radicalVec3 q i) =
      -(q - 1) * (q ^ 5 - q ^ 4 + q ^ 3 + q ^ 2 - q + 1) / q ^ 5 := by
  unfold thomaeJacksonGeomCost
  rw [inner_coxeterSymmetric_radicalVec3 hq]
  field_simp
  ring

/-! ### 3. Scale invariance, residual orthogonality, and 1D dual feasibility line -/

/-- Scaling the radical generator `v ↦ c • v` (`c ≠ 0`) leaves the solver-free shadow price
`y₀ = <t, v> / <1, v>` strictly invariant. -/
theorem shadowPrice_scale_invariant {ι : Type*} [Fintype ι]
    (t one v : ι → F) {c : F} (hc : c ≠ 0) :
    (∑ i, t i * (c * v i)) / (∑ i, one i * (c * v i)) =
      (∑ i, t i * v i) / (∑ i, one i * v i) := by
  have h1 : (∑ i, t i * (c * v i)) = c * ∑ i, t i * v i := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun i _ => by ring)
  have h2 : (∑ i, one i * (c * v i)) = c * ∑ i, one i * v i := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun i _ => by ring)
  rw [h1, h2, mul_div_mul_left _ _ hc]

/-- **Residual orthogonality (`t - y₀ • 1 ∈ v⊥`):**
Setting `y₀ = <t, v> / <1, v>` guarantees `<t - y₀ • 1, v> = 0` identically, so
`t - y₀ • 1` lies in `v⊥ = Im(G_D)` for *every* cost vector `t`. -/
theorem residual_orthogonal_to_radical {ι : Type*} [Fintype ι]
    (t one v : ι → F) (hone : ∑ i, one i * v i ≠ 0) :
    let y₀ := (∑ i, t i * v i) / (∑ i, one i * v i)
    (∑ i, (t i - y₀ * one i) * v i) = 0 := by
  intro y₀
  have hsub : (∑ i, (t i - y₀ * one i) * v i) =
      (∑ i, t i * v i) - y₀ * (∑ i, one i * v i) := by
    calc (∑ i, (t i - y₀ * one i) * v i)
        = ∑ i, (t i * v i - y₀ * (one i * v i)) :=
          Finset.sum_congr rfl (fun _ _ => by ring)
      _ = (∑ i, t i * v i) - ∑ i, y₀ * (one i * v i) := by rw [Finset.sum_sub_distrib]
      _ = (∑ i, t i * v i) - y₀ * (∑ i, one i * v i) := by rw [← Finset.mul_sum]
  rw [hsub]
  dsimp [y₀]
  rw [div_mul_cancel₀ _ hone, sub_self]

/-- **One-parameter affine solution line for dual feasibility:**
If `v` lies in the right kernel of `G` (`∀ j, ∑ i, G j i * v i = 0`), then shifting any
solution `y` of `y₀ • 1 + G y = t` along `v` (`y' i = y i + α * v i`) satisfies the exact
same dual equality `y₀ • 1 + G y' = t` for every scalar `α : F`. -/
theorem dual_equality_shift_along_radical {ι : Type*} [Fintype ι]
    (G : ι → ι → F) (t one v y : ι → F) (y₀ α : F)
    (hker : ∀ j, ∑ i, G j i * v i = 0)
    (hdual : ∀ j, y₀ * one j + (∑ i, G j i * y i) = t j) :
    ∀ j, y₀ * one j + (∑ i, G j i * (y i + α * v i)) = t j := by
  intro j
  have hexp : (∑ i, G j i * (y i + α * v i)) =
      (∑ i, G j i * y i) + α * (∑ i, G j i * v i) := by
    calc (∑ i, G j i * (y i + α * v i))
        = ∑ i, (G j i * y i + α * (G j i * v i)) :=
          Finset.sum_congr rfl (fun _ _ => by ring)
      _ = (∑ i, G j i * y i) + ∑ i, α * (G j i * v i) := Finset.sum_add_distrib
      _ = (∑ i, G j i * y i) + α * (∑ i, G j i * v i) := by rw [← Finset.mul_sum]
  rw [hexp, hker j, mul_zero, add_zero, hdual j]

end GenericField

/-! ### 4. Ordered-field non-vanishing theorems & live shadow-price certificates -/

section OrderedField

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Over any ordered field, `q² - q + 1 > 0` everywhere (`4(q² - q + 1) = (2q - 1)² + 3 > 0`). -/
theorem cyclotomic6_pos (q : F) : 0 < q ^ 2 - q + 1 := by
  have hsq : 0 ≤ (2 * q - 1) ^ 2 := sq_nonneg (2 * q - 1)
  have hid : 4 * (q ^ 2 - q + 1) = (2 * q - 1) ^ 2 + 3 := by ring
  linarith

/-- Over any ordered field, `2 q² - 4 q + 3 > 0` everywhere (`2(q - 1)² + 1 > 0`). -/
theorem crossing_quad_pos (q : F) : 0 < 2 * q ^ 2 - 4 * q + 3 := by
  have hsq : 0 ≤ (q - 1) ^ 2 := sq_nonneg (q - 1)
  have hid : 2 * q ^ 2 - 4 * q + 3 = 2 * (q - 1) ^ 2 + 1 := by ring
  linarith

/-- **`ECatLPDualRadical` normalisation hypothesis `hone` holds unconditionally on `H₃(q)`:**
for every `q ≠ 0` and `q ≠ 1` in an ordered field, `<1, v_(1³)> ≠ 0`. -/
theorem inner_one_radicalVec3_ne_zero {q : F} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    (∑ i : Fin 6, allOnes6 i * radicalVec3 q i) ≠ 0 := by
  rw [inner_one_radicalVec3 hq0]
  have hq3 : q ^ 3 ≠ 0 := pow_ne_zero 3 hq0
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hcyc : q ^ 2 - q + 1 ≠ 0 := ne_of_gt (cyclotomic6_pos q)
  exact div_ne_zero (mul_ne_zero hsub hcyc) hq3

/-- **Nonzero solver-free shadow price for Thomae–Jackson / Coxeter crossing cost:**
for any `q ≠ 0`, `q ≠ 1`, and nonzero step weight `w ≠ 0`, every dual-feasible shadow price
`y₀` for `thomaeJacksonCrossingCost w` is strictly nonzero (`y₀ ≠ 0`) and equals
`-w * (2 q² - 4 q + 3) / ((q - 1) * (q² - q + 1))`. -/
theorem thomaeJacksonCrossing_shadowPrice_closed_form
    {q w y₀ : F} (Gy : Fin 6 → F) (hq0 : q ≠ 0) (hq1 : q ≠ 1) (hw : w ≠ 0)
    (hdual : ∀ j, y₀ * allOnes6 j + Gy j = thomaeJacksonCrossingCost w j)
    (hGy : ∑ i : Fin 6, Gy i * radicalVec3 q i = 0) :
    y₀ = -w * (2 * q ^ 2 - 4 * q + 3) / ((q - 1) * (q ^ 2 - q + 1)) ∧ y₀ ≠ 0 := by
  have hone : (∑ i : Fin 6, allOnes6 i * radicalVec3 q i) ≠ 0 :=
    inner_one_radicalVec3_ne_zero hq0 hq1
  have hquad_ne : 2 * q ^ 2 - 4 * q + 3 ≠ 0 := ne_of_gt (crossing_quad_pos q)
  have hq3_ne : q ^ 3 ≠ 0 := pow_ne_zero 3 hq0
  have htv_ne : (∑ i : Fin 6, thomaeJacksonCrossingCost w i * radicalVec3 q i) ≠ 0 := by
    rw [inner_thomaeJacksonCrossing_radicalVec3 hq0 w]
    exact div_ne_zero (mul_ne_zero (neg_ne_zero.mpr hw) hquad_ne) hq3_ne
  have hy0_ne : y₀ ≠ 0 :=
    dual_price_ne_zero_of_cost_not_orthogonal
      (thomaeJacksonCrossingCost w) allOnes6 (radicalVec3 q) Gy y₀ hdual hGy hone htv_ne
  have hy0_eq : y₀ = -w * (2 * q ^ 2 - 4 * q + 3) / ((q - 1) * (q ^ 2 - q + 1)) := by
    rw [dual_price_determined_by_radical
          (thomaeJacksonCrossingCost w) allOnes6 (radicalVec3 q) Gy y₀ hdual hGy hone,
        inner_thomaeJacksonCrossing_radicalVec3 hq0 w,
        inner_one_radicalVec3 hq0]
    have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
    have hcyc : q ^ 2 - q + 1 ≠ 0 := ne_of_gt (cyclotomic6_pos q)
    field_simp
  exact ⟨hy0_eq, hy0_ne⟩

/-- On the entire substrate half-line `2 * q ≤ 3` (including `q₀ ≈ 1.10998`),
the numerator `2 q⁷ - 3 q⁶ - q⁴ - q² - 1` of `<t_pair,cyc, v_(1³)>` is strictly negative. -/
theorem ecatPairCyclic_numerator_neg {q : F} (hq_ub : 2 * q ≤ 3) :
    2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1 < 0 := by
  have hq6 : 0 ≤ q ^ 6 := Even.pow_nonneg (by decide) q
  have hq4 : 0 ≤ q ^ 4 := Even.pow_nonneg (by decide) q
  have hq2 : 0 ≤ q ^ 2 := sq_nonneg q
  have hprod : q ^ 6 * (2 * q - 3) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hq6 (by linarith)
  have hid : 2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1 =
      q ^ 6 * (2 * q - 3) - q ^ 4 - q ^ 2 - 1 := by ring
  linarith

/-- **Nonzero solver-free shadow price for `ECatProbeAssertions` cyclic pair kernel:**
for every `0 < q` with `q ≠ 1` and `2 * q ≤ 3` (which contains `q₀ ≈ 1.10998`),
`ecatPairCyclicCost q` clears the `ECatLPDualRadical` escape bar (`<t, v_(1³)> ≠ 0`) and
pins every dual-feasible shadow price to the nonzero closed form
`(2 q⁷ - 3 q⁶ - q⁴ - q² - 1) / ((q - 1) * (q² - q + 1) * (q² + 1)²)`. -/
theorem ecatPairCyclic_shadowPrice_closed_form
    {q y₀ : F} (Gy : Fin 6 → F) (hq_pos : 0 < q) (hq1 : q ≠ 1) (hq_ub : 2 * q ≤ 3)
    (hdual : ∀ j, y₀ * allOnes6 j + Gy j = ecatPairCyclicCost q j)
    (hGy : ∑ i : Fin 6, Gy i * radicalVec3 q i = 0) :
    y₀ = (2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1) /
          ((q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + 1) ^ 2) ∧ y₀ ≠ 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq_pos
  have hq2_pos : 0 < q ^ 2 + 1 := by linarith [sq_nonneg q]
  have hq2_ne : q ^ 2 + 1 ≠ 0 := ne_of_gt hq2_pos
  have hone : (∑ i : Fin 6, allOnes6 i * radicalVec3 q i) ≠ 0 :=
    inner_one_radicalVec3_ne_zero hq0 hq1
  have hnum_ne : 2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1 ≠ 0 :=
    ne_of_lt (ecatPairCyclic_numerator_neg hq_ub)
  have hden_ne : q ^ 3 * (q ^ 2 + 1) ^ 2 ≠ 0 :=
    mul_ne_zero (pow_ne_zero 3 hq0) (pow_ne_zero 2 hq2_ne)
  have htv_ne : (∑ i : Fin 6, ecatPairCyclicCost q i * radicalVec3 q i) ≠ 0 := by
    rw [inner_ecatPairCyclicCost_radicalVec3 hq0 hq2_ne]
    exact div_ne_zero hnum_ne hden_ne
  have hy0_ne : y₀ ≠ 0 :=
    dual_price_ne_zero_of_cost_not_orthogonal
      (ecatPairCyclicCost q) allOnes6 (radicalVec3 q) Gy y₀ hdual hGy hone htv_ne
  have hy0_eq : y₀ = (2 * q ^ 7 - 3 * q ^ 6 - q ^ 4 - q ^ 2 - 1) /
      ((q - 1) * (q ^ 2 - q + 1) * (q ^ 2 + 1) ^ 2) := by
    rw [dual_price_determined_by_radical
          (ecatPairCyclicCost q) allOnes6 (radicalVec3 q) Gy y₀ hdual hGy hone,
        inner_ecatPairCyclicCost_radicalVec3 hq0 hq2_ne,
        inner_one_radicalVec3 hq0]
    have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
    have hcyc : q ^ 2 - q + 1 ≠ 0 := ne_of_gt (cyclotomic6_pos q)
    field_simp
  exact ⟨hy0_eq, hy0_ne⟩

end OrderedField

end QOU.Nuclear.ECatRadicalShadowPriceEvaluation
