# Rust port scoping — markov_peel hot path

**Date:** 2026-05-20
**Trigger:** "what can we add to rust? where are performance bottlenecks we can move over? be careful of roundtripping rust/python (you can lose speed optimizations with conversions)"
**Companion:** [`2026-05-20-markov-peel-bottleneck-profile.md`](2026-05-20-markov-peel-bottleneck-profile.md) (the Python-side bottleneck audit + Phase-1 LaurentQ implementation in `laurent_q_trace.py`)

## Existing Rust integration (and why it doesn't scale)

`canonical_mass_table_extended.py` already routes to a Rust binary `hecke-canonical-chi` via subprocess + JSON IPC:

```
method        ⁴He wall   ⁵Li wall   regime
markov_peel   13 s       89 s       symbolic-q, scales through H_15+
rust_f64      12 s       > 1500 s   direct Hoefsmit f64; DOESN'T SCALE
rust_mpfr     ~15 min    impractical at H_15+
```

The Rust paths use per-Wedderburn-block Hoefsmit matmul (dim 462 at λ=[4,4,4]) — this is the wrong algorithm at scale per compute-audit P20. The IPC boundary (~5-50 ms per call) is acceptable for the few-call use case but irrelevant to the algorithmic problem.

## Where the roundtrip kills you (and where it doesn't)

The 5Li profile shows 37 M `Basic.compare` + 22 M `cache.wrapper` + 12 M `Numbers.__eq__` calls. **Per-call Rust bindings would not work:**

| Call granularity | Frequency (5Li) | PyO3 boundary | Pure overhead |
|------------------|---------------:|--------------:|--------------:|
| Per-`LaurentQ.__mul__` | 67 K | ~50 ns | 3 ms (fine) |
| Per-`Basic.compare` | 37 M | ~50 ns | **1.85 s** ← dominates if done per-call |
| Per-`cache.wrapper` | 22 M | ~50 ns | **1.10 s** ← same |

**The right granularity:** port the **entire trace assembly** as a single Rust call. Boundary cost amortizes over the whole compute.

## Proposed Rust crate: `crates/markov-peel-rust/`

PyO3 binding exposing one entry point per atomic compute:

```rust
// crates/markov-peel-rust/src/lib.rs
use pyo3::prelude::*;
use pyo3::types::PyBytes;

#[pyfunction]
fn tr_M_atomic(py: Python, z: u32, n: u32) -> PyResult<Py<PyBytes>> {
    // 1. Build atomic braid word for (Z=z, N=n) in Rust
    let word = build_atom_braid_word_3a(z, n, /*include_inter=*/ true);
    // 2. Incremental reduce in LaurentQ-equivalent (rust)
    let reduced = incremental_reduce(&word, max_iter=10_000)?;
    // 3. Markov-axiom recursive ascent (ZHLaurent in rust)
    let zh = tr_M_element(&reduced, 3 * (z + n))?;
    // 4. Serialise ZHLaurent → bytes
    let bytes = zh.to_bytes();
    Ok(PyBytes::new(py, &bytes).into())
}

#[pymodule]
fn markov_peel_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(tr_M_atomic, m)?)?;
    Ok(())
}
```

Python side:

```python
# computations/markov/markov_peel_rust_bridge.py
from markov_peel_rust import tr_M_atomic as _rust_tr_M_atomic
from laurent_q_trace import ZHLaurent

def tr_M_atomic_rs(Z: int, N: int) -> ZHLaurent:
    zh_bytes = _rust_tr_M_atomic(Z, N)         # 1 boundary crossing
    return ZHLaurent.from_bytes(zh_bytes)       # cheap deserialise
```

**Total boundary cost: 1 PyO3 call + 1 bytes deserialise per atom.** O(few μs) overhead, negligible vs the multi-minute compute.

## Rust algorithmic choices

| Decision | Option A | Option B | Recommended |
|----------|---------|---------|-------------|
| Coefficient type | `num_rational::BigRational` (exact) | `f64` (lossy) | **`BigRational`** — matches LaurentQ semantics exactly; trace must hit machine ε against the sympy reference, lossy floats break that |
| Polynomial storage | `Vec<(i32, BigRational)>` (sparse Laurent in q) | `BTreeMap<i32, BigRational>` | **`Vec`** sorted by exponent — better cache locality for the inner mul loop, lower per-element overhead |
| ZHLaurent storage | `Vec<((i32, i32), LaurentQ)>` | `HashMap<(i32, i32), LaurentQ>` | **`HashMap`** — collision rate is low and the lookup pattern (add into existing key) hits the hot path |
| Bigint backend | `num-bigint` | `gmp` / `rug` | **`num-bigint`** — pure Rust, no system libgmp dependency; the coefficients here are small (typical Hecke trace coefficients are integers < 10⁶), so num-bigint's overhead is minimal |
| Threading | rayon over per-word terms | serial | **serial first** — the recursion tree is irregular; parallelism adds memory overhead. Revisit only after the serial version is empirically slow. |
| Memoization | `LruCache` from `lru` crate | `HashMap` (unbounded) | **`LruCache(100K)`** — matches the Python-side bound; bounds memory under worst-case input |
| Serialisation | bincode → PyBytes | direct PyO3 typed objects | **direct PyO3** — let Rust expose a `PyZHLaurent` class with `.evaluate(q, z, h)` and skip the serialise round entirely. The Python `ZHLaurent` becomes a thin shim over the Rust object. |

## Phase plan

| Phase | Scope | Effort | Risk | Speedup |
|-------|-------|--------|------|--------:|
| **0** | Crate skeleton + PyO3 binding + `pip install` workflow (maturin) + smoke test on identity case | 1 day | low | n/a |
| **1** | `LaurentQ` + `ZHLaurent` in Rust, exposed via PyO3; cross-check `(p, n, D, T, ³He, ⁴He).evaluate(q₀, z₀, h₀)` to 1e-30 vs Python | 3-4 days | low | 5-10× over Phase-1 Python (estimate) |
| **2** | `tr_M_word_lq` Rust port with LruCache memoization | 2-3 days | medium (recursion depth + cache semantics) | additional 2-5× |
| **3** | `incremental_reduce` Rust port (LaurentQ rule loop) | 2-3 days | medium (rules R1-R3 are well-defined; R4 quotient ideal skipped per `hecke_laurent_fast.py:246`) | additional 2-3× |
| **4** | Wire `tr_M_atomic_rs` as the default `use_fast=True` path; deprecate JSON-IPC `rust_f64` / `rust_mpfr` (they're algorithmically wrong) | 1 day | low | n/a |

**Total: ~2 weeks focused work for a projected 20-100× over current `markov_peel.tr_M_atomic` production fast path.**

## Cost / benefit at the target atom roadmap

Given the Phase-1 (Python LaurentQ) baseline from `laurent_q_trace.py`:

| atom | Python LaurentQ (proj) | Rust full port (proj) | comment |
|------|----------------------:|----------------------:|---------|
| ⁴He  |  4 s                  |  ~0.05-0.2 s          | ~20-80× |
| ⁵Li  | ~25 s                 |  ~1-3 s               | unlocks fine-grained scans |
| ⁶Li  | ~6 min                |  ~10-30 s             | unlocks ⁶Li iterative sweeps |
| ⁷Li  | ~1.8 hr               |  ~5-15 min            | unlocks A=7 within reasonable budget |
| ⁸Be  | ~12 hr                |  ~30-60 min           | **unlocks A=8 for the first time** |
| ⁹Be  | ~80 hr (infeasible)   |  ~3-6 hr              | feasible within a CI nightly run |

The break-even point is ⁷Li: ~2 weeks of Rust work saves >1.5 hr per ⁷Li run × however many compute campaigns. For ⁸Be / ⁹Be, the Rust port is **enabling**, not optimising.

## Risks / non-trivial decisions

1. **Build infrastructure.** Need `maturin` + cargo workspace; the repo doesn't yet have a `crates/` layout. **Mitigation:** existing Rust binary (`hecke-canonical-chi`) presumably already has a cargo setup — reuse / extend it.
2. **PyO3 + GIL.** PyO3 holds the GIL by default. For long Rust computations, release it with `py.allow_threads(|| ...)`. Otherwise Python sees the call as a blocking syscall + can't respond to KeyboardInterrupt.
3. **BigRational performance.** Pure-Rust `num-bigint` is ~2-3× slower than libgmp. If profiling shows BigRational dominates, switch to `rug` (libgmp wrapper) with a system dep. Defer this decision to Phase 1 measurements.
4. **Floating-point evaluation at boundary.** `ZHLaurent.evaluate(q, z, h)` needs `f64` arithmetic; the Rust side should expose this method natively so we don't ferry BigRationals back to Python. The PyO3 binding for `evaluate` is a one-liner.
5. **Test parity.** Every algorithmic case in the Python `_self_check` must reproduce in Rust to machine precision. Add a Rust-side `cargo test` plus a Python-side cross-check on the full atom set (p..⁷Li).
6. **Case B (braid relation).** Phase-1 Python raises `NotImplementedError`. The Rust port should match — caller catches and falls back to the sympy path. Phase 2 of `laurent_q_trace.py` will implement Case B natively in Python; the Rust port follows once that lands.

## Out of scope (this scoping doc)

- Actual implementation (queued behind explicit author go/no-go due to ~2-week scope)
- ⁸Be / ⁹Be mass-table extensions (enabled by, but not part of, the Rust port)
- R4 quotient ideal in Rust (the LaurentQ Python path already skips R4 per `hecke_laurent_fast.py:246`; revisit only if A ≥ 8 walls require it)
- Replacing the existing `hecke-canonical-chi` Rust binary (different algorithm — direct Hoefsmit matmul; not on the markov_peel critical path)

## Recommendation

**Go/no-go decision needed from author.** The work is ~2 weeks focused; the payoff is unlocking A ≥ 8 mass-table compute (currently infeasible) and ~20× routine speedup on A ≤ 7. Items 4-7 in the next-direction recommendations from the bottleneck audit are all gated on this.

If green-lit:
1. Phase 0 (skeleton + maturin) ships as a separate small PR (~1 day) for fast feedback on build infra
2. Phases 1-4 ship as a single PR (~1.5 weeks)
3. Cross-check vs Python LaurentQ on every catalogued atom before merging Phase 4

If yellow-lit or no-go:
- The Phase-1 Python `laurent_q_trace.py` (already shipping in #859) provides 2.7× over the prior fast path and unlocks ⁷Li within a ~1.8 hr budget. That's the floor.

## References

- `laurent_q_trace.py` (Phase-1 Python LaurentQ — PR #859, just merged or about to)
- `2026-05-20-markov-peel-bottleneck-profile.md` §Optimisation candidates (Strategy #1 implementation)
- `hecke_laurent_fast.py:246` (R4 quotient ideal deferral note)
- `markov_peel.py:312-318` (route selection: `use_fast` + IPC paths)
- `compute-audit.md §P20` (recursive Markov-axiom ascent vs Wedderburn matmul)
- `compute-audit.md §P29` (profile-first discipline)
