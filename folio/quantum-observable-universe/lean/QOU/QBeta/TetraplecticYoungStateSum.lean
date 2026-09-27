/-
# QOU.QBeta.TetraplecticYoungStateSum — Φ_b workplan result L5

**Tetraplectic → Young organization of the `N = 5` finite state-sum** (bean
`qou-d7lh`, PR #3768).

Result L1 (`QOU/QBeta/CyclotomicDilogCollapse.lean`) reduced the analytic
q-Pochhammer denominator at a primitive fifth root of unity to the finite
cyclotomic product `∏_{k<5}(1 − x·ζ^k) = 1 − x^5` — a product over the five
fifth roots of unity, indexed by `Finset.range 5`.  L5 records the *combinatorial
organization* of that finite reduction: the `S₅`-symmetry of the tetraplectic
form (`def:bring-cone-tetraplectic-structure`) decomposes
`L²(M,Ω)` into irreducible `S₅`-representations indexed by the **partitions of 5**,
and Nekrasov localization concentrates the finite state-sum on the corresponding
Young-tableaux fixed points (Hoefsmit seminormal basis,
`mass-theory/hoefsmit-ew-cell-content.md`).

## Honest scope — what is PROVED vs. structure-carried

**Proved, sorry-free (genuine combinatorial index matching):**

* `fifthRoots_index_card` — the L1 product index `Finset.range 5` has `5` elements
  (the five fifth roots of unity).
* `factorial_five`, `card_perm_fin_five` — `|S₅| = 5! = 120`.
* `partitions5_card` — the seven partitions of 5, exhibited as explicit
  `Nat.Partition 5` terms, are pairwise distinct (`= 7`).
* `partMultisets5_{card,sum,pos}` — the seven partition *multisets* (Young-diagram
  row-length data) are distinct, each sums to `5`, and has positive parts.
* `seven_le_card_partitions_five` — `7 ≤ Fintype.card (Nat.Partition 5)`, tying the
  explicit enumeration to Mathlib's `Nat.Partition`.  Mathlib's
  `Fintype (Nat.Partition 5)` instance depends on `Classical.choice`, so the exact
  count `p(5) = 7` (confirmed by `#eval Fintype.card (Nat.Partition 5)`, which
  returns `7`) is not kernel-reducible by `decide`; the seven exhibited distinct
  terms give the rigorous lower half.

**Structure-carried (§3b-cond conditional class; CONJECTURAL, NOT proved here):**
`YoungOrganization` axiomatizes the *physics inputs* — Nekrasov-localization
occupancy of every partition sector and the Burnside/Plancherel dimension identity
`Σ_λ (f^λ)² = 120`.  From those hypothesis fields the file *derives* genuine
consequences (`occupied_card`, `plancherel_eq_perm`); the hypotheses themselves are
the open tetraplectic → Young correspondence and stay unproved (no instance is
fabricated).  This is the honest state of L5 — the fuzziest of the five results.
-/
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Tactic

namespace QOU.QBeta.TetraplecticYoungStateSum

open Finset

/-! ## Combinatorial index matching (proved) -/

/-- The fifth-roots-of-unity index set of the L1 product `∏_{k<5}(1 − x·ζ^k)`
has `5` elements. -/
theorem fifthRoots_index_card : (Finset.range 5).card = 5 := by simp

/-- `5! = 120`. -/
theorem factorial_five : Nat.factorial 5 = 120 := by decide

/-- `|S₅| = 5! = 120`.  The order of the symmetric group whose irreducibles the
Young sectors index. -/
theorem card_perm_fin_five : Fintype.card (Equiv.Perm (Fin 5)) = 120 := by
  rw [Fintype.card_perm, Fintype.card_fin]; decide

/-! ### The seven partitions of 5 as explicit `Nat.Partition 5` terms

These are the seven Young diagrams `λ ⊢ 5` indexing the irreducible
`S₅`-representations / the sectors of the tetraplectic Young state-sum. -/

/-- `[5]`. -/
def part_5      : Nat.Partition 5 := ⟨{5},           by decide, by decide⟩
/-- `[4,1]`. -/
def part_41     : Nat.Partition 5 := ⟨{4, 1},        by decide, by decide⟩
/-- `[3,2]`. -/
def part_32     : Nat.Partition 5 := ⟨{3, 2},        by decide, by decide⟩
/-- `[3,1,1]`. -/
def part_311    : Nat.Partition 5 := ⟨{3, 1, 1},     by decide, by decide⟩
/-- `[2,2,1]`. -/
def part_221    : Nat.Partition 5 := ⟨{2, 2, 1},     by decide, by decide⟩
/-- `[2,1,1,1]`. -/
def part_2111   : Nat.Partition 5 := ⟨{2, 1, 1, 1},  by decide, by decide⟩
/-- `[1,1,1,1,1]`. -/
def part_11111  : Nat.Partition 5 := ⟨{1, 1, 1, 1, 1}, by decide, by decide⟩

/-- The seven partitions of 5, collected as a finset of `Nat.Partition 5`. -/
def partitions5 : Finset (Nat.Partition 5) :=
  {part_5, part_41, part_32, part_311, part_221, part_2111, part_11111}

/-- The seven exhibited partitions of 5 are pairwise distinct: `p(5) ≥ 7`, realized
inside Mathlib's `Nat.Partition 5`. -/
theorem partitions5_card : partitions5.card = 7 := by decide

/-- **`p(5) = 7`, lower half (rigorous).** There are at least seven partitions of 5,
tying the explicit enumeration to Mathlib's `Nat.Partition`.

The exact equality is `Fintype.card (Nat.Partition 5) = 7` (`#eval` confirms `7`),
but Mathlib's `Fintype (Nat.Partition 5)` instance is built with `Classical.choice`,
so the count is not kernel-reducible by `decide`; the completeness half ("every
partition of 5 is one of these seven") is the standard partition-count fact and is
not re-derived here. -/
theorem seven_le_card_partitions_five : 7 ≤ Fintype.card (Nat.Partition 5) :=
  partitions5_card ▸ Finset.card_le_univ partitions5

/-! ### The seven partition multisets (Young-diagram row-length data) -/

/-- The seven partition multisets of 5 — the row lengths of the seven Young
diagrams. -/
def partMultisets5 : Finset (Multiset ℕ) :=
  {{5}, {4, 1}, {3, 2}, {3, 1, 1}, {2, 2, 1}, {2, 1, 1, 1}, {1, 1, 1, 1, 1}}

/-- There are seven distinct partition multisets of 5. -/
theorem partMultisets5_card : partMultisets5.card = 7 := by decide

/-- Each partition multiset of 5 sums to `5`. -/
theorem partMultisets5_sum : ∀ m ∈ partMultisets5, m.sum = 5 := by decide

/-- Each partition multiset of 5 has strictly positive parts. -/
theorem partMultisets5_pos : ∀ m ∈ partMultisets5, ∀ i ∈ m, 0 < i := by decide

/-! ## Tetraplectic → Young correspondence (§3b-cond conditional class)

The deep content — that the `S₅`-equivariant Nekrasov localization of `L²(M,Ω)`
organizes the finite state-sum into exactly the partition-indexed irrep sectors —
is *conjectural* and is carried as hypothesis fields, not proved.  No instance is
constructed (the correspondence stays open); the derived theorems below are genuine
consequences of the hypotheses. -/

/-- **Tetraplectic → Young organization data** for the `N = 5` finite state-sum.

The two hypothesis fields axiomatize the conjectural physics inputs (per
AGENTS.md §3b-cond) — they are NOT theorems of this file:

* `nekrasov_occupied` — Nekrasov localization leaves no empty fixed-point stratum:
  every partition sector carries positive multiplicity in `L²(M,Ω)`;
* `plancherel` — the seminormal dimensions `f^λ` (numbers of standard Young
  tableaux of shape `λ`) satisfy the Burnside/Plancherel identity
  `Σ_λ (f^λ)² = 120 = |S₅|`.

`mult` and `dim` are the multiplicity and seminormal-dimension data; the file
derives `occupied_card` and `plancherel_eq_perm` from the two hypotheses. -/
structure YoungOrganization where
  /-- Multiplicity of the irrep `V_λ` in `L²(M,Ω)`, indexed by partitions of 5. -/
  mult : Nat.Partition 5 → ℕ
  /-- Seminormal dimension `f^λ` — the number of standard Young tableaux of
      shape `λ`. -/
  dim : Nat.Partition 5 → ℕ
  /-- HYPOTHESIS (Nekrasov localization, conjectural): every partition sector is
      occupied. -/
  nekrasov_occupied : ∀ p, 0 < mult p
  /-- HYPOTHESIS (Burnside / Plancherel, conjectural): `Σ_λ (f^λ)² = 120`. -/
  plancherel : ∑ p, (dim p) ^ 2 = 120

namespace YoungOrganization

variable (Y : YoungOrganization)

/-- **Derived consequence.** Given the Nekrasov-occupancy hypothesis, the number of
occupied partition sectors equals the total number of partitions of 5 — every
sector positive means the occupied-sector filter is all of `univ`.  Genuinely
derived from `nekrasov_occupied` (not a restatement of a field). -/
theorem occupied_card :
    (Finset.univ.filter (fun p : Nat.Partition 5 => 0 < Y.mult p)).card
      = Fintype.card (Nat.Partition 5) := by
  rw [Finset.filter_true_of_mem (fun p _ => Y.nekrasov_occupied p)]
  exact Finset.card_univ

/-- **Derived consequence.** The Plancherel dimension sum equals `|S₅|`, combining
the `plancherel` hypothesis with the proved `card_perm_fin_five`.  This realizes the
sum-of-squares-of-dimensions = group-order identity against Mathlib's
`Fintype.card (Equiv.Perm (Fin 5))`. -/
theorem plancherel_eq_perm :
    ∑ p, (Y.dim p) ^ 2 = Fintype.card (Equiv.Perm (Fin 5)) := by
  rw [Y.plancherel, card_perm_fin_five]

end YoungOrganization

end QOU.QBeta.TetraplecticYoungStateSum
