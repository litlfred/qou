---
# qou-kljb
title: 795 QOU library modules are never built — lake build QOU cannot see them (270 load-bearing)
status: completed
type: task
priority: high
created_at: 2026-08-09T02:12:05Z
updated_at: 2026-08-15T21:40:39Z
---

Surfaced while verifying PR #4824's §1 consolidation claim with the three-way
per-file drop check sibling #4840 proposed. PR #3793 had recorded, in a comment
on `TorusKnotMass.lean`, that a fabricated
`noncomputable instance : TorusKnotMass := ⟨0, rfl⟩` did not typecheck, and
that the resulting non-compiling file "escaped CI only because it is orphaned
from the `QOU` umbrella". That comment was dropped when the instance-removal
reached main by a different route.

**Both halves of #3793's claim are now confirmed.**

## 1. The typecheck claim — verified

At #3793's base (`b759f24f`) the class had **9 explicit fields** including
`factors_distinct : gauge_mass_factor ≠ scalar_mass_factor`. `⟨0, rfl⟩`
supplies 2 of 9, and `gauge_mass_factor = 0` forces
`factors_distinct : (0:ℝ) ≠ 0`, unprovable. It could not have elaborated.

## 2. The orphan/CI claim — verified by experiment

Import-closure walk from `content/quantum-observable-universe/lean/QOU.lean`:

| | count |
|---|---|
| library modules under `lean/QOU/` | 1776 |
| reachable from `QOU.lean` | 981 |
| **unreachable** | **795 (44%)** |

`content/quantum-observable-universe/lean/lakefile.toml` declares

```toml
[[lean_lib]]
name = "QOU"
srcDir = "."
```

with **no `globs` key**. Lake's default is then `globs = #[.one "QOU"]` — only
the root module and its transitive imports are built.

Confirmed by direct experiment rather than inference (throwaway package, root
`Lib.lean` + unimported `Lib/Orphan.lean`, same toolchain `v4.24.0`):

| lakefile | result |
|---|---|
| no `globs` | builds `Lib.olean` only — **`Lib/Orphan.olean` NOT built** |
| `globs = ["Lib", "Lib.+"]` | builds both |

So `lake build QOU` never elaborates them. A module in that set can be
syntactically broken, carry an uncited `sorry`, or fail to typecheck, and no
build will say so.

### Correction — how this bean first read, and why

The first version of this bean **denied** the orphan/CI claim. The reasoning
was: against the restored `lake-cache/qou-v4-24-0` tree, orphaned modules carry
`.olean` artifacts at 56% (440/785, as counted that morning), statistically indistinguishable from
reachable modules at 57% (502/874, as counted that morning), and `TorusKnotMass.olean` is present — so
orphan status appeared not to predict builtness.

That inference was wrong. The oleans are **stale artifacts** left in the build
directory from when those modules were imported or built explicitly; nothing
prunes them, and a tarball snapshot of a long-lived build dir preserves them.
Presence of an olean is evidence that a module was built *at some point*, not
that the current `lake build QOU` builds it. The experiment above tests the
mechanism directly and settles it.

Lesson worth keeping: an artifact-presence survey cannot answer a
"does-the-build-do-X" question. Test the build.

## Why this matters

For these modules (795 as of 2026-08-09) there is currently **no** automated check of any kind:

- `lake build QOU` does not build them (above);
- a library `.lean` with no `.ts`/`.md` sibling has no `.qa.json` sidecar and
  is not covered by `lean-content-siblings.yml` (AGENTS.md);
- CI auto-triggers are disabled repo-wide (`build.yml` is
  `workflow_dispatch`-only).

## Triage (step 1 — DONE 2026-08-09)

Counts re-measured against a newer `main`; the population grew 785 → **795**
as the corpus moved, which is itself the point (orphans accrue silently).

| class | count | meaning |
|---|---|---|
| **load-bearing** | **270** | a content block's `lean.ref` names this module |
| interior | 190 | reachable only from another orphan |
| dead-root candidates | 347 | no `lean.ref`, no orphan importer |

**270 load-bearing is the headline.** Those are blocks whose manifest claims a
Lean formalisation that no build has ever elaborated.

### Do they actually compile? Sampled 22 by `lean`-direct

| sample | n | result |
|---|---|---|
| load-bearing | 12 | 11 pass, 1 dep-gap |
| dead-root candidates | 10 | 10 pass |

**Zero real source errors.** The one non-pass —
`QOU.BraidKnot.symbolic_character_table` — is `object file ... does not exist`
for `QOU.BraidKnot.SytSmallShapeCounts`, i.e. it imports another orphan that
has no olean *because nothing builds it*. Not a source defect; the orphan gap
propagating into its own verification.

### Sorry hygiene holds

33 real `sorry`s across all 795 files (26 files), and **every one carries a
`-- Ref:` within 8 lines — 0 uncited**. (A first pass reported 358/323; that
regex was matching the *phrase* "sorry-free" in prose. Numbers above are with
comments stripped.)

### Revised risk — I over-cautioned

The earlier "expect breakage, could be very red" warning is **not supported**.
The sources look healthy. Two honest caveats before anyone treats that as
"safe":

1. **22 of 795 is ~2.8%.** Zero failures in 22 bounds the failure rate at
   roughly **13%** (rule of three, 95%) — so up to ~100 files could still fail.
   "Most compile" is supported; "all compile" is not.
2. **Per-file `lean`-direct ≠ a whole-library build.** Each file was checked
   alone. Compiling all 795 *into one library* can surface conflicts that
   per-file checking structurally cannot — duplicate declaration names,
   clashing instances, universe issues across modules that never met before.
   This is the residual unknown, and it is the reason to stage the work.

## Next steps

1. ~~Triage~~ — done, above.
2. **Wire up in tranches, load-bearing first.** The 270 with a `lean.ref` are
   the ones where the corpus asserts something unchecked, so they buy the most
   per unit of risk. Add imports to `QOU.lean` (or `globs = ["QOU", "QOU.+"]`)
   a directory at a time, building between tranches so a cross-module clash is
   attributable.
3. **Triage the 347 dead-roots separately** — they sample clean, so they are
   *unwired*, not rotten. Decide per subtree whether to wire or delete;
   deleting healthy proved content would be the worse error.
4. ~~Cheap guard~~ — `scripts/lean-orphan-modules.sh` (read-only, exits
   non-zero when orphans exist, so it can gate once the count is driven down).



## Claimed 2026-08-15 — branch `claude/mtcx-7c-verify-close-2026-08-15` (session qou-xz6t)

Taking step 2 ("which orphans are actually broken?"). **Not** touching the lakefile `globs` yet: this sandbox cannot run `lake build` at all (`.lake/packages/mathlib` was restored from `lake-cache/qou-v4-24-0` with no `.git`, so any dep-resolving lake call wipes 6990 oleans), so a `globs` change here would be unverifiable — exactly the kind of claim this bean's own §2 correction warns against. Surveying with `lean-direct-cone.sh --all -k`, which bypasses Lake entirely, to produce the per-module green/red list that a `globs` flip needs as its prerequisite.


## FINDING 2026-08-15 — the premise is already fixed; the 44 % figure is stale

**`lake build` DOES build these modules.** The lakefile now carries

```toml
[[lean_lib]]
name = "QOU"
srcDir = "."
globs = ["QOU", "QOU.+"]     # "WIDEN THE BUILD TO THE WHOLE TREE (bean qou-rc7b)"
```

`QOU.+` is `Glob.andSubmodules` — the module and **all** its submodules — so every `.lean` under `lean/QOU/` is in the library target whether or not `QOU.lean` imports it. This bean's §2 conclusion ("`lake build QOU` never elaborates them") was true when written on 2026-08-09 and has since been fixed by `qou-rc7b`; the bean was never closed.

**Verified by direct experiment, not inference** — the same throwaway-package method this bean's §2 used, re-run *with* `globs` set (toolchain v4.24.0, no Mathlib, so it cannot touch the restored cache):

```
lakefile: globs = ["Lib", "Lib.+"];  Lib.lean (root) + Lib/Orphan.lean (imported by nothing)
$ lake build
  ✔ [2/4] Built Lib
  ✔ [3/4] Built Lib.Orphan        ← built despite nothing importing it
produced: lean/Lib.olean, lean/Lib/Orphan.olean
```

### Consequence: two pieces of tooling now measure a premise that no longer holds

- **`content/pipeline/lean-orphan-audit.ts`** — its own header states the lakefile has *"`globs` unset"* (line ~15) and it computes reachability by walking `QOU.lean`'s imports (line ~127). Both are now wrong, so its headline "**837 of 1902 modules (44.0 %) are never built by `lake build`**" is **not** a statement about builtness. It measures *umbrella-import hygiene*, which is a real but different (and much less alarming) property.
- **`.github/workflows/lean-orphan-gate.yml`** — its rationale ("a module nothing imports is never compiled by anything, ever") no longer holds. The gate may still be wanted for umbrella hygiene, but not for the reason stated.

### The question this displaces — and it is more urgent

If `globs` builds all 1902 modules, then **any broken module makes `lake build` red right now**. This bean's own sample (153 modules, 94.8 % green, 8 failures) implies on the order of tens of genuinely-failing modules across the tree. That is no longer "unchecked code sitting in the dark" — it is a **currently-failing build**, or else those modules were fixed too.

A whole-corpus `scripts/lean-direct-cone.sh --all -k` survey is running to settle it; results to be appended here.

### Correction to my own commit on this branch

Commit `8becb91` ("register the §7c split sibling + QChebyshevFunction") justified adding those imports partly as making the modules "actually get compiled by `lake build QOU`". **That justification was wrong** — `globs` already compiled them. What the commit did correctly was satisfy `lean-orphan-gate` (which exited 1) and make the umbrella explicit; the build-coverage benefit I claimed was not real. The change is still defensible as hygiene, but the stated benefit is retracted here.


## Whole-corpus compile survey — INTERIM at 99.5 % (2026-08-15)

`scripts/lean-direct-cone.sh --all -k -j4` over the whole tree (v4.24.0, restored oleans, Lake bypassed). Two runs: the first was killed by a container restart at ~82 %, the second resumed from the surviving oleans and reached 99.5 %.

```
[1893/1903 99.5%] ok=1891 err=1 blocked=1 ready=0 inflight=1
```

**The central question is answered: the corpus is essentially green.** 1891 of 1903 modules compile. **Exactly one genuine error**, plus one module blocked behind it.

That refutes two predictions, including my own:

- This bean's §"Why this matters" implied a large unchecked-and-possibly-broken set; the 153-module sample (94.8 % green, 8 failures) extrapolates to ~100 failures across 1903. Actual: **1**.
- My own escalation hypothesis — "if `globs` builds everything then any red module means `lake build` is red *now*, and there are probably tens" — is also wrong on the count. There is one.

So the honest close is: the `globs` change (bean `qou-rc7b`) did not expose a broken corpus. The modules that were previously unbuilt are, with one exception, fine.

**Still in flight:** `QOU.Machinery.HeckeH4WedderburnMulC` (>5 min single-module elaboration; the H4 Wedderburn modules are heavy), with 8 dependents queued behind it — `HeckeH4Semisimple`, `HeckeH4RepDecomp`, `HeckeH4WedderburnInv`, `HeckeH4Wedderburn`, `Hecke.MarkovTraceOnH3A/H4A`, `Hecke.FullRankFromWedderburn`, `Hecke.InstanceOnH3A/H4A`, `SchurWeyl.QJucysMurphy`.

The identity of the single `err` module comes from the run's `--report` TSV, written at completion; it is one of that Hecke/Wedderburn chain. **Not naming it until the TSV lands** — guessing which of eleven modules failed is exactly the over-claim this repo's disciplines forbid.

**Caveat on scope.** `lean-direct-cone` bypasses Lake and writes **no `.trace` files**, so this is evidence about *elaboration*, not about what a real `lake build` would do incrementally. It is the right instrument for "does this code compile"; it is not a substitute for a real build, and (per the note added to `qou-52i4`) its output is not a cache-seeding candidate.


## RESOLVED — the one error is identified and fixed

The survey's single `err` is **`QOU.SchurWeyl.QJucysMurphy`**, failing with six occurrences of

```
error: ring_nf made no progress on goal      (lines 170, 174, 176, 197, 201, 203)
```

**Diagnosis.** All six are pure re-association steps inside two `calc` chains proving `qJM * qJMInv = 1`, over `Hecke K q qi n` — a **noncommutative** algebra. `ring` requires a `CommSemiring`, so it cannot normalise these goals and falls through to `ring_nf`, which reports no progress. The proof's own docstring already says the step is "by associativity"; only the tactic was wrong for the structure.

**Fix.** Six `by ring` → `by noncomm_ring`, the Mathlib tactic for exactly this setting. Nothing else touched: the diff is 6 insertions / 6 deletions. Verified by deleting the module's olean and recompiling from scratch — `ok=1`, no errors. The pre-existing `sorry` at line 286 (`qJM_commute`, documented in-file as blocked on the general seminormal rep) is untouched.

**Why this is the failure mode the gate was written for.** `ring_nf made no progress` is a stale-reference symptom — a tactic whose behaviour or applicability drifted out from under a proof that once compiled. Nothing imports `QJucysMurphy`, so it had no dependents to fail loudly, and before `globs` nothing built it at all.

## Final corpus verdict

| | count |
|---|---|
| modules surveyed | 1903 |
| compile green | **1902 after this fix** (1900 green + this one + the last heavy module) |
| genuine errors | **1 → 0** |

So `qou-kljb` closes as: **the premise was fixed by `qou-rc7b`'s `globs`, and widening the build exposed exactly one real breakage, now repaired.** Neither this bean's implied ~100 failures (extrapolating its 153-module sample) nor my own "tens of failures" escalation was right.

Remaining honest caveat: `lean-direct-cone` bypasses Lake and writes no `.trace` files, so this is evidence about **elaboration**, not about what an incremental `lake build` does. A real `lake build` run is still the only way to confirm build-level green, and cannot be done in this container without evicting the restored olean cache.


### Side finding — `QOU.Machinery.HeckeH4Semisimple` is a resource outlier

The survey's final module took **>11 minutes and 5.2 GB RSS** to elaborate, for 688 lines carrying **8 declarations**. Every other module in the corpus finished in seconds.

Worth recording because it is a **CI-feasibility** issue, not a correctness one: a standard GitHub-hosted runner has ~7 GB of RAM, so a single module at 5.2 GB is close to the ceiling — and `lake build` would elaborate it in the same process tree as everything else. Anyone who re-enables auto-triggered CI (currently all workflows are `workflow_dispatch`-only by the 2026-06-30 owner directive) should expect this module to be the binding constraint, and may need a larger runner or a split.

This is a distinct resource class from the one the lakefile already documents: `AllKnownIsotopesUniqueness` needs `moreLeanArgs = ["-s", "65536"]` because it overflows the elaboration **stack**; this one is **heap**. Raising the stack does not help it.

Neighbouring `QOU.Machinery.HeckeH4WedderburnMulC` was also slow (~10 min) — the H4 Wedderburn cluster as a whole is the expensive region of the corpus.


## FINAL — survey complete, and a correction to my own reading

```
done: blocked=1, error=1, ok=515, up-to-date=1386 in 4631s      (1903 modules)
```

| row | value |
|---|---|
| **error** | `QOU.SchurWeyl.QJucysMurphy` — `ring_nf made no progress on goal` (223.9 s to fail) |
| **blocked** | **`QOU`** — the root module, blocker `QOU.SchurWeyl.QJucysMurphy` |

### Correction: I said "nothing imports QJucysMurphy". That was wrong.

`QOU.lean:332` imports it. My grep was `grep -rln "import QOU.SchurWeyl.QJucysMurphy" QOU/` — which searches the `QOU/` **subdirectory** and therefore never looks at the root file `lean/QOU.lean` itself. The conclusion I drew from it ("no dependents, so it failed silently with nothing downstream") was an artifact of that path restriction.

### What that changes — the conclusion is stronger, not weaker

The single error was **not** an isolated orphan. It blocked the umbrella root, and the lakefile sets `defaultTargets = ["QOU"]`. So **`lake build` was failing** on this corpus until the fix in this branch.

That means my earlier escalation hypothesis was right *in kind* and wrong *in magnitude*: I predicted "`lake build` is red now, probably tens of failures". It was red — from exactly **one** module.

### Close

`qou-kljb` closes as: the "795/837 never built" premise was already fixed by `qou-rc7b`'s `globs`; widening the build exposed exactly one real breakage, which blocked the root; that breakage is fixed (`ring` → `noncomm_ring`, six sites, compile-verified) and the corpus is now green.

### Resource outliers (the real remaining constraint)

Six modules dominate build time — the H4 Wedderburn cluster plus one Pauli witness:

| seconds | module |
|---|---|
| 1636 | `QOU.Archimedean.PauliWitness.Witness12B` |
| 1561 | `QOU.Machinery.HeckeH4BlockMap211` |
| 1195 | `QOU.Machinery.HeckeH4Semisimple` (measured at 5.2 GB RSS) |
| 748 | `QOU.Machinery.HeckeH4WedderburnMulB` |
| 680 | `QOU.Machinery.HeckeH4WedderburnMulA` |
| 609 | `QOU.Machinery.HeckeH4WedderburnCoord` |

Two of these exceed **25 minutes each**. Anyone re-enabling auto-triggered CI should size for that; a standard runner's memory is the binding constraint before wall-clock is.

**Standing caveat:** `lean-direct-cone` bypasses Lake and writes no `.trace` files, so this is evidence about elaboration. A real `lake build` remains the only build-level confirmation, and cannot run in this container without evicting the restored olean cache.
