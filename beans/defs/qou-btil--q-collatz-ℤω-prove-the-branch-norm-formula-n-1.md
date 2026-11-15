---
# qou-btil
title: 'q-Collatz ℤ[ω]: prove the branch-norm formula N = 1 + 6k + 12k²'
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:07:55Z
updated_at: 2026-08-30T03:20:16Z
---

PROVED. `QOU.AppendixSurreals.CollatzEisenstein.branch_norm`: N(Q_k(w)) = 1 + 6k + 12k^2, plus branch_norm_eq_one_iff (=1 only at k=0) and branch_norm_ge (>=19 for k>=1). The route: differentiate [3]_q*Q = [2]_q*P - 1 at w where [3]_q vanishes, giving (2w+1)Q(w) = P(w) + (w+1)P'(w) (branch_deriv_relation); at n=6k the chain data is (u,v) = (-w, -6k-(6k+1)w) by chainData_at_six_mul, and 1/(2w+1) = -(2w+1)/3 gives Q_k(w) = -(4k+1) - (2k+1)w, whose norm x^2-xy+y^2 is 12k^2+6k+1 by ring. lean-direct exit 0; #print axioms shows no sorryAx. Agrees with all 11 probe values.
