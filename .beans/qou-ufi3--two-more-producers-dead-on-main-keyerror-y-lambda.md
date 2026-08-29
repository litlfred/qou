---
# qou-ufi3
title: 'Two more producers dead on main: KeyError ''y_lambda'' from an upstream schema change'
status: todo
type: task
created_at: 2026-08-29T20:03:23Z
updated_at: 2026-08-29T20:03:23Z
---

Found while draining the byte-exact AME routes (897caf93f). PRE-EXISTING on
main, unrelated to that change — confirmed by running main's own code with my
edits reverted.

    computations/probe_q6j_jm_spectral_delta_lambda.py
    computations/probe_volume_wedderburn_delta_lambda.py

Both die at:
    blocks = [{"part": list(r["partition"]), "y": mp.mpf(r["y_lambda"]), ...
    KeyError: 'y_lambda'

They read an upstream witness for a per-partition `y_lambda` field their
source no longer emits. Same CLASS as qou-0djm (a contract drifted and the
consumer was never updated) but a different mechanism: qou-0djm was a
function ARITY drift (`_constants()` 4 -> 3, `_row()` losing `g8`), this is a
witness SCHEMA drift.

WHAT BEING DEAD COSTS, from the qou-0djm precedent: probe-collective-binding-
residual's witness had been frozen since 2026-06-25 and 23 of its 76 leaves
were ~27% wrong, because no drain can reach a producer that cannot start.
These two are in the same position — their committed witnesses cannot be
trusted and cannot be refreshed.

THE FIX NEEDS A DECISION, which is why this is a bean and not a patch: find
what replaced `y_lambda` upstream (a rename? a restructure? dropped
entirely?) and whether these probes' claims still hold under it. That is a
question about the upstream witness's contract, not a mechanical repair.

Their AME routes are already applied (byte-exact, so they cannot regress a
producer that cannot run), and will be correct the moment the KeyError is
fixed.
