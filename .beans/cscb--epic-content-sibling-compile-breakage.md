---
# cscb
title: 'EPIC: repair content-sibling .lean standalone-compile breakage (~300+ files, ~57%)'
status: in-progress
type: epic
priority: high
created_at: 2026-06-28T16:00:00Z
updated_at: 2026-06-28T16:00:00Z
---

A `lake env lean` sweep over all **892** content-block `.lean` siblings
(`content/quantum-observable-universe/**/*.lean` outside the `lean/` package)
found **~57% do not compile standalone**. These files live OUTSIDE the
CI-built `lake build QOU` target, so they were never compile-checked and
accumulated breakage over many PRs.

**This is now gated forward:** PR #2964 adds a diff-scoped
`content-sibling-compile` CI job (`lake env lean` on changed content-siblings)
so NEW breakage is blocked. This epic remediates the EXISTING backlog.

## Confirmed failure categories (genuine, diverse — not a harness artifact)
- **missing-import / unknown-decl** — e.g. `Unknown constant Nat.factorial`
  (needs `import Mathlib.Data.Nat.Factorial.Basic`); files with *no imports at all*.
- **bad/renamed import** — module split at the pinned Mathlib rev (e.g.
  `Mathlib.LinearAlgebra.Dimension` → `.Dimension.Finrank`; `Mathlib.Tactic.Omega`
  doesn't exist — `omega` is core).
- **orphaned body / syntax** — `unexpected token 'section'/'/--'` from a prior
  head-only comment-out leaving live proof bodies; stacked docstrings.
- **needs-noncomputable** — `compiler IR check failed … LaurentPolynomial.T has no
  executable code; mark noncomputable`.
- **proof / type error** — genuine `unsolved goals` / `type mismatch`.

## Method (mirror the vacuity tranche)
1. Sweep (`/tmp/sweep-results.tsv`) → categorize (`/tmp/sweep-categorized.tsv`,
   scratchpad `categorize.sh`): the full FAIL list + first-error per file.
2. Cluster the FAILs by directory + category into file-disjoint work-units.
3. Swarm: one high-quality agent per cluster — fix imports / restore orphaned
   bodies / `noncomputable` / renamed modules; **verify each `lake env lean`
   exit 0** before committing (cache is intact; do NOT `lake build`). No
   audit-dodging; preserve the math (a `: True`/`sorry` workaround is a failure).
4. Commit per-cluster; the diff-scoped CI gate confirms each fixed file.

## Done when
Every content-sibling `.lean` compiles standalone (`lake env lean` exit 0), or
the residue is a small, documented set of genuinely-hard cases tracked as
child beans. Whole-tree `content-sibling-compile` could then be promoted from
diff-scoped to a full gate.

(Exact file list + per-cluster children to be generated from the sweep once it
completes — count was ~303 FAIL at 535/892 swept.)
