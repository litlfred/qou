---
# qou-64jx
title: 'GAP: identify the 3.7e-4 branch splitting in the C1 q-Borel singularity'
status: completed
type: task
priority: high
created_at: 2026-08-07T08:45:08Z
updated_at: 2026-08-07T09:42:34Z
---

MEASUREMENT (no label attached — deliberately):
The level-1/2 q-Borel transform of the C1 solutions has finite radius
~ q^8.2526. Ratio-test limits converge to 10 digits WITHIN a branch but
differ BETWEEN branches by 3.7e-4.

The same 3.7e-4 scale has now shown up in three independent estimators:
  1. the step-2 ratio test
  2. the step-3 Prony blend
  3. step-4's C

Three independent estimators agreeing on a scale makes it a real feature,
not numerical noise. WHAT IT IS HAS NOT BEEN ESTABLISHED. Candidate
readings (none tested): the separation of the two q-Borel singularities;
a relative offset between the two sectors indexed by B_1,2 = ±sqrt(q-1)/q;
an artefact of the level-1/2 normalisation. Do NOT write any of these into
a witness description before measuring it.

PROCESS NOTE inherited from agent 4656, and the reason this bean is
phrased as a measurement: three times across steps 2-4 that agent wrote
the interpretation into the probe output BEFORE seeing the numbers, and
the data contradicted it each time ('ratios are NOT settling' -> they
settled to 10 digits; 'same singularity => module invariant' -> branches
disagreed; same again for C). Each was caught only because the number
happened to print next to the claim. Rule going forward: print the
measurement, derive the label afterwards.

Witness: computations/qbeta/c3-w2-c1-qborel-singularity.witness.json

## RESOLVED 2026-08-07 — it is single-parity sampling of a 2-cycle

Measured, then labelled (the discipline this bean was written to enforce).

**The estimator.** Step 2 used `xi = 1/(c[901]/c[900])` — a single-point ratio —
and checked stability by comparing `m=400` against `m=900`. Both even. The
ratio `1/(c_{m+1}/c_m)` is **exactly 2-periodic in m**, so that check reported
`1e-10` "convergence" while sampling one phase of a 2-cycle.

**The measurement.** Parity-free estimator (geometric mean of the two phases,
equivalently the two-step ratio `1/sqrt(c_{m+2}/c_m)` — these agree to 1e-100):

    xi_s = 2.3651035824525764564   for ALL THREE branches

agreeing to **3.1e-25**, against the `3.7e-4` spread of the even-only samples.
That is 21 orders of magnitude. And `log_q(xi_s) = 8.250104239513764` matches
the independent q-Gevrey fit `B + 1/4 = 8.00010423951 + 0.25` exactly.

**Verdict.** The radius is ONE number. The `3.7e-4` is not a second
singularity and not evidence for the two-sector structure. Step 2's
interpretation ("branch-dependent ratio limit => two nearby singularities")
is refuted.

**What survives, and why it is not new.** The 2-cycle is a genuine stable
feature — amplitude constant to 12 digits from m=600 to m=1200, so not a
transient — and its amplitude is branch-dependent:

    (1,0): +2.60074633423e-4   (0,1): -1.06038019777e-4   (1,1): +1.99499358648e-5

A pair of singularities at `+/- xi` (equal modulus) would produce exactly this.
But that antipodal structure is what step 3 already classified as **two-step
decoupling of the recurrence, not Stokes sectors** (PR #4656). So this is the
same phenomenon reappearing inside step 2's estimator.

**Correction to the handover.** It recorded the `3.7e-4` as having "appeared in
three independent estimators" and treated that as corroboration of a real new
feature. The three appearances are real but **not independent** — they are the
same two-step decoupling seen through three estimators that all sample parity.
So the scale was never independent evidence for two sectors, and identifying it
does **not** advance the multipliers. The theta-normalised canonical solutions
(`qou-wgnx`) remain the genuine route.

**Artifacts.**
- probe: `computations/qbeta/c3_w2_c1_parity_artifact.py`
- witness: `computations/qbeta/c3-w2-c1-parity-artifact.witness.json`
- Lean: `QOU/QBeta/ParityModulatedRatio.lean` — the mechanism, sorry-free. For
  `parityGeom γ α β m = γ^m * (α if Even m else β)`, the two-step ratio is
  `γ^2` identically (branch datum cancels, no hypothesis relating α and β),
  while the one-step ratio is `γ*(β/α)` at even m and `γ*(α/β)` at odd m. The
  two phases multiply to `γ^2` — which is why the geometric mean is the
  *canonical* repair, and why a single-parity sample cannot be fixed by going
  to larger m. It is converging to the wrong thing, not converging slowly.

**Follow-up for step 2's witness.** `c3-w2-c1-qborel-singularity.witness.json`
still carries the refuted interpretation in its `description`, `interpretation`
and `verdict` fields. It should be re-scoped; not done here to keep this PR's
diff to the new files.
