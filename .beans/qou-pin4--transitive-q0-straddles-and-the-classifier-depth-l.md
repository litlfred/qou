---
# qou-pin4
title: 'Transitive q0 straddles: 3 producers pull BOTH layers via different helpers, invisible to a file-local scan (+ 27 cross-layer fallbacks)'
status: completed
type: task
priority: normal
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

`computations/audits/q0_cross_layer_fallback_scan.py` (new) finds **31** files
(pre-fix) where a **muon literal sits inside an `except` handler** in a file
that also reaches for a proton accessor — so on any import hiccup the producer computes at
the ideal pin under proton labelling, with nothing signalling the switch.

Two were fixed (`t25_cinquefoil_deltalambda_sign_probe`, `zhabiro_phiq_wiring`)
by raising instead of substituting, and the scan confirms neither is still
flagged. **29 remain.** (An earlier note here said 27 — that was a miscount: the
29 was measured *after* the two fixes had already landed, so the pre-fix total
was 31, not 29.) Each needs a one-line judgement — is the bare-environment path
load-bearing? — so they were not swept.

The scan deliberately requires the literal to be *in a handler* **and** a proton
accessor to be present: ~315 files contain the muon literal and most are
legitimate (muon-declared producers, explicit comparison probes per the owner
ruling, `_deprecated/`). Flagging on the literal alone is noise.

Run `python3 computations/audits/q0_cross_layer_fallback_scan.py --strict` to
gate this class in CI once the 27 are triaged.


## RESOLVED 2026-08-08 — and TWO OF MY THREE FLAGS WERE FALSE POSITIVES

I predicted `_li_2_q_util` might make the phase5c defect "not a one-off". It is
much narrower than that, and my own flagging was too coarse. Recorded because
the correction is the useful part.

### `_li_2_q_util` measured, not assumed

It is imported by **114** files, which is what made it look alarming. But
importing it is not the hazard -- most callers take pure math functions
(`li_2_q`, `flavor_split_leading/subleading`) that carry **no q_0 at all**.

The hazard is exactly one function: `load_q_50dps(path=None)`, whose default
path is the **muon** `q-pinning-50-digit.witness.json`. Measured:

    references to load_q_50dps        62
    no-arg calls (=> muon default)    27
    calls with an explicit path        0
    of the 27, ALSO pulling a proton q_0    1

So 26 of 27 use the muon q_0 *consistently* -- internally coherent, not
straddles.

### My three "transitive straddles": 1 real, 2 false

| flagged | verdict |
|---|---|
| `interface_factor_enhancing_check_probe` | **FALSE** -- imports `flavor_split_subleading`, a pure function. No q_0. |
| `probe_9b_gate_interface_algebra` | **FALSE** -- imports `flavor_split_leading`, a pure function. No q_0. |
| `delta_lambda_v_hat_z_transfer_phase5d_4` | **REAL** -- fixed below |

A fourth candidate surfaced by the wider scan, `fr_pullback_borromean_h3a_test`,
is **also NOT a defect**: it takes q_0 from the witness deliberately and imports
the runtime proton value marked `# drift measurement only`, with the docstring
saying the computation uses the witness q_0 "NOT" the runtime one. That is an
explicit comparison probe -- the class the owner ruled OK.

**The lesson:** "imports a muon-classified helper" is far too coarse a test. It
must be "calls a q_0-*returning* function from that helper". My depth-1
transitive check did not distinguish the two, and 2 of 3 flags were wrong.

### The one real fix

`delta_lambda_v_hat_z_transfer_phase5d_4` called `load_q_50dps()` (muon) and
applied the resulting `q, h, z` to V̂ values from
`per_generator_V_hat_3A` -- which takes **no q argument** and binds its own q_0
at module level from `q_parameter`, resolving **proton**. So muon q/h/z met
proton-computed V̂ inside one quantity, and the witness recorded the muon q_0
as this producer's own. Exactly the phase5c shape.

Fixed by taking q_0 from the same place the V̂ side takes it, so the pair is
single-layer by construction. Then declared `physical_proton` (inert) so the
stamp matches the computation: witness now reads `proton`.

**Effect:** `allPassed` was False BEFORE and after -- not a regression. The
assertion `interface_v_hat_flavor_selective_rule` **improved**: computed
0.0 -> 2.0 against expected 5.0. The straddle had been suppressing the signal
entirely; de-straddled, 2 of 5 interfaces match. Same pattern as phase5c, where
removing the mix restored an exact identity.

### Still open

The **29 cross-layer fallbacks** (section 3 above) are untouched and remain the
live item here. `load_q_50dps`'s muon default is arguably the same hazard in
library form -- a q_0-returning helper whose default is the ideal layer, in a
corpus whose production default is proton. Worth considering making the `path`
argument required.
