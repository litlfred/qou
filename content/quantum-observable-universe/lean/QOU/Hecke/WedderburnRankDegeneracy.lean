import QOU.Hecke.Wedderburn
import QOU.Hecke.FullRank

/-!
# `WedderburnDecomp` does not characterise `H_n(q)` — an instance would prove nothing

**Bean `qou-luq7`, answered in the negative.** Re-verified against the
repaired class 2026-08-30 (bean `qou-0cyu`); see "The repair ... does not close
the hole" below.

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
partition; `complete` because that one value is `1`; and `block_scaling`
because the block character `χ^λ` is *itself* a free field of the class, so
`tr_M(x · π_λ) = y_λ · χ^λ(x)` constrains only the **product** `y_λ · χ^λ` —
choose `χ^λ` to absorb whatever `y_λ` you picked.

## The repair this module originally asked for has landed, and does not close
the hole

The first version of this file (2026-08-21) named a specific repair: replace
the old `trace_decomp` field — which asserted the summation identity outright
— with the block-scaling sentence `tr_M(x · π_λ) = y_λ · χ^λ(x)`, "so that
`y_λ` is pinned and `trace_decomp` can be deleted rather than assumed".

That repair landed in PR #5710 (commit `30e5df8938`), and it is a real
improvement: `trace_decomposition` is now *derived* from `complete` +
`block_scaling` rather than projected out of an axiom, and the pair of
theorems `weights_inert` / `weight_one_or_block_trace_zero` that the old field
forced are gone with it.

**But it does not pin `y_λ`, and this module now proves that too.** The class
stores the blocks abstractly, so `χ^λ` had to come in as a field alongside
`y_λ`; an equation on their product pins neither factor. `rankOneWedderburnScaled`
below realises **every** nonzero rational as the weight at every partition,
under an otherwise unchanged witness. So the degeneracy survives the repair,
and the reason it survives is the same reason the repair was needed: what the
class stores is not enough to compute the block character from, so the
character is assumed, and an assumed character can absorb an assumed weight.

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

## What would have to change (revised 2026-08-30)

Pairing the class with the rank predicate is still necessary:

```
variable [HeckeAlgebra R n q A] [IsHeckeOfFullRank R n A] [WedderburnDecomp n q A]
```

It is no longer *sufficient*, and the block-scaling half of the original
prescription has been tried. Two things would additionally have to hold:

1. **`χ^λ` must stop being a free field.** It has to be *computed* — as the
   trace of a matrix representation `ρ_λ : A → M_{f^λ}(R)`, which is the
   content the header docstring promises ("the matrix-algebra isomorphisms are
   captured abstractly") and the class does not carry. Only a `χ^λ` that is
   determined by the algebra makes `block_scaling` an equation about one
   unknown.
2. **`f^λ` must be tied to the partition.** `SpechtDimension` is a class with a
   free `dim` field and no link to `lam`; the hook-length formula is stated in
   its docstring and encoded nowhere. Without it there is no dimension count to
   contradict, which is why the exclusion below has to be argued from
   `Module.finrank ℚ ℚ` rather than from anything the class says.

Both are Mathas (1999) Theorem 3.43 — the seminormal form and its indexing by
`Partition n` — and neither is in Mathlib.

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
  chi_lambda := fun lam x => if lam.parts = (lam0 n).parts then x else 0
  block_scaling := by
    intro x lam
    by_cases h : lam.parts = (lam0 n).parts <;> simp [h, rankOneMarkov]

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

/-- **The witness assigns weight `1` at every partition**, including at ranks
where a genuine Ocneanu weight is not `1`. The `c = 1` case of
`yLambda_not_pinned` below, kept separately because it is the weight the
default witness above carries. -/
theorem rankOne_yLambda_all_one (n : ℕ) (lam : Partition n) :
    (rankOneWedderburn n).y_lambda lam = 1 := rfl

open Classical in
/-- **The same witness at an arbitrary nonzero weight.** Identical to
`rankOneWedderburn` except that `y_λ ≡ c` and the block character is rescaled
by `c⁻¹` to compensate. This is a `def`, not an `instance`: registering a
`c`-indexed family would make typeclass search ambiguous, and the point is made
by exhibiting it, not by having it found. -/
noncomputable def rankOneWedderburnScaled (n : ℕ) (c : ℚ) (hc : c ≠ 0) :
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
  y_lambda := fun _ => c
  all_parts := {lam0 n}
  complete := by rw [Finset.sum_singleton]; simp
  chi_lambda := fun lam x => if lam.parts = (lam0 n).parts then c⁻¹ * x else 0
  block_scaling := by
    intro x lam
    by_cases h : lam.parts = (lam0 n).parts <;>
      simp [h, rankOneMarkov, ← mul_assoc, mul_inv_cancel₀ hc]

/-- **`block_scaling` does not pin `y_λ`.** Every nonzero rational is realised
as the weight at every partition, by a witness that satisfies the whole class.

This is the sharper form of the module's claim, and it is what distinguishes
the current class from the one this file was written against. The 2026-08-21
version could say only that `y_λ` "appears in no other field"; PR #5710 gave it
another field, and it is still not pinned, because `chi_lambda` is free too and
absorbs the rescaling. An equation on a product of two unknowns pins neither.

Consequence for the audit: an instance of `WedderburnDecomp` still carries no
information about the Ocneanu weights, so it cannot be evidence for
`prop:y-lambda-recipe-from-partition` or anything downstream of it. -/
theorem yLambda_not_pinned (n : ℕ) (c : ℚ) (hc : c ≠ 0) :
    ∃ WD : WedderburnDecomp (R := ℚ) n 1 ℚ, ∀ lam, WD.y_lambda lam = c :=
  ⟨rankOneWedderburnScaled n c hc, fun _ => rfl⟩

end QOU.Hecke.RankOneDegeneracy
