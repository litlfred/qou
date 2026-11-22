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
  multiplying by any transposition flips it: `orbitDefect_swap_mul_odd`.
* `sameCycle_swap_mul_iff` — a transposition exactly toggles whether two points share
  a cycle.
* **The transposition step itself, both directions, sorry-free**:
  `orbitDefect_swap_mul_of_sameCycle` (split: the defect drops by exactly one) and
  `orbitDefect_swap_mul_of_not_sameCycle` (merge: it rises by exactly one).

## The transposition step, and how it is proved

Multiplying by a transposition changes the orbit count by **exactly one** — up when
the two points lay in different cycles, down when they lay in the same one. The
*parity* comes free from the sign (`orbitDefect_swap_mul_odd`); the **magnitude** is
the content, and Mathlib supplies none of it — there is no `cycleType_swap_mul` lemma
in the library at all. It is proved here from one base case, reached twice per
induction step.

* **(S-adj)** `orbitDefect_swap_apply_mul` — the **adjacent** case `b = f a`. Split
  `f = cycleOf f a * (f * (cycleOf f a)⁻¹)` into disjoint halves
  (`disjoint_mul_inv_of_mem_cycleFactorsFinset`); the transposition cannot leave the
  first, so `orbitDefect_mul_of_disjoint` reduces to a single cycle, where Mathlib's
  `IsCycle.swap_mul` and `support_swap_mul_eq` give a cycle on one fewer point — or,
  when the cycle *is* that transposition, the identity.
* **(S)** `orbitDefect_swap_mul_of_sameCycle` — the general case. `b = σ^k a` for a
  least `k ≥ 1`, and `orbitDefect_swap_mul_aux` walks that arc down to `k = 1`: each
  step peels the first letter off the front of the arc with (S-adj) and puts it back
  at the far end with (S-adj) again, glued by the three-cycle identity
  `swap (σa) b · swap a (σa) = swap a (σa) · swap a b`.
* **(R)** `sameCycle_swap_mul_of_not_sameCycle` and **(R2)**
  `not_sameCycle_swap_mul_of_sameCycle` — the dynamics: a transposition **toggles**
  whether `a` and `b` share a cycle (`sameCycle_swap_mul_iff`). Both are the same walk
  along `σ`'s orbit of `a`; (R) needs no `a ≠ b` at all.
* The **merge** is *derived* from (S) and (R) rather than proved again, since
  `swap a b` is an involution.

## 🛑 What this does and does not settle for `ClassicalTraceFloor`

It closes the **free** half outright (`orbitCount_prod_of_disjoint_unit_defect`), and
it supplies the general step the **atom** half needs. It does **not** by itself
discharge that file's stated counts: knowing that each letter moves the count by ±1
leaves the bookkeeping of *which* sign each letter of the canonical word carries —
i.e. whether that letter's two strands already lay in one orbit. That is a statement
about the specific word, not about permutations in general, and it is not in this
file.

So the general cycle-count gap those two files name is closed; the word-specific
accounting is not. **Do not cite this file as verifying `c(σ_atom) = A + 1`.**

-- Ref: [leitner2026] bean qou-zrx2 follow-up (5); the transposition/cycle-count
-- step is the classical fact underlying well-definedness of the sign of a
-- permutation, standard in any treatment of symmetric groups.
-/

namespace QOU.MassTheory

open Equiv Equiv.Perm Finset

/-- If `x` returns to itself after `k` steps, every multiple of `k` fixes it. -/
private theorem pow_mul_eq_self {α : Type*} {f : Perm α} {x : α} {k : ℕ}
    (hk : (f ^ k) x = x) : ∀ q, ((f ^ k) ^ q) x = x
  | 0 => by simp
  | q + 1 => by rw [pow_succ, Perm.mul_apply, hk, pow_mul_eq_self hk q]

/-- …so iterating from `x` is periodic mod `k`. -/
private theorem pow_eq_pow_mod {α : Type*} {f : Perm α} {x : α} {k : ℕ}
    (hk : (f ^ k) x = x) (i : ℕ) : (f ^ i) x = (f ^ (i % k)) x := by
  conv_lhs => rw [← Nat.mod_add_div i k]
  rw [pow_add, Perm.mul_apply, pow_mul, pow_mul_eq_self hk]

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

/-! ### The transposition step

`orbitDefect_swap_mul_odd` above gives the **parity** of the step. The **magnitude**
`|Δ| = 1` is the content, and it comes in two halves:

* **(S) the split**, `orbitDefect_swap_mul_of_sameCycle` — within one cycle, the
  transposition splits it and the defect drops. Proved below via the adjacent case
  `orbitDefect_swap_apply_mul`, which is where `Equiv.Perm.IsCycle.swap_mul` (removing
  a point from a cycle leaves a cycle) does the work.
* **(R) reachability**, `sameCycle_swap_mul_of_not_sameCycle` — joining two
  *different* cycles puts `a` and `b` in the *same* cycle of the product. Elementary,
  and the argument is short: iterating `swap a b * σ` from `b` follows `σ`'s cycle
  (`τ x = σ x` whenever `σ x ∉ {a, b}`) until it reaches `b`'s predecessor `x` with
  `σ x = b`, where `τ x = swap a b b = a`. So `a` is reached from `b`.

**The merge case is derived, not assumed** — `orbitDefect_swap_mul_of_not_sameCycle`
below is *proved* from (S) and (R), because `swap a b` is an involution: applying (S)
to `swap a b * σ`, whose `a` and `b` are in one cycle by (R), and using
`swap a b * (swap a b * σ) = σ`, gives the merge statement directly.

Everything in this section is sorry-free.
-/

/-- **(R)** Joining two different cycles with a transposition puts the two points in
one cycle of the product. **Proved.**

Iterating `τ = swap a b * σ` from `a` agrees with `σ` (because `τ x = σ x` whenever
`σ x ∉ {a, b}`) all the way to the first return `σ^m a = a`, where the swap finally
fires and sends `a` to `b`. Nothing on `a`'s orbit is `b`, or `a` and `b` would
already share a cycle; and nothing before step `m` is `a`, by minimality.

Note it needs no `a ≠ b`: at `a = b` the hypothesis is already false, `SameCycle`
being reflexive. -/
theorem sameCycle_swap_mul_of_not_sameCycle {σ : Perm α} {a b : α}
    (hnc : ¬ σ.SameCycle a b) :
    (swap a b * σ).SameCycle a b := by
  classical
  -- `a` returns to itself under some positive power; take the least such `m`.
  have hex : ∃ m, 0 < m ∧ (σ ^ m) a = a := by
    refine ⟨orderOf σ, orderOf_pos σ, ?_⟩
    rw [pow_orderOf_eq_one]; rfl
  obtain ⟨hmpos, hma⟩ := Nat.find_spec hex
  set m := Nat.find hex with hmdef
  -- nothing on `a`'s forward orbit is `b`, or `a` and `b` would share a cycle
  have hne_b : ∀ k : ℕ, (σ ^ k) a ≠ b := fun k hk =>
    hnc ⟨(k : ℤ), by rw [zpow_natCast]; exact hk⟩
  -- before the first return, `swap a b * σ` cannot tell itself from `σ`
  have key : ∀ k, k < m → ((swap a b * σ) ^ k) a = (σ ^ k) a := by
    intro k
    induction k with
    | zero => intro _; simp
    | succ n ih =>
        intro hn
        have hn' : n < m := Nat.lt_of_succ_lt hn
        have hne_a : (σ ^ (n + 1)) a ≠ a := by
          intro hcon
          exact absurd ⟨Nat.succ_pos n, hcon⟩ (Nat.find_min hex hn)
        have hcomp : (σ ^ (n + 1)) a = σ ((σ ^ n) a) := by
          rw [pow_succ', Perm.mul_apply]
        rw [pow_succ', Perm.mul_apply, ih hn', Perm.mul_apply, ← hcomp]
        exact swap_apply_of_ne_of_ne hne_a (hne_b (n + 1))
  -- at the return step the swap fires, and sends `a` to `b`
  refine ⟨(m : ℤ), ?_⟩
  rw [zpow_natCast]
  obtain ⟨n, hn⟩ : ∃ n, m = n + 1 := ⟨m - 1, by omega⟩
  have hcomp : (σ ^ (n + 1)) a = σ ((σ ^ n) a) := by
    rw [pow_succ', Perm.mul_apply]
  have hma' : (σ ^ (n + 1)) a = a := by rw [← hn]; exact hma
  rw [hn, pow_succ', Perm.mul_apply, key n (by omega), Perm.mul_apply, ← hcomp,
    hma', swap_apply_left]

/-- **(R2)** The converse of (R), and the *separation* half of the split: if `a` and
`b` already share a cycle, the transposition puts them in **different** cycles of the
product. **Proved**, by the same walk.

Take `k` least positive with `σ^k a ∈ {a, b}`. If `σ^k a = a` then `b` never appears
on `a`'s orbit, contradicting the hypothesis; so `σ^k a = b`, and then `τ = swap a b * σ`
follows `σ` up to step `k−1` and closes back to `a` at step `k` — `τ^k a = a`, with the
whole `τ`-orbit of `a` sitting inside `{σ^j a : j < k}`, which avoids `b`.

This is the arc-separation fact any counting proof of (S) needs. -/
theorem not_sameCycle_swap_mul_of_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hc : σ.SameCycle a b) :
    ¬ (swap a b * σ).SameCycle a b := by
  classical
  have hex : ∃ k, 0 < k ∧ ((σ ^ k) a = a ∨ (σ ^ k) a = b) := by
    refine ⟨orderOf σ, orderOf_pos σ, Or.inl ?_⟩
    rw [pow_orderOf_eq_one]; rfl
  obtain ⟨hkpos, hk⟩ := Nat.find_spec hex
  set k := Nat.find hex with hkdef
  have hmin : ∀ j, 0 < j → j < k → (σ ^ j) a ≠ a ∧ (σ ^ j) a ≠ b := by
    intro j hj hjk
    have hnf := Nat.find_min hex hjk
    push_neg at hnf
    exact hnf hj
  -- on `a`'s orbit, only step `k` can reach `a` or `b`
  have horb : ∀ j, j < k → (σ ^ j) a ≠ b := by
    intro j hjk
    rcases Nat.eq_zero_or_pos j with rfl | hj
    · simpa using h
    · exact (hmin j hj hjk).2
  rcases hk with hka | hkb
  · -- `a` returns before meeting `b`, so they never shared a cycle: contradiction
    exfalso
    obtain ⟨i, _, hi⟩ := hc.exists_pow_eq'
    exact horb (i % k) (Nat.mod_lt _ hkpos) ((pow_eq_pow_mod hka i).symm.trans hi)
  · -- `τ` follows `σ` to step `k−1`, then closes back to `a`
    have key : ∀ j, j < k → ((swap a b * σ) ^ j) a = (σ ^ j) a := by
      intro j
      induction j with
      | zero => intro _; simp
      | succ n ih =>
          intro hn
          have hn' : n < k := Nat.lt_of_succ_lt hn
          have hcomp : (σ ^ (n + 1)) a = σ ((σ ^ n) a) := by
            rw [pow_succ', Perm.mul_apply]
          rw [pow_succ', Perm.mul_apply, ih hn', Perm.mul_apply, ← hcomp]
          exact swap_apply_of_ne_of_ne (hmin _ (Nat.succ_pos n) hn).1
            (hmin _ (Nat.succ_pos n) hn).2
    have hclose : ((swap a b * σ) ^ k) a = a := by
      obtain ⟨n, hn⟩ : ∃ n, k = n + 1 := ⟨k - 1, by omega⟩
      have hcomp : (σ ^ (n + 1)) a = σ ((σ ^ n) a) := by
        rw [pow_succ', Perm.mul_apply]
      have hkb' : (σ ^ (n + 1)) a = b := by rw [← hn]; exact hkb
      rw [hn, pow_succ', Perm.mul_apply, key n (by omega), Perm.mul_apply, ← hcomp,
        hkb', swap_apply_right]
    intro hsc
    obtain ⟨j, _, hj⟩ := hsc.exists_pow_eq'
    have : ((swap a b * σ) ^ (j % k)) a = b :=
      (pow_eq_pow_mod hclose j).symm.trans hj
    rw [key _ (Nat.mod_lt _ hkpos)] at this
    exact horb (j % k) (Nat.mod_lt _ hkpos) this

/-- **(R) and (R2) together: a transposition exactly toggles whether the two points
share a cycle.** The complete dynamical picture at `{a, b}`, and all the dynamical
input a counting proof of (S) needs — what remains there is the counting itself. -/
theorem sameCycle_swap_mul_iff {σ : Perm α} {a b : α} (h : a ≠ b) :
    (swap a b * σ).SameCycle a b ↔ ¬ σ.SameCycle a b :=
  ⟨fun hτ hσ => not_sameCycle_swap_mul_of_sameCycle h hσ hτ,
   sameCycle_swap_mul_of_not_sameCycle⟩

/-! ### (S-adj): the adjacent case, and the arc induction that reduces (S) to it -/

/-- **(S-adj) for a single cycle.** Removing a cycle's start point drops its defect by
one: `swap x (c x) * c` is the identity when `c` is the transposition `(x, c x)`, and
otherwise is a cycle on `support c \ {x}` — Mathlib's `IsCycle.swap_mul` and
`support_swap_mul_eq`. -/
private theorem orbitDefect_swap_apply_mul_isCycle {c : Perm α} (hc : c.IsCycle) {x : α}
    (hx : c x ≠ x) :
    orbitDefect (swap x (c x) * c) + 1 = orbitDefect c := by
  have hdef : orbitDefect c = #c.support - 1 := by simp [orbitDefect, hc.cycleType]
  have h2 : 2 ≤ #c.support := hc.two_le_card_support
  by_cases hcc : c (c x) = x
  · -- `c` IS the transposition, so the product is the identity and `#support c = 2`
    have hswap : c = swap x (c x) := hc.eq_swap_of_apply_apply_eq_self hx hcc
    have key : ∀ (d : Perm α) (z : α), d = swap x z → swap x z * d = 1 := by
      rintro d z rfl; exact swap_mul_self x z
    have hone : swap x (c x) * c = 1 := key c (c x) hswap
    have hsupp2 : #c.support = 2 := by
      rw [hswap]; exact card_support_swap (Ne.symm hx)
    rw [hone, orbitDefect_one, hdef, hsupp2]
  · -- the product is a cycle on one fewer point
    have hcyc : IsCycle (swap x (c x) * c) := hc.swap_mul hx hcc
    have hxmem : x ∈ c.support := mem_support.mpr hx
    have hcard : #(swap x (c x) * c).support = #c.support - 1 := by
      rw [support_swap_mul_eq c x hcc, card_sdiff,
        Finset.singleton_inter_of_mem hxmem, card_singleton]
    have hdef2 : orbitDefect (swap x (c x) * c) = #c.support - 1 - 1 := by
      unfold orbitDefect
      rw [hcyc.cycleType, hcard]
      simp
    have h3 : 2 ≤ #(swap x (c x) * c).support := hcyc.two_le_card_support
    rw [hcard] at h3
    omega

/-- **(S-adj)** Multiplying by the transposition of `x` with its own image `f x` removes
`x` from its cycle, dropping the defect by exactly one.

Reduces to the single-cycle case by splitting `f = cycleOf f x * (f * (cycleOf f x)⁻¹)`
into disjoint halves (`disjoint_mul_inv_of_mem_cycleFactorsFinset`) — the transposition
touches only the first — and applying `orbitDefect_mul_of_disjoint`. -/
theorem orbitDefect_swap_apply_mul {f : Perm α} {x : α} (hf : f x ≠ x) :
    orbitDefect (swap x (f x) * f) + 1 = orbitDefect f := by
  have hxs : x ∈ f.support := mem_support.mpr hf
  have hcx : f.cycleOf x x = f x := cycleOf_apply_self f x
  have hcxne : f.cycleOf x x ≠ x := by rw [hcx]; exact hf
  have hciscyc : (f.cycleOf x).IsCycle := isCycle_cycleOf f hf
  have hdisj : Disjoint (f.cycleOf x) (f * (f.cycleOf x)⁻¹) :=
    (disjoint_mul_inv_of_mem_cycleFactorsFinset
      (cycleOf_mem_cycleFactorsFinset_iff.mpr hxs)).symm
  have hfeq : f.cycleOf x * (f * (f.cycleOf x)⁻¹) = f := by
    rw [hdisj.commute.eq, mul_assoc, inv_mul_cancel, mul_one]
  -- the transposition cannot leave `x`'s own cycle
  have hsub : (swap x (f.cycleOf x x) * f.cycleOf x).support ⊆ (f.cycleOf x).support := by
    intro y hy
    by_contra hnot
    have hcy : f.cycleOf x y = y := notMem_support.mp hnot
    have hyx : y ≠ x := by rintro rfl; exact hcxne hcy
    have hycx : y ≠ f.cycleOf x x := by
      rintro rfl; exact hcxne ((f.cycleOf x).injective hcy)
    exact (mem_support.mp hy)
      (by rw [Perm.mul_apply, hcy, swap_apply_of_ne_of_ne hyx hycx])
  have hdisj2 : Disjoint (swap x (f.cycleOf x x) * f.cycleOf x) (f * (f.cycleOf x)⁻¹) :=
    disjoint_iff_disjoint_support.mpr
      (Finset.disjoint_of_subset_left hsub (disjoint_iff_disjoint_support.mp hdisj))
  have hsplit : (swap x (f.cycleOf x x) * f.cycleOf x) * (f * (f.cycleOf x)⁻¹)
      = swap x (f x) * f := by
    rw [mul_assoc, hfeq, hcx]
  have h1 : orbitDefect (swap x (f x) * f)
      = orbitDefect (swap x (f.cycleOf x x) * f.cycleOf x)
        + orbitDefect (f * (f.cycleOf x)⁻¹) := by
    rw [← hsplit, orbitDefect_mul_of_disjoint hdisj2]
  have h2 : orbitDefect f
      = orbitDefect (f.cycleOf x) + orbitDefect (f * (f.cycleOf x)⁻¹) := by
    conv_lhs => rw [← hfeq]
    rw [orbitDefect_mul_of_disjoint hdisj]
  have h3 := orbitDefect_swap_apply_mul_isCycle hciscyc hcxne
  omega

/-- **The arc induction.** `b = σ^{k+1} a` with `k+1` least, so `a … b` is an arc of
`a`'s cycle with no early return. Each step peels the first letter of the arc off the
front with `(S-adj)` and puts it back at the other end with `(S-adj)` again, via the
three-cycle identity `swap (σa) b · swap a (σa) = swap a (σa) · swap a b`. -/
private theorem orbitDefect_swap_mul_aux :
    ∀ (k : ℕ) (σ : Perm α) (a b : α), a ≠ b → (σ ^ (k + 1)) a = b →
      (∀ j, 0 < j → j < k + 1 → (σ ^ j) a ≠ b) →
      orbitDefect (swap a b * σ) + 1 = orbitDefect σ := by
  intro k
  induction k with
  | zero =>
      -- `b = σ a`: this IS the adjacent case
      intro σ a b hab hb _
      have hsa : σ a = b := by simpa using hb
      have h := orbitDefect_swap_apply_mul (f := σ) (x := a)
        (by rw [hsa]; exact Ne.symm hab)
      rwa [hsa] at h
  | succ n ih =>
      intro σ a b hab hb hmin
      -- minimality of the arc forbids an early return to `a` as well as to `b`
      have hne_a : ∀ j, 0 < j → j < n + 2 → (σ ^ j) a ≠ a := by
        intro j hj hjk hja
        have hmod := pow_eq_pow_mod hja (n + 2)
        rcases Nat.eq_zero_or_pos ((n + 2) % j) with h0 | hpos
        · rw [h0, pow_zero] at hmod
          simp only [Perm.coe_one, id_eq] at hmod
          exact hab (hmod.symm.trans hb)
        · exact hmin _ hpos (lt_trans (Nat.mod_lt _ hj) hjk) (by rw [← hmod]; exact hb)
      have hca : σ a ≠ a := by
        have := hne_a 1 one_pos (by omega); rwa [pow_one] at this
      have hcb : σ a ≠ b := by
        have := hmin 1 one_pos (by omega); rwa [pow_one] at this
      -- peel the first letter: `ρ = swap a (σ a) * σ` drops the defect by one
      have hρ : orbitDefect (swap a (σ a) * σ) + 1 = orbitDefect σ :=
        orbitDefect_swap_apply_mul hca
      -- and `ρ` traces the rest of the arc exactly as `σ` did
      have hpow : ∀ j, j ≤ n + 1 → ((swap a (σ a) * σ) ^ j) (σ a) = (σ ^ (j + 1)) a := by
        intro j
        induction j with
        | zero => intro _; simp
        | succ m ihm =>
            intro hm
            have hstep : (σ ^ (m + 2)) a = σ ((σ ^ (m + 1)) a) := by
              rw [pow_succ', Perm.mul_apply]
            have hne1 : (σ ^ (m + 2)) a ≠ a := by
              rcases eq_or_lt_of_le hm with h | h
              · rw [show m + 2 = n + 2 by omega, hb]; exact Ne.symm hab
              · exact hne_a (m + 2) (by omega) (by omega)
            have hne2 : (σ ^ (m + 2)) a ≠ σ a := by
              intro hcon
              exact hne_a (m + 1) (by omega) (by omega)
                (σ.injective (by rw [← hstep, hcon]))
            rw [pow_succ', Perm.mul_apply, ihm (by omega), Perm.mul_apply, ← hstep]
            exact swap_apply_of_ne_of_ne hne1 hne2
      have hIH := ih (swap a (σ a) * σ) (σ a) b hcb
        (by rw [hpow (n + 1) le_rfl]; exact hb)
        (fun j hj hjn => by rw [hpow j (by omega)]; exact hmin (j + 1) (by omega) (by omega))
      -- the three-cycle identity `(a b σa)`, written two ways
      have hswapid : swap (σ a) b * swap a (σ a) = swap a (σ a) * swap a b := by
        have hba : b ≠ a := Ne.symm hab
        have hac : a ≠ σ a := Ne.symm hca
        have hbc : b ≠ σ a := Ne.symm hcb
        ext y
        simp only [Perm.mul_apply]
        by_cases h1 : y = a
        · subst h1
          rw [swap_apply_left, swap_apply_left, swap_apply_left,
            swap_apply_of_ne_of_ne hba hbc]
        by_cases h2 : y = b
        · subst h2
          rw [swap_apply_of_ne_of_ne hba hbc, swap_apply_right, swap_apply_right,
            swap_apply_left]
        by_cases h3 : y = σ a
        · subst h3
          rw [swap_apply_right, swap_apply_of_ne_of_ne hac hab,
            swap_apply_of_ne_of_ne hca hcb, swap_apply_right]
        · rw [swap_apply_of_ne_of_ne h1 h3, swap_apply_of_ne_of_ne h3 h2,
            swap_apply_of_ne_of_ne h1 h2, swap_apply_of_ne_of_ne h1 h3]
      have hψ : swap a (σ a) * (swap a b * σ) = swap (σ a) b * (swap a (σ a) * σ) := by
        rw [← mul_assoc, ← hswapid, mul_assoc]
      -- `(swap a b * σ) a = σ a`, so (S-adj) applies to it at `a` and puts the letter back
      have hτa : (swap a b * σ) a = σ a := by
        rw [Perm.mul_apply, swap_apply_of_ne_of_ne hca hcb]
      have hτ : orbitDefect (swap a (σ a) * (swap a b * σ)) + 1
          = orbitDefect (swap a b * σ) := by
        have h := orbitDefect_swap_apply_mul (f := swap a b * σ) (x := a)
          (by rw [hτa]; exact hca)
        rwa [hτa] at h
      rw [hψ] at hτ
      omega

/-- **(S)** Within one cycle, the transposition splits it and the defect drops by
exactly one. **Proved.**

`a` and `b` lie on one cycle, so `b = σ^k a` for a least `k ≥ 1`; the arc induction
`orbitDefect_swap_mul_aux` walks that arc down to the adjacent case `k = 1`, which is
`orbitDefect_swap_apply_mul`. -/
theorem orbitDefect_swap_mul_of_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hc : σ.SameCycle a b) :
    orbitDefect (swap a b * σ) + 1 = orbitDefect σ := by
  classical
  have hex : ∃ k, 0 < k ∧ (σ ^ k) a = b := by
    obtain ⟨i, _, hi⟩ := hc.exists_pow_eq'
    refine ⟨i, ?_, hi⟩
    rcases Nat.eq_zero_or_pos i with rfl | hp
    · simp only [pow_zero, Perm.coe_one, id_eq] at hi
      exact absurd hi h
    · exact hp
  obtain ⟨hkpos, hk⟩ := Nat.find_spec hex
  have hmin : ∀ j, j < Nat.find hex → ¬ (0 < j ∧ (σ ^ j) a = b) :=
    fun j hj => Nat.find_min hex hj
  obtain ⟨m, hm⟩ : ∃ m, Nat.find hex = m + 1 := ⟨Nat.find hex - 1, by omega⟩
  rw [hm] at hk hmin
  exact orbitDefect_swap_mul_aux m σ a b h hk
    (fun j hj hjm hjb => hmin j hjm ⟨hj, hjb⟩)

/-- **The merge case, DERIVED from (S) and (R).** When `a` and `b` lie in different
cycles of `σ`, those two orbits merge and the defect rises by exactly one.

`swap a b` is an involution, so `swap a b * σ` has `a` and `b` in one cycle by (R),
and applying (S) to it returns `σ`. Nothing new is proved here. -/
theorem orbitDefect_swap_mul_of_not_sameCycle {σ : Perm α} {a b : α} (h : a ≠ b)
    (hnc : ¬ σ.SameCycle a b) :
    orbitDefect (swap a b * σ) = orbitDefect σ + 1 := by
  have hsc : (swap a b * σ).SameCycle a b := sameCycle_swap_mul_of_not_sameCycle hnc
  have hinv : swap a b * (swap a b * σ) = σ := by
    rw [← mul_assoc, swap_mul_self, one_mul]
  have hs := orbitDefect_swap_mul_of_sameCycle (σ := swap a b * σ) h hsc
  rw [hinv] at hs
  omega

end QOU.MassTheory
