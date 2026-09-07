import QOU.Mass.PairwiseCumulantVanishing
import Mathlib.Tactic

/-!
# Why the crossing model's mutual channel cannot be a bare pair sum

Two results landed on `main` on 2026-08-30 from different sessions, and this file is the
consequence of putting them together.

* `QOU.Mass.SelfMutualPartition.binding_eq_neg_mutualEnergy` (bean `qou-brng`, #6145) — with
  binding defined the standard way, `B := Σ(isolated self masses) − (assembled mass)`, the self
  energies cancel exactly and `B = −(mutual energy)`, where the mutual energy is the sum of
  `energy c` over the **inter-component** crossings of the assembled diagram.
* `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise` (bean `qou-bhzt`, #6101) — a
  pairwise-additive binding has identically vanishing connected 3-body cumulant.

The first is a sum over crossings, and **every crossing joins exactly two components**, so that
sum groups by unordered pair with no further hypothesis: `mutualEnergy = Σ_{i<j} w_ij`. That looks
like the second result's `IsPairwise`, and if it were, R2 would be refuted on contact — AME2020
measures `b₃ = +1.4262225` (`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`), not zero.

It is not, and the gap is exactly one hypothesis: whether a pair's weight `w_ij` is the **same** in
every assembly containing that pair. Call that `PairLocal`. This file proves that the hypothesis is
the whole of the difference, and therefore that the measured `b₃` **forces** the crossing structure
between two components to depend on what else is present.

## The results

* `isPairwise_of_pairLocal` — assembly-independent pair weights ⇒ the induced binding map is
  pairwise-additive.
* `b3_eq_zero_of_pairLocal` — hence `b₃ = 0` identically.
* `not_pairLocal_of_b3_ne_zero` — hence a nonzero measured `b₃` **refutes pair-locality**. This is
  the load-bearing direction: it is a constraint the framework's carrier has to satisfy, derived
  from AME rather than assumed.

## The proposed escape, and why it is NOT available — CORRECTED 2026-09-07

This section originally read: *"A **Brunnian** carrier is precisely a maximal violation of
`PairLocal` … the corpus already establishes that the ³He/⁴He carrier `L6a4` is Brunnian
(`QOU.Mass.BrunnianBindingChannel`, #6125) … `b3_eq_neg_tripleMutual_of_brunnian` is the
falsifiable payoff … Measuring `b₃` therefore pins the Brunnian triple channel to a specific
number."*  **The escape does not work, and the cited file is what rules it out.**

Two different properties were sharing the name `Brunnian`:

| | condition | true of `L6a4`? |
|---|---|---|
| topological (`QOU.KnotTheory.Brunnian`, `BrunnianBindingChannel`) | pairwise linking number `= 0`, i.e. `n₊ = n₋` | **yes** |
| the hypothesis below, now `NoIsolatedPairEnergy` | pairwise mutual *energy* `w₂ = 0` | **no** |

`BrunnianBindingChannel` establishes the **first** and then proves
`brunnian_binding_survives`: for a crossing pair at `q > 1` the count channel is **strictly
positive**, so `w₂ ≠ 0`.  Its whole point is that binding *survives* the Brunnian vanishing — the
opposite of what the citation above claimed it established.  Independently, the AME cumulant
`b₂ = 2.2245662` MeV refutes `w₂ = 0` outright, by the same contrapositive
`not_pairLocal_of_b3_ne_zero` uses one hypothesis up.  Both refutations are sorry-free in
`QOU.Mass.BrunnianHypothesisNotSatisfied`.

**So the hypothesis is renamed to say what it is** (`NoIsolatedPairEnergy`), and the theorems
below are kept and remain true — as implications with a hypothesis this carrier does not satisfy.
`not_pairLocal_of_noIsolatedPairEnergy` is in any case redundant: `not_pairLocal_of_b3_ne_zero`
reaches `¬PairLocal` from data with no unsatisfied hypothesis at all.

**And the falsifiable payoff was collected elsewhere, as a negative.**
`QOU.Mass.BrunnianTripleExhaustion` computes the count-channel prediction directly and gets
`b₃/b₂ = M − 3`, an *integer* for any total crossing count `M`, against a measured ratio strictly
inside `(0,1)`: `no_carrier_reproduces_b3` — no carrier of **any** crossing number works, missing
by at least 55.98 % of the measured value, and the Borromean rings themselves (`M = 3`) give
`b₃/b₂ = 0` exactly.  That is the honest state of the three-body channel; reading `b₃` off as the
triple mutual energy would have hidden it.

## Scope

This is a conditional structural result, not a magnitude derivation. It says what the carrier must
do; it does not identify the carrier, does not compute `w₃`, and does not touch the `ℏ_q²`
saturation question (`qou-brng` R3, measured numerology-suspect). The `CrossingModel` here records
a pair's mutual energy in each of the three cluster sizes on four components — it is a faithful
bookkeeping of the crossing sum grouped by pair, not a new physical postulate.

Base ring is a generic `CommRing` for everything but the sign corollary, which needs an ordering
(AGENTS.md §7c).

Beans `qou-brng`, `qou-bhzt`.
-/

namespace QOU.Mass.CrossingModelPairLocality

open QOU.Mass.PairwiseCumulantVanishing

variable {R : Type*} [CommRing R]

/-- The inter-component crossing energy of a four-component assembly, **grouped by the pair each
crossing joins**. Every crossing joins exactly two components, so this grouping is a bookkeeping
identity rather than an assumption; what is *not* assumed is that a pair's weight is the same
across cluster sizes, which is why there are three fields rather than one.

* `w2 i j` — the mutual energy of the pair `{i,j}` in the isolated two-component assembly;
* `w3 i j k` — the mutual energy of the pair `{i,j}` inside the triple `{i,j,k}`;
* `w4 i j` — the mutual energy of the pair `{i,j}` inside the full four-component assembly. -/
structure CrossingModel (R : Type*) [CommRing R] where
  /-- mutual energy of the pair `{i,j}` measured in the isolated pair -/
  w2 : Fin 4 → Fin 4 → R
  /-- mutual energy of the pair `{i,j}` measured inside the triple `{i,j,k}` -/
  w3 : Fin 4 → Fin 4 → Fin 4 → R
  /-- mutual energy of the pair `{i,j}` measured inside the four-component assembly -/
  w4 : Fin 4 → Fin 4 → R

namespace CrossingModel

variable (C : CrossingModel R)

/-- **Pair-locality**: a pair's mutual energy does not depend on what else is in the assembly.
This is the hypothesis that turns `binding = −(mutual energy)` into a pairwise-additive binding,
and the one the measured 3-body cumulant refutes. -/
def PairLocal : Prop :=
  (∀ i j k, C.w3 i j k = C.w2 i j) ∧ (∀ i j, C.w4 i j = C.w2 i j)

/-- **`NoIsolatedPairEnergy`** (RENAMED 2026-09-07 from `Brunnian`): a crossing model in which
a pair measured in
isolation carries no mutual energy.

**CORRECTED 2026-09-07 — this docstring cited `QOU.Mass.BrunnianBindingChannel` as
establishing that the ³He/⁴He carrier `L6a4` "has this property". It does not; it proves
the opposite.** That file establishes L6a4 has vanishing pairwise *Gauss linking number*
(`n₊ = n₋`) and then proves `brunnian_binding_survives`: the mutual energy of such a pair
is **strictly positive**, `0 < countChannel m m q` for `0 < m`, `1 < q`. Its whole point
is that binding *survives* the Brunnian vanishing.

So two distinct properties share one name — topological (linking number zero, TRUE of
L6a4) and energetic (`w₂ = 0`, FALSE of it) — and the first does not imply the second.
Consequently `b3_eq_neg_tripleMutual_of_brunnian` below is a correct theorem whose
hypothesis **L6a4 does not satisfy**, and the measured `b₃` does not cleanly pin the
triple channel. Independently, the measured `b₂ = 2.2245662` MeV refutes this hypothesis
outright. Both refutations are formalised, sorry-free, in
`QOU.Mass.BrunnianHypothesisNotSatisfied`.  Tier table for the four things this corpus calls `Brunnian`, and which implications hold: `QOU.Mass.BrunnianTierDisambiguation`. -/
def NoIsolatedPairEnergy : Prop := ∀ i j, C.w2 i j = 0

/-- The total mutual energy of the triple `{i,j,k}`: its three pairs, each measured inside the
triple. -/
def tripleMutual (i j k : Fin 4) : R := C.w3 i j k + C.w3 i k j + C.w3 j k i

/-- The total mutual energy of the four-component assembly: its six pairs, each measured inside
the assembly. -/
def quadMutual : R :=
  C.w4 0 1 + C.w4 0 2 + C.w4 0 3 + C.w4 1 2 + C.w4 1 3 + C.w4 2 3

/-- The binding map induced by the crossing model, via
`SelfMutualPartition.binding_eq_neg_mutualEnergy`: each cluster's binding is the negative of its
mutual energy. -/
def toBindingMap : BindingMap R where
  pair i j := - C.w2 i j
  triple i j k := - C.tripleMutual i j k
  quad := - C.quadMutual

@[simp] theorem toBindingMap_pair (i j : Fin 4) :
    C.toBindingMap.pair i j = - C.w2 i j := rfl

@[simp] theorem toBindingMap_triple (i j k : Fin 4) :
    C.toBindingMap.triple i j k = - C.tripleMutual i j k := rfl

@[simp] theorem toBindingMap_quad : C.toBindingMap.quad = - C.quadMutual := rfl

end CrossingModel

open CrossingModel

/-- **Pair-locality makes the crossing model pairwise-additive.** Grouping the mutual energy by
pair is automatic; it is assembly-independence of the pair weights that produces the shape
`PairwiseCumulantVanishing.IsPairwise`. -/
theorem isPairwise_of_pairLocal {C : CrossingModel R} (h : C.PairLocal) :
    C.toBindingMap.IsPairwise := by
  obtain ⟨h3, h4⟩ := h
  constructor
  · intro i j k
    simp only [toBindingMap_triple, toBindingMap_pair, CrossingModel.tripleMutual,
      h3 i j k, h3 i k j, h3 j k i]
    ring
  · simp only [toBindingMap_quad, BindingMap.pairSum, toBindingMap_pair,
      CrossingModel.quadMutual, h4]
    ring

/-- **So a pair-local crossing model has identically vanishing 3-body cumulant.** Composing with
`PairwiseCumulantVanishing.b3_eq_zero_of_isPairwise`. -/
theorem b3_eq_zero_of_pairLocal {C : CrossingModel R} (h : C.PairLocal) (i j k : Fin 4) :
    C.toBindingMap.b3 i j k = 0 :=
  b3_eq_zero_of_isPairwise (isPairwise_of_pairLocal h) i j k

/-- **And the 4-body cumulant too.** -/
theorem b4_eq_zero_of_pairLocal {C : CrossingModel R} (h : C.PairLocal) :
    C.toBindingMap.b4 = 0 :=
  b4_eq_zero_of_isPairwise (isPairwise_of_pairLocal h)

/-- **The load-bearing direction: a nonzero 3-body cumulant refutes pair-locality.** AME2020
measures `b₃ = +1.4262225` (`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`), so the crossing
structure between two components *must* depend on what else is present. This is a constraint on
the carrier derived from data, not a modelling choice. -/
theorem not_pairLocal_of_b3_ne_zero {C : CrossingModel R} {i j k : Fin 4}
    (h : C.toBindingMap.b3 i j k ≠ 0) : ¬ C.PairLocal :=
  fun hp => h (b3_eq_zero_of_pairLocal hp i j k)

/-! ### The Brunnian carrier is exactly the escape -/

/-- **A Brunnian carrier violates pair-locality**, provided some triple is nontrivial — which is
the defining content of Brunnian-ness, that the whole is linked while every pair is not. So the
Brunnian property is not incidental: it is what lets `binding = −(mutual energy)` coexist with a
nonzero measured 3-body cumulant. -/
theorem not_pairLocal_of_noIsolatedPairEnergy {C : CrossingModel R} (hB : C.NoIsolatedPairEnergy)
    {i j k : Fin 4} (h3 : C.w3 i j k ≠ 0) : ¬ C.PairLocal := by
  intro ⟨hw3, _⟩
  exact h3 (by rw [hw3 i j k, hB i j])

/-- **With a Brunnian carrier the 3-body cumulant is exactly the negated triple mutual energy.**
No pair contamination and no free constant: the pair terms vanish identically, so the whole of
`b₃` is the irreducibly three-body channel. Measuring `b₃` therefore pins that channel. -/
theorem b3_eq_neg_tripleMutual_of_noIsolatedPairEnergy {C : CrossingModel R} (hB : C.NoIsolatedPairEnergy)
    (i j k : Fin 4) :
    C.toBindingMap.b3 i j k = - C.tripleMutual i j k := by
  have hw : ∀ a b : Fin 4, C.w2 a b = 0 := hB
  simp only [BindingMap.b3, toBindingMap_triple, toBindingMap_pair, hw]
  ring

/-- **Non-vacuity of `PairLocal`.** A model whose pair weight is literally the same function in
every cluster size is pair-local, so `isPairwise_of_pairLocal` is not vacuous. -/
theorem pairLocal_of_constant (w : Fin 4 → Fin 4 → R) :
    (CrossingModel.mk w (fun i j _ => w i j) w : CrossingModel R).PairLocal :=
  ⟨fun _ _ _ => rfl, fun _ _ => rfl⟩

end QOU.Mass.CrossingModelPairLocality

/-! ### The sign, over an ordered ring -/

namespace QOU.Mass.CrossingModelPairLocality

variable {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]

open CrossingModel

/-- **A positive 3-body cumulant forces the Brunnian triple channel to be negative.** With the
pair terms gone, `b₃ = −(triple mutual energy)` exactly, so the sign of the measured cumulant
fixes the sign of the channel with nothing in between. AME gives `b₃ > 0`, hence an attractive
(negative-energy) three-body mutual channel. -/
theorem tripleMutual_neg_of_b3_pos {C : CrossingModel R} (hB : C.NoIsolatedPairEnergy)
    {i j k : Fin 4} (hb : 0 < C.toBindingMap.b3 i j k) :
    C.tripleMutual i j k < 0 := by
  rw [b3_eq_neg_tripleMutual_of_noIsolatedPairEnergy hB] at hb
  exact neg_pos.mp hb

end QOU.Mass.CrossingModelPairLocality
