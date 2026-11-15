---
# qou-o227
title: Three new q-NS probes carry raw float64 without declaring precision_tier
status: completed
type: task
priority: normal
created_at: 2026-08-15T03:40:21Z
updated_at: 2026-08-15T04:08:46Z
---


## State

Found while rebasing #5051 (f64-integrator carve-out) onto main. NOT caused
by that PR — these landed on main from q-NS work in the interim, and they
are different probes from the three #5051 carves out.

    22 fields  computations/qns-nonlocal-transfer-probe.witness.json
    12 fields  computations/qns-amplitude-step-probe.witness.json
    12 fields  computations/qns-dissipation-scale-probe.witness.json

## They plainly qualify — their own docstrings say so

    qns_nonlocal_transfer_probe.py:38   "Precision tier: float64 RK2 adaptive CFL (SF6/SF7 integrator)"
    qns_amplitude_step_probe.py:33      "Precision tier: float64 RK2 with adaptive CFL"
    qns_dissipation_scale_probe.py:45   "Precision tier: float64 RK2 adaptive CFL (same integrator as SF6)"

Same class as the three #5051 carves out. The integrator IS the source, so
"carry mpmath.mpf from the source" has nothing to act on.

## Why I did NOT just add the line

One line each would clear it:

    w.add_data("precision_tier", "float64-integrator")

I deliberately didn't, for two reasons worth preserving:

1. **The declaration is supposed to be the AUTHOR's claim on the record**,
   not something the auditor infers on their behalf — that is the whole
   design of the #5051 carve-out. These probes belong to active q-NS work
   that merged hours ago; their author should opt in.
2. **Widening a carve-out to turn a number green is the abuse the design
   guards against**, regardless of how defensible each individual case
   looks. The moment it becomes normal to add the declaration for someone
   else, the gate stops meaning anything.

## Next step

Ask the q-NS author to add the declaration to the three producers and
re-run them. If they say the tier is wrong for any of the three, that one
needs a producer fix instead — do NOT baseline it.

Also still open and unrelated: `rho-k-co-casimir-extended` REGRESSED 3 -> 4
on `compute_wall_sec`; diagnosed in #5051 as a stale witness (the producer
already emits the formatted value), heals on its next legitimate run.

## RESOLVED by PR #5080 (the q-NS author, ~40 min after this bean opened)

All three declared, and done the way that holds up: the `precision_tier`
marker was added to the **producer**, and the witnesses were **re-run**
rather than hand-edited — `scriptHash` moved and `scriptCommitSha` went
`"unknown"` -> a real sha on all three.

That distinction is the point. A hand-added `precision_tier` in the JSON
would have passed the audit while leaving the producer un-declared, i.e. an
excuse with no author behind it — exactly what the carve-out design exists
to prevent.

Confirms the call to bean this rather than fix it myself: the declaration is
the author's claim on the record, and the author made it.
