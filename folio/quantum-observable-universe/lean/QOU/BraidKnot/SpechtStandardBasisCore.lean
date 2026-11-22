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
| `standardPolytabloid_linearIndependent` | **sorry-free** (via the proved triangular core; declared in `SpechtStandardBasis`) |
| `colStab_smul_self`, `polytabloid_colStab_smul` (column-antisymmetry) | **sorry-free** |
| `domCount'`, `domWeight`, `domBound`, `domCount'_le`, `domWeight_le` (tabloid-dominance measure — **now orphaned**, see note below) | **sorry-free** |
| `cmajSig`, `colWordNum` (the **column-word measure** — validated straightening measure) | **sorry-free** |
| `straightening_step_colMax` (Garnir core, **column-word-minimal case**, on `colWordNum`) | **sorry-free** — row descent + Garnir coset-sum annihilation + `fibre_colWordNum_decrease` |
| `straightening_step` (Garnir straightening core) | **sorry-free** (column-sort dichotomy: the `colWordNum`-lowering branch via `polytabloid_colStab_smul`) |
| `standardPolytabloid_straightening` | **sorry-free** (well-founded induction on `colWordNum`, descending) |
| `standardPolytabloid_span` | **sorry-free** (Garnir relations) |
| `standardBasis` | **sorry-free** (`Basis.mk` wiring) |
| `specht_finrank_eq_numSYT` | **sorry-free** (the reduction) |

The reduction (`standardBasis` + `specht_finrank_eq_numSYT`) is **sorry-free
outright** — both former stubs are now discharged, so it has no `sorry`-tainted
input at all. Machine-checked: `#print axioms` on `specht_finrank_eq_numSYT`,
`specht_finrank_eq_numSYT_wired`, `standardPolytabloid_span`,
`standardPolytabloid_straightening`, `straightening_step_colMax` and
`Triangular.linearIndependent` each yields exactly
`[propext, Classical.choice, Quot.sound]` — no `sorryAx`. The
SYT→tableau conversion **and** the `Fintype` instance brick 1 left open are
*both* proved sorry-free here.

**Spanning half — reduction (this file, §3b).** The spanning stub
`standardPolytabloid_straightening` (every polytabloid `e_t` lies in the span of
the *standard* polytabloids) is **proved sorry-free by well-founded induction** on
the **column-word measure** `colWordNum` (descending), reducing the whole spanning
half to a **single** combinatorial core, `straightening_step`: a *non-standard*
polytabloid is a `k`-combination of polytabloids of strictly `colWordNum`-smaller
tableaux (Sagan §2.6 Garnir relations).

> **Measure correction (2026-07-07).** An earlier version used `domWeight` (a linear
> extension of *tabloid dominance*). That measure is **wrong** for straightening:
> `straightening_step_colMax` stated over it is FALSE (exact-arithmetic disproof,
> μ=(3,2), t=[[1,2,3],[5,4]]; audit §3.5), because Garnir produces terms whose
> tabloids are dominance-*incomparable* to `{t}`. The correct, validated measure is
> the classical **column-reading word** `colWordNum` (every non-identity Garnir term
> is strictly `colWordNum`-smaller — validated exhaustively to (3,3,2)/(4,3,1), audit
> §4.5). The `domWeight` / `domBound` defs are retained but **orphaned** (no longer on
> the spanning path); they remain sorry-free scaffolding.

That core is **proved sorry-free MODULO a still-sharper residual**,
`straightening_step_colMax`, via a **column-sort dichotomy** on whether some column
permutation `σ ∈ C_t` strictly *lowers* `colWordNum`. The `colWordNum`-lowering branch
is discharged outright by the column-antisymmetry lemma `polytabloid_colStab_smul`
(`e_{σ·t} = sgn(σ)·e_t` for `σ ∈ C_t`, proved sorry-free here): since `sgn(σ)² = 1`,
`e_t = sgn(σ)·e_{σ·t}`, a one-term combination whose single term is strictly
`colWordNum`-smaller by the branch hypothesis. What remains is only the
**column-word-minimal** branch (no `σ ∈ C_t` lowers `colWordNum`, i.e. columns are
sorted): the genuine Garnir coset-sum at a row descent, isolated as the residual
`straightening_step_colMax`. Its one open piece is the **column-word-decrease bound**
(every non-identity shuffle-transversal term is `colWordNum`-smaller); the coset-sum
algebra it consumes is already proved sorry-free.

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
index argument; works over any `CommRing`. A natural Mathlib-upstream candidate.

Declared as `Triangular.linearIndependent` (not bare `linearIndependent`) because both
call sites consume it by dot-notation on a `Triangular` term (`htri.linearIndependent`,
in `SpechtStandardBasis` and `SpechtFinrankWired`). The `Triangular.` prefix here is
load-bearing, not a redundant namespace component. -/
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
the Garnir core (`straightening_step_colMax`, proved)
consumes; the pieces still missing on top of it — the coset→polytabloid
antisymmetriser bridge (needs `CharZero k`), the Garnir-set/row-descent existence
for a column-word-minimal non-standard tableau, and the **column-word decrease**
(`colWordNum (π•t) < colWordNum t`; the former `domWeight`-increase claim was FALSE —
audit §3.5) — are recorded in the module docstring. -/
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

/-! #### The column-word measure (validated replacement for `domWeight`)

`domWeight` (a linear extension of *tabloid dominance*) is the WRONG measure for
the straightening induction: `straightening_step_colMax` stated over it is FALSE
(exact-arithmetic disproof, μ=(3,2), t=[[1,2,3],[5,4]]; see
`docs/audits/2026-07-06-garnir-strict-domweight-counterexample.md` §3.5). Garnir
straightening produces terms whose *tabloids are dominance-incomparable* to `{t}`,
so no tabloid-level measure orders them.

The correct measure is the classical **column-reading word** (James Thm 8.4,
Sagan §2.6): read the labels in column-major cell order (column index first, then
row) into a word, compared lexicographically. Encoded as a single `ℕ` (base
`n+1`, first column-major cell most significant), *every* non-identity Garnir
straightening term has strictly smaller `colWordNum` — validated exhaustively to
shape (3,3,2)/(4,3,1) (audit §4.5). The straightening induction runs on this
measure DESCENDING. -/

/-- Column-major **significance exponent** of a cell `c`: the number of `μ`-cells
strictly LATER in column-major order (compare column index first, then row). The
first column-major cell (top of the leftmost column) has the highest exponent. -/
def cmajSig (μ : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (μ.cells.filter (fun c' => c.2 < c'.2 ∨ (c.2 = c'.2 ∧ c.1 < c'.1))).card

/-- The **column-word measure** of a tableau — the validated well-founded measure
for Garnir straightening (replaces the false-for-this-purpose `domWeight`). Reads
the labels in column-major cell order and encodes base `(n+1)` with the first
cell most significant. Every non-identity Garnir straightening term has strictly
smaller `colWordNum`. -/
def colWordNum (t : Specht.Tableau μ) : ℕ :=
  ∑ l : Fin (Specht.nOf μ), (l : ℕ) * (Specht.nOf μ + 1) ^ (cmajSig μ ((t l : ℕ × ℕ)))

/-- **`colWordNum` as a sum over cells (sorry-free).** Reindexing the label-indexed
definition through the tableau bijection `t`: `colWordNum t` is the total of
`(label at cell c) · (n+1)^{cmajSig c}` over all cells `c`. The cell-indexed form is the
natural shape for the "most-significant differing cell" comparison. -/
theorem colWordNum_eq_cellSum (t : Specht.Tableau μ) :
    colWordNum t = ∑ c : μ.cells, ((t.symm c : Fin (Specht.nOf μ)) : ℕ)
        * (Specht.nOf μ + 1) ^ cmajSig μ (c : ℕ × ℕ) := by
  unfold colWordNum
  rw [← Equiv.sum_comp t (fun c : μ.cells =>
      ((t.symm c : Fin (Specht.nOf μ)) : ℕ) * (Specht.nOf μ + 1) ^ cmajSig μ (c : ℕ × ℕ))]
  apply Finset.sum_congr rfl
  intro l _
  rw [Equiv.symm_apply_apply]

/-- **`cmajSig` strict monotonicity (sorry-free).** Within one column (equal column
index), a cell in an EARLIER row is column-major-*before*, hence has strictly larger
`cmajSig` (more cells come after it). The engine of `colWordNum_swap_lt`. -/
theorem cmajSig_lt_of_col_row {c c' : ℕ × ℕ} (hc' : c' ∈ μ.cells)
    (hcol : c.2 = c'.2) (hrow : c.1 < c'.1) :
    cmajSig μ c' < cmajSig μ c := by
  classical
  unfold cmajSig
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · refine ⟨c', ?_, ?_⟩
    · simp only [Finset.mem_filter]; exact ⟨hc', Or.inr ⟨hcol, hrow⟩⟩
    · simp only [Finset.mem_filter, not_and]; intro _; push_neg
      exact ⟨by omega, fun _ => by omega⟩
  · intro x hx
    simp only [Finset.mem_filter] at hx ⊢
    obtain ⟨hxc, hlater⟩ := hx
    refine ⟨hxc, ?_⟩
    rcases hlater with h | ⟨h1, h2⟩
    · left; omega
    · rcases lt_or_eq_of_le (le_of_eq h1.symm) with h | h
      · left; omega
      · right; exact ⟨by omega, by omega⟩

/-- **`cmajSig` strict monotonicity, general column-major order (sorry-free).** If `c` is
column-major-*before* `c'` (lexicographic on `(col, row)`), then `cmajSig c' < cmajSig c`.
Generalises `cmajSig_lt_of_col_row` to cells in different columns. -/
theorem cmajSig_lt_of_before {c c' : ℕ × ℕ} (hc' : c' ∈ μ.cells)
    (hbefore : c.2 < c'.2 ∨ (c.2 = c'.2 ∧ c.1 < c'.1)) :
    cmajSig μ c' < cmajSig μ c := by
  classical
  unfold cmajSig
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · refine ⟨c', ?_, ?_⟩
    · simp only [Finset.mem_filter]; exact ⟨hc', hbefore⟩
    · simp only [Finset.mem_filter, not_and]; intro _
      rintro (h | ⟨_, h⟩) <;> omega
  · intro x hx
    simp only [Finset.mem_filter] at hx ⊢
    obtain ⟨hxc, hlater⟩ := hx
    refine ⟨hxc, ?_⟩
    rcases hbefore with h | ⟨h1, h2⟩ <;> rcases hlater with g | ⟨g1, g2⟩
    · left; omega
    · left; omega
    · left; omega
    · right; exact ⟨by omega, by omega⟩

/-- **`cmajSig` is injective on cells (sorry-free).** Distinct cells have distinct
significance — column-major order is linear, so one cell strictly precedes the other and
has the strictly larger `cmajSig`. Makes `cmajSig` a bijection `μ.cells → {0,…,n-1}`, the
positional index used by the base-`(n+1)` first-difference comparison. -/
theorem cmajSig_injOn : Set.InjOn (cmajSig μ) μ.cells := by
  intro c hc c' hc' heq
  have hcf : c ∈ μ.cells := Finset.mem_coe.mp hc
  have hcf' : c' ∈ μ.cells := Finset.mem_coe.mp hc'
  by_contra hne
  rcases lt_trichotomy c.2 c'.2 with h | h | h
  · exact absurd heq (Nat.ne_of_gt (cmajSig_lt_of_before hcf' (Or.inl h)))
  · rcases lt_trichotomy c.1 c'.1 with h1 | h1 | h1
    · exact absurd heq (Nat.ne_of_gt (cmajSig_lt_of_before hcf' (Or.inr ⟨h, h1⟩)))
    · exact hne (Prod.ext h1 h)
    · exact absurd heq.symm (Nat.ne_of_gt (cmajSig_lt_of_before hcf (Or.inr ⟨h.symm, h1⟩)))
  · exact absurd heq.symm (Nat.ne_of_gt (cmajSig_lt_of_before hcf (Or.inl h)))

/-- **Converse of `cmajSig` monotonicity (sorry-free).** Column-major order is linear, so a
strictly larger `cmajSig` forces the cell column-major-*before*: `cmajSig c₀ < cmajSig c`
gives `c` precedes `c₀` (smaller column, or same column and smaller row). This is what
discharges the `hhigh` hypothesis of `colWordNum_lt_of_first_diff` — "every
higher-significance cell agrees" reduces to "every column-major-earlier cell agrees",
which for the fibre decrease is "cells in columns `< j`, and cells in column `j` above the
first change". -/
theorem before_of_cmajSig_lt {c c₀ : ℕ × ℕ} (hc : c ∈ μ.cells)
    (h : cmajSig μ c₀ < cmajSig μ c) :
    c.2 < c₀.2 ∨ (c.2 = c₀.2 ∧ c.1 < c₀.1) := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨hcol, hrow⟩ := hcon
  rcases lt_trichotomy c.2 c₀.2 with hlt | heqc | hgt
  · exact absurd hlt (not_lt.mpr hcol)
  · rcases lt_trichotomy c.1 c₀.1 with h1 | h1 | h1
    · exact absurd h1 (not_lt.mpr (hrow heqc))
    · exact absurd (Prod.ext h1 heqc ▸ h) (lt_irrefl _)
    · exact absurd (cmajSig_lt_of_before hc (Or.inr ⟨heqc.symm, h1⟩)) (by omega)
  · exact absurd (cmajSig_lt_of_before hc (Or.inl hgt)) (by omega)

/-- Geometric identity over ℕ: `(∑_{x<K} (B-1)·B^x) + 1 = B^K` for `1 ≤ B`. -/
theorem geom_sum_pred (B K : ℕ) (hB : 1 ≤ B) :
    (∑ x ∈ Finset.range K, (B - 1) * B ^ x) + 1 = B ^ K := by
  induction K with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, pow_succ]
    have hb : B - 1 + 1 = B := Nat.sub_add_cancel hB
    have key : (B - 1) * B ^ n + B ^ n = B ^ n * B := by
      have h1 : (B - 1) * B ^ n + B ^ n = (B - 1 + 1) * B ^ n := by ring
      rw [h1, hb]; ring
    omega

/-- **Base-`B` digit bound (sorry-free):** a sum of digits `< B` at DISTINCT positions
`< K` is `< B^K`. The arithmetic core of the "most-significant differing cell"
comparison. -/
theorem geom_digit_bound (B K : ℕ) (hB : 1 ≤ B) (s : Finset ℕ)
    (hs : ∀ x ∈ s, x < K) (d : ℕ → ℕ) (hd : ∀ x, d x < B) :
    ∑ x ∈ s, d x * B ^ x < B ^ K := by
  have hsub : s ⊆ Finset.range K := fun x hx => Finset.mem_range.mpr (hs x hx)
  calc ∑ x ∈ s, d x * B ^ x
      ≤ ∑ x ∈ s, (B - 1) * B ^ x := by
        apply Finset.sum_le_sum
        intro x _
        exact Nat.mul_le_mul_right _ (by have := hd x; omega)
    _ ≤ ∑ x ∈ Finset.range K, (B - 1) * B ^ x :=
        Finset.sum_le_sum_of_subset hsub
    _ < B ^ K := by have := geom_sum_pred B K hB; omega

/-- **Indexed base-`B` digit bound (sorry-free):** distinct positions `e i < K`, digits
`d i < B` ⇒ `∑ d i·B^{e i} < B^K`. The form the cell-indexed first-difference comparison
consumes (`e = cmajSig`, `d =` label). -/
theorem digit_bound_indexed {ι : Type*} (B K : ℕ) (hB : 1 ≤ B) (s : Finset ι)
    (e : ι → ℕ) (hinj : Set.InjOn e s) (he : ∀ i ∈ s, e i < K)
    (d : ι → ℕ) (hd : ∀ i, d i < B) :
    ∑ i ∈ s, d i * B ^ e i < B ^ K := by
  classical
  have h1 : ∑ i ∈ s, d i * B ^ e i ≤ ∑ i ∈ s, (B - 1) * B ^ e i := by
    apply Finset.sum_le_sum; intro i _
    exact Nat.mul_le_mul_right _ (by have := hd i; omega)
  have h3 : ∑ i ∈ s, B ^ e i = ∑ x ∈ s.image e, B ^ x := by
    rw [Finset.sum_image
      (fun a ha b hb hab => hinj (Finset.mem_coe.mpr ha) (Finset.mem_coe.mpr hb) hab)]
  have h4 : s.image e ⊆ Finset.range K := by
    intro x hx; rw [Finset.mem_image] at hx; obtain ⟨i, hi, rfl⟩ := hx
    exact Finset.mem_range.mpr (he i hi)
  calc ∑ i ∈ s, d i * B ^ e i
      ≤ ∑ i ∈ s, (B - 1) * B ^ e i := h1
    _ = (B - 1) * ∑ i ∈ s, B ^ e i := by rw [Finset.mul_sum]
    _ = (B - 1) * ∑ x ∈ s.image e, B ^ x := by rw [h3]
    _ ≤ (B - 1) * ∑ x ∈ Finset.range K, B ^ x :=
        Nat.mul_le_mul_left _ (Finset.sum_le_sum_of_subset h4)
    _ < B ^ K := by have hg := geom_sum_pred B K hB; rw [Finset.mul_sum]; omega

/-- `#{i : Fin n | (i:ℕ) ≤ m} = m + 1` for `m < n` (sorry-free). -/
theorem card_fin_le (n m : ℕ) (hm : m < n) :
    (Finset.univ.filter (fun i : Fin n => (i : ℕ) ≤ m)).card = m + 1 := by
  rw [← Finset.card_image_of_injective _ Fin.val_injective]
  have : (Finset.univ.filter (fun i : Fin n => (i : ℕ) ≤ m)).image Fin.val
      = Finset.range (m + 1) := by
    ext k
    simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_range]
    constructor
    · rintro ⟨i, hi, rfl⟩; omega
    · intro hk; exact ⟨⟨k, by omega⟩, show k ≤ m by omega, rfl⟩
  rw [this, Finset.card_range]

/-- `#{i : Fin n | (i:ℕ) < m} = m` for `m ≤ n` (sorry-free). -/
theorem card_fin_lt (n m : ℕ) (hm : m ≤ n) :
    (Finset.univ.filter (fun i : Fin n => (i : ℕ) < m)).card = m := by
  rw [← Finset.card_image_of_injective _ Fin.val_injective]
  have : (Finset.univ.filter (fun i : Fin n => (i : ℕ) < m)).image Fin.val
      = Finset.range m := by
    ext k
    simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_range]
    constructor
    · rintro ⟨i, hi, rfl⟩; omega
    · intro hk; exact ⟨⟨k, by omega⟩, hk, rfl⟩
  rw [this, Finset.card_range]

/-- **Order-statistic domination (sorry-free).** If for every threshold `w` the finset `X`
has at least as many elements `≤ w` as `Y`, then `X`'s `r`-th smallest is `≤` `Y`'s `r`-th
smallest (`orderEmbOfFin` = the increasing enumeration). The order-theoretic core of the
fibre-decrease: `B < A` makes `A` the top-`|A|` subset, so its column content dominates. -/
theorem orderStat_le_of_count_ge {X Y : Finset ℕ} (h : X.card = Y.card)
    (hcount : ∀ w, (Y.filter (· ≤ w)).card ≤ (X.filter (· ≤ w)).card)
    (r : Fin X.card) :
    X.orderEmbOfFin rfl r ≤ Y.orderEmbOfFin h.symm r := by
  classical
  set v := Y.orderEmbOfFin h.symm r with hv
  have hYcount : (r : ℕ) + 1 ≤ (Y.filter (· ≤ v)).card := by
    have hsub : (Finset.univ.filter (fun i : Fin X.card => (i : ℕ) ≤ (r:ℕ))).image
          (Y.orderEmbOfFin h.symm) ⊆ Y.filter (· ≤ v) := by
      intro y hy
      rw [Finset.mem_image] at hy
      obtain ⟨i, hi, rfl⟩ := hy
      rw [Finset.mem_filter] at hi ⊢
      refine ⟨Finset.orderEmbOfFin_mem _ _ _, ?_⟩
      rw [hv]; exact (Y.orderEmbOfFin h.symm).monotone hi.2
    calc (r : ℕ) + 1 = (Finset.univ.filter (fun i : Fin X.card => (i : ℕ) ≤ (r:ℕ))).card :=
              (card_fin_le X.card r r.2).symm
        _ = _ := (Finset.card_image_of_injective _ (Y.orderEmbOfFin h.symm).injective).symm
        _ ≤ _ := Finset.card_le_card hsub
  have hXcount : (r : ℕ) + 1 ≤ (X.filter (· ≤ v)).card := le_trans hYcount (hcount v)
  by_contra hlt
  push_neg at hlt
  have hbad : (X.filter (· ≤ v)).card ≤ (r : ℕ) := by
    have hsub : X.filter (· ≤ v) ⊆
        (Finset.univ.filter (fun i : Fin X.card => (i:ℕ) < (r:ℕ))).image (X.orderEmbOfFin rfl) := by
      intro x hx
      rw [Finset.mem_filter] at hx
      obtain ⟨i, rfl⟩ : ∃ i, X.orderEmbOfFin rfl i = x := by
        have hxc : x ∈ (X : Set ℕ) := Finset.mem_coe.mpr hx.1
        rw [← Finset.range_orderEmbOfFin X rfl] at hxc
        exact hxc
      rw [Finset.mem_image]
      refine ⟨i, ?_, rfl⟩
      rw [Finset.mem_filter]
      refine ⟨Finset.mem_univ _, ?_⟩
      by_contra hge; push_neg at hge
      have : v < X.orderEmbOfFin rfl i :=
        lt_of_lt_of_le hlt ((X.orderEmbOfFin rfl).monotone hge)
      exact absurd hx.2 (not_le.mpr this)
    calc (X.filter (· ≤ v)).card ≤ _ := Finset.card_le_card hsub
      _ ≤ (Finset.univ.filter (fun i : Fin X.card => (i:ℕ) < (r:ℕ))).card := Finset.card_image_le
      _ = (r : ℕ) := card_fin_lt X.card r (le_of_lt r.2)
  omega

/-- **`orderEmbOfFin` value is independent of the cardinality proof / index type
(sorry-free).** For a fixed finset `s`, `s.orderEmbOfFin` at two indices with the same
`ℕ`-value agrees — the increasing enumeration only depends on `s` and the position, not on
which `s.card = k` proof presents the domain `Fin k`. Bridges `orderStat_le_of_count_ge`'s
`Fin X.card` indexing to `labelAt_eq_orderStat`'s `Fin (colLen j)` indexing. -/
theorem orderEmbOfFin_congr {s : Finset ℕ} {k k' : ℕ} (hk : s.card = k) (hk' : s.card = k')
    (i : Fin k) (i' : Fin k') (hii : (i : ℕ) = (i' : ℕ)) :
    s.orderEmbOfFin hk i = s.orderEmbOfFin hk' i' := by
  subst hk; subst hk'
  exact congrArg (⇑(s.orderEmbOfFin rfl)) (Fin.ext hii)

/-- **Order-statistic domination, common-`k` form (sorry-free).** `orderStat_le_of_count_ge`
restated with both finsets carrying a card proof to the *same* `k`, so the index `r : Fin k`
matches on both sides — the shape `labelAt_eq_orderStat` produces (`Fin (μ.colLen j)`). -/
theorem orderEmbOfFin_le_of_count {X Y : Finset ℕ} {k : ℕ} (hX : X.card = k) (hY : Y.card = k)
    (hcount : ∀ w, (Y.filter (· ≤ w)).card ≤ (X.filter (· ≤ w)).card) (r : Fin k) :
    X.orderEmbOfFin hX r ≤ Y.orderEmbOfFin hY r := by
  have hXY : X.card = Y.card := by rw [hX, hY]
  have key := orderStat_le_of_count_ge hXY hcount (Fin.cast hX.symm r)
  rw [orderEmbOfFin_congr rfl hX (Fin.cast hX.symm r) r (by simp),
      orderEmbOfFin_congr hXY.symm hY (Fin.cast hX.symm r) r (by simp)] at key
  exact key

/-- **Count-domination from the top-`|A|` structure (sorry-free).** If `A` is "above" `B`
(every `b ∈ B` is below every `a ∈ A`) and `S ⊆ A ∪ B` has `|S| = |A|`, then for every
threshold `w` the top set `A` has no more elements `≤ w` than `S`. Feeds
`orderStat_le_of_count_ge`: a Garnir fibre's column-`j` content `S` (a different `|A|`-subset
of `A∪B`) sorted-dominates `t`'s content `A`, because `B < A` makes `A` the top subset. -/
theorem count_dom_of_top {A B S : Finset ℕ} (hBA : ∀ b ∈ B, ∀ a ∈ A, b < a)
    (hS : S ⊆ A ∪ B) (hcard : S.card = A.card) (w : ℕ) :
    (A.filter (· ≤ w)).card ≤ (S.filter (· ≤ w)).card := by
  classical
  have hgt : (S.filter (fun x => w < x)).card ≤ (A.filter (fun x => w < x)).card := by
    by_cases hb : ∃ b ∈ B, w < b
    · obtain ⟨b, hbB, hwb⟩ := hb
      have hAall : A.filter (fun x => w < x) = A := by
        apply Finset.filter_true_of_mem
        intro a ha; exact lt_trans hwb (hBA b hbB a ha)
      rw [hAall]
      calc (S.filter (fun x => w < x)).card ≤ S.card := Finset.card_filter_le _ _
        _ = A.card := hcard
    · push_neg at hb
      apply Finset.card_le_card
      intro x hx
      rw [Finset.mem_filter] at hx ⊢
      obtain ⟨hxS, hxw⟩ := hx
      have hxAB := hS hxS
      rw [Finset.mem_union] at hxAB
      rcases hxAB with hxA | hxB
      · exact ⟨hxA, hxw⟩
      · exact absurd hxw (not_lt.mpr (hb x hxB))
  have hAeq := Finset.filter_card_add_filter_neg_card_eq_card (s := A) (p := (· ≤ w))
  have hSeq := Finset.filter_card_add_filter_neg_card_eq_card (s := S) (p := (· ≤ w))
  have hAneg : (A.filter (fun x => ¬ x ≤ w)).card = (A.filter (fun x => w < x)).card := by
    congr 1; apply Finset.filter_congr; intro x _; simp [not_le]
  have hSneg : (S.filter (fun x => ¬ x ≤ w)).card = (S.filter (fun x => w < x)).card := by
    congr 1; apply Finset.filter_congr; intro x _; simp [not_le]
  omega

/-- **Count-domination is preserved by adding a common disjoint part (sorry-free).** If `X`
is count-dominated by `Y` (`≤ w` counts) and `P` is disjoint from both, then `P ∪ X` is
count-dominated by `P ∪ Y`. For the fibre decrease `P` is column `j`'s labels above the
descent row (fixed by the Garnir element), `X = A` (top-`|A|`), `Y = S = π(A)`. -/
theorem filter_le_card_union_mono {P X Y : Finset ℕ}
    (hPX : Disjoint P X) (hPY : Disjoint P Y)
    (hXY : ∀ w, (X.filter (· ≤ w)).card ≤ (Y.filter (· ≤ w)).card) (w : ℕ) :
    ((P ∪ X).filter (· ≤ w)).card ≤ ((P ∪ Y).filter (· ≤ w)).card := by
  classical
  have hX : ((P ∪ X).filter (· ≤ w)).card
      = (P.filter (· ≤ w)).card + (X.filter (· ≤ w)).card := by
    rw [Finset.filter_union, Finset.card_union_of_disjoint
      (hPX.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _))]
  have hY : ((P ∪ Y).filter (· ≤ w)).card
      = (P.filter (· ≤ w)).card + (Y.filter (· ≤ w)).card := by
    rw [Finset.filter_union, Finset.card_union_of_disjoint
      (hPY.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _))]
  rw [hX, hY]; exact Nat.add_le_add_left (hXY w) _

/-- **First strict index of a pointwise-`≤`, unequal pair (sorry-free).** If `f ≤ g`
pointwise on `Fin N` and `f ≠ g`, there is a *least* index `r₀` with `f r₀ < g r₀`, below
which `f` and `g` agree. Supplies `colWordNum_lt_of_first_diff_col`'s cell `c₀` (the
top-most changed row of the Garnir column) together with its `habove` (agreement above). -/
theorem exists_first_lt_of_le_of_ne {N : ℕ} (f g : Fin N → ℕ)
    (hle : ∀ r, f r ≤ g r) (hne : f ≠ g) :
    ∃ r₀ : Fin N, f r₀ < g r₀ ∧ ∀ r : Fin N, r < r₀ → f r = g r := by
  classical
  have hne' : ∃ r, f r < g r := by
    by_contra h
    push_neg at h
    exact hne (funext fun r => le_antisymm (hle r) (h r))
  set S := Finset.univ.filter (fun r : Fin N => f r < g r)
  have hSne : S.Nonempty := by
    obtain ⟨r, hr⟩ := hne'
    exact ⟨r, Finset.mem_filter.mpr ⟨Finset.mem_univ _, hr⟩⟩
  refine ⟨S.min' hSne, ?_, ?_⟩
  · exact (Finset.mem_filter.mp (S.min'_mem hSne)).2
  · intro r hr
    have hrnot : r ∉ S := fun hrS => absurd (S.min'_le r hrS) (not_le.mpr hr)
    have hnlt : ¬ (f r < g r) :=
      fun hlt => hrnot (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hlt⟩)
    exact le_antisymm (hle r) (not_lt.mp hnlt)

/-- **First-difference comparison for `colWordNum` (sorry-free).** If `u` and `v` agree
(as labels) on every cell column-major-*earlier* than a cell `c₀` (i.e. `cmajSig` strictly
larger), and `v` has a strictly smaller label at `c₀`, then `colWordNum v < colWordNum u`.
This is the base-`(n+1)` "most-significant differing digit decides" principle, with
`cmajSig` as the positional index. -/
theorem colWordNum_lt_of_first_diff (u v : Specht.Tableau μ) (c₀ : μ.cells)
    (hhigh : ∀ c : μ.cells, cmajSig μ (c₀ : ℕ × ℕ) < cmajSig μ (c : ℕ × ℕ) →
        ((u.symm c : Fin (Specht.nOf μ)) : ℕ) = ((v.symm c : Fin (Specht.nOf μ)) : ℕ))
    (hlt : ((v.symm c₀ : Fin (Specht.nOf μ)) : ℕ) < ((u.symm c₀ : Fin (Specht.nOf μ)) : ℕ)) :
    colWordNum v < colWordNum u := by
  classical
  set B := Specht.nOf μ + 1 with hB
  set K := cmajSig μ (c₀ : ℕ × ℕ) with hK
  set gu : μ.cells → ℕ :=
    fun c => ((u.symm c : Fin (Specht.nOf μ)) : ℕ) * B ^ cmajSig μ (c : ℕ × ℕ) with hgu
  set gv : μ.cells → ℕ :=
    fun c => ((v.symm c : Fin (Specht.nOf μ)) : ℕ) * B ^ cmajSig μ (c : ℕ × ℕ) with hgv
  rw [colWordNum_eq_cellSum u, colWordNum_eq_cellSum v]
  -- the predicate splitting cells: strictly higher significance than c₀
  set p : μ.cells → Prop := fun c => K < cmajSig μ (c : ℕ × ℕ) with hp
  -- high parts agree
  have hhi : ∑ c ∈ Finset.univ.filter p, gv c = ∑ c ∈ Finset.univ.filter p, gu c := by
    apply Finset.sum_congr rfl
    intro c hc
    rw [Finset.mem_filter] at hc
    simp only [hgu, hgv]
    rw [hhigh c hc.2]
  -- low part: split off c₀
  have hc0mem : c₀ ∈ Finset.univ.filter (fun c => ¬ p c) := by
    rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, by rw [hp]; simp [hK]⟩
  -- the erased low set has strictly smaller significance
  set T := (Finset.univ.filter (fun c => ¬ p c)).erase c₀ with hT
  have hTlt : ∀ c ∈ T, cmajSig μ (c : ℕ × ℕ) < K := by
    intro c hc
    rw [hT, Finset.mem_erase, Finset.mem_filter] at hc
    obtain ⟨hcne, _, hcp⟩ := hc
    rw [hp] at hcp; push_neg at hcp
    rcases lt_or_eq_of_le hcp with h | h
    · exact h
    · exfalso; apply hcne
      have : (c : ℕ × ℕ) = (c₀ : ℕ × ℕ) :=
        cmajSig_injOn (Finset.mem_coe.mpr c.2) (Finset.mem_coe.mpr c₀.2) (by rw [h, hK])
      exact Subtype.ext this
  have hTinj : Set.InjOn (fun c : μ.cells => cmajSig μ (c : ℕ × ℕ)) T := by
    intro c _ c' _ heq
    exact Subtype.ext (cmajSig_injOn (Finset.mem_coe.mpr c.2) (Finset.mem_coe.mpr c'.2) heq)
  -- digit bounds on the erased tails
  have hRu : ∑ c ∈ T, gu c < B ^ K :=
    digit_bound_indexed B K (by omega) T (fun c => cmajSig μ (c : ℕ × ℕ)) hTinj hTlt
      (fun c => ((u.symm c : Fin (Specht.nOf μ)) : ℕ)) (fun c => by
        show ((u.symm c : Fin (Specht.nOf μ)) : ℕ) < B
        have := (u.symm c).isLt; rw [hB]; omega)
  have hRv : ∑ c ∈ T, gv c < B ^ K :=
    digit_bound_indexed B K (by omega) T (fun c => cmajSig μ (c : ℕ × ℕ)) hTinj hTlt
      (fun c => ((v.symm c : Fin (Specht.nOf μ)) : ℕ)) (fun c => by
        show ((v.symm c : Fin (Specht.nOf μ)) : ℕ) < B
        have := (v.symm c).isLt; rw [hB]; omega)
  -- assemble each side: Σ = high + (c₀ term + tail)
  have hsplit : ∀ g : μ.cells → ℕ, ∑ c, g c
      = (∑ c ∈ Finset.univ.filter p, g c) + (g c₀ + ∑ c ∈ T, g c) := by
    intro g
    rw [← Finset.sum_filter_add_sum_filter_not Finset.univ p g, hT,
        Finset.add_sum_erase _ g hc0mem]
  rw [hsplit gu, hsplit gv, hhi]
  -- reduce to the low parts
  have hc0u : gu c₀ = ((u.symm c₀ : Fin (Specht.nOf μ)) : ℕ) * B ^ K := by rw [hgu, hK]
  have hc0v : gv c₀ = ((v.symm c₀ : Fin (Specht.nOf μ)) : ℕ) * B ^ K := by rw [hgv, hK]
  have hkey : gv c₀ + ∑ c ∈ T, gv c < gu c₀ + ∑ c ∈ T, gu c := by
    rw [hc0u, hc0v]
    set a := ((v.symm c₀ : Fin (Specht.nOf μ)) : ℕ) with ha
    set b := ((u.symm c₀ : Fin (Specht.nOf μ)) : ℕ) with hbb
    set M := B ^ K with hM
    have h1 : a + 1 ≤ b := hlt
    have e2 : a * M + M ≤ b * M := by
      have e1 : (a + 1) * M = a * M + M := by ring
      rw [← e1]; exact Nat.mul_le_mul_right _ h1
    have hv : ∑ c ∈ T, gv c < M := hRv
    omega
  omega

omit [CharZero k] in
/-- **First-difference comparison in geometric (column-major) terms (sorry-free).** The
`colWordNum_lt_of_first_diff` `hhigh` hypothesis, restated via `before_of_cmajSig_lt` in the
two geometric conditions the fibre decrease actually supplies: `u` and `v` agree on every
cell in a column strictly **left** of `c₀`'s column, and on every cell in `c₀`'s column
**above** `c₀`; and `v` has a strictly smaller label at `c₀`. Then `colWordNum v <
colWordNum u`. For the Garnir fibre decrease `c₀` is the top-most cell of column `j` whose
label changes; columns `< j` are untouched and column `j` above `c₀` is unchanged. -/
theorem colWordNum_lt_of_first_diff_col (u v : Specht.Tableau μ) (c₀ : μ.cells)
    (hleft : ∀ c : μ.cells, (c : ℕ × ℕ).2 < (c₀ : ℕ × ℕ).2 →
        ((u.symm c : Fin (Specht.nOf μ)) : ℕ) = ((v.symm c : Fin (Specht.nOf μ)) : ℕ))
    (habove : ∀ c : μ.cells, (c : ℕ × ℕ).2 = (c₀ : ℕ × ℕ).2 → (c : ℕ × ℕ).1 < (c₀ : ℕ × ℕ).1 →
        ((u.symm c : Fin (Specht.nOf μ)) : ℕ) = ((v.symm c : Fin (Specht.nOf μ)) : ℕ))
    (hlt : ((v.symm c₀ : Fin (Specht.nOf μ)) : ℕ) < ((u.symm c₀ : Fin (Specht.nOf μ)) : ℕ)) :
    colWordNum v < colWordNum u := by
  apply colWordNum_lt_of_first_diff u v c₀
  · intro c hc
    rcases before_of_cmajSig_lt c.2 hc with hcol | ⟨hcol, hrow⟩
    · exact hleft c hcol
    · exact habove c hcol hrow
  · exact hlt

/-- **Keystone (sorry-free): a within-column descent swap strictly lowers `colWordNum`.**
If labels `a < b` sit in the same column with `b` in an EARLIER row than `a` (a column
descent — the larger label higher up), swapping them strictly decreases the column-word
measure. This is the `colWordNum` analogue of `domWeight_swap_lt`, and the lever the
`straightening_step` column-lowering branch and the `colMax` row-descent argument will
consume. Proof: `cmajSig (t a) < cmajSig (t b)` (same column, `b` higher) gives
`w a < w b` with `w m = (n+1)^{cmajSig (t m)}`; reindexing the swapped sum leaves only the
`a,b` terms, and `b·w a + a·w b < a·w a + b·w b` is the rearrangement inequality. -/
theorem colWordNum_swap_lt (t : Specht.Tableau μ) {a b : Fin (Specht.nOf μ)}
    (hab : (a : ℕ) < (b : ℕ))
    (hcol : Specht.colPattern t a = Specht.colPattern t b)
    (hrow : Specht.rowPattern t b < Specht.rowPattern t a) :
    colWordNum (Equiv.swap a b • t) < colWordNum t := by
  classical
  have hne : a ≠ b := fun h => (Nat.ne_of_lt hab) (by rw [h])
  set B := Specht.nOf μ + 1 with hB
  set w : Fin (Specht.nOf μ) → ℕ := fun m => B ^ (cmajSig μ ((t m : ℕ × ℕ))) with hw
  have hsig : cmajSig μ ((t a : ℕ × ℕ)) < cmajSig μ ((t b : ℕ × ℕ)) := by
    apply cmajSig_lt_of_col_row (c := ((t b : ℕ × ℕ))) (c' := ((t a : ℕ × ℕ))) (t a).property
    · exact hcol.symm
    · exact hrow
  have hwab : w a < w b := by rw [hw]; exact Nat.pow_lt_pow_right (by omega) hsig
  have hreindex : colWordNum (Equiv.swap a b • t)
      = ∑ m : Fin (Specht.nOf μ), ((Equiv.swap a b m : Fin (Specht.nOf μ)) : ℕ) * w m := by
    unfold colWordNum
    rw [← Equiv.sum_comp (Equiv.swap a b)
          (fun m => ((Equiv.swap a b m : Fin (Specht.nOf μ)) : ℕ) * w m)]
    apply Finset.sum_congr rfl
    intro l _
    rw [Equiv.swap_apply_self, hw]
    congr 2
  have hct : colWordNum t = ∑ m : Fin (Specht.nOf μ), (m : ℕ) * w m := by
    unfold colWordNum; rw [hw]
  rw [hreindex, hct]
  have hbmem : b ∈ Finset.univ.erase a := Finset.mem_erase.mpr ⟨hne.symm, Finset.mem_univ b⟩
  have key : ∀ (g : Fin (Specht.nOf μ) → ℕ),
      ∑ m, g m = g a + (g b + ∑ m ∈ (Finset.univ.erase a).erase b, g m) := by
    intro g
    rw [← Finset.add_sum_erase Finset.univ g (Finset.mem_univ a),
        ← Finset.add_sum_erase (Finset.univ.erase a) g hbmem]
  rw [key (fun m => ((Equiv.swap a b m : Fin (Specht.nOf μ)) : ℕ) * w m),
      key (fun m => (m : ℕ) * w m)]
  have htail : ∑ m ∈ (Finset.univ.erase a).erase b,
        ((Equiv.swap a b m : Fin (Specht.nOf μ)) : ℕ) * w m
      = ∑ m ∈ (Finset.univ.erase a).erase b, (m : ℕ) * w m := by
    apply Finset.sum_congr rfl
    intro m hm
    have hma : m ≠ a := (Finset.mem_erase.mp (Finset.mem_of_mem_erase hm)).1
    have hmb : m ≠ b := (Finset.mem_erase.mp hm).1
    rw [Equiv.swap_apply_of_ne_of_ne hma hmb]
  rw [htail, Equiv.swap_apply_left, Equiv.swap_apply_right]
  have hcore : (b : ℕ) * w a + (a : ℕ) * w b < (a : ℕ) * w a + (b : ℕ) * w b := by
    nlinarith [hab, hwab, Nat.zero_le (w a), Nat.zero_le (w b)]
  omega

/-- **Column stabiliser is invariant under its own action (sorry-free).** If
`σ ∈ C_s` (preserves `s`'s columns), then `σ • s` has the *same* column pattern as `s`,
so `C_{σ•s} = C_s`. Used to compose column permutations while sorting. -/
theorem colStab_smul_eq (s : Specht.Tableau μ)
    {σ : Equiv.Perm (Fin (Specht.nOf μ))} (hσ : σ ∈ Specht.colStab s) :
    Specht.colStab (σ • s) = Specht.colStab s := by
  have h : Specht.colPattern (σ • s) = Specht.colPattern s := by
    rw [Specht.colPattern_smul]; exact Specht.mem_colStab.mp hσ
  unfold Specht.colStab; rw [h]

/-- **Existence of a column-word-minimal form (sorry-free) — the `colsort` substitute.**
Every tableau `s` has a column permutation `ρ ∈ C_s` for which `ρ • s` is
**column-word-minimal** (no `C_{ρ•s}` element lowers `colWordNum`) and
`colWordNum (ρ • s) ≤ colWordNum s`. Since `ρ ∈ C_s`, `ρ • s` has the same
column-membership as `s` and `e_{ρ•s} = ±e_s` (column antisymmetry). This replaces an
explicit `colsort` **operation**: the sorted form is obtained by well-founded descent —
if `s` is not already minimal, some `C_s`-element strictly lowers `colWordNum`, and the
induction hypothesis (strong induction on `colWordNum s`) supplies the minimal form of
that smaller tableau; column stabilisers compose via `colStab_smul_eq`. -/
theorem exists_colWordMin_form (s : Specht.Tableau μ) :
    ∃ ρ : Equiv.Perm (Fin (Specht.nOf μ)), ρ ∈ Specht.colStab s ∧
      colWordNum (ρ • s) ≤ colWordNum s ∧
      (∀ σ : Equiv.Perm (Fin (Specht.nOf μ)),
        σ ∈ Specht.colStab (ρ • s) → colWordNum (ρ • s) ≤ colWordNum (σ • (ρ • s))) := by
  classical
  generalize hn : colWordNum s = n
  induction n using Nat.strong_induction_on generalizing s with
  | _ n IH =>
    by_cases hmin : ∀ σ : Equiv.Perm (Fin (Specht.nOf μ)),
        σ ∈ Specht.colStab s → colWordNum s ≤ colWordNum (σ • s)
    · refine ⟨1, Subgroup.one_mem _, ?_, ?_⟩
      · rw [one_smul]; exact hn.le
      · intro σ hσ
        simp only [one_smul] at hσ ⊢
        exact hmin σ hσ
    · push_neg at hmin
      obtain ⟨σ, hσmem, hσlt⟩ := hmin
      obtain ⟨ρ', hρ'mem, hρ'le, hρ'min⟩ := IH (colWordNum (σ • s)) (by omega) (σ • s) rfl
      have hcs : Specht.colStab (σ • s) = Specht.colStab s := colStab_smul_eq s hσmem
      refine ⟨ρ' * σ, ?_, ?_, ?_⟩
      · rw [hcs] at hρ'mem; exact Subgroup.mul_mem _ hρ'mem hσmem
      · rw [mul_smul]
        exact le_trans hρ'le (le_of_lt (hn ▸ hσlt))
      · intro τ hτ
        rw [mul_smul] at hτ ⊢
        exact hρ'min τ hτ

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
`(0,0), …, (i,0)` lie in `ν` by down-closure). Single copy — downstream
`SpechtDominanceCore` resolves to this declaration through its
`open QOU.BraidKnot.SpechtStandardBasis`. -/
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

/-- The row pattern of a tableau is bounded by `nOf μ`. Single copy (see
`row_lt_card`); serves `SpechtDominanceCore` through its `open`. -/
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

/-- **Column-standardness under column-word-minimality (sorry-free) — the `colWordNum`
analogue of `colStandard_of_colMax`.** If `t` is column-word-minimal (`hmax`: no
`σ ∈ C_t` *lowers* `colWordNum`), then each column's labels strictly increase with the
row. A violation (`↑a < ↑b` same column but `rowPattern t b < rowPattern t a`) would be a
column descent, giving a `colWordNum`-*lowering* transposition (`colStab_swap_mem` +
`colWordNum_swap_lt`) that contradicts `hmax`. -/
theorem colStandard_of_colWordMin (t : Specht.Tableau μ)
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t))
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
      (not_le.mpr (colWordNum_swap_lt t hab hcol h))

omit [CharZero k] in
/-- **Pure row-descent existence under column-word-minimality (sorry-free) — the
`colWordNum` analogue of `exists_row_descent_of_colMax`.** A column-word-minimal `t`
whose polytabloid is non-standard has a **row descent** (column descents are killed by
`colStandard_of_colWordMin`). This is the row descent the `colWordNum` Garnir coset-sum
step of `straightening_step_colMax` consumes. -/
theorem exists_row_descent_of_colWordMin (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t)) :
    ∃ i j, ∃ (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ), labelAt t hij1 ≤ labelAt t hij := by
  rcases exists_descent_of_not_mem_range (k := k) t h with hrow | hcol
  · exact hrow
  · exfalso
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
    have hrow := colStandard_of_colWordMin t hmax hcolab hab
    rw [show Specht.rowPattern t a = i + 1 from by show (t a : ℕ × ℕ).1 = i + 1; rw [hta],
        show Specht.rowPattern t b = i from by show (t b : ℕ × ℕ).1 = i; rw [htb]] at hrow
    omega

omit [CharZero k] in
/-- **Garnir assembly (sorry-free) — the `domWeight`-era bookkeeping helper.**
Given a transversal `T ∋ π₀` for which (i) the signed representation sum vanishes
(`hann` — the output of `transversal_sum_eq_zero`), and (ii) every *non-distinguished*
representative `π` strictly raises the dominance measure
(`hdom : domWeight t < domWeight (π • t)`), the polytabloid `e_t` is a `k`-linear
combination of polytabloids of strictly `domWeight`-greater tabloids.

Pure bookkeeping: isolate the distinguished term `sgn(π₀)·(π₀·e_t) = ±e_t` from `hann`,
giving `e_t = ∑_{π ∈ T, π ≠ π₀} (−sgn π)·e_{π·t}` (via equivariance
`polytabloid_rep_smul`), then reindex the permutation sum to a sum over the tableaux
`{π·t}` with fibrewise-aggregated coefficients.

**Orphaned by the 2026-07-07 measure correction.** `straightening_step_colMax` has been
restated over `colWordNum` (the `domWeight` version was FALSE — audit §3.5), so this
`domWeight`-based assembly is NO LONGER on the straightening path and does not close the
current `colMax`. It is retained sorry-free (parallel to the orphaned `domWeight`/
`domBound` scaffolding); the `colWordNum` colMax will want an analogous assembly whose
`hdom` reads `colWordNum (π • t) < colWordNum t`. The *reindexing* argument here (identity
isolation → `sum_image` fibre-aggregation) is measure-agnostic and transcribes directly. -/
theorem garnir_assembly (t : Specht.Tableau μ)
    (T : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (π₀ : Equiv.Perm (Fin (Specht.nOf μ))) (hπ₀ : π₀ ∈ T)
    (hfix : Specht.Mtab.rep μ π₀ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign π₀ : ℤ) • Specht.polytabloid (k := k) t)
    (hdom : ∀ π ∈ T, π ≠ π₀ →
      domWeight t < domWeight ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hann : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) = 0) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, domWeight t < domWeight t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  -- Abbreviations: the non-identity part of the transversal, and the coefficient sum.
  set E := T.erase π₀ with hE
  -- Isolate the distinguished term of `hann`: `e_t + ∑_{π ∈ E} sgn(π)·(π·e_t) = 0`.
  rw [← Finset.add_sum_erase T _ hπ₀] at hann
  rw [hfix, smul_smul] at hann
  have hs2 : (Equiv.Perm.sign π₀ : ℤ) * (Equiv.Perm.sign π₀ : ℤ) = 1 := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign π₀) with h | h <;> rw [h] <;> decide
  rw [hs2, one_smul] at hann
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

omit [CharZero k] in
/-- **Garnir assembly, measure-generic (sorry-free).** The `domWeight`-free version of
`garnir_assembly`: parametric over an arbitrary predicate `P : Tableau → Prop` classifying
the "good" (further-reducible or terminal) neighbours. Given a transversal `T ∋ π₀` with
the signed representation sum vanishing (`hann`) and every non-distinguished rep `π`
landing in `P` (`hgood`), the polytabloid `e_t` is a `k`-linear combination of
polytabloids of tableaux all satisfying `P`. The reindexing (identity isolation →
`sum_fiberwise` aggregation) is measure-agnostic; only the classifying predicate changes.

The `colWordNum` `straightening_step_colMax` instantiates this with
`P t' := colWordNum t' < colWordNum t` (via `hgood` = the column-word-decrease bound). -/
theorem garnir_assembly_gen (t : Specht.Tableau μ) (P : Specht.Tableau μ → Prop)
    (T : Finset (Equiv.Perm (Fin (Specht.nOf μ))))
    (π₀ : Equiv.Perm (Fin (Specht.nOf μ))) (hπ₀ : π₀ ∈ T)
    (hfix : Specht.Mtab.rep μ π₀ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign π₀ : ℤ) • Specht.polytabloid (k := k) t)
    (hgood : ∀ π ∈ T, π ≠ π₀ → P ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hann : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
        Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) = 0) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, P t') ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  set E := T.erase π₀ with hE
  rw [← Finset.add_sum_erase T _ hπ₀] at hann
  rw [hfix, smul_smul] at hann
  have hs2 : (Equiv.Perm.sign π₀ : ℤ) * (Equiv.Perm.sign π₀ : ℤ) = 1 := by
    rcases Int.units_eq_one_or (Equiv.Perm.sign π₀) with h | h <;> rw [h] <;> decide
  rw [hs2, one_smul] at hann
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
  refine ⟨E.image (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t),
    fun t' => ∑ π ∈ E.filter (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t = t'),
      (-(Equiv.Perm.sign π : k)), ?_, ?_⟩
  · intro t' ht'
    rw [Finset.mem_image] at ht'
    obtain ⟨π, hπ, rfl⟩ := ht'
    exact hgood π (Finset.mem_of_mem_erase hπ) (Finset.ne_of_mem_erase hπ)
  · rw [hexp]
    rw [← Finset.sum_fiberwise_of_maps_to
          (g := fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t)
          (t := E.image (fun π => (π : Equiv.Perm (Fin (Specht.nOf μ))) • t))
          (fun π _ => Finset.mem_image_of_mem _ (by assumption))]
    refine Finset.sum_congr rfl (fun t' _ => ?_)
    rw [Finset.sum_smul]
    refine Finset.sum_congr rfl (fun π hπ => ?_)
    rw [(Finset.mem_filter.mp hπ).2]

omit [CharZero k] in
/-- **Reindex a polytabloid combination through per-term reductions (sorry-free).** If
`e_t = ∑_{t'∈s} c_{t'} e_{t'}` and each `e_{t'}` equals a scalar multiple of some `e_u` with
`colWordNum u < colWordNum t`, then `e_t` is a combination of *strictly `colWordNum`-smaller*
polytabloids. This is the raw→sorted bookkeeping that upgrades `garnir_assembly_gen`'s output
(terms `e_{π•t}` on the raw fibre) into the `straightening_step_colMax` conclusion (terms on
the column-sorted images `e_{ρ•(π•t)}`, each strictly smaller by `fibre_colWordNum_decrease`).
Same fiberwise regrouping as `garnir_assembly_gen`. -/
theorem poly_combo_reindex (t : Specht.Tableau μ) (s : Finset (Specht.Tableau μ))
    (c : Specht.Tableau μ → k)
    (heq : Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t')
    (hsmall : ∀ t' ∈ s, ∃ u : Specht.Tableau μ, colWordNum u < colWordNum t ∧
        ∃ ε : k, Specht.polytabloid (k := k) t' = ε • Specht.polytabloid (k := k) u) :
    ∃ (s2 : Finset (Specht.Tableau μ)) (c2 : Specht.Tableau μ → k),
      (∀ t2 ∈ s2, colWordNum t2 < colWordNum t) ∧
      Specht.polytabloid (k := k) t = ∑ t2 ∈ s2, c2 t2 • Specht.polytabloid (k := k) t2 := by
  classical
  choose! u hu ε hε using hsmall
  refine ⟨s.image u, fun t2 => ∑ t' ∈ s.filter (fun t' => u t' = t2), c t' * ε t', ?_, ?_⟩
  · intro t2 ht2
    rw [Finset.mem_image] at ht2
    obtain ⟨t', ht', rfl⟩ := ht2
    exact hu t' ht'
  · rw [heq, ← Finset.sum_fiberwise_of_maps_to (g := u) (t := s.image u)
      (fun t' ht' => Finset.mem_image_of_mem _ ht')]
    refine Finset.sum_congr rfl (fun t2 _ => ?_)
    rw [Finset.sum_smul]
    refine Finset.sum_congr rfl (fun t' ht' => ?_)
    rw [Finset.mem_filter] at ht'
    rw [hε t' ht'.1, ← ht'.2, mul_smul]

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
/-- **Column-`j` label content of a tableau, as a `Finset ℕ`** — the set of the labels
sitting in column `j` (the image of the column-`j` label fibre under `Fin.val`). This is
the order-statistics substrate for the column-word decrease: the Garnir shuffle only
changes the *contents* of columns `j` and `j+1`, and the resulting column-word change is
governed by how these `Finset ℕ` contents compare (`orderStat_le_of_count_ge`). -/
def colContent (t : Specht.Tableau μ) (j : ℕ) : Finset ℕ :=
  (Finset.univ.filter (fun l => Specht.colPattern t l = j)).image Fin.val

omit [CharZero k] in
/-- **`colContent` cardinality (sorry-free).** Column `j` holds exactly `μ.colLen j`
labels; `Fin.val` is injective, so the image keeps that count. Supplies the
`s.card = k` hypothesis for `orderEmbOfFin`. -/
theorem colContent_card (t : Specht.Tableau μ) (j : ℕ) :
    (colContent t j).card = μ.colLen j := by
  classical
  rw [colContent, Finset.card_image_of_injOn (fun a _ b _ h => Fin.val_injective h)]
  exact card_col_labels t j

omit [CharZero k] in
/-- **Cell label = order statistic (sorry-free).** For a column-word-minimal (hence
column-standard, `colStandard_of_colWordMin`) tableau `t`, the label sitting at cell
`(r, j)` is the `r`-th smallest label of column `j` — reading a sorted column
top-to-bottom enumerates `colContent t j` in increasing order. This is the
tableau ↔ order-statistic bridge that lets the abstract `orderStat_le_of_count_ge`
domination be read off actual tableaux, feeding the column-word decrease bound. -/
theorem labelAt_eq_orderStat (t : Specht.Tableau μ)
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (j : ℕ) (r : Fin (μ.colLen j)) :
    labelAt t (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt) =
      (colContent t j).orderEmbOfFin (colContent_card t j) r := by
  classical
  -- column/row pattern of the label sitting at cell `(m, j)`
  have hpat : ∀ (m : ℕ) (hm : (m, j) ∈ μ),
      Specht.colPattern t (t.symm ⟨(m, j), (YoungDiagram.mem_cells _).mpr hm⟩) = j ∧
      Specht.rowPattern t (t.symm ⟨(m, j), (YoungDiagram.mem_cells _).mpr hm⟩) = m := by
    intro m hm
    refine ⟨?_, ?_⟩
    · show ((t (t.symm ⟨(m, j), _⟩) : ℕ × ℕ)).2 = j; rw [Equiv.apply_symm_apply]
    · show ((t (t.symm ⟨(m, j), _⟩) : ℕ × ℕ)).1 = m; rw [Equiv.apply_symm_apply]
  -- The map `x ↦ labelAt t (x, j)` is the increasing enumeration of `colContent t j`.
  have key : (fun x : Fin (μ.colLen j) =>
        labelAt t (YoungDiagram.mem_iff_lt_colLen.mpr x.isLt))
      = ⇑((colContent t j).orderEmbOfFin (colContent_card t j)) := by
    apply Finset.orderEmbOfFin_unique
    · -- membership: the label at cell `(x, j)` lies in column `j`, hence in `colContent`
      intro x
      rw [colContent, Finset.mem_image]
      refine ⟨t.symm ⟨(↑x, j), (YoungDiagram.mem_cells _).mpr
        (YoungDiagram.mem_iff_lt_colLen.mpr x.isLt)⟩, ?_, rfl⟩
      simp only [Finset.mem_filter, Finset.mem_univ, true_and]
      exact (hpat (↑x) (YoungDiagram.mem_iff_lt_colLen.mpr x.isLt)).1
    · -- StrictMono: rows increase ⇒ (column-standardness) labels increase
      intro a b hab
      have hla := hpat (↑a) (YoungDiagram.mem_iff_lt_colLen.mpr a.isLt)
      have hlb := hpat (↑b) (YoungDiagram.mem_iff_lt_colLen.mpr b.isLt)
      have hab' : (↑a : ℕ) < (↑b : ℕ) := hab
      show (t.symm ⟨((↑a : ℕ), j), _⟩ : Fin (Specht.nOf μ)).val
         < (t.symm ⟨((↑b : ℕ), j), _⟩ : Fin (Specht.nOf μ)).val
      by_contra hcon
      push_neg at hcon
      rcases eq_or_lt_of_le hcon with h | h
      · -- equal labels ⇒ same cell ⇒ equal rows ⇒ `↑a = ↑b`, contradicting `↑a < ↑b`
        have heq : (t.symm ⟨((↑b : ℕ), j), _⟩ : Fin (Specht.nOf μ))
                 = t.symm ⟨((↑a : ℕ), j), _⟩ := Fin.val_injective h
        rw [heq, hla.2] at hlb
        omega
      · -- `↑b`-label `<` `↑a`-label ⇒ (column-standardness) row `↑b` `<` row `↑a`, absurd
        have hrow := colStandard_of_colWordMin t hmax (hlb.1.trans hla.1.symm) h
        rw [hla.2, hlb.2] at hrow
        omega
  exact congrFun key r

omit [CharZero k] in
/-- **Column content under the `S_n`-action (sorry-free).** The action `σ • t = σ.symm.trans
t` sends the label at cell `c` to `σ` of the old label (`colPattern (σ•t) l = colPattern t
(σ.symm l)`), so column `j`'s content of `σ•t` is the `σ`-image of column `j`'s labels of
`t`. For the Garnir fibre element `σ`, this is exactly the reindexing that turns the abstract
`A∪B` shuffle into the concrete `colContent (σ•t) j`, feeding `count_dom_of_top`. -/
theorem colContent_smul (σ : Equiv.Perm (Fin (Specht.nOf μ))) (t : Specht.Tableau μ) (j : ℕ) :
    colContent (σ • t) j
      = (Finset.univ.filter (fun m => Specht.colPattern t m = j)).image (fun m => (σ m : ℕ)) := by
  classical
  unfold colContent
  have hset : (Finset.univ.filter (fun l => Specht.colPattern (σ • t) l = j))
      = (Finset.univ.filter (fun m => Specht.colPattern t m = j)).image σ := by
    ext l
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image,
      Specht.colPattern_smul, Specht.arrow_smul_apply]
    constructor
    · intro hl; exact ⟨σ.symm l, hl, Equiv.apply_symm_apply σ l⟩
    · rintro ⟨m, hm, rfl⟩; rwa [Equiv.symm_apply_apply]
  rw [hset, Finset.image_image]; rfl

omit [CharZero k] in
/-- **A column permutation preserves every column's content (sorry-free).** If `ρ ∈ C_t`
(fixes the column pattern) then `colContent (ρ•t) c = colContent t c` for every column `c`.
The column-sort `ρ` that produces the column-word-minimal image of a fibre `π•t` therefore
leaves each `colContent (π•t) c` unchanged — which is what lets `labelAt_eq_orderStat` read
the sorted image's cell labels off the (unsorted) fibre's column content. -/
theorem colContent_colStab_eq {ρ : Equiv.Perm (Fin (Specht.nOf μ))} (t : Specht.Tableau μ)
    (hρ : ρ ∈ Specht.colStab t) (c : ℕ) :
    colContent (ρ • t) c = colContent t c := by
  classical
  have hcol : ∀ l, Specht.colPattern t (ρ.symm l) = Specht.colPattern t l := fun l => by
    calc Specht.colPattern t (ρ.symm l)
        = (ρ • Specht.colPattern t) l := (Specht.arrow_smul_apply _ _ _ _).symm
      _ = Specht.colPattern t l := by rw [Specht.mem_colStab.mp hρ]
  rw [colContent_smul]
  unfold colContent
  ext v
  simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨m, hm, rfl⟩
    refine ⟨ρ m, ?_, rfl⟩
    have hm' := hcol (ρ m); rw [Equiv.symm_apply_apply] at hm'; rw [← hm']; exact hm
  · rintro ⟨l, hl, rfl⟩
    exact ⟨ρ.symm l, by rw [hcol]; exact hl, by rw [Equiv.apply_symm_apply]⟩

omit [CharZero k] in
/-- **Equal column content ⇒ equal cell labels (sorry-free).** Two column-word-minimal
(hence column-standard) tableaux with the *same* column-`c` content have the *same* label at
every cell `(r, c)` — both are the increasing enumeration of that content
(`labelAt_eq_orderStat`), and `orderEmbOfFin` depends only on the finset. This is the lemma
that turns "the fibre and `t` share a column's content" into "they agree cell-by-cell on
that column" — supplying both the `hleft` (columns left of `j`) and the strict-row
comparison for `colWordNum_lt_of_first_diff_col`. -/
theorem labelAt_eq_of_colContent_eq (u v : Specht.Tableau μ)
    (hmaxu : ∀ σ : Specht.colStab u,
      colWordNum u ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • u))
    (hmaxv : ∀ σ : Specht.colStab v,
      colWordNum v ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • v))
    (c : ℕ) (hcc : colContent u c = colContent v c) (r : Fin (μ.colLen c)) :
    labelAt u (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt)
      = labelAt v (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt) := by
  rw [labelAt_eq_orderStat u hmaxu c r, labelAt_eq_orderStat v hmaxv c r]
  simp only [hcc]

omit [CharZero k] in
/-- **Equal cell labels ⇒ equal column content (sorry-free).** Converse of
`labelAt_eq_of_colContent_eq`: two column-word-minimal tableaux whose column-`c` cell labels
agree at every row have the *same* column-`c` content — the two increasing enumerations
coincide, so (via `range_orderEmbOfFin`) their ranges, hence the finsets, coincide. Supplies
the `f ≠ g` (strictness) input from `colContent (π•t) j ≠ colContent t j`. -/
theorem colContent_eq_of_labelAt_eq (u v : Specht.Tableau μ)
    (hmaxu : ∀ σ : Specht.colStab u,
      colWordNum u ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • u))
    (hmaxv : ∀ σ : Specht.colStab v,
      colWordNum v ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • v))
    (c : ℕ)
    (h : ∀ r : Fin (μ.colLen c),
      labelAt u (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt)
        = labelAt v (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt)) :
    colContent u c = colContent v c := by
  have hfun : ⇑((colContent u c).orderEmbOfFin (colContent_card u c))
      = ⇑((colContent v c).orderEmbOfFin (colContent_card v c)) := by
    funext r
    rw [← labelAt_eq_orderStat u hmaxu c r, ← labelAt_eq_orderStat v hmaxv c r]
    exact h r
  apply Finset.coe_injective
  rw [← Finset.range_orderEmbOfFin (colContent u c) (colContent_card u c),
      ← Finset.range_orderEmbOfFin (colContent v c) (colContent_card v c), hfun]

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

omit [CharZero k] in
/-- **`B < A` entirely (sorry-free) — the foundation of the fibre-decrease bound.**
At a Garnir row descent — `labelAt t hij1 ≤ labelAt t hij`, i.e. in label order the
col-`j+1` entry at row `i` is `≤` the col-`j` entry at row `i` — of a column-word-minimal
(hence column-standard) `t`, **every** label `b ∈ B` (col `j+1`, rows `≤ i`) is strictly
smaller (in label order) than **every** label `a ∈ A` (col `j`, rows `≥ i`). Reason:
column-standardness gives `b ≤ labelAt(i,j+1)` (b at row `≤ i` in col `j+1`) and
`labelAt(i,j) ≤ a` (a at row `≥ i` in col `j`), while the descent + label-distinctness give
`labelAt(i,j+1) < labelAt(i,j)`. This is why any non-identity fibre — which moves a
`B`-label into column `j` — strictly lowers `colWordNum`: column `j` precedes column `j+1`
in the column-major reading, so a smaller label entering column `j`'s cells lowers a more
significant digit of the base-`(n+1)` word. -/
theorem garnir_B_lt_A (t : Specht.Tableau μ) (i j : ℕ)
    (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ)
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hdesc : labelAt t hij1 ≤ labelAt t hij)
    {a b : Fin (Specht.nOf μ)}
    (ha : a ∈ garnirA t i j) (hb : b ∈ garnirB t i j) :
    (b : ℕ) < (a : ℕ) := by
  classical
  -- the distinguished labels at the two descent cells
  set a₀ := t.symm ⟨(i, j), (YoungDiagram.mem_cells _).2 hij⟩ with ha0
  set b₀ := t.symm ⟨(i, j + 1), (YoungDiagram.mem_cells _).2 hij1⟩ with hb0
  have hta0 : (t a₀ : ℕ × ℕ) = (i, j) := by rw [ha0, Equiv.apply_symm_apply]
  have htb0 : (t b₀ : ℕ × ℕ) = (i, j + 1) := by rw [hb0, Equiv.apply_symm_apply]
  have hcol_a0 : Specht.colPattern t a₀ = j := by show (t a₀ : ℕ × ℕ).2 = j; rw [hta0]
  have hrow_a0 : Specht.rowPattern t a₀ = i := by show (t a₀ : ℕ × ℕ).1 = i; rw [hta0]
  have hcol_b0 : Specht.colPattern t b₀ = j + 1 := by show (t b₀ : ℕ × ℕ).2 = j + 1; rw [htb0]
  have hrow_b0 : Specht.rowPattern t b₀ = i := by show (t b₀ : ℕ × ℕ).1 = i; rw [htb0]
  rw [garnirA, Finset.mem_filter] at ha
  rw [garnirB, Finset.mem_filter] at hb
  obtain ⟨_, hca, hra⟩ := ha
  obtain ⟨_, hcb, hrb⟩ := hb
  -- a₀ ≤ a : same column j, and rowPattern a ≥ i = rowPattern a₀
  have ha0a : (a₀ : ℕ) ≤ (a : ℕ) := by
    by_contra hlt
    push_neg at hlt
    have := colStandard_of_colWordMin t hmax (by rw [hca, hcol_a0]) hlt
    rw [hrow_a0] at this; omega
  -- b ≤ b₀ : same column j+1, and rowPattern b ≤ i = rowPattern b₀
  have hbb0 : (b : ℕ) ≤ (b₀ : ℕ) := by
    by_contra hlt
    push_neg at hlt
    have := colStandard_of_colWordMin t hmax (by rw [hcol_b0, hcb]) hlt
    rw [hrow_b0] at this; omega
  -- labelAt values, and strictness from distinct cells
  have hla : labelAt t hij = (a₀ : ℕ) := by rw [labelAt, ← ha0]
  have hlb : labelAt t hij1 = (b₀ : ℕ) := by rw [labelAt, ← hb0]
  have hne : (b₀ : ℕ) ≠ (a₀ : ℕ) := by
    intro he
    have : b₀ = a₀ := Fin.ext he
    rw [this, hta0] at htb0
    injection htb0 with _ h2
    omega
  rw [hla] at hdesc; rw [hlb] at hdesc
  omega

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

omit [CharZero k] in
/-- **The `H`-part of the Garnir sum collapses to `|H|·e_t` (sorry-free).** Every
`σ ∈ H = S_A × S_B ⊆ C_t` acts on `e_t` by its sign (column antisymmetry
`polytabloid_colStab_smul` composed with equivariance `polytabloid_rep_smul`), so the
signed term `sgn(σ)·(σ·e_t) = sgn(σ)²·e_t = e_t`. Summing over `H` gives `|H|` copies.
This isolates `e_t` from `garnir_full_annihilation` for the full-group straightening path
(see the audit doc §5.1): `|H|·e_t = −∑_{σ ∈ garnirG \ H} sgn(σ)·(σ·e_t)`. -/
theorem garnir_H_sum_eq (t : Specht.Tableau μ) (i j : ℕ) :
    ∑ σ ∈ garnirH t i j, (Equiv.Perm.sign σ : ℤ) •
        Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t)
      = (garnirH t i j).card • Specht.polytabloid (k := k) t := by
  classical
  have h1 : ∀ σ ∈ garnirH t i j,
      (Equiv.Perm.sign σ : ℤ) • Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t)
        = Specht.polytabloid (k := k) t := by
    intro σ hσ
    have hcol : σ ∈ Specht.colStab t := garnirH_subset_colStab t i j σ hσ
    rw [← polytabloid_rep_smul, polytabloid_colStab_smul t hcol, smul_smul]
    have hs2 : (Equiv.Perm.sign σ : ℤ) * (Equiv.Perm.sign σ : ℤ) = 1 := by
      rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> rw [h] <;> decide
    rw [hs2, one_smul]
  rw [Finset.sum_congr rfl h1, Finset.sum_const]

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
/-- **Garnir transversal existence (sorry-free).** A left transversal `T` of `H` in `G`
whose product family `{π·ρ}` covers `garnirG` bijectively — the exact hypotheses
`sum_over_garnirG_reindex` consumes.  Built from Mathlib's `exists_left_transversal_of_le`
through the subgroup-carrier bridges `garnirGSub_coe`/`garnirHSub_coe`. -/
theorem garnir_transversal_exists (t : Specht.Tableau μ) (i j : ℕ) :
    ∃ T : Finset (Equiv.Perm (Fin (Specht.nOf μ))),
      garnirG t i j ⊆ (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) ∧
      (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) ⊆ garnirG t i j ∧
      (garnirG t i j).card = (T ×ˢ garnirH t i j).card := by
  classical
  obtain ⟨S, hSH, hScard⟩ := Subgroup.exists_left_transversal_of_le (garnirHSub_le t i j)
  rw [garnirHSub_coe, garnirGSub_coe] at hSH
  have h1H : (1 : Equiv.Perm (Fin (Specht.nOf μ))) ∈ garnirH t i j := by
    rw [garnirH, Finset.mem_inter]
    exact ⟨by rw [garnirG, Finset.mem_filter]; exact ⟨Finset.mem_univ _, fun l _ => rfl⟩,
      by rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, Subgroup.one_mem _⟩⟩
  have hGsub : ∀ σ, σ ∈ garnirG t i j ↔ σ ∈ garnirGSub t i j := by
    intro σ; rw [mem_garnirGSub, garnirG, Finset.mem_filter]
    exact ⟨fun h => h.2, fun h => ⟨Finset.mem_univ _, h⟩⟩
  have hHsubG : ∀ h ∈ garnirH t i j, h ∈ garnirGSub t i j := by
    intro h hh; rw [← hGsub]; exact (Finset.mem_inter.mp hh).1
  have hSfin : S.Finite := Set.toFinite S
  haveI : Fintype S := hSfin.fintype
  refine ⟨S.toFinset, ?_, ?_, ?_⟩
  · -- cover: garnirG ⊆ image
    intro σ hσ
    have hσS : σ ∈ (↑(garnirG t i j) : Set _) := Finset.mem_coe.mpr hσ
    rw [← hSH] at hσS
    obtain ⟨s, hs, h, hh, rfl⟩ := hσS
    exact Finset.mem_image.mpr ⟨(s, h),
      Finset.mem_product.mpr ⟨Set.mem_toFinset.mpr hs, Finset.mem_coe.mp hh⟩, rfl⟩
  · -- closed: image ⊆ garnirG
    intro σ hσ
    rw [Finset.mem_image] at hσ
    obtain ⟨⟨s, h⟩, hsh, rfl⟩ := hσ
    rw [Finset.mem_product] at hsh
    have hsG : s ∈ garnirGSub t i j := by
      rw [← hGsub, ← Finset.mem_coe, ← hSH]
      exact ⟨s, Set.mem_toFinset.mp hsh.1, 1, Finset.mem_coe.mpr h1H, mul_one s⟩
    rw [hGsub]
    exact Subgroup.mul_mem _ hsG (hHsubG h hsh.2)
  · -- card: |garnirG| = |T ×ˢ garnirH|
    rw [Finset.card_product]
    have e1 : Nat.card S = S.toFinset.card := by
      rw [Nat.card_coe_set_eq, Set.ncard_eq_toFinset_card']
    have e2 : Nat.card (garnirHSub t i j) = (garnirH t i j).card := by
      rw [← SetLike.coe_sort_coe, Nat.card_coe_set_eq, garnirHSub_coe, Set.ncard_coe_finset]
    have e3 : Nat.card (garnirGSub t i j) = (garnirG t i j).card := by
      rw [← SetLike.coe_sort_coe, Nat.card_coe_set_eq, garnirGSub_coe, Set.ncard_coe_finset]
    rw [← e3, ← hScard, e1, e2]

omit [CharZero k] in
/-- **Garnir transversal with a distinguished `H`-pivot (sorry-free).** Strengthens
`garnir_transversal_exists`: since `T` is a *transversal* of the subgroup `H = garnirH`, it
contains exactly one element of `H` — the pivot `π₀` (the `H`-coset representative,
extracted by factoring `1 ∈ garnirG` through the product bijection). Every *other* `T`-element
is `∉ garnirH`, so it is a genuine Garnir fibre and `fibre_colWordNum_decrease` applies. `π₀`
serves as `garnir_assembly_gen`'s `π₀` (its `hfix` holds because `π₀ ∈ garnirH ⊆ colStab`). -/
theorem garnir_transversal_with_pivot (t : Specht.Tableau μ) (i j : ℕ) :
    ∃ (T : Finset (Equiv.Perm (Fin (Specht.nOf μ)))) (π₀ : Equiv.Perm (Fin (Specht.nOf μ))),
      π₀ ∈ T ∧ π₀ ∈ garnirH t i j ∧
      (∀ π ∈ T, π ≠ π₀ → π ∉ garnirH t i j) ∧
      garnirG t i j ⊆ (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) ∧
      (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) ⊆ garnirG t i j ∧
      (garnirG t i j).card = (T ×ˢ garnirH t i j).card := by
  classical
  obtain ⟨T, hcover, hclosed, hcard⟩ := garnir_transversal_exists t i j
  have himg : garnirG t i j = (T ×ˢ garnirH t i j).image (fun p => p.1 * p.2) :=
    Finset.Subset.antisymm hcover hclosed
  have hinj := Finset.injOn_of_card_image_eq (f := fun p => p.1 * p.2)
    (s := T ×ˢ garnirH t i j) (by rw [← himg]; exact hcard)
  have hHmem : ∀ π, π ∈ garnirH t i j ↔ π ∈ garnirHSub t i j := fun π => by
    rw [← Finset.mem_coe, ← garnirHSub_coe, SetLike.mem_coe]
  have h1H : (1 : Equiv.Perm (Fin (Specht.nOf μ))) ∈ garnirH t i j := (hHmem 1).mpr (Subgroup.one_mem _)
  -- factor `1 ∈ garnirG` through the bijection to find the pivot
  have h1G : (1 : Equiv.Perm (Fin (Specht.nOf μ))) ∈ garnirG t i j := by
    rw [garnirG, Finset.mem_filter]; exact ⟨Finset.mem_univ _, fun l _ => rfl⟩
  rw [himg, Finset.mem_image] at h1G
  obtain ⟨⟨π₀, ρ₀⟩, hp₀mem, hp₀⟩ := h1G
  rw [Finset.mem_product] at hp₀mem
  have hπ₀T : π₀ ∈ T := hp₀mem.1
  have hρ₀H : ρ₀ ∈ garnirH t i j := hp₀mem.2
  have hp₀' : π₀ * ρ₀ = 1 := hp₀
  have hπ₀H : π₀ ∈ garnirH t i j := by
    have hinv : π₀ = ρ₀⁻¹ := mul_eq_one_iff_eq_inv.mp hp₀'
    rw [hHmem, hinv]
    exact Subgroup.inv_mem _ ((hHmem ρ₀).mp hρ₀H)
  refine ⟨T, π₀, hπ₀T, hπ₀H, ?_, hcover, hclosed, hcard⟩
  intro π hπT hπne hπH
  apply hπne
  have hfactor : π₀⁻¹ * π ∈ garnirH t i j := by
    rw [hHmem]
    exact Subgroup.mul_mem _ (Subgroup.inv_mem _ ((hHmem π₀).mp hπ₀H)) ((hHmem π).mp hπH)
  have hmap : (fun p : Equiv.Perm (Fin (Specht.nOf μ)) × Equiv.Perm (Fin (Specht.nOf μ)) =>
      p.1 * p.2) (π, 1) = (fun p => p.1 * p.2) (π₀, π₀⁻¹ * π) := by
    show π * 1 = π₀ * (π₀⁻¹ * π); rw [mul_one, mul_inv_cancel_left]
  have hpair := hinj (Finset.mem_coe.mpr (Finset.mem_product.mpr ⟨hπT, h1H⟩))
    (Finset.mem_coe.mpr (Finset.mem_product.mpr ⟨hπ₀T, hfactor⟩)) hmap
  exact (Prod.ext_iff.mp hpair).1

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

/-! #### Fibre-decrease core — the column-word decrease of each non-identity Garnir term -/

omit [CharZero k] in
/-- **A Garnir element fixes the content of every column left of `j` (sorry-free).** For
`π ∈ S_{A∪B}` (`garnirG`), a column `c < j` holds only labels *outside* `A∪B` (`A` is in
column `j`, `B` in `j+1`), so `π` fixes them pointwise and `colContent (π•t) c = colContent t
c`. Combined with `colContent_colStab_eq` + `labelAt_eq_of_colContent_eq`, this discharges
`colWordNum_lt_of_first_diff_col`'s `hleft`: the fibre and `t` agree on every cell to the
left of the Garnir columns. -/
theorem colContent_garnirG_eq_of_lt {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) (i j : ℕ) (hπ : π ∈ garnirG t i j) {c : ℕ} (hc : c < j) :
    colContent (π • t) c = colContent t c := by
  classical
  simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hπ
  rw [colContent_smul]
  unfold colContent
  apply Finset.image_congr
  intro l hl
  rw [Finset.mem_coe, Finset.mem_filter] at hl
  have hnotAB : l ∉ garnirA t i j ∪ garnirB t i j := by
    rw [Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter]
    rintro (⟨_, hcj, _⟩ | ⟨_, hcj, _⟩) <;> rw [hl.2] at hcj <;> omega
  show ((π l : Fin (Specht.nOf μ)) : ℕ) = ((l : Fin (Specht.nOf μ)) : ℕ)
  rw [hπ l hnotAB]

omit [CharZero k] in
/-- **Fibre column-`j` count-domination (sorry-free) — the order-statistics heart.** At a
Garnir row descent of a column-word-minimal `t`, the column-`j` content of the raw fibre
`π•t` count-dominates that of `t`: for every `w`, `colContent t j` has no more elements
`≤ w` than `colContent (π•t) j`. Reason: both share the fixed above-descent part `P`
(column `j`, rows `< i`, which `π` fixes); the changing part is `A = garnirA` for `t` versus
`S = π(A)` for `π•t`, and since **every** `B`-label is `< ` every `A`-label
(`garnir_B_lt_A`), `A` is the *top-`|A|`* subset of `A∪B`, so any `|A|`-subset `S ⊆ A∪B`
count-dominates it (`count_dom_of_top`); adding the common `P` preserves this
(`filter_le_card_union_mono`). Via `orderStat_le_of_count_ge` this is exactly
`labelAt (π•t sorted) (r,j) ≤ labelAt t (r,j)`. -/
theorem fibre_colContent_j_count_dom {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) {i j : ℕ} (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ)
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hdesc : labelAt t hij1 ≤ labelAt t hij)
    (hπG : π ∈ garnirG t i j) (w : ℕ) :
    ((colContent t j).filter (· ≤ w)).card
      ≤ ((colContent (π • t) j).filter (· ≤ w)).card := by
  classical
  set P := Finset.univ.filter
    (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i) with hPdef
  -- column j (label level) splits into the fixed above-descent part `P` and `garnirA`
  have hcolj : Finset.univ.filter (fun l => Specht.colPattern t l = j) = P ∪ garnirA t i j := by
    ext l
    simp only [hPdef, garnirA, Finset.mem_union, Finset.mem_filter, Finset.mem_univ, true_and]
    constructor
    · intro h; rcases lt_or_ge (Specht.rowPattern t l) i with hr | hr
      · exact Or.inl ⟨h, hr⟩
      · exact Or.inr ⟨h, hr⟩
    · rintro (⟨h, _⟩ | ⟨h, _⟩) <;> exact h
  have hdisjPA : Disjoint P (garnirA t i j) := by
    rw [Finset.disjoint_left]; intro l hlP hlA
    simp only [hPdef, garnirA, Finset.mem_filter, Finset.mem_univ, true_and] at hlP hlA
    omega
  -- `π` fixes the labels of `P` (they lie outside `A∪B`)
  have hπfix : ∀ l ∈ P, π l = l := by
    simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hπG
    intro l hlP
    apply hπG
    simp only [hPdef, Finset.mem_filter, Finset.mem_univ, true_and] at hlP
    rw [Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter]
    rintro (⟨_, hc, _⟩ | ⟨_, hc, _⟩) <;> omega
  -- value-set decompositions of the two column contents
  have hCt : colContent t j = P.image Fin.val ∪ (garnirA t i j).image Fin.val := by
    unfold colContent; rw [hcolj, Finset.image_union]
  have hCpt : colContent (π • t) j
      = P.image Fin.val ∪ ((garnirA t i j).image π).image Fin.val := by
    rw [colContent_smul, hcolj, Finset.image_union]
    congr 1
    · apply Finset.image_congr; intro l hl
      rw [Finset.mem_coe] at hl
      show ((π l : Fin (Specht.nOf μ)) : ℕ) = ((l : Fin (Specht.nOf μ)) : ℕ)
      rw [hπfix l hl]
    · rw [Finset.image_image]; rfl
  -- `π(A) ⊆ A∪B` (π maps the Garnir cells onto themselves)
  have hSsub : (garnirA t i j).image π ⊆ garnirA t i j ∪ garnirB t i j := by
    intro x hx
    rw [Finset.mem_image] at hx
    obtain ⟨l, hlA, rfl⟩ := hx
    by_contra hnot
    have hfixπl : π (π l) = π l := by
      simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hπG
      exact hπG (π l) hnot
    have hpll : π l = l := π.injective hfixπl
    rw [hpll] at hnot
    exact hnot (Finset.mem_union_left _ hlA)
  have hSvalsub : ((garnirA t i j).image π).image Fin.val
      ⊆ (garnirA t i j).image Fin.val ∪ (garnirB t i j).image Fin.val := by
    rw [← Finset.image_union]; exact Finset.image_subset_image hSsub
  have hScard : (((garnirA t i j).image π).image Fin.val).card
      = ((garnirA t i j).image Fin.val).card := by
    rw [Finset.card_image_of_injective _ Fin.val_injective,
        Finset.card_image_of_injective _ π.injective,
        Finset.card_image_of_injective _ Fin.val_injective]
  -- `B < A` at the value level
  have hBA : ∀ b ∈ (garnirB t i j).image Fin.val, ∀ a ∈ (garnirA t i j).image Fin.val, b < a := by
    intro b hb a ha
    rw [Finset.mem_image] at hb ha
    obtain ⟨lb, hlbB, rfl⟩ := hb
    obtain ⟨la, hlaA, rfl⟩ := ha
    exact garnir_B_lt_A t i j hij hij1 hmax hdesc hlaA hlbB
  -- disjointness of the fixed part `P` from both changing parts
  have hPAval : Disjoint (P.image Fin.val) ((garnirA t i j).image Fin.val) := by
    rw [Finset.disjoint_left]; rintro v hvP hvA
    rw [Finset.mem_image] at hvP hvA
    obtain ⟨l, hlP, rfl⟩ := hvP; obtain ⟨m, hmA, hlm⟩ := hvA
    exact absurd (Fin.val_injective hlm ▸ hmA) (Finset.disjoint_left.mp hdisjPA hlP)
  have hPBval : Disjoint (P.image Fin.val) ((garnirB t i j).image Fin.val) := by
    rw [Finset.disjoint_left]; rintro v hvP hvB
    rw [Finset.mem_image] at hvP hvB
    obtain ⟨l, hlP, rfl⟩ := hvP; obtain ⟨m, hmB, hlm⟩ := hvB
    have hml : m = l := Fin.val_injective hlm
    rw [hml] at hmB
    simp only [hPdef, garnirB, Finset.mem_filter, Finset.mem_univ, true_and] at hlP hmB
    omega
  have hPSval : Disjoint (P.image Fin.val) (((garnirA t i j).image π).image Fin.val) :=
    Finset.disjoint_of_subset_right hSvalsub
      (by rw [Finset.disjoint_union_right]; exact ⟨hPAval, hPBval⟩)
  rw [hCt, hCpt]
  exact filter_le_card_union_mono hPAval hPSval
    (fun w => count_dom_of_top hBA hSvalsub hScard w) w

omit [CharZero k] in
/-- Column `j`'s labels split into the above-descent part (rows `< i`) and `garnirA`
(rows `≥ i`). -/
theorem colj_labelset_split (t : Specht.Tableau μ) (i j : ℕ) :
    Finset.univ.filter (fun l => Specht.colPattern t l = j)
      = Finset.univ.filter (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)
        ∪ garnirA t i j := by
  ext l
  simp only [garnirA, Finset.mem_union, Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · intro h; rcases lt_or_ge (Specht.rowPattern t l) i with hr | hr
    · exact Or.inl ⟨h, hr⟩
    · exact Or.inr ⟨h, hr⟩
  · rintro (⟨h, _⟩ | ⟨h, _⟩) <;> exact h

omit [CharZero k] in
/-- **Column-`j` content decomposition (sorry-free).** `colContent t j` is the (disjoint)
union of the above-descent value set `P` and the `garnirA` value set. -/
theorem colContent_j_split (t : Specht.Tableau μ) (i j : ℕ) :
    colContent t j
      = (Finset.univ.filter
          (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)).image Fin.val
        ∪ (garnirA t i j).image Fin.val := by
  classical
  unfold colContent
  rw [← Finset.image_union, ← colj_labelset_split]

omit [CharZero k] in
/-- **Fibre column-`j` content decomposition (sorry-free).** For `π ∈ garnirG`, `colContent
(π•t) j` is `P` (unchanged — `π` fixes it) union the `π`-image of `garnirA`'s value set. -/
theorem colContent_smul_j_split {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) (i j : ℕ) (hπG : π ∈ garnirG t i j) :
    colContent (π • t) j
      = (Finset.univ.filter
          (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)).image Fin.val
        ∪ ((garnirA t i j).image π).image Fin.val := by
  classical
  rw [colContent_smul, colj_labelset_split t i j, Finset.image_union]
  simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hπG
  congr 1
  · apply Finset.image_congr
    intro l hl
    obtain ⟨-, hlc, hlr⟩ := Finset.mem_filter.mp (Finset.mem_coe.mp hl)
    have hnotAB : l ∉ garnirA t i j ∪ garnirB t i j := by
      rw [Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter]
      rintro (⟨_, _, hr⟩ | ⟨_, hc, _⟩) <;> omega
    show ((π l : Fin (Specht.nOf μ)) : ℕ) = ((l : Fin (Specht.nOf μ)) : ℕ)
    rw [hπG l hnotAB]
  · rw [Finset.image_image]; rfl

omit [CharZero k] in
/-- **A Garnir element maps `A∪B` onto itself (sorry-free).** `π ∈ garnirG` fixes every label
outside `A∪B` and is a bijection, so it permutes `A∪B`. -/
theorem garnirG_image_AB {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) (i j : ℕ) (hπG : π ∈ garnirG t i j) :
    (garnirA t i j ∪ garnirB t i j).image π = garnirA t i j ∪ garnirB t i j := by
  classical
  apply Finset.eq_of_subset_of_card_le
  · intro x hx
    rw [Finset.mem_image] at hx
    obtain ⟨l, hl, rfl⟩ := hx
    by_contra hnot
    simp only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] at hπG
    have hfix := hπG (π l) hnot
    rw [π.injective hfix] at hnot
    exact hnot hl
  · exact le_of_eq (Finset.card_image_of_injective _ π.injective).symm

omit [CharZero k] in
/-- **`garnirA` fixed setwise ⇒ column stabiliser (sorry-free).** If `π ∈ garnirG` maps
`garnirA` onto itself, then it maps `garnirB` onto itself (card argument on `A∪B`) and fixes
the complement of `A∪B`, so it preserves the whole column pattern: `π ∈ C_t`. This is the
converse used for the fibre strictness — a fibre that leaves column `j`'s content unchanged
is a column permutation, hence lies in `garnirH` (excluded for a genuine Garnir term). -/
theorem colStab_of_garnirA_image_eq {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) (i j : ℕ) (hπG : π ∈ garnirG t i j)
    (hAeq : (garnirA t i j).image π = garnirA t i j) : π ∈ Specht.colStab t := by
  classical
  have hfix : ∀ l, l ∉ garnirA t i j ∪ garnirB t i j → π l = l := by
    simpa only [garnirG, Finset.mem_filter, Finset.mem_univ, true_and] using hπG
  have hdisjAB : Disjoint (garnirA t i j) (garnirB t i j) := by
    rw [Finset.disjoint_left]; intro l hlA hlB
    simp only [garnirA, garnirB, Finset.mem_filter, Finset.mem_univ, true_and] at hlA hlB
    omega
  -- π maps B onto B
  have hcardX : ((garnirB t i j).image π).card = (garnirB t i j).card :=
    Finset.card_image_of_injective _ π.injective
  have hunion : garnirA t i j ∪ (garnirB t i j).image π = garnirA t i j ∪ garnirB t i j := by
    conv_lhs => rw [← hAeq]
    rw [← Finset.image_union]; exact garnirG_image_AB t i j hπG
  have hdisjAX : Disjoint (garnirA t i j) ((garnirB t i j).image π) := by
    rw [Finset.disjoint_iff_inter_eq_empty, ← Finset.card_eq_zero]
    have hci := Finset.card_union_add_card_inter (garnirA t i j) ((garnirB t i j).image π)
    rw [hunion, Finset.card_union_of_disjoint hdisjAB, hcardX] at hci
    omega
  have hBeq : (garnirB t i j).image π = garnirB t i j := by
    have hXsub : (garnirB t i j).image π ⊆ garnirB t i j := by
      intro x hx
      have hxAB : x ∈ garnirA t i j ∪ garnirB t i j := by
        rw [← garnirG_image_AB t i j hπG]
        exact Finset.image_subset_image Finset.subset_union_right hx
      have hxnA : x ∉ garnirA t i j := fun hxa => (Finset.disjoint_left.mp hdisjAX hxa) hx
      exact (Finset.mem_union.mp hxAB).resolve_left hxnA
    exact Finset.eq_of_subset_of_card_le hXsub (le_of_eq hcardX.symm)
  -- π.symm maps A→A, B→B, fixes the complement
  have hsymmA : ∀ a ∈ garnirA t i j, π.symm a ∈ garnirA t i j := by
    intro a ha; rw [← hAeq, Finset.mem_image] at ha
    obtain ⟨a', ha', rfl⟩ := ha; rw [Equiv.symm_apply_apply]; exact ha'
  have hsymmB : ∀ b ∈ garnirB t i j, π.symm b ∈ garnirB t i j := by
    intro b hb; rw [← hBeq, Finset.mem_image] at hb
    obtain ⟨b', hb', rfl⟩ := hb; rw [Equiv.symm_apply_apply]; exact hb'
  have hsymmfix : ∀ l, l ∉ garnirA t i j ∪ garnirB t i j → π.symm l = l := by
    intro l hl
    have hl' := hfix l hl
    calc π.symm l = π.symm (π l) := by rw [hl']
      _ = l := Equiv.symm_apply_apply π l
  rw [Specht.mem_colStab]
  funext l
  rw [Specht.arrow_smul_apply]
  by_cases hlA : l ∈ garnirA t i j
  · have hsa := hsymmA l hlA
    simp only [garnirA, Finset.mem_filter, Finset.mem_univ, true_and] at hlA hsa
    rw [hsa.1, hlA.1]
  by_cases hlB : l ∈ garnirB t i j
  · have hsb := hsymmB l hlB
    simp only [garnirB, Finset.mem_filter, Finset.mem_univ, true_and] at hlB hsb
    rw [hsb.1, hlB.1]
  · have hlnot : l ∉ garnirA t i j ∪ garnirB t i j := by
      rw [Finset.mem_union]; push_neg; exact ⟨hlA, hlB⟩
    rw [hsymmfix l hlnot]

omit [CharZero k] in
/-- **A genuine Garnir fibre changes column `j`'s content (sorry-free).** For `π ∈ garnirG`
with `π ∉ garnirH` (a non-column-preserving coset element), `colContent (π•t) j ≠ colContent
t j`. Contrapositive of `colStab_of_garnirA_image_eq`: equal column-`j` content forces
`garnirA.image π = garnirA` (cancel the common above-descent part `P`), hence `π ∈ colStab t`,
hence `π ∈ garnirH` — excluded. Supplies the strict row for `exists_first_lt_of_le_of_ne`. -/
theorem fibre_colContent_j_ne {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) (i j : ℕ) (hπG : π ∈ garnirG t i j) (hπH : π ∉ garnirH t i j) :
    colContent (π • t) j ≠ colContent t j := by
  classical
  intro heq
  apply hπH
  rw [garnirH, Finset.mem_inter, Finset.mem_filter]
  refine ⟨hπG, Finset.mem_univ _, colStab_of_garnirA_image_eq t i j hπG ?_⟩
  rw [colContent_smul_j_split t i j hπG, colContent_j_split t i j] at heq
  set Pv := (Finset.univ.filter
    (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i)).image Fin.val with hPv
  -- `P` labels lie outside `A∪B`; `garnirA.image π ⊆ A∪B`
  have hPdisjAB : ∀ l ∈ Finset.univ.filter
      (fun l => Specht.colPattern t l = j ∧ Specht.rowPattern t l < i),
      l ∉ garnirA t i j ∪ garnirB t i j := by
    intro l hlP
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hlP
    rw [Finset.mem_union, garnirA, garnirB, Finset.mem_filter, Finset.mem_filter]
    rintro (⟨_, _, hr⟩ | ⟨_, hc, _⟩) <;> omega
  have hSAB : (garnirA t i j).image π ⊆ garnirA t i j ∪ garnirB t i j := by
    rw [← garnirG_image_AB t i j hπG]
    exact Finset.image_subset_image Finset.subset_union_left
  -- cancel `Pv`: the changed value set equals the original
  have hSA : ((garnirA t i j).image π).image Fin.val = (garnirA t i j).image Fin.val := by
    apply Finset.eq_of_subset_of_card_le
    · intro v hv
      have hvU := heq ▸ Finset.mem_union_right Pv hv
      have hvnP : v ∉ Pv := by
        rw [hPv, Finset.mem_image]; rintro ⟨p, hp, hpv⟩
        rw [Finset.mem_image] at hv; obtain ⟨x, hx, hxv⟩ := hv
        have hpx : p = x := Fin.val_injective (hpv.trans hxv.symm)
        exact hPdisjAB p hp (hpx ▸ hSAB hx)
      exact (Finset.mem_union.mp hvU).resolve_left hvnP
    · rw [Finset.card_image_of_injective _ Fin.val_injective,
          Finset.card_image_of_injective _ Fin.val_injective,
          Finset.card_image_of_injective _ π.injective]
  exact Finset.image_injective Fin.val_injective hSA

omit [CharZero k] in
/-- **Fibre-decrease capstone (sorry-free).** For a column-word-minimal `t` at a row descent
`(i,j)/(i,j+1)` and a genuine Garnir fibre `π ∈ garnirG \ garnirH`, the column-sorted image
`ρ•(π•t)` (from `exists_colWordMin_form`) is strictly `colWordNum`-smaller than `t`. Column
`j` decreases pointwise (count-domination `fibre_colContent_j_count_dom` →
`orderEmbOfFin_le_of_count` → `labelAt_eq_orderStat`), strictly at the top-most changed row
(`fibre_colContent_j_ne` → `exists_first_lt_of_le_of_ne`), columns `< j` are untouched
(`colContent_garnirG_eq_of_lt`), and `colWordNum_lt_of_first_diff_col` closes it. This is the
`hgood` the straightening assembly needs. -/
theorem fibre_colWordNum_decrease {π : Equiv.Perm (Fin (Specht.nOf μ))}
    (t : Specht.Tableau μ) {i j : ℕ} (hij : (i, j) ∈ μ) (hij1 : (i, j + 1) ∈ μ)
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t))
    (hdesc : labelAt t hij1 ≤ labelAt t hij)
    (hπG : π ∈ garnirG t i j) (hπH : π ∉ garnirH t i j) :
    ∃ ρ : Equiv.Perm (Fin (Specht.nOf μ)), ρ ∈ Specht.colStab (π • t) ∧
      colWordNum (ρ • (π • t)) < colWordNum t := by
  classical
  obtain ⟨ρ, hρmem, -, hρmin⟩ := exists_colWordMin_form (π • t)
  refine ⟨ρ, hρmem, ?_⟩
  have hmaxs : ∀ σ : Specht.colStab (ρ • (π • t)),
      colWordNum (ρ • (π • t))
        ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • (ρ • (π • t))) :=
    fun σ => hρmin (σ : Equiv.Perm (Fin (Specht.nOf μ))) σ.2
  have hCeq : ∀ c, colContent (ρ • (π • t)) c = colContent (π • t) c :=
    fun c => colContent_colStab_eq (π • t) hρmem c
  have hle : ∀ r : Fin (μ.colLen j),
      labelAt (ρ • (π • t)) (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt)
        ≤ labelAt t (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt) := by
    intro r
    rw [labelAt_eq_orderStat (ρ • (π • t)) hmaxs j r, labelAt_eq_orderStat t hmax j r]
    refine orderEmbOfFin_le_of_count (colContent_card (ρ • (π • t)) j) (colContent_card t j)
      (fun w => ?_) r
    rw [hCeq j]
    exact fibre_colContent_j_count_dom t hij hij1 hmax hdesc hπG w
  have hne : (fun r : Fin (μ.colLen j) =>
        labelAt (ρ • (π • t)) (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt))
      ≠ (fun r => labelAt t (YoungDiagram.mem_iff_lt_colLen.mpr r.isLt)) := by
    intro hfg
    apply fibre_colContent_j_ne t i j hπG hπH
    rw [← hCeq j]
    exact colContent_eq_of_labelAt_eq (ρ • (π • t)) t hmaxs hmax j (fun r => congrFun hfg r)
  obtain ⟨r₀, hr₀lt, hr₀below⟩ := exists_first_lt_of_le_of_ne _ _ hle hne
  refine colWordNum_lt_of_first_diff_col t (ρ • (π • t))
    ⟨((r₀ : ℕ), j), (YoungDiagram.mem_cells _).mpr
      (YoungDiagram.mem_iff_lt_colLen.mpr r₀.isLt)⟩ ?_ ?_ ?_
  · intro c hc2
    have hc2' : (c : ℕ × ℕ).2 < j := hc2
    have hcmem : ((c : ℕ × ℕ).1, (c : ℕ × ℕ).2) ∈ μ := by
      rw [Prod.mk.eta]; exact (YoungDiagram.mem_cells _).mp c.2
    have hr : (c : ℕ × ℕ).1 < μ.colLen (c : ℕ × ℕ).2 :=
      YoungDiagram.mem_iff_lt_colLen.mp hcmem
    have hcc : colContent t (c : ℕ × ℕ).2 = colContent (ρ • (π • t)) (c : ℕ × ℕ).2 := by
      rw [hCeq, colContent_garnirG_eq_of_lt t i j hπG hc2']
    have hkey := labelAt_eq_of_colContent_eq t (ρ • (π • t)) hmax hmaxs
      (c : ℕ × ℕ).2 hcc ⟨(c : ℕ × ℕ).1, hr⟩
    show labelAt t hcmem = labelAt (ρ • (π • t)) hcmem
    exact hkey
  · intro c hc2 hc1
    have hcj : (c : ℕ × ℕ).2 = j := hc2
    have hr : (c : ℕ × ℕ).1 < μ.colLen j := by
      rw [← hcj]
      exact YoungDiagram.mem_iff_lt_colLen.mp (by rw [Prod.mk.eta]; exact (YoungDiagram.mem_cells _).mp c.2)
    have hlt₀ : (⟨(c : ℕ × ℕ).1, hr⟩ : Fin (μ.colLen j)) < r₀ := hc1
    have hkey := hr₀below ⟨(c : ℕ × ℕ).1, hr⟩ hlt₀
    have hcval : (c : μ.cells) = ⟨((c : ℕ × ℕ).1, j),
        (YoungDiagram.mem_cells _).mpr (YoungDiagram.mem_iff_lt_colLen.mpr hr)⟩ := by
      apply Subtype.ext
      show (c : ℕ × ℕ) = ((c : ℕ × ℕ).1, j)
      rw [← hcj]
    show ((t.symm c : Fin (Specht.nOf μ)) : ℕ)
      = (((ρ • (π • t)).symm c : Fin (Specht.nOf μ)) : ℕ)
    rw [hcval]
    exact hkey.symm
  · show labelAt (ρ • (π • t)) (YoungDiagram.mem_iff_lt_colLen.mpr r₀.isLt)
      < labelAt t (YoungDiagram.mem_iff_lt_colLen.mpr r₀.isLt)
    exact hr₀lt

/-! #### The single residual straightening core + the induction skeleton -/

/-- **The residual straightening core, on the CORRECT `colWordNum` measure
(Sagan §2.6 Garnir relations).**
A polytabloid `e_t` that is *not itself* a standard polytabloid **and** whose tableau
`t` is already **column-word-minimal** — no column permutation `σ ∈ C_t` *lowers* the
column-word measure `colWordNum` (hypothesis `hmax`: `colWordNum t ≤ colWordNum (σ•t)`
for all `σ`, i.e. `t`'s columns are already sorted) — is a `k`-linear combination of
polytabloids of **strictly `colWordNum`-smaller** tableaux.

This restatement replaces the earlier `domWeight`-based version, which was **false**
(exact-arithmetic disproof, μ=(3,2), t=[[1,2,3],[5,4]]; audit §3.5): `domWeight`
(tabloid dominance) cannot order the Garnir terms because they are dominance-
*incomparable* to `{t}`. The **column-word** measure does order them — every
non-identity Garnir term is strictly `colWordNum`-smaller (validated exhaustively to
shape (3,3,2)/(4,3,1); audit §4.5). This theorem is therefore now a TRUE statement.

This is the *irreducible* combinatorial heart of the straightening algorithm with the
**column-sort already exhausted**: because `hmax` says no column permutation lowers
`colWordNum` further (columns sorted), the column-antisymmetry lever
`polytabloid_colStab_smul` is spent, and closing this requires the **Garnir coset-sum
identity at a row descent** (Sagan §2.6) — proved sorry-free below
(`garnir_full_annihilation`, `sum_over_garnirG_reindex`, `transversal_sum_eq_zero`,
`garnir_transversal_exists`, `sum_sign_rep_polytabloid_eq_zero_of_family`) — plus the
new **column-word decrease** lemma. The general `straightening_step` reduces to this
case sorry-free by splitting on whether a `colWordNum`-lowering column permutation
exists.

`hmax` is a genuine restriction (a column-word-minimal `t` is column-standard), so
this is an honest sub-case: for a column-standard non-standard `t` a row descent
between adjacent columns exists and the Garnir relation yields strictly
`colWordNum`-smaller terms. -/
theorem straightening_step_colMax (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ)))
    (hmax : ∀ σ : Specht.colStab t,
      colWordNum t ≤ colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t)) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, colWordNum t' < colWordNum t) ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  -- Ref: [sagan2001] §2.6 (Garnir relations / straightening algorithm); also
  -- [james1984representation] §8. On the CORRECT `colWordNum` measure (the earlier
  -- `domWeight` goal was FALSE — audit §3.5). Assembly: a row descent + the Garnir
  -- coset-sum annihilation express `e_t` as a combination of raw fibre polytabloids
  -- `e_{π•t}`; each non-pivot fibre's column-sorted image is strictly `colWordNum`-smaller
  -- (`fibre_colWordNum_decrease`), and `poly_combo_reindex` reindexes onto those sorted
  -- images to give the strictly-smaller conclusion.
  classical
  -- 1. row descent from column-word-minimality
  obtain ⟨i, j, hij, hij1, hdesc⟩ := exists_row_descent_of_colWordMin t h hmax
  -- 2. transversal `T` of `H = garnirH` in `garnirG`, with its distinguished `H`-pivot `π₀`
  obtain ⟨T, π₀, hπ₀T, hπ₀H, hother, hcover, hclosed, hcard⟩ :=
    garnir_transversal_with_pivot t i j
  have h1H : (1 : Equiv.Perm (Fin (Specht.nOf μ))) ∈ garnirH t i j := by
    rw [garnirH, Finset.mem_inter]
    exact ⟨by rw [garnirG, Finset.mem_filter]; exact ⟨Finset.mem_univ _, fun l _ => rfl⟩,
      by rw [Finset.mem_filter]; exact ⟨Finset.mem_univ _, Subgroup.one_mem _⟩⟩
  -- 3. the full-Garnir annihilation reindexes to a vanishing transversal sum
  have hann : ∑ π ∈ T, (Equiv.Perm.sign π : ℤ) •
      Specht.Mtab.rep μ π (Specht.polytabloid (k := k) t) = 0 := by
    apply transversal_sum_eq_zero t T (garnirH t i j)
      (garnirH_subset_colStab t i j) (garnirH_card_pos t i j)
    rw [← sum_over_garnirG_reindex t i j T hcover hclosed hcard
      (fun σ => (Equiv.Perm.sign σ : ℤ) • Specht.Mtab.rep μ σ (Specht.polytabloid (k := k) t))]
    exact garnir_full_annihilation t hij hij1
  -- 4. `hfix`: the pivot acts by its sign (`π₀ ∈ garnirH ⊆ colStab`)
  have hfix : Specht.Mtab.rep μ π₀ (Specht.polytabloid (k := k) t)
      = (Equiv.Perm.sign π₀ : ℤ) • Specht.polytabloid (k := k) t :=
    rep_polytabloid_of_mem_colStab t (garnirH_subset_colStab t i j π₀ hπ₀H)
  -- 5. `hgood`: every non-pivot fibre reduces to a strictly `colWordNum`-smaller polytabloid
  have hgood : ∀ π ∈ T, π ≠ π₀ →
      ∃ u : Specht.Tableau μ, colWordNum u < colWordNum t ∧
        ∃ ε : k, Specht.polytabloid (k := k) ((π : Equiv.Perm (Fin (Specht.nOf μ))) • t)
          = ε • Specht.polytabloid (k := k) u := by
    intro π hπT hπne
    have hπnotH : π ∉ garnirH t i j := hother π hπT hπne
    have hπG : π ∈ garnirG t i j := by
      apply hclosed
      rw [Finset.mem_image]
      exact ⟨(π, 1), Finset.mem_product.mpr ⟨hπT, h1H⟩, mul_one π⟩
    obtain ⟨ρ, hρmem, hlt⟩ := fibre_colWordNum_decrease t hij hij1 hmax hdesc hπG hπnotH
    refine ⟨ρ • (π • t), hlt, ((Equiv.Perm.sign ρ : ℤ) : k), ?_⟩
    have hpoly : Specht.polytabloid (k := k) (π • t)
        = (Equiv.Perm.sign ρ : ℤ) • Specht.polytabloid (k := k) (ρ • (π • t)) := by
      rw [polytabloid_colStab_smul (π • t) hρmem, smul_smul]
      have hs2 : (Equiv.Perm.sign ρ : ℤ) * (Equiv.Perm.sign ρ : ℤ) = 1 := by
        rcases Int.units_eq_one_or (Equiv.Perm.sign ρ) with hh | hh <;> rw [hh] <;> decide
      rw [hs2, one_smul]
    rw [hpoly, ← Int.cast_smul_eq_zsmul k]
  -- 6. assemble `e_t = Σ c_{π•t} e_{π•t}` then reindex onto the sorted images
  obtain ⟨s, c, hsP, hseq⟩ := garnir_assembly_gen t
    (fun t' => ∃ u : Specht.Tableau μ, colWordNum u < colWordNum t ∧
      ∃ ε : k, Specht.polytabloid (k := k) t' = ε • Specht.polytabloid (k := k) u)
    T π₀ hπ₀T hfix hgood hann
  exact poly_combo_reindex t s c hseq hsP

/-- **Straightening step (Sagan §2.6) — reduced sorry-free to the column-maximal core.**
A polytabloid `e_t` that is *not itself* a standard polytabloid is a `k`-linear
combination of polytabloids of **strictly `colWordNum`-smaller** tableaux (the
validated column-word measure). From this core, the full spanning half
(`standardPolytabloid_straightening`) follows sorry-free by well-founded induction on
`colWordNum t` (descending).

**Reduction (sorry-free half).** Split on whether some column permutation `σ ∈ C_t`
strictly *lowers* `colWordNum` (equivalently: `t`'s columns are not yet sorted):

* **Column-lowering** (`∃ σ ∈ C_t, colWordNum (σ•t) < colWordNum t`) — handled here
  outright by the column-antisymmetry lever `polytabloid_colStab_smul`: since
  `e_{σ•t} = sgn(σ)·e_t` and `sgn(σ)² = 1`, we get `e_t = sgn(σ)·e_{σ•t}`, a
  one-term combination over `{σ•t}`, and `colWordNum (σ•t) < colWordNum t` is exactly
  the branch hypothesis. No dominance theory needed.
* **Column-word-minimal** (no such `σ`, i.e. columns sorted) — delegated to
  `straightening_step_colMax`, the single Garnir residual, which carries the
  hypothesis `hmax` that no column permutation lowers `colWordNum`. -/
theorem straightening_step (t : Specht.Tableau μ)
    (h : Specht.polytabloid (k := k) t ∉ Set.range (standardPolytabloid (k := k) (μ := μ))) :
    ∃ (s : Finset (Specht.Tableau μ)) (c : Specht.Tableau μ → k),
      (∀ t' ∈ s, colWordNum t' < colWordNum t) ∧
      Specht.polytabloid (k := k) t = ∑ t' ∈ s, c t' • Specht.polytabloid (k := k) t' := by
  classical
  by_cases hraise : ∃ σ : Specht.colStab t,
      colWordNum ((σ : Equiv.Perm (Fin (Specht.nOf μ))) • t) < colWordNum t
  · -- Column-lowering case (`colWordNum (σ•t) < colWordNum t`): fully proved via
    -- column-antisymmetry.
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

/-- **Spanning half — proved sorry-free.** Every polytabloid `e_t` (arbitrary tableau `t`)
lies in the
span of the *standard* polytabloids, by well-founded (strong) induction on the
**column-word measure** `colWordNum t` (DESCENDING): if `e_t` is already a standard
polytabloid it is in the spanning set; otherwise `straightening_step` rewrites it
over tableaux of strictly *smaller* `colWordNum`, each in the span by the induction
hypothesis, and the span is closed under `k`-linear combinations. (The measure is
`colWordNum`, not `domWeight`: `domWeight` — tabloid dominance — cannot drive this
induction, since Garnir produces dominance-incomparable terms; see the audit doc.) -/
theorem standardPolytabloid_straightening :
    ∀ t : Specht.Tableau μ,
      Specht.polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  intro t
  generalize hg : colWordNum t = g
  induction g using Nat.strong_induction_on generalizing t with
  | _ g IH =>
    by_cases hr : Specht.polytabloid (k := k) t ∈
        Set.range (standardPolytabloid (k := k) (μ := μ))
    · exact Submodule.subset_span hr
    · obtain ⟨s, c, hgt, heq⟩ := straightening_step (k := k) t hr
      rw [heq]
      refine Submodule.sum_mem _ (fun t' ht' => ?_)
      refine Submodule.smul_mem _ _ ?_
      have hlt : colWordNum t' < colWordNum t := hgt t' ht'
      exact IH (colWordNum t') (by omega) t' rfl

/-- **M^μ-level span identity.** The standard polytabloids span exactly `S^μ`
inside `M^μ`. (≤): each standard polytabloid is a polytabloid (`standardPolytabloid_mem`);
(≥): the straightening core. Sorry-free. -/
theorem standardPolytabloid_span_eq_specht :
    Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ)))
      = Specht.SpechtSubmodule (k := k) μ := by
  apply le_antisymm
  · rw [Submodule.span_le]
    rintro _ ⟨T, rfl⟩
    exact standardPolytabloid_mem (k := k) T
  · rw [Specht.SpechtSubmodule, Submodule.span_le, Set.range_subset_iff]
    exact standardPolytabloid_straightening (k := k) (μ := μ)

/-- **Content obligation 2/2 — spanning**, now derived **sorry-free** (the M^μ span
identity + the corestriction to `⊤` in `S^μ` are discharged here). Keeps the original
name/signature for `Basis.mk`. -/
theorem standardPolytabloid_span :
    Submodule.span k (Set.range (standardPolytabloidS (k := k) (μ := μ))) = ⊤ := by
  apply Submodule.map_injective_of_injective
    (Submodule.injective_subtype (Specht.SpechtSubmodule (k := k) μ))
  rw [Submodule.map_subtype_top, Submodule.map_span, ← Set.range_comp,
      subtype_comp_standardPolytabloidS]
  exact standardPolytabloid_span_eq_specht (k := k) (μ := μ)

/-- Every element of `Specht.SpechtSubmodule μ` lies in the `k`-span of the range of `standardPolytabloid`. -/
theorem mem_span_standardPolytabloid_of_mem_specht {x : Specht.Mtab (k := k) μ}
    (hx : x ∈ Specht.SpechtSubmodule (k := k) μ) :
    x ∈ Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  rw [standardPolytabloid_span_eq_specht (k := k) (μ := μ)]
  exact hx

end QOU.BraidKnot.SpechtStandardBasis
