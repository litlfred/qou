/-
# The row cap leaves exactly three self-conjugate shapes

`QOU/Hecke/RowCap.lean` proves the fibre-dimension cap: a column of height `≥ 3`
admits no injective filling into a 2-dimensional fibre, so `ℓ(λ) > 2 ⇒ y_λ = 0`
under convention D. This file asks what that leaves of the **self-conjugate**
partitions, and the answer is very little.

Self-conjugacy forces `ℓ(λ) = λ₁` — the diagram has as many rows as its first
row has columns — so `ℓ(λ) ≤ 2` is `λ₁ ≤ 2`, and the whole diagram fits in a
2×2 box. Exactly three shapes survive:

```
(1)      n = 1
(2,1)    n = 3
(2,2)    n = 4
```

**and none at any `n ≥ 5`** (`selfConj_two_row_size_le_four`). Enumerated to
`n = 30` in `computations/qbeta/qbeta_self_conjugate_row_cap_probe.py`; the
self-conjugate partitions do not stop existing — there are 2 at `n = 8`, 3 at
`n = 12` — they simply all have three or more rows.

## Why this matters, and the step this file deliberately does NOT take

The corpus's Wigner energy `-Δ_W · T(T+1)/A` — the symmetry energy, in the mass
channel rather than the binding one — is built from **self-conjugate shadow
prices**: `content/quantum-observable-universe/mass-theory/unified-iterative-correction-proof.md`
names `λ = (2,2)` at `k = 4` and `λ = (3,1,1)` at `k = 5`, and
`figure-eight-branching-rule-proof.md` states the general rule that
self-conjugate partitions carry the isospin Casimir terms `T(T+1)/A`,
`T(T+1)(T+2)/A²`. Of those two, `(2,2)` has `ℓ = 2` and survives the cap;
`(3,1,1)` has `ℓ = 3` and has zero Markov weight.

🛑 **That is a tension, not a refutation, and the difference is load-bearing.**
The shadow prices `C_λ` are described as q-integer products of hooks, contents
and Frobenius coordinates; `y_λ` enters the same construction separately, as the
budget constraint `Σ_λ d_λ y_λ = 1`. **Whether `y_λ = 0` forces `C_λ = 0` is not
established anywhere**, and this file does not assume it — every theorem below is
about partition shapes and list lengths, with no dependency on the LP. So the
enumeration stands whichever way that question goes, and the question itself is
the successor (bean `qou-a5jk`).

## Representation

A partition with at most two rows is a pair `(a, b)` with `b ≤ a`. Its conjugate
is read off the columns: `b` columns of height 2, then `a - b` of height 1. So
the conjugate has exactly `a` parts (`conjTwoRow_length`), and self-conjugacy —
which asks for two parts — forces `a = 2` immediately.
-/

import Mathlib.Tactic

namespace QOU.Hecke.SelfConjugateRowCap

/-- Column heights of the two-row shape `(a, b)` with `b ≤ a`: `b` columns of
height `2`, then `a - b` columns of height `1`. This is the conjugate partition,
written as a list of parts. -/
def conjTwoRow (a b : ℕ) : List ℕ :=
  List.replicate b 2 ++ List.replicate (a - b) 1

/-- **The conjugate of a two-row shape has exactly `a` parts.** All the content
is here: conjugating turns the FIRST ROW LENGTH into the ROW COUNT. -/
theorem conjTwoRow_length {a b : ℕ} (hab : b ≤ a) : (conjTwoRow a b).length = a := by
  simp [conjTwoRow, List.length_append, List.length_replicate]
  omega

/-- **Self-conjugacy with two rows forces `a = 2`.** The conjugate has `a` parts
and the original has `2`, so a shape equal to its own conjugate has `λ₁ = 2`. -/
theorem selfConj_forces_first_row_two {a b : ℕ} (hab : b ≤ a)
    (hsc : conjTwoRow a b = [a, b]) : a = 2 := by
  have h := congrArg List.length hsc
  rw [conjTwoRow_length hab] at h
  simpa using h

/-- **The enumeration.** With `1 ≤ b ≤ a`, the only self-conjugate two-row shapes
are `(2,1)` and `(2,2)`. -/
theorem selfConj_two_row_enum {a b : ℕ} (hb : 1 ≤ b) (hab : b ≤ a)
    (hsc : conjTwoRow a b = [a, b]) :
    (a = 2 ∧ b = 1) ∨ (a = 2 ∧ b = 2) := by
  have ha : a = 2 := selfConj_forces_first_row_two hab hsc
  subst ha
  interval_cases b
  · exact Or.inl ⟨rfl, rfl⟩
  · exact Or.inr ⟨rfl, rfl⟩

/-- **The size bound, and the consequence.** A self-conjugate shape with at most
two rows has at most four cells — so under the row cap there is NO self-conjugate
partition at any level `n ≥ 5`, and a mechanism resting on self-conjugate shadow
prices has nothing to draw on above `k = 4`. -/
theorem selfConj_two_row_size_le_four {a b : ℕ} (hb : 1 ≤ b) (hab : b ≤ a)
    (hsc : conjTwoRow a b = [a, b]) : a + b ≤ 4 := by
  rcases selfConj_two_row_enum hb hab hsc with ⟨ha, hbv⟩ | ⟨ha, hbv⟩ <;> omega

/-- `(2,1)` is self-conjugate: the `k = 3` survivor. -/
theorem selfConj_two_one : conjTwoRow 2 1 = [2, 1] := by decide

/-- `(2,2)` is self-conjugate: the `k = 4` survivor, and the one Wigner shadow
price the row cap leaves standing. -/
theorem selfConj_two_two : conjTwoRow 2 2 = [2, 2] := by decide

/-- `(3,1)` is NOT — its conjugate `[2,1,1]` has three parts, which is the row
cap biting. Included as the smallest concrete failure. -/
theorem not_selfConj_three_one : conjTwoRow 3 1 ≠ [3, 1] := by decide

/-- **No self-conjugate two-row shape has five or more cells.** The
contrapositive of `selfConj_two_row_size_le_four`, and the form the consequence
is actually used in: a self-conjugate partition of `n ≥ 5` necessarily has
`ℓ(λ) > 2`, hence `y_λ = 0` under convention D.

The rest of the chain lives in the content sibling
`content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.lean`,
which the library tree cannot import (siblings sit outside the package globs):
`shadow_price_eq_zero_of_weight_eq_zero` proves `w̃_λ = 0 → u*_λ = 0` from the
class field `C_eq : C λ = w̃_λ · h·⅟2`. Joined, they say **the Wigner mechanism
contributes nothing above `k = 4`** — only `λ = (2,2)` is left.

Bean `qou-w06d`; answers the successor `qou-a5jk` opened. -/
theorem no_selfConj_two_row_of_five_le {a b : ℕ} (hb : 1 ≤ b) (hab : b ≤ a)
    (hn : 5 ≤ a + b) : conjTwoRow a b ≠ [a, b] := by
  intro hsc
  have := selfConj_two_row_size_le_four hb hab hsc
  omega

end QOU.Hecke.SelfConjugateRowCap
