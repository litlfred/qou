---
# qou-orph
title: 'INFRA (measured): 761 of 1598 QOU Lean modules are never built by `lake build`'
status: completed
type: task
priority: high
tags:
    - lean
    - infra
    - lakefile
    - ci
created_at: 2026-08-07T23:50:00Z
updated_at: 2026-09-13T17:25:00Z
---


## The finding

`lake build` compiles **52%** of the QOU Lean library. The other **761 modules
are never compiled by anything** — not by `lake build`, not by CI, not by any
gate. A module can be broken for months and nothing says so.

```
modules under lean/QOU/       1598
reachable from QOU.lean        837
ORPHANED                       761   (47.6%)
```

**Re-measured 2026-08-08 against `origin/main` at `d4c9a36022`** (194 commits
later), by `content/pipeline/lean-orphan-audit.ts`:

```
modules under lean/QOU/       1621
reachable from QOU.lean        854
ORPHANED                       767   (47.3%)
```

Re-measured again at `origin/main` = `ee66f30102` (same day, later):

```
modules under lean/QOU/       1644
reachable from QOU.lean        858
ORPHANED                       786   (47.8%)
```

The ratio is stable across all three measurements; the library grows and the
orphan set grows with it. Largest orphan directories: `QOU.BraidKnot` 152,
`QOU.QBeta` 84, `QOU.Archimedean` 64, `QOU.MassTheory` 46, `QOU.Mathlib` 37,
`QOU.MathlibExt` 11.

**Every count above names the `origin/main` sha it was taken at.** That is the
format fix this bean's sibling `qou-mfst` argued for after two beans shipped
stale claims about main: a measurement without its base is a claim that ages
silently into a false one. Quote the sha with the number or do not quote the
number.

## Why

`content/quantum-observable-universe/lean/lakefile.toml`:

```toml
defaultTargets = ["QOU"]

[[lean_lib]]
name = "QOU"
srcDir = "."
```

`globs` is unset. Lake's default is `Glob.one` of `roots`, and `roots` defaults
to `#[<lib name>]` — so the glob is the **single module** `QOU`, and
`lake build` compiles exactly `QOU.lean` plus its transitive `import` closure.
**A file nothing imports is not in the library.** `srcDir = "."` sets where
Lake *looks*, not what it *builds*; that distinction is the whole bug.

The count above is that import closure, computed from the `import QOU.*` lines
in every `lean/QOU/**/*.lean` — reproduce it with the snippet at the bottom.

## How it surfaced

The 5₂ lane (`qou-0yqu`). All nine `FiveTwo*` modules were orphaned, including
the two that shipped in **PR #4658** as "sorry-free, axioms audited":

```
QOU.QBeta.FiveTwoCyclotomicBloch        <- merged in #4658
QOU.QBeta.FiveTwoLevelSevenLadder       <- PR #4701
QOU.QBeta.FiveTwoRogersExtend           <- PR #4701
QOU.QBeta.FiveTwoRogersReflection
QOU.QBeta.FiveTwoDTSpectrumSplit        <- pre-existing, and imported by 3 modules
QOU.QBeta.FiveTwoSaddleCurve            <- pre-existing
QOU.QBeta.FiveTwoSaddleSumRule          <- pre-existing
QOU.QBeta.FiveTwoStokesMatrixIdentities <- pre-existing
QOU.QBeta.FiveTwoSumRuleIntegrand       <- pre-existing
```

Those audits were real — the builds were run by hand, targeted, and the axioms
printed. But **nothing in the repo would have caught a later regression**, and
that is worth being blunt about: "sorry-free and axiom-audited" described a
build that happened once on someone's laptop, not a property the repo maintains.

Note `FiveTwoDTSpectrumSplit` is imported by three other modules and is *still*
orphaned — because those three are orphaned too. Orphaning is contagious
upward, so import-count is not a proxy for reachability.

## What was done about it, and what deliberately was not

**Done (PR #4701, scoped):** the three modules that lane has personally compiled
are now imported from `QOU.lean`, so `lake build` covers them.
`QOU.Archimedean.DilogReflection` was already in the closure (`QOU.lean:247`),
so this adds **no** new Mathlib cone — the marginal build cost is three small
files.

**Not done, deliberately:** the other 758. Two reasons, and the second is the
real one:

1. Scope — it was found on a PR about the 5₂ sum rule.
2. **Nobody knows whether they compile.** Wiring 758 unbuilt modules into the
   default target would, on current evidence, be a way of discovering how many
   are broken by breaking `lake build` for everyone at once.

## To fix — the honest sequencing

1. **Measure before deciding.** Compile the 758 orphans *individually*
   (`scripts/lean-verify.sh` is lean-direct, no lake lock, so this parallelises)
   and count how many already fail. That number decides everything below; do not
   guess it.
2. If the failure count is small, wire them in and let `lake build` hold the
   line.
3. If it is large, wire in the green ones, and add the red ones to an explicit
   quarantine list with a bean each. Do **not** set `globs = ["QOU.+"]` as a
   first move: it converts a silent, survivable problem into a red default
   build, which is worse than the status quo until step 1 has been done.
4. Whatever the outcome, add a gate that **fails on a NEW orphan** — a `.lean`
   under `lean/QOU/` that a PR adds without an import path from `QOU.lean`.
   Diff-scoped, in the style `lean-content-siblings.yml` already uses for the
   import-order backlog. That stops the number growing while the backlog is
   worked.

## ⚠ Related but different — do not conflate

`.github/workflows/lean-content-siblings.yml` already gates **content-block
siblings** (`content/<paper>/<chapter>/*.lean`), which are outside the lean tree
entirely. Its header says those "live OUTSIDE the CI-built `lake build QOU`
target (the qou lakefile globs srcDir='.' = the lean/ tree only)" — which reads
as if everything *inside* `lean/` is covered. **It is not**, and that sentence is
probably how this went unnoticed. Fixing the sentence is part of fixing this.

## Reproduce

```sh
cd content/quantum-observable-universe/lean
python3 - <<'PY'
import pathlib, re
root = pathlib.Path('.')
mods = {'QOU.' + str(p.relative_to('QOU')).replace('/', '.')[:-5]
        for p in root.glob('QOU/**/*.lean')}
imports = {'QOU.' + str(p.relative_to('QOU')).replace('/', '.')[:-5]:
           re.findall(r'^import (QOU\.[\w.]+)', p.read_text(), re.M)
           for p in root.glob('QOU/**/*.lean')}
seen, stack = set(), re.findall(r'^import (QOU\.[\w.]+)',
                                pathlib.Path('QOU.lean').read_text(), re.M)
while stack:
    m = stack.pop()
    if m not in seen:
        seen.add(m); stack.extend(imports.get(m, []))
print(len(mods), len(seen & mods), len(mods - seen))
PY
```

## Refs

* `qou-0yqu` (the 5₂ lane this surfaced in), `qou-rhyp`, `qou-mfst` (the other
  open lakefile-drift bean), PRs #4658 (merged), #4701

---

## 2026-08-08 — STEP 1 DONE for 153 of the 757 orphans: **94.8% are green**

The bean said "measure before deciding; that number decides everything below; do
not guess it." Measured, on the two directories this lane depends on:

| scope | orphans | fail | green |
|---|---|---|---|
| `QOU.QBeta.*` | 82 | **1** | 98.8% |
| `QOU.Archimedean.*` + `QOU.MathlibExt.*` | 71 | **7** | 90.1% |
| **total** | **153** | **8** | **94.8%** |

Method: `lake build <all orphans in scope>` in one invocation, so lake builds the
union of dependencies and reports every failure rather than stopping at the
first. Toolchain was already warm from the 5₂ lane's Mathlib cone.

### The eight, and what is actually wrong with them

**Mathlib drift — renamed or removed lemmas (3):**

* `QOU.MathlibExt` — `Unknown constant List.foldl_mul_eq_mul_prod` (×3),
  `Unknown constant Real.rpow_half_eq_sqrt`
* `QOU.MathlibExt.FrobeniusInnerProduct`
* `QOU.MathlibExt.PosSemidefDiagZero`

**Internal drift — QOU declarations that no longer exist (5):**

* `QOU.QBeta.FaddeevModularDouble` — `Eq.sq_eq_one_of_bar_even`, `Eq.inv`,
  `Eq.mul_bar_self`. The `Eq.` prefix is the tell: dot-notation fell back to `Eq`
  because the intended lemma is gone.
* `QOU.Archimedean.BreitWheelerPairProduction` — `TransferMatrixOperator.reduce_sigma_squared`
* `QOU.Archimedean.TorusKnot` — `TorusKnotLabel.seifertRank`, `.embeddableOn`
* `QOU.Archimedean.QMomentum` — `QMomentum.writhe`
* `QOU.Archimedean.yekutieli_leading_coefficient`

**Every one of these is the kind of breakage a build gate catches the day it
happens.** None is deep; all are stale references. That is the argument for step
4 (the new-orphan gate) more than any amount of prose.

### What this changes

The bean's step 2 applies: the failure count *is* small, so wiring the green
ones in is safe. Not done wholesale here — 145 new imports on a PR about the 5₂
sum rule invites conflicts with the ~120 in-progress sibling beans. What **was**
done: `QOU.MathlibExt.ComplexDilogarithm` is now imported from `QOU.lean`. It is
this lane's own dependency (a ~500-line sorry-free complex dilogarithm), it was
orphaned, and it builds green.

### For whoever does step 2 properly

* The measurement command is one line; reuse it per directory.
* Wire in the green ones **per directory**, not all at once, so a conflict with a
  sibling is a small rebase rather than a large one.
* The eight above should each get a bean or a fix first — do **not** wire them in
  and leave `lake build` red.
* 604 orphans are still unmeasured: `QOU.BraidKnot` (147), `QOU.MassTheory` (46),
  `QOU.BraidsAndKnots` (35), `QOU.Machinery` (29), `QOU.FluidDynamics` (26),
  `QOU.ParticleInteractions` (21), `QOU.Hecke` (20), and the tail.
  **Do not extrapolate 94.8% to them** — the two directories measured are the
  ones this lane has been actively working in, which is exactly the sampling bias
  that would make them healthier than average.

---

## 2026-08-08 — STEP 4 DONE: the gate exists, so the number stops growing

`content/pipeline/lean-orphan-audit.ts` + `.github/workflows/lean-orphan-gate.yml`.

Two modes:

```sh
bun run content/pipeline/lean-orphan-audit.ts                 # survey, always exit 0
bun run content/pipeline/lean-orphan-audit.ts --diff <files>  # GATE, exit 1 on a new orphan
```

Diff-scoped, in the style `lean-content-siblings.yml` already uses — a whole-tree
gate would block every PR on the ~750-module backlog. Paths outside the library
tree are ignored, so passing a PR's whole `.lean` diff is safe. Exit codes
verified directly (1 on an orphan, 0 on a wired module, 0 on survey) rather than
through a pipe, which reports the pipe's status.

**Also fixed the sentence this bean identified as the likely reason the problem
went unnoticed.** `lean-content-siblings.yml`'s header said the lakefile "globs
`srcDir='.'` = the lean/ tree only", which reads as though everything *inside*
`lean/` is covered by `lake build`. It is not, and that header is the most
natural place for someone to have formed the wrong belief. It now says so
explicitly and points at the new gate.

Workflow is `workflow_dispatch:` only — CI auto-triggers are disabled repo-wide
(owner directive 2026-06-30, Actions billing), so the **local command is the
real gate** today. That is a limitation of the repo, not of this change.

### Remaining on this bean

* **Steps 2-3: the backlog.** 604 orphans still unmeasured. Measure per
  directory, wire in the green ones per directory (small rebases, not one large
  one), bean or fix the red ones. Do not wire in a red module and leave
  `lake build` broken.
* **The eight known failures** listed above still need owners.


## 🟩 STEP 1 IS DONE, AND THE ANSWER IS ZERO — measured 2026-09-13 (bean qou-g5sp)

This bean's §"To fix — the honest sequencing" opens:

> **1. Measure before deciding.** Compile the 758 orphans *individually* … and
> count how many already fail. **That number decides everything below; do not
> guess it.**

**The number is ZERO.** Measured on `main` `16ccc3f7e2` with
`scripts/lean-library-sweep.py`, which compiles each module from source into a
hardlinked shadow — never invoking `lake`, so the restored olean cache is not
evicted. Four runs, unioned:

| run | selector | judged | RED |
|---|---|---|---|
| 1 | `--only-exact QOU` (the library root) | 1451 | 0 |
| 2 | `--all` | 2821 ok, 1 TIMEOUT, 14 skipped | 0 |
| 3 | `--all --only QOU.Hecke --timeout 5400` | 269 | 0 |
| 4 | `--all --only-exact …HeckeH4RepDecomp --timeout 5400` | 17 | 0 |

**2836 of 2836 modules judged, 0 RED.** Under `--all` nothing is trusted: every
module is rebuilt from source, so the stale-dependency false-RED class is
structurally impossible, and a signal death is reported `UNVERIFIED` rather than
RED. Write-up:
`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`.

### What that settles, step by step

* **Step 1 — measure.** Done. Not the 758 sampled, the whole 2836.
* **Step 2 — "if the failure count is small, wire them in and let `lake build`
  hold the line."** Already done, by bean **`qou-rc7b`** on 2026-08-08: the paper
  lakefile now declares `globs = ["QOU", "QOU.+"]`, and `QOU.+` is
  `Glob.andSubmodules`, so the library target is the whole tree. The measurement
  above is the retroactive justification that step 2 was the right branch.
* **Step 3 — quarantine the red ones.** **Moot.** There are none.
* **Step 4 — a gate that fails on a NEW orphan.** Done:
  `.github/workflows/lean-orphan-gate.yml`, diff-scoped, as this bean specified.
* **§"Remaining on this bean" — "604 orphans still unmeasured."** Now measured;
  all green.
* **§"The eight known failures … still need owners."** All eight are inside the
  2836 and none is RED, so all eight have been repaired in the intervening five
  weeks. Named for a reader who wants to check one: `QOU.MathlibExt`,
  `QOU.MathlibExt.FrobeniusInnerProduct`, `QOU.MathlibExt.PosSemidefDiagZero`,
  `QOU.QBeta.FaddeevModularDouble`, `QOU.Archimedean.BreitWheelerPairProduction`,
  `QOU.Archimedean.TorusKnot`, `QOU.Archimedean.QMomentum`,
  `QOU.Archimedean.yekutieli_leading_coefficient`.

### The title is now false, and so is the premise it spread

`761 of 1598 QOU Lean modules are never built by lake build` — they ARE built,
and have been since 2026-08-08. The reachability figure survives as a statement
about the **import closure** (measured 2026-09-13: 1451 of 2836 reachable from
`QOU.lean`, 48.8% outside — consistent with this bean's 47% and with
`lean-root-coverage-audit.py`'s 47.7%), but "outside the import closure" and
"not built" are different claims and this bean's title conflates them.

That conflation propagated. It was corrected in
`.github/workflows/lean-orphan-gate.yml` on 2026-08-15 (bean `qou-kljb`, verified
there by direct experiment on a throwaway package) and left standing in
`.github/workflows/lean-content-siblings.yml` — the very sentence this bean set
out to fix, re-broken in the fixing — until the PR carrying this append. It also
reached `scripts/lean-root-coverage-audit.py`'s docstring and
`scripts/lean-library-sweep.py`'s `--all` help text, both corrected in #7272.

### The caution in step 3 was sound, and the outcome resolved it

> Do **not** set `globs = ["QOU.+"]` as a first move: it converts a silent,
> survivable problem into a red default build, which is worse than the status quo
> until step 1 has been done.

`qou-rc7b` set the glob anyway, before step 1. On the evidence available at the
time that was the riskier branch, and this bean was right to say so — the hazard
simply did not materialise, because the modules were green. Recording it rather
than quietly dropping it: the reasoning was correct under uncertainty and the
measurement, arriving five weeks later, is what retires it.

### What genuinely remains, and it is NOT a compile backlog

Nothing runs any of this automatically. Every workflow in this repo is
`workflow_dispatch`-only (owner directive 2026-06-30, Actions billing), so
`lake build QOU` builds the whole tree and **nobody builds it** unless an agent
asks. That — not coverage, not breakage — is the live gap, and it is a standing
condition of the repo rather than a task this bean can close.

The narrower thing the orphan gate still protects, quoting its own header: an
unreferenced module is invisible to everything that *walks imports* — blueprint,
doc-gen, dependency analysis, import-cone builds rooted at `QOU`. It is not
invisible to the compiler. Do not quote this bean as evidence about build
coverage.

Status → completed; the remaining gap above is a repo condition, not this bean's
task.
