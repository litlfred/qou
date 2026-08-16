---
# qou-cdh1
title: 'H1 (hygiene): register the 2026-08-15 ruling in the trace-convention registry'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T02:10:40Z
---

Parent: `qou-cdx1`. Audit:
[`2026-08-15-owner-ruling-convention-d-proton-color.md`](../docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).

**Must land first.** It is what makes every later tranche's convention
unambiguous.

## Edits

`docs/coordination/trace-convention-registry.json`:

- `channels.qbeta-decay.definitional_convention`: `null` → `"D"`
- `channels.qbeta-decay.production_convention`: `"C"` → `"D"` **as the target**;
  keep the current `production_source` text describing the live C state until
  `qou-cds1` actually moves it, or the registry will lie about the code.
- `channels.qbeta-decay.status`: `"disputed"` → `"agreed"`
- `channels.qbeta-decay.open_item`: repoint from `qou-b3nk` to `qou-cds1`
  (the re-derivation), with a `resolution` block naming the owner ruling
- `blocked_migrations[0].owner_decision_required`: `true` → `false`, with the
  ruling recorded — **and a note that the ruling answers the convention
  question, not the singularity** (that is `qou-cds2`)
- `meta`: add the 2026-08-15 ruling alongside 2026-08-09

`docs/coordination/ck-dk-canonical-registry.md`: supersession pointer on §9g
(and §9h's cross-reference). **Do not edit §9g's measured table** — those
numbers are correct measurements of the C→D sensitivity and stay.

## Why "production: D as target" and not just "D"

The registry's value is that it describes what the code *does*. Flipping
`production_convention` to D while `qbeta_utils.py::markov_parameter` still
returns `z_C` would make the R9 evaluator disagree with the registry — and that
evaluator exists precisely to assert the C-state mechanically. Either move the
code first (`qou-cds1`) or record the target explicitly.

## Verification

Registry validator (`kernel_constraints_registry_validate.py --lint-docs
--strict`) plus the R9 evaluator on `qbeta_utils.markov_parameter`.
