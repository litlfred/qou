---
# qou-bred
title: 'A-vs-C muon pin: B/C is SETTLED in corpus (CODATA edition); A is a FIXED POINT, not a vintage'
status: completed
type: task
priority: normal
created_at: 2026-08-22T19:40:59Z
updated_at: 2026-08-23T07:43:36Z
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


---

# DECISION BRIEF — A vs C (2026-08-22)

Written because the escalation so far gave the question without the material to
rule on it.

## The number that decides it

    |A - C|                      = 0.0769 ppb
    sigma(q0) from the muon anchor = 1.2234 ppb
                                     (m_mu/m_e = 206.7682827 +/- 4.6e-6, 22.25 ppb)
    |A - C| / sigma              = 0.063 sigma

**A and C are the same value to one sixteenth of a standard deviation.** For
scale the mu-p tension is 9.4 sigma at the same anchor.

So NO measurement in the framework distinguishes A from C and NO prediction can
depend on the choice. Anyone arguing a physics reason to prefer one is
over-reading the arithmetic. This is a governance/hygiene ruling.

## Corrections to my own earlier claims

1. **"A is an undocumented accident"** -- WRONG. The fixed point is deliberate
   and documented. `q0_anchor_manifest.json::_convention` says `ideal_muon`
   "holds the ANCHOR-DEFINING producer ... Move it and the muon anchor ceases
   to exist -- that is what broke main for 208 producers (qou-m9xp)". The
   witness's own description also spells it out: listed under ideal_muon,
   q_parameter rebinds q_at, "the Newton solve described below never
   executes", and "the m_p/m_e route is what DEFINES the quantity, not what
   ran".
2. **"A is not reproducible from a published muon ratio AT ALL"** -- too
   strong. A implies m_mu/m_e = 206.768282989315, which ROUNDS to the 2018
   published figure 206.7682830. But it is not equal to Vol/206.7682830 --
   that is B, verified exactly (9.5e-30). A sits 0.052 ppb from the
   2018-derived value and 11.5 ppb from the proton solve. Accurate statement:
   **A's exact digits remain unattributed; it is near the 2018-derived value
   without equalling it.**

## Blast radius

    files touching the anchor machinery (A's route)   48
    files calling q_muon_at (C's route)              141
    witnesses stamped muon                            56   (proton: 623)
    manifest ideal_muon entries                        3   (proton: 406)

The muon layer is small and NOT in the production path -- the 2026-08-07
directive routes production through proton. This ruling governs the ideal/CAL-2
layer, i.e. what the framework CLAIMS about its calibration, not what it
predicts.

## Pros / cons

**A (stored constant)**
  + stability: 56 witnesses stay valid, nothing regenerates
  + the 208-producer break is the measured cost of disturbing this anchor
  + a `muon` stamp means the same thing in five years
  - it VALIDATES ITSELF: re-running returns its own input; the one label in
    the vocabulary nothing can check
  - its digits are unattributed
  - it is a transcribed constant -- what "read the authority, do not
    transcribe it" was written against

**C (live derivation)**
  + checkable and self-updating; reads the vendored drift-tested NIST table
  + consistent with PR #5149's direction (constants moved from transcription
    to reading)
  + honest: CAL-2 is DEFINED by m_mu/m_e, so its pin should follow it
  - every muon-stamped witness goes stale on the next CODATA release, with no
    signal -- the failure mode that produced B
  - measured downstream: mu-p tension 11.534 -> 11.614 ppb (WORSE),
    m_mu L2 miss 963.6x -> 970.2x. Trivial, but the wrong direction.
  - reintroduces the drift the fixed point exists to prevent

## RECOMMENDATION

**Rule C canonical for what the pin MEANS; keep a stored value for what the
anchor SERVES.** Four steps:

  1. C is the definition -- CAL-2 is defined by m_mu/m_e, so derive, do not
     transcribe.
  2. Retain the fixed-point mechanism (do NOT repeat the 208-producer break),
     but REGENERATE the stored string from C and record in the witness which
     table edition and which ratio produced it. That turns A from an
     unfalsifiable constant into a CHECKABLE SNAPSHOT.
  3. Add a staleness gate asserting stored == q_muon_at() at the current
     table; warn when CODATA moves. Drift DETECTION without drift.
  4. Only then start the 71-site literal migration, which is gated on this.

**Alternative, defensible:** rule A and change nothing -- at 0.063 sigma
nothing observable moves. But then record the unattributed digits as a known
open item rather than leaving it implicit.

**What to avoid:** switching the anchor to call q_muon_at() directly. Maximum
drift exposure across 56 witnesses for a 0.063-sigma gain, via the mechanism
whose removal already broke main once.


## RULED, 2026-08-23 — owner: "adopt C per recommendation"

The A-vs-C question is CLOSED in favour of **C**. Two independent owner
statements now say the same thing:

- 2026-08-22, on #5500: *"2022 CODATA better than 2018. A --> CODATA 2022."*
- 2026-08-23, this session: *"adopt C per recommendation"*

## The execution is ALREADY IN FLIGHT — do not duplicate it

**PR #5500 / `claude/muon-anchor-codata-2022-2026-08-22` is implementing
this.** It re-points `q_parameter`'s ideal/muon branch at the live
`q_muon_at()`, updates 10 hardcoded guards in 8 files, and regenerates the
anchor-defining witness. That branch is the owner of this work. This is
mechanical migration, not open research, so the AGENTS.md
measured-research-overlap relaxation does NOT apply: one owner.

## What I under-costed in my own recommendation

My step 2 said "regenerate the stored string from C" without stating the
cost. Measured on an untouched tree:

    muon-stamped witnesses          : 56
      with q0Value                  : 56  (none unstamped)
      q0Value at A                  : 56  <- ALL become Q0_FLIP if anchor -> C
      q0Value already at C          :  0

**All 56 flip.** #5500 reports 53 because its branch has already regenerated
3 — the two figures reconcile exactly, which is an independent confirmation
of both. The regeneration is not a follow-up; it is part of the change.

## Sequencing answer (posted to #5500)

Their open question was "land the core first, or regenerate all 53 in this
tranche?". Answer: **all 53 in one tranche.** AGENTS.md
§"OWNER AUTHORISATION, RECORDED 2026-08-19" constraint 4 — *"Do not split
the change... #5049 merged the witnesses and held the manifest, and the half
that landed is the half that broke main."* Landing the anchor move with 53
stale witnesses is the qou-m9xp failure mode at smaller radius.

## What this bean shipped, and what stays true after the re-pin

The staleness gate `muon_pin_stored_vs_live_gate.py` (#5471). After #5500
lands, its reported gap goes 0.063sigma -> ~0 and its committed witness needs
one refresh. The gate itself stays correct and useful: it is what makes the
NEXT CODATA revision visible instead of silent, which is the whole reason
"derive, don't transcribe" is the right rule.

The 0.063sigma finding is unaffected by the ruling and is the reason the
ruling is safe: |A - C| = 0.0769 ppb vs sigma(q0) = 1.2234 ppb. No framework
observable distinguishes them; 53 regenerations move no physics.
