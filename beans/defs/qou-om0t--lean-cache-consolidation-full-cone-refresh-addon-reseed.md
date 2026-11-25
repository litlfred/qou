---
# qou-om0t
title: 'Lean cache consolidation: full lean-direct cone green, refresh addon reseeded, gap addon extended (PRs #9398 #9412 #9413)'
status: completed
type: task
priority: normal
created_at: 2026-11-25T11:02:54Z
updated_at: 2026-11-25T11:02:54Z
---

Logged after the fact: this work ran without a bean (session 2026-11-24/25).
Mechanical cache infrastructure only; no mathematics changed.

## Merged
- #9398 -> 1e75378ad38: lean-cache-restore.sh layers the gap and refresh
  addons over the base seed; lean-verifier memory traps.
- #9413 (folded into #9398): the gap restore reads mathlib-gap-oleans.tgz
  plus mathlib-gap-oleans-NN.tgz, original first. The next gap addition must
  go in mathlib-gap-oleans-02.tgz; the original is 80.6 MB.
- #9412 -> 4c79c33026f: lean-library-sweep --report decides freshness by the
  .srcsha stamp when present.

## Cache branches (child commits, no force-push)
- gap: fe45a7c5b63 -> fd6c1e47a21 (+19) -> 91643168ca5 (+11; 335 entries).
- refresh: 4b44063549a -> bedc1a000a1. 3961 oleans, each stamped against its
  source at 74a6167bd: the whole qou graph (3913) + UGB 45 + Fred2005 3.

## Measured
- Full cone at 74a6167bd (main 327f01818 merged): 3913/3913 green.
  HeckeTemperleyLieb.HeckeH4Semisimple was OOM-killed at -j2 (8.3 GB RSS,
  15 GB cgroup) and is ok alone at -j1 in 847 s.
- A fresh restore in a clean worktree: lean-direct-cone --all reports
  3913 up to date in 1 s; BorromeanWordForcing.lean is exit 0.

## Left open
- UGB.GrobnerShirshov.HeckeGSThree is not in the refresh addon. It is a leaf
  that nothing imports and builds in 2.7 s.
- The base seed's Lake-traced reseed: see qou-ag7m.
