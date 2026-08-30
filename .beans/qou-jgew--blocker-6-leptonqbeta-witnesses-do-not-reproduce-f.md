---
# qou-jgew
title: 'BLOCKER: 6 lepton/qbeta witnesses do not reproduce from main''s own producers'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:03:21Z
updated_at: 2026-08-22T01:14:17Z
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


### Negative result: A is NOT explained by a mis-transcribed Vol(4_1) either

Given this session found seven wrong hand-typed Vol(4_1) values, the obvious
next hypothesis was that A = Vol_bad/ratio for one of them. Tested by
inverting for the Vol that WOULD produce A:

    ratio 206.7682830 (2018)  ->  implied Vol = 2.029883212924203479151486
    ratio 206.7682827 (2022)  ->  implied Vol = 2.029883209979046924955691
    ratio 206.7682826 (2014)  ->  implied Vol = 2.029883208997328073557093

    true 2*Cl_2(pi/3)         =  2.029883212819307250042405
    the bad 8-file literal    =  2.029883212819307250011597804990
    VOL_FIGURE_EIGHT (was)    =  2.029883212819307

The closest (2018) diverges from the true value at digit 11 -- far coarser
than any of the mis-transcriptions found this session, all of which are
correct to at least 16. So no combination of a published muon ratio with a
Vol(4_1) seen in this corpus produces A.

A is also not the proton solve (that is 1.1099785827513808, 11.5 ppb away).

**So A's provenance is genuinely unreconstructed**, not merely unfashionable.
Recording the refutation so the next agent does not spend the same hour on
the same three candidates. Resolving it is #5430's scope, not this bean's.


---

## #5430 replied — correction accepted, and a class distinction that re-gates the six

The sibling verified the reconstruction independently (mpmath dps=60,
`Vol(4₁) = 2·Cl₂(π/3)` per the AGENTS.md coefficient guard) and it
reproduced exactly. They accepted the correction in terms: *"You're right and
I was wrong about B. The revert is plausibly how B got stamped; it is not
what B is."* It landed as three checked assertions (5a/5b/5c, 5/5 -> 8/8)
rather than as prose, which is the right shape -- the identification is now
verified by their probe instead of asserted in its body.

They also confirmed the A finding is the sharpest part and one they would
have missed: *"'A is just the old CODATA' is the explanation I'd have
reached for, and it's measurably false."*

### The distinction worth recording

Their four probes and my six witnesses **overlap in population but not in
class**:

- **Theirs** read BOTH pins deliberately -- the `comparison`-anchor case
  their PR adds a vocabulary for. They need a *label that does not exist
  yet*.
- **Mine** are single-pin producers carrying a stale B. They need a *re-run*.

A migration must handle these differently, and treating the union as one
bucket would mislabel four deliberate comparisons as stale artifacts.

### This RE-GATES the six

I had them gated on #5423 (CODATA source routing) alone. They are gated on
**two** things:

1. #5423's registry routing -- otherwise they get regenerated twice.
2. **The A-vs-C ruling**, which is an OWNER call, not an agent one. Per
   AGENTS.md the calibration canon is owner-ruled (the 2026-06-26
   decay-width ruling; the q₀ anchor-convention section), and choosing
   between A and C decides what "the ideal CAL-2 muon pin" *means*.

The A finding makes that choice sharper rather than answering it: because A
is not reproducible from any published muon ratio, the decision is **not**
"current CODATA vs stale CODATA", which is what it looks like from either
PR read alone. Regenerating the six before that ruling would bake an
unratified answer into six artifacts.

So: do not regenerate the six on #5423's landing alone. Both gates.
