---
# qou-qf20
title: 'vacuity-audit tail: 1 real defect of 4, three already adjudicated'
status: completed
type: task
priority: normal
created_at: 2026-09-03T08:57:48Z
updated_at: 2026-09-03T08:57:49Z
---

MEASURED 2026-09-03 on origin/main, from bun run content/pipeline/lean-vacuity-axiom-audit.ts.

Four findings outside the two owned lanes (62 self-assuming-projection = PR #6422 / qou-z9ws; 12 docstring-sorry-mismatch = PR #6471 / qou-q6f8). ONE was a real defect. Three were already adjudicated in docs/audits/lean-vacuity-review-ledger.json before I looked -- my independent reads agree with all three verdicts.

REAL -- like_nucleon_rates_coincide (QOU/QBeta/BondDecayRates.lean:151), proof-no-unused-hypothesis-rfl, major. It read

    theorem like_nucleon_rates_coincide {q : R} (_hq : 1 < q) :
        (1 : R) / q ^ 2 = 1 / q ^ 2 := rfl

which is literally X = X, closed by rfl, with the hypothesis under an underscore because nothing used it. It named the claim that survived the file's 2026-09-01 withdrawal and asserted none of it: 1/q^2 = 1/q^2 holds for every real q and says nothing about nucleon bonds. Banned by AGENTS.md 5 (tautological conclusions).

FIXED to the claim the name makes: the p-p and n-n rates, reached through DIFFERENT expressions (|E2|/|E1| at d=0 versus |E1|/|E2| at d=-h), are equal. Falsifiable -- the ordering error this same file documents made them 1/q^2 and q^2 -- and the proof composes rate_pp and rate_nn, so it genuinely needs 1 < q. lean-direct exit 0; #print axioms [propext, Classical.choice, Quot.sound], no sorryAx. The audit category is gone on re-run.

ALREADY ADJUDICATED, verdicts confirmed independently, no action:
  borromean_crossing_minimal (KauffmanTL3.lean:267, proof-no-decide-masking) -- ledger 'advisory' 2026-08-21. native_decide on a genuinely finite decidable enumeration over all length-<6 3-braid words; legitimate per AGENTS.md 6. The docstring names the added axioms (Lean.ofReduceBool + Lean.trustCompiler) and records a Python enumeration oracle cross-check. Model of honest use.
  parallelogramIntegral_eq_zero_of_differentiable + parallelogramIntegral_inv_sub_eq_two_pi_i (ParallelogramContour.lean, proof-no-provable-axiom x2) -- ledger 'advisory' 2026-08-24, disposition cite-as-axiom-or-prove. NOT provable in current Mathlib, and the file documents why correctly: Cauchy-Goursat exists only for AXIS-ALIGNED rectangles, an affine pullback of a generic parallelogram is R-linear so does not preserve complex differentiability, and Mathlib lacks both triangle integrals and Goursat for simplices. Both axioms were UNSOUND until 2026-08-24 (False derivable; the second inconsistent BY ITSELF at the degenerate omega1=omega2=0) and were repaired with correct hypotheses. The file also states that Differentiable C f is the SOUND repair rather than the SHARP one and leaves the sharpening open deliberately.

TAKEAWAY for whoever reads the audit's headline count next: '83 candidates' includes items already carrying agent verdicts. Read the ledger before treating a number as a backlog. proof-no-provable-axiom in particular fires on the SHAPE of an axiom declaration and cannot distinguish an honestly-documented Mathlib gap from a laundered assumption -- these two are the former, and are close to a worked example of how to declare one.
