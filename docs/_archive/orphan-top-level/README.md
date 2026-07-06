# `docs/_archive/orphan-top-level/`

**Purpose:** historical record of top-level `docs/*.md` files that are
**not referenced** by any active code, content block, witness, audit,
or canonical documentation. Moved here during the 2026-05-24 docs
consolidation so that `docs/` root contains only the currently-active
canonical references.

## What's here

32 markdown files from March–early May 2026, comprising:

- **Session handoffs / summaries** — point-in-time records of work
  tranches (beta-decay-session, d-session, pyhecke-session). Useful for
  understanding past decisions; not load-bearing for current work.
- **Old workplans** — superseded by the canonical
  [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §5 migration backlog (all 5 items closed as of 2026-05-23) and by the
  ongoing PR-driven coordination ledgers in
  [`../coordination/`](../coordination/).
- **One-off audits** — historical investigations that were resolved
  in their respective PRs (alpha-fsc-audit, archimedean-existence-audit,
  recast-tightening-audit-2026-04-27).
- **Migration plans** — FOLIO_MIGRATION_PLAN, MIGRATION-PLAN, PLAN,
  plan — all from a chapter / repo-layout reorganization that is
  complete.
- **Path-to-1ppb series** (path-to-1ppb.md, -02-content, -03-engine) —
  an old roadmap from before the L2 100× per-observable framework
  replaced it. The canonical "what passes 100×" answer now lives in
  [`computations/per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json).
- **Phase-3 findings, tr_M reconciliation, qou-open-conjecture-strategies**
  — all subsumed by the canonical cheat sheet's §3 Phase 5 findings
  table.

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

- [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) (33 refs)
- [`precision-goals.md`](../precision-goals.md) (15 refs)
- [`ilp-sdp-audit.md`](../ilp-sdp-audit.md) (16 refs)
- [`path-to-1ppb-04-plan.md`](../path-to-1ppb-04-plan.md) (8 refs)
- [`chi-sym-alt-theorem.md`](../chi-sym-alt-theorem.md) (7 refs)
- Other actively-referenced docs.

If you find yourself looking for a doc in this archive that you
actually need at top level, just move it back — the archive is for
reducing noise, not gating access.
