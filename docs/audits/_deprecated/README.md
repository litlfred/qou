# `docs/audits/_deprecated/` — convention

This folder holds audit documents under `docs/audits/` that have been
**superseded** by later work or that documented work-in-progress whose
findings have been integrated into main and no longer warrant top-level
visibility.

## Why move audits here instead of deleting

Deleted audits lose the historical record of what was known at the time
and which closure paths were considered. The `_deprecated/` folder keeps
the documents discoverable for archaeology while removing them from the
top-level `docs/audits/` list.

## When to move an audit here

| Criterion | Action |
|-----------|--------|
| The audit explicitly says `DEPRECATED` / `SUPERSEDED` / `RETRACTED` in its title or top line | Move with original filename |
| The audit's findings have been integrated into main and the audit no longer drives action | Move with original filename, add deprecation header (see below) |
| The audit is a planning doc (`workplan-vN`) whose plan has been executed | Move and rename to `<original>.executed.md` (and rename any companion `<original>.witness.json` sidecar to `<original>.executed.witness.json` to preserve pairing — see "Companion witness JSONs" below) |
| The audit is a WIP scratch doc whose conclusions live elsewhere | Move; add header pointing to the canonical block / PR |

**Do NOT move**:
- Audits whose findings are still actionable (queue items open, sibling PRs in flight, conjectures unresolved)
- The latest revision of an ongoing-status document (e.g., `derivation-audit-report.md` — that lives in `content/`, not `docs/audits/`, but the principle holds for analogous ongoing docs in `docs/audits/`)
- Audits cited by current code/content as references — moving them breaks the link

## Deprecation header convention

When moving an audit, prepend a top-of-file header:

```markdown
> **DEPRECATED on YYYY-MM-DD.** Superseded by <link to current source>.
> Original audit preserved here for historical record.
```

For workplans whose plan has been executed, use:

```markdown
> **EXECUTED on YYYY-MM-DD.** Plan items have been integrated into main
> via <links to merged PRs>. Original workplan preserved here.
```

## Companion witness JSONs

Some audits have `.witness.json` sidecars under `docs/audits/`. When
moving an audit `.md`, also move its sidecar — they belong together.

## Index

A top-level [`docs/audits/INDEX.md`](../INDEX.md) (created 2026-05-24)
catalogues the audit corpus by date cluster, with per-cluster
deprecation-readiness assessment. Future deprecation tranches should
consult it before moving files.

## See also

- [`content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md`](../../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md) — the *content-level* audit doc (not in `docs/audits/`; tracks GAP-A/B/C/D status)
- AGENTS.md §"Branch + PR workflow" rule 4 (small structured commits + cherry-pick discipline)
