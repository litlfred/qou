---
# qou-i68l
title: three QOU modules do not compile on main, one broken today
status: todo
type: bug
priority: high
created_at: 2026-08-30T16:04:02Z
updated_at: 2026-08-30T16:04:02Z
---

Found while rebuilding the whole qou package to reseed the lake cache (2026-08-30). `lake build`
exits 1 with 11 errors across three modules. **NONE of them is touched by the Roth branch** -- this
is main's state.

    QOU/AppendixSurreals/collatz_block_descent.lean:131:43  unknown universe level `u`
    QOU/AppendixSurreals/collatz_block_descent.lean:149:66  unknown universe level `u`
    QOU/AppendixSurreals/collatz_block_descent.lean:159:10  Invalid <...> notation: expected type
                                                            could not be determined
    QOU/SchurWeyl/BranchingGenericity.lean:115:22          Application type mismatch
    QOU/SchurWeyl/BranchingGenericity.lean:115:43          rcases failed: `x : ?m.54` is not an
                                                            inductive datatype
    QOU/SchurWeyl/BranchingGenericity.lean:251:21          Application type mismatch
    QOU/SchurWeyl/TwoRowCorners.lean:179:21                Application type mismatch

Provenance -- last commit touching each:

    collatz_block_descent.lean    e31b8e376a  2026-08-30  lean(q-Collatz): prove the two remaining
    BranchingGenericity.lean      a4c0922674  2026-08-24  SchurWeyl: rule out beta_b = beta_i + 1
    TwoRowCorners.lean            eb8264e461  2026-08-23  lean(qou-uer7): the corners of a <=2-row

ONE OF THESE WAS BROKEN TODAY and merged. That is the point, not the individual errors.

WHY NOBODY SAW IT. Every workflow in this repo is `workflow_dispatch`-only by owner directive over
Actions billing, so nothing runs on push or PR. A module can stop compiling and nothing says so.
`.claude/skills/local/prepare-merge.md` already records the precedent: Lean CI last ran 2026-04-25,
failed, and 37 modules silently stopped compiling over the following four months. This is that same
mechanism producing three more, one of them the same day it was introduced.

WHAT MAKES IT INVISIBLE LOCALLY TOO: `lake build` at the REPO ROOT builds NOTHING -- the root
package declares no lean_lib, so it exits 0 with "Build completed successfully (0 jobs)" having
examined not one file. The root lakefile says so in a comment; the real command is
`lake build QOU UGB Fred2005`. Anyone gating on a bare root `lake build` gets a green that means
nothing.

NOT FIXED HERE. Three separate authors' work, none of it Roth. The cache seeded from this tree
simply carries no oleans for these three, which is honest -- the next build retries them and fails
the same way.

SUGGESTED: whoever owns each module fixes it; separately, a cheap local gate that actually compiles
the package (not the root no-op) would have caught all three at authoring time.
