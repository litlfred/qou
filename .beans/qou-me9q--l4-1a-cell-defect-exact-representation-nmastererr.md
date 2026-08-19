---
# qou-me9q
title: 'L4-1a: cell-defect exact representation — N*(masterErr-defect) as sum of per-cell integrals (exact, no estimate)'
status: completed
type: task
created_at: 2026-08-11T01:06:41Z
updated_at: 2026-08-11T10:00:00Z
---


DONE: LogSineCellDefect.lean cell_defect_repr sorry-free — (pi/N)S(n) - F(n pi/N) = sum of per-cell integrals of f(x_j) - f(u), EXACT, no range restriction on n. Built on sum_integral_adjacent_intervals + integral_log_two_sin + intervalIntegrable_log_two_sin. Next: qou-itg0 (Stirling half-log).

REDUNDANT (2026-08-19) -- L4-1's target was ALREADY PROVED ON MAIN, stronger,
since 2026-08-10 19:24 UTC, one day BEFORE the L4-1 feasibility pass that
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

Specifically superseded by KashaevEndpointSplit.sum_log_two_sin_split, which
is the same decomposition as EXACT ALGEBRA -- no cell-integral representation,
no telescope.
