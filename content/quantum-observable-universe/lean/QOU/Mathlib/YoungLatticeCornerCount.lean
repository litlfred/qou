import QOU.Mathlib.YoungLatticeDifferential
import QOU.Mathlib.SchenstedPartitionShape

/-!
# QOU.Mathlib.YoungLatticeCornerCount — the corner/addable exchange, summed over a rank

The rank-level consequence of the two ingredients already proved:

* `cornerAddEquiv` (`YoungDiagramAddCell`) — the pointwise exchange
  `(λ, removable corner) ≃ (λ ∖ c, that corner as an addable one)`;
* `card_addableCells_eq_card_cornerCells_add_one` (`YoungLatticeDifferential`) —
  `a(μ) = r(μ) + 1`.

Summing the first over a whole rank gives

    Σ_{λ of size n+1} r(λ)  =  Σ_{ν of size n} a(ν),

and feeding the second into the right-hand side gives

    Σ_{λ of size n+1} r(λ)  =  Σ_{ν of size n} r(ν)  +  #{diagrams of size n}.

Both are verified numerically for `n = 0..10` before formalisation (the second reads
1, 2, 4, 7, 12, 19, 30, 45, 67, 97, 139 against partition counts 1, 1, 2, 3, 5, 7, 11,
15, 22, 30, 42).

## Why it is the shape the tower needs

This is the **unweighted** form of the `D U = U D + I` step. The weighted form,
`Σ_λ f^λ r(λ) = n · s(n-1)`, is what turns the branching rule into the involution
recurrence `s(n+1) = s(n) + n·s(n-1)` and hence closes `Σ_λ f^λ = I(n)`. Getting the
unweighted identity first isolates the *reindexing* — which is what this file is — from
the *weighting*, which is what remains.

## Not proved here

The weighted step. Nothing in this file carries an SYT dimension; the sums count
diagrams and cells only.

Pure combinatorics; nothing archimedean (§7c).

## References

- [stanley1999] Enumerative Combinatorics I, §3.21 (differential posets)
-/

namespace QOU.Mathlib

open YoungDiagram Finset

/-- Diagrams of a fixed size form a `Fintype`, transported from `Nat.Partition n` along
`partitionShapeEquiv`. -/
noncomputable instance fintypeSizedDiagram (n : ℕ) :
    Fintype {μ : YoungDiagram // μ.cells.card = n} :=
  Fintype.ofEquiv (Nat.Partition n) (partitionShapeEquiv n)

/-- `CornerPair n` regrouped as a sigma over the diagram. -/
def cornerPairSigma (n : ℕ) :
    CornerPair n ≃ Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
        {c : ℕ × ℕ // c ∈ cornerCells μ.1} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, mem_cornerCells_of_isCornerCell p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, isCornerCell_of_mem_cornerCells q.2.2⟩⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- `AddPair n` regrouped as a sigma over the diagram. -/
def addPairSigma (n : ℕ) :
    AddPair n ≃ Σ ν : {ν : YoungDiagram // ν.cells.card = n},
        {s : ℕ × ℕ // s ∈ addableCells ν.1} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, mem_addableCells_of_isAddableCell p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, isAddableCell_of_mem_addableCells q.2.2⟩⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- **The rank-level exchange.** Summed over a whole rank, the number of removable
corners at size `n+1` equals the number of addable cells at size `n`. This is
`cornerAddEquiv` with both sides regrouped by diagram and counted. -/
theorem sum_cornerCells_succ_eq_sum_addableCells (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, (cornerCells μ.1).card
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n}, (addableCells ν.1).card := by
  classical
  have e : (Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
             {c : ℕ × ℕ // c ∈ cornerCells μ.1})
         ≃ (Σ ν : {ν : YoungDiagram // ν.cells.card = n},
             {s : ℕ × ℕ // s ∈ addableCells ν.1}) :=
    (cornerPairSigma n).symm.trans ((cornerAddEquiv n).trans (addPairSigma n))
  have hcard := Fintype.card_congr e
  simpa [Fintype.card_sigma, Fintype.card_coe] using hcard

/-- **The differential form of the rank exchange.** Feeding `a(ν) = r(ν) + 1` into the
right-hand side: the corner count at size `n+1` exceeds that at size `n` by exactly the
number of diagrams of size `n`. -/
theorem sum_cornerCells_succ (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, (cornerCells μ.1).card
      = (∑ ν : {ν : YoungDiagram // ν.cells.card = n}, (cornerCells ν.1).card)
        + Fintype.card {ν : YoungDiagram // ν.cells.card = n} := by
  classical
  rw [sum_cornerCells_succ_eq_sum_addableCells]
  simp only [card_addableCells_eq_card_cornerCells_add_one]
  rw [Finset.sum_add_distrib]
  simp [Finset.card_univ]

end QOU.Mathlib
