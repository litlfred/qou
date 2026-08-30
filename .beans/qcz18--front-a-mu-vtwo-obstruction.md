---
# qcz18
title: 'Front A (mu descent): v_[2] obstruction witness + conditional descent'
status: completed
type: task
priority: medium
created_at: 2026-07-31T20:00:00Z
updated_at: 2026-08-29T16:25:56Z
---

The q-Collatz convergence wall = construct a descent measure mu strictly
decreasing off the attractor (reaches_cycle_of_descent reduces convergence to
this). Attack options:
- A1 (START, tractable negative): PROVE the natural candidate v_[2] fails —
  concrete witness P=-X-2 (q-odd, v_[2]=0) whose odd branch ([3]_q P+1)/[2]_q =
  -(X+1)^2 has v_[2]=2, so v_[2] INCREASES on an odd step. Honest scope-(a): rules
  out the OBVIOUS mu, not the existence of ANY mu. Machine-checks the audit's
  prose wall with a witness.
- A2 (conditional): sharpen reaches_cycle_of_descent with a §3b-cond 'if
  <v_[2]> >= 2 average then descent'.
- A3 (hard): combined mu = a*deg + b*v_[2] — but degree ALSO fails at -q^-2 (odd
  fixed pt, +1 top-cancellation); needs a genuinely new invariant.
Anti-laundering: A1 is scope-(a) negative, NOT structural exclusion; no fabricated mu.

STALE-REFRESH 2026-08-29 (session claude/q-collatz-gaps-conjectures-7bz3hg). All three A-items are settled on main; this bean was left in-progress:
- A1 LANDED: AppendixSurreals/collatz_vtwo_obstruction.lean, qcollatz_vTwo_increases_on_odd_branch (witness -X-2, v_[2] 0 -> 2 on an odd step). Sorry-free.
- A1 SUPERSEDED by collatz_vtwo_domain_rescope.lean: that witness ESCAPES the domain at step 4 (qcollatz_vTwo_witness_escapes_domain), so the negative does NOT apply on the domain-stable cone D_infty. This is what re-opened qou-4atn.
- A2/A3 recast: the live question is no longer 'does v_[2] fail' but 'does v_[2] descend ON D_infty'. Carried by qou-4atn, not here.
Closing as completed; the live descendant is qou-4atn.
