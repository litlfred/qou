/-
Copyright (c) 2026 litlfred. All rights reserved.

# Derived character catalogue — Lean schema (Phase 4 scaffold, 2026-06-07)

> **Lean side of the 3-axis (knot, partition, atom) derived-χ catalogue**
> implemented in Python at
> [`folio-assistant/computations/derived_chi_catalogue.py`](../../../../../folio-assistant/computations/derived_chi_catalogue.py)
> (PR #1952). This module gives the catalogue a Lean type-level
> presence: a `KnotPartitionAtomCell` structure mirroring the Python
> schema, conditional classes for R-matrix derivation provenance, and
> a worked instance (the Borromean / (2,1) / baryon cell that
> cross-validates T17 in PR #1933).

## What this provides

- `KnotPartitionAtomCell` — a `structure` carrying every catalogue
  field at the type level.
- `IsRMatrixDerived` — a conditional class (§3b-cond) marking a cell
  as derived from the R-matrix on V⊗ⁿ + Schur-Weyl projection.
- `borromean_two_one_baryon` — the first instance, recording T17's
  result `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶` (Kassel) /
  `−q¹² + 3q⁸ − 3q⁴ + 4 − 3q⁻⁴ + 3q⁻⁸ − q⁻¹²` (Kauffman, factor 2
  in q-degree).

## Provenance ladder

Per the Python schema's `tier` field, three provenance levels are
exposed at the type level via separate marker classes:

  `DerivedTier`        : structural derivation (R-matrix + LR + …)
  `CalAnchoredTier`    : extracted from CODATA (circular, not a
                         prediction)
  `ExtractedTier`      : back-solved from related compute (weaker
                         than cal-anchored)

Only `DerivedTier` cells are safe to consume as predictions; this
mirrors the Python `lookup_derived` failing-loud guard.

## Cross-refs

- Catalogue work-plan:
  [`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`](../../../../../docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md)
- T17 R-matrix derivation (PR #1933): `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶`
- LR / parabolic factorisation roadmap (Tier 1):
  [`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../../../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)
-/
import Mathlib.Data.Rat.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import QOU.BraidsAndKnots.BorromeanChiPerRep

namespace QOU.Machinery

/-! ## Q-convention enum

Mirrors `derived_chi_catalogue.QConvention`. Captures whether
`χ^λ(β_K)` is stored in Kassel (skein) or Kauffman (`t = q²`)
variable. Production Rust cells use Kauffman; legacy sympy cells
use Kassel. -/

/-- Two conventions for the catalogue's Laurent-in-q storage. -/
inductive QConvention where
  | kauffman : QConvention  -- t = q² (pyhecke_native native)
  | kassel : QConvention    -- skein variable (sympy R-matrix legacy)
deriving DecidableEq, Repr

/-! ## Provenance tier enum

Mirrors `derived_chi_catalogue.Tier`. Captures the source of a
catalogue cell. Only `derived` cells are safe to consume as
predictions. -/

/-- Three provenance tiers per CLAUDE.md `tier` discipline. -/
inductive Tier where
  | derived : Tier        -- structural derivation, safe to consume
  | calAnchored : Tier    -- extracted from CODATA, circular
  | extracted : Tier      -- back-solved from related compute
deriving DecidableEq, Repr

/-! ## Per-cell record (mirrors `KnotPartitionAtomCell`) -/

/-- A catalogue cell identifies a (knot K, partition λ, atom A) triple
and stores the derived character data plus provenance.

This is the Lean schema mirror of the Python
`KnotPartitionAtomCell` dataclass. Fields are kept as primitive types
(strings, integer lists, etc.) so the schema can be ported across the
Python/Lean boundary without bringing in heavy algebra. -/
structure KnotPartitionAtomCell where
  /-- Knot operator name (from the PR #1677 census or atom-braid prefix). -/
  knot : String
  /-- Partition λ ⊢ n_K as a non-increasing list of positive ints. -/
  partition : List Nat
  /-- QOU atom / observable target (e.g. "borromean-baryon", "5Li"). -/
  atom : String
  /-- Canonical braid word for K in B_{n_K}, as a pretty string. -/
  braidWord : String
  /-- n_K, the strand count of the braid representative. -/
  strandCount : Nat
  /-- χ^λ(β_K)(q) as a Laurent in q: list of (q_degree, coefficient_string)
  pairs. Negative q_degree allowed. Convention stored in `qConvention`. -/
  chiLambdaQLaurent : List (Int × String)
  /-- Variable convention for `chiLambdaQLaurent`. -/
  qConvention : QConvention
  /-- Per-partition truncation order `k_λ` per
  `prop:per-partition-k-lambda-rule`. -/
  kLambda : Nat
  /-- Provenance tier (see `Tier`). -/
  tier : Tier
  /-- Citation: commit-sha or audit-doc path of the structural derivation. -/
  derivationRef : String

/-! ## Conditional class — R-matrix derivation

§3b-cond pattern: cells whose χ^λ was computed via the R-matrix
template (T17 / PR #1933) carry this class. The instance is the
proof that the cell's stored data agrees with the R-matrix output.
NEAR-MATCH tier; instance fully verified only once a complete
parabolic-restriction proof is in place. -/

/-- A cell is R-matrix-derived when its stored `χ^λ` (as a genuine
`ℚ → ℚ` Laurent evaluation, `storedChi`) agrees, away from `q = 0`,
with the categorical R-matrix character `rmatrixChi` obtained from the
T17 template (R-matrix on `V⊗ⁿ` + Schur-Weyl projection to the
`λ`-block + trace).

This is a genuine §3b-cond conditional class — its fields carry real
`R → R` data (generic over a field `R`, §7c) and a real equality `Prop`,
not an opaque `True` marker.
The instance for `borromeanTwoOneBaryon` is **fully discharged** (no
`sorry`): `agrees` is the proven theorem `borromeanTwoOneBaryonChi_eq_t17`,
which reuses T17's `chi21_borromean_qform_eq_hform`.

HONESTY (mirrors the `BorromeanChiPerRep.lean` scope note): the proven
content is `storedChi = rmatrixChi` at the level of *q-rational forms*.
That `rmatrixChi` is itself the categorical R-matrix trace (rather than
just the published h-polynomial) is, at the time of writing,
NARRATIVE-ONLY for the seminormal Hecke-representation step — it is
independently confirmed numerically (≤ 4e-50) by
`borromean_chi_independent_crosscheck.py`. The class therefore certifies
the catalogue cell against the *formalised* T17 polynomial, not against
an in-Lean construction of the seminormal representation. -/
class IsRMatrixDerived (R : Type*) [Field R] (cell : KnotPartitionAtomCell) :
    Prop where
  /-- A genuine `R → R` evaluation of the cell's stored Laurent
  `chiLambdaQLaurent` (in the Kauffman variable). Generic over a field
  `R` per §7c — no ordering / `Real.*` is involved, only the inverses
  the Laurent needs. -/
  storedChi : R → R
  /-- The categorical R-matrix character `χ^λ(β_K)` this cell realises,
  as a `q`-rational function (T17 template). -/
  rmatrixChi : R → R
  /-- The stored Laurent agrees with the R-matrix character at every
  nonzero `q`. -/
  agrees : ∀ q : R, q ≠ 0 → storedChi q = rmatrixChi q

/-! ## Conditional class — LR / parabolic factorisation derivation

A cell whose χ^λ comes from the Tier 1 LR + parabolic + bridge
factorisation (audit doc
`2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`). Used
once Phase 1.1 (deuteron base case) lands and downstream atoms
inherit it. -/

/-- A cell is LR-factorised-derived when its χ^λ was computed via the
parabolic restriction + LR-multi-coefficient + bridge-factor `ω`
formula. NEAR-MATCH tier; instance gated on Phase 1.1 of the Tier 1
roadmap. -/
class IsLRFactorisedDerived (cell : KnotPartitionAtomCell) : Prop where
  /-- Opaque marker; instance not constructed until the bridge factor
  table `ω_{μ_p, μ_n, λ}(q)` is rigorously derived for the deuteron
  base case. -/
  lrEquivalence : True

/-! ## First instance — Borromean (2,1) baryon (T17 cross-validated)

Worked example: the T17 result, recorded as a Lean cell with
`IsRMatrixDerived` instance. Q-convention here is Kauffman to match
the production Rust output; the Kassel form `2 − 3h⁴ − h⁶` is cited
in the derivationRef. -/

/-- The Borromean / (2,1) / baryon cell, recording T17's R-matrix
derivation in Kauffman convention. The Laurent encoding
`−q¹² + 3q⁸ − 3q⁴ + 4 − 3q⁻⁴ + 3q⁻⁸ − q⁻¹²` is the q-doubled form
of the Kassel polynomial `χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶` (with
h = q − q⁻¹). -/
def borromeanTwoOneBaryon : KnotPartitionAtomCell where
  knot := "borromean"
  partition := [2, 1]
  atom := "borromean-baryon"
  braidWord := "(σ_1⁻¹·σ_2)³"
  strandCount := 3
  chiLambdaQLaurent := [
    (-12, "-1"), (-8, "3"), (-4, "-3"), (0, "4"),
    (4, "-3"), (8, "3"), (12, "-1"),
  ]
  qConvention := QConvention.kauffman
  kLambda := 1
  tier := Tier.derived
  derivationRef :=
    "PR #1933 (T17 R-matrix on V⊗3); independent re-derivation in "
    ++ "folio-assistant/computations/derived_chi_catalogue_build.py "
    ++ "(Kassel form 2 − 3h⁴ − h⁶ with h = q − q⁻¹)"

/-- Genuine `ℚ → ℚ` evaluation of `borromeanTwoOneBaryon.chiLambdaQLaurent`
(hand-transcribed from the cell's `(q_degree, coeff)` pairs
`[(-12,-1),(-8,3),(-4,-3),(0,4),(4,-3),(8,3),(12,-1)]` to avoid string
parsing in Lean — degrees are in the Kauffman variable `t = q²`). -/
def borromeanTwoOneBaryonChi {R : Type*} [Field R] (q : R) : R :=
  -q^12 + 3*q^8 - 3*q^4 + 4 - 3/q^4 + 3/q^8 - 1/q^12

/-- **T17 is the first catalogue instance.** The stored Kauffman Laurent
of the Borromean `(2,1)` cell equals T17's published h-form
`2 − 3h⁴ − h⁶` evaluated at `q²` (the Kauffman `t = q²` substitution),
for every nonzero `q` in any field. The proof reuses T17's proven
form-equivalence `chi21_borromean_qform_eq_hform`. -/
theorem borromeanTwoOneBaryonChi_eq_t17 {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    borromeanTwoOneBaryonChi q
      = QOU.BraidsAndKnots.chi21_borromean_hform (q ^ 2) := by
  have hq2 : (q ^ 2 : R) ≠ 0 := pow_ne_zero 2 hq
  rw [← QOU.BraidsAndKnots.chi21_borromean_qform_eq_hform (q ^ 2) hq2]
  unfold borromeanTwoOneBaryonChi QOU.BraidsAndKnots.chi21_borromean_qform
  field_simp
  ring

/-- The Borromean / (2,1) / baryon cell is R-matrix-derived. The instance
is **fully discharged** (no `sorry`): `agrees` is the proven theorem
`borromeanTwoOneBaryonChi_eq_t17`, with `rmatrixChi` set to the T17
h-form in the Kauffman variable. -/
instance {R : Type*} [Field R] : IsRMatrixDerived R borromeanTwoOneBaryon where
  storedChi := borromeanTwoOneBaryonChi
  rmatrixChi := fun q => QOU.BraidsAndKnots.chi21_borromean_hform (q ^ 2)
  agrees := borromeanTwoOneBaryonChi_eq_t17

/-! ## Basic invariants -/

/-- The Borromean / (2,1) / baryon cell is tagged `derived`. -/
theorem borromean_two_one_baryon_is_derived :
    borromeanTwoOneBaryon.tier = Tier.derived := rfl

/-- The Borromean / (2,1) / baryon cell uses the Kauffman convention. -/
theorem borromean_two_one_baryon_kauffman :
    borromeanTwoOneBaryon.qConvention = QConvention.kauffman := rfl

/-- Sanity: the partition `[2, 1]` sums to the strand count `3`. -/
theorem borromean_two_one_baryon_partition_sum :
    borromeanTwoOneBaryon.partition.sum = borromeanTwoOneBaryon.strandCount := by
  rfl

end QOU.Machinery
