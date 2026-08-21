---
# qou-jgew
title: 'BLOCKER: 6 lepton/qbeta witnesses do not reproduce from main''s own producers'
status: todo
type: task
priority: normal
created_at: 2026-08-21T22:03:21Z
updated_at: 2026-08-21T22:04:00Z
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
