import Mathlib.Data.List.Basic
import Mathlib.Data.List.Perm
import Mathlib.Data.List.Sort
import Mathlib.Algebra.BigOperators.Group.List
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

end QOU.MathlibExt
