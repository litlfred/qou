---
# mgy9
title: Wenzl A>=3 per-nucleon branching scope — tractable first step (opt 3, multi-day)
status: completed
type: task
priority: normal
created_at: 2026-06-20T16:39:31Z
updated_at: 2026-06-21T19:39:07Z
---


## Triage verdict (2026-06-20, background Explore) — pilot already done, unlock verdict-blocked

- **A=2/A=3 per-nucleon factorization pilot ALREADY EXISTS:** `computations/a_operator/canonical_tr_m_combiner_crosscheck.py` reconstructs tr_M by peeling the last nucleon via the merged categorical `A^λ_{ξν}` operator (`a_operator_recursive.py`, PR #2403), matching the transfer at 7.8e-17 (D), 1.1e-16 (³He), 2.2e-16 (⁴He). Building the proposed pilot would RE-WALK this.
- **¹⁶O unlock is VERDICT-BLOCKED:** `docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md` — the per-nucleon recursion's effective bond dimension is χ_eff(k)=p(3k), so it CANNOT beat the p(3A) transfer wall asymptotically. Rust Tasks A/B/C give constant-factor speedups only, not a new feasibility class.
- Refuted: regenerating H_9+ least-squares extracts (rank-deficient, explodes).

**DECISION: the headline goal (exact ¹⁶O tr_M via per-nucleon branching) is blocked
by a merged bond-dimension verdict.** Constant-factor Rust speedups remain possible
but do not unlock new isotopes; not a clean session deliverable.
