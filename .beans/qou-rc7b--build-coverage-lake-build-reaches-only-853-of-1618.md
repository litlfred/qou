---
# qou-rc7b
title: 'BUILD COVERAGE: `lake build` reaches only 853 of 1618 QOU Lean modules — 47% never compiled'
status: in-progress
type: task
priority: high
created_at: 2026-08-08T09:29:19Z
updated_at: 2026-08-08T09:29:49Z
---


`lake build` in `content/quantum-observable-universe/lean/` builds the default
target `QOU`, which is the **root module `QOU.lean` plus its transitive
imports** — not the `lean/` tree. Measured on `claude/sorry-audit-joo5`
(2026-08-08):

| | count |
|---|---|
| `.lean` modules under `lean/QOU/` | 1618 |
| reachable from `QOU.lean` by `import` | 853 |
| **never compiled by `lake build`** | **766** (47%) |

Confirmed two independent ways:

1. **Import-closure walk** from `QOU.lean` over every `import QOU.*` line.
2. **Empirically** — after a green full `lake build` (4346 jobs),
   `find .lake/build/lib/lean/QOU -name '*.olean' | wc -l` = **860**.
   No olean exists for the other ~758.

## This is Lake's documented default, not a bug in the build

`Lake/Config/LeanLibConfig.lean:45` — `globs : Array Glob := roots.map Glob.one`.
A `lean_lib` with no explicit `globs` builds **only its root module**. The qou
lakefile sets `srcDir = "."` and no `globs`, so `srcDir` widens where Lake
*looks for* sources; it does not widen what gets *built*.

## It corrects a documented assumption

`docs/audits/2026-06-28-content-sibling-compile-sweep.md:11` and
`.github/workflows/lean-content-siblings.yml:4-6` both state the premise:

> content-block `.lean` siblings … live **outside** the CI-built
> `lake build QOU` target (the qou lakefile globs `srcDir="."` = the
> `lean/` tree only)

The parenthetical is wrong. `srcDir="."` is not a glob, and the library build
covers **53% of the `lean/` tree**, not all of it. The sibling sweep's own
numbers stand (it swept `content/**` outside `lean/`); what is wrong is the
belief that everything inside `lean/` is therefore covered.

## Concrete instance

`QOU/BraidKnot/SpechtIrreducible.lean` — the module holding
`specht_form_nondegenerate`, the single sorry gating the whole Specht
irreducibility chain (bean qou-0xyc) — is **not** in the closure. A full
`lake build` reports 11 `declaration uses 'sorry'` warnings and none of them
is this one. `lake build QOU.BraidKnot.SpechtIrreducible` builds it (1589
jobs) and reports it at line 1041.

So the corpus sorry count read off a package build is an undercount by
construction, independently of the "a module that fails to compile never
reports its own sorries" effect already recorded in qou-joo5.

## Why this is the same failure mode as the CI one

qou's Lean CI last ran 2026-04-25 and 37 modules rotted unseen (qou-k21h).
The lesson written into folio-assistant's prepare-merge / content-author /
content-test skills was "a workflow nobody runs is not a safety net". This is
the sibling: **a build target that reaches half the tree is not a safety net
either.** Both are invisible for the same reason — the artifact exists, so it
is assumed to be doing its job.

## Fix — and why it is not a one-liner

The mechanical change is one line in `lakefile.toml`:

```toml
[[lean_lib]]
name = "QOU"
srcDir = "."
globs = ["QOU", "QOU.+"]     # `.+` = Glob.andSubmodules
```

That will surface every latent break in the 766 at once. Before flipping it
someone has to measure the rot (a stratified sample is being taken on this
branch) and decide whether to fix, quarantine, or split into a second
`lean_lib` that CI builds warn-only. Flipping it blind would red the build for
everyone.

## Todo

- [ ] Finish the stratified sample; publish a pass/fail rate for the 766.
- [ ] Decide: fix-then-flip, or flip with a quarantine list.
- [ ] Correct the premise sentence in
      `docs/audits/2026-06-28-content-sibling-compile-sweep.md` and
      `.github/workflows/lean-content-siblings.yml`.
- [ ] Once flipped, re-run the corpus sorry audit (qou-joo5) — the current
      figure is measured on 53% of the tree.

## Stratified sample of the 766 — 2026-08-08

One module drawn at random from each of the 54 top-level `QOU.<dir>`
namespaces, shuffled, first 14 built with `lake build <module>` (which builds
dependencies too, so this is a real compile, not a cache-subset probe).

| result | count |
|---|---|
| PASS | 13 |
| FAIL | 1 |

**Failure rate 1/14 ≈ 7%.** Point estimate for the 766: **~55 broken
modules**. Treat that as an order of magnitude, not a figure — a 14-module
sample puts the 95% interval at roughly 0.2%–34%.

This is much better than the content-sibling sweep's 41% (those live outside
`lean/` entirely and were never in any build). The `lean/` orphans mostly do
compile; they are simply unwatched.

The single failure, `QOU.BraidsAndKnots.CombinerBranchingCompleteness`:

    Unknown constant `…CombinerBranchingCompleteness.IsSubPartition.refl`
    Invalid field `trans`: The environment does not contain `Function.trans`

Both are the **exact two signatures fixed in qou-k21h** — a `theorem
Foo.bar` declared inside a `namespace` landing at `Namespace.Foo.bar`, and
dot-notation on a `def … : Prop` unfolding to a Pi type so the lookup is
reported against `Function`. That sweep fixed what `lake build` reported, so
it never reached this file. Same bug class, one import edge away, invisible
for four months.

Sample data: `orphan-modules.txt` / `orphan-sample-results.txt` (scratch, not
committed — regenerate with the import-closure walk described above).

## Revised recommendation

At ~7%, fix-then-flip is realistic rather than a rewrite. Suggested order:

1. Sweep the 766 for the two known mechanical signatures first — they are
   scriptable and were already diagnosed in qou-k21h.
2. Compile the remainder in batches, quarantining what is genuinely stale.
3. Then flip `globs = ["QOU", "QOU.+"]` so the closure can never silently
   shrink again.
