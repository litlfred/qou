---
# qou-1evu
title: 'f64 laundering: three probes read q0 through mpf(str(f64)), freezing a 17-digit floor'
status: completed
type: task
priority: normal
created_at: 2026-09-07T06:20:21Z
updated_at: 2026-09-07T06:20:50Z
---

Found by the `f64-into-mpmath` advisory in `scripts/precision-gates.sh`, which
reported: `LAUNDERED — mpf(str(<f64>)): 3 file(s), 3 site(s). These are defects.`

## The defect

    computations/probes/c5_sign_is_robust_convergence_claim_is_not_probe.py:157
    computations/probes/cumulant_hierarchy_does_not_converge_probe.py:169
    computations/probes/planck_symbolic_in_q_probe.py:103

all did `mp.mpf(str(Q0))` where `Q0` is `q_parameter.Q` — the **float64** q0. The
substrate exports `Q_MP`, an mpf carrying the anchor's full 50 digits, from the
same module. Measured:

    Q_MP           1.10997858275138080759166909561
    mpf(str(Q))    1.1099785827513808
    relative gap   6.839e-18

`str()` on a float round-trips, so nothing is lost *relative to the float* — but
the float itself is a 17-digit floor, and these probes then compute at 30–40 dps
against it. AGENTS.md is explicit that probes are not exempt and that a float64
input poisons the result; `c5_sign...` in particular is a probe about whether a
**convergence claim** survives, i.e. exactly where trailing digits decide.

## Fixed: import `Q_MP` instead

All three now take `from q_parameter import Q_MP`, and the `mpf(str(...))` wrap is
gone. In `planck_symbolic_in_q_probe` the sympy hand-off also went from
`sp.Float(str(Q), 40)` — 17 digits dressed as 40 — to `sp.Float(mp.nstr(Q, 40), 40)`.

## MEASURED consequence — small, and I am not overstating it

    cumulant_hierarchy: recursive-vs-direct Mobius residual  2.66e-15 -> 1.78e-15
    planck_symbolic:    output identical but for one provenance line
    c5_sign:            rows identical to all displayed digits

The cumulant move is a 33 % reduction on a residual **the probe's own docstring
already flags as suspect** — it says the 2.7e-15 agreement "was read straight off
that floor and was NOT evidence as stated". It still is not evidence: the
matrices are `numpy.ndarray(dtype=float)` by construction, so that residual
remains a float64 floor and the epistemic reading is unchanged. Only the q input
improved.

**This is precision HYGIENE, not a result.** No conclusion in any of the three
probes moves. Reporting it that way rather than as a win, because a 6.8e-18 input
correction that leaves every displayed digit alone is exactly the kind of change
that gets over-sold.

## One documentation defect fixed alongside

`cumulant_hierarchy`'s docstring described this defect in the PAST tense — "`q`
came from `mp.mpf(str(Q0))` ... so it carried 17 digits" — while the code below
still did it. That past tense is now true, and the docstring says so, with the
measured residual move.

Deliberate `float()` downcasts feeding the numpy path are untouched: they are
declared, and the numpy leg is float64 by design.

Landed on litlfred/qou#6971.
