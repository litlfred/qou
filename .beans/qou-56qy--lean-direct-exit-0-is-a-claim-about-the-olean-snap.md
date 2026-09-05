---
# qou-56qy
title: lean-direct exit 0 is a claim about the olean snapshot, not about the library source (305 modules stale)
status: todo
type: task
priority: high
created_at: 2026-09-05T07:09:21Z
updated_at: 2026-09-05T08:40:24Z
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

## SWEEP RESULT 2026-09-05 — 261 content-block files, ZERO red

Ran `scripts/lean-content-sweep.sh` over every content-block `.lean` sibling
carrying `import QOU`, against a shadow tree with the whole dirty library cone
rebuilt from source.

    library cone rebuilt from source   129 / 129  clean
    content-block targets swept        261
    genuinely red                        0

The single red the first run reported was the sweep's own two bugs, not a
finding: the target filter pruned a package's library TREE but not its ROOT
module, and `LEAN_PATH` carried only the qou package, so `QOU.lean`'s
`import UGB` failed as `unknown module prefix`. Both fixed; `QOU.lean` compiles
clean. `unknown module prefix` appears in exactly one of the 262 logs, so the
path gap could not have affected any other target — no full re-run needed.

## What this changes about the bean

**The prior was wrong, and in the reassuring direction.** I expected more than
one red, on the reasoning that `descartes-knot-eigenbasis.lean` had no special
property. The measurement says the opposite: it was the only one. So the
`NotRootOfUnity` retype was the sole recent library signature change whose
content-block consumers were missed, and the exposure this bean describes is
real but has been realised **once**, not systematically.

That is a statement about **today's tree**, not about the mechanism. Nothing
prevents the next signature change from doing the same thing — the structural
gap (no lake target, no `.qa.json` Lean criterion, no CI on 261 files) is
untouched by this result.

## What is still open

1. **Reseed `lake-cache/qou-v4-24-0`.** The snapshot is ~6 days behind; 129
   modules had to be rebuilt to make one sweep honest. A reseed collapses that
   to zero until the next drift.
2. **Sibling packages are not covered.** The shadow rebuild walks the qou
   package only. `QOU.lean`'s UGB import resolved against UGB's prebuilt
   oleans, so that one green is snapshot-conditional.
3. **Wire the sweep to something.** A verifier nobody runs is what produced
   this bean. Cheapest honest option is a documented pre-merge step for PRs
   touching `content/**/*.lean`; CI is unavailable (auto-triggers disabled
   repo-wide, owner directive 2026-06-30).
4. **AGENTS.md §"VERIFY a single file with lean-direct"** still presents
   `lean`-direct against the restored cache as verification with no caveat
   that the cache ages. That wording is what I followed for seven merged PRs.
   Changing it is an owner call, not mine.


## LIBRARY SWEEP 2026-09-05 — 74 stale modules, ZERO red

`scripts/lean-library-sweep.py` closes the gap the content sweep left. It
computes the **dirty closure** over the whole library — a module that changed,
has no olean at all, or transitively imports one that did — and rebuilds it from
source in topological order, continuing past a failure so one break cannot mask
the rest.

    library modules        2643
      source-changed         24
      never built (new)       6
      DIRTY CLOSURE          74     rebuilt from source
      snapshot-current     2569
    result: 74 ok, 0 RED, 0 skipped, 122 s

**The closure is the right population, and it is what a source-change count
misses.** Six of the 74 have no olean at all: a NEW file inherits its
dependencies staleness without ever appearing in a drift count keyed on changed
sources. That is exactly the shape of the `FiveTwoCuspShapeBarParity` case.

## Correction to my own 305 figure

This bean opens by saying **305** QOU modules have both a prebuilt olean and a
source change since the snapshot. That number came from the coarse method this
bean is itself about: one snapshot date (`--since` the newest olean in a
mixed-age tree) instead of per-module comparison. Measured per module on the
same tree: **24 source-changed, 6 never built, 74 in the dirty closure.**

Do not quote 305. It is not a stale figure, it is a wrong one, produced by the
method the script was fixed to stop using.

## The dirty closure is CONTAINER-dependent — so is any "zero red"

The sibling instance recorded above does not reproduce here:

    BarParityZeta4Swap.olean   this container  2026-08-24
    BarParityZeta4Swap.lean    last commit     2026-08-19   (olean NEWER)

so it is not dirty on this tree, while on theirs the olean was 20 days older
than the source. Both readings are correct about their own container. The
consequence is that **a sweep is only as complete as the staleness of the tree
it runs against**, and "zero red" is a claim about one snapshot at one moment,
not about the corpus. A container restored from an older cache has a larger
closure and needs its own run.

## A false alarm worth recording, because the shape recurs

The SessionStart background `lake build` reported **21 errors** and
`status: failed`. Twenty of them were in
`QOU/MassTheory/AtomWordShadow.lean` — a real-looking find that is **not a live
defect**: the build started 08:13:10, the fix `400db05b738` landed 08:14, and
compiling that file at HEAD gives exit 0. The build had read the pre-fix
content.

Two things to carry:

* **A failing build log is a claim about the tree at the moment it ran.** Same
  class as the olean snapshot, one level up — and it is the *reason* the raw
  `lake` log is worth checking against HEAD before reporting anything from it.
* **Lakes error format is `error: <file>:<line>:<col>: <msg>`**, not
  `<file>:<line>:<col>: error:`. A grep for `: error:` over a `lake` log returns
  **0** on a log holding 20 real errors. (The sweep scripts are unaffected —
  they invoke `lean` directly, which uses the second form, and they decide red
  by exit code rather than by grep.)
