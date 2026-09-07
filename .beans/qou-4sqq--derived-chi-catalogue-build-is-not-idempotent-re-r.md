---
# qou-4sqq
title: derived_chi_catalogue_build is not idempotent — re-running duplicates its own cells
status: completed
type: bug
priority: normal
created_at: 2026-09-06T10:15:38Z
updated_at: 2026-09-07T09:54:41Z
---

Surfaced by the qou-hu1f regeneration pass. Pre-existing since at least 2026-06-07.

## Measured

    ValueError: duplicate catalogue cell ('borromean', (3,), 'borromean-baryon');
    re-derive or update the existing record explicitly.

`derived_chi_catalogue_build.py` calls `load_catalogue()` and then `cat.add(c)`
for cells it re-derives. `DerivedChiCatalogue.add` refuses a repeated
`(knot, partition, atom)` key by design. The committed
`derived-chi-catalogue.witness.json` is dated **2026-06-07**, holds **342
cells**, and already contains the key — so the builder has been unable to run
against its own output for three months.

## NOT the intra-ordering ruling, despite appearances

The duplicate key contains the string `borromean`, and I initially misread that
as the `intra_order="borromean"` default. It is not: `'borromean'` here is a
**knot** name, built from the hardcoded braid word `[-1, +2, -1, +2, -1, +2]`
= `(σ₁⁻¹σ₂)³`. The collision with the ordering's name is coincidental.
Confirmed by running under both orderings — fails identically.

## The decision this needs

The guard is deliberate and its message says so: *"re-derive or update the
existing record explicitly."* So the fix is not to relax it. Either the builder
should be re-runnable (skip or replace existing cells, explicitly), or it is a
one-shot generator and should say so and refuse to run against a populated
catalogue with a clearer message than a duplicate-key error.

- [x] Decide: re-runnable builder, or one-shot generator with an explicit guard?
- [x] Whichever, the current failure mode — a raw `ValueError` on a key that
      looks ordering-related — is the worst of both.

---

## Summary of Changes (2026-09-07) — FIXED, and it was hiding a blocked correction

### The decision

The builder answers its own question, in a comment three lines above the
failure: *"Merge into existing catalogue if present so Phase 2 sympy cells
coexist with Phase 3 Rust production cells in a single witness."* It is a
**re-runnable merging builder by design**. It just merged with `add()`, whose
duplicate guard exists to protect *foreign* cells — and which therefore also
blocked the script from re-deriving its own.

So: `add()` is unchanged and still strict (a caller that did not expect a
collision has a bug, and Phase 3 Rust cells must not be clobbered). A new
`DerivedChiCatalogue.upsert()` is the explicit path the guard's own message
asked for, returning `"added"` / `"unchanged"` / `"replaced"`. The builder uses
it and **reports** rather than overwriting silently.

### What the report immediately caught

First run after the fix: **0 added, 2 unchanged, 10 REPLACED** — and the 10 are
exactly the 1-dimensional blocks of all five census knots, with both `(2,1)`
cells unchanged. Field-by-field diff: **one** field moved, `y_lambda_at_zero`,
`"1"` → `"?"`.

That is not a regression. It is a correction the source already carried and
this bug had blocked. The builder's own comment at the assignment says:

> This was "1", which is indistinguishable from a genuine weight: the
> convention-C audit read it as a nonzero y_lambda on the 3-row (1,1,1) cells
> and flagged this witness as convention C. "?" is the idiom the sibling sweep
> already uses for not-computed, and it cannot be mistaken for data.

Someone fixed the source, could not regenerate the witness, and the misleading
`"1"` sat in the committed catalogue for three months. Corroborated by the
distribution: of 342 committed cells **331 already carry `"?"`**, `1` appears in
exactly the 10 cells this builder owns, and `1/4` once (the real T18 Borromean
weight). The 10 were the last survivors of the placeholder-as-data.

Had `upsert` overwritten quietly, this would have landed as an unexplained
witness diff. Reporting is what made it a finding.

### Idempotence is tested as idempotence

The first draft asserted `replaced == 0` on the merge. That is the wrong
property — it fails on a legitimate one-time correction, which is precisely the
case here. The assertion now applies the same cells a **second** time and
requires the operation to have a fixed point:

    This run:            0 added,  2 unchanged, 10 REPLACED
    Idempotence re-run: 12 unchanged, 0 added,  0 replaced  -> OK

`merge_outcome`, `merge_replaced_cells` and `idempotence_second_pass` are
recorded in the witness, so a future replacement is auditable rather than
silent.

### Blast radius

Witness diff is exactly the 10 `y_lambda_at_zero` values — same 342 keys, no
other field, no cell added or lost. No consumer parses the field numerically;
it is stored and round-tripped as a string (`str(c["y_lambda_at_zero"])`), and
331 cells already carried `"?"`, so every reader already handled it.

5/5 assertions pass, 342 cells emitted.
