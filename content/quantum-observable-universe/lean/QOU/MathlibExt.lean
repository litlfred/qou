import Mathlib.Data.List.Basic
import Mathlib.Data.List.Perm
import Mathlib.Data.List.Sort
import Mathlib.Algebra.BigOperators.Group.List
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# QOU.MathlibExt — Mathlib-extension lemmas for the QOU formalisation

Standard / mechanical lemmas not yet in Mathlib but needed by the
QOU formalisation. Each is a candidate for upstream contribution;
until they land, callers in `QOU.*` use the local versions.

## Sections

- §1 List sort identities (sum / product preserved by `insertionSort`)
- §2 Foldl-as-product for commutative monoids
- §3 Permutation-invariance of foldl/foldr over commutative ops
- §4 `Real.rpow` numerical helpers (sqrt bridge for half-powers)

Each lemma has a `-- TODO upstream:` comment.
-/

namespace QOU.MathlibExt

/-! ## §1  List sort identities -/

/-- Sorting (by any relation) preserves the list's sum.

    Proof: `insertionSort` is a permutation; `List.Perm.sum_eq`
    transfers sum across permutations.

    TODO upstream: `Mathlib.Data.List.Sort` or
    `Mathlib.Algebra.BigOperators.Group.List`. -/
theorem List.sum_insertionSort_eq {α : Type*} [AddCommMonoid α]
    (xs : List α) (r : α → α → Bool) :
    (xs.insertionSort r).sum = xs.sum :=
  (xs.perm_insertionSort r).symm.sum_eq

/-- Sorting (by any relation) preserves the list's product
    (for commutative monoids).

    TODO upstream: `Mathlib.Data.List.Sort`. -/
theorem List.prod_insertionSort_eq {α : Type*} [CommMonoid α]
    (xs : List α) (r : α → α → Bool) :
    (xs.insertionSort r).prod = xs.prod :=
  (xs.perm_insertionSort r).symm.prod_eq

/-! ## §2  Foldl as initial · product (commutative monoids) -/

/-- For a commutative monoid, `List.foldl (· * ·) init xs` equals
    `init * xs.prod`.

    Proof: induction on `xs`, using `mul_assoc` to associate the
    accumulator forwards, and `mul_comm` to commute past `hd`.

    TODO upstream: `Mathlib.Algebra.BigOperators.Group.List` —
    Mathlib has `List.foldl_assoc` for `init = 1`; this is the
    `init ≠ 1` generalisation. -/
theorem List.foldl_mul_eq_prod_mul {α : Type*} [CommMonoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = init * xs.prod := by
  induction xs generalizing init with
  | nil => simp
  | cons hd tl ih =>
    rw [List.foldl_cons, ih, List.prod_cons, mul_comm init hd, mul_assoc]

/-- Companion for `foldr`: `List.foldr (· * ·) init xs = xs.prod * init`. -/
theorem List.foldr_mul_eq_prod_mul {α : Type*} [CommMonoid α]
    (xs : List α) (init : α) :
    xs.foldr (· * ·) init = xs.prod * init := by
  induction xs with
  | nil => simp
  | cons hd tl ih =>
    rw [List.foldr_cons, ih, List.prod_cons, mul_assoc]

/-! ## §3  Foldl/foldr commutativity for commutative monoids -/

/-- For a commutative monoid, foldl and foldr agree (regardless of
    fold direction): both produce `init * xs.prod`.

    This discharges `MatrixChainEqBuildChains` once the matrices
    are known to commute (the matrices then form a commutative
    submonoid of `Matrix _ _ R_q`).

    TODO upstream: `Mathlib.Data.List.Basic` /
    `Mathlib.Algebra.BigOperators.Group.List`. -/
theorem List.foldl_eq_foldr_comm {α : Type*} [CommMonoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = xs.foldr (· * ·) init := by
  rw [List.foldl_mul_eq_prod_mul, List.foldr_mul_eq_prod_mul, mul_comm]

/-- Permutation-invariance of products in a commutative monoid
    (specialisation of `List.Perm.prod_eq` for use as a lookup
    target by automation). -/
theorem List.prod_eq_of_perm {α : Type*} [CommMonoid α]
    {xs ys : List α} (h : xs.Perm ys) :
    xs.prod = ys.prod :=
  h.prod_eq

/-- For a `CommMonoid`, the underlying Mathlib lemma
    `List.Perm.prod_eq` already gives us order-invariance of
    products — folding from any direction over any permutation of
    the list produces the same answer. The two corollaries below
    package this for use at common call sites. -/

/-- `xs.reverse.prod = xs.prod` in a `CommMonoid`. -/
theorem List.prod_reverse_eq {α : Type*} [CommMonoid α] (xs : List α) :
    xs.reverse.prod = xs.prod :=
  (xs.reverse_perm).prod_eq

/-! ## §4  `Real.rpow` numerical helpers

The `Real.rpow` function is central to several QOU bounds (skein
mass relation, pair-skein decomposition, q-Planck constant), but
`norm_num` does not yet evaluate it on non-integer exponents. The
lemmas below convert the most common QOU pattern
`q^(1/2 : ℝ) + q^(-(1/2) : ℝ)` to `Real.sqrt q + 1 / Real.sqrt q`,
where Mathlib's existing `Real.sqrt`-based numerics apply. -/

/-- `x^(1/2 : ℝ) = Real.sqrt x` (for any real `x`; both sides
    are zero on the negative reals via the rpow / sqrt
    conventions).  Symmetric form of Mathlib's
    `Real.sqrt_eq_rpow`.

    TODO upstream: this is `Real.rpow_one_div_two` in some Mathlib
    versions. -/
theorem Real.rpow_half_eq_sqrt (x : ℝ) :
    x ^ (1/2 : ℝ) = Real.sqrt x :=
  (Real.sqrt_eq_rpow x).symm

/-- For `x > 0`, `x^(-(1/2) : ℝ) = 1 / Real.sqrt x`. -/
theorem Real.rpow_neg_half_eq (x : ℝ) (hx : 0 < x) :
    x ^ (-(1/2 : ℝ)) = 1 / Real.sqrt x := by
  rw [Real.rpow_neg hx.le, Real.rpow_half_eq_sqrt x, one_div]

/-- The QOU "denominator" `q^(1/2) + q^(-1/2)` equals
    `sqrt q + 1 / sqrt q`. -/
theorem Real.q_half_denom (q : ℝ) (hq : 0 < q) :
    q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)) = Real.sqrt q + 1 / Real.sqrt q := by
  rw [Real.rpow_half_eq_sqrt q, Real.rpow_neg_half_eq q hq]

/-- For `x > 0`, the function `t ↦ t + 1/t` evaluated at
    `t = Real.sqrt x` is non-negative and admits a clean
    cross-multiplication identity:
    `(Real.sqrt x) · ((Real.sqrt x) + 1 / (Real.sqrt x))
       = x + 1`,
    i.e. multiplying the QOU half-denominator by `sqrt x` clears
    the inverse, yielding a closed-form polynomial in `x`. -/
theorem Real.sqrt_mul_half_denom (x : ℝ) (hx : 0 < x) :
    Real.sqrt x * (Real.sqrt x + 1 / Real.sqrt x) = x + 1 := by
  have hsqrt_pos : 0 < Real.sqrt x := Real.sqrt_pos.mpr hx
  have hsqrt_ne : Real.sqrt x ≠ 0 := ne_of_gt hsqrt_pos
  have hsq : Real.sqrt x * Real.sqrt x = x :=
    Real.mul_self_sqrt hx.le
  field_simp
  linarith [hsq]

/-- **Bracketing helper**: if `a > 0` and `a^2 < x`, then
    `a < Real.sqrt x`. Lifted from `Real.sqrt_lt_sqrt` with the
    `Real.sqrt_sq` simplification baked in. -/
theorem Real.lt_sqrt_of_sq_lt (a x : ℝ) (ha : 0 ≤ a) (hsq : a^2 < x) :
    a < Real.sqrt x := by
  have hax : a = Real.sqrt (a^2) := by
    rw [Real.sqrt_sq ha]
  rw [hax]
  exact Real.sqrt_lt_sqrt (by positivity) hsq

/-- **Bracketing helper**: if `0 ≤ x` and `x < a^2`, then
    `Real.sqrt x < a` (assuming `0 ≤ a`). -/
theorem Real.sqrt_lt_of_lt_sq (a x : ℝ) (ha : 0 ≤ a) (hx : 0 ≤ x)
    (hsq : x < a^2) :
    Real.sqrt x < a := by
  have hax : a = Real.sqrt (a^2) := by
    rw [Real.sqrt_sq ha]
  rw [hax]
  exact Real.sqrt_lt_sqrt hx hsq

end QOU.MathlibExt
