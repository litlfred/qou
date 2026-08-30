---
# qou-3hre
title: phase-transition assertion name claims gap ratio ~6-10x but the script computes 4.26-6.45x
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:45:18Z
updated_at: 2026-08-30T09:51:04Z
---


## The measurement

`computations/phase_transition_q_ideal_gas.py` computes boil gap ratios and
then reports a band that does not contain them.

| material | T_boil pred | obs | gap ratio |
|---|---|---|---|
| H2O | 2405.0 K | 373.1 K | **6.45x** |
| HF  | 1477.0 K | 293.1 K | **5.04x** |
| NH3 | 1022.1 K | 239.8 K | **4.26x** |

Measured range **4.26–6.45x**. Only H2O falls inside the claimed 6–10x, and
nothing anywhere near 10x exists — the melt ratios are lower still (1.38x,
2.56x, 1.72x).

## It is stated in three places, all wrong the same way

1. the assertion name — `"Direct substitution of [2]_q yields gap ratio
   ~6-10x"`;
2. `set_description(...)` — "over-predicts the temperatures by a factor of
   6.4x to 10x";
3. `add_data("finding", ...)` — "over-predicts T_boil and T_melt by 6-10x".

## Why it survived

The assertion was `computed=True, expected=True` — a literal on both sides
(bean `qou-26f2`), so no value of any ratio could contradict it. The band
lived only in prose that nothing checked. Draining the constant is what
surfaced it: the first falsifiable form of the claim failed immediately, 1 of
3 in band.

## Not resolved here — deliberately

Widening the band to fit the observation is exactly the move this file's own
header forbids ("NO fitted scales are used to force the temperatures"). And
which of the two is wrong is an author call:

* the **band** is a stale number and the model is behaving as expected, in
  which case all three sites want correcting to 4.26–6.45x; or
* the **model** has drifted since the band was written — `Q0` now comes from
  `q_at()` rather than a hardcoded literal (see the excised fallback in the
  same file), so the ratios may genuinely have moved.

The second is worth checking before the first: this file's history shows a
`Q0 = 1.1099780333553254` literal was removed for sitting ~500 ppb from either
pin, and the recorded band may predate that fix.

What this branch asserts instead is the over-prediction finding itself — every
ratio > 1, counted — which is what the probe actually establishes and still
fails if the geometric mapping ever starts working.

## RESOLVED 2026-08-30 — the band was wrong when written, not stale

The bean posed two candidates and said the second was worth checking first:
the band is stale, or the model drifted since it was written. Both were
tested; **neither is "the model drifted"**.

**q₀ is not the explanation.** This file's history includes the excision of a
hardcoded `Q0 = 1.1099780333553254`, removed for sitting ~495 ppb from the
proton pin, and the bean flagged that the band might predate that fix.
Computing the ratios at both values:

    excised literal 1.1099780333553254 : H2O 6.44x  HF 5.04x  NH3 4.26x
    current q_at()  1.1099785827513808 : H2O 6.45x  HF 5.04x  NH3 4.26x

A 495 ppb shift in q₀ moves these ratios by 0.01x. One of three sits in
"6-10x" either way.

**The inputs are not the explanation either.** `git log -p --follow` shows
`MOLECULES` and the cohesion formula introduced once and never modified since.
Every later commit touching this file is the float64 excision
(`874431aeba0`), the q₀ fallback hardening (`3d726190c31`), the mpf-source
refresh (`ebc21d1ae73`), or the `qou-26f2` drain.

So the computation has produced 4.26-6.45x for its whole recorded history, and
the "6-10x" in the prose never described it.

## What was corrected, and why it is not a fit

All three sites now carry the measured range:

* the assertion — already replaced during the drain by the over-prediction
  claim, which is true and falsifiable (3 of 3 ratios > 1);
* `set_description` — "6.4x to 10x" -> "4.26x to 6.45x (H2O 6.45, HF 5.04,
  NH3 4.26)", and the melt band added at 1.38-2.56x, which was never stated;
* `add_data("finding", ...)` — same correction.

The bean held this back as an author call because widening a band to fit an
observation is exactly what this file's "NO fitted scales" header forbids.
That concern was right about *fitting the model*, and does not apply to
*correcting a description*: nothing in the model was adjusted, and the numbers
being described did not change. The direction matters — the prose was moved to
the computation, not the computation to the prose.

`boil_ratio_range` in the witness records `previously_claimed_band: "6-10x"`
so the correction is visible in the artefact rather than only in git.
