---
# qou-b7cf
title: LAUNDERED refilled 0 -> 34 files on main -- drain the mpf(str(f64)) sites
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T12:46:17Z
updated_at: 2026-09-03T20:20:19Z
---

## State (2026-09-03, PR #6489, branch claude/laundered-sweep-2026-09-03)

`f64_into_mpmath_audit.py --tier LAUNDERED` went 0 -> 34 files on `main`.
Confirmed against `origin/main` blobs: 34 files carry
`mpf(str(Q|Q0))`; on this branch, 0. Corpus-wide the audit now reports
**LAUNDERED - none**, and none of the 34 appears in F64_CAST (the 195
sites there are pre-existing on `main`).

### The 68 expressions split three ways, and only two are defects

| class | sites | source | verdict |
|---|---|---|---|
| (a) | 38 / 34 files | `q_parameter.Q` = `_solve_q_proton_f64` | **defect**, 6.8395e-18 read at 25-65 dps. Fixed: `q_at(mp.mp.dps)` |
| (b) | 21 / 9 files | `codata_constants` | **NOT a defect** - already `mpf` at prec=169 from exact decimal literals; `mpf(str(v)) - v` measures exactly `0.0`. Left alone |
| (c) | 11 / 7 files | `D_PN`, `build_nucleon_nf`, `build_atom_nf` | **defect** for the first two; the third has no correct exact route |

Class (b) is the one worth remembering: the planned producer-side `_STR`
companions would have been pure churn. The owner's question - "isn't
`str()` bad?" - is what forced the measurement.

### Three sites the `mpf(str(` regex cannot see

`sp.Float(str(Q0), 30)`, `sp.Float(float(Q0))` x5, `build(str(Q0))`. The
first renders `1.10997858275138080000000000000` - thirteen trailing zeros
where the true digits `759166909561` belong. Another entry for the
detector-blindness taxonomy.

### Producer bug found and fixed on the way (see PR)

`pyhecke.atom.build_nucleon_nf_mp`, the "float64-free twin", was stale by
the 2026-08-30 gluon term (`qou-1qsw`, crossing budget 9 -> 11) while its
docstring advertised agreement to `1.4e-16`. Measured, every component
disagreed, worst **2288 %**. Fixed; restores 5.032e-16 / 1.143e-15. Zero
consumers, which is how it went stale. `hecke_core` now re-exports it.

### Method note - two traps hit, both named in AGENTS.md

1. **Probes write SIBLING witnesses.** My first before/after run mutated
   the tree it was measuring - 32 `*.witness.json` dirtied. The harness
   now restores `computations/` after every run.
2. **`origin/main`'s own probe produced different numbers 80 minutes
   apart on an unchanged tree** (C14->N14 disc 12.94889 vs 12.80479,
   1.1 %). Refuted by measurement: q0 conditioning (a 1e-16 perturbation
   moves nothing), `pyhecke_native` dispatch (`QOU_DISABLE_NATIVE=1`
   identical), a witness input (the import cone reads no JSON), my own
   edits (main's file on the current tree gives the NEW value). The
   container was then replaced, which is the likeliest cause and is now
   unconfirmable. First comparison discarded; both sides re-run in one
   environment from a clean tree.

### Not a gate - a claim I made and retracted

I twice asked the owner whether to register the 34 in
`q0_anchor_manifest.json`, saying the branch would otherwise land
knowingly red. Wrong: `q_parameter` selects muon only for stems listed
in `ideal_muon` and falls through to proton otherwise, and
`Q0_ANCHOR_MISSING` is "a tolerated, visible state" per `witness.py`. The
manifest covers 764 of 3798 scripts. Not registering.

### Out of scope, filed not fixed

`pyhecke.gram.q0` is a **float64** module constant; `pyhecke.atom` binds
`D_PN` from it, and that file's own comment says 1027 of the 1929
witness-writing producers reach it. Far beyond this branch.


## Sweep complete (PR #6489)

**35 sites, not 34.** `precision-gates.sh --changed` found
`mirror_penalty_decomposition_probe.py:95` after I had recorded the count
as zero. It is on main and was outside my sweep list because that list was
"files I changed", not "files the detector flags". **A sweep keyed on the
files you touched cannot close a defect class; only re-running the detector
can.**

### Before/after, both sides in one environment from a clean tree

|  | before (origin/main) | after (branch) |
|---|---|---|
| exit 0 | 32 | 32 |
| exit 1 | 1 | 1 |
| exit 124 | 1 | 1 |

* exit codes identical; both failures pre-existing and unrelated
  (`qbeta_habiro...` raises its own `AmDifferenceInvalid` guard,
  `the_alpha_spike...` exceeds 300 s)
* **verdict changes: 0 / 34** — no PASS/FAIL/allPassed/ELLIPTIC/REFUTED/
  CONFIRMED moves anywhere
* stdout: 19 identical, 8 digits-only, 7 other — all 7 read individually,
  every one a near-zero residual whose printed value is round-off, or an
  added digit

Two worth recording as improvements rather than churn:
`qbeta_bring_tau0`'s `w_sym - w_alt` went `4.6e-41/1.8e-40/7.3e-40` ->
`0.0/0.0/3.7e-40` (two became exactly zero), and the protium probe's
`|E_0*(-eps) - Q_A| = 0.0` became `2.67e-51` — the `0.0` was the laundered
q_0 faking exact agreement with a Lean theorem.

### The one non-numeric change was a pre-existing degeneracy

`the_hull_exit`'s `e_max` row: `u = -log c = LQ` EXACTLY by the definition
of `e_max`, so `ratio_at_u`'s `u < LQ` is a strict comparison on an exact
tie and `LQ - u` in its denominator IS the round-off. Laundered q_0 printed
`False / T=1 BINDS`; `q_at` printed `True` and a ratio of 4.8e40. Neither
meant anything. Window is half-open, so the row now reads
`boundary / excluded`. Assertion never read it; still PASS.

### Precision gates: red, and it is main's red

11 gates red, exit 1. **Proved not attributable to this branch**: the
ratchets read `*.witness.json`, and between the merge base and HEAD exactly
4 witnesses differ, all 4 byte-identical to origin/main's (untracked files
swept in by the bad `63a8f129d9`; they vanish on rebase). Nothing else in
the diff but `.py` and `.beans/`.

Two of my own measurement errors, corrected: I first read the ratchet as
1748/153 (branch) vs 1630/39 (main) and nearly called the 114 difference
mine — but `git checkout origin/main -- computations` compares my BASE to
CURRENT main (base `098983e5a2`, main `b8d883189d`) and does not remove
files absent from it, so that tree was a mixture; and my "only on branch"
list was measuring output VERBOSITY, not content (two sampled entries exist
identically on both refs). The audit also **self-perturbs** — two
consecutive runs on an unchanged tree gave `NEW: 153` then `154`, because
the run writes its own witness into its own scope.

### Method traps hit, all three named in AGENTS.md

1. Probes write SIBLING witnesses; my first run mutated the tree it
   measured (32 dirtied). Harness now restores `computations/` per run.
2. `origin/main`'s own probe gave different numbers 80 min apart on an
   unchanged tree; four hypotheses refuted by measurement before the
   container was replaced, which is the likeliest cause and is now
   unconfirmable. First comparison discarded.
3. **`git checkout <ref> -- <path>` STAGES.** A later `git add .beans &&
   git commit` swept 56 `.py` reversions into a commit labelled
   `beans(...)` — the whole of class (a) and (c). Caught only because the
   re-run reported 16 of 17 probes IDENTICAL, impossible for this change.
   Reverted in `5119c3dcea`.


## RETRACTION (2026-09-03): "the q0 ratchet self-perturbs" was my error

Re-measured on a genuinely clean tree: three consecutive
`q0_anchor_ratchet.py` runs give **NEW=39 every time** and dirty **zero**
files. The script writes nothing on its read path, and it ALREADY excludes
audit-emitted witnesses (`AUDIT_SUFFIXES`, imported from
`q0_anchor_consistency_audit`, filtered at `_is_in_scope`).

The `153 -> 154` came from the same contaminated sequence as the retracted
`1748 vs 1630`: a tree dirty with witnesses my own probe runs had written,
with `git checkout origin/main -- computations` in between. **I retracted
the pair and kept the mechanism without re-checking it** — that is the
actual error, and it is worse than the original mistake because the
retraction was the moment to catch it.

I had also conflated two scripts: `q0_anchor_consistency_audit.py` DOES
write a witness via `WitnessBuilder`, but it ends in `-audit.witness.json`
and is excluded by the very convention above.

Cost: I published this on #6453, #6489 and in the ledger, and #6453 spent
three verification runs answering the false version.

**The general rule survives — never measure a gate on a tree your own runs
have written to.** It is simply not what this gate does.
