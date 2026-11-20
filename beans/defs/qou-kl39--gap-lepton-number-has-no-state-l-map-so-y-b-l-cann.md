---
# qou-kl39
title: 'GAP: lepton number has no state->L map, so Y = B - L cannot be assembled'
status: todo
pr: 8211
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-08-09T11:07:51Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-20sx
---

Found 2026-08-09 while checking whether the corpus's existing lepton number closes
the L half of Y = B - L (proved requirement: HyperchargeBatteryReduction.lean).

WHAT EXISTS (folio/quantum-observable-universe/predicted-spectra/lepton-number-categorical.*):
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


UPDATE 2026-08-10 — the stated bridge is PROVED IMPOSSIBLE; next step narrowed.

lepton-number-categorical-properties.md offered the state<-transition bridge as a
Z-grading on the Skein module by smoothing count. That grading CANNOT EXIST:
the skein relation L+ - L- = (q-q^-1)L_0 is inhomogeneous (LHS grade g, RHS grade
g+1), and distinct homogeneous components meet only in 0, so both sides vanish.
Imposing it annihilates every smoothing => L identically 0, the one value it
cannot take. Proved sorry-free in
QOU/StandardModel/LeptonNumberGradingObstruction.lean (3 theorems, axioms =
[propext, Classical.choice, Quot.sound], negative control passes). The hypothesis
is deliberately weak (disjointness only, NOT full direct-sum), so it cannot be
evaded by weakening 'grading'. Scope-(b), invariant cited. The .md paragraph is
corrected in place.

NEXT STEP (narrowed, still open): an inhomogeneous relation is what a FILTRATION
tolerates -- the skein relation lowers filtration degree by one. That is the
Vassiliev/finite-type filtration, already in-corpus at QOU/KnotTheory/Vassiliev/
(finiteTypeSubmodule_mono, IsFiniteType, symbol, MilnorVassilievBridge). Two
reasons to look there, neither a result: (1) the filtration is by powers of
(q-q^-1), exactly the coefficient a smoothing carries, so 'smoothing count' and
'finite-type degree' are plausibly the same counter; (2) mu-bar_123, the B-half
candidate, is degree-2 Vassiliev -- if L is also a filtration degree then B and L
live in ONE structure.

So the task is no longer 'find a state->L map' but 'test whether the Vassiliev
filtration degree supplies one, and whether it returns 0 on a single quark'.
Caveat 2 from the original bean (no quark carries L in the corpus) is untouched.


UPDATE 2 (2026-08-10) — stronger obstruction; my own filtration suggestion was wrong.

(a) CORRECTION to update 1: the Vassiliev filtration grades INVARIANTS
    (IsFiniteType (m) (v : K -> R); finiteTypeSubmodule : Submodule R (K -> R)),
    NOT states. It cannot by itself supply the state->L map. That suggestion is
    withdrawn.

(b) STRONGER RESULT: no function of the UNFRAMED KNOT TYPE can reproduce the
    corpus L table at all. The table sends nu_e -> unknot (L=+1) and
    nubar_e -> mirror unknot (L=-1). The unknot is AMPHICHIRAL (bounds a disk,
    isotopic to its mirror), so those two rows assign +1 and -1 to the SAME knot.
    Proved in QOU/StandardModel/LeptonNumberCarrierChirality.lean:
      no_lepton_number_on_amphichiral_carrier  (NO axioms)
      mirror_must_move_the_carrier             (NO axioms)
      chiral_carrier_admits_lepton_number      ([propext])
    The third is the honesty check: the obstruction is EXACTLY amphichirality
    and nothing more, so this rules out the unknot as neutrino carrier, not the
    idea. Charged rows unaffected (the trefoil is chiral).

NEXT STEP — exactly two repairs exist:
  1. give the neutrino a CHIRAL carrier (the unknot cannot work); or
  2. define L on FRAMED knots -- framing +n vs -n are distinct even over an
     amphichiral knot, so the mirror acts freely there.
Route 2 is the interesting one: that framing datum is T(t)
(def:strand-twist-datum), the SAME object the eightfold-way chapter carries for
hypercharge. If L needs framing while Y needs a framing-independent second
invariant, that tension is worth making explicit before either is wired.
Neither route pursued yet.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress (2026-11-16, PR #8211)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ElectroweakWeinbergTraceLeptonFiltrationHiggsAndVevScale.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`8ca6e00d291446c4a5427c3266d272e793c16d8e`, `scriptHash: f6006da25e32`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8211`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8211, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
