# C-full Step 6 bench: GP without cuspidal moves is **slower** than seminormal at H_9

> **Status (2026-05-18, this branch):** the all-partitions GP MPFR
> path from C-full Step 3 ([PR #728](https://github.com/litlfred/qou/pull/728)) is
> measured against the seminormal MPFR path on a tritium-like
> canonical braid at H_9. Result: GP is **32× slower** (9433 ms vs
> 294 ms). The audit's 10-50× speedup projection ([PR #710](https://github.com/litlfred/qou/pull/710))
> **does not materialise** without F3.2.ζ cuspidal-moves reduction
> (C-full Step 4). This was an unstated assumption in the audit;
> documenting now so the Step 4 effort can be properly scoped.

## Measurements

`tools/hecke-engine/src/bin/gp_bench.rs` runs both
`chi_lambda_canonical_all_partitions_mpfr` (seminormal direct-
averaging path) and `chi_lambda_via_gp_hoefsmit_all_partitions_mpfr`
(the new GP path) on the same canonical braid at MPFR-50dps, then
compares output and times each.

| atom | H_n | word_len | partitions | seminormal | GP | speedup |
|---|---|---|---|---|---|---|
| proton | 3 | 11 | 3 | 0 ms | 0 ms | (too small to time) |
| neutron | 3 | 11 | 3 | 0 ms | 0 ms | (too small to time) |
| deuteron-like | 6 | 23 | 11 | 0 ms | 4 ms | seminormal wins by ~∞ |
| **tritium-like** | **9** | **35** | **30** | **294 ms** | **9 433 ms** | **0.03× (32× slower)** |

Numerical agreement holds at the round-off floor:

| atom | worst abs_diff |
|---|---|
| proton | 1e-49 |
| neutron | 1e-49 |
| deuteron-like | 3e-49 |
| tritium-like | 2e-48 |

All within tolerance 1e-45. The GP path is **algorithmically correct**
— it just loses badly on wall time.

## Why GP loses without cuspidal moves

The audit's [scaling argument](2026-05-18-hoefsmit-c-gate-gp-cross-validate.md) §C assumed:

> "The key structural win: `braid_to_hecke` is done **once per braid**
> (not per partition). Per-partition work drops to **O(n!)** lookups
> + multiplications, **independent of dim**."

This is true asymptotically as `dim → ∞` (per-partition Hoefsmit
matrix product is O(dim² × |word|), while per-partition GP basis
sum is O(|basis| × dim_per_T_w_char). At max dim 7,700 for n=12 the
GP path wins by orders of magnitude **if `|basis|` stays small**.

In practice at H_9 the basis expansion is **wide** because the
canonical braid contains many `σ⁻¹` and averaged crossings that
spread the permutation across many distinct S_n elements.
Concretely: 35 crossings × Hecke-basis multiplications produces a
basis expansion with hundreds to thousands of distinct
`(w, c_w(q))` terms. Each `reduced_word(w)` is **long** (not
minimal-length within its conjugacy class), so each per-T_w call
to `chi_lambda_braid_mpfr(λ, positive_word)` runs a long positive
word at full dim²·|word| cost.

The seminormal path runs ONE chi_lambda_braid_mpfr per partition,
on the original 35-crossing canonical word. The GP path runs MANY
per partition (one per distinct reduced_word in the basis), each
on a similar-length positive word. The cache hit rate across
distinct_words is empirically low for atomic braids of this shape.

## What changes with F3.2.ζ cuspidal moves (Step 4)

Per `tools/hecke-engine/src/geck_pfeiffer.rs:326 reduce_basis_to_minimal_length`'s
docstring:

> "**Empirical**: on the D atomic braid (n=6, word_len=23), this
> partial reduction takes the basis from ~700 elements down to 145,
> of which 17 are minimal-length and 128 still need the full
> cuspidal-move algorithm."

So:
- Without cuspidal moves: 700 basis elements, mostly NON-minimal
- With partial reduction only: 145 elements, 17 minimal + 128 not
- With full F3.2.ζ cuspidal moves: presumably ~30-50 minimal-length
  elements (one per conjugacy class representative)

At minimal-length, each per-T_w call uses the **shortest** positive
word in its conjugacy class — typically `(ℓ_min - 1) << 35`
crossings. Combined with the cache deduplication, the per-T_w
cost drops by ~10-100×.

So Step 4 (cuspidal moves) is **mandatory** for the GP speedup to
emerge. It is NOT an optional follow-up.

## Revised recommendation

1. **Stop here on C-full Steps 1-3** as merged in [PR #720](https://github.com/litlfred/qou/pull/720) /
   [#725](https://github.com/litlfred/qou/pull/725) / [#728](https://github.com/litlfred/qou/pull/728). They deliver:
   - Correct GP MPFR algorithm with averaged-crossing handling
   - Cross-validated against seminormal at f64 and MPFR-50dps
   - Memoisation infrastructure for when cuspidal moves arrive
   - All within ~1e-49 of the seminormal output at 50 dps
2. **Step 4 (cuspidal moves) becomes the gating prerequisite** for
   any GP-vs-seminormal speedup. The audit's 10-50× projection
   should be re-stated as: "10-50× faster than seminormal, **after**
   F3.2.ζ minimal-length reduction is implemented".
3. **Step 5 (PyO3 bridge)** is still useful in isolation — exposes
   the (correct, slow-without-cuspidal-moves) MPFR GP path to
   Python callers. But unless cuspidal moves are also done, calling
   it from Python doesn't beat the seminormal path.
4. **Step 4 effort** per the geck_pfeiffer.rs docstring: F3.2.ζ
   "uses 'good cuspidal moves' (specific products of consecutive
   simple reflections) to reach minimal-length representatives".
   The algorithm is in Geck-Pfeiffer 2000 §3.2 but not published as
   a clean Rust crate; this is research-grade porting work.

## Files

- [`tools/hecke-engine/src/bin/gp_bench.rs`](../../tools/hecke-engine/src/bin/gp_bench.rs)
  — the bench binary

## Cross-references

- [`docs/audits/2026-05-18-hoefsmit-c-gate-gp-cross-validate.md`](2026-05-18-hoefsmit-c-gate-gp-cross-validate.md)
  — C-gate audit; its "10-50×" projection should be qualified
- [`docs/audits/2026-05-18-hoefsmit-matrix-product-optimization.md`](2026-05-18-hoefsmit-matrix-product-optimization.md)
  — parent audit; candidate C row needs the cuspidal-moves qualifier
