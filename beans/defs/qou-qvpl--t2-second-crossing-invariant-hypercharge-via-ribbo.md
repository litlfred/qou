---
# qou-qvpl
title: 'T2: second crossing invariant (hypercharge) via ribbon twist'
status: in-progress
type: task
priority: critical
created_at: 2026-08-03T23:27:16Z
updated_at: 2026-08-04T17:51:00Z
parent: qou-8lxd
---

Corpus #1 open item. The derivation chain:

PROVED (Lean):
1. Hecke category is ribbon → twist θ_λ = q^{c_λ} exists
2. Per-strand twist datum t: {1,...,n} → Z is categorical
3. T(t) and multiset {t₁,...,tₙ} are gauge-invariant
4. Bar involution negates: T(t̄) = -T(t)
5. Twist is INDEPENDENT of writhe (factorization criterion)

BATTERY PASSED (T2b, witness):
6. 10,000 candidate helon-style assignments → only 4 survive
7. u-quark multiset {0,1,1} uniquely determined
8. electron multiset {-1,-1,-1} uniquely determined
9. All 4 survivors = sign-flip variants of SAME assignment

OPEN:
A. Is Y_t = 2(T(t)/3 - I₃) categorically derived or a candidate?
   Current status: CANDIDATE (the formula makes GMN hold iff
   Q_twist = Q against Coulomb charge). Not yet derived from axioms.
B. Does 1910.09966 §5 (Asselmeyer-Maluga: charge as Hirzebruch
   signature ±1/3, ±2/3, ±1 from 3-manifold boundary) provide an
   independent route to the same formula?
C. Z₆ spectrum check: first-generation hypercharges form a Z₆
   subgroup of U(1)_Y. Does the twist battery reproduce this?

CROSS-CHECK: strand-twist-datum.md (content block) is well-written
and honest about epistemic status. No false derivation claims found.
