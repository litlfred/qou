import QOU.Mathlib.YoungLatticeExchange
import QOU.Mathlib.SchenstedPartitionShape
import QOU.Mathlib.SYTBranchingRule

/-!
# QOU.Mathlib.YoungLatticeCornerCount — the corner/addable exchange, summed over a rank

The rank-level consequence of the two ingredients already proved:

* `sizedCornerAddEquiv` (`YoungLatticeExchange`, on the `YoungDiagramAddable` API) — the pointwise exchange
  `(λ, removable corner) ≃ (λ ∖ c, that corner as an addable one)`;
* `card_addableCells_eq_card_cornerCells_succ` (`YoungDiagramAddable`) —
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

/-- `SizedCornerPair n` regrouped as a sigma over the diagram. -/
def sizedCornerPairSigma (n : ℕ) :
    SizedCornerPair n ≃ Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
        {c : ℕ × ℕ // c ∈ cornerCells μ.1} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, (mem_cornerCells _ _).mpr p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, (mem_cornerCells _ _).mp q.2.2⟩⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- `SizedAddPair n` regrouped as a sigma over the diagram. -/
def sizedAddPairSigma (n : ℕ) :
    SizedAddPair n ≃ Σ ν : {ν : YoungDiagram // ν.cells.card = n},
        {s : ℕ × ℕ // s ∈ addableCells ν.1} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, (mem_addableCells _ _).mpr p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, (mem_addableCells _ _).mp q.2.2⟩⟩
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
    (sizedCornerPairSigma n).symm.trans ((sizedCornerAddEquiv n).trans (sizedAddPairSigma n))
  have hcard := Fintype.card_congr e
  simpa [Fintype.card_sigma, Fintype.card_coe, -mem_cornerCells, -mem_addableCells] using hcard

/-- **The differential form of the rank exchange.** Feeding `a(ν) = r(ν) + 1` into the
right-hand side: the corner count at size `n+1` exceeds that at size `n` by exactly the
number of diagrams of size `n`. -/
theorem sum_cornerCells_succ (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, (cornerCells μ.1).card
      = (∑ ν : {ν : YoungDiagram // ν.cells.card = n}, (cornerCells ν.1).card)
        + Fintype.card {ν : YoungDiagram // ν.cells.card = n} := by
  classical
  rw [sum_cornerCells_succ_eq_sum_addableCells]
  simp only [card_addableCells_eq_card_cornerCells_succ]
  rw [Finset.sum_add_distrib]
  simp [Finset.card_univ]

/-! ## The weighted exchange

The same regrouping, now carrying `#SYT` of the SMALLER diagram as a weight. Under
`cornerAddEquiv` the pair `(λ, c)` goes to `(λ ∖ c, c)`, so a weight of
`#SYT (λ ∖ c)` on the corner side becomes a weight of `#SYT ν` on the addable side —
depending only on the diagram, which is what lets it factor out of the inner sum.
-/

/-- Addable cells of a fixed diagram form a `Fintype`, via `addableCells`. (The corner
counterpart already exists as `SYTBranchingRule.fintypeCorners`; there is no competing
instance for the addable side.) -/
instance fintypeAddableSubtype (ν : YoungDiagram) :
    Fintype {s : ℕ × ℕ // IsAddableCell ν s} :=
  Fintype.ofFinset (addableCells ν) (fun _ => mem_addableCells _ _)

/-- `SizedCornerPair n` as a sigma, indexed by the branching theorem's corner subtype. -/
def sizedCornerPairSigma' (n : ℕ) :
    SizedCornerPair n ≃ Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
        {c : ℕ × ℕ // IsCornerCell μ.1 c} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, q.2.2⟩⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- `SizedAddPair n` as a sigma, indexed by `IsAddableCell`. -/
def sizedAddPairSigma' (n : ℕ) :
    SizedAddPair n ≃ Σ ν : {ν : YoungDiagram // ν.cells.card = n},
        {s : ℕ × ℕ // IsAddableCell ν.1 s} where
  toFun p := ⟨⟨p.1.1, p.2.1⟩, ⟨p.1.2, p.2.2⟩⟩
  invFun q := ⟨(q.1.1, q.2.1), ⟨q.1.2, q.2.2⟩⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- The rank exchange as a single equiv of sigma types: `cornerAddEquiv` with both sides
regrouped by diagram. Kept as a top-level `def` (rather than a `have` inside the proof)
so that the weight-matching step can unfold it. -/
def rankExchange (n : ℕ) :
    (Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, {c : ℕ × ℕ // IsCornerCell μ.1 c})
      ≃ (Σ ν : {ν : YoungDiagram // ν.cells.card = n}, {s : ℕ × ℕ // IsAddableCell ν.1 s}) :=
  (sizedCornerPairSigma' n).symm.trans ((sizedCornerAddEquiv n).trans (sizedAddPairSigma' n))

@[simp] theorem rankExchange_fst_fst (n : ℕ)
    (x : Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, {c : ℕ × ℕ // IsCornerCell μ.1 c}) :
    ((rankExchange n x).1 : YoungDiagram) = eraseCorner x.1.1 x.2.1 x.2.2 := rfl

set_option maxHeartbeats 1000000 in
/-- **The weighted rank exchange.** Summing `#SYT` over a whole rank equals summing, one
rank down, `#SYT ν` times the number of addable cells of `ν`:

    s(n+1) = Σ_{ν of size n} #SYT(ν) · a(ν).

The left side is the branching rule summed over the rank; the right side is the same sum
reindexed by `cornerAddEquiv`. -/
theorem sum_numSYT_succ (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, numStandardYoungTableaux μ.1
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          numStandardYoungTableaux ν.1 * Fintype.card {s : ℕ × ℕ // IsAddableCell ν.1 s} := by
  classical
  -- (1) branching, applied rankwise
  have hbranch : ∀ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
      numStandardYoungTableaux μ.1
        = ∑ c : {c : ℕ × ℕ // IsCornerCell μ.1 c},
            numStandardYoungTableaux (eraseCorner μ.1 c.1 c.2) := by
    intro μ
    exact numStandardYoungTableaux_branching (by rw [μ.2]; omega)
  -- (2) the weight matches across the exchange: erase-then-index = index-of-target
  have hw : ∀ x : (Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
                    {c : ℕ × ℕ // IsCornerCell μ.1 c}),
      numStandardYoungTableaux (eraseCorner x.1.1 x.2.1 x.2.2)
        = numStandardYoungTableaux (rankExchange n x).1.1 := by
    intro x
    rw [rankExchange_fst_fst]
  calc ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, numStandardYoungTableaux μ.1
      = ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
          ∑ c : {c : ℕ × ℕ // IsCornerCell μ.1 c},
            numStandardYoungTableaux (eraseCorner μ.1 c.1 c.2) :=
        Finset.sum_congr rfl fun μ _ => hbranch μ
    _ = ∑ x : (Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
                {c : ℕ × ℕ // IsCornerCell μ.1 c}),
          numStandardYoungTableaux (eraseCorner x.1.1 x.2.1 x.2.2) :=
        (Fintype.sum_sigma
          (fun x : (Σ μ : {μ : YoungDiagram // μ.cells.card = n + 1},
                     {c : ℕ × ℕ // IsCornerCell μ.1 c}) =>
            numStandardYoungTableaux (eraseCorner x.1.1 x.2.1 x.2.2))).symm
    _ = ∑ y : (Σ ν : {ν : YoungDiagram // ν.cells.card = n},
                {s : ℕ × ℕ // IsAddableCell ν.1 s}),
          numStandardYoungTableaux y.1.1 :=
        Fintype.sum_equiv (rankExchange n) _ _ (fun x => hw x)
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          ∑ _s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, numStandardYoungTableaux ν.1 :=
        Fintype.sum_sigma
          (fun y : (Σ ν : {ν : YoungDiagram // ν.cells.card = n},
                     {s : ℕ × ℕ // IsAddableCell ν.1 s}) =>
            numStandardYoungTableaux y.1.1)
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          numStandardYoungTableaux ν.1 * Fintype.card {s : ℕ × ℕ // IsAddableCell ν.1 s} := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [Finset.sum_const, Finset.card_univ, smul_eq_mul, mul_comm]

/-- **The recurrence's shape.** Feeding the differential property `a(ν) = r(ν) + 1` into
the weighted exchange splits it:

    s(n+1) = s(n) + Σ_{ν of size n} #SYT(ν) · r(ν).

Compare the involution recurrence `I(n+2) = I(n+1) + (n+1)·I(n)`. The two agree exactly
when `Σ_ν #SYT(ν)·r(ν) = n · s(n-1)` — the one step still open, and now the *only* thing
between this file and `Σ_λ f^λ = I(n)`. -/
theorem sum_numSYT_succ_split (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, numStandardYoungTableaux μ.1
      = (∑ ν : {ν : YoungDiagram // ν.cells.card = n}, numStandardYoungTableaux ν.1)
        + ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
            numStandardYoungTableaux ν.1 * (cornerCells ν.1).card := by
  classical
  rw [sum_numSYT_succ]
  have h : ∀ ν : {ν : YoungDiagram // ν.cells.card = n},
      Fintype.card {s : ℕ × ℕ // IsAddableCell ν.1 s} = (cornerCells ν.1).card + 1 := by
    intro ν
    rw [Fintype.card_of_subtype (addableCells ν.1) (fun _ => mem_addableCells _ _),
        card_addableCells_eq_card_cornerCells_succ]
  calc ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          numStandardYoungTableaux ν.1 * Fintype.card {s : ℕ × ℕ // IsAddableCell ν.1 s}
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (numStandardYoungTableaux ν.1 * (cornerCells ν.1).card
            + numStandardYoungTableaux ν.1) := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [h ν, Nat.mul_add, mul_one]
    _ = (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
            numStandardYoungTableaux ν.1 * (cornerCells ν.1).card)
          + ∑ ν : {ν : YoungDiagram // ν.cells.card = n}, numStandardYoungTableaux ν.1 :=
        Finset.sum_add_distrib
    _ = (∑ ν : {ν : YoungDiagram // ν.cells.card = n}, numStandardYoungTableaux ν.1)
          + ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
              numStandardYoungTableaux ν.1 * (cornerCells ν.1).card := Nat.add_comm _ _

/-! ## The last step, reduced to a pointwise identity

What remains between this file and `Σ_λ f^λ = I(n)` is

    Σ_{ν of size n+1} #SYT(ν)·r(ν) = (n+1) · s(n).

Reindexing it by `rankExchange` (weight = `#SYT` of the BIGGER diagram this time, which
the exchange reconstructs as `addCell μ s`) turns it into a sum of *pointwise* statements.
The pointwise statement is the classical **up-operator identity** of Young's lattice:

    Σ_{λ = μ + box} #SYT(λ) = (|μ| + 1) · #SYT(μ).

Verified with zero counterexamples over every partition of `0..9` (97 shapes). It is
carried here as an explicit hypothesis, NOT asserted: its own proof needs the
differential-poset induction, which this file does not do. -/

/-- **The up-operator identity of Young's lattice**, as a named hypothesis.
`Σ_{λ = μ + box} #SYT(λ) = (|μ| + 1)·#SYT(μ)`. Open in this corpus; see bean `qou-jlam`. -/
def UpOperatorIdentity : Prop :=
  ∀ (m : ℕ) (μ : YoungDiagram), μ.cells.card = m →
    ∑ s : {s : ℕ × ℕ // IsAddableCell μ s},
        numStandardYoungTableaux (addCell μ s.1 s.2) = (m + 1) * numStandardYoungTableaux μ

set_option maxHeartbeats 1000000 in
/-- **The weighted corner sum, reduced.** Given the up-operator identity, the corner-weighted
rank sum is exactly `(n+1)·s(n)` — which is the coefficient the involution recurrence needs. -/
theorem sum_numSYT_mul_corners_of_upOperator (h : UpOperatorIdentity) (n : ℕ) :
    ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
        numStandardYoungTableaux ν.1 * Fintype.card {c : ℕ × ℕ // IsCornerCell ν.1 c}
      = (n + 1) * ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, numStandardYoungTableaux μ.1 := by
  classical
  -- weight on the corner side is #SYT of the BIGGER diagram; the exchange rebuilds it
  have hw : ∀ x : (Σ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
                    {c : ℕ × ℕ // IsCornerCell ν.1 c}),
      numStandardYoungTableaux x.1.1
        = numStandardYoungTableaux
            (addCell (rankExchange n x).1.1 (rankExchange n x).2.1 (rankExchange n x).2.2) := by
    intro x
    congr 1
    exact (addCell_eraseCorner' x.2.1 x.2.2 (isAddableCell_eraseCorner' x.2.1 x.2.2)).symm
  calc ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
          numStandardYoungTableaux ν.1 * Fintype.card {c : ℕ × ℕ // IsCornerCell ν.1 c}
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
          ∑ _c : {c : ℕ × ℕ // IsCornerCell ν.1 c}, numStandardYoungTableaux ν.1 := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [Finset.sum_const, Finset.card_univ, smul_eq_mul, mul_comm]
    _ = ∑ x : (Σ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
                {c : ℕ × ℕ // IsCornerCell ν.1 c}), numStandardYoungTableaux x.1.1 :=
        (Fintype.sum_sigma
          (fun x : (Σ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
                     {c : ℕ × ℕ // IsCornerCell ν.1 c}) =>
            numStandardYoungTableaux x.1.1)).symm
    _ = ∑ y : (Σ μ : {μ : YoungDiagram // μ.cells.card = n},
                {s : ℕ × ℕ // IsAddableCell μ.1 s}),
          numStandardYoungTableaux (addCell y.1.1 y.2.1 y.2.2) :=
        Fintype.sum_equiv (rankExchange n) _ _ (fun x => hw x)
    _ = ∑ μ : {μ : YoungDiagram // μ.cells.card = n},
          ∑ s : {s : ℕ × ℕ // IsAddableCell μ.1 s},
            numStandardYoungTableaux (addCell μ.1 s.1 s.2) :=
        Fintype.sum_sigma
          (fun y : (Σ μ : {μ : YoungDiagram // μ.cells.card = n},
                     {s : ℕ × ℕ // IsAddableCell μ.1 s}) =>
            numStandardYoungTableaux (addCell y.1.1 y.2.1 y.2.2))
    _ = ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, (n + 1) * numStandardYoungTableaux μ.1 :=
        Finset.sum_congr rfl fun μ _ => h n μ.1 μ.2
    _ = (n + 1) * ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, numStandardYoungTableaux μ.1 :=
        (Finset.mul_sum _ _ _).symm

set_option maxHeartbeats 1000000 in
/-- **The involution recurrence, conditional on the up-operator identity.**

    s(n+2) = s(n+1) + (n+1)·s(n),      s(k) := Σ_{μ of size k} #SYT(μ).

This is *exactly* the recurrence defining the involution numbers,
`I(n+2) = I(n+1) + (n+1)·I(n)` (`QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber`).
With matching base cases `s(0) = s(1) = 1` it gives `Σ_{λ⊢n} f^λ = I(n)` — the identity
that licenses reading the involution numbers as the `q = 1` na-Stokes period in
`QOU.Mass.SWPeriodSuperExponential`, and the open target of beans `qou-m3xr` / `qou-jlam`.

**Everything here is proved except `UpOperatorIdentity`**, which is carried as an explicit
hypothesis and is the single remaining obligation. It is not asserted anywhere in this
file; §3b-cond, and "conditional-proved ≠ premise-established". -/
theorem sum_numSYT_recurrence (h : UpOperatorIdentity) (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n + 2}, numStandardYoungTableaux μ.1
      = (∑ μ : {μ : YoungDiagram // μ.cells.card = n + 1}, numStandardYoungTableaux μ.1)
        + (n + 1) * ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, numStandardYoungTableaux μ.1 := by
  classical
  rw [sum_numSYT_succ_split (n + 1), ← sum_numSYT_mul_corners_of_upOperator h n]
  congr 1
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [card_cornerCells_eq_card_subtype]

end QOU.Mathlib
