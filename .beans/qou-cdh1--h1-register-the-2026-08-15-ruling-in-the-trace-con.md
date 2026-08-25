---
# qou-cdh1
title: 'H1 (hygiene): register the 2026-08-15 ruling in the trace-convention registry'
status: completed
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T02:19:13Z
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


---

## Done 2026-08-16 — with one deliberate deviation

All edits landed. **Deviation: `status` is `agreed-migration-pending`, not
`agreed`.** The bean asks for `status: "agreed"` *and* for
`production_convention` to keep describing the live C state — and `R8` makes
those two mutually impossible (`definitional != production ⟹ status MUST be
"disputed"`). Recording the settlement therefore forced a choice between lying
about the code and losing the ruling. Added a third status for the question the
vocabulary could not ask: `"disputed"` answers *which convention is right*;
`"agreed-migration-pending"` answers *the owner settled it and the code has not
moved*. It requires strictly more evidence than `"disputed"` did — a
`resolution` block naming the ruling and its date, plus
`production_convention_target == definitional_convention` — so it cannot be used
to quiet a live dispute. Regression cases `RC8`/`RC9`/`RC10` pin all three
guarantees and all three fire.

- `definitional_convention` null → `"D"`; `definitional_source` records the
  ruling and that `qou-b3nk` is superseded **as a status, not as analysis**
- `production_convention` stays `"C"` (fact) + `production_convention_target: "D"`
  + a note explaining why flipping it early would contradict R9
- `open_item` repointed `qou-b3nk` → `qou-cds1`; `resolution` block added,
  carrying the `decayLadder_zC_threeRow_ne_zero` scope note (re-derive, not
  re-evaluate; `c₃ ≈ −974` is a sensitivity measurement, not a proposed value)
- `blocked_migrations[0].owner_decision_required` → answered, in
  `resolved_migrations` where the row now lives — **plus a `premise_correction`**
  (see `qou-cdh2` / `qou-cds2`, both annotated: the audit's "gram.py::z stays C"
  premise was already false at its own commit)
- `meta.owner_rulings` records 2026-08-09 and 2026-08-15
- `ck-dk-canonical-registry.md`: supersession banner on §9g, scope note on §9h.
  **Measured C→D sensitivity table untouched**, as instructed.

**Verification.** `trace_convention_registry_validate.py --selftest`: PASS,
0 errors, 23 warnings, RC1/2/3/8/9/10 all caught. `R9` confirms
`qbeta_utils.markov_parameter` is C by evaluation (|d| = 1.9e-51) while the
registry records D as settled — they disagree on purpose and say so.
Producer 44/44, witness 16/16, substitution 23/23.
`kernel_constraints_registry_validate.py --lint-docs --strict` reports
**22 rows, 0 errors, 9 warnings → FAIL — byte-identical on `origin/main`**
(verified in a detached worktree). Pre-existing and unrelated to §9g/§9h; not
introduced and not fixed here.
