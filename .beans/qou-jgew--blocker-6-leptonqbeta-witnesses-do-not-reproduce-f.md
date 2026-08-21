---
# qou-jgew
title: 'BLOCKER: 6 lepton/qbeta witnesses do not reproduce from main''s own producers'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:03:21Z
updated_at: 2026-08-21T22:49:51Z
---

## What was measured

Found while attempting the `qou-ckbv` OVER_CLAIMED drain. Six producers were
run UNMODIFIED, on a clean checkout of main, and their output compared to
their own committed witnesses. Ephemeral provenance fields (computedAt,
durationMs, commitSha, scriptHash, engineVersion, package versions) were
excluded, so these are numeric/content differences:

    canonical-lepton-braid-words                   54 diff lines
    f-ell-derivation-via-per-braid-mass-tower      26
    per-generator-V-hat-general                    73
    q-beta-complex-q-test1-phasea-v2               16
    t6-lepton-h3-3channel-convention               54
    probes/gap-a4-T2-per-knot-vol-probe           106

**Six of six. None reproduce.**

Worked example, `t6-lepton-h3-3channel-convention`:

    committed  q_0 = 1.1099785955541805752806677289528087346650276795181
    main today q_0 = 1.1099785956427390466808687787224812726951201803937

An 8e-10 relative move -- ~800 ppb, i.e. ~70x the entire muon-proton
substrate tension -- in a quantity the corpus otherwise pins to 50 digits.
`h`, `z`, `W_SYM`, `W_STD`, `W_ALT` all move at the same order.

## The environment confound was CONTROLLED, and it is not the cause

The witness records `mpmath 1.3.0`; the first run was under 1.4.1. AGENTS.md
warns specifically about this (and about my having mis-attributed an
environment effect once before -- the `binding_canonical` 48% case). So the
producer was re-run under **1.3.0**, the exact recorded version:

    under 1.4.1  q_0 = 1.1099785956427390466808687787224812726951201803937
    under 1.3.0  q_0 = 1.1099785956427390466808687787224812726951201803937

Byte-identical. The mpmath version is NOT the cause.

## Likely cause

`t6`'s witness records `scriptCommitSha c790dd29`, while the producer's
current commit is `a4d9906659` -- the large "VolDensity -> PerKnotDensity"
rename. That same commit is implicated in the four import-breakages repaired
in PR #5407, so it is a strong candidate for having changed behaviour here
too, silently, without regenerating these witnesses.

NOT yet verified. Confirming it means checking out `c790dd29`'s producer and
seeing whether it reproduces the committed value, exactly as was done for
the convention C/D archaeology on PR #5386. That is the next step.

## Why this BLOCKS the qou-ckbv OVER_CLAIMED drain

The `Vol(4_1)` correction in those files moves numbers at digit 21. The
pre-existing drift moves them at digit 10 -- **eleven orders larger**. So
regenerating any of these witnesses as part of a "volume literal fix" would
bury an unexplained 8e-10 discrepancy inside a commit labelled as a
precision improvement. That is precisely the failure mode PR #5386 was about.

The volume fix for these six must therefore wait until this is resolved, or
land with the witnesses deliberately untouched and this bean cited.

## Correction to my own earlier partition (recorded because it was wrong)

`qou-ckbv` claimed a cheap tier of "7 source-only" sites needing no witness
regeneration. That was produced by a STATIC heuristic (regex for
`.witness.json` strings and `WitnessBuilder("literal")` calls) and it is
wrong: run empirically, **6 of those 7 write a committed witness**. The
heuristic missed producers whose witness name is derived rather than
written as a literal.

There is no cheap tier. Classify by running, not by grepping.

Also: `q_beta_complex_q_test1_phaseA.py` exceeds 300 s and did not finish --
long-compute, needs the tee'd-log discipline.


---

## RESOLVED 2026-08-21 — it is the CODATA 2018 -> 2022 update. Not a mystery, and NOT a blocker.

The "likely cause" above guessed `a4d9906659` and guessed the mechanism wrong
(I suspected the VolDensity->PerKnotDensity rename changed behaviour). The
commit is right; the mechanism is not. Determined by inverting the committed
q_0 rather than by reading code.

These producers DERIVE q_0 from CAL-2 rather than reading a pin:

    hbar_q^2 = Vol(4_1) / (m_mu/m_e)
    q_0      = 1 / (1 - hbar_q)

so q_0 is invertible back to the muon ratio that produced it:

    committed witness  =>  m_mu/m_e = 206.7682830   <- CODATA 2018
    main today         =>  m_mu/m_e = 206.7682827   <- CODATA 2022

`a4d9906659` CREATED `computations/codata_2022_source.py` (465 lines, all new)
carrying `M_MU_OVER_M_E = 206.7682827`. The witnesses predate it and were
never regenerated.

Consistency check on the magnitude: the ratio moved 1.45e-9 relative;
d(q_0)/q_0 = 0.55 * d(cal2)/cal2 for this map, giving ~8e-10 -- which is what
was measured. The arithmetic closes.

Confirmed across the class: all four of the six witnesses that carry a `q_0`
field record the identical value 1.1099785955541805752806677289528087346650276795181,
i.e. the CODATA-2018 q_0. (`q-beta-complex-q-test1-phasea-v2` has no `q_0`
field; `gap-a4-T2-per-knot-vol-probe` not checked this way.)

### What this changes

**The `qou-ckbv` drain is NOT blocked.** Regenerating these witnesses is
correct and safe -- the diff is explainable rather than mysterious, and the
CODATA update is a deliberate corpus change that these witnesses simply have
not caught up with.

The remaining requirement is DISCLOSURE, not investigation: a commit that
regenerates them must state that the bulk of the numeric diff is the CODATA
2018 -> 2022 update and NOT the Vol(4_1) correction, which contributes only at
digit 21. Two effects, one diff, both named.

### Distinct from PR #5436's mechanism -- checked, does not apply

#5436 documents unlisted producers falling through `q0_anchor_manifest.json`
to the proton default, flipping muon -> proton (11.5 ppb). That is NOT this:
these producers never consult the manifest, and 0.8 ppb is the wrong
magnitude and the wrong direction. Two different stale-q_0 mechanisms in the
same session; do not conflate them.

### Coordination

PR #5423 ("CODATA drain (7ot6-a): route the constants modules at the registry,
not literals") is live on the same input. Any regeneration of these six should
land after, or coordinate with, that work -- otherwise they get regenerated
twice.


---

## Cross-check against PR #5430 (independent, same values, different route)

#5430 ("A `comparison` q0 anchor -- and the three different values all called
'the muon q_0'") reached the same two numbers from the pin-vocabulary side.
Its labels, kept here so the two records line up:

    A  1.10997859555733471989...  canonical pin, frozen (q-pinning-50-digit)
    B  1.10997859555418057528...  what the committed witnesses carry
    C  1.10997859564273904668...  what a fresh run produces

My six producers never touch the pin machinery -- they derive q_0 inline --
so this is a genuinely independent route to the same values.

### Refinement of #5430's account of B

#5430 attributes B to a change made and reverted on 2026-08-15, whose revert
"restored the anchor source and did not regenerate the witnesses". That may
well be how B got STAMPED. But B's VALUE is forward-verified as a CODATA-2018
derivation:

    Vol(4_1) / 206.7682830  ->  B    (agreement 3.9e-50, i.e. all 50 digits)
    Vol(4_1) / 206.7682827  ->  C

206.7682830 is CODATA 2018; 206.7682827 is CODATA 2022. So B and C are the
SAME derivation at two vintages, not two unrelated incidents, and B is not an
artifact of the revert.

### New: A is not a CODATA derivation at any vintage

Inverting A the same way gives

    m_mu/m_e = 206.768282989315

which matches NEITHER published figure. It sits between them, 5.2e-11
relative from the 2018 value. So "A is just the old CODATA" -- the tempting
explanation -- is measurably false. A is a stamped literal not reproducible
from a published muon ratio.

**Recording a near-miss:** I first ran this check with A typed as
`1.1099785955733347`, which DROPS A DIGIT from the real
`1.10997859555733471989...` (they differ at digit 12). Caught before it
reached the sibling PR. Noting it because it is exactly the transcription
class this whole arc is about, and it nearly landed inside the analysis
rather than in the data.

### Population note

#5430 names four probes carrying B. The six here are additional B-carriers,
so the B population is larger than either PR alone shows. If a migration off
B happens, both sets belong in it.

Posted as https://github.com/litlfred/qou/pull/5430#issuecomment-5376190909
