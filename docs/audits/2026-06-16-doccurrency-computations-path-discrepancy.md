# Doc-currency: compute path `folio-assistant/computations/` → `computations/` (3576 stale refs — owner confirmation requested)

**Date:** 2026-06-16
**Branch:** `claude/doccurrency-computations-path-discrepancy-2026-06-16`
**Status:** finding + recommendation. **No unilateral sweep performed** — flags an architecture-sensitive
discrepancy for owner confirmation.
**Discipline:** critical-distance (surface the finding with evidence; do not guess the intended architecture).

## The discrepancy

The corpus refers to the Python compute as **`folio-assistant/computations/*.py`** in **3576 tracked files**
(docs, witnesses, `.beans`, skills, AGENTS.md ×10, …). But that path **does not resolve** in a fresh checkout:

| Check | Result |
|---|---|
| Tracked files under `computations/` (qou top-level) | **5770** |
| Tracked files referencing `folio-assistant/computations/` | **3576** |
| `folio-assistant/computations/` exists after `scripts/setup-folio-assistant.sh`? | **No** — the platform clone (`litlfred/folio-assistant` main) has **no `computations/` dir** |
| Sampled scripts (`closed_form_tau_M.py`, `kazhdan_lusztig.py`, `per_observable_100x_status.py`) | resolve at **`computations/X.py`**, not `folio-assistant/computations/X.py` |

So the compute that the corpus calls `folio-assistant/computations/` actually lives at qou's top-level
**`computations/`** (likely moved by commit `d27b002745` "merge physics logic and cleanup platform scripts",
part of the platform/content split).

## Real impact (why this matters)

This is not cosmetic. **This session an agent (me) twice concluded "the compute is absent / not runnable in
this sandbox" based on the stale `folio-assistant/computations/` path** — and accordingly framed PROBE 4 / the
keystone weighting as un-runnable — before discovering the engine at `computations/kazhdan_lusztig.py` and
running it. The stale path actively misleads agents about what compute is available.

## Two interpretations (why a blind sweep is NOT done here)

1. **Migration left refs stale (most likely).** Compute moved into qou at `computations/`; the 3576
   `folio-assistant/computations/` refs are legacy. ⇒ a mechanical `folio-assistant/computations/` →
   `computations/` sweep is correct.
2. **Platform-repo lag (less likely).** The intended canonical home is `folio-assistant/computations/` and the
   platform repo's `main` is *missing* `computations/`; the qou top-level `computations/` is a transitional copy.
   ⇒ the fix is in the *platform* repo, and the refs are "correct" pending it.

The evidence (scripts tracked in qou; imports resolve from `computations/`; CI/witness pipeline runs against
`computations/`) strongly favors **(1)**, but the canonical-path decision is an **owner architecture call**, and
a 3576-file sweep is too large + irreversible to run on an inference.

## Recommendation

- **Owner: confirm** `computations/` (qou top-level) is the canonical compute path.
- If confirmed, a **mechanical sweep** `folio-assistant/computations/` → `computations/` across the 3576 refs is
  a clean follow-up (single bulk commit per the integration-watcher sweep exception), **including the ~10
  occurrences in `AGENTS.md`** (the LP/SDP canonical-entry-point block, the project-structure table, the
  precision-dashboard paths, the long-compute logging discipline). This doc deliberately does **not** touch
  `AGENTS.md` or run the sweep — the blast radius (3576 files) and the small chance of interpretation (2) warrant
  explicit authorization first.

## Cross-references

- `scripts/setup-folio-assistant.sh` — sets up `folio-assistant/` → platform clone (which lacks `computations/`)
- `computations/` — the actual, resolving compute tree (5770 files, incl. `kazhdan_lusztig.py`)
- This session's PRs #2378/#2381 (Option-E PROBE-4 prune) — where the stale path first misled, then `computations/` was found
