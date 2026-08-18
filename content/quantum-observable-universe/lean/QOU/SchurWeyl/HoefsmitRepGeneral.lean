import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.SytAdmissible
import QOU.Mathlib.YoungDiagramCard

/-!
# `hoefsmit_seminormal_rep`, proved

The general-`λ` seminormal representation, with the non-degeneracy that distinguishes it from the
trivial `q·1` matrix rep. This statement carried a `-- Ref:`-cited `sorry` in `HoefsmitRep.lean`
from the file's creation; it is discharged here, and **removed there** rather than left standing
beside a proved twin.

It lives in its own file for an import reason, not a stylistic one: the proof consumes
`SeminormalRep.seminormalRepFin`, and `SeminormalRep` imports `TableauCells`, which imports
`HoefsmitRep`. Stating it where it was would be circular.

## What closed it, and in what order

Three things had to land, and only the middle one was ever the hard part:

1. **The braid relation for arbitrary `λ`** — `SeminormalRep.genMat_braid`, unconditional on all of
   `SYT μ`, dispatching over every `⟨s_k, s_{k+1}⟩`-orbit shape (PR #5076). This is what bean
   `qou-im9l` called "the hard core, NOT a plumbing task, multi-session".
2. **Non-scalarity's missing half** — `TableauCells.exists_swapAdmissible_of_one_lt_card`
   (bean SW-5, PR #5266). `genMat_ne_scalar` already gave non-scalarity for a generator that
   *moves* a tableau; what was absent is that `#SYT μ ≥ 2` produces such a tableau at all.
3. **A Young-diagram cardinality lemma the pinned Mathlib lacks** —
   `QOU.Mathlib.card_cells_partitionShape`. `seminormalRepFin` takes `μ.cells.card = m + 1` as a
   hypothesis, and nothing upstream said a partition's shape has `N` cells.

Step 3 is worth flagging: the reindexing was twice described (in the bean, and in #5076's body) as
"mechanical". The reindex itself is — `seminormalRepFin` is four lines — but its *precondition* was
a missing lemma, and calling the step mechanical hid that.

## The `N = 0` branch is not a formality

`Fin (N - 1)` is `Fin 0` there, so the conclusion's `∃ i` cannot be produced and the hypothesis
`2 ≤ dLambda lam` has to be *refuted* instead. It is: the empty shape has no cells, so
`syt_ext_on_cells` makes `StandardYoungTableau` a subsingleton vacuously, giving `dLambda ≤ 1`.
The representation itself is still supplied — via `Hecke.lift` over the empty generator family.

Refs:
- [hoefsmit1974] P. N. Hoefsmit, PhD thesis, UBC (1974) — the seminormal form.
- [ram1997] A. Ram, Proc. LMS (1997), https://doi.org/10.1112/S0024611597000282 — axial distances.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib
open TableauCells

/-- A shape with no cells has at most one standard tableau: there is nothing to fill, so
`syt_ext_on_cells` applies vacuously. -/
theorem card_le_one_of_cells_card_zero {μ : YoungDiagram} (h : μ.cells.card = 0) :
    Fintype.card (StandardYoungTableau μ) ≤ 1 := by
  rw [Fintype.card_le_one_iff_subsingleton]
  refine ⟨fun T₁ T₂ => syt_ext_on_cells (fun i j hij => ?_)⟩
  exact absurd (Finset.card_eq_zero.mp h ▸ (YoungDiagram.mem_cells (i, j)).mpr hij)
    (Finset.notMem_empty _)

/-- **Hoefsmit seminormal representation, general shape `λ` — PROVED.**

For every partition `λ ⊢ N` there is a `d_λ`-dimensional representation
`ρ_λ : H_N(q) →ₐ[ℝ] M_{d_λ}(ℝ)` which, when `d_λ ≥ 2`, sends at least one generator to a
**non-scalar** matrix — so it is not the reducible `σ_i ↦ q·1` rep, and the statement is
non-vacuous.

`q ≠ 0` together with `q ^ 2 ≠ 1` says exactly that `q` is not a root of unity over `ℝ`, which is
the genericity `[ram1997]`'s axial-distance formulas presuppose. Note this **admits negative `q`**:
it is strictly weaker than `0 < q ∧ q ≠ 1`. -/
theorem hoefsmit_seminormal_rep {N : ℕ} (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (lam : Partition N) :
    ∃ ρ : Hecke ℝ q q⁻¹ (N - 1) →ₐ[ℝ] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ,
      2 ≤ dLambda lam →
        ∃ i : Fin (N - 1), ∀ s : ℝ,
          ρ (Hecke.σ ℝ q q⁻¹ (N - 1) i)
            ≠ s • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) := by
  classical
  rcases Nat.eq_zero_or_pos N with hN0 | hNpos
  · -- `Fin (N - 1)` is empty, so the payload must be refuted, not produced.
    subst hN0
    refine ⟨Hecke.lift ℝ q q⁻¹ 0 (fun i => i.elim0) (fun i => i.elim0)
      (fun i _ => i.elim0) (fun i _ => i.elim0), fun h2 => absurd h2 ?_⟩
    have hcard : (shape lam).cells.card = 0 := by
      show (partitionShape lam).cells.card = 0
      exact card_cells_partitionShape lam
    have hle : dLambda lam ≤ 1 := card_le_one_of_cells_card_zero hcard
    omega
  · have hcard : (shape lam).cells.card = (N - 1) + 1 := by
      show (partitionShape lam).cells.card = (N - 1) + 1
      rw [card_cells_partitionShape]
      omega
    refine ⟨SeminormalRep.seminormalRepFin q hq hq2 lam (N - 1) hcard, fun h2 => ?_⟩
    have h1lt : 1 < Fintype.card (StandardYoungTableau (shape lam)) := by
      have hd : dLambda lam = Fintype.card (StandardYoungTableau (shape lam)) := rfl
      omega
    obtain ⟨T, k, hk1, hk2, hadm⟩ := exists_swapAdmissible_of_one_lt_card h1lt
    -- name the predecessor so the generator index matches `genMat`'s `(i : ℕ) + 1` on the nose
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    have hkN : k' + 1 + 1 ≤ N := by
      have h := hk2
      rw [show (shape lam).cells.card = N from by
        show (partitionShape lam).cells.card = N
        exact card_cells_partitionShape lam] at h
      exact h
    refine ⟨⟨k', by omega⟩, fun s hcon => ?_⟩
    have hstep : SeminormalRep.seminormalGen q (N - 1) hcard ⟨k', by omega⟩
        = s • (1 : Matrix (StandardYoungTableau (shape lam))
            (StandardYoungTableau (shape lam)) ℝ) := by
      apply (Matrix.reindexAlgEquiv ℝ ℝ (Fintype.equivFin (SYT lam))).injective
      have hc : (Matrix.reindexAlgEquiv ℝ ℝ (Fintype.equivFin (SYT lam)))
          (SeminormalRep.seminormalRep q hq hq2 (N - 1) hcard
            (Hecke.σ ℝ q q⁻¹ (N - 1) ⟨k', by omega⟩)) = s • 1 := hcon
      rw [SeminormalRep.seminormalRep_σ] at hc
      rw [hc, map_smul, map_one]
    rw [SeminormalRep.seminormalGen] at hstep
    exact SeminormalRep.genMat_ne_scalar q (k' + 1) hk1 hk2 hadm s hstep

end QOU.SchurWeyl
