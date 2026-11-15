import QOU.Mathlib.YoungLatticeCornerCount
import QOU.Mass.InvolutionNumbers
import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.SchenstedPartitionShape

/-!
# `QOU.Mass.SumSYTEqInvolution` — `∑_{λ ⊢ n} f^λ = I(n)`

The Robinson–Schensted corollary, proved **without RSK**.

`QOU.Mathlib.sum_numSYT_recurrence'` gives, unconditionally,

    s(n+2) = s(n+1) + (n+1)·s(n),        s(k) := ∑_{|μ| = k} #SYT(μ),

which is verbatim the recurrence defining `QOU.Mass.involutionNumber`
(`involutionNumber_succ_succ`).  All that is left is the two base cases, and this file
supplies them:

* `numStandardYoungTableaux_bot` — the empty shape carries exactly one tableau.  Both halves
  are proved rather than assumed: `Subsingleton` because every entry of a tableau on `⊥` is
  forced to `0` by `SemistandardYoungTableau.zeros`, and `Nonempty` by exhibiting that
  tableau (`botSsyt`, whose row/column conditions are vacuous and whose `Set.BijOn` obligation
  is `∅ → Set.Icc 1 0`).
* `sum_numSYT_size_zero` — `s(0) = 1`, since `⊥` is the *only* diagram with no cells.
* `sum_numSYT_size_one` — `s(1) = 1`, read off `sum_numSYT_succ_split 0`: the corner-weighted
  term vanishes because `⊥` has no removable corner, leaving `s(1) = s(0)`.

Composing with `card_involutions_eq_involutionNumber` (already in `InvolutionNumbers`)
gives `sum_numSYT_eq_card_involutions`: the sum of SYT counts over a rank equals the number
of involutions in `S_n` — the statement RSK is normally invoked for.

## Why this is not circular

Nothing here counts involutions by tableaux.  `involutionNumber` is defined by its
recurrence and is separately proved to count involutions; the SYT side reaches the same
recurrence through the differential-poset structure of Young's lattice
(`QOU.Mathlib.upSum_eq`).  The two are then matched as sequences.

Base ring: `ℕ` throughout — pure counting, nothing archimedean (§7c).

## References

- [stanley1999ec2] Enumerative Combinatorics I, §3.21 (differential posets)
- [leitner2026] QOU/Mathlib/YoungLatticeUpOperator.lean
-/

namespace QOU.Mathlib

open YoungDiagram Finset

/-! ### The empty shape carries exactly one tableau -/

instance : Subsingleton (StandardYoungTableau (⊥ : YoungDiagram)) := by
  constructor
  intro T1 T2
  have hall : ∀ i j, T1.toSsyt i j = T2.toSsyt i j := by
    intro i j
    rw [T1.toSsyt.zeros (by simp), T2.toSsyt.zeros (by simp)]
  have h := SemistandardYoungTableau.ext hall
  cases T1; cases T2; cases h; rfl

/-- The unique semistandard tableau of the empty shape: every entry is `0`, and both the row
and column conditions are vacuous because no cell is in `⊥`. -/
def botSsyt : SemistandardYoungTableau (⊥ : YoungDiagram) where
  entry := fun _ _ => 0
  row_weak' := by intro i j1 j2 _ hcell; simp at hcell
  col_strict' := by intro i1 i2 j _ hcell; simp at hcell
  zeros' := by intro i j _; rfl

instance : Nonempty (StandardYoungTableau (⊥ : YoungDiagram)) :=
  ⟨{ toSsyt := botSsyt
     bijOn := by
       refine ⟨?_, ?_, ?_⟩
       · intro c hc; simp at hc
       · intro a ha; simp at ha
       · intro y hy; simp at hy }⟩

/-- `#SYT(∅) = 1`. -/
theorem numStandardYoungTableaux_bot : numStandardYoungTableaux (⊥ : YoungDiagram) = 1 := by
  unfold numStandardYoungTableaux
  exact Nat.card_eq_one_iff_unique.mpr ⟨inferInstance, inferInstance⟩

/-- A diagram with no cells is the empty diagram. -/
theorem eq_bot_of_card_eq_zero {μ : YoungDiagram} (h : μ.cells.card = 0) : μ = ⊥ :=
  YoungDiagram.ext (by simpa using Finset.card_eq_zero.mp h)

/-- The empty diagram has no removable corner. -/
theorem cornerCells_bot : cornerCells (⊥ : YoungDiagram) = ∅ := by
  rw [Finset.eq_empty_iff_forall_notMem]
  intro c hc
  rw [mem_cornerCells] at hc
  simpa using hc.1

/-! ### The two base cases -/

/-- `s(0) = 1`. -/
theorem sum_numSYT_size_zero :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = 0}, numStandardYoungTableaux μ.1 = 1 := by
  classical
  have hbot : (⊥ : YoungDiagram).cells.card = 0 := by simp
  have huniq : ∀ x : {μ : YoungDiagram // μ.cells.card = 0}, x = ⟨⊥, hbot⟩ :=
    fun x => Subtype.ext (eq_bot_of_card_eq_zero x.2)
  have hcard : Fintype.card {μ : YoungDiagram // μ.cells.card = 0} = 1 :=
    Fintype.card_eq_one_iff.mpr ⟨⟨⊥, hbot⟩, huniq⟩
  have hconst : ∀ x ∈ (Finset.univ : Finset {μ : YoungDiagram // μ.cells.card = 0}),
      numStandardYoungTableaux x.1 = numStandardYoungTableaux (⊥ : YoungDiagram) := by
    intro x _
    rw [huniq x]
  rw [Finset.sum_const_nat hconst, Finset.card_univ, hcard,
    numStandardYoungTableaux_bot]

/-- `s(1) = 1`.  Read off the rank-`0` case of `sum_numSYT_succ_split`: the corner-weighted
term vanishes because `⊥` has no removable corner. -/
theorem sum_numSYT_size_one :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = 1}, numStandardYoungTableaux μ.1 = 1 := by
  classical
  have hbot : (⊥ : YoungDiagram).cells.card = 0 := by simp
  have hzero : ∀ ν : {ν : YoungDiagram // ν.cells.card = 0},
      numStandardYoungTableaux ν.1 * (cornerCells ν.1).card = 0 := by
    intro ν
    rw [show ν.1 = (⊥ : YoungDiagram) from eq_bot_of_card_eq_zero ν.2, cornerCells_bot]
    simp
  have := sum_numSYT_succ_split 0
  rw [Finset.sum_congr rfl (fun ν _ => hzero ν), Finset.sum_const_nat (fun _ _ => rfl)] at this
  rw [show (0 : ℕ) + 1 = 1 from rfl] at this
  rw [this, sum_numSYT_size_zero]
  simp

end QOU.Mathlib

namespace QOU.Mass

open QOU.Mathlib

/-- **`∑_{λ ⊢ n} f^λ = I(n)`.**  Sorry-free, and without RSK: the left side satisfies the
involution recurrence by the differential-poset structure of Young's lattice
(`QOU.Mathlib.sum_numSYT_recurrence'`), the right side by definition, and the two base
cases match. -/
theorem sum_numSYT_eq_involutionNumber (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, numStandardYoungTableaux μ.1
      = involutionNumber n := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 => exact sum_numSYT_size_zero
    | 1 => exact sum_numSYT_size_one
    | (k + 2) =>
      rw [sum_numSYT_recurrence' k, ih (k + 1) (by omega), ih k (by omega),
        involutionNumber_succ_succ]

/-- **The Robinson–Schensted corollary**: the sum of SYT counts over the shapes of size `n`
is the number of involutions in `S_n`.  Obtained by composing
`sum_numSYT_eq_involutionNumber` with `card_involutions_eq_involutionNumber`, neither of
which counts involutions by tableaux — so the identity is not circular. -/
theorem sum_numSYT_eq_card_involutions (n : ℕ) :
    ∑ μ : {μ : YoungDiagram // μ.cells.card = n}, numStandardYoungTableaux μ.1
      = Fintype.card {σ : Equiv.Perm (Fin n) // σ * σ = 1} := by
  rw [sum_numSYT_eq_involutionNumber, ← card_involutions_eq_involutionNumber]

/-- The same identity indexed by `Nat.Partition n` rather than by sized diagrams — the shape
`RSKIdentitiesContext.sum_dimSYT_eq_involution` is stated in.  `dimSYT p` is by definition
`#SYT (partitionShape p)`, and `partitionShapeEquiv` matches the two index types. -/
theorem sum_dimSYT_eq_involutionNumber (n : ℕ) :
    (∑ p : Nat.Partition n, dimSYT p) = involutionNumber n := by
  classical
  rw [← sum_numSYT_eq_involutionNumber n]
  refine Fintype.sum_equiv (partitionShapeEquiv n) _ _ (fun p => ?_)
  rw [partitionShapeEquiv_apply]
  rfl

/-- **`RSKIdentitiesContext.sum_dimSYT_eq_involution`'s exact statement.**  Kept as a named
alias because that field is stated over `Nat.Partition` while the theorem above is the natural
form; they are now literally the same proposition, since `KeystoneC8SuperExpBound` no longer
carries its own copy of `involutionNumber`. -/
theorem sum_dimSYT_eq_involution_keystone (k : ℕ) :
    (∑ p : Nat.Partition k, dimSYT p) = involutionNumber k :=
  sum_dimSYT_eq_involutionNumber k

end QOU.Mass
