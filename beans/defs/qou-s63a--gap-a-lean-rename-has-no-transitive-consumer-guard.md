---
# qou-s63a
title: 'GAP: a Lean rename has no transitive-consumer guard — two regressions reached main from the same one-level check'
status: in-progress
pr: 8333
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T16:26:11Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

## The evidence — two regressions, one cause, both mine

Both reached `main` and sat there red:

| module | rename | PR | how the check missed it |
|---|---|---|---|
| `QOU/Archimedean/MassGapGm.lean` | `GroundRing.hbar_q` -> `hbarQ` | #6191 | final "three stragglers" batch got **no** importer check |
| `QOU/BraidKnot/KeystoneMcKayValueMap.lean` | `BraidKnot.qInt` -> `qIntGeo` | #6257 | reaches the name via `open QOU.BraidKnot (qInt qFactorial)` — **second-order**, my check was one level deep |

Both fixed in #6278.

## Why nothing caught them

Two independent gaps, and BOTH have to close or the third one lands:

1. **`lean QOU.lean` is not a corpus-wide gate**, and #6191 measured exactly that
   — the root reaches **1290 of 2389** modules; **1099 (46%) are outside it**.
   Neither broken module is in the 1290. So the gate I used exits 0 while the
   corpus is red, and it did, twice.
2. **A rename's consumer set is the TRANSITIVE reverse-import cone, not the
   direct importers.** An `open Ns (name)` in a module that never imports the
   declaring module is a consumer with no import edge to the declaring FILE.

## What would close it

A script that, given a renamed FQN, computes the transitive reverse-import cone
and compiles it `lean`-direct. The parsing half already exists — the reverse
edges are exactly what `scripts/lean-duplicate-fqn-audit.py`'s `IMP` scan
builds, and `scripts/lean-name-surface-audit.py` already imports that parser
rather than copying it. What is missing is:

- reverse-edge closure (currently nobody computes it);
- resolving `open Ns (name)` as a use-edge, not only `import`;
- a driver that takes `old -> new` and compiles the cone.

Cost estimate is honest-but-unmeasured: the cone for a low-level module such as
`GroundRing` may be large, and `PauliWitness/Witness12B` already exceeds 900 s
on pristine main, so a full-cone compile is not free. A cheaper first cut is
**grep the cone for the old identifier and compile only the hits** — which
would have caught both of these, since both still *mention* the old name.

## Do NOT read this as "add it to the merge pipeline"

That is an authorial call, not mine. The pipeline is already long, CI is
`workflow_dispatch`-only, and a gate that takes 20 minutes on a low-level
rename will be skipped. A hand-run script invoked when a rename is in the diff
is the cheaper shape and is what I would build.

Bean opened 2026-08-30 from PR #6278 rather than left implicit, per the
report-unclaimed-work rule: the two fixes are claimed work, the missing guard
is not.


## Round 56 Implementation (PR #8333)
- Implemented on branch `claude/round56-trd0-9nnz-fixes` (commit `e33bff7d43b72a19e618441a16ae41a21af05e0e`, https://github.com/litlfred/qou/pull/8333).

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

Still open on main: no rename/transitive-consumer guard script under `scripts/` at `2ae54ab401`. A guard is proposed on open PR #8333 (not merged). Note that today's whole-library lean-direct sweep (`lean-direct-cone.sh --all -k`, see issue #8817) is the corpus-wide check this bean says `lean QOU.lean` is not; it is about 2 h on 4 cores.
