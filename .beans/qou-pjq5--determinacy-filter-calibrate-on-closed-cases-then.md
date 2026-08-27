---
# qou-pjq5
title: 'Determinacy filter: calibrate on closed cases, then apply to surviving binding-term candidates'
status: completed
type: task
priority: normal
created_at: 2026-08-27T05:15:47Z
updated_at: 2026-08-27T05:32:08Z
---

TESTED BY TRYING TO BREAK IT. It breaks in both halves.

DEFECT 1 -- 'extremal' does no work. Single-constraint L1: cost at coordinate i is w_i*|b|/|a_i|, ordering governed by w_i/|a_i|; a is fixed by the constraint, w is not. both_orderings_achievable proves BOTH orderings reachable for ANY constraint. Measured on real Hecke objects: Plancherel-style cost picks (6,), Frobenius-style picks (5,1). The corpus recorded this in May 2026 (Option D 'moves the underdetermination to the choice of cost') and I had not read it before proposing the filter.

DEFECT 2 -- 'structural' does not predict success. Frobenius co-Casimir: 'theorem-forced (no free params)' and FAILED, later 'PROVED-INSUFFICIENT ... vortex-blind'. 3 of 8 settled candidates. Recomputed the reason rather than citing it: chi^lambda varies with the word by 1.3301 at n=6 while 1/dim_q(lambda) has no word argument.

WHAT SURVIVES, inverting my claim: the filter separates DETERMINATE from UNDERDETERMINED, never right from wrong. Its value is FALSIFIABILITY -- no free choice means a testable prediction; co-Casimir was promoted to testable and refuted, which is the filter working. An underdetermined candidate can never be falsified. The warning sign means 'cannot be tested', not 'will be wrong'.

The freedom hides in THREE places: parameter, objective, selection rule. My phrasing named only the first, which is why 'extremal' looked like an escape. An optimum relocates the freedom into the objective.

Probe: computations/meson/determinacy_filter_calibration_probe.py, 6/6.
Lean: QOU/MassTheory/ExtremalPrincipleDoesNotDetermine.lean, 4 decls sorry-free.
Audit: docs/audits/2026-08-27-determinacy-filter-calibration.md. PR #5868.

DO NOT QUOTE THE 8/8 -- I assigned both axes of that table; it checks bookkeeping, not the rule. Earning a hit-rate needs candidates classified BEFORE outcomes are known. That is the natural follow-on.
