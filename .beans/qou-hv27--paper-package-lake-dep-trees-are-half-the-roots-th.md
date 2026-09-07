---
# qou-hv27
title: Paper-package Lake dep trees are HALF the root's — the sweep gate reads it as 855 corpus REDs
status: todo
type: bug
priority: normal
created_at: 2026-09-07T18:28:49Z
updated_at: 2026-09-07T18:35:43Z
---

MEASURED 2026-09-07 while running the /prepare-merge Phase-4 gate on PR #7077 (merged as 8360a30ff).

THE SYMPTOM. scripts/lean-library-sweep.py returned 855 RED out of a 2776-module dirty closure. Classified by error text, every single one was the SAME class and there were ZERO source errors:
    855  MISSING-OLEAN   ("object file '...' of module X does not exist")
      0  everything else

THE CAUSE. The paper package keeps its OWN copies of the Lake dependency trees, separate from the repo root's, and they were roughly half-populated:
    tree                                                             oleans
    .lake/packages/mathlib/.lake/build/lib/lean                       3480   (root)
    content/quantum-observable-universe/lean/.lake/packages/mathlib/    1801   (paper)
    proofwidgets, paper vs root                                       8 vs 35
    batteries,    paper vs root                                      83 vs 85
133 distinct Mathlib modules were absent from the paper tree.

THE TELL, and it is worth internalising because it looks impossible: Mathlib.Tactic.Positivity.olean is PRESENT in root and ABSENT in paper, so content/.../QOU/BringsSurface/ColourCurveModulus.lean was simultaneously
    exit 0   under lean-direct with a root-derived LEAN_PATH
    RED      under lean-library-sweep.py
at the SAME commit, for a reason that is neither the file nor main. A green and a red on one file at one commit is the signature of this bug.

THE REPAIR — free, and it does NOT survive a fresh container, so re-apply it each session:
    ROOT=$(pwd)
    for pkg in mathlib batteries aesop proofwidgets Qq plausible LeanSearchClient importGraph; do
      SRC="$ROOT/.lake/packages/$pkg/.lake/build/lib/lean"
      DST="$ROOT/content/quantum-observable-universe/lean/.lake/packages/$pkg/.lake/build/lib/lean"
      [ -d "$SRC" ] && mkdir -p "$DST" && cp -rln "$SRC"/. "$DST"/
    done
cp -l hardlinks (same filesystem, no disk cost) and -n never overwrites a newer local build. Result: mathlib 1801 -> 3485, proofwidgets 8 -> 35, batteries 83 -> 85, disk unchanged. Re-running the sweep then gave 285 modules / 0 RED where the previous run was RED from module 4.

WHY IT MATTERS BEYOND ONE PR. This makes the repo's own merge gate produce false corpus verdicts, and they are the WORST kind of false verdict: hundreds of REDs naming real modules with plausible-looking errors. An agent that trusts them will 'fix' files whose imports are fine.

RELATION TO #7099 / qou-g5sp. That PR reached the same conclusion independently an hour earlier — 'a RED is a statement about the disk, not the corpus' — from a DIFFERENT cause (oleans built at an older commit, a hand-built patchwork). Two distinct mechanisms, one class. Its docstring fix (a RED means 'unverified here', never 'broken') is the right general guard; this bean is one concrete cause with a concrete repair. Posted there: #7099 comment 5574351684.

ONE CORRECTION TO #7099 worth carrying: it names lean-library-sweep.py as the sound gate BECAUSE it rebuilds from source. It rebuilds the DIRTY CLOSURE from source but only LINKS the dependency packages, so when those are short it inherits exactly the disk-dependence that PR retracts. More sound than lean-corpus-typecheck.py; not immune to the class.

WHAT IS NOT ESTABLISHED. Why the paper trees are short in the first place — whether lake-cache/qou-v4-24-0 seeds only the root, whether a partial SessionStart lake build populated one and not the other, or whether the paper package resolves deps to its own directory by design and the cache restore never covered it. That is the actual fix (seed both, or symlink paper -> root at restore time); the cp -rln above is a per-session workaround, not a cure.

SUGGESTED NEXT STEP: check scripts/lean-olean-cache-seed.sh and the restore recipe in .claude/skills/local/lean-environment-setup.md to see which trees they cover, then either extend the seed or make the paper trees symlinks to root.

SHARPENED 2026-09-07, and this SUPERSEDES the 'trees are short' framing above. The root cause is not that the paper tree is short -- it is that a PARTIAL tree SHADOWS a COMPLETE one, and the sweep's LEAN_PATH ordering decides which.

THE MECHANISM is already recorded in sibling bean qou-tpdg (in-progress, PR #6827, 2026-09-05), stated there as: 'Lean commits to the FIRST LEAN_PATH root containing the module's TOP-LEVEL NAMESPACE DIRECTORY and never consults a later root for anything under it.' Measured there three ways. So a tree that merely CONTAINS Mathlib/ captures every Mathlib import, however few oleans it actually holds; there is no fall-through.

WHAT THAT MEANS HERE. scripts/lean-library-sweep.py lines 335-336 order the roots PAPER FIRST:
    pkg_roots = ([... ROOT.glob('content/*/lean/.lake/packages/*/.lake/build/lib/lean')]
              +  [... ROOT.glob('.lake/packages/*/.lake/build/lib/lean')])
My paper tree had Mathlib/ with 1801 oleans, so Lean committed to it and never saw root's complete 3480. Hence 855 REDs.

THE ORDERING WAS A DELIBERATE FIX FOR THE MIRROR FAILURE, and the code comment says so: on the container behind qou-tpdg the ROOT tree was the broken one (1212 oleans, a 0-byte Mathlib/Tactic.olean, no Mathlib/Data/Real/Basic.olean) and globbing root produced 22 false REDs. That comment ends 'Globbing the root alone therefore makes this gate correct by luck of environment.'

*** THE POINT: putting the paper tree first has the IDENTICAL property with the containers swapped. *** qou-tpdg correctly identified the failure mode and then adopted its mirror image. Neither ordering is right, because the mechanism qou-tpdg itself documents -- first-root-wins, per top-level namespace, no fall-through -- means ANY single incomplete tree in front is fatal, and the sweep cannot know which tree is the complete one.

SO THE GENERAL FIX IS NOT AN ORDERING, IT IS A MERGE. Union the trees before sweeping, so whichever root Lean commits to is complete. That is exactly what the cp -rln repair in this bean does, which is why it worked, and it is why it is not merely a workaround: it is the shape of the correct fix.

THREE CANDIDATE FIXES, for the owner to pick -- NOT implemented, per the 2026-09-07 ask-the-owner directive (this is tooling, so neither precision-increasing nor corpus-derived):
  A. In lean-library-sweep.py, union the trees into the shadow before sweeping
     (hardlink, free) instead of concatenating roots on LEAN_PATH. Smallest
     change that removes the environment dependence entirely. Touches a gate
     script owned by qou-tpdg's arc.
  B. Extend scripts/lean-olean-cache-seed.sh to cover the paper DEP trees. It
     currently covers root .lake/packages/<pkg>/.lake/build (line 248) and the
     paper's OWN library content/*/lean/.lake/build (line 257) -- but NOT
     content/*/lean/.lake/packages/<pkg>/.lake/build. Fixes the restore rather
     than the gate, so a fresh container starts consistent. Grows the cache
     branch, which is already ~1.7 GiB in 20 parts.
  C. Delete the partial paper dep trees at restore time so nothing shadows.
     Cheapest, but loses the guarantee qou-tpdg's comment relies on.

MY JUDGEMENT (not a finding): A, because it makes the gate correct regardless of which trees a container happens to have, and because the union is free on one filesystem. B is the better long-term fix but is a bigger change to a load-bearing cache with a live size budget.

COORDINATION: qou-tpdg is IN-PROGRESS and owned by another arc. Do NOT push a change to lean-library-sweep.py against it without checking in -- this bean is the finding, not a claim on their file. Their PR is #6827.
