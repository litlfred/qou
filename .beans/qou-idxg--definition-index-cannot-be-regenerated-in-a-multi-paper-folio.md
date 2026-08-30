---
# qou-idxg
title: 'The generated definition index cannot be regenerated in this folio — requirePaper() takes no argument'
status: todo
type: task
priority: medium
created_at: 2026-08-29T17:45:00Z
updated_at: 2026-08-29T17:45:00Z
---

Hit while demoting `thm:explicit-formula` → `conj:explicit-formula` (owner
decision, 2026-08-29). `content/quantum-observable-universe/index-of-definitions/definition-index.md`
is a **generated** artifact, committed to the repo, produced by the platform
script `folio-assistant/content/pipeline/generate-index.ts`. It cannot be run
here:

```
$ bun run folio-assistant/content/pipeline/generate-index.ts content/quantum-observable-universe
error: 5 papers found (bach2013-double-slit, fred2005-formal-groups,
quantum-observable-universe, unital-groebner-bases, visualizer) — name one explicitly.
```

The script calls `requirePaper()` at line 25 **with no argument**, and
`requirePaper(explicit?)` throws whenever the folio has more than one paper. It
reads no argv and no env var, and there is no wrapper in `scripts/` or any
workflow. So the documented path is unreachable in this repo, which has five
papers, and the positional argument the invocation seems to accept is ignored.

`requirePaper`'s own docstring says it replaced hardcoded
`"quantum-observable-universe"` defaults that *"silently pointed at a directory
that was not there"*. That fix is right; the caller was simply never updated to
pass the name it now must pass.

## The index is already stale, measured

Not a hypothetical consequence — the drift predates this branch. Comparing live
`label:` fields in `content/quantum-observable-universe` against the index rows:

```
live labels   1278
indexed       1269
dangling (indexed, not live)   1     <- introduced by this branch, hand-fixed
missing  (live, not indexed)  10     <- 2 from this branch, 8 pre-existing
```

The eight that predate this branch:

```
conj:qou-motivic-galois-instance        prop:atomic-q-reeb-universal-rho
prop:chi-sym-alt-closed-form            prop:delta-lambda-dt-index-unification
prop:delta-max-numerical-scale          prop:qbeta-toroidal-harmonics-basis
thm:birthday-axioms-underdetermine      thm:ideal-tetrahedron-law-of-sines
```

## What was done here, and why it is not the fix

The demotion left a dangling `#thm:explicit-formula` anchor, which
`run-validate` flags (13 → 14 issues). Since that warning was introduced by this
branch and the generator cannot run, the single row was **moved by hand** from
the Theorems table to the Conjectures table, in the generator's sort position —
the edit the generator would have produced. `run-validate` is back to its
pre-existing 13.

That is a patch on one row, not a fix. **Do not read the index as current**: the
eight missing entries above are still missing, and any future block will keep
missing until the generator can run. The repo rule is to regenerate generated
files with the repo's tooling and never by hand, and this is the exception that
proves it — hand-editing was the lesser evil only because a warning had been
introduced and the tooling was unavailable.

## Fix

One line in the platform repo (`litlfred/folio-assistant`): pass the paper
through, e.g. `requirePaper(Bun.argv[2])` — `requirePaper` already accepts the
`explicit?` argument and returns it unchanged. Then regenerate here and the ten
missing entries land in one commit. Worth adding a `scripts/` wrapper on the qou
side at the same time, so the invocation is discoverable; the grep that should
have found one returned nothing.
