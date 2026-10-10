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
| `fintypeAddableCells` | a diagram has finitely many addable cells |
| `sum_cornerPair_flat`, `sum_addPair_flat` | each pair sum as a double sum |
| `sum_corner_eq_sum_addable` | the exchange as a **double**-sum reindexing — the usable form |

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


theorem isAddableCell_mem_bound {ν : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell ν s) :
    s ∈ insert ((0, 0) : ℕ × ℕ)
      ((ν.cells.image fun c => (c.1 + 1, c.2)) ∪ (ν.cells.image fun c => (c.1, c.2 + 1))) := by
  obtain ⟨_, h1, h2⟩ := hs
  rcases Nat.eq_zero_or_pos s.1 with hz1 | hp1
  · rcases Nat.eq_zero_or_pos s.2 with hz2 | hp2
    · have : s = ((0, 0) : ℕ × ℕ) := Prod.ext hz1 hz2
      rw [this]; exact Finset.mem_insert_self _ _
    · have hmem : (s.1, s.2 - 1) ∈ ν := by rcases h2 with h | h; · omega
                                           · exact h
      exact Finset.mem_insert_of_mem (Finset.mem_union_right _ (Finset.mem_image.mpr
        ⟨(s.1, s.2 - 1), (YoungDiagram.mem_cells _).mpr hmem, Prod.ext rfl (by omega)⟩))
  · have hmem : (s.1 - 1, s.2) ∈ ν := by rcases h1 with h | h; · omega
                                         · exact h
    exact Finset.mem_insert_of_mem (Finset.mem_union_left _ (Finset.mem_image.mpr
      ⟨(s.1 - 1, s.2), (YoungDiagram.mem_cells _).mpr hmem, Prod.ext (by omega) rfl⟩))

noncomputable instance fintypeAddableCells (ν : YoungDiagram) :
    Fintype {s : ℕ × ℕ // IsAddableCell ν s} := by
  apply Set.Finite.fintype
  apply Set.Finite.subset (Finset.finite_toSet (insert ((0, 0) : ℕ × ℕ)
      ((ν.cells.image fun c => (c.1 + 1, c.2)) ∪ (ν.cells.image fun c => (c.1, c.2 + 1)))))
  intro s hs
  exact Finset.mem_coe.mpr (isAddableCell_mem_bound hs)

def addPairEquivSigma (n : ℕ) :
    AddPair n
      ≃ Σ M : {μ : YoungDiagram // μ.cells.card = n}, {s : ℕ × ℕ // IsAddableCell M.1 s} where
  toFun := fun p => ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, p.2.2⟩⟩
  invFun := fun p => ⟨(p.1.1, p.2.1), ⟨p.1.2, p.2.2⟩⟩
  left_inv := fun _ => rfl
  right_inv := fun _ => rfl

theorem sum_cornerPair_flat {M : Type*} [AddCommMonoid M] (n : ℕ) (g : CornerPair n → M) :
    ∑ p : CornerPair n, g p
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
          ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c}, g ⟨(L.1, c.1), ⟨L.2, c.2⟩⟩ := by
  set F : (Σ L : {ρ : YoungDiagram // ρ.cells.card = n + 1}, {c : ℕ × ℕ // IsCornerCell L.1 c}) → M
    := fun q => g ⟨(q.1.1, q.2.1), ⟨q.1.2, q.2.2⟩⟩ with hF
  exact (Fintype.sum_equiv (cornerPairEquivSigma n) g F (fun _ => rfl)).trans
    (Fintype.sum_sigma F)

theorem sum_addPair_flat {M : Type*} [AddCommMonoid M] (n : ℕ) (g : AddPair n → M) :
    ∑ p : AddPair n, g p
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, g ⟨(ν.1, s.1), ⟨ν.2, s.2⟩⟩ := by
  set F : (Σ M : {μ : YoungDiagram // μ.cells.card = n}, {s : ℕ × ℕ // IsAddableCell M.1 s}) → M
    := fun q => g ⟨(q.1.1, q.2.1), ⟨q.1.2, q.2.2⟩⟩ with hF
  exact (Fintype.sum_equiv (addPairEquivSigma n) g F (fun _ => rfl)).trans
    (Fintype.sum_sigma F)

/-- **The exchange as a double-sum reindexing.**  Summing over `(λ, removable corner)` at size
`n + 1` — with the summand read on the *erased* diagram — is summing over `(ν, addable corner)` at
size `n`. -/
theorem sum_corner_eq_sum_addable {M : Type*} [AddCommMonoid M] (n : ℕ)
    (f : {ν : YoungDiagram // ν.cells.card = n} → (ℕ × ℕ) → M) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
        ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
          f ⟨eraseCorner L.1 c.1 c.2, by
            have := card_eraseCorner L.1 c.1 c.2
            have := L.2
            omega⟩ c.1
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, f ν s.1 := by
  set g : AddPair n → M := fun p => f ⟨p.1.1, p.2.1⟩ p.1.2 with hg
  rw [← sum_addPair_flat n g, ← sum_cornerPair_eq_sum_addPair n g,
    sum_cornerPair_flat n (fun p => g (cornerAddEquiv n p))]
  rfl

end QOU.Mathlib
