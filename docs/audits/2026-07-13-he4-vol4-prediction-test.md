# ⁴He `Vol₄ = 8.05` falsifiable prediction test — executed (exact back-out + SnapPy + guarded census)

**Date:** 2026-07-13 · **Task:** R2-b (cheat-sheet 9b open item "⁴He `Vol₄=8.05`
falsifiable prediction") · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/he4_vol4_prediction_test_probe.py`](../../computations/deltalambda/he4_vol4_prediction_test_probe.py)
· **Witness:** [`he4-vol4-prediction-test.witness.json`](../../computations/deltalambda/he4-vol4-prediction-test.witness.json)
(allPassed: true) · **Companion (same day, this branch):**
[`vol4_4he_snappy_falsification_probe.py`](../../computations/deltalambda/vol4_4he_snappy_falsification_probe.py)
(pre-registered candidate list + first execution, commit `784c6f9d`).

## 1. What the prediction precisely means (provenance)

The bond-count binding tower
([`2026-07-04-theta-mn-bondcount-derived-linearchain.md`](2026-07-04-theta-mn-bondcount-derived-linearchain.md),
`prop:linear-chain-bond-count`, multiplicity `M_n = (n−1)` Lean-proved sorry-free
in `QOU/Mass/LinearChainBondCount.lean`) is

`B(K) = m_e · Σ_{n=2}^{A} Σ_{consecutive n-clusters c} (n−1) · Vol(c)`,

with `Vol(c)` the hyperbolic volume of the n-nucleon sub-chain's link (isospin
carrier: `ppn → L6a4`, `pnn → 8₁₁`, any 2-chain → Hopf, `Vol = 0`, KMM
convention). For ⁴He (`ppnn` linear chain) every `n = 2, 3` volume is known, so
the tower **inverts**: the `n = 4` term is fixed by AME2020,

`Vol₄ = (B_AME(⁴He) − m_e·[2·Vol(L6a4) + 2·Vol(8₁₁)]) / (3·m_e)`.

So **`Vol₄` is the hyperbolic volume of the single 4-component link carried by
the full `ppnn` 4-chain** — the whole-chain sub-link at level `n = 4`, one bond
multiplicity 3, isospin-aware only through the `n = 3` sub-terms (the `n = 4`
term itself is a single volume; the linear-chain reading offers exactly one
4-cluster, so there is no isospin split at that level). The "8.05" of the
cheat-sheet is the 2026-07-04 back-out (`theta_mn_bondcount_linearchain.py`
prints 8.048 / "≈8.05"). The falsifiable test: does an actual, in-advance-named
4-component link have hyperbolic volume ≈ 8.048?

## 2. Corpus link-assignment status (scopes the verdict)

The corpus fixes **no derived ⁴He binding link**
([`2026-07-04-he4-vol4-gated-on-r5full.md`](2026-07-04-he4-vol4-gated-on-r5full.md)):
the canonical knot-ID is gated on the R5-full categorical SDP
(`conj:canonical-knot-id-sdp`, #604), and the A≤3 IDs (6₂/8₁₁/L6a4) are
themselves deprecated volume-search matches that the principled Markov-trace
test does not confirm. What *is* testable — without a census scan feeding the
verdict (anti-numerology) — is the naive structural reading "the `n=4` term is
the volume of the linear 4-chain closure", against candidates **named in
advance** by structural analogy (pre-registered in
`vol4_4he_snappy_falsification_probe.py`): L8n8 (4-component brunnian,
Borromean analogue), L8a21/L8a20 (linear 4-chain closures), L8a19
(4-component alternating), L8n7 (4-component non-alternating).

## 3. Probe numbers (this probe; SnapPy 3.3.2, validated vs corpus to 1e-11)

Exact back-out (mpmath at production dps; inputs: `m_e` = 0.51099895069 MeV
CODATA/CAL-1, `B_AME(⁴He)` = 28.2956624 MeV vendored AME2020,
`Vol(L6a4)` = 7.327724753417752, `Vol(8₁₁)` = 8.286316817806593 from
`binding-link-volumes.witness.json`):

| quantity | value |
|---|--:|
| n=2,3 contribution `m_e·2·(Vol(L6a4)+Vol(8₁₁))` | 15.9575 MeV (56.4% of AME) |
| residual (n=4 term) `= m_e·3·Vol₄` | 12.3381 MeV |
| **implied `Vol₄`** | **8.0484** (pre-registered 8.048, Δ = +0.0004 ✓) |
| model tolerance (±3% A=3-residual band on the n=3 term) | ±0.312 |

Pre-named candidates vs 8.0484:

| link | Vol (SnapPy) | Δ | role |
|---|--:|--:|---|
| L8n8 | ~0 (non-hyperbolic) | −8.05 | brunnian Borromean-analogue |
| L8a21 | 10.149416 | +2.10 (+26%) | **linear 4-chain closure** |
| L8a20 | 10.149416 | +2.10 | 4-chain variant |
| L8a19 | 10.666979 | +2.62 | 4-component alternating |
| L8n7 | 7.327725 | −0.72 | non-alt (= Vol(Borromean) exactly) |

**Guarded census datum** (non-evidential; quantifies what a post-hoc scan could
even find): scanning all 7463 4-component HT census links (≤14 crossings),
**zero** links lie within ±0.05 of 8.048 and only **2** within the ±0.312 model
band (nearest: L13n11075/L13n11059 at 8.3555, +0.31; L11n459-family at 7.7069,
−0.34). The implied volume falls in a **gap** of the ≤14-crossing 4-component
volume spectrum. (Guard: the HT census is not all links; this says nothing
about higher-crossing links, and matching one post-hoc would be a CAL-4 fit.)

## 4. Verdict (scope-classified per the refutation discipline)

**Two layers:**

1. **Not decisively testable as a model falsification** — the link assignment
   is the open model input (no corpus-derived ⁴He link; gate = R5-full SDP
   #604). A decisive test needs the SDP canonical knot-ID at H₁₂.
2. **Scope-(a) NEGATIVE for the pre-registered structural reading**: no
   in-advance-named candidate matches within even the generous ±0.31 band —
   in particular the linear-chain closure L8a21/L8a20 (the reading that
   *generated* the prediction) overshoots by +26%, and using it in the
   assembly would overshoot B(⁴He) by ~+11%. The naive "n=4 term = one
   chain-link volume" reading **fails at ⁴He**. Structurally consonant:
   8.048 < Vol(8₁₁) = 8.286 would make the 4-body link *simpler* than the
   3-body one, against the volume-complexity trend; and the census-gap datum
   shows no ≤14-crossing 4-component link carries 8.048 at all.

**What survives (explicitly, no over-claim):** the Lean-proved multiplicity
`M_n = (n−1)`, the parameter-free A=3 results (³H −0.16%, ³He −2.97%), and the
tower form `B = m_e·Σ (n−1)·Vol_n` itself. What is constrained is only the
**single-link linear-chain-closure identification of the n=4 term**. Honest
routes forward: (a) R5-full SDP canonical knot-ID at H₁₂ for the true ⁴He
link; (b) a non-single-volume n=4 term (consistent with
`binding_link_volumes.py`: "A-dependence is not in a single binding-link
volume").

## 5. Relation to the same-day companion probe

`vol4_4he_snappy_falsification_probe.py` (commit `784c6f9d`) pre-registered the
candidate list and first executed the negative with `Vol₄ = 8.048` hardcoded.
This probe closes its two gaps: the implied `Vol₄` is now **computed exactly**
from AME/m_e/corpus volumes (confirming 8.048 to 4e-4), and the census-gap
datum (0 within ±0.05 among all 7463 4-component HT links) is recorded as
guarded data. Ledger updated:
[`binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md)
item 1. Nothing wired; no tier change; the cheat-sheet 9b "open" item moves
from *untested prediction* to *executed test, negative for the naive reading,
decisive version gated on R5-full*.
