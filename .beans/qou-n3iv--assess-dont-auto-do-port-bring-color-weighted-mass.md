---
# qou-n3iv
title: 'ASSESS (don''t auto-do): port bring_color_weighted mass convention to Rust hecke-engine — speed-neutral, re-opens the Py<->Rust divergence qou-m7py just closed'
status: completed
type: task
priority: normal
created_at: 2026-08-15T21:27:22Z
updated_at: 2026-08-15T22:39:42Z
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
## OUTCOME 2026-08-15 — owner overrode the recommendation; ported.

Landed as `tools/hecke-engine/src/color_weight.rs` (commits 6132ee32 f64
layer, be0095fe MPFR layer, 60d2a0f6 convergence self-check, e2b2dc97 tests,
a3e09510 clippy).

The bean's three objections, re-checked after building it:

1. **"No speed win"** — CONFIRMED. Nothing was measured as faster. The port
   is `A-1` multiplications on top of a trace the engine already has.
2. **"No consumer"** — CONFIRMED, still none. Grep for
   `markov_z|interface_factor|closed_form` across `src/` finds only
   `gram.rs` self-uses and two comments; nothing calls `color_weight`. The
   nearest call site, `gram::atom_per_generator_volumes:727`, hardcodes p-n
   as `(1.0, -0.5*h)` = strict_averaged, and its Python mirror
   `pyhecke/atom.py:679` does the same — so the colour weighting is absent
   from that channel in BOTH languages, which is a scope fact, not a drift.
   Wiring it there would change production numbers and is an owner call.
3. **"Re-opens the divergence surface"** — ADDRESSED, not dismissed. The
   self-check is the reason the port is allowed to exist: `CANONICAL` pins
   the Python 50-dps output for 6 isotopes, `verify_mpfr_convergence` /
   `verify_f64_convergence` recompute and refuse loudly, mirroring
   `pyhecke.gram::_native_ok`. Measured agreement: MPFR worst 3.467e-50
   (⁴He) — digit-for-digit identical to the Python across all six — f64
   worst 5.531e-16 (⁷Li).

**Correction to the prior transcription of the math.** `closed_form_tau_M.py`'s
module docstring (line 17) still spells `z` as convention C,
`1/(q^1/2 + q^-1/2)`; the live `markov_z` has returned convention D,
`q^3/(q^2+1)`, since the owner ruling of 2026-08-09. A port following the
docstring would have been ~23% wrong. The Rust module re-uses
`gram::markov_z` rather than re-spelling it.

**Precision, stated rather than degraded.** The Python carries `mpmath.mpf` at
50+ dps and the engine's `gram` layer is f64. So the port ships both, labelled:
`closed_form_ratio` (f64, documented LOSSY) and `mpfr::closed_form_ratio_mpfr`
(`rug::Float`), and the 1e-45 gate runs against the MPFR one.

**Adjacent finding — already tracked, no new bean.** `pyhecke/atom.py:691`
computes `z_mark = 1/(q^0.5 + qi^0.5)` (convention C) while `gram.rs:762`
computes `z_mark = markov_z(q)` (convention D), in the same function, selected
by `_native_ok` dispatch — and `_native_ok` cannot catch it because it compares
only `trace_weights` and `gram_matrix`. Corpus-grep first: this is already
`qou-5wpk` (its line 24 names `atom_per_generator_volumes` explicitly) and
`qou-wgta` (line 69 names `atom.py`). Recorded here as corroboration with the
line numbers and the `_native_ok` blind spot; not re-declared open.
