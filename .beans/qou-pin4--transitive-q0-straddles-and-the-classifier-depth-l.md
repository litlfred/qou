---
# qou-pin4
title: 'Transitive q0 straddles: 3 producers pull BOTH layers via different helpers, invisible to a file-local scan (+ 27 cross-layer fallbacks)'
status: todo
type: task
priority: high
created_at: 2026-08-08T20:40:00Z
updated_at: 2026-08-08T20:40:00Z
---

Two findings from the 2026-08-08 `qou-pin2` work, both of which say the same
thing: **a file-local scan under-detects q₀ layer mixing.**

## 1. Transitive straddles (HIGH — same class as the fixed phase5c defect)

Three producers classify as `none` (no q₀ in their own file) yet reach **both
layers through different local imports**:

| producer | proton via | muon via |
|---|---|---|
| `interface_factor_enhancing_check_probe.py` | `closed_form_tau_M` | `_li_2_q_util` |
| `probe_9b_gate_interface_algebra.py` | `closed_form_tau_M` | `_li_2_q_util` |
| `delta_lambda_v_hat_z_transfer_phase5d_4.py` | `mass_at_3A_proper` | `_li_2_q_util` |

This is the **same defect** as `delta_lambda_fr_identity_phase5c` (fixed
2026-08-08), one level deeper. There, mixing muon-built `y_λ` with
proton-evaluated `χ_λ` injected a ~1e-8 error into an *exact* identity —
the Markov-interface residual ran at 9.0e-08 and dropped to 1.2e-15 once the
layers were unified. A 7.6-million-fold improvement in a quantity that should
have been machine-zero all along.

If any of these three combines its two layers inside one computed quantity, it
carries the same silent ~11.5 ppb contamination. **Check each the way phase5c
was checked**: find where the proton-derived and muon-derived values meet, and
whether they meet inside a single number.

Note `_li_2_q_util` appears in all three — start there. If it is muon-pinned and
widely imported, the blast radius is larger than these three.

## 2. My "spurious pins on symbolic producers" hypothesis was WRONG

I expected ~13 producers carrying a q₀ pin on a purely symbolic artifact (the
`chi-deuteron-h6` / `qou-pin1` shape) and intended to drop those pins.

A depth-1 transitive check found **0 of 13 clean** — every one reaches a q₀
through a local import. So none of those pins is spurious, and dropping them
would have destroyed 13 correct labels. Recorded because the negative is the
useful part: `chi-deuteron-h6` was genuinely symbolic *all the way down*
(verified by hand), and that turns out to be the exception, not a pattern.

**Consequence for `q0_producer_pin_classifier.py`:** its `none` verdict means
"no q₀ **in this file**", not "no q₀". The docstring says proposals are
conservative for exactly this reason, and the conservatism held — nothing was
mis-proposed — but the `none` bucket should not be read as "symbolic".
Worth adding a depth-1 transitive pass so `none` means what a reader assumes.

## 3. 27 remaining cross-layer fallbacks

`computations/audits/q0_cross_layer_fallback_scan.py` (new) finds **29** files
where a **muon literal sits inside an `except` handler** in a file that also
reaches for a proton accessor — so on any import hiccup the producer computes at
the ideal pin under proton labelling, with nothing signalling the switch.

Two were fixed (`t25_cinquefoil_deltalambda_sign_probe`, `zhabiro_phiq_wiring`)
by raising instead of substituting. **27 remain.** Each needs a one-line
judgement — is the bare-environment path load-bearing? — so they were not swept.

The scan deliberately requires the literal to be *in a handler* **and** a proton
accessor to be present: ~315 files contain the muon literal and most are
legitimate (muon-declared producers, explicit comparison probes per the owner
ruling, `_deprecated/`). Flagging on the literal alone is noise.

Run `python3 computations/audits/q0_cross_layer_fallback_scan.py --strict` to
gate this class in CI once the 27 are triaged.
