---
# qou-o3ta
title: 'BLOCKER MERGE: the metric blocker and the colour-weight blocker are the SAME null vector, and convention D created it'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T13:52:13Z
updated_at: 2026-10-10T07:56:23Z
parent: qou-cdx1
---


Branch: claude/anchor-followups-2026-08-08.

OWNER'S STANDARD: better = more accurate to experiment and/or backed by
canonical derivation. Scored below on both.

## THE MERGE -- one object, two symptoms

Both blockers are the SAME vector: the (1^3) row cap, the q-antisymmetriser,
components (-q^-1)^len(w) on the NF basis. Its Wedderburn weight is
y_(1^3), and under convention D that weight is ZERO.

  * METRIC BLOCKER. A zero weight is a RADICAL of the Markov-Gram form. A
    Lipschitz seminorm built from a form with a radical has a kernel, and
    GramSignature.lean's `lip_kernel_forces_unbounded` (sorry-free) shows the
    Connes sup is then UNBOUNDED whenever the two states separate on that
    kernel vector. So the spectral distance is not merely hard to compute --
    it is +infinity as currently posed.

  * COLOUR-WEIGHT BLOCKER. The same vanishing block is the one the bond family
    cannot reach: sigma^2 = h sigma + 1 closes span{1, sigma_2}, a 2-plane in
    the 4-dimensional V_(2,1), and the (1^3) direction carries no weight to
    push against.

## AND CONVENTION D IS WHAT CREATED IT -- measured, at the proton pin

From tools/pyhecke/python/pyhecke/gram.py (bilinear pairing as that module
builds it):

    C   eigs -0.855067 +0.101797 +0.855067 x3 +3.476950
        det -0.18920521914403668    cond 3.4e+01    NON-singular
    D   eigs -0.752702  0.000000  +0.752702 x3 +4.230339
        det  3.998e-17              cond 4.9e+16    SINGULAR

Under C, y_(1^3) = 0.0227 != 0 and there is NO radical -- under the correct
star pairing C is (6,0,0) POSITIVE DEFINITE. Under D it is (5,0,1), one null
direction, under BOTH pairings.

This is NOT an argument to revert to C. D is the production convention and is
the derived one. It is a statement about WHERE the work is: the excision did
not merely relabel a constant, it changed the SIGNATURE of the pairing every
distance and every projection is built on, and nothing downstream was
re-derived for a degenerate form.

## TWO STOPPERS THAT NEED AN OWNER RULING (from the qou-wgta agent)

  1. pyhecke/gram.py runs `G_INV = np.linalg.inv(G)` AT IMPORT. Under D that
     is singular and NUMPY RAISES NOTHING -- it returns entries to 7.6e15 with
     ||G G^-1 - I|| = 1.64, exported into constants.py, atom.py, molecular.py,
     sdp.py and nine consumers. The file is currently PINNED to C with a
     blocking note. Anyone who "finishes the excision" on that one line
     silently poisons the stack.
  2. observations/neutron-proton-mass-splitting.lean bakes C into the INTEGERS
     (4993 = 10000 z_C). Under D: 1.054110 MeV vs the theorem's asserted
     1.302 +- 0.001, failing by a factor of 248. Against CODATA 1.293 MeV, C
     is +0.66% and D is -18.5%. Not touched; tolerance NOT adjusted.

Item 2 is the sharper one for the owner's standard: on THIS observable the
excised convention is the accurate one. Either the n-p splitting derivation
uses a different pairing than the one D fixes, or D is wrong somewhere, or the
+0.66% was luck. Do not paper over it.

## ATTACK OPTIONS -- METRIC BLOCKER

  [ ] M1. QUOTIENT BY THE RADICAL. Cheapest, and GramSignature.lean already
          names it. Distance becomes finite on the 5-dimensional quotient.
          COST: the quotient kills the (1^3) block = the q-antisymmetriser =
          the totally antisymmetric (fermionic) sector. Check FIRST whether
          the nuclear singlet channel lives there; if it does, this amputates
          the physics it is meant to serve.
  [ ] M2. USE THE STAR FORM tr_M(b_i b_j*), T_w* = T_{w^-1}. Lean-proved PSD
          (`starform_M2_sum_of_squares`, sum of squares). Strictly the right
          object -- an inner product, not an indefinite pairing. Under D still
          leaves the one null direction, so M2 does not REPLACE M1, it makes
          M1 legitimate: you cannot quotient an indefinite form sensibly.
          DO M2 THEN M1, in that order.
  [ ] M3. RESTRICT THE STATE SPACE to states agreeing on the radical. Then
          obj k = 0 and the hypothesis of `lip_kernel_forces_unbounded` simply
          fails -- distance finite with NO quotient and no loss of the block.
          Physically: only compare states of equal (1^3) charge. Strongest on
          the derivation criterion; needs a superselection argument.
  [ ] M4. Q-DEFORM THE SEMINORM so the vanishing block gets nonzero weight.
          Speculative -- would need the weight DERIVED, else it is a fit.
          Lowest priority.

## ATTACK OPTIONS -- COLOUR-WEIGHT BLOCKER (supersedes qou-17gn's list)

  [ ] C1. SHADOW PRICE. Unchanged and still first: it is the gate. Note it now
          inherits the radical problem -- the dual of a degenerate program is
          not unique -- so M2 is a PREREQUISITE, not a parallel track.
  [ ] C2. FROBENIUS PROJECTION onto the reachable 2-plane. Blocked on
          gram-matrix-dual.py (bilinear + C + float64) AND on M1/M2.
  [x] C3. LIFT THE MONOTONE-WORD RESTRICTION -- DEAD. Now Lean-proved dead:
          `trace_conj_eq` / `conjugation_reaches_no_new_values` in
          InterfaceScalar.lean, from cyclicity alone, no convention, no q_0.
  [ ] C4. Q-DEFORMED GRADING of the (2,1) block. Gate on C1.
  [ ] C5. NEW -- ENLARGE THE ALGEBRA. H_3(q) has only three irreps and the
          bond family closes a 2-plane in the only 2-dimensional one. If the
          interface genuinely needs 4 parameters it may simply not fit in
          H_3, and the honest move is H_4 (five irreps, a 3-dimensional block)
          rather than deforming H_3 until it yields. Most expensive; scores
          highest on "backed by canonical derivation" because it changes no
          definition, only the arena. Cost the strand-count blowup first.

## ORDER

  M2 -> M1 (or M3 if superselection is derivable) -> C1 -> then C2/C4, with
  C5 held as the structural fallback if C1's shadow price comes back large.

Per AGENTS.md:779 each of these gets its Lean scaffold BEFORE any Python.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

The metric/colour-weight null-vector merge is a Gram-degeneracy science
question downstream of convention D, not a C site to excise. Belongs with
`qou-cds2`/`qou-v7qj`, not the excision milestone. Keep open, re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## RETRACTION, same session — this bean was CORRECTLY parented and my verdict above was wrong (bean `qou-am5t`)

The 2026-10-10 verdict above says **REPARENT**, on the reasoning that this is the
q0/colour axis rather than the convention axis and therefore the wrong milestone.
**That reasoning is wrong, and `qou-cdx1`'s own title says so**:

> `MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)`

Its body states the three rulings explicitly — **R1** convention D canonical / C
excised, **R2** proton pin canonical, **R3** `bring_color_weighted` canonical.
So the milestone is a THREE-RULING milestone, not a C-excision milestone, and a
q0-pin bean (R2) or a colour-weight bean (R3) sits under it by design.

My §9 paragraph calling the shared milestone an artefact of the two rulings
"landing in the same message" had it backwards: they share a milestone because
the milestone was scoped to cover all three, deliberately.

**This bean stays under `qou-cdx1`. It is not re-parented, and the REPARENT
verdict above is withdrawn.** Everything else in that verdict — that it is live
and worth doing — stands.

Third correction of this session, and the same class each time: a claim about a
bean made without reading that bean's own primary text closely enough. The first
was `qou-m7py` (called satisfied off one grepped line), the second was the
66-unscoped paper classifier.

## Round 76 Progress (2026-11-17T12:02:46Z)
- Advanced in PR `litlfred/qou#8337` (branch `feat/round76-torusmass-pinchoct-gramsig-motivic-spectrahedral-43c1`, head `df1ab810bdd422f72dc74878dc341f5f55564271`).
