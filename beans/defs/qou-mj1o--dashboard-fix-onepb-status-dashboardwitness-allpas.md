---
# qou-mj1o
title: 'dashboard-fix: onepb-status-dashboard.witness allPassed:false is a DEAD-INVENTORY artifact (2 producerless structural witnesses: brundan-kleshchev-audit, alpha-k-macdonald-closed-form) — L1 actually MET; fix the producer to not count dead inventory as failure (touches existing producer, not a new-file task)'
status: completed
type: task
priority: normal
created_at: 2026-07-20T05:35:55Z
updated_at: 2026-08-29T06:52:24Z
---

---

## The "L1 actually MET" conclusion is FALSIFIED (2026-08-29, PR #5962)

Recorded here because this bean is `completed` and its title asserts *"L1
actually MET"*, so an agent grepping the corpus for L1 status lands on it and
stops. That conclusion no longer holds — and the reason is a defect this bean's
own fix could not have seen.

**This bean's fix was right and is untouched.** Excluding the dead structural
inventory (`brundan-kleshchev-audit`, `alpha-k-macdonald-closed-form`) from
`allPassed` was correct; the `structural_inventory` non-gating carve-out stays
exactly as this bean left it. `allPassed` is False again for a completely
different reason.

**What this bean's fix left in place** is stated in its own comment in the
producer:

> *"allPassed reflects the L1 compute assertions only (lp_max_duality_gap,
> markov_trace_max_rel_delta)."*

**One of those two assertions could not fail.** `markov_trace_max_rel_delta` is
fed by `summary.markov_trace_consistency.max_rel_delta`, computed as

    max((float(d.get("rel_delta", 0)) for d in trm["deltas"]), default=0.0)

and **no delta entry has ever carried a `rel_delta` key** (they carry
`rel_delta_max`, `peel_rel_delta`, `exact_method_rel_delta`,
`pairwise_rel_deltas`). So the generator yielded `0` six times, `max_rel_delta`
was `0.0` **by key-miss**, and the assertion compared 0.0 against 0.0 at
tolerance 1e-9 — passing unconditionally, forever.

Measured from the key that exists: **2.90663e-7**, 290x that tolerance, on 6 of
6 atoms.

So when this bean concluded "L1 actually MET", one of the two gates it was
relying on was reading a missing key. That is not a criticism of the fix — the
dead-inventory diagnosis was correct and independent — it is that the remaining
green was not evidence.

**Current state after the fix in #5962:** `allPassed` False, driven by
`markov_trace_max_rel_delta` alone. `lp_max_duality_gap` still passes
(7.31e-50). The 1e-9 tolerance was NOT widened.

**Cross-links.** `qou-wgaw` (the disagreement that surfaced this, now settled);
`qou-3zby`, which reached *"while it is red, 'L1 compute met' is not
supportable by this cross-check"* from the cross-check side on 2026-08-16 —
this is the same conclusion arrived at from the dashboard side, and the two now
agree.
