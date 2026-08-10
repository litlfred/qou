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

---

## Scoped (from qou-3jwy, which cleared everything else). Every route is closed — structurally, not for effort.

After qou-3jwy this is the **only** entry keeping `precision-gates.sh` red:

    raw-float64   NEW dirty 0,  REGRESSED 1   a-K-via-lp-dual-full  395 -> 867
    padding       13 = baseline, 0 NEW        GREEN
    q0 drift      stale 321, 0 NEW            GREEN

Blast radius, measured: **58 witnesses** carry `x_star`/`y_star`, **56
producers** call the solver.

### The obvious fix is already a rejected decision, in writing

The kappa repair (qou-3jwy) worked by rendering 53-bit values with
`str_at_true_precision`. That move is **explicitly ruled out here** by
`to_dict`'s own docstring in `tools/pyhecke/python/pyhecke/lp_dual_solver.py`:

> The numeric fields are kept verbatim: every existing consumer does
> arithmetic on them (`sum(r["y_star"] …)`, `r["duality_gap"] < 1e-6`), so
> turning them into strings here would break readers silently rather than
> loudly.

That is a considered prior decision, not an oversight. Do not "just stringify
it" — 56 producers and their consumers compute on those floats directly, and
the failure mode is silent.

### The other three routes

* **Audit exemption for LP-dual fields.** `witness_raw_float64_audit.py` has
  no exemption mechanism and no knowledge of `y_star`/`x_star` (grepped).
  Adding one is an audit-POLICY change, not a producer fix.
* **Re-baseline.** Forbidden — AGENTS.md: *"Never make a red run green by
  widening a baseline. Baselines drain, never grow."*
* **MPFR backend `*_str` companions** (the qou-t0rf path). Dead here on three
  counts: `clarabel` is **not installed** in this container; the a-K witness
  records `engine: numpy`, i.e. the scipy/f64 path, which per the same
  docstring *"has nothing beyond f64 to report"*; and even with it the float
  fields REMAIN, so the audit count would not move without also changing the
  audit.

### And the growth is not a precision loss

395 -> 867 is not degradation. The count grew because a row that main leaves
empty now solves (deuteron, `A=None` -> `A=2`, 11 entries) — i.e. the witness
contains MORE correct data. Draining "the regression" therefore means
draining LP duals corpus-wide, not repairing a defect.

### What is actually being decided

Not an implementation. A choice between:

1. **Change the contract** — float -> string for the dual fields, fix the
   arithmetic consumers loudly, regenerate 58 witnesses. Honest, large, and
   reverses a documented decision.
2. **Teach the audit that an f64 with a full-precision `*_str` sibling is a
   shadow, not a defect** — principled (the information IS present at full
   precision in the same witness), but requires the MPFR backend to actually
   be used, so it is a solver-provisioning change plus an audit change.
3. **Accept LP duals as structurally f64** and give the audit a narrow,
   documented carve-out for exactly those field names — smallest change,
   but it is a carve-out and should be named as one rather than slipped in.
4. **Leave it red**, and accept that `precision-gates.sh` reports red for a
   reason that is understood and recorded.

Owner call. Recorded so the next agent does not re-derive the four routes.
