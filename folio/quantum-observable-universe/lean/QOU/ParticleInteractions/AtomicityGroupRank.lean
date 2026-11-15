import Mathlib.Algebra.Lie.Rank
import Mathlib.Tactic

/-!
# Atomicity — the GROUP-rank premise `rank G = rank Lie(G)` (conditional scaffold)

**This file is a CONDITIONAL SCAFFOLD, not a closure of `rank G = rank Lie(G)`.**
It sets up the *target API* for the standard structural theorem

  `rank G = rank Lie(G)`   (algebraic-group rank = Lie-algebra rank),

which is **absent from Mathlib** and which this file does **not** prove. The theorem
is a genuine major result (its proof runs through maximal tori of an algebraic group,
the Lie functor, and the identification of a maximal torus with a Cartan subalgebra of
the Lie algebra — see the survey below). Here we (1) axiomatize it as a §3b-cond
conditional class carrying the *real* equality as its field, provide **no** instance,
and mark it an **OPEN premise**; and (2) derive the downstream group bound
`groupRank G ≤ 1` *conditionally* on that class, from the already-landed Lie-side bound
`LieAlgebra.rank K 𝔤 ≤ 1`. Only the conditional implication is proved; the group-rank
premise itself stays open.

## Why this is needed (atomicity context)

QOU atomicity needs `rank G ≤ 1` for the Tannaka dual `G` of a self-dual rank-2 object.
The Lie-side bound is **already proved sorry-free** on branch
`claude/atomicity-rankone-order-separation-2026-07-25` (PR #4285),
`QOU/ParticleInteractions/AtomicityLieRank.lean`:

  `QOU.Atomicity.sl2_subalgebra_rank_le_one : ∀ 𝔤 ⊆ 𝔰𝔩₂, LieAlgebra.rank K 𝔤 ≤ 1`
  `QOU.Atomicity.sl2_rank_eq_one           : LieAlgebra.rank K 𝔰𝔩₂ = 1`.

To lift `rank 𝔤 ≤ 1` (Lie) to `rank G ≤ 1` (group) one needs precisely
`rank G = rank Lie(G)`. That is the single open premise this file isolates.

## Mathlib survey — what is present, what is absent

**Present (Lie side):**
* `LieAlgebra.rank R L : ℕ` — the Lie-algebra rank (`Mathlib.Algebra.Lie.Rank`),
  defined as the minimum over `x` of `natTrailingDegree (charpoly (ad R L x))`, i.e. the
  generic dimension of `ad`-generalized-`0`-eigenspaces.
* `LieAlgebra.rank_le_natTrailingDegree_charpoly_ad` — the specific-element upper bound.
* `LieAlgebra.IsCartanSubalgebra`, `LieSubalgebra.engel`, `LieAlgebra.finrank_engel`,
  `LieAlgebra.exists_isCartanSubalgebra_engel`, `LieAlgebra.rank_le_finrank_engel`,
  `LieAlgebra.exists_isRegular`, `LieAlgebra.isRegular_iff_finrank_engel_eq_rank`
  (`Mathlib.Algebra.Lie.{Rank,CartanExists,EngelSubalgebra}`) — a genuine
  Cartan-subalgebra-of-a-Lie-algebra API. The maximal-torus notion **on the Lie side**
  is thus available (a Cartan subalgebra of a semisimple Lie algebra is a maximal torus).

**Absent (group side):**
* No `LinearAlgebraicGroup` / `AlgebraicGroup` rank, no maximal-torus-of-an-algebraic-group
  theory. Mathlib has `Mathlib.Algebra.Group.*`, `Mathlib.GroupTheory.*`,
  `Mathlib.AlgebraicGeometry.*`, and `Mathlib.Geometry.Manifold.Algebra.LieGroup`
  (smooth Lie groups), but **no** algebraic-group `rank`, no maximal split torus, and
  **no** `Lie : AlgebraicGroup ⥤ LieAlgebra` functor with a rank-preservation theorem.
* Consequently `rank G` for an algebraic group `G` cannot even be *stated* against a
  Mathlib definition, let alone equated to `LieAlgebra.rank`.

**Gap this file bridges:** it introduces an abstract handle `AlgebraicGroupRank G`
(the datum "G carries a rank") and the conditional equality class
`RankGroupEqRankLie` (the open theorem `rank G = rank Lie(G)`), then proves the
downstream implication. It does **not** construct algebraic-group rank theory.

-- Ref: [leitner2026] conj:binding-manybody-eq-jet-filtration (atomicity); def:tannaka-dual
-- Ref: [leitner2026] rank G = rank Lie(G): Milne, *Algebraic Groups*, CUP 2017, §17
--       (maximal tori); Springer, *Linear Algebraic Groups*, 2nd ed., §6–§7 (tori,
--       Cartan subgroups, and their Lie algebras) — standard, not in Mathlib.
-/

namespace QOU.Atomicity

open LieAlgebra

/-! ## The abstract group-rank handle and the conditional equality class -/

/-- **Abstract algebraic-group rank (data).** Mathlib has no maximal-torus-of-an-algebraic-
group theory, so the rank of an algebraic group `G` — the common dimension of its maximal
tori — cannot be constructed here. We carry it as *opaque data*: `[AlgebraicGroupRank G]`
means "`G` comes equipped with a well-defined rank `groupRank G : ℕ`". This is a data
class (like `Fintype` carrying `card`), **not** a proposition — it makes no unproved
logical claim; it only names a quantity the ambient algebraic-group theory would supply.

This is the honest placeholder for the missing Mathlib API. It is deliberately weak: it
asserts nothing about how `groupRank G` relates to anything, so it cannot be used to
launder a claim. The load-bearing relation lives in `RankGroupEqRankLie` below. -/
class AlgebraicGroupRank (G : Type*) where
  /-- The rank of `G` (dimension of a maximal torus). Supplied by the ambient
      algebraic-group theory; abstract here. -/
  groupRank : ℕ

/-- The rank of an algebraic group `G`, once `G` carries an `AlgebraicGroupRank` handle. -/
def groupRank (G : Type*) [AlgebraicGroupRank G] : ℕ :=
  AlgebraicGroupRank.groupRank G

/-- **Conditional class (§3b-cond): `rank G = rank Lie(G)`.** This is the standard
structural theorem identifying the rank of an algebraic group `G` with the rank of its
Lie algebra `L = Lie(G)`, **absent from Mathlib** (see the survey above). We axiomatize
it as a `Prop`-valued class whose single field is the **genuine equality**
`groupRank G = LieAlgebra.rank R L` — *not* `True`, and *not* the block's own conclusion.

The equality is non-trivial to discharge: `groupRank G` is fixed independently by the
`AlgebraicGroupRank G` instance (it does not mention `L`), so an instance of this class
must actually *prove* that the group's maximal-torus dimension equals the Lie-algebra
generic-`ad`-nullity — the whole content of the theorem. Establishing that in general
requires the maximal-torus / Lie-functor theory Mathlib lacks.

**OPEN PREMISE — no canonical instance is provided.** Per the anti-laundering rule
(`AGENTS.md §"Axiomatization is NOT a Proof"`), writing this class does **not** prove
`rank G = rank Lie(G)`; the theorem remains mathematically open in this corpus. Any
downstream result depending on it is a *rigorous conditional* (proved modulo this class),
never an unconditional claim.

-- Ref: [leitner2026] rank G = rank Lie(G); see file docstring for standard references. -/
class RankGroupEqRankLie (R L G : Type*) [CommRing R] [Nontrivial R] [LieRing L]
    [LieAlgebra R L] [Module.Finite R L] [Module.Free R L]
    [AlgebraicGroupRank G] : Prop where
  /-- The genuine content: the algebraic-group rank equals the Lie-algebra rank.
      This is the open premise. -/
  rank_group_eq_rank_lie : groupRank G = LieAlgebra.rank R L

/-! ## Downstream: the conditional group bound (fully proved modulo the class) -/

/-- **General conditional bound.** If `rank G = rank Lie(G)` (the open premise, as the
class `RankGroupEqRankLie R L G`) and the Lie-algebra rank is `≤ n`, then the group rank
is `≤ n`. Fully proved modulo the class — a rigorous conditional. The Lie-rank bound
`hLie` is the input the Lie-side development supplies. -/
theorem groupRank_le_of_lieRank_le {R L G : Type*} [CommRing R] [Nontrivial R] [LieRing L]
    [LieAlgebra R L] [Module.Finite R L] [Module.Free R L]
    [AlgebraicGroupRank G] [RankGroupEqRankLie R L G] {n : ℕ}
    (hLie : LieAlgebra.rank R L ≤ n) :
    groupRank G ≤ n := by
  rw [RankGroupEqRankLie.rank_group_eq_rank_lie (R := R) (L := L)]
  exact hLie

/-- **Atomicity group-rank upper bound (conditional).** For the Tannaka dual `G` whose
Lie algebra is a subalgebra `𝔤 ⊆ 𝔰𝔩₂`, *if* `rank G = rank Lie(G)` (the open premise
`RankGroupEqRankLie K 𝔤 G`), then `rank G ≤ 1`.

**What is proved vs. open.** The implication is proved sorry-free: it is
`groupRank_le_of_lieRank_le` fed the landed Lie-side bound `hLie`. The bound `hLie`
itself — `LieAlgebra.rank K 𝔤 ≤ 1` — is discharged sorry-free by
`QOU.Atomicity.sl2_subalgebra_rank_le_one h2 𝔤` (landed, PR #4285) and is threaded here
as an explicit hypothesis to keep this file decoupled from that in-flight branch. The
**group-rank premise** `RankGroupEqRankLie K 𝔤 G` is **OPEN** — no instance exists; this
is a conditional result, not a closure of atomicity on the group side. -/
theorem atomicity_group_rank_le_one {K G : Type*} [Field K]
    [AlgebraicGroupRank G] (𝔤 : Type*) [LieRing 𝔤] [LieAlgebra K 𝔤]
    [Module.Finite K 𝔤] [Module.Free K 𝔤]
    [RankGroupEqRankLie K 𝔤 G]
    (hLie : LieAlgebra.rank K 𝔤 ≤ 1) :
    groupRank G ≤ 1 :=
  groupRank_le_of_lieRank_le hLie

/-- **Exact group rank (conditional).** If `rank G = rank Lie(G)` and the Lie-algebra
rank is exactly `n`, then the group rank is exactly `n`. The equality-direction companion
of `groupRank_le_of_lieRank_le`; a direct rewrite by the class field. Fully proved modulo
the class. -/
theorem groupRank_eq_of_lieRank_eq {R L G : Type*} [CommRing R] [Nontrivial R] [LieRing L]
    [LieAlgebra R L] [Module.Finite R L] [Module.Free R L]
    [AlgebraicGroupRank G] [RankGroupEqRankLie R L G] {n : ℕ}
    (hLie : LieAlgebra.rank R L = n) :
    groupRank G = n := by
  rw [RankGroupEqRankLie.rank_group_eq_rank_lie (R := R) (L := L)]
  exact hLie

/-- **Atomicity exact group rank (conditional).** For `G` whose Lie algebra is a subalgebra
`𝔤 ⊆ 𝔰𝔩₂`, *if* `rank G = rank Lie(G)` then `rank G = 1`. Fed the landed exact Lie-side
value `LieAlgebra.rank K 𝔤 = 1` (discharged sorry-free by
`QOU.Atomicity.sl2_rank_eq_one`, PR #4285, threaded here as a hypothesis). The
group-rank premise `RankGroupEqRankLie K 𝔤 G` is **OPEN**; only this implication is proved. -/
theorem atomicity_group_rank_eq_one {K G : Type*} [Field K]
    [AlgebraicGroupRank G] (𝔤 : Type*) [LieRing 𝔤] [LieAlgebra K 𝔤]
    [Module.Finite K 𝔤] [Module.Free K 𝔤]
    [RankGroupEqRankLie K 𝔤 G]
    (hLie : LieAlgebra.rank K 𝔤 = 1) :
    groupRank G = 1 :=
  groupRank_eq_of_lieRank_eq hLie

end QOU.Atomicity
