---
# qou-hv27
title: Paper-package Lake dep trees are HALF the root's — the sweep gate reads it as 855 corpus REDs
status: todo
type: bug
priority: normal
created_at: 2026-09-07T18:28:49Z
updated_at: 2026-09-07T18:29:28Z
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
