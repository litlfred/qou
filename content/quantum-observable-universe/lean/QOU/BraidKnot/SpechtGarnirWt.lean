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

end QOU.BraidKnot.SpechtGarnirWt
