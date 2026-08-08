---
# qou-h7mh
title: 'binding: the gap is coordination geometry, not a missing force term — derive the bond count from the SU(4) partition shape'
status: todo
type: task
created_at: 2026-08-08T20:51:00Z
updated_at: 2026-08-08T20:51:00Z
---

MEASUREMENT (read-only, this session). B_AME / B_sym_chain on the most-bound isotope at each A:

    A       4     6     9    12    16    24    40    56    90   140   208   238
    ratio 2.742 1.738 1.837 2.160 2.169 2.175 2.144 2.187 2.122 1.997 1.849 1.771

A plateau at ~2.15 across 12 <= A <= 90, a deficit below A~12, a decline above A~100, and a 4He spike to 2.742. That is the SEMF decomposition — volume/saturation, surface, Coulomb (~Z^2), closed shell — emerging as a COORDINATION RATIO against the framework's own chain, with nothing fitted.

THE DEFECT IS TOPOLOGICAL, NOT ENERGETIC.
  * bond ENERGIES are right: the deuteron is a single p-n bond and B_AME/B_chain = 1.00 exactly.
  * bond COUNT is wrong: B_sym = alpha[(Z-1)L_pp + L_pn + (N-1)L_nn] walks a 1-D chain of (A-1) bonds through a 3-D object.
  * all-pairs is the other extreme and over-binds with no saturation: B_AME/B_allpairs falls 0.996 (2H) -> 0.100 (56Fe).

Isospin/8-fold-way content is ALREADY present — L_pp=0.6945, L_pn=0.5336, L_nn=1.237 are distinct, so asymmetry is built in. What is missing is geometry, not flavour.

THE LEVER ALREADY EXISTS: atom_braid_word_3A(Z, N, *, m_pp=1, m_pn=1, m_nn=1, ...). The chain is the m=1 special case.

DO NOT JUST FIT m_*. Tuning them to reproduce 2.15 buys a good table and costs the parameter-free claim, which is the point of the framework (cf. the dashboard header: 'lambda_A fit + naive Vol*tr_M both EXCISED').

PROPOSED ROUTE. B_gate and B_sym currently use DISJOINT information about the same nucleus: B_gate takes the SU(4) partition lambda's WEIGHT (scalar, ln 1/W_lambda) and discards its shape; B_sym takes a chain topology and ignores lambda entirely. The Young-diagram shape of lambda IS an occupancy geometry. Deriving the bond count from it would unify the two forms and stay parameter-free. Acceptance: the derived coordination reproduces the ~2.15 plateau and its A-dependence WITHOUT a fitted constant.

TWO DEFECTS FOUND ON THE WAY (independent of the above):
  * B_sym breaks for Z=0 — the (Z-1) coefficient goes negative, so a pure-neutron system gets a spurious -L_pp. It also hard-codes exactly one p-n bond regardless of composition.
  * L_nn (1.237) > L_pp (0.695) > L_pn (0.534) makes the p-n bond the WEAKEST, yet the deuteron binds and the dineutron does not. Nothing breaks today (the deuteron is the single-L_pn case and comes out exact), but the ordering should be understood before coordination multiplies these up.

Also: B_gate and B_vol both report 7.58 MeV for a FREE nucleon, where B_AME = 0 by definition. The 7.58 is a_V, the per-nucleon saturation constant, and deriving it is legitimate — but printing it in a binding column against zero is a category error, and makes err gate read 0.00 as though it were a perfect score. Suppress to em-dash at A=1.
