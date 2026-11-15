/-
# On a path linking graph, a Milnor-defined triple is a split triple

The canonical atom word's closure has `μ = A + 1` components whose linking graph
is the **path** `P_μ`: the only pairs that link are the consecutive ones
(`QOU.Mass.SLq2Label` for `μ = A + 1`;
`computations/probes/atom_closure_milnor_indeterminacy_probe.py` for the path).

Milnor's `μ̄(ijk)` is defined modulo `Δ(ijk) = gcd(lk ij, lk jk, lk ki)`, so it is
a genuine integer exactly when all three pairs are unlinked — on a path, exactly
when the three components are mutually non-adjacent.

`computations/probes/milnor_defined_triples_are_split_probe.py` measures the
second half: between non-adjacent components the closure has **zero crossings**,
each component occupies a **contiguous strand block**, and the blocks of a
mutually non-adjacent triple are **pairwise disjoint intervals** acted on by no
common letter. Such a sublink is the closure of a braid on three disjoint,
non-interacting blocks — split by construction.

This file records the consequence: on this structure **definedness implies
vanishing**, so no non-trivial well-defined Milnor triple invariant exists at any
`A`. The two conditions coincide *because* the graph is a path — there, "not
linked" and "never interacts" are one condition. A genuinely Brunnian closure
(pairwise unlinked while still interacting, which `L6a4` is and this word is not)
would separate them, and that is the sharp requirement on any future assignment.

**Note on "the closure".** `atom_braid_word_3A` returns a *Hecke element*, not
a braid word: there is no single link behind it, only `2^(2A+1)` branch
closures, and its docstring forbids reading a topological quantity off the
element itself. Nothing here does. The measured facts concern which strand
pairs each letter acts on — identical in every branch, since an `averaged`
letter and both of its resolutions project to the same transposition — so
`PathLinkingStructure` is instantiated by **every branch closure separately**,
and the conclusion holds for each.

**Scope (b)** for every branch closure of this word, invariant named — a split
link has vanishing Milnor invariants. **Scope (a)** for the route.

No `sorry`. The two measured facts and the classical vanishing fact are carried
as hypotheses of `PathLinkingStructure`; the theorems derive the collapse.
-/
import Mathlib.Data.Nat.Basic

namespace QOU.Mass.MilnorPathCollapse

variable {ι : Type*}

/-- The measured structure of the atom closure's linking, as a bundle of
hypotheses. `Adj` is adjacency on the path; `Linked` records which pairs have
nonzero linking number; `Interacts` records which pairs share a crossing; `Split`
records which triples bound a splitting; `MubarZero` records the classical fact
that a split triple has vanishing Milnor invariant.

The class carries the *inputs* and the theorems below *derive* the conclusion —
`Δ = 0 → μ̄ = 0` is not a field. -/
structure PathLinkingStructure (ι : Type*) where
  /-- Adjacency of the path `P_μ`. -/
  Adj : ι → ι → Prop
  /-- The pair has nonzero linking number. -/
  Linked : ι → ι → Prop
  /-- Some letter of the word acts on both components. -/
  Interacts : ι → ι → Prop
  /-- The triple bounds a splitting into three pieces. -/
  Split : ι → ι → ι → Prop
  /-- Milnor's `μ̄` vanishes on the triple. -/
  MubarZero : ι → ι → ι → Prop
  /-- Measured: exactly the adjacent pairs link. -/
  linked_iff_adj : ∀ i j, Linked i j ↔ Adj i j
  /-- Measured: exactly the adjacent pairs share a crossing — the closure has
  *zero* crossings between non-adjacent components, not merely a zero signed
  sum. This is what makes the collapse happen. -/
  interacts_iff_adj : ∀ i j, Interacts i j ↔ Adj i j
  /-- Measured: three pairwise non-interacting components occupy pairwise
  disjoint contiguous strand blocks, so the sublink is split. -/
  split_of_not_interacts : ∀ i j k,
    ¬ Interacts i j → ¬ Interacts j k → ¬ Interacts i k → Split i j k
  /-- Classical: a split link has vanishing Milnor invariants. -/
  mubar_zero_of_split : ∀ i j k, Split i j k → MubarZero i j k

variable (S : PathLinkingStructure ι)

/-- `μ̄(ijk)` is a genuine integer — `Δ = 0` — exactly when all three pairs are
unlinked. -/
def MilnorDefined (i j k : ι) : Prop :=
  ¬ S.Linked i j ∧ ¬ S.Linked j k ∧ ¬ S.Linked i k

/-- **On a path, "unlinked" and "non-interacting" are the same condition.** This
is the step that has no analogue for a Brunnian link, where components interact
while their linking numbers vanish. -/
theorem not_linked_iff_not_interacts (i j : ι) :
    ¬ S.Linked i j ↔ ¬ S.Interacts i j := by
  rw [S.linked_iff_adj, S.interacts_iff_adj]

/-- **The collapse: every Milnor-defined triple is split.** -/
theorem split_of_milnorDefined {i j k : ι} (h : MilnorDefined S i j k) :
    S.Split i j k := by
  obtain ⟨hij, hjk, hik⟩ := h
  exact S.split_of_not_interacts i j k
    ((not_linked_iff_not_interacts S i j).mp hij)
    ((not_linked_iff_not_interacts S j k).mp hjk)
    ((not_linked_iff_not_interacts S i k).mp hik)

/-- **Definedness implies vanishing.** So no non-trivial well-defined Milnor
triple invariant exists in this closure, at any `A`: where `μ̄` is meaningful it
is zero, and where it is nonzero it is not well defined. -/
theorem mubarZero_of_milnorDefined {i j k : ι} (h : MilnorDefined S i j k) :
    S.MubarZero i j k :=
  S.mubar_zero_of_split i j k (split_of_milnorDefined S h)

/-- The contrapositive, as the requirement on any future nucleus→link
assignment: a triple carrying a nonzero well-defined `μ̄` must have a pair that
**interacts without linking** — precisely what Brunnian means, and precisely what
`interacts_iff_adj` forbids here. -/
theorem interacts_without_linking_of_nonzero {i j k : ι}
    (hdef : MilnorDefined S i j k) (hne : ¬ S.MubarZero i j k) : False :=
  hne (mubarZero_of_milnorDefined S hdef)

end QOU.Mass.MilnorPathCollapse
