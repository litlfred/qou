---
# qou-ifot
title: 'Session: q-Collatz arc — refresh stale work plan, general-word cycle forcing'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-29T16:28:38Z
updated_at: 2026-08-29T17:57:53Z
---

TURN 1 (2026-08-29). Reviewed the arc against main -- main's collatz substance is IDENTICAL to the working tree (only .qa.json sidecar churn differs on those paths), so 'lots landed on main' is true corpus-wide but did not move this arc. What HAD moved is the arc's own record: six beans listed as open work that had already landed. Refreshed all six (commit 4c8d75a98a) and opened + landed the successor chip qou-rcgi (commit 13d3d51bbb, PR #6042).

LIVE q-COLLATZ GAPS after this turn, in the order I would attack them:
1. C12 (largest unformalized): rem:collatz-three-forms states the Markov-trace convergence tr_M(C_q^k(h)) -> 1 over H_n(q) in PROSE and its .ts carries NO lean ref at all. Tractable to at least state.
2. qou-4atn: does v_[2] descend on D_infty? Blocker cleared. Honest ceiling: a global descent measure there CLOSES q-Collatz-on-a-QOU via reaches_cycle_of_descent_domainStable, so expect a wall, and the useful move is a D_infty counterexample rather than a proof.
3. C11 residual: the contact-boundary iff stays conditional on the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext -- now a named, single, finite target rather than a diffuse 'conditional'.
4. Multi-window generalisation of qou-rcgi (see that bean).
5. The general word / q-Steiner. Open, and open classically; do not expect to close it.

TURN 3. Two more items landed. qcz15 C12: rem:collatz-three-forms now has a Lean carrier (commit d09d3357e7), and it surfaced a live overclaim -- QOU.Substrate.contact_threshold_lt_two announced '1 < v* < 2' while proving only the upper half, with the lower half absent corpus-wide; both fixed (876f70faa3). qou-4atn: SETTLED NEGATIVE (105465b558) -- v_[2] does not descend on D_inf, structurally, and the general obstruction (any N-valued descent measure is positive off the target) is the reusable part.

REVISED live gap order for the arc:
1. Find a descent measure for D_inf that is NOT a valuation. qou-4atn's descent_measure_pos_off_target now constrains the search: mu must be strictly positive at every non-attractor point, which kills every [k]_q-adic valuation at once. A height (degree, L1 coefficient norm) is the natural next family. NOTE the honest ceiling is unchanged: a working mu CLOSES q-Collatz-on-a-QOU, so this is not expected to close cheaply.
2. C11 residual: the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext -- a single named finite target.
3. Multi-window generalisation of the general-word forcing (qou-rcgi).
4. Wire the arc's library .lean files to content blocks as a class -- needs the folio-assistant pipeline, absent in this container.
5. The general word / q-Steiner. Open, and open classically.
