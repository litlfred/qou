import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Field.ZMod
import QOU.BraidKnot.SpechtStandardBasis
import QOU.BraidKnot.SpechtBaseChange
import QOU.BraidKnot.SpechtCrossKappa

/-!
# QOU.BraidKnot.SpechtCharFreeStandardBasis — characteristic-free standard basis and modular counterexample (`qou-73kb`)

Resolves bean `qou-73kb` (*audit which Specht `CharZero` hypotheses are load-bearing and which are
proof artifacts*) in machine-checked form without altering precompiled signatures of the 25 existing
`Specht*.lean` modules:

1. **Category-2 proof artifact #1 (`SpechtCrossKappa.polytabloid_ne_zero`) — generalized to any
   nontrivial commutative ring.**
   `SpechtCrossKappa.polytabloid_ne_zero` required `[Field K] [CharZero K]` because it evaluated
   `⟨e_t, e_t⟩ = |C_t| ≠ 0`. In fact the `{t}`-coordinate of `e_t` is `+1` by
   `SpechtTriangularCore.colStab_inf_rowStab_eq_one` (`C_t ∩ R_t = {1}`), giving
   `polytabloid_diag_one` over `[CommRing R]` and `polytabloid_ne_zero_charFree` over
   `[CommRing R] [Nontrivial R]`.

2. **Category-2 proof artifact #2 (`SpechtStandardBasisCore.transversal_sum_eq_zero` →
   `SpechtStandardBasis.specht_finrank_eq_numSYT`) — generalized to ANY field `[Field k]` of
   arbitrary characteristic.**
   In `SpechtStandardBasisCore`, the *only* step using `[CharZero k]` in the entire Garnir
   straightening / standard-basis chain is cancelling `|H| = |S_A × S_B|` in
   `transversal_sum_eq_zero`. Because polytabloids have `ℤ`-coordinates
   (`SpechtBaseChange.polytabloid_apply_eq_intCast`), the transversal Garnir identity established at
   `k := ℚ` (`[Field ℚ] [CharZero ℚ]`) forces every integer tabloid coordinate of the signed
   transversal sum to vanish in `ℤ`, and therefore to vanish after casting into *any* commutative
   ring (`transversal_rep_sum_eq_zero_of_rat`). Re-assembling with the `[CharZero]`-free Garnir
   decrease and triangular-independence lemmas yields:
   * `standardBasis_charFree : Module.Basis (StandardYoungTableau μ) k (SpechtSubmodule (k := k) μ)`
   * `specht_finrank_eq_numSYT_charFree : Module.finrank k (SpechtSubmodule (k := k) μ) = numSYT μ`
   over **every** `[Field k]` (including `𝔽_p` for `p ∣ n!`), with zero `sorry` and zero `[CharZero k]`.

3. **Category-1 load-bearing boundary (`SpechtIrreducible.specht_form_nondegenerate`) — proved
   FALSE without `[CharZero k]`.**
   Over `K = ZMod 2` (`[Field (ZMod 2)]`), for the two-box single-column shape `colTwo = [1, 1]`,
   every tableau has full column stabilizer `C_t = ⊤` of cardinality `2`, so `e_t ≠ 0` lies in the
   radical of `bilinM` on `S^{[1,1]}` (`specht_form_rad_nontrivial_zmod2`). Thus `[CharZero k]` on
   `specht_form_nondegenerate`, `specht_isSimple`, `isCompl_specht_perp`, and the Wedderburn /
   classification theorems is mathematically necessary (James's `D^λ = S^λ / (S^λ ∩ (S^λ)ᗮ)`).

## Base ring (§7c)
Purely algebraic (`[CommRing R]`, `[Field k]`, `ZMod 2`); no `ℝ`, no `Real.*`, no archimedean order.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtCharFreeStandardBasis

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

/-! ## 1. Characteristic-free nonvanishing of polytabloids (`[CommRing R] [Nontrivial R]`) -/

/-- The `{t}`-coordinate of any polytabloid `e_t` over any commutative ring `R` is `1`:
a column permutation `π ∈ C_t` satisfies `{π • t} = {t}` iff `π ∈ R_t`, forcing `π = 1`
by `C_t ∩ R_t = {1}`. -/
theorem polytabloid_diag_one {R : Type} [CommRing R] (μ : YoungDiagram) (t : Tableau μ) :
    (polytabloid (k := R) t) (Tabloid.mk t) = 1 := by
  classical
  rw [polytabloid, Finsupp.finset_sum_apply]
  have hterm : ∀ π : colStab t,
      ((Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
        Mtab.of (k := R) ((π : Equiv.Perm (Fin (nOf μ))) • t)) (Tabloid.mk t)
        = (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
            (if (π : Equiv.Perm (Fin (nOf μ))) ∈ rowStab t then (1 : R) else 0) := by
    intro π
    rw [Finsupp.smul_apply]
    congr 1
    rw [Mtab.of, Finsupp.single_apply]
    have hmk : (Tabloid.mk ((π : Equiv.Perm (Fin (nOf μ))) • t) = Tabloid.mk t)
        ↔ (π : Equiv.Perm (Fin (nOf μ))) ∈ rowStab t := by
      rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff, rowPattern_smul, mem_rowStab]
    by_cases h : (π : Equiv.Perm (Fin (nOf μ))) ∈ rowStab t
    · rw [if_pos (hmk.2 h), if_pos h]
    · rw [if_neg (fun heq => h (hmk.1 heq)), if_neg h]
  simp_rw [hterm]
  rw [Finset.sum_eq_single (⟨1, Subgroup.one_mem _⟩ : colStab t)]
  · have h1r : (1 : Equiv.Perm (Fin (nOf μ))) ∈ rowStab t := Subgroup.one_mem _
    simp only [if_pos h1r, Equiv.Perm.sign_one, Units.val_one, one_zsmul]
  · intro π _ hπne
    by_cases h : (π : Equiv.Perm (Fin (nOf μ))) ∈ rowStab t
    · exfalso
      apply hπne
      apply Subtype.ext
      exact SpechtTriangularCore.colStab_inf_rowStab_eq_one t π.2 h
    · simp [if_neg h]
  · intro hmem
    exact absurd (Finset.mem_univ _) hmem

/-- **Characteristic-free `polytabloid_ne_zero`.** Over any nontrivial commutative ring `R`
(no `Field`, no `CharZero`), every polytabloid is nonzero because its `{t}`-coordinate is `1`. -/
theorem polytabloid_ne_zero_charFree {R : Type} [CommRing R] [Nontrivial R]
    (μ : YoungDiagram) (t : Tableau μ) :
    polytabloid (k := R) t ≠ 0 := by
  intro hzero
  have h1 := polytabloid_diag_one (R := R) μ t
  rw [hzero, Finsupp.zero_apply] at h1
  exact zero_ne_one h1

/-! ## 2. Base-change elimination of `CharZero` from Garnir transversal annihilation -/

/-- Every tabloid coordinate of a `ℤ`-signed sum of permuted polytabloids over `S` is the cast of
the corresponding integer coordinate over `ℤ`. -/
theorem transversal_polytabloid_sum_apply_intCast {S : Type} [CommRing S]
    {μ : YoungDiagram} (t : Tableau μ)
    (T : Finset (Equiv.Perm (Fin (nOf μ)))) (d : Tabloid μ) :
    (∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • polytabloid (k := S) (π • t)) d
      = ((∑ π ∈ T, (Equiv.Perm.sign π : ℤ) * (polytabloid (k := ℤ) (π • t)) d : ℤ) : S) := by
  rw [Finsupp.finset_sum_apply, Int.cast_sum]
  refine Finset.sum_congr rfl (fun π _ => ?_)
  rw [Finsupp.smul_apply, SpechtBaseChange.polytabloid_apply_eq_intCast (S := S) (π • t) d,
    zsmul_eq_mul, Int.cast_mul]

/-- **Characteristic-free transfer of Garnir transversal annihilation.**
If the `ℤ`-signed transversal sum `∑_{π ∈ T} sgn(π) · (π · e_t)` vanishes over `ℚ`, then its
underlying `ℤ`-coordinates vanish identically, so the sum vanishes over **any** field `k`
(with no `[CharZero k]` assumption). -/
theorem transversal_rep_sum_eq_zero_of_rat {k : Type} [Field k] {μ : YoungDiagram}
    (t : Tableau μ) (T : Finset (Equiv.Perm (Fin (nOf μ))))
    (hQ : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Mtab.rep μ π (polytabloid (k := ℚ) t) = 0) :
    ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Mtab.rep μ π (polytabloid (k := k) t) = 0 := by
  have hrwK : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • Mtab.rep μ π (polytabloid (k := k) t)
      = ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • polytabloid (k := k) (π • t) :=
    Finset.sum_congr rfl (fun π _ => by rw [← polytabloid_rep_smul])
  have hrwQ : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • Mtab.rep μ π (polytabloid (k := ℚ) t)
      = ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • polytabloid (k := ℚ) (π • t) :=
    Finset.sum_congr rfl (fun π _ => by rw [← polytabloid_rep_smul])
  rw [hrwQ] at hQ
  rw [hrwK]
  ext d
  rw [Finsupp.zero_apply, transversal_polytabloid_sum_apply_intCast (S := k) t T d]
  have hdQ : (∑ π ∈ T, (Equiv.Perm.sign π : ℤ) • polytabloid (k := ℚ) (π • t)) d = 0 := by
    rw [hQ, Finsupp.zero_apply]
  rw [transversal_polytabloid_sum_apply_intCast (S := ℚ) t T d, Int.cast_eq_zero] at hdQ
  rw [hdQ, Int.cast_zero]

/-! ## 3. Characteristic-free Garnir straightening and standard-basis theorem (`[Field k]`) -/

section ArbitraryField

variable {k : Type} [Field k] {μ : YoungDiagram}

/-- **Characteristic-free Garnir straightening core (column-word-minimal case).**
Identical to `SpechtStandardBasis.straightening_step_colMax`, with `[CharZero k]` removed by
computing the Garnir transversal annihilation over `ℚ` and transferring via `ℤ`-coordinates. -/
theorem straightening_step_colMax_charFree (t : Tableau μ)
    (h : polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (nOf μ))) • t)) :
    ∃ (s : Finset (Tableau μ)) (c : Tableau μ → k),
      (∀ t' ∈ s, colWordNum t' < colWordNum t) ∧
      polytabloid (k := k) t = ∑ t' ∈ s, c t' • polytabloid (k := k) t' := by
  classical
  obtain ⟨i, j, hij, hij1, hdesc⟩ := exists_row_descent_of_colWordMin t h hmax
  obtain ⟨T, π₀, hπ₀T, hπ₀H, hother, hcover, hclosed, hcard⟩ :=
    garnir_transversal_with_pivot (μ := μ) t i j
  have h1H : (1 : Equiv.Perm (Fin (nOf μ))) ∈ garnirH t i j := by
    rw [garnirH, Finset.mem_inter]
    exact ⟨by rw [garnirG, Finset.mem_filter]; exact ⟨Finset.mem_univ _, fun l _ => rfl⟩,
      by rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, Subgroup.one_mem _⟩⟩
  have hannQ : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
      Mtab.rep μ π (polytabloid (k := ℚ) t) = 0 := by
    apply transversal_sum_eq_zero (k := ℚ) t T (garnirH t i j)
      (garnirH_subset_colStab t i j) (garnirH_card_pos t i j)
    rw [← sum_over_garnirG_reindex t i j T hcover hclosed hcard
      (fun σ => (Equiv.Perm.sign σ : ℤ) • Mtab.rep μ σ (polytabloid (k := ℚ) t))]
    exact garnir_full_annihilation (k := ℚ) t hij hij1
  have hann : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
      Mtab.rep μ π (polytabloid (k := k) t) = 0 :=
    transversal_rep_sum_eq_zero_of_rat t T hannQ
  have hfix : Mtab.rep μ π₀ (polytabloid (k := k) t)
      = (Equiv.Perm.sign π₀ : ℤ) • polytabloid (k := k) t :=
    rep_polytabloid_of_mem_colStab t (garnirH_subset_colStab t i j π₀ hπ₀H)
  have hgood : ∀ π ∈ T, π ≠ π₀ →
      ∃ u : Tableau μ, colWordNum u < colWordNum t ∧
        ∃ ε : k, polytabloid (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • t)
          = ε • polytabloid (k := k) u := by
    intro π hπT hπne
    have hπnotH : π ∉ garnirH t i j := hother π hπT hπne
    have hπG : π ∈ garnirG t i j := by
      apply hclosed
      rw [Finset.mem_image]
      exact ⟨(π, 1), Finset.mem_product.mpr ⟨hπT, h1H⟩, mul_one π⟩
    obtain ⟨ρ, hρmem, hlt⟩ := fibre_colWordNum_decrease t hij hij1 hmax hdesc hπG hπnotH
    refine ⟨ρ • (π • t), hlt, ((Equiv.Perm.sign ρ : ℤ) : k), ?_⟩
    have hpoly : polytabloid (k := k) (π • t)
        = (Equiv.Perm.sign ρ : ℤ) • polytabloid (k := k) (ρ • (π • t)) := by
      rw [polytabloid_colStab_smul (π • t) hρmem, smul_smul]
      have hs2 : (Equiv.Perm.sign ρ : ℤ) * (Equiv.Perm.sign ρ : ℤ) = 1 := by
        rcases Int.units_eq_one_or (Equiv.Perm.sign ρ) with hh | hh <;> rw [hh] <;> decide
      rw [hs2, one_smul]
    rw [hpoly, ← Int.cast_smul_eq_zsmul k]
  obtain ⟨s, c, hsP, hseq⟩ := garnir_assembly_gen t
    (fun t' => ∃ u : Tableau μ, colWordNum u < colWordNum t ∧
      ∃ ε : k, polytabloid (k := k) t' = ε • polytabloid (k := k) u)
    T π₀ hπ₀T hfix hgood hann
  exact poly_combo_reindex t s c hseq hsP

/-- **Characteristic-free Garnir straightening step.** -/
theorem straightening_step_charFree (t : Tableau μ)
    (h : polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ))) :
    ∃ (s : Finset (Tableau μ)) (c : Tableau μ → k),
      (∀ t' ∈ s, colWordNum t' < colWordNum t) ∧
      polytabloid (k := k) t = ∑ t' ∈ s, c t' • polytabloid (k := k) t' := by
  classical
  by_cases hraise : ∃ σ : colStab t,
      colWordNum ((σ : Equiv.Perm (Fin (nOf μ))) • t) < colWordNum t
  · obtain ⟨σ, hσ⟩ := hraise
    set σ0 : Equiv.Perm (Fin (nOf μ)) := (σ : Equiv.Perm (Fin (nOf μ)))
    have hmem : σ0 ∈ colStab t := σ.property
    have hpc : polytabloid (k := k) (σ0 • t)
        = (Equiv.Perm.sign σ0 : ℤ) • polytabloid (k := k) t :=
      polytabloid_colStab_smul (k := k) t hmem
    have hs2 : (Equiv.Perm.sign σ0 : ℤ) * (Equiv.Perm.sign σ0 : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign σ0) with h1 | h1 <;> rw [h1] <;> decide
    refine ⟨{σ0 • t}, fun _ => ((Equiv.Perm.sign σ0 : ℤ) : k), ?_, ?_⟩
    · intro t' ht'
      rw [Finset.mem_singleton] at ht'; subst ht'; exact hσ
    · rw [Finset.sum_singleton, hpc,
          ← Int.cast_smul_eq_zsmul k (Equiv.Perm.sign σ0 : ℤ) (polytabloid (k := k) t),
          smul_smul, ← Int.cast_mul, hs2, Int.cast_one, one_smul]
  · push_neg at hraise
    exact straightening_step_colMax_charFree (k := k) t h hraise

/-- **Characteristic-free spanning of standard polytabloids in `M^μ`.** -/
theorem standardPolytabloid_straightening_charFree :
    ∀ t : Tableau μ,
      polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  intro t
  generalize hg : colWordNum t = g
  induction g using Nat.strong_induction_on generalizing t with
  | _ g IH =>
    by_cases hr : polytabloid (k := k) t ∈
        Set.range (standardPolytabloid (k := k) (μ := μ))
    · exact Submodule.subset_span hr
    · obtain ⟨s, c, hgt, heq⟩ := straightening_step_charFree (k := k) t hr
      rw [heq]
      refine Submodule.sum_mem _ (fun t' ht' => ?_)
      refine Submodule.smul_mem _ _ ?_
      have hlt : colWordNum t' < colWordNum t := hgt t' ht'
      exact IH (colWordNum t') (by omega) t' rfl

/-- **Characteristic-free `M^μ`-level span identity.** -/
theorem standardPolytabloid_span_eq_specht_charFree :
    Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ)))
      = SpechtSubmodule (k := k) μ := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro _ ⟨T, rfl⟩
    exact standardPolytabloid_mem (k := k) T
  · rw [SpechtSubmodule, Submodule.span_le, Set.range_subset_iff]
    exact standardPolytabloid_straightening_charFree (k := k) (μ := μ)

/-- **Characteristic-free `S^μ`-level spanning (`span = ⊤`).** -/
theorem standardPolytabloid_span_charFree :
    Submodule.span k (Set.range (standardPolytabloidS (k := k) (μ := μ))) = ⊤ := by
  apply Submodule.map_injective_of_injective
    (Submodule.injective_subtype (SpechtSubmodule (k := k) μ))
  rw [Submodule.map_subtype_top, Submodule.map_span, ← Set.range_comp,
      subtype_comp_standardPolytabloidS]
  exact standardPolytabloid_span_eq_specht_charFree (k := k) (μ := μ)

/-- **Characteristic-free standard basis of `S^μ`** over an arbitrary field `k` (no `[CharZero k]`). -/
noncomputable def standardBasis_charFree :
    Module.Basis (StandardYoungTableau μ) k (SpechtSubmodule (k := k) μ) :=
  Module.Basis.mk standardPolytabloid_linearIndependent
    (by rw [standardPolytabloid_span_charFree])

/-- **Characteristic-free standard-basis dimension theorem (Sagan Thm 2.5.2 / James Thm 8.4):**
`dim_k S^μ = #SYT(μ)` over **every** field `k` of arbitrary characteristic `p ≥ 0`. -/
theorem specht_finrank_eq_numSYT_charFree (μ : YoungDiagram) :
    Module.finrank k (SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ := by
  rw [Module.finrank_eq_nat_card_basis (standardBasis_charFree (k := k) (μ := μ))]
  rfl

end ArbitraryField

/-! ## 4. Category-1 load-bearing witness: Gram form degenerates in prime characteristic -/

/-- The single-column two-cell Young diagram `μ = [1, 1]` (`1² ⊢ 2`), with cells `{(0, 0), (1, 0)}`. -/
def colTwo : YoungDiagram where
  cells := {(0, 0), (1, 0)}
  isLowerSet := by
    intro a b hle ha
    simp only [Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton] at ha ⊢
    rcases a with ⟨ra, ca⟩
    rcases b with ⟨rb, cb⟩
    have h1 : rb ≤ ra := hle.1
    have h2 : cb ≤ ca := hle.2
    rcases ha with ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩
    · left; exact Prod.ext (by omega) (by omega)
    · have hcb : cb = 0 := by omega
      subst hcb
      have hrb : rb = 0 ∨ rb = 1 := by omega
      rcases hrb with rfl | rfl
      · left; rfl
      · right; rfl

theorem colTwo_card : nOf colTwo = 2 := by
  decide

/-- Every cell of `colTwo = [1, 1]` lies in column `0`. -/
theorem colTwo_col_eq_zero (c : colTwo.cells) : (c : ℕ × ℕ).2 = 0 := by
  rcases c with ⟨⟨r, col⟩, hc⟩
  simp only [colTwo, Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq] at hc
  rcases hc with ⟨_, rfl⟩ | ⟨_, rfl⟩ <;> rfl

/-- Every permutation of `Fin (nOf colTwo)` lies in the column stabilizer of any `colTwo`-tableau. -/
theorem colTwo_colStab_eq_top (t : Tableau colTwo) :
    colStab t = ⊤ := by
  ext σ
  simp only [Subgroup.mem_top, iff_true, mem_colStab]
  funext l
  show (t (σ.symm l) : ℕ × ℕ).2 = (t l : ℕ × ℕ).2
  rw [colTwo_col_eq_zero, colTwo_col_eq_zero]

/-- The column stabilizer of any `colTwo`-tableau has cardinality `2! = 2`. -/
theorem colTwo_card_colStab (t : Tableau colTwo) :
    Fintype.card (colStab t) = 2 := by
  have htop : Fintype.card (colStab t) = Fintype.card (Equiv.Perm (Fin (nOf colTwo))) :=
    Fintype.card_congr
      { toFun := fun x => x.1
        invFun := fun σ => ⟨σ, by rw [colTwo_colStab_eq_top]; trivial⟩
        left_inv := fun x => Subtype.ext rfl
        right_inv := fun _ => rfl }
  rw [htop, Fintype.card_perm, Fintype.card_fin, colTwo_card]
  rfl

/-- **Category-1 load-bearing certificate (`ZMod 2`):**
Over `K = ZMod 2` (`[Field (ZMod 2)]`, since `2` is prime), there exists a **nonzero** element of
`SpechtSubmodule colTwo` that is orthogonal under `SpechtIrreducible.bilinM` to the **entire**
Specht submodule `SpechtSubmodule colTwo`. Hence `SpechtIrreducible.specht_form_nondegenerate` is
genuinely **false** when `[CharZero k]` is dropped. -/
theorem specht_form_rad_nontrivial_zmod2 :
    ∃ x ∈ SpechtSubmodule (k := ZMod 2) colTwo,
      x ≠ 0 ∧ ∀ y ∈ SpechtSubmodule (k := ZMod 2) colTwo,
        SpechtIrreducible.bilinM (k := ZMod 2) colTwo x y = 0 := by
  classical
  haveI : Fact (Nat.Prime 2) := ⟨by decide⟩
  have hcard : Fintype.card colTwo.cells = nOf colTwo := by
    rw [Fintype.card_coe]
  let t : Tableau colTwo := ((Fintype.equivFin colTwo.cells).trans (finCongr hcard)).symm
  refine ⟨polytabloid (k := ZMod 2) t, polytabloid_mem_specht t,
    polytabloid_ne_zero_charFree colTwo t, ?_⟩
  intro y hy
  refine Submodule.span_induction ?_ ?_ ?_ ?_ hy
  · rintro _ ⟨t', rfl⟩
    obtain ⟨σ, rfl⟩ := SpechtIrreducible.tableau_transitive t t'
    have hσmem : σ ∈ colStab t := by rw [colTwo_colStab_eq_top]; trivial
    rw [polytabloid_colStab_smul (k := ZMod 2) t hσmem, map_zsmul,
      SpechtIrreducible.bilinM_polytabloid_self (k := ZMod 2) colTwo t, colTwo_card_colStab]
    have h2 : ((2 : ℕ) : ZMod 2) = 0 := ZMod.natCast_self 2
    rw [h2, zsmul_zero]
  · simp
  · intro a b _ _ ha hb
    rw [map_add, ha, hb, add_zero]
  · intro c a _ ha
    rw [map_smul, ha, smul_zero]

end QOU.BraidKnot.SpechtCharFreeStandardBasis
