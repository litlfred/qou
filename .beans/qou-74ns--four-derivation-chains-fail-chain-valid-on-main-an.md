---
# qou-74ns
title: Four derivation chains fail chain_valid on main, and main's committed audit witness says allPassed:True because it is stale
status: todo
type: task
priority: high
created_at: 2026-09-04T11:15:20Z
updated_at: 2026-09-04T11:15:59Z
---

Found 2026-09-04 on PR #6519, by running `derivation_chain_validator.py` after
merging 72 commits of `origin/main` into `claude/standard-model-terms-status-ftoejr`.
The validator exits **2** and writes `allPassed: False`. The failure is **not
numerical and not this branch's** — see the attribution below before treating
it as merge breakage.

## The four failing chains

| chain | reason reported |
|---|---|
| `D-tr-M-q0.derivation.json` | step *"Atomic D Hecke element T_w(Z=1, N=1) — NOT a braid word"*: script-cited step requires a `script: <path>` note |
| `n-tr-M-q0.derivation.json` | same shape, step *"Atomic n Hecke element T_w(Z=0, N=1)"* |
| `p-tr-M-q0.derivation.json` | same shape, step *"Atomic p Hecke element T_w(Z=1, N=0)"* |
| `markov-trace-assembly-deuteron.derivation.json` | step *"Per-irrep characters χ^λ_q(β_D) via Hoefsmit recipe"* cites `computations/hecke_character_symbolic.py`, **which does not exist** |

Three are a metadata defect in the derivation JSON (a step names a script
without carrying the `script:` key the schema requires). The fourth is a
dangling citation.

## The citation has NEVER resolved

`computations/hecke_character_symbolic.py` is absent at the branch's merge-base,
absent on `origin/main`, absent on this branch, and `git log --all -- <path>`
returns **no commit that ever touched it**. So this is not a file someone
deleted; the chain has cited a path that has never existed in this repository.

## Why `main` looks green: its audit witness is STALE, provably

`origin/main`'s committed `computations/derivation-chain-audit.witness.json`
records `allPassed: True` — measured against a tree that no longer exists.
Compare `origin/main` against itself:

    markov-trace-assembly-deuteron.derivation.json  (on main)  value = 0.5751722439177719
    derivation-chain-audit.witness.json             (on main)  leaf  = 0.3882864240747888

The witness records a leaf value the derivation JSON beside it has not held
since `9b00d47036` / `aec2eaa7cf` (the `qou-1ucq` fix, 2026-08-30..09-04),
which rewrote five derivation JSONs. Those commits did not regenerate this
audit, and the audit's own last regeneration (`038faafb73`) predates them.
So **`allPassed: True` on main is an artifact, not a passing run.**

## Attribution — measured, not assumed

- This branch changed **0** `*.derivation.json` files
  (`git diff --name-only <merge-base> <branch-head> -- '*.derivation.json'` is empty).
- `origin/main` changed **5**, and they are exactly the five involved here.
- The audit witness at `origin/main` **and** at this branch's pre-merge head
  (`47a5aca7f7`) both read `allPassed: True` with zero failing assertions; the
  failures appear only once main's derivation JSONs and a fresh validator run
  are in the same tree.

## Disposition on PR #6519

The freshly-computed witness is committed **as it stands, red**, rather than
reverted to main's stale green one. Restoring the stale artifact would be the
"make a red run green by widening a baseline" move AGENTS.md forbids, one
artifact type over.

## Next honest step (not taken here — out of this PR's scope)

1. Add the missing `script:` note to the three `T_w(Z,N)` steps, or drop the
   script citation if the step is not script-backed.
2. Decide what `hecke_character_symbolic.py` was meant to name. The Hoefsmit
   character route does exist in the corpus under other filenames; the chain
   should cite the real producer or say the step is narrative.
3. Regenerate `derivation-chain-audit.witness.json` on `main` in the same
   commit as either fix, so the artifact stops disagreeing with its own tree.

Related: `qou-1ucq` (completed — the 73×/122× numerical contradiction whose fix
rewrote these JSONs), `qou-rm57` (the convention-frame scoping of the same
documents).
