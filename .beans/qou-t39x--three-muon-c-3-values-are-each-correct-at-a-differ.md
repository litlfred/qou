---
# qou-t39x
title: Three muon c_3 values are each correct at a different muon anchor; -2.0097 matches none, and four files pair it with three different pins
status: in-progress
type: bug
priority: normal
created_at: 2026-08-29T02:27:01Z
updated_at: 2026-08-29T02:50:22Z
---

Found chasing the root cause behind `qou-kt8o` (the `dc_3/dq ≈ 4.6e6`
staleness). It is **not** "one stale constant" — it is a missing pairing rule.

## THE MEASUREMENT

I re-implemented the extraction `c_3 = (Q_codata/Q_N2 − 1)/u³` independently and
evaluated it at every q₀ the corpus calls an anchor. It reproduces the corpus
proton value to **12 digits**, which is what licenses the rest:

    anchor                          c_3                matches
    proton                          -2.06934257712     corpus proton, exactly
    muon FROZEN pin  (…5557…)       -2.02018812814     —
    muon CODATA-2018 (…5554…)       -2.02020023502     the "corpus/registry" value
    muon CODATA-2022 (…5642…)       -2.01986031187     qbeta-c3-barodd-sleak.witness
    -2.0097                         (matches none)     pre-#1422, genuinely superseded

**So there is no single "live muon c_3".** There are three, each correct at its
own anchor, and the widely-quoted `-2.02020024` is the **CODATA-2018** one —
itself superseded since `fca08de7d` moved the anchor to CODATA-2022. The
barodd-sleak witness already carries the current one; the probes quoting
"CORPUS_C3_MUON" do not.

## THE DEFECT: four files, three different anchors, one constant

Each hardcodes `-2.0097` independently (no shared source), and each sits on a
DIFFERENT muon pin, so each needs a different correction:

| file | its own muon q₀ | correct c_3 |
|---|---|---|
| `qbeta/qbeta_eigenphase_taylor_in_u.py` | …5554… (CODATA-2018) | −2.02020024 |
| `probes/qbeta_exponentiated_per_block_probe.py` | …5573… (frozen) | −2.02018813 |
| `probes/qbeta_ck_basis_constrained_pslq.py` | …5573… (frozen) | −2.02018813 |
| `audits/qbeta_multiblock_order_audit.py` | **see below** | — |

These are NOT display-only: `qbeta_ck_basis_constrained_pslq.py:154` computes
`slope_c3 = (C3_EMP_PROTON − C3_EMP_MUON_HOPF)/(Q0_PROTON − Q0_CANONICAL)`, and
the other two compute an error and a swing. Fixing them MOVES RECORDED NUMBERS.

## A SEPARATE, WORSE DEFECT in the multiblock audit

    Q0_MUON_PIN = Q_50_DIGIT_STR      # comment: "the framework (muon-derived) q₀"
    Q0_MP_PIN   = "1.10997858275…"

`Q_50_DIGIT_STR` is the **PROTON** pin (since the 2026-05-28 re-pin). So
`Q0_MUON_PIN == Q0_MP_PIN`, verified identical — the file's two "different"
anchors are the same number, and its comment asserts the opposite. Mitigating:
**both constants are dead** (defined at :81-82, referenced nowhere), so no
computation is corrupted. The false comment is live misinformation regardless,
and the c_3 "swing" the file prints and records comes entirely from the two
hardcoded constants, not from its pins.

## THE GENERAL RULE this argues for

**A c_3 value is meaningless without its anchor.** Three values differing in the
4th significant figure all legitimately call themselves "muon c_3". Any file
carrying one without naming the pin it belongs to is a straddle waiting to
happen — and four files are in exactly that state.

## AND IT CAUGHT ME

I reported `dc_3/dq = 3.812e6` on PR #5942 and claimed AGENTS.md's `3.8375e6`
was "~0.7 % stale because the muon anchor moved". **That was my own straddle**:
2018 c_3 against 2022 Δq. Computed consistently the slope is

    CODATA-2018 c_3 with 2018 Δq   ->  3838405.9
    CODATA-2022 c_3 with 2022 Δq   ->  3838405.9   (identical to 8 digits)

**`dc_3/dq` is anchor-layer INVARIANT** (both legs move together), AGENTS.md's
3.84e6 is right, and my "stale" claim is retracted. Recorded here because it is
the same error the bean is about, committed while writing about it.


## Landed 2026-08-29 (PR #5952)

Three producers drained of the pre-#1422 `C3_EMP_MUON = -2.0097`, each getting
the value extracted AT ITS OWN muon pin (there is no single 'muon c_3' — the
three pins in use give -2.02018813 / -2.02020024 / -2.01986031). Extraction
validated by reproducing the corpus PROTON value -2.06934257712 to 12 digits.

A fourth file (`qbeta_ck_basis_constrained_pslq.py`) had a different defect —
a slope dividing a proton-minus-muon Delta-c3 by a proton-minus-canonical
Delta-q, which is where the corpus's 4657409.9 came from. Slope fixed; the
mismatched constant KEPT at :196 where it deliberately measures inter-producer
spread.

The provenance was circular: the exponentiated probe cited the multiblock audit
as its source, and that file's `Q0_MUON_PIN` held `Q_50_DIGIT_STR` — the
PROTON pin. Renamed `Q0_PROTON_PIN`; dead constant, no number moves.

Re-running the exponentiated probe turned the raw-float64 ratchet RED with one
NEW dirty witness — mine, not pre-existing (the committed witness had a STRING
"1e-35" while the producer emits the bare float literal, i.e. the file had
drifted from its own producer). Fixed at the producer: mpf tolerance + mp.nstr
serialization, mpf comparisons replacing float64 ones, and the `float(c[2])`
cast that was reporting a 35-digit agreement as -1.0. Ratchet green after.
Also killed three hardcoded '2.9%' empirical swings by interpolating the value
the function already computes (2.38%).

Two witnesses deliberately NOT regenerated, disclosed in the PR: the pslq one
(unmodified main gives convention-D -974.38 vs committed convention-C -2.02) and
the eigenphase one (unmodified main already fails its a2 assertion with computed
0.9642627018922193 while the committed witness says passed: true). Source fixes
land, contaminated witnesses do not.

OPEN, not started: AGENTS.md's own site list for this figure ('five other sites
... audit docs and local/compute-author') is wrong — measured 55 files, incl. 3
.lean and several under computations/.
