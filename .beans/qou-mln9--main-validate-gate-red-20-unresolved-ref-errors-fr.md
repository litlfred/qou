---
# qou-mln9
title: 'main validate gate RED: 20 unresolved-ref errors from eightfold-way / mass-binding-appendix landings (def:hecke-algebra, def:octonion-algebra, alg:delta-lambda-closure, prop:q-deformation-weight-lattice)'
status: todo
type: task
priority: high
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-08-07T01:00:00Z
---

## Symptom

`bun run scripts/run-validate.ts content/quantum-observable-universe` on
current `main` exits 1 with **20 issues**. This blocks the validate gate for
**every branch**, not only the ones that introduced it.

Named failures:

| block | error |
|---|---|
| `q-deformation-weight-lattice` | Import error |
| `mba-sidecar-delta-lambda-closure` | algorithm block `alg:delta-lambda-closure` must cite at least one provable in `uses[]` — algorithms are downstream of math |
| `a2-from-three-strands` | Unresolved uses: `def:hecke-algebra` |
| `meson-mass-splitting` | Unresolved uses: `prop:q-deformation-weight-lattice` |
| `schur-weyl-eightfold` | Unresolved uses: `def:hecke-algebra` |
| `color-su3-from-g2` | Unresolved uses: `def:octonion-algebra` |
| `mba-sidecar-mirror-cancellation` | Unresolved uses: `alg:delta-lambda-closure` |

## Diagnosis sketch

Two distinct classes, likely two different fixes:

1. **Missing definition blocks.** `def:hecke-algebra` and
   `def:octonion-algebra` are referenced by the eightfold-way blocks but do
   not resolve. Either the blocks were authored expecting definitions that
   were never landed, or the labels are wrong (a Hecke-algebra definition
   almost certainly exists somewhere in the corpus under another label —
   **corpus-grep before creating a new one**).
2. **Cascade from a schema-invalid block.** `q-deformation-weight-lattice`
   fails to import, which is why `meson-mass-splitting`'s reference to
   `prop:q-deformation-weight-lattice` cannot resolve. Fix the import and the
   dependent error likely clears. Same shape for
   `alg:delta-lambda-closure` → `mba-sidecar-mirror-cancellation`.

So the effective count is smaller than 20 — several are downstream of two or
three root causes.

## Ownership note

These came in with recent eightfold-way (`content(eightfold §…)`) and
mass-binding-appendix landings. **Coordinate before fixing** — the authors are
probably mid-tranche and may have the definitions in flight on a branch.
Posting intent on the relevant sibling PRs is cheaper than a collision.

## Why high priority

It is not a math gap, it is a gate outage. Every agent running the standard
pre-commit checks currently sees a red validate they did not cause, which
trains people to ignore it — the expensive failure mode.
