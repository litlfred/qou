---
# qou-epmq
title: 'Delta_L''s e_minus coordinate vanishes ONLY in the grouped frame: canonical gives -(q^2-1)^2*Phi_12(q)^2/(2q^6), so net != tr_M(z=1) on the long model'
status: in-progress
pr: 8197
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T17:42:13Z
updated_at: 2026-11-16T20:55:10Z
parent: qou-v2om
---

## Measured

`Delta_L` is the LONG Delta model — the eleven typed crossings of
`hecke_core._PROTON_G0/_G1` and `_NEUTRON_G0/_G1`, as
`beta_n - beta_p` in the regular representation of H_3. Its sixth basis
coordinate is the `e_minus` coordinate. Reordering the SAME symbols into the
borromean word (`nucleon_word_letters`' branch, so nothing depends on
precision or on q):

    grouped (committed)   delta_l[5] = 0                     exactly
    borromean (canonical) delta_l[5] = -(q-1)^2 (q+1)^2 (q^4 - q^2 + 1)^2
                                       / (2 q^6)

i.e. `-(q^2-1)^2 * Phi_12(q)^2 / (2 q^6)`, where `Phi_12` is the 12th
cyclotomic polynomial. Nonzero for every q except the roots of unity it names.

## Why it matters

`qbeta_delta_bar_parity_probe`'s assertion
`net_equals_tr_at_z_one_ONLY_when_e_minus_vanishes` records that in general
`tr_M(z=1) - net = h * (e_minus coordinate)`, because `tr_M(z=1)` weights the
basis `[1,1,1,1,1,h+1]` while `net` weights it `[1,1,1,1,1,1]`. Both Delta
models were measured to have `e_minus = 0`, so the two functionals coincide on
them — the probe is explicit that "the identity is not general and must not be"
relied on beyond these elements.

Under the canonical ordering that coincidence is **gone for the long model**:
`net(Delta_L) != tr_M(z=1)(Delta_L)`, by exactly `h * delta_l[5]`. The short
model is unaffected — it is a hand-written 6-vector, not built from a nucleon
word, so its `e_minus` stays 0 either way.

So the vanishing was a property of the GROUPED word, not of `Delta_L`.

## What does NOT change — measured, and this is most of it

Every substantive fork conclusion is frame-invariant. Driving both probes with
the reordered word:

| probe | grouped | borromean |
|---|---|---|
| `qbeta_delta_bar_parity_probe` | 16/16 pass | **15/16** |
| `qbeta_delta_element_fork_pricing_probe` | 15/15 pass | **13/15** |

Invariant across the change: `the_two_models_are_DIFFERENT_elements`,
`corpus_counit_closed_form_FAILS_on_the_long_model`,
`corpus_trace_closed_form_FAILS_on_the_long_model`,
`corpus_trace_closed_form_holds_on_the_short_model`,
`chi_two_one_vanishes_on_the_short_model_only`,
`phase_identity_FAILS_on_the_long_model`, `short_model_is_exactly_bar_odd`,
`long_model_is_neither_bar_odd_nor_bar_even`,
`long_model_has_a_nonzero_bar_even_part`, `the_fork_survives_descent`,
`neither_element_lies_in_the_two_row_quotient`,
`no_rescaling_identifies_the_two_models`,
`the_consistent_short_model_price_is_LARGER`. **The Delta fork — the thing
`qou-cds1` / `qou-bg3w` are about — does not depend on the intra ordering.**

The other two that move are both named `calibration_*`
(`calibration_long_model_reproduces_the_committed_trace_witness`,
`calibration_reproduces_the_published_mixed_ratio`): they check the probe
against COMMITTED grouped-era witnesses and published values, so they are
frame-bound by construction, exactly like the calibration that made
`qbeta_delta_vs_deltaTbeta_settled_probe` choose grouped deliberately
(2026-09-06, `qou-y2o7`).

## Status

The two probes stay in the grouped frame and are now DECLARED (bean
`qou-t29k`), with this measurement in their docstrings. That is the same
disposition as their settled sibling and it is well-evidenced rather than
inherited: their findings do not depend on the frame, and their calibration
legs require it.

**Open, and not mine to decide:** whether `Delta_L`'s `e_minus` being nonzero
in the canonical frame changes anything downstream of the fork. It is a new
exact closed form for a coordinate previously recorded as identically zero, and
`net` and `tr_M(z=1)` are no longer interchangeable on the long model. Nothing
in this session traced who relies on that.

## Progress Update (PR #8197 — `status: in-progress`)

- [x] Formalized pure Lean 4 module(s) (`QOU/MassTheory/BorromeanShadowCycleMerge.lean`, `QOU/MassTheory/SecondOrderContentCancellation.lean`, `QOU/Hecke/DeltaLongEMinusOrderingSplit.lean`, `QOU/MassTheory/LoopValueNormaliserAndFrameDiff.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` + exact rational probe `computations/probes/borromean_shadow_c2_deltal_loop_frame_probe.py` and 2-commit stamped witness `computations/probes/borromean-shadow-c2-deltal-loop-frame-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8197](https://github.com/litlfred/qou/pull/8197) (`ready: 4a2ed9a21b68b7d23b2e693b68f472d7dcf102a6`).
