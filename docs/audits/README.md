# `docs/audits/` — process + conventions

This directory holds **audit documents** — agent or human write-ups
that record investigations, findings, post-mortems, and Rule-14
escalations. Audits are first-class artifacts: many become the
canonical reference for "why does the framework do X this way" or
"is this item open or closed?"

## When to write an audit doc

Write an audit when **at least one** of:

1. You investigated a non-trivial finding and want the trail to be
   discoverable by future agents/sessions.
2. You discovered an "already-implemented" answer to something that
   was framed as open (post-mortem the source of the miss; see
   §"Corpus check before declaring open" below).
3. You're escalating a production coefficient or formula that does
   not derive from one of the canonical 13 drivers (Rule 14 escalation
   per [`2026-05-23-lambda-scale-canonical-unification.md`](2026-05-23-lambda-scale-canonical-unification.md)).
4. You're synthesising findings across multiple files, scripts, or
   conjectures into a single readable summary.

Don't write an audit for routine fixes that the commit message
captures fully.

## File naming

```
docs/audits/YYYY-MM-DD-<theme-slug>.md
```

`theme-slug` is lowercase, hyphenated, ≤ 60 chars, describing the
investigation scope (`binding-magic-A-wireup`,
`q0-repin-stale-witness-audit`, `klr-dialog-assessment`).

The date is the day the audit was authored, **not** the day the
underlying finding occurred (use the body for that).

## Standard structure

```markdown
# <Theme as natural-language title>

**Date:** YYYY-MM-DD
**Branch:** `claude/<branch>` (and the PR if open)
**Trigger:** one sentence describing what prompted the audit

## Headline

The 2-3 sentence finding. A reader who reads only the headline
should know what the audit concludes.

## Findings / Math content

Substantive analysis. Use tables for cross-checks; cite source
files with `path:line` references where exact.

## Action items

- ✓ Items the audit closes (with PR commit SHA if applicable)
- ⏳ Items still open / queued
- ⏸ Items deferred to research

## References

- Source files investigated
- Related audit docs (cross-link via path, or PR-blob URL if cross-branch)
- Coordination ledger (if part of a multi-PR thread)
```

## Corpus check **before** declaring "open" (STRICT)

Per [`CLAUDE.md` §"Before declaring 'open' math / questions / gaps"](../../CLAUDE.md),
do **not** write an audit declaring an item "open" / "Open Math X" /
"TODO" / "pending" before running the corpus-grep checklist:

1. `grep -rln <topic> docs/audits/`
2. `grep -rln <topic> content/` (whole tree)
3. `grep -rln <topic> computations/`
4. `docs/coordination/<theme>.md`

Source files' status notes (`## Status`, `Open math`, `Phase 3
open`, etc.) **lag the corpus** — owner-authorised resolutions
typically land as audit docs first, with the originating source
file updated weeks later. Three consecutive misses on this in May
2026 (PRs [#1515](https://github.com/litlfred/qou/pull/1515),
[#1532](https://github.com/litlfred/qou/pull/1532),
[#1543](https://github.com/litlfred/qou/pull/1543)) prompted the
strict rule and the
[`2026-05-31-binding-magic-A-wireup.md` §"Why was the resolution
missed?"](2026-05-31-binding-magic-A-wireup.md) post-mortem.

## Reanalysis convention

When an audit's framing is found wrong after publication
(e.g. an "Open Math A" turns out already-resolved), do **not**
silently rewrite. Add a section:

```markdown
## <topic> — reanalysed YYYY-MM-DD

**Status:** structurally answered by <pointer>. [Findings...]

**What remains open:** [verification / formalisation items only]
```

Plus, if the miss is structural (third-time pattern), add a
`## Why was this missed?` post-mortem section explaining the
source of the miss and the corrective discipline.

This preserves the audit trail (the original framing is still
visible) while pointing readers to the correct resolution.

## Cross-references with the coordination ledger

When an audit is part of a multi-PR thread, the
[`docs/coordination/<theme>.md`](../coordination/) ledger
should carry a pointer back to the audit. Conversely the audit's
"References" section should link the coordination ledger. The
ledger is the *who-is-doing-what* index; the audit is the
*what-did-we-find* writeup.

## Related skills

- [`local/proof-gap-audit`](../../.claude/skills/local/proof-gap-audit.md)
  §K codifies the corpus-grep checklist for proof-gap declarations.
- [`local/coordinate`](../../.claude/skills/local/coordinate.md)
  manages multi-PR scope; produces the coordination ledger.
- [`local/integration-watcher`](../../.claude/skills/local/integration-watcher.md)
  family triages incoming work; surfaces gaps that often become
  audit topics.
