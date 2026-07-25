---
# qcz14
title: 'TIER B: achievable q-Collatz-on-QOU Lean formalization gaps'
status: in-progress
type: milestone
priority: medium
created_at: 2026-07-25T03:10:00Z
updated_at: 2026-07-25T03:11:10Z
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
