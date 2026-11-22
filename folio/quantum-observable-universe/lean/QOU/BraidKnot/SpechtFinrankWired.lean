import QOU.BraidKnot.SpechtTriangularCore

/-!
# QOU.BraidKnot.SpechtFinrankWired — brick-4 `finrank = numSYT`, re-routed onto proved independence

This module rebuilds the standard-basis dimension identity
`dim_k S^μ = #SYT(μ)` of brick 4, but **sources its linear-independence input from the
*proved* triangular core** `SpechtTriangularCore.standardPolytabloid_triangular'`
(independence — fully sorry-free apart from Sagan's relation-level dominance core) rather
than from the opaque brick-2 stub `Specht.specht_finrank_eq_numSYT` (which carries an
opaque `sorry : finrank Sᵘ = numSYT μ`).

Concretely:

* `standardBasis_wired` mirrors `SpechtStandardBasis.standardBasis` — a `Module.Basis.mk`
  of the corestricted standard polytabloids — but its independence half comes from
  `SpechtTriangularCore.standardPolytabloid_triangular'`
  (`obtain ⟨_, htri⟩ := …; htri.linearIndependent`, corestricted via
  `SpechtStandardBasis.linearIndependent_corestrict_iff`), and its spanning half is the
  existing `SpechtStandardBasis.standardPolytabloid_span`.
* `specht_finrank_eq_numSYT_wired` mirrors `SpechtStandardBasis.specht_finrank_eq_numSYT`
  but reads off `standardBasis_wired`.

The net effect on the OV capstone (`OVTopAssembly.snSpectralData`'s `rank` field): after the
capstone's `rank` rewrites with `specht_finrank_eq_numSYT_wired` instead of the brick-2 stub,
the `rank` sorry-path no longer contains the independence stub
`SpechtStandardBasis.standardPolytabloid_triangular` **nor** the opaque brick-2 finrank stub —
its **only** remaining sorry is the spanning / straightening stub
`SpechtStandardBasis.standardPolytabloid_straightening` (via `standardPolytabloid_span`),
plus the relation-level dominance core `SpechtDominanceCore.dominance_relation_exists` that
the *proved* `triangular'` legitimately consumes.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `standardBasis_wired` | **sorry-free MODULO** `triangular'`'s dominance core + the spanning stub |
| `specht_finrank_eq_numSYT_wired` | **sorry-free MODULO** the same two cores |

Independence here flows through the **proved** `triangular'`; there is no independence
`sorry`. The residual `sorry`-tainted inputs are exactly:
1. `SpechtStandardBasis.standardPolytabloid_straightening` (spanning / Garnir straightening), and
2. `SpechtDominanceCore.dominance_relation_exists` (Sagan's dominance lemma, consumed by the
   *proved* `triangular'`).

## Base ring (§7c)

`variable {k : Type} [Field k] [CharZero k]` — algebraic; `Field` is what `Basis.mk` /
`finrank` need, `CharZero` is inherited from the brick-4 signature contract. No `ℝ`, no
`Real.*`, no ordering on `k`.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (the standard basis, Thm 2.5.2).
- [james1984representation] James, *The Representation Theory of the Symmetric Groups* §8.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtFinrankWired

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

-- `CharZero k` is part of the brick-4 signature contract (the capstone instantiates this module at
-- `k := R` with `[Field R] [CharZero R]`); some of the wired theorems do not use it directly, so the
-- unused-section-variable linter flags it.  Keep it (it documents the real contract and matches the
-- brick-4 / capstone interface) and disable the linter for the file rather than drop the typeclass.
set_option linter.unusedSectionVars false

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-- **Linear independence of the corestricted standard polytabloids — sourced from the PROVED
triangular core.** Identical conclusion to
`SpechtStandardBasis.standardPolytabloid_linearIndependent`, but its triangular input is the
*proved* `SpechtTriangularCore.standardPolytabloid_triangular'` (independence) rather than the
opaque stub `SpechtStandardBasis.standardPolytabloid_triangular`. Hence this carries **no
independence `sorry`** — its only sorry-path is the dominance core that `triangular'` itself
legitimately consumes. -/
theorem standardPolytabloid_linearIndependent_wired :
    LinearIndependent k (standardPolytabloidS (k := k) (μ := μ)) := by
  refine linearIndependent_corestrict_iff.mpr ?_
  obtain ⟨_ord, htri⟩ :=
    SpechtTriangularCore.standardPolytabloid_triangular' (k := k) (μ := μ)
  exact htri.linearIndependent

/-- **The standard polytabloid basis of `S^μ`, wired to proved independence.**

Mirrors `SpechtStandardBasis.standardBasis` (a `Module.Basis.mk` of the corestricted standard
polytabloids), but its independence half is `standardPolytabloid_linearIndependent_wired`
(sourced from the *proved* `triangular'`) and its spanning half is the existing
`SpechtStandardBasis.standardPolytabloid_span`. Sorry-free apart from the spanning stub and the
dominance core consumed by `triangular'`. -/
noncomputable def standardBasis_wired :
    Module.Basis (StandardYoungTableau μ) k (Specht.SpechtSubmodule (k := k) μ) :=
  Module.Basis.mk standardPolytabloid_linearIndependent_wired
    (by rw [standardPolytabloid_span])

/-- **Standard-basis dimension theorem (wired).** `dim_k S^μ = #SYT(μ)`, read off
`standardBasis_wired`. Mirrors `SpechtStandardBasis.specht_finrank_eq_numSYT`, but its
independence input is the *proved* triangular core — so this declaration's sorry-path is the
spanning stub + dominance core only, and does **not** include the opaque brick-2 finrank stub
`Specht.specht_finrank_eq_numSYT`. -/
theorem specht_finrank_eq_numSYT_wired (μ : YoungDiagram) :
    Module.finrank k (Specht.SpechtSubmodule (k := k) μ) = QOU.BraidKnot.numSYT μ := by
  rw [Module.finrank_eq_nat_card_basis (standardBasis_wired (k := k) (μ := μ))]
  rfl

/-- Zero-subtracted difference between the wired Specht submodule finrank and `numSYT μ` vanishes. -/
theorem specht_finrank_sub_numSYT_wired_eq_zero (μ : YoungDiagram) :
    Module.finrank k (Specht.SpechtSubmodule (k := k) μ) - QOU.BraidKnot.numSYT μ = 0 := by
  rw [specht_finrank_eq_numSYT_wired (k := k) μ]
  exact Nat.sub_self (QOU.BraidKnot.numSYT μ)

end QOU.BraidKnot.SpechtFinrankWired
