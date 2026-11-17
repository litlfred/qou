---
# qou-dt14
title: 'FRONT-2: probe the irreducibly-external Behrend-weighted DT count (driver-14 / A_ω / Δ_λ)'
status: in-progress
pr: 8236
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T01:00:00Z
updated_at: 2026-11-17T06:55:00Z
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


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** The parity obstruction is machine-checked (re-compiled 2026-10-10). The subject, a supplier of the Behrend-weighted DT count, is open, as the bean's own 2026-09-08 note says.

Evidence: `QBeta/DTBehrendParityObstruction.lean` is Mathlib-free and compiled exit 0 locally (Lean 4.25). `no_constant_weight_yields_three`, `at_least_two_strata` and `odd_count_needs_odd_stratum` are present and sorry-free. They are elementary parity facts.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-17 — Round 52 formalization & probe witness (PR #8236, status: in-progress)

- [x] PR #8236 (`62b8fce5d1e824cf9dd59a1d9845d15631382086`): formalized `two_stratum_behrend_elimination`, `two_stratum_fourone_opposite_weight_parity`, `dtCount_sub_chiEuTotal_even_of_all_odd_weights`, and `no_all_odd_behrend_weights_yield_three_over_neg_two` in `QOU/QBeta/StokesDiagonalVsOffDiagonalAndCrossKnotSplit.lean` (`0 sorry`, `0 axiom`, `0 vacuity`), proving that any all-odd-weight (including `+/-1` LCI) Behrend stratification preserves parity `DT = chi_eu (mod 2)` and cannot yield `DT = 3` over `chi_eu = -2`.
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
