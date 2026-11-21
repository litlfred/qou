/-
# The minimal U(1)-neutral gluon vertex in `H₃(q)` is `V³`

Question (bean `qou-99qc`, Q1): the shipped gluon term is the `H₂` vertex
`σ₀²`, while the γγ construction produces powers of the chiral vertex
`V = σ₀σ₁⁻¹ ∈ H₃(q)`. Which is the gluon segment? This file derives what the
algebra forces, without choosing.

## The setting

`H₃(q)` has three Wedderburn blocks, `(3)`, `(2,1)` and `(1³)`. Reading 3 of the
confinement criterion (owner, 2026-09-12; scope "whole word", 2026-09-13) asks
that the block character of the vertex be non-negative on every block with
`y_λ > 0`.

* On the one-dimensional blocks `V` acts by `q · q⁻¹ = 1` and by
  `(-q⁻¹) · (-q) = 1`. So every power `Vᵏ` is `1` there and never binds.
* On the two-dimensional block `(2,1)` we use the matrices
  `σ₀ = [[q, 1], [0, -q⁻¹]]`, `σ₁ = [[-q⁻¹, 0], [1, q]]`, which satisfy the
  braid relation and the Hecke relation (proved below). Then
  `V = [[1 - q², q⁻¹], [-q⁻¹, -q⁻²]]`, with `det V = 1` and
  `tr V = t := -(q² - 1 + q⁻²)`.

Because `det V = 1`, the traces `s_k = tr(Vᵏ)` obey the Chebyshev recursion
`s_{k+2} = t·s_{k+1} - s_k`. So `s₁ = t`, `s₂ = t² - 2`, `s₃ = t(t² - 3)`.

## What is proved

* `t ≤ -1` for every nonzero real `q`, since `q² + q⁻² ≥ 2`.
* `s₁ < 0` always: `V` itself is never admissible.
* Under `t² < 2`, both `s₂ < 0` and `s₃ > 0`. So `V³` is the **least**
  positive power of `V` whose `(2,1)` character is non-negative.
* `σ₀ᵏ` has writhe `k`, and a U(1)-neutral word has writhe `0`
  (`PhotonU1NeutralCut.writhe_eq_zero_of_neutral`). So the only U(1)-neutral
  `H₂` vertex `σ₀ᵏ` is the empty one, `k = 0`.

## What it does not settle

* The hypothesis `t² < 2` is a condition on `q`, equivalent to
  `q² + q⁻² < 1 + √2`. It holds at `q = 1` (`t = -1`) and fails for large `q`.
  Whether it holds at the substrate pin is a numerical evaluation, kept out of
  this file. The probe
  `computations/probes/gluon_pure_power/gluon_pure_power_probe.py` does it.
* Reading 3 is the owner's choice of criterion among three. Readings 1 and 2
  are parked, and this file says nothing about them.
* U(1) neutrality is imposed here on the vertex itself. Whether it should be
  imposed on each factor or only on the whole product word is the scope
  question recorded in `PhotonU1NeutralCut`. Under a whole-word reading the
  `H₂` result above does not apply to a factor.

## Base ring

The algebra (relations, trace, determinant, recursion) is over a generic
`Field`. The sign statements need an order and use
`[Field R] [LinearOrder R] [IsStrictOrderedRing R]` (AGENTS.md §7c). No
numerical value of `q` appears.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.PhotonU1NeutralCut

namespace QOU.QBeta.GluonVertexPurePower

variable {R : Type*}

/-- A 2 × 2 matrix, written out entry by entry. Kept elementary so that every
identity below is a `ring` / `field_simp` computation. -/
structure M2 (R : Type*) where
  a : R
  b : R
  c : R
  d : R

section Algebra
variable [Field R]

namespace M2

omit [Field R] in
@[ext] theorem ext' {X Y : M2 R} (h1 : X.a = Y.a) (h2 : X.b = Y.b)
    (h3 : X.c = Y.c) (h4 : X.d = Y.d) : X = Y := by
  cases X; cases Y; simp_all

def mul (X Y : M2 R) : M2 R :=
  ⟨X.a * Y.a + X.b * Y.c, X.a * Y.b + X.b * Y.d,
   X.c * Y.a + X.d * Y.c, X.c * Y.b + X.d * Y.d⟩

def one : M2 R := ⟨1, 0, 0, 1⟩

def smulAdd (x : R) (X : M2 R) (y : R) : M2 R :=
  ⟨x * X.a + y, x * X.b, x * X.c, x * X.d + y⟩

def tr (X : M2 R) : R := X.a + X.d

def det (X : M2 R) : R := X.a * X.d - X.b * X.c

def pow (X : M2 R) : ℕ → M2 R
  | 0 => one
  | k + 1 => mul (pow X k) X

/-- Cayley–Hamilton for 2 × 2: `X² = tr X · X - det X · 1`. -/
theorem sq_eq (X : M2 R) : mul X X = smulAdd (tr X) X (-det X) := by
  ext <;> simp only [mul, smulAdd, tr, det] <;> ring

theorem pow_succ_succ (X : M2 R) (k : ℕ) :
    pow X (k + 2) = mul (pow X k) (mul X X) := by
  -- associativity, entry by entry
  show mul (mul (pow X k) X) X = mul (pow X k) (mul X X)
  ext <;> simp only [mul] <;> ring

/-- The trace recursion. With `det X = 1` it is the Chebyshev recursion. -/
theorem tr_pow_succ_succ (X : M2 R) (k : ℕ) :
    tr (pow X (k + 2)) = tr X * tr (pow X (k + 1)) - det X * tr (pow X k) := by
  rw [pow_succ_succ, sq_eq]
  show _ = tr X * tr (mul (pow X k) X) - det X * tr (pow X k)
  simp only [mul, smulAdd, tr]
  ring

end M2

open M2

/-- `σ₀` on the `(2,1)` block. -/
def sigma0 (q : R) : M2 R := ⟨q, 1, 0, -q⁻¹⟩

/-- `σ₁` on the `(2,1)` block. -/
def sigma1 (q : R) : M2 R := ⟨-q⁻¹, 0, 1, q⟩

/-- `σ₁⁻¹ = σ₁ - (q - q⁻¹)`, from the Hecke relation. -/
def sigma1Inv (q : R) : M2 R := ⟨-q, 0, 1, q⁻¹⟩

theorem braid_relation {q : R} (hq : q ≠ 0) :
    mul (mul (sigma0 q) (sigma1 q)) (sigma0 q) =
      mul (mul (sigma1 q) (sigma0 q)) (sigma1 q) := by
  ext <;> simp only [mul, sigma0, sigma1] <;> field_simp <;> ring

theorem hecke_sigma0 {q : R} (hq : q ≠ 0) :
    mul (sigma0 q) (sigma0 q) = smulAdd (q - q⁻¹) (sigma0 q) 1 := by
  ext <;> simp only [mul, smulAdd, sigma0] <;> field_simp <;> ring

theorem hecke_sigma1 {q : R} (hq : q ≠ 0) :
    mul (sigma1 q) (sigma1 q) = smulAdd (q - q⁻¹) (sigma1 q) 1 := by
  ext <;> simp only [mul, smulAdd, sigma1] <;> field_simp <;> ring

theorem sigma1_mul_inv {q : R} (hq : q ≠ 0) :
    mul (sigma1 q) (sigma1Inv q) = one := by
  ext <;> simp only [mul, sigma1, sigma1Inv, one] <;> field_simp <;> ring

/-- The chiral vertex `V = σ₀σ₁⁻¹` on the `(2,1)` block. -/
def V (q : R) : M2 R := mul (sigma0 q) (sigma1Inv q)

/-- `t = -(q² - 1 + q⁻²)`, the `(2,1)` character of `V`. -/
def t (q : R) : R := -(q ^ 2 - 1 + q⁻¹ ^ 2)

theorem det_V {q : R} (hq : q ≠ 0) : det (V q) = 1 := by
  simp only [V, mul, det, sigma0, sigma1Inv]; field_simp; ring

theorem tr_V (q : R) : tr (V q) = t q := by
  simp only [V, mul, tr, sigma0, sigma1Inv, t]; ring

/-- The `(2,1)` characters `s k = χ_(2,1)(Vᵏ)`. -/
def s (q : R) (k : ℕ) : R := tr (pow (V q) k)

theorem s_zero (q : R) : s q 0 = 2 := by
  simp only [s, pow, tr, one]; norm_num

theorem s_one (q : R) : s q 1 = t q := by
  rw [← tr_V]; simp only [s, pow]
  show tr (mul one (V q)) = tr (V q)
  simp only [mul, one, tr]; ring

theorem s_succ_succ {q : R} (hq : q ≠ 0) (k : ℕ) :
    s q (k + 2) = t q * s q (k + 1) - s q k := by
  simp only [s]; rw [tr_pow_succ_succ, tr_V, det_V hq, one_mul]

theorem s_two {q : R} (hq : q ≠ 0) : s q 2 = t q ^ 2 - 2 := by
  rw [s_succ_succ hq 0, s_one, s_zero]; ring

theorem s_three {q : R} (hq : q ≠ 0) : s q 3 = t q * (t q ^ 2 - 3) := by
  rw [s_succ_succ hq 1, s_two hq, s_one]; ring

/-- On the one-dimensional blocks `V` acts by `1`: on `(3)` the generators act by
`q` and `σ₁⁻¹` by `q⁻¹`; on `(1³)` by `-q⁻¹` and `-q`. -/
theorem V_trivial_blocks {q : R} (hq : q ≠ 0) :
    q * q⁻¹ = 1 ∧ (-q⁻¹) * (-q) = 1 := by
  constructor <;> field_simp

end Algebra

section Ordered
variable [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- `t ≤ -1` for every nonzero `q`, because `q² + q⁻² ≥ 2`. -/
theorem t_le_neg_one {q : R} (hq : q ≠ 0) : t q ≤ -1 := by
  have h : 0 ≤ (q - q⁻¹) ^ 2 := sq_nonneg _
  have hm : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  unfold t
  nlinarith [h, hm]

/-- `V` itself is never admissible: its `(2,1)` character is negative. -/
theorem s_one_neg {q : R} (hq : q ≠ 0) : s q 1 < 0 := by
  rw [s_one]; linarith [t_le_neg_one hq]

/-- In the regime `t² < 2`, `V²` is not admissible. -/
theorem s_two_neg {q : R} (hq : q ≠ 0) (ht : t q ^ 2 < 2) : s q 2 < 0 := by
  rw [s_two hq]; linarith

/-- In the regime `t² < 2`, `V³` is admissible, strictly. -/
theorem s_three_pos {q : R} (hq : q ≠ 0) (ht : t q ^ 2 < 2) : 0 < s q 3 := by
  rw [s_three hq]
  have h1 : t q < 0 := by linarith [t_le_neg_one hq]
  have h2 : t q ^ 2 - 3 < 0 := by linarith
  exact mul_pos_of_neg_of_neg h1 h2

/-- **The pure-power rule.** For `t² < 2`, `k = 3` is the least positive power
of the chiral vertex whose `(2,1)` character is non-negative. With the
one-dimensional blocks acting by `1`, `V³` is the least positive power that is
admissible under reading 3. -/
theorem least_admissible_power {q : R} (hq : q ≠ 0) (ht : t q ^ 2 < 2) :
    s q 1 < 0 ∧ s q 2 < 0 ∧ 0 < s q 3 :=
  ⟨s_one_neg hq, s_two_neg hq ht, s_three_pos hq ht⟩

/-- The window is exact at both ends: `0 ≤ s₂ ↔ 2 ≤ t²`, and (since `t < 0`)
`0 ≤ s₃ ↔ t² ≤ 3`. So the rule `k = 3` holds precisely while `t² < 2`, and
`V³` stays admissible until `t² = 3`. -/
theorem s_two_nonneg_iff {q : R} (hq : q ≠ 0) : 0 ≤ s q 2 ↔ 2 ≤ t q ^ 2 := by
  rw [s_two hq]; constructor <;> intro h <;> linarith

theorem s_three_nonneg_iff {q : R} (hq : q ≠ 0) : 0 ≤ s q 3 ↔ t q ^ 2 ≤ 3 := by
  rw [s_three hq]
  have h1 : t q < 0 := by linarith [t_le_neg_one hq]
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : t q * (t q ^ 2 - 3) < 0 := mul_neg_of_neg_of_pos h1 (by linarith)
    linarith
  · intro h
    exact mul_nonneg_of_nonpos_of_nonpos h1.le (by linarith)

/-- At `q = 1` (the classical point) the regime holds: `t = -1`. -/
theorem t_at_one : t (1 : R) = -1 := by
  unfold t; norm_num

end Ordered

section H2
open QOU.PhotonU1NeutralCut

/-- `σ₀ᵏ` as a braid word. -/
def sigma0Pow (k : ℕ) : List Letter := List.replicate k (0, 1)

theorem writhe_sigma0Pow (k : ℕ) : writhe (sigma0Pow k) = k := by
  induction k with
  | zero => rfl
  | succ n ih =>
    simp only [sigma0Pow, List.replicate_succ, writhe] at *
    rw [ih]; push_cast; ring

/-- **The `H₂` route under U(1) neutrality.** The only U(1)-neutral vertex
`σ₀ᵏ` is the empty one. Combined with the `H₂` parity rule
(`GluonVertexPsdParity.vertex_psd_iff_even`), the H₂ selection leaves only the
identity once neutrality is imposed on the vertex. -/
theorem sigma0Pow_neutral_iff (k : ℕ) : Neutral (sigma0Pow k) → k = 0 := by
  intro h
  have := writhe_eq_zero_of_neutral _ h
  rw [writhe_sigma0Pow] at this
  exact_mod_cast this

end H2

end QOU.QBeta.GluonVertexPurePower
