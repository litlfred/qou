---
# qou-fo7l
title: 'lean-library-sweep''s UNVERIFIED verdict is non-deterministic: it names a different present-on-disk package each run'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T13:04:28Z
updated_at: 2026-11-15T20:59:00Z
parent: qou-3e6w
---

Found 2026-10-10 while verifying `QOU/BraidKnot/PenaltyFamilyCeiling.lean` (bean
`qou-as81`, PR #7579).

## The finding

`scripts/lean-library-sweep.py --only-exact QOU.BraidKnot.PenaltyFamilyCeiling
--jobs 2` returns a **different verdict on repeated runs with no source change**,
and when it reports `UNVERIFIED` it names a **different package each time** —
every one of which is present on disk in both olean trees:

| run | verdict | named package |
|---|---|---|
| 1 | UNVERIFIED | `Batteries.Data.Array.Merge` (genuinely absent from the paper tree) |
| 2 (after `scripts/lean-sync-olean-trees.sh`) | **1 ok, 0 RED** | — |
| 3 | UNVERIFIED | `Qq` |
| 4 | UNVERIFIED | `LeanSearchClient` |
| 5 | UNVERIFIED | `LeanSearchClient` |

Run 1 was a real gap and the sync fixed it: the paper mathlib tree went
**2713 → 3486** oleans and `Batteries/Data/Array/Merge.olean` arrived. Run 2 is
the clean result. Runs 3-5 are **not** the same class — measured directly,
`Qq.olean` and `LeanSearchClient.olean` are present with a top-level olean in
**both** `.lake/packages/<pkg>/.lake/build/lib/lean/` and
`folio/quantum-observable-universe/lean/.lake/packages/<pkg>/.lake/build/lib/lean/`
(1 each, both trees, for `LeanSearchClient`, `Qq`, `aesop`, `plausible`). Two
further `lean-sync-olean-trees.sh` runs linked `plausible` (10 files) and then
nothing, so the trees are stable while the verdict is not.

Independent evidence the file is fine: `lean -DautoImplicit=false -s 65536` on it
exits **0** against the root olean tree, with `#print axioms` clean on all 12
declarations.

## Why it matters

The sweep is the gate AGENTS.md tells agents to prefer over bare `lean`-direct on
any branch touching `.lean`, on the grounds that lean-direct's green is a claim
about a snapshot. A gate whose verdict flips between runs cannot discharge that —
and the failure direction is the benign-looking one: `UNVERIFIED` is labelled
"NOT failing", so it reads as a shrug rather than as a gate that did not run.
An agent who happens to get run 2 reports a clean sweep; one who gets run 4
reports nothing was verified; neither is wrong about what it saw.

Note the sweep's own message says `(build order)`, i.e. it is reporting its
shadow's construction rather than the corpus — so it is almost certainly a
shadow-linking or `LEAN_PATH`-ordering effect inside the sweep, not a missing
olean. `scripts/lean-sync-olean-trees.sh`'s own header documents that both
orderings (PAPER-first and ROOT-first) have been measured to fail in opposite
directions (beans `qou-4h26`, `qou-tpdg`), which is the neighbourhood.

## Not done, deliberately

Not investigated or fixed here — under §🟥 ASK THE OWNER this is neither a
precision fix nor corpus-derived, and chasing sweep plumbing was not the task.
Recorded so the next agent who gets an `UNVERIFIED` on a file that lean-direct
passes knows it is a measured flake and not their file.

## What would settle it

Run the sweep ≥ 5 times on an unchanged file and log, per run, the shadow path,
the constructed `LEAN_PATH`, and whether the named olean exists under each root.
If the named package is present on disk every time, the bug is in the shadow
link or the path order, and the fix is in `lean-shadow-verify.sh` /
`lean-library-sweep.py`, not in the olean trees.

## 2026-11-15 — PR opened (`Q-3E6W-1 = 1`)

- PR: https://github.com/litlfred/qou/pull/8000 (`claude/qou-fo7l-zx9y-2026-11-15`, head `59133917a93a808efb21853b8dfef6b8cd35880e`)
- Fixed `find_oleans()` to pick by largest non-empty `.olean` count, deterministically sorted `siblings` and `pkg_roots` (ordering `PKG` and `ROOT` package roots ahead of other `folio/*` roots and filtering out incomplete package roots), sorted `missing` diagnostics by module name before reporting `UNVERIFIED`, and classified Mathlib dependency packages (`Qq`, `Batteries`, `LeanSearchClient`, `Aesop`, `Plausible`, `ImportGraph`, `ProofWidgets`) as `mathlib dep cache`.
- Verified with 5 consecutive runs of `python3 scripts/lean-library-sweep.py --only-exact QOU.BraidKnot.PenaltyFamilyCeiling --jobs 2` -> 5/5 `1 ok, 0 RED, 0 UNVERIFIED`.
