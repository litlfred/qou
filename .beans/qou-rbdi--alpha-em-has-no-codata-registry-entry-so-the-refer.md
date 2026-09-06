---
# qou-rbdi
title: alpha_em has no CODATA registry entry, so the reference-literal gate is blind to it
status: todo
type: task
priority: normal
created_at: 2026-09-06T09:08:15Z
updated_at: 2026-09-06T09:09:13Z
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
