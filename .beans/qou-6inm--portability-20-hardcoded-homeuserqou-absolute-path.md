---
# qou-6inm
title: 'Portability: 20 hardcoded /home/user/qou absolute paths across 12 files silently break every other checkout'
status: todo
type: task
created_at: 2026-08-30T18:39:51Z
updated_at: 2026-08-30T18:39:51Z
---


Surfaced 2026-08-30 while closing two items of `qou-c7g8`. One of those
failures — `qbeta_counit_trace_transport_overshoot_probe.py` — was caused by
exactly this and had been misfiled as a `qou-ya1e`-shaped path-bridge fault.

## The defect

Producers hardcode absolute paths into a checkout at `/home/user/qou`. This
repo lives at `/workspace/qou`, and any clone anywhere else has the same
problem. The failure mode is usually **silent**: a `sys.path.insert` of a
nonexistent directory raises nothing, so the producer limps on and only dies
later at an unrelated-looking import — or, worse, works by accident because
`_path_bridge` happened to cover the same module, leaving a dead line that
looks load-bearing.

Where the path is a FILE target rather than a sys.path entry it is not silent:
`gen_l6a4_angle_structure_lean.py` died with FileNotFoundError writing its Lean
output, never emitting the file it exists to generate.

## Remaining: 20 live occurrences across 12 files

    computations/audits/no_q0_recorded_producer_split.py
    computations/audits/witness_dependency_residue_run.py
    computations/audits/witness_dependency_residue_targets.py
    computations/deltalambda/threerow_isospin_parity_probe.py
    computations/deltalambda/threerow_n12_isospin_control.py
    computations/deltalambda/threerow_qcross_trend_probe.py
    computations/h4_gram/hecke_h4_markov_gram_derive.py
    computations/h4_wedderburn_iso/derive_wedderburn4_cofactors.py
    computations/markov/d_frame_closed_form_law_probe.py
    computations/probes/qbeta_3bp8_a2_sample_point_delta_check.py
    computations/qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py
    scripts/lean-build-cone.py

(Comment/docstring mentions excluded; those are harmless.)

## Already fixed (in `qou-c7g8`)

    computations/probes/flavor_split_3strand_derivation_probe.py
    computations/probes/flavor_split_partial_derivation_probe.py
    computations/probes/gen_l6a4_angle_structure_lean.py      (2: syspath + output)
    computations/qbeta/qbeta_counit_trace_transport_overshoot_probe.py

## Counting hazard — do not repeat my mistake

I first reported "6 live" by grepping `sys.path.insert`. That undercounts badly.
The forms in use are at least:

    sys.path.insert(0, "/home/user/qou/…")
    sys.path[:0] = ["/home/user/qou/…", …]
    for _p in ("/home/user/qou/…", "/home/user/qou/…"): …
    ROOT = Path("/home/user/qou")
    DATA = "/home/user/qou/computations/…json"
    out  = "/home/user/qou/content/…lean"

Count the literal `/home/user/qou`, minus comment lines — not one call shape.

## Fix

Derive the root from `__file__` at the file's own depth (`parents[1]` for
`computations/x.py`, `parents[2]` for `computations/sub/x.py`, …). Verify each
file still parses AND imports afterwards: several of these paths are currently
dead, so repairing them makes code run that has not run in a while, and that
can surface real failures underneath. Fix in small batches, not one sweep.
