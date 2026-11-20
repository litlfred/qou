import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.BraidsAndKnots.BorromeanPairwiseLinking

/-!
# Two-term QED beyond first order: every derived covariant term vanishes on `V³` through degree 3

Front: owner instruction 2026-11-20, "Derive to make two-term primary". The question is whether a
**derived** (not selected) QED term on the Borromean nucleon word `V³ = (σ₁σ₂⁻¹)³` exists. The
first-order classes were closed on two sibling branches: the commutant of the crossing action
(`NucleonQEDCovariance`, PR #8552) and the first-order crossing-local strand-labelled insertion,
which is forced to be a scalar and reduces to the coloured writhe `Σ Q_aQ_b·2lk_ab = 0` on `V³`
(`CrossingCovariantQED`, PR #8557). This file goes to **all orders** in the local class and to
**second order** in the non-local class.

## What is proved

* **§E — exact (all-orders, non-perturbative) local insertions.** Replace each letter that
  exchanges the labelled strands `{a, b}` by an arbitrary element of the algebra that crossing
  generates, `σ ↦ x_{ab} σ + y_{ab}` (every element of `span{1, σ}`). The `(0,1)` entry of the
  braid-relation defect for the labelling `(a,b,c)` is an explicit polynomial (`defect3_01`).
  Covariance under the six labellings forces `y_{ab} = t · x_{ab}` for **one** `t` common to all
  pairs, with `t = 0` or `t = −(q − q⁻¹)` (`exact_local_covariant`). `t = −h` is `x_{ab}σ⁻¹`, the
  mirror; the branch connected to the identity is `t = 0`, i.e. a **label-dependent scalar
  rescaling of each crossing**, to every order in the coupling. For uniform coefficients the
  defect is `x·y·(x h + y) • (σ₁ − σ₂)` exactly (`defect3_uniform`).
* **§M — the exact rescaling is a product of linking numbers, hence `1` on `V³`.** With
  `σ^e ↦ u_{ab}^e σ^e`, the deformed `V³` is `facU • V³` where `facU = 1` for every symmetric,
  nonvanishing `u` (`facU_borromean`, `trace_defWordU_borromean`). So the trace of `V³` is
  unchanged **to all orders** in any power series `u_{ab}(ε) = 1 + ε α_{ab} + ε² β_{ab} + …`; in
  particular the `ε²` (second-order, "two-insertion") term of the local class is `0` on proton and
  neutron. Control: on the Hopf word the factor is `u₀₁²` (`facU_hopf`).
* **§D — the naive photon-exchange double sum.** The ordered double crossing sum
  `D = Σ_{c<c'} w_c w_{c'}` with `w_c = e_c α_{ab}` satisfies `2D + Σ w_c² = S²`, `S` the coloured
  writhe (`two_D_add_sq`). It is **not** braid-covariant: prefixing the cancelling pair
  `σ₁σ₁⁻¹` to `V³` changes it by `−α₀₁²` (`doubleSum_r2_borromean`). Its covariant completion
  `D + ½Σw²` is `S²/2`, which is `0` on `V³` (`doubleSum_completion_borromean`).
* **§C — no charge-quadratic coupling to the Milnor invariant exists.** A coupling of the
  alternating `μ̄₁₂₃` that is covariant under relabelling needs a charge weight alternating under
  every transposition. Every such weight that is a polynomial of degree `≤ 2` in the charges is
  **identically zero** (`quad_alternating_eq_zero`), not merely zero on repeated charges. Order
  `α_em` is charge-quadratic, so the second-order Milnor channel is empty at order `α_em`. An
  alternating weight of any degree still vanishes on both nucleons (`alternating_vanishes_on_pair`).
* **§S — the degree-0 terms.** What survives is braid-independent: a charge-symmetric quadratic
  `k₁ ΣQ_a² + k₂ Σ_{a<b} Q_aQ_b` takes `k₁` on the proton and `(2/3)k₁ − (1/3)k₂` on the neutron
  (`degreeZero_values`). On the proton only the self-energy coefficient `k₁` enters, and as a
  scalar insertion it rescales the whole `F_Bor` term — so a proton value of it is not separable
  from `q₀` by the proton mass alone. **`k₁`, `k₂` are not derived here.**

## Scope (AGENTS.md (a)/(b))

§E is a structural exclusion **within the class** of local insertions valued in the crossing's own
algebra `span{1, σ}` (the braid relation is the invariant). §M is exact for that class. §D is a
statement about the specific double sum written, not about every bilinear non-local functional.
§C is structural for polynomial charge weights of degree `≤ 2`. None of this excludes the
degree-4 even term `c₃·Q₁Q₂Q₃·μ̄²` (bean `qou-qc3d`), nor non-local insertions outside §D.

-- Ref: [kassel1995] (Hecke representation of `B₃`; braid relations);
-- [milnor1957] (`μ̄` invariants; antisymmetry under odd relabelling);
-- [evansberger1992] (hierarchy of linking integrals: second level is `μ̄` when pairwise `lk = 0`).
-/

namespace QOU.BraidsAndKnots.QEDHigherOrderCovariance

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.BorromeanPairwiseLinking

variable {R : Type*} [Field R]

/-! ## §E. Exact local insertions -/

/-- The deformed letter `x σ + y`. -/
def loc (x y : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  x • X + y • (1 : Matrix (Fin 3) (Fin 3) R)

/-- Braid-relation defect `σ₁'σ₂'σ₁' − σ₂'σ₁'σ₂'` with the three left letters carrying
`(x₁,y₁), (x₂,y₂), (x₃,y₃)` and the right letters `(x₃,y₃), (x₂,y₂), (x₁,y₁)`. For the labelling
`(a,b,c)` index 1 is the pair `{a,b}`, index 2 the pair `{a,c}`, index 3 the pair `{b,c}`. -/
def defect3 (q x₁ y₁ x₂ y₂ x₃ y₃ : R) : Matrix (Fin 3) (Fin 3) R :=
  loc x₁ y₁ (A₁ q) * loc x₂ y₂ (A₂ q) * loc x₃ y₃ (A₁ q)
    - loc x₃ y₃ (A₂ q) * loc x₂ y₂ (A₁ q) * loc x₁ y₁ (A₂ q)

theorem defect3_01 (q x₁ y₁ x₂ y₂ x₃ y₃ : R) :
    defect3 q x₁ y₁ x₂ y₂ x₃ y₃ 0 1
      = -(q - q⁻¹) * x₁ * x₃ * y₂ - x₁ * y₂ * y₃ + x₂ * y₁ * y₃ - x₃ * y₁ * y₂ := by
  simp [defect3, loc, A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply]
  ring

/-- **Uniform coefficients, exactly:** the defect is `x y (x h + y) • (σ₁ − σ₂)`. -/
theorem defect3_uniform (q x y : R) (hq : q ≠ 0) :
    defect3 q x y x y x y = (x * y * (x * (q - q⁻¹) + y)) • (A₁ q - A₂ q) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [defect3, loc, A₁, A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

theorem sigma_diff_00 (q : R) : (A₁ q - A₂ q) 0 0 = q := by simp [A₁, A₂]

/-- Negative control: a non-scalar, non-mirror uniform insertion is not covariant. -/
theorem defect3_uniform_ne_zero (q x y : R) (hq : q ≠ 0)
    (hxy : x * y * (x * (q - q⁻¹) + y) ≠ 0) : defect3 q x y x y x y ≠ 0 := by
  intro h
  have h00 := congrFun (congrFun h 0) 0
  rw [defect3_uniform q x y hq, Matrix.smul_apply, sigma_diff_00, smul_eq_mul,
    Matrix.zero_apply] at h00
  rcases mul_eq_zero.mp h00 with h1 | h1
  · exact hxy h1
  · exact hq h1

/-- Algebraic core: three ratios with `h (tᵢ + tⱼ) + 2 tᵢ tⱼ = 0` for all distinct pairs are
equal, and the common value satisfies `t (h + t) = 0`. -/
theorem ratios_core (h t₁ t₂ t₃ : R) (hh : h ≠ 0) (h2 : (2 : R) ≠ 0)
    (r₁₂ : h * (t₁ + t₂) + 2 * t₁ * t₂ = 0) (r₁₃ : h * (t₁ + t₃) + 2 * t₁ * t₃ = 0)
    (r₂₃ : h * (t₂ + t₃) + 2 * t₂ * t₃ = 0) :
    t₁ = t₂ ∧ t₂ = t₃ ∧ (t₁ = 0 ∨ t₁ = -h) := by
  -- if tᵢ ≠ tⱼ then the third ratio is −h/2, which contradicts its own pair relation
  have key : ∀ a b c : R, h * (a + b) + 2 * a * b = 0 → h * (a + c) + 2 * a * c = 0 →
      h * (b + c) + 2 * b * c = 0 → b = c := by
    intro a b c rab rac rbc
    by_contra hbc
    have e1 : (b - c) * (h + 2 * a) = 0 := by linear_combination rab - rac
    have ha : h + 2 * a = 0 := by
      rcases mul_eq_zero.mp e1 with e | e
      · exact absurd (sub_eq_zero.mp e) hbc
      · exact e
    -- from rab with 2a = −h: h·a + h·b − h·b = h·a = 0 … then a = 0, so h = 0
    have hab : h * a = 0 := by linear_combination rab - b * ha
    have h_a : a = 0 := by
      rcases mul_eq_zero.mp hab with e | e
      · exact absurd e hh
      · exact e
    exact hh (by linear_combination ha - 2 * h_a)
  have e23 : t₂ = t₃ := key t₁ t₂ t₃ r₁₂ r₁₃ r₂₃
  have e13 : t₁ = t₃ := key t₂ t₁ t₃ (by linear_combination r₁₂) r₂₃ r₁₃
  refine ⟨e13.trans e23.symm, e23, ?_⟩
  have : 2 * (t₁ * (h + t₁)) = 0 := by
    have := r₁₂; rw [← e13.trans e23.symm] at this; linear_combination this
  rcases mul_eq_zero.mp this with e | e
  · exact absurd e h2
  · rcases mul_eq_zero.mp e with e' | e'
    · exact Or.inl e'
    · exact Or.inr (by linear_combination e')

/-- **Exact local covariance.** Pairs `{0,1}, {0,2}, {1,2}` carry `(x₀₁,y₀₁)` etc. with all
`x ≠ 0`. If the braid relation holds for the six labellings, then `y = t·x` for a single `t`
with `t = 0` (scalar rescaling) or `t = −(q − q⁻¹)` (mirror, `x σ⁻¹`). Only the `(0,1)` entry of
two labellings per pair is used. -/
theorem exact_local_covariant (q x₀₁ y₀₁ x₀₂ y₀₂ x₁₂ y₁₂ : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (h2 : (2 : R) ≠ 0) (h01 : x₀₁ ≠ 0) (h02 : x₀₂ ≠ 0) (h12 : x₁₂ ≠ 0)
    -- labellings (0,1,2),(1,0,2): letters ({0,1},{0,2},{1,2}) and ({0,1},{1,2},{0,2})
    (c₁ : defect3 q x₀₁ y₀₁ x₀₂ y₀₂ x₁₂ y₁₂ = 0) (c₂ : defect3 q x₀₁ y₀₁ x₁₂ y₁₂ x₀₂ y₀₂ = 0)
    -- labellings (0,2,1),(2,0,1): letters ({0,2},{0,1},{1,2}) and ({0,2},{1,2},{0,1})
    (c₃ : defect3 q x₀₂ y₀₂ x₀₁ y₀₁ x₁₂ y₁₂ = 0) (c₄ : defect3 q x₀₂ y₀₂ x₁₂ y₁₂ x₀₁ y₀₁ = 0)
    -- labellings (1,2,0),(2,1,0): letters ({1,2},{0,1},{0,2}) and ({1,2},{0,2},{0,1})
    (c₅ : defect3 q x₁₂ y₁₂ x₀₁ y₀₁ x₀₂ y₀₂ = 0) (c₆ : defect3 q x₁₂ y₁₂ x₀₂ y₀₂ x₀₁ y₀₁ = 0) :
    ∃ t : R, (t = 0 ∨ t = -(q - q⁻¹)) ∧
      y₀₁ = t * x₀₁ ∧ y₀₂ = t * x₀₂ ∧ y₁₂ = t * x₁₂ := by
  set h := q - q⁻¹ with hhdef
  have hh : h ≠ 0 := by
    intro e
    apply hq2
    have : q * h = 0 := by rw [e, mul_zero]
    rw [hhdef, mul_sub, mul_inv_cancel₀ hq] at this
    linear_combination this
  have d₁ := congrFun (congrFun c₁ 0) 1; have d₂ := congrFun (congrFun c₂ 0) 1
  have d₃ := congrFun (congrFun c₃ 0) 1; have d₄ := congrFun (congrFun c₄ 0) 1
  have d₅ := congrFun (congrFun c₅ 0) 1; have d₆ := congrFun (congrFun c₆ 0) 1
  rw [defect3_01] at d₁ d₂ d₃ d₄ d₅ d₆
  simp only [Matrix.zero_apply] at d₁ d₂ d₃ d₄ d₅ d₆
  set t₀₁ := y₀₁ / x₀₁; set t₀₂ := y₀₂ / x₀₂; set t₁₂ := y₁₂ / x₁₂
  have hy01 : y₀₁ = t₀₁ * x₀₁ := by simp [t₀₁, div_mul_cancel₀ _ h01]
  have hy02 : y₀₂ = t₀₂ * x₀₂ := by simp [t₀₂, div_mul_cancel₀ _ h02]
  have hy12 : y₁₂ = t₁₂ * x₁₂ := by simp [t₁₂, div_mul_cancel₀ _ h12]
  -- the sum of the two (0,1) entries per pair is −x·(h(sum) + 2·prod)·(x x)
  have r₂₃ : h * (t₀₂ + t₁₂) + 2 * t₀₂ * t₁₂ = 0 := by
    have : x₀₁ * (x₀₂ * x₁₂) * (h * (t₀₂ + t₁₂) + 2 * t₀₂ * t₁₂) = 0 := by
      rw [hy02, hy12] at d₁ d₂; linear_combination -d₁ - d₂
    rcases mul_eq_zero.mp this with e | e
    · exact absurd e (mul_ne_zero h01 (mul_ne_zero h02 h12))
    · exact e
  have r₁₃ : h * (t₀₁ + t₁₂) + 2 * t₀₁ * t₁₂ = 0 := by
    have : x₀₂ * (x₀₁ * x₁₂) * (h * (t₀₁ + t₁₂) + 2 * t₀₁ * t₁₂) = 0 := by
      rw [hy01, hy12] at d₃ d₄; linear_combination -d₃ - d₄
    rcases mul_eq_zero.mp this with e | e
    · exact absurd e (mul_ne_zero h02 (mul_ne_zero h01 h12))
    · exact e
  have r₁₂ : h * (t₀₁ + t₀₂) + 2 * t₀₁ * t₀₂ = 0 := by
    have : x₁₂ * (x₀₁ * x₀₂) * (h * (t₀₁ + t₀₂) + 2 * t₀₁ * t₀₂) = 0 := by
      rw [hy01, hy02] at d₅ d₆; linear_combination -d₅ - d₆
    rcases mul_eq_zero.mp this with e | e
    · exact absurd e (mul_ne_zero h12 (mul_ne_zero h01 h02))
    · exact e
  obtain ⟨a, b, c⟩ := ratios_core h t₀₁ t₀₂ t₁₂ hh h2 r₁₂ r₁₃ r₂₃
  exact ⟨t₀₁, c, hy01, by rw [a]; exact hy02, by rw [a, b]; exact hy12⟩

/-! ## §M. The exact rescaling is a product over linking numbers; it is `1` on `V³` -/

/-- The label pair exchanged by letter `i` at labelling `pos`. -/
def pairAt (pos : List ℕ) (i : ℕ) : ℕ × ℕ := (pos.getD i 0, pos.getD (i + 1) 0)

/-- A braid letter on the proton weight space. -/
def gen (q : R) : Letter → Matrix (Fin 3) (Fin 3) R
  | (i, e) => if i = 0 then (if e = 1 then A₁ q else A₁Inv q)
              else (if e = 1 then A₂ q else A₂Inv q)

/-- The undeformed word. -/
def wordL (q : R) : List Letter → Matrix (Fin 3) (Fin 3) R
  | [] => 1
  | l :: w => gen q l * wordL q w

/-- The accumulated rescaling factor `Π u_{ab}^{e}`. -/
def facU (u : ℕ → ℕ → R) : List Letter → List ℕ → R
  | [], _ => 1
  | (i, e) :: w, pos => u (pairAt pos i).1 (pairAt pos i).2 ^ e * facU u w (swapAt pos i)

/-- The word with every letter rescaled exactly: `σ^e ↦ u_{ab}^e σ^e`. -/
def defWordU (q : R) (u : ℕ → ℕ → R) : List Letter → List ℕ → Matrix (Fin 3) (Fin 3) R
  | [], _ => 1
  | (i, e) :: w, pos =>
      (u (pairAt pos i).1 (pairAt pos i).2 ^ e) • gen q (i, e) * defWordU q u w (swapAt pos i)

theorem defWordU_eq_smul (q : R) (u : ℕ → ℕ → R) (w : List Letter) (pos : List ℕ) :
    defWordU q u w pos = facU u w pos • wordL q w := by
  induction w generalizing pos with
  | nil => simp [defWordU, facU, wordL]
  | cons l w ih =>
    obtain ⟨i, e⟩ := l
    simp only [defWordU, facU, wordL, ih, Matrix.smul_mul, Matrix.mul_smul, smul_smul, mul_comm]

/-- **On `V³` the exact rescaling factor is `1`** for every symmetric, nonvanishing `u`. -/
theorem facU_borromean (u : ℕ → ℕ → R) (hu : ∀ a b, u a b = u b a)
    (h01 : u 0 1 ≠ 0) (h02 : u 0 2 ≠ 0) (h12 : u 1 2 ≠ 0) :
    facU u borWord [0, 1, 2] = 1 := by
  simp [facU, borWord, pairAt, swapAt, hu 1 0, hu 2 0, hu 2 1]
  field_simp

/-- **All orders:** the trace of the rescaled `V³` equals the trace of `V³`. -/
theorem trace_defWordU_borromean (q : R) (u : ℕ → ℕ → R) (hu : ∀ a b, u a b = u b a)
    (h01 : u 0 1 ≠ 0) (h02 : u 0 2 ≠ 0) (h12 : u 1 2 ≠ 0) :
    trace (defWordU q u borWord [0, 1, 2]) = trace (wordL q borWord) := by
  rw [defWordU_eq_smul, facU_borromean u hu h01 h02 h12, one_smul]

/-- Control: on the Hopf word the factor is `u₀₁²`, not `1`. -/
theorem facU_hopf (u : ℕ → ℕ → R) (hu : ∀ a b, u a b = u b a) :
    facU u hopfWord [0, 1, 2] = u 0 1 ^ 2 := by
  simp [facU, hopfWord, pairAt, swapAt, hu 1 0]; ring

/-! ## §D. The naive photon-exchange double sum -/

/-- Coloured writhe `S = Σ_c w_c`, `w_c = e_c α_{ab}`. -/
def S (α : ℕ → ℕ → R) : List Letter → List ℕ → R
  | [], _ => 0
  | (i, e) :: w, pos => (e : R) * α (pairAt pos i).1 (pairAt pos i).2 + S α w (swapAt pos i)

/-- Sum of squares `Σ_c w_c²`. -/
def Sq (α : ℕ → ℕ → R) : List Letter → List ℕ → R
  | [], _ => 0
  | (i, e) :: w, pos =>
      ((e : R) * α (pairAt pos i).1 (pairAt pos i).2) ^ 2 + Sq α w (swapAt pos i)

/-- Ordered double crossing sum `D = Σ_{c<c'} w_c w_{c'}`. -/
def D (α : ℕ → ℕ → R) : List Letter → List ℕ → R
  | [], _ => 0
  | (i, e) :: w, pos =>
      (e : R) * α (pairAt pos i).1 (pairAt pos i).2 * S α w (swapAt pos i)
        + D α w (swapAt pos i)

theorem two_D_add_sq (α : ℕ → ℕ → R) (w : List Letter) (pos : List ℕ) :
    2 * D α w pos + Sq α w pos = S α w pos ^ 2 := by
  induction w generalizing pos with
  | nil => simp [D, Sq, S]
  | cons l w ih =>
    obtain ⟨i, e⟩ := l
    simp only [D, Sq, S]
    linear_combination ih (swapAt pos i)

/-- The coloured writhe vanishes on `V³` (all pairwise linking numbers are `0`). -/
theorem S_borromean (α : ℕ → ℕ → R) (hα : ∀ a b, α a b = α b a) :
    S α borWord [0, 1, 2] = 0 := by
  simp [S, borWord, pairAt, swapAt, hα 1 0, hα 2 0, hα 2 1]; ring

/-- **The covariant completion `D + ½ Σ w²` is `S²/2`, which vanishes on `V³`.** -/
theorem doubleSum_completion_borromean (α : ℕ → ℕ → R) (hα : ∀ a b, α a b = α b a) :
    2 * D α borWord [0, 1, 2] + Sq α borWord [0, 1, 2] = 0 := by
  rw [two_D_add_sq, S_borromean α hα]; ring

/-- **The naive double sum is not covariant:** prefixing `σ₁σ₁⁻¹` (which is the identity in the
braid group) to `V³` shifts it by `−α₀₁²`. -/
theorem doubleSum_r2_borromean (α : ℕ → ℕ → R) (hα : ∀ a b, α a b = α b a) :
    D α ((0, 1) :: (0, -1) :: borWord) [0, 1, 2] = D α borWord [0, 1, 2] - α 0 1 ^ 2 := by
  have hS := S_borromean α hα
  simp only [D, S] at hS ⊢
  simp [pairAt, swapAt, hα 1 0] at hS ⊢
  linear_combination hS * (α 0 1 - α 0 1)

/-! ## §C. Charge weights for the Milnor channel -/

/-- A general polynomial of degree `≤ 2` in three charges. -/
def quad (c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ x y z : R) : R :=
  c₀ + c₁ * x + c₂ * y + c₃ * z + c₁₁ * x ^ 2 + c₂₂ * y ^ 2 + c₃₃ * z ^ 2
    + c₁₂ * x * y + c₁₃ * x * z + c₂₃ * y * z

/-- **A charge weight of degree `≤ 2` alternating under the transpositions `(12)` and `(23)` is
identically zero** (needs `2 ≠ 0`). So no charge-quadratic (order-`α_em`) coefficient can
covariantly couple to the alternating invariant `μ̄₁₂₃`. -/
theorem quad_alternating_eq_zero (c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ : R) (h2 : (2 : R) ≠ 0)
    (s₁₂ : ∀ x y z, quad c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ x y z
      = -quad c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ y x z)
    (s₂₃ : ∀ x y z, quad c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ x y z
      = -quad c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ x z y)
    (x y z : R) : quad c₀ c₁ c₂ c₃ c₁₁ c₂₂ c₃₃ c₁₂ c₁₃ c₂₃ x y z = 0 := by
  have z2 : ∀ r : R, 2 * r = 0 → r = 0 := fun r hr => by
    rcases mul_eq_zero.mp hr with e | e
    · exact absurd e h2
    · exact e
  simp only [quad] at s₁₂ s₂₃ ⊢
  -- (12)-symmetrised: 2c₀, 2c₃ + 2c₃₃, c₁+c₂, c₁₁+c₂₂, c₁₂, c₁₃+c₂₃
  have z4 : ∀ r : R, 2 * (2 * r) = 0 → r = 0 := fun r hr => z2 r (z2 _ hr)
  have a0 := z2 c₀ (by linear_combination s₁₂ 0 0 0)
  have a3 := z4 c₃ (by linear_combination s₁₂ 0 0 1 - s₁₂ 0 0 (-1))
  have a33 := z4 c₃₃ (by linear_combination s₁₂ 0 0 1 + s₁₂ 0 0 (-1) - 4 * a0)
  have a1 := z4 c₁ (by linear_combination s₂₃ 1 0 0 - s₂₃ (-1) 0 0)
  have a11 := z4 c₁₁ (by linear_combination s₂₃ 1 0 0 + s₂₃ (-1) 0 0 - 4 * a0)
  have a2 := z2 c₂ (by linear_combination s₁₂ 1 0 0 - s₁₂ (-1) 0 0 - 2 * a1)
  have a22 := z2 c₂₂ (by linear_combination s₁₂ 1 0 0 + s₁₂ (-1) 0 0 - 4 * a0 - 2 * a11)
  have a12 := z2 c₁₂ (by
    linear_combination s₁₂ 1 1 0 - 2 * a0 - 2 * a1 - 2 * a2 - 2 * a11 - 2 * a22)
  have a23 := z2 c₂₃ (by
    linear_combination s₂₃ 0 1 1 - 2 * a0 - 2 * a2 - 2 * a3 - 2 * a22 - 2 * a33)
  have a13 : c₁₃ = 0 := by
    linear_combination s₁₂ 1 0 1 - 2 * a0 - a1 - a2 - 2 * a3 - a11 - a22 - 2 * a33 - a23
  rw [a0, a1, a2, a3, a11, a22, a33, a12, a13, a23]; ring

/-- An alternating weight of any form vanishes when two charges coincide — both nucleons
(`(u,u,d)`, `(u,d,d)`) have a repeated charge. -/
theorem alternating_vanishes_on_pair (f : R → R → R → R) (h2 : (2 : R) ≠ 0)
    (halt : ∀ x y z, f x y z = -f y x z) (x z : R) : f x x z = 0 := by
  have : 2 * f x x z = 0 := by linear_combination halt x x z
  rcases mul_eq_zero.mp this with e | e
  · exact absurd e h2
  · exact e

/-! ## §S. The degree-0 (braid-independent) terms -/

/-- Charge-symmetric quadratic `k₁ ΣQ² + k₂ Σ_{a<b} Q_aQ_b` on the proton `(2/3, 2/3, −1/3)` and
the neutron `(2/3, −1/3, −1/3)`. -/
theorem degreeZero_values (k₁ k₂ : R) (h3 : (3 : R) ≠ 0) :
    (k₁ * ((2/3)^2 + (2/3)^2 + (-1/3)^2) + k₂ * ((2/3)*(2/3) + (2/3)*(-1/3) + (2/3)*(-1/3)) = k₁)
    ∧ (k₁ * ((2/3)^2 + (-1/3)^2 + (-1/3)^2) + k₂ * ((2/3)*(-1/3) + (2/3)*(-1/3) + (-1/3)*(-1/3))
        = (2/3) * k₁ - (1/3) * k₂) := by
  constructor <;> field_simp <;> ring

/-- A scalar insertion `(1 + a)` on the `F_Bor` term of the substrate identity
`m_p = 2 m_μ T [3]!/q³ − 12 m_e` shifts the proton by exactly `a · 2 m_μ T [3]!/q³`: the whole
QCD-term multiplier, not a separate electromagnetic scale. -/
theorem scalar_insertion_shift (a M T fac qcube me : R) :
    (2 * M * (T * (1 + a)) * fac / qcube - 12 * me) - (2 * M * T * fac / qcube - 12 * me)
      = a * (2 * M * T * fac / qcube) := by ring

end QOU.BraidsAndKnots.QEDHigherOrderCovariance
