---
# qou-2361
title: 'LIVE SPLIT: q_muon_at() yields C (CODATA-2022) but the anchor-defining witness still holds A'
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:41:19Z
updated_at: 2026-08-22T20:24:13Z
---

Found while attributing a witness refresh on the cds1 branch (PR #5448).

## The split

    q_muon_at()                          -> 1.109978595642739929  (= C, CODATA 2022)
    q-pinning-50-digit.witness.json      -> 1.10997859555733471989 (= A)

The code path and the ANCHOR-DEFINING witness disagree at the 8th decimal
(~80 ppb). q_muon_at() computes LIVE from the closed form
q = 1/(1 - sqrt(Vol(4_1)/(m_mu/m_e))) using MASS_RATIO_MU_E_STR, and main's
98acdf5024 ('fix(codata): read the two substrate mass ratios from the table,
not literals') routed that through the CODATA table, moving it to the 2022
value. The witness string was not moved with it.

## Why this matters

1. It is the exact hazard AGENTS.md rule 1 names: q-pinning-50-digit.witness.json
   is what qou_substrate.witness._q0_value_for_anchor('muon') READS. Code and
   witness now answer 'what is the muon pin?' differently depending on which
   door you come through. A producer reading the witness and a producer calling
   q_muon_at() are on different anchors while both are labelled ideal_muon.
2. It moves published numbers. The cross-anchor swing |c_3(p) - c_3(m)| goes
   0.0491423 -> 0.0494823. AGENTS.md's c_k banner and registry 9g still quote
   0.0491423, so that figure is now stale corpus-wide.
3. It partly PRE-EMPTS the owner's 'go with C' ruling — for q_muon_at() only,
   as a side effect of a CODATA-literals drain rather than as the deliberate
   A->C migration. The 257 ideal_muon producers and the witness string are
   untouched, so the corpus is now HALF-migrated.

## Not done here, deliberately

Did not touch the anchor-defining witness. AGENTS.md rule 1 forbids re-pinning
it as a migration move (it redefines what 'muon' means; a prior attempt at this
class broke main for 208 producers, qou-m9xp). Whether to complete A->C or to
revert q_muon_at() to the recorded string is the owner's call and is the
substance of the held A->C item.

## Suggested triage

- Decide direction (complete A->C, or restore q_muon_at() to read the witness).
- Whichever way: the two must agree, and the doc-currency sweep for 0.0491423
  rides with it.
- Sibling overlap: #5417 (q0 anchor correctness), #5439 (CODATA code-site drain
  — 98acdf5024 is that arc's work), #5430 (anchor vocabulary).


## CORRECTION 2026-08-22 — the gap is 0.077 ppb, not ~80 ppb (I was 1000x out)

Measured at 60 dps:
    A (frozen witness)   1.1099785955573347199
    C (live q_muon_at)   1.1099785956427390467
    P (proton canonical) 1.1099785827513808076

    A vs C =   0.0769 ppb   <- the split; I had been writing '~80 ppb'
    A vs P = -11.537  ppb   <- the mu-p substrate tension (matches the
                               documented ~11.5 ppb, which is what confirms
                               the arithmetic rather than my earlier figure)
    C vs P = -11.614  ppb

The digits diverge at the 10th place (…955|5733 vs …956|4273), i.e. ~8.5e-11
absolute. My '~80 ppb' read the divergence position as if it were the exponent.

**This changes the disposition, not just the number.** At 0.077 ppb the split is
~150x SMALLER than the mu-p tension it sits inside, and below the L2 target of
every scoreable observable. So A->C is not a physics-moving change; the obstacles
are purely mechanical (three hardcoded guards, below). Any earlier reading of
this bean that treated the split as large should be re-read.

## Blast radius, re-measured (my '257 ideal_muon producers' was also stale)

Manifest today: ideal_muon = **3** (atomic_tr_m_mpfr_50dps, cross_check_trM_1ppb,
q_pinning_50_digit); physical_proton = 406; ambiguous = 1. The migration already
ran — only three producers remain on the ideal layer.

Witnesses containing the A string: **184**, of which **65** still carry
q0Anchor: muon. Witnesses carrying C: 4.

## The three mechanical blockers

1. computations/substrate/q_parameter.py:113 — hard-asserts
   _d['q'].startswith('1.109978595557') and raises otherwise. Changing the
   witness to C hard-fails every ideal_muon producer at import.
2. qou-mass/src/qou_mass/_internal/q_parameter.py:112 — a duplicate of the same
   guard in the VENDORED mirror (regenerate via scripts/sync-qou-mass-vendor.py,
   never hand-edit).
3. qou-mass/src/qou_mass/_internal/witness_polynomial.py:48 — a third hardcode,
   sp.Rational('1.10997859555733471').
