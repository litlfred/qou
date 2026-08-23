import QOU.Mathlib.YoungDiagramAddCell
import QOU.Mathlib.SchenstedPartitionShape
import QOU.Mathlib.SYTBranchingRule

/-!
# QOU.Mathlib.YoungDiagramCornerReindex — the corner/addable exchange as a sum reindexing

`YoungDiagramAddCell` builds the bijection

`cornerAddEquiv n : CornerPair n ≃ AddPair n`,

`(λ, removable corner of λ) ↔ (λ ∖ c, that corner as an addable one)`, for `|λ| = n + 1`.  An
equivalence is not yet usable under a `∑`: both sides must be `Fintype`s.  This file supplies those
instances and the resulting reindexing lemma.

| | |
|---|---|
| `fintypeDiagramsOfCard` | diagrams of a fixed size are finite, transported from `Nat.Partition` |
| `fintypeCornerPair`, `fintypeAddPair` | the two pair types are finite |
| `sum_cornerPair_eq_sum_addPair` | `∑` over removable corners at `n + 1` = `∑` over addable ones at `n` |

## Why the imports differ from `YoungDiagramAddCell`

Finiteness is the one part of this story that is *not* pure `ℕ × ℕ` combinatorics: it comes from
`partitionShapeEquiv` (a diagram of size `n` is a partition of `n`), which sits on the RSK/Schensted
cone; the finiteness of a diagram's corner set comes from `SYTBranchingRule`.  Keeping it in a separate file leaves `YoungDiagramAddCell` importable by anything that only
wants `addCell` and the round-trips.

`AddPair`'s instance costs nothing extra: transporting along `cornerAddEquiv` avoids ever having to
bound the addable cells of a diagram directly — the removable side already did that work.

Nothing archimedean; no ring; no fit.

LaTeX label: `def:young-diagram-corner-reindex`
-/

namespace QOU.Mathlib

open YoungDiagram

/-- Young diagrams with `n` cells form a finite type — transported from `Nat.Partition n`. -/
noncomputable instance fintypeDiagramsOfCard (n : ℕ) :
    Fintype {μ : YoungDiagram // μ.cells.card = n} :=
  Fintype.ofEquiv (Nat.Partition n) (partitionShapeEquiv n)

/-- `CornerPair` repackaged as a `Sigma` over the diagram.  Nothing moves, so both round-trips are
`rfl`; this is the harmless direction of the subtype-vs-`Sigma` phrasing choice recorded on
`cornerAddEquiv` (the `Sigma` form of *that* bijection is the one that produces `HEq`). -/
def cornerPairEquivSigma (n : ℕ) :
    CornerPair n
      ≃ Σ L : {μ : YoungDiagram // μ.cells.card = n + 1}, {c : ℕ × ℕ // IsCornerCell L.1 c} where
  toFun := fun p => ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, p.2.2⟩⟩
  invFun := fun p => ⟨(p.1.1, p.2.1), ⟨p.1.2, p.2.2⟩⟩
  left_inv := fun _ => rfl
  right_inv := fun _ => rfl

noncomputable instance fintypeCornerPair (n : ℕ) : Fintype (CornerPair n) :=
  Fintype.ofEquiv _ (cornerPairEquivSigma n).symm

/-- `AddPair`'s finiteness comes free from the exchange — no separate bound on addable cells. -/
noncomputable instance fintypeAddPair (n : ℕ) : Fintype (AddPair n) :=
  Fintype.ofEquiv _ (cornerAddEquiv n)

/-- **The outer branching exchange as a sum reindexing.**  Summing a function of
(diagram of size `n`, addable corner) over all such pairs is the same as summing it, pulled back
along the exchange, over (diagram of size `n + 1`, removable corner). -/
theorem sum_cornerPair_eq_sum_addPair {M : Type*} [AddCommMonoid M] (n : ℕ)
    (f : AddPair n → M) :
    ∑ p : CornerPair n, f (cornerAddEquiv n p) = ∑ p : AddPair n, f p :=
  Fintype.sum_equiv (cornerAddEquiv n) _ _ (fun _ => rfl)

end QOU.Mathlib
