---
# qou-q3q2
title: 'GAP: Schur element c_λ(Q) divides [n]_Q! (fake-degree polynomiality)'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T13:52:16Z
updated_at: 2026-10-10T16:35:09Z
---

Open, not attempted to closure (session 2026-10-10, PR #7596).

Statement: for λ ⊢ n, [n]_Q! / c_λ(Q) = Q^{n(λ)} [n]_Q! / ∏_x [h(x)]_Q is a polynomial in Q with
nonnegative integer coefficients, where c_λ = `QOU.SchurWeyl.schurElt` (= 1 / molienWeight).

Why open: this is the q-hook-length formula / fake-degree polynomiality,
Σ_{T ∈ SYT(λ)} Q^{maj T} = Q^{n(λ)} [n]_Q! / ∏ [h]_Q (Stanley EC2 Cor. 7.21.5). The corpus proves the
SUM identity Σ_λ f^λ R_λ = [n]_Q! (`NormalizedSumUnconditional.normalizedSum_eq_one`) but not the
per-λ polynomiality: no `maj` statistic, no coinvariant-algebra grading, and no corner recursion
for R_λ that keeps polynomiality (the maj change on removing n is descent-dependent).

Searched: QOU/MathlibExt/{MolienFakeDegree*,QPlancherel,QPartitionCombinatorics,QIntegerCanonical},
QOU/Mathlib/QHookVandermonde, beans/defs (no polynomiality statement found).

Routes: (1) define maj on SYT and prove the q-hook formula by the
Greene–Nijenhuis–Wilf-style q-hook walk; (2) graded coinvariant algebra (heavy);
(3) Krattenthaler bijection. Not needed for Schur orthogonality, which is proved without it
(`QOU.SchurWeyl.HeckeSchurOrthogonality`).


## Update 2026-10-10 (PR #7630): integrality PROVED; nonnegativity still OPEN

Proved sorry-free in `QOU/SchurWeyl/HookDivisibility.lean` (lean-direct -DautoImplicit=false exit 0; axioms propext/Classical.choice/Quot.sound only):
- `hookProd_dvd_qFactorial`: ∏_x [h(x)] ∣ [n]! in R[X], any CommRing R.
- `exists_qFactorial_eq_schurElt_mul`: [n]_Q! = c_λ(Q)·Q^{n(λ)}·P(Q), P ∈ ℤ[X], any field, Q ≠ 0,1.
- Route: cyclotomic factorisation + hook inequality d·#{x : d ∣ h(x)} ≤ n (`mul_card_filter_dvd_hook_le`), via beta-sets/abacus.

Still open (this bean stays open): nonnegative coefficients, i.e. the maj formula Σ_{T∈SYT} Q^{maj T} = Q^{n(λ)}[n]!/∏[h]. Not reachable from the integrality route.
