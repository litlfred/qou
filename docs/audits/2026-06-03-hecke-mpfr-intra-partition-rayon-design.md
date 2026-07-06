# Intra-partition rayon for `chi_lambda_braid_mpfr` — design

## Status

**Draft (stub, 2026-06-03).** Placeholder so PR opens immediately per
AGENTS.md ALWAYS-PR. Implementation follows in subsequent commits on
the same branch.

## Problem (gap-4 reframe)

PR #1741 confirmed the MPFR all-partitions wiring works at D / T / ³He
(≤ 1s wall), but ⁴He (n=12) hangs in the rayon-parallel batch because
one dominant partition (`λ` with `dim_λ = 7700`) is itself
single-threaded. The outer `chi_lambda_canonical_all_partitions_mpfr`
already uses `par_iter` over the 77 partitions
(`tools/hecke-engine/src/wenzl_lr.rs:311`), but on a 4-core box the
dim=7700 partition's matmul chain saturates one core for ~5 minutes
while the other 76 partitions finish in seconds.

## Kernel

`tools/hecke-engine/src/seminormal_mpfr.rs:197` — function
`chi_lambda_braid_mpfr`:

```rust
let mut trace = Float::with_val(prec, 0);
for i in 0..dim {                       // ← OUTER LOOP, basis vectors
    let mut v: Vec<Float> = vec![Float::zero(); dim];
    v[i] = Float::with_val(prec, 1);
    for &(sign, blocks) in resolved.iter().rev() {
        // apply σ_g / σ_g⁻¹ / averaged — matrix-vector matmul
        match sign { ... }
    }
    trace += &v[i];
}
```

Each iteration `i` is **independent**: it gets its own `v`, applies the
same `resolved` word, and contributes `v[i]` to the trace. No
cross-`i` shared mutable state.

## Fix

Replace the `for i in 0..dim` loop with `(0..dim).into_par_iter()`:

```rust
use rayon::prelude::*;
let trace_terms: Vec<Float> = (0..dim).into_par_iter().map(|i| {
    let mut v: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
    v[i] = Float::with_val(prec, 1);
    for &(sign, blocks) in resolved.iter().rev() {
        if sign > 0 { apply_sigma_mpfr(&mut v, blocks, prec); }
        else if sign < 0 { apply_sigma_inv_mpfr(&mut v, blocks, &h, prec); }
        else { apply_sigma_averaged_mpfr(&mut v, blocks, &h, prec); }
    }
    std::mem::replace(&mut v[i], Float::with_val(prec, 0))
}).collect();
let trace = trace_terms.into_iter()
    .fold(Float::with_val(prec, 0), |acc, x| acc + x);
```

Thread safety: `resolved` is `Vec<(i32, &[BlockMpfr])>` — shared `&`
slices over `all_blocks`, which is `Sync` because `rug::Float` is
`Sync`. `h: &Float` shared `&` is also `Sync`. Each thread mutates
only its own local `v`.

## Expected speedup on ⁴He (n=12)

On a 4-core box with `dim_λ = 7700` dominant partition:

- Current: 1 thread × 5+ min sequential = > 5 min wall
- Patched: 4 threads × ~75s each = ~75s wall (4× speedup)

Doesn't change the asymptotic O(dim² · |word|) cost, but cuts the
constant by `n_cores`.

## Nested rayon — non-issue

The outer
`chi_lambda_canonical_all_partitions_mpfr.par_iter()` over partitions
PLUS the new inner `(0..dim).into_par_iter()` share rayon's global
thread pool. When all 77 partitions are in flight, inner par_iter
gets ~0 extra threads. When only the dim=7700 partition remains,
inner par_iter gets all 4 cores. Net behavior is exactly the desired
"fill idle cores with intra-partition work" pattern.

## Validation plan

1. Build `pyhecke-native` wheel (`cd tools/pyhecke-native && maturin develop --release`)
2. Run D/T/³He chi-cache regen — verify bit-identical χ_λ at 50 dps
3. Run ⁴He chi-cache regen — measure wall (expect < 5 min, target ~75s)
4. Commit + push + comment with timing on PR

## Coordination

This is the real gap-4 from PR #1741 — the hypothesis "no rayon at all"
in PR #1741's design doc was wrong (verified: outer rayon is at
`wenzl_lr.rs:311`). The real gap is **intra-partition** parallelism.
The fix lives in the Rust crate, not in the Python wiring; PR #1741's
wiring fix is correct and orthogonal.
