---
# qou-580o
title: 'UNDISCLOSED C->D FLIP: the PSLQ probe''s z was switched to convention D inside a Lambda-Cl2 naming commit, and its witness was never regenerated'
status: in-progress
type: task
priority: normal
created_at: 2026-08-18T08:21:15Z
updated_at: 2026-08-18T08:22:07Z
---

## Found by re-running, not by reading (2026-08-18, while draining qou-zdz5)

I renamed one mislabelled dict key in
computations/probes/qbeta_ck_basis_constrained_pslq.py and re-ran the producer
to regenerate its witness.  A key rename cannot move a number.  The re-run
moved this:

  c3_reproduced_canonical   committed  -2.02018812814143945582016855395
                            re-run     -974.382476607697851630950275826
  assertion 'passed'        committed  true
                            re-run     FALSE  (allPassed true -> false)

-974.38 is EXACTLY the registry §9g convention-D muon c_3.

## Cause: the probe's z was flipped C -> D, in a naming-drain commit

  90140791d 2026-08-10  z = 1 / (mp.sqrt(q) + 1/mp.sqrt(q))     <- convention C
  98e78d396 2026-08-15  z = q**3 / (q**2 + 1)                   <- convention D

98e78d396 is titled 'fix(vol-4_1): 9 Lambda<->Cl2 sites -- this does NOT
complete the drain'.  A CONVENTION CHANGE rode inside a NAMING commit, and the
witness was not regenerated.  The committed witness has been C-frame, and
passing, ever since; the failure only appears if you actually re-run.

Note the pre-flip spelling: 1/(sqrt(q) + 1/sqrt(q)) IS sqrt(q)/(q+1) exactly.
That is one of the DETECTOR-BLIND C spellings AGENTS.md warns about, and it is
why convention-c-producer-audit.py's '0 actionable producers' does not mean the
C surface is clear.  Live example of the documented blind spot.

## What I did NOT do, deliberately

I did NOT commit the regenerated witness.  Committing it would:
  (a) RATIFY an undisclosed convention flip that no ruling authorised for this
      probe, and
  (b) wire c_3 = -974 into the corpus -- which qou-cds1 states explicitly is
      'a sensitivity measurement, not a proposed value.  Do not wire it
      anywhere.'
I also did NOT revert the z line to C: the owner ruling makes D canonical, so
silently reverting would be its own unilateral convention decision.

So the witness stays stale AND is now documented as stale.  That is the honest
intermediate state; ratifying either frame is the thing to avoid.

## What resolution requires (belongs with qou-cds1)

The ladder must be RE-DERIVED under D, not re-evaluated -- proved by
QOU.QBeta.decayLadder_zC_threeRow_ne_zero.  This probe currently does exactly
the forbidden thing: it substitutes z_D into the C-frame functional form
alpha = (z-1)h/2.  That is why it returns -974 rather than anything meaningful.
Fixing the witness is downstream of deriving the D-frame phase.

## Kept from the same pass (real naming fixes, no numbers touched)

  docs/audits/2026-06-03-m-tau-knot-prediction-falsification.md:18
    Vol(4_1) = 2\Lambda(\pi/3) -> 2\,\mathrm{Cl}_2(\pi/3) = 6\Lambda(\pi/3)
    (the value 2.02988 was already correct -- wrong NAME, right NUMBER)
  qbeta_ck_basis_constrained_pslq.py:313  dict key
    'Vol(4_1)=2*Lambda(pi/3)' -> 'Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)'
    (vol41 = 2*Im Li_2(e^{i pi/3}) = 2*Cl_2(pi/3), computed correctly)
