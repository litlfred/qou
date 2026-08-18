import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.SytRigidity
import QOU.BraidKnot.SpechtClassification

/-!
# `QOU.SchurWeyl.HoefsmitGeneral` — the general-`λ` Hoefsmit representation, assembled

Closes the last gap of bean `qou-im9l` (SW-4-gen).  Everything it needs is already proved:

* `SeminormalRep.seminormalRepFin` — the representation `H_{N-1}(q) →ₐ[ℝ] M_{d_λ}(ℝ)`, built
  from `genMat_quadratic` / `genMat_far_comm` / `genMat_braid` through `Hecke.lift` and
  transported along `Fintype.equivFin`;
* `SeminormalRep.genMat_ne_scalar` — a generator that *moves some tableau* is not scalar;
* `TableauCells.exists_admissible_of_ne` — two distinct tableaux force such a generator.

The statement is the one `HoefsmitRep.hoefsmit_seminormal_rep` carried as a `-- Ref:`-cited
`sorry`.  It cannot be discharged there: the proof runs through `SeminormalRep`, which imports
`HoefsmitRep`, so the theorem has to live downstream.

Base ring `ℝ` (the seminormal parameters are archimedean, §7c).
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)

/-- **`|shape λ| = N`** — the Young diagram of a partition of `N` has `N` cells. -/
theorem card_shape {N : ℕ} (lam : Partition N) : (shape lam).cells.card = N := by
  have hrow : (shape lam).rowLens = lam.parts.sort (· ≥ ·) :=
    YoungDiagram.rowLens_ofRowLens_eq_self
      (QOU.BraidKnot.SpechtClassification.sorted_parts_pos N lam)
  have h := QOU.BraidKnot.SpechtClassification.card_eq_rowLens_sum (shape lam)
  rw [hrow] at h
  have hq : ((lam.parts.sort (· ≥ ·) : List ℕ) : Multiset ℕ) = lam.parts :=
    Multiset.sort_eq _ _
  have hsum : (lam.parts.sort (· ≥ ·)).sum = N := by
    rw [← Multiset.sum_coe, hq]
    exact lam.parts_sum
  exact h.trans hsum

/-- **The general-`λ` Hoefsmit seminormal representation.**  For every partition `λ ⊢ N`
there is an algebra map `H_{N-1}(q) →ₐ[ℝ] M_{d_λ}(ℝ)`, and when `d_λ ≥ 2` some generator is
sent to a **non-scalar** matrix (so the representation is not a sum of characters).

This is the statement `HoefsmitRep.hoefsmit_seminormal_rep` carried as a cited `sorry`; it
is proved here because the argument runs through `SeminormalRep`, which imports
`HoefsmitRep`.

The two inputs: `SeminormalRep.seminormalRepFin` (the representation, from the three Hecke
relations via `Hecke.lift`) and, for non-scalarity, `TableauCells.exists_admissible_of_ne`
feeding `SeminormalRep.genMat_ne_scalar`. -/
theorem hoefsmit_seminormal_rep_general {N : ℕ} (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (lam : Partition N) :
    ∃ ρ : Hecke ℝ q q⁻¹ (N - 1) →ₐ[ℝ] Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ,
      2 ≤ dLambda lam →
        ∃ i : Fin (N - 1), ∀ s : ℝ,
          ρ (Hecke.σ ℝ q q⁻¹ (N - 1) i)
            ≠ s • (1 : Matrix (Fin (dLambda lam)) (Fin (dLambda lam)) ℝ) := by
  rcases Nat.eq_zero_or_pos N with hN0 | hNpos
  · -- Empty shape: exactly one tableau, so `2 ≤ d_λ` is false and the implication is vacuous.
    subst hN0
    refine ⟨Hecke.lift ℝ q q⁻¹ 0 Fin.elim0 (fun i => i.elim0) (fun i => i.elim0)
      (fun i => i.elim0), ?_⟩
    intro h2
    exfalso
    have hsub : Subsingleton (SYT lam) := by
      refine ⟨fun U V => TableauCells.syt_eq_of_cellOf_eq U V (fun j hj => ?_)⟩
      have h1 := hj.1
      have h2' := hj.2
      rw [card_shape] at h2'
      omega
    have hle : Fintype.card (SYT lam) ≤ 1 := Fintype.card_le_one_iff_subsingleton.mpr hsub
    have : dLambda lam = Fintype.card (SYT lam) := rfl
    omega
  · obtain ⟨m, rfl⟩ : ∃ m, N = m + 1 := ⟨N - 1, by omega⟩
    have hN : (shape lam).cells.card = m + 1 := card_shape lam
    refine ⟨SeminormalRep.seminormalRepFin q hq hq2 lam m hN, ?_⟩
    intro h2
    -- `d_λ ≥ 2` gives two distinct tableaux, hence an admissible swap.
    have hcard : 1 < Fintype.card (SYT lam) := by
      have : dLambda lam = Fintype.card (SYT lam) := rfl
      omega
    obtain ⟨U, V, hUV⟩ := (Fintype.one_lt_card_iff_nontrivial.mp hcard).exists_pair_ne
    obtain ⟨T, k, hk1, hkn, hadm⟩ := TableauCells.exists_admissible_of_ne hUV
    have hkm : k - 1 < m := by omega
    refine ⟨⟨k - 1, hkm⟩, ?_⟩
    intro s hcon
    have hik : ((⟨k - 1, hkm⟩ : Fin m) : ℕ) + 1 = k := by simp; omega
    have hk1' : 1 ≤ ((⟨k - 1, hkm⟩ : Fin m) : ℕ) + 1 := by omega
    have hkn' : ((⟨k - 1, hkm⟩ : Fin m) : ℕ) + 1 + 1 ≤ (shape lam).cells.card := by
      rw [hik]; exact hkn
    have hadm' : TableauCells.SwapAdmissible T (((⟨k - 1, hkm⟩ : Fin m) : ℕ) + 1) := by
      rw [hik]; exact hadm
    -- The image is the reindexed generator matrix; reindexing is injective and fixes scalars.
    have hcon2 : (Matrix.reindexAlgEquiv ℝ ℝ (Fintype.equivFin (SYT lam)))
        (SeminormalRep.seminormalRep q hq hq2 m hN
          (Hecke.σ ℝ q q⁻¹ m ⟨k - 1, hkm⟩)) = s • 1 := hcon
    rw [SeminormalRep.seminormalRep_σ] at hcon2
    have hgen : SeminormalRep.genMat q (((⟨k - 1, hkm⟩ : Fin m) : ℕ) + 1) hk1' hkn'
        = s • (1 : Matrix (StandardYoungTableau (shape lam))
                (StandardYoungTableau (shape lam)) ℝ) := by
      have hinj := (Matrix.reindexAlgEquiv ℝ ℝ (Fintype.equivFin (SYT lam))).injective
      apply hinj
      rw [map_smul, map_one]
      exact hcon2
    exact SeminormalRep.genMat_ne_scalar q _ hk1' hkn' hadm' s hgen

end QOU.SchurWeyl
