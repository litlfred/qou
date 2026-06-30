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

end QOU.BraidKnot.SpechtGarnirWt
