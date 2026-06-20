# Port payload: block-QA schemas → litlfred/folio-assistant

**Date:** 2026-06-12 · **Prepared by:** the qou session that authored qou PRs #2195/#2198 · **Status:** ready to apply

## Why

Owner directive (2026-06-12): the folio-assistant platform components have moved to
the standalone repo [litlfred/folio-assistant](https://github.com/litlfred/folio-assistant);
the block-QA schemas belong there. A Gemini-driven migration of the platform tree is
in progress but, as of 2026-06-12 ~19:30 UTC, **nothing of it is pushed**: the remote
has only `main` @ `03d635d` (last activity 2026-03-24, PR #2) and no open PRs. The
preparing session had read-only access (its credentials are scoped to litlfred/qou),
so the port is delivered here as an apply-ready patch series instead of a
folio-assistant PR.

## What the patches contain

Built on folio-assistant `main` (`03d635d`), **additive-only** (no existing file
modified except one barrel-export line), so they rebase/`git am --3way` cleanly onto
any migration branch that doesn't already add these paths:

| Patch | Adds |
|---|---|
| `0001-schemas-block-qa-…` | `schemas/block-qa.ts` (producing TS interfaces, evidence field already widened to `string \| {line,text}[]` per live-corpus shapes) + barrel export in `schemas/index.ts` |
| `0002-pkg-block-qa-schema-…` | `tools/block-qa-schema/` — canonical JSON Schemas (`block-qa/v1` + `qa-script/v1`), Zod mirror (npm `@litlfred/block-qa-schema`), Pydantic mirror (PyPI `block-qa-schema`), tests, README, packaging. All repo URLs/links rewritten qou → folio-assistant. |

Source of truth ported from qou `main` (landed there via qou PR #2198 incl. the
Gemini review fixes: integer line numbers, int-preserving metrics).

## How to apply (in a folio-assistant checkout)

```bash
# from the folio-assistant repo root, on main or on the migration branch
git am --3way path/to/qou/docs/ports/2026-06-12-folio-assistant-block-qa/*.patch
```

If the migration relocates `schemas/` or `tools/`, apply then `git mv` — the package
is self-contained.

## Verification performed at port time

- `python3 -m pytest tests/` inside the ported tree — 8/8 pass.
- Both JSON Schemas parse; models previously validated against the full qou corpus
  (2,250/2,250 block sidecars + 62/62 script sidecars; see qou PR #2198).
- Not done (no toolchain in the sandbox): root `tsc` over the new TS; `tsup` build.

## Follow-ups for the landing session

1. Compile check: root `npm run build` (tsc) over `schemas/block-qa.ts`; the package's
   own `tsup` build at publish time.
2. Optionally wire the canonical JSON Schemas into `scripts/generate-schemas.ts`
   conventions (the new repo generates schemas from zod; this package deliberately
   keeps a hand-maintained canonical JSON Schema per the witness-schema pattern —
   reconcile or document).
3. Registry publication (npm + PyPI) — owner credentials.
4. Once landed, remove the qou copies (`tools/block-qa-schema/`,
   `folio-assistant/schemas/block-qa.ts`) and update qou's AGENTS.md project-structure
   row — presumably as part of the broader migration's qou-side cleanup.
