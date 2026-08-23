---
# qou-58sa
title: 'GAP: the muon anchor-defining witness is 0.85 ppb stale — CODATA-2018 value baked in; blocks the C->D witness migrations'
status: todo
type: task
priority: normal
created_at: 2026-08-23T17:20:31Z
updated_at: 2026-08-23T17:21:45Z
---

Found while starting the B4 half of the convention-C excision (`qou-cds1`,
PR #5565), which needs producers re-run and their witnesses diffed. The first
re-run did not reproduce its committed witness, and the cause is not the
convention and not my container.

## The measurement

`qbeta_h_frame_rungs_probe.py`, source UNMODIFIED, re-run on current main:
4 mathematical fields move, all of them the **muon** anchor row (the proton row
is stable):

    anchors[muon].q   committed 1.10997859555418057528159407960950937799328...
                      fresh     1.10997859564273904668179512938000175270006...

Ruled out, by testing rather than assuming:
  * sympy version — the drift is identical under 1.12 and 1.14.0
  * mpmath / clarabel — installed 1.4.1 + 0.11.1 to match the witness's own
    `environment` block exactly; drift unchanged
  * my container generally — the proton anchor reproduces byte-identically

## The cause

`q_muon_at()` does not read a pin. It COMPUTES

    q = 1 / (1 - sqrt(Vol(4_1) / (m_mu/m_e)))

`Vol(4_1)` is fine (`vol_4_1_at(50)` equals `2*Cl_2(pi/3)` exactly). The moved
input is the mass ratio, changed by main's `98acdf5024` (2026-08-19),
"fix(codata): read the two substrate mass ratios from the table, not literals".
That commit's own diff says it:

    MASS_RATIO_MU_E  206.7682830  ->  206.7682827

i.e. a hand-typed **CODATA-2018** literal was sitting under a "CODATA 2022"
comment, 1.451 ppb off, and was corrected. **The fix is right.**

## The consequence, which the fix did not carry through

Inverting the closed form at the anchor witness's own recorded q gives the ratio
it was built from:

    m_mu/m_e implied by q-pinning-50-digit.witness.json = 206.76828298931504382
    m_mu/m_e in constants now                           = 206.7682827

So `computations/q-pinning-50-digit.witness.json` — the ANCHOR-DEFINING file,
whose 50-digit string is quoted verbatim in AGENTS.md as the canonical muon pin
— still encodes the CODATA-2018-derived value. It disagrees with the closed form
that defines it by **~0.85 ppb**.

The commit note "Nothing physical moved" is right about the constant and wrong
about the corpus: every muon-anchored derived quantity moved with it, including
the anchor's own self-consistency.

## Why this is NOT mine to fix

AGENTS.md rule 1: `q-pinning-50-digit.witness.json` is anchor-DEFINING. Re-pinning
it redefines what "muon" means corpus-wide — the failure mode that produced 262
`Q0_FLIP`s and hard-failed every `ideal_muon` producer. `q0_repin_sweep.py`
excludes it by name and that exclusion must stay. This needs the owner, or the
branch that owns the CODATA arc (`qou-7ot6`), not a drive-by re-pin.

## Why it BLOCKS the excision

The B4/B4t class of `qou-cds1` is 19 sites, each requiring: migrate C->D, re-run
the producer, diff the witness, justify the value change. With the muon anchor
0.85 ppb off its own definition, every muon-anchored producer moves for TWO
reasons at once and the diff cannot attribute them. That is the straddle
AGENTS.md forbids inside a single quantity, one level up.

Sequencing: settle this, then do the B4 migrations. Proton-anchored producers in
the B4 set are unaffected and could go first if the anchor fix is slow.

## Also worth checking (not done here)

The q0-anchor consistency audit's `check_reference_integrity` guard keys on
`_EXPECTED_PREFIX = {"muon": "1.109978595557", ...}`. The live `q_muon_at()` is
`1.109978595642...`, which does NOT carry that prefix. Whether the audit
currently flags this, or only checks the witness against itself, was not
verified.
