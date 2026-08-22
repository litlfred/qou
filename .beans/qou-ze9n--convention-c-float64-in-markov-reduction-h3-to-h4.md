---
# qou-ze9n
title: Convention-C + float64 in markov_reduction_h3_to_h4_verify — cited as Lean keystone evidence
status: todo
type: task
priority: normal
created_at: 2026-08-22T09:59:39Z
updated_at: 2026-08-22T10:00:30Z
---

## What was found

`computations/probes/markov_reduction_h3_to_h4_verify.py` carries two defects,
and its conclusion is quoted in `QOU/Machinery/MarkovTraceOnHecke.lean` as the
evidence for keystone ingredient 2 (the `Ind_{H3}^{H4}` Markov stabilization).

**1. Convention C, after the 2026-08-15 ruling excised it.** Line 60:

```python
z = float(+(1.0 / (mp.sqrt(Q_MP) + 1.0 / mp.sqrt(Q_MP))))
```

Measured at the proton pin: this is **0.4993203342**, which is `sqrt(q)/(q+1)`
= z_C exactly. Convention D is `q**3/(q**2+1)` = **0.6126880371**. They differ
by 0.113 — 23 %, a different quantity, not a rounding difference.

**2. float64 end to end**, against the STRICT 2026-08-18 "PROBES ARE NOT
EXEMPT" directive:

- `q = float(Q0_FLOAT)`
- line 60 computes inside `mp.workdps(100)` and immediately casts to `float` —
  the dps no-op the precision gates exist to catch, buying 100 digits and
  discarding them on the same line
- `np.eye`, `np.trace`, `float(np.trace(M))`
- `np.linalg.solve(A, b)` for the Markov weights `y_vec` — a linear solve on a
  character matrix, in float64, where conditioning can be far worse than 1e-16
- `TOL = 1e-9`

## Why this is not just hygiene

The directive's own reasoning applies exactly: *"A witness is a number that
gets re-derived; a probe conclusion is an argument that gets written into a
bean, an audit doc, a PR body and a content block, where nothing re-derives
it."* Here the argument was written into a **Lean docstring**, as the evidence
for a keystone ingredient, and has sat there since.

## Done under this bean

- Extended `scripts/convention-c-producer-audit.py` with `unwrap_casts()` so
  the cast-wrapped spelling is matchable at all — it was blind spelling #14,
  recorded in `docs/audits/2026-08-15-detector-blindness-taxonomy.md` §7.
  Self-test battery 50 -> 58, all pre-existing cases still pass.
- Re-measured: the fix moves the actionable count **1 -> 2**, not 0 -> 2. The
  other site (`qbeta_h_frame_rungs_probe.py:73`) was already detected.

## NOT done — deliberately

The probe has **not** been ported to D or to exact arithmetic. Both changes
alter what the keystone evidence says, and the Markov law
`tr_M4(x*sigma_2) = z*tr_M3(x)` contains `z` explicitly, so a C -> D swap can
change whether it holds. That is a re-derivation, not a migration — the same
distinction AGENTS.md draws for the c_k ladder under `qou-cds1` ("not a
z-swap, and that is proved").

Next honest step: re-derive under D in exact arithmetic and report whether the
stabilization law survives. If it does, the keystone evidence is upgraded from
float64/C to exact/D. If it does not, `MarkovTraceOnHecke.lean`'s ingredient-2
paragraph needs rewriting, and that is the more valuable outcome.
