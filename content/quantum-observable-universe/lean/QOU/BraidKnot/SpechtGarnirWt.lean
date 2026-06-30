import QOU.BraidKnot.SpechtDominanceCore

/-!
# QOU.BraidKnot.SpechtGarnirWt — the order-reversing ℕ-measure for straightening

`SpechtSpanningCore.polytabloid_garnir_core` asks for a measure `wt : Tableau μ → ℕ`
under which a Garnir rewrite `e_t = Σ (more-dominant polytabloids)` strictly
decreases. The dominance order `domRel` on tabloids is already a sorry-free
partial order (`SpechtDominanceCore`), so its **up-set cardinality** supplies the
measure for free:

> `domWt a = #{d : domRel a d}` — and `domRel a b`, `a ≠ b` ⟹ `domWt b < domWt a`.

Because `domRel a b` means "`a` is dominated by `b`", a strictly-more-dominant
tabloid has a strictly **smaller** `domWt`. Lifting along `Tabloid.mk` gives
`tabWt : Tableau μ → ℕ` with the same strict-decrease law. Combined with
`SpechtGarnirSplit.polytabloid_mem_span_shuffled` (`e_t ∈ span{e_{σ·t}}`), the
**only** remaining input for `polytabloid_garnir_core` is the strict-dominance
claim `domRel {t} {σ·t}` (and `≠`) for the Garnir shuffles `σ ∈ S_X ∖ C_t`.

All sorry-free; reuses only the proved `domRel` order axioms.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirWt

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtDominanceCore

variable {μ : YoungDiagram}

/-- **The order-reversing rank.** `domWt a` is the size of the up-set of `a` in the
dominance order (the number of tabloids weakly dominating... i.e. with `domRel a ·`).
A strictly-more-dominant tabloid has strictly smaller `domWt`. -/
def domWt (a : Tabloid μ) : ℕ :=
  (Finset.univ.filter (fun d => domRel a d)).card

/-- **Strict decrease.** If `a` is dominated by `b` and `a ≠ b`, then
`domWt b < domWt a`: the up-set of `b` is a strict subset of the up-set of `a`. -/
theorem domWt_lt_of_domRel {a b : Tabloid μ} (hab : domRel a b) (hne : a ≠ b) :
    domWt b < domWt a := by
  classical
  unfold domWt
  have hsub : (Finset.univ.filter (fun d => domRel b d))
      ⊆ (Finset.univ.filter (fun d => domRel a d)) := by
    intro d hd
    rw [Finset.mem_filter] at hd ⊢
    exact ⟨Finset.mem_univ _, domRel_trans a b d hab hd.2⟩
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset hsub]
  refine ⟨a, ?_, ?_⟩
  · rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, domRel_refl a⟩
  · rw [Finset.mem_filter]; push_neg; intro _ hba
    exact hne (domRel_antisymm a b hab hba)

/-- **The straightening measure on tableaux.** `tabWt t = domWt {t}`. -/
def tabWt (t : Tableau μ) : ℕ := domWt (Tabloid.mk t)

/-- **Strict decrease for tableaux.** A strictly-more-dominant tabloid `{t}`
(over `{s}`) has strictly smaller measure. This is exactly the per-step decrease
`polytabloid_garnir_core` needs: a Garnir shuffle producing a strictly more
dominant tableau strictly decreases `tabWt`. -/
theorem tabWt_lt_of_domRel {s t : Tableau μ}
    (h : domRel (Tabloid.mk s) (Tabloid.mk t)) (hne : Tabloid.mk s ≠ Tabloid.mk t) :
    tabWt t < tabWt s :=
  domWt_lt_of_domRel h hne

/-! ## Column-pattern dominance — the measure that actually plugs into straightening

The row-tabloid measure `tabWt` above is correct but **does not** strictly
decrease under a Garnir rewrite: a straightening term can be *row-equivalent* to
`t` (e.g. for `μ = (2,1)`, `t = [[2,1],[3]]` straightens to `e_{[[1,2],[3]]} −
e_{[[1,3],[2]]}`, and `[[1,2],[3]]` has the same row tabloid as `t`). The correct
order is on the **column** pattern: there `[[1,2],[3]]` (colpat `[0,1,0]`) and
`[[1,3],[2]]` (`[0,0,1]`) are both **strictly more dominant** than `t` (`[1,0,0]`).

The `domCount` engine of `SpechtDominanceCore` is generic over the pattern
function, so we reuse it on `colPattern`. `patRel` is the resulting partial order
on patterns (antisymmetry is `domCount_inj`), and `colWt` its order-reversing
up-set rank on tableaux. The strict-decrease law `colWt_lt_of_patRel` is exactly
what `polytabloid_garnir_core` needs — the remaining input being the
column-dominance Garnir lemma (`patRel (colPattern t) (colPattern (σ·t))` strict
for the Garnir transversal reps `σ`). -/

/-- **Pattern dominance** (generic, reusing `domCount`): `f ⊴ g` iff every
dominance count of `f` is `≤` that of `g`. A partial order on `Fin n → ℕ`. -/
def patRel (f g : Fin (Specht.nOf μ) → ℕ) : Prop :=
  ∀ i m : ℕ, domCount f i m ≤ domCount g i m

theorem patRel_refl (f : Fin (Specht.nOf μ) → ℕ) : patRel f f := fun _ _ => le_refl _

theorem patRel_trans (f g h : Fin (Specht.nOf μ) → ℕ) :
    patRel f g → patRel g h → patRel f h :=
  fun hfg hgh i m => le_trans (hfg i m) (hgh i m)

theorem patRel_antisymm (f g : Fin (Specht.nOf μ) → ℕ) :
    patRel f g → patRel g f → f = g :=
  fun hfg hgf => domCount_inj f g (fun i m => le_antisymm (hfg i m) (hgf i m))

open Classical in
/-- **The column-dominance measure.** `colWt t` is the up-set cardinality of `t`'s
**column** pattern under `patRel` — an order-reversing `ℕ`-rank: a strictly more
column-dominant tableau has strictly smaller `colWt`. -/
noncomputable def colWt (t : Tableau μ) : ℕ :=
  (Finset.univ.filter
    (fun T : Tableau μ => patRel (Specht.colPattern t) (Specht.colPattern T))).card

open Classical in
/-- **Strict decrease (the straightening measure law).** If `t`'s column pattern
strictly dominates `s`'s (`patRel (colPattern s) (colPattern t)`, patterns
distinct), then `colWt t < colWt s`. Unlike the row measure, this *does* strictly
decrease on Garnir rewrites. -/
theorem colWt_lt_of_patRel {s t : Tableau μ}
    (h : patRel (Specht.colPattern s) (Specht.colPattern t))
    (hne : Specht.colPattern s ≠ Specht.colPattern t) :
    colWt t < colWt s := by
  unfold colWt
  have hsub :
      (Finset.univ.filter (fun T : Tableau μ => patRel (Specht.colPattern t) (Specht.colPattern T)))
        ⊆ (Finset.univ.filter
            (fun T : Tableau μ => patRel (Specht.colPattern s) (Specht.colPattern T))) := by
    intro T hT
    rw [Finset.mem_filter] at hT ⊢
    exact ⟨Finset.mem_univ _, patRel_trans _ _ _ h hT.2⟩
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset hsub]
  refine ⟨s, ?_, ?_⟩
  · rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, patRel_refl _⟩
  · rw [Finset.mem_filter]; push_neg; intro _ hts
    exact hne (patRel_antisymm _ _ hts h).symm

/-- **`colWt` is invariant under column permutations.** A column permutation
`κ ∈ C_t` does not change the column pattern (`colPattern (κ·t) = colPattern t`),
hence not `colWt`. Consequence (the measure wrinkle): column-standardisation does
**not** strictly decrease `colWt` — only a Garnir row-shuffle does. So closing
`polytabloid_garnir_core` over *non-column-standard* `t` needs `colWt` paired with
a column-inversion tie-breaker (column-standardise first, same `colWt`; then
Garnir strictly drops `colWt`). -/
theorem colWt_smul_colStab {t : Tableau μ} {κ : Equiv.Perm (Fin (Specht.nOf μ))}
    (hκ : κ ∈ Specht.colStab t) :
    colWt (κ • t) = colWt t := by
  have hpat : Specht.colPattern (κ • t) = Specht.colPattern t := by
    rw [Specht.colPattern_smul]; exact Specht.mem_colStab.mp hκ
  unfold colWt; rw [hpat]

/-! ## Toward the column-dominance Garnir lemma (piece A: the reindexing)

`colWt (σ·t) < colWt t` reduces (via `colWt_lt_of_patRel`) to
`patRel (colPattern t) (colPattern (σ·t))` strict, and
`colPattern (σ·t) = colPattern t ∘ σ⁻¹`. The twisted count
`domCount (c ∘ σ⁻¹) i m` reindexes to a σ-image count over the *untwisted*
down-set `{l : c l ≤ i}` — the first concrete step of the dominance comparison
(only the threshold separating the two Garnir columns will matter). -/

/-- **Reindexing the σ-twisted dominance count.** `domCount (c ∘ σ⁻¹) i m` counts
the labels `l < m` with `c (σ⁻¹ l) ≤ i`; substituting `l = σ l'` rewrites it as
the count of `l'` with `σ l' < m` and `c l' ≤ i`. -/
theorem domCount_comp_perm (c : Fin (Specht.nOf μ) → ℕ)
    (σ : Equiv.Perm (Fin (Specht.nOf μ))) (i m : ℕ) :
    domCount (fun l => c (σ⁻¹ l)) i m
      = (Finset.univ.filter
          (fun l : Fin (Specht.nOf μ) => ((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ c l ≤ i)).card := by
  classical
  unfold domCount
  refine Finset.card_bij' (fun l _ => σ⁻¹ l) (fun l _ => σ l) ?_ ?_ ?_ ?_
  · intro l hl
    rw [Finset.mem_filter] at hl ⊢
    refine ⟨Finset.mem_univ _, ?_, hl.2.2⟩
    rw [Equiv.Perm.apply_inv_self]; exact hl.2.1
  · intro l hl
    rw [Finset.mem_filter] at hl ⊢
    refine ⟨Finset.mem_univ _, ?_, ?_⟩
    · exact hl.2.1
    · show c (σ⁻¹ (σ l)) ≤ i
      rw [Equiv.Perm.inv_apply_self]; exact hl.2.2
  · intro l _; exact Equiv.Perm.apply_inv_self σ l
  · intro l _; exact Equiv.Perm.inv_apply_self σ l

/-- **Bottom-heaviness ⟹ column dominance (piece A).** If, for every threshold
`i`, applying `σ` to the down-set `{l : c l ≤ i}` is bottom-heavy — every initial
segment `[0, m)` captures at least as many `σ`-images as originals — then
`patRel c (c ∘ σ⁻¹)`, i.e. the relabelled pattern `c ∘ σ⁻¹` weakly dominates `c`.
Immediate from `domCount_comp_perm`: the hypothesis *is* the count inequality
`domCount c i m ≤ domCount (c ∘ σ⁻¹) i m`. -/
theorem patRel_comp_perm_of_bottomHeavy (c : Fin (Specht.nOf μ) → ℕ)
    (σ : Equiv.Perm (Fin (Specht.nOf μ)))
    (h : ∀ i m, (Finset.univ.filter
            (fun l : Fin (Specht.nOf μ) => (l : ℕ) < m ∧ c l ≤ i)).card
          ≤ (Finset.univ.filter
            (fun l : Fin (Specht.nOf μ) => ((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ c l ≤ i)).card) :
    patRel c (fun l => c (σ⁻¹ l)) := by
  intro i m
  rw [domCount_comp_perm]
  exact h i m

/-- **Two-column bottom-heaviness ⟹ column dominance (piece A3).** Let `c` be a
pattern, `σ` a permutation supported on the two-value set `X = c⁻¹{j, j+1}` (it
fixes everything outside and preserves `X`), and suppose the threshold-`j`
bottom-heaviness `#{c l = j ∧ l < m} ≤ #{c l = j ∧ σ l < m}` holds for all `m`.
Then `patRel c (c ∘ σ⁻¹)`: the relabelled pattern weakly dominates `c`.

For the Garnir set at a column-standard row-violation, `σ ∈ S_X ∖ C_t` satisfies
all three hypotheses — `hbh` because every `B`-label `< ` every `A`-label, so
`A = {c = j}` holds the largest labels and any `σ(A) ≠ A` is more bottom-heavy. -/
theorem patRel_comp_perm_two_column (c : Fin (Specht.nOf μ) → ℕ)
    (σ : Equiv.Perm (Fin (Specht.nOf μ))) (j : ℕ)
    (hsupp : ∀ l, ¬ (c l = j ∨ c l = j + 1) → σ l = l)
    (hstab : ∀ l, (c (σ l) = j ∨ c (σ l) = j + 1) ↔ (c l = j ∨ c l = j + 1))
    (hbh : ∀ m, (Finset.univ.filter (fun l => c l = j ∧ (l : ℕ) < m)).card
              ≤ (Finset.univ.filter
                  (fun l => c l = j ∧ ((σ l : Fin (Specht.nOf μ)) : ℕ) < m)).card) :
    patRel c (fun l => c (σ⁻¹ l)) := by
  apply patRel_comp_perm_of_bottomHeavy
  intro i m
  have split : ∀ (P : Fin (Specht.nOf μ) → Prop) [DecidablePred P],
      (Finset.univ.filter P).card
        = (Finset.univ.filter (fun l => P l ∧ (c l = j ∨ c l = j + 1))).card
          + (Finset.univ.filter (fun l => P l ∧ ¬ (c l = j ∨ c l = j + 1))).card := by
    intro P _
    rw [← Finset.filter_filter, ← Finset.filter_filter]
    exact (Finset.filter_card_add_filter_neg_card_eq_card _).symm
  rw [split (fun l => (l : ℕ) < m ∧ c l ≤ i),
      split (fun l => ((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ c l ≤ i)]
  apply Nat.add_le_add
  · -- in-`X` part
    rcases lt_trichotomy i j with hlt | heq | hgt
    · -- i < j: left filter empty
      have he : (Finset.univ.filter
          (fun l : Fin (Specht.nOf μ) => ((l : ℕ) < m ∧ c l ≤ i) ∧ (c l = j ∨ c l = j + 1))) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        rintro l _ ⟨⟨_, hci⟩, hx⟩
        rcases hx with h | h <;> omega
      rw [he]; exact Nat.zero_le _
    · -- i = j: hbh
      subst heq
      have hL : (Finset.univ.filter
            (fun l : Fin (Specht.nOf μ) => ((l : ℕ) < m ∧ c l ≤ i) ∧ (c l = i ∨ c l = i + 1)))
          = (Finset.univ.filter (fun l => c l = i ∧ (l : ℕ) < m)) := by
        apply Finset.filter_congr; intro l _
        constructor
        · rintro ⟨⟨hlm, hci⟩, hx⟩; rcases hx with h | h
          · exact ⟨h, hlm⟩
          · omega
        · rintro ⟨hcj, hlm⟩; exact ⟨⟨hlm, le_of_eq hcj⟩, Or.inl hcj⟩
      have hR : (Finset.univ.filter
            (fun l => (((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ c l ≤ i) ∧ (c l = i ∨ c l = i + 1)))
          = (Finset.univ.filter (fun l => c l = i ∧ ((σ l : Fin (Specht.nOf μ)) : ℕ) < m)) := by
        apply Finset.filter_congr; intro l _
        constructor
        · rintro ⟨⟨hlm, hci⟩, hx⟩; rcases hx with h | h
          · exact ⟨h, hlm⟩
          · omega
        · rintro ⟨hcj, hlm⟩; exact ⟨⟨hlm, le_of_eq hcj⟩, Or.inl hcj⟩
      rw [hL, hR]; exact hbh m
    · -- i > j: c l ≤ i holds on `X`; reindex by σ
      have hL : (Finset.univ.filter
            (fun l : Fin (Specht.nOf μ) => ((l : ℕ) < m ∧ c l ≤ i) ∧ (c l = j ∨ c l = j + 1)))
          = (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) < m ∧ (c l = j ∨ c l = j + 1))) := by
        apply Finset.filter_congr; intro l _
        constructor
        · rintro ⟨⟨hlm, _⟩, hx⟩; exact ⟨hlm, hx⟩
        · rintro ⟨hlm, hx⟩; refine ⟨⟨hlm, ?_⟩, hx⟩; rcases hx with h | h <;> omega
      have hR : (Finset.univ.filter
            (fun l => (((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ c l ≤ i) ∧ (c l = j ∨ c l = j + 1)))
          = (Finset.univ.filter
              (fun l => ((σ l : Fin (Specht.nOf μ)) : ℕ) < m ∧ (c l = j ∨ c l = j + 1))) := by
        apply Finset.filter_congr; intro l _
        constructor
        · rintro ⟨⟨hlm, _⟩, hx⟩; exact ⟨hlm, hx⟩
        · rintro ⟨hlm, hx⟩; refine ⟨⟨hlm, ?_⟩, hx⟩; rcases hx with h | h <;> omega
      rw [hL, hR]
      apply le_of_eq
      refine Finset.card_bij' (fun l _ => σ⁻¹ l) (fun l _ => σ l) ?_ ?_ ?_ ?_
      · intro l hl
        rw [Finset.mem_filter] at hl ⊢
        refine ⟨Finset.mem_univ _, ?_, ?_⟩
        · show ((σ (σ⁻¹ l) : Fin (Specht.nOf μ)) : ℕ) < m
          rw [Equiv.Perm.apply_inv_self]; exact hl.2.1
        · have hh := hstab (σ⁻¹ l); rw [Equiv.Perm.apply_inv_self] at hh; exact hh.mp hl.2.2
      · intro l hl
        rw [Finset.mem_filter] at hl ⊢
        exact ⟨Finset.mem_univ _, hl.2.1, (hstab l).mpr hl.2.2⟩
      · intro l _; exact Equiv.Perm.apply_inv_self σ l
      · intro l _; exact Equiv.Perm.inv_apply_self σ l
  · -- out-of-`X` part: σ fixes these, so the two filters coincide
    apply le_of_eq
    apply congrArg Finset.card
    apply Finset.filter_congr
    intro l _
    by_cases hx : c l = j ∨ c l = j + 1
    · simp [hx]
    · simp [hsupp l hx]

/-- **`colWt` strictly drops under a two-column shuffle (piece A capstone).** For a
permutation `σ` supported on the two columns `X = colPattern t ⁻¹ {j, j+1}`, with
the threshold-`j` bottom-heaviness and a genuine column change
(`colPattern (σ·t) ≠ colPattern t`), the column-dominance measure strictly
decreases: `colWt (σ·t) < colWt t`. This is exactly the per-shuffle input
`polytabloid_mem_span_colWt_of_decrease` consumes; piece B (the `A∪B`-from-
violation construction) is left only to supply `hsupp`/`hstab`/`hbh`/`hne`. -/
theorem colWt_lt_of_two_column {t : Tableau μ}
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} {j : ℕ}
    (hsupp : ∀ l, ¬ (Specht.colPattern t l = j ∨ Specht.colPattern t l = j + 1) → σ l = l)
    (hstab : ∀ l, (Specht.colPattern t (σ l) = j ∨ Specht.colPattern t (σ l) = j + 1)
                ↔ (Specht.colPattern t l = j ∨ Specht.colPattern t l = j + 1))
    (hbh : ∀ m, (Finset.univ.filter
            (fun l => Specht.colPattern t l = j ∧ (l : ℕ) < m)).card
          ≤ (Finset.univ.filter
            (fun l => Specht.colPattern t l = j ∧ ((σ l : Fin (Specht.nOf μ)) : ℕ) < m)).card)
    (hne : Specht.colPattern (σ • t) ≠ Specht.colPattern t) :
    colWt (σ • t) < colWt t := by
  apply colWt_lt_of_patRel (s := t) (t := σ • t)
  · have hp := patRel_comp_perm_two_column (Specht.colPattern t) σ j hsupp hstab hbh
    have heq : Specht.colPattern (σ • t) = fun l => Specht.colPattern t (σ⁻¹ l) := by
      rw [Specht.colPattern_smul]; rfl
    rw [heq]; exact hp
  · exact fun h => hne h.symm

/-! ## Piece B (geometric): the all-`B`<all-`A` bottom-heaviness

The mathematical heart of the Garnir `hbh` hypothesis. At a row-violation in a
column-standard tableau, the column-`j` Garnir cells `A` hold the `|A|` *largest*
labels of `X = A ∪ B` (every `B`-label `<` every `A`-label). Abstractly: if `A`
is the "top" subset of `S` — every element of `S` outside `A` is smaller than
every element of `A` — then any equal-size subset `A' ⊆ S` is **more
bottom-heavy** (`#(A ∩ [0,m)) ≤ #(A' ∩ [0,m))` for all `m`). This is the
combinatorial core; the Garnir reindex turns `hbh` into exactly this with
`A' = σ(A)`. -/

/-- **A "top" subset is the least bottom-heavy.** If every element of `S` outside
`A` is `<` every element of `A`, then any equal-cardinality subset `A' ⊆ S`
captures at least as many elements below each threshold `m`. -/
theorem bottomHeavy_of_top_subset {n : ℕ} (S A A' : Finset (Fin n))
    (hA'S : A' ⊆ S) (hcard : A'.card = A.card)
    (htop : ∀ a ∈ A, ∀ s ∈ S, s ∉ A → (s : ℕ) < (a : ℕ)) (m : ℕ) :
    (A.filter (fun l : Fin n => (l : ℕ) < m)).card ≤ (A'.filter (fun l : Fin n => (l : ℕ) < m)).card := by
  classical
  have key : (A'.filter (fun l : Fin n => ¬ (l : ℕ) < m)).card
      ≤ (A.filter (fun l : Fin n => ¬ (l : ℕ) < m)).card := by
    rcases A.eq_empty_or_nonempty with hAe | hAne
    · have hA' : A' = ∅ := Finset.card_eq_zero.mp (by rw [hcard, hAe]; rfl)
      rw [hA', hAe]
    · rcases le_or_gt m (A.min' hAne : ℕ) with hmt | hmt
      · have hAfull : A.filter (fun l : Fin n => ¬ (l : ℕ) < m) = A := by
          apply Finset.filter_true_of_mem
          intro a ha
          have : (A.min' hAne : ℕ) ≤ (a : ℕ) := A.min'_le a ha
          omega
        rw [hAfull]
        calc (A'.filter (fun l : Fin n => ¬ (l : ℕ) < m)).card ≤ A'.card := Finset.card_filter_le _ _
          _ = A.card := hcard
      · apply Finset.card_le_card
        intro s hs
        rw [Finset.mem_filter] at hs ⊢
        obtain ⟨hsA', hsm⟩ := hs
        refine ⟨?_, hsm⟩
        by_contra hsnA
        have hlt := htop (A.min' hAne) (A.min'_mem hAne) s (hA'S hsA') hsnA
        have hsm' : m ≤ (s : ℕ) := not_lt.mp hsm
        omega
  have eA : (A.filter (fun l : Fin n => (l : ℕ) < m)).card
      + (A.filter (fun l : Fin n => ¬ (l : ℕ) < m)).card = A.card :=
    Finset.filter_card_add_filter_neg_card_eq_card _
  have eA' : (A'.filter (fun l : Fin n => (l : ℕ) < m)).card
      + (A'.filter (fun l : Fin n => ¬ (l : ℕ) < m)).card = A'.card :=
    Finset.filter_card_add_filter_neg_card_eq_card _
  omega

end QOU.BraidKnot.SpechtGarnirWt
