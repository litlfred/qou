---
# qou-rz8m
title: 'GAP: lean-coverage tool version drift — refresh-authors-note rewrites 97.2%->93.9% from platform version alone'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T11:05:51Z
updated_at: 2026-11-19T16:48:42Z
parent: qou-n4r9
---

Found during `/prepare-merge` on PR #4597
(`claude/hypercharge-second-invariant-2026-08-02`).

## Symptom

`scripts/check-sidecars.sh` reports *"authors-note Lean-coverage stats
STALE (proved-counts drifted)"*. Running the prescribed fix,
`bun run scripts/refresh-authors-note.ts`, rewrites the advertised
coverage **downward**:

| field | committed | after refresh |
|---|---|---|
| `provable.sorry_free` | 684 | 661 |
| `provable.percent_sorry_free` | 97.2 | 93.9 |
| `provable.with_lean_file` | 699 | 698 |
| `conjectures.class_axiomatized` | 158 | 157 |
| `conjectures.percent_class_axiomatized` | 92.4 | **key removed** |
| `conjectures.with_lean_file` | 168 | **key removed** |

## Why this is NOT the branch's doing

1. **The committed JSON carries keys the current tool no longer emits**
   (`percent_class_axiomatized`, `conjectures.with_lean_file`). A tool
   cannot drop keys it still writes, so the committed file was produced
   by a *different version* of
   `folio-assistant/scripts/lean-coverage`.
2. **PR #4597 adds only library Lean** — `QOU/StandardModel/*.lean`
   with no `.ts`/`.md` content-block siblings. `computeStats` counts
   *provable content blocks*; a branch that adds zero content blocks
   cannot move that count by 23.

So the delta measures the platform clone
(`scripts/setup-folio-assistant.sh` → whatever `folio-assistant` HEAD
is at the time) against whichever platform version last wrote the
committed JSON — not any change in the paper.

The refresh was therefore **reverted, not committed**, on #4597:
committing it would have published a false 93.9% and silently dropped
two schema keys, attributing a platform-version change to this PR.

## Why it matters

`check-sidecars.sh` flags this on *every* branch, so every agent that
obeys the "resolve ⚠ before commit" instruction will write the same
spurious number into `authors-note.md` — the paper's own advertised
formalisation coverage. It is a standing trap, and the first agent to
comply lands the regression.

## Next honest step

1. Pin or record the `folio-assistant` commit that produces the
   committed `lean-coverage.json` (the qou side has no lockfile for the
   platform clone — `setup-folio-assistant.sh` takes HEAD).
2. Decide which tool version is canonical, regenerate once against it,
   and commit note + JSON together.
3. Until then, treat the `check-sidecars.sh` authors-note ⚠ as a known
   false positive and do **not** commit the refresh from a feature
   branch.



## Completed (2026-11-19)
Completed: fixed `scripts/refresh-authors-note.ts` import path and refreshed `introduction/authors-note.md` + `introduction/lean-coverage.json` to `741/741 provable sorry-free (100%)` (`refresh-authors-note.ts --check` exit `0`).
