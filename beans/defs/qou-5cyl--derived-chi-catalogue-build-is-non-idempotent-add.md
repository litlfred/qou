---
# qou-5cyl
title: 'derived_chi_catalogue_build is non-idempotent: add() refuses duplicates, no update path exists'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T14:18:04Z
updated_at: 2026-11-16T19:29:47Z
parent: qou-trd0
---


## What was found

`exit1` in the `qou-eea0` pass-2 regeneration run (PR #4928):

```
File "computations/derived_chi_catalogue.py", line 175, in add
ValueError: duplicate catalogue cell ('borromean', (3,), 'borromean-baryon');
            re-derive or update the existing record explicitly.
```

`derived_chi_catalogue_build.py:368` deliberately loads the existing
catalogue and merges into it — *"so Phase 2 sympy cells coexist with Phase 3
Rust production cells in a single witness"* — and then calls `cat.add(c)` for
every cell it derives. `add()` raises on any key already present, so the
builder succeeds **only** on a catalogue that does not yet contain its cells.
Once it has run, it can never run again.

That makes it unrunnable by any regeneration harness, and it is why its
witness is still convention C: the migration cannot reach a producer that
refuses to execute.

The error message advises to *"update the existing record explicitly"*, but
`DerivedChiCatalogue` exposes exactly one mutator — `add` at line 172. There
is no `update`, `replace`, `upsert` or `remove`. The advised route does not
exist.

## Why this is not a one-line fix

The obvious repair — make the builder upsert instead of add — carries a real
correctness risk that should be decided, not assumed. The catalogue is
explicitly **tiered**: Phase 2 cells come from sympy, Phase 3 cells from Rust
production, and `tier_counts()` reports the split. A blind upsert lets a
re-derived *sympy* cell silently overwrite a *Rust production* cell of the
same key, downgrading the catalogue while reporting success.

So the question to answer first is: when a re-derivation produces a cell that
already exists at a different tier, which wins? Plausible answers, all
defensible:

1. **Higher tier wins** — upsert only if the incoming tier is at least the
   stored tier; otherwise keep and log. Preserves the tiering by
   construction.
2. **Newest wins, tier recorded** — always overwrite, but keep the tier on
   the cell so a downgrade is visible in `tier_counts()` rather than silent.
3. **Builder owns its keys** — the builder removes exactly the cells it is
   about to derive, then adds. Needs a `remove`, and needs "its own cells" to
   be well-defined.

## Close condition

`derived_chi_catalogue_build.py` runs twice in a row without error, the
second run leaves the catalogue's `tier_counts()` no worse than the first,
and the chosen tier-collision rule is written down where `add()` is defined.

## Progress Update (Round 49 — PR #8170)

- Added provenance-tier (`extracted < cal-anchored < derived`) and `q_convention` (`kassel < kauffman`) preservation guard to `DerivedChiCatalogue.upsert(self, cell, *, allow_downgrade=False)` in `computations/derived_chi_catalogue.py`, returning `'kept_higher_tier'` instead of silently downgrading Phase-3 `derived` / `kauffman` cells.
- Wired `'kept_higher_tier'` reporting into `computations/derived_chi_catalogue_build.py` and added `--self-test` to `computations/derived_chi_catalogue.py`.
- PR: https://github.com/litlfred/qou/pull/8170 (`8b83507c7e14547848b5b991bdd3396fc7f3a703`)
