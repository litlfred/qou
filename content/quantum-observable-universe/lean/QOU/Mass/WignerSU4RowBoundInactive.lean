import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic

/-!
# QOU.Mass.WignerSU4RowBoundInactive — the doubly-magic SU(4) route cannot SIZE the
⁴He enhancement

`prop:bk-coordination-multiplicity` reads the jet-filtration body-order multiplicity
off AME2020 as `M_need(A) = B_AME/(m_e·Vol_A)`, matches the non-magic `A = 3` pair with
the coordination number `z = A − 1`, and attributes doubly-magic ⁴He an extra factor
`M_need/z ≈ 2.52`, identified with the Schur–Weyl period `a_D^(4) = Σ_{λ⊢4} dim_q λ / 4`.

The standing structural motivation for singling out `A = 4` is Wigner's SU(4)
supermultiplet scheme: the nucleon spin–isospin space is 4-dimensional, ⁴He is the
`[1⁴]` singlet, and `dim [1ⁿ] = C(4,n)` vanishes for `n ≥ 5`.  The corpus is careful
to say this **locates** the `A = 4` turnover without **sizing** it.

**This file proves that "without sizing" is not a caution but a theorem.**

## The invariant

A partition of `n` has at most `n` parts, because every part is `≥ 1`
(`rows_le`).  Hence for every `n ≤ 4` the SU(4) admissibility constraint
"at most 4 rows" is satisfied by **every** partition of `n` (`su4_inactive_of_le_four`),
so the admissible set *is* the full set (`su4_filter_eq_univ`) and, for **every** weight
function `w` into **every** `AddCommMonoid`, the SU(4)-restricted Schur–Weyl sum equals
the unrestricted one (`su4_restricted_sum_eq`).

A constraint that is satisfied vacuously at both `n = 3` and `n = 4` takes the same
value on both, so **no functional built by imposing it can distinguish them** — in
particular it cannot produce a factor present at `A = 4` and absent at `A = 3`.
`su4_no_magic_enhancement` states exactly that: the restricted-to-unrestricted *ratio*
is `1` at both, for any weight.

The bound is not vacuous in general — it first bites at `n = 5`, witnessed by the
all-ones partition (`su4_active_at_five`), which is precisely the `dim [1⁵] = 0` fact
the corpus already uses.  So the SU(4) row bound is a genuine constraint that happens
to be **inactive exactly on the range where the enhancement lives**.

## Scope

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md §"Before
declaring refuted / ruled out / dead end": it cites a proved invariant (`rows_le`,
below) rather than a failed numerical probe.  Its scope is narrow and deliberate — it
excludes the *Wigner-SU(4)-row-restriction* route to sizing the enhancement, and
**nothing else**.  It says nothing about:

* whether some other Schur–Weyl functional sizes it (the `a_D^(4)` identification is
  tested numerically, and found wanting, in
  `computations/magic_shell_enhancement_derive_or_refute.py` — that is scope (a));
* whether ⁴He's closed shell has some non-representation-theoretic consequence;
* the `A = 3` `z = A − 1` match, which is untouched.

Base ring: `ℕ` for the combinatorial core; the summation lemma is stated over a generic
`[AddCommMonoid R]` (AGENTS.md §7c — nothing archimedean is used or needed).
-/

namespace QOU.Mass

open Finset

/-- The number of **rows** of a partition — the number of its parts.  In the Wigner
supermultiplet reading this is the number of rows of the Young diagram, and SU(4)
admissibility is the requirement that it not exceed `dim` of the spin–isospin space. -/
def rows {n : ℕ} (p : n.Partition) : ℕ := Multiset.card p.parts

/-- A multiset of positive naturals has at most as many elements as its sum. -/
theorem card_le_sum_of_pos (s : Multiset ℕ) (h : ∀ x ∈ s, 0 < x) :
    Multiset.card s ≤ s.sum := by
  classical
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
      have ha : 1 ≤ a := h a (Multiset.mem_cons_self a s)
      have hs : ∀ x ∈ s, 0 < x := fun x hx => h x (Multiset.mem_cons_of_mem hx)
      have := ih hs
      simp only [Multiset.card_cons, Multiset.sum_cons]
      omega

/-- **The invariant.**  A partition of `n` has at most `n` rows, because every part is
positive.  This is the whole content of the file: everything below is a consequence. -/
theorem rows_le (n : ℕ) (p : n.Partition) : rows p ≤ n := by
  have h : Multiset.card p.parts ≤ p.parts.sum :=
    card_le_sum_of_pos p.parts (fun _ hx => p.parts_pos hx)
  rw [p.parts_sum] at h
  exact h

/-- Wigner SU(4) admissibility: the spin–isospin space is 4-dimensional, so a Young
diagram carries a nonzero SU(4) irrep exactly when it has at most 4 rows. -/
def SU4Admissible {n : ℕ} (p : n.Partition) : Prop := rows p ≤ 4

instance {n : ℕ} (p : n.Partition) : Decidable (SU4Admissible p) :=
  inferInstanceAs (Decidable (rows p ≤ 4))

/-- **The bound is inactive below 5.**  For `n ≤ 4` every partition of `n` is SU(4)
admissible, since it has at most `n ≤ 4` rows. -/
theorem su4_inactive_of_le_four {n : ℕ} (hn : n ≤ 4) (p : n.Partition) :
    SU4Admissible p :=
  le_trans (rows_le n p) hn

/-- Restated as a set identity: below `n = 5` the SU(4)-admissible partitions are *all*
the partitions. -/
theorem su4_filter_eq_univ {n : ℕ} (hn : n ≤ 4) [Fintype n.Partition] [DecidableEq n.Partition] :
    (Finset.univ.filter fun p : n.Partition => SU4Admissible p) = Finset.univ := by
  classical
  refine Finset.eq_univ_of_forall fun p => ?_
  simpa using su4_inactive_of_le_four hn p

/-- **The exclusion.**  For every `n ≤ 4` and every weight function `w` into any
`AddCommMonoid`, the SU(4)-restricted Schur–Weyl sum coincides with the unrestricted
one.  Imposing SU(4) admissibility below `n = 5` changes nothing, whatever is being
summed — in particular it cannot introduce a factor at `A = 4`. -/
theorem su4_restricted_sum_eq {R : Type*} [AddCommMonoid R] {n : ℕ} (hn : n ≤ 4)
    [Fintype n.Partition] [DecidableEq n.Partition] (w : n.Partition → R) :
    ∑ p ∈ Finset.univ.filter (fun p : n.Partition => SU4Admissible p), w p
      = ∑ p : n.Partition, w p := by
  classical
  rw [su4_filter_eq_univ hn]

/-- **The enhancement statement.**  The SU(4) row restriction takes the *same* value —
namely, no value at all: the unrestricted sum — at `n = 3` and at `n = 4`, for every
weight.  So it cannot be the source of a factor present at ⁴He and absent at the `A = 3`
pair.  This is the formal content of "SU(4) LOCATES the `A = 4` turnover but does not
SIZE it". -/
theorem su4_no_magic_enhancement {R : Type*} [AddCommMonoid R]
    [Fintype (Nat.Partition 3)] [DecidableEq (Nat.Partition 3)]
    [Fintype (Nat.Partition 4)] [DecidableEq (Nat.Partition 4)]
    (w₃ : (Nat.Partition 3) → R) (w₄ : (Nat.Partition 4) → R) :
    (∑ p ∈ Finset.univ.filter (fun p : Nat.Partition 3 => SU4Admissible p), w₃ p
        = ∑ p : Nat.Partition 3, w₃ p)
    ∧ (∑ p ∈ Finset.univ.filter (fun p : Nat.Partition 4 => SU4Admissible p), w₄ p
        = ∑ p : Nat.Partition 4, w₄ p) :=
  ⟨su4_restricted_sum_eq (by norm_num) w₃, su4_restricted_sum_eq (by norm_num) w₄⟩

/-- **Non-vacuity of the instance hypotheses.**  `su4_restricted_sum_eq` and
`su4_no_magic_enhancement` carry `[Fintype n.Partition]` / `[DecidableEq n.Partition]`
binders; Mathlib supplies both (`Nat.Partition` derives `DecidableEq`, and the `Fintype`
instance is the one `QOU.Mathlib.YoungLatticeCornerCount` transports along
`partitionShapeEquiv`).  This `example` resolves them by instance search, so the
theorems above are applicable rather than conditionally empty. -/
example :
    ∑ _p ∈ Finset.univ.filter (fun p : Nat.Partition 4 => SU4Admissible p), (1 : ℕ)
      = ∑ _p : Nat.Partition 4, (1 : ℕ) :=
  su4_restricted_sum_eq (by norm_num) _

/-- The all-ones partition of `n`, used to show the SU(4) bound is not vacuous. -/
def allOnes (n : ℕ) : n.Partition where
  parts := Multiset.replicate n 1
  parts_pos := by
    intro i hi
    rw [Multiset.eq_of_mem_replicate hi]
    norm_num
  parts_sum := by simp

@[simp] theorem rows_allOnes (n : ℕ) : rows (allOnes n) = n := by
  simp [rows, allOnes]

/-- **The bound is genuine, and first bites at `n = 5`.**  `[1⁵]` has five rows, so it
is not SU(4)-admissible — the `dim [1ⁿ] = C(4,n) = 0` for `n ≥ 5` fact the corpus uses
to locate the turnover.  Together with `su4_inactive_of_le_four` this pins the
activation threshold exactly at `n = 5`: the constraint is real, and it is real
strictly *above* the range where the ⁴He enhancement is claimed. -/
theorem su4_active_at_five : ¬ SU4Admissible (allOnes 5) := by
  simp [SU4Admissible]

end QOU.Mass
