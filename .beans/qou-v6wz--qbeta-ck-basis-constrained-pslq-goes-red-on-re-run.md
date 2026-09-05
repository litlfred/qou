---
# qou-v6wz
title: 'qbeta-ck-basis-constrained-pslq goes RED on re-run: c3 moves by 972, and the witness is stamped q0-independent while carrying q0_canonical'
status: todo
type: bug
priority: high
created_at: 2026-09-04T11:46:20Z
updated_at: 2026-09-04T11:46:20Z
---

FOUND 2026-09-04 as a hook-triggered producer re-run in a working tree, NOT by looking for it. Re-run against main at eb2f4588ce. NOT MY BRANCH'S CHANGE - reverted rather than committed, so this bean is the only record. Reproduce with: run the producer for computations/probes/qbeta-ck-basis-constrained-pslq.witness.json on current main and diff.

THE WITNESS GOES RED. allPassed: true -> false. Its own self-check: computed 1.5835e-30 -> 972.3619589513947 against tolerance 1e-08, passed false.

c3_reproduced_canonical: -2.02018812814143945582 -> -974.382147079536184945.

THE ANCHOR RE-PIN DOES NOT EXPLAIN IT, by a factor of 7.8 MILLION. q0_canonical moved 1.1099785955573347... -> 1.109978595642739... which is the retired pin -> the live CODATA-2022 pin, a 0.0769 ppb move (the qou-3f7a drain, correct and expected). With u^3 = 6.178685604e-7 the amplification gives a c3 shift of 1.245e-04. The observed shift is 972.362. Ratio 7.813e+06. So the migration is a red herring; something else changed.

THE LIKELY CAUSE IS IN THE SAME DIFF: anchor_slope_dc3_dq 4.65741e+6 -> 3.81298e+6. That is exactly the stale-4.66e6 -> corrected-3.84e6 figure AGENTS.md documents at length (the stale-c3 twin; beans qou-3nva / qou-kt8o). So a sibling corrected the slope - correctly - and c3_reproduced, which is computed FROM the slope, was not reconciled. Note the failing check's 'computed' value 972.3619589513947 IS the c3 shift 972.362 to ten digits: the check is measuring exactly this discrepancy.

SECOND DEFECT, INDEPENDENT AND WORSE FOR THE AUDIT SURFACE. The refreshed witness is stamped
    q0Anchor: 'independent'
    q0AnchorReason: 'producer declared q0-independent at the stamp site (q0_anchor=False): no q0-dependent field in this witness'
while the witness plainly carries q0_canonical AND c3_reproduced_canonical, both q0-dependent. The stamp contradicts the file it is on. A q0-dependent witness labelled q0-independent escapes the q0-anchor-flip audit entirely - it will never be reported as a flip no matter which pin it is on. Verify at the producer's stamp site (q0_anchor=False) before fixing; the reason string suggests the flag is hand-set rather than derived from the emitted fields.

UNRELATED AND CORRECT, noted so nobody 'fixes' it: the key rename 'Vol(4_1)=2*Lambda(pi/3)' -> 'Vol(4_1)=2*Cl_2(pi/3)=6*Lambda(pi/3)' with the VALUE unchanged (2.02988321281930725004240510855) is the Lambda-vs-Cl_2 naming drain (qou-zdz5) landing properly.

WHY THIS IS NOT MINE TO FIX HERE: PR #6584 is the eightfold/hyperbolic-volume arc; this is the c_k ladder producer, a different domain, and the change that broke it came from main. Fixing it would widen the PR and the reviewer is not loaded on that area. Also do NOT make it green by widening the tolerance or re-baselining - AGENTS.md forbids that explicitly; fix at the producer by reconciling c3_reproduced with the corrected slope.
