---
# qou-n3iv
title: 'ASSESS (don''t auto-do): port bring_color_weighted mass convention to Rust hecke-engine — speed-neutral, re-opens the Py<->Rust divergence qou-m7py just closed'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T21:27:22Z
updated_at: 2026-08-15T22:20:56Z
parent: qou-pq8k
---

Follow-up to qou-m7py. Question: should bring_color_weighted (the pn_convention color-weighting in computations/closed_form_tau_M.py / canonical_mass.py) be ported to Rust hecke-engine?

ROAST / recommendation: probably NOT, absent a concrete native consumer.
- No speed win: the expensive layer (Gram/NF/tr_M/colored-Jones) is already native post-5088. Color-weighting is cheap arithmetic on top of tr_M.
- Re-opens divergence risk: a second numeric implementation of the convention is exactly the Python<->Rust drift surface qou-m7py just eliminated (trace_weights z3 vs h*z2+z). Would need its own runtime self-check to babysit.
- No consumer: nothing needs native color-weighted mass; the Python assembly over the native tr_M is fast.

Rust currently HAS: colored-Jones (tl_cable), a 'color content' poly (certificate.rs color field = sum_{l>=2} net(l)), type-weighted generator_volumes_typed ([u,u,d] quark types). It does NOT have bring_color_weighted / pn_convention (grep empty).

If revived: first name the native consumer that justifies it, then port WITH a convergence self-check vs the Python canonical (mirror the gram.py _native_ok pattern).

Claimed 2026-08-15 by claude/agent-discussions-queue-gibk4e (session qou-pq8k). Dispatched to a background agent; work lands in a worktree and is integrated onto the session branch by the parent.
