---
# qou-dt14
title: 'FRONT-2: probe the irreducibly-external Behrend-weighted DT count (driver-14 / A_ω / Δ_λ)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T01:00:00Z
updated_at: 2026-10-04T15:19:24Z
parent: qou-avtq
---

Owner picked front 2. Per 2026-08-02-1ppq-lever-map: Δ_λ (partition-level) and A_ω (knot-level) are
the SAME missing input — a categorical Behrend-weighted DT moduli count — shown irreducibly external
to the 13 QOU drivers (#4599 Euler-char gives -2 not count 3; #4601 driver-14 = chirality-refined
set-valued count outside the drivers). BOUNDED scope: examine whether that DT count can be supplied/
characterized, KNOWING (#4601 derive-then-check) it would NOT close binding (deuteron B(D) -82.9%).
So this is characterization, not a closure claim. Formalize-first: find the structural constraint the
count must satisfy before any wide search. NOT absolute-mass work.

---
2026-08-11 RESULT (branch claude/dt14-behrend-count-2026-08-11): parity obstruction extracted and
proved (DTBehrendParityObstruction.lean, lean-direct exit 0, Mathlib-FREE so machine-verified
independently of the olean cache). The characterization asked for: what must any supplier of the
knot DT count satisfy?
 - no_constant_weight_yields_three: c*(-2) != 3 for every integer c. The QOU Wedderburn/Springer
   Euler characteristic is -2 (partitionEuler3_eq, qou-qnnq); the DT count is 3. Constant Behrend
   weight gives c*chi = EVEN; the target is ODD.
 - at_least_two_strata: hence any supplier has >=2 Behrend strata (empty has chi=0; single forces
   the even n*(-2)=3).
 - odd_count_needs_odd_stratum: some stratum must carry BOTH an odd Behrend value and an odd
   Euler characteristic.
PRUNE (scope-(b), invariant NAMED = parity): the Behrend function of a SMOOTH moduli is the
constant (-1)^dim, so no smooth moduli with chi=-2 can supply 3. This excludes the whole
"smooth moduli + (signed) Euler characteristic" family — which is the shape every QOU-internal
route has taken — and explains structurally WHY they land on -2: an unweighted/constant-weighted
count has no mechanism to be odd. Does NOT supply the count, does NOT close A_omega/Delta_lambda/
bwse, and (lever map #4601) closing it would NOT close binding anyway. Bounded characterization.


---

## 2026-09-08 — NOT closeable: the bean says so itself. Read for the completion-candidate queue.

`scripts/bean-completion-candidates.py` flags this on `c949eb6a516`,
*"fix(qou-dt14): correct notation (χ is characters, not Euler char) + generalize
parity to all even"*. The completion verb governs a **notation correction**, not
the probe this bean is about.

What landed is real and bounded — `DTBehrendParityObstruction.lean`, lean-direct
exit 0 and **Mathlib-free**, so machine-verified independently of the olean
cache: `no_constant_weight_yields_three` (`c·(−2) ≠ 3` for every integer `c`),
`at_least_two_strata`, `odd_count_needs_odd_stratum`, plus a genuine scope-(b)
prune with the invariant **named** (parity): the Behrend function of a *smooth*
moduli is the constant `(−1)^dim`, so no smooth moduli with `χ = −2` can supply
3. That excludes the whole "smooth moduli + (signed) Euler characteristic"
family — the shape every QOU-internal route has taken — and explains structurally
why they all land on −2.

**But the bean's own closing lines are the verdict**: it *"Does NOT supply the
count, does NOT close A_ω/Δ_λ/bwse, and (lever map #4601) closing it would NOT
close binding anyway. Bounded characterization."* A characterization of what any
supplier must satisfy is not a supplier. Rule 13a: the subject — the
irreducibly-external Behrend-weighted DT count — is open. Stays `todo`.
