---
# qou-vibo
title: 'Session: M_n(K) magnitude gap -- can new 24h math close it'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T06:16:39Z
updated_at: 2026-10-04T15:13:56Z
---

FINDING 2026-08-29 (honest, scope-a): the binding MAGNITUDE gap is GEOMETRIC, not algebraic, and the new 24h math does NOT close it.
- Map (workplan 2026-07-11-mnk-derivation-gaps.md): B(K)=Sum_n m_e a_D^(n) w_n M_n(K). Everything algebraic DERIVED (a_D^(n) na-Stokes; per-bond b*; bond-extensivity; Milnor M_n of a GIVEN link; M2=C(A,2) A<=4; R(q,x)=x^2-tau x+1 kernel mostly done, z2bn, lambda+=2.1846). OPEN = M_n(K) coordination geometry: GAP-1 max-contact packing A>=5, GAP-2 M3 Borromean-triple count. He4 magic surplus 14.95 MeV = the M3 term.
- NOT from SDP: operator-selection SDP is intensive (per-nucleus n_target), no propto-A output. (agent map confirmed.)
- sibling M1>0 (qou-k5r5) is a SEPARATE leg (Delta_lambda super-exp growth bound = Plancherel cov moment), does not touch magnitude.
- MY Molien normalizer-log idea = REDISCOVERY of the already-Lean-proved B_sym (A-1) linear chain (BsymLinearChain.lean; 2026-06-16-b-sym-linear-chain-closed-form.md). Per-bond E0*|log(1+q0 zD-q0^2)|=3.36 MeV, extensive, zero-fit -- but +51% on deuteron, (A-1)->3x / C(A,2)->6x growth vs AME 12.72x. Touches the SOLVED 2-body piece only, NOT the open >=3-body cooperative alpha-unit magnitude.
- Actionable magnitude frontier = GAP-2: run validated binding_mn_milnor_linking.py mu-bar tower on He4 link, count nonzero Borromean triples, test m_e a_D^(3) w_3 M3(He4) vs 14.95 MeV, no tuning (anti-fit: w_3 from na-Stokes+deuteron, NOT from He4 residual). Possible connection: fake-degree cyclotomic prod(1-u^d_i) <-> GAP-3 Habiro (q-1)^2 Phi kernel, but GAP-3 mostly done (join z2bn, don't parallel).

GAP-2 done (qou-klgu): He4 magic surplus is NOT Milnor -- max-contact K4 has all lk=1 so higher mu-bar indeterminate mod 1 => M3_irr=M4=0 (scope-b, Milnor indeterminacy). Surplus lives in the non-link-invariant SU(4)[1^4] shell object. Milnor route works for loosely-bound low-lk terms (triton triple = Borromean +1), blind to tightly-bound He4.



## Summary of Changes

Session log closed 2026-10-04 (owner decision 2): open children were reparented to programme epics and prose follow-ups extracted as their own beans. Kept as a record, not deleted.
