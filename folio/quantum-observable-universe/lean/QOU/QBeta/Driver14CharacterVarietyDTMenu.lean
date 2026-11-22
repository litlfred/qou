import Init.Data.Nat.Basic
import Init.Data.Int.Basic
import Init.Data.List.Basic
import Init.Omega

/-!
# QOU.QBeta.Driver14CharacterVarietyDTMenu — Route-1 cross-knot exclusion: no QOU scalar driver-integer reproduces the character-variety DT count, and the count is inherently chirality-refined

**Branch `claude/driver-14-character-variety-dt-moduli-2026-08-02`.**
Audit: `docs/audits/2026-08-02-driver-14-character-variety-dt-moduli-constructibility.md`.

## The question this file answers (formalize-first, honest negative)

The arc ledger (`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`,
"How to resolve — routes") names the **tractable, decidable, still-UNCHECKED**
Route 1: does a categorical q→0 DT count from Hecke/Bring data (drivers 11/13)
reproduce the character-variety DT datum `4₁ ↦ 3`, `5₂ ↦ {3,4}`? Deciding it is
the concrete test for whether the missing **"driver-14"** — a Behrend-weighted DT
moduli of the character variety / `T[K]` BPS Hilbert space (#4599) — is
constructible from the drivers, even as a fragment.

`StokesDTCountExceedsRecursionOrder` (#4599) already showed the two *specific*
QOU integers it examined miss the `4₁` count (`partitionEuler₃ = −2 ≠ 3`;
`recursionOrder 4₁ = 2 < 3`). `FiveTwoDTSpectrumSplit` (#4593) showed the `5₂`
datum is a genuine **chirality-split 2-element spectrum** (`4` in `S⁺`, `3` in
`S⁻`), not a knot-independent scalar. This file **consolidates Route 1**: it runs
the *whole menu* of QOU-derivable (and, for good measure, classical) knot
integers against the cross-knot DT datum and proves

1. **no menu invariant reproduces the DT count vector** `(4₁,5₂) ↦ (3,4)`
   (`no_menu_invariant_hits_dt_vector`), and
2. **the deeper obstruction is a *cardinality / chirality-refinement* mismatch**:
   the `5₂` DT datum is a 2-element set, while every QOU scalar driver invariant is
   single-valued per knot, so **no scalar invariant can equal the DT datum**
   (`no_scalar_matches_chirality_split_datum`). The missing driver-14 count is
   therefore inherently a **chirality-refined (set-valued) moduli count** — an
   object no scalar Wedderburn Euler characteristic / recursion order / block count
   supplies.

This is a **scope-(a) structural negative**. It derives NO count, axiomatizes NO
DT moduli, and — crucially — it does **NOT** assert the 2-point coincidence
`dtMax K = recursionOrder K + 1` (`4₁`: `2+1=3`; `5₂`: `3+1=4`) as a law: two
knots always admit a linear fit, the `+1` reads as the *abelian branch* of the
character variety (imported exponential-network geometry, not a QOU driver), and
it is recorded in the audit as an **unclaimed probe needing a third-knot
(`3₁`/`6₁`) check**, never a Lean theorem. Nothing fitted, nothing wired.
Core-Lean only (no Mathlib olean); every fact is `decide`/`omega`-checkable.

-- Ref: [garoufalidis-gu-marino2023peacock] GGM 2012.00062 (S⁺(0) for 4₁, 5₂ blocks; DT/3d-index count)
-- Ref: [nguyen-tran-2021] strong AJ for 4₁ (recursion order 2 = A-polynomial L-degree 2)
-- Ref: [leitner2026] docs/audits/2026-08-02-driver-14-character-variety-dt-moduli-constructibility.md
-/

namespace QOU.QBeta.Driver14CharacterVarietyDTMenu

/-- The two keystone knots: amphichiral `4₁` (muon anchor), chiral `5₂`. -/
inductive KKnot
  | fourOne
  | fiveTwo
deriving DecidableEq

open KKnot

/-! ## The character-variety DT datum (imported GGM values — recorded, not derived) -/

/-- **The imported character-variety Behrend/BPS DT datum**, as the *set* of
leading off-diagonal Stokes integers. `4₁` (amphichiral) carries the single
integer `3` (`StokesQZeroDTCount`: `S⁺(0)₀₁ = 3`). `5₂` (chiral) carries the
**chirality-split** pair `{3,4}` — `4` in `S⁺(0)`, `3` in `S⁻(0)`
(`FiveTwoDTSpectrumSplit`, certified matrices). These are *imported* geometric
counts (spectral curve `A_K = 0` / rotated 3d-index of `T[K]`), recorded only to
test the QOU driver menu against them. -/
def dtDatum : KKnot → List Int
  | fourOne => [3]
  | fiveTwo => [4, 3]

/-- The maximal DT off-diagonal count per knot (the `dtOffDiagMax` of #4599):
`4₁ ↦ 3`, `5₂ ↦ 4`. -/
def dtMax : KKnot → Int
  | fourOne => 3
  | fiveTwo => 4

/-! ## The QOU-driver integer menu (all internally derivable) + a classical control set

Each entry is a knot-indexed integer the framework (or classical knot theory)
supplies. The point of the menu is that it is *complete* for the natural
scalar integers: if none hits the DT datum, the count is not any of them. -/

/-- Wedderburn block count: both `4₁` and `5₂` are 3-braids, home `H₃(q)`, whose
blocks are the 3 partitions `λ ⊢ 3`. Knot-**independent** (`3,3`). -/
def blockCountH3 : KKnot → Int := fun _ => 3

/-- `|Σ_{λ⊢3} Δ_λ|`, the QOU Wedderburn/Springer signed-Euler total over `H₃`
(`= |−2| = 2`, `partitionEuler₃` of #4599). Knot-independent (`2,2`). -/
def partitionEulerAbs : KKnot → Int := fun _ => 2

/-- QOU-owned recursion order = order of the AJ `q`-difference annihilator
= `A`-polynomial `L`-degree = GGM Stokes-matrix dimension. `4₁ ↦ 2`
(proved sorry-free `AJFigureEightAnnihilation`), `5₂ ↦ 3`. -/
def recursionOrder : KKnot → Int
  | fourOne => 2
  | fiveTwo => 3

/-- Classical control invariants (crossing number, knot determinant `|Δ_K(−1)|`,
minimal ideal-tetrahedron count, braid index, Seifert genus). Included to show the
DT count is not *any* natural knot integer, QOU-derived or classical. -/
def crossingNumber : KKnot → Int | fourOne => 4 | fiveTwo => 5
def determinant    : KKnot → Int | fourOne => 5 | fiveTwo => 7
def idealTetrahedra: KKnot → Int | fourOne => 2 | fiveTwo => 3
def braidIndex     : KKnot → Int := fun _ => 3
def seifertGenus   : KKnot → Int := fun _ => 1

/-- **The menu**, as the list of its `(f 4₁, f 5₂)` value-vectors. -/
def menuVectors : List (Int × Int) :=
  [ (blockCountH3 fourOne, blockCountH3 fiveTwo),        -- (3,3)
    (partitionEulerAbs fourOne, partitionEulerAbs fiveTwo), -- (2,2)
    (recursionOrder fourOne, recursionOrder fiveTwo),     -- (2,3)
    (crossingNumber fourOne, crossingNumber fiveTwo),     -- (4,5)
    (determinant fourOne, determinant fiveTwo),           -- (5,7)
    (idealTetrahedra fourOne, idealTetrahedra fiveTwo),   -- (2,3)
    (braidIndex fourOne, braidIndex fiveTwo),             -- (3,3)
    (seifertGenus fourOne, seifertGenus fiveTwo) ]        -- (1,1)

/-- The DT count vector to hit: `(dtMax 4₁, dtMax 5₂) = (3,4)`. -/
def dtVector : Int × Int := (dtMax fourOne, dtMax fiveTwo)

theorem dtVector_eq : dtVector = (3, 4) := by decide

/-! ## Part 1 — no menu invariant reproduces the DT count vector `(3,4)` -/

/-- **Route-1 cross-knot exclusion.** No integer in the QOU driver menu (nor in
the classical control set) has value-vector `(3,4)` over `(4₁, 5₂)`: every menu
vector differs from `dtVector`. So no single natural scalar knot-integer — Hecke
block count, Wedderburn Euler total, AJ recursion order, crossing, determinant,
tetrahedra, braid index, genus — reproduces the character-variety DT count. -/
theorem no_menu_invariant_hits_dt_vector :
    ∀ v ∈ menuVectors, v ≠ dtVector := by decide

/-- Explicit corollary form: the two genuinely QOU-derivable non-constant scalars
(block count / Euler total are knot-independent, so cannot even *vary* with the
knot; recursion order varies but as `(2,3)`) all miss `(3,4)`. -/
theorem qou_scalars_miss_dt_vector :
    (blockCountH3 fourOne, blockCountH3 fiveTwo) ≠ dtVector ∧
    (partitionEulerAbs fourOne, partitionEulerAbs fiveTwo) ≠ dtVector ∧
    (recursionOrder fourOne, recursionOrder fiveTwo) ≠ dtVector := by decide

/-! ## Part 2 — the deeper obstruction: the DT count is chirality-refined (set-valued),
    every QOU scalar invariant is single-valued -/

/-- The `5₂` DT datum has **two distinct** members (`4 ≠ 3`) — the chirality split
of `FiveTwoDTSpectrumSplit`. -/
theorem dtDatum_fiveTwo_two_distinct :
    (4 : Int) ∈ dtDatum fiveTwo ∧ (3 : Int) ∈ dtDatum fiveTwo ∧ (4 : Int) ≠ 3 := by
  decide

/-- A **scalar** knot invariant `f : KKnot → Int` produces a single value per knot;
its associated one-element datum `[f K]` has all members equal. -/
theorem scalar_datum_single_valued (f : KKnot → Int) (K : KKnot) :
    ∀ a ∈ [f K], ∀ b ∈ [f K], a = b := by
  intro a ha b hb
  simp only [List.mem_singleton] at ha hb
  omega

/-- **The chirality-refinement obstruction (the precise missing driver-14 input).**
No scalar knot invariant `f : KKnot → Int` has its one-element datum `[f 5₂]` equal
(as a set) to the `5₂` DT datum `{3,4}`: matching would force `f 5₂ = 4` and
`f 5₂ = 3`, i.e. `4 = 3`. Hence the character-variety DT count is **not** any scalar
Euler characteristic / recursion order / block count; supplying it requires a
**chirality-refined, set-valued moduli count** — an object outside the scalar-integer
range of the 13 drivers. This is the sharpened, formalized name of the missing
"driver-14". -/
theorem no_scalar_matches_chirality_split_datum (f : KKnot → Int) :
    ¬ (∀ x : Int, (x ∈ dtDatum fiveTwo ↔ x ∈ [f fiveTwo])) := by
  intro h
  -- 4 ∈ dtDatum 5₂ ⇒ 4 ∈ [f 5₂] ⇒ f 5₂ = 4
  have h4 : (4 : Int) ∈ [f fiveTwo] := (h 4).mp (by decide)
  have h3 : (3 : Int) ∈ [f fiveTwo] := (h 3).mp (by decide)
  simp only [List.mem_singleton] at h4 h3
  omega

/-! ## Part 3 — packaged verdict -/

/-- **Formalize-first honest verdict (Route 1).** Neither reading of "driver-14
supplies the DT count" holds from the QOU scalar drivers: (1) no menu invariant hits
the count vector `(3,4)`, and (2) — the deeper obstruction — the `5₂` count is a
chirality-split 2-set, which no single-valued scalar invariant can equal. The
Behrend-weighted character-variety DT count is therefore **not constructible as a
scalar QOU invariant**; it is an inherently chirality-refined geometric count of the
spectral curve — external input, exactly as #4599's per-knot negative and the
Rossmann-CC partition-level verdict independently found. -/
theorem driver14_dt_count_not_a_qou_scalar :
    (∀ v ∈ menuVectors, v ≠ dtVector) ∧
    (¬ ∀ x : Int, (x ∈ dtDatum fiveTwo ↔ x ∈ [(fun _ => (3 : Int)) fiveTwo])) :=
  ⟨no_menu_invariant_hits_dt_vector,
   no_scalar_matches_chirality_split_datum (fun _ => 3)⟩

end QOU.QBeta.Driver14CharacterVarietyDTMenu
