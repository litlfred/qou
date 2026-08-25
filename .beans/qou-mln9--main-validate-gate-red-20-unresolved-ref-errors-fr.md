---
# qou-mln9
title: 'main validate gate RED: 20 unresolved-ref errors from eightfold-way / mass-binding-appendix landings (def:hecke-algebra, def:octonion-algebra, alg:delta-lambda-closure, prop:q-deformation-weight-lattice)'
status: todo
type: task
priority: high
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-08-25T17:05:16Z
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

## Verified fixed on main 2026-08-16 — closing evidence, not a new fix

`bun run scripts/run-validate.ts content/quantum-observable-universe` on
`main @ 84ea022e18` exits **0**: `✓ Valid — 27 issue(s)`, all advisory
(`no Lean declaration yet`, dangling-remark, unknown-field). **Zero errors.**
Ran it both with and without the path argument; same result.

Checked it was fixed rather than suppressed. Three of the four named labels are
still absent from the corpus — so the repair was on the referring side, and it
was done the way this bean asked ("corpus-grep before creating a new one"):

| block | then | now |
|---|---|---|
| `a2-from-three-strands` | `def:hecke-algebra` (absent) | `def:braid-group`, `rem:hecke-algebra-from-braiding` — existing blocks |
| `meson-mass-splitting` | `prop:q-deformation-weight-lattice` | `rem:q-deformation-weight-lattice` — the label was `rem:`, not `prop:` |
| `schur-weyl-eightfold` | `def:hecke-algebra` | `prop:a2-from-three-strands` |
| `color-su3-from-g2` | `def:octonion-algebra` (absent) | `uses: []` with an in-file comment recording that the octonion algebra is used but never defined as a block, and a bean (`qou-8fl1`) |
| `mba-sidecar-mirror-cancellation` | `alg:delta-lambda-closure` unresolved | `alg:delta-lambda-closure` now exists (`appendix-mass-binding-algorithms/mba-sidecar-delta-lambda-closure.ts`) |

No block was deleted and no dependency was silently dropped — `color-su3-from-g2`
is the only one that lost an edge, and it is documented in place rather than
quietly removed.

Left at `todo`: closing is an owner action (AGENTS.md §4a). Nothing remains to
do on the symptom.


## Re-measured 2026-08-25T16:20Z — named failures drained, the CLASS recurred

Measured on pristine `origin/main` @ `8ce76190cd` in a clean worktree:

```
run-validate content/quantum-observable-universe
  ✗ Invalid — 36 issue(s), 9 errors
```

**None of the seven failures this bean names is still present.** `def:hecke-algebra`,
`def:octonion-algebra`, `alg:delta-lambda-closure` and `prop:q-deformation-weight-lattice`
all resolve on current main. So the instance recorded here is drained.

**But item 2 of this bean's own diagnosis — "cascade from a schema-invalid block" —
recurred, in a new instance, and it is 100 % of main's current error count.**
All 9 errors are one cascade:

```
✗ [gauge-coupling-uniqueness] (gauge-coupling-uniqueness.ts): Import error:
    Invalid enum value. Expected 'not_checked' | 'stub' | 'trivial' | 'external'
    | 'validated' | 'error' | 'leanok' | 'axioms_only', received 'lean_direct_exit_0'
✗ [alpha-em-categorical-trace]        Unresolved uses: "cor:gauge-coupling-uniqueness"
✗ [em-completeness-interpretation]    Unresolved uses: "cor:gauge-coupling-uniqueness"
✗ [gauge-coupling-uniqueness-novelty] Unresolved uses + interprets label not found
✗ [gauge-coupling-uniqueness-proof]   Unresolved uses: "cor:gauge-coupling-uniqueness"
✗ [physics-names-knot-operations]     Unresolved uses: "cor:gauge-coupling-uniqueness"
✗ [vdw-pskew-isolation]               Unresolved uses: "cor:gauge-coupling-uniqueness"
✗ [vdw-pskew-isolation-interpretation] Unresolved uses: "cor:gauge-coupling-uniqueness"
```

One invalid token in one `.ts` makes the schema reject the block on import, so its
label never registers, so every consumer of that label fails to resolve. Landed via
#5745 (`fed69b1c4d`); it is the only occurrence in that chapter, the other 67 blocks
using `not_checked` or `stub`.

**Fix pushed on PR #5761** (`ff6292960f` → `3d828dd0c5`): `lean_direct_exit_0` →
`leanok`. Branch + fix measures **0 errors, 24 issues, "✓ Valid"**. The 24 residual
are pre-existing warnings (unknown-field drops, two undefined cross-references),
not errors, and not that branch's.

**Left `todo` deliberately.** The named instance is drained and the new one has a
fix in flight, but #5761 is a **draft awaiting an owner merge decision** — until it
lands, main stays validate-RED for every branch, which is what this bean is about.
Closing is the author's call.

**The recurrence is the durable finding.** This is now twice that a single
schema-invalid block has taken the whole corpus validate red by label cascade. The
generalisable guard is a schema check on `lean.validation` at authoring time; the
enum is closed and the failure mode is silent at the point of the edit.
