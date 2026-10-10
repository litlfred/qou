---
# qou-fd2u
title: 'M6: re-derive frobenius-s classification under convention D'
status: todo
type: task
priority: normal
created_at: 2026-10-10T08:52:03Z
updated_at: 2026-10-10T08:57:45Z
parent: qou-d8c7
---

frobenius-s-classification-proof.md:16 and table2-data:9 rest on z being invariant under q->1/q, true only for z_C. z_D(1/q0)=0.4036 vs z_D(q0)=0.6127. Classification must be re-derived under D (owner pick 3a, 2026-10-10: bean, not a restatement). Open research.


2026-10-10: under D, S maps z_D to 1/(q(q^2+1)) = z - h (sympy-verified), i.e. S swaps the two loop values. So Phi_1 = sum log|z a_i + b_i| needs re-derivation (its partner is sum log|(z-h) a_i + b_i|). Scope notes added to the proof and table2 on PR #7562.
