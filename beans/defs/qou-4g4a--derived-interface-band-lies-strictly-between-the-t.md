---
# qou-4g4a
title: 'DERIVED: interface band lies strictly BETWEEN the two isospin weights -- the two NN mechanisms compute on disjoint sets'
status: todo
pr: 8215
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T14:09:04Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---


Branch: claude/anchor-followups-2026-08-08.
Lean: folio/quantum-observable-universe/lean/QOU/QBeta/GramSignature.lean,
section BandSeparation. sorry-free, lake build exit 0,
#print axioms = [propext, Classical.choice, Quot.sound] on all four theorems.

## THE RESULT

Measured at q0 = 1.1099785827513808076 under convention D:

    mu_-  (T=0)       0.24729788674803459841     63.22 % BELOW the floor
    z - h  (floor)    0.40362773835082593616
    z      (ceiling)  0.61268803714646525160
    mu_+  (T=1)       0.75270211325196540159     22.85 % ABOVE the ceiling

The admissible interface band [z-h, z] lies STRICTLY BETWEEN the two isospin
weights. No admissible d reaches either one.

Reductions, both proved as conditionals with the q-condition explicit:
  mu_+ > z    <=>  z(q+q^-1) < z+q^-1   <=>  q^5 < q^2+1   holds for q < 1.193859
  mu_- < z-h  <=>  q - z < (z-h)(q+q^-1)                   holds for q < 1.465571
q0 clears both with room -- 7.56 % margin on the tighter. NOT a knife-edge, and
not fixable by a better q.

## WHY IT MATTERS

Two mechanisms have been running side by side without ever being shown to be the
same object:

  * ISOSPIN selects the channel. mu_- < mu_+ so T=0 binds harder, matching the
    one bound NN channel in nature. Proved:
    InterfaceScalar.mu_singlet_lt_mu_triplet, singlet_binds_more.
  * THE INTERFACE produces the number. One sigma_2 bond, mu = z + d,
    d in [-h, 0], B = -alpha ln mu.

They compute on DISJOINT SETS. Using the T=0 projector AS the interface is not
merely unmotivated -- it is unavailable. This is the colour-weight blocker of
qou-17gn read off on the observable side, where for the first time it is
QUANTITATIVE: the targets miss by 63 % and 23 %.

## CONVENTION-DEPENDENCE -- state it, do not bury it

The LOWER separation is a D phenomenon. Under C, mu_- = 0.303675 sits INSIDE the
band [0.290260, 0.499320]; only the upper separation survives there.

So D gains and loses:
  GAINS   the band now contains B_AME(2H) at d = -0.11923 h. Under C the whole
          band sat 30.69 % above the deuteron -- the old impossibility result.
  LOSES   the singlet's reachability (this bean), the Gram invertibility
          (qou-o3ta), and the n-p mass splitting (C +0.66 % vs CODATA, D -18.5 %).

Third place D trades one agreement for another. The pattern is the owner's to
rule on, not an agent's to bury.

## WHAT THIS KILLS

Tuning d, choosing a crossing sign, adding a writhe term, or picking a different
q CANNOT close a gap the band is on the wrong side of. Any repair must change
the ARENA:
  * C5 -- enlarge H_3 to H_4 (five irreps, a 3-dimensional block). The bond
    family closes a 2-plane in H_3's only 2-dimensional block; if the interface
    genuinely needs more, H_3 cannot hold it.
  * or a genuinely different PAIRING between the isospin label and the bond --
    the two need not be the same scalar. Nothing yet says B = -alpha ln(mu_iso).

## WHAT DOES NOT FOLLOW -- guard against over-reading

  * This does NOT say the deuteron is unreachable. It IS reachable, at
    d = -0.11923 h, mu_req = 0.5877624445555949099. What is unreachable is the
    ISOSPIN WEIGHT, so the deuteron's d has no derivation from isospin yet.
  * B_pn from the production dashboard is 2.832825 MeV against AME 2.224566,
    +27.3 %. That is the live error, NOT the 163 % that comes from misreading
    mu_- as a deuteron prediction. mu_- = mu_pp * mu_nn is a TWO-bond quantity,
    B(T=0) = B_pp + B_nn = 5.8485 MeV, and quoting it for 2H is a double count.

## A LEAD, EXPLICITLY NOT A RESULT

mu_req = 0.5877624445555949099 and  z - hbar_q/4 = 0.5879176081354006250,
a relative miss of 0.0264 %. That is ~100x better than best-of-12 chance for the
candidate list I screened, which is suggestive and nothing more. I picked the
list partly by eye and there is no derivation of the /4. DO NOT put this in the
paper. Either derive the quarter-Reeb step or drop it.

## NEXT

  [ ] Prove rad(S) = the (1^3) block as a SUBSPACE, not just at trace level.
  [ ] Prove rad is a two-sided IDEAL (needed for H_3/rad to be an algebra).
  [ ] Prove the quotient form is positive DEFINITE, not merely PSD.
  [ ] Then C1 shadow price, now well-posed.
  [ ] Cost out C5 (H_4) -- strand-count blowup first.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (PR #8215)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`FreeNucleonPrecisionStraddleDefect.lean`, `TowerPartitionGrowthAndWeightSubstitution.lean`, `InterfaceScaleFloorAndBandDisjointness.lean`, `SWaveAntisymmetryIsospinGrading.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact integer-partition DP probe (`computations/probes/free_nucleon_straddle_h3a_band_isospin_probe.py`) and stamped witness (`computations/probes/free-nucleon-straddle-h3a-band-isospin-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8215 (`ready: 5d009c2bc892c5362b5b72a46c0f7f2e162d8d40`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8215, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
