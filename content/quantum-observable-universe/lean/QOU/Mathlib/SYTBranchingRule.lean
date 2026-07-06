import QOU.Mathlib.SYTBranchingBijection

/-!
# QOU.Mathlib.SYTBranchingRule — the structural GNW branching count

Packaging the deletion/insertion bijection (`SYTBranchingBijection`) as a cardinality identity: for a
**non-empty** Young diagram `μ`,

    numStandardYoungTableaux μ = ∑_{removable corners c} numStandardYoungTableaux (μ ∖ c).

The bijection `⨆_{corners c} SYT(μ ∖ c) → SYT μ`, `(c, S) ↦ insertMax c S`, is shown bijective
(surjective by re-inserting the max value; injective because the inserted corner is recovered as the
unique max-value cell, then the roundtrip pins `S`).  `Equiv.ofBijective` + `Nat.card_sigma` give the
sum.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

instance instDecidableIsCornerCell (μ : YoungDiagram) (c : ℕ × ℕ) : Decidable (IsCornerCell μ c) := by
  unfold IsCornerCell; infer_instance

/-- The removable corners of `μ` form a finite type (they sit inside the finite cell set). -/
noncomputable instance fintypeCorners (μ : YoungDiagram) :
    Fintype {c : ℕ × ℕ // IsCornerCell μ c} := by
  apply Set.Finite.fintype
  apply Set.Finite.subset μ.cells.finite_toSet
  intro c hc
  exact Finset.mem_coe.mpr ((mem_cells _).mpr hc.1)

/-- The inverse branching map on the corner-indexed disjoint union: re-insert `|μ|` at corner `c`. -/
def branchInv (p : Σ c : {c : ℕ × ℕ // IsCornerCell μ c}, StandardYoungTableau (eraseCorner μ c.1 c.2)) :
    StandardYoungTableau μ :=
  insertMax p.1.1 p.1.2 p.2

/-- `branchInv` is surjective: every `T` is the re-insertion at its max corner of the deletion of that
corner. -/
theorem branchInv_surjective (hμ : 0 < μ.cells.card) : Function.Surjective (branchInv (μ := μ)) := by
  intro T
  obtain ⟨c, _hcμ, hc, hmax⟩ := exists_corner_entry_eq_card T hμ
  exact ⟨⟨⟨c, hc⟩, eraseMax T c hc hmax⟩, insertMax_eraseMax T c hc hmax⟩

/-- `branchInv` is injective: the inserted corner is recovered as the unique max-value cell, then the
deletion roundtrip pins the tableau. -/
theorem branchInv_injective : Function.Injective (branchInv (μ := μ)) := by
  rintro ⟨a1, S1⟩ ⟨a2, S2⟩ hpq
  simp only [branchInv] at hpq
  -- recover the corner: both `a1.1` and `a2.1` carry the top value `|μ|` in the common tableau
  have e1 : (insertMax a1.1 a1.2 S1).entry a1.1.1 a1.1.2 = μ.cells.card :=
    entry_insertMax_corner a1.1 a1.2 S1
  have e2 : (insertMax a2.1 a2.2 S2).entry a2.1.1 a2.1.2 = μ.cells.card :=
    entry_insertMax_corner a2.1 a2.2 S2
  rw [hpq] at e1
  have hm1 : a1.1 ∈ (μ.cells : Set (ℕ × ℕ)) := Finset.mem_coe.mpr ((mem_cells _).mpr a1.2.1)
  have hm2 : a2.1 ∈ (μ.cells : Set (ℕ × ℕ)) := Finset.mem_coe.mpr ((mem_cells _).mpr a2.2.1)
  have hc12 : a1.1 = a2.1 := (insertMax a2.1 a2.2 S2).injOn_cells hm1 hm2 (e1.trans e2.symm)
  have ha : a1 = a2 := Subtype.ext hc12
  subst a2
  -- both fibers now live over `eraseCorner μ a1.1 a1.2`; the deletion roundtrip pins `S`
  have hS : S1 = S2 := by
    apply syt_ext
    intro i j
    by_cases hij : (i, j) = a1.1
    · have hz1 : S1.entry i j = 0 :=
        S1.toSsyt.zeros (by rw [hij]; exact fun h => ((mem_eraseCorner μ a1.1 a1.2 a1.1).mp h).2 rfl)
      have hz2 : S2.entry i j = 0 :=
        S2.toSsyt.zeros (by rw [hij]; exact fun h => ((mem_eraseCorner μ a1.1 a1.2 a1.1).mp h).2 rfl)
      rw [hz1, hz2]
    · have l1 : (insertMax a1.1 a1.2 S1).entry i j = S1.entry i j := by
        show (if (i, j) = a1.1 then μ.cells.card else S1.entry i j) = S1.entry i j
        rw [if_neg hij]
      have l2 : (insertMax a1.1 a1.2 S2).entry i j = S2.entry i j := by
        show (if (i, j) = a1.1 then μ.cells.card else S2.entry i j) = S2.entry i j
        rw [if_neg hij]
      rw [← l1, ← l2, hpq]
  rw [hS]

/-- **The structural GNW branching count.** For a non-empty Young diagram,
`numStandardYoungTableaux μ = ∑_{removable corners c} numStandardYoungTableaux (μ ∖ c)`. -/
theorem numStandardYoungTableaux_branching (hμ : 0 < μ.cells.card) :
    numStandardYoungTableaux μ
      = ∑ c : {c : ℕ × ℕ // IsCornerCell μ c}, numStandardYoungTableaux (eraseCorner μ c.1 c.2) := by
  have hbij : Function.Bijective (branchInv (μ := μ)) :=
    ⟨branchInv_injective, branchInv_surjective hμ⟩
  unfold numStandardYoungTableaux
  rw [← Nat.card_congr (Equiv.ofBijective _ hbij), Nat.card_sigma]

end QOU.Mathlib
