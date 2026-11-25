# qou-v4-24-0-lean-direct-refresh — addon over `qou-v4-24-0`

Reseeded 2026-11-25 from qou `74a6167bd` (branch
`claude/lean-cache-consolidate-2026-11-24` = origin/main `327f01818` merged),
parent commit `4b44063549a` (the 2026-11-19 seed from `c4a0c309a`).
**Lean-direct output: plain oleans, NO fresh `.trace`.** Restore with `tar`
(`scripts/lean-restore-refresh-oleans.sh`, called by
`scripts/lean-cache-restore.sh`), verify with `lean`-direct /
`scripts/lean-direct-cone.sh`. **Never `lake build` over it.**

## What it holds (repo-relative `folio/…` paths)

3961 `.olean`, each with a `.srcsha` stamp equal to sha256 of its current
source at `74a6167bd` (checked one by one before packing), plus 246 `.ilean`
written alongside them:

- 3913 modules of the `qou` package graph — the WHOLE current graph, not a
  diff: QOU 2126 (including the root `QOU.olean`, green at this commit) and the
  top-level namespace libraries that 559a7210b introduced: BraidKnotOctonion
  834, HeckeTemperleyLieb 496, MathlibExt 302, QCalculus 92, TwistedFrobeniusHopf
  25, ToricConicOpt 20, CompactQuantumMetrics 18.  Earlier seeds had no
  HeckeTemperleyLieb oleans, so any file importing it (e.g.
  QOU/MassTheory/BorromeanWordForcing.lean) failed with "unknown module prefix".
- 45 UGB and 3 Fred2005 modules, rebuilt lean-direct where the base seed's
  olean did not match its current source.

Not included: ~3150 orphan oleans left in a working tree for module paths that
no longer exist after the chapter consolidation, and every Lake `.trace` /
`.hash` (stale for rebuilt modules).

## How it was built

`scripts/lean-direct-cone.sh --all -k -j2` over the base seed + gap addon
(`mathlib-gap-modules` @ `91643168ca5`), then `-j1` for
HeckeTemperleyLieb.HeckeH4Semisimple (OOM-killed at -j2: 8.3 GB RSS) and the
root `QOU`, then an incremental top-up after merging main (6 modules).
3908 + 6 modules, 0 errors.  Flags: `-DautoImplicit=false -s 65536`.

## Restore (after the base seed and the gap addon)

```sh
scripts/lean-cache-restore.sh     # base + gap + this addon
```
