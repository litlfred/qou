---
# qou-56qy
title: lean-direct exit 0 is a claim about the olean snapshot, not about the library source (305 modules stale)
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:21Z
updated_at: 2026-09-05T07:09:55Z
---

## The claim

`lean`-direct verification against the restored `lake-cache/qou-<slug>` olean
tree — the recipe AGENTS.md §"VERIFY a single file with lean-direct"
prescribes, and the one every recent Lean PR in this repo has used — checks a
file against a **snapshot of the library**, not against the library source. On
2026-09-05 the snapshot was **2026-08-30**, and **305 QOU modules had both a
prebuilt olean in it and a source change since**. For any of those, `exit 0`
is evidence about a six-day-old signature.

## The evidence (one confirmed false green, found by accident)

`SeminormalRep.wtrace` took `hq2 : q ^ 2 ≠ 1` in the snapshot. Commit
`794c34897d7` (2026-09-03) retyped it to `GenericParameter.NotRootOfUnity q`
and ported **seven library consumers**. `descartes-knot-eigenbasis.lean` is a
content-block sibling, was not ported, kept passing `q ^ 2 ≠ 1`, recorded
`exit 0` in #6684, and landed on `main` **red**:

    descartes-knot-eigenbasis.lean:398:53: error: Application type mismatch
    descartes-knot-eigenbasis.lean:413:60: error: Application type mismatch

Reproduced by rebuilding the 27-module dirty cone from source into a shadow
tree placed first on `LEAN_PATH` — ~90 s — and recompiling. Fixed in the same
PR as this bean.

Note what made it invisible: **the library half of the retype was done
correctly**. A signature change ported to every consumer *inside the package*
leaves content-block siblings behind, and those are exactly the files with no
`lake` target, no `.qa.json` Lean gate, and no CI (auto-triggers are disabled
repo-wide), so `lean`-direct against the cache is the only thing that looks at
them at all.

## The remedy, and what it does not do

[`scripts/lean-shadow-verify.sh`](../scripts/lean-shadow-verify.sh) copies the
olean tree into a shadow, recomputes which modules changed since the snapshot
was built, rebuilds only the dirty cone of the targets’ imports from source in
topological order, and runs `lean` against that. Mathlib is untouched; `lake`
is never invoked, so the restored cache cannot be evicted. On the case above:
27 modules, ~90 s.

It is a **verifier**, not a fix. It does not tell you which of the 263
content-block `.lean` files that import QOU are currently red — running it
across all of them is the open work.

## Open work

1. **Sweep the 263.** `find content -name "*.lean" -not -path "*/lean/QOU/*"
   -exec grep -l "^import QOU" {} \;`. One shadow can be reused across all of
   them (`SHADOW=…`), so the cost is dominated by the per-file `lean` run, not
   by rebuilds. Expect more than one red.
2. **Reseed the cache.** A fresh `lake-cache/qou-v4-24-0` seed collapses the
   dirty cone to zero and makes plain `lean`-direct honest again — until the
   next signature moves. Reseeding is the cheap half; the sweep is what finds
   what already broke.
3. **Decide whether AGENTS.md §"VERIFY a single file" should say this.** As
   written it presents `lean`-direct + restored cache as verification full
   stop, with no caveat that the cache ages. That wording is what I followed
   for seven merged PRs this session.

## What generalises

"Green against a snapshot" and "green against the source" are different
claims, and only one of them is what a PR body means by `lean`-direct exit 0.
Same shape as the `scriptCommitSha` / `scriptHash` distinction in AGENTS.md
§"Refresh stale sidecars + witnesses": a provenance stamp that has silently
stopped tracking the thing it names.
