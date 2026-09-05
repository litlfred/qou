---
# qou-56qy
title: lean-direct exit 0 is a claim about the olean snapshot, not about the library source (305 modules stale)
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:21Z
updated_at: 2026-09-05T08:02:44Z
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


## The script could not run at all on a root-restored tree (2026-09-05)

`OLEANS` was hardcoded to `\$PKG/.lake/build/lib/lean`, the **per-paper** path.
The `lake-cache/qou-<slug>` restore that AGENTS.md prescribes seeds the **root**
workspace. Measured on a correctly-restored container this session:

    /home/user/qou/.lake/build/lib/lean/QOU                          2442 oleans
    content/quantum-observable-universe/lean/.lake/build/lib/lean    no QOU dir, 0

So the guard `[ -d "\$OLEANS/QOU" ]` fired and the script exited 2 on exactly the
tree it exists to verify against. Fixed: it now probes the per-paper path, then
the root, honours an `OLEANS=` override, prints which tree it chose, and lists
both paths in the failure message instead of one.

Worth noting the shape, because it is the same one this bean is about. Both
paths are real — a per-paper `lake build` genuinely writes to the first — so the
hardcode is not a typo but a **build route silently assumed**. I made the
identical assumption by hand an hour earlier: I checked the per-paper `.lake`,
found it empty, and concluded a restore that had in fact written 6172 oleans had
delivered nothing.

## A second stale-olean instance, caught before publication

`QOU/QBeta/FiveTwoCuspShapeBarParity.lean` (PR #6694) recorded `lean`-direct
exit 0 against the restored cache. Its one QOU dependency measured:

    BarParityZeta4Swap.olean   mtime  2026-08-08
    BarParityZeta4Swap.lean    commit 2026-08-28    (20 days newer)

Same class as `descartesWtrace`, and caught only because `d3b96a29f0` landed on
main while the PR was open. Re-verified by rebuilding that dependency from
current source into a shadow placed first on `LEAN_PATH` (exit 0) and
recompiling against it (exit 0, sorry-free, 19 declarations). The mathematics
did not move; the evidence did.

This is one more argument for the sweep in "Open work" item 1: the file was
**not** in the 305, because it is new. A new file importing a stale module
inherits the staleness without appearing in any drift count keyed on changed
sources.
