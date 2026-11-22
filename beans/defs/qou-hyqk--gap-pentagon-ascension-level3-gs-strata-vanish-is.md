---
# qou-hyqk
title: 'GAP: pentagon ascension (level>=3 GS strata vanish) is a hypothesis'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T10:47:15Z
updated_at: 2026-11-22T11:06:52Z
parent: qou-uwyf
---

phi_q_tower_algebraic_stratification_of_pentagon assumes f S = 0 for |S|>=3. Decide whether this is provable from a definition of f (Phi_q of Frobenius norm of V_S) or is a genuine conjecture; if the latter, record it as such (do not close while open).

Follow-up to qou-02q4 (PR #9001, merged). Owner 2026-11-22: 'Fill the gaps ... Make them beans and work them.' Session https://claude.ai/code/session_01Qmmkt5ngCVGxt8cKmAnoR2

2026-11-22 finding: pentagon ascension has no proof in the corpus. The proof .md step 3 cites rem:mass-endomorphism-jet-tower's narrative rewrite; JetProlongation.lean carries it as an operator-lift typeclass (a hypothesis). So the block's 'unconditional' wording overstates: the stratification is proved only given ascension. Owner decision needed: (a) relabel the block conditional on pentagon ascension, or (b) attempt a proof from a concrete definition of f S. Stays open.
