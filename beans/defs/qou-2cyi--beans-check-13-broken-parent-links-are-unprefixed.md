---
# qou-2cyi
title: 'beans check: 13 broken parent links are unprefixed bean IDs (0yqu, krvm)'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
    - beans
    - tracker-hygiene
created_at: 2026-08-16T12:55:03Z
updated_at: 2026-10-04T15:15:35Z
parent: qou-5vkl
---

## Symptom

`beans check` reports **13 broken links**, all of them `parent:`:

```
✗ qou-8v3k: broken link parent:0yqu      ✗ qou-rstq: broken link parent:0yqu
✗ qou-b7cy: broken link parent:0yqu      ✗ qou-clx8: broken link parent:0yqu
✗ qou-g2wr: broken link parent:0yqu      ✗ qou-r7ml: broken link parent:0yqu
✗ qou-fivt: broken link parent:0yqu      ✗ qou-trns: broken link parent:0yqu
✗ qou-rhyp: broken link parent:0yqu      ✗ qou-mlbg: broken link parent:0yqu
✗ qou-abel: broken link parent:0yqu      ✗ m015:     broken link parent:krvm
✗ rvnc:     broken link parent:krvm
```

11 point at `0yqu`, 2 at `krvm`.

## Diagnosis — the parents are NOT missing

Both targets exist:

- `qou-0yqu` — *"GAP: prove the 5₂ saddle sum rule Σ_j Re V_j = -3π²/2"*, in-progress
- `qou-krvm` — *"GAP: discharge optima_coincide's hypotheses for the actual m004/L6a4 polytopes"*, in-progress, high

The stored field is the **bare suffix**, not the full ID:

```
$ grep -n parent .beans/qou-8v3k--route-8-transport-the-sum-rule-to-the-cyclotomic.md
14:parent: 0yqu
$ grep -n parent .beans/m015--m015-5-2-angle-structure-polytope.md
12:parent: krvm
```

while the bean IDs on disk are `qou-0yqu` and `qou-krvm`.

**It is a resolution inconsistency inside the CLI, not data loss.** `beans show`
resolves a bare suffix happily — `beans show krvm` prints `qou-krvm` — but
`beans check` compares the link against the full ID and fails. So the two code
paths disagree about what a valid reference is.

Root cause of the mixed convention: some beans carry the `qou-` prefix and some
do not (`m015`, `rvnc`, `j5g5`, `slv0`, `00vb`, … are bare). A `parent:` written
when the prefix config differed, or written by hand, lands unprefixed.

## Why it is worth fixing rather than ignoring

The hierarchy is load-bearing for triage: these 13 are children of two live
in-progress GAP beans, and a broken parent link means they do not show up as
that GAP's children. The 5₂ sum-rule GAP `qou-0yqu` silently appears to have
**zero** children when it has eleven.

## Fix

Mechanical and safe — normalise the 13 `parent:` values to the full bean ID:

- [ ] `parent: 0yqu` → `parent: qou-0yqu` (11 files)
- [ ] `parent: krvm` → `parent: qou-krvm` (2 files)
- [ ] Re-run `beans check`; expect 0 issues.
- [ ] Decide whether to also normalise the **bare-ID beans themselves**
      (`m015`, `rvnc`, …) to the `qou-` prefix. Probably NOT worth it — renaming
      a bean ID breaks every existing reference to it, which is a much larger
      blast radius than the 13 links. Prefer leaving mixed IDs and making
      references full-form.
- [ ] Consider filing upstream (hmans/beans) that `check` should resolve links
      the same way `show` does, since that asymmetry is what produced this.

Pre-existing; untouched by PR #5221 (which installed the CLI). Found while
running `beans check` during PR #5230.

- **Round 92 (`litlfred/qou#8416`)**: Advanced in `feat/round92-jetmono-jetsign-kzratio-kzunit-kappacorr-43c1` (Commit 1 `b85484a2b9309c11a8832becee2e728a03219677`, Commit 2 `de3ca907bd3d3c7bb260ce5aa08259ade30c6cc9`, probe sha256 `7a5dfeb80aacf1b23a7e663221ecc9f97b20abf96256db6ae736e9dd7742c6f9`).
