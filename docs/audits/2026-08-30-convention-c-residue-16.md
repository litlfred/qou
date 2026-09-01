# The convention-C residue after #6058: 16 sites

Baseline taken on `main` @ `ff9002e651`, immediately after #6058 merged.

    adjudicated in the ledger : 75
    BLOCKING (unadjudicated)  : 16

This document is the working record for draining those 16. It is opened at the
start rather than written at the end, so the baseline is recorded before any
site is touched — the count moves in both directions (siblings land new C
bindings; adjudication and elimination remove them), and a figure quoted after
the fact cannot be checked.

## The 16

See `/tmp` listing in the first commit; enumerated per-site below as each is read.

## Method

Per site, decide between exactly three outcomes, and record which:

1. **Legitimate comparison** — the C arm of a two-arm test. Adjudicate.
2. **Reproduces a C-defined object** — a Lean declaration, a published C-era
   artefact, or a corpus-proved closed form. Adjudicate, and say what would
   break if it were migrated.
3. **Residual C** — genuinely migratable. Migrate, or if the blast radius is
   large or the object may be C-*derived* rather than merely evaluated at a z,
   bean it with the measurement rather than swapping.

The third outcome is the one that needs care: `qou-cds1` establishes that the
C-frame ladder and the mass channel's three-row forcing are mutually exclusive
(`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`, sorry-free), so substituting z_D
into a C-derived object can be incoherent rather than merely different.
