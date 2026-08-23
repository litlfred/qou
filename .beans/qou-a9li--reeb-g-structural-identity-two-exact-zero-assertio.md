---
# qou-a9li
title: 'reeb_g_structural_identity: two exact-zero assertions carry tolerance=None'
status: todo
type: task
priority: normal
created_at: 2026-08-23T08:05:32Z
updated_at: 2026-08-23T08:06:07Z
---

Exposed 2026-08-23 re-running the `load_q_50dps` callers (PR #5494).

    I1_polynomial_identity            0.0 -> 7.2445e-71   expected 0.0, tolerance=None
    I2_g_equals_inverse_deformed_eig  0.0 -> 4.5278e-72   expected 0.0, tolerance=None

**The identities still hold** — to 71 and 72 digits, far inside the 50-dps
arithmetic floor. The assertions carry `tolerance=None`, i.e. they demand
*exact* `0.0`. Under the muon pin the arithmetic happened to cancel exactly;
under the proton pin it lands at ~1e-71 instead.

So this is **assertion strictness, not a mathematical regression**. An
exact-zero identity evaluated in floating/mpmath arithmetic should carry a
tolerance at the precision floor (the sibling assertions in this corpus use
`tolerance=1e-40`).

Fix: give both a tolerance rather than 'fixing' the number. Do **not** widen
anything else — the value is correct, the comparison is what is wrong.
