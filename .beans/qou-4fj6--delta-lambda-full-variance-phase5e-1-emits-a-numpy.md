---
# qou-4fj6
title: delta_lambda_full_variance_phase5e_1 emits a numpy Gram inverse as raw float64 once its try/except path succeeds
status: completed
type: task
priority: normal
created_at: 2026-08-23T16:29:22Z
updated_at: 2026-08-23T22:14:41Z
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


---

## RESOLVED 2026-08-23 — there was no tier to declare, only a wheel to rebuild

Both "possible resolutions" this bean posed were predicated on the stale
wheel, and neither is needed.

`gram_inverse` was DELETED from the Rust source on 2026-08-15 (the Markov-Gram
form is singular under convention D, so the 6x6 inverse does not exist and
`AttributeError` is the documented intended outcome). The container's wheel was
built 2026-08-09 and still exported it, so the try/except at
`delta_lambda_full_variance_phase5e_1.py:317` — written to catch exactly that
AttributeError — never fired, and 37 float64 values entered the witness. That,
not a precision-tier question, is why the raw-float64 ratchet reported
445 -> 482.

With the wheel rebuilt (bean qou-nm6y), regenerated 2026-08-23 in 9a5d18462:

    Gram inverse load failed: module 'pyhecke_native' has no attribute 'gram_inverse'

    gram_inverse_H3 present:                 False
    gram_inverse_condition_number present:   False
    raw float64 fields:                      445   (baseline)

So the fields are correctly absent, the ratchet is back at its baseline, and
the witness is no longer knowingly stale — it now says what the producer
actually computes. The domain call this bean was blocked on ("is the Gram-dual
at H_3 a diagnostic or does it feed a scored observable?") does not arise: the
quantity is not computed at all under convention D, because it does not exist.

The bean's "worth checking alongside" question — why the load fails on some
machines and not others — is answered and now GATED:
`scripts/check-pyhecke-native-staleness.py` (360a9ae0c, blocking in
`staleness-gates.sh`) compares the installed module's exports against the
`#[pymodule]` block that declares them, and fails on any export the source no
longer declares. Verified to fire on this exact case.

The remaining 445 raw float64 in that witness are pre-existing debt tracked
under qou-gqt5, not this bean.
