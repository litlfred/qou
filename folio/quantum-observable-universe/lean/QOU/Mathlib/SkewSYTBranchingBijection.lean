import QOU.Mathlib.SkewSYTMaxCorner

/-!
# `QOU.Mathlib.SkewSYTBranchingBijection` — the skew branching rule

`QOU/Mathlib/SkewSYTMaxCorner.lean` built both directions of the erase-max step and stopped
there, recording explicitly that *"both directions built" is not "bijection proved"*.  This
file closes that gap and draws the count:

    f^{outer/inner} = ∑_{c a corner of outer, c ∉ inner}  f^{(outer ∖ c)/inner}.

The shape of the argument is the straight case's (`QOU/Mathlib/SYTBranchingRule.lean`): a map
`⨆_c SkewSYT(outer ∖ c, inner) → SkewSYT(outer, inner)` given by re-inserting the maximum, shown
bijective, then `Equiv.ofBijective` + `Nat.card_sigma`.

## What is genuinely different from the straight case

Three things, and each cost a lemma here rather than a rewrite:

* **The index type carries a second condition.**  The corner must also lie outside `inner`,
  since a corner of `outer` that sits inside `inner` is not a skew cell at all and deleting it
  would break `inner ≤ outer ∖ c`.  So the fibre is indexed by
  `{c // IsCornerCell outer c ∧ c ∉ inner}`, not by corners alone.
* **`content` must be re-derived rather than cited.**  `StandardYoungTableau` hands over
  `bijOn`; `SkewStandardYoungTableau` certifies its filling with a Finset image equality, so
  the erase step has to *recover* `image = range n` from `image = range (n+1)` by erasing the
  top value from both sides.  That is what `skewEraseMax`'s `content` field does.
* **Entries are 0-based.**  The maximum of a skew tableau on `n + 1` cells is `n`, not `n + 1`;
  the straight case's `μ.cells.card` reads as `card - 1` here.  Index arithmetic does not port,
  which is why every statement below carries the size explicitly.

Pure combinatorics; nothing archimedean (§7c); no fit.

## References

- [stanley1999ec2] Enumerative Combinatorics I, §7.10 (skew tableaux)
- [leitner2026] bean `qou-b21r`
-/

namespace QOU.BraidKnot.YoungTableauStandard

open Finset QOU.Mathlib

variable {outer inner : YoungDiagram} {c : ℕ × ℕ}

/-- Two skew tableaux of the same shape are equal when their entry maps agree — the other four
fields are `Prop`s, hence proof-irrelevant. -/
theorem skew_syt_ext {T₁ T₂ : SkewStandardYoungTableau outer inner}
    (h : ∀ i j, T₁.entry i j = T₂.entry i j) : T₁ = T₂ := by
  cases T₁; cases T₂
  congr 1
  funext i j
  exact h i j

/-- A corner outside `inner` is a skew cell. -/
theorem mem_skewCellsOf_of_corner (hc : IsCornerCell outer c) (hcn : c ∉ inner) :
    c ∈ skewCellsOf outer inner := by
  simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells]
  exact ⟨hc.1, hcn⟩

/-- Two skew tableaux agreeing on the skew region agree everywhere: off it both are `0`. -/
theorem skew_entry_ext {T₁ T₂ : SkewStandardYoungTableau outer inner}
    (h : ∀ c ∈ skewCellsOf outer inner, T₁.entry c.1 c.2 = T₂.entry c.1 c.2) : T₁ = T₂ := by
  refine skew_syt_ext (fun i j => ?_)
  by_cases hm : (i, j) ∈ skewCellsOf outer inner
  · exact h (i, j) hm
  · simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells, not_and, not_not] at hm
    by_cases ho : (i, j) ∈ outer
    · rw [T₁.zeros (Or.inl (hm ho)), T₂.zeros (Or.inl (hm ho))]
    · rw [T₁.zeros (Or.inr ho), T₂.zeros (Or.inr ho)]

/-- **There are finitely many skew standard tableaux of a given shape.**

`fDimSkew` is defined as a `Nat.card`, and nothing in the corpus had yet established that this
count is finite — so every `Nat.card` fact about it was, strictly, a fact about a possibly-junk
`0`.  The restriction map `T ↦ (entry on the skew cells, valued in `Fin |skew|`)` is injective by
`skew_entry_ext` and lands in a finite type, which settles it. -/
instance finiteSkewSYT (outer inner : YoungDiagram) :
    Finite (SkewStandardYoungTableau outer inner) := by
  refine Finite.of_injective
    (fun T : SkewStandardYoungTableau outer inner =>
      fun c : {x : ℕ × ℕ // x ∈ skewCellsOf outer inner} =>
        (⟨T.entry c.1.1 c.1.2, skew_mem_range T c.2⟩ : Fin (skewCellsOf outer inner).card))
    (fun T₁ T₂ h => ?_)
  refine skew_entry_ext (fun c hc => ?_)
  exact congrArg Fin.val (congrFun h ⟨c, hc⟩)

/-! ### The erase direction as a map

`exists_max_corner` produces the corner; this turns the deletion into an actual
`SkewStandardYoungTableau` on the smaller shape. -/

/-- **Delete the maximal entry at a corner outside `inner`.**  The mirror of `skewInsertMax`:
zero out the corner and keep `T` elsewhere.

`content` is the only field that does real work.  Splitting `skew outer inner` as
`insert c (skew (outer ∖ c) inner)` turns `T.content : image = range (n + 1)` into
`insert n (image over the smaller region) = insert n (range n)`; since `n` is missing from both
inner sets (from `skew_injOn`, the only cell carrying `n` is the deleted corner), erasing `n`
from both sides gives exactly the smaller `content`. -/
noncomputable def skewEraseMax (p q n : ℕ) (hc : IsCornerCell outer (p, q))
    (hcm : (p, q) ∈ skewCellsOf outer inner)
    (T : SkewStandardYoungTableau outer inner)
    (hn : (skewCellsOf outer inner).card = n + 1)
    (hval : T.entry p q = n) :
    SkewStandardYoungTableau (eraseCorner outer (p, q) hc) inner where
  entry := fun i j => if i = p ∧ j = q then 0 else T.entry i j
  row_strict := by
    intro i j₁ j₂ hlt hj₂ hj₁
    have hj₂o : (i, j₂) ∈ outer := ((mem_eraseCorner outer (p, q) hc (i, j₂)).mp hj₂).1
    have hne2 : (i, j₂) ≠ (p, q) := ((mem_eraseCorner outer (p, q) hc (i, j₂)).mp hj₂).2
    have hne1 : (i, j₁) ≠ (p, q) := by
      rintro h
      have hi : i = p := congrArg Prod.fst h
      have hj : j₁ = q := congrArg Prod.snd h
      refine not_mem_right_of_corner hc (show q < j₂ by omega) ?_
      rw [← hi]; exact hj₂o
    rw [if_neg (fun h => hne1 (Prod.ext h.1 h.2)), if_neg (fun h => hne2 (Prod.ext h.1 h.2))]
    exact T.row_strict hlt hj₂o hj₁
  col_strict := by
    intro i₁ i₂ j hlt hi₂ hi₁
    have hi₂o : (i₂, j) ∈ outer := ((mem_eraseCorner outer (p, q) hc (i₂, j)).mp hi₂).1
    have hne2 : (i₂, j) ≠ (p, q) := ((mem_eraseCorner outer (p, q) hc (i₂, j)).mp hi₂).2
    have hne1 : (i₁, j) ≠ (p, q) := by
      rintro h
      have hi : i₁ = p := congrArg Prod.fst h
      have hj : j = q := congrArg Prod.snd h
      refine not_mem_below_of_corner hc (show p < i₂ by omega) ?_
      rw [← hj]; exact hi₂o
    rw [if_neg (fun h => hne1 (Prod.ext h.1 h.2)), if_neg (fun h => hne2 (Prod.ext h.1 h.2))]
    exact T.col_strict hlt hi₂o hi₁
  zeros := by
    intro i j h
    by_cases hpq : i = p ∧ j = q
    · rw [if_pos hpq]
    · rw [if_neg hpq]
      refine T.zeros ?_
      rcases h with h | h
      · exact Or.inl h
      · refine Or.inr (fun hout => h ?_)
        exact (mem_eraseCorner outer (p, q) hc (i, j)).mpr
          ⟨hout, fun he => hpq ⟨congrArg Prod.fst he, congrArg Prod.snd he⟩⟩
  content := by
    set f : ℕ × ℕ → ℕ := fun x => if x.1 = p ∧ x.2 = q then 0 else T.entry x.1 x.2 with hf
    have hnotin : (p, q) ∉ skewCellsOf (eraseCorner outer (p, q) hc) inner := by
      simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells, mem_eraseCorner,
        not_and, not_not]
      intro h
      exact absurd rfl h.2
    have hcard : (skewCellsOf (eraseCorner outer (p, q) hc) inner).card = n := by
      have := card_skewCellsOf_eraseCorner hc hcm
      omega
    -- on the smaller region `f` is just `T.entry`
    have hagree : Set.EqOn f (fun x : ℕ × ℕ => T.entry x.1 x.2)
        ↑(skewCellsOf (eraseCorner outer (p, q) hc) inner) := by
      intro x hx
      simp only [Finset.mem_coe] at hx
      refine if_neg (fun hxe => hnotin ?_)
      exact (Prod.ext hxe.1 hxe.2 : x = (p, q)) ▸ hx
    have hsplit : outer.cells \ inner.cells
        = insert (p, q) (skewCellsOf (eraseCorner outer (p, q) hc) inner) := by
      show skewCellsOf outer inner = _
      rw [skewCellsOf_eraseCorner hc, Finset.insert_erase hcm]
    -- `n` is carried only by the deleted corner, so it is missing from the smaller image
    have hnmem : n ∉ (skewCellsOf (eraseCorner outer (p, q) hc) inner).image
        (fun x : ℕ × ℕ => T.entry x.1 x.2) := by
      intro hmem
      obtain ⟨x, hx, hxv⟩ := Finset.mem_image.mp hmem
      have hxskew : x ∈ skewCellsOf outer inner := by
        rw [skewCellsOf_eraseCorner hc] at hx
        exact Finset.mem_of_mem_erase hx
      have hxpq : x = (p, q) :=
        skew_injOn T (Finset.mem_coe.mpr hxskew) (Finset.mem_coe.mpr hcm) (by
          simp only; rw [hxv, hval])
      exact hnotin (hxpq ▸ hx)
    have key : insert n ((skewCellsOf (eraseCorner outer (p, q) hc) inner).image
        (fun x : ℕ × ℕ => T.entry x.1 x.2)) = insert n (Finset.range n) := by
      have h1 := T.content
      rw [hsplit, Finset.image_insert] at h1
      simpa [hval, hcard, Finset.card_insert_of_notMem hnotin, Finset.range_add_one] using h1
    show (skewCellsOf (eraseCorner outer (p, q) hc) inner).image f
        = Finset.range (skewCellsOf (eraseCorner outer (p, q) hc) inner).card
    rw [Finset.image_congr hagree, hcard]
    calc (skewCellsOf (eraseCorner outer (p, q) hc) inner).image
            (fun x : ℕ × ℕ => T.entry x.1 x.2)
        = (insert n ((skewCellsOf (eraseCorner outer (p, q) hc) inner).image
            (fun x : ℕ × ℕ => T.entry x.1 x.2))).erase n := (Finset.erase_insert hnmem).symm
      _ = (insert n (Finset.range n)).erase n := by rw [key]
      _ = Finset.range n := Finset.erase_insert (by simp)

/-! ### The two roundtrips -/

/-- **The re-inserted tableau carries the top value at the corner.** -/
theorem entry_skewInsertMax_corner (p q : ℕ) (hc : IsCornerCell outer (p, q))
    (hcn : (p, q) ∉ inner)
    (S : SkewStandardYoungTableau (eraseCorner outer (p, q) hc) inner) :
    (skewInsertMax p q hc hcn S).entry p q
      = (skewCellsOf (eraseCorner outer (p, q) hc) inner).card := by
  show (if p = p ∧ q = q then (skewCellsOf (eraseCorner outer (p, q) hc) inner).card
    else S.entry p q) = _
  rw [if_pos ⟨rfl, rfl⟩]

/-- **Roundtrip 1.**  Deleting the maximal corner and re-inserting the top value recovers `T`. -/
theorem skewInsertMax_skewEraseMax (p q n : ℕ) (hc : IsCornerCell outer (p, q))
    (hcm : (p, q) ∈ skewCellsOf outer inner)
    (T : SkewStandardYoungTableau outer inner)
    (hn : (skewCellsOf outer inner).card = n + 1)
    (hval : T.entry p q = n)
    (hcn : (p, q) ∉ inner) :
    skewInsertMax p q hc hcn (skewEraseMax p q n hc hcm T hn hval) = T := by
  have hcard : (skewCellsOf (eraseCorner outer (p, q) hc) inner).card = n := by
    have := card_skewCellsOf_eraseCorner hc hcm
    omega
  refine skew_syt_ext (fun i j => ?_)
  show (if i = p ∧ j = q then (skewCellsOf (eraseCorner outer (p, q) hc) inner).card
    else (skewEraseMax p q n hc hcm T hn hval).entry i j) = T.entry i j
  by_cases hij : i = p ∧ j = q
  · rw [if_pos hij, hcard, hij.1, hij.2]
    exact hval.symm
  · rw [if_neg hij]
    show (if i = p ∧ j = q then 0 else T.entry i j) = T.entry i j
    rw [if_neg hij]

/-- **Roundtrip 2.**  Re-inserting the top value at `c` and deleting that corner recovers `S`. -/
theorem skewEraseMax_skewInsertMax (p q : ℕ) (hc : IsCornerCell outer (p, q))
    (hcn : (p, q) ∉ inner)
    (S : SkewStandardYoungTableau (eraseCorner outer (p, q) hc) inner)
    (hcm : (p, q) ∈ skewCellsOf outer inner)
    (hn : (skewCellsOf outer inner).card
      = (skewCellsOf (eraseCorner outer (p, q) hc) inner).card + 1) :
    skewEraseMax p q (skewCellsOf (eraseCorner outer (p, q) hc) inner).card hc hcm
        (skewInsertMax p q hc hcn S) hn (entry_skewInsertMax_corner p q hc hcn S) = S := by
  refine skew_syt_ext (fun i j => ?_)
  show (if i = p ∧ j = q then 0 else (skewInsertMax p q hc hcn S).entry i j) = S.entry i j
  by_cases hij : i = p ∧ j = q
  · rw [if_pos hij, hij.1, hij.2]
    exact (S.zeros (Or.inr (fun h =>
      ((mem_eraseCorner outer (p, q) hc (p, q)).mp h).2 rfl))).symm
  · rw [if_neg hij]
    show (if i = p ∧ j = q then _ else S.entry i j) = S.entry i j
    rw [if_neg hij]

/-! ### The branching count -/

/-- The corners of `outer` lying outside `inner` form a finite type. -/
noncomputable instance fintypeSkewCorners (outer inner : YoungDiagram) :
    Fintype {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner} := by
  apply Set.Finite.fintype
  apply Set.Finite.subset outer.cells.finite_toSet
  intro c hc
  exact Finset.mem_coe.mpr ((YoungDiagram.mem_cells _).mpr hc.1.1)

/-- Re-insert the top value at the indexed corner. -/
noncomputable def skewBranchInv
    (p : Σ c : {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner},
      SkewStandardYoungTableau (eraseCorner outer c.1 c.2.1) inner) :
    SkewStandardYoungTableau outer inner :=
  skewInsertMax p.1.1.1 p.1.1.2 p.1.2.1 p.1.2.2 p.2

/-- `skewBranchInv` is surjective: every skew tableau on a non-empty skew region is the
re-insertion, at its maximal corner, of the deletion of that corner. -/
theorem skewBranchInv_surjective (hpos : 0 < (skewCellsOf outer inner).card) :
    Function.Surjective (skewBranchInv (outer := outer) (inner := inner)) := by
  intro T
  obtain ⟨n, hn⟩ : ∃ n, (skewCellsOf outer inner).card = n + 1 :=
    ⟨(skewCellsOf outer inner).card - 1, by omega⟩
  obtain ⟨c, hcm, hval, hdown, hright⟩ := exists_max_corner T n hn
  have hcout : c ∈ outer := by
    simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells] at hcm
    exact hcm.1
  have hcn : c ∉ inner := by
    simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells] at hcm
    exact hcm.2
  have hc : IsCornerCell outer c := ⟨hcout, hdown, hright⟩
  exact ⟨⟨⟨c, hc, hcn⟩, skewEraseMax c.1 c.2 n hc hcm T hn hval⟩,
    skewInsertMax_skewEraseMax c.1 c.2 n hc hcm T hn hval hcn⟩

/-- `skewBranchInv` is injective: the inserted corner is recovered as the unique cell carrying
the top value (both fibres put the *same* value there, since deleting any corner drops the skew
size by exactly one), and then roundtrip 2 pins the tableau. -/
theorem skewBranchInv_injective :
    Function.Injective (skewBranchInv (outer := outer) (inner := inner)) := by
  rintro ⟨a₁, S₁⟩ ⟨a₂, S₂⟩ hpq
  simp only [skewBranchInv] at hpq
  have hm₁ : a₁.1 ∈ skewCellsOf outer inner := mem_skewCellsOf_of_corner a₁.2.1 a₁.2.2
  have hm₂ : a₂.1 ∈ skewCellsOf outer inner := mem_skewCellsOf_of_corner a₂.2.1 a₂.2.2
  -- both erased regions have the same size, so both corners carry the same top value
  have hc₁ := card_skewCellsOf_eraseCorner a₁.2.1 hm₁
  have hc₂ := card_skewCellsOf_eraseCorner a₂.2.1 hm₂
  have hcards : (skewCellsOf (eraseCorner outer a₁.1 a₁.2.1) inner).card
      = (skewCellsOf (eraseCorner outer a₂.1 a₂.2.1) inner).card := by omega
  have e₁ := entry_skewInsertMax_corner a₁.1.1 a₁.1.2 a₁.2.1 a₁.2.2 S₁
  have e₂ := entry_skewInsertMax_corner a₂.1.1 a₂.1.2 a₂.2.1 a₂.2.2 S₂
  rw [hpq] at e₁
  have hval : (skewInsertMax a₂.1.1 a₂.1.2 a₂.2.1 a₂.2.2 S₂).entry a₁.1.1 a₁.1.2
      = (skewInsertMax a₂.1.1 a₂.1.2 a₂.2.1 a₂.2.2 S₂).entry a₂.1.1 a₂.1.2 := by
    rw [e₁, e₂, hcards]
  have hc₁₂ : a₁.1 = a₂.1 :=
    skew_injOn _ (Finset.mem_coe.mpr hm₁) (Finset.mem_coe.mpr hm₂) hval
  have ha : a₁ = a₂ := Subtype.ext hc₁₂
  subst ha
  have hS : S₁ = S₂ := by
    refine skew_syt_ext (fun i j => ?_)
    by_cases hij : i = a₁.1.1 ∧ j = a₁.1.2
    · have hz : ∀ S : SkewStandardYoungTableau (eraseCorner outer a₁.1 a₁.2.1) inner,
          S.entry i j = 0 := by
        intro S
        refine S.zeros (Or.inr (fun h => ?_))
        have : (i, j) = a₁.1 := Prod.ext hij.1 hij.2
        exact ((mem_eraseCorner outer a₁.1 a₁.2.1 (i, j)).mp h).2 this
      rw [hz S₁, hz S₂]
    · have l₁ : (skewInsertMax a₁.1.1 a₁.1.2 a₁.2.1 a₁.2.2 S₁).entry i j = S₁.entry i j := by
        show (if i = a₁.1.1 ∧ j = a₁.1.2 then _ else S₁.entry i j) = S₁.entry i j
        rw [if_neg hij]
      have l₂ : (skewInsertMax a₁.1.1 a₁.1.2 a₁.2.1 a₁.2.2 S₂).entry i j = S₂.entry i j := by
        show (if i = a₁.1.1 ∧ j = a₁.1.2 then _ else S₂.entry i j) = S₂.entry i j
        rw [if_neg hij]
      rw [← l₁, ← l₂, hpq]
  rw [hS]

/-- **The skew branching rule, at the level of `Nat.card`.**  For a non-empty skew region,

    #SkewSYT(outer/inner) = ∑_{c a corner of outer, c ∉ inner} #SkewSYT((outer ∖ c)/inner). -/
theorem card_skewSYT_branching (hpos : 0 < (skewCellsOf outer inner).card) :
    Nat.card (SkewStandardYoungTableau outer inner)
      = ∑ c : {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner},
          Nat.card (SkewStandardYoungTableau (eraseCorner outer c.1 c.2.1) inner) := by
  have hbij : Function.Bijective (skewBranchInv (outer := outer) (inner := inner)) :=
    ⟨skewBranchInv_injective, skewBranchInv_surjective hpos⟩
  rw [← Nat.card_congr (Equiv.ofBijective _ hbij), Nat.card_sigma]

/-- **The skew branching rule for `fDimSkew`.**

    f^{outer/inner} = ∑_{c a corner of outer, c ∉ inner} f^{(outer ∖ c)/inner}.

The containment hypothesis is what lets the guard in `fDimSkew` be discharged on both sides:
`le_eraseCorner_of_notMem` says deleting a corner outside `inner` keeps `inner` inside. -/
theorem fDimSkew_branching (hle : inner ≤ outer) (hpos : 0 < (skewCellsOf outer inner).card) :
    fDimSkew outer inner
      = ∑ c : {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner},
          fDimSkew (eraseCorner outer c.1 c.2.1) inner := by
  rw [fDimSkew_of_le hle, card_skewSYT_branching hpos]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  exact (fDimSkew_of_le (le_eraseCorner_of_notMem hle c.2.1 c.2.2)).symm

end QOU.BraidKnot.YoungTableauStandard
