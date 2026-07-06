import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Finsupp.VectorSpace
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.OfMap
import Mathlib.Data.Finset.Max
import Mathlib.GroupTheory.GroupAction.FixingSubgroup
import Mathlib.GroupTheory.Complement
import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.Specht
import Mathlib.Tactic.Group

/-!
# QOU.BraidKnot.SpechtStandardBasisCore — brick-4 definitions + the order-agnostic core

**Definitions-and-lower-machinery half** of brick 4's standard-basis theorem for
Specht modules (`dim_k S^μ = #SYT(μ)`, Sagan, *The Symmetric Group*, Thm 2.5.2).

This module holds **all the brick-4 objects and every lemma that does not itself
depend on the dominance/triangular core** — the SYT→tableau conversion, the
standard polytabloids, the abstract `Triangular` lever, the corestriction
reduction, and the spanning half (with its single honest straightening stub).

It sits **below** the two independence cores (`SpechtDominanceCore`,
`SpechtTriangularCore`), which import it read-only. The triangular-dependent
capstone declarations (`standardPolytabloid_triangular` — now **proved** by
consuming `SpechtTriangularCore.standardPolytabloid_triangular'` — plus
`standardPolytabloid_linearIndependent`, `standardBasis`,
`specht_finrank_eq_numSYT`) live **above** those cores, in
`QOU.BraidKnot.SpechtStandardBasis`.

Everything here is declared in the `QOU.BraidKnot.SpechtStandardBasis`
namespace (unchanged), so downstream references (`SpechtStandardBasis.sytToTableau`,
`.cellLabel`, `.standardPolytabloid`, `.leadTab`, `.Triangular`,
`.linearIndependent_corestrict_iff`, `.standardPolytabloid_span`, …) resolve exactly
as before — `SpechtStandardBasis` re-exports this file by importing it.

So the opaque dimension identity `dim = numSYT` becomes a clean map:
*"it is a basis question — linear independence + spanning, both classically
cited, everything else machine-checked."*

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `cellLabel`, `cellLabel_injective` | **sorry-free** (injectivity of `T.entry` via `inj_on`) |
| `instFintypeStandardYoungTableau` | **sorry-free** (`Fintype` of an SYT via `Fintype.ofInjective`) |
| `sytToTableau` | **sorry-free** (the bijective filling `Fin n ≃ μ.cells`) |
| `standardPolytabloid` | **sorry-free** (definition) |
| `standardPolytabloid_mem` | **sorry-free** (lands in `S^μ`) |
| `standardPolytabloidS` (corestriction) | **sorry-free** |
| `standardPolytabloid_linearIndependent` | **STUB** `sorry` — `-- Ref: [sagan2001]` Thm 2.5.2 |
| `colStab_smul_self`, `polytabloid_colStab_smul` (column-antisymmetry) | **sorry-free** |
| `domCount'`, `domWeight`, `domBound`, `domCount'_le`, `domWeight_le` (the dominance measure) | **sorry-free** |
| `straightening_step_colMax` (Garnir core, **column-maximal case**) | **STUB** `sorry` — `-- Ref: [sagan2001]` §2.6 |
| `straightening_step` (Garnir straightening core) | **sorry-free MODULO `straightening_step_colMax`** (column-sort dichotomy: the `domWeight`-raising branch is proved outright via `polytabloid_colStab_smul`) |
| `standardPolytabloid_straightening` | **sorry-free MODULO `straightening_step_colMax`** (well-founded induction on the dominance weight) |
| `standardPolytabloid_span` | **sorry-free MODULO `straightening_step_colMax`** (Garnir relations) |
| `standardBasis` | **sorry-free MODULO the two stubs** (`Basis.mk` wiring) |
| `specht_finrank_eq_numSYT` | **sorry-free MODULO the two stubs** (the reduction) |

The reduction (`standardBasis` + `specht_finrank_eq_numSYT`) is **genuinely
sorry-free**: its only `sorry`-tainted inputs are the two named classical facts
(`standardPolytabloid_linearIndependent`, and — via
`standardPolytabloid_straightening` and `straightening_step` — the single Garnir
core `straightening_step_colMax`). The
SYT→tableau conversion **and** the `Fintype` instance brick 1 left open are
*both* proved sorry-free here.

**Spanning half — reduction (this file, §3b).** The former single spanning stub
`standardPolytabloid_straightening` (every polytabloid `e_t` lies in the span of
the *standard* polytabloids) is now **proved sorry-free by well-founded induction**
on a self-contained dominance weight (`domWeight`, a strictly-monotone ℕ-valued
linear extension of Sagan's dominance order, defined locally because this file sits
*below* `SpechtDominanceCore` in the import graph), reducing the whole spanning
half to a **single** sharper combinatorial core, `straightening_step`: a
*non-standard* polytabloid is a `k`-combination of polytabloids of strictly
dominance-greater (`domWeight`-greater) tabloids (Sagan §2.6 Garnir relations).

That core is itself now **proved sorry-free MODULO a still-sharper residual**,
`straightening_step_colMax`, via a **column-sort dichotomy** on whether some column
permutation `σ ∈ C_t` strictly raises `domWeight`. The `domWeight`-raising branch is
discharged outright by the column-antisymmetry lemma `polytabloid_colStab_smul`
(`e_{σ·t} = sgn(σ)·e_t` for `σ ∈ C_t`, proved sorry-free here): since `sgn(σ)² = 1`,
`e_t = sgn(σ)·e_{σ·t}`, a one-term combination whose single term is strictly
`domWeight`-greater by the branch hypothesis. What remains is only the
**column-maximal** branch (no `σ ∈ C_t` raises `domWeight`, so the column-sort is
exhausted): the genuine Garnir coset-sum at a row descent, isolated as the residual
`straightening_step_colMax` with the sharpening hypothesis that `t` is
column-dominance-maximal.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (the standard basis, Thm 2.5.2;
  independence via the dominance/last-letter order, spanning via Garnir
  relations).
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups* (Specht modules, the standard basis theorem).
- [fulton1997] Fulton, *Young Tableaux* (tableaux / tabloids, standard fillings).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtStandardBasis

open QOU.BraidKnot
open QOU.BraidKnot.Specht

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## 1. SYT → general tableau conversion (sorry-free)

A standard Young tableau `T` assigns to each cell `(i, j) ∈ μ` a label
`T.entry i j < μ.card`, *injectively* (`T.inj_on`). Reading this off as a map
`μ.cells → Fin (μ.card)` gives an injection between two finite types of equal
cardinality (`Fintype.card μ.cells = μ.cells.card = μ.card`), hence a bijection.
Inverting it yields the general (bijective) tableau `Fin (nOf μ) ≃ μ.cells` that
brick 2 consumes. -/

/-- The label that a standard tableau `T` assigns to a cell, as an element of
`Fin (μ.card) = Fin (nOf μ)`. The bound is exactly `T.lt_card`. -/
def cellLabel (T : StandardYoungTableau μ) : μ.cells → Fin (nOf μ) :=
  fun c => ⟨T.entry c.1.1 c.1.2, T.lt_card c.1.1 c.1.2 ((YoungDiagram.mem_cells _).1 c.2)⟩

/-- `cellLabel T` is injective: distinct cells carry distinct labels (`T.inj_on`). -/
theorem cellLabel_injective (T : StandardYoungTableau μ) :
    Function.Injective (cellLabel T) := by
  rintro ⟨⟨i, j⟩, hc⟩ ⟨⟨i', j'⟩, hc'⟩ h
  have hmem : (i, j) ∈ μ := (YoungDiagram.mem_cells _).1 hc
  have hmem' : (i', j') ∈ μ := (YoungDiagram.mem_cells _).1 hc'
  have hval : T.entry i j = T.entry i' j' := by
    simpa [cellLabel, Fin.ext_iff] using h
  obtain ⟨hi, hj⟩ := T.inj_on i j i' j' hmem hmem' hval
  subst hi; subst hj; rfl

/-- **`Fintype (StandardYoungTableau μ)`** — the instance brick 1 left open.

An SYT is determined by its values on `μ.cells` (off-cell entries are pinned to
`0` by `zero_off`, and the bounds/strictness fields are `Prop`s). The map
`T ↦ (the restricted entry function on cells)` into the *finite* function space
`μ.cells → Fin (μ.card)` is injective, so `Fintype.ofInjective` supplies the
instance. (Two SYTs agreeing on every cell are equal: on-cells by the agreement,
off-cells by `zero_off` — discharged via the `@[ext]` lemma.)

This is a **bonus**: the headline `specht_finrank_eq_numSYT` uses
`Module.finrank_eq_nat_card_basis` (which needs no `Fintype` on the index), so
it does not depend on this instance. Provided here to close brick 1's open
instance sorry-free. -/
noncomputable instance instFintypeStandardYoungTableau :
    Fintype (StandardYoungTableau μ) :=
  Fintype.ofInjective (β := μ.cells → Fin (nOf μ)) cellLabel <| by
    intro T T' h
    ext i j
    by_cases hij : (i, j) ∈ μ
    · -- on a cell: the labels agree, so the entries agree
      have hc : (i, j) ∈ μ.cells := (YoungDiagram.mem_cells _).2 hij
      have := congrFun h ⟨(i, j), hc⟩
      simpa [cellLabel, Fin.ext_iff] using this
    · -- off a cell: both pinned to 0 by `zero_off`
      rw [T.zero_off i j hij, T'.zero_off i j hij]

/-- `cellLabel T` is bijective: an injection between two finite types of equal
cardinality (`card μ.cells = μ.cells.card = μ.card = nOf μ`). -/
theorem cellLabel_bijective (T : StandardYoungTableau μ) :
    Function.Bijective (cellLabel T) := by
  rw [Fintype.bijective_iff_injective_and_card]
  refine ⟨cellLabel_injective T, ?_⟩
  rw [Fintype.card_coe, Fintype.card_fin]

/-- **SYT → general tableau** (sorry-free). The bijective filling
`Fin (nOf μ) ≃ μ.cells` reading off `T.entry`: label `l ↦` the unique cell whose
entry is `l`. Built by inverting the bijection `cellLabel T : μ.cells ≃ Fin n`. -/
noncomputable def sytToTableau (T : StandardYoungTableau μ) : Specht.Tableau μ :=
  (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)).symm

/-! ## 2. Standard polytabloids (sorry-free definitions) -/

/-- The **standard polytabloid** `e_T = e_{sytToTableau T} ∈ M^μ` of a standard
Young tableau `T`. These are the candidate basis vectors of `S^μ`. -/
noncomputable def standardPolytabloid (T : StandardYoungTableau μ) :
    Specht.Mtab (k := k) μ :=
  Specht.polytabloid (k := k) (sytToTableau T)

omit [CharZero k] in
/-- Every standard polytabloid lies in the Specht module (it is a polytabloid). -/
theorem standardPolytabloid_mem (T : StandardYoungTableau μ) :
    standardPolytabloid (k := k) T ∈ Specht.SpechtSubmodule (k := k) μ :=
  Specht.polytabloid_mem_specht (k := k) (sytToTableau T)

/-- The standard polytabloid **corestricted** to `S^μ` (i.e. valued in the
submodule `Specht.SpechtSubmodule μ`), using `standardPolytabloid_mem`. This is
the family `Basis.mk` builds a basis from. -/
noncomputable def standardPolytabloidS (T : StandardYoungTableau μ) :
    Specht.SpechtSubmodule (k := k) μ :=
  ⟨standardPolytabloid (k := k) T, standardPolytabloid_mem (k := k) T⟩

/-! ### 2a. Row/column-descent existence (SYT recognition, sorry-free)

The first layer of the Garnir core `straightening_step_colMax`: a polytabloid that is
*not* a standard polytabloid comes from a tableau with a **descent** — either a row
descent (a right-neighbour label `≤` its left) or a column descent (a lower-neighbour
label `≤` its upper). Proved via the SYT-recognition bridge: a filling strict along
rows and down columns *is* the `sytToTableau` image of an honest `StandardYoungTableau`,
so a non-standard polytabloid must fail strictness somewhere. `hmax` later kills the
column disjunct (a column descent would give a `domWeight`-raising `colStab` swap),
leaving a pure row descent to feed the Garnir coset-sum.

Ref: [sagan2001] §2.5-2.6; [james1984representation] §8 (standard tableaux). -/

/-- The label a `Tableau μ = Fin n ≃ μ.cells` assigns to a cell `(i, j) ∈ μ` — the
"entry at a cell" view, dual to `rowPattern`/`colPattern` (which report the row/column
of a *label*): `labelAt t h = (t.symm ⟨(i,j),…⟩).val`. -/
def labelAt (t : Specht.Tableau μ) {i j : ℕ} (h : (i, j) ∈ μ) : ℕ :=
  (t.symm ⟨(i, j), (YoungDiagram.mem_cells (i, j)).2 h⟩ : Fin (Specht.nOf μ)).val

/-- A `Tableau` filling that is strictly increasing along rows and down columns is an
honest `StandardYoungTableau`. -/
noncomputable def sytOfStrict (t : Specht.Tableau μ)
    (hrow : ∀ i j (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij < labelAt t hij1)
    (hcol : ∀ i j (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ), labelAt t hij < labelAt t hi1j) :
    StandardYoungTableau μ where
  entry := fun i j => if h : (i, j) ∈ μ then labelAt t h else 0
  lt_card := fun i j h => by rw [dif_pos h]; exact (t.symm _).isLt
  zero_off := fun i j h => by simp only [dif_neg h]
  inj_on := fun i j i' j' hij hij' he => by
    rw [dif_pos hij, dif_pos hij'] at he
    simp only [labelAt] at he
    exact Prod.ext_iff.mp (Subtype.ext_iff.mp (t.symm.injective (Fin.val_injective he)))
  row_strict := fun i j hj1 => by
    have hij : (i, j) ∈ μ := μ.up_left_mem (le_refl i) (Nat.le_succ j) hj1
    rw [dif_pos hij, dif_pos hj1]; exact hrow i j hij hj1
  col_strict := fun i j hi1 => by
    have hij : (i, j) ∈ μ := μ.up_left_mem (Nat.le_succ i) (le_refl j) hi1
    rw [dif_pos hij, dif_pos hi1]; exact hcol i j hij hi1

/-- `sytToTableau` inverts `sytOfStrict`: the honest SYT built from a strict filling
maps back to the original tableau. -/
theorem sytToTableau_sytOfStrict (t : Specht.Tableau μ)
    (hrow : ∀ i j (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij < labelAt t hij1)
    (hcol : ∀ i j (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ), labelAt t hij < labelAt t hi1j) :
    sytToTableau (sytOfStrict t hrow hcol) = t := by
  set T := sytOfStrict t hrow hcol with hT
  have key : cellLabel T = t.symm := by
    funext c
    apply Fin.ext
    show T.entry c.1.1 c.1.2 = (t.symm c).val
    have hc : (c.1.1, c.1.2) ∈ μ := (YoungDiagram.mem_cells _).1 c.2
    have hcell : (⟨(c.1.1, c.1.2), (YoungDiagram.mem_cells _).2 hc⟩ : μ.cells) = c :=
      Subtype.ext rfl
    show (if h : (c.1.1, c.1.2) ∈ μ then labelAt t h else 0) = (t.symm c).val
    rw [dif_pos hc]
    simp only [labelAt, hcell]
  unfold sytToTableau
  rw [show (Equiv.ofBijective (cellLabel T) (cellLabel_bijective T)) = t.symm from
        Equiv.ext (fun c => by rw [Equiv.ofBijective_apply, key]),
      Equiv.symm_symm]

omit [CharZero k] in
/-- **SYT recognition:** a tableau strict along rows and down columns has a standard
polytabloid. -/
theorem mem_range_standardPolytabloid_of_strict (t : Specht.Tableau μ)
    (hrow : ∀ i j (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij < labelAt t hij1)
    (hcol : ∀ i j (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ), labelAt t hij < labelAt t hi1j) :
    Specht.polytabloid (k := k) t ∈ Set.range (standardPolytabloid (k := k) (μ := μ)) := by
  refine ⟨sytOfStrict t hrow hcol, ?_⟩
  show Specht.polytabloid (k := k) (sytToTableau (sytOfStrict t hrow hcol))
      = Specht.polytabloid (k := k) t
  rw [sytToTableau_sytOfStrict t hrow hcol]

omit [CharZero k] in
/-- **Descent existence (sorry-free).** A non-standard polytabloid comes from a tableau
with a row descent (right neighbour `≤`) or a column descent (lower neighbour `≤`) —
the contrapositive of SYT recognition. This is the entry point of the column-maximal
Garnir core `straightening_step_colMax`. -/
theorem exists_descent_of_not_mem_range (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ))) :
    (∃ i j, ∃ (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij1 ≤ labelAt t hij) ∨
      (∃ i j, ∃ (hij : (i, j) ∈ μ) (hi1j : (i + 1, j) ∈ μ), labelAt t hi1j ≤ labelAt t hij) := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨hnrow, hncol⟩ := hcon
  exact h (mem_range_standardPolytabloid_of_strict (k := k) t hnrow hncol)

/-! ## 3. The two genuine content obligations

The linear-independence half (§3a) is **reduced**, sorry-free, to a single
combinatorial core (`standardPolytabloid_triangular`) via a locally-proved
triangular-independence lever; the spanning half (§3b) remains one honest stub. -/

/-! ### 3a. Linear independence — reduced to Sagan's dominance lemma

The classical independence argument is *unitriangularity in the dominance order*:
`e_T = ±{T} + (dominated terms)`, so the standard polytabloids form a triangular
family over the tabloid basis and are therefore independent. The "triangular ⇒
independent" lever is **absent from the pinned Mathlib** (its only such machinery is
Gram–Schmidt-specific, requiring an inner-product space), so we supply it locally,
sorry-free, and reduce the obligation to exactly Sagan's dominance lemma. -/

/-- The triangular hypothesis bundle (upper-bound form), over any `CommRing`:
`lead` injective, the diagonal coefficient `(v i)(lead i)` a unit, and `lead i` an
upper bound of `supp (v i)`. -/
structure Triangular {ι : Type*} {α : Type*} {R : Type*} [LinearOrder α] [CommRing R]
    (v : ι → (α →₀ R)) (lead : ι → α) : Prop where
  /-- distinct vectors have distinct leading indices -/
  lead_inj : Function.Injective lead
  /-- the diagonal coefficient is a unit -/
  diag_unit : ∀ i, IsUnit ((v i) (lead i))
  /-- `lead i` is an upper bound of `supp (v i)` -/
  supp_le : ∀ i, ∀ a ∈ (v i).support, a ≤ lead i

/-- **Triangular-independence lever** — the lemma the pinned Mathlib lacks, supplied
sorry-free. A triangular `Finsupp` family (injective leading map, unit diagonal,
support bounded above by the leading index) is linearly independent. Maximal-leading-
index argument; works over any `CommRing`. A natural Mathlib-upstream candidate. -/
theorem Triangular.linearIndependent {ι : Type*} {α : Type*} {R : Type*}
    [LinearOrder α] [CommRing R] {v : ι → (α →₀ R)} {lead : ι → α}
    (h : Triangular v lead) : LinearIndependent R v := by
  classical
  rw [linearIndependent_iff']
  intro s g hsum
  by_contra hne
  push_neg at hne
  obtain ⟨i, hiS, hgi⟩ := hne
  set T : Finset ι := s.filter (fun i => g i ≠ 0) with hT
  have hiT : i ∈ T := by rw [hT]; simp [hiS, hgi]
  obtain ⟨i₀, hi₀T, hi₀max⟩ := T.exists_max_image lead ⟨i, hiT⟩
  have hg0 : g i₀ ≠ 0 := by rw [hT] at hi₀T; exact (Finset.mem_filter.mp hi₀T).2
  have hi₀S : i₀ ∈ s := by rw [hT] at hi₀T; exact (Finset.mem_filter.mp hi₀T).1
  have hpt : (∑ j ∈ s, g j • v j) (lead i₀) = 0 := by rw [hsum]; rfl
  rw [Finsupp.finset_sum_apply] at hpt
  have hterm : ∀ j, (g j • v j) (lead i₀) = g j * (v j) (lead i₀) := by
    intro j; rw [Finsupp.smul_apply, smul_eq_mul]
  simp_rw [hterm] at hpt
  have hzero : ∀ j ∈ s, j ≠ i₀ → g j * (v j) (lead i₀) = 0 := by
    intro j hjS hji₀
    by_cases hgj : g j = 0
    · rw [hgj, zero_mul]
    · have hjT : j ∈ T := by rw [hT]; simp [hjS, hgj]
      have hlt : lead j < lead i₀ :=
        lt_of_le_of_ne (hi₀max j hjT) (fun heq => hji₀ (h.lead_inj heq))
      have : (v j) (lead i₀) = 0 :=
        Finsupp.notMem_support_iff.mp
          (fun hmem => absurd (h.supp_le j (lead i₀) hmem) (not_le.mpr hlt))
      rw [this, mul_zero]
  rw [Finset.sum_eq_single i₀ (fun j hjS hji₀ => hzero j hjS hji₀)
      (fun hi₀notS => absurd hi₀S hi₀notS)] at hpt
  refine hg0 ?_
  rcases (h.diag_unit i₀).exists_right_inv with ⟨c, hc⟩
  have hcalc := congrArg (· * c) hpt
  simp only [zero_mul] at hcalc
  rwa [mul_assoc, hc, mul_one] at hcalc

/-- The concrete **leading-tabloid map** `lead T = {sytToTableau T}` (the row-class of
`T`'s own filling) — the leading tabloid of `e_T`. Sorry-free. -/
noncomputable def leadTab (T : StandardYoungTableau μ) : Specht.Tabloid μ :=
  Specht.Tabloid.mk (sytToTableau T)

omit [CharZero k] in
/-- `(S^μ).subtype ∘ standardPolytabloidS = standardPolytabloid` (definitional). -/
theorem subtype_comp_standardPolytabloidS :
    (Specht.SpechtSubmodule (k := k) μ).subtype ∘ standardPolytabloidS (k := k) (μ := μ)
      = standardPolytabloid (k := k) (μ := μ) := by
  funext T; rfl

omit [CharZero k] in
/-- **Corestriction reflects independence**: independence of `standardPolytabloidS`
(in `S^μ`) ⟺ independence of `standardPolytabloid` (in `M^μ`), since the `S^μ`
inclusion has trivial kernel. Sorry-free. -/
theorem linearIndependent_corestrict_iff :
    LinearIndependent k (standardPolytabloidS (k := k) (μ := μ))
      ↔ LinearIndependent k (standardPolytabloid (k := k) (μ := μ)) := by
  have hker : LinearMap.ker (Specht.SpechtSubmodule (k := k) μ).subtype = ⊥ :=
    Submodule.ker_subtype _
  have key := LinearMap.linearIndependent_iff
      (Specht.SpechtSubmodule (k := k) μ).subtype hker
      (v := standardPolytabloidS (k := k) (μ := μ))
  rw [subtype_comp_standardPolytabloidS] at key
  exact key.symm

/-! ### 3b. Spanning (single honest stub)

(The triangular-dependent `standardPolytabloid_triangular` — now proved — and
`standardPolytabloid_linearIndependent` live in `SpechtStandardBasis`, above the
independence cores.) -/

/-! #### The column-antisymmetry lemma (`e_{σ·t} = sgn(σ)·e_t`, sorry-free)

The first ingredient of Sagan's §2.6 straightening algorithm: a column
permutation `σ ∈ C_t` acts on the polytabloid by its sign. This is the
"column-sort" reduction — every `e_t` equals `±e_{column-sorted t}`. -/

/-- For `σ ∈ C_t`, the column stabilizer is `σ`-invariant: `C_{σ·t} = C_t`.
(`colPattern (σ·t) = σ · colPattern t = colPattern t` since `σ ∈ C_t`.) -/
theorem colStab_smul_self (t : Specht.Tableau μ) {σ : Equiv.Perm (Fin (Specht.nOf μ))}
    (hσ : σ ∈ Specht.colStab t) : Specht.colStab (σ • t) = Specht.colStab t := by
  unfold Specht.colStab
  rw [Specht.colPattern_smul, Specht.mem_colStab.mp hσ]

omit [CharZero k] in
/-- **Column-antisymmetry (sorry-free).** A column permutation `σ ∈ C_t` acts on
the polytabloid by its sign: `e_{σ·t} = sgn(σ)·e_t`. The sum over `C_{σ·t} = C_t`
is reindexed `ρ ↦ ρσ` (right multiplication by `σ ∈ C_t`), using
`sgn(ρσ) = sgn(ρ)sgn(σ)`, `ρ·(σ·t) = (ρσ)·t`, and `sgn(σ)² = 1`. This is the
column-sort step of Sagan §2.6: every polytabloid equals `±` its
column-standardised representative. -/
theorem polytabloid_colStab_smul (t : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab t) :
    Specht.polytabloid (k := k) (σ • t)
      = (Equiv.Perm.sign σ : ℤ) • Specht.polytabloid (k := k) t := by
  classical
  have hEq : Specht.colStab (σ • t) = Specht.colStab t := colStab_smul_self t hσ
  have hs2 : (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> rw [h] <;> decide
  rw [Specht.polytabloid, Specht.polytabloid, Finset.smul_sum]
  refine Finset.sum_bij'
    (i := fun (ρ : Specht.colStab (σ • t)) _ =>
      (⟨(ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ, ?_⟩ : Specht.colStab t))
    (j := fun (π : Specht.colStab t) _ =>
      (⟨(π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹, ?_⟩ : Specht.colStab (σ • t)))
    ?_ ?_ ?_ ?_ ?_
  · exact Subgroup.mul_mem _ (hEq ▸ ρ.2) hσ
  · exact hEq.symm ▸ Subgroup.mul_mem _ π.2 (Subgroup.inv_mem _ hσ)
  · intro ρ _; exact Finset.mem_univ _
  · intro π _; exact Finset.mem_univ _
  · intro ρ _; apply Subtype.ext; simp [mul_assoc]
  · intro π _; apply Subtype.ext; simp [mul_assoc]
  · intro ρ _
    have e1 : (ρ : Equiv.Perm (Fin (Specht.nOf μ))) • (σ • t)
        = ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t := (mul_smul _ _ _).symm
    show (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
          • Specht.Mtab.of (k := k) ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) • (σ • t))
      = (Equiv.Perm.sign σ : ℤ) • ((Equiv.Perm.sign
            ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) : ℤ)
          • Specht.Mtab.of (k := k) (((ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t))
    rw [e1, ← mul_smul]
    congr 1
    rw [map_mul]
    push_cast
    have : (Equiv.Perm.sign σ : ℤ)
        * ((Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) * (Equiv.Perm.sign σ : ℤ))
      = (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ)
        * ((Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ)) := by ring
    rw [this, hs2, mul_one]

omit [CharZero k] in
/-- **Garnir annihilation — algebraic core (sorry-free).** The sign-reversing
involution at the heart of every Garnir relation. If `τ` is an involution
(`τ*τ = 1`) of sign `-1` lying in the *row* stabiliser of `t` (so `τ` fixes the
tabloid `{t}`), and `G` is a finite set of permutations closed under right
multiplication by `τ`, then the signed sum of basis tabloids
`∑_{g∈G} sgn(g)·{g·t}` vanishes: pairing `g ↔ gτ` cancels terms, because
`{gτ·t} = {g·t}` (`τ` fixes the row pattern) while `sgn(gτ) = -sgn(g)`.
This is the Mathlib-side realisation of "the full column antisymmetriser of a
Garnir set annihilates the tabloid" (Sagan §2.6). It is the algebraic ingredient
the column-maximal Garnir core (`straightening_step_colMax`, still `sorry`)
consumes; the three pieces still missing on top of it — the coset→polytabloid
antisymmetriser bridge (needs `CharZero k`), the Garnir-set/row-descent existence
for a column-maximal non-standard tableau, and the dominance strict-increase —
are recorded in the module docstring. -/
-- Ref: [sagan2001] Sagan, *The Symmetric Group*, §2.6 (Garnir relations).
theorem mtab_sum_sign_smul_of_eq_zero (t : Specht.Tableau μ)
    (G : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (τ : Equiv.Perm (Fin (Specht.nOf μ)))
    (hτ2 : τ * τ = 1) (hτsign : Equiv.Perm.sign τ = -1)
    (hτrow : τ ∈ Specht.rowStab t)
    (hGclosed : ∀ g ∈ G, g * τ ∈ G) :
    ∑ g ∈ G, (Equiv.Perm.sign g : ℤ) • Specht.Mtab.of (k := k) (g • t) = 0 := by
  classical
  -- `τ` fixes the tabloid of `t`: `{τ·t} = {t}`.
  have hrow : Specht.Tabloid.mk (τ • t) = Specht.Tabloid.mk t :=
    Quotient.sound (by
      show Specht.rowPattern (τ • t) = Specht.rowPattern t
      rw [Specht.rowPattern_smul]; exact Specht.mem_rowStab.mp hτrow)
  -- Hence `of ((g*τ)·t) = of (g·t)` for every `g`.
  have hofeq : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      Specht.Mtab.of (k := k) ((g * τ) • t) = Specht.Mtab.of (k := k) (g • t) := by
    intro g
    have hmk : Specht.Tabloid.mk ((g * τ) • t) = Specht.Tabloid.mk (g • t) := by
      rw [mul_smul, ← Specht.Tabloid.smul_mk g (τ • t), hrow, Specht.Tabloid.smul_mk]
    simp only [Specht.Mtab.of, hmk]
  -- Sign is reversed by right-multiplication with `τ`.
  have hs : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      (Equiv.Perm.sign (g * τ) : ℤ) = -(Equiv.Perm.sign g : ℤ) := by
    intro g; rw [map_mul, hτsign]; simp
  refine Finset.sum_involution (fun g _ => g * τ) ?_ ?_ ?_ ?_
  · -- paired terms cancel
    intro g _
    rw [hofeq g, hs g, neg_smul]
    abel
  · -- involution is fixed-point free (τ ≠ 1), so the `f a ≠ 0 → …` premise is free
    intro g _ _ hgg
    have hτ1 : τ = 1 := by
      have hg1 : g * τ = g * 1 := by rw [mul_one]; exact hgg
      exact mul_left_cancel hg1
    rw [hτ1, map_one] at hτsign
    exact absurd hτsign (by decide)
  · -- closed under the involution
    intro g hg; exact hGclosed g hg
  · -- it is an involution
    intro g _; show (g * τ) * τ = g
    rw [mul_assoc, hτ2, mul_one]

omit [CharZero k] in
/-- **Column-stabiliser conjugation.** `ρ ∈ C_{σ·t} ↔ σ⁻¹ρσ ∈ C_t` — the column
stabiliser transforms by conjugation under the `Sₙ` action, since
`colPattern (σ·t) = σ · colPattern t`. -/
theorem mem_colStab_smul (σ : Equiv.Perm (Fin (Specht.nOf μ))) (t : Specht.Tableau μ)
    (ρ : Equiv.Perm (Fin (Specht.nOf μ))) :
    ρ ∈ Specht.colStab (σ • t) ↔ σ⁻¹ * ρ * σ ∈ Specht.colStab t := by
  rw [Specht.mem_colStab, Specht.mem_colStab, Specht.colPattern_smul]
  constructor
  · intro h
    rw [mul_smul, mul_smul, h, ← mul_smul, inv_mul_cancel, one_smul]
  · intro h
    rw [← mul_smul]
    have hrw : ρ * σ = σ * (σ⁻¹ * ρ * σ) := by group
    rw [hrw, mul_smul, h]

omit [CharZero k] in
/-- **Polytabloid equivariance (sorry-free).** The polytabloid is `Sₙ`-equivariant:
`e_{σ·t} = σ · e_t`, i.e. acting on the tableau by `σ` equals acting on the
polytabloid by the module representation `Mtab.rep`. Reindex the column-stabiliser
sum by the conjugation `π ↦ σπσ⁻¹` (bijecting `C_t ≅ C_{σ·t}`, preserving sign,
and sending `σ·(π·t)` to `(σπσ⁻¹)·(σ·t)`). -/
theorem polytabloid_rep_smul (σ : Equiv.Perm (Fin (Specht.nOf μ))) (t : Specht.Tableau μ) :
    Specht.polytabloid (k := k) (σ • t)
      = Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t) := by
  classical
  rw [Specht.polytabloid, Specht.polytabloid, map_sum]
  refine Finset.sum_bij'
    (i := fun (ρ : Specht.colStab (σ • t)) _ =>
      (⟨σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ,
        (mem_colStab_smul σ t _).mp ρ.2⟩ : Specht.colStab t))
    (j := fun (π : Specht.colStab t) _ =>
      (⟨σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹, ?_⟩ : Specht.colStab (σ • t)))
    ?_ ?_ ?_ ?_ ?_
  · -- `σπσ⁻¹ ∈ C_{σ·t}`
    rw [mem_colStab_smul]
    have : σ⁻¹ * (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹) * σ
        = (π : Equiv.Perm (Fin (Specht.nOf μ))) := by group
    rw [this]; exact π.2
  · intro ρ _; exact Finset.mem_univ _
  · intro π _; exact Finset.mem_univ _
  · -- left inverse `j (i ρ) = ρ`
    intro ρ _; apply Subtype.ext
    show σ * (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) * σ⁻¹ = ρ
    group
  · -- right inverse `i (j π) = π`
    intro π _; apply Subtype.ext
    show σ⁻¹ * (σ * (π : Equiv.Perm (Fin (Specht.nOf μ))) * σ⁻¹) * σ = π
    group
  · -- term equality
    intro ρ _
    rw [map_zsmul, Specht.Mtab.rep_of]
    congr 1
    · -- sign: `sgn ρ = sgn (σ⁻¹ρσ)`
      have : Equiv.Perm.sign (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ)
          = Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) := by
        rw [map_mul, map_mul, map_inv, mul_right_comm, inv_mul_cancel, one_mul]
      rw [this]
    · -- tabloid: `ρ • σ • t = σ • (σ⁻¹ρσ) • t`
      show Specht.Mtab.of (k := k) ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) • σ • t)
        = Specht.Mtab.of (k := k)
            (σ • (σ⁻¹ * (ρ : Equiv.Perm (Fin (Specht.nOf μ))) * σ) • t)
      congr 1
      rw [← mul_smul, ← mul_smul, ← mul_assoc, ← mul_assoc, mul_inv_cancel,
        one_mul, mul_smul]

omit [CharZero k] in
/-- **Polytabloid is a sign-eigenvector of its column stabiliser (sorry-free).**
For `σ ∈ C_t`, the representation acts on `e_t` by the sign character:
`σ · e_t = sgn(σ) · e_t`. Immediate from equivariance
(`polytabloid_rep_smul`: `e_{σ·t} = σ · e_t`) composed with column-antisymmetry
(`polytabloid_colStab_smul`: `e_{σ·t} = sgn(σ) · e_t` for `σ ∈ C_t`). This is the
eigenvector property the Garnir antisymmetriser bridge consumes. -/
theorem rep_polytabloid_of_mem_colStab (t : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab t) :
    Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign σ : ℤ) • Specht.polytabloid (k := k) t := by
  rw [← polytabloid_rep_smul, polytabloid_colStab_smul t hσ]

omit [CharZero k] in
/-- **Antisymmetriser eigenvalue (sorry-free).** Summing the signed group action
over any finite set `H` of column-stabiliser elements collapses to `|H| · e_t`:
`∑_{ρ∈H} sgn(ρ) · (ρ · e_t) = |H| · e_t`, because each term is
`sgn(ρ)·sgn(ρ)·e_t = e_t` by the sign-eigenvector property (`sgn(ρ)² = 1`). This
is the `α · e_t = |S_A×S_B| · e_t` step of the Garnir coset→polytabloid bridge
(here for an arbitrary `H ⊆ C_t`, of which `S_A×S_B` is the relevant instance). -/
theorem sum_sign_rep_polytabloid (t : Specht.Tableau μ)
    (H : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hH : ∀ ρ ∈ H, ρ ∈ Specht.colStab t) :
    ∑ ρ ∈ H, (Equiv.Perm.sign ρ : ℤ) •
        Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)
      = H.card • Specht.polytabloid (k := k) t := by
  classical
  have hterm : ∀ ρ ∈ H, (Equiv.Perm.sign ρ : ℤ) •
      Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)
        = Specht.polytabloid (k := k) t := by
    intro ρ hρ
    rw [rep_polytabloid_of_mem_colStab t (hH ρ hρ), smul_smul]
    have hs2 : (Equiv.Perm.sign ρ : ℤ) * (Equiv.Perm.sign ρ : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign ρ) with h | h <;> rw [h] <;> decide
    rw [hs2, one_smul]
  rw [Finset.sum_congr rfl hterm, Finset.sum_const]

omit [CharZero k] in
/-- **Polytabloid-level Garnir annihilation (sorry-free).** The `rep`-level analog
of `mtab_sum_sign_smul_of_eq_zero`: if a `sign(-1)` involution `τ` *fixes the
polytabloid* (`τ · e_t = e_t`) and `G` is right-`τ`-closed, the signed group-action
sum vanishes, `∑_{g∈G} sgn(g) · (g · e_t) = 0`. Same sign-reversing-involution
pairing `g ↔ gτ`: `rep(gτ)(e_t) = rep(g)(rep(τ)(e_t)) = rep(g)(e_t)` while
`sgn(gτ) = -sgn(g)`. Once a row descent supplies such a `τ` (fixing `e_t` because
it lies in a row after the Garnir swap), this is the Garnir relation
`g_{A,B} · e_t = 0` at the polytabloid level. -/
theorem sum_sign_rep_eq_zero_of_fixed (t : Specht.Tableau μ)
    (G : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (τ : Equiv.Perm (Fin (Specht.nOf μ)))
    (hτ2 : τ * τ = 1) (hτsign : Equiv.Perm.sign τ = -1)
    (hτfix : Specht.Mtab.rep μ τ (Specht.polytabloid (k := k) t)
      = Specht.polytabloid (k := k) t)
    (hGclosed : ∀ g ∈ G, g * τ ∈ G) :
    ∑ g ∈ G, (Equiv.Perm.sign g : ℤ) •
        Specht.Mtab.rep μ g (Specht.polytabloid (k := k) t) = 0 := by
  classical
  have hfix : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      Specht.Mtab.rep μ (g * τ) (Specht.polytabloid (k := k) t)
        = Specht.Mtab.rep μ g (Specht.polytabloid (k := k) t) := by
    intro g
    rw [map_mul]
    exact congrArg (Specht.Mtab.rep μ g) hτfix
  have hs : ∀ g : Equiv.Perm (Fin (Specht.nOf μ)),
      (Equiv.Perm.sign (g * τ) : ℤ) = -(Equiv.Perm.sign g : ℤ) := by
    intro g; rw [map_mul, hτsign]; simp
  refine Finset.sum_involution (fun g _ => g * τ) ?_ ?_ ?_ ?_
  · intro g _
    rw [hfix g, hs g, neg_smul]; abel
  · intro g _ _ hgg
    have hτ1 : τ = 1 := by
      have hg1 : g * τ = g * 1 := by rw [mul_one]; exact hgg
      exact mul_left_cancel hg1
    rw [hτ1, map_one] at hτsign; exact absurd hτsign (by decide)
  · intro g hg; exact hGclosed g hg
  · intro g _; show (g * τ) * τ = g; rw [mul_assoc, hτ2, mul_one]

omit [CharZero k] in
/-- **Coset antisymmetriser collapse (sorry-free) — Garnir piece 2, bridge step 1.**
Factoring the representation of a fixed `π` out of an inner signed sum over a set
`H ⊆ C_t`: since every `ρ ∈ H` fixes `e_t` up to its sign
(`rep_polytabloid_of_mem_colStab`), the signed sum over the *left-translated* family
`{π·ρ : ρ ∈ H}` collapses to `sgn(π)·|H|·(π·e_t)`.

This is the inner-antisymmetriser step of the Garnir coset decomposition
`S_{A∪B} = ⊔_π π·(S_A × S_B)`: within each coset the `S_A × S_B` factor (a subgroup of
`C_t`) collapses via `sum_sign_rep_polytabloid`, leaving a single `±π·e_t` per coset
representative `π`. Summing this identity over a transversal is the next bridge step. -/
theorem sum_sign_rep_coset_collapse (t : Specht.Tableau μ)
    (H : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (π : Equiv.Perm (Fin (Specht.nOf μ)))
    (hH : ∀ ρ ∈ H, ρ ∈ Specht.colStab t) :
    ∑ ρ ∈ H, (Equiv.Perm.sign (π * ρ) : ℤ) •
        Specht.Mtab.rep μ (π * ρ) (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign π : ℤ) • H.card •
          Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) := by
  classical
  -- Rewrite each term `sgn(π*ρ) • rep(π*ρ) e_t` as `sgn π • rep π (sgn ρ • rep ρ e_t)`.
  have hterm : ∀ ρ ∈ H, (Equiv.Perm.sign (π * ρ) : ℤ) •
      Specht.Mtab.rep μ (π * ρ) (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign π : ℤ) • Specht.Mtab.rep μ π
          ((Equiv.Perm.sign ρ : ℤ) • Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)) := by
    intro ρ _
    have hsign : (Equiv.Perm.sign (π * ρ) : ℤ)
        = (Equiv.Perm.sign π : ℤ) * (Equiv.Perm.sign ρ : ℤ) := by
      rw [map_mul]; push_cast; ring
    have hrep : Specht.Mtab.rep μ (π * ρ) (Specht.polytabloid (k := k) t)
        = Specht.Mtab.rep μ π (Specht.Mtab.rep μ ρ (Specht.polytabloid (k := k) t)) := by
      rw [map_mul, Module.End.mul_apply]
    rw [hsign, hrep, map_zsmul, mul_smul]
  rw [Finset.sum_congr rfl hterm, ← Finset.smul_sum, ← map_sum]
  -- Inner sum collapses: `∑_{ρ∈H} sgn ρ • rep ρ e_t = |H| • e_t`.
  rw [sum_sign_rep_polytabloid t H hH, map_nsmul]

/-- **Transversal annihilation (sorry-free) — Garnir piece 2, bridge step 2.**
Given a set `H ⊆ C_t` with `0 < |H|` (the `S_A × S_B` factor) and a transversal `T`
(coset representatives), *if* the signed group-action sum over the full product family
`{π·ρ : π ∈ T, ρ ∈ H}` vanishes (hypothesis `hann` — supplied by the tabloid-level
Garnir annihilation `mtab_sum_sign_smul_of_eq_zero` / `sum_sign_rep_eq_zero_of_fixed`
once the Garnir set is built), then the *transversal* signed sum vanishes:
`∑_{π ∈ T} sgn(π)·(π·e_t) = 0`.

The `|H|` factor produced by collapsing each coset (`sum_sign_rep_coset_collapse`)
is cancelled using `CharZero` — this is where dividing by `|S_A × S_B|` enters. The
final Garnir relation `e_t = −∑_{π ≠ 1} sgn(π)·e_{π·t}` then follows by isolating the
identity coset representative. -/
theorem transversal_sum_eq_zero (t : Specht.Tableau μ)
    (T H : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hH : ∀ ρ ∈ H, ρ ∈ Specht.colStab t) (hpos : 0 < H.card)
    (hann : ∑ π ∈ T, ∑ ρ ∈ H, (Equiv.Perm.sign (π * ρ) : ℤ) •
        Specht.Mtab.rep μ (π * ρ) (Specht.polytabloid (k := k) t) = 0) :
    ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) = 0 := by
  classical
  set S := ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
      Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) with hS
  -- Collapse each coset's inner sum, then pull the `|H|` factor out front.
  have h2 : ∀ π ∈ T, ∑ ρ ∈ H, (Equiv.Perm.sign (π * ρ) : ℤ) •
      Specht.Mtab.rep μ (π * ρ) (Specht.polytabloid (k := k) t)
      = H.card • ((Equiv.Perm.sign π : ℤ) •
          Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t)) := by
    intro π _
    rw [sum_sign_rep_coset_collapse t H π hH, smul_comm]
  rw [Finset.sum_congr rfl h2, ← Finset.smul_sum, ← hS] at hann
  -- `|H| • S = 0` with `|H| ≠ 0` in a char-0 field module ⇒ `S = 0`.
  have hne : (H.card : k) ≠ 0 := Nat.cast_ne_zero.mpr hpos.ne'
  calc S = (H.card : k)⁻¹ • (H.card : k) • S := by rw [inv_smul_smul₀ hne]
    _ = (H.card : k)⁻¹ • (H.card • S) := by rw [Nat.cast_smul_eq_nsmul]
    _ = (H.card : k)⁻¹ • (0 : Specht.Mtab (k := k) μ) := by rw [hann]
    _ = 0 := smul_zero _

omit [CharZero k] in
/-- **Polytabloid annihilation from a tabloid-annihilation family (sorry-free) —
Garnir piece 2, annihilation reduction.** The rep-level signed sum
`∑_{σ ∈ G} sgn(σ)·(σ·e_t)` vanishes as soon as, for *every* column-stabiliser element
`ρ ∈ C_t`, the tabloid-level signed sum `∑_{σ ∈ G} sgn(σ)·{σ·ρ·t}` vanishes (`hfam`).

Pure linear algebra: expand `e_t = ∑_{ρ ∈ C_t} sgn(ρ)·{ρ·t}`, push `rep σ` through
(`rep_of`: `σ·{ρ·t} = {σ·ρ·t}`), swap the `G`- and `C_t`-sums, and factor out `sgn(ρ)`
so each inner sum is exactly a term of `hfam`. This is the bridge from the tabloid-level
Garnir annihilation (`mtab_sum_sign_smul_of_eq_zero`, applied to each `ρ·t` with a
same-row transposition of the Garnir set) to `transversal_sum_eq_zero`'s `hann`
hypothesis — isolating the remaining pigeonhole crux entirely inside `hfam`. -/
theorem sum_sign_rep_polytabloid_eq_zero_of_family (t : Specht.Tableau μ)
    (G : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hfam : ∀ ρ : Specht.colStab t, ∑ σ ∈ G, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.of (k := k)
          (σ • (ρ : Equiv.Perm (Fin (Specht.nOf μ))) • t) = 0) :
    ∑ σ ∈ G, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t) = 0 := by
  classical
  simp only [Specht.polytabloid, map_sum, map_zsmul, Specht.Mtab.rep_of, Finset.smul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_eq_zero (fun ρ _ => ?_)
  have hpull : ∑ σ ∈ G, (Equiv.Perm.sign σ : ℤ) •
        (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) •
          Specht.Mtab.of (k := k) (σ • (ρ : Equiv.Perm (Fin (Specht.nOf μ))) • t)
      = (Equiv.Perm.sign (ρ : Equiv.Perm (Fin (Specht.nOf μ))) : ℤ) •
          ∑ σ ∈ G, (Equiv.Perm.sign σ : ℤ) •
            Specht.Mtab.of (k := k) (σ • (ρ : Equiv.Perm (Fin (Specht.nOf μ))) • t) := by
    rw [Finset.smul_sum]
    exact Finset.sum_congr rfl (fun σ _ => smul_comm _ _ _)
  rw [hpull, hfam ρ, smul_zero]

/-! #### The self-contained dominance weight (sorry-free)

The straightening induction needs a well-founded measure that strictly increases
under a Garnir step. Because this file sits **below** `SpechtDominanceCore` in the
import graph, we cannot reuse that module's `domRel`; instead we define, locally
and self-containedly, a strictly-monotone ℕ-valued *linear extension* of the
dominance order — the total of all clamped dominance counts `domCount' f i m`
(`= #{l : (l:ℕ) < m ∧ f l ≤ i}`, "how many of the `m` smallest labels lie in rows
`≤ i`"), summed over `i, m ∈ [0, n]`. A tabloid strictly dominating another has
this total strictly larger, so it is a valid well-founded measure. All ℕ-valued
(§7c-clean: no `ℝ`, no ordering on `q`). -/

/-- The **dominance count** of a row pattern `f` (self-contained, local to this
file): `domCount' f i m = #{l : (l:ℕ) < m ∧ f l ≤ i}`. -/
def domCount' (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) : ℕ :=
  (Finset.univ.filter (fun l : Fin (Specht.nOf μ) => (l : ℕ) < m ∧ f l ≤ i)).card

/-- The **dominance weight** of a tableau: the total of all clamped dominance
counts of its row pattern. A strictly-monotone linear extension of the dominance
order (a Garnir straightening step strictly increases it), hence a valid
well-founded measure for the straightening induction. -/
def domWeight (t : Specht.Tableau μ) : ℕ :=
  ∑ i ∈ Finset.range (Specht.nOf μ + 1), ∑ m ∈ Finset.range (Specht.nOf μ + 1),
    domCount' (Specht.rowPattern t) i m

/-- A fixed ceiling for `domWeight` (used to run the strong induction on the
decreasing measure `domBound μ - domWeight t`). -/
def domBound (μ : YoungDiagram) : ℕ :=
  (Specht.nOf μ + 1) * ((Specht.nOf μ + 1) * Specht.nOf μ)

/-- Each dominance count is bounded by `n = nOf μ` (a filtered subset of the
`n`-element label set). -/
theorem domCount'_le (f : Fin (Specht.nOf μ) → ℕ) (i m : ℕ) :
    domCount' (μ := μ) f i m ≤ Specht.nOf μ := by
  unfold domCount'
  refine le_trans (Finset.card_filter_le _ _) ?_
  rw [Finset.card_univ, Fintype.card_fin]

/-- `domWeight t ≤ domBound μ` (sum of `(n+1)²` counts, each `≤ n`). -/
theorem domWeight_le (t : Specht.Tableau μ) : domWeight t ≤ domBound μ := by
  unfold domWeight domBound
  calc ∑ i ∈ Finset.range (Specht.nOf μ + 1), ∑ m ∈ Finset.range (Specht.nOf μ + 1),
          domCount' (Specht.rowPattern t) i m
      ≤ ∑ _i ∈ Finset.range (Specht.nOf μ + 1), ∑ _m ∈ Finset.range (Specht.nOf μ + 1),
          Specht.nOf μ := by
        refine Finset.sum_le_sum (fun i _ => ?_)
        refine Finset.sum_le_sum (fun m _ => ?_)
        exact domCount'_le _ i m
    _ = (Specht.nOf μ + 1) * ((Specht.nOf μ + 1) * Specht.nOf μ) := by
        simp [Finset.sum_const, Finset.card_range, Nat.mul_comm, Nat.mul_left_comm]

/-! #### Column-maximality kills column descents (Garnir steps 3b/3c, sorry-free)

Two sorry-free pieces: (3b) the transposition of two same-column labels lies in the
column stabiliser `C_t`; (3c) swapping a *column descent* — a same-column pair whose
larger label sits in a strictly lower row — strictly raises the dominance measure
`domWeight`. Together they say: under column-maximality `hmax` (no `σ ∈ C_t` raises
`domWeight`), `t` has no column descent. All `ℕ`-valued (§7c-clean). -/

/-- **Garnir step 3b (sorry-free).** The transposition of two labels lying in the same
column of `t` stabilises the column pattern, hence lies in `C_t`. -/
theorem colStab_swap_mem (t : Specht.Tableau μ) {a b : Fin (Specht.nOf μ)}
    (hcol : Specht.colPattern t a = Specht.colPattern t b) :
    Equiv.swap a b ∈ Specht.colStab t := by
  rw [Specht.mem_colStab]
  funext l
  rw [Specht.arrow_smul_apply, Equiv.symm_swap]
  rcases eq_or_ne l a with rfl | hla
  · rw [Equiv.swap_apply_left]; exact hcol.symm
  rcases eq_or_ne l b with rfl | hlb
  · rw [Equiv.swap_apply_right]; exact hcol
  · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]

/-- The row index of any cell of a Young diagram is `< ν.card` (the `i+1` cells
`(0,0), …, (i,0)` lie in `ν` by down-closure). Local copy — the identical
`SpechtDominanceCore.row_lt_card` sits *above* this file in the import graph. -/
theorem row_lt_card (ν : YoungDiagram) (i j : ℕ) (h : (i, j) ∈ ν) : i < ν.card := by
  classical
  have hsub : (Finset.range (i + 1)).image (fun i' => (i', 0)) ⊆ ν.cells := by
    intro c hc
    rw [Finset.mem_image] at hc
    obtain ⟨i', hi', rfl⟩ := hc
    rw [Finset.mem_range] at hi'
    rw [YoungDiagram.mem_cells]
    exact YoungDiagram.up_left_mem ν (Nat.lt_succ_iff.mp hi') (Nat.zero_le _) h
  have hcard : ((Finset.range (i + 1)).image (fun i' => (i', 0))).card = i + 1 := by
    rw [Finset.card_image_of_injective]
    · rw [Finset.card_range]
    · intro x y hxy; simpa using hxy
  have hle : i + 1 ≤ ν.card := by
    show i + 1 ≤ ν.cells.card
    rw [← hcard]; exact Finset.card_le_card hsub
  omega

/-- The row pattern of a tableau is bounded by `nOf μ`. Local copy (see `row_lt_card`). -/
theorem rowPattern_lt_nOf (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) :
    Specht.rowPattern t l < Specht.nOf μ :=
  row_lt_card μ _ _ (t l).2

/-- **Two-point surgery for `domCount'`.** Splitting the underlying `card` sum at the
labels `a ≠ b` leaves a common tail (the sum over `univ \ {a,b}`) plus the two
indicator contributions of `a` and `b`. -/
theorem domCount'_two_point (g : Fin (Specht.nOf μ) → ℕ) {a b : Fin (Specht.nOf μ)}
    (hab : a ≠ b) (i m : ℕ) :
    domCount' (μ := μ) g i m
      = (∑ l ∈ (Finset.univ.erase a).erase b,
            if ((l : ℕ) < m ∧ g l ≤ i) then 1 else 0)
        + (if ((a : ℕ) < m ∧ g a ≤ i) then 1 else 0)
        + (if ((b : ℕ) < m ∧ g b ≤ i) then 1 else 0) := by
  classical
  unfold domCount'
  rw [Finset.card_filter]
  have hb : b ∈ Finset.univ.erase a :=
    Finset.mem_erase.mpr ⟨hab.symm, Finset.mem_univ b⟩
  rw [← Finset.add_sum_erase Finset.univ _ (Finset.mem_univ a),
      ← Finset.add_sum_erase (Finset.univ.erase a) _ hb]
  ring

/-- **Garnir step 3c (sorry-free) — the dominance strict-increase core.** Swapping a
*column descent* strictly raises `domWeight`: if the smaller label `a` (`↑a < ↑b`)
sits in a strictly lower row than the larger label `b`
(`rowPattern t b < rowPattern t a`), then the transposition `swap a b` — which moves
the smaller label up — strictly increases the dominance measure. The gap is exactly
`(rowPattern t a − rowPattern t b) · (↑b − ↑a) ≥ 1`, realised termwise at
`(i, m) = (rowPattern t b, ↑b)`. -/
theorem domWeight_swap_lt (t : Specht.Tableau μ) {a b : Fin (Specht.nOf μ)}
    (hab : (a : ℕ) < (b : ℕ))
    (hrow : Specht.rowPattern t b < Specht.rowPattern t a) :
    domWeight t < domWeight (Equiv.swap a b • t) := by
  classical
  set f := Specht.rowPattern t
  have hne : a ≠ b := fun h => (Nat.ne_of_lt hab) (by rw [h])
  have hrp : Specht.rowPattern (Equiv.swap a b • t)
      = fun l => f (Equiv.swap a b l) := by
    funext l
    rw [Specht.rowPattern_smul, Specht.arrow_smul_apply, Equiv.symm_swap]
  have hpt : ∀ i m,
      (if ((a : ℕ) < m ∧ f a ≤ i) then (1:ℕ) else 0)
        + (if ((b : ℕ) < m ∧ f b ≤ i) then 1 else 0)
      ≤ (if ((a : ℕ) < m ∧ f b ≤ i) then 1 else 0)
        + (if ((b : ℕ) < m ∧ f a ≤ i) then 1 else 0) := by
    intro i m
    split_ifs <;> omega
  have key : ∀ i m,
      domCount' (μ := μ) f i m
        ≤ domCount' (μ := μ) (Specht.rowPattern (Equiv.swap a b • t)) i m := by
    intro i m
    rw [hrp, domCount'_two_point (μ := μ) f hne i m,
        domCount'_two_point (μ := μ) (fun l => f (Equiv.swap a b l)) hne i m]
    have htail :
        (∑ l ∈ (Finset.univ.erase a).erase b,
            if ((l : ℕ) < m ∧ f l ≤ i) then (1:ℕ) else 0)
        = ∑ l ∈ (Finset.univ.erase a).erase b,
            if ((l : ℕ) < m ∧ f (Equiv.swap a b l) ≤ i) then (1:ℕ) else 0 := by
      apply Finset.sum_congr rfl
      intro l hl
      have hla : l ≠ a := (Finset.mem_erase.mp (Finset.mem_of_mem_erase hl)).1
      have hlb : l ≠ b := (Finset.mem_erase.mp hl).1
      rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
    rw [htail, Equiv.swap_apply_left, Equiv.swap_apply_right]
    have := hpt i m
    omega
  have hstrict :
      domCount' (μ := μ) f (f b) (b : ℕ)
        < domCount' (μ := μ) (Specht.rowPattern (Equiv.swap a b • t)) (f b) (b : ℕ) := by
    rw [hrp, domCount'_two_point (μ := μ) f hne (f b) (b : ℕ),
        domCount'_two_point (μ := μ) (fun l => f (Equiv.swap a b l)) hne (f b) (b : ℕ)]
    have htail :
        (∑ l ∈ (Finset.univ.erase a).erase b,
            if ((l : ℕ) < (b : ℕ) ∧ f l ≤ f b) then (1:ℕ) else 0)
        = ∑ l ∈ (Finset.univ.erase a).erase b,
            if ((l : ℕ) < (b : ℕ) ∧ f (Equiv.swap a b l) ≤ f b) then (1:ℕ) else 0 := by
      apply Finset.sum_congr rfl
      intro l hl
      have hla : l ≠ a := (Finset.mem_erase.mp (Finset.mem_of_mem_erase hl)).1
      have hlb : l ≠ b := (Finset.mem_erase.mp hl).1
      rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
    rw [htail, Equiv.swap_apply_left, Equiv.swap_apply_right]
    split_ifs <;> omega
  unfold domWeight
  refine Finset.sum_lt_sum (fun i _ => Finset.sum_le_sum (fun m _ => key i m)) ?_
  refine ⟨f b, Finset.mem_range.mpr (Nat.lt_succ_of_lt (rowPattern_lt_nOf t b)), ?_⟩
  refine Finset.sum_lt_sum (fun m _ => key (f b) m) ?_
  exact ⟨(b : ℕ), Finset.mem_range.mpr (Nat.lt_succ_of_lt b.2), hstrict⟩

/-- **Column-standardness under column-maximality (sorry-free).** Combining steps 3b/3c:
if `t` is column-(dominance-)maximal (`hmax`: no `σ ∈ C_t` raises `domWeight`), then the
labels in each column of `t` strictly increase with the row — `t` has **no column
descent**. Two same-column labels with `↑a < ↑b` have `rowPattern t a < rowPattern t b`;
a violation would give a `domWeight`-raising column transposition (`colStab_swap_mem` +
`domWeight_swap_lt`) contradicting `hmax`. This is the exact "column-sort exhausted"
consequence the Garnir core `straightening_step_colMax` consumes: it leaves only pure
*row* descents to resolve. -/
theorem colStandard_of_colMax (t : Specht.Tableau μ)
    (hmax : ∀ σ : Specht.colStab t,
      domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t) ≤ domWeight t)
    {a b : Fin (Specht.nOf μ)}
    (hcol : Specht.colPattern t a = Specht.colPattern t b)
    (hab : (a : ℕ) < (b : ℕ)) :
    Specht.rowPattern t a < Specht.rowPattern t b := by
  rcases lt_trichotomy (Specht.rowPattern t a) (Specht.rowPattern t b) with h | h | h
  · exact h
  · exfalso
    have hcell : (t a : ℕ × ℕ) = (t b : ℕ × ℕ) := Prod.ext h hcol
    have hab' : a = b := t.injective (Subtype.ext hcell)
    exact (Nat.ne_of_lt hab) (by rw [hab'])
  · exfalso
    exact absurd (hmax ⟨Equiv.swap a b, colStab_swap_mem t hcol⟩)
      (not_le.mpr (domWeight_swap_lt t hab h))

omit [CharZero k] in
/-- **Pure row-descent existence under column-maximality (sorry-free).** Combines
`exists_descent_of_not_mem_range` (a non-standard polytabloid has a row *or* column
descent) with `colStandard_of_colMax` (column-maximality kills column descents): a
column-maximal `t` whose polytabloid is non-standard has a **row descent**. This is
exactly the input the Garnir coset-sum step of `straightening_step_colMax` consumes —
it closes Garnir piece 1. -/
theorem exists_row_descent_of_colMax (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : Specht.colStab t,
      domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t) ≤ domWeight t) :
    ∃ i j, ∃ (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij1 ≤ labelAt t hij := by
  rcases exists_descent_of_not_mem_range (k := k) t h with hrow | hcol
  · -- already a row descent
    exact hrow
  · -- column descent is impossible under `hmax`
    exfalso
    obtain ⟨i, j, hij, hi1j, hle⟩ := hcol
    set a := t.symm ⟨(i + 1, j), (YoungDiagram.mem_cells _).2 hi1j⟩ with ha
    set b := t.symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩ with hb
    have hta : (t a : ℕ × ℕ) = (i + 1, j) := by rw [ha, Equiv.apply_symm_apply]
    have htb : (t b : ℕ × ℕ) = (i, j) := by rw [hb, Equiv.apply_symm_apply]
    have hle' : (a : ℕ) ≤ (b : ℕ) := hle
    have hne : a ≠ b := by
      intro he
      rw [he] at hta
      rw [htb] at hta
      exact (by simp : ((i, j) : ℕ × ℕ) ≠ (i + 1, j)) hta
    have hab : (a : ℕ) < (b : ℕ) := lt_of_le_of_ne hle' (fun he => hne (Fin.ext he))
    have hcolab : Specht.colPattern t a = Specht.colPattern t b := by
      show (t a : ℕ × ℕ).2 = (t b : ℕ × ℕ).2
      rw [hta, htb]
    have hrow := colStandard_of_colMax t hmax hcolab hab
    rw [show Specht.rowPattern t a = i + 1 from by show (t a : ℕ × ℕ).1 = i + 1; rw [hta],
        show Specht.rowPattern t b = i from by show (t b : ℕ × ℕ).1 = i; rw [htb]] at hrow
    omega

omit [CharZero k] in
/-- **Garnir assembly (sorry-free) — Garnir piece 2, final bookkeeping.**
Given a transversal `T ∋ 1` for which (i) the signed representation sum vanishes
(`hann` — the output of `transversal_sum_eq_zero`), and (ii) every *non-identity*
representative `π` strictly raises the dominance measure
(`hdom : domWeight t < domWeight (π • t)`), the polytabloid `e_t` is a `k`-linear
combination of polytabloids of strictly `domWeight`-greater tabloids.

Pure bookkeeping: isolate the identity term `sgn(1)·(1·e_t) = e_t` from `hann`, giving
`e_t = ∑_{π ∈ T, π ≠ 1} (−sgn π)·e_{π·t}` (via equivariance `polytabloid_rep_smul`),
then reindex the permutation sum to a sum over the tableaux `{π·t}` with fibrewise-
aggregated coefficients. This is the interface that closes `straightening_step_colMax`
once the Garnir set supplies `hann` and `hdom`. -/
theorem garnir_assembly (t : Specht.Tableau μ)
    (T : Finset (Equiv.Perm (Fin (Specht.nOf μ)))) (h1 : (1 : Equiv.Perm (Fin (Specht.nOf μ))) ∈ T)
    (hdom : ∀ π ∈ T, π ≠ 1 →
      domWeight t < domWeight ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hann : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) = 0) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  -- Abbreviations: the non-identity part of the transversal, and the coefficient sum.
  set E := T.erase (1 : Equiv.Perm (Fin (Specht.nOf μ))) with hE
  -- Isolate the identity term of `hann`: `e_t + ∑_{π ∈ E} sgn(π)·(π·e_t) = 0`.
  rw [← Finset.add_sum_erase T _ h1] at hann
  simp only [map_one, Module.End.one_apply, Units.val_one, one_smul] at hann
  -- Hence `e_t = ∑_{π ∈ E} (−sgn π : k) · e_{π·t}` (equivariance turns `π·e_t` into `e_{π·t}`).
  have hexp : Specht.polytabloid (k := k) t
      = ∑ π ∈ E, (-(Equiv.Perm.sign π : k)) •
          Specht.polytabloid (k := k) ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t) := by
    have hneg : Specht.polytabloid (k := k) t
        = - ∑ π ∈ E, (Equiv.Perm.sign π : ℤ) •
            Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) := by
      rw [eq_neg_iff_add_eq_zero]; exact hann
    rw [hneg, ← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl (fun π _ => ?_)
    rw [← polytabloid_rep_smul, ← neg_smul, ← Int.cast_smul_eq_zsmul k, Int.cast_neg]
  -- Reindex the permutation sum to a sum over tableaux `{π·t}`, aggregating coefficients.
  refine ⟨E.image (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t),
    fun t' => ∑ π ∈ E.filter (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t = t'),
      (-(Equiv.Perm.sign π : k)), ?_, ?_⟩
  · -- dominance: every image tableau strictly dominates `t`
    intro t' ht'
    rw [Finset.mem_image] at ht'
    obtain ⟨π, hπ, rfl⟩ := ht'
    exact hdom π (Finset.mem_of_mem_erase hπ) (Finset.ne_of_mem_erase hπ)
  · -- the linear combination, via fibrewise summation over `π ↦ π·t`
    rw [hexp]
    rw [← Finset.sum_fiberwise_of_maps_to
          (g := fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t)
          (t := E.image (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t))
          (fun π _ => Finset.mem_image_of_mem _ (by assumption))]
    refine Finset.sum_congr rfl (fun t' _ => ?_)
    rw [Finset.sum_smul]
    refine Finset.sum_congr rfl (fun π hπ => ?_)
    rw [(Finset.mem_filter.mp hπ).2]

/-! #### Garnir set — column label counts (sorry-free)

Foundational cardinalities for the Garnir pigeonhole: the labels sitting in a fixed
column `c` of `t` biject (via `t`) with the cells `μ.col c`, so there are exactly
`μ.colLen c` of them. -/

omit [CharZero k] in
/-- The labels in column `c` of `t` number exactly `μ.colLen c` (they biject with the
cells of `μ.col c` under the tableau equivalence `t`). -/
theorem card_col_labels (t : Specht.Tableau μ) (c : ℕ) :
    (Finset.univ.filter (fun l => Specht.colPattern t l = c)).card = μ.colLen c := by
  classical
  rw [YoungDiagram.colLen_eq_card]
  refine (Finset.card_image_of_injOn (fun a _ b _ h => t.injective (Subtype.ext h))).symm.trans
    (congrArg Finset.card ?_)
  ext p
  simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and,
    YoungDiagram.mem_col_iff]
  constructor
  · rintro ⟨l, hl, rfl⟩
    exact ⟨(YoungDiagram.mem_cells _).mp (t l).2, hl⟩
  · rintro ⟨hp, hpc⟩
    refine ⟨t.symm ⟨p, (YoungDiagram.mem_cells _).mpr hp⟩, ?_, ?_⟩
    · show Specht.colPattern t _ = c
      show ((t (t.symm ⟨p, _⟩) : ℕ × ℕ)).2 = c
      rw [Equiv.apply_symm_apply]; exact hpc
    · show ((t (t.symm ⟨p, _⟩) : ℕ × ℕ)) = p
      rw [Equiv.apply_symm_apply]

omit [CharZero k] in
/-- The labels in column `c` of `t` with row index `< m` number exactly `m`, provided
`m ≤ μ.colLen c` (they biject with rows `0, …, m-1`, all of which occur in column `c`). -/
theorem card_col_labels_row_lt_of_le (t : Specht.Tableau μ) (c m : ℕ)
    (hm : m ≤ μ.colLen c) :
    (Finset.univ.filter
      (fun l => Specht.colPattern t l = c ∧ Specht.rowPattern t l < m)).card = m := by
  classical
  refine Eq.trans
    (Finset.card_bij (fun l _ => Specht.rowPattern t l) ?_ ?_ ?_) (Finset.card_range m)
  · intro l hl
    rw [Finset.mem_range]
    exact (Finset.mem_filter.mp hl).2.2
  · intro a ha b hb hab
    rw [Finset.mem_filter] at ha hb
    refine t.injective (Subtype.ext (Prod.ext hab ?_))
    exact (ha.2.1).trans (hb.2.1).symm
  · intro r hr
    rw [Finset.mem_range] at hr
    have hcell : (r, c) ∈ μ := YoungDiagram.mem_iff_lt_colLen.mpr (lt_of_lt_of_le hr hm)
    refine ⟨t.symm ⟨(r, c), (YoungDiagram.mem_cells _).2 hcell⟩, ?_, ?_⟩
    · rw [Finset.mem_filter]
      refine ⟨Finset.mem_univ _, ?_, ?_⟩
      · show ((t (t.symm ⟨(r, c), _⟩) : ℕ × ℕ)).2 = c
        rw [Equiv.apply_symm_apply]
      · show ((t (t.symm ⟨(r, c), _⟩) : ℕ × ℕ)).1 < m
        rw [Equiv.apply_symm_apply]; exact hr
    · show ((t (t.symm ⟨(r, c), _⟩) : ℕ × ℕ)).1 = r
      rw [Equiv.apply_symm_apply]

omit [CharZero k] in
/-- **Garnir pigeonhole (sorry-free) — the row collision for `hfam`.**
At a row descent `(i,j),(i,j+1) ∈ μ`, for *every* column permutation `ρ ∈ C_t` there
are two distinct labels — one in `A` (column `j`, row `≥ i`) and one in `B`
(column `j+1`, row `≤ i`) — that land in the **same row** of `ρ • t`.

Proof: `|A| = colLen j − i`, `|B| = i+1`, so `|A ∪ B| = colLen j + 1`; the map
`l ↦ rowPattern (ρ•t) l = rowPattern t (ρ⁻¹ l)` sends `A ∪ B` into
`{0, …, colLen j − 1}` (`ρ ∈ C_t` keeps `ρ⁻¹ l` in its column; `colLen (j+1) ≤ colLen j`),
a set of size `colLen j`, so two elements collide. Column-injectivity of the map rules
out both being in `A` or both in `B`, so the colliding pair straddles `A` and `B`. This
is exactly the same-row transposition `τ_ρ ∈ rowStab (ρ•t) ∩ S_{A∪B}` that
`mtab_sum_sign_smul_of_eq_zero` consumes to discharge `hfam ρ`. -/
theorem garnir_row_collision (t : Specht.Tableau μ) {i j : ℕ}
    (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ)
    (ρ : Equiv.Perm (Fin (Specht.nOf μ))) (hρ : ρ ∈ Specht.colStab t) :
    ∃ a b, a ≠ b ∧
      (Specht.colPattern t a = j ∧ i ≤ Specht.rowPattern t a) ∧
      (Specht.colPattern t b = j + 1 ∧ Specht.rowPattern t b ≤ i) ∧
      Specht.rowPattern (ρ • t) a = Specht.rowPattern (ρ • t) b := by
  classical
  set A := Finset.univ.filter
    (fun l => Specht.colPattern t l = j ∧ i ≤ Specht.rowPattern t l) with hA
  set B := Finset.univ.filter
    (fun l => Specht.colPattern t l = j + 1 ∧ Specht.rowPattern t l ≤ i) with hB
  have hi_lt : i < μ.colLen j := YoungDiagram.mem_iff_lt_colLen.mp hij
  have hi1_lt : i < μ.colLen (j + 1) := YoungDiagram.mem_iff_lt_colLen.mp hij1
  -- Helper facts about `ρ ∈ C_t` and the equivariance of the patterns.
  have hcol : ∀ l, Specht.colPattern t (ρ.symm l) = Specht.colPattern t l := by
    intro l
    calc Specht.colPattern t (ρ.symm l)
        = (ρ • Specht.colPattern t) l := (Specht.arrow_smul_apply _ _ _ _).symm
      _ = Specht.colPattern t l := by rw [Specht.mem_colStab.mp hρ]
  have hrow_eq : ∀ l, Specht.rowPattern (ρ • t) l = Specht.rowPattern t (ρ.symm l) := by
    intro l; rw [Specht.rowPattern_smul, Specht.arrow_smul_apply]
  have hcellmem : ∀ u, (Specht.rowPattern t u, Specht.colPattern t u) ∈ μ :=
    fun u => (YoungDiagram.mem_cells _).1 (t u).2
  have hcell_inj : ∀ u v, Specht.rowPattern t u = Specht.rowPattern t v →
      Specht.colPattern t u = Specht.colPattern t v → u = v :=
    fun u v hr hc => t.injective (Subtype.ext (Prod.ext hr hc))
  -- Cardinalities.
  have hcardA : A.card = μ.colLen j - i := by
    have hsub : Finset.univ.filter
        (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)
        ⊆ Finset.univ.filter (fun l => Specht.colPattern t l = j) := by
      intro l hl; rw [Finset.mem_filter] at hl ⊢; exact ⟨hl.1, hl.2.1⟩
    have hAeq : A = (Finset.univ.filter (fun l => Specht.colPattern t l = j)) \
        (Finset.univ.filter (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)) := by
      ext l
      simp only [hA, Finset.mem_filter, Finset.mem_sdiff, Finset.mem_univ, true_and, not_and,
        not_lt]
      constructor
      · rintro ⟨hc, hge⟩; exact ⟨hc, fun _ => hge⟩
      · rintro ⟨hc, hge⟩; exact ⟨hc, hge hc⟩
    rw [hAeq, Finset.card_sdiff, card_col_labels, Finset.inter_eq_left.mpr hsub,
      card_col_labels_row_lt_of_le t j i (le_of_lt hi_lt)]
  have hcardB : B.card = i + 1 := by
    have hBeq : B = Finset.univ.filter
        (fun l => Specht.colPattern t l = j + 1 ∧ Specht.rowPattern t l < i + 1) := by
      ext l; simp only [hB, Finset.mem_filter, Nat.lt_succ_iff]
    rw [hBeq, card_col_labels_row_lt_of_le t (j + 1) (i + 1) (by omega)]
  have hdisj : Disjoint A B := by
    rw [Finset.disjoint_left]
    intro l hlA hlB
    rw [hA, Finset.mem_filter] at hlA
    rw [hB, Finset.mem_filter] at hlB
    omega
  have hcardU : (A ∪ B).card = μ.colLen j + 1 := by
    rw [Finset.card_union_of_disjoint hdisj, hcardA, hcardB]; omega
  -- The row map lands in `range (colLen j)`.
  have hmaps : ∀ l ∈ A ∪ B, Specht.rowPattern (ρ • t) l ∈ Finset.range (μ.colLen j) := by
    intro l hl
    rw [Finset.mem_range, hrow_eq]
    rw [Finset.mem_union, hA, hB, Finset.mem_filter, Finset.mem_filter] at hl
    have hc : Specht.colPattern t (ρ.symm l) = j ∨ Specht.colPattern t (ρ.symm l) = j + 1 := by
      rw [hcol]; rcases hl with h | h
      · exact Or.inl h.2.1
      · exact Or.inr h.2.1
    rcases hc with h | h
    · have hmem : (Specht.rowPattern t (ρ.symm l), j) ∈ μ := by rw [← h]; exact hcellmem _
      exact YoungDiagram.mem_iff_lt_colLen.mp hmem
    · have hmem : (Specht.rowPattern t (ρ.symm l), j + 1) ∈ μ := by rw [← h]; exact hcellmem _
      exact lt_of_lt_of_le (YoungDiagram.mem_iff_lt_colLen.mp hmem)
        (μ.colLen_anti j (j + 1) (by omega))
  -- Pigeonhole.
  obtain ⟨x, hx, y, hy, hxy, hfxy⟩ :=
    Finset.exists_ne_map_eq_of_card_lt_of_maps_to
      (by rw [Finset.card_range, hcardU]; omega) hmaps
  -- Column-injectivity of the row map.
  have hinj : ∀ u v, Specht.colPattern t u = Specht.colPattern t v →
      Specht.rowPattern (ρ • t) u = Specht.rowPattern (ρ • t) v → u = v := by
    intro u v hc hr
    rw [hrow_eq, hrow_eq] at hr
    have hcuv : Specht.colPattern t (ρ.symm u) = Specht.colPattern t (ρ.symm v) := by
      rw [hcol, hcol, hc]
    exact ρ.symm.injective (hcell_inj _ _ hr hcuv)
  -- The colliding pair straddles `A` and `B`.
  rw [Finset.mem_union] at hx hy
  rcases hx with hxA | hxB
  · rcases hy with hyA | hyB
    · rw [hA, Finset.mem_filter] at hxA hyA
      exact absurd (hinj x y (hxA.2.1.trans hyA.2.1.symm) hfxy) hxy
    · rw [hA, Finset.mem_filter] at hxA
      rw [hB, Finset.mem_filter] at hyB
      exact ⟨x, y, hxy, hxA.2, hyB.2, hfxy⟩
  · rcases hy with hyA | hyB
    · rw [hB, Finset.mem_filter] at hxB
      rw [hA, Finset.mem_filter] at hyA
      exact ⟨y, x, hxy.symm, hyA.2, hxB.2, hfxy.symm⟩
    · rw [hB, Finset.mem_filter] at hxB hyB
      exact absurd (hinj x y (hxB.2.1.trans hyB.2.1.symm) hfxy) hxy

/-- The Garnir label-set `A`: labels in column `j` of `t` at rows `≥ i`. -/
def garnirA (t : Specht.Tableau μ) (i j : ℕ) : Finset (Fin (Specht.nOf μ)) :=
  Finset.univ.filter (fun l => Specht.colPattern t l = j ∧ i ≤ Specht.rowPattern t l)

/-- The Garnir label-set `B`: labels in column `j+1` of `t` at rows `≤ i`. -/
def garnirB (t : Specht.Tableau μ) (i j : ℕ) : Finset (Fin (Specht.nOf μ)) :=
  Finset.univ.filter (fun l => Specht.colPattern t l = j + 1 ∧ Specht.rowPattern t l ≤ i)

/-- The Garnir permutation set `S_{A∪B}`: permutations fixing every label outside
`A ∪ B`.  A subgroup (as a `Finset`) closed under right-multiplication by any
transposition of two labels of `A ∪ B`. -/
def garnirG (t : Specht.Tableau μ) (i j : ℕ) : Finset (Equiv.Perm (Fin (Specht.nOf μ))) :=
  Finset.univ.filter (fun σ => ∀ l, l ∉ garnirA t i j ∪ garnirB t i j → σ l = l)

omit [CharZero k] in
/-- **Garnir full-set annihilation (sorry-free).** The rep-level signed sum over
`S_{A∪B}` annihilates `e_t`.  For every `ρ ∈ C_t` the pigeonhole
(`garnir_row_collision`) supplies a same-row transposition `τ_ρ = swap a b` of
`A ∪ B` labels; `mtab_sum_sign_smul_of_eq_zero` then kills the tabloid family, and
`sum_sign_rep_polytabloid_eq_zero_of_family` lifts it to the polytabloid. -/
theorem garnir_full_annihilation (t : Specht.Tableau μ) {i j : ℕ}
    (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ) :
    ∑ σ ∈ garnirG t i j, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t) = 0 := by
  classical
  refine sum_sign_rep_polytabloid_eq_zero_of_family t (garnirG t i j) (fun ρ => ?_)
  obtain ⟨a, b, hab, haA, hbB, hcollide⟩ :=
    garnir_row_collision t hij hij1 (ρ : Equiv.Perm (Fin (Specht.nOf μ))) ρ.2
  have haU : a ∈ garnirA t i j ∪ garnirB t i j :=
    Finset.mem_union_left _ (by rw [garnirA, Finset.mem_filter]; exact ⟨Finset.mem_univ _, haA⟩)
  have hbU : b ∈ garnirA t i j ∪ garnirB t i j :=
    Finset.mem_union_right _ (by rw [garnirB, Finset.mem_filter]; exact ⟨Finset.mem_univ _, hbB⟩)
  refine mtab_sum_sign_smul_of_eq_zero ((ρ : Equiv.Perm (Fin (Specht.nOf μ))) • t)
    (garnirG t i j) (Equiv.swap a b) (Equiv.swap_mul_self a b) (Equiv.Perm.sign_swap hab) ?_ ?_
  · -- `swap a b` fixes the row pattern of `ρ • t` (it swaps two same-row labels)
    rw [Specht.mem_rowStab]
    funext l
    rw [Specht.arrow_smul_apply, Equiv.symm_swap]
    rcases eq_or_ne l a with rfl | hla
    · rw [Equiv.swap_apply_left]; exact hcollide.symm
    rcases eq_or_ne l b with rfl | hlb
    · rw [Equiv.swap_apply_right]; exact hcollide
    · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
  · -- `garnirG` is closed under right-multiplication by `swap a b`
    intro σ hσ
    simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hσ ⊢
    intro l hl
    rw [Equiv.Perm.mul_apply,
      Equiv.swap_apply_of_ne_of_ne (fun h => hl (by rw [h]; exact haU))
        (fun h => hl (by rw [h]; exact hbU))]
    exact hσ l hl

/-- The Garnir subgroup `H = S_A × S_B`: the elements of `S_{A∪B}` that additionally
preserve every column of `t` (so they permute within `A` and within `B` separately).
Realised as `garnirG ∩ C_t`. -/
def garnirH (t : Specht.Tableau μ) (i j : ℕ) : Finset (Equiv.Perm (Fin (Specht.nOf μ))) :=
  garnirG t i j ∩ Finset.univ.filter (· ∈ Specht.colStab t)

omit [CharZero k] in
/-- `H ⊆ C_t` — every Garnir-subgroup element preserves columns. -/
theorem garnirH_subset_colStab (t : Specht.Tableau μ) (i j : ℕ) :
    ∀ ρ ∈ garnirH t i j, ρ ∈ Specht.colStab t := by
  intro ρ hρ
  rw [garnirH, Finset.mem_inter, Finset.mem_filter] at hρ
  exact hρ.2.2

omit [CharZero k] in
/-- `0 < |H|` — the identity lies in the Garnir subgroup. -/
theorem garnirH_card_pos (t : Specht.Tableau μ) (i j : ℕ) : 0 < (garnirH t i j).card := by
  rw [Finset.card_pos]
  refine ⟨1, ?_⟩
  rw [garnirH, Finset.mem_inter]
  refine ⟨?_, ?_⟩
  · simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and]
    intro l _; rfl
  · rw [Finset.mem_filter]
    exact ⟨Finset.mem_univ _, Subgroup.one_mem _⟩

/-- `S_{A∪B}` as a genuine `Subgroup` (via `fixingSubgroup` of the complement of
`A ∪ B`), for the coset-transversal reindexing that connects `garnir_full_annihilation`
to `garnir_assembly`. -/
def garnirGSub (t : Specht.Tableau μ) (i j : ℕ) : Subgroup (Equiv.Perm (Fin (Specht.nOf μ))) :=
  fixingSubgroup (Equiv.Perm (Fin (Specht.nOf μ)))
    ((↑(garnirA t i j ∪ garnirB t i j) : Set (Fin (Specht.nOf μ)))ᶜ)

omit [CharZero k] in
theorem mem_garnirGSub (t : Specht.Tableau μ) (i j : ℕ)
    (σ : Equiv.Perm (Fin (Specht.nOf μ))) :
    σ ∈ garnirGSub t i j ↔ ∀ l ∉ garnirA t i j ∪ garnirB t i j, σ l = l := by
  rw [garnirGSub, mem_fixingSubgroup_iff]
  constructor
  · intro h l hl
    have := h l (by rw [Set.mem_compl_iff, Finset.mem_coe]; exact hl)
    rwa [Equiv.Perm.smul_def] at this
  · intro h y hy
    rw [Set.mem_compl_iff, Finset.mem_coe] at hy
    rw [Equiv.Perm.smul_def]; exact h y hy

/-- `H = S_A × S_B` as a `Subgroup`: the elements of `garnirGSub` preserving columns. -/
def garnirHSub (t : Specht.Tableau μ) (i j : ℕ) : Subgroup (Equiv.Perm (Fin (Specht.nOf μ))) :=
  garnirGSub t i j ⊓ Specht.colStab t

omit [CharZero k] in
/-- `H ≤ G` at the subgroup level — the input to `exists_left_transversal_of_le`
for the (future) coset-transversal reindexing. -/
theorem garnirHSub_le (t : Specht.Tableau μ) (i j : ℕ) :
    garnirHSub t i j ≤ garnirGSub t i j := inf_le_left

omit [CharZero k] in
/-- The subgroup `garnirGSub`'s carrier equals the `Finset` `garnirG` as sets. -/
theorem garnirGSub_coe (t : Specht.Tableau μ) (i j : ℕ) :
    (garnirGSub t i j : Set (Equiv.Perm (Fin (Specht.nOf μ)))) = ↑(garnirG t i j) := by
  ext σ
  rw [SetLike.mem_coe, mem_garnirGSub, Finset.mem_coe, garnirG, Finset.mem_filter]
  exact ⟨fun h => ⟨Finset.mem_univ _, h⟩, fun h => h.2⟩

omit [CharZero k] in
/-- The subgroup `garnirHSub`'s carrier equals the `Finset` `garnirH` as sets. -/
theorem garnirHSub_coe (t : Specht.Tableau μ) (i j : ℕ) :
    (garnirHSub t i j : Set (Equiv.Perm (Fin (Specht.nOf μ)))) = ↑(garnirH t i j) := by
  ext σ
  rw [SetLike.mem_coe, garnirHSub, Subgroup.mem_inf, Finset.mem_coe, garnirH, Finset.mem_inter,
    garnirG, Finset.mem_filter, Finset.mem_filter, ← mem_garnirGSub]
  exact ⟨fun h => ⟨⟨Finset.mem_univ _, h.1⟩, ⟨Finset.mem_univ _, h.2⟩⟩,
    fun h => ⟨h.1.2, h.2.2⟩⟩

omit [CharZero k] in
/-- **Coset reindexing (sorry-free) — Garnir bridge, reindex step.** For any transversal
`T` whose product family `{π·ρ : π ∈ T, ρ ∈ H}` covers `garnirG` bijectively (encoded by
the two inclusions + the cardinality match), a sum over `garnirG` reindexes as the double
sum `∑_{π∈T} ∑_{ρ∈H}`. Purely `Finset`-level (image + injectivity-from-cardinality); this
turns `garnir_full_annihilation` into `transversal_sum_eq_zero`'s `hann`. -/
theorem sum_over_garnirG_reindex {M : Type*} [AddCommMonoid M] (t : Specht.Tableau μ)
    (i j : ℕ) (T : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (hcover : garnirG t i j ⊆ (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2))
    (hclosed : (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) ⊆ garnirG t i j)
    (hcard : (garnirG t i j).card = (T ×ˢ garnirH t i j).card)
    (F : Equiv.Perm (Fin (Specht.nOf μ)) → M) :
    ∑ σ ∈ garnirG t i j, F σ = ∑ π ∈ T, ∑ ρ ∈ garnirH t i j, F (π * ρ) := by
  classical
  have himg : garnirG t i j = (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) :=
    Finset.Subset.antisymm hcover hclosed
  have hinj := Finset.injOn_of_card_image_eq (f := fun p => p.1 * p.2)
    (s := T ×ˢ garnirH t i j) (by rw [← himg, hcard])
  calc ∑ σ ∈ garnirG t i j, F σ
      = ∑ p ∈ (T ×ˢ garnirH t i j), F (p.1 * p.2) := by
        rw [himg, Finset.sum_image
          (fun a ha b hb => hinj (Finset.mem_coe.mpr ha) (Finset.mem_coe.mpr hb))]
    _ = ∑ π ∈ T, ∑ ρ ∈ garnirH t i j, F (π * ρ) := by rw [Finset.sum_product]

/-! #### The single residual straightening core + the induction skeleton -/

omit [CharZero k] in
/-- **STUB — the residual straightening core, SHARPENED to the column-maximal case
(Sagan §2.6 Garnir relations).**
A polytabloid `e_t` that is *not itself* a standard polytabloid **and** whose tableau
`t` is already **column-(dominance-)maximal** — no column permutation `σ ∈ C_t`
strictly raises the dominance measure `domWeight` (hypothesis `hmax`) — is a
`k`-linear combination of polytabloids of **strictly `domWeight`-greater** tabloids.

This is the *irreducible* combinatorial heart of the straightening algorithm with the
**column-sort already exhausted**: because `hmax` says no column permutation can raise
`domWeight` further, the column-antisymmetry lever `polytabloid_colStab_smul` (proved
above) is spent, and closing this requires a genuine **Garnir coset-sum identity at a
row descent** (Sagan §2.6), whose non-identity coset terms are `±e_{π•t}` with
`domWeight (π•t) > domWeight t`. The general `straightening_step` (below) reduces to
this case sorry-free by splitting on whether a `domWeight`-raising column permutation
exists.

`hmax` is a genuine restriction (a column-maximal `t` is column-standard up to the
row order), so this is an honest sub-case, cited but not vacuous: for a column-maximal
non-standard `t` a row descent between adjacent columns exists and the Garnir relation
yields strictly dominance-greater — hence strictly `domWeight`-greater — terms. -/
theorem straightening_step_colMax (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : Specht.colStab t,
      domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t) ≤ domWeight t) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  -- Ref: [sagan2001] §2.6 (Garnir relations / straightening algorithm). See also
  -- [james1984representation] §8. With the column-sort exhausted (`hmax`: `t` is
  -- column-dominance-maximal), the residual is a pure Garnir coset-sum identity at a
  -- row descent, whose non-identity terms are polytabloids of strictly
  -- dominance-greater (hence `domWeight`-greater) tabloids.
  --
  -- REDUCTION ROADMAP (the algebraic half is already proved sorry-free; only the
  -- combinatorial Garnir-set construction remains). The proved pieces compose as
  --   Garnir set → hfam → `sum_sign_rep_polytabloid_eq_zero_of_family`
  --              → `transversal_sum_eq_zero` → `garnir_assembly` → this goal.
  --
  -- 1. Take the row descent from `exists_row_descent_of_colMax t h hmax`:
  --    cells (i,j),(i,j+1) ∈ μ with `labelAt t hij1 ≤ labelAt t hij`.
  -- 2. Garnir label-sets (as `Finset (Fin (nOf μ))`, via `colPattern`/`rowPattern`):
  --      A := univ.filter (fun l => colPattern t l = j     ∧ i ≤ rowPattern t l)
  --      B := univ.filter (fun l => colPattern t l = j + 1 ∧ rowPattern t l ≤ i)
  --    Disjoint (columns j ≠ j+1). Cardinalities via the labels↔rows bijection in a
  --    column (each column c has one label per row 0..colLen c − 1):
  --      |A| = colLen j − i,  |B| = i + 1  (rows 0..i all in col j+1 since (i,j+1)∈μ),
  --    so |A| + |B| = colLen j + 1.
  -- 3. `H := (S_A × S_B)` as the subgroup of perms supported on A resp. B, and `T` a
  --    left transversal of H in `S_{A∪B}`; both are `⊆ colStab t` for H (A,B live in
  --    single columns), giving `garnir_assembly`'s `1 ∈ T` and
  --    `transversal_sum_eq_zero`'s `hH`, `0 < H.card`.
  -- 4. hfam (the pigeonhole crux, now fully worked out): for every ρ ∈ colStab t set
  --    φ l := rowPattern t (ρ⁻¹ l). φ is injective on A and on B (a column has ≤ 1
  --    label per row, and t is a bijection); φ(A), φ(B) ⊆ {0..colLen j − 1} (φ(B) via
  --    colLen (j+1) ≤ colLen j). Were φ(A) ∩ φ(B) = ∅ they would occupy
  --    |A|+|B| = colLen j + 1 distinct rows inside a colLen j-element set — impossible
  --    (`Finset.exists_ne_map_eq_of_card_lt_of_maps_to`). Hence ∃ a∈A, b∈B with
  --    rowPattern (ρ•t) a = rowPattern (ρ•t) b (`rowPattern_smul`), so
  --    τ_ρ := Equiv.swap a b ∈ rowStab (ρ•t) ∩ S_{A∪B}; feed `mtab_sum_sign_smul_of_eq_zero`
  --    at the tableau ρ•t (G = S_{A∪B} right-τ_ρ-closed) to get hfam ρ.
  -- 5. hdom: each non-identity transversal rep interleaves an A-label (col j, row ≥ i)
  --    with a B-label (col j+1, row ≤ i), a row-raising exchange → `domWeight` strictly
  --    up (the multi-swap generalization of `domWeight_swap_lt`).
  -- Combine: `garnir_assembly t T h1 hdom (transversal_sum_eq_zero t T H hH hpos
  --   (sum_sign_rep_polytabloid_eq_zero_of_family t (S_{A∪B}) hfam |> reindexed))`.
  sorry

omit [CharZero k] in
/-- **Straightening step (Sagan §2.6) — reduced sorry-free to the column-maximal core.**
A polytabloid `e_t` that is *not itself* a standard polytabloid is a `k`-linear
combination of polytabloids of **strictly dominance-greater** tabloids (encoded by the
strictly-monotone measure `domWeight`). From this core, the full spanning half
(`standardPolytabloid_straightening`) follows sorry-free by well-founded induction on
`domBound μ - domWeight t`.

**Reduction (sorry-free half).** Split on whether some column permutation `σ ∈ C_t`
strictly raises `domWeight`:

* **Column-raising** (`∃ σ ∈ C_t, domWeight t < domWeight (σ•t)`) — handled here
  outright by the column-antisymmetry lever `polytabloid_colStab_smul`: since
  `e_{σ•t} = sgn(σ)·e_t` and `sgn(σ)² = 1`, we get `e_t = sgn(σ)·e_{σ•t}`, a
  one-term combination over `{σ•t}`, and `domWeight t < domWeight (σ•t)` is exactly
  the branch hypothesis. No dominance theory needed.
* **Column-maximal** (no such `σ`) — delegated to `straightening_step_colMax`, the
  single sharpened Garnir residual, which now carries the extra hypothesis `hmax`
  that no column permutation raises `domWeight`. -/
theorem straightening_step (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ))) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  by_cases hraise : ∃ σ : Specht.colStab t,
      domWeight t < domWeight ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t)
  · -- Column-raising case: fully proved via column-antisymmetry.
    obtain ⟨σ, hσ⟩ := hraise
    set σ0 : Equiv.Perm (Fin (Specht.nOf μ)) := (σ : Equiv.Perm (Fin (Specht.nOf μ))) with hσ0
    have hmem : σ0 ∈ Specht.colStab t := σ.property
    have hpc : Specht.polytabloid (k := k) (σ0 • t)
        = (Equiv.Perm.sign σ0 : ℤ) • Specht.polytabloid (k := k) t :=
      polytabloid_colStab_smul (k := k) t hmem
    have hs2 : (Equiv.Perm.sign σ0 : ℤ) * (Equiv.Perm.sign σ0 : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign σ0) with h1 | h1 <;> rw [h1] <;> decide
    refine ⟨{σ0 • t}, fun _ => ((Equiv.Perm.sign σ0 : ℤ) : k), ?_, ?_⟩
    · intro t' ht'
      rw [Finset.mem_singleton] at ht'; subst ht'; exact hσ
    · rw [Finset.sum_singleton, hpc,
          ← Int.cast_smul_eq_zsmul k (Equiv.Perm.sign σ0 : ℤ) (Specht.polytabloid (k := k) t),
          smul_smul, ← Int.cast_mul, hs2, Int.cast_one, one_smul]
  · -- Column-maximal case: delegated to the sharpened Garnir residual.
    push_neg at hraise
    exact straightening_step_colMax (k := k) t h hraise

omit [CharZero k] in
/-- **Spanning half — now proved sorry-free MODULO the single core
`straightening_step`.** Every polytabloid `e_t` (arbitrary tableau `t`) lies in the
span of the *standard* polytabloids, by well-founded (strong) induction on the
measure `domBound μ - domWeight t`: if `e_t` is already a standard polytabloid it is
in the spanning set; otherwise `straightening_step` rewrites it over tabloids of
strictly greater `domWeight` (strictly smaller measure), each in the span by the
induction hypothesis, and the span is closed under `k`-linear combinations. -/
theorem standardPolytabloid_straightening :
    ∀ t : Specht.Tableau μ,
      Specht.polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  intro t
  generalize hg : domBound μ - domWeight t = g
  induction g using Nat.strong_induction_on generalizing t with
  | _ g IH =>
    by_cases hr : Specht.polytabloid (k := k) t ∈
        Set.range (standardPolytabloid (k := k) (μ := μ))
    · exact Submodule.subset_span hr
    · obtain ⟨s, c, hgt, heq⟩ := straightening_step (k := k) t hr
      rw [heq]
      refine Submodule.sum_mem _ (fun t' ht' => ?_)
      refine Submodule.smul_mem _ _ ?_
      have hlt : domWeight t < domWeight t' := hgt t' ht'
      have hb : domWeight t' ≤ domBound μ := domWeight_le t'
      exact IH (domBound μ - domWeight t') (by omega) t' rfl

omit [CharZero k] in
/-- **M^μ-level span identity.** The standard polytabloids span exactly `S^μ`
inside `M^μ`. (≤): each standard polytabloid is a polytabloid (`standardPolytabloid_mem`);
(≥): the straightening core. Sorry-free modulo `standardPolytabloid_straightening`. -/
theorem standardPolytabloid_span_eq_specht :
    Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ)))
      = Specht.SpechtSubmodule (k := k) μ := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro _ ⟨T, rfl⟩
    exact standardPolytabloid_mem (k := k) T
  · rw [Specht.SpechtSubmodule, Submodule.span_le, Set.range_subset_iff]
    exact standardPolytabloid_straightening (k := k) (μ := μ)

omit [CharZero k] in
/-- **Content obligation 2/2 — spanning**, now derived **sorry-free modulo the single
core** `standardPolytabloid_straightening` (the M^μ span identity + the corestriction
to `⊤` in `S^μ` are discharged here). Keeps the original name/signature for `Basis.mk`. -/
theorem standardPolytabloid_span :
    Submodule.span k (Set.range (standardPolytabloidS (k := k) (μ := μ))) = ⊤ := by
  apply Submodule.map_injective_of_injective
    (Submodule.injective_subtype (Specht.SpechtSubmodule (k := k) μ))
  rw [Submodule.map_subtype_top, Submodule.map_span, ← Set.range_comp,
      subtype_comp_standardPolytabloidS]
  exact standardPolytabloid_span_eq_specht (k := k) (μ := μ)

end QOU.BraidKnot.SpechtStandardBasis
