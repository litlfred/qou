---
# qou-17gn
title: 'Colour-weight blocker attack: shadow price + Frobenius projection; option 3 KILLED by trace conjugation-invariance; gram-matrix-dual is geometrically ill-posed'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T13:43:56Z
updated_at: 2026-10-04T15:17:58Z
parent: qou-8lxd
---


Branch: claude/anchor-followups-2026-08-08.

OWNER'S STANDARD, adopted throughout: **better = more accurate to experiment
and/or backed by canonical derivation.** Every option below is scored on both.

## THE BLOCKER, precisely

sigma^2 = h sigma + 1 closes span{1, sigma_2} -- TWO-dimensional. In the
V_(2,1) Wedderburn block that maps to a 2-PLANE inside M_2 (four-dimensional).
So the bond family reaches half the block, `t in [z-h, z]` IS that 2-plane
parameterised, and the isospin projectors live in the other two dimensions.

## OPTION 3 IS DEAD -- killed by trace conjugation-invariance (owner's catch)

The owner asked whether rigid monoidality already says ordering should not
matter. The proposition
`mass-theory/prop-rigid-monoidal-structural-gap-invariance.md` claims something
NARROWER than that -- invariance under "any choice of operator-volume
convention", not under ordering. But the stronger fact comes free from the trace
axiom:

    tr(ab) = tr(ba)   =>   tr(a b a^-1) = tr(b a^-1 a) = tr(b)

So a CONJUGATED interface -- e.g. sigma_1 sigma_2 sigma_1^-1 to reach strands
1<->3, which `chi_monotone_transfer.word_to_mpfr` currently REJECTS as
non-monotone -- has the SAME TRACE VALUE as sigma_2. Lifting the monotone-word
restriction therefore reaches NO NEW VALUES. Option 3 (enlarge the reachable set
by allowing non-monotone words) is refuted by derivation, not by measurement.
Do not spend effort there.

### And the ordering-dependence is NOT a trace defect

qou-c6gx recorded that B depends on the hard-coded `ordering = ['p']*Z+['n']*N`
(3He: ppn 6.7969 vs pnp 7.7794; 4He spread 2.27 MeV) and treated it as alarming.
It is not a violation of trace invariance: `ppn` carries bond multiset {pp, pn}
while `pnp` carries {pn, pn}. Different multisets => genuinely different links,
NOT conjugates, so different traces are CORRECT.

What it does show is that the CHAIN TOPOLOGY is not a well-defined function of a
nucleus -- a nucleus has no ordering. The trace is doing its job; the INPUT is
ill-posed. That is evidence against the chain as a nuclear model (qou-h7mh), not
evidence against the trace.

## DEFECT FOUND: gram-matrix-dual.py is geometrically ill-posed

`computations/gram-matrix-dual.py` computes G, G^-1 and the Frobenius dual
`K_dual = Sum_i c_i (G^-1)_ij b_j`. Two defects:

  (a) it uses the BILINEAR Gram `tr_M(b_i b_j)`, which is INDEFINITE --
      signature (5,1) under C, (4,1)+null under D. With an indefinite form G^-1
      exists but ORTHOGONAL PROJECTION IS NOT WELL-DEFINED: you can project onto
      a null direction and get nonsense. So the Frobenius duals it produces may
      be geometrically meaningless as currently built.
  (b) it is on convention C (`z = 1.0/(q0**0.5 + qi**0.5)`, and in float64) via
      `pyhecke.gram` -- bean qou-wgta item 11.

BOTH are repaired by the same change: use the STAR form
`S_ij = tr_M(b_i b_j*)` with `T_w* = T_{w^-1}` (qou-018h), which is positive
semidefinite -- (6,0,0) under C, (5,0,1) under D with the only defect the
row-cap null direction. Quotient by the radical and projection becomes valid.

## THE LIVE PLAN

  [ ] 1. SHADOW PRICE. Formulate min |B_pred - B_AME| s.t. the interface lies in
         span{1, sigma_2}; take the dual on that constraint. It measures the
         marginal accuracy gained per unit of relaxation -- small means the
         confinement is NOT the blocker and this whole line is misdirected;
         large means it is, and quantifies the price.
         Infrastructure exists: `prop:mass-coefficient-shadow-price`,
         `aK_via_lp_dual.py`, `pn_alpha_lp_dual.py:31` ("dual shadow prices y_i
         tell us which Frobenius-positivity constraints bind"),
         `shadow_price_c_321_q0.py`.
         SCORE: derivation-backed (an LP dual is exact, not fitted) but
         DIAGNOSTIC -- improves no number by itself. Cheap; do it first to
         decide whether 4 is worth funding.

  [ ] 2. FROBENIUS / ORTHOGONAL PROJECTION -- the strongest on both criteria.
         Fix gram-matrix-dual.py per the defect above, then project the target
         onto the reachable 2-plane. Yields the BEST REACHABLE t (a projection,
         not a tuned parameter => derivation-backed) AND a residual norm that is
         a rigorous irreducible-error bound (=> accuracy-relevant). Newly valid
         only because of the star-form positivity.

  [x] 3. LIFT THE MONOTONE-WORD RESTRICTION -- DEAD, see above.

  [ ] 4. Q-DEFORMED GRADING. The symmetric/antisymmetric split of the (2,1)
         block was taken CLASSICALLY, but the Hecke eigenvalues are q and
         -q^-1, an ASYMMETRIC pair, not +/-1. Whether the q-deformed grading
         changes which matrix entries a bond word can reach is open and
         well-posed. NOTE: option 3's death does NOT kill this -- conjugation
         invariance says the trace cannot distinguish conjugates, but a
         different GRADING changes which subspace the bond family spans, which
         is a different question.
         SCORE: derivation-backed if it works; unknown accuracy effect. Gate on
         the shadow price from 1.

## AGENTS.md 779 REMINDER

Items 2 and 4 are new math. Lean scaffold FIRST, before Python. That directive
was violated repeatedly earlier in this session; do not repeat it here.
