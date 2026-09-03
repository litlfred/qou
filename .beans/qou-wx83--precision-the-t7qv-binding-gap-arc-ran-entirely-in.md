---
# qou-wx83
title: 'PRECISION: the t7qv binding-gap arc ran entirely in float64 — exact 200-bit re-run'
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T04:21:57Z
updated_at: 2026-09-03T04:22:03Z
---


Owner flag: "why using float?? ?forbidden!"  Correct — `docs/precision-goals.md`
forbids float64 in the hot path of anything feeding a witnessed quantity, and
`compute-precision-auditor` rule 4 forbids calling a float64 agreement "exact".
The whole arc broke both.

Two losses, not one:
- matrices: `build_seminormal_matrices` -> numpy/scipy `dtype=float`, while the
  exact twin `build_seminormal_matrices_mp` sits in the same file, unused;
- q itself, the worse one: every probe opened `q = mp.mpf(str(Q0))` off
  `qou_substrate.constants.Q`, a Python float. 17 digits. `Q_50_DIGIT_STR` was
  there the whole time.

## Done
- `the_binding_arc_was_measured_in_float64_probe` — 200-bit MPFR engine (mpmath
  fallback), faithful to `build_seminormal_matrices_mp` to 9.3e-61. Every
  identity the arc asserted re-measured at A=2,3,4. **All hold**, residuals
  1e-15 -> 1e-60. Bond constants exact; the arc's float64 values were good to
  ~1e-13 (set by the truncated q), not the ~1e-15 it implied.
- Bonus, and it pays for itself: `L_S` is n-independent — `L_nn` identical at
  n=6, 9, 12. Markov split-link factorisation. So `L_k` is computable in its own
  minimal system n=3k, and A=6 needs 2 traces at n=18 instead of 5.
- Killed both float64 A=6 jobs; replaced with exact runs.

## Running
- A=5 exact, `pnpnn` and `nnnnn`, 200-bit, 26 subset traces each.
- A=6 homonuclear exact, 128-bit, minimal-n route (L_2..L_5 at n=6..15, then two
  n=18 traces for L_6). Long.

## Open
- Until A=5/A=6 land, every A>=5 number in the arc — the c_5 sign, the A=5
  hierarchy, the 12-ordering sweep — stays a float64 measurement. Sign and
  magnitude claims with margins ~1e13 above the float64 floor, so not in doubt
  the way a 1e-15 residual was, but NOT exact and not to be quoted as exact.
- Add forward-pointer blocks to the arc's probes that quoted a residual as
  evidence: `cumulant_hierarchy_does_not_converge`,
  `c5_sign_is_robust_convergence_claim_is_not`,
  `four_body_term_and_the_h12_collapse`, `three_body_term_has_the_wrong_sign`.
- Nothing here shows the float64 route harmless elsewhere. It was harmless HERE
  because every identity tested is exact and every magnitude is O(1). The arc
  had no way to tell the difference, which is the point.
