# Matrix-M optimization path for A=8, A=9 — investigation (2026-06-08)

> **Status**: investigation triggered during PR #2004 follow-up. Goal:
> identify which optimization tier (Phase 1.3 (μ_p, μ_n) extraction
> vs Rust port vs alternatives) gives the most leverage for the
> heaviest atoms ⁸Be (A=8, n=24) and ⁹Be (A=9, n=27), currently
> "days-of-compute" via direct `chi_q_via_gp`.

## 1. Why A=8,9 are days currently

| atom | A | n | p(n) | max dim V_λ | typical chi_q_via_gp wall |
|------|---|---|------|-------------|---------------------------|
| ⁴He  | 4 | 12| 77   | 132         | 25 ms / partition         |
| ⁵Li  | 5 | 15| 176  | 1430        | ~100 ms / partition       |
| ⁶Li  | 6 | 18| 385  | 3375        | ~1 s / partition          |
| ⁷Li  | 7 | 21| 792  | 9009        | ~10 s / partition         |
| ⁸Be  | 8 | 24| 1575 | 32760       | ~hours / partition (extr.)|
| ⁹Be  | 9 | 27| 3010 | 165620      | ~day / partition (extr.)  |

`chi_q_via_gp` cost per partition is dominated by the
`dim_V_λ × dim_V_λ` Hoefsmit seminormal-form matrix product across
the canonical braid word (Geck-Pfeiffer reduction). The matrix
construction is O(`dim²`) memory, O(`dim² · word_length`) compute.

For ⁹Be λ = (5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 1) etc., `dim² ≈ 2.7×10¹⁰`
entries per matrix. Even at 10 ns per fp operation that's 270 s per
multiply × ~60 multiplies (word length 71-83 for these atoms) ≈
4-5 hours per partition × 3010 partitions ≈ **~600 atom-days for
⁹Be**. Hard wall regardless of multi-core.

## 2. Optimization-tier table — projected speedups

Working from the matrix-M μ_p factorisation already proved (PRs
#1980 → #2004) and the structural identity in `docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md` §5.

### Tier 0 — current state (post-PR #2004, ⁵Li in production)

- sp.Rational backend: **~3× slower than Rust chi_q_via_gp**
  (aggregate). Loses high-dim.
- mpfr backend: **~1.34× faster than Rust** on ⁴He; ~equal on
  ⁵Li; degrades further for A ≥ 6 high-dim λ because per-multiply
  cost grows with running denominator/precision.
- **Verdict**: matrix-M μ_p alone is NOT sufficient for A ≥ 6.
  Need a smaller per-call block size.

### Tier 1 — Phase 1.3 (μ_p, μ_n)-block extraction

Within each μ_p block, further decompose under H_3(right) via H_3(q)
q-Young symmetrizers. Per-block sizes drop from
`c_LR · dim(V_μ_p) · dim(V_skew(λ/μ_p))` to `c_LR · dim(V_μ_p) ·
dim(V_μ_n)`. For μ_p, μ_n ⊢ 3, both dims ≤ 2, so per-block size
becomes **c_LR · ≤ 4**.

Total compute = Σ_{(μ_p, μ_n): c_LR > 0} (c_LR · 4)² · word_length.
Roughly p(3) × p(3) = 9 blocks per λ; typical c_LR ≤ 3 for low λ
and ≤ ~10 for high-dim λ. Worst-case block ≈ 40, vs current dim 1000s.

#### Projected per-partition wall for ⁹Be (n=27):

| backend | per-partition wall | atom (×3010 parts) |
|---------|-------------------:|--------------------:|
| Rust GP (current) | ~1 day | 8 years |
| mpfr μ_p only | ~1-5 days | 30-150 years |
| **mpfr (μ_p, μ_n)** | **~5-50 ms** | **15 s – 2.5 min** |
| Rust (μ_p, μ_n) | ~50 µs – 5 ms | 150 ms – 15 s |

**(μ_p, μ_n)-block extraction is the critical path** — it turns
the per-partition cost from `dim²` (scaling with λ) to bounded
block² (bounded by ~40²). This is the difference between
"days per atom" and "minutes per atom" at A=9.

### Tier 2 — Rust port of the matrix-M block path

The (μ_p, μ_n)-block matrices are tiny (≤ 4×4 in most cases). A Rust
port using `BigRational` or `mpfr-rs` would replace per-multiply
mpmath cost (~10-100 µs for 4×4 at 50 dps) with native
`mpfr_mul` (~100 ns). Estimated **~100-1000× per-multiply**.

Combined Tier 1 + Tier 2: ⁹Be sweep in seconds.

### Tier 3 — multi-level recursive decomposition (audit §6.2)

For A ≥ 3, recurse on the bridge structure:

  β = β_0 · σ_3 · (β_1 · σ_6 · (β_2 · σ_9 · ...))

Each recursive level applies Tier 1's (μ_k, μ_{k+1}, …, μ_A)-block
extraction. For deeper atoms, the block sizes shrink further at
each level. The audit's full bridge-table approach (Phase 2)
combines all levels into a single precomputed table per (λ, μ_0,
…, μ_{A-1}) tuple.

For ⁹Be: per (μ_0, μ_1, …, μ_8) tuple, block is c_LR · ∏ dim(V_{μ_k})
≤ ~256 at worst (8 levels × max-dim-2 per level). Many tuples zero.
Multi-level adds only modest gain over Tier 1's single-level (μ_p,
μ_n) split, since the heavy cost was already gone.

**Verdict**: Tier 3 is a follow-up nice-to-have. Tier 1 + Tier 2
already deliver "minutes per atom".

## 3. Alternative / orthogonal optimizations

### 3a. Skip zero-LR (μ_p, μ_n) pairs

Many partition pairs (μ_p, μ_n ⊢ 3 with λ ⊢ 3A) have c_LR = 0.
`pyhecke_native.lr_coefficient` already computes these; skip
nonzero pairs entirely. **Saves ~30-60% in block count.**

### 3b. Precompute seminormal H_3 matrices once

Current path rebuilds seminormal matrices per λ. The H_3 matrices
for (3), (2,1), (1,1,1) are FIXED. Precompute once, reuse across
ALL λ. **Saves ~1-5 ms per partition × 3010 partitions = 3-15 s
overhead removed at A=9.** Small relative to per-call compute but
non-trivial.

### 3c. Parallel batch via Rust `chi_lambdas_via_gp`

`pyhecke_native.chi_lambdas_via_gp` (Patch 2, exposed but unrouted
in production per `derived_chi_catalogue_parallel.py` docstring)
batches all partitions in one Rust call. For atoms at A=8,9, this
might shave the Rust-call overhead but doesn't help the per-partition
matrix cost. **Modest gain (~5-20%) — not a path to A=9.**

### 3d. Bar symmetry (already wired)

Tier 3 Phase 3 (PR #1952): conjugate pairs λ, λᵀ derive one from
the other. Already saves ~50% across the sweep. Stacks
multiplicatively with everything above.

## 4. Recommended path forward

**Critical path = Tier 1 (Phase 1.3) + Tier 2 (Rust port).**

Sequence:

1. **Phase 1.3 prototype** — sympy/mpmath (μ_p, μ_n)-block
   extraction on small λ for VALIDATION. One PR. Demonstrates the
   block sizes drop as predicted.

2. **Phase 1.3 production** — wire into mpfr backend
   (`derived_chi_catalogue_matrix_m_mpfr.py`) as a `--use-mu-n-blocks`
   flag. Cross-validate against the existing μ_p-only path on D / T
   / ³He / ⁴He / ⁵Li. One PR.

3. **A=6 catalogue extension** — re-run sweep with the new backend.
   Should finish in minutes. (Without Phase 1.3, takes ~hour.)

4. **A=7 catalogue extension** — re-run. ~10s minutes with Phase 1.3,
   hours without.

5. **A=8, A=9 catalogue extension** — viable with Phase 1.3. Phase
   1.3 enables A=9 in ~minutes; Tier 2 brings it to seconds.

6. **Tier 2 Rust port** — after Phase 1.3 lands. Substantial
   engineering effort (hecke-engine extension + PyO3 binding + cross-
   check with the mpmath Phase 1.3 backend). Final tier.

## 5. Risk / unknowns

- **q-Young symmetrizer numerical stability**: the Hecke
  symmetrizer involves `1 / [3]!_q` factor. At q_0 ≈ 1.11,
  `[3]!_q ≈ 6.6` — well away from zero, so no numerical concerns.
- **LR coefficient table size**: for A=9 we'd need c_LR^λ_{μ_0,
  μ_1, …, μ_8} multi-LR tables. The existing
  `pyhecke_native.lr_coefficient` is two-argument; we'd iterate it.
  Per audit §6.2 the largest table is 51975 entries for ⁹Be —
  one-time precompute, < 1 s.
- **mpmath precision for stacked operations**: cumulative matrix
  products at 50 dps have error ~O(word_length · block_size · 10⁻⁵⁰).
  For A=9 word ~83, block ~40: error ~10⁻⁴⁷. Still well within
  any production tolerance.

## 6. Conclusion

Phase 1.3 (μ_p, μ_n) extraction is the **enabling step** for A=8,9.
Without it, no amount of Rust porting makes A=9 tractable, because
the per-partition `dim²` cost dominates. With Phase 1.3, A=9 fits
in minutes on the existing mpmath backend; with Tier 2 Rust port,
seconds.

Recommended next PR: Phase 1.3 sympy prototype for λ ⊢ 6 (deuteron)
demonstrating the (μ_p, μ_n)-block extraction matches the existing
μ_p-only path, then ramp to mpfr backend wire-in.
