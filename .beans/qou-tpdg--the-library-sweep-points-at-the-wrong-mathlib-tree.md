---
# qou-tpdg
title: The library sweep points at the wrong Mathlib tree — 22 false REDs, and the 2.3GB shadow is redundant
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T11:48:55Z
updated_at: 2026-09-05T12:12:58Z
---

## 2026-09-05 — measured, fixed, verified. PR #6827

`scripts/lean-library-sweep.py` is the gate AGENTS.md adopted TODAY for any
branch touching `.lean`, and in this container it was measuring itself.

**The mechanism (the reusable part).** Lean commits to the FIRST `LEAN_PATH`
root containing the module's TOP-LEVEL NAMESPACE DIRECTORY and never consults a
later root for anything under it. Measured 3 ways on one import whose olean IS
present in the real tree (476544 B):

  first root has no `QOU/`                    -> exit 0  (falls through)
  first root has `QOU/` + 1 unrelated module  -> exit 1  "does not exist"
  real tree only (control)                    -> exit 0

So a PARTIAL overlay MASKS the tree behind it. The error names the OVERLAY
path, so it reads as "missing from the corpus" when the module is present and
merely unreachable.

**Defect 1 — wrong Mathlib tree.** LEAN_PATH globbed `ROOT/.lake/packages/*`
plus each paper's own BUILD OUTPUT, never each paper's `.lake/packages/` — which
is the one the documented restore fills:

  ROOT  mathlib: Tactic.olean 0 BYTES (Aug 7), Data/Real/Basic MISSING, 1212
  PAPER mathlib: Tactic.olean 68040 B (Aug 29), Data/Real/Basic 785328 B, 3477

=> 22 REDs entirely about the environment, formatted like real findings.

**Defect 2 — the 2.3 GB copy.** `copytree` needs ~2.3 GB; 1.1 GB free against a
per-session quota, so the sweep died on ENOSPC having judged nothing. Now
hardlinked: `du` says 2.3 GB, `df` does not move. `build()` unlinks its target
(+ same-stem .olean.hash/.ilean) before `lean -o`, so no write through a shared
inode. Real-copy fallback on OSError.

**A claim of mine the measurement REFUTED.** I first read the copy as
REDUNDANT (shadow first, real tree last => should fall through). It does not —
see the mechanism. The full tree in the shadow is NECESSARY; hardlinking is what
makes it cheap. Shipping the first reading would have left the sweep judging
almost nothing while looking greener.

**Result.** RED 22 -> 0, skipped 15 -> 0, 22/22 ok, 33 s, 0 blocks of disk.
Safety verified not argued: the real tree's 2660 oleans snapshotted by inode,
size and mtime before and compared after — IDENTICAL on all 2660.

**Bonus:** `QOU.Braiding.SkeinNormalisation` reports `ok`, an independent
confirmation of the file merged in #6820.

**Still open / not done.** The AGENTS.md `lean`-direct recipe carries the same
overlay-masking trap (`LEAN_PATH="$SP/oleans:$LP"`, overlay first) and is NOT
edited here — changing the primary Lean verification guidance is not a passing
change. And `scripts/lean-content-sweep.sh` was not audited for the same
LEAN_PATH defect.


## 2026-09-05 (cont.) — the SIBLING gate had the same pair, plus two more

`scripts/lean-content-sweep.sh` delegates its whole LEAN_PATH + shadow build to
`scripts/lean-shadow-verify.sh`, which carried BOTH defects (root-only package
glob; real `cp -a`) plus two of its own:

3. **The documented `SHADOW=<dir>` reuse path never created its directory** —
   `$SHADOW` was only made by `mktemp -d` in the branch where SHADOW is UNSET,
   so the advertised form failed on first use with `cp: cannot create
   directory`. Pre-existing.
4. **My own fix to (1) reintroduced the bug it fixed.** I wrote
   `ls -d <paper-pat> <root-pat>` and **`ls` SORTS its arguments**:
   `$ROOT/.lake/...` sorts before `$ROOT/content/...`, so the broken root tree
   came back FIRST and Mathlib still resolved against it. Replaced with a loop
   (glob expansion keeps written order). The original was safe only because it
   had ONE pattern.

## 🛑 CREDIT — the mechanism was ALREADY DOCUMENTED; I re-derived it

Line 27 of `lean-shadow-verify.sh`: *"Lean resolves a module from the first
LEAN_PATH root holding that package directory, so the shadow must be complete,
not a sparse overlay."* So my three-way measurement CONFIRMS a documented fact
rather than discovering one, and my empty-shadow experiment tested a question
the comment two lines from the code already answered. Audit doc corrected. What
is new is the quantification, and that the Python sweep carries no such comment
— which is why it was re-derived there.

**Verified (shell path):** `SHADOW=<dir> lean-shadow-verify.sh
QOU/Braiding/SkeinNormalisation.lean` -> EXIT 0, both dirty cone modules
rebuilt, target clean; real tree's 2660 oleans IDENTICAL in inode, size and
mtime before/after. Disk moved 1 MB across the run.
