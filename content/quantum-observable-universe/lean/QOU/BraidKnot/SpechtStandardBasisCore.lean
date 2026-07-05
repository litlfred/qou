import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Finsupp.VectorSpace
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.OfMap
import Mathlib.Data.Finset.Max
import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.Specht

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
| `standardPolytabloid_span` | **STUB** `sorry` — `-- Ref: [sagan2001]` (Garnir relations) |
| `standardBasis` | **sorry-free MODULO the two stubs** (`Basis.mk` wiring) |
| `specht_finrank_eq_numSYT` | **sorry-free MODULO the two stubs** (the reduction) |

The reduction (`standardBasis` + `specht_finrank_eq_numSYT`) is **genuinely
sorry-free**: its only `sorry`-tainted inputs are the two named classical facts
(`standardPolytabloid_linearIndependent`, `standardPolytabloid_span`). The
SYT→tableau conversion **and** the `Fintype` instance brick 1 left open are
*both* proved sorry-free here, so the two stubs above are the *entire* remaining
mathematical debt.

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

omit [CharZero k] in
/-- **STUB — the irreducible spanning core (Garnir / straightening law).** Every
polytabloid `e_t` (arbitrary tableau `t`) lies in the span of the *standard*
polytabloids. This is Sagan's §2.6 straightening algorithm; from it, spanning
follows sorry-free. -/
theorem standardPolytabloid_straightening :
    ∀ t : Specht.Tableau μ,
      Specht.polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  -- Ref: [sagan2001] §2.6 (Garnir relations / straightening algorithm: every
  -- polytabloid is a ℤ-combination of standard polytabloids). See also
  -- [james1984representation] §8. The irreducible spanning core of brick 4.
  sorry

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
