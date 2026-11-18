---
# qou-rc7b
title: 'BUILD COVERAGE: `lake build` reaches only 853 of 1618 QOU Lean modules — 47% never compiled'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T09:29:19Z
updated_at: 2026-10-04T15:14:41Z
parent: qou-5vkl
---


`lake build` in `folio/quantum-observable-universe/lean/` builds the default
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

---

## Drain executed — 2026-08-08

`globs = ["QOU", "QOU.+"]` is **flipped** and the tree drained. 45 modules
fixed across the sweep. Coverage went from **888 oleans / 1654 modules (53%)**
to **1652 / 1654**.

The 7% estimate above was in the right ballpark for *rate* but the sample
badly understated *concentration*: `QOU/Mathlib/HeckeAlgebra.lean` alone
carried 101 errors, and one module (`exists_axiom_2_observability.lean`) had
no `import` line at all.

### What the 766 actually contained

Overwhelmingly one defect — a declaration at file scope that every call site
addresses through a namespace — but it presents in **five** distinct error
shapes, which is why earlier sweeps kept missing subsets of it:

| shape | when |
|---|---|
| `Invalid field 'x'` | receiver's type is a `structure` |
| `Unknown constant 'NS.x'` | written out explicitly |
| `Invalid dotted identifier` | `.ctor` with undetermined expected type |
| `Invalid field: … 'Function.x'` | type is a `def` whnf-ing to a Pi |
| `'NS.x' has already been declared` | two blocks both claiming the bare name |

The last one only appears once a *sibling* block is also fixed, so it cannot
be enumerated up front. HeckeAlgebra had four `def one`, three `def basis`,
three `def basis_count` and three `def mulSigmaAbstract` all colliding at
module scope.

Three defect classes the blind spot hid that **no sorry census would ever
show**:

1. never-compiled modules (the 766),
2. unaudited vacuity — e.g. `PentagonUvCommutation`'s `∨ True` (bean
   qou-zzhw), invisible while the module was outside the build,
3. plausible-looking calls to API that does not exist — `SDPRankEquality`
   invoked two invented Mathlib lemmas; `JointGaloisBraidAction` carried a
   live global instance against a 5-field class built from a stale 2-field
   shape, in a file whose own siblings comment such instances out per
   AGENTS.md §3b-cond.

### Method note — standalone `lean` is NOT authoritative

Verifying a file with `lean` against the build's `LEAN_PATH` gives false
greens: the seeded olean cache can be **stale relative to current sources**.
`QOU/BraidKnot/SubstrateEWHypotheses.lean` verified clean that way and then
failed under `lake build`, because the cached
`CategoricalHiggsIdempotent.olean` predated the refactor that moved
`gauge_coupling_g`, `vev_v_GeV` &c. into class fields. Standalone `lean` is
fine as a fast inner loop; **only `lake build` closes a module.**

### Remaining

- `QOU/Machinery/MarkovTraceH4.lean` compiles but takes **over an hour**.
  Not a correctness problem; it is now the critical path of every full build
  and wants its own bean.
- Re-run the corpus sorry/vacuity audit (qou-joo5): every previous figure was
  measured on 53% of the tree.
- Correct the premise sentence in
  `docs/audits/2026-06-28-content-sibling-compile-sweep.md` and
  `.github/workflows/lean-content-siblings.yml` (still open from above).

---

## DRAIN COMPLETE — 2026-08-09

`lake build` **exit 0, 0 failing modules, 1675/1675.** The 47% blind spot is
closed and the glob stays widened, so the closure cannot silently shrink again.

Final tally: **50 modules fixed.** The section above ("Drain executed") was
written one module short of done and understated two things.

### The "~55 broken modules" estimate was right on rate, wrong on shape

The stratified sample put 1/14 ≈ 7% and projected ~55. Roughly right for
*count*, badly wrong for *concentration and kind*:

- `QOU/Mathlib/HeckeAlgebra.lean` alone carried **101 errors**.
- `exists_axiom_2_observability.lean` had **no `import` line at all**.
- `MarkovTraceH4.lean` needed **~15 GB** and could not compile in the container
  at any setting (bean qou-8hjy, resolved by splitting).
- One module carried a **theorem that is false** (below).

A 14-module sample cannot see any of those; they are tail events, and the tail
is where the interesting failures were.

### A fourth false statement, and the first that was not a `sorry`

`QOU/BraidKnot/HiggsCategoricalMassFormula.lean` asserted the W- and
Z-anchored Higgs predictions agree given `m_W/m_Z = P_3/P_2`. Substituting
gives `m_Z·P_3·P_4·S/P_2^2` versus `m_Z·P_4·S/P_3` — equal only if
`P_3^2 = P_2^2`, which holds only at `h = 0`. At `h = 1` the two predictions
differ by a factor of **6.76**.

Tranche 2 of this PR found three *cited `sorry`s* guarding false propositions.
This is the same defect one step worse: a **theorem**, with a tactic proof that
simply does not go through. It was invisible for exactly the reason all of this
was invisible — the module was never built. Replaced by
`higgs_W_Z_prediction_ratio`, stating the exact `(P_3/P_2)^2` discrepancy under
the nonvanishing hypotheses the original never carried.

**Consequence for the audit story:** a sorry census cannot find this class, and
neither can a vacuity scanner. Only compiling the module can.

### Method note, corrected

An earlier note here said standalone `lean` gives false greens because the
olean cache can be stale. True, and there is a second, larger reason: **a build
that dies partway never reaches the modules after it.** `Summary.lean` and
`HyperbolicVolumeTranscendence.lean` were both clean-looking for the whole
sweep purely because every full build died on `MarkovTraceH4` first. Neither
had ever been compiled. Only a build that runs to **exit 0** licenses any claim
about the tree.

### Census on the complete tree

**34 `sorry`s across 28 modules.** Every corpus figure recorded before this —
including the ones in qou-joo5 — was measured on 53% of the tree and is an
undercount by construction.

### Remaining from the original todo list

- [x] Sweep for the mechanical signatures — done, 50 modules.
- [x] Flip `globs = ["QOU", "QOU.+"]` — done, and now green.
- [ ] Correct the premise sentence in
      `docs/audits/2026-06-28-content-sibling-compile-sweep.md` and
      `.github/workflows/lean-content-siblings.yml`.
- [ ] Re-run the corpus sorry/vacuity audit (qou-joo5) against 34/28.
