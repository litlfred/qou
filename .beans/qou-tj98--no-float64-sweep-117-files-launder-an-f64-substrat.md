---
# qou-tj98
title: 'NO FLOAT64 sweep: 117 files launder an f64 substrate constant through mpf(str(...))'
status: todo
type: bug
created_at: 2026-08-08T19:43:43Z
updated_at: 2026-08-08T19:43:43Z
---

`computations/f64_into_mpmath_audit.py` (added this session) finds 117 files doing `mpf(str(X))` where X is a float64 substrate constant — an mpf holding ~17 real digits, which then looks exact at every later inspection (type() says mpf, nstr(...,50) prints 50 digits).

These are DEFECTS, not candidates: if you want the value, read Q_50_DIGIT_STR or the _MP family. A further 119 files are F64_IMPORT (hold an f64 beside mpmath) — circumstantial, review individually, do not bulk-edit.

Fixed already in this session, as the worked examples: mass_at_3A_proper + pyhecke.atom (braid word), mass_binding_dashboard (incl. its q0^-1 leg), gram_qtrace_hutchinson_probe, gram_norm_binding_probe, test_nucleon_gen_chains_q_param, chi_convention_from_values_audit. Measured payoff on the chi chain: the dual-path cross-check went 1e-16 -> 1e-50.

Two entries worth doing first, both high blast radius:
  * canonical_braid_crossings.py:76 — this is `_avg_color_delta()`, which AGENTS.md already documents as capping at ~5e-16, and it has 16 live consumers.
  * borromean_binding_recompute.py:78,134 — feeds the mass dashboard's canonical mass m_can.

Do NOT bulk-rewrite. Each fix changes witness values, so each needs its producer re-run and its witness classified under witness_regen_wave, same discipline as the anchor migration.

Guard already in place: reject_float64_q() refuses a float64 q at the braid-word builders (including the laundered form, detected by float64 round-trip), so that path cannot regress. Nothing equivalent guards the other 117.

Acceptance: `python3 computations/f64_into_mpmath_audit.py --tier LAUNDERED` exits 0.
