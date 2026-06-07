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

/-- A cell is R-matrix-derived when its χ^λ was computed via the
T17 template: R-matrix on V⊗ⁿ + Schur-Weyl projection to the
λ-block + trace. The marker field is `True` at this scaffolding
level; the actual proof of equivalence between the stored Laurent
and the categorical computation is left to a follow-up. -/
class IsRMatrixDerived (cell : KnotPartitionAtomCell) : Prop where
  /-- Opaque marker for "this cell's stored χ^λ equals the R-matrix
  computation of `χ^λ(β_K)` on the parabolic block specified by
  `partition`, in the convention `qConvention`". -/
  rmatrixEquivalence : True

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

/-- The Borromean / (2,1) / baryon cell satisfies the R-matrix
derivation marker. -/
instance : IsRMatrixDerived borromeanTwoOneBaryon where
  rmatrixEquivalence := trivial

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
