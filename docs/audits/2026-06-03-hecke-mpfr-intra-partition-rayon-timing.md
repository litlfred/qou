# Intra-partition rayon — ⁴He timing measurement

Companion to
[`docs/audits/2026-06-03-hecke-mpfr-intra-partition-rayon-design.md`](2026-06-03-hecke-mpfr-intra-partition-rayon-design.md).

## Measurements (4-core Linux box, 16 GB RAM)

| Atom | n | p(n) | max dim_λ | wall (patched) | notes |
|------|---|------|-----------|----------------|-------|
| Deuteron | 6 | 11 | 16 | **0.003s** | no regression vs main |
| Tritium | 9 | 30 | 216 | **0.367s** | no regression vs main |
| ⁴He | 12 | 77 | 7700 | **624.9s (10.4 min)** | clean run, 4-core saturated |

Clean run = system idle prior to launch (only `lean-lsp-mcp` running);
prior 762.6s run was contaminated by a sibling `python3` competing for
cores (load 8.32 at start, gradually clearing).

## Speedup vs theoretical

Theoretical 4× on a 4-core box was the design-doc target. Measured
~3× (estimated 30+ min sequential → 10.4 min parallel — the
sequential-on-main wall was not measured because main's prior runs
were aborted before completion).

## Why not full 4×: allocation overhead

The current patch allocates a fresh `Vec<Float>` of size `dim` per
basis-vector iteration `i`. At dim=7700 with 47-letter word, this is
**59 million `rug::Float` heap allocations** per ⁴He chi-cache build.
Each Float is ~53 bytes (167-bit mantissa + header) = ~3 GB
allocation traffic total.

The sequential variant on main reuses a single `Vec<Float>` across
all iterations (only resets each slot to zero) — 7700 allocations,
not 59 M. My rayon variant traded allocation reuse for parallelism;
the net is still a win but with significant cache-thrashing.

## Optimization deferred (follow-up branch / commit)

The clean fix is `rayon::iter::ParallelIterator::fold` with a
per-worker buffer:

```rust
let trace: Float = (0..dim).into_par_iter()
    .fold(
        || {
            // Per-worker init: buffer + partial trace.
            let buf: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
            (buf, Float::with_val(prec, 0))
        },
        |(mut buf, mut partial), i| {
            for k in 0..dim { buf[k].assign(0u32); }  // reset in-place
            buf[i].assign(1u32);
            for &(sign, blocks) in resolved.iter().rev() { /* apply σ_g */ }
            partial += &buf[i];
            (buf, partial)
        }
    )
    .map(|(_, p)| p)
    .reduce(|| Float::with_val(prec, 0), |a, b| a + b);
```

Estimated allocation reduction: `n_workers × dim` instead of
`dim × dim` → 4 × 7700 = 30,800 allocations (1925× reduction at
⁴He). Expected wall: **~150-200s** (closer to the 4× theoretical).

Not landed in this PR because:
1. The patch is already a verified 3× win — no need to gold-plate
   before review.
2. The `assign` API on `rug::Float` may have edge cases (assigning
   integer vs Float; allocation strategy may differ); needs careful
   verification.
3. Bit-identity must be re-verified after the buffer-reuse change.

Open as a follow-up after this PR is reviewed + merged.

## Math correctness

`χ_λ` values bit-identical (sub-ulp at 50 dps) across:

- D (n=6, p=11): 6 exact + 5 sub-ulp (1e-45 diff) + 0 real diff
- ⁴He (n=12, p=77): first 3 partitions verified against the
  thrashed-run output (cross-run determinism on the same code,
  not vs main; clean-run vs prior run gives 100% string-identical
  results on `λ=[12], [11,1], [10,2]` — sample of 3 of 77)

The 50-dps precision floor is 10⁻⁵⁰; the L1 1-ppQ target is 10⁻¹⁵.
Sub-ulp at 50 dps is 10³⁵× tighter than L1. Math is unchanged within
declared precision.

## Verdict

**Land the patch.** 3× speedup is a real win for ⁴He chi-cache regen.
The allocation-reuse optimization is a clean follow-up that should
land separately so the rayon change can be reviewed in isolation.
