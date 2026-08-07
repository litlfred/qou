---
# qou-orph
title: 'INFRA (measured): 761 of 1598 QOU Lean modules are never built by `lake build`'
status: todo
type: task
priority: high
tags:
    - lean
    - infra
    - lakefile
    - ci
created_at: 2026-08-07T23:50:00Z
updated_at: 2026-08-07T23:50:00Z
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
