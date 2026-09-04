---
# qou-b7cf
title: LAUNDERED refilled 0 -> 34 files on main -- drain the mpf(str(f64)) sites
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T12:46:17Z
updated_at: 2026-09-03T12:46:51Z
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
