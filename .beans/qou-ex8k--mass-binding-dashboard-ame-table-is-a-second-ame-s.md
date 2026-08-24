---
# qou-ex8k
title: mass_binding_dashboard._ame_table() is a second AME source reading the column the canonical accessor exists to avoid
status: todo
type: task
created_at: 2026-08-24T08:46:39Z
updated_at: 2026-08-24T08:46:39Z
---

HIGH LEVERAGE, NOT A DRIVE-BY. 19 producers consume `_ame_table()`, and the
fix risks the object-dtype trap (mpf into a numpy array -> object dtype ->
pure-Python O(dim^3) loop; proven in this codebase, see mass_at_3A_proper).
Each consumer needs re-running and checking. Diagnosis is complete; the
change is not started.

THE TWO SOURCES
  codata_constants.ame_binding_mev(Z, A) -> mp.mpf
      The canonical public accessor. Its docstring: built from
      `binding_energy_per_A_keV`, "the column AME QUOTES -- not from
      `binding_energy_total_keV`, which the table's own metadata flags as
      'derived' and which vendor_ame2020.py computed in float64. That derived
      column carries a binary tail: 6Li is stored as 31993.987199999996 where
      the quoted column gives exactly 31993.9872." It calls itself "the
      canonical AME entry point for 300+ scripts" and says NO-FLOAT64 means
      fixing at the source.

  mass_binding_dashboard._ame_table()
      Reads computations/data/ame2020.json directly and takes
          b = r.get("binding_energy_total_keV")
      -- the exact column above -- then does `b / 1000.0` in float64.

MEASURED, not inferred (both accessors, same process):
     nuclide     _ame_table (float64)      ame_binding_mev (mpf)     delta
        6Li      31.993987199999996                  31.9939872   -4.0e-15
       56Fe      492.25995279999995                 492.2599528   -5.0e-14
          D      2.2245662000000004                   2.2245662    4.0e-16
        4He              28.2956624                  28.2956624        0.0
        12C              92.1617352                  92.1617352        0.0
The 6Li row reproduces the docstring's own cited example exactly. 4He and 12C
are clean only because the derived column happened to land on the value.

WHY IT MATTERS BEYOND THE RULE
`B_AME_MeV` / `AME_MeV` / `M_AME_MeV` is the single most common float64 field
across the raw-float64 regressed set -- it appears in 5 of the 10 remaining
(binding-single-pipeline x16, catalan-binding x18, log-ratio-prototype x7,
atom-vhyp-closure x6, bar-pairing-extension x4, path-b-habiro x3). One fix at
`_ame_table()` reaches all of them.

The accessor's docstring already predicted this failure mode in the abstract:
"Consumers working over a *table* of nuclides need the same source for
arbitrary (Z, A), and without a public entry point they hand-type the rest --
which is exactly how mass_table_ppb.py ended up with eleven typed literals
sitting up to 1.6e-5 away from this table." `_ame_table()` is the same
mistake one level up: not hand-typed literals, but a second reader of the
wrong column.

SUGGESTED SHAPE
  1. Re-point `_ame_table()` at `ame_binding_mev` for the binding column.
  2. Decide deliberately whether it returns mpf (correct, ripples to 19
     consumers) or casts once at the boundary with a stated reason, as
     `_constants()` already does ("cast ONCE at the boundary").
  3. Re-run all 19 and diff each witness; watch runtime for the object-dtype
     blowup, not just correctness.

## Summary of Changes

Fixed in 2f283e133 + follow-up. `_ame_table()` now calls `ame_binding_mev`
and `_ame_atomic_mev` and returns mpf. Verified before changing: membership
identical (all 3558 entries carry both columns), cost 0.31s for the whole
table, and the object-dtype trap does not apply (only 2 of 19 consumers
import numpy, and in neither does an AME value reach it -- the numpy/scipy
there is the Gram/seminormal path, which takes only (Z, N)).

Ran the consumers rather than assuming. 15 of 19 clean; 5 witnesses changed,
each diffed leaf by leaf with ZERO numerical values moved:
    su4-occupancy-binding-mass    f64 193 -> 102
    clambda-shape-invariant            58 ->  40
    coulomb-mirror-killswitch          28 ->  19
    charge-symmetry-bond               26 ->  20
    gg-production-bond                 12 ->   9
                                      317 -> 190   (-127 fields)
witness_raw_float64_audit: drained_files 75 -> 79, total_fields -127.

## CORRECTION: this was NOT the root cause of the regressed 5

This bean claimed `_ame_table()` was "ONE ROOT CAUSE" behind ~54 B_AME_MeV
fields in 5 of the 10 raw-float64 regressed witnesses, and that "one fix
reaches all of them". WRONG, and the measurement said so: after the fix,
`regressed` stayed at 10, unchanged.

The reason is simple and I should have checked it before predicting: NONE of
those five producers consume `_ame_table()`. They are not in the 19. There
are at least THREE AME paths in this tree, not two:
  1. codata_constants.ame_binding_mev            canonical, mpf
  2. mass_binding_dashboard._ame_table()         was float64 + wrong column
                                                 (this bean; now fixed)
  3. per-producer ad-hoc reads, each with its own float() cast:
       atom_vhyp_closure_matrix_m.py:73  ame = json.loads(AME.read_text())["data"]
                                    :87  B = float(ame[bkey])
       log_ratio_binding_prototype.py:80 B_ame = float(r["B_AME_MeV"])
       catalan_binding.py, bar_pairing_binding_observable.py  similar
Path 3 is what feeds the regressed witnesses, and it is a per-producer tail,
not a single root cause.

The fix stands on its own merits -- it was reading the derived, float64-
tainted column for 19 producers, and 127 fields is a real drop -- but the
leverage claim was mine and it was wrong.

## Discovered while doing this, not actioned

TWO DEAD PRODUCERS on main, unrelated to this change. Both unpack a 4-tuple
from `mass_binding_dashboard._constants()`, which has returned 3 values since
at least 2026-08-08, so both crash on the first line of main():
    computations/delta_lambda_shape_probe.py:80
    computations/probe_collective_binding_residual.py:79
`binding_single_pipeline_comparison.py:242` looks identical but is NOT dead --
it has its own local `_constants()` returning 4. Only running it showed that.

TWO PRODUCERS THAT CANNOT COMPLETE bare, also pre-existing: both Gram probes
stall in `gram_norm_zn` at "3H: n=9". A/B'd gram_transfer_quadratic at HEAD
WITHOUT this change: identical stall, identical point, same 240s.
pn_pair_two_sector_split.py hits 1200s in the scipy seminormal path its own
header names.
