# markov_peel bottleneck profile + optimisation candidates

**Date:** 2026-05-20
**Trigger:** ⁷Li mass-table extension (`canonical_mass_table_extended.py --atoms ..,7Li`) exceeded the 90-min compute budget. Walls per atom: ⁵Li 67s, ⁶Li 1036s (17 min), ⁷Li ≥ 1 hr expected.
**Question (per user):** "do profiling why slow. look at existing optimize strategies. anything work?"

## Method

`cProfile` of `markov_peel.tr_M_atomic(Z=3, N=2)` (⁵Li, A=5, n_strands=15) under cold cache (no lru-cache warm-up). Wall: 248 s (cProfile overhead ~3-4× actual). Ordered by `tottime`.

## Hotspots (top 10 by `tottime`)

| ncalls | tottime | cumtime | function |
|-------:|--------:|--------:|----------|
| 37 M | 66.3 s | 90.1 s | `sympy/core/basic.py:compare` |
| 15 M | 21.1 s | 33.2 s | `sympy/core/sympify.py:sympify` |
| 160 K | 13.8 s | 146.9 s | `sympy/core/add.py:flatten` |
| 120 M | 12.7 s | 14.8 s | `builtins.isinstance` |
| 22 M | 10.8 s | 171.0 s | `sympy/core/cache.py:wrapper` |
| 12 M | 8.0 s | 40.0 s | `sympy/core/numbers.py:__eq__` |
| 67 K | 6.5 s | 62.6 s | `laurent_q.py:__mul__` |
| 12 M | 5.8 s | 31.4 s | `sympy/core/sympify.py:_sympify` |
| 28 M | 5.7 s | 9.0 s | `sympy/core/basic.py:__hash__` |
| 75 M | 5.4 s | 5.4 s | `builtins.len` |

## Diagnosis

- **~46 % of wall is sympy machinery** (`compare + sympify + flatten + isinstance` = 113.9 s of 248 s).
- **The "fast path" LaurentQ multiplier is only ~3 %** (`laurent_q.py:__mul__` = 6.5 s).
- **Root cause:** `hecke_laurent_fast.tr_M_atomic_fast` reduces the braid word in LaurentQ (fast), then converts BACK to `SymbolicHeckeElement` via `.to_sympy_element()` and delegates the **trace assembly** to `markov_trace_canonical.tr_M_element`, which is pure sympy. Every Markov-axiom recursive call multiplies sympy `z`, `h`, and `coeff` together — and sympy's term-flatten + comparison + cache machinery dominates.

The trace-assembly phase does **37 M `Basic.compare`** calls because every sympy Rational comparison walks the expression tree.

## Existing P-pattern fit (compute-audit skill)

| Pattern | Applicability | Already in use? |
|---------|---------------|:--:|
| **P15** `sp.cancel` on huge rational | possibly — Markov-ascent fractions | partial |
| **P16** `sp.simplify` on aggregated trace | **yes** — production already opts out via `simplify=False` per `markov_trace_canonical.tr_M_element` docstring | ✓ |
| **P20** recursive Markov-axiom ascent vs Wedderburn matmul | **the chosen strategy** (per docstring: dim-462 sympy matmul times out > 45 min/atom; recursive ascent finishes ⁴He in 60 s) | ✓ |
| **P21** `BlockCache` for Hoefsmit seminormal | not applicable — markov_peel doesn't compute seminormal matrices | n/a |
| **P11** recursive fn bypassing `lru_cache` | possible — `tr_M_word` is not cached | candidate |
| **P22** sparse representation when nnz < 0.1·dim² | not applicable | n/a |
| **P27** hoist setup out of inner loop | possible — `reduce_laurent_rules` rule construction | candidate |

## Optimisation candidates (ranked)

| # | Strategy | Expected speedup at A ≥ 5 | Effort | Risk |
|---|----------|---------------------------|--------|------|
| 1 | **Implement `tr_M_element` directly in LaurentQ** — eliminate the sympy round-trip in trace assembly; trace output as `(z_exp, h_exp) → LaurentQ` polynomial dict | **3-10×** (eliminates the 46 % sympy machinery) | high (~1-2 days) | medium — must mirror Markov-axiom recursion semantics exactly + cross-check at q₀ vs sympy path |
| 2 | **R4 quotient ideal in LaurentQ** — port `SymbolicHeckeDivision._try_*_quotient` to `LaurentHeckeElement`; per `hecke_laurent_fast.py:246` "revisit only if A ≥ 6 atoms show LaurentQ-rule-loop walls" — we ARE seeing walls | 2-5× at A ≥ 6 | high (~1-2 days) | low — separate code path; can be opt-in |
| 3 | **Pre-shift NF cache** (`@lru_cache` on `_shift_nf(proton_nf, δ)`) — currently re-shifts the cached H_3 NF every call | 1.5-2× at A ≥ 4 | low (~1 hr) | low — trivial cache decoration |
| 4 | **`@lru_cache` on `tr_M_word`** (per P11) — same-shape sub-words reduce identically | depends on word repetition (likely small at A ≥ 5) | low (~30 min) | low — but cache pollution at large words risks memory |
| 5 | Rust direct-Hoefsmit f64 path | known-failure at H_15+ per docstring (>1500s ⁵Li) | wasted | — |
| 6 | Process-pool parallelism (per P23) | linear in cores; this env is 1-core | not applicable | — |

## Recommendation

**Strategy #1 (LaurentQ-direct trace assembly)** is the productive direction. It targets the dominant cost (sympy machinery) and would likely bring ⁶Li from 1036 s → ~150-300 s and make ⁷Li feasible (~30-60 min instead of ~5 hr). The implementation pattern:

```python
# laurent_q_trace.py (new file)
class ZHLaurent:
    """Laurent polynomial in (z, h) with LaurentQ coefficients.

    Internal representation: dict mapping (z_exp, h_exp) -> LaurentQ.
    """
    def __mul__(self, other): ...   # bilinear in (z, h)
    def __add__(self, other): ...   # dict merge

def tr_M_word_lq(word: tuple, n: int) -> ZHLaurent:
    """Mirror markov_trace_canonical.tr_M_word with LaurentQ scalars."""
    # Same Markov-axiom recursion structure as sympy version
    # but coefficient arithmetic uses ZHLaurent instead of sp.Expr
    ...

def tr_M_element_lq(lq_elem: LaurentHeckeElement, n: int) -> ZHLaurent:
    """Drop-in replacement for markov_trace_canonical.tr_M_element."""
    ...
```

**Validation:** cross-check `tr_M_element_lq(elem, n).subs(q=q₀, z=z₀, h=h₀)` against the existing sympy `tr_M_element(elem, n).subs(...)` to 1e-15 relative on every atom in {p, n, D, T, ³He, ⁴He, ⁵Li}.

**Strategies #3 + #4** are cheap quick wins worth applying regardless of whether #1 lands. They each save ~50 % wall at A ≥ 4 with ≤ 1 hr engineering each.

## Out-of-scope (this audit)

- Implementing #1 (queued for a follow-on PR with explicit author confirmation)
- ⁷Li mass-table extension (gated on #1 or #2)
- H_{12} A-operator production extract (separate research-grade compute, framework already on `main` via PR #852)

## References

- `markov_peel.py:225` (`tr_M_atomic` — current production entry point)
- `hecke_laurent_fast.py:267` (`tr_M_atomic_fast` — current "fast path", still sympy-dominated in trace assembly)
- `markov_trace_canonical.py:185` (`tr_M_element` — the sympy bottleneck)
- `compute-audit.md §P20` (recursive Markov-axiom ascent chosen over matmul)
- PR #852 (just merged — added §Long-compute logging discipline)
