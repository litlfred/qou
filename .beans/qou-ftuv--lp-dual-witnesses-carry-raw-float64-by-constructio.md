---
# qou-ftuv
title: LP-dual witnesses carry raw float64 by construction — draining needs the shared contract changed
status: todo
type: task
created_at: 2026-08-10T09:13:32Z
updated_at: 2026-08-10T09:13:32Z
---


Surfaced preparing the #4899 merge. The raw-float64 ratchet reports
`a-K-via-lp-dual-full.witness.json` REGRESSED, 395 -> 867 fields.

It is **not** a precision regression. The producer (`aK_via_lp_dual_full.py`)
is byte-identical to main's, and the count grew because more of the LP solves:

    main    deuteron  A=None  len(x_star)=0    (row empty)
    ours    deuteron  A=2     len(x_star)=11

Every added field is a genuine LP result main's witness did not contain.
Verified by re-running the producer from a clean tree rather than reading the
diff.

**Why it cannot simply be drained.** `x_star`, `y_star`, `u_lambda_star` are
Clarabel output, and Clarabel is a float64 solver — there is no `mpmath.mpf`
to carry from the source, which is what the standing fix ("carry mpf from the
source, serialize with `_precision.fmt`") assumes. The drained convention for
such values is to serialize them as strings, recording them honestly without
claiming precision they do not have.

That is a change to the **shared** contract, not to one producer:
`solve_operator_selection_lp(...).to_dict()` /
`solve_psd_operator_selection_sdp(...)` are the canonical entry points per
AGENTS.md, and `lp_dual_witness_validator.py` reads the fields. Every LP/SDP
witness in the corpus moves with it. Scope it deliberately:

1. decide whether `y0_star` / `y_star` / `active_set` / `primal_obj` /
   `dual_obj` / `duality_gap` become strings, and what the validator accepts;
2. change `lp_dual_solver.to_dict()` once;
3. re-run the LP/SDP producers;
4. drain the baseline by the resulting delta.

Also parked here: `kappa-shell8-excess-convention.witness.json` (25 fields)
is flagged NEW by the ratchet but is byte-identical to main's copy — inherited,
not introduced by #4899, and another arc's to drain.
