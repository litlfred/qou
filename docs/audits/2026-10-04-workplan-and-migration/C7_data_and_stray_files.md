# C7: data and stray files under `folio/`, measured (bean `qou-4s33`)

Measured on `main` `f5e20a23f6`, 2026-10-05. All 11 rows below are classified;
none has been moved, deleted or rewritten. Every action needs a ruling from
the owner. "Recommended" is the agent's judgement, not a finding.

The `git log` date on all of these is 2026-09-27. That is when `content/`
was renamed to `folio/`, so it says nothing about how old a file is.

| # | file | what it is (measured) | read by | recommended |
|---|---|---|---|---|
| 1 | `folio/quantum-observable-universe/foreshadows.json` (145 KB) | derived index of `foreshadows` edges | no reader found by grep | **regenerate** (stale: built from 3,144 blocks; there are 3,620) |
| 2 | `folio/quantum-observable-universe/introduction/lean-coverage.json` (852 B) | derived Lean-coverage counts | `scripts/refresh-authors-note.ts`, `scripts/check-sidecars.sh` | **regenerate** (same stale block count) |
| 3 | `folio/quantum-observable-universe/glossary.json` (7.9 KB) | the glossary build output (`build-glossary.ts`) | README, skills `formalizer`, `ontologist`, `content-block-review` | **regenerate** (stale since 2026-05-20) |
| 4 | `folio/quantum-observable-universe/observations/jwst-observational-data.json` (195 B) | 5 numbers labelled "fit" (`fit_z_cosmo`, `fit_q_local`, `residual`), a hardcoded `q_baseline: 1.1097`, `"status": "VERIFIED"` | no producer and no reader | **leave it byte-identical and record it as orphan data.** It is physics data with no provenance, so a move or an edit is the owner's call alone. |
| 5 | `folio/schema/references.review.json` (1.8 KB) | per-reference human-review status (bib-human-review, phase 1) | `scripts/bib-agent-backfill.ts` | **keep** in place; it is a human judgement, so it is attestation data |
| 6 | `folio/get_fails.py`, `get_failures.py`, `get_md_files.py` | one-off scripts that read an `evaluations` key no sidecar carries | none | **move** to `fsh-guts/deprecated/` (dead) |
| 7 | `folio/pipeline/triage_stubs.ts` (9.3 KB) | calls `unlinkSync` on `.lean` "shadows" and rewrites placeholders; no docblock | none | **move** to `fsh-guts/deprecated/` so it cannot run by accident |
| 8 | `folio/package.json` | deps for `folio/pipeline/` tools; its `build` scripts call an atlas renderer that is in `_deprecated/` | `folio/pipeline/*` | **keep**; the dead `render-atlas` scripts already no-op with a note |
| 9 | `folio/bib-qa-images/` (only `.gitkeep`) | upload target for bib photo evidence | skill `bib-qa` | **keep** |
| 10 | `folio/bach2013-double-slit/` (a `paperRef`) | tagged `imported`; 3 remarks without `interprets` | `folio.ts` | **owner:** paper, or library entry? |
| 11 | `folio/visualizer/` (a `paperRef`) | 3 blocks that define viewer-state types and carry `lean.ref` | `folio.ts`; also why `validate-references` needs `--paper` | **owner:** paper, or viewer/tile? |

Parity (P-C): this file is the only change. No `folio/` blob moved.
