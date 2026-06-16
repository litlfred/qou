# y_λ table scaling: how far does the Wenzl-bridge closed form go?

> **Status (2026-05-18, this branch):** the y_λ ceiling at n=12
> identified in PR #689's audit was closed in PR #691 via the
> Wenzl-bridge closed-form numerical evaluator. This audit
> documents the **empirical scaling** of that evaluator beyond
> n=15, and answers the questions:
>
> - Do we need y_λ for every n, or only some?
> - How far can the closed form take us before compute or storage
>   becomes a real constraint?

## The two questions

### "Do we need this for all atoms?"

**No — only for `n = 3·A` for each target atom A.** Atomic
braids are 3A-strand objects (3 quarks × A nucleons), so the
y_λ table is consumed via `wedderburn_jones_markov.y_lambda_at(n=3·A, q_0)`.
Non-multiples of 3 are not consumed by any canonical-|tr_M|
or chi-cache combiner.

That said, the Wenzl-bridge evaluator runs over every n in its
input range, and the per-non-multiple-of-3 partitions cost very
little (see scaling table below). The current cache covers all
n ∈ {2..30} — both for completeness (downstream tools that
sample intermediate n for testing) and because skipping
non-multiples-of-3 saves negligible compute.

### "How far does the closed form scale?"

The fractional-Schur evaluator `y_lambda_wenzl_bridge` is O(n)
per partition. Total compute is bounded by partition count, which
grows asymptotically as $p(n) \sim \exp(\pi\sqrt{2n/3}) / (4n\sqrt{3})$
(Hardy–Ramanujan). Empirically, the prefactor at 100 dps is
~1 ms/partition (measured below).

## Empirical scaling (this branch)

Measured by running `y_lambda_wenzl_bridge.py <n>` per group:

| n range | partitions added | wall time | per-partition | cumulative cache size |
|---|---|---|---|---|
| 13, 14, 15 | 412 | ~0.5 s | 1.2 ms | 230 KB |
| 16, 17, 18 | 913 | 0.9 s | 1.0 ms | 558 KB |
| 19, 20, 21 | 1,909 | ~1.6 s | 0.8 ms | 1.3 MB |
| 22, 23, 24 | 3,832 | ~3.2 s | 0.8 ms | 2.8 MB |
| 25, 26, 27 | 7,404 | ~7.5 s | 1.0 ms | 5.8 MB |
| 28, 29, 30 | 13,887 | ~13 s | 0.9 ms | 11 MB |
| **n=2..30 total** | **28,627** | ~25 s | 0.9 ms | **11 MB** |

The merge step into `y-lambda-at-q0.witness.json` (truncating
100-dps strings to 50-dps for the production cache) adds another
~10 s for n=2..30. Final production-cache size: 7.7 MB.

## Projected scaling (extrapolation)

Using the empirical 0.9 ms/partition prefactor at 100 dps:

| n | atom (A=n/3) | partitions | est. wall time | est. per-n size |
|---|---|---|---|---|
| 36 | ¹²C, ¹²B | 17,977 | 16 s | 4 MB |
| 42 | ¹⁴N, ¹⁴C | 53,174 | 48 s | 12 MB |
| 48 | ¹⁶O | 147,273 | 2.2 min | 33 MB |
| 60 | ²⁰Ne | 966,467 | 14.5 min | 220 MB |
| 90 | ³⁰Si | 56.6 M | 14 hr | 13 GB |
| 120 | ⁴⁰Ca | 1.84 B | 19 days | 420 GB |

**Practical ceiling**:
- `n ≤ 48` (atoms up to ¹⁶O): trivially feasible (~minutes,
  ~30 MB witness)
- `n ≤ 60` (atoms up to ²⁰Ne): feasible in one session
  (~15 min, ~200 MB witness — would need git LFS)
- `n ≤ 90` (atoms up to ³⁰Si): overnight compute, multi-GB
  witness — needs git LFS and a Rust accelerator for the
  evaluator itself
- `n > 90` (atoms ⁴⁰Ca and heavier): out of reach without
  algorithmic compression (e.g., only sample partitions that
  appear in the specific atomic braid's Wedderburn support)

## What's actually consumed downstream

The y_λ table at n = 3A is read by:

1. **`canonical_tr_m_via_chi_cache.py`** (chi-cache combiner;
   merged in PR #682) — `Σ_λ y_λ(q_0) · χ^λ(β; q_0)`. Needs
   FULL coverage: every partition of n=3A.
2. **`canonical_tr_m_via_rust.py`** (Rust binary; merged in #682)
   — same shape; full coverage needed.
3. **`mass_formula_6term_mpfr_50dps.term_4_frobenius_mp`**
   (Frobenius co-Casimir term in the unified mass formula) —
   needs y_λ at n=3A for every atom A in the sweep.
4. **`per_irrep_pole_atom.py`** (symbolic-q pole-order analysis)
   — needs **symbolic** y_λ(q), which the wenzl-witness output
   does NOT provide. Pole-order analysis is stuck at n ≤ 12
   until either:
   - the symbolic-bridge generator (sympy `sp.cancel`) is
     extended (intractable, per the #689 audit)
   - a Rust accelerator is written for the symbolic closed form
   - CRT / Lagrange reconstruction is implemented from
     numerical samples

## Why this matters for the 1ppb roadmap

| Atom | needs | currently feasible? |
|---|---|---|
| p, n, D, T, ³He, ⁴He | y_λ at n ≤ 12 | ✓ (was already in main pre-#691) |
| ⁵Li | y_λ at n = 15 | ✓ (PR #691) |
| ⁶Li, ⁶He, ⁷Li, ⁷Be, ⁸Be, ⁸Li, ⁹Be, ¹⁰Be | y_λ at n = 18..30 | ✓ (this audit + branch) |
| ¹²C, ¹⁴N, ¹⁴C, ¹⁶O | y_λ at n = 36..48 | ✓ (extension is ~minutes; not yet in cache) |
| heavier (²⁰Ne and up) | y_λ at n ≥ 60 | needs git LFS + algorithmic upgrades |

For the canonical |tr_M| via the Rust binary, the **per-partition
Hoefsmit matrix product** is the real bottleneck (not y_λ): max
partition dim grows ~exp(c√n) and MPFR-50dps multiplications at
that dim are expensive. The relevant figure under FULL coverage
(every λ ⊢ n, not just balanced (n/3,)×3) is the **maximum** dim
across all partitions of n, since the slowest block dominates:

| n | max dim_λ | partition λ | balanced (n/3)³ dim | Σ dim_λ² (= n!/n!) |
|---|---|---|---|---|
| 12 | **7,700** | (5,3,2,1,1) | 462 | 12! ≈ 4.8 × 10⁸ |
| 15 | **292,864** | (5,4,3,2,1) | 6,006 | 15! ≈ 1.3 × 10¹² |
| 18 | **16,336,320** | (7,4,3,2,1,1) | 87,516 | 18! ≈ 6.4 × 10¹⁵ |
| 21 | **1,118,939,184** | (7,5,3,2,2,1,1) | 1,385,670 | 21! ≈ 5.1 × 10¹⁹ |

⁴He at H_12 took 17 min on 4-core rayon. ⁵Li at H_15 with max dim
292,864 (38× over ⁴He's 7,700) would project to **wall × ~(N/N')³ ×
(crossings ratio)** at fixed dps. The dominant matrix-product cost
per partition is O(dim_λ³) per crossing, so a naive single-machine
projection from ⁴He → ⁵Li at fixed precision is **many orders of
magnitude** worse than 17 min, not the ~30-50 hr a balanced-dim
projection would suggest. Concretely: at 4-core rayon, an MPFR-50dps
chi_lambda compute for ⁵Li at H_15 is **multi-week wall time** on a
single machine without algorithmic compression. ⁶Li at H_18 (max
dim ~1.6 × 10⁷) is **infeasible on a single machine at all**.

That is the next-step gating concern, not y_λ. Possible mitigations
(deferred to a separate audit):
- Sparse-block exploitation of the Hoefsmit YSN form (only
  computing the diagonal contribution per SYT basis)
- Per-partition rayon parallelism at finer granularity than the
  current per-atom parallelism
- f64 fast path (against the "no float64" directive — would only
  be acceptable as a cross-check, not production)

## Conclusion

**y_λ is no longer the bottleneck for atoms up to ²⁰Ne.** The
Wenzl-bridge closed-form path scales linearly in partition count
at ~1 ms/partition × 100-dps mpmath; n=2..30 builds in 25 s and
costs 7.7 MB. The original ceiling at n=12 was an artifact of
the sympy `sp.cancel` symbolic-q path — not the math.

The new bottleneck for canonical |tr_M| at H_n for high n is the
per-partition Hoefsmit matrix product (max dim grows ~exp(c√n)).
That is the next research target.

## Files modified by this audit's run

- `computations/y-lambda-wenzl-witness.json` —
  extended to n=2..30 (11 MB; raw 100-dps closed-form output)
- `computations/y-lambda-at-q0.witness.json` —
  extended to n=2..30 (7.7 MB; 50-dps production cache)
