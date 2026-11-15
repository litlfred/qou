# The gap cache branch is seeded 7 → 86; the library root is now one fetch away

*2026-09-11 — beans `qou-g5sp`, `qou-ed8a`. Branch commit `d7e3ae8c662`.*

## What landed

`lake-cache/qou-v4-24-0-mathlib-gap-modules` carried **7** Mathlib oleans. It now
carries **86**: the original seven plus the **79-module transitive cone** of
`Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree`.

**22 MB gzipped, 68.4 MB raw.** Fast-forward, not a force-push: all 7 originals
are byte-identical and the previous tarball remains at the parent commit
`100bdfde4bf`.

| area | modules |
|---|---|
| Algebra | 30 |
| CategoryTheory | 26 |
| AlgebraicTopology | 13 |
| Order | 7 |
| RepresentationTheory | 3 |
| RingTheory | 3 |
| Topology | 2 |
| Analysis / Data / LinearAlgebra | 1 each |

## Why it matters

The seven originals unblock seven content blocks. They do **not** cover
`LowDegree`, which `QOU.Eightfold.ObstructionH2Mathlib` needs — and **the library
root `QOU` is SKIPPED behind that module**, so the single module `lake build QOU`
gates on could not be checked in a stock container at all.

That was attributed to a container resource limit (bean `qou-ed8a`, repeated in a
sibling's merged audit). **It is not one.** It is 79 missing oleans: **188 s** to
build from source, **22 MB** to fetch. This branch converts the former into the
latter for every future agent.

## How the 86 were identified — and it is not by mtime

An `mtime` discriminator fails here, and the reason is recorded elsewhere in this
corpus at some cost: `shutil.copy2` preserves mtime, and so does a tar restore.

The sound discriminator is structural. `lake-cache/qou-v4-24-0` is **100 %
trace-paired**, while *both* this branch's restore and a `lean`-direct build write
**plain oleans with no `.trace`**. So an olean in the paper mathlib tree with no
paired trace is exactly one the main cache did not provide.

That found **87**. One of them — `Mathlib/Data/Multiset/ZeroCons.olean`, mtime
**2026-08-28**, eleven days before this cone was built (04:04–04:07 on 09-08) — is
an untraced leftover from an earlier session, unrelated to this cone. It is
**deliberately excluded**, so the 86 shipped are exactly the 7 + the 79-module
cone and the artifact matches its own description. The builder's reported "79" was
correct; the 87 was not a contradiction of it.

## Verify with the SWEEP, not bare `lean`-direct

Two hand-verification attempts failed here, and **neither was evidence about the
cache** — both were about the command:

1. **`lean-direct-env.sh` pins the ROOT tree**, which holds 1298 oleans against
   the paper tree's 3563. It reported a missing *Mathlib* olean
   (`CategoryTheory.Limits.Preserves.Shapes.Zero`) that the paper tree has. This
   is the ROOT-vs-PAPER trap the restore script's own header documents.
2. **Re-pinned to the paper tree**, it reported a missing **QOU** olean
   (`QOU.Eightfold.ObstructionH2`) — a sibling *library* module that the sweep
   builds into its shadow and a bare `lean` never does.

The second failure is the informative one: the error moved from a Mathlib object
to a QOU object, which is exactly what "the Mathlib gap is satisfied" looks like.

The gate is:

```bash
scripts/lean-library-sweep.py --all --only-exact QOU
```

`--all` is load-bearing — `--only-exact` alone selects within the *dirty* closure,
and a module that is not dirty compiles nothing and exits 0, which is
indistinguishable from a pass unless you check the population.

## Still not a Lake restore

No `.trace` sidecars, so `lake build` treats these as stale and evicts them along
with the rest of the restored cache (bean `02kc`). Untar and use `lean`-direct or
the sweep; never `lake build` afterwards.
