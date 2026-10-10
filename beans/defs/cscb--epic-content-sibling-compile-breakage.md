---
# cscb
title: 'EPIC: repair content-sibling .lean standalone-compile breakage (~300+ files, ~57%)'
status: completed
type: epic
priority: high
created_at: 2026-06-28T16:00:00Z
updated_at: 2026-09-13T18:05:00Z
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


## 🟩 DONE — 938 of 938 compile, 0 RED (measured 2026-09-13, bean qou-g5sp)

This EPIC's **Done when** is:

> Every content-sibling `.lean` compiles standalone (`lake env lean` exit 0), or
> the residue is a small, documented set of genuinely-hard cases tracked as
> child beans.

**The first disjunct is met, with no residue.** `scripts/lean-content-sweep.sh`
over every `content/**/*.lean` outside the `lean/` package trees, on `main`
`16ccc3f7e2`:

```
=== swept 938, RED 0 ===
```

938 targets, every one `exit 0` with zero `: error:` lines. Per-file data:
[`docs/audits/2026-09-13-content-sibling-compile-sweep.tsv`](../docs/audits/2026-09-13-content-sibling-compile-sweep.tsv);
write-up:
[`2026-09-13-every-content-sibling-compiles-zero-red.md`](../docs/audits/2026-09-13-every-content-sibling-compiles-zero-red.md).

**Wider than this EPIC's own scope.** It counts 892 QOU siblings; the sweep
covers **938 across all three papers plus the visualizer** — QOU 902, UGB 22,
fred2005 12, visualizer 2. The UGB and fred2005 siblings are reachable by
neither this EPIC's original sweep nor `lean-library-sweep.py`, so no previous
count in the corpus spans them.

## 🛑 The ~57 % is NOT shown to have been wrong — say which claim you mean

This measurement establishes that the population is green **now**. It does
**not** re-run the 2026-06-28 `lake env lean` sweep, and is **no evidence at all
about it**. The likeliest reading is the boring one: this EPIC was right, and
the 2.5 months of repair work it set in motion — `qou-e7xv`'s five passes,
`qou-0xrn`, `qou-8qby`, `qou-xdwp`, `qou-isps`, `qou-29pv` and siblings — closed
it. That is the EPIC succeeding, not the EPIC being wrong.

**What is defective is the title**, which still reads *"~300+ files, ~57%"* at
`priority: high`. That one line is what an agent triaging the backlog sees, and
it has been ~2.5 months stale against a population that is now entirely green —
the exact failure mode this repo's AGENTS.md is a monument to.

## Why this green is not a silent skip

- **Flags:** `-DautoImplicit=false -s 65536`, set by the script. A bare `lean`
  does not read the lakefile and defaults `autoImplicit` *true*, which silently
  auto-binds an unbound identifier instead of erroring — strictly weaker than
  Lake (`qou-56qy`). This sweep does not have that hole; note the EPIC's own
  original method (`lake env lean`) did not either.
- **Positive control:** `theorem bogus : 1 = 2 := rfl` through the identical
  command and `LEAN_PATH` returns **exit 1, 2 errors**. The harness reports RED
  when RED exists.
- 939 logs for 938 targets; no `lake` invoked, so the restored cache is intact.

## Scope

The shadow rebuilt **260** library modules from source and trusted ~2532 whose
olean postdates their source — the standing snapshot-conditionality of
`qou-56qy`. **The companion run removes it:** the same container's
`lean-library-sweep.py --all` judged **2836 of 2836** library modules with
*nothing* trusted at **0 RED**, which is exactly that trusted population. So
between the two runs no library module is assumed rather than compiled.
Residual conditionality is against Mathlib only.

## The forward half of this EPIC, restated

Its §"This is now gated forward" says PR #2964 added a diff-scoped
`content-sibling-compile` CI job, and its last line offers:

> Whole-tree `content-sibling-compile` could then be promoted from diff-scoped
> to a full gate.

The backlog that diff-scoping existed to avoid blocking on is now **empty**, so
the promotion is unblocked on its own terms. It is **not** actioned here, and
the reason is not this EPIC's to fix: every workflow in this repo is
`workflow_dispatch`-only under the 2026-06-30 owner directive (Actions billing),
reaffirmed 2026-08-09. A whole-tree gate in a workflow nothing triggers changes
nothing. The live gate today is `scripts/lean-content-sweep.sh` run by hand,
wired into `/prepare-merge` §4 and `prepare-merge-auto` Phases 1 and 4 — which
is what a gate means under §"QA is agent-owned; CI is a backup".

Status → completed. If the owner wants the CI promotion tracked separately, it
is a one-line workflow change gated on a billing decision they have already
made twice, not a remediation task.
