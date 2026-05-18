# C-gate: Geck-Pfeiffer cross-validation results

> **Status (2026-05-18, this branch):** **GREEN LIGHT** for the full
> Geck-Pfeiffer implementation (candidate C-full per the Hoefsmit
> optimization audit). Cross-validation against the Hoefsmit
> seminormal path passes on all 28 partition rows tested, with
> worst relative diff = 1.55 × 10⁻¹⁵ (f64 round-off floor).
>
> One caveat: the existing `braid_to_hecke` in `geck_pfeiffer.rs`
> does **not** handle averaged crossings (sign == 0). C-full needs
> to extend it.

## What this audit gates

The Hoefsmit-optimization audit
([PR #710](https://github.com/litlfred/qou/pull/710)) identified the
Geck-Pfeiffer factorisation as the highest-leverage structural win
for canonical-χ at n ≥ 12 — potentially 10-50× over the seminormal
path **if** the T_β basis-expansion is sparse at high n. The
binary `tools/hecke-engine/src/bin/gp_cross_validate.rs` (added
this branch) runs the gate:

1. Cross-validate `chi_lambda_via_gp_hoefsmit` against
   `chi_lambda_braid` (Hoefsmit seminormal) at f64 precision on 6
   test words covering n ∈ {3, 4, 6}.
2. Measure the T_β basis-expansion sparsity factor (`n! / |basis|`)
   per word.
3. Exit non-zero if any partition row exceeds relative diff `1e-12`.

## Results

### Correctness (1) — PASSES

| word | n | partitions checked | worst rel_diff |
|---|---|---|---|
| `σ_1` | 3 | 3 | 0 |
| `σ_1 σ_2` | 3 | 3 | 0 |
| `σ_1 σ_2 σ_1` | 3 | 3 | 0 |
| `σ_1 σ_2⁻¹` (mixed) | 3 | 3 | 0 |
| `σ_1 σ_2 σ_3 σ_1 σ_2` | 4 | 5 | 1.55 × 10⁻¹⁵ |
| `σ_1 σ_2 σ_3 σ_4 σ_5 σ_1⁻¹ σ_2⁻¹ σ_3⁻¹ σ_4⁻¹ σ_5⁻¹` | 6 | 11 | 1.55 × 10⁻¹⁵ |

**Total**: 28 partition rows, worst rel_diff = 1.55 × 10⁻¹⁵ — f64
round-off floor. GP and seminormal produce algebraically identical
χ^λ values; the small numerical residuals come from non-associativity
of f64 addition in the two algorithms' different summation orders.

### Sparsity (2) — strong signal

| word | n | |T_β basis| | n! | sparsity factor |
|---|---|---|---|---|
| `σ_1` | 3 | 1 | 6 | 6× |
| `σ_1 σ_2` | 3 | 1 | 6 | 6× |
| `σ_1 σ_2 σ_1` | 3 | 1 | 6 | 6× |
| `σ_1 σ_2⁻¹` | 3 | 2 | 6 | 3× |
| 5-crossing positive at n=4 | 4 | 1 | 24 | 24× |
| 10-crossing mixed at n=6 | 6 | 16 | 720 | **45×** |

**Interpretation**:

- **Pure-positive words** collapse to a single basis element after
  full Hecke reduction (their image under `S_n` is a single
  permutation). Sparsity factor = n!. Direct evidence that the GP
  path's per-basis evaluation cost scales as O(1), not O(n!), on
  positive-only words.
- **Mixed σ/σ⁻¹ words** spread across multiple basis elements;
  empirically the basis size grows much slower than n! up to the
  scales tested. At n=6 with 10 crossings, 16/720 ≈ 2.2% of basis
  occupied → 45× sparsity factor. Extrapolating to n=12 (where
  Σ dim² = 12! ≈ 5×10⁸) this means GP could plausibly evaluate the
  canonical |tr_M| using 10-100× fewer ops than seminormal.

**Caveat**: the test atomic braids are short pure-positive or
positive/negative mixes. **Real atomic braids** have averaged
crossings (sign == 0); each averaged crossing expands to
½σ + ½σ⁻¹ in the Hecke basis, doubling the basis size per averaged
crossing in the worst case. For ⁴He at H_12 with 16+ averaged
crossings, the worst-case post-expansion basis is 2¹⁶ × |mixed basis|.
The empirical sparsity at canonical atomic words is **not yet
measured** — it requires extending `braid_to_hecke` to handle sign
== 0 (see "Known limitation" below).

## Known limitation: averaged-crossing handling

`tools/hecke-engine/src/geck_pfeiffer.rs:203 braid_to_hecke` does
not handle sign == 0:

```rust
pub fn braid_to_hecke(n: usize, word: &[(i32, u32)]) -> HeckeElement {
    let mut x = hecke_identity(n);
    for &(sign, gen) in word {
        let i = (gen as usize).saturating_sub(1);
        if i + 1 >= n { continue; }
        x = if sign >= 0 {
            hecke_mul_ts_right(&x, i)
        } else {
            hecke_mul_ts_inv_right(&x, i)
        };
    }
    x
}
```

`sign == 0` (averaged crossing) is currently bucketed into the
`sign >= 0` branch and treated as σ — **incorrect**. To handle
averaged crossings properly via the direct-substitution identity
`(σ + σ⁻¹) / 2 = σ - h/2 · I` (Hecke relation), `braid_to_hecke`
should expand each averaged crossing to a half-sum of `T_{w · s_i}`
and `T_{w · s_i⁻¹}` Hecke elements at the appropriate coefficient
(±h/2). This is a candidate C-full work item.

For C-gate, validating on positive/mixed σ-σ⁻¹ words is sufficient
to confirm the **core GP machinery is correct**. The averaged-
crossing extension is mechanical follow-up; the algebraic structure
doesn't change.

## Verdict

- **GP per-T_w character evaluation** matches seminormal to f64
  round-off — go for C-full.
- **Sparsity factor at small n** is encouraging (45× at n=6
  with 10-crossing mixed word) — supports the audit's "10-50×
  speedup at high n" projection.
- **Averaged-crossing extension** in `braid_to_hecke` is the
  first concrete task for C-full (deferred).
- **MPFR variant** of GP path needs to be written for production
  use (current GP is f64-only via `seminormal::chi_lambda_braid`).
  Cost: re-implement `evaluate_f64` as `evaluate_mpfr` on
  `LaurentPolyQ` + route through `chi_lambda_braid_mpfr`. ~1 day
  (deferred).

## Recommended C-full next steps (in dependency order)

1. **Extend `braid_to_hecke`** to handle averaged crossings via
   half-sum expansion (~½ day).
2. **MPFR variant of `chi_lambda_via_gp_hoefsmit`** (~1 day) —
   uses `chi_lambda_braid_mpfr` per-T_w and Laurent-poly evaluation
   at MPFR precision.
3. **Memoization** of `chi_lambda_braid_mpfr(λ, T_w_word)` keyed
   on `(λ, T_w_word_hash)` so cross-atom reuse is exploited
   (the audit's "amortise across atoms" win).
4. **Implement the F3.2.ζ cuspidal-moves algorithm** for the cases
   where `reduce_basis_to_minimal_length` does not fully reduce
   (per the file's docstring: D braid n=6 takes 145 → 17 minimal,
   128 still need cuspidal moves). Without full reduction, GP's
   per-T_w cost is dim²·|reduced_word|, not the O(1) we want.
5. **PyO3 bridge** so Python can call the MPFR GP path.
6. **Benchmark** on ⁴He H_12 (current seminormal baseline: 8m25s
   wall via candidate B's inner-rayon in
   [PR #716](https://github.com/litlfred/qou/pull/716)).

If steps 1-4 land, the projected speedup on ⁴He at H_12 is 10-50×
over the seminormal path (per the Hoefsmit audit). For ⁵Li at H_15
(max dim 292,864) the projected improvement could be 100×+ —
the difference between "multi-week" and "overnight".

## Files

- [`tools/hecke-engine/src/bin/gp_cross_validate.rs`](../../tools/hecke-engine/src/bin/gp_cross_validate.rs)
  — the cross-validation binary (run with `cargo run --release --bin gp_cross_validate`)
- [`docs/audits/2026-05-18-hoefsmit-c-gate-gp-cross-validate.md`](2026-05-18-hoefsmit-c-gate-gp-cross-validate.md)
  (this file)

## Cross-references

- [`docs/audits/2026-05-18-hoefsmit-matrix-product-optimization.md`](2026-05-18-hoefsmit-matrix-product-optimization.md) §C
- [`tools/hecke-engine/src/geck_pfeiffer.rs`](../../tools/hecke-engine/src/geck_pfeiffer.rs)
- [PR #716](https://github.com/litlfred/qou/pull/716) — candidate B (parallel baseline)
