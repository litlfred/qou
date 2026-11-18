---
# qou-shdv
title: 'MEASURED: the 3-branch stack shares 24 files; 2 have diverged, both benign, both invisible to per-PR CI'
status: in-progress
type: task
priority: medium
tags:
    - close-candidate
    - infra
    - ci
    - coordination
    - qou-glbl
    - reorg-2026-10-04
created_at: 2026-08-09T16:00:00Z
updated_at: 2026-10-04T15:26:08Z
parent: qou-5vkl
---

## Why this exists

**Files duplicated across a stack are invisible to per-PR CI by construction.**
Each PR's checks run against its own tree, so a file that two branches both
carry is validated twice against two possibly-different contents, and *neither*
run can see the difference. This has already bitten twice this session — the
`lean-content-siblings.yml` workflow diverged, and one copy was textually broken
with a note spliced mid-sentence.

This bean is the **measurement**, so the divergence set stops being rediscovered
by accident.

## The stack

| branch | role |
|---|---|
| `claude/fivetwo-level7-ladder-numerators` | the 5₂ saddle sum-rule lane |
| `claude/mathlibext-dilog-continuation-ift` | Li₂ continuation + scalar IFT (**owns** the shared `MathlibExt` dilog files) |
| `claude/probe-float64-and-orphan-gates` | the float64 / orphan gates (**owns** `scripts/probe-float64-guard.py`) |

Measured against `origin/main` at **`2c341838b4`**, 2026-08-09.

## The shared sets

**5₂ lane ∩ dilog/IFT lane — 13 files.** 11 byte-identical, 2 differ:

| file | state |
|---|---|
| `QOU.lean` | **differs, by design.** The 5₂ lane's copy carries the whole 5₂ import block plus `ComplexDilogarithmOnCut` / `ComplexDilogarithmInversion`, which exist only on that branch. The sibling's copy is a proper subset — not a divergence, a prefix. |
| `MathlibExt/ComplexDilogarithmLanden.lean` | **genuinely diverged.** The 5₂ lane is ahead by `92cba32697`, which drops the unused `ht : t ≤ 0` from `continuousOn_landenCombo_ofReal` and updates its caller. The sibling still carries both. |

**5₂ lane ∩ gates lane — 11 files**, all beans / workflows / gate scripts, none
touched by this session's Lean work.

## Is the Landen divergence dangerous? No — and here is why, so nobody "fixes" it

Both merge orders are clean, and the reason is that the signature change and its
**caller are in the same file**:

* sibling merges first → main has the `ht` version; the 5₂ lane is the only side
  that changed it from the common ancestor, so its version wins, self-consistent;
* 5₂ lane merges first → main has the `ht`-free version; the sibling changed
  nothing, so main's version wins.

⚠ **The actual risk is a well-meaning second fix.** `continuousOn_landenCombo_ofReal`
emits an unused-hypothesis warning on the sibling branch, and it is exactly the
kind of warning a reviewer clears in passing. If the sibling drops `ht`
*independently*, both sides have changed the same hunk and the merge conflicts
for the first time. Recorded here so that fix is recognised as already done
rather than still needed.

## What this does NOT license

The git constraint on these sessions is **never push to a branch other than the
designated one**. So the divergence is *recorded*, not repaired across branches:
the 5₂ lane cannot push the Landen cleanup onto the sibling, and the sibling
cannot pull it. Whoever merges second inherits the resolution for free.

## Re-measure with

```sh
git fetch origin main:refs/remotes/origin/main
git fetch origin <sibling>:refs/remotes/origin/<sibling>   # the colon form is required —
                                                           # plain `git fetch origin <b>` creates
                                                           # no tracking ref in this clone, and
                                                           # merge-tree then reports a bogus CONFLICT
comm -12 <(git diff --name-only origin/main...HEAD | sort) \
         <(git diff --name-only origin/main...origin/<sibling> | sort)
# then, per shared file:
git diff --quiet HEAD origin/<sibling> -- <file> && echo IDENTICAL || echo DIFFERS
```

## Refs

* `qou-glbl` (the lane that surfaced it), `qou-orph`, `qou-f64g`
* Prior instances: `lean-content-siblings.yml` (twice)

**The 5₂ sum rule remains verified to 80 dps, unproved.**
