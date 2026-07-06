# qou-mass P3 deprecation audit

**Date:** 2026-05-19
**Branch:** `claude/follow-ups-from-808`
**Scope:** Compare every module under
[`qou-mass/src/qou_mass/_internal/`](../../qou-mass/src/qou_mass/_internal/)
against its sibling in
[`computations/`](../../computations/)
and decide which vendored copies can be deprecated outright.

## Method

For each `<name>.py` in `qou-mass/src/qou_mass/_internal/`:

1. `cmp -s qou-mass/src/qou_mass/_internal/<name>.py computations/<name>.py`
   to detect byte-identical copies.
2. `diff` for divergence size when not identical.
3. `grep -rl --include='*.py' -E "(from <name> import|import <name>\b)"
   computations/` to count folio-side importers of the
   *module name* (this is how every folio script imports its sibling —
   confirmed below).

Cross-check: `grep -rl "from qou_mass" computations/`
returned **zero hits**, and likewise for `import qou_mass`. No folio
script consumes the `qou_mass` package — every importer uses the bare
sibling name (`from _precision import set_compute_dps, fmt`, etc.).
This means the importer counts below are folio-internal sibling
imports, not consumers of the vendored library. They measure what
**would have to be refactored** if folio-assistant scripts were
migrated onto the `qou_mass` package, **not** what already depends on
qou-mass.

## Vendored modules table

| Module | folio-assistant equivalent | Status | folio sibling-importers |
|--------|----------------------------|--------|-------------------------|
| `_precision.py` | exists | byte-identical | 160 |
| `active_set_pruning.py` | exists | byte-identical | 1 |
| `canonical_braid_crossings.py` | exists | byte-identical | 26 |
| `codata_constants.py` | exists | byte-identical | 98 |
| `experimental_constants.py` | exists | byte-identical | 328 |
| `hecke_characters.py` | exists | byte-identical | 157 |
| `hoefsmit_symbolic.py` | exists | byte-identical | 21 |
| `isotope_record_schema.py` | exists | byte-identical | 1 |
| `knot_volumes.py` | exists | byte-identical | 8 |
| `markov_trace_recursive.py` | exists | byte-identical | 2 |
| `markov_weights_symbolic.py` | exists | byte-identical | 10 |
| `q_parameter.py` | exists | byte-identical | 742 |
| `wedderburn_jones_markov.py` | exists | byte-identical | 35 |
| `witness_base.py` | exists | byte-identical | 516 |

**14 modules / 14 byte-identical.** Zero diverged. Zero novel.

## Deprecation candidates (pure-redundant)

All 14 vendored modules are byte-identical copies of the
folio-assistant originals and have **no folio-side consumer that
imports them via the `qou_mass` package**. They are pure-redundant
and can be deprecated today without any folio refactor:

- `_precision.py`
- `active_set_pruning.py`
- `canonical_braid_crossings.py`
- `codata_constants.py`
- `experimental_constants.py`
- `hecke_characters.py`
- `hoefsmit_symbolic.py`
- `isotope_record_schema.py`
- `knot_volumes.py`
- `markov_trace_recursive.py`
- `markov_weights_symbolic.py`
- `q_parameter.py`
- `wedderburn_jones_markov.py`
- `witness_base.py`

Recommended deprecation mechanism (least-disruptive first):

1. **Stage 1 — make `qou_mass._internal.<name>` a re-export shim.**
   Replace each module body with
   `from <name> import *  # re-export from folio-assistant`
   plus a `DeprecationWarning` at import time. Requires
   folio-assistant's `computations/` to be on `sys.path` when
   `qou_mass` is imported in dev mode (already true for the in-repo
   test harness). This eliminates drift risk immediately.
2. **Stage 2 — delete the vendored copies.** Once the shim has had
   one release cycle and no external consumer has surfaced, remove
   `qou-mass/src/qou_mass/_internal/<name>.py` entirely and ship the
   package as a thin wrapper that re-exports folio-side modules at
   install time (or document folio-assistant as the authoritative
   source and treat qou-mass as repo-internal only).

The 742-importer / 516-importer / 328-importer fan-out figures
(`q_parameter`, `witness_base`, `experimental_constants`) measure
folio-internal coupling, **not** qou-mass consumers. They do not
block the Stage 1 shim. They do tell us that any future renaming of
those modules will be a much bigger task — out of scope here.

## Refactor candidates (active-consumer)

**None.** No folio script imports from `qou_mass`. The vendored copy
has no active consumer that needs to be rewritten.

If qou-mass acquires external (pip-install) users in the future,
their imports of `qou_mass._internal.<name>` will need to keep
working through the Stage 1 shim until they migrate. At present
there is no such consumer in this repo.

## Legitimately distinct (no deprecation)

**None.** Every module is byte-identical to its folio-assistant
counterpart.

## Net summary

- **14 modules deprecatable today** (all byte-identical, zero
  external consumers).
- **0 modules need consumer-rewrite first** (no folio script imports
  from `qou_mass`).
- **0 modules legitimately distinct** (no novel content in the
  vendored copy).

The qou-mass `_internal/` tree is entirely redundant with
computations/ as of this audit. P3 deprecation can
proceed without folio-side refactor; only the qou-mass package
itself needs editing (Stage 1 shim, then Stage 2 deletion).

## Top 3 deprecation candidates

Ranked by simplicity (fewest folio-side sibling imports → smallest
blast-radius if the shim is later removed and folio consumers must
migrate onto `qou_mass`):

1. **`active_set_pruning.py`** — 1 folio sibling-importer. Smallest
   coupling; ideal first shim.
2. **`isotope_record_schema.py`** — 1 folio sibling-importer. Pure
   data-schema module; trivial to re-export.
3. **`markov_trace_recursive.py`** — 2 folio sibling-importers.
   Recursive trace helper; small surface area.

These three are the cleanest starting points if the deprecation is
staged module-by-module rather than bulk. For a bulk Stage 1
conversion, all 14 can be shimmed in one commit since they are
byte-identical and have no folio-side `qou_mass` consumer to break.

## Source

- Vendored copies: [`qou-mass/src/qou_mass/_internal/`](../../qou-mass/src/qou_mass/_internal/)
- Authoritative originals: [`computations/`](../../computations/)
- Package metadata: [`qou-mass/pyproject.toml`](../../qou-mass/pyproject.toml)
  (version `0.1.0a1`, Development Status `3 - Alpha`).
