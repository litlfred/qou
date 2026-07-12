import QOU.Mathlib.StandardYoungTableau

/-!
# `#SYT(⊥) = 1` — the empty-diagram standard-tableau count

A single small, sorry-free lemma: the empty Young diagram `⊥` has exactly one
standard Young tableau, `numStandardYoungTableaux ⊥ = 1`.

It is proved **directly**, via `Subsingleton` + `Nonempty` on
`QOU.Mathlib.StandardYoungTableau ⊥` — it does **not** route through the
Frame–Robinson–Thrall hook-length bridge (`IdentityIHLFBridge.dimSYT_eq_dimHLF`)
or the `n ≤ 12` `decide` certificate (`PartitionsOfBridge.rskBurnsideHolds_le12`)
that the sibling RSK build uses. So it is an independent, elementary computation of
a `numStandardYoungTableaux` (a **noncomputable** `Nat.card`, so `decide` is
impossible on it) of a concrete shape. The technique — `Nat.card_eq_one_iff_unique`
with the `Set.BijOn` onto `Set.Icc 1 0 = ∅` discharged by `Set.bijOn_empty` — is the
reusable pattern for any single-cell / small concrete shape.

Scope: pure combinatorics on `ℕ`; §7c-clean; no fit. The general RSK / Burnside
identity is developed elsewhere (`QOU.Mathlib.RSKBurnsideTarget`,
`PartitionsOfBridge`, the P1–P5 program).
-/

namespace QOU.Mathlib

open YoungDiagram

/-- **`#SYT(⊥) = 1`.** The empty Young diagram has exactly one standard Young
tableau. Proved directly by `Subsingleton` (every entry is `0` by `zeros`, as `⊥`
has no cells) + `Nonempty` (the all-zero `highestWeight ⊥`, whose `BijOn` onto
`Set.Icc 1 (⊥.cells.card) = Set.Icc 1 0 = ∅` is `Set.bijOn_empty`), then
`Nat.card_eq_one_iff_unique`. -/
theorem numStandardYoungTableaux_bot : numStandardYoungTableaux (⊥ : YoungDiagram) = 1 := by
  rw [numStandardYoungTableaux, Nat.card_eq_one_iff_unique]
  refine ⟨⟨fun T1 T2 => ?_⟩, ⟨?_⟩⟩
  · -- Subsingleton: two standard tableaux over `⊥` agree.
    obtain ⟨s1, h1⟩ := T1
    obtain ⟨s2, h2⟩ := T2
    have hs : s1 = s2 :=
      SemistandardYoungTableau.ext fun i j => by
        rw [s1.zeros (YoungDiagram.notMem_bot _), s2.zeros (YoungDiagram.notMem_bot _)]
    subst hs
    rfl
  · -- Nonempty: the highest-weight (all-zero) SSYT is a standard tableau over `⊥`.
    refine ⟨SemistandardYoungTableau.highestWeight ⊥, ?_⟩
    have hcard : (⊥ : YoungDiagram).cells.card = 0 := by rw [cells_bot]; rfl
    rw [hcard, cells_bot, Finset.coe_empty, Set.Icc_eq_empty (by decide)]
    exact Set.bijOn_empty _

end QOU.Mathlib
