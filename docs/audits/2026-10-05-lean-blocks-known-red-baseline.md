# Lean blocks — first known-red baseline (2026-10-05)

> **Update, 2026-10-05 (after measurement): the 30 are fixed.** litlfred/qou#7538
> (merged as `015a93a39b26`) adds the missing `[BraidedCategory C]` binder to all 30
> consumers. Re-checked by the same lean-direct path as this baseline: every one went
> from exit 1 to exit 0, with error counts before the edit matching the table below, and
> no `sorryAx`. Current reds are the **6 `QOUAudits`** files only (3 superseded, 2
> fragments, 1 red by construction), none of which is a corpus defect. The tables below
> are left as measured; the JSON records the resolution in `resolutions` /
> `current_counts` and a `resolved` field on each of the 30 entries.


Story LEANNODES **L3**, bean `qou-1f1w`, epic `qou-ahxm`, issue litlfred/qou#7513.
Machine-readable twin:
[`2026-10-05-lean-blocks-known-red-baseline.json`](2026-10-05-lean-blocks-known-red-baseline.json),
which has one entry per module (source path, verdict, failure class, first error).

Everything here ran **locally in one container**. No GitHub workflow was dispatched,
because GitHub Actions are no longer available (owner ruling, 2026-10-05).

## Headline

| library | modules | green | red | skipped (missing olean) | timeout |
|---|---:|---:|---:|---:|---:|
| `QOUBlocks` | 902 | 872 | 30 | 0 | 0 |
| `UGBBlocks` | 22 | 22 | 0 | 0 | 0 |
| `Fred2005Blocks` | 12 | 12 | 0 | 0 | 0 |
| `QOUAudits` | 30 | 24 | 6 | 0 | 0 |
| **total** | **966** | **930** | **36** | **0** | **0** |

The 36 reds fall into four classes:

| class | n | what it is |
|---|---:|---|
| **corpus:** consumer not ported to `FrobeniusHopfData [BraidedCategory C]` | **30** | Real source errors, all from one root cause (below). |
| **corpus:** audit record superseded by a library repair | 3 | A dated `docs/audits` probe names declarations the library has since removed. |
| **design:** fragment, not standalone | 2 | The file says it has no imports and must be concatenated with sibling blocks. |
| **design:** probe red by construction | 1 | Generated probe whose header says a failure to elaborate means "undecided". |

**Environment gaps: zero.** No module failed for a missing Mathlib olean, a missing QOU
olean, a stack overflow, a crash or a timeout. The slowest target took 80 s. That holds
only after the two restores and the 76-module library rebuild described under Method.
Without the rebuild, the 30 corpus reds read green (see the verification section).

So the corpus defects are **30 content blocks with one cause**, plus 3 stale audit
records. Nothing in `UGBBlocks` or `Fred2005Blocks` is red.

## The 30: one library signature change, unported consumers

The library's
`QOU/QuantumObservableUniverse/CategoricalFoundations.lean` (line 60) now declares

```lean
structure FrobeniusHopfData (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
```

Its own comment at line 126 says that "the structure now requires `[BraidedCategory C]`".
The 30 content blocks still bind only `[Category C] [MonoidalCategory C]`. Each one fails
with `failed to synthesize BraidedCategory C`, or with `type expected, got
(@FrobeniusHopfData C … : [BraidedCategory C] → Type …)` where the structure is used
as a type. By chapter:

- `quantum-observable-universes`: 18
- `quantum-universes`: 6
- `lifting-and-descent`: 3
- `models-of-qous`: 2
- `mass-endomorphism`: 1

The JSON lists every file.

The library half was done correctly. The content-block siblings were left out of the
port. This is the snapshot trap AGENTS.md records for `descartesWtrace` (#6751),
repeated at 30× the size.

The fix is to add the binder, or a `BraidedCategory` hypothesis, in each consumer. That
is a Lean edit to `folio/` content, so it is **not done here**. This story is
measurement only.

## The 6 `QOUAudits` reds

| file | class | first error |
|---|---|---|
| `2026-08-30-context-classes-are-inhabited-by-zero.lean` | superseded | `Unknown identifier QOU.BraidKnot.SixTermMassFormulaContext` |
| `2026-08-30-context-classes-hand-adjudicated.lean` | superseded | `Unknown identifier QOU.ParticleInteractions.AtomicLPStabilityContext` |
| `2026-08-24-qintegermassformula-vacuity-probe.lean` | superseded | `#synth QIntegerMassFormula` fails |
| `2026-08-30-gate-classes-admit-zero.lean` | fragment | `unknown namespace QOU.Mass.MassSideKernelFormalize` |
| `2026-08-31-h2s-and-the-inert-radius-gate.lean` | fragment | `unknown namespace QOU.Molecular` |
| `2026-08-24-vacuous-prop-carrier-probe.lean` | by construction | `unsolved goals` on two `Cand*` carriers |

**Superseded (3).** The probed classes, and the global instance, were removed by the
repairs these very audits asked for. The library now mentions the removed classes only
in past-tense prose (`six_term_mass_formula_complete.lean:25`,
`atomic_lp_stability.lean:27`), and `QIntegerMassFormula.lean` "supplies no instance".
The files are dated records of a premise that no longer holds. They are not broken
library code.

**Fragment (2).** Each file's header says it has no imports and is compiled by
concatenating it with its sibling blocks (`scripts/lean-sibling-witness-check.sh`). As a
standalone `[[lean_lib]]` module it cannot elaborate. This is a membership question for
the L2 `QOUAudits` glob, not a defect in the file.

**By construction (1).** The generated probe's header says: "A carrier that does NOT
elaborate is simply undecided here." Red is a legitimate output of that file.

## Method

**Platform.**
- Lean 4.24.0, commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. GitHub-release binaries, no elan. Matches the root `lean-toolchain`.
- Mathlib rev `f897ebcf72cd`.
- Repo `main` at `d37c232b1c5`.
- Options `-DautoImplicit=false -s 65536`. A two-sided control was run first: with the flag, a file binding an undeclared `Unbound` exits 1; without it, the same file exits 0.

**Cache.**
- `lake-cache/qou-v4-24-0` at head **`a792c46d01b`**, the 2026-09-06 seed. Restored as 3480 mathlib oleans, 2703 QOU, 29 UGB and 2 Fred2005.
- `lake-cache/qou-v4-24-0-mathlib-gap-modules` at **`d7e3ae8c662`**, which adds 86 more Mathlib oleans.

The archive still stores the pre-rename paths `content/<paper>/lean/.lake`. It was
extracted with `tar --transform 's,^content/,folio/,'`. Without that, the paper oleans
land in a `content/` directory that nothing reads.

**Staleness, decided by Lake's own hash.** Every restored olean carries a `.trace`. The
trace records the Lake `Hash.ofText` of the source it was built from. The
[`lake-text-hash.lean`](../../scripts/lean-blocks-baseline/lake-text-hash.lean) helper
computes the same hash for the current source. Checked on `QOU/KnotTheory.lean`, where
both sides give `10187092109162527967`.

Of the 2983 library modules:

| state | n |
|---|---:|
| fresh | 2540 |
| source changed since the seed | 190 |
| no olean | 253 |
| dirty closure (stale, or importing something stale) | 628 |
| in the targets' library import cone | 319 |
| rebuilt from current source (dirty ∩ cone) | 76 — all exit 0, ~3.5 min |

This replaces mtime and commit-time tests. In this clone both of those flag the whole tree.

**Compile.**
- All olean roots were hardlinked into one union mirror (`cp -a --link`). Real disk cost was 44 MB of rebuilt oleans.
- Before each rebuilt output was written, the mirror entry was `rm -f`'d. The real trees were checked unchanged afterwards (QOU still 2703).
- Then `lean` ran on each of the 966 sources with `LEAN_PATH` = the mirror, 3-way parallel, with a 1800 s timeout.
- `lake` was never invoked.

Drivers: [`scripts/lean-blocks-baseline/`](../../scripts/lean-blocks-baseline/)
(`plan.py`, then `run.py`, with `L3_WORK` set to a work directory). The mirror is built
beforehand with
`for d in .lake/packages/*/.lake/build/lib/lean folio/*/lean/.lake/build/lib/lean; do cp -a --link --update=none $d/. $L3_WORK/mirror/; done`.

**"Built in place" means lean-direct on the real source path.** This is not
`lake build QOUBlocks`, which the brief forbids because it can evict the restored cache.
The modules and sources are exactly `gen-lean-blocks-shadow.py --list`. 56 of the 966
import nothing at all.

**Wall time.** Restore: fetch 1 m 56 s, extract 1 m 03 s, gap 3 s. Plan: 6 s. Library
rebuild plus 966 targets: **1075 s (17.9 min)**.

## Verification of the classification (re-run by hand)

1. **`categorical-self-duality.lean`, a corpus red.**
   - Against the current-source mirror: exit 1, `41:7: failed to synthesize BraidedCategory C`.
   - The same file against the **restored, un-rebuilt** trees: **exit 0**.

   So the red is real against the current library. It is invisible to any check run
   against the snapshot. It is not an environment gap.

2. **`2026-08-30-gate-classes-admit-zero.lean`, a fragment.** Re-run by hand: exit 1,
   `unknown namespace`. `grep` finds no `MassSideKernelFormalize` anywhere under
   `lean/QOU`, and the file has no `import` line. This matches its own header.

## Tooling gaps found on the way (not fixed here)

The `content/` → `folio/` rename left stale globs in the existing sweeps. This list comes
from reading the code; none of these scripts was run:

- `scripts/lean-content-sweep.sh` runs `find content …`, so it finds zero targets.
- `scripts/lean-library-sweep.py` discovers packages via `content/*/lean/lakefile.toml`, so it discovers none, and exits.
- `scripts/lean-shadow-verify.sh` and `scripts/lean-restore-gap-oleans.sh` also glob `content/*/lean/.lake/…`. The gap restore therefore fills only the root mathlib tree.

The cache branch also still uses the old paths. That is why this baseline used its own
drivers instead of the two sweeps the brief named.
