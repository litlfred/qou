---
# qcz14
title: 'TIER B: achievable q-Collatz-on-QOU Lean formalization gaps'
status: in-progress
type: milestone
priority: medium
created_at: 2026-07-25T03:10:00Z
updated_at: 2026-08-29T16:26:26Z
---

Achievable Lean chips (real work, no research breakthrough needed). Follow-up
to merged PRs #3996 + #4180. Attack in this order:
- B5 (start): bridge pos_domain_stable <-> reaches_cycle_of_descent. Cleanest via
  a generic reaches_of_descent_of_forward over any forward-invariant predicate S,
  then specialize to the domain-stable cone (forward-invariance FREE).
- B3: formalize D-infinity = domain-stable cone as a Lean predicate
  (inDomain P := qi2 | P or qi2 | P+1; domainStable P := forall k, inDomain(C^[k]P));
  prove domainStable is forward-invariant.
- B4: odd-branch valuation lemma (v_[2] of ([3]P+1)/[2]) complementing
  qTwoValuation_mul_qplus_one.
- B6: census -> Lean bridge "no positive cycle <= period N" for small N.
- B7: period-3 mixed-word exclusion (low marginal value vs the exact census).
Anti-fabrication holds: no faked mu, no faked instance.

B3+B5 DONE: QCollatz.inDomain + QCollatz.domainStable (D-infinity) formalized; domainStable_forward (forward-invariance) PROVED; reaches_of_descent_of_forward (generic, cone-abstracted) + reaches_cycle_of_descent_domainStable (hclosed discharged for free over D-infinity). All sorry-free. Remaining Tier B: B4 odd-branch valuation, B6 census->Lean, B7 period-3.

B4 DONE: qTwoDvd_oddBranch — [2]_q | ([3]_q P + 1) for q-odd P (odd branch stays in ℤ[q]), via [3]P+1 = q[2]P+(P+1). Sorry-free. Remaining: B6 census->Lean, B7 period-3 (low value).

B7 DONE: qcollatz_period3_EEO/EOO — no nontrivial period-3 cycle. EEO forces q(q^2+2q+2)P2=1, EOO forces q(q^3+q^2-1)P1=-(q^2+2q+2); both non-unit coeffs in Z[q^pm1] (units are only +-q^n), so no solution. linear_combination over generic [CommRing R] (section 7c), sorry-free (lean-direct exit 0). Periods 1-3 now ALL closed by explicit word-elimination. Remaining Tier B: only B6 census->Lean (qcz16, low marginal value). Status snapshot + reasonable-stopping-point + next-steps written into docs/audits/2026-07-18-collatz-no-cycles-multiplicative-shadow-gap.md for future agents.

STALE-REFRESH 2026-08-29. The three items this bean listed as remaining are all landed or superseded:
- B4 (odd-branch valuation) LANDED twice over: QCollatz.qTwoDvd_oddBranch (the divisibility) and collatz_vtwo_obstruction.qcollatz_vTwo_increases_on_odd_branch (the valuation direction, v_[2] increases).
- B7 (period-3) LANDED: QCollatz.qcollatz_period3_EEO and qcollatz_period3_EOO.
- B6 (census -> Lean) SUPERSEDED in substance: collatz_period4.lean covers period 4 exactly, and collatz_one_odd_family.lean proves two INFINITE families, which is strictly stronger than the 'no cycle <= period N' stamp B6 asked for. qcz16 (the B6 task) stays low/optional.
Tier B is effectively drained. The live successor is the general-word forcing (qou-gwrd).
