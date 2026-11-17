---
# qou-9bei
title: 'GAP: he_nu_sdp_saturation_obstruction''s indefiniteness premise is contradicted by its own witness'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T11:42:47Z
updated_at: 2026-11-17T07:26:20Z
parent: qou-10v9
---

`computations/probes/he_nu_sdp_saturation_obstruction.py` states, in its module
docstring, the premise its OBSTRUCTED verdict leans on:

  > q0 — the Gram is indefinite (**negative-norm blocks present at BOTH q→1 and
  > q0**, so the indefiniteness is structural, not a q0 artifact)

**Its own committed witness reports `neg_norm_blocks: 0` for every atom in BOTH
regimes** — D/T/3He at q→1 and at q0, six zeros. That was true before this
session touched anything; it is not a regression.

## Why nobody noticed: the field was reading arithmetic residue

`n_neg = int((frob < 0).sum())` with `frob = y_lambda * hook_dim`, and the
hook-length dimension is a positive integer — so the count is entirely
`sign(y_lambda)`. **Eight of the eleven n=6 y_lambda are mathematically zero**,
and their computed values sit at 1e-52 .. 1e-54 while the real blocks are
1e-2 .. 1e-1. Fifty orders of magnitude apart, with the cut at exactly 0.

At the retired A pin those residues came out as **exact 0.0**, so the count read
0. Moving to the proton pin (11.5 ppb) moved them off exact zero and the count
jumped **0 → 3** for D and **0 → 10** for 3He and T — with nothing about the
Gram having changed. Control run confirms it is the pin and not code drift: the
OLD pin under CURRENT code reproduces the committed 0/0/0 byte-identically.

Thresholded at 1e-30 (PR on `claude/he-nu-sdp-pin-straddle-fix-2026-08-30`),
the count is stable at 0 under either pin, and a companion
`blocks_indistinguishable_from_zero` (7 for D, 25 for T and 3He) records the
separation instead of hiding it behind a cut.

## What is open

**Scope (a), not (b).** The stated EVIDENCE for structural indefiniteness is not
present in the witness. That does not establish the claim is false: the verdict
also rests on the LP being unbounded / rail-degenerate, which is a separate
observation and is untouched here. What is needed is either

  1. a different, actually-measured witness for indefiniteness (a genuine
     negative eigenvalue of the Frobenius Gram, not a sign count over blocks
     that are zero), or
  2. a corrected docstring that drops the negative-norm-block justification and
     rests the OBSTRUCTED verdict on the LP behaviour alone.

Not decided here — which of the two is right is a judgement about what the
probe is claiming, and the docstring is the probe's own scientific statement.
The measurement is done; the interpretation is the author's.

Related: `qou-tekx` (the pin straddle that surfaced this), `qou-2whe` (the
detector that could not see it).

## Implementation & Witness Progress (PR #8253)
- Branch: `qou-10v9-4e5k-742w-9bei-cblw-fv0s` (`52305a7a1e7f9836f16e0d5d8d454bd72705f9b1`), PR: `litlfred/qou#8253`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/deuteron_trace_discrepancy_m1_rho_constant_sdp_zero_threshold_pn_colour_factor_and_sign_wire_loss_probe.py` -> `computations/probes/deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss.witness.json` (`allPassed: true`, `scriptHash: ece5f27ee4a5`, `scriptCommitSha: 1c76aa0739f7803dab0155515577d8888a08fc68`)
