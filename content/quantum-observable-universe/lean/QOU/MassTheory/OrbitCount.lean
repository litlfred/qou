import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.Perm.Support
import Mathlib.Tactic

/-!
# Orbit counting for permutations: the additive core

Bean `qou-zrx2` follow-up (5), reopened by `qou-pdg9` / `qou-qqm4`.

## Why this file exists

`ClassicalTraceFloor` derives the classical floor `c₀(A) = 2^{−A} − 2^{1−2A}` of the
Markov trace difference from two cycle counts of the canonical braid word,

    c(σ_free) = 2A,        c(σ_atom) = A + 1,

and `LeadingOrderTraceCoefficient` derives `c₁` from the same counts with one
letter deleted. **Both take those counts as stated hypotheses**, verified by an
18-point computation rather than proved, because Mathlib has `Equiv.Perm.cycleType`,
`SameCycle` and `Disjoint.cycleType_mul` but **no orbit-count API** and no lemma
for how an orbit count moves when a permutation is multiplied by a transposition.

This file supplies the API and the additive half of what those counts need.

## The right object is the DEFECT, not the count

The number of orbits (cycles *including* fixed points) of `σ` on a fintype `α` is

    orbitCount σ = (fixed points) + (number of nontrivial cycles)
                 = card α − #support σ + card (cycleType σ)

which subtracts, so it is awkward in `ℕ` and not additive. Its complement

    orbitDefect σ = #support σ − card (cycleType σ) = Σ_{c ∈ cycleType σ} (c − 1)

**is** additive over disjoint permutations, is `0` for the identity, and is `1` for
a transposition. `orbitCount σ = card α − orbitDefect σ` recovers the count.

## What is proved here

* `orbitDefect_one`, `orbitDefect_swap`, and `card_cycleType_le_card_support`
  (so the `ℕ` subtraction in the definition is honest, not truncating).
* `orbitDefect_mul_of_disjoint` — the additive core.
* `orbitDefect_prod_of_pairwise_disjoint` — additivity over a list, which is what a
  braid word built one disjoint nucleon block at a time needs.
* `orbitCount_prod_of_disjoint_unit_defect` — **the free-word half of
  `ClassicalTraceFloor`'s hypotheses, provable now.** The free word is a disjoint
  product of one identical block per nucleon, each of defect one, so on `3A` strands
  it leaves `3A − A = 2A` orbits: exactly the `c(σ_free) = 2A` that file assumes.
* `sign_eq_neg_one_pow_orbitDefect` — the defect's **parity** is the sign, so
  multiplying by any transposition flips it: `orbitDefect_swap_mul_odd`. Half of the
  ±1 step comes free this way.

## 🛑 What is NOT proved here, stated plainly

The **magnitude** of the transposition step — that multiplying by a transposition
changes the orbit count by *exactly* one. Its parity is proved
(`orbitDefect_swap_mul_odd`); the bound `|Δ| ≤ 1` is the gap.

**It reduces to two strictly smaller pieces**, and the merge case is then *derived*
rather than assumed (see the section before them):

* **(S)** `orbitDefect_swap_mul_of_sameCycle` — the split, within one cycle. This is
  the direction Mathlib comes closest to: `Equiv.Perm.IsCycle.swap_mul` already
  proves that removing a point from a cycle leaves a cycle.
* **(R)** `sameCycle_swap_mul_of_not_sameCycle` — joining two different cycles puts
  the two points in one cycle of the product. Elementary; the walk argument is
  written out at the statement.

`orbitDefect_swap_mul_of_not_sameCycle` (the merge) is **proved from (S) and (R)**,
using that `swap a b` is an involution. So the two `sorry`s are exactly (S) and (R),
not the general statement.

So this file does **not** yet discharge the `ClassicalTraceFloor` hypotheses: it
closes the **free** half outright and reduces the **atom** half from "a tabulated
count at every `A`" to the two pieces (S) and (R), proving everything else that
reduction needs — including the merge case itself. That is the honest state; do not cite it as closing the
cycle-count gap.

-- Ref: [manuscript] bean qou-zrx2 follow-up (5); the transposition/cycle-count
-- step is the classical fact underlying well-definedness of the sign of a
-- permutation, standard in any treatment of symmetric groups.
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm Finset

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- A multiset of naturals each at least two has sum at least twice its cardinality.
(Stated standalone: inducting on `σ.cycleType` in place generalises the multiset and
loses the `two_le_of_mem_cycleType` hypothesis.) -/
private theorem two_mul_card_le_sum {s : Multiset ℕ} (h : ∀ n ∈ s, 2 ≤ n) :
    2 * Multiset.card s ≤ s.sum := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a t ih =>
      have ha : 2 ≤ a := h a (Multiset.mem_cons_self a t)
      have ih' := ih (fun n hn => h n (Multiset.mem_cons_of_mem hn))
      simp only [Multiset.card_cons, Multiset.sum_cons]
      omega

/-- Every cycle in `cycleType` has length at least two, so there are at most as many
cycles as support elements — this is what makes the `ℕ` subtraction in `orbitDefect`
an honest one. -/
theorem card_cycleType_le_card_support (σ : Perm α) :
    Multiset.card σ.cycleType ≤ #σ.support := by
  have hsum : σ.cycleType.sum = #σ.support := sum_cycleType σ
  have h2 : 2 * Multiset.card σ.cycleType ≤ σ.cycleType.sum :=
    two_mul_card_le_sum (fun _ hn => two_le_of_mem_cycleType hn)
  omega

/-- `orbitDefect σ = Σ_{c ∈ cycleType σ} (c − 1)`: the number of elements a
permutation "uses up" beyond one representative per orbit. Additive over disjoint
permutations, unlike the orbit count itself. -/
def orbitDefect (σ : Perm α) : ℕ := #σ.support - Multiset.card σ.cycleType

/-- The number of orbits of `σ` on `α`, fixed points included. -/
def orbitCount (σ : Perm α) : ℕ := Fintype.card α - orbitDefect σ

theorem orbitDefect_one : orbitDefect (1 : Perm α) = 0 := by
  simp [orbitDefect, cycleType_one]

theorem orbitCount_one : orbitCount (1 : Perm α) = Fintype.card α := by
  simp [orbitCount, orbitDefect_one]

/-- The defect never exceeds the support, so the orbit count never underflows. -/
theorem orbitDefect_le_card (σ : Perm α) : orbitDefect σ ≤ Fintype.card α :=
  le_trans (Nat.sub_le _ _) (card_le_univ _ |>.trans_eq (Finset.card_univ))

/-- A transposition has defect one: two support elements, one cycle. -/
theorem orbitDefect_swap {a b : α} (h : a ≠ b) : orbitDefect (swap a b) = 1 := by
  have hs : #(swap a b).support = 2 := by
    rw [support_swap h]; exact card_pair h
  have hc : (swap a b).cycleType = {2} := isSwap_iff_cycleType.mp ⟨a, b, h, rfl⟩
  simp [orbitDefect, hs, hc]

/-- **The additive core.** Disjoint permutations have additive defect. -/
theorem orbitDefect_mul_of_disjoint {σ τ : Perm α} (h : Disjoint σ τ) :
    orbitDefect (σ * τ) = orbitDefect σ + orbitDefect τ := by
  have hsupp : #(σ * τ).support = #σ.support + #τ.support := h.card_support_mul
  have hcyc : (σ * τ).cycleType = σ.cycleType + τ.cycleType := h.cycleType_mul
  have h1 := card_cycleType_le_card_support σ
  have h2 := card_cycleType_le_card_support τ
  simp only [orbitDefect, hsupp, hcyc, Multiset.card_add]
  omega

/-- Additivity over a list of pairwise-disjoint permutations — the shape a braid word
assembled one nucleon block at a time actually has. -/
theorem orbitDefect_prod_of_pairwise_disjoint :
    ∀ (l : List (Perm α)), l.Pairwise Disjoint →
      orbitDefect l.prod = (l.map orbitDefect).sum
  | [], _ => by simpa using orbitDefect_one
  | σ :: l, hl => by
    have hd : Disjoint σ l.prod :=
      disjoint_prod_right _ (fun τ hτ => (List.pairwise_cons.mp hl).1 τ hτ)
    rw [List.prod_cons, orbitDefect_mul_of_disjoint hd,
      orbitDefect_prod_of_pairwise_disjoint l (List.pairwise_cons.mp hl).2]
    simp

/-- The orbit count of a disjoint product, in the form the free braid word has:
`A` pairwise-disjoint blocks of defect one leave `card α − A` orbits.

This is the **free-word half of `ClassicalTraceFloor`'s hypotheses, provable now**:
the free word is a disjoint product of one identical block per nucleon, each block
acting on that nucleon's own three strands with defect `1` (two orbits on three
points). With `card α = 3A` it gives `c(σ_free) = 3A − A = 2A`, which is the count
that file assumes.

The block's own defect enters as a hypothesis rather than being computed, exactly as
`ClassicalTraceFloor` takes its counts — but it is now a statement about **one
concrete permutation of three points**, decidable in principle, instead of a claim
about the whole word at every `A`. -/
theorem orbitCount_prod_of_disjoint_unit_defect (l : List (Perm α))
    (hpair : l.Pairwise Disjoint) (hone : ∀ σ ∈ l, orbitDefect σ = 1)
    (hle : l.length ≤ Fintype.card α) :
    orbitCount l.prod = Fintype.card α - l.length := by
  have hsum : (l.map orbitDefect).sum = l.length := by
    induction l with
    | nil => simp
    | cons σ t ih =>
        rw [List.map_cons, List.sum_cons, hone σ (List.mem_cons_self ..),
          ih (List.pairwise_cons.mp hpair).2
            (fun τ hτ => hone τ (List.mem_cons_of_mem _ hτ))
            (by simp at hle ⊢; omega)]
        simp [Nat.add_comm]
  rw [orbitCount, orbitDefect_prod_of_pairwise_disjoint l hpair, hsum]

/-- **The parity of the defect is the sign.** `sign σ = (−1)^{orbitDefect σ}`, since
`sum + card ≡ sum − card (mod 2)` and Mathlib gives the sign as `(−1)^{sum + card}`. -/
theorem sign_eq_neg_one_pow_orbitDefect (σ : Perm α) :
    sign σ = (-1 : ℤˣ) ^ orbitDefect σ := by
  rw [sign_of_cycleType]
  have hsum : σ.cycleType.sum = #σ.support := sum_cycleType σ
  have hle := card_cycleType_le_card_support σ
  have hpar : σ.cycleType.sum + Multiset.card σ.cycleType
      = orbitDefect σ + 2 * Multiset.card σ.cycleType := by
    simp only [orbitDefect, hsum]; omega
  rw [hpar, pow_add, pow_mul]
  simp

/-- **Half of the ±1 step, free.** Multiplying by a transposition flips the defect's
parity — so the change is odd, hence nonzero, and in particular `swap a b * σ ≠ σ`
in defect. What this does NOT give is that the change is exactly one. -/
theorem orbitDefect_swap_mul_odd {σ : Perm α} {a b : α} (h : a ≠ b) :
    ¬ (orbitDefect (swap a b * σ) % 2 = orbitDefect σ % 2) := by
  intro hcon
  have hs : sign (swap a b * σ) = - sign σ := by
    rw [map_mul, sign_swap h]; simp
  rw [sign_eq_neg_one_pow_orbitDefect, sign_eq_neg_one_pow_orbitDefect] at hs
  rcases Nat.even_or_odd (orbitDefect σ) with he | ho
  · have he' : Even (orbitDefect (swap a b * σ)) := by
      rw [Nat.even_iff] at he ⊢; omega
    rw [he.neg_one_pow, he'.neg_one_pow] at hs
    exact (by decide : (1 : ℤˣ) ≠ -1) hs
  · have ho' : Odd (orbitDefect (swap a b * σ)) := by
      rw [Nat.odd_iff] at ho ⊢; omega
    rw [ho.neg_one_pow, ho'.neg_one_pow] at hs
    exact (by decide : (-1 : ℤˣ) ≠ 1) hs

/-! ### The transposition step: what remains, and how far it reduces

`orbitDefect_swap_mul_odd` gives the **parity** of the step. The **magnitude**
`|Δ| ≤ 1` is the gap, and it splits into exactly two pieces, both smaller than the
statement they replace:

* **(S) the split**, `orbitDefect_swap_mul_of_sameCycle` — within one cycle, the
  transposition splits it and the defect drops. This is the direction Mathlib comes
  closest to: `Equiv.Perm.IsCycle.swap_mul` already proves that removing a point
  from a cycle leaves a cycle.
* **(R) reachability**, `sameCycle_swap_mul_of_not_sameCycle` — joining two
  *different* cycles puts `a` and `b` in the *same* cycle of the product. Elementary,
  and the argument is short: iterating `swap a b * σ` from `b` follows `σ`'s cycle
  (`τ x = σ x` whenever `σ x ∉ {a, b}`) until it reaches `b`'s predecessor `x` with
  `σ x = b`, where `τ x = swap a b b = a`. So `a` is reached from `b`.

**The merge case is then derived, not assumed** — `orbitDefect_swap_mul_of_not_sameCycle`
below is *proved* from (S) and (R), because `swap a b` is an involution: applying (S)
to `swap a b * σ`, whose `a` and `b` are in one cycle by (R), and using
`swap a b * (swap a b * σ) = σ`, gives the merge statement directly.

Both (S) and (R) carry `sorry` with `-- Ref:` as the honest "stated, not yet proved"
marker per the repo's Lean discipline — NOT axiomatised, NOT weakened to something
provable, and consumed by nothing outside this section.
-/

/-- **(R)** Joining two different cycles with a transposition puts the two points in
one cycle of the product.

Elementary: iterating `τ = swap a b * σ` from `b` agrees with `σ` (since
`τ x = σ x` whenever `σ x ∉ {a, b}`) until it reaches the `σ`-predecessor `x` of `b`,
where `τ x = swap a b b = a`. Formalising it needs induction along `b`'s `σ`-cycle
with `σ^j b ∉ {a, b}` for `0 < j < k`. -/
theorem sameCycle_swap_mul_of_not_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hnc : ¬ σ.SameCycle a b) :
    (swap a b * σ).SameCycle a b := by
  -- Ref: [manuscript] bean qou-zrx2 follow-up (5), piece (R).
  sorry

/-- **(S)** Within one cycle, the transposition splits it and the defect drops.
The direction Mathlib comes closest to (`Equiv.Perm.IsCycle.swap_mul`). -/
theorem orbitDefect_swap_mul_of_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hc : σ.SameCycle a b) :
    orbitDefect (swap a b * σ) + 1 = orbitDefect σ := by
  -- Ref: [manuscript] bean qou-zrx2 follow-up (5), piece (S).
  sorry

/-- **The merge case, DERIVED from (S) and (R).** When `a` and `b` lie in different
cycles of `σ`, those two orbits merge and the defect rises by exactly one.

No `sorry` of its own: `swap a b` is an involution, so `swap a b * σ` has `a` and `b`
in one cycle by (R), and applying (S) to it returns `σ`. This is why the two pieces
above are the whole remaining gap. -/
theorem orbitDefect_swap_mul_of_not_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hnc : ¬ σ.SameCycle a b) :
    orbitDefect (swap a b * σ) = orbitDefect σ + 1 := by
  have hsc : (swap a b * σ).SameCycle a b := sameCycle_swap_mul_of_not_sameCycle h hnc
  have hinv : swap a b * (swap a b * σ) = σ := by
    rw [← mul_assoc, swap_mul_self, one_mul]
  have hs := orbitDefect_swap_mul_of_sameCycle (σ := swap a b * σ) h hsc
  rw [hinv] at hs
  omega

end QOU.MassTheory
