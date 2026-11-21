---
# qou-4h26
title: The paper mathlib olean tree is ~1678 modules short of the root tree, so scripts/lean-content-sweep.sh emits ~855 phantom MISSING-OLEAN REDs
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:07:55Z
updated_at: 2026-11-21T17:58:40Z
parent: qou-5vkl
---

## Independent confirmation, and the one thing the union does not cover (2026-09-08, bean `qou-ei4q`)

A third container, reached from the other direction — `lean-shadow-verify.sh`
died on `import Mathlib.Tactic` while verifying a new `QOU/Mass` file. Same
asymmetry, same direction as yours: paper mathlib **2352** non-empty oleans and
**no** `Mathlib/Tactic.olean`, root **3469** with it.

`scripts/lean-sync-olean-trees.sh` fixes it exactly as designed. `--selftest`
PASS, and on the real tree: mathlib `3469 / 3258 -> 3548 / 3548`, batteries
`85 / 84 -> 85 / 85`, 740 files linked. Both locations identical afterwards, so
which one wins genuinely stops mattering. **I reverted my own reordering of
`lean-shadow-verify.sh` in favour of this** — your header says the paper-first
pin "is correct and is NOT changed here" and it was right; ordering only re-aims
the asymmetry, the union removes it. That script now only *diagnoses* the
imbalance and points here.

Two things to add, one of which is a caveat on the fix.

**1. It has no callers.** `git grep olean-union|lean-sync-olean-trees` over
`scripts/` and `.claude/` on `main` returns nothing — no sweep, no hook, no
skill invokes it. So until an agent runs it by hand the gate still fails the way
it failed for both of us, and the failure does not name the script. Worth wiring
into `lean-shadow-verify.sh` / `lean-content-sweep.sh` / `lean-library-sweep.py`
as a preflight, or into the SessionStart hook.

**2. THE UNION IS A SNAPSHOT TOO, because one tree is being WRITTEN.** This is
the part I think is new. The two trees are not "two different partial builds"
sitting still — `scripts/lean-build-bg.sh`, started by a **SessionStart hook**,
runs `lake build` with **cwd = the paper package** (confirmed via
`ls -l /proc/<pid>/cwd`, not inferred), so the paper tree is under construction
from minute one of every fresh session. Measured over ~40 min, one session, no
action of mine: paper went **2 -> 17** QOU oleans and **2352 -> 3007** mathlib
oleans while root sat unchanged at 2442 / 3469.

Consequences for this bean:

- **A union run during that build unions a moving target**, and goes stale as the
  build continues — the paper tree keeps gaining modules the root tree lacks. So
  "run it once at session start" is the wrong reflex; it wants to run *after* the
  build, or to be re-run.
- **Your 1802-vs-3480 and my 2352-vs-3469 may be the same tree at two ages**, not
  two containers configured differently. That would explain why the direction is
  reproducible while the numbers never match.
- **The root restore is NOT at risk** from this particular build — its cwd is the
  paper package — which is worth stating so nobody reaches for the 02kc eviction
  story when they see the counts move.

Recorded in `.claude/agent-memory/lean-verifier/verification-harness.md` §17a.

- **Round 94 (`litlfred/qou#8424`)**: Advanced in `feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1` (Commit 1 `c1698951b30460bb111c1e97552482f0b0622bd0`, Commit 2 `5a166eac86b999ab31c9bdd39f5908e1c848e122`, probe sha256 `1438398dfd335d3f6e9ebdcaa8df8fdc4613a507b4d480b0c9dde22e4b3c8bcb`).

2026-11-21 (PR #8885): wired. lean-library-sweep.py runs lean-sync-olean-trees.sh at start. lean-shadow-verify.sh (and so lean-content-sweep.sh) runs it when its imbalance check fires. Because it runs every sweep, it also re-unions a tree that the SessionStart build is still writing. Closes when #8885 merges.

2026-11-21: PR #8885 merged as 6731f98cf1 (owner approval). Closing.
