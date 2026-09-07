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
- §3b Reversal-invariance of products under `Pairwise Commute`
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
theorem sum_insertionSort_eq {α : Type*} [AddCommMonoid α]
    (r : α → α → Prop) [DecidableRel r] (xs : List α) :
    (xs.insertionSort r).sum = xs.sum :=
  (xs.perm_insertionSort r).sum_eq

/-- Sorting (by any relation) preserves the list's product
    (for commutative monoids).

    TODO upstream: `Mathlib.Data.List.Sort`. -/
theorem prod_insertionSort_eq {α : Type*} [CommMonoid α]
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
theorem foldl_mul_eq_prod_mul {α : Type*} [Monoid α]
    (xs : List α) (init : α) :
    xs.foldl (· * ·) init = init * xs.prod :=
  List.foldl_mul_eq_mul_prod xs init

/-! ## §3  Foldl/foldr commutativity -/

/-- For a *commutative* monoid, foldl and foldr agree: both
    produce `init * xs.prod = xs.prod * init`. -/
theorem foldl_eq_foldr_comm {α : Type*} [CommMonoid α]
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

    **CORRECTION 2026-09-05: this does NOT discharge
    `MatrixChainEqBuildChains`.**  The sentence removed here claimed it did
    "after some rearrangement".  It does not, and the reason is structural
    rather than a missing rearrangement: this lemma moves the *initial
    accumulator* from one end of the product to the other and leaves the
    list order alone (both sides are `init * xs.prod` / `xs.prod * init`).
    `matrixChain` does not have an accumulator problem — it **reverses the
    list** (`matrixChain (x :: l) = matrixChain l * f x`, so
    `matrixChain seq = (seq.map f).reverse.prod`).  The lemma that applies
    is `prod_reverse_eq_of_pairwise_commute` in §3b.  (That call site is now
    fully closed — `QOU.TMCorrespondence.matrixChain_eq_buildChains` is proved
    unconditionally as of 2026-09-05, and the class has an instance.)

    The lemma itself is correct and is kept; only its claimed consequence
    was wrong. -/
theorem foldl_eq_foldr_of_commute_init {α : Type*} [Monoid α]
    (xs : List α) (init : α) (h : ∀ x ∈ xs, Commute init x) :
    xs.foldl (· * ·) init = xs.foldr (· * ·) init := by
  rw [List.foldl_mul_eq_mul_prod, List.foldr_mul_eq_prod_mul]
  exact (List.commute_init_prod init xs h)

/-- Permutation-invariance of products in a commutative monoid
    (specialisation of `List.Perm.prod_eq` for use as a lookup
    target by automation). -/
theorem prod_eq_of_perm {α : Type*} [CommMonoid α]
    {xs ys : List α} (h : xs.Perm ys) :
    xs.prod = ys.prod :=
  List.Perm.prod_eq h

/-! For a `CommMonoid`, the underlying Mathlib lemma
    `List.Perm.prod_eq` already gives us order-invariance of
    products — folding from any direction over any permutation of
    the list produces the same answer. The two corollaries below
    package this for use at common call sites. -/

/-- `xs.reverse.prod = xs.prod` in a `CommMonoid`. -/
theorem prod_reverse_eq {α : Type*} [CommMonoid α] (xs : List α) :
    xs.reverse.prod = xs.prod :=
  (xs.reverse_perm).prod_eq

/-! ### §3b  Reversal-invariance WITHOUT commutativity of the operation

    `prod_reverse_eq` above needs a `CommMonoid`.  The matrices this
    formalisation actually reverses (`QOU.TMCorrespondence.matrixChain`)
    live in `Matrix (Fin 2) (Fin 2) R_t`, which is **not** commutative —
    only the *specific* transfer matrices in play commute pairwise
    (`QOU.Archimedean.transferMatrix_comm`).  The lemmas below are the
    `Pairwise Commute` strengthening that case needs. -/

/-- A `Pairwise` relation that holds for *every* pair holds along any list. -/
theorem pairwise_of_forall {α : Type*} {R : α → α → Prop} (xs : List α)
    (h : ∀ a b, R a b) : xs.Pairwise R := by
  induction xs with
  | nil => exact List.Pairwise.nil
  | cons hd tl ih => exact List.Pairwise.cons (fun b _ => h hd b) ih

/-- **Reversing a list does not change its product when the list's own
    elements commute pairwise** — the non-commutative-monoid form of
    `prod_reverse_eq`.

    Note this needs nothing new from Mathlib: `List.Perm.prod_eq'`
    (`Mathlib/Algebra/BigOperators/Group/List/Lemmas.lean:56`) already
    takes exactly a `Pairwise Commute` hypothesis, and `List.reverse_perm`
    supplies the permutation.  Recorded here because the QOU call site had
    been looking for a `foldl`/`foldr` bridge lemma instead, which is a
    different (and, for that call site, unnecessary) statement — see the
    correction on `§3a` below and on
    `QOU.TMCorrespondence.MatrixChainEqBuildChains`. -/
theorem prod_reverse_eq_of_pairwise_commute {α : Type*} [Monoid α]
    (xs : List α) (h : xs.Pairwise Commute) :
    xs.reverse.prod = xs.prod :=
  ((List.reverse_perm xs).symm.prod_eq' h).symm

/-- Mapped form: when a family `f` commutes with itself globally, the
    product over `xs.map f` is reversal-invariant. -/
theorem prod_map_reverse_eq_of_forall_commute {α β : Type*} [Monoid β]
    (f : α → β) (xs : List α) (h : ∀ x y : α, Commute (f x) (f y)) :
    (xs.map f).reverse.prod = (xs.map f).prod :=
  prod_reverse_eq_of_pairwise_commute _
    (List.pairwise_map.mpr (pairwise_of_forall xs (fun a b => h a b)))

/-- A natural-number list's sum equals the indexed Finset sum
    of its `getD ·  0` accessor. Mechanical induction on the list.

    TODO upstream: `Mathlib.Algebra.BigOperators.Group.List` —
    standard sum-is-finset-sum identity. -/
theorem sum_eq_finsetSum_getD {α : Type*} [AddCommMonoid α]
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

    Upstream status: this is the `.symm` of Mathlib's `Real.sqrt_eq_rpow`
    (present in the pinned v4.24).  A named `Real.rpow_one_div_two` is
    **not** in the pinned Mathlib (probed 2026-06-26 — `unknown constant`),
    so this local convenience wrapper stays until/unless one lands upstream. -/
theorem Real.rpow_half_eq_sqrt (x : ℝ) :
    x ^ (1/2 : ℝ) = Real.sqrt x :=
  (Real.sqrt_eq_rpow x).symm

/-- For `x > 0`, `x^(-(1/2) : ℝ) = 1 / Real.sqrt x`. -/
theorem Real.rpow_neg_half_eq (x : ℝ) (hx : 0 < x) :
    x ^ (-(1/2 : ℝ)) = 1 / Real.sqrt x := by
  rw [Real.rpow_neg hx.le, Real.rpow_half_eq_sqrt x, one_div]

/-- The QOU "denominator" `q^(1/2) + q^(-1/2)` equals
    `sqrt q + 1 / sqrt q`. -/
theorem q_half_denom (q : ℝ) (hq : 0 < q) :
    q ^ (1/2 : ℝ) + q ^ (-(1/2 : ℝ)) = Real.sqrt q + 1 / Real.sqrt q := by
  rw [Real.rpow_half_eq_sqrt q, Real.rpow_neg_half_eq q hq]

/-- For `x > 0`, the function `t ↦ t + 1/t` evaluated at
    `t = Real.sqrt x` is non-negative and admits a clean
    cross-multiplication identity:
    `(Real.sqrt x) · ((Real.sqrt x) + 1 / (Real.sqrt x))
       = x + 1`,
    i.e. multiplying the QOU half-denominator by `sqrt x` clears
    the inverse, yielding a closed-form polynomial in `x`. -/
theorem sqrt_mul_half_denom (x : ℝ) (hx : 0 < x) :
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
theorem sqrt_add_inv_ge_two (x : ℝ) (hx : 0 < x) :
    Real.sqrt x + 1 / Real.sqrt x ≥ 2 := by
  exact add_inv_ge_two (Real.sqrt x) (Real.sqrt_pos.mpr hx)

end QOU.MathlibExt
