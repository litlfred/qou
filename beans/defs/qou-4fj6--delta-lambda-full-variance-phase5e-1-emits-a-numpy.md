---
# qou-4fj6
title: delta_lambda_full_variance_phase5e_1 emits a numpy Gram inverse as raw float64 once its try/except path succeeds
status: in-progress
pr: 8190
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T16:29:22Z
updated_at: 2026-11-16T20:28:40Z
parent: qou-9nnz
---

`computations/delta_lambda_full_variance_phase5e_1.py:321` emits a numpy matrix:

    builder.add_data("gram_inverse_H3", gram_inv.tolist())
    builder.add_data("gram_inverse_condition_number", float(np.linalg.cond(gram_inv)))

Both sit inside a `try/except` whose handler prints *"Gram inverse load failed"*.
In the committed witness **both fields are absent** — the load was failing. In
this container it now succeeds, so the fields appear, carrying 37 raw float64
values, and the blocking raw-float64 ratchet reports the witness REGRESSED
(445 -> 482).

## This is not a downcast leak

Nothing stringified an mpf. `np.linalg.inv` and `np.linalg.cond` are float64 by
construction, and the values are genuine numerical-linear-algebra output. The
change is that a previously-broken code path started working.

## Two possible resolutions — both are domain calls

1. **Declare the tier.** `witness_raw_float64_audit.py:200` documents
   `w.add_data("precision_tier", "float64-integrator")` for exactly this class,
   and the audit already excuses 65 fields across 3 witnesses under it. A Gram
   inverse is plausibly such a case.
2. **Carry it at substrate precision** — compute the inverse in mpmath rather
   than numpy, if the Gram dual is meant to be exact.

Which is right depends on whether the Gram-dual at H_3 is a diagnostic or feeds
a scored observable. That is not a call to make silently, and declaring a tier to
turn a red gate green is precisely what the ratchet's own output warns against.

## Interim state

The witness is reverted to its pre-regeneration content (without the fields), so
the blocking gate is green. It is therefore knowingly stale, and understates the
producer's output, until this is decided.

## Worth checking alongside

Why the load fails on some machines and not others. If it depends on a file that
is present here and absent in CI (or vice versa), other producers may be silently
skipping outputs the same way — a `try/except` that prints and continues will not
show up in any ratchet.



---

## Attribution settled: this is main's, not the dps sweep's

I ran **main's own version** of `delta_lambda_full_variance_phase5e_1.py` in this
container:

    MAIN-side producer -> gram_inverse_H3 present: True

So the field appears from main's unmodified producer too. The dps sweep did not
cause it, and neither did anything else on this branch. **Main's committed
witness is stale relative to what main's own producer emits** — it was generated
on a machine where the `try/except` load failed, and it has carried that hole
ever since.

The blocking raw-float64 ratchet therefore reports REGRESSED (445 -> 482) for a
condition that is latent in main and becomes visible the moment anyone
regenerates this witness on a machine where the Gram inverse loads.

Reverting the witness is not a way out: the witness shape guard (also blocking)
then reports it COLLAPSED, and `precision-gates.sh:75` invokes that guard with no
arguments, so its `--accept` escape is unreachable from the gate. The two
blocking gates pin the witness between them until the tier question is answered.

## Progress Update (2026-11-16, PR #8190)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/Float64EngineReachabilityAndGramInverse.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/float64_engine_reachability_and_gram_inverse_probe.py` and stamped witness `computations/probes/float64-engine-reachability-and-gram-inverse.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 2ed61761fb447e7b912df4f3ef73e8603236969a`).
- [ ] Awaiting merge of PR [`litlfred/qou#8190`](https://github.com/litlfred/qou/pull/8190) (`345a3f9ff4ba913bb465b8884e861bfccde997ca`).

