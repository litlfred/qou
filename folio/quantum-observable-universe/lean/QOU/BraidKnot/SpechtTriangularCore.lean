import QOU.BraidKnot.SpechtStandardBasisCore
import QOU.BraidKnot.SpechtDominanceCore
import Mathlib.Data.Finset.Sort
import Mathlib.Order.Monotone.Basic

/-!
# QOU.BraidKnot.SpechtTriangularCore — further reduction of brick-4's `Triangular` stub

`QOU.BraidKnot.SpechtStandardBasis.standardPolytabloid_triangular` packages the
linear-independence half of the standard-basis theorem into a single
`Triangular` bundle (three fields: `lead_inj`, `diag_unit`, `supp_le`) modulo
*one* `sorry`. Two of those three fields are **order-independent**; only the
third (`supp_le`, the dominance bound) needs the dominance order on tabloids and
is the genuine deep core.

This module REDUCES the bundle further: it proves **both** order-independent
fields **sorry-free** (`diag_unit` *and* `lead_inj` — the latter via the
leading-tabloid-determines-SYT argument, fully formalised here). The remaining
field (`supp_le`) is supplied by `standardPolytabloid_dominance_order`, itself
discharged **sorry-free** here by consuming the deeper relation-level core
`SpechtDominanceCore.standardPolytabloid_dominance_order'` (which peels off the
`LinearOrder` construction + `Finsupp`/`support` plumbing via a
Szpilrajn-for-Fintypes lever, leaving only Sagan's dominance lemma as
`SpechtDominanceCore.dominance_relation_exists`). It then reassembles
`standardPolytabloid_triangular'` — a verbatim restatement of the brick-4 bundle —
sorry-free modulo that one relation-level core.

It imports `SpechtStandardBasis` and `SpechtDominanceCore` read-only (mirroring how
`SpechtIrreducible` reproduces brick 2 reduced to fewer cores); it does **not**
modify them.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `colStab_inf_rowStab_eq_one` (the `C_t ∩ R_t = {1}` key lemma) | **sorry-free** |
| `standardPolytabloid_diag_coeff` (`(e_T)({T}) = 1`) | **sorry-free** |
| `standardPolytabloid_diag_unit` (the `diag_unit` field) | **sorry-free** |
| `entry_sytToTableau`, `sytToTableau_cellLabel` (decoding plumbing) | **sorry-free** |
| `entry_row_strictMonoOn`, `entry_fin_strictMono`, `rowSet_card` (row monotonicity) | **sorry-free** |
| `mem_rowSet_iff`, `rowSet_eq_of_rowPattern_eq`, `entry_eq_orderEmbOfFin` | **sorry-free** |
| `leadTab_injective_core` (leading tabloid ⇒ SYT determined) | **sorry-free** (fully proved) |
| `leadTab_injective` (the `lead_inj` field) | **sorry-free** |
| `standardPolytabloid_dominance_order` (order + `supp_le`) | **sorry-free** (consumes `SpechtDominanceCore.standardPolytabloid_dominance_order'`) |
| `standardPolytabloid_triangular'` (the reassembled bundle) | **sorry-free MODULO the single core** |

`#print axioms` confirms `sorryAx` enters `standardPolytabloid_triangular'`
*only* through the lone relation-level core
`SpechtDominanceCore.dominance_relation_exists` (Sagan's dominance lemma +
antisymmetry); everything else — both order-independent fields here, and the whole
`SpechtDominanceCore` reduction (Layer 1, the Szpilrajn-for-Fintypes lever, the
row-pattern bridge) — is `[propext, Classical.choice, Quot.sound]`.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (standard basis, Thm 2.5.2;
  the dominance order on tabloids, `e_T = ±{T} + (lower terms)`, `{T}` maximal
  with unit coefficient, `T ↦ {T}` injective on SYT). The leading-tabloid
  injectivity argument (`leadTab_injective`) is the "within a row, the entries
  are the strictly-increasing enumeration of the row's label set" fact.
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* §8.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtTriangularCore

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## 1. The key lemma: `C_t ∩ R_t = {1}` (sorry-free)

A permutation lying in *both* the column stabilizer and the row stabilizer of a
(bijective) tableau `t` fixes both coordinate-projections of every cell, hence
fixes every cell, hence — `t` being an `Equiv` — is the identity. This is the
one fact that makes the diagonal coefficient `±1`: only `π = 1` contributes both
a nonzero `sign` and the leading tabloid `{t}`. -/

/-- **`C_t ∩ R_t = {1}`.** If `π : Perm (Fin (nOf μ))` stabilizes both the
column pattern and the row pattern of a bijective tableau `t`, then `π = 1`. -/
theorem colStab_inf_rowStab_eq_one (t : Specht.Tableau μ)
    {π : Equiv.Perm (Fin (nOf μ))} (hc : π ∈ Specht.colStab t)
    (hr : π ∈ Specht.rowStab t) : π = 1 := by
  -- From membership: the patterns are pointwise fixed by `π.symm`.
  have hrow : ∀ l, Specht.rowPattern t (π.symm l) = Specht.rowPattern t l := by
    have := (Specht.mem_rowStab).1 hr
    intro l
    have := congrFun this l
    simpa [Specht.arrow_smul_apply] using this
  have hcol : ∀ l, Specht.colPattern t (π.symm l) = Specht.colPattern t l := by
    have := (Specht.mem_colStab).1 hc
    intro l
    have := congrFun this l
    simpa [Specht.arrow_smul_apply] using this
  -- Equal coordinates ⇒ equal cell (cells are subtypes of ℕ × ℕ).
  have hcell : ∀ l, t (π.symm l) = t l := by
    intro l
    have h1 : (t (π.symm l) : ℕ × ℕ).1 = (t l : ℕ × ℕ).1 := hrow l
    have h2 : (t (π.symm l) : ℕ × ℕ).2 = (t l : ℕ × ℕ).2 := hcol l
    apply Subtype.ext
    exact Prod.ext h1 h2
  -- `t` is injective (it is an `Equiv`), so `π.symm l = l` for all `l`.
  have hfix : ∀ l, π.symm l = l := fun l => t.injective (hcell l)
  -- Hence `π.symm = 1`, so `π = 1`.
  have : π.symm = 1 := Equiv.ext hfix
  simpa using congrArg Equiv.symm this

/-! ## 2. FACT 1 — the diagonal coefficient is `1` (sorry-free) -/

omit [CharZero k] in
/-- **The diagonal coefficient is `1`.** The coefficient of the leading tabloid
`{T}` in the standard polytabloid `e_T` is `1`:
`(standardPolytabloid T)(leadTab T) = 1`. The sum over `C_t` collapses to its
identity term by `colStab_inf_rowStab_eq_one`: a column permutation contributes
to the `{t}`-coefficient iff `{π • t} = {t}` iff `π ∈ R_t`, which together with
`π ∈ C_t` forces `π = 1`, whose sign is `+1`. -/
theorem standardPolytabloid_diag_coeff (T : StandardYoungTableau μ) :
    (standardPolytabloid (k := k) T) (leadTab T) = 1 := by
  classical
  set t : Specht.Tableau μ := sytToTableau T with ht
  -- Unfold to the polytabloid and the leading tabloid.
  show (Specht.polytabloid (k := k) t) (Specht.Tabloid.mk t) = 1
  rw [Specht.polytabloid]
  -- Push Finsupp evaluation through the sum.
  rw [Finsupp.finset_sum_apply]
  -- Identify each term.
  have hterm : ∀ π : Specht.colStab t,
      ((Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
        Specht.Mtab.of (k := k) ((π : Equiv.Perm (Fin (nOf μ))) • t))
          (Specht.Tabloid.mk t)
        = (Equiv.Perm.sign (π : Equiv.Perm (Fin (nOf μ))) : ℤ) •
            (if (π : Equiv.Perm (Fin (nOf μ))) ∈ Specht.rowStab t then (1 : k) else 0) := by
    intro π
    rw [Finsupp.smul_apply]
    congr 1
    rw [Specht.Mtab.of, Finsupp.single_apply]
    -- `Tabloid.mk (π • t) = Tabloid.mk t ↔ π ∈ rowStab t`
    have hmk : (Specht.Tabloid.mk ((π : Equiv.Perm (Fin (nOf μ))) • t)
                  = Specht.Tabloid.mk t)
                ↔ (π : Equiv.Perm (Fin (nOf μ))) ∈ Specht.rowStab t := by
      rw [Specht.Tabloid.mk, Specht.Tabloid.mk, Quotient.eq]
      rw [Specht.rowEquiv_iff, Specht.rowPattern_smul, Specht.mem_rowStab]
    by_cases h : (π : Equiv.Perm (Fin (nOf μ))) ∈ Specht.rowStab t
    · rw [if_pos (hmk.2 h), if_pos h]
    · rw [if_neg (fun heq => h (hmk.1 heq)), if_neg h]
  simp_rw [hterm]
  -- Collapse to the identity term.
  rw [Finset.sum_eq_single (⟨1, Subgroup.one_mem _⟩ : Specht.colStab t)]
  · -- identity term: sign 1 = 1, in rowStab, value 1
    have h1r : (1 : Equiv.Perm (Fin (nOf μ))) ∈ Specht.rowStab t := Subgroup.one_mem _
    simp only [if_pos h1r]
    rw [Equiv.Perm.sign_one]
    norm_num
  · -- other terms vanish
    intro π _ hπne
    by_cases h : (π : Equiv.Perm (Fin (nOf μ))) ∈ Specht.rowStab t
    · -- π ∈ C_t (it's in the index set) and π ∈ R_t ⇒ π = 1, contradiction
      exfalso
      apply hπne
      have hπc : (π : Equiv.Perm (Fin (nOf μ))) ∈ Specht.colStab t := π.2
      have : (π : Equiv.Perm (Fin (nOf μ))) = 1 := colStab_inf_rowStab_eq_one t hπc h
      exact Subtype.ext this
    · rw [if_neg h, smul_zero]
  · -- identity element is in the index Finset
    intro h
    exact absurd (Finset.mem_univ _) h

omit [CharZero k] in
/-- The `diag_unit` field: `(standardPolytabloid T)(leadTab T)` is a unit. -/
theorem standardPolytabloid_diag_unit (T : StandardYoungTableau μ) :
    IsUnit ((standardPolytabloid (k := k) T) (leadTab T)) := by
  rw [standardPolytabloid_diag_coeff]
  exact isUnit_one

/-! ## 3. FACT 2 — `leadTab` injective (fully sorry-free)

`leadTab T = {sytToTableau T}` and tabloid equality is row-pattern equality, so
`leadTab T₁ = leadTab T₂` decodes to: *for every label `l`, the `T₁`-cell with
entry `l` and the `T₂`-cell with entry `l` lie in the same row.* The conclusion
`T₁ = T₂` then follows because within a row the entries appear in strictly
increasing column order (`row_strict`), so within row `i` the entry function is
the **unique strict-monotone enumeration** of the row's value-set — and since the
row's value-set is the same for both tableaux (the decoded hypothesis), the two
enumerations coincide (`Finset.orderEmbOfFin_unique`). This whole argument is
formalised here, so `leadTab_injective` carries **no** `sorry`. -/

/-- The cell that `sytToTableau T` assigns to a label carries `T`-entry equal to
that label: `T.entry (sytToTableau T l).1.1 (sytToTableau T l).1.2 = l`. This
inverts `cellLabel` (sorry-free). -/
theorem entry_sytToTableau (T : StandardYoungTableau μ) (l : Fin (nOf μ)) :
    T.entry ((sytToTableau T l : ℕ × ℕ).1) ((sytToTableau T l : ℕ × ℕ).2)
      = (l : ℕ) := by
  -- `cellLabel T (sytToTableau T l) = l` by `Equiv.apply_symm_apply` on `ofBijective`.
  have h : cellLabel T (sytToTableau T l) = l := by
    rw [sytToTableau]
    exact Equiv.apply_symm_apply (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)) l
  have := congrArg (Fin.val) h
  simpa [cellLabel] using this

/-- The cell with `T`-entry `cellLabel T c` is `c` itself: `sytToTableau` inverts
`cellLabel` (sorry-free). -/
theorem sytToTableau_cellLabel (T : StandardYoungTableau μ) (c : μ.cells) :
    sytToTableau T (cellLabel T c) = c := by
  rw [sytToTableau]
  exact Equiv.symm_apply_apply (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)) c

/-- The cell `sytToTableau T l` is a genuine cell of `μ` (sorry-free). -/
theorem sytToTableau_mem (T : StandardYoungTableau μ) (l : Fin (nOf μ)) :
    ((sytToTableau T l : ℕ × ℕ).1, (sytToTableau T l : ℕ × ℕ).2) ∈ μ :=
  (YoungDiagram.mem_cells _).1 (sytToTableau T l).2

/-- `leadTab T₁ = leadTab T₂` decodes to equality of row patterns of the
underlying fillings (sorry-free). -/
theorem leadTab_eq_iff (T₁ T₂ : StandardYoungTableau μ) :
    leadTab (μ := μ) T₁ = leadTab (μ := μ) T₂
      ↔ Specht.rowPattern (sytToTableau T₁) = Specht.rowPattern (sytToTableau T₂) := by
  rw [leadTab, leadTab, Specht.Tabloid.mk, Specht.Tabloid.mk, Quotient.eq, Specht.rowEquiv_iff]

/-- **Row-monotonicity upgrade.** The consecutive-step `row_strict` upgrades to a
strict-monotonicity statement on a whole row: for cells `(i,j),(i,j') ∈ μ` with
`j < j'`, `T.entry i j < T.entry i j'`. Induction on the gap (cells in a row are
downward-closed in the column index, `YoungDiagram.mem_iff_lt_rowLen`). -/
theorem entry_row_strictMonoOn (T : StandardYoungTableau μ) (i : ℕ) :
    ∀ j j', (i, j) ∈ μ → (i, j') ∈ μ → j < j' → T.entry i j < T.entry i j' := by
  intro j j' hj hj' hlt
  obtain ⟨d, rfl⟩ : ∃ d, j' = j + d + 1 := ⟨j' - j - 1, by omega⟩
  clear hlt
  induction d with
  | zero =>
    have hj1 : (i, j + 1) ∈ μ := by
      rw [YoungDiagram.mem_iff_lt_rowLen] at hj' ⊢; omega
    have := T.row_strict i j hj1
    have he : j + 0 + 1 = j + 1 := by omega
    rw [he]; exact this
  | succ e ih =>
    have hmem_mid : (i, j + e + 1) ∈ μ := by
      rw [YoungDiagram.mem_iff_lt_rowLen] at hj' ⊢; omega
    have hmem_top : (i, (j + e + 1) + 1) ∈ μ := by
      rw [YoungDiagram.mem_iff_lt_rowLen] at hj' ⊢; omega
    have step : T.entry i (j + e + 1) < T.entry i ((j + e + 1) + 1) :=
      T.row_strict i (j + e + 1) hmem_top
    have prev : T.entry i j < T.entry i (j + e + 1) := ih hmem_mid
    have he : j + (e + 1) + 1 = (j + e + 1) + 1 := by omega
    rw [he]; omega

/-- The **per-row value set** of `T` at row `i`: `{T.entry i j : j < rowLen i}`. -/
noncomputable def rowSet (T : StandardYoungTableau μ) (i : ℕ) : Finset ℕ :=
  (Finset.range (μ.rowLen i)).image (fun j => T.entry i j)

/-- The row-indexed entry map `Fin (rowLen i) → ℕ`, `j ↦ T.entry i j`, is strictly
monotone (sorry-free, from `entry_row_strictMonoOn`). -/
theorem entry_fin_strictMono (T : StandardYoungTableau μ) (i : ℕ) :
    StrictMono (fun j : Fin (μ.rowLen i) => T.entry i (j : ℕ)) := by
  intro a b hab
  apply entry_row_strictMonoOn T i
  · rw [YoungDiagram.mem_iff_lt_rowLen]; exact a.2
  · rw [YoungDiagram.mem_iff_lt_rowLen]; exact b.2
  · exact hab

/-- **Value↔row bridge.** A value `v` lies in `rowSet T i` iff `v` is a valid
label whose cell (under `sytToTableau T`) sits in row `i`. This connects the
entry-indexed `rowSet` to the label-indexed `rowPattern` (sorry-free). -/
theorem mem_rowSet_iff (T : StandardYoungTableau μ) (i v : ℕ) :
    v ∈ rowSet T i ↔ ∃ hv : v < nOf μ, (sytToTableau T ⟨v, hv⟩ : ℕ × ℕ).1 = i := by
  constructor
  · intro hmem
    rw [rowSet, Finset.mem_image] at hmem
    obtain ⟨j, hj, hval⟩ := hmem
    rw [Finset.mem_range] at hj
    have hcell : (i, j) ∈ μ := by rw [YoungDiagram.mem_iff_lt_rowLen]; exact hj
    have hvlt : v < nOf μ := by rw [← hval]; exact T.lt_card i j hcell
    refine ⟨hvlt, ?_⟩
    have hc : (i, j) ∈ μ.cells := (YoungDiagram.mem_cells _).2 hcell
    have hlabel : cellLabel T ⟨(i, j), hc⟩ = ⟨v, hvlt⟩ := by
      apply Fin.ext; simp only [cellLabel]; exact hval
    have := sytToTableau_cellLabel T ⟨(i, j), hc⟩
    rw [hlabel] at this
    rw [this]
  · rintro ⟨hv, hrow⟩
    set c := sytToTableau T ⟨v, hv⟩ with hc
    have hentry : T.entry ((c : ℕ × ℕ).1) ((c : ℕ × ℕ).2) = v := by
      have := entry_sytToTableau T ⟨v, hv⟩; simpa using this
    have hmem : ((c : ℕ × ℕ).1, (c : ℕ × ℕ).2) ∈ μ :=
      (YoungDiagram.mem_cells _).1 c.2
    rw [hrow] at hmem hentry
    rw [YoungDiagram.mem_iff_lt_rowLen] at hmem
    rw [rowSet, Finset.mem_image]
    exact ⟨(c : ℕ × ℕ).2, Finset.mem_range.2 hmem, hentry⟩

/-- Equal row patterns ⇒ equal per-row value sets (sorry-free): the bridge
`mem_rowSet_iff` plus pointwise equality of `rowPattern`. -/
theorem rowSet_eq_of_rowPattern_eq (T₁ T₂ : StandardYoungTableau μ)
    (hrow : Specht.rowPattern (sytToTableau T₁) = Specht.rowPattern (sytToTableau T₂))
    (i : ℕ) : rowSet T₁ i = rowSet T₂ i := by
  ext v
  rw [mem_rowSet_iff, mem_rowSet_iff]
  constructor
  · rintro ⟨hv, h1⟩
    refine ⟨hv, ?_⟩
    have := congrFun hrow ⟨v, hv⟩
    rw [Specht.rowPattern, Specht.rowPattern] at this
    rw [← this]; exact h1
  · rintro ⟨hv, h2⟩
    refine ⟨hv, ?_⟩
    have := congrFun hrow ⟨v, hv⟩
    rw [Specht.rowPattern, Specht.rowPattern] at this
    rw [this]; exact h2

/-- `#(rowSet T i) = rowLen i` (sorry-free): the entry map is injective on the
row's column range (strict-mono), so the image has full cardinality. -/
theorem rowSet_card (T : StandardYoungTableau μ) (i : ℕ) :
    (rowSet T i).card = μ.rowLen i := by
  rw [rowSet, Finset.card_image_of_injOn, Finset.card_range]
  intro a ha b hb hab
  rw [Finset.mem_coe, Finset.mem_range] at ha hb
  by_contra hne
  rcases Nat.lt_or_ge a b with hlt | hge
  · exact absurd hab (ne_of_lt (entry_row_strictMonoOn T i a b
      (by rw [YoungDiagram.mem_iff_lt_rowLen]; exact ha)
      (by rw [YoungDiagram.mem_iff_lt_rowLen]; exact hb) hlt))
  · have hlt' : b < a := by omega
    exact absurd hab.symm (ne_of_lt (entry_row_strictMonoOn T i b a
      (by rw [YoungDiagram.mem_iff_lt_rowLen]; exact hb)
      (by rw [YoungDiagram.mem_iff_lt_rowLen]; exact ha) hlt'))

/-- The entry function on row `i` **is** the unique order-embedding of `rowSet T i`
into `ℕ` (sorry-free): it is strict-mono into `rowSet`, so by
`Finset.orderEmbOfFin_unique` it equals `(rowSet T i).orderEmbOfFin`. -/
theorem entry_eq_orderEmbOfFin (T : StandardYoungTableau μ) (i : ℕ) :
    (fun j : Fin (μ.rowLen i) => T.entry i (j : ℕ))
      = (rowSet T i).orderEmbOfFin (rowSet_card T i) := by
  apply Finset.orderEmbOfFin_unique
  · intro j
    rw [rowSet, Finset.mem_image]
    exact ⟨(j : ℕ), Finset.mem_range.2 j.2, rfl⟩
  · exact entry_fin_strictMono T i

/-- **Leading tabloid ⇒ SYT determined (fully proved, sorry-free).** Two standard
Young tableaux whose underlying fillings have the *same row pattern* (each label
occupies the same row in both) are equal. Off-diagram entries agree by
`zero_off`; on-diagram, within each row both entry functions are the unique
strict-monotone enumeration (`entry_eq_orderEmbOfFin`) of the row's value set,
and those value sets agree (`rowSet_eq_of_rowPattern_eq`), so the entries agree. -/
theorem leadTab_injective_core (T₁ T₂ : StandardYoungTableau μ)
    (hrow : Specht.rowPattern (sytToTableau T₁) = Specht.rowPattern (sytToTableau T₂)) :
    T₁ = T₂ := by
  ext i j
  by_cases hij : (i, j) ∈ μ
  · have hjlt : j < μ.rowLen i := by rw [← YoungDiagram.mem_iff_lt_rowLen]; exact hij
    have hset : rowSet T₁ i = rowSet T₂ i := rowSet_eq_of_rowPattern_eq T₁ T₂ hrow i
    have h1 := entry_eq_orderEmbOfFin T₁ i
    have h2 := entry_eq_orderEmbOfFin T₂ i
    have e1 : T₁.entry i j = (rowSet T₁ i).orderEmbOfFin (rowSet_card T₁ i) ⟨j, hjlt⟩ := by
      have := congrFun h1 ⟨j, hjlt⟩; simpa using this
    have e2 : T₂.entry i j = (rowSet T₂ i).orderEmbOfFin (rowSet_card T₂ i) ⟨j, hjlt⟩ := by
      have := congrFun h2 ⟨j, hjlt⟩; simpa using this
    rw [e1, e2]
    clear h1 h2 e1 e2
    -- generalize the card proofs so the finset equality can be rewritten
    generalize hc1 : rowSet_card T₁ i = pc1
    generalize hc2 : rowSet_card T₂ i = pc2
    clear hc1 hc2
    revert pc1 pc2
    rw [hset]
    intro pc1 pc2
    rfl
  · rw [T₁.zero_off i j hij, T₂.zero_off i j hij]

omit [CharZero k] in
/-- The `lead_inj` field: `leadTab` is injective on standard Young tableaux —
**fully sorry-free** (the row-pattern decoding `leadTab_eq_iff` plus the
leading-tabloid-determines-SYT core `leadTab_injective_core`). -/
theorem leadTab_injective : Function.Injective (leadTab (μ := μ)) := by
  intro T₁ T₂ h
  exact leadTab_injective_core T₁ T₂ ((leadTab_eq_iff T₁ T₂).1 h)

/-! ## 4. The genuine dominance core (one cited `sorry`) -/

omit [CharZero k] in
/-- **The dominance core, discharged by reduction.** Proved **sorry-free modulo**
the deeper relation-level core `SpechtDominanceCore.dominance_relation_exists`: the
`SpechtDominanceCore` reduction peels off the `LinearOrder` construction (a
Szpilrajn-for-Fintypes lever) and the `Finsupp`/`support` plumbing, leaving only
Sagan's dominance lemma (`DominanceData`: a partial order on tabloids under which
column permutations weakly decrease, plus antisymmetry). This consumes its verbatim
restatement `standardPolytabloid_dominance_order'`. -/
theorem standardPolytabloid_dominance_order :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      ∀ T : StandardYoungTableau μ, ∀ a ∈ (standardPolytabloid (k := k) T).support,
        a ≤ leadTab T :=
  SpechtDominanceCore.standardPolytabloid_dominance_order' (k := k) (μ := μ)

/-! ## 5. The reassembled `Triangular` bundle (sorry-free modulo the single core) -/

omit [CharZero k] in
/-- **Reassembled brick-4 bundle.** A verbatim restatement of
`SpechtStandardBasis.standardPolytabloid_triangular`, proved sorry-free modulo
**the single** isolated dominance core `standardPolytabloid_dominance_order`
(the order + `supp_le` field). The other two fields are fully sorry-free here:
`diag_unit` (`standardPolytabloid_diag_unit`) and `lead_inj`
(`leadTab_injective`, whose leading-tabloid-determines-SYT core
`leadTab_injective_core` is fully proved above). -/
theorem standardPolytabloid_triangular' :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      Triangular (standardPolytabloid (k := k) (μ := μ)) (leadTab (μ := μ)) := by
  obtain ⟨ord, hsupp⟩ := standardPolytabloid_dominance_order (k := k) (μ := μ)
  exact ⟨ord, { lead_inj := leadTab_injective
                diag_unit := standardPolytabloid_diag_unit
                supp_le := hsupp }⟩

omit [CharZero k] in
/-- Zero-subtracted difference between the cardinality of `rowSet T i` and `μ.rowLen i` vanishes. -/
theorem rowSet_card_sub_rowLen_eq_zero (T : StandardYoungTableau μ) (i : ℕ) :
    (rowSet T i).card - μ.rowLen i = 0 := by
  rw [rowSet_card T i]
  exact Nat.sub_self (μ.rowLen i)

end QOU.BraidKnot.SpechtTriangularCore
