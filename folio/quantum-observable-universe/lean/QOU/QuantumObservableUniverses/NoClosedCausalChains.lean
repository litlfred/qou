import Mathlib.Logic.Relation
import Mathlib.Order.WellFounded
import QOU.MathlibExt.BraidGroup
import Mathlib.GroupTheory.Perm.Sign

/-!
# No closed chains under a well-founded precedence relation

Pure order theory, used by `rem:no-goedel-closed-chains`.

Let `r` be any relation on a type `α`, read as "immediately precedes".
A *closed chain* through `p` is a finite `r`-chain from `p` back to `p`,
i.e. `Relation.TransGen r p p`. *Total chronology* means every point
reaches every point (itself included) by a finite chain; this is the
order-theoretic shape of Gödel's rotating universe, where the
chronological future of every event is the whole spacetime.

If `r` is well-founded, then:

* `not_closedChainAt_of_wellFounded`: no point lies on a closed chain;
* `not_totalChronology_of_wellFounded`: on a nonempty type, total
  chronology fails.

Nothing here uses a braiding, a metric or any physical input. The
application to `≺_c` is in the content file
`quantum-observable-universes/braiding-induced-ordering.lean`
(`QOU.degLex_no_closedChain`).
-/

namespace QOU.Chronology

variable {α : Type*}

/-- A closed `r`-chain through `p`: a finite chain `p r … r p`. -/
def ClosedChainAt (r : α → α → Prop) (p : α) : Prop :=
  Relation.TransGen r p p

/-- Total chronology: every point reaches every point by a finite `r`-chain.
This is the order-theoretic content of `I⁺(p) = M` for all `p`. -/
def TotalChronology (r : α → α → Prop) : Prop :=
  ∀ p q : α, Relation.TransGen r p q

/-- A well-founded relation has no closed chains. -/
theorem not_closedChainAt_of_wellFounded {r : α → α → Prop}
    (hwf : WellFounded r) (p : α) : ¬ ClosedChainAt r p := by
  have h' : WellFounded (Relation.TransGen r) := hwf.transGen
  exact h'.induction (C := fun x => ¬ Relation.TransGen r x x) p
    (fun x ih hx => ih x hx hx)

/-- A well-founded relation on a nonempty type is not totally chronological. -/
theorem not_totalChronology_of_wellFounded {r : α → α → Prop} [Nonempty α]
    (hwf : WellFounded r) : ¬ TotalChronology r := fun h =>
  not_closedChainAt_of_wellFounded hwf (Classical.arbitrary α) (h _ _)

/-! ## Crossing-application order on states

Time order is defined, not identified: one tick is one application of a
crossing (`rem:no-goedel-closed-chains`, following
`prf:braiding-induced-ordering`, "one application of `c` advances one
tick"). On a monoid `G` of states with crossing elements `s i`, the tick
relation is `h = g * s i`, and chronological precedence is its transitive
closure.

* `tick_transGen_degree`: a homomorphism `χ : G →* Multiplicative ℤ` with
  `χ (s i) = ofAdd 1` strictly increases along every chain.
* `not_closedChainAt_tick`: hence no closed chains.
* `braid_no_closedChainAt`: for the braid group with Artin generators, the
  writhe `exponentSum` is such a `χ`, so the braid group has no closed chains.
* `closedChainAt_of_pow_eq_one`: if some crossing has finite order
  (`s i ^ (k+1) = 1`), every state lies on a closed chain. A symmetric
  braiding (`c² = id`) is the case `k = 1`: `closedChainAt_of_sq_eq_one`.

A degree `χ` is a sufficient obstruction to closed chains, and a crossing
of finite order is a sufficient cause. A symmetric braiding (`c² = id`) is
one such cause; it is not the only one (a crossing of order `≥ 3`, e.g. a
Hecke generator at a root of unity `q ≠ -1`, also has finite order), and the
two conditions need not cover every state monoid. On words (`DegLex`),
closed chains are absent for every braiding. -/

section Ticks

variable {G : Type*} [Monoid G] {ι : Type*}

/-- One tick: apply one crossing `s i` to the state `g`. -/
def Tick (s : ι → G) (g h : G) : Prop := ∃ i, h = g * s i

/-- A degree `χ` with every crossing of degree one strictly increases along
every chain of ticks. -/
theorem tick_transGen_degree (s : ι → G) {χ : G →* Multiplicative ℤ}
    (hχ : ∀ i, χ (s i) = Multiplicative.ofAdd (1 : ℤ)) {g h : G}
    (H : Relation.TransGen (Tick s) g h) :
    Multiplicative.toAdd (χ g) < Multiplicative.toAdd (χ h) := by
  induction H with
  | single hab =>
      obtain ⟨i, rfl⟩ := hab
      rw [map_mul, hχ, toAdd_mul, toAdd_ofAdd]
      omega
  | tail _ hbc ih =>
      obtain ⟨i, rfl⟩ := hbc
      rw [map_mul, hχ, toAdd_mul, toAdd_ofAdd]
      omega

/-- With such a degree, no state lies on a closed chain of ticks. -/
theorem not_closedChainAt_tick (s : ι → G) {χ : G →* Multiplicative ℤ}
    (hχ : ∀ i, χ (s i) = Multiplicative.ofAdd (1 : ℤ)) (g : G) :
    ¬ ClosedChainAt (Tick s) g := fun H =>
  lt_irrefl _ (tick_transGen_degree s hχ H)

/-- `k + 1` ticks by the same crossing reach `g * s i ^ (k + 1)`. -/
theorem tick_transGen_pow (s : ι → G) (i : ι) (g : G) (k : ℕ) :
    Relation.TransGen (Tick s) g (g * s i ^ (k + 1)) := by
  induction k with
  | zero => exact Relation.TransGen.single ⟨i, by rw [zero_add, pow_one]⟩
  | succ k ih =>
      exact Relation.TransGen.tail ih ⟨i, by rw [pow_succ (s i) (k + 1), mul_assoc]⟩

/-- A crossing of finite order puts every state on a closed chain. -/
theorem closedChainAt_of_pow_eq_one (s : ι → G) {i : ι} {k : ℕ}
    (hk : s i ^ (k + 1) = 1) (g : G) : ClosedChainAt (Tick s) g := by
  have h := tick_transGen_pow s i g k
  rwa [hk, mul_one] at h

/-- **Symmetric case.** If a crossing squares to the identity (`c² = id`),
every state lies on a closed chain of length two. -/
theorem closedChainAt_of_sq_eq_one (s : ι → G) {i : ι}
    (hs : s i * s i = 1) (g : G) : ClosedChainAt (Tick s) g :=
  closedChainAt_of_pow_eq_one s (k := 1) (by rw [pow_two]; exact hs) g

end Ticks

/-- **Braid group.** Ticks by Artin generators have no closed chains: the
writhe `exponentSum` raises the degree by one at each tick. -/
theorem braid_no_closedChainAt (n : ℕ) (g : QOU.MathlibExt.Braid.BraidGroup n) :
    ¬ ClosedChainAt (Tick (QOU.MathlibExt.Braid.σ (n := n))) g :=
  not_closedChainAt_tick _ (χ := QOU.MathlibExt.Braid.exponentSum n)
    (fun i => QOU.MathlibExt.Braid.exponentSum_σ i) g

/-- **Symmetric group.** On `S_{n+2}` with the adjacent transpositions as
crossings (at least one generator), every permutation lies on a closed chain
of length two: transpositions square to the identity. -/
theorem perm_closedChainAt (n : ℕ) (g : Equiv.Perm (Fin (n + 2))) :
    ClosedChainAt (Tick (fun i : Fin (n + 1) => Equiv.swap i.castSucc i.succ)) g :=
  closedChainAt_of_sq_eq_one (fun i : Fin (n + 1) => Equiv.swap i.castSucc i.succ)
    (i := 0) (Equiv.swap_mul_self (0 : Fin (n + 1)).castSucc (0 : Fin (n + 1)).succ) g

end QOU.Chronology
