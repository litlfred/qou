---
# qou-rbdi
title: alpha_em has no CODATA registry entry, so the reference-literal gate is blind to it
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T09:08:15Z
updated_at: 2026-10-04T15:16:20Z
---

Found by continuing the class-D read (`qou-psjm`) into the 7 deprecated-source
findings that the self-reference fix (`qou-4kc0`) made visible. One of them --
`alpha_em_b2_invariant_c_probe.py:74`, `ALPHA_EM = mp.mpf("0.0072973525693")`
labelled "CODATA fine-structure const" -- is a CODATA-2018 value, i.e. exactly
the edition-drift class `codata_truncation_audit.py` exists to catch. It did not
catch it, and the reason is structural.

## The gate cannot see alpha, by construction

`CANON` in `codata_truncation_audit.py` is sourced from the CODATA registry.
`tools/qou-substrate/python/qou_substrate/codata.py` has **NO fine-structure
entry** -- grep for `alpha`/`fine` returns only "alpha particle mass" in a
docstring. So alpha cannot be in CANON, and every hardcoded alpha in the corpus
is unguarded.

CANON currently covers: B_2H B_3H B_3He B_4He B_5Li B_6Li B_7Li m_e m_mu m_n m_p
m_pi q0 q0_muon q0_muon_live u_MeV. No alpha.

## Three live values, 62 files

    137.035999084   41 files   CODATA 2018 (Cs recoil)
                               named CODATA_ALPHA_INV / INVERSE_ALPHA_CODATA
    137.035999177   19 files   CODATA 2022, correctly commented
    137.035999206    2 files   Morel et al. (LKB Rb) -- NOT CODATA, but the
                               variable is named CODATA_ALPHA_INV
    (137.0359999982  1 file    a PREDICTION in _deprecated/, correctly not a
                               defect -- listed so nobody re-flags it)

Spread, computed at dps 30 against CODATA 2022:

    137.035999084   -0.67865 ppb
    137.035999206   +0.21162 ppb

0.89 ppb across the live set. Against the m_K/m_pi L2 target (264 ppb) that is
small; against L1 (1 ppQ = 1e-6 ppb) it is ~890,000x, so any cross-method
comparison that mixes two of these cannot meet L1 no matter how it is computed.

## The edition question is NOT open -- there is a ruling

Bean `qou-6dcc` (completed 2026-08-29) records it verbatim: *"refresh on CODATA
2022 as needed"; "2018 vintage/comparison, 2022 is current"*. The owner
re-affirmed the same preference this session for the u->MeV edition ("Codata
2022"). So 2022 is canonical and 2018 is vintage/comparison.

**This does NOT make the 41 files 41 defects.** The corpus legitimately carries
vintage values as deliberate comparisons and frozen historical records -- the
seven `option_e_*` probes are the worked example. Each of the 41 needs its own
read. What IS unambiguous is below.

## Unambiguous, in order of confidence

1. **The registry has no alpha.** Gate coverage gap. Not a judgement call.
2. **`computations/substrate/experimental_constants.py:153`**

       ALPHA_EM_INV = 137.035999084  # noqa: P31 - CODATA 2018, Cs recoil

   is a bare Python **float** at the **vintage** edition, and it is the closest
   thing the corpus has to a canonical alpha. Same defect SHAPE as
   `VOL_FIGURE_EIGHT` in bean `qou-9ies`, same file, ~50 lines apart -- a float64
   canonical that consumers import. Whether these two share a root cause (that
   file being treated as a dumping ground for "measured" constants) is worth one
   look.
3. **Two files name the Morel et al. value `CODATA_ALPHA_INV`.** It is not
   CODATA; it is a single experiment. A reader resolving that identifier gets the
   wrong provenance. Naming-only fix,
   `computations/probes/em_coupling_projection_probe.py:21,65`.

## Options

1. Add alpha to `codata.py` at CODATA 2022 and to CANON. Closes the gate gap
   permanently. **Measure the baseline impact FIRST** -- with 62 files carrying
   a non-2022 or hardcoded alpha this could add many findings at once, and the
   owner has already questioned a 232 -> 277 growth on the sibling gate.
2. Do (1) but stage it: add to `codata.py` only (no CANON row), so the canonical
   exists and consumers can migrate, then add the CANON row once the drain is
   done. Slower, no baseline shock.
3. Fix item 3 only (the naming defect). Two lines, zero numerical change.
4. Nothing. alpha stays unguarded, three values stay live, and the next
   edition-drift instance in alpha goes undetected exactly as this one did.

**Recommendation (my judgement, not a finding): 2, then 3.** The registry entry
is the thing with no downside -- it creates a canonical to migrate toward without
firing a gate at 62 files on the day it lands. Item 3 is free and can ride along.

## Default if nobody acts

Option 4. Nothing breaks today; alpha simply remains the one CODATA constant the
CODATA gate cannot see.

## Blast radius

62 live `.py` files. The consumers that matter for something a reader sees are
the alpha_EM derivation probes feeding `m_K/m_pi` -- the framework's only
scoreable L2 result -- and `qou-aemx` (in-progress, high) is already working that
front. Coordinate there before touching those files.


---

## 🛑 CORRECTED 2026-09-06 — three of this bean's claims were WRONG

Fixed in the same change that closed the real gap. Read this before acting on
anything above.

**1. "codata.py has NO fine-structure entry" — FALSE.** It has both
`fine-structure constant` = 7.2973525643e-3 and `inverse fine-structure
constant` = 137.035999177, and the latter is already CODATA 2022. I grepped the
PARSER source and got one docstring mention of "alpha particle mass"; the data
lives in `data/allascii.txt`, which the parser reads. Grepping a parser instead
of the data it serves is the detector-blindness shape AGENTS.md catalogues.

**2. "41 files are off-canon against the CODATA-2022 ruling" — FALSE, and this
is the one that would have done damage.** The three values are three
DETERMINATIONS, not three editions:

    137.035999046   Parker et al. 2018, Cs recoil (Berkeley)
    137.035999206   Morel  et al. 2020, Rb recoil (LKB)          2 files
    137.035999084   CODATA 2018, Cs-weighted                    41 files
    137.035999177   CODATA 2022, incorporating both             19 files

Cs and Rb disagree at **7.6σ** — an open experimental tension, not a currency
question. `experimental_constants.py:150`, three lines above the constant I
called stale, says: *"DELIBERATE determination choice, not a stale edition. The
Cs-recoil value is retained on purpose; CODATA-2022 would be a different
determination, not merely newer digits."* I did not read it. The `qou-6dcc`
owner ruling on CODATA vintage is about EDITION CURRENCY and does not reach a
determination choice.

**3. "Two files misname the Rb value CODATA_ALPHA_INV" — ALREADY FOUND.**
`the_em_coupling_projection_block_cites_a_producer_that_leaves_no_witness_probe.py:34`
documents exactly this, marks it fixed, and the consumer now names Morel et al.
(2020) Rb-87 explicitly and explains why the retained identifier is harmless. I
filed it without running the corpus-grep for prior work.

## What survives, and what shipped

The gate genuinely had no α coverage. α is now in CANON, **sourced from the
CODATA table rather than typed**, and carried as THREE determinations — the same
shape as `q0`/`q0_muon`, for the same reason.

    single CODATA-2022 canonical    63 NEW   (38 of them determination choices)
    three determinations            25 NEW   (all genuine truncations)
    DIVERGENT 134 -> 96 · baseline 218 -> 243

## Remaining queue: 25 truncations, NOT drained

`137.0359991` (23 files) and `137.035999` (2). Not drained because
`137.0359991` is simultaneously a prefix of CODATA-2022 AND the 10-figure
rounding of CODATA-2018 — lengthening it needs the author's determination.

**Do not blind-migrate.** `alpha_em_schwinger_ladder_probe.py:114` asserts
`schwinger_brings_alpha_within_3sigma`; the 2018→2022 shift is 9.3e-8 against
σ = 2.1e-8 = **4.43σ**, so an edition bump can flip that verdict — and that
4.43σ IS the Cs-vs-Rb tension appearing in a probe's conclusion. `qou-aemx`
(in-progress, high) owns the α_EM front.

🛑 CORRECTED 2026-09-07 (PR #7069) — the premise of this bean is FALSE. codata.py DOES carry the fine-structure constant. Measured by CALLING it, not grepping it: C.table() contains 'fine-structure constant' (value_str='7.2973525643e-3', uncertainty_str='0.0000000011e-3') and 'inverse fine-structure constant' (value_str='137.035999177', uncertainty_str='0.000000021') — both CODATA 2022, both with uncertainties. This bean greps codata.py's SOURCE, which cannot see entries the module parses at RUNTIME out of data/allascii.txt (line 169). Same detector-blindness class the taxonomy catalogues: the interesting content was assumed to be in the file you searched.

What SURVIVES, and is a different defect: CANON in codata_truncation_audit.py is a HAND-WRITTEN list that omits alpha, so the GATE is blind even though the REGISTRY is not. Fixing that is one entry in CANON, not an addition to the registry — much cheaper than this bean says. The 62-file / three-value census below stands and is useful.

Consequence for anyone acting on this bean: do NOT add a fine-structure entry to codata.py (it is already there, and a second one would be the duplicate class). Fix CANON instead, and route producers through codata.codata('inverse fine-structure constant') — done for alpha_em_schwinger_ladder_probe.py in #7069.


## 2026-09-30: alpha now has a CODATA 2022 source
library/codata-2022 (ingested from NIST allascii via codata-ingest, 355 quantities) carries inverse-fine-structure-constant = 137.035999177 and fine-structure-constant. alpha_em_shift_chain.py reads it instead of the literal 137.035999084, which was the CODATA 2018 value labelled 2022; its witness is regenerated. Not done here: wiring codata_truncation_audit's CANON to the dataset, which is what would make the gate see alpha.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 33ccc1895b records CODATA-2022 alpha source; 37j2 reanalysis: false premise (registry has alpha); 7 main commits
