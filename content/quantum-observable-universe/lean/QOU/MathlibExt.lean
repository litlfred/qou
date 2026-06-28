import Mathlib.Data.List.Basic
import Mathlib.Data.List.Sort
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
    (r : α → α → Prop) [DecidableRel r] (xs : List α) :
    (xs.insertionSort r).sum = xs.sum :=
  (xs.perm_insertionSort r).sum_eq

/-- Sorting (by any relation) preserves the list's product
    (for commutative monoids).

    TODO upstream: `Mathlib.Data.List.Sort`. -/
theorem List.prod_insertionSort_eq {α : Type*} [CommMonoid α]
    (r : α → α → Prop) [DecidableRel r] (xs : List α) :
    (xs.insertionSort r).prod = xs.prod :=
  (xs.perm_insertionSort r).prod_eq

/-! ## §2  Foldl as initial · product (commutative monoids) -/

/-- For *any* monoid, `List.foldl (· * ·) init xs` equals
    `init * xs.prod`. Holds for arbitrary `Monoid` — no
    commutativity needed; the proof uses associativity only.

    TODO upstream: `Mathlib.Algebra.BigOperators.Group.List` —
    Mathlib has `List.foldl_assoc` for `init = 1`; this is the
    `init ≠ 1` generalisation. -/
theorem List.foldl_mul_eq_mul_prod {α : Type*} [Monoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = init * xs.prod := by
  induction xs generalizing init with
  | nil => simp
  | cons hd tl ih =>
    rw [List.foldl_cons, ih, List.prod_cons, mul_assoc]

/-- Companion for `foldr`: `List.foldr (· * ·) init xs = xs.prod * init`.
    Also `Monoid`-level — no commutativity required. -/
theorem List.foldr_mul_eq_prod_mul {α : Type*} [Monoid α]
    (xs : List α) (init : α) :
    xs.foldr (· * ·) init = xs.prod * init := by
  induction xs with
  | nil => simp
  | cons hd tl ih =>
    rw [List.foldr_cons, ih, List.prod_cons, mul_assoc]

/-- Backward-compatible alias matching the original CommMonoid
    name (the statement and proof generalise to any Monoid). -/
theorem List.foldl_mul_eq_prod_mul {α : Type*} [Monoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = init * xs.prod :=
  List.foldl_mul_eq_mul_prod xs init

/-! ## §3  Foldl/foldr commutativity -/

/-- For a *commutative* monoid, foldl and foldr agree: both
    produce `init * xs.prod = xs.prod * init`. -/
theorem List.foldl_eq_foldr_comm {α : Type*} [CommMonoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = xs.foldr (· * ·) init := by
  rw [List.foldl_mul_eq_mul_prod, List.foldr_mul_eq_prod_mul, mul_comm]

/-! ### §3a  `Pairwise Commute` foldl/foldr theorem

This is the form needed for `MatrixChainEqBuildChains`: matrices
are not a `CommMonoid`, but the *specific* transfer matrices in
the chain pairwise commute (witnessed by `transferMatrix_comm`),
and the chain initialiser commutes with each matrix in the chain.
Under those hypotheses, foldl and foldr agree. -/

/-- `Commute init xs.prod` follows from `init` commuting with
    every element of `xs`. -/
theorem List.commute_init_prod {α : Type*} [Monoid α]
    (init : α) (xs : List α) (h : ∀ x ∈ xs, Commute init x) :
    Commute init xs.prod := by
  induction xs with
  | nil => simp [List.prod_nil, Commute.one_right]
  | cons hd tl ih =>
    rw [List.prod_cons]
    refine Commute.mul_right (h hd List.mem_cons_self) ?_
    exact ih (fun x hx => h x (List.mem_cons_of_mem _ hx))

/-- **Foldl/foldr equality from a Commute hypothesis on the
    initial accumulator**: foldl and foldr produce the same
    result over an arbitrary `Monoid` whenever the initial
    accumulator commutes with every list element.

    Note: pairwise commutativity *among* the list elements is not
    needed for this form — the result is `init * xs.prod` either
    way (foldl) or `xs.prod * init` (foldr), and these are equal
    iff `init` commutes with `xs.prod`, which is exactly the
    `Commute init x for all x` hypothesis (via `commute_init_prod`).

    This discharges `MatrixChainEqBuildChains` (after some
    rearrangement) since `transferMatrix_comm` gives the
    pairwise-commute property. -/
theorem List.foldl_eq_foldr_of_commute_init {α : Type*} [Monoid α]
    (xs : List α) (init : α) (h : ∀ x ∈ xs, Commute init x) :
    xs.foldl (· * ·) init = xs.foldr (· * ·) init := by
  rw [List.foldl_mul_eq_mul_prod, List.foldr_mul_eq_prod_mul]
  exact (List.commute_init_prod init xs h)

/-- Permutation-invariance of products in a commutative monoid
    (specialisation of `List.Perm.prod_eq` for use as a lookup
    target by automation). -/
theorem List.prod_eq_of_perm {α : Type*} [CommMonoid α]
    {xs ys : List α} (h : xs.Perm ys) :
    xs.prod = ys.prod :=
  List.Perm.prod_eq h

/-! For a `CommMonoid`, the underlying Mathlib lemma
    `List.Perm.prod_eq` already gives us order-invariance of
    products — folding from any direction over any permutation of
    the list produces the same answer. The two corollaries below
    package this for use at common call sites. -/

/-- `xs.reverse.prod = xs.prod` in a `CommMonoid`. -/
theorem List.prod_reverse_eq {α : Type*} [CommMonoid α] (xs : List α) :
    xs.reverse.prod = xs.prod :=
  (xs.reverse_perm).prod_eq

/-- A natural-number list's sum equals the indexed Finset sum
    of its `getD ·  0` accessor. Mechanical induction on the list.

    TODO upstream: `Mathlib.Algebra.BigOperators.Group.List` —
    standard sum-is-finset-sum identity. -/
theorem List.sum_eq_finsetSum_getD {α : Type*} [AddCommMonoid α]
    (xs : List α) (z : α) :
    xs.sum = ∑ i ∈ Finset.range xs.length, xs.getD i z := by
  induction xs with
  | nil => simp
  | cons hd tl ih =>
    rw [List.sum_cons, List.length_cons, Finset.sum_range_succ',
        List.getD_cons_zero]
    simp only [List.getD_cons_succ]
    rw [← ih]
    abel

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

/-- **AM-GM for `t + 1/t`**: for `t > 0`, `t + 1/t ≥ 2`.

    Proof: `(t - 1)² ≥ 0` expands to `t² - 2t + 1 ≥ 0`, dividing
    by `t` gives `t - 2 + 1/t ≥ 0`, i.e. `t + 1/t ≥ 2`. -/
theorem add_inv_ge_two (t : ℝ) (ht : 0 < t) : t + 1 / t ≥ 2 := by
  have h_sq : (t - 1) ^ 2 ≥ 0 := sq_nonneg _
  have h_t_ne : t ≠ 0 := ne_of_gt ht
  have h_expand : (t - 1) ^ 2 = t^2 - 2*t + 1 := by ring
  rw [h_expand] at h_sq
  -- Divide through by t (positive)
  have : t + 1/t - 2 ≥ 0 := by
    rw [ge_iff_le, sub_nonneg, ← sub_le_iff_le_add']
    have h_div : (t^2 - 2*t + 1) / t ≥ 0 := div_nonneg h_sq ht.le
    have h_simp : (t^2 - 2*t + 1) / t = t - 2 + 1/t := by
      field_simp
    rw [h_simp] at h_div
    linarith
  linarith

/-- **AM-GM for `√x + 1/√x`**: for `x > 0`, `√x + 1/√x ≥ 2`.

    Direct corollary of `add_inv_ge_two` applied to `t := √x`. -/
theorem Real.sqrt_add_inv_ge_two (x : ℝ) (hx : 0 < x) :
    Real.sqrt x + 1 / Real.sqrt x ≥ 2 := by
  exact add_inv_ge_two (Real.sqrt x) (Real.sqrt_pos.mpr hx)

end QOU.MathlibExt
