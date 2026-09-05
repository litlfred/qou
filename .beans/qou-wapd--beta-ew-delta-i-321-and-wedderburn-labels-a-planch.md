---
# qou-wapd
title: beta_ew_delta_I_321_and_wedderburn labels a Plancherel-weighted sum a 'Markov trace' — it sends the identity to 11.139, not 1
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T12:23:07Z
updated_at: 2026-09-05T12:23:40Z
---

## Finding, measured 2026-09-05 — `probes/beta_ew_weight_is_not_markov_probe.py` (4/4)

Follow-on from `qou-oots`. That bean's consumer audit named
`beta_ew_delta_I_321_and_wedderburn.py` as the ONE live non-harness file still
on the superseded `dim_q^2/[n]_q!` weight, and the obvious next step was to
migrate it to the now-canonical Molien. Reading it first turns up a PRIOR
question that makes the migration question moot for this file.

The file computes and labels a **'Wedderburn-weighted Markov trace'**:

    tr_M(beta_EW Delta_I) = SUM_lam w_lam chi^lam,   w_lam = dim_q^2/[n]_q!

The canonical Frobenius pairing of this framework is `tr_M = SUM_lam y_lam
chi_lam` with the **Ocneanu/Markov** weights. Those are different objects, and
the difference is not a convention.

**THE DECISIVE MEASUREMENT: a Markov trace is NORMALISED, tr_M(1) = 1.**
Evaluating both weightings at the identity braid (chi^lam(1) = f^lam), n = 6,
q0, 50 dps:

    SUM_lam y_lam       chi^lam(1) = 1.000000000000000000...   <- a Markov trace
    SUM_lam (d_q^2/[n]_q!) chi^lam(1) = 11.13944754035206007   <- not one

So the object the file calls `tr_M` does not send the identity to 1. That is a
fact about the object, independent of any convention choice.

**THEY DO NOT EVEN HAVE THE SAME SUPPORT.** At n = 6, `y_lam` is **exactly
zero on 7 of the 11 partitions** — every lambda with more than 2 rows, the
SU(2) row cap — while the consumer's weight is nonzero on all 11. No
lambda-independent rescaling relates a weight that vanishes where another is
positive, so this is not two normalisations of one sum; the sums run over
different index sets.

**THE CONSEQUENCES ARE NOT CONFINED TO THE LABEL.** All six of the file's
cot(theta_W) candidates are ratios of w-weighted quantities at fixed n = 6, so
a lambda-INDEPENDENT reweighting would cancel from every one. Measured, the
ratio y/w over the shared support alone spreads **234x**, and that excludes the
7 partitions where y vanishes. So the six reported candidates are not invariant
under using the weight the name claims.

**AND IT IS NOT A q-DEFORMATION EFFECT.** The notation register says the three
partition-weight families coincide at q = 1. Control at q = 1 + 1e-25: y_lam is
**still zero on the same 7 partitions**, and the shared-support spread is still
**189**. The support difference is the row cap — a statement about N — and it
survives the classical limit. A reader taking 'the families coincide at q = 1'
to cover y_lam at N = 2 would be wrong.

### What is NOT established

Which weight this file's physics actually wants. That is a question about what
`beta_EW Delta_I` is a trace OF, and this probe does not touch it. Three
readings are open and they are not equivalent: (a) it wants the Markov trace,
and the weight is simply wrong; (b) it wants a Plancherel-weighted spectral
aggregate and only the NAME 'Markov trace' is wrong; (c) it wants something
else again. Under (b) the qou-oots migration to Molien applies and the six
candidates move; under (a) they are replaced entirely.

**Not fixed here, deliberately** — picking among (a)/(b)/(c) changes a
physics-facing cot(theta_W) search and is not mine to decide from the naming
alone.
