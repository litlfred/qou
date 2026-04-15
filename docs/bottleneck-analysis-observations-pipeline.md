# Bottleneck Analysis: Physical Observations Expected-Value Pipeline

**Date:** 2026-04-15
**Scope:** `folio-assistant/computations/`, `tools/hecke-engine/`, `scripts/witness-audit.ts`

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

## Priority Order

1. Phase-space vectorization (quick win, ~1 hour, ~500x speedup)
2. Python→Rust bridge for ground-state search (high impact, ~1 day)
3. DAG runner for witness pipeline (high impact, ~1 day)
4. Batch git queries in audit (quick win, ~2 hours)
5. hecke_core precompute cache (moderate, ~half day)
6. Compress large witness JSON (trivial)
