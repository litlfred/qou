---
# qou-4jhp
title: 'GAP: qa-sweep cannot load at platform pin b61e856 (sci layer imports moved cat-harness/schemas); first fixing pin a6e5884 needs owner ruling'
status: completed
type: bug
priority: high
created_at: 2026-11-15T09:00:38Z
updated_at: 2026-11-21T12:30:00Z
parent: qou-n4r9
---


Parent epic: `qou-s4ws` (tracker #7735), owner decision S3 = yes (fix qa-sweep).
Session: https://claude.ai/code/session_01Qmmkt8RPNkJLAu7MkUPE3f

## Reproduction (measured 2026-11-15, corpus 2de71e518)

`scripts/setup-folio-assistant.sh` at the pin `b61e856`, then
`bun run folio-assistant/cat-harness-tools/pipeline/qa-sweep.ts <block>.md`:

    error: Cannot find module '../../cat-harness/schemas/kg/cat-harness'
      from '.../folio-assistant-sci/pipeline/qa-checkers-triviality.ts'

## Root cause — inside the platform lock, not in qou

The pin's `index.lock.json` mounts `folio-assistant-sci@1e31c506`. That commit
still imports `../../cat-harness/schemas/kg/cat-harness` (value import, line 79;
the two `block-qa` imports are `import type` and are erased by Bun). The
`b61e856` bump (bean 8lcl, folio-assistant#2774) moved those schemas to
`cat-harness-tools/schemas/` and re-pointed qou, but its lock did not include
sci#140 (`689a0e7`, "8lcl: point the QA checkers ... at cat-harness-tools/schemas"),
which landed the same day. So the pinned platform is internally inconsistent.
It is not a missing sibling clone: all 11 layers mount fine (`mount:lock: OK`).

**No qou-side fix exists that is not a pin move** — the broken file is a mounted
platform file. (A shim file in the mount would be a hack against the fixity digest.)

## Smallest fixing pin: `a6e58846b` (folio-assistant#2785, 2026-10-30)

First platform commit after `b61e856` whose lock mounts a sci descendant of
`689a0e7` (sci `977a5dc`). Searched the lock history in order. It is 13,842
commits past the pin (platform main is 14,469 past).

Measured at `a6e58846b`, same corpus:

| check | `b61e856` (pin) | `a6e58846b` |
|---|---|---|
| qa-sweep loads | **no** | yes |
| run-validate, qou unchanged | 16 issues | **crashes**: `lean-formal-ref` moved `cat-harness-tools/pipeline/` -> `folio-assistant-sci/pipeline/` |
| run-validate, 2 imports re-pointed (`scripts/run-validate.ts`, `scripts/preload-registry.ts`) | — | **16 issues, byte-identical lines** |

So the bump is a 4-site commit: `.folio-assistant-pin`, `build.yml` `uses:`,
`qou.config.json` sci `ref` (per the pin file's coupling note), plus the 2 imports.

## What a qa-sweep refresh would produce (dry-run at a6e58846b)

Note: qa-sweep at this platform writes to `test/results/block-qa/` (gitignored;
published to the qa-reports branch per owner ruling 2026-10-04 decision 11,
`qou.json` dir `qa`), NOT to the 3652 committed in-tree `<block>.qa.json`.
And it takes ONE path per call; extra paths are ignored without a warning.

| block | critical | major | minor | needs-agent |
|---|---|---|---|---|
| confinement-universality | 0 | 0 | 0 | 27 |
| breit-wheeler-vertex | 0 | 0 | 0 | 24 |
| calibration-inputs | **1** | **2** | 0 | 24 |
| breit-wheeler-observation | 0 | 0 | 0 | 24 |
| breit-wheeler-pair-production-derivation | 0 | 0 | 0 | 24 |
| sl-n-color-framing (no in-tree sidecar) | 0 | 0 | 0 | 27 |
| sl-n-color-frame-scope (no in-tree sidecar) | 0 | 0 | 0 | 24 |

`calibration-inputs.md:208`: `voice-unicode-crash` (critical) + `voice-emoji-content`
on the `> **⚠ Vintage: this row is CODATA 2018 ...**` banner (the `⚠`), and
`voice-author-notes-pollution` x2 at :212 (a status banner in prose, §4d).
Pre-existing (blame fee4ad592), not introduced by #7825. Not fixed here.

## Still open (owner)

1. Move the pin to `a6e58846b` (or later)? Default: nothing changes, qa-sweep stays unloadable.
2. Where should refreshed verdicts land — in-tree `.qa.json` or the qa-reports store?

## 2026-11-15 — owner rulings P1 = B, P2 = yes (relayed by coordinator qou-s4ws)

- **P1 = B, done on PR #7842 (d00e3c24e):** pin -> platform main 82b389982a. run-validate gives
  16 issues at both pins with the lines identical; qa-sweep loads.
  **Known break found:** platform 0c5468ac46 DELETED `.github/workflows/publish.yml`, so
  `build.yml`'s `uses:` names a missing file. a6e58846b does NOT have this break.
  Owner choice at merge: keep B (render entry broken until qou carries its own publish), or
  fall back to A.
- **P2, done (4d63b18f5):** the calibration-inputs vintage banner moved to authorNotes;
  qa-sweep is now clean on that block.
- The sidecar-destination question was appended to `qou-6ccl` (it already is that question).

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-n4r9`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.


## Progress 2026-11-16 (Round 49 verification — kept `in-progress` per owner closure rule)

- **Verified at current `.folio-assistant-pin` (`82b389982a73701b77f723d34d42c77acf41b5b4` on `origin/main`):**
  - `bun /Users/litlfred/space_cats/folio-assistant/cat-harness-tools/pipeline/qa-sweep.ts --help` loads cleanly (`EXIT=0`) with zero missing-module errors (`cat-harness-tools/schemas/kg/cat-harness` resolves cleanly).


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- `.folio-assistant-pin` = `82b389982a73701b77f723d34d42c77acf41b5b4` (bumped by PR #7842, owner ruling P1 = B). The 2026-11-16 note above measured `qa-sweep.ts --help` loading at that pin with no missing-module error. Both open questions are answered: P1 = B (pin moved), and the verdict-destination question was moved to `qou-6ccl`.
- Still true and NOT closed by this: the `build.yml` `uses:` names `publish.yml`, which platform 0c5468ac46 deleted (recorded in the pin file). That is a separate defect about the render entry point, not about qa-sweep loading.
