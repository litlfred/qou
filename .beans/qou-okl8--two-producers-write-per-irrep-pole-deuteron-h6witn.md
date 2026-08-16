---
# qou-okl8
title: Two producers write per-irrep-pole-deuteron-h6.witness.json (schema-lossy collision)
status: todo
type: task
priority: normal
created_at: 2026-08-16T21:23:41Z
updated_at: 2026-08-16T21:24:24Z
---

## Evidence (found while draining the deuteron chi cache, PR #5260)

Two producers emit the SAME witness filename with DIFFERENT schemas:

| producer | line | name emitted |
|---|---|---|
| `per_irrep_pole_atom.py` | 364 | `f"per-irrep-pole-{atom_name}-h{n}"` -> `per-irrep-pole-deuteron-h6` |
| `per_irrep_pole_deuteron_h6.py` | 226 | `"per-irrep-pole-deuteron-h6"` |

Whichever runs last wins, and the atom producer's schema is strictly richer.
Running the deuteron-specific script over a committed atom-produced witness
DELETES, among others:

    cemetery_class_signed_power_projection   net_signed_power
    is_pure_power_in_cemetery                per-gen_idx crossing breakdown
    sigma / sigma_inv / averaged counts       total_crossings

Measured on this branch: 230 deletions vs 39 insertions. I triggered it, caught
it in the diff, and restored from HEAD; nothing was lost. But nothing WARNED —
`WitnessBuilder` happily overwrites, so the loss is silent and the next agent
may not diff before committing.

Note the two agree on the physics (both give per-term poles 46/42/30/10 for the
colour-weighted word), so this is purely a schema/ownership defect, not a
numerical disagreement.

**Fix options:** (a) give the deuteron-specific script a distinct name, e.g.
`per-irrep-pole-deuteron-h6-poleonly`; (b) delete it as superseded by the
generalised atom producer (its docstring already says "same recipe as
per_irrep_pole_proton_h3 / per_irrep_pole_deuteron_h6"); (c) have
`WitnessBuilder.save()` refuse to shrink a witness whose committed copy carries
keys the new payload lacks, unless passed an explicit override. (c) is the
general guard and would catch the whole class.
