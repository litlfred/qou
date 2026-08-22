---
# qou-bred
title: 'A-vs-C muon pin: B/C is SETTLED in corpus (CODATA edition); A is a FIXED POINT, not a vintage'
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:40:59Z
updated_at: 2026-08-22T19:41:47Z
---

Corpus-grep answer to "is A-vs-C already in the corpus?", run 2026-08-22 per the
AGENTS.md checklist. Short answer: **half of it is settled, the other half is a
different question than anyone stated -- including me.**

## B vs C: SETTLED, and it predates my PR by three days

`docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md` (+ PR #5149)
already resolved the CODATA edition question:

    206.7682830   one edition earlier, carried under a "CODATA 2022" comment
    206.7682827   CODATA 2022 (the vendored NIST table)

PR #5149 made `qou_substrate.constants` READ the table
(`qou_substrate/data/allascii.txt`, drift-tested) instead of transcribing it, so
`q_muon_at()` -- my value C -- now tracks the current edition automatically. The
sweep found the same staleness in 275 distinct literals across 1962 sites, all
same-sign and same-order (1.3-1.5 ppb).

So PR #5430 and PR #5434 independently rediscovered, from the q0 side, a thing
the corpus had already fixed from the constants side. Worth knowing before
anyone treats either PR as the origin of that finding.

## MY OVER-CLAIM, recorded

#5430's merged body states **"B = CODATA 2018"** as fact. #5434 said the same.
The corpus's own audit explicitly refuses that attribution:

  > "The 'CODATA-2018' identification is not verified. Only the 2022 table is
  >  in the repository. That these literals are specifically the 2018
  >  adjustment is inferred from the coherence of the offsets plus recall...
  >  it is stated as inference."

Two separable claims, and I conflated them:
  (a) B = Vol(4_1)/206.7682830 exactly          <- VERIFIED (mpmath dps=60)
  (b) 206.7682830 IS the CODATA 2018 adjustment <- INFERENCE, unverifiable here

(a) stands. (b) is not checkable without a 2018 listing in the repo. Say
"one edition earlier" rather than "CODATA 2018" unless someone uploads it.

## A: NOT settled -- and it is a FIXED POINT, not a stale vintage

Nothing in the corpus explains A. And the reason it inverts to a muon ratio
matching no published figure (206.768282989315) is not that it is an old
vintage. It is that **A is not derived from a muon ratio at all**:

  * `q_pinning_50_digit.py` computes `Q = q_at(mp.dps)`;
  * the producer is listed under `ideal_muon` in `q0_anchor_manifest.json`;
  * so `q_parameter` resolves the anchor from the argv stem and REBINDS `q_at`
    to return the witness's own stored string.

The producer reproduces its own input. VERIFIED empirically: ran it under its
real argv, `q0Value` before == after, byte-identical.

`_q0_value_for_anchor`'s docstring already says this ("The producer is a FIXED
POINT; re-running it changes nothing") -- as an argument for why a proposed
change was safe to revert. Its consequence for the A-vs-C question is not drawn
anywhere: **A has no live derivation. It is a stored constant that validates
itself.**

## What that makes the actual question

Not "which CODATA vintage should the muon pin use" -- C already tracks the
current table. It is:

    should the ideal CAL-2 muon pin be a STORED CONSTANT that reproduces
    itself (A), or a LIVE DERIVATION over the current NIST table (C)?

Those have different failure modes. A cannot drift but also cannot be checked
against anything. C is checkable and self-updating but moves whenever CODATA
adjusts, which is what produced the B/C split in the first place.

Still an owner ruling -- it decides what "the ideal CAL-2 muon pin" MEANS, and
AGENTS.md puts the calibration canon under owner sign-off. But it is a sharper
question than the one I escalated, and the "current vs stale CODATA" framing in
#5430's body is wrong: C is current, and A is not a vintage at all.
