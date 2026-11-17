---
# qou-j3u0
title: 'GAP: keystone-qdeform-projector-shift witness contradicts its own producer at the SAME pin'
status: in-progress
pr: 8189
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:44:54Z
updated_at: 2026-10-04T15:20:07Z
parent: qou-9nnz
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


## SECOND INSTANCE, same mechanism — `keystone_branching_shift_probe.py` (2026-08-30)

The `trace_weights_n` float64 leak is **not unique to the qdeform probe**. Audit
of every caller found the same defect in `keystone_branching_shift_probe.py`,
where it is the probe's **headline quantity**:

    y5 = dict(zip(..., ph.trace_weights_n(5, Q0)))
    y_mu, y_el = y5[(3, 2)], y5[(3, 1, 1)]
    r = y_mu / y_el                      # <-- divides by an EXACT ZERO

The old output was **self-contradictory on its face**: it printed

    y_(3,1,1)^H5 = 0.000000000000
    ratio r      = 5587920869536671.000000000000

— a finite ratio obtained by dividing 0.0611562 by a printed zero. 5.59e15 is
exactly `0.0611562 / 1.09e-17`, the float64 noise floor.

**Fixed** the same way: exact route + a tolerance guard, and Model B now reports
**UNDEFINED** instead of a fabricated magnitude.

**A second-order trap found while fixing it.** The first fix used
`mpf(str(Q0))`, and y_(3,1,1) came out at **4.63291310128e-52** rather than 0 —
because this probe's `Q0` is `q_parameter.Q`, a **float64**. Feeding its
17-digit decimal into a 50-dps computation lands on the dps=50 floor for a
float64-accurate q, not on the exact zero. Using `Q_50_DIGIT_STR` gives exactly
0. So *"use mpmath"* is not sufficient — **the INPUT must be full-precision
too**, or you have merely moved the floor from 1e-17 to 1e-52. The guard is a
tolerance (1e-30) rather than `== 0` for exactly this reason.

**Stale verdict flagged, not rewritten.** The probe's structural verdict item 3
calls Model B a *"well-posed object ~1e0"*. Model B does not exist. Note it was
**already contradicted before the fix** — the float64 route printed 5.59e15, not
~1e0 — so this is a pre-existing defect in the prose, not one the fix created.
The probe now prints a banner saying so; whether the verdict survives with Model
B removed is the author's judgement.

## The other callers — measured, and they are NOT all defects

- `keystone_h3_h5_lift_block_shift.py` — passes q to `trace_weights_n` and its
  own comment says *"expect ~1e-16 ... y_lambda are f64-internal"*. It sets its
  tolerance **to** the float64 floor knowingly. That is a scope limitation
  honestly stated, not a laundered number: its cross-check simply cannot resolve
  below 1e-16.
- `computations/atom_vhyp_bar_trace_test.py` — `float(q)` with the comment
  *"native y_λ wants a float q"*, then sums `y*chi`. The zero blocks contribute
  noise to a sum dominated by nonzero terms; lower severity, not chased here.
- `computations/pyhecke_n_generic.py` — declares `q: float = Q0_F64` and returns
  `list[float]`. Float64 **by design and by signature**; the defect is never the
  routine, it is a caller treating its output as high precision.

So the rule to carry forward: `trace_weights_n` is a float64 API. Any caller
that divides by one of its outputs, compares one to zero, or records one in a
witness at high precision has a defect — and there were **two**.


## Q1/Q2/Q3 ANSWERED 2026-08-30 (owner picked all three)

### The context that reframes it: the corpus ALREADY has this rule

`docs/audits/2026-06-22-keystone-schurweyl-su2-rowcount.md` states the theorem
and its consequence: SU(2) Schur-Weyl admits only **≤2-row** partitions, so muon
(3,2) is spin-reachable and electron (3,1,1) is **not** — it is an SU(3)-colour
object. `y_(3,1,1) = 0` is that same theorem showing up in the Jones-Markov
weights, not a defect in the physics.

### Two weight families, and the probes used the wrong one

| λ | rows | `y_λ` (SU(2) Markov) | `W_λ` (keystone `d_q²/[n]_q!`) |
|---|---|---|---|
| (5,) | 1 | 0.194277187378 | 0.00761538731 |
| (4,1) | 2 | 0.124985397168 | 0.12862000420 |
| (3,2) μ | 2 | 0.061156244790 | 0.20754220450 |
| (3,1,1) e | 3 | **0** | **0.29466895630** |
| (2,2,1) | 3 | **0** | 0.20754220450 |
| (2,1,1,1) | 4 | **0** | 0.12862000420 |
| (1⁵) | 5 | **0** | 0.00761538731 |

`W_λ` is conjugation-symmetric (the Lean-proved **C2** — verified exactly:
W_(3,2) == W_(2,2,1)) and reproduces the canonical table to 5 dp. `y_λ` has
neither property. **Q1 answered: yes, W_λ is the right weight** — it is what
C1/C2/C6 are stated over.

### Q2 — the "exhausted" claim: ONE LEG SURVIVES, ONE FAILS

Re-derived in `computations/probes/keystone_wlambda_vs_ylambda_projected_shift.py`:

    T_muon     = W_(3,2)   * chi^(3,2)   = 0.207542204506 * 4.9883716259599 = 1.0352976441462
    T_electron = W_(3,1,1) * chi^(3,1,1) = 0.294668956300 * 5.9883716259599 = 1.7645872169611
    delta = -0.72928957281492     delta/T_mu = -0.7044250288

- **leg (a) "6-7 orders too large" — SURVIVES.** |δ/T_μ| / 210 ppb = **3.3544e6×**.
- **leg (b) "bar-mixed, fails bar-even" — FAILS.** δ(q) − δ(1/q) = **4.0091471e-50**
  at dps=50: the shift is **exactly bar-EVEN**. The "bar-mixed" reading came from
  the float64-corrupted witness numbers.

**Consequence in the corpus's own vocabulary.** "Too large by 6.5 orders" is a
**scope-(a)** negative. "The Markov-trace surface is exhausted; any surviving
q-closure must leave the trace-weighting **entirely**" is a **scope-(b)**
structural exclusion — and it rested on the refuted parity leg. The route is
**not foreclosed**; it is wrongly-scaled, which is weaker and different.
**Nothing here claims the trace-weighting route works.**

### Q3 — both audit docs now carry the corrected numbers

Banners extended with the `W_λ` table, δ, and both legs' verdicts. The original
`y_λ` figures stay as the historical record (`qou-3nva`); the correction sits
above them rather than replacing them. `docs/coordination/s5-so3-keystone.md`
row for #2584 corrected in place — it is a live ledger, not a dated audit.

### Unresolved, flagged not chased

The ledger elsewhere records "consumer weight `y_(3,2)/y_(3,1,1) = 3.68` at q₀"
(#2520). That matches **none** of the candidates measured here: W_μ/W_e = 0.7043,
W_e/W_μ = 1.4198, d_q ratios 0.8392 / 1.1916. A **fourth** value for the same
named ratio; provenance unknown, not chased.


## Round 52 Progress
- [x] PR https://github.com/litlfred/qou/pull/8189 (`523155d5604cc384f307eb1cb22785f1fded85da`): wired `WitnessBuilder.wrap_legacy` with 3 checkable assertions into `docs/audits/scripts/keystone_qdeform_projector_shift_probe.py` and regenerated `computations/keystone-qdeform-projector-shift.witness.json` (`allPassed: true`, 0 raw float64).
