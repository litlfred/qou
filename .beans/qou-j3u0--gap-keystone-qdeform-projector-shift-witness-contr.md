---
# qou-j3u0
title: 'GAP: keystone-qdeform-projector-shift witness contradicts its own producer at the SAME pin'
status: todo
type: task
priority: normal
created_at: 2026-08-30T12:44:54Z
updated_at: 2026-08-30T12:59:45Z
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


## RESOLVED 2026-08-30 — the witness is wrong, and the mechanism is a float64 leak

The disagreement is not between two defensible computations. **`y_(3,1,1)^{H5}`
is EXACTLY ZERO**, so `T_electron = 0` and the live producer was right.

**Mechanism**, at `weights5()` in the producer:

    ws = ph.trace_weights_n(5, float(q))        # 50-dps pin -> 53 bits
    return {p: mpf(str(w)) ...}                 # 53-bit data dressed as 50 dps

`trace_weights_n` is float64 internally — it returns a Python float even when
handed an mpf — so the whole weight vector resolved at the float64 floor.
Measured, float64 route vs exact (`y_lambda_wenzl_bridge_numeric`):

    lambda        float64                exact
    (5,)          0.19427718737799       0.19427718737799
    (4,1)         0.12498539716795       0.12498539716795
    (3,2)         0.061156244790044      0.061156244790044
    (3,1,1)       1.094436485732e-17     0
    (2,2,1)       1.9631309013882e-17    0
    (2,1,1,1)     -3.2754415082272e-17   0
    (1,1,1,1,1)   3.5151413120942e-18    0

**The zeros are structural, not numerical:** `y_λ = 0` exactly iff λ has **more
than two rows** — the SU(2)/N=2 truncation. (5,), (4,1), (3,2) have ≤ 2 rows and
survive; every deeper partition is killed. Perfect correlation across all seven.

**Independent confirmation the leak was real:** with the exact route the
bar-parity residual sharpens **5.5e-17 → 7.14e-42**, and the (3,1,1) branching
cross-check goes to exactly 0.0. Those are 50-dps numbers; the old ones were the
float64 floor.

## FIXED in the producer

`weights5()` now uses `y_lambda_wenzl_bridge_numeric`. `delta / T_e` was
`4.65e+15`, which was δ divided by the noise floor — a statement about the
arithmetic, not the traces; it now reports **UNDEFINED (T_e is exactly 0)**
rather than a fabricated magnitude, in both places it was printed.

## What this does to the probe's PREMISE — scope (a), author's call

The probe exists to compare a "muon home-block (3,2)" against an "electron
home-block (3,1,1)". With `y_(3,1,1) = 0` structurally, **that comparison is
vacuous on one side**: δ = T_μ − 0 = T_μ, and the probe's own `δ/T_μ = 1.0`
exactly says so. The whole measured quantity is T_μ under another name.

Not fixed here — whether the probe should compare different blocks, or whether
the (3,1,1) "home block" idea survives the SU(2) truncation at all, is a
question about what the probe is for.

## Contamination — 2 docs, annotated not rewritten

`y_(3,1,1) = 0.0167666` reached
`docs/audits/2026-06-22-keystone-qdeform-projector-shift.md` and
`docs/audits/2026-06-20-keystone-branching-shift-first-crack.md`. Both now carry
a correction banner; their numbers are **left as the historical record**, per the
standing `qou-3nva` decision on dated audit docs. The committed witness is
likewise left — it has no producer to regenerate it (`qou-bake`).
