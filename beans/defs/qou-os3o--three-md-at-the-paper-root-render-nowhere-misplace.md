---
# qou-os3o
title: Three .md at the paper root render nowhere — misplaced as well as unmanifested
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:26:02Z
updated_at: 2026-08-24T13:26:02Z
---

Found while closing `qou-orpc`, whose four are resolved. That bean claimed the
class was **bounded at four** and that "nothing is hiding here". Re-measured
2026-08-24: **3571 .md, 18 with no .ts sibling.**

## The 18, classified

- **13** under `*/audit/` — probe write-ups, a deliberate non-block convention.
- **1** `lean/AUDIT-REPORT.md` — generated; `qou-orpc` already excluded it.
- **3** genuinely unmanifested prose, all **new since** that bean:

| file | bytes | opens with |
|---|---|---|
| `PieceACornerInduction.md` | 3147 | corner-removal induction for hook lengths |
| `PieceASpechtCharacter.md` | 2156 | character of the central Jucys–Murphy element |
| `bring_tetraplectic.md` | 4608 | "**Scope.** This is a motivating exposition, not a formal result." |

None is referenced by any `.ts` anywhere under `content/`.

## Why this is not just "write three manifests"

They sit at **`content/quantum-observable-universe/` top level**, not in a
chapter directory. Blocks live in chapter dirs and are listed by a section
manifest, so these are **misplaced as well as unmanifested**. Fixing them means
deciding which chapter each belongs to — or that they do not belong in
`content/` at all.

`bring_tetraplectic.md` says outright it is exposition rather than a result,
which points at `docs/` rather than a `prose()` block. The two `PieceA*`
files look like working notes for a Specht/hook-length argument and may already
be superseded by whatever landed in the Lean tree — check before manifesting,
because publishing a stale derivation is worse than leaving it unrendered.

## Options

1. **Manifest into a chapter** — needs an owner call per file on placement.
2. **Move to `docs/`** — right for `bring_tetraplectic.md` on its own account.
3. **Delete** — only after checking the `PieceA*` content is superseded; `qou-orpc`
   is the cautionary case, where deleting would have destroyed a live correction.

## The framing lesson worth keeping

`qou-orpc` presented a point-in-time count as a structural bound. The
content-block class really is small, but it **refills**, and a bean that says
"nothing is hiding here" invites nobody to look again. Whoever closes this one
should say when it was measured, not that it is bounded.
