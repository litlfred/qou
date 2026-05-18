# Hoefsmit per-partition matrix-product cost: what optimizes, what doesn't

> **Status (2026-05-18, audit-only):** the y_λ scaling audit
> ([`2026-05-18-y-lambda-scaling-analysis.md`](2026-05-18-y-lambda-scaling-analysis.md))
> identified the per-partition Hoefsmit matrix product in the Rust
> canonical-χ kernel as the next bottleneck for canonical |tr_M|
> compute at higher n. This audit characterizes that cost and
> enumerates concrete optimization candidates ranked by
> effort × expected speedup. **No implementation in this branch.**

## Current algorithm (`chi_lambda_braid_mpfr`)

[`tools/hecke-engine/src/seminormal_mpfr.rs:197`](../../tools/hecke-engine/src/seminormal_mpfr.rs).
Pseudocode for one (λ, β) call:

```text
build_blocks_mpfr(λ, q, prec) → (dim, all_blocks)
  # all_blocks[g-1] is a list of 1×1 and 2×2 Hoefsmit blocks for σ_g

trace ← 0
for i in 0..dim:                          # ← outer loop over basis vectors
    v ← e_i  (zero vector with v[i] = 1)
    for (sign, gen) in word in reverse:   # ← word-length loop
        apply σ_gen^sign in-place to v    # ← sparse matvec: O(dim) MPFR ops
    trace += v[i]
return trace
```

**Per-partition complexity** (at fixed dps):

| factor | scaling | note |
|---|---|---|
| dim outer loop | × dim | trace accumulator |
| word loop | × \|word\| | sequential, ~50 crossings for ⁴He |
| matvec per σ_g | × dim | YSN already exploits sparsity (only 1×1 + 2×2 blocks) |
| MPFR op cost | × prec | ≈ 200 bits at 50 dps |
| **Total** | **O(dim² × \|word\| × MPFR-cost)** |  |

**Aggregate over all partitions of n** (FULL coverage):

| n | max dim | Σ dim² (= n!) | per-atom matmuls ≈ n! × \|word\| |
|---|---|---|---|
| 9  (T, ³He) | 42 | 9! = 362,880 | ~1.8 × 10⁷ |
| 12 (⁴He) | 7,700 | 12! ≈ 4.8 × 10⁸ | ~2.4 × 10¹⁰ |
| 15 (⁵Li) | 292,864 | 15! ≈ 1.3 × 10¹² | ~6.5 × 10¹³ |
| 18 (⁶Li) | 1.6 × 10⁷ | 18! ≈ 6.4 × 10¹⁵ | ~3.2 × 10¹⁷ |

The dim² outer-loop term dominates at high n. At n=18 the cost is
~7 orders of magnitude over ⁴He. The empirical 17 min for ⁴He at H_12
maps to a single-machine projection of multi-week / infeasible at
H_15 / H_18 respectively (consistent with the y_λ scaling audit's
revised projection).

## Parallelism currently exploited

- **rayon over partitions** (`chi_lambdas_braid_mpfr` uses
  `shapes.par_iter().map(…)`) — N-core scaling on the **outer**
  loop over the 30/77/385 partitions at n=9/12/15.
- **No parallelism within a partition**: the dim outer loop and the
  word loop are both sequential.

For ⁴He at H_12, 77 partitions divided over 4 cores gives ~20
partitions per core × per-partition cost. The max-dim partition
(7,700) is the longest tail; rayon's work-stealing helps but the
slowest partition still bounds wall time.

## Optimization candidates

### A. Materialize σ_gen as sparse matrices once, then matrix-matrix product (rejected)

The per-σ blocks are already sparse. Matrix-matrix product over the
word would be O(dim³ × |word|) for dense, O(nnz_M × dim × |word|)
for sparse — but after a few crossings the product densifies. **No
speedup; worse constants.**

### B. Parallelize the dim outer loop with rayon

The `for i in 0..dim` accumulator is embarrassingly parallel.
Each iteration is independent; reduction is a simple sum.

| metric | current | with B |
|---|---|---|
| per-partition wall | ~M × dim² × MPFR | ~M × dim² × MPFR / C_inner |
| parallelism | partitions only | partitions × dim |

**Caveat**: rayon's nested parallelism currently parallelizes only
the outer (partitions) loop. For ⁴He, 77 partitions × 4 cores
already saturates; adding inner parallelism would help only on the
max-dim partitions (which is the tail). For ⁵Li / ⁶Li with 385 /
913 partitions, **per-partition inner parallelism is irrelevant
unless single-partition cost > total wall budget**, which is the
case at n=15 + (max dim 292,864 partition alone is hours).

**Verdict**: implement for n ≥ 15. Effort: ~½ day (rayon
`par_iter()` on outer `for i in 0..dim`, with care for
thread-local MPFR buffers). Expected speedup: ~Nc on the
max-dim partition.

### C. Geck–Pfeiffer factorization (already scaffolded — biggest potential)

[`tools/hecke-engine/src/geck_pfeiffer.rs`](../../tools/hecke-engine/src/geck_pfeiffer.rs)
already implements:
- `braid_to_hecke(n, word)` — expand `T_β = Σ_w c_w(q) · T_w` in
  the canonical Hecke basis (O(n! × |word|) Laurent-poly ops)
- `chi_lambda_via_gp_hoefsmit(λ, n, word, q)` — sums `c_w(q) · χ^λ(T_w)`

The key structural win: `braid_to_hecke` is done **once per braid**
(not per partition). Per-partition work drops to **O(n!)** lookups
+ multiplications, **independent of dim**.

Per-atom cost (cf. table above):

| n | current (seminormal, all λ) | GP (all λ via shared T_β expansion) | ratio |
|---|---|---|---|
| 9  | ~1.8 × 10⁷ MPFR matvec | 9! + p(9)·9! ≈ 1.1 × 10⁷ ops | ~2× |
| 12 | ~2.4 × 10¹⁰ MPFR matvec | 12! + p(12)·12! ≈ 4 × 10¹⁰ ops | ~0.6× |
| 15 | ~6.5 × 10¹³ MPFR matvec | 15! + p(15)·15! ≈ 1.7 × 10¹⁴ ops | ~0.4× |

**GP is NOT a free win** — the n! factor in `braid_to_hecke` doesn't
scale well. At n=15 it's actually slower. The win is when:
- `braid_to_hecke` output is **sparse** (most c_w = 0). For local
  braid words (small |word|), basis expansion has support << n!.
  Empirically `reduce_basis_to_minimal_length` reports D braid
  (n=6, |word|=23) takes ~700 basis elements → 145 → 17 minimal
  (per its docstring). **If sparsity factor is ~100× at high n, GP wins.**
- The expansion is **cached** per word and reused across atoms
  sharing word patterns.

Current scaffolding gaps (per docstring):
- 🚧 Memoization across multiplications
- 🚧 PyO3 export (so Python can call it)
- 🚧 Cross-validation with seminormal at q_0 on full atomic braids
- F3.2.ζ partial conjugation reduction implemented but limited
  (the docstring notes D braid n=6 takes the basis from ~700 → 145,
  of which 17 are minimal-length and 128 still need the full
  cuspidal-move algorithm of Geck-Pfeiffer 2000 §3.2)

**Verdict**: highest-leverage candidate IF the sparsity at
n≥12 lives up to the small-n pattern. The cross-validation step
(1-2 days) is the gate — if at q_0 GP matches seminormal to
expected precision on D and T, then full implementation
(F3.2.ζ cuspidal-moves + memoization + PyO3) is a 1-2 week
project that potentially **10-100× speedup at n=12+**.

### D. Murnaghan–Nakayama / Ram's q-character recursion (research-level)

Classical MN: χ^λ(C_µ) for a cycle-type-µ class element of S_n is
a sum over rim-hook tableaux of shape λ filled with content µ.
Cost: O(p(n) × |MN-recursion-tree|) per partition. The Hecke
analogue (Ram 1991, Halverson–Ram 2005) replaces the rim-hook sign
with a q-deformation; computable but more complex.

If implemented:
- Cost: O(per-class MN tree) per λ per cycle type. For ⁴He at H_12,
  ~50 nontrivial cycle types × 77 partitions × MN-tree of size
  ~exp(c√n) ≈ 10⁴ each ≈ ~4×10⁷ ops. **6 orders of magnitude
  faster than seminormal at n=12.**
- The braid is reduced to its T_w expansion first (via GP), then
  each T_w is class-evaluated via MN.

**Effort**: 2-3 weeks (no existing in-tree scaffold; need to port
Halverson–Ram). Highest payoff at n≥15 but research-level work
to validate at MPFR precision.

### E. Use `seminormal_matrices_mpfr` + dense linear algebra

`seminormal_mpfr.rs:290` already exposes `seminormal_matrices_mpfr`
which materializes σ_i as sparse matrices at MPFR precision.
Multiplying these together as dense MPFR matrices and tracing the
result is O(dim³ × |word|) per partition — **worse** than the
current O(dim² × |word|) sparse-matvec approach for varied-σ
words. **No win.**

### F. f64 cross-check path (against `no float64` directive)

`hecke-canonical-chi --dps 0` already supports an f64 fast path
via `chi_lambda_braid_f64`. f64 ops are ~50× faster than MPFR-50dps.
Useful as a cross-check / smoke test, **NOT** as a production path
per the standing directive. Mention only for completeness.

### G. Block-fusion (per existing audit — **re-analysis: does NOT win in current architecture**)

Originally claimed in
[`2026-05-18-lie-eigendecomp-sigma-g.md`](2026-05-18-lie-eigendecomp-sigma-g.md):
"Fuse `(σ_0 σ_1⁻¹)^3` confinement word once per partition. ~3-5×
speedup."

**Re-analysis (2026-05-18, this PR follow-up):** the claim does not
survive close inspection of the current `chi_lambda_braid_mpfr`
algorithm. At dim = 7700 (max for n=12):

| approach | per-partition cost | concrete |
|---|---|---|
| current sparse-matvec (6 ops × dim outer × O(dim) per matvec) | **6 × dim²** | 3.6 × 10⁸ |
| fused F = (σ_0 σ_1⁻¹)³ as dense, 1 matvec × dim outer | **dim³** | 4.6 × 10¹¹ |
| F³ as sparse (~64 × dim nnz after 3 sparse matmuls) | **64 × dim²** | 3.8 × 10⁹ |

Both fused variants are **worse** than the current sparse-per-op
path because the σ matrices are already sparse (1×1 + 2×2 blocks)
and per-matvec stays O(dim). Block fusion only pays off when **F
is reused** across many applications — which only happens if
**multiple atoms are batched in one Rust call**. The current
`canonical_tr_m_via_rust.py` invokes the binary **once per atom**
(subprocess per atom), so within a single invocation, no reuse.

The original "3-5× speedup" estimate from the Lie-eigendecomp
audit appears to have implicitly assumed batched-atom calls; the
audit also explicitly noted "matrix exponentiation F^A via
repeated squaring + Lie diagonalization is O(d² log A) instead of
O(A × d²)" — but each nucleon's F is at a DIFFERENT generator
base index (`gen = 3k, 3k+1`), so F at k=0 ≠ F at k=1; matrix
exponentiation doesn't apply within a single atomic braid.

**Revised verdict**: G in isolation is NOT a 1-2 day mechanical
win. To realize the claimed speedup, the change requires:
- Refactor `canonical_tr_m_via_rust.py` to batch atoms per Rust
  invocation, AND
- Add a per-(λ, gen_base, nucleon_type) cache for intra-nucleon
  fused operators
- Total effort: ~1 week, not 1-2 days

Without batching, candidate **B (inner rayon over the dim outer
loop)** is the genuine "mechanical safe win". G can be revisited
once atom batching is implemented; the savings only materialize
across atoms, not within one atom call.

## Recommended sequence (REVISED)

In dependency / risk-adjusted order, after the §G re-analysis:

| # | Candidate | Effort | Speedup (n=12 / n=15) | Risk |
|---|---|---|---|---|
| 1 | **B — rayon over dim outer loop** | ½ day | ~Nc on max-dim partition | Low; thread-local MPFR buffers |
| 2 | **C — Geck-Pfeiffer cross-validation** (gate for full impl) | 1-2 days | TBD; if sparsity is ~100×, 10× / 50× | Medium; depends on sparsity |
| 3 | **G + atom batching** (combined) | ~1 week | 3-5× / 3-5× | Medium; subprocess refactor + cache |
| 4 | **C-full — GP implementation** (after gate passes) | 1-2 weeks | per gate result | Medium; need F3.2.ζ cuspidal moves |
| 5 | **D — q-MN recursion** | 2-3 weeks | 100× / 1000× (estimated) | High; research-level porting |

Step 1 (B) is the genuine **mechanical safe win**: per-partition
inner rayon parallelism, ½ day, definitely speeds up max-dim
partitions by ~Nc on n ≥ 15 workloads.

Step 2 (C-gate) is the **highest-leverage 1-2 day investment**: a
cross-validation of `chi_lambda_via_gp_hoefsmit` against
`chi_lambda_braid_mpfr` at q_0 on D/T/³He tells us whether the GP
basis-expansion sparsity holds at higher n; if yes, the GP path is
10-50× faster than the seminormal path at n=12+.

Step 3 (G + batching) becomes attractive **only after** step 1+2
characterise the workload. The original "1-2 day mechanical"
estimate was wrong; the actual realisation needs atom batching to
make F reusable across atom invocations.

Steps 4+5 are **research-grade** and target ⁶Li and beyond
(n ≥ 18) where steps 1+2 alone are not enough.

## What does NOT pay off (negative results worth recording)

- **Dense matrix multiplication of σ matrices** (E): worse complexity
  than current sparse-matvec for varied-σ words.
- **Per-σ_g eigendecomposition** (per Lie-eigendecomp audit): no
  savings for varied-σ braids (atomic braids), since the same matrix
  doesn't appear repeatedly.
- **f64 fast path as production** (F): violates the precision
  directive.

## Cross-references

- [`tools/hecke-engine/src/seminormal_mpfr.rs`](../../tools/hecke-engine/src/seminormal_mpfr.rs) — current `chi_lambda_braid_mpfr`
- [`tools/hecke-engine/src/wenzl_lr.rs`](../../tools/hecke-engine/src/wenzl_lr.rs) — `chi_lambda_canonical_h_n_mpfr` (the canonical wrapper with averaged-crossing direct-substitution)
- [`tools/hecke-engine/src/bin/hecke_canonical_chi.rs`](../../tools/hecke-engine/src/bin/hecke_canonical_chi.rs) — the binary entry point
- [`tools/hecke-engine/src/geck_pfeiffer.rs`](../../tools/hecke-engine/src/geck_pfeiffer.rs) — alternative algorithm (scaffolded, not wired)
- [`2026-05-18-y-lambda-scaling-analysis.md`](2026-05-18-y-lambda-scaling-analysis.md) — identifies the per-partition Hoefsmit product as the next bottleneck (max-dim table)
- [`2026-05-18-lie-eigendecomp-sigma-g.md`](2026-05-18-lie-eigendecomp-sigma-g.md) — covers block-fusion (candidate G)

## Status

**Documentation-only audit** — no Rust code changes in this branch.
Next concrete step is implementing candidate G (confinement block
fusion) which is mechanical and low-risk. Candidates B and C
follow naturally; C is the gate for the bigger payoff at n ≥ 15.
