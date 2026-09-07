# The Mathlib cache gap is 3 targets / 7 modules, not 4 — and it is closed

**2026-09-07.** Beans `qou-9yt9`, `qou-56qy`.

## What was recorded

`AGENTS.md` documents that the restored `lake-cache/qou-v4-24-0` olean tree is
short some Mathlib modules, that **8 content blocks** therefore cannot be
verified in a stock container, and — correctly — that this is a cache defect
rather than a corpus one:

> do NOT "fix" those blocks: their imports are fine, the cache is short. Fix at
> the cache branch (reseed those four cones) or give the gate an expected-RED
> list, so it distinguishes *cannot verify* from *fails*.

It names four absent modules: `Topology.FiberBundle.Basic`,
`RingTheory.HopfAlgebra.Basic`, `Analysis.Complex.UpperHalfPlane.Basic`,
`Analysis.Real.Pi.Bounds`.

## Measured

**`Analysis.Real.Pi.Bounds` is present.** So the gap is **three** targets, whose
transitive cones are **seven** modules:

| target | cone |
|---|---|
| `RingTheory.HopfAlgebra.Basic` | + `Bialgebra.Basic`, `Coalgebra.Basic`, `LinearAlgebra.TensorProduct.Finiteness` |
| `Topology.FiberBundle.Basic` | + `FiberBundle.Trivialization` |
| `Analysis.Complex.UpperHalfPlane.Basic` | (leaf) |

All seven build from source against the pinned Mathlib with `lean`-direct —
no `lake`, no network, a few minutes total. Packaged: **2.3 MB**.

## Closed

Seeded to the addon orphan branch
**`lake-cache/qou-v4-24-0-mathlib-gap-modules`**, restored by
[`scripts/lean-restore-gap-oleans.sh`](../../scripts/lean-restore-gap-oleans.sh).

Verified end to end: with the seven restored into the real olean dir, the blocks
compile with **plain `lean`-direct and no shadow overlay**.

Seven content blocks import these modules and were unverifiable without them.
All seven are now `lean -DautoImplicit=false -s 65536` **exit 0**:

```
algebraic-geometric-dilog-equivalence   categorical-transfer-matrix
gb-depth-period-correspondence          hq-bi-filtration
reeb-bundle                             vertex-operator
tannaka-krein-reconstruction
```

This confirms the recorded diagnosis exactly: **the blocks were never broken.**

## 🛑 Seven, not eight — and the difference is not established here

`AGENTS.md`'s **8** came from a full content sweep. My **7** comes from grepping
`import` lines for the three targets. Those are different populations: a block
blocked *transitively*, through a `QOU` module that imports one of these, would
not appear in my grep.

So this does **not** establish that the 8th is spurious. It establishes that
seven blocks are closed and one is unaccounted for. Identifying it needs the
full content sweep (~55 min), which was not run. Do not read "7" as a correction
of "8".

## Restoring is not a Lake restore

The seven are plain oleans with no `.trace` sidecars. Lake would treat them as
stale and evict them along with the rest of the restored cache (`AGENTS.md`,
bean `02kc`). Untar and use `lean`-direct; never `lake build` afterwards. The
script says so and traps its temp file — a leaked 2.4 GB scratch tarball is how
this container has run out of disk before.

## Two traps found building it, both mine

1. **An EMPTY shadow first on `LEAN_PATH` makes `lean -o` report every
   dependency as missing** even when it is present in the real tree. The shadow
   must be a complete hardlink overlay, not an empty directory. Two builds
   failed this way before I noticed the reported paths were all shadow paths.
2. **My cone-depth script said 4; the first build reported a 5th missing module**
   (`LinearAlgebra.DFinsupp`). That 5th was trap 1, not a real gap — `DFinsupp`
   compiles standalone. I came within one commit of recording a deeper cache gap
   than exists.
