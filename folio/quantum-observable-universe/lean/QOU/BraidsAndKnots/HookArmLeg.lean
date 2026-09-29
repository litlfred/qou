import QOU.BraidsAndKnots.YoungDiagramKernelPincer

/-!
# The arm/leg decomposition of a hook, as reusable lemmas

`YoungDiagramKernelPincer.hookShape_of_hookLen_eq_sum` (the `v = n` carrier lemma) proved its
arm/leg machinery inline as local `have`s: the hook of `(i,j)` is the disjoint union of its **arm**
`{(i,j') : j ≤ j' < λᵢ}` and its **strict leg** `{(i',j) : i < i' < λ'ⱼ}`, both inside the cell set,
with total cardinality `hookLen`.

Depth-1 (`ν_{n−1}`, epic `qou-ec5z`, bean D1) needs the same decomposition but with a *different*
equality analysis: `hookLen = n − 1` means the union misses exactly one cell, so the classification
splits on **which** cell is missed rather than collapsing to the corner. That requires the pieces as
named lemmas rather than as `have`s inside someone else's proof. This file extracts them; the `v = n`
proof is left as-is (it is merged and green).

Nothing here is new mathematics — it is the merged argument, factored.
-/

namespace QOU.BraidsAndKnots.HookArmLeg

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer

/-- The **arm** of a cell: the cells to its right in the same row. -/
def armF (l : List ℕ) (p : ℕ × ℕ) : Finset (ℕ × ℕ) :=
  (Finset.Ico p.2 (l.getD p.1 0)).image (fun j' => (p.1, j'))

/-- The **strict leg** of a cell: the cells strictly below it in the same column. -/
def legF (l : List ℕ) (p : ℕ × ℕ) : Finset (ℕ × ℕ) :=
  (Finset.Ioo p.1 ((conj l).getD p.2 0)).image (fun i' => (i', p.2))

theorem armF_subset (l : List ℕ) (p : ℕ × ℕ) : armF l p ⊆ cells l := by
  intro q hq
  obtain ⟨j', hj', rfl⟩ := Finset.mem_image.mp hq
  rw [mem_cells]
  exact (Finset.mem_Ico.mp hj').2

theorem legF_subset (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ) : legF l p ⊆ cells l := by
  intro q hq
  obtain ⟨i', hi', rfl⟩ := Finset.mem_image.mp hq
  rw [mem_cells]
  refine (lt_countP_iff l hs p.2 i').mp ?_
  have h2 := (Finset.mem_Ioo.mp hi').2
  rwa [conj_getD l hs] at h2

theorem armF_legF_disjoint (l : List ℕ) (p : ℕ × ℕ) : Disjoint (armF l p) (legF l p) := by
  rw [Finset.disjoint_left]
  intro q hqa hql
  obtain ⟨j', _, rfl⟩ := Finset.mem_image.mp hqa
  obtain ⟨i', hi', h'⟩ := Finset.mem_image.mp hql
  simp only [Prod.mk.injEq] at h'
  have h1 := (Finset.mem_Ioo.mp hi').1
  omega

theorem hookUnion_subset (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ) :
    armF l p ∪ legF l p ⊆ cells l :=
  Finset.union_subset (armF_subset l p) (legF_subset l hs p)

/-- **The hook's cardinality**: `|arm ∪ strict leg| = hookLen`. -/
theorem card_hookUnion (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ) (hp : p ∈ cells l) :
    (armF l p ∪ legF l p).card = hookLen l p := by
  have hinj1 : Function.Injective (fun j' : ℕ => (p.1, j')) := fun a b h => by
    simpa using congrArg Prod.snd h
  have hinj2 : Function.Injective (fun i' : ℕ => (i', p.2)) := fun a b h => by
    simpa using congrArg Prod.fst h
  rw [mem_cells] at hp
  have hcol : p.1 < (conj l).getD p.2 0 := by
    rw [conj_getD l hs]
    exact (lt_countP_iff l hs p.2 p.1).mpr hp
  rw [Finset.card_union_of_disjoint (armF_legF_disjoint l p), armF, legF,
    Finset.card_image_of_injective _ hinj1, Finset.card_image_of_injective _ hinj2,
    Nat.card_Ico, Nat.card_Ioo]
  unfold hookLen
  omega

/-! ## Depth-1: the hook misses exactly one cell

The equality analysis `(TAIL)` depth-1 needs (bean `qou-ckyw`). At `hookLen = n − 1` the arm/leg
union sits inside the `n`-cell set with `n − 1` elements, so its complement is a **singleton** — and
the depth-1 carrier classification is then a case split on which cell that is. -/

/-- **At `hookLen = n − 1` the complement of the hook is a singleton.** -/
theorem card_sdiff_hookUnion_eq_one (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 1 = l.sum) :
    ((cells l) \ (armF l p ∪ legF l p)).card = 1 := by
  rw [Finset.card_sdiff, Finset.inter_eq_left.mpr (hookUnion_subset l hs p), card_cells,
    card_hookUnion l hs p hp]
  omega

/-- The missed cell, named: at `hookLen = n − 1` there is exactly one cell outside the hook. -/
theorem exists_unique_missed_cell (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 1 = l.sum) :
    ∃ c, (cells l) \ (armF l p ∪ legF l p) = {c} :=
  Finset.card_eq_one.mp (card_sdiff_hookUnion_eq_one l hs p hp heq)

/-! ## Membership criteria, and the first step of the depth-1 case analysis -/

/-- Membership in the arm, unfolded. -/
theorem mem_armF_iff (l : List ℕ) (p q : ℕ × ℕ) :
    q ∈ armF l p ↔ q.1 = p.1 ∧ p.2 ≤ q.2 ∧ q.2 < l.getD p.1 0 := by
  constructor
  · intro hq
    obtain ⟨j', hj', rfl⟩ := Finset.mem_image.mp hq
    exact ⟨rfl, (Finset.mem_Ico.mp hj').1, (Finset.mem_Ico.mp hj').2⟩
  · rintro ⟨h1, h2, h3⟩
    refine Finset.mem_image.mpr ⟨q.2, Finset.mem_Ico.mpr ⟨h2, h3⟩, ?_⟩
    exact Prod.ext h1.symm rfl

/-- Membership in the strict leg, unfolded. -/
theorem mem_legF_iff (l : List ℕ) (p q : ℕ × ℕ) :
    q ∈ legF l p ↔ q.2 = p.2 ∧ p.1 < q.1 ∧ q.1 < (conj l).getD p.2 0 := by
  constructor
  · intro hq
    obtain ⟨i', hi', rfl⟩ := Finset.mem_image.mp hq
    exact ⟨rfl, (Finset.mem_Ioo.mp hi').1, (Finset.mem_Ioo.mp hi').2⟩
  · rintro ⟨h1, h2, h3⟩
    refine Finset.mem_image.mpr ⟨q.1, Finset.mem_Ioo.mpr ⟨h2, h3⟩, ?_⟩
    exact Prod.ext rfl h1.symm

/-- **The corner is outside every hook but its own.** The hook of `p` meets row `p.1` only from
column `p.2` rightward and column `p.2` only strictly below row `p.1`, so it contains `(0,0)`
exactly when `p = (0,0)`. This is the pivot of the depth-1 case analysis: for any other carrier the
corner is *the* missed cell, which then forces every other cell into the hook. -/
theorem origin_not_mem_hookUnion (l : List ℕ) (p : ℕ × ℕ) (hp : p ≠ (0, 0)) :
    ((0, 0) : ℕ × ℕ) ∉ armF l p ∪ legF l p := by
  intro hmem
  rcases Finset.mem_union.mp hmem with harm | hleg
  · obtain ⟨h1, h2, _⟩ := (mem_armF_iff l p (0, 0)).mp harm
    exact hp (Prod.ext h1.symm (by simpa using Nat.le_zero.mp h2))
  · obtain ⟨_, h2, _⟩ := (mem_legF_iff l p (0, 0)).mp hleg
    exact absurd h2 (Nat.not_lt_zero p.1)

/-- **The carrier lies on the first row or the first column.** If both coordinates were positive
the hook would miss *two* distinct cells — the corner `(0,0)` and `(0, p.2)` — contradicting
`card_sdiff_hookUnion_eq_one`. Combined with the corner lemma this is the case split that pins the
depth-1 carriers. -/
theorem carrier_fst_or_snd_eq_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 1 = l.sum) : p.1 = 0 ∨ p.2 = 0 := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨h1, h2⟩ := hcon
  have hpc : p.2 < l.getD p.1 0 := by rw [mem_cells] at hp; exact hp
  have hilen : p.1 < l.length := by
    by_contra hcon2
    rw [List.getD_eq_default _ _ (le_of_not_gt hcon2)] at hpc
    exact Nat.not_lt_zero p.2 hpc
  have hhead : l.getD p.1 0 ≤ l.getD 0 0 := by
    rw [getD_zero_eq_headD]
    refine mem_le_headD l hs _ ?_
    rw [List.getD_eq_getElem _ _ hilen]
    exact List.getElem_mem hilen
  have hlt0 : p.2 < l.getD 0 0 := lt_of_lt_of_le hpc hhead
  obtain ⟨c, hc⟩ := exists_unique_missed_cell l hs p hp heq
  have hA : ((0 : ℕ), (0 : ℕ)) ∈ (cells l) \ (armF l p ∪ legF l p) := by
    refine Finset.mem_sdiff.mpr ⟨?_, origin_not_mem_hookUnion l p ?_⟩
    · rw [mem_cells]; dsimp only; omega
    · intro hpe; exact h1 (congrArg Prod.fst hpe)
  have hB : ((0 : ℕ), p.2) ∈ (cells l) \ (armF l p ∪ legF l p) := by
    refine Finset.mem_sdiff.mpr ⟨by rw [mem_cells]; exact hlt0, ?_⟩
    intro hmem
    rcases Finset.mem_union.mp hmem with harm | hleg
    · exact h1 ((mem_armF_iff l p (0, p.2)).mp harm).1.symm
    · exact absurd ((mem_legF_iff l p (0, p.2)).mp hleg).2.1 (Nat.not_lt_zero p.1)
  rw [hc, Finset.mem_singleton] at hA hB
  exact h2 (congrArg Prod.snd (hA.trans hB.symm)).symm

/-- **The depth-1 carrier is one of three cells**: `(0,0)`, `(0,1)` or `(1,0)`.

`carrier_fst_or_snd_eq_zero` puts it on row 0 or column 0; pushing further out along either
axis produces a *second* missed cell — `(0,1)` in the row case, `(1,0)` in the column case —
contradicting the singleton. These are exactly the carriers of the second-instance audit's three
shapes: two-corner `(a,2,1^c)` at `(0,0)`, row `(n)` at `(0,1)`, column `(1^n)` at `(1,0)`. -/
theorem carrier_mem_three (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 1 = l.sum) :
    p = (0, 0) ∨ p = (0, 1) ∨ p = (1, 0) := by
  have hpc : p.2 < l.getD p.1 0 := by rw [mem_cells] at hp; exact hp
  obtain ⟨c, hc⟩ := exists_unique_missed_cell l hs p hp heq
  have hmissed : ∀ q : ℕ × ℕ, q ∈ cells l → q ∉ armF l p ∪ legF l p → q = c := by
    intro q hq hnot
    have hqs : q ∈ (cells l) \ (armF l p ∪ legF l p) := Finset.mem_sdiff.mpr ⟨hq, hnot⟩
    rw [hc, Finset.mem_singleton] at hqs
    exact hqs
  rcases carrier_fst_or_snd_eq_zero l hs p hp heq with h1 | h2
  · rw [h1] at hpc
    by_cases hp2 : p.2 ≤ 1
    · have hcase : p.2 = 0 ∨ p.2 = 1 := by omega
      rcases hcase with h | h
      · exact Or.inl (Prod.ext h1 h)
      · exact Or.inr (Or.inl (Prod.ext h1 h))
    · exfalso
      push_neg at hp2
      have hne : p ≠ (0, 0) := by
        intro he
        have hz : p.2 = 0 := congrArg Prod.snd he
        omega
      have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by rw [mem_cells]; dsimp only; omega
      have h01 : ((0 : ℕ), (1 : ℕ)) ∈ cells l := by rw [mem_cells]; dsimp only; omega
      have hnot01 : ((0 : ℕ), (1 : ℕ)) ∉ armF l p ∪ legF l p := by
        intro hmem
        rcases Finset.mem_union.mp hmem with harm | hleg
        · have := ((mem_armF_iff l p (0, 1)).mp harm).2.1
          omega
        · exact absurd ((mem_legF_iff l p (0, 1)).mp hleg).2.1 (Nat.not_lt_zero p.1)
      have hA := hmissed (0, 0) h00 (origin_not_mem_hookUnion l p hne)
      have hB := hmissed (0, 1) h01 hnot01
      have hcontra : (0 : ℕ) = 1 := congrArg Prod.snd (hA.trans hB.symm)
      omega
  · rw [h2] at hpc
    by_cases hp1 : p.1 ≤ 1
    · have hcase : p.1 = 0 ∨ p.1 = 1 := by omega
      rcases hcase with h | h
      · exact Or.inl (Prod.ext h h2)
      · exact Or.inr (Or.inr (Prod.ext h h2))
    · exfalso
      push_neg at hp1
      have hcount : p.1 < l.countP (fun x => decide (0 < x)) :=
        (lt_countP_iff l hs 0 p.1).mpr hpc
      have h10 : ((1 : ℕ), (0 : ℕ)) ∈ cells l := by
        rw [mem_cells]; exact (lt_countP_iff l hs 0 1).mp (by omega)
      have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := by
        rw [mem_cells]; exact (lt_countP_iff l hs 0 0).mp (by omega)
      have hne : p ≠ (0, 0) := by
        intro he
        have hz : p.1 = 0 := congrArg Prod.fst he
        omega
      have hnot10 : ((1 : ℕ), (0 : ℕ)) ∉ armF l p ∪ legF l p := by
        intro hmem
        rcases Finset.mem_union.mp hmem with harm | hleg
        · have := ((mem_armF_iff l p (1, 0)).mp harm).1
          omega
        · have := ((mem_legF_iff l p (1, 0)).mp hleg).2.1
          omega
      have hA := hmissed (0, 0) h00 (origin_not_mem_hookUnion l p hne)
      have hB := hmissed (1, 0) h10 hnot10
      have hcontra : (0 : ℕ) = 1 := congrArg Prod.fst (hA.trans hB.symm)
      omega

end QOU.BraidsAndKnots.HookArmLeg
