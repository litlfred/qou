---
# qou-t39x
title: Three muon c_3 values are each correct at a different muon anchor; -2.0097 matches none, and four files pair it with three different pins
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T02:27:01Z
updated_at: 2026-11-15T17:33:14Z
parent: qou-avtq
blocked_by:
    - qou-cds1
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


## 2026-08-31 — the pairing rule reached the registry, the content and AGENTS.md

This bean's general rule ("a `c_3` value is meaningless without its anchor") was
landed into *producers* on 2026-08-29. It had not reached the places a reader
takes the number **from**, and `qou-cds1` Finding B is what that cost: an agent
three weeks later read `−2.01986031187` as "a third value" of unknown origin,
340× tolerance, and opened it as a defect. It was this bean's CODATA-2022 row.
Closed against this bean; commits `636c1541c0` + `1ee9666f7d`.

**Sites corrected** (all had `−2.02020024` as *today's* value): the sensitivity
probe's regression target; `c3_even_canonical_split_contradiction.py` (was
itself a straddle — **frozen** pin paired with the **CODATA-2018** `c_3`);
`sleak_offset_genericity_check.py`; `ck-dk-registry.json` + the `.md` twin
(`--twin` T1–T5 green after); `SLeakZeroCrossing.lean`,
`FaddeevModularDouble.lean`, `ThetaLipschitzObstruction.lean`;
`qbeta-ck-truncation-canonical.ts`; `AGENTS.md`. Anchors are now **derived**
where they were transcribed.

**A live self-contradiction this turned up**, worse than a stale literal:
`qbeta_c3_crossanchor_swing_provenance_probe.py` *computed* 2.3912 % / 2.4741 %
and then printed, three lines later, "the current swing, which is 2.3748 % /
2.4571 %" — the stale pair hard-typed under the fresh one, and the stale pair is
what went into its witness description. Now interpolated.

### Two more CODATA-2018-era literals the same edition step surfaces

1. **`S(muon) = 886.8`** (2026-07-07 audit, 4 s.f.) is **3.17× outside its own
   rounding window** at the live pin, where it reads **886.6**.
2. **KC21's Φ_b scale claim degrades 3.01 % → 6.63 %** — 2.2× worse. The deficit
   0.0094 is anchor-blind to sub-ppm, so *all* the movement is on the `|S|`
   side: the quoted "~2.9 %" was never a property of the saddle. Recorded in the
   Lean table it is read off, and computed rather than asserted.

### `dc_3/dq` — your retraction re-verified, and it holds

You retracted a "3.812e6 / 0.7 % stale" claim here as your own straddle and
asserted the slope is anchor-layer invariant. Confirmed independently at the
2022 pin: secant **3838405.894** (2018) vs **3838405.878** (2022), identical to
8 digits. `3.84e6` stays everywhere; it was the one number that did **not** need
correcting, and it is the one an unwary sweep would have "fixed".

### What the pairing rule was missing: an error bar

Three values differing in the fourth significant figure all call themselves
"muon `c_3`" — and **none of them carries four significant figures**. Propagated
through the CAL inputs at CODATA-2022 published uncertainties (recomputed at
±1σ, not via a recorded derivative): **`c_3(muon) = −2.0199 ± 1.26`**, dominated
by `Q_β` alone (0.78 ppm × `1/u³` = 1.6e6) — **0.2** supported significant
figures against the **9** quoted. So the three-way spread this bean is about is
**3700× inside** the experimental bar; the pairing rule is about
*reproducibility*, and was right to be, but it should not be read as being about
physical resolution.

What *is* resolved: `Q_β` and `m_e` are **common mode** and cancel in the
difference, leaving the cross-anchor swing at **−0.0494823 ± 0.0052 = 9.5σ** —
the same 9.5σ as the μ–p tension, because it is the same statement.
Probe `qbeta-c3-muon-anchor-codata-edition-attribution` (11/11).

**Still open** (unchanged): re-pinning `Q_MUON_50_DIGIT_STR` and migrating the
336 ancestor-bearing files, sequenced behind PR #5500 and `qou-1c4y`; and the
audit docs under `docs/audits/` that record `−2.02020024` — those are dated
records of what was true then and were deliberately left alone.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-31 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The four files named in the bean are fixed and the attribution reproduces 11/11. The same superseded -2.0097 is still a live constant in at least 9 other producers (listed in the evidence column), and the muon re-pin waits on qou-1c4y. All these values are convention-C.

Evidence: Landed: PR #5952, plus 636c1541c0 and 1ee9666f7d. The four named files are fixed: `qbeta_eigenphase_taylor_in_u.py:104` = -2.02020023502, `qbeta_exponentiated_per_block_probe.py:124` = -2.02018812814, the pslq file keeps -2.0097 only as a labelled spread constant at L109, and the multiblock audit renamed to `Q0_PROTON_PIN` (L96). `qbeta_c3_muon_anchor_codata_edition_attribution_probe.py` re-run exits 0, 11/11. **Still open:** at least 9 other producers use `-2.0097` as a live empirical muon c_3: `probes/qbeta_li2q_spectral_combiner_crossanchor_probe.py:147`, `probes/qbeta_borromean_cyclotomic_probe.py:146`, `probes/qbeta_c3_habiro_3rung_crossanchor_rigidity_probe.py:74`, `probes/phi_q_spectral_combiner_probe.py:170`, `probes/qbeta_complex_c3_fibre_probe.py:95`, `c_3_categorical_derivation_attempt.py:371`, `habiro/habiro_mode_to_ladder_bridge.py:232`, `qbeta/qbeta_ck_truncation_order_analysis.py:237`, `qbeta/qbeta_c4_qhermite_entry_gate_probe.py:61`. The re-pin is queued behind `qou-1c4y` (todo).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

### Progress (Round 73 — PR litlfred/qou#8318)
- Formalized in PR `litlfred/qou#8318` (`feat/round73-symsquare-fibretl-mu3slot-sleak-deuteronz-43c1`, Commit 1 `d5360fac6f1464f5fd03c06ef76e726e30c785fd`, Head `e58aca150b7054a3222889e8bb9937602e515ca4`, `scriptHash: 19f0b8589c79`).
