import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.OfMap
import QOU.BraidKnot.StandardYoungTableau
import QOU.BraidKnot.Specht

/-!
# QOU.BraidKnot.SpechtStandardBasis — brick 4 of the Okounkov–Vershik tower

The **standard-basis theorem** for Specht modules:
`dim_k S^μ = #SYT(μ)` (Sagan, *The Symmetric Group*, Thm 2.5.2).

This file is a **strategic scaffold**, not a full proof. The headline theorem
`specht_finrank_eq_numSYT` is reduced — *sorry-free* — to the existence of a
`Module.Basis (StandardYoungTableau μ) k (Specht.SpechtSubmodule μ)` (the
standard polytabloid basis; `Basis` lives in the `Module` namespace in this
Mathlib). That basis is assembled from its two classical defining facts via
`Module.Basis.mk`; **those two facts are the only honest content stubs.**

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

/-! ## 3. The two genuine content obligations (honest stubs) -/

/-- **STUB — content obligation 1/2.** The standard polytabloids are linearly
independent in `M^μ` (equivalently, in `S^μ`). Classical: independence follows
from the *dominance / last-letter* ordering on tableaux — the leading tabloid of
each standard `e_T` is distinct, so no nontrivial combination vanishes.

Phrased on the corestricted family `standardPolytabloidS` (valued in `S^μ`), as
required by `Basis.mk`. -/
theorem standardPolytabloid_linearIndependent :
    LinearIndependent k (standardPolytabloidS (k := k) (μ := μ)) := by
  -- Ref: [sagan2001] Thm 2.5.2 (the standard polytabloids are linearly
  -- independent; dominance-order / last-letter argument). See also
  -- [james1984representation] §8. Genuine content obligation; brick-4 target.
  sorry

/-- **STUB — content obligation 2/2.** The standard polytabloids *span* the
Specht module `S^μ`. Classical: every polytabloid `e_t` (arbitrary tableau `t`)
is, by the **Garnir relations**, a `ℤ`-combination of standard ones, so the
standard family generates the same span as all polytabloids — which is `S^μ` by
definition (`SpechtSubmodule = span (range polytabloid)`). -/
theorem standardPolytabloid_span :
    Submodule.span k (Set.range (standardPolytabloidS (k := k) (μ := μ))) = ⊤ := by
  -- Ref: [sagan2001] §2.6 (Garnir relations) + Thm 2.5.2 (standard basis spans
  -- S^μ). See also [james1984representation] §8. Genuine content obligation;
  -- brick-4 target.
  sorry

/-! ## 4. The basis + the reduction (sorry-free MODULO §3) -/

/-- **The standard polytabloid basis** of `S^μ`, indexed by `StandardYoungTableau μ`.

Assembled by `Basis.mk` from the two §3 facts:
* `standardPolytabloid_linearIndependent` (independence), and
* `standardPolytabloid_span` (spanning, with the `≥ ⊤` direction supplied as
  required by `Basis.mk`).

This definition is **sorry-free apart from those two named inputs** — all the
`Basis.mk` plumbing (corestriction to `S^μ`, the `span ≥ ⊤` reshaping) is
discharged here. -/
noncomputable def standardBasis :
    Module.Basis (StandardYoungTableau μ) k (Specht.SpechtSubmodule (k := k) μ) :=
  Module.Basis.mk standardPolytabloid_linearIndependent
    (by rw [standardPolytabloid_span])

/-- **Standard-basis theorem (reduction).**
`dim_k S^μ = #SYT(μ)`.

Proved sorry-free *from* `standardBasis` via `Module.finrank_eq_nat_card_basis`
(which gives `finrank = Nat.card ι` directly, with no `Fintype` on the index),
and `numSYT μ = Nat.card (StandardYoungTableau μ)` definitionally. Hence the only
unproved inputs are the two classical facts of §3. -/
theorem specht_finrank_eq_numSYT (μ : YoungDiagram) :
    Module.finrank k (Specht.SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ := by
  rw [Module.finrank_eq_nat_card_basis (standardBasis (k := k) (μ := μ))]
  rfl

end QOU.BraidKnot.SpechtStandardBasis
