---
# qou-j3u0
title: 'GAP: keystone-qdeform-projector-shift witness contradicts its own producer at the SAME pin'
status: todo
type: task
priority: normal
created_at: 2026-08-30T12:44:54Z
updated_at: 2026-08-30T12:45:29Z
---

## The disagreement, measured AT THE WITNESS'S OWN PIN

`computations/keystone-qdeform-projector-shift.witness.json` records `q0 =
1.1099785955541805` (B). Running its named producer
`docs/audits/scripts/keystone_qdeform_projector_shift_probe.py` **pinned to that
same B**:

| field | witness | producer at B | |
|---|---|---|---|
| `projected_traces/T_muon_3_2` | 0.30790082984625 | 0.30507007447976 | −0.93 % |
| `projected_traces/T_electron_3_1_1` | 0.10040468526556 | 1.6489690183772e-17 | **16 orders of magnitude** |
| `projected_traces/delta` | 0.20749614458069 | 0.30507007447976 | +47 % |
| `bar_parity/diff` | −0.157998 | −7.7663258e-17 | nonzero → zero |

**The pin is ruled out, not assumed away:** this control run uses the witness's
own value of q₀, so an 11.5 ppb difference cannot be the cause. The proton run
gives the same picture (T_electron 6.55e-17, δ 0.30507007626091), which is what
an 11.5 ppb move off the control looks like — the two live runs agree with each
other to ~1e-8 and both disagree with the witness by orders of magnitude.

## The conclusion flips, not just the numbers

The probe's bar-parity verdict is decided by whether `δ(q) − δ(1/q)` is ≈ 0. The
witness records **−0.157998**; the producer computes **−7.8e-17** and prints
*"(≈0 ⟹ bar-EVEN)"*. On the witness's numbers that test does not pass. So this
is not a stale figure — it is a **recorded conclusion the current code
contradicts**.

## Which one is right is NOT established here

Scope (a). Either the producer changed after the witness was written (the
witness is a superseded computation), or the witness was transcribed from a
different run/quantity. `T_electron` collapsing to ~1e-17 means the projected
(3,1,1) trace of the Borromean braid is now numerically zero, which is a
substantive structural claim in its own right and wants checking before either
number is trusted.

**Nothing about this witness has a staleness signal.** It carries no
`scriptHash`, no `scriptFile`, no `q0Anchor` (bean `qou-bake`: it is
hand-written, and no script emits it), so no audit in the corpus can detect the
disagreement. It was found only by running the producer by hand.

## NOT a systemic failure of the five

`keystone-wrt-color-schurweyl` was checked the same way and **reproduces
faithfully** at B — all four Ψ̃ components and the sum match to the recorded
digits, with one field recorded at 13 significant figures where the probe prints
14 (`0.04796281223285` vs `0.047962812232851`), a truncation and not an error.
So the hand-written route is not inherently unreliable; this specific witness is
wrong or superseded.

Two of the five (`schurweyl-dual-sides`, `schurweyl-su2-rowcount`) carry a
single number each and reproduced. `habiro-wrt-s3-2i` has one number
(`10.4959110098`) not located in its output by a string scan — **not
investigated**, and that scan over-reports (it compares different precisions),
so treat it as unchecked rather than as a finding.
