---
# qou-wlnx
title: 'M6: redo spectral-decomposition-qvalue in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-d8c7
---

predicted-spectra/spectral-decomposition-qvalue.md:23 defines z = z_C in the chain V_j = z M[0][0] + M[1][0] (12 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed; tr_M^D(tau(2,9))=1.82841 spot-checked). z -> q^3/(q^2+1); F_deg2 0.5904 -> 3.6844 (and not a suppression factor under C either: 4.581 by the stated formula); trace column recomputed. HONEST NEGATIVES: Pauli branch of (iii) gives F=0 (y_(1^3)=0) so Q=0 for every magic shell, no replacement derived; F_Pauli 0.6382 not reproducible (producer hard-coded); two old C table entries were wrong (markov_trace bug qou-ix74). OPEN: Q_bare values and 2-10% error range need a producer re-run; producer rosso-jones-qvalues.py is deprecated and float-only. Stays open.

2026-10-10 (branch claude/spectral-qvalue-d-producer-2026-10-10): producer computations/spectral_decomposition_qvalue_d.py (mpmath, 70 dps, proton q0, z_D) + witness spectral-decomposition-qvalue-d.witness.json. Reproduces PR #7562 D Table 1 traces (0.52693 ... 0.91725), tr_M(T_beta)=0.247298, J(2,9)=7.39357, J(3,4)=16.38509, F_deg2=3.68442. Pauli case: tr_M^D(e_(1^3))~1e-72 so Pauli=0 for every knot and any normalisation of e (asserted). Q_bare^D (published normalisation |log_q ratio|*hbar_q*m_e/3, protons-first ordering): 3H 0.03675 (+97.5%), 14C 0.14379 (-8.1%), 60Co 0.08553 (-73.1%), 90Sr 0.05482 (-90.0%), 137Cs 0.15314 (-70.2%), 210Bi 0.52314 (-55.0%). Combined (F_deg2 for shells>=5, Pauli for filled shell>=5): 60Co 0.31514 (-1.0%, isolated), 90Sr 0.20198 (-63%), 137Cs 0 (-100%), 210Bi 1.92747 (+65.8%). So under D no 2-10% range: 8-98% bare, 1-100% combined; tables updated in interpretation + geometric blocks. PROVENANCE: the deprecated rosso-jones bare_Q (C, ported, verified against a float rerun) gives Sr90 0.0280, not 0.944; it used |Delta ln P|*m_e/3, which differs from the published formula by hbar_q/ln q=0.9496. The 0.944 / 2-10% / F_Pauli 0.6382 figures come from another producer (qvalue-representation-theory.py q-weighted method, quoted in observations/qvalue-observation.md, NOT touched here). Normalised e_(1^3) under C gives Pauli 0.157 for T_beta, not 0.6382; 0.6382 still unreproduced. C-hist traces for tau(3,5), tau(3,4) (1.7614, 0.6861) differ from the old column (1.5586, 0.5850), consistent with qou-ix74. OPEN: no replacement for the Pauli branch; nucleon ordering is an inherited choice; qvalue-observation.md still quotes C figures (F_deg2 0.5904, F_Pauli 0.6382, Sr90 0.944) — separate bean needed.


## 2026-10-10 — qvalue-observation.md scoped (branch claude/qvalue-obs-trivialvortex-2026-10-10, fce3182682)

observations/qvalue-observation.md now labels F_deg2 0.5904, F_Pauli 0.6382, Sr-90 Q_bare 0.944 / 0.557, MAE 4.4 % / RMS 5.4 % as convention-C outputs of the q-weighted method in computations/_deprecated/qvalue-representation-theory.py. That file is float64, uses Z_m = 1/(sqrt q + 1/sqrt q) (convention C), and hard-codes F_DEG2 = 0.5904 / F_PAULI = 0.6382 at lines 45-46 rather than computing them. The block links to the D table in rem:spectral-decomposition-qvalue-interpretation and quotes D figures only from spectral-decomposition-qvalue-d.witness.json: F_deg2 3.68442; Pauli Markov-trace form 0 (y_(1^3)=0); Sr-90 Q_bare 0.05482 (-90.0 %), combined 0.20198 (-63.0 %); ranges 8-98 % bare and 1-100 % combined. It states that the q-weighted stage itself (q / q^-1 channel weights) has NOT been re-derived under D, because the D producer recomputes the corollary's bare normalisation, and that 0.6382 is unreproduced under either convention. validate: 9 issues (baseline).

Still open, NOT closeable: (1) no replacement for the Pauli branch; (2) the q-weighted method has no D producer; (3) the table sibling tbl:qvalue-observation-table-data still carries the C-era q-weighted rows (0.590 / 0.377 F_shell column). It is scoped by the referring prose but was not itself edited.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
