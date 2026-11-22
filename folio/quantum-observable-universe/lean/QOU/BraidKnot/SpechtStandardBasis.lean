import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import QOU.BraidKnot.SpechtStandardBasisCore
import QOU.BraidKnot.SpechtTriangularCore

/-!
# QOU.BraidKnot.SpechtStandardBasis — brick 4 of the Okounkov–Vershik tower (capstone)

The **standard-basis theorem** for Specht modules:
`dim_k S^μ = #SYT(μ)` (Sagan, *The Symmetric Group*, Thm 2.5.2).

This is the **capstone** half of brick 4. All of the objects (SYT→tableau
conversion, standard polytabloids, the abstract `Triangular` lever, corestriction,
spanning half) live one layer down in
[`SpechtStandardBasisCore`](./SpechtStandardBasisCore.lean); the two independence
cores ([`SpechtDominanceCore`](./SpechtDominanceCore.lean),
[`SpechtTriangularCore`](./SpechtTriangularCore.lean)) sit between them and this
file. Everything is declared in the **same** `QOU.BraidKnot.SpechtStandardBasis`
namespace across the three files, so external references are unchanged.

## The triangular core is now *consumed*, not stubbed

Historically `standardPolytabloid_triangular` was an honest `sorry` here (the
dominance core, cited to Sagan Thm 2.5.2). That core has since been **proved
sorry-free** in `SpechtTriangularCore.standardPolytabloid_triangular'`
(independence, modulo only the relation-level dominance lemma
`SpechtDominanceCore.dominance_relation_exists`). Because that proof lives in a
module that *imports* the brick-4 definitions, it could not be consumed from the
old single-file layout without a circular import; the definitions were therefore
split into `SpechtStandardBasisCore`, and this file — now sitting *above* the
cores — proves `standardPolytabloid_triangular` by **directly consuming** the
already-proved `standardPolytabloid_triangular'`.

Net effect: `standardPolytabloid_triangular` carries **no independence `sorry`**.
Both former brick-4 stubs — the dominance core and the spanning / straightening
core `standardPolytabloid_straightening` — have since been discharged, so the whole
chain is now sorry-free outright.

## sorry-free map (machine-checked)

Every row verified by `#print axioms`, each yielding exactly
`[propext, Classical.choice, Quot.sound]` — **no `sorryAx`**.

| Declaration | Status |
|---|---|
| `standardPolytabloid_triangular` | **PROVED** (`:= SpechtTriangularCore.standardPolytabloid_triangular'`) |
| `standardPolytabloid_linearIndependent` | **sorry-free** (via the proved triangular) |
| `standardPolytabloid_span` (in Core) | **sorry-free** (Garnir straightening, via `straightening_step_colMax`) |
| `standardBasis` | **sorry-free** |
| `specht_finrank_eq_numSYT` | **sorry-free** |

Note `[CharZero k]` is **required** on `specht_finrank_eq_numSYT` (it consumes
`standardBasis`); it must not be `omit`ted.

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

/-! ## 3a. Linear independence — now consuming the PROVED triangular core -/

omit [CharZero k] in
/-- **The triangular family exists — PROVED.** There is a linear extension of
dominance on `Tabloid μ` under which the standard polytabloids form a `Triangular`
family with the concrete leading map `leadTab`. Historically the irreducible
combinatorial core of brick 4 (an honest `sorry` cited to Sagan Thm 2.5.2); now
**proved sorry-free** by directly consuming the reassembled bundle
`SpechtTriangularCore.standardPolytabloid_triangular'` (which discharges the two
order-independent fields `diag_unit`, `lead_inj` fully and reduces `supp_le` to the
relation-level dominance lemma `SpechtDominanceCore.dominance_relation_exists`). -/
theorem standardPolytabloid_triangular :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      Triangular (standardPolytabloid (k := k) (μ := μ)) (leadTab (μ := μ)) :=
  SpechtTriangularCore.standardPolytabloid_triangular' (k := k) (μ := μ)

omit [CharZero k] in
/-- **Content obligation 1/2 — linear independence**, now derived **sorry-free modulo
the single dominance core** via the proved `standardPolytabloid_triangular` (the
triangular lever + the corestriction reduction discharge everything else). Phrased on
the corestricted family `standardPolytabloidS` (valued in `S^μ`), as required by
`Basis.mk`. -/
theorem standardPolytabloid_linearIndependent :
    LinearIndependent k (standardPolytabloidS (k := k) (μ := μ)) := by
  refine linearIndependent_corestrict_iff.mpr ?_
  obtain ⟨_inst, htri⟩ := standardPolytabloid_triangular (k := k) (μ := μ)
  exact htri.linearIndependent

/-! ## 4. The basis + the reduction (sorry-free MODULO the dominance + spanning cores) -/

/-- **The standard polytabloid basis** of `S^μ`, indexed by `StandardYoungTableau μ`.

Assembled by `Basis.mk` from:
* `standardPolytabloid_linearIndependent` (independence, via the proved triangular
  core), and
* `standardPolytabloid_span` (spanning, with the `≥ ⊤` direction supplied as
  required by `Basis.mk`).

This definition is **sorry-free apart from the dominance core + the spanning stub**
— all the `Basis.mk` plumbing (corestriction to `S^μ`, the `span ≥ ⊤` reshaping) is
discharged in the core file. -/
noncomputable def standardBasis :
    Module.Basis (StandardYoungTableau μ) k (Specht.SpechtSubmodule (k := k) μ) :=
  Module.Basis.mk standardPolytabloid_linearIndependent
    (by rw [standardPolytabloid_span])

/-- **Standard-basis theorem (reduction).**
`dim_k S^μ = #SYT(μ)`.

Proved sorry-free *from* `standardBasis` via `Module.finrank_eq_nat_card_basis`
(which gives `finrank = Nat.card ι` directly, with no `Fintype` on the index),
and `numSYT μ = Nat.card (StandardYoungTableau μ)` definitionally. Hence the only
unproved inputs are the dominance core (now consumed by the proved triangular) and
`standardPolytabloid_straightening` (spanning).

Carries `[CharZero k]`, inherited from `standardBasis`. This declaration previously
bore an `omit [CharZero k] in`, which made the file fail to compile: the proof
applies `standardBasis`, which genuinely takes the instance, so the omitted binder
left `CharZero k` unsynthesizable at the application. The generality the `omit`
asserted was never established — dropping it is what the existing proof supports.
(The standard-polytabloid basis does exist over an arbitrary field, so the
hypothesis is likely removable, but that needs the `CharZero` uses inside
`standardBasis`'s own inputs traced and discharged — not an annotation change.) -/
theorem specht_finrank_eq_numSYT (μ : YoungDiagram) :
    Module.finrank k (Specht.SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ := by
  rw [Module.finrank_eq_nat_card_basis (standardBasis (k := k) (μ := μ))]
  rfl

/-- Zero-subtracted difference between the standard-basis Specht finrank and `numSYT μ` vanishes. -/
theorem specht_finrank_sub_numSYT_eq_zero (μ : YoungDiagram) :
    Module.finrank k (Specht.SpechtSubmodule (k := k) μ) - QOU.BraidKnot.numSYT μ = 0 := by
  rw [specht_finrank_eq_numSYT (k := k) μ]
  exact Nat.sub_self (QOU.BraidKnot.numSYT μ)

end QOU.BraidKnot.SpechtStandardBasis
