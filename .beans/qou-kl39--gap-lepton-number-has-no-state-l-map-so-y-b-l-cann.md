---
# qou-kl39
title: 'GAP: lepton number has no state->L map, so Y = B - L cannot be assembled'
status: todo
type: task
priority: normal
created_at: 2026-08-09T11:07:51Z
updated_at: 2026-08-09T11:07:52Z
parent: qou-5b8n
---

Found 2026-08-09 while checking whether the corpus's existing lepton number closes
the L half of Y = B - L (proved requirement: HyperchargeBatteryReduction.lean).

WHAT EXISTS (content/quantum-observable-universe/predicted-spectra/lepton-number-categorical.*):
  - .md: L := count of Skein smoothings on the nuclear normal form; prose table
    assigning L to e-, e+, nu_e, nubar_e; 'hadrons carry L = 0' as prose.
  - .lean: structure LeptonNumber { L : Int }  -- a one-field wrapper, computes nothing
           structure SkeinSmoothing { charged, neutral, pair_conservation : charged+neutral=0 }
           theorem lepton_number_conservation : (map (c+n)).sum = 0

WHY IT DOES NOT CLOSE:
 1. NO state -> L function anywhere. Y is a property of a STATE; L as defined is a
    count along a TRANSITION (a beta decay). Converting one to the other is a real
    step, not bookkeeping. The .md gestures at a Z-grading on the Skein module as
    the mechanism; that grading is not formalised.
 2. No quark appears in the file. The B-L = 1/3 quark row has nothing behind it;
    only 'hadrons L=0' in prose.
 3. lepton_number_conservation is near-vacuous: every SkeinSmoothing must supply
    pair_conservation as a FIELD, so the theorem sums a list of zeros. A
    non-conserving smoothing is unconstructible, making conservation definitional
    rather than derived. Candidate for the lean-vacuity-audit self-assuming class.

NEXT HONEST STEP (do NOT skip to wiring B-L):
  formalise the Z-grading on the Skein module K(S^3;q) so that L becomes a function
  of a state, then check it returns 0 on a single quark. Only then is Y = B - L
  assemblable. The B half (mu-bar_123) is separately still a conjecture with no
  instance (PR #4597).

Blocks: assembling Y = B - L, which is the LH half of the eightfold-way open item 2.
