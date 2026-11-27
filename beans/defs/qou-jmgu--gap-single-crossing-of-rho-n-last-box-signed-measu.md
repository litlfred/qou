---
# qou-jmgu
title: 'GAP: single crossing of rho_n (last-box signed measure) for all n>=79, which implies M1>0'
status: todo
type: task
priority: normal
created_at: 2026-11-27T22:17:45Z
updated_at: 2026-11-27T23:14:36Z
parent: qou-h315
---

Conjecture (SC). Let rho_n(s) = E_PG[1{i_n+j_n=s}/(r_{n-1} r_{n-2})] over Plancherel growth, with r_k = c(k+1)-c(k) and (i_n,j_n) the 1-indexed position of box n. It is a mass-zero signed measure, and M1(n) = (n(n-1)(n-2)/3) sum_s s rho_n(s) (Jucys-Murphy + Young orthogonal form; verified exactly against the hook formula n=3..7).
Claim: rho_n is <=0 then >=0 in s (one sign change). Checked exactly for n=3..40 (computations/deltalambda/wlambda_covariance_M1_jucys_murphy_form.py). With the Lean lemma YoungDiagramKernelSingleCrossing.firstMoment_pos_of_single_crossing and the n<=78 table, (SC) for n>=79 gives M1>0 for all n, with no finite-n analytic bound needed.
OPEN: no proof. Suggested attack: Kerov transition measures (rho_n is a three-step transition average). Audit: docs/audits/2026-11-27-covariance-kernel-M1-jucys-murphy-form.md. Do not close while the conjecture is open.

2026-11-27: (SC) re-checked exactly for n = 41..49 with plancherel_growth_side + single_crossing. Single crossing holds for all of them. The threshold is s = 11 for n = 31..46 and moves to s = 12 at n = 47..49. Each n takes 1-6 min and grows about 1.25x per step, so n = 50 was not reached within the 1 h run budget. Still open: no proof.
