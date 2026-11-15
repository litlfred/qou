---
# qou-jqjc
title: 'FIBRE-F: complex-volume witness emits assertions:[] with allPassed -- machine surface reads as verified while nothing is checked'
status: completed
type: task
priority: normal
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-08-23T17:20:00Z
---

Evidence: computations/complex-volume-unification.witness.json has assertions:[] with allPassed set; a consumer reading allPassed sees a pass over zero checks. The PRODUCER DOCSTRING IS HONEST -- it states the single-frakV descent "is the open conjecture, not proved here" -- so this is a machine-surface defect, not a prose defect, and the fix must not be described as correcting a false claim. Im is ASSIGNED from q_beta_substrate, not derived from a trace. Fix: emit assertions for the checks that actually run (Re vs AME, Im vs CODATA) plus a verdict naming the descent unproved. Blocked by nothing; advances no physics. Doc: docs/audits/2026-08-19-frakv-fibre-workplan-options.md option F.

DONE 2026-08-19. The witness now emits 2 real assertions and 3 caveats instead of assertions:[] under allPassed.

WHAT IS ASSERTED, and only what is actually checked:
  im_qbeta_matches_codata          0.7836458273746213 vs 0.7823334093100222, tol 0.2% -> PASS (0.168%)
  im_channel_isotope_independent   spread 0.0 across 2H/3H/3He/4He, tol 1e-30 -> PASS

WHAT IS DELIBERATELY NOT ASSERTED:
 * NO Re assertion. The log-trace binding is 22-69% from AME (2H 27.4%, 3H 21.8%, 3He 36.7%, 4He 69.3%). That is a recorded gap, not a passing test, and asserting it would be false.
 * NOT the single-frakV descent. Im is ASSIGNED from q_beta_substrate, not derived from a trace. A caveat now says so and says allPassed refers to the two assertions and nothing else.

NO RATCHET REGRESSION. Values passed as STRINGS (the drained convention, qou-t0rf), so raw-float64 stayed at 47 -- unchanged. Gates: REGRESSED 0, shape guard "no witness lost content", the only RED is the pre-existing gswz witness.

ENVIRONMENT PRESERVED. scipy and clarabel were genuinely missing from this container, which is why an earlier regeneration would have dropped them. Installed at exactly the recorded versions (scipy 1.17.1, clarabel 0.11.1) BEFORE regenerating, per the witness writer own instruction to install rather than commit a weaker record. The environment block is byte-identical.

SECOND FIX, found while doing this: the PRINTED bar-norm caveat still claimed "the color-weighted word bakes q0 and cannot re-lift at q^-1" -- which the table printed directly above it disproves, since the q0^-1 column is computed for every row. I had corrected the code COMMENT earlier in the session but missed this user-visible line. Now states the real reason: the product is NEGATIVE so it has no real square root, which is stronger than "not yet computable" and means the claim should be retired rather than repaired.
