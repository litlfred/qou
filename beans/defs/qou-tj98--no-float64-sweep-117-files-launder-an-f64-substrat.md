---
# qou-tj98
title: 'NO FLOAT64 sweep: 117 files launder an f64 substrate constant through mpf(str(...))'
status: completed
type: bug
priority: normal
created_at: 2026-08-08T19:43:43Z
updated_at: 2026-08-08T19:46:03Z
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


## DONE — LAUNDERED is zero

`python3 computations/f64_into_mpmath_audit.py --tier LAUNDERED` exits 0.

Two passes. 102 files went as mechanical single-import swaps (`Q` -> `Q_MP`,
`Q_INV` -> `Q_INV_MP`, `HA` -> `HA_MP`), each AST-classified, dry-run, re-parsed
and re-scanned first. The remaining 15 used the alias in bare arithmetic and
were done one at a time.

Worth recording from the second pass:

- **`mp.nstr(Q, 50)` on a float prints 17 digits, not 50.** So
  `he3_pairknot_composite_lp_probe` and `su2_spinor_multiplicity_resolution`
  were writing 17-digit values into a field named `q_0_50dps`. That is a
  witness-content defect, not cosmetics.
- **`markov_peel`** substituted the f64 q into a symbolic expression and then
  called `.evalf(50)` — 17 good digits dressed as 50. The file already carried
  a "float64 is EVIL" note and a `compute_no_mpf_to_float_cast` QA criterion
  aimed at exactly this.
- **`set_q` takes `float | str`** and does `mp.mpf(str(...))` internally, so the
  three `delta_lambda_*` / `proton_residual_rootcause` files now pass
  `Q_50_DIGIT_STR` and get the full 50 digits. Their alias was renamed
  `Q0_FLOAT` -> `Q0_STR`; a name asserting float over a string is the same
  label defect in miniature.
- **A wrong comment I wrote and then corrected.** I annotated three probes as
  reading the muon `y-lambda-at-q0` cache — the mu3 straddle. Prompted to
  actually read the gate, it is already fixed: it compares the caller's q
  against the WITNESS's own recorded q0, not `q_parameter.Q`. |q_muon -
  q_proton| = 1.28e-8 is 12810x the 1e-12 tolerance, so a proton caller misses
  the muon cache and falls through to the live closed form. **AGENTS.md still
  describes the old broken gate and is stale on this point.**

Bounds on that 1e-12, since it looked arbitrary: float64 ulp at q~1.11 is
2.46e-16 and the anchor gap is 1.28e-8, so the tolerance sits ~4 orders above
representation jitter and ~4 orders below the thing it must not confuse.

F64_IMPORT is now 152 (was 119): files whose laundering was fixed but which
still hold an f64 for a legitimate float purpose moved down a tier. That
bucket is circumstantial by construction and is not a defect list.

NOT DONE: the witnesses of every touched producer are stale against their
sources. Each needs its producer re-run and its output classified under
`witness_regen_wave`. That is a separate wave.
