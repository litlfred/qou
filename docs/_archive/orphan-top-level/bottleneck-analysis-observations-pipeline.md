# Bottleneck Analysis: Physical Observations Expected-Value Pipeline

**Date:** 2026-04-15
**Scope:** `computations/`, `tools/hecke-engine/`, `scripts/witness-audit.ts`

## Pipeline Architecture

```
q_parameter.py (q₀ from m_μ/m_e + Vol(4₁))
  → hecke_core.py (H₃(q): NF basis, Gram matrix, Wedderburn weights)
  → ~211 Python computation scripts
  → ~144 .witness.json files (structured: computed vs expected)
  → witness_base.py (staleness via script content hash)
  → witness-audit.ts (unified staleness audit)
  → 91 content blocks in observations/ (reference witness data)
```

## Bottlenecks

### 1. CRITICAL — Ground-State Ordering Search (Combinatorial Explosion)

**Files:** `hecke_engine.py:131-150`, `braid-registry.py:98-141`

Ground-state ordering for N(p,n) searches C(A,p) permutations.
Each evaluates A-1 generator volumes at O(A²) per volume.

| Nucleus | A  | C(A,p)     | Method     |
|---------|----|------------|------------|
| ¹²C     | 12 | 924        | exhaustive |
| ¹⁴C     | 14 | 3,003      | exhaustive |
| ⁵⁶Fe    | 56 | 7.6×10¹⁵  | heuristic  |
| ²³⁸U    | 238| ~10⁷⁰     | heuristic  |

Python `hecke_engine.py` uses `Fraction` exact arithmetic (~100x slower
than float). The braid-registry (269 nuclei) takes hours to regenerate.

**Fix:** Route Python scripts through the Rust `hecke-engine` binary,
which has rayon parallelism and proper BigInt support. Memoize ground-state
orderings in a persistent cache keyed by (p, n, q_rational).

### 2. CRITICAL — Phase-Space Integration (Pure Python Loop)

**Files:** `all-nuclei-transfer-matrix.py:125-138`, `halflife-from-transfer-matrix.py:53-60`

Fermi beta-decay phase space uses a 50,000-step Python `for` loop per
nucleus. Called 12× per run (6 nuclei × predicted + experimental Q).

```python
for k in range(n_steps):  # 50,000 iterations in pure Python
    W = 1.0 + (k + 0.5) * dW
    p_e = math.sqrt(W*W - 1)
    ...
```

**Fix:** Vectorize with numpy (single `np.linspace` + array ops).
Estimated speedup: ~500x.

### 3. HIGH — No Pipeline Runner (Manual Script Invocation)

211 computation scripts with no orchestration. When `q_parameter.py`
changes, all 144 witnesses go stale. No dependency graph or `make`-like
runner exists. `witness-audit.ts` detects staleness but does not trigger
recomputation.

**Fix:** Build a DAG runner (`scripts/run-witnesses.py`) that:
1. Reads import dependencies between scripts
2. Checks staleness via `witness_base.check_witness_staleness()`
3. Runs only stale scripts in topological order
4. Parallelizes independent scripts

### 4. HIGH — Python ↔ Rust Engine Duplication

Three separate implementations of Hecke algebra computation:

| Engine              | Language | Precision           |
|---------------------|----------|---------------------|
| `hecke_engine.py`   | Python   | Exact (Fraction)    |
| `hecke_core.py`     | Python   | Float64 + numpy     |
| `tools/hecke-engine` | Rust    | BigInt/CRT/float    |

Python scripts don't call the Rust engine. The Rust engine has 19 binaries
covering different precision/algorithm trade-offs, plus rayon parallelism.

**Fix:** Add a Python wrapper that calls the Rust binary via subprocess
and parses JSON output. Route heavy computations (A > 14) through Rust.

### 5. MODERATE — hecke_core Re-initialization Per Script

Every script re-imports `hecke_core`, which recomputes:
- Wedderburn-Artin weights
- Gram matrix eigenvalue decomposition
- Fine structure constant (CS corrections)
- Nuclear energy scales

This happens 211× when running all scripts (~10s total overhead).

**Fix:** Serialize precomputed constants to a JSON/pickle cache.
Only recompute when q_parameter.py changes.

### 6. MODERATE — Witness Audit Sequential Git Calls

**Files:** `scripts/witness-audit.ts:80-88`, `scripts/lean-witness.ts:64-74`

Each staleness check calls `git log -1 --format=%H -- <file>` via
`execSync`. With ~243 files: ~15-25 seconds of subprocess overhead.

**Fix:** Single `git log --name-only` batch query, parse results.

### 7. MINOR — 152K-Line Witness JSON

`quark-level-knot-table.witness.json` is 151,943 lines.
Dominates I/O during audits.

**Fix:** Compress or split into per-nucleus files (already done for
braid-registry).

## Witness Usage Analysis

Of 144 `.witness.json` files:
- **20** are linked to content blocks via `contentBlock` field (13.9%)
- **124** are orphaned — exploratory/historical, not displayed in paper
- **103** of 204 scripts produce orphaned witnesses

Content-linked witnesses:

| Content block | Witnesses |
|--------------|-----------|
| `def:molecular-braid` | 4 (ch-bond, frobenius-lp, trefoil-scan, unified-mass) |
| `def:h2-molecular-braid` | 2 (hh-trefoil, hh-vertex) |
| `prop:h2-lp-dual-binding` | 2 (h2-integer-lp, h2-molecular) |
| `prop:spectral-decomposition-qvalue` | 2 (qvalue-rep-theory, rosso-jones) |
| `rem:atom-mass-full-hecke` | 2 (atom-mass-derived, atom-mass-full-hecke) |
| `rem:q-integer-mass-table` | 2 (channel-product, q-integer-bw-7term) |
| `rem:amc-calculations` | 1 (topological-mass-table) |
| `thm:topological-mass` | 1 (mass-from-q-symbolic) |
| others | 4 (full-witness, picard-lefschetz, tau-lepton, universal-ilp) |

**Recommendation:** Focus pipeline runs on the 20 content-linked witnesses.
Use `run_pipeline.py --content-only` to skip exploratory scripts.

## Implemented Fixes

### 1. `phase_space.py` — Vectorized Fermi integral (bottleneck #2)

Replaces the 50K-step Python loop with numpy vectorization.
Measured 18x speedup with full numerical agreement (2.2e-15 relative error).

### 2. `hecke_startup_cache.py` — Precomputed constants (bottleneck #5)

Serializes Gram matrix, Wedderburn weights, fine structure constant, BW
coefficients, and nucleon NFs to JSON. Cache invalidates automatically when
`q_parameter.py`, `experimental_constants.py`, or `hecke_core.py` change.

- Generation: 88ms (one-time)
- Cache load: 20ms vs 70ms fresh import (3.5x faster)
- 59 keys covering all downstream-consumed constants

### 3. `run_pipeline.py` — Dependency DAG runner (bottleneck #3)

Scans import statements to build a dependency graph, checks staleness,
propagates staleness through dependencies, and runs scripts in topological
order.

Features:
- `--dry-run`: show what would run
- `--content-only`: only content-linked witnesses (20 scripts)
- `--list-deps`: print dependency graph
- `--list-orphaned`: find unlinked witnesses
- `--force SCRIPT`: force rerun + dependents
- `--jobs N`: parallel execution (future)

## Remaining Work

1. Python→Rust bridge for ground-state search (bottleneck #1, highest impact)
2. Batch git queries in witness-audit.ts (bottleneck #6)
3. Compress/archive orphaned witnesses (bottleneck #7)
4. Migrate `all-nuclei-transfer-matrix.py` to use `phase_space.py`
