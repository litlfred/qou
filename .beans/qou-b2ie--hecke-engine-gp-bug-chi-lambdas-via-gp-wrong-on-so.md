---
# qou-b2ie
title: 'hecke-engine GP bug: chi_lambdas_via_gp wrong on some plain words (min reproducer [(1,6),(1,7),(-1,9),(1,8),(-1,7)] at H12, chi_[12] != q); seminormal mpfr correct — fix Rust GP path + add trivial-rep regression'
status: completed
type: bug
created_at: 2026-07-14T01:32:09Z
updated_at: 2026-07-17T20:55:00Z
---

## Guard landed (2026-07-17, PR #3812) — silent-wrong closed; full reduction still open

Exact trivial-rep cross-check `χ_[n] = q^{writhe}` added to the Rust GP path
(`geck_pfeiffer::trivial_rep_char`, `chi_gp_trivial_rep_consistent` — also
exported to Python). `chi_lambda_via_geck_pfeiffer` / `chi_lambdas_via_geck_pfeiffer`
now **panic** on `[n]`-row disagreement instead of returning silently-wrong
characters (refuse-on-disagreement). Regression tests green (`cargo test --lib
geck_pfeiffer` 16/16); pyhecke-native `cargo check` clean. Audit:
`docs/audits/2026-07-17-gp-kernel-trivial-rep-guard.md`.

**Still open:** the necessary-condition guard closes the *silent-wrong* hazard but
is not a completeness fix. The full remedy is the Geck–Pfeiffer 2000 §3.2
cuspidal-move reduction (reach true minimal length for all classes at n≥7) OR
routing every GP consumer to the seminormal kernel. Bean stays open for that
milestone; GP consumers on longer/structured words must pre-screen with
`chi_gp_trivial_rep_consistent` until it lands.

## RESOLVED (2026-07-17) — guard + cyclic-shift completion

- Guard (merged PR #3812): exact trivial-rep check `χ_[n]=q^{writhe}` makes
  the GP path refuse (panic) instead of returning silently-wrong characters;
  correct seminormal migration target certified in Rust.
- Full fix (this branch): `reduce_basis_to_minimal_length_complete` +
  `find_length_decreasing_path` add the Geck-Pfeiffer cyclic-shift escape,
  so the GP q-MN path reaches genuinely minimal-length reps. Validated:
  GP(complete) == direct seminormal on the H12 reproducer (6 partitions) AND
  a randomized battery (n=4..8, 20 words x 2 q x every partition, 1e-6).
  19/19 Rust tests green. Audit:
  docs/audits/2026-07-17-gp-kernel-cyclic-shift-completion.md
- Deployment residual: pyhecke-native wheel rebuild (maturin, CI/dev) +
  re-run of GP-witness consumers; not runnable in sandbox.
