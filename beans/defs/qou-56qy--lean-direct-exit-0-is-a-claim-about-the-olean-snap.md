---
# qou-56qy
title: lean-direct exit 0 is a claim about the olean snapshot, not about the library source (305 modules stale)
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T07:09:21Z
updated_at: 2026-11-21T18:02:37Z
parent: qou-5vkl
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
    folio/quantum-observable-universe/lean/.lake/build/lib/lean    no QOU dir, 0

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


## 🛑 THE BIGGER DEFECT — a bare `lean` is a WEAKER check than `lake build` (2026-09-05)

Everything above concerns a green going **stale**. This one makes a green
**wrong from the start**, on any tree however fresh, and it invalidated all three
of my own scripts plus this repo's documented verification recipe.

`lean` invoked directly does **not** read the lakefile, so it does not apply its
`[leanOptions]`. `autoImplicit` defaults **true** in `lean` and is set **false**
in both the root and paper lakefiles. With it on, Lean silently auto-binds an
unbound identifier as an implicit argument instead of erroring.

Measured on `QOU/MassTheory/AtomWordShadow.lean` — same file, same `LEAN_PATH`,
one flag apart:

    lean                        ->  exit 0,  0 errors
    lean -DautoImplicit=false   ->  exit 1,  6 errors
    lake build (per-paper)      ->  exit 1, 20 errors

**That file was RED on `main`** and was called clean by: a bare `lean`-direct
run, the content sweep, and the library sweep — three independent "verifications"
that all shared one wrong assumption.

### How it was found, which is the part worth keeping

Not by any detector. By trying to **reseed the olean cache**: the seeder refused,
which forced a real per-paper `lake build`, which failed on a file I had
personally verified `exit 0` an hour earlier. **The contradiction between two
tools is what exposed it** — neither tool alone could have.

### Fixed

* `lean-shadow-verify.sh`, `lean-content-sweep.sh`, `lean-library-sweep.py` all
  pass `-DautoImplicit=false -s 65536` (the latter mirroring the paper
  lakefile's `moreLeanArgs`; one generated module overflows the default
  elaboration stack and aborts as a bare `exit 134` with no source error).
* `AGENTS.md` and `/prepare-merge` §4 corrected — the documented recipe was bare
  `lean`.
* `AtomWordShadow.lean` fixed: `fresh_freeIdx`, `fresh_atomIdx` and
  `orbitCount_freeShadow` never bound `A`. The sibling declaration
  `orbitCount_atomShadow` in the same file already had `{A : ℕ}`, so the fix is
  that binder on the other three.
* Re-run with the fix: library sweep **1 RED + 4 skipped**, matching lake
  exactly — then **73/73 ok** after the repair.

### RESEED: BLOCKED, and this is why

You cannot seed a cache from a tree that does not build. Beyond that, this
container cannot produce a valid seed at all:

    root .lake/packages/mathlib   6990 oleans,    0 traces   <- restored, untraced
    per-paper .lake/packages      3734 oleans, 3746 traces   <- genuinely built
    per-paper QOU build           2642 oleans, 2642 traces

`lean-olean-cache-seed.sh` collects from the **workspace root** and refuses at
`n_ml=0` (it seeds only *freshly rebuilt* mathlib oleans, tracked in
`/tmp/parbuild_built.txt`, which does not exist here). Its own message is right:
force-pushing a mathlib-less branch would make the next agent's restore count
~0 mathlib oleans and conclude Lean is unavailable. **Do not use
`SEED_ALLOW_NO_MATHLIB=1` from a container in this state.**

`SEED_PAPER=1` is the sanctioned narrow path and is viable *here* — the
per-paper tree is fully traced — but it reseeds only the paper oleans, so it
does not fix the untraced root mathlib that makes the closure non-empty in the
first place. Left undone deliberately; needs a container with a real
mathlib build, or the parallel-build producer that writes
`/tmp/parbuild_built.txt`.


## THE SIX CONTENT-BLOCK VACUITIES — found, fixed (2026-09-05)

Re-running the content sweep under `-DautoImplicit=false` turned **261 swept /
0 red** into **261 swept / 6 red**. All six are the same defect class, and none
of them broke a build — nothing compiles content-block `.lean` files — so they
are **semantic** defects: declarations that mean less than they say.

| file | symptom | cause |
|---|---|---|
| `knots-particles-confinement/stable-atom` | `Unknown identifier AtomKnot` | real `AtomKnot` is in `QOU/ParticleInteractions/AtomKnot.lean`, never imported |
| `knots-particles-confinement/unstable-atom` | same | same |
| `information-theory/hydrogen-partition-function` | `Unknown identifier q` | `boltzmann_ground_state (β hbar : ℝ)` never bound `q`; its own sibling at line 61 does |
| `quantum-observable-universes/qou-exists-axiom-1` | `unknown universe level v` ×2 | `.{u, v}` applied with neither level declared |
| `quantum-observable-universes/qou-exists-axiom-3` | same ×1 | same |
| `quantum-observable-universes/substrate-parameter-exists` | `v` ×2, then `WeightDecomposition` / `CategoricalReeb` unknown | `universe u` declared, `v` used by `[Category.{v} C]`; the two "unknown identifiers" are a cascade from the killed structure definitions |

### The evidence that these were real, not imposed strictness

Content blocks sit outside the Lake package, so no lakefile governs them and
`-DautoImplicit=false` could have been a scoping error on my part. It was not.
`#check` on the same structure, one import apart:

    fixed        StableAtom : (R : Type u_1) → [CommRing R] → Type u_1
    old regime   StableAtom : (R : Type u_1) → [CommRing R] → Type (max u_1 u_2)

That `u_2` is the auto-bound `AtomKnot`. The field documented *"The atom-knot"*
held an element of **an arbitrary type**. This is the vacuity class of
AGENTS.md §1a, invisible to every checker in the repo because bare `lean`
accepted it.

### The redeclaration question, answered by the file itself

I flagged `substrate-parameter-exists` as possibly needing a judgement about
redeclare-vs-import, since `WeightDecomposition` and `CategoricalReeb` also
exist in their own files. Its own docstring settles it — *"Mirror of
`weight-decomposition.lean`'s `WeightDecomposition`"* — so the local copies are
deliberate and the fix is the missing `universe v`, nothing structural.

### Fixes and verification

Two missing imports, one missing value binder, three missing universe
declarations. Verified 6/6 exit 0 under the corrected options, then the whole
261 re-swept.

## THE SWEEP WAS AIMED AT 28% OF ITS TARGET (2026-09-05)

Extending the sweeps to the sibling packages turned up something bigger than
the sibling packages.

`lean-content-sweep.sh` selected targets with `grep -l "^import QOU"`. That reads
as *"the content blocks that depend on the library"* and is the wrong population:

    content-block .lean files, total          938
    reached by the import filter              263
    never swept at all                        675

The 675 import only Mathlib. They are still content blocks, still compiled by
nothing else in the repo, and still able to carry the auto-implicit vacuity class
the sweep exists to catch. **So "261/261, 0 red" was a claim about 28% of the
population** — the same shape of false green this bean is about, in the tool
written to prevent it. Filter widened to every `.lean` under `content/` outside a
package `lean/` tree.

## UGB: 997 errors, one cause

`UGB/GrobnerShirshov/HeckeCompletion.lean` — `variable {n : ℕ}` at line 14981 is
scoped inside `namespace CornerCriterion`, whose `end` at 15078 closes it. Lines
15128-18779 (~3700) use `n` as `HeckeGen n`, `0 < n`, `heckeOrder n` and nothing
rebinds it. Under `autoImplicit = false` none of it elaborates: **997
`Unknown identifier n`**, capped at 100 by `maxErrors` until re-run with
`-DmaxErrors=100000`.

One `variable {n : ℕ}` after the `end`, matching the three namespaces above it
(11420, 13951, 14981): **997 -> 0**.

**UGB and Fred2005 both set `autoImplicit = false` in their own lakefiles**, so
this is their regime, not strictness imported from QOU. Checked before reporting.

Fred2005: 1 module, clean.

## Both sweeps now cover all three packages

* `lean-library-sweep.py` takes `--package` and otherwise **discovers** packages
  from `content/*/lean/lakefile.toml` + a top-level `<Lib>.lean` with a matching
  directory, so a fourth paper needs no edit. Per-library shadow subdirectory,
  since `LEAN_PATH` resolves a module from the first root holding that package
  dir and two libraries must not share one root.
* `lean-content-sweep.sh` sweeps all 938.

Sibling-package library result: **UGB 21 ok / 1 red (fixed), Fred2005 1 ok.**


## THE 938-FILE SWEEP: 14 red, 8 of them never previously reachable

First run of the widened sweep over the real population.

    swept   938
    RED      14   =  6 already fixed on #6811  +  8 NEW

The 8 new ones are all in the 675 the old `^import QOU` filter could not reach,
and all 8 are the same class — verified by running each under both regimes
rather than assumed:

    file                              autoImplicit=ON   autoImplicit=OFF
    frobenius-antipode-lean-stub          exit 0            exit 1
    ns-regular-qou                        exit 0            exit 1
    glossary-descent                      exit 0            exit 1
    markov-trace-recursive-reducer        exit 0            exit 1
    conj-atom-braid-exterior-algebra      exit 0            exit 1
    reeb-bundle                           exit 0            exit 1
    braiding-induced-ordering             exit 0            exit 1
    q-heat-equation                       exit 0            exit 1

### The two that show what the class actually costs

`glossary/glossary-descent.lean` and `fluid-dynamics/ns-regular-qou.lean` have
**no imports at all**, so `ℕ`, `ℝ` and `ℤ` were auto-bound as arbitrary types.

`ns-regular-qou` is self-refuting, and worth quoting because the author was
explicitly guarding against exactly this: *"We therefore carry the Euler
characteristic `chi` as data and encode NS-regularity as its genuine defining
property `chi = 0` (**not a `: True` placeholder**)."* The intent is right and
the guard failed one level down — `chi : ℤ` where `ℤ` is an auto-bound variable
is no more contentful than the `: True` it was written to avoid.

### Fixes

Four missing imports (`Mathlib.Data.Nat.Basic`, `Mathlib.Data.Real.Basic` ×2,
`Mathlib.Data.Int.Basic`), one missing `universe u`, two missing value binders
(`{α : Type*}`, `{Z N : ℕ}`), one `_q` → `q` typo where the parameter is `q`.

`reeb-bundle` needed a judgement rather than a typo fix, and its own note asked
for it: *"full Reeb-bundle formalization is pending the ExceptionalDivisor
structure (Ch 6 §2)"*. That structure **exists** —
`QOU/ArchimedeanUniverse.lean:104`, as `ExceptionalDivisor (M : Type*)`. So the
fix imports it, carries its parameter (`ReebBundle (M : Type*) (q : ℝ)`), and
names it fully qualified: the file is inside `namespace QOU` while the structure
is in `QOU.ArchimedeanUniverse`, so the bare name still does not resolve — the
import alone left it red, which the sweep caught.

All 8 verified exit 0.


## RESEED DONE 2026-09-06 — and the predecessor was never measured

`lake-cache/qou-v4-24-0` @ `1c496980587`. Seeded from a full
`lake build QOU UGB Fred2005` at the workspace root — **6484 jobs, 0 errors**,
which is also the strongest gate `main` has had this session (stronger than
either sweep).

    mathlib  3471 oleans / 3471 traces
    QOU      2702 / 2702
    UGB        28 / 28
    Fred2005    1 / 1
    32416 files, 20 parts (~1.8 GB), 100% trace coverage

**Verified by round-trip, not by the seeder saying so.** Parts streamed back
through `tar tzf -` (32416 in = 32416 out, exit 0); three oleans extracted from
the pushed branch hash byte-identical to local (`Mathlib/Tactic`,
`Mathlib/Data/Real/Basic`, `QOU/MassTheory/AtomWordShadow`). Rehearsed on
`lake-cache/qou-v4-24-0-test` first, kept as the record.

**Payoff, measured after:** dirty closure UGB 22 -> **0**, Fred2005 1 -> **0**,
QOU 33 remaining and all of those are commits that landed after the build began
(`main` moved 291 commits), **0 RED**.

### The documented seed path does not work — this is what does

`lean-olean-cache-seed.sh` takes mathlib only from `$BUILT_FILE`
(`/tmp/parbuild_built.txt`) and **nothing in this repo writes it**. Its own
comment records the producer/consumer mismatch (PR #4705). That, not a missing
build, is the `n_ml=0` refusal. Reconstructing the file from the build log
(3471 modules, all 3471 oleans verified present) is what unblocked it.

**And my earlier "sanctioned narrow path" was wrong in a way that mattered.**
`SEED_PAPER=1` adds `content/*/lean/.lake/build` — the paper *build output*, not
any mathlib — so `SEED_PAPER=1 CACHE_BRANCH=lake-cache/qou-v4-24-0 --push` on
its own force-pushes a **mathlib-less** branch over the working one. The
`n_ml` guard is the only thing between that and production. It was right to
refuse and I was wrong to call it the path.

### 🛑 The failure of discipline, recorded because it is mine

**I overwrote the previous branch without measuring it.** Head `a2bf415e7a7`
was force-pushed away and is now unreachable (GitHub refuses arbitrary-sha
fetches). I verified what went in and what comes back out — and never what was
displaced, then reasoned about it anyway.

* **Withdrawn:** "the old seed was built lean-direct, so it carried the trace
  gap." Unsupported. AGENTS.md records the 2026-08-31 seed at 6170/6172 oleans,
  100% paired traces, which contradicts it, and I can no longer check.
* My first attempt to repair this measured `15f6f00e89c` — an **intermediate
  commit of my own push**. I nearly published a measurement of my own partial
  seed as the baseline. The true displaced head is the left-hand sha on the
  `(forced update)` line of the push log; read that, not an arbitrary earlier
  commit.
* **Next reseed: measure the outgoing branch first** and record the counts.

The new branch is verified good on its own terms; the gap is that no
before/after comparison exists.

--------

**2026-09-14, RE-MEASURED on `main` `d534ac2a8e`: the drift has MORE THAN
DOUBLED, and the number that governs whether a green means anything was never
recorded.**

This bean's headline is "305 modules stale", measured 2026-09-05. Nine days
later, using **the sweep's own definition** rather than a second spelling of the
question (`scripts/lean-library-sweep.py --report`, added in the same PR so this
is one command rather than an import of the module's internals):

```
modules in graph                              2872
never built (no olean at all)                 123
changed (source newer than its own olean)     683   <- the bean's 305
standard-dirty (snapshot cannot vouch)        683
DIRTY CLOSURE (changed + their importers)     1252  (43.6% of the library)
clean in snapshot                             1620
```

**305 -> 683.** The drift compounds; it does not drain. And **1252** is the
figure that actually decides whether a `lean`-direct exit 0 is evidence about
`main` — a module is untrustworthy if anything it imports moved, not only if it
moved itself — and this bean never carried it.

**Open item 1 is closed but does NOT generalise.** `cscb` / `qou-e7xv` swept the
content-block siblings to 938/938 green. That is the *sibling* population. The
*library* population above is a different set and is 43.6 % dirty.

**Two packages neither sweep covers, quantified:** UGB is **23 of 29 never
built** (79.3 %), Fred2005 has **no olean tree at all**. AGENTS.md notes the
scripts are QOU-only; these are the numbers behind that note.

**The failure mode recurred, and was found the same way it was found the first
time — by accident.** Building #7337 I hit
`QOU.MathlibExt.DisjointBlockTraceLaw`: cached olean 2026-09-07, source
2026-09-13, `unknown identifier 'sandwich'` (defined at line 548, added after
the snapshot). Red against the cache, clean against source. The whole live
bond-product / colimit cone is dirty — `OcneanuTrace`, `MarkovBondFactor`,
`PureBondChainProduct`, `InteriorMarkovOfBraidedTower`,
`ProductionChainBondProduct`, `SchurWeyl.MarkovTraceInstance` — and #7274 is
committing into it now.

**RETRACTED before it was written anywhere durable: a "239 re-restorable / 77
irreducible" split.** The reasoning was that 2248 of 2753 QOU oleans here carry
mtime **2026-08-29** while `refs/heads/lake-cache/qou-v4-24-0` is
`a792c46d01b6e350` — the head AGENTS.md records as a **2026-09-06** reseed — so
most of the drift would vanish on a re-restore. **`tar` preserves mtimes**, so a
seed built incrementally on top of a restore carries old dates too, and the two
cases are indistinguishable from here. Nor is this tree the seed as-published:
`mathlib` 3407 against the recorded 3480, QOU 2751 against 2702 — a restore plus
local rebuilds.

Settling it costs a ~1.7 GiB fetch and this container has **642 MB free**
(`df` reads 252 G at 99 %; the real limit is the ~38 G per-session quota, and
deleting a 2.4 G *hardlinked* shadow returned 12 MB). So **remedy #2 (reseed)
stays open and, separately, cannot be executed from a container in this state** —
worth knowing before someone plans it as an idle-pass job.

**Open work, updated.**
1. ~~Sweep the 263 content-block siblings~~ — done, 938/938 green (`cscb`).
2. **Reseed** — still open, still unmeasured, and needs a container with room.
3. **Decide the AGENTS.md wording** — still open. §"VERIFY a single file with
   lean-direct" now carries a `qou-56qy` caveat block, but does not give the
   reader a way to find out whether *their* file is in the dirty 43.6 %.
   `--report --only <prefix>` is that way; whether AGENTS.md should say so is an
   owner call, not taken here.

## Round 70 Formalization Progress (PR #8297)
- Formalized `QOU.MassTheory.orbitCount_freeShadow_sub_atomShadow` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/tl_uniqueness_threerow_factorisation_shadow_gluon_probe.py`, `scriptHash: 3ae4cba85e90`, Commit 1 `1f88e71305a6e71d41389edf2285daae1528f7d8`, Commit 2 / Witness `cfb7f3d64020483db10298c3ccdd51ae1d1bd7d8`, PR `litlfred/qou#8297`).

2026-11-21 (lean-build-red drain, issue #8817): a lean-direct-cone --all sweep from source on main 42ca186dad found only the QOU.lean root red (fixed in PR #8878). Reseed (remedy 2) and the AGENTS.md wording are still open.

2026-11-21: remedy 2 (reseed) done. Cache head is 7c61a1ba876: a fresh incremental lake build of main 9428c3511c, every olean traced, and a clean restore rebuilds 0 modules. AGENTS.md records it on PR #8885. Item 3, the AGENTS wording on finding your dirty files, is still an owner call.

2026-11-21: item 3 (AGENTS.md stale-olean check note) merged via PR #8909 on owner approval. Reseed done earlier (7c61a1ba876). Closing.
