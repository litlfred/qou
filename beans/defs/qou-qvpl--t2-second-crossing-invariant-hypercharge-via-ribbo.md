---
# qou-qvpl
title: 'T2: second crossing invariant (hypercharge) via ribbon twist'
status: in-progress
type: task
priority: critical
tags:
    - reorg-2026-10-04
    - 8f-tseries
    - 8f-open
created_at: 2026-08-03T23:27:16Z
updated_at: 2026-11-16T18:32:12Z
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



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Triage 2026-10-10 — open, and the body's own OPEN list is the reason

Tagged `8f-open`. The body above is unusually well-stated and needs no
correction: five Lean-proved facts, four battery results, and three explicitly
OPEN sub-items (A: is `Y_t = 2(T(t)/3 − I₃)` derived or a candidate — the body
answers its own question, **CANDIDATE**; B: the Asselmeyer-Maluga independent
route; C: the `Z₆` spectrum check).

**Why it cannot be mechanical:** sub-item A is the whole question, and the body
states its status honestly — the formula "makes GMN hold iff `Q_twist = Q`
against Coulomb charge", which is a consistency property, not a derivation from
axioms. Under §NO FITTING a formula selected because it makes a known relation
hold is selection against the target; the body does not claim otherwise, and
nothing should be wired until A is answered.

**Its own cross-check is a positive finding worth preserving:**
`strand-twist-datum.md` was audited and found honest about epistemic status,
with no false derivation claims. That is the state to maintain, not to fix.

**Relation to `qou-kebu` (T2b).** The body credits T2b's battery as PASSED
(items 6–9), which reads as T2b being done. It is not: `kebu`'s own body
records the derivation gap explicitly — *"the battery proves CONSISTENCY … but
does NOT DERIVE them from QOU axioms"* — and its "DEPENDS ON: T2" names this
bean. So the dependency runs `kebu` → this bean, and a reader going by T2's
item 6–9 alone would close T2b wrongly. Recorded on both.


## Progress Update — 2026-11-16 (`litlfred/qou#8149`, `e824457ca8e0ff4e0b85644c5478eebd2c3c8d56`)

- **Resolved Open Question C (Baez–Huerta $\mathbb{Z}_6$ compatibility) & Open Question B (Asselmeyer–Maluga Hirzebruch signature comparison) in Lean 4 (`folio/quantum-observable-universe/lean/QOU/StandardModel/RibbonTwistZ6Hypercharge.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - **Check C (`baez_huerta_z6_from_triality_and_weak_parity` & `firstGenChiralStates_all_valid_z6`)**: Under $3Y_t = 2T(t) - 6I_3$, proves the exact algebraic identity $2\tau + 3w + 3Y_t = 2(\tau + T(t)) + 3(w - 2I_3)$. Consequently, whenever colour triality satisfies $3 \mid (\tau + T(t))$ and weak isospin satisfies $2 \mid (w - 2I_3)$, the Baez–Huerta $\mathbb{Z}_6$ congruence $6 \mid (2\tau + 3w + 3Y_t)$ holds identically across all 8 chiral states $(u_L, d_L, \nu_L, e_L, u_R, d_R, \nu_R, e_R)$ and all 4 battery survivors ($3Y \in \{+1, +1, -3, -3, +4, -2, 0, -6\}$).
  - **Check B (`qou_torus_knot_signatures_even` & `knot_signature_even_obstruction`)**: Proves that for any 1-component knot $K$ (including the QOU torus-knot carriers $T(2,p)$ for $p \in \{1,3,5,7\}$ with $\sigma(T(2,p)) = -(p-1) \in \{0, -2, -4, -6\}$), the classical knot signature $\sigma(K) = 2k \in 2\mathbb{Z}$ is always even, so Asselmeyer–Maluga's $Q = \sigma/3$ ($3Q = 2k$) can never hit the odd cleared charges $3Q_d = -1$ or $3Q_e = -3$, whereas the 3-strand ribbon twist $T(t) = t_1 + t_2 + t_3$ hits $\{-3, -1, 0, +2\}$.
- **Witness (`computations/probes/ribbon-twist-z6-hypercharge-hirzebruch.witness.json`)**: `allPassed: true`, `4/4` assertions passed (`q0Anchor: "independent"`).
