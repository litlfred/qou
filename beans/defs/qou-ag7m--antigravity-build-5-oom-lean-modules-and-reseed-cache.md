---
# qou-ag7m
title: 'Antigravity: build the 5 Lean modules that run out of memory here, then reseed the lake cache'
status: todo
type: task
priority: normal
owner: Antigravity
parent: qou-c20n
created_at: 2026-11-21T05:45:00Z
updated_at: 2026-11-21T05:45:00Z
---

Owner instruction (2026-11-21 04:42 Copenhagen): put things that fail because of a
time/resource limitation in a bean for Antigravity.

## What failed, and why
A full `lake build QOU UGB Fred2005` at main `2d317625f88` (2026-11-20) rebuilt the
whole workspace (Mathlib from scratch; the old cache's traces no longer matched).
Five QOU modules were killed by the container's memory cgroup (exit 137, ~6 GB
limit), **each one even when built ALONE** with `lake build <Module>`. Measured peak
RSS ~5.9 GB before the kill. No source error in any of them.

| module | wall before kill (alone) |
|---|---|
| `QOU.BraidsAndKnots.YoungDiagramKernel` | 105 s |
| `QOU.Interactions.GramMatrixH3Symbolic` | 113 s |
| `QOU.Mathlib.SYTEnumerationN7` | 123 s |
| `QOU.Knot.GeneratedGluingHigh` | 204 s |
| `QOU.Machinery.HeckeH4Semisimple` | 744 s |

Their downstream cone (12 modules) was therefore skipped, including the library
root `QOU`: `QOU.Archimedean.spectrahedral_phase_collapse`,
`QOU.BraidKnot.WedderburnUnconditional`, `QOU.BraidsAndKnots.HookArmLeg`,
`QOU.BraidsAndKnots.PlancherelNormalisation`,
`QOU.BraidsAndKnots.SecondMomentKernelVanishes`,
`QOU.BraidsAndKnots.YoungDiagramKernelDimPos`,
`QOU.BraidsAndKnots.YoungDiagramKernelPincer`,
`QOU.BraidsAndKnots.YoungDiagramTailFirstInstance`,
`QOU.BraidsAndKnots.YoungDiagramTransposeBridge`,
`QOU.Interactions.GramQuotientDetD`, `QOU.Knot.GeneratedCertifiedHigh`, `QOU`.
These 17 have STALE oleans in the reseeded cache (old traces), so Lake rebuilds them
on restore. **So whether these 17 compile on current main is UNVERIFIED** — not shown
red, not shown green.

## Task (needs a machine with >= 12-16 GB RAM)
1. Restore `cat/folio-assistant-sci/lake-cache/qou-v4-24-0` (reseeded 2026-11-21,
   100 % trace coverage, Mathlib 3631 oleans), then
   `lake build QOU UGB Fred2005` — only the 17 above should build.
2. Report each module green/red. A red that is a real source error is a corpus
   defect: file a bean per module.
3. Reseed: `SEED_PAPER=1 CACHE_BRANCH=cat/folio-assistant-sci/lake-cache/qou-v4-24-0
   scripts/lean-olean-cache-seed.sh --push` (run `scripts/lean-content-mathlib-gap.sh
   --build` first).

Logs from the run that found this: `/tmp/lake-full.log`, `/tmp/lake-full2.log`,
`/tmp/lb-QOU.*.log` in the coordinator container (ephemeral).
