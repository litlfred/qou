---
# qou-jmgu
title: 'GAP: single crossing of rho_n (last-box signed measure) for all n>=79, which implies M1>0'
status: todo
type: task
priority: normal
created_at: 2026-11-27T22:17:45Z
updated_at: 2026-11-28T00:12:20Z
parent: qou-h315
---

Conjecture (SC). Let rho_n(s) = E_PG[1{i_n+j_n=s}/(r_{n-1} r_{n-2})] over Plancherel growth, with r_k = c(k+1)-c(k) and (i_n,j_n) the 1-indexed position of box n. It is a mass-zero signed measure, and M1(n) = (n(n-1)(n-2)/3) sum_s s rho_n(s) (Jucys-Murphy + Young orthogonal form; verified exactly against the hook formula n=3..7).
Claim: rho_n is <=0 then >=0 in s (one sign change). Checked exactly for n=3..40 (computations/deltalambda/wlambda_covariance_M1_jucys_murphy_form.py). With the Lean lemma YoungDiagramKernelSingleCrossing.firstMoment_pos_of_single_crossing and the n<=78 table, (SC) for n>=79 gives M1>0 for all n, with no finite-n analytic bound needed.
OPEN: no proof. Suggested attack: Kerov transition measures (rho_n is a three-step transition average). Audit: docs/audits/2026-11-27-covariance-kernel-M1-jucys-murphy-form.md. Do not close while the conjecture is open.

2026-11-27: (SC) re-checked exactly for n = 41..49 with plancherel_growth_side + single_crossing. Single crossing holds for all of them. The threshold is s = 11 for n = 31..46 and moves to s = 12 at n = 47..49. Each n takes 1-6 min and grows about 1.25x per step, so n = 50 was not reached within the 1 h run budget. Still open: no proof.


2026-11-27 (PR #9828): one-cell (newest-box) form proved by Kerov cotransition identity: rho_n(s)=E[1{s}(c^2-(n-1))]/((n-1)(n-2)), M1=(n/3)Cov(s,c^2). Lower half of SC PROVED: rho_n(s)<=0 for (s-2)^2<=n-1. Two sufficient conditions FAIL: monotone regression E[c^2|s] (from n=24), per-nu covariance (nu=(3,3,2)). SC checked n<=58 (t=13 at n=57,58). Upper half (window 2+sqrt(n-1)<s, and s>=t_n) still OPEN; bean stays open. Audit docs/audits/2026-11-27-covariance-kernel-M1-newest-box-form.md.


2026-11-27: SC extended exactly to n<=67 (scfast run stopped at the 1h limit at n=68); t_n=13 for n=57..67.


2026-11-27 (PR upper tail): PROVED rho_n(s)>=0 for s^2>=5n-1 (addable cell has ij<=n). Open window now 2+sqrt(n-1) < s < sqrt(5n-1). Heuristic: (t_n-1)/sqrt(n) -> Omega(1)=1/3+2sqrt3/pi (VKLS), measured 1.64,1.49,1.48,1.47 at n=30,45,55,67. Still OPEN.


2026-11-28: E[c^2|s] non-decreasing for s>=4 holds exactly n<=62 (only failure is s=3->4). MR4 => SC for n>=5 (with proved lower half + upper tail). MR4 NOT proved; next: prove MR4 or stochastic monotonicity of |c| given s.
