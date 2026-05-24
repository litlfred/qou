# Compute pipeline benchmark table — per-step timing × mathematical object size

**Date:** 2026-05-23 (active — update after each optimization)
**Location:** referenced from `docs/canonical-derivation-cheat-sheet.md`

## Full pipeline: q₀ → mass prediction

Each row = one pipeline step. Columns show the mathematical object
produced, its SIZE at each Hecke level, wall time BEFORE and AFTER
each optimization, and whether the optimization has been implemented.

### Step-by-step benchmark (at q₀ = 1.10997...)

| Step | What it computes | Math object | H₃ (A=1) | H₆ (A=2) | H₉ (A=3) | H₁₂ (A=4) | H₁₅ (A=5) | H₆₀ (A=20, Ca) |
|---|---|---|---|---|---|---|---|---|
| **0. Substrate** | q₀, h_q, ℏ_q, G | scalars (5) | <1ms | — | — | — | — | — |
| **1. Partitions** | enumerate λ ⊢ n | set of shapes | p(3)=3 | p(6)=11 | p(9)=30 | p(12)=77 | p(15)=176 | p(60)=966K |
| **2. SYT enumeration** | standard Young tableaux per λ | dim(V_λ) per λ | max 2 | max 16 | max 42 | max 132 | max 352 | max ~10⁶ |
| **3. Hoefsmit matrices** | σ_k seminormal ∈ ℝ^{dim×dim} | (n-1) matrices per λ | 2×2 ×2 | 16×16 ×5 | 42×42 ×8 | 132×132 ×11 | 352×352 ×14 | huge |
| **4. Braid-word product** | Π σ_k over crossings | dim×dim matrix | 6 cross. | 17 cr. | 29 cr. | 47 cr. | 68 cr. | ~200 cr. |
| **5. Trace → χ^λ** | tr(product matrix) | 1 scalar per λ | 3 vals | 11 vals | 30 vals | 77 vals | 176 vals | 966K vals |
| **6. y_λ weights** | Wenzl-bridge Schur eval | 1 scalar per λ | 3 vals | 11 vals | 30 vals | 77 vals | 176 vals | 966K vals |
| **7. Markov trace** | Σ y_λ · χ^λ | 1 scalar | <1ms | <1ms | <1ms | <1ms | <1ms | <1ms |
| **8. Mass formula** | m_e × Vol/ℏ² × linking weight | 1 scalar | <1ms | <1ms | <1ms | <1ms | <1ms | <1ms |

### Wall-time benchmark: BEFORE and AFTER optimizations

| Atom | A | n | BEFORE (direct Hoefsmit) | Opt #1 (Wenzl LR) | Opt #2 (y_λ cache) | Opt #3 (Hoefsmit cache) | ALL opts | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| p | 1 | 3 | <1ms | — | — | — | <1ms | ✅ |
| n | 1 | 3 | <1ms | — | — | — | <1ms | ✅ |
| D | 2 | 6 | 3.8s | 0.3s | 0.0s (2nd call) | 0.0s (2nd call) | **0.3s** | ✅ Wenzl LR |
| T | 3 | 9 | 27s | <1s | 0.0s | 0.0s | **<1s** | ✅ Wenzl LR |
| ³He | 3 | 9 | 28s | <1s | 0.0s (shared w/ T) | 0.0s | **<1s** | ✅ cached from T |
| **⁴He** | **4** | **12** | **542s** | **0.45s** | **0.0s** | **0.0s** | **0.45s** | ✅ **Wenzl LR (1200×)** |
| ⁶Li | 6 | 18 | ~4 hrs est. | ~5 min est. | cached | cached | **~5 min** | ⏳ not yet run |
| ⁷Li | 7 | 21 | ~days est. | ~30 min est. | cached | cached | **~30 min** | ⏳ not yet run |
| ⁴⁰Ca | 20 | 60 | infeasible | ~days est. | cached | cached | **needs #5+#6** | 🔬 research |

### Optimization status

| # | Optimization | Mechanism | Speedup | Status |
|---|---|---|---:|---|
| **1** | Wenzl LR closed-form at A≤4 | LR decomposition: χ^λ(β₁⊗...⊗β_A) = Σ c^λ_{μν} · χ^μ · χ^ν | **1200×** at A=4 | ✅ **IMPLEMENTED** (commit `38c16d8b3`) |
| **2** | y_λ module-level cache | `@lru_cache` on `_y_lambda_wenzl_bridge_numeric_impl` by (partition, q, dps) | **∞ on repeat** (10-30× amortized) | ✅ **IMPLEMENTED** (this commit) |
| **3** | Hoefsmit numpy cache | `dict` cache by `(shape, round(q, 15))` in `hoefsmit_matrices_numpy` | **∞ on repeat** (10× amortized) | ✅ **IMPLEMENTED** (this commit) |
| **4** | Partition-inclusion recursion (Okounkov-Vershik) | Build H_n matrices from H_{n-1} by adding one cell; O(dim) per new box | **n×** (12× at H₁₂) | 📋 documented; = Wenzl LR at character level |
| **5** | Quaternionic ijk 3-fold symmetry | 3 color tubes → i,j,k cyclic; halve conjugate-pair partitions | **6×** on partition count | 🔬 investigated; commit `557e9d309` wired at Markov-trace level |
| **6** | GB-NF jet-order grading | Grade-by-grade evaluation; each grade reuses previous | **k×** per grade | 🔬 investigated; Rust prefix cache partially covers |
| **7** | Seminormal factorization | σ_i = (h/2)·I + ([2]_q/2)·J_i where J_i²=I; O(dim) per crossing | **dim×** per crossing | 🔬 investigated; superseded by Wenzl LR for current atoms |

### Mathematical object sizes driving the wall

| Level | p(n) | max dim(V_λ) | Total matrix entries | Braid crossings | Dominant cost |
|---|---:|---:|---:|---:|---|
| H₃ | 3 | 2 | 12 | 6 | negligible |
| H₆ | 11 | 16 | 2,816 | 17 | negligible |
| H₉ | 30 | 42 | 52,920 | 29 | seconds (Python) |
| H₁₂ | 77 | 132 | 1,344,816 | 47 | **542s direct; 0.45s Wenzl LR** |
| H₁₅ | 176 | 352 | 21,856,256 | 68 | ~5 min Wenzl LR (est.) |
| H₁₈ | 385 | 854 | 280,866,460 | 92 | ~1 hr Wenzl LR (est.) |
| H₂₁ | 792 | 1,936 | 2,971,392,768 | 119 | ~12 hrs Wenzl LR (est.) |
| H₆₀ | 966,467 | ~10⁶ | ~10¹⁸ | ~200 | infeasible direct; **needs #5+#6** |

### Where caching helps vs doesn't

| Component | Atom-independent? | Cached now? | Cache hit scenario |
|---|---|---|---|
| q₀, h_q, ℏ_q | ✅ | ✅ (module globals) | always |
| y_λ(q₀) for λ ⊢ n | ✅ (same for ALL atoms at same n) | ✅ **NOW** (lru_cache) | T and ³He share H₉; all A=1 share H₃ |
| Hoefsmit matrices for λ | ✅ (same shape + q = same matrix) | ✅ **NOW** (dict cache) | any repeated evaluation |
| χ^λ(β_K) | ❌ (depends on braid word per atom) | ✅ (lru_cache in symbolic; witness on disk) | re-evaluation of same atom |
| Wenzl LR coefficients | ✅ (combinatorial, q-independent) | ✅ (precomputed in Rust) | always |
| GB-NF reduction | per braid word | ✅ (Rust prefix cache) | shared braid prefixes across atoms |
| Vol(𝓑₃), Catalan G | ✅ | ✅ (constants) | always |

### Feasibility wall with all current optimizations

```
A=1-4:   ✅  sub-second (Wenzl LR + caches)
A=5-6:   ⏳  minutes (Wenzl LR, no new infra needed)
A=7-10:  ⏳  hours (Wenzl LR; quaternionic #5 would cut to minutes)
A=11-20: 🔬  quaternionic #5 + jet-graded #6 required
A=20+:   🔬  all of #4-#7 + cluster-decomposition (A=20 → 5×⁴He)
```
