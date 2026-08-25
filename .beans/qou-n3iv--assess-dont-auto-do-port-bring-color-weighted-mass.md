---
# qou-n3iv
title: 'ASSESS (don''t auto-do): port bring_color_weighted mass convention to Rust hecke-engine — speed-neutral, re-opens the Py<->Rust divergence qou-m7py just closed'
status: completed
type: task
priority: normal
created_at: 2026-08-15T21:27:22Z
updated_at: 2026-08-19T21:09:11Z
parent: qou-pq8k
---

SUPERSEDED then VERIFIED. Closed by a sibling who landed
tools/hecke-engine/src/color_weight.rs on main -- correctly, and better than the
draft this bean was tracking: it ships BOTH an f64 and an MPFR (rug::Float)
layer (the draft was f64-only, which silently misses the L1 50-dps floor), plus
the CANONICAL pinned table + verify_python_convergence self-check, plus the
q0-literal discipline note.

Per AGENTS.md 'converge on landing', this context re-scoped from re-derive to
VERIFY, and the verification is the contribution:

1. INDEPENDENT DERIVATION AGREES. This context derived the three bond factors
   (p-p: z; n-n: z-h; p-n: z - h(1/2 - delta/4), delta = flavor_split_leading)
   from the Python separately, before seeing the landed module. Same result.
2. CANONICAL TABLE CONFIRMED against ground truth computed independently here:
   2H 0.5082297893767389625779958, 3He 0.3113863120725956524128884,
   4He 0.1256841528952662694138785, 7Li 0.01254532544244002460663017,
   delta 0.001375710807027096008551109 -- all agree to every digit carried.
3. NO DRIFT after 26k commits. Their table was pinned against closed_form_tau_M.py
   at commit 85e94fb8; re-run against live Python gives worst relative drift
   3.467e-50, inside their 1e-45 gate. The table is still valid.
4. 11/11 color_weight tests pass, including the MPFR 50-dps convergence gate.

No further work needed on the port itself.
