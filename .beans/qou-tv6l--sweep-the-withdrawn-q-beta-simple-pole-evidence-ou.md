---
# qou-tv6l
title: Sweep the withdrawn Q_beta simple-pole evidence out of 8 durable artifacts
status: todo
type: task
priority: normal
created_at: 2026-08-23T22:22:28Z
updated_at: 2026-08-23T22:44:31Z
---

qou-8ofm / qou-frch (2026-08-10) established that the SDP c_k extractor emitted the model's accuracy floor as data, and that R(q0) being a single scalar means at most ONE rung is determinable. Both fixed the producer; neither swept the consumers. PR #1727's simple-pole verdict was read off k=8,9,10, which are deep in the stalled range, so all three cited signatures (flat c_k*u^k, ratio test -> 1/u, branch-fit beta=0.999) are the same arithmetic identity, and residue A = 1.804e-15 is the floor rescaled by u_subst. Measured against the extractor's own quotients: |c_k u^k| = floor to 1e-21, ratio -> 1/u to 2.4e-15. Audit: docs/audits/2026-08-23-qbeta-simple-pole-evidence-is-the-residual-floor.md. NOT refuted: the pole's existence (independent support in PR #1713 radius-of-convergence and PR #2454 algebraic Q_A(silver)=0). Withdrawn: that this evidence establishes the pole TYPE or its RESIDUE. The Lean is a 3b-cond conditional class and is unaffected; only its docstring's empirical justification is. Artifacts to sweep: q-beta-radius-of-convergence-gate.lean:11 docstring; docs/coordination/1ppq-qbeta.md (rows 2026-06-02 / 06-03 / 06-22, dead-ends table, open-target table); the 2026-06-02 originating audit; 2026-06-04 residue-a-unblock-kernel-scope; 2026-06-04 precision-ceiling plan+verdict; 2026-06-04 residue-a-followup plan+verdict; 2026-06-04 mixed-chains-plan; 2026-06-22 two-pole-ladder. Not done unilaterally: the rewrite is opinionated and spans a coordination ledger.

SHARPENED by the convention finding: PR #1727's floor f = 2.118e-13 was the muon + convention-C floor, so the simple-pole evidence is C-frame as well as floor-derived. The floor IDENTITY is arithmetic and frame-independent; only the floor's magnitude is frame-dependent. That is a second, independent reason the eight downstream artifacts cannot be quoted as they stand, and it means the sweep should scope them to C rather than merely annotate the floor issue.
