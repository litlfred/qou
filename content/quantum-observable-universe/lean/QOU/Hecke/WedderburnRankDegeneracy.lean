import QOU.Hecke.Wedderburn
import QOU.Hecke.FullRank

/-!
# `WedderburnDecomp` does not characterise `H_n(q)` — an instance would prove nothing

**Bean `qou-luq7`, answered in the negative.**

## The question this module settles

`QOU.Hecke.WedderburnDecomp` has no instance anywhere in the tree, so its
consequences are conditional on an uninhabited class — and `#print axioms`
cannot see that. The natural repair is to *build* an instance, joining Mathlib's
Artin–Wedderburn (`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`) to
the Hecke dimension count.

**That repair would not work, and this module proves why.** The class is
satisfiable by a **one-dimensional** algebra at every `n`. Constructing an
instance would therefore establish nothing about `H_n(q)`, whose dimension is
`n!`; it would only silence the audit.

## The mechanism

`WedderburnDecomp` takes `[HeckeAlgebra R n q A]` as a hypothesis, and
`QOU.Hecke.InstanceH2.rankOneModel` inhabits *that* class at every `n` with
`A = R = ℚ`, `q = 1`, `embed := fun _ => 1`. PR #4857 found this degeneracy and
repaired it for `HeckeAlgebra` by adding the companion predicate
`IsHeckeOfFullRank` (`QOU/Hecke/FullRank.lean`), whose whole purpose is to
exclude the rank-one model. `WedderburnDecomp` never picked that companion up,
so it inherits the hole through its own hypothesis.

Every remaining field then goes through on `ℚ` for structural reasons, not by
any dodge: `central` because `ℚ` is commutative; `idempotent` and `orthogonal`
because the family `π_λ = if λ = λ₀ then 1 else 0` is supported at one
partition; `complete` because that one value is `1`; and `trace_decomp` because
— as `QOU/QBeta/WedderburnTraceDecomposition.lean` already records — the
weighted sum follows from `complete` alone once `y_λ` is unconstrained, and
`y_λ` *is* unconstrained: it appears in no other field.

## What this module does and does not claim

It does **not** claim `WedderburnDecomp` is false, or that its fields are
wrong. Each field is a true and meaningful sentence about a genuine Wedderburn
decomposition. The claim is the weaker, sharper one: **the fields do not
together pin down the algebra**, so inhabiting them is not evidence.

Scope, per AGENTS.md §"Before declaring refuted": this is a **structural
exclusion (b)**, and the invariant cited is a dimension count —
`Module.finrank ℚ ℚ = 1` against `n! ≥ 2` for `n ≥ 2`. It excludes
"an instance of the class as it stands is worth building", not the Wedderburn
decomposition itself.

## What would have to change

Pair the class with the rank predicate exactly as `HeckeAlgebra` was paired:

```
variable [HeckeAlgebra R n q A] [IsHeckeOfFullRank R n A] [WedderburnDecomp n q A]
```

and encode the block-scaling sentence `tr(x · π_λ) = y_λ · χ_λ(x)` — present in
the class docstring, absent from its fields — so that `y_λ` is pinned and
`trace_decomp` can be deleted rather than assumed
(`QOU/QBeta/WedderburnTraceDecomposition.lean` derives the sum from that
hypothesis). Only then does an instance carry content.

## References

- PR #4857 (`IsHeckeOfFullRank`, `rankOneModel`) — the same degeneracy, one
  class upstream.
- Mathas (1999), Theorem 3.43 — the mathematics an honest instance needs.
-/

namespace QOU.Hecke.RankOneDegeneracy

open QOU.Hecke

/-! ## The witness

Both instances below are **`scoped`**. Registering them globally would let
typeclass search discharge `[MarkovTrace …]` and `[WedderburnDecomp …]`
hypotheses with the degenerate model, which is the opposite of the point.
-/

/-- The Markov trace on the rank-one model: the identity functional on `ℚ`.
Normalisation, cyclicity and both generator-value axioms hold because every
generator maps to `1` and `ℚ` is commutative. -/
scoped instance rankOneMarkov (n : ℕ) : MarkovTrace (R := ℚ) n 1 ℚ where
  trace := LinearMap.id
  normalised := rfl
  cyclic := by intro x y; simp [mul_comm]
  z_param := 1
  trace_gen := by intro i; rfl
  trace_prod_gen := by intro i j _; rfl

/-- The all-ones partition `1 + 1 + ⋯ + 1 = n`. Exists at every `n`, which is
what lets the witness below be stated uniformly rather than at one fixed rank. -/
def lam0 (n : ℕ) : Partition n where
  parts := List.replicate n 1
  sum_eq := by simp
  positive := by
    intro p hp
    rw [List.eq_of_mem_replicate hp]
    norm_num
  decreasing := by
    simp [List.Sorted, List.pairwise_replicate]

open Classical in
/-- **The degenerate Wedderburn decomposition, at every `n`.**

Every field is the class's genuine equation, discharged: no `Prop`-variable
field, no `True`, no `sorry`. The carrier is `ℚ`, which is `Nontrivial` — so
this is a strictly stronger witness than a `PUnit`-style one, and it is not the
`triv_wedderburn` pattern of `QOU/Mathlib/HeckeAlgebra.lean`. -/
noncomputable scoped instance rankOneWedderburn (n : ℕ) :
    WedderburnDecomp (R := ℚ) n 1 ℚ where
  pi_lambda := fun lam => if lam.parts = (lam0 n).parts then (1 : ℚ) else 0
  idempotent := by
    intro lam; by_cases h : lam.parts = (lam0 n).parts <;> simp [h]
  orthogonal := by
    intro lam mu hne
    by_cases hl : lam.parts = (lam0 n).parts
    · by_cases hm : mu.parts = (lam0 n).parts
      · exact absurd (hl.trans hm.symm) hne
      · simp [hm]
    · simp [hl]
  central := by intro lam a; exact mul_comm _ _
  y_lambda := fun _ => 1
  all_parts := {lam0 n}
  complete := by rw [Finset.sum_singleton]; simp
  trace_decomp := by intro x; rw [Finset.sum_singleton]; simp

/-! ## The consequence -/

/-- **The headline.** At every `n ≥ 2` the class `WedderburnDecomp` is
inhabited by an algebra that provably **fails** the Hecke rank predicate.

Read the two conjuncts together: inhabiting `WedderburnDecomp` is compatible
with `¬ IsHeckeOfFullRank`, so an instance of the former is not evidence that
the carrier is `H_n(q)`. The second conjunct is `not_isHeckeOfFullRank_rankOne`
from `QOU/Hecke/FullRank.lean`, i.e. the same invariant PR #4857 introduced. -/
theorem wedderburnDecomp_does_not_pin_rank {n : ℕ} (hn : 2 ≤ n) :
    Nonempty (WedderburnDecomp (R := ℚ) n 1 ℚ) ∧ ¬ IsHeckeOfFullRank ℚ n ℚ :=
  ⟨⟨rankOneWedderburn n⟩, not_isHeckeOfFullRank_rankOne hn⟩

/-- The dimension invariant the exclusion rests on, stated on its own so the
`(b)`-scope citation is checkable: the witness carrier is one-dimensional, and
`H_n(q)` is not, at every `n ≥ 2`. -/
theorem rankOne_finrank_ne_factorial {n : ℕ} (hn : 2 ≤ n) :
    Module.finrank ℚ ℚ ≠ n.factorial := by
  rw [Module.finrank_self]
  have h2 : 2 ≤ n.factorial := by
    calc 2 = Nat.factorial 2 := rfl
      _ ≤ n.factorial := Nat.factorial_le hn
  omega

/-- **`y_lambda` is unconstrained.** The class's only use of `y_lambda` is in
`trace_decomp`, and that field follows from `complete` alone once the weights
may be chosen — here they are all `1`. Stated as the concrete fact that the
witness above assigns weight `1` to every partition, including at ranks where a
genuine Ocneanu weight is not `1`.

This re-confirms, on the merged class rather than in the abstract, what
`QOU/QBeta/WedderburnTraceDecomposition.lean` records: the weighted summation
identity was never the thing that needed assuming. -/
theorem rankOne_yLambda_all_one (n : ℕ) (lam : Partition n) :
    (rankOneWedderburn n).y_lambda lam = 1 := rfl

end QOU.Hecke.RankOneDegeneracy
