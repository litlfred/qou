---
# qou-ifot
title: 'Session: q-Collatz arc — refresh stale work plan, general-word cycle forcing'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-29T16:28:38Z
updated_at: 2026-08-29T16:43:52Z
---

TURN 1 (2026-08-29). Reviewed the arc against main -- main's collatz substance is IDENTICAL to the working tree (only .qa.json sidecar churn differs on those paths), so 'lots landed on main' is true corpus-wide but did not move this arc. What HAD moved is the arc's own record: six beans listed as open work that had already landed. Refreshed all six (commit 4c8d75a98a) and opened + landed the successor chip qou-rcgi (commit 13d3d51bbb, PR #6042).

LIVE q-COLLATZ GAPS after this turn, in the order I would attack them:
1. C12 (largest unformalized): rem:collatz-three-forms states the Markov-trace convergence tr_M(C_q^k(h)) -> 1 over H_n(q) in PROSE and its .ts carries NO lean ref at all. Tractable to at least state.
2. qou-4atn: does v_[2] descend on D_infty? Blocker cleared. Honest ceiling: a global descent measure there CLOSES q-Collatz-on-a-QOU via reaches_cycle_of_descent_domainStable, so expect a wall, and the useful move is a D_infty counterexample rather than a proof.
3. C11 residual: the contact-boundary iff stays conditional on the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext -- now a named, single, finite target rather than a diffuse 'conditional'.
4. Multi-window generalisation of qou-rcgi (see that bean).
5. The general word / q-Steiner. Open, and open classically; do not expect to close it.
