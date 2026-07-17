# GP character kernel: exact trivial-rep guard closes the silent-wrong path (bean qou-b2ie)

**Date:** 2026-07-17 · **Branch:** `claude/h4-exponents-value-screen-96501m`
(PR #3812) · **Bean:** `qou-b2ie` · **Scope:** (a); Rust compute-kernel
correctness; no witness re-derivation, nothing wired to a dashboard.

## The bug (recap from qou-b2ie)

`pyhecke_native.chi_lambdas_via_gp` / `chi_q_via_gp` (the Rust Geck–Pfeiffer
exact-Laurent character path, `geck_pfeiffer::chi_lambda_via_geck_pfeiffer`)
return **wrong characters on some plain ±1 braid words**. Minimal reproducer,
delta-debugged from a 91-letter H₁₂ failure:

```
word = [(1,6), (1,7), (-1,9), (1,8), (-1,7)]   # σ₆ σ₇ σ₉⁻¹ σ₈ σ₇⁻¹ at H₁₂
```

On the trivial (index) rep `[12]` every generator acts as `q`, so
`χ_[12] = q^{writhe} = q` exactly. Measured: GP path returned `0.79263…` (wrong);
the seminormal mpfr kernel returned `q = 1.10997859…` (correct to 50 dps).

## Root cause (confirmed this session)

The GP path is `braid_to_hecke` (exact, correct) → `reduce_basis_to_minimal_length`
→ `chi_lambda_mn_qdef(λ, cycle_type(w))` per basis element. The reduction uses
**simple-reflection Hecke conjugation only**, which does **not** reach genuinely
minimal-length representatives for every conjugacy class once `n` grows (the full
Geck–Pfeiffer 2000 §3.2 "good cuspidal moves" are needed — the code's own
docstrings flag this as the incomplete F3.2.γ milestone). For any leftover
non-minimal `w`, the code applies `χ_[n](cycle_type(w)) = q^{minlen}` when the true
trivial-rep value is `q^{ℓ(w)} > q^{minlen}` — so the `[n]` row disagrees with the
exact homomorphism value. Engine-confirmed: `chi_gp_trivial_rep_consistent(12, word)`
returns `false` on the reproducer, `true` on words that reduce completely.

## Fix — exact trivial-rep cross-check + refuse-on-disagreement guard

Rather than land the full GP cuspidal-move reduction (a large milestone that cannot
be cross-validated against `pyhecke_native` in this sandbox), this PR closes the
**silent-wrong** failure mode — the actual hazard — with an exact, free check:

- **`trivial_rep_char(n, word)`** computes `χ_[n](T_β)` directly as the algebra
  homomorphism `T_{s_i} ↦ q` (`σ↦q`, `σ⁻¹↦q⁻¹`, doubled-averaged `↦[2]_q`,
  out-of-range gen `↦1`) — a single exact Laurent polynomial, independent of any
  reduction.
- **`chi_gp_trivial_rep_consistent(n, word) -> bool`** (also exported to Python):
  the necessary-condition pre-check named in the bean's "rule of thumb". `false`
  **proves** the GP output is wrong for that word.
- **Refuse-on-disagreement guard**: `chi_lambda_via_geck_pfeiffer` and
  `chi_lambdas_via_geck_pfeiffer` now assert the `[n]` row equals `trivial_rep_char`
  and **panic** (surfaced as a Python `PanicException`) on mismatch. This converts
  silent-wrong into loud-fail — the compute-author "two independent engines, assert
  agreement, refuse to publish" discipline, the same cross-check that caught the bug
  in the A=4 stage-2 probe.

Regression tests (`cargo test --lib geck_pfeiffer`, 16/16 green in-sandbox):
`trivial_rep_char_reproducer_is_q`, `trivial_rep_char_averaged_is_two_q`,
`gp_trivial_check_flags_reproducer` (asserts the H₁₂ reproducer is flagged
inconsistent), `gp_trivial_check_ok_on_reduced_word`, and
`gp_guard_panics_on_reproducer` (`#[should_panic]`).

## What this does and does not do

- ✓ **Silent-wrong is closed.** Any GP call that would return a wrong character now
  fails loudly; consumers can pre-screen with `chi_gp_trivial_rep_consistent`.
- ✓ **Necessary condition, exact.** `q^{writhe}` on the `[n]` row is a genuine
  ground-truth gate (a homomorphism), not a heuristic.
- ✗ **Not a completeness fix.** The check is necessary, not sufficient: a word that
  passes the `[n]` gate is not *proven* correct on all λ. The full remedy remains
  the Geck–Pfeiffer cuspidal-move reduction (or routing every GP consumer to the
  seminormal kernel). Bean `qou-b2ie` stays open for that milestone.
- ✓ **Validated migration target (Rust-level, in-sandbox).** The correct
  Hoefsmit-per-`T_w` path (`chi_lambda_via_gp_hoefsmit` = exact basis expansion +
  direct seminormal on each reduced word) **agrees with the direct seminormal
  kernel** (`chi_lambda_braid`) on the reproducer across `λ ∈ {[12], [11,1], [6,6],
  [2⁶], [1¹²]}` at q=1.1 (`correct_path_agrees_with_seminormal_on_reproducer`,
  green) — exactly the word where the q-MN path is wrong. So GP consumers that hit
  the guard route through the seminormal path — in the Python binding,
  `chi_lambda_all_partitions_mpfr` (Wenzl–LR canonical, all 77 partitions, 50 dps,
  already exported) — and get correct characters at q₀. No Python binding was
  needed to certify this: both paths are cross-validated inside `hecke-engine`.
- **Blast radius (unchanged from the bean):** the certified combiner chain
  (`chi_at_q0_via_hoefsmit_mpfr` → `canonical_tr_m_via_chi_cache`) is seminormal
  throughout and untouched. GP consumers on longer/structured words
  (`derived_chi_catalogue_sweep.py`, `li6_h18_amplification_discriminator_probe.py`,
  the `he4_binding_k_*` stage probes) should pre-screen with the new check; words it
  rejects must use the seminormal path.

## Cross-references

- Bug audit: [`2026-07-14-gp-kernel-bug-and-he4-stage2.md`](2026-07-14-gp-kernel-bug-and-he4-stage2.md)
- Kernel: [`tools/hecke-engine/src/geck_pfeiffer.rs`](../../tools/hecke-engine/src/geck_pfeiffer.rs)
  (`trivial_rep_char`, `chi_gp_trivial_rep_consistent`, `assert_gp_trivial_rep_consistent`)
- Binding: [`tools/pyhecke-native/src/lib.rs`](../../tools/pyhecke-native/src/lib.rs)
  (`chi_gp_trivial_rep_consistent` PyO3 export)
