/-
# On a one-dimensional representation, a braid word collapses to three exponents

Two producers in this corpus compute `χ^λ(β)` for the same atomic braid word at the same
`q₀` and disagree in the fifth decimal (`chi_at_q0_via_hoefsmit_mpfr` vs
`rho_w_crystal_vertex_trace`, 1.1e-4 apart on the deuteron). Neither can adjudicate the
other directly, so the dispute is settled by a third route that uses no linear algebra at
all — but only once that route's own convention is fitted rather than assumed (see below).

The route: of the partitions of `n`, the one-row `[n]` and one-column `[1ⁿ]` give
**one-dimensional** Hecke representations. There every generator acts as a *scalar*, so the
representation is a monoid map into the units of a commutative ring, and evaluating a word
is a product of scalars rather than a product of matrices. Grouping the word's letters by
type then turns a 23-letter product into three exponents.

This file proves that collapse. `word_eval` evaluates a letter-list through an arbitrary
assignment `f`, and:

* `word_eval_append` — evaluation is multiplicative in concatenation;
* `word_eval_replicate` — a run of one letter is a power;
* `word_eval_three_types` — the statement actually used: a word built from three letter
  types evaluates to `f a ^ i * f b ^ j * f c ^ k`, regardless of interleaving.

The last one is what licenses reading the deuteron word as
`s^11 · (s⁻¹)^7 · I^5` with `s` the generator scalar and `I = s − h/2` the interface
("averaged") crossing — an expression a reader can evaluate by hand, depending on no
implementation. Commutativity is doing real work: on a 1-dim rep the letters commute even
though the braid group they come from does not, which is exactly why the interleaving can
be forgotten.

**What this does and does not settle.** It makes the collapse *valid*: the closed form is
the character of the one-dimensional rep, given an assignment of scalars to letters. It does
NOT pick the assignment — and that is exactly what was in dispute.

A first pass got this wrong and is recorded because the error is instructive. It fixed the
interface ("averaged") crossing at the color-blind `I = s − h/2`, taken from one of the two
disputing producers, and concluded the other was wrong. Since the arbiter had adopted one
side's convention, it agreed with that side by construction. The convention has to be
*fitted*, not assumed.

Fitting it (`computations/audits/chi_interface_convention_fit.py`) reverses the verdict.
Writing `k` for the number of averaged crossings taking the color-WEIGHTED form
`−h·(1/2 − δ/4)` instead of `−h/2`, every atomic χ cache fits an exact `k` to machine zero,
with `k = 1` precisely when the atom contains both a proton and a neutron. So the cache
implements the color-weighted p–n interface and `rho_w_crystal_vertex_trace`, which applies
`I = σ − h/2` to *every* averaged crossing, drops `δ` on that one crossing. Homogeneous atoms
(p, n, pp, nn) have no p–n interface and agree to 1e-50; every mixed atom disagrees.

The root cause is upstream of both: `classify_crossing` maps `−h/2` and `−h·(1/2 − δ/4)` onto
the single label `"averaged"`, and `atom_canonical_crossings` returns only that label, so a
consumer rebuilding operators from it cannot recover which crossing it had.

Numerical companion: `computations/audits/chi_interface_convention_fit.py`.
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Group.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU
namespace MassTheory
namespace OneDimWordCharacter

variable {L : Type*} {K : Type*} [CommMonoid K]

/-- Evaluate a word (a list of letters) through a scalar assignment `f`. On a
one-dimensional representation each generator acts by a scalar, so this *is* the
representation of the word. -/
def wordEval (f : L → K) : List L → K
  | [] => 1
  | x :: xs => f x * wordEval f xs

@[simp] theorem wordEval_nil (f : L → K) : wordEval f ([] : List L) = 1 := rfl

@[simp] theorem wordEval_cons (f : L → K) (x : L) (xs : List L) :
    wordEval f (x :: xs) = f x * wordEval f xs := rfl

/-- Evaluation is multiplicative in concatenation. -/
theorem wordEval_append (f : L → K) (u v : List L) :
    wordEval f (u ++ v) = wordEval f u * wordEval f v := by
  induction u with
  | nil => simp
  | cons x xs ih => simp [ih, mul_assoc]

/-- A run of a single repeated letter evaluates to a power. -/
theorem wordEval_replicate (f : L → K) (x : L) (m : ℕ) :
    wordEval f (List.replicate m x) = f x ^ m := by
  induction m with
  | zero => simp
  | succ m ih => simp [List.replicate_succ, ih, pow_succ, mul_comm]

/-- **The collapse.** A word built from three letter types — `i` copies of `a`, `j` of `b`,
`k` of `c` — evaluates to `f a ^ i * f b ^ j * f c ^ k`.

This is the step that turns the 23-letter deuteron word into `s^11 · (s⁻¹)^7 · I^5`. -/
theorem wordEval_three_types (f : L → K) (a b c : L) (i j k : ℕ) :
    wordEval f (List.replicate i a ++ List.replicate j b ++ List.replicate k c)
      = f a ^ i * f b ^ j * f c ^ k := by
  rw [wordEval_append, wordEval_append, wordEval_replicate, wordEval_replicate,
    wordEval_replicate, mul_assoc]

/-- **Interleaving does not matter.** Any permutation of a word evaluates the same, because
on a one-dimensional representation the letters commute — even though the braid group they
are drawn from does not. This is what lets the audit count letter types and ignore the order
in which they appear. -/
theorem wordEval_perm (f : L → K) {u v : List L} (h : u.Perm v) :
    wordEval f u = wordEval f v := by
  induction h with
  | nil => rfl
  | cons x _ ih => simp [ih]
  | swap x y l => simp [← mul_assoc, mul_comm (f x) (f y)]
  | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- The COLOR-BLIND interface ("averaged") crossing on a one-dimensional rep,
`I = s − h/2` with `h = q − q⁻¹`. On the trivial rep `s = q` this is exactly `(q + q⁻¹)/2` —
literally the average of `q` and `q⁻¹`, which is what the name asserts. The audit prints this
as a sanity check that it is reading the convention correctly.

Note the `2 ≠ 0` hypothesis is not bureaucratic: in characteristic 2 the right-hand side
divides by zero and the identity is FALSE, which is why `ring` alone refuses it. -/
theorem interface_on_trivial_rep {F : Type*} [Field F] (q : F) (h2 : (2 : F) ≠ 0) :
    q - (q - q⁻¹) / 2 = (q + q⁻¹) / 2 := by
  field_simp
  ring

end OneDimWordCharacter
end MassTheory
end QOU
