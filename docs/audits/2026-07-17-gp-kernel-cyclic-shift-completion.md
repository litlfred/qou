# GP character kernel: cyclic-shift completion closes the reduction bug (bean qou-b2ie)

**Date:** 2026-07-17 · **Branch:** `claude/h4-exponents-value-screen-96501m`
· **Bean:** `qou-b2ie` · **Scope:** (a); Rust compute-kernel correctness;
follow-up to the merged trivial-rep guard
([`2026-07-17-gp-kernel-trivial-rep-guard.md`](2026-07-17-gp-kernel-trivial-rep-guard.md),
PR #3812).

## What was still broken after the guard

The merged guard converted the GP path's silent-wrong characters into a
loud panic, but the underlying incompleteness remained: `chi_lambdas_via_gp`
/ `chi_q_via_gp` still could not return characters for the words the guard
rejected (the H₁₂ reproducer and its class). The root cause was that
`reduce_basis_to_minimal_length` only took **strictly length-decreasing**
simple conjugations `w ↦ s w s`, so it stalled at non-minimal elements with
no immediate length-reducing simple reflection — then q-MN on `cycle_type(w)`
was applied to a non-minimal `w` and gave the wrong character.

## The fix — Geck–Pfeiffer cyclic-shift completion

Geck–Pfeiffer 2000 §3: in type A every element reaches a minimal-length
representative of its conjugacy class by a sequence of simple conjugations
that is **non-increasing** in length — one may need to move *sideways*
through equal-length "cyclic shifts" before a length drop opens up.

- **`find_length_decreasing_path(w0, n)`** BFS's the equal-length
  cyclic-shift class of a stalled element (edges: simple conjugations with
  `ℓ(sws) = ℓ(w0)`) and returns the simple-reflection sequence that drives
  it strictly shorter (equal-length shifts, then one length-drop).
- **`reduce_basis_to_minimal_length_complete`** applies that sequence as
  exact Hecke conjugations (each preserving `χ_λ` for **all** λ) until every
  basis element is minimal-length. **Termination:** no conjugation exceeds
  the stalled length `ℓ₀` (BFS follows only `ℓ(sws)=ℓ₀` edges then one
  `ℓ(sws)<ℓ₀` edge), so the potential `Σ(ℓ(w) − minlen(class(w)))` strictly
  decreases each outer step. A 10⁶-node BFS cap + large outer cap backstop
  pathological inputs; the exact trivial-rep guard remains as a final
  safety net (never silently wrong).
- Both `chi_lambda_via_geck_pfeiffer` and `chi_lambdas_via_geck_pfeiffer`
  (backing `chi_q_via_gp` / `chi_lambdas_via_gp`) now use the completed
  reduction.

## Validation (in-sandbox, Rust `cargo test`, 19/19 green)

- `gp_correct_on_reproducer_after_completion`: `χ_[12]` on the H₁₂
  reproducer now equals `q^{writhe} = q` exactly (was the 0.79… bug).
- `gp_matches_seminormal_on_reproducer_battery`: the completed GP q-MN path
  matches the direct seminormal kernel (`chi_lambda_braid`) on the
  reproducer across `λ ∈ {[12],[11,1],[6,6],[3⁴],[2⁶],[1¹²]}`.
- **`gp_matches_seminormal_random_battery`**: a deterministic pseudo-random
  battery of ±1 braid words at `n = 4..8` (20 words/n × 2 q-values × **every**
  partition of n) — the completed GP path agrees with the seminormal kernel
  to 1e-6 throughout. This is the exhaustive check that the completion is
  correct, not merely patched for one word.

The seminormal kernel (`chi_lambda_braid`, and the Wenzl–LR
`chi_lambda_all_partitions_mpfr` used by the certified chain) is the
independent ground truth; both live in `hecke-engine`, so no Python binding
was needed to certify the fix.

## Residual / deployment note

The Rust source fix is complete and validated. For the fix to reach the
Python consumers (`he4_binding_k_*`, `chi_4he_via_rust_lossless.py`,
`derived_chi_catalogue_*`), the `pyhecke-native` wheel must be rebuilt
(`maturin`) — a CI/dev step, not runnable in this sandbox. Consumers that
were producing GP witnesses on rejected word-classes should be re-run after
the wheel rebuild; the trivial-rep guard + the new completion mean they now
either get correct characters or a loud failure, never silent-wrong output.

## Cross-references

- Guard (merged): [`2026-07-17-gp-kernel-trivial-rep-guard.md`](2026-07-17-gp-kernel-trivial-rep-guard.md)
- Bug audit: [`2026-07-14-gp-kernel-bug-and-he4-stage2.md`](2026-07-14-gp-kernel-bug-and-he4-stage2.md)
- Kernel: [`tools/hecke-engine/src/geck_pfeiffer.rs`](../../tools/hecke-engine/src/geck_pfeiffer.rs)
