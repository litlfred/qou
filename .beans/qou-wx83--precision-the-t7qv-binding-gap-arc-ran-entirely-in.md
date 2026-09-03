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
- [x] Forward-pointer blocks on the four probes that quoted a residual as
  evidence (`0d5c3f9972a`).
- [x] Lean: `QOU/Mass/SubsetCumulantRecursion.lean` (`dce9420f3b8`) — reconstruction,
  the size-only `c_k` recursion, mixed cumulants vanish across an additive
  split, the seminormal radicand `a·a' = −1/[ρ]²`, and the Hecke root product.
  Sorry-free, axioms `propext/Classical.choice/Quot.sound` only, recompiled
  after the 2026-09-03 container reset. What is NOT in Lean: exchangeability
  of `L_S` and its n-independence — properties of the specific trace,
  established at 200 bits, not derivable from the corpus's `MarkovTrace.lean`
  (cyclicity + single-generator conjugation only; no split-link tensor rule).
- [x] A=5 exact, both orders (200-bit, all 26 subset traces each, ~29 min per
  ordering, 2026-09-03): every float64 figure reproduced to all 9 printed
  digits. `pnpnn`: c₂ +7.272615735, c₃ −3.786046394, c₄ −1.230795704,
  c₅ +1.604498983, |c₅/c₄| = 1.303627, signs + − − +. `nnnnn`: c₂ +9.072622655,
  c₃ −5.081967559, c₄ −1.148549425, c₅ +1.955406398, ratio 1.702501.
  Reconstruction residual 0 at 200 bits, both. Exchangeability spreads
  1.74e-59 / 2.49e-59 / 1.74e-59 (were 3.33e-15 / 5.77e-15 / 6.22e-15 in
  float64); size-only vs full Möbius 3.73e-59 (was 7.55e-15). Raw 60-digit
  traces committed as `*.a5_exact.{pnpnn,nnnnn}.json`; the precision probe
  re-derives the table from them. (First runs were killed by a container
  reset; re-run on the rebuilt engine.)
- [ ] A=6 homonuclear exact — running, minimal-n route, two n=18 traces at
  128 bits, ~2.5 h remaining at 2 workers.
- Nothing here shows the float64 route harmless elsewhere. It was harmless HERE
  because every identity tested is exact and every magnitude is O(1). The arc
  had no way to tell the difference, which is the point.
