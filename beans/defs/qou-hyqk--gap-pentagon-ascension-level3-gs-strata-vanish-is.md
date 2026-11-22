---
# qou-hyqk
title: 'GAP: pentagon ascension (level>=3 GS strata vanish) is a hypothesis'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T10:47:15Z
updated_at: 2026-11-22T11:58:12Z
parent: qou-uwyf
---

phi_q_tower_algebraic_stratification_of_pentagon assumes f S = 0 for |S|>=3. Decide whether this is provable from a definition of f (Phi_q of Frobenius norm of V_S) or is a genuine conjecture; if the latter, record it as such (do not close while open).

Follow-up to qou-02q4 (PR #9001, merged). Owner 2026-11-22: 'Fill the gaps ... Make them beans and work them.' Session https://claude.ai/code/session_01Qmmkt5ngCVGxt8cKmAnoR2

2026-11-22 finding: pentagon ascension has no proof in the corpus. The proof .md step 3 cites rem:mass-endomorphism-jet-tower's narrative rewrite; JetProlongation.lean carries it as an operator-lift typeclass (a hypothesis). So the block's 'unconditional' wording overstates: the stratification is proved only given ascension. Owner decision needed: (a) relabel the block conditional on pentagon ascension, or (b) attempt a proof from a concrete definition of f S. Stays open.

2026-11-22 owner '1 2'. Option 1 done (block now conditional; owner-rulings row). Option 2 attempt: proved phiQTrunc_eq_zero_iff (truncated Phi_q = 0 iff q^m x = 1 for some m) and phiQTrunc_zero (=1). So with the def:phi-q-piece summand f S = Phi_q(x_S), the vanishing form of ascension is false except at resonant x_S. The narrative's ascension is a REGROUPING (level-3 term = lower factors + residual at jet level n+1), which needs (a) a definition of the full tower across jet levels and (b) a concrete InterLevelLift instance (none exists) plus the Faddeev-Kashaev pentagon in a quantum torus. Not provable from current definitions. Stays open; next decision: restate the hypothesis as the regrouping, or leave as bookkeeping.

2026-11-22 owner 'Works of Pentagon' (option 1): hypothesis restated as regrouping. phi_q_tower_algebraic_stratification_of_regrouping proves stratification mod J given (level>=3 sum - low-stratum correction delta) in J; vanishing form is delta=0, J=bot. PR #9018. Ascension itself still unproved (needs J from jet tower, delta from Faddeev-Kashaev pentagon). Stays open.

2026-11-22 coordination note: before defining J from the jet tower, coordinate with thread 'Give descent, Reidemeister, Schur-Weyl honest Lean' (cmsg_01H9cBvdoT3vcjHkS7QAyTqgArV4fqfX1pv4MzvPNQug8A), which is switching the tower definition and descent Step 1 to the jet module (S⊗S)/I^2. J should be built from that module.
