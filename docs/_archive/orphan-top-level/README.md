# `docs/_archive/orphan-top-level/`

**Purpose:** historical record of orphaned markdown that is **not
referenced** by any active code, content block, witness, audit, or
canonical documentation — kept so it is findable without polluting the
places a reader looks first.

Two intakes so far, and the scope widened at the second:

1. **2026-05-24** — 32 files from the `docs/` root, during the docs
   consolidation, so that `docs/` root held only currently-active
   canonical references.
2. **2026-09-26** — 11 files from the **REPOSITORY root**, on the owner
   directive *"the qou audit docs and such should be moved under
   `docs/`"*. Same principle, one level out: the repo root had 134
   tracked files of which 23 belonged there.

## What's here

**43 markdown files.** The original 32 from March–early May 2026 comprise:

- **Session handoffs / summaries** — point-in-time records of work
  tranches (beta-decay-session, d-session, pyhecke-session). Useful for
  understanding past decisions; not load-bearing for current work.
- **Old workplans** — superseded by the canonical
  [`canonical-derivation-cheat-sheet.md`](../../canonical-derivation-cheat-sheet.md)
  §5 migration backlog (all 5 items closed as of 2026-05-23) and by the
  ongoing PR-driven coordination ledgers in
  [`../coordination/`](../../coordination/).
- **One-off audits** — historical investigations that were resolved
  in their respective PRs (alpha-fsc-audit, archimedean-existence-audit,
  recast-tightening-audit-2026-04-27).
- **Migration plans** — FOLIO_MIGRATION_PLAN, MIGRATION-PLAN, PLAN,
  plan — all from a chapter / repo-layout reorganization that is
  complete.
- **Path-to-1ppb series** (path-to-1ppb.md, -02-content, -03-engine) —
  an old roadmap from before the L2 100× per-observable framework
  replaced it. The canonical "what passes 100×" answer now lives in
  [`computations/per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).
- **Phase-3 findings, tr_M reconciliation, qou-open-conjecture-strategies**
  — all subsumed by the canonical cheat sheet's §3 Phase 5 findings
  table.

### The 11 added 2026-09-26, from the repository root

- `AUDIT-DEEP-2026-05.md` — the May deep audit. **Still linked from 19
  files**, mostly as `"audit_reference"` provenance in
  `computations/*.witness.json`, so those records name a path that has
  moved. Deliberately not rewritten: they record where the document was
  when a number was computed, and editing a witness to fix a link would
  dirty it for no gain.
- `AUDIT-REPORT.md`, `lean-qa-report.md` — earlier one-off reports.
- `STATUS.md` — the goals list. `scripts/session-start-coord-sweep.sh`
  names it to every session at start and was updated to the new path.
  Note its true referrer count is **16**, not the 26 a `grep -F` reports:
  `computations/DERIVATION-STATUS.md` and `HANDOVER-STATUS.md` end in the
  same string and are different files.
- `ORIGINAL_REQUEST.md`, `plan_of_attack.md`, `session-beans.md` —
  point-in-time records.
- `TEST_INFRA.md`, `TEST_READY.md` — test-infrastructure notes.
- `dashboard_raw_output_low.md`, `dashboard_raw_output_sweep.md` — raw
  dashboard captures, superseded by
  [`computations/per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).

## Why archived (not deleted)

These docs contain historical reasoning, refutations, and
decision-trails that are valuable to preserve as a record of negative
results. Per the repo owner's 2026-05-24 housekeeping directive
*"leave record of negatives in easy to find place but don't pollute"*,
they live here rather than at top level where they'd dilute the
canonical references.

## Not here

The following remain in `docs/` root because they are actively
referenced or canonically current:

- [`canonical-derivation-cheat-sheet.md`](../../canonical-derivation-cheat-sheet.md) (33 refs)
- [`precision-goals.md`](../../precision-goals.md) (15 refs)
- [`ilp-sdp-audit.md`](../../ilp-sdp-audit.md) (16 refs)
- [`path-to-1ppb-04-plan.md`](../../path-to-1ppb-04-plan.md) (8 refs)
- [`chi-sym-alt-theorem.md`](../../chi-sym-alt-theorem.md) (7 refs)
- Other actively-referenced docs.

If you find yourself looking for a doc in this archive that you
actually need at top level, just move it back — the archive is for
reducing noise, not gating access.

**This directory is markdown only, deliberately** — 43 files, zero of any
other type. Orphaned scratch *scripts* and *data* from the repository root
do not belong here and are parked under `fsh-guts/deprecated/` instead;
mixing them in would make "an orphaned document" and "an abandoned script"
the same category, and they are not.

**It is also rendered on the docs site**, `nav_exclude`d rather than
excluded, precisely so the 19 links into `AUDIT-DEEP-2026-05.md` resolve
there as well as in the repo.
