/-
# Skew standard Young tableaux + the keystone C8 corollary

This file **reuses** the canonical in-repo standard-Young-tableau infrastructure
rather than redefining it:

* `QOU.Mathlib.StandardYoungTableau` / `QOU.Mathlib.numStandardYoungTableaux`
  (`QOU/Mathlib/StandardYoungTableau.lean`) — the `SemistandardYoungTableau`-refinement
  with a `Set.BijOn` filling, proving strict rows (`row_strict`), `injOn_cells`, a
  `Finite` instance, and the count `#SYT(μ) = Nat.card (StandardYoungTableau μ)`.
* `QOU.Mathlib.partitionShape` / `QOU.Mathlib.dimSYT`
  (`QOU/Mathlib/RSKBurnsideTarget.lean`) — the partition → `YoungDiagram` map (via
  `ofRowLens` of the weakly-decreasing sorted parts) and `dimSYT p := #SYT(partitionShape p)`,
  together with the `RSKBurnsideHolds` target `∑_{p⊢n} dim(p)² = n!`.

It therefore no longer defines its own `StandardYoungTableau`, `fDim`, or
`ydOfPartition`; those were duplicates of the canonical, superior versions above.

## Scope (honest)

What remains here is genuinely new — the canonical infra has **no** skew tableaux
and the C8 corollary is `KeystoneC8SuperExpBound`-specific:

* `SkewStandardYoungTableau` — skew SYT (fillings of `outer.cells \ inner.cells` by
  `{0,…,|diff|−1}`, strictly increasing along rows and columns among the skew cells);
  Mathlib and the canonical `QOU.Mathlib` SYT both lack this.
* `fDimSkew` — the skew SYT dimension count `f^{outer/inner}`, **guarded on
  `inner ≤ outer`**; see below.
* `mu21` — the hook shape `(2,1)`; `row3` — the shape `(3)`, the witness of
  `skewSYT_nonempty_of_not_le`.
* `involutionNumber_pos` — a genuine, fully proved positivity helper
  (`involutionNumber` lives in the imported `KeystoneC8SuperExpBound`).
* `c8_superexp` — a corollary of the sibling arithmetic core `c8_lower_bound`,
  expressed over the canonical `dimSYT` / `partitionShape`. All of its own arithmetic
  is proved; it inherits `branching_two_one` below as the `[RSKIdentitiesContext]`
  hypothesis rather than as a `sorry` — and that class is now **inhabited**, so `c8_superexp`
  applies at every concrete `k ≥ 3`.

`branching_two_one` is `§3b`-conditional on the `RSKIdentitiesContext` class and its body
is the matching class field, so `#print axioms` on it is clean and the hypothesis shows up
in the signature rather than in the term.

**The class is now inhabited** (2026-08-31): `QOU.Mathlib.SkewBranchingTwoOne` supplies
`rskIdentitiesContextInstance`, so `branching_two_one` and `c8_superexp` apply at every
concrete `k ≥ 3`. The instance lives downstream because everything skew is defined *here*;
it is not stated unconditionally in this file only for that import-order reason.

And it turned out **not to need RSK**, exactly as its former companion
`sum_dimSYT_eq_involution` did not. That companion was removed from the class on 2026-08-30
and proved by the `1`-differential structure of Young's lattice; `branching_two_one` falls to
the same machinery one step further on — the skew branching rule
(`QOU.Mathlib.SkewSYTBranchingBijection`) plus the up-operator identity
(`QOU.Mathlib.upSum_eq`), assembled in `QOU.Mathlib.SkewBranchingSum`. That is twice now that
"Mathlib lacks RSK, therefore blocked" was recorded here as an infrastructure fact and was
actually a mis-diagnosis.

The third, `skew_le_straight`, is **proved** (§"Skew ↪ straight"): it is an
*inequality*, and an inequality between two counts needs only an injection, not a
bijection. The explicit extension `straightOfSkew` supplies it. Only the two
*equalities* need RSK.

## The containment guard on `fDimSkew` (was: a false statement behind a `sorry`)

`SkewStandardYoungTableau outer inner` fills the set difference
`outer.cells \ inner.cells`, and imposes **no** containment `inner ⊆ outer`.  That
difference stays inhabited when `inner ⊄ outer`, so the raw
`Nat.card (SkewStandardYoungTableau outer inner)` is *not* the classical skew
count `f^{outer/inner}`, which is `0` off containment.  `fDimSkew` therefore
guards on `inner ≤ outer`, and `skewSYT_nonempty_of_not_le` machine-proves that
the guard is necessary rather than defensive.

Unguarded, `branching_two_one` was **false, not merely open** — already at
`k = 3`, where the shapes `(3)` and `(1,1,1)` each contribute a spurious `1` and
`3 · 4 = 12 ≠ 6 = 3!`.  A `sorry` in front of a false proposition is worse than an
open gap, so the definition is fixed rather than the statement weakened; guarded,
the identity checks out at `k = 3` and `k = 4` (arithmetic in the
`skewSYT_nonempty_of_not_le` docstring).

Base ring `ℝ` appears only in the C8 corollary (it consumes the archimedean
`c8_lower_bound`); the tableau infrastructure itself is entirely over `ℕ`
(AGENTS.md §7c).

-- Ref: [sagan2001] Sagan, The Symmetric Group, §3–4 (SYT, RSK, branching)
-/
import Mathlib.Combinatorics.Young.SemistandardTableau
import Mathlib.SetTheory.Cardinal.Finite
import QOU.Mathlib.RSKBurnsideTarget
import QOU.BraidKnot.KeystoneC8SuperExpBound
import QOU.Mass.SumSYTEqInvolution

namespace QOU.BraidKnot.YoungTableauStandard

open Finset
open QOU.BraidKnot.KeystoneC8SuperExpBound
open QOU.Mathlib

/-- Containment of Young diagrams is decidable — it *is* `Finset` inclusion of the
cells (`YoungDiagram.cells_subset_iff` is `Iff.rfl`), but instance search cannot
see through the `Preorder` instance to find that.  Supplying it keeps `fDimSkew`
free of `Classical`, which matters: an ambient classical `DecidableEq (ℕ × ℕ)`
would make the `\` in `Y.cells \ mu21.cells` elaborate to a different instance
than the one in `SkewStandardYoungTableau.content`, and the two would not
rewrite against each other. -/
instance decidableLEYoungDiagram (μ ν : YoungDiagram) : Decidable (μ ≤ ν) :=
  decidable_of_iff (μ.cells ⊆ ν.cells) YoungDiagram.cells_subset_iff

/-! ## Skew standard Young tableaux (genuinely new — canonical infra lacks these) -/

/-- A **skew standard Young tableau** of shape `outer / inner` is a filling of the
skew cells `outer.cells \ inner.cells` by `{0, …, |diff|−1}`, each used once,
strictly increasing along rows and columns among the skew (non-`inner`) cells. -/
structure SkewStandardYoungTableau (outer inner : YoungDiagram) where
  /-- `entry i j` is the value in cell `(i, j)`. -/
  entry : ℕ → ℕ → ℕ
  /-- Rows are strictly increasing among the skew cells. -/
  row_strict : ∀ {i j₁ j₂ : ℕ}, j₁ < j₂ → (i, j₂) ∈ outer → (i, j₁) ∉ inner →
    entry i j₁ < entry i j₂
  /-- Columns are strictly increasing among the skew cells. -/
  col_strict : ∀ {i₁ i₂ j : ℕ}, i₁ < i₂ → (i₂, j) ∈ outer → (i₁, j) ∉ inner →
    entry i₁ j < entry i₂ j
  /-- `entry` vanishes off the skew region (on `inner`, or outside `outer`). -/
  zeros : ∀ {i j : ℕ}, (i, j) ∈ inner ∨ (i, j) ∉ outer → entry i j = 0
  /-- The entries on the skew cells are exactly `{0, …, |diff|−1}`. -/
  content : (outer.cells \ inner.cells).image (fun c => entry c.1 c.2)
    = Finset.range (outer.cells \ inner.cells).card

/-- `f^{outer/inner}` — the number of skew standard Young tableaux of shape
`outer / inner`.

**The containment guard is load-bearing, not defensive.**  The classical skew
count is `0` unless `inner ⊆ outer` (the skew shape `λ/μ` is undefined
otherwise), but `SkewStandardYoungTableau` imposes no containment: it fills the
set difference `outer.cells \ inner.cells`, which stays perfectly well-behaved —
and inhabited — when `inner ⊄ outer`.  `skewSYT_nonempty_of_not_le` below exhibits
that, and records the arithmetic showing that the unguarded count makes
`branching_two_one` false. -/
noncomputable def fDimSkew (outer inner : YoungDiagram) : ℕ :=
  if inner ≤ outer then Nat.card (SkewStandardYoungTableau outer inner) else 0

theorem fDimSkew_of_le {outer inner : YoungDiagram} (h : inner ≤ outer) :
    fDimSkew outer inner = Nat.card (SkewStandardYoungTableau outer inner) :=
  if_pos h

theorem fDimSkew_of_not_le {outer inner : YoungDiagram} (h : ¬ inner ≤ outer) :
    fDimSkew outer inner = 0 :=
  if_neg h

/-- Two skew tableaux with the same entry map are equal (the remaining fields are
propositions). -/
theorem SkewStandardYoungTableau.ext {outer inner : YoungDiagram}
    {T₁ T₂ : SkewStandardYoungTableau outer inner}
    (h : ∀ i j, T₁.entry i j = T₂.entry i j) : T₁ = T₂ := by
  cases T₁ with
  | mk e₁ r₁ c₁ z₁ n₁ =>
    cases T₂ with
    | mk e₂ r₂ c₂ z₂ n₂ =>
      have he : e₁ = e₂ := funext fun i => funext fun j => h i j
      subst he
      rfl

/-! ## The shape `(2,1)` -/

/-- The Young diagram of shape `(2, 1)` — the smallest hook, with `f^{(2,1)} = 2`
and `|(2,1)|! = 6`. -/
def mu21 : YoungDiagram := YoungDiagram.ofRowLens [2, 1] (by decide)

/-- The single-row shape `(3)`.  Present only as the witness shape of
`skewSYT_nonempty_of_not_le`: it is the smallest partition of `3` that does *not*
contain `(2,1)`. -/
def row3 : YoungDiagram := YoungDiagram.ofRowLens [3] (by decide)

/-- **Why `fDimSkew` must guard on containment** (machine-proved, no `sorry`).

`(2,1) ⊄ (3)`, yet `SkewStandardYoungTableau (3) (2,1)` is inhabited: the skew
region `(3).cells \ (2,1).cells` is the single cell `(0,2)`, both strictness
fields are vacuous there, and the all-zero filling satisfies `zeros` and
`content`.  So the *raw* `Nat.card` is `1` where the classical `f^{(3)/(2,1)}`
is `0`.

Unguarded, `branching_two_one` would be **false already at `k = 3`**: the three
partitions of `3` contribute `f^{(3)}·1 + f^{(2,1)}·1 + f^{(1,1,1)}·1
= 1 + 2 + 1 = 4` (each raw skew count is `1`, the shapes `(3)` and `(1,1,1)`
contributing spuriously), and `3 · 4 = 12 ≠ 6 = 3!`.  Guarded, only `(2,1)`
survives and the sum is `2`, with `3 · 2 = 6 = 3!` ✓ — and at `k = 4` the
surviving shapes `(3,1), (2,2), (2,1,1)` give `3·1 + 2·1 + 3·1 = 8` with
`3 · 8 = 24 = 4!` ✓. -/
theorem skewSYT_nonempty_of_not_le :
    ¬ mu21 ≤ row3 ∧ Nonempty (SkewStandardYoungTableau row3 mu21) := by
  constructor
  · rw [← YoungDiagram.cells_subset_iff]
    intro hsub
    have hmem : ((1, 0) : ℕ × ℕ) ∈ mu21.cells := by
      simp [mu21, YoungDiagram.mem_ofRowLens]
    have hnot : ((1, 0) : ℕ × ℕ) ∉ row3.cells := by
      simp [row3, YoungDiagram.mem_ofRowLens]
    exact hnot (hsub hmem)
  · refine ⟨⟨fun _ _ => 0, ?_, ?_, fun _ => rfl, ?_⟩⟩
    · -- rows: `(i, j₂) ∈ (3)` forces `i = 0` and `j₂ < 3`, so `j₁ < j₂ ≤ 2 < 2`
      -- puts `(0, j₁)` inside `(2,1)` after all — contradicting the hypothesis
      intro i j₁ j₂ hj hout hin
      exfalso
      apply hin
      simp only [row3, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add] at hout
      obtain ⟨hi, hj₂⟩ := hout
      have hi0 : i = 0 := by omega
      subst hi0
      simp only [List.getElem_cons_zero] at hj₂
      simp only [mu21, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add, List.getElem_cons_zero]
      exact ⟨by norm_num, by omega⟩
    · -- columns: `(i₂, j) ∈ (3)` forces `i₂ = 0`, and nothing is `< 0`
      intro i₁ i₂ j hi hout _
      exfalso
      simp only [row3, YoungDiagram.mem_ofRowLens, List.length_cons, List.length_nil,
        Nat.zero_add] at hout
      obtain ⟨hi₂, -⟩ := hout
      omega
    · -- the skew region is the single cell `(0,2)`; both sides are `{0}`
      decide

/-! ## Skew ↪ straight — the injection that discharges `skew_le_straight`

For `μ ⊆ λ`, a skew SYT of shape `λ/μ` extends to a *straight* SYT of `λ`: fill
`μ` with a fixed standard tableau of `μ` (values `1…|μ|`) and shift every skew
value up past it.  The extension is injective — subtract the shift on the skew
cells to recover the skew tableau — so `f^{λ/μ} ≤ f^λ` shape by shape, and
summing gives `skew_le_straight`.

Everything is specialised to `μ = (2,1)`, the only shape the C8 corollary needs;
a general version would take a chosen SYT of `μ` as a parameter.  Note the target
`QOU.Mathlib.StandardYoungTableau` is `1`-indexed (a `Set.BijOn` onto
`Icc 1 |λ|`) while `SkewStandardYoungTableau` is `0`-indexed (image `= range d`),
so the shift is `+4`, not `+3`. -/

/-- The three cells of `(2,1)`. -/
theorem mu21_cells : mu21.cells = {(0, 0), (0, 1), (1, 0)} := by decide

theorem mu21_card : mu21.cells.card = 3 := by decide

theorem mem_mu21 {i j : ℕ} :
    (i, j) ∈ mu21 ↔ (i = 0 ∧ j = 0) ∨ (i = 0 ∧ j = 1) ∨ (i = 1 ∧ j = 0) := by
  rw [← YoungDiagram.mem_cells, mu21_cells]
  simp [Prod.ext_iff]

/-- The canonical standard filling of `(2,1)` by `1, 2, 3`. -/
def kappa21 (i j : ℕ) : ℕ := if i = 0 then (if j = 0 then 1 else 2) else 3

theorem kappa21_pos (i j : ℕ) : 1 ≤ kappa21 i j := by
  unfold kappa21; split_ifs <;> omega

theorem kappa21_le (i j : ℕ) : kappa21 i j ≤ 3 := by
  unfold kappa21; split_ifs <;> omega

theorem kappa21_row {i j₁ j₂ : ℕ} (hj : j₁ < j₂)
    (h1 : (i, j₁) ∈ mu21) (h2 : (i, j₂) ∈ mu21) : kappa21 i j₁ ≤ kappa21 i j₂ := by
  rw [mem_mu21] at h1 h2
  unfold kappa21
  split_ifs <;> omega

theorem kappa21_col {i₁ i₂ j : ℕ} (hi : i₁ < i₂)
    (h1 : (i₁, j) ∈ mu21) (h2 : (i₂, j) ∈ mu21) : kappa21 i₁ j < kappa21 i₂ j := by
  rw [mem_mu21] at h1 h2
  unfold kappa21
  split_ifs <;> omega

theorem kappa21_injOn {i₁ j₁ i₂ j₂ : ℕ} (h1 : (i₁, j₁) ∈ mu21) (h2 : (i₂, j₂) ∈ mu21)
    (he : kappa21 i₁ j₁ = kappa21 i₂ j₂) : ((i₁, j₁) : ℕ × ℕ) = (i₂, j₂) := by
  rw [mem_mu21] at h1 h2
  unfold kappa21 at he
  rw [Prod.mk.injEq]
  split_ifs at he <;> omega

/-- Every value in `{1,2,3}` is realised by `κ` on a cell of `(2,1)`. -/
theorem kappa21_surj {v : ℕ} (h1 : 1 ≤ v) (h3 : v ≤ 3) :
    ∃ c : ℕ × ℕ, c ∈ mu21.cells ∧ kappa21 c.1 c.2 = v := by
  interval_cases v
  · exact ⟨(0, 0), by decide, by decide⟩
  · exact ⟨(0, 1), by decide, by decide⟩
  · exact ⟨(1, 0), by decide, by decide⟩

section SkewToStraight

variable {Y : YoungDiagram}

theorem mu21_cells_subset (hsub : mu21 ≤ Y) : mu21.cells ⊆ Y.cells :=
  YoungDiagram.cells_subset_iff.mpr hsub

theorem skew_card (hsub : mu21 ≤ Y) :
    (Y.cells \ mu21.cells).card = Y.cells.card - 3 := by
  rw [Finset.card_sdiff, Finset.inter_eq_left.mpr (mu21_cells_subset hsub), mu21_card]

theorem three_le_card (hsub : mu21 ≤ Y) : 3 ≤ Y.cells.card := by
  rw [← mu21_card]; exact Finset.card_le_card (mu21_cells_subset hsub)

/-- Skew entries land in `{0, …, d−1}` (`d` the number of skew cells). -/
theorem skew_entry_lt (T : SkewStandardYoungTableau Y mu21)
    {i j : ℕ} (hc : ((i, j) : ℕ × ℕ) ∈ Y.cells \ mu21.cells) :
    T.entry i j < (Y.cells \ mu21.cells).card := by
  have hmem : T.entry i j ∈ (Y.cells \ mu21.cells).image (fun c => T.entry c.1 c.2) :=
    Finset.mem_image_of_mem (fun c => T.entry c.1 c.2) hc
  rw [T.content, Finset.mem_range] at hmem
  exact hmem

/-- …and hit every one of them (the `content` field is an equality, not an
inclusion). -/
theorem skew_entry_surj (T : SkewStandardYoungTableau Y mu21) {v : ℕ}
    (hv : v < (Y.cells \ mu21.cells).card) :
    ∃ c ∈ Y.cells \ mu21.cells, T.entry c.1 c.2 = v := by
  refine Finset.mem_image.mp ?_
  rw [T.content, Finset.mem_range]
  exact hv

/-- Equal cardinalities of source and image make the skew filling injective. -/
theorem skew_entry_injOn (T : SkewStandardYoungTableau Y mu21) :
    Set.InjOn (fun c : ℕ × ℕ => T.entry c.1 c.2) ↑(Y.cells \ mu21.cells) :=
  Finset.card_image_iff.mp (by rw [T.content, Finset.card_range])

/-- The straight filling: `(2,1)` gets `κ ∈ {1,2,3}`, each skew cell gets its skew
value shifted to `{4, …, |Y|}`, everything off `Y` gets `0`. -/
noncomputable def straightEntry (T : SkewStandardYoungTableau Y mu21) (i j : ℕ) : ℕ :=
  if (i, j) ∈ Y then (if (i, j) ∈ mu21 then kappa21 i j else T.entry i j + 4) else 0

theorem straightEntry_row (T : SkewStandardYoungTableau Y mu21) {i j₁ j₂ : ℕ}
    (hj : j₁ < j₂) (h2 : (i, j₂) ∈ Y) :
    straightEntry T i j₁ ≤ straightEntry T i j₂ := by
  have h1 : (i, j₁) ∈ Y := Y.up_left_mem (le_refl i) hj.le h2
  unfold straightEntry
  rw [if_pos h1, if_pos h2]
  by_cases hm2 : (i, j₂) ∈ mu21
  · have hm1 : (i, j₁) ∈ mu21 := mu21.up_left_mem (le_refl i) hj.le hm2
    rw [if_pos hm1, if_pos hm2]
    exact kappa21_row hj hm1 hm2
  · rw [if_neg hm2]
    by_cases hm1 : (i, j₁) ∈ mu21
    · rw [if_pos hm1]
      have := kappa21_le i j₁
      omega
    · rw [if_neg hm1]
      have := T.row_strict hj h2 hm1
      omega

theorem straightEntry_col (T : SkewStandardYoungTableau Y mu21) {i₁ i₂ j : ℕ}
    (hi : i₁ < i₂) (h2 : (i₂, j) ∈ Y) :
    straightEntry T i₁ j < straightEntry T i₂ j := by
  have h1 : (i₁, j) ∈ Y := Y.up_left_mem hi.le (le_refl j) h2
  unfold straightEntry
  rw [if_pos h1, if_pos h2]
  by_cases hm2 : (i₂, j) ∈ mu21
  · have hm1 : (i₁, j) ∈ mu21 := mu21.up_left_mem hi.le (le_refl j) hm2
    rw [if_pos hm1, if_pos hm2]
    exact kappa21_col hi hm1 hm2
  · rw [if_neg hm2]
    by_cases hm1 : (i₁, j) ∈ mu21
    · rw [if_pos hm1]
      have := kappa21_le i₁ j
      omega
    · rw [if_neg hm1]
      have := T.col_strict hi h2 hm1
      omega

/-- The straight tableau's underlying semistandard tableau. -/
noncomputable def straightSsyt (T : SkewStandardYoungTableau Y mu21) :
    SemistandardYoungTableau Y where
  entry := straightEntry T
  row_weak' := fun hj h2 => straightEntry_row T hj h2
  col_strict' := fun hi h2 => straightEntry_col T hi h2
  zeros' := fun {i j} hij => by unfold straightEntry; rw [if_neg hij]

theorem straightEntry_mapsTo (hsub : mu21 ≤ Y) (T : SkewStandardYoungTableau Y mu21) :
    Set.MapsTo (fun c : ℕ × ℕ => straightEntry T c.1 c.2)
      (Y.cells : Set (ℕ × ℕ)) (Set.Icc 1 Y.cells.card) := by
  rintro ⟨i, j⟩ hc
  rw [Finset.mem_coe, YoungDiagram.mem_cells] at hc
  have h3 := three_le_card hsub
  simp only [Set.mem_Icc]
  unfold straightEntry
  rw [if_pos hc]
  by_cases hm : ((i, j) : ℕ × ℕ) ∈ mu21
  · rw [if_pos hm]
    exact ⟨kappa21_pos i j, le_trans (kappa21_le i j) h3⟩
  · rw [if_neg hm]
    have hcs : ((i, j) : ℕ × ℕ) ∈ Y.cells \ mu21.cells :=
      Finset.mem_sdiff.mpr ⟨(YoungDiagram.mem_cells _).mpr hc,
        fun hx => hm ((YoungDiagram.mem_cells _).mp hx)⟩
    have hlt := skew_entry_lt T hcs
    rw [skew_card hsub] at hlt
    omega

theorem straightEntry_injOn (T : SkewStandardYoungTableau Y mu21) :
    Set.InjOn (fun c : ℕ × ℕ => straightEntry T c.1 c.2) (Y.cells : Set (ℕ × ℕ)) := by
  rintro ⟨i₁, j₁⟩ hc1 ⟨i₂, j₂⟩ hc2 he
  rw [Finset.mem_coe, YoungDiagram.mem_cells] at hc1 hc2
  simp only [straightEntry, if_pos hc1, if_pos hc2] at he
  by_cases hm1 : ((i₁, j₁) : ℕ × ℕ) ∈ mu21 <;> by_cases hm2 : ((i₂, j₂) : ℕ × ℕ) ∈ mu21
  · rw [if_pos hm1, if_pos hm2] at he
    exact kappa21_injOn hm1 hm2 he
  · rw [if_pos hm1, if_neg hm2] at he
    have := kappa21_le i₁ j₁
    omega
  · rw [if_neg hm1, if_pos hm2] at he
    have := kappa21_le i₂ j₂
    omega
  · rw [if_neg hm1, if_neg hm2] at he
    have hs1 : ((i₁, j₁) : ℕ × ℕ) ∈ Y.cells \ mu21.cells :=
      Finset.mem_sdiff.mpr ⟨(YoungDiagram.mem_cells _).mpr hc1,
        fun hx => hm1 ((YoungDiagram.mem_cells _).mp hx)⟩
    have hs2 : ((i₂, j₂) : ℕ × ℕ) ∈ Y.cells \ mu21.cells :=
      Finset.mem_sdiff.mpr ⟨(YoungDiagram.mem_cells _).mpr hc2,
        fun hx => hm2 ((YoungDiagram.mem_cells _).mp hx)⟩
    have heq : T.entry i₁ j₁ = T.entry i₂ j₂ := by omega
    exact skew_entry_injOn T (Finset.mem_coe.mpr hs1) (Finset.mem_coe.mpr hs2) heq

theorem straightEntry_surjOn (hsub : mu21 ≤ Y) (T : SkewStandardYoungTableau Y mu21) :
    Set.SurjOn (fun c : ℕ × ℕ => straightEntry T c.1 c.2)
      (Y.cells : Set (ℕ × ℕ)) (Set.Icc 1 Y.cells.card) := by
  intro v hv
  simp only [Set.mem_Icc] at hv
  obtain ⟨hv1, hvN⟩ := hv
  have h3 := three_le_card hsub
  by_cases hv3 : v ≤ 3
  · obtain ⟨c, hc, hkc⟩ := kappa21_surj hv1 hv3
    have hcY : c ∈ Y.cells := mu21_cells_subset hsub hc
    refine ⟨c, Finset.mem_coe.mpr hcY, ?_⟩
    have hcm : ((c.1, c.2) : ℕ × ℕ) ∈ mu21 := by
      rw [← YoungDiagram.mem_cells]; simpa using hc
    have hcy : ((c.1, c.2) : ℕ × ℕ) ∈ Y := by
      rw [← YoungDiagram.mem_cells]; simpa using hcY
    simp only [straightEntry, if_pos hcy, if_pos hcm]
    exact hkc
  · have hvd : v - 4 < (Y.cells \ mu21.cells).card := by
      rw [skew_card hsub]; omega
    obtain ⟨c, hc, hTc⟩ := skew_entry_surj T hvd
    obtain ⟨hcY, hcm⟩ := Finset.mem_sdiff.mp hc
    refine ⟨c, Finset.mem_coe.mpr hcY, ?_⟩
    have hcy : ((c.1, c.2) : ℕ × ℕ) ∈ Y := by
      rw [← YoungDiagram.mem_cells]; simpa using hcY
    have hcnm : ((c.1, c.2) : ℕ × ℕ) ∉ mu21 := by
      rw [← YoungDiagram.mem_cells]; simpa using hcm
    simp only [straightEntry, if_pos hcy, if_neg hcnm]
    omega

/-- **The extension.**  A skew SYT of shape `Y/(2,1)` becomes a straight SYT of
`Y`. -/
noncomputable def straightOfSkew (hsub : mu21 ≤ Y) (T : SkewStandardYoungTableau Y mu21) :
    QOU.Mathlib.StandardYoungTableau Y where
  toSsyt := straightSsyt T
  bijOn := ⟨straightEntry_mapsTo hsub T, straightEntry_injOn T,
    straightEntry_surjOn hsub T⟩

/-- The extension is injective: subtracting the shift on the skew cells recovers
the skew tableau, and `zeros` pins it everywhere else. -/
theorem straightOfSkew_injective (hsub : mu21 ≤ Y) :
    Function.Injective (straightOfSkew hsub) := by
  intro T₁ T₂ h
  refine SkewStandardYoungTableau.ext (fun i j => ?_)
  by_cases hY : ((i, j) : ℕ × ℕ) ∈ Y
  · by_cases hm : ((i, j) : ℕ × ℕ) ∈ mu21
    · rw [T₁.zeros (Or.inl hm), T₂.zeros (Or.inl hm)]
    · have he := congrArg (fun S : QOU.Mathlib.StandardYoungTableau Y => S.entry i j) h
      simp only [straightOfSkew, QOU.Mathlib.StandardYoungTableau.entry, straightSsyt,
        straightEntry, if_pos hY, if_neg hm] at he
      omega
  · rw [T₁.zeros (Or.inr hY), T₂.zeros (Or.inr hY)]

/-- **`f^{Y/(2,1)} ≤ f^Y`** whenever `(2,1) ⊆ Y`. -/
theorem card_skew_le_card_straight (hsub : mu21 ≤ Y) :
    Nat.card (SkewStandardYoungTableau Y mu21)
      ≤ Nat.card (QOU.Mathlib.StandardYoungTableau Y) :=
  Nat.card_le_card_of_injective _ (straightOfSkew_injective hsub)

end SkewToStraight

/-! ## Involution-number positivity (fully proved) -/

/-- The involution numbers are strictly positive (`I(n) ≥ 1`). Needed as the C8
denominator `I(k)` must be positive for `k!/(9·I(k))` to be a finite lower
bound. -/
theorem involutionNumber_pos : ∀ n, 0 < involutionNumber n := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 ih2 =>
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    omega

/-! ## The one remaining RSK-family identity (a hypothesis, not a `sorry`)

`branching_two_one` is the deep Standard-Young-Tableau counting fact Mathlib does not
prove.  It states the real proposition over the canonical `dimSYT` / `partitionShape` /
skew count.

**How the gap is carried.** This section text once said the fill "is `sorry` with a
`-- Ref:` to Sagan". It is not: the identity is `§3b`-conditional on the
`RSKIdentitiesContext` class below, and the theorem's body is the matching class field.
Nothing here is axiomatised and nothing is `sorry`, so `#print axioms` is clean — the gap
is visible in the *signature*, as an instance argument a caller has to produce.

**No instance exists.** `RSKIdentitiesContext` has no instance anywhere in this corpus,
degenerate or otherwise, so `branching_two_one` cannot be applied at a concrete `k` and
nothing downstream is silently discharged.

**`sum_dimSYT_eq_involution` used to be the class's second field, and is now PROVED
(2026-08-30).**  It has been removed from the class and the theorem is unconditional;
`QOU.Mass.sum_dimSYT_eq_involution_keystone` is the proof.

Worth recording *why* it sat here as long as it did, because the reason was wrong rather
than merely out of date. This section said the identity needed the RSK correspondence,
which Mathlib lacks. **It needs no RSK at all.** Young's lattice is a `1`-differential
poset, and that route proves the identity with finite combinatorics on `YoungDiagram` — no
insertion, no bumping, no permutation↔tableau-pair bijection (`QOU.Mathlib.upSum_eq` is the
step it turns on). *"Mathlib lacks X, therefore blocked"* is sound only when `X` is actually
required; here the textbook route was mistaken for the only route, and that mistake was
recorded in this file, in beans `qou-jlam` / `qou-m3xr`, and in three other docstrings as
though it were an infrastructure fact.

Their sibling `skew_le_straight` is stated here too but is no longer cited — it is proved
above, unconditionally.

**`branching_two_one` is probably not RSK-blocked either (2026-08-30) — do not assume the
P1–P5 program is the only route.**  This text listed it as "discharged by the RSK
correspondence (open P1–P5 program
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`)", which is the same
framing that turned out to be wrong for its former companion.  The differential-poset route
reaches it too, by induction on `k`:

    G(μ, k) := Σ_{|λ|=k} f^λ · f^{λ/μ},   claim  G(μ, k) = (k!/|μ|!) · f^μ

which at `μ = (2,1)` (`f^μ = 2`, `|μ|! = 6`) is `3 · Σ = k!` verbatim.  The step is

    G(μ, k+1) = Σ_λ f^λ Σ_{ν ⋖ λ, ν ⊇ μ} f^{ν/μ}      (skew branching)
              = Σ_ν f^{ν/μ} Σ_{λ ⋗ ν} f^λ              (transpose, as `pairTerm` does)
              = (k+1) · G(μ, k)                        (`QOU.Mathlib.upSum_eq`)

with base `G(μ, |μ|) = f^μ`.  Two of the three inputs are in hand: `upSum_eq` is proved
sorry-free, and the transposition is the `Finset.sum_comm` manoeuvre already used for it.
The **one open input is the skew branching rule** — remove the largest entry of a skew SYT —
the direct analogue of the proved `QOU.Mathlib.numStandardYoungTableaux_branching`.

Checked exactly for `k = 3..11` in
[`computations/combinatorics/branching_two_one_route_probe.py`](../../../../../computations/combinatorics/branching_two_one_route_probe.py).
**That probe confirms the route's arithmetic, not its open input**: it computes `f^{λ/μ}` *by*
the skew branching recursion, so it assumes that rule rather than verifying it.  So this is a
credible route with one real obligation left, **not** a proof.

**Since closed:** the skew branching rule is proved (`factorial_mul_skewPair_of_le`,
`QOU.Mathlib.SkewBranchingSum`), `branching_two_one_holds` is proved sorry-free in
`QOU.Mathlib.SkewBranchingTwoOne`, and that file supplies the instance
`rskIdentitiesContextInstance`. -/

class RSKIdentitiesContext where
  branching_two_one : ∀ (k : ℕ), 3 ≤ k → 3 * (∑ p : Nat.Partition k, dimSYT p * fDimSkew (partitionShape p) mu21) = Nat.factorial k

/-- **Classical branching** `Σ_{λ⊢k} f^λ · f^{λ/(2,1)} = k! · f^{(2,1)} / |(2,1)|!`
at `μ = (2,1)` (where `f^{(2,1)} = 2`, `|(2,1)|! = 6`, so the RHS is `k!/3`).
Stated in the cast-clean form `3 · (Σ …) = k!`, valid for `k ≥ |μ| = 3`.

Representation-theoretically this is the dimension of
`Ind_{S_m × S_{k−m}}^{S_k}(S^μ ⊠ ℚ[S_{k−m}])` counted two ways: `k!·f^μ/m!` by the
index-times-dimension formula, and `Σ_λ f^{λ/μ} f^λ` by `s_μ·s_1^{k−m} =
Σ_λ f^{λ/μ} s_λ`.

**Only true because `fDimSkew` guards on containment** — the sum must skip every
`λ` not containing `(2,1)`.  See `skewSYT_nonempty_of_not_le`, which exhibits the
counterexample the guard removes and checks this identity at `k = 3, 4`.

The body is `ctx.branching_two_one`, the matching field of the `[RSKIdentitiesContext]`
hypothesis, so the hypothesis sits in the signature rather than in the term and
`#print axioms` on this declaration is clean.

**No longer a gap (2026-08-31).** `QOU.Mathlib.SkewBranchingTwoOne.branching_two_one_holds`
proves this statement unconditionally and registers `rskIdentitiesContextInstance`, so the
`[ctx]` here resolves and the theorem applies at every concrete `k ≥ 3`. It is kept in
conditional form only because `SkewStandardYoungTableau` and `fDimSkew` are defined in *this*
file, so the proof has to live downstream of it.

**And it did not need RSK.** This docstring used to say the identity "requires massive
infrastructure (the RSK correspondence and hook-length formula)". The proof uses neither: it
is `|μ|!·∑_λ f^λ f^{λ/μ} = k!·f^μ` (`QOU.Mathlib.factorial_mul_skewPair_of_le`) at
`μ = (2,1)`, which is the skew branching rule plus the up-operator identity — finite
combinatorics on `YoungDiagram`. The one shelf item is the single number `f^{(2,1)} = 2`,
from the `decide`-verified small-`n` hook bridge: a computation on one three-cell shape, not
the hook-length formula as a theorem. -/
theorem branching_two_one (k : ℕ) (hk : 3 ≤ k) [ctx : RSKIdentitiesContext] :
    3 * (∑ p : Nat.Partition k,
        dimSYT p * fDimSkew (partitionShape p) mu21) = Nat.factorial k :=
  ctx.branching_two_one k hk

/-- **Skew SYT inject into straight SYT (PROVED, no longer cited).**
`Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ_{λ⊢k} f^λ`, the latter being the involution number
`I(k)` (RSK for involutions, below).

Proved term by term, by the explicit extension `straightOfSkew`: fill `(2,1)`
with `κ = 1,2,3` and shift each skew value into `{4, …, |λ|}`.  Shapes not
containing `(2,1)` contribute `0` on the left by the `fDimSkew` guard, so nothing
is needed for them.  No Jacobi–Trudi and no RSK: the *inequality* is elementary
once the injection is written down.

(This used to close by saying "only the two *equalities* — `branching_two_one`,
`sum_dimSYT_eq_involution` — need the real machinery". Both are now proved, and **neither**
needed it. What is true is the weaker claim that an inequality needs only an injection while
an equality needs a bijection.) -/
theorem skew_le_straight (k : ℕ) :
    (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21)
      ≤ (∑ p : Nat.Partition k, dimSYT p) := by
  refine Finset.sum_le_sum (fun p _ => ?_)
  by_cases h : mu21 ≤ partitionShape p
  · rw [fDimSkew_of_le h]
    exact card_skew_le_card_straight h
  · rw [fDimSkew_of_not_le h]
    exact Nat.zero_le _

/-- **RSK for involutions.** `Σ_{λ⊢k} f^λ = I(k)`, the number of involutions in `S_k` — the
`q = 1` value of the QOU na-Stokes period.  **Unconditional**, and it needs no instance.

Until 2026-08-30 this was a field of `RSKIdentitiesContext` and this docstring said the
identity "requires massive infrastructure (the RSK correspondence)" and was "an open gap".
**That was a mis-diagnosis, not merely a stale status note**: the identity does not need RSK
at all.  Young's lattice is a `1`-differential poset, and that route proves it with finite
combinatorics on `YoungDiagram` — no insertion, no bumping, no permutation↔tableau-pair
bijection.  See `QOU.Mass.sum_dimSYT_eq_involution_keystone`, and `QOU.Mathlib.upSum_eq` for
the up-operator step the whole argument turns on.

The lesson is worth keeping: *"Mathlib lacks X, therefore blocked"* is sound only when `X` is
actually required.  Here the standard textbook route was mistaken for the only route, and that
mistake was recorded in this file, in two beans and in three other docstrings as though it
were an infrastructure fact. -/
theorem sum_dimSYT_eq_involution (k : ℕ) :
    (∑ p : Nat.Partition k, dimSYT p) = involutionNumber k :=
  QOU.Mass.sum_dimSYT_eq_involution_keystone k

/-! ## The unconditional C8 super-exponential corollary -/

/-- **C8 super-exponential lower bound (`§3b`-conditional on `[RSKIdentitiesContext]`).**
This said "unconditional modulo the two remaining RSK `sorry`s above"; there are no
`sorry`s above — the two RSK identities are fields of the `[RSKIdentitiesContext]`
hypothesis this theorem also takes, so the conditionality is in the signature and
`#print axioms` here is clean. Instantiating the sibling arithmetic core `c8_lower_bound`
with `f = f^λ = dimSYT`, `g = f^{λ/(2,1)}`, `kfac = k!`, `Ik = I(k)`, and
discharging its inputs by casting `branching_two_one` (A) and `skew_le_straight` +
`sum_dimSYT_eq_involution` (C) to `ℝ`, the Plancherel-weighted branched sum obeys

    k! / (9·I(k))  ≤  (Σ_{λ⊢k} (f^λ)² f^{λ/(2,1)}) / k!.

All positivity and arithmetic are proved here. (A) and (C) are *hypotheses* of this
statement, not RSK inputs: (C) is proved outright above, and (A) is `branching_two_one`,
whose class is discharged in `QOU.Mathlib.SkewBranchingTwoOne`. So this bound now holds at
every concrete `k ≥ 3`. -/
theorem c8_superexp (k : ℕ) (hk : 3 ≤ k) [RSKIdentitiesContext] :
    (Nat.factorial k : ℝ) / (9 * (involutionNumber k : ℝ))
      ≤ (∑ p : Nat.Partition k,
            (dimSYT p : ℝ) ^ 2 * (fDimSkew (partitionShape p) mu21 : ℝ))
          / (Nat.factorial k : ℝ) := by
  classical
  have hIkpos : 0 < involutionNumber k := involutionNumber_pos k
  -- (A) Σ f g = k!/3, from `3 · Σ = k!` cast to ℝ.
  have hA : ∑ p : Nat.Partition k,
      (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ)
        = (Nat.factorial k : ℝ) / 3 := by
    have hnat := branching_two_one k hk
    have hc : (3 : ℝ) * (∑ p : Nat.Partition k,
        (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ))
        = (Nat.factorial k : ℝ) := by exact_mod_cast hnat
    linarith [hc]
  -- (C) Σ g ≤ I(k), from skew↪straight and RSK-for-involutions cast to ℝ.
  have hC : ∑ p : Nat.Partition k, (fDimSkew (partitionShape p) mu21 : ℝ)
        ≤ (involutionNumber k : ℝ) := by
    have hnat : (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21)
        ≤ involutionNumber k := by
      rw [← sum_dimSYT_eq_involution k]; exact skew_le_straight k
    exact_mod_cast hnat
  exact c8_lower_bound (Finset.univ : Finset (Nat.Partition k))
    (fun p => (dimSYT p : ℝ))
    (fun p => (fDimSkew (partitionShape p) mu21 : ℝ))
    (Nat.factorial k : ℝ) (involutionNumber k : ℝ)
    (fun i _ => by positivity)
    (by exact_mod_cast Nat.factorial_pos k)
    (by exact_mod_cast hIkpos)
    hA hC

end QOU.BraidKnot.YoungTableauStandard
