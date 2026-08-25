---
# qou-itg0
title: 'L4-1b: Stirling half-log — the -(1/2)log n term via Mathlib Stirling/log-factorial'
status: completed
type: task
created_at: 2026-08-11T01:06:41Z
updated_at: 2026-08-11T10:20:00Z
---


DONE: LogFactorialStirling.lean sorry-free — log_stirlingSeq_eq (additive expansion of Mathlib's multiplicative stirlingSeq for n>=1) + tendsto_log_factorial_stirling: log(n!) - (n log n - n + (1/2)log n + (1/2)log(2pi)) -> 0. Exactly the constant vdV cites from Zheng p.7. Remaining L4-1 input: qou-q8lc (uniform second-order cell remainder).

REDUNDANT (2026-08-19) -- L4-1's target was ALREADY PROVED ON MAIN, stronger,
since 2026-08-08 22:33 UTC, THREE DAYS BEFORE the L4-1 feasibility pass that
opened this bean.

  QOU/Knot/KashaevAsymptotic.lean :: kashaev_log_sum_asymptotic
    | sum_{j=1}^{k} log(2 sin(j pi/N))
        - ( -(N/pi) Lob(k pi/N) + (1/2) log(2N sin(k pi/N))
            + (pi/(12N)) cot(k pi/N) ) |
      <= 1/(144 k^2) + (7/12)(pi/N)^2 + (pi/N)^2/(12 sin^2(k pi/N))

Verified: 17-module cone ok=17, axioms [propext, Classical.choice, Quot.sound],
no sorryAx.  It is STRICTLY STRONGER than the L4-1 target: it identifies the
O(1/N) term as (pi/12N)cot, and its error is effective (explicit constants).
The two (1/2)log terms differ by exactly (1/2)log(2pi) -- the Stirling constant
the L4-1 route was going to produce.

Nothing is deleted; the work here is correct and sorry-free.  Downstream
consumers should cite kashaev_log_sum_asymptotic instead.
Audit: docs/audits/2026-08-19-l41-was-already-proved-on-main.md

Specifically: the log(k!) handling is internal to the corpus proof.
