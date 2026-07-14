# Deuteron-ladder falsification test of the "resonance at k = A_light" reading — R10

**Date:** 2026-07-14 · **Task:** R10 (follows R9) · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/deuteron_ladder_falsification_probe.py`](../../computations/deltalambda/deuteron_ladder_falsification_probe.py)
· **Witness:** [`deuteron-ladder-falsification.witness.json`](../../computations/deltalambda/deuteron-ladder-falsification.witness.json)
(allPassed: true, 8/8; witness-fed — `b` and the Model-G ledger reused from
the committed R5-a/Model-G witnesses, ¹⁴N miss reproduced from the committed
row to `0.0` MeV, only the fresh ¹⁰B/¹⁸F/¹³C/¹⁷O AME deficits read from
vendored AME2020; **no fitted constant** — this is a falsification test, not a fit)
**Discipline:** falsification (`compute-author.md` §3.3) — the prediction and
its null were pre-registered in R9 §6 (item 3) and restated in the probe
docstring **before** the fresh ¹⁰B/¹⁸F compute.

## 1. Pre-registered prediction (from R9 §6, item 3)

R9 read the t-ladder interior maximum at k=3 as a **resonance at
k = A_light** — the miss peaks where the α count matches the triton's nucleon
count (A_light = 3). The falsifiable consequence, stated in R9's next-steps:

> Repeat the ladder with the deuteron (A_light = 2; ⁶Li k=1, ¹⁴N k=3) to test
> whether the peak tracks k = A_light (**predict a peak at k=2 for the
> d-ladder**).

- **RESONANCE PREDICTION** (k = A_light = 2): the deuteron ladder peaks at
  **k=2** (¹⁰B): miss(¹⁰B) > miss(¹⁴N) > miss(¹⁸F).
- **NULL / FALSIFIER**: the deuteron ladder peaks at **k=3** (¹⁴N) *again* —
  the same k as the triton ladder — ⇒ the peak is a **fixed-k=3 effect** (the
  3-α Brunnian onset, i.e. the k≥3 α·α gate turn-on), independent of A_light.

The deuteron ladder = (k α)+d, A_light = 2: ⁶Li (k=1, α+d), ¹⁰B (k=2, 2α+d),
¹⁴N (k=3, 3α+d), ¹⁸F (k=4, 4α+d). Only ¹⁴N (and ⁶Li) were already in the
committed data; ¹⁰B and ¹⁸F are computed fresh with the **same** Model-G ledger.

## 2. Result — the deuteron ladder peaks at k=3, NOT k=2

Model-G miss = deficit − pred, pred = `3b·C(k,2)·[k≥3] + k·A_light·b`,
`b = 0.78192` MeV/nucleon (committed, reused):

| k | iso | pieces | miss (MeV) | note |
|--:|---|---|--:|---|
| 1 | ⁶Li | α+d | −0.090 | closed (committed; ≈ 0, +0.28% B) |
| 2 | ¹⁰B | 2α+d | **2.807** | fresh — resonance predicted the **peak** here |
| 3 | ¹⁴N | 3α+d | **5.818** | committed (R8; reproduced to 0.0 MeV) — **actual peak** |
| 4 | ¹⁸F | 4α+d | 1.632 | fresh |

The miss **rises** 1→2→3 then **falls** 3→4, a strict interior maximum at
**k=3 (¹⁴N)**. The resonance prediction (peak at k=A_light=2) is **FALSIFIED**:
¹⁴N (5.818) > ¹⁰B (2.807), the opposite of the predicted ordering.

## 3. Two-ladder cross-table (the decisive comparison)

| k | d-ladder (A_light=2) | miss | | t-ladder (A_light=3) | miss |
|--:|---|--:|:-:|---|--:|
| 1 | ⁶Li | −0.090 | | ⁷Li | 0.122 |
| 2 | ¹⁰B | 2.807 | | ¹¹B | 6.440 |
| 3 | ¹⁴N | **5.818** ★ | | ¹⁵N | **8.048** ★ |
| 4 | ¹⁸F | 1.632 | | ¹⁹F | 2.679 |

★ = peak. **Both ladders peak at k=3.** The peak location does **not** move
from k=3 to k=2 when A_light drops from 3 to 2. The peak does not track
A_light — it is fixed at k=3.

## 4. Triangulation — the neutron ladder (A_light=1) also peaks at k=3

Third A_light value, (k α)+n, A_light = 1 (k=1 ⁵He is unbound; start at k=2):

| k | iso | miss (MeV) |
|--:|---|--:|
| 2 | ⁹Be | 0.009 (closed) |
| 3 | ¹³C | **2.838** ★ |
| 4 | ¹⁷O | 1.377 |

Peak at **k=3 (¹³C)** again. This is the strongest triangulation point: for
A_light = 1 the R9 resonance shape `S(k) = (k−1)(2·A_light−1−k) = −(k−1)²` is
**degenerate** (≤ 0, no positive interior peak), so resonance predicts *no*
peak here — yet the miss shows a clean k=3 maximum. A third independent
falsifier.

**Three ladders, three A_light values (1, 2, 3), one peak location — k=3.**

## 5. What A_light actually controls — amplitude, not location

The peak k=3 heights across the three ladders:

| A_light | iso (k=3) | peak miss (MeV) |
|--:|---|--:|
| 1 | ¹³C | 2.838 |
| 2 | ¹⁴N | 5.818 |
| 3 | ¹⁵N | 8.048 |

The peak **location** is fixed at k=3 (the 3-α onset); the peak **amplitude**
grows monotonically with A_light (≈ 2.8, 5.8, 8.0 MeV for A_light = 1, 2, 3 —
roughly ∝ A_light). The correct decomposition of the shared-channel miss is
therefore

> (a **fixed** envelope in k, peaked at the 3-α Brunnian onset k=3)
> × (an **amplitude** that scales with A_light),

**not** a resonance whose peak location tracks A_light. The interior maximum
is the signature of the α·α gate switching on at k=3 (Model G's k≥3
activation), re-weighted by how large the shared light cluster is.

## 6. Honest classification

**FALSIFIED (scope-(a) correction of R9's *interpretation* only).**

- The "resonance at k = A_light" reading (R9 §3 candidate (c), R9 §5, R9 §6
  item 3) is **refuted**: the peak is fixed at k=3 across A_light ∈ {1, 2, 3},
  it does not track A_light. This corrects R9's forward-reading; an erratum
  note has been added to the R9 audit.
- **R9's structural prunes P1 and P2 STAND** — they were not under test here.
  P1 (additive non-negative counting cone excluded) and P2 (monotone-saturating
  1−∏ idempotent class excluded) both rest on the **interior-maximum
  invariant** `0 ≈ M(1) < M(2) < M(3) > M(4)`, which holds — indeed is
  *strengthened* — on all three ladders (each rises to k=3 then falls). The
  surviving class is still genuinely non-monotone; only its *seed* changes from
  "resonance matched to A_light" to "fixed 3-α onset × A_light amplitude".
- **Nothing derived, nothing wired.** This is a falsification test, not a fit:
  `b` and the ledger reused from committed witnesses; only the fresh ¹⁰B / ¹⁸F
  / ¹³C / ¹⁷O AME deficits read. No tier change; no production wiring.

**Net.** The R9 turnover is real and its class-prune survives, but its
mechanistic label was wrong. The shared-channel closure target sharpens to
**(fixed 3-α-onset envelope in k) × (A_light-scaled amplitude) × (bar-parity
fall)** — replacing "(resonance at k=A_light) × (bar-parity fall)". The next
object to derive is the *fixed* k-envelope peaked at the α·α gate onset (k=3),
not a k=A_light resonance.

## 7. Next steps (named, not run)

1. **Derive the fixed k=3 envelope.** The peak sits exactly at the Model-G
   k≥3 α·α gate turn-on. Formalize-first target: does the Brunnian/Milnor
   onset (μ̄ triple activation at k=3) predict a miss *envelope* peaked at k=3
   with the observed k=2→3 rise / k=3→4 fall, independent of the light
   cluster?
2. **Derive the A_light amplitude law.** The k=3 heights (2.84 / 5.82 / 8.05
   for A_light = 1 / 2 / 3) are the clean amplitude datum — test whether they
   follow a per-nucleon shared-channel law (≈ 2.9·A_light? sub-linear?) before
   inventing a scale.
3. **Bar-parity fall (unchanged from R9 §6.2).** The descending k>3 side is
   still asymmetric; the even-sublattice / odd-Z pairing route is unchanged by
   this correction.

## Provenance

Inputs: committed
[`alpha-activation-brunnian.witness.json`](../../computations/deltalambda/alpha-activation-brunnian.witness.json)
(Model-G ledger + `b`; ⁶Li/¹⁴N/⁹Be misses reused, ¹⁴N reproduced to 0.0 MeV),
committed
[`saturating-shared-channel.witness.json`](../../computations/deltalambda/saturating-shared-channel.witness.json)
(R9 — the resonance reading under test), vendored AME2020
(`_ame_binding_mev`, ¹⁰B/¹⁸F/¹³C/¹⁷O deficits only). Companions:
[R9 saturating shared-channel](2026-07-14-saturating-shared-channel-derive-or-refute.md)
(erratum added), [R8 mixed multi-bond](2026-07-14-mixed-multibond-interface-derive-or-refute.md),
[Model G consolidated record](2026-07-14-model-g-consolidated-record.md).
EXPLORATORY — audit + witness only; no production wiring; no fitted constant.
Render-QA: pipeline render unavailable in this sandbox; the manual grep
battery (balanced `$`/`$$`/`{}`/`\begin`-`\end`; no `\operatorname`; no
list-hijack lines in display math; align-family fenced) was run by hand — not
machine-validated.
