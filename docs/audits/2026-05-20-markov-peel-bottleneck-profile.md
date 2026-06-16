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
| 3 | **Pre-shift NF cache** (`@lru_cache` on `_shift_nf(proton_nf, δ)`) — currently re-shifts the cached H_3 NF every call | **0× in production** — see footnote ⚠️ | low (~1 hr) | low — trivial cache decoration |

⚠️ **Strategy #3 footnote (2026-05-20 follow-up):** the `_shift_nf` and `register_quotient` machinery lives in the **slow sympy fallback path** (`markov_peel.tr_M_atomic` line 343, guarded by `if pre_register_nucleons and A >= 2`). The **production fast path** routes through `tr_M_atomic_fast` (line 318) for `use_fast=True` (the default), which **skips the pre-register optimisation entirely** (per `hecke_laurent_fast.py:275-278` comment: "Skips the `pre_register_nucleons` quotient-folding optimisation entirely. ... with the LaurentQ inner loop running 5-25× faster per term, the unfolded reduce is fast enough."). The bottleneck in the fast path is downstream of reduction — it's the sympy trace-assembly handoff (Strategy #1). Strategy #3 as originally framed only helps the slow path. The refactor still lands (cleaner code, scaffolding for any future pre-register-in-LaurentQ work) but does not change ⁶Li / ⁷Li walls.
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

**Strategies #3 + #4** were originally framed as cheap quick wins (~50 % wall at A ≥ 4 each, ≤ 1 hr engineering). After implementation, see the Strategy #3 footnote ⚠️ above: that estimate applied to the **slow sympy path only**, not to the production fast path (which is the path the profile measured). Strategy #4 (`@lru_cache` on `tr_M_word`) is still a candidate; it would apply to either path, but its potential gain depends on word-repetition rates that the Phase-1 LaurentQ implementation already exploits via `_tr_M_word_lq_cached` (LRU cache, maxsize 100K). So once #1 lands, #4 is largely subsumed.

## Phase-1 implementation results (2026-05-20)

`computations/laurent_q_trace.py` ships a Phase-1 implementation of Strategy #1 (`ZHLaurent` + `tr_M_word_lq` + `tr_M_element_lq` + `tr_M_atomic_lq`). Phase-1 scope: empty / single-top / multi-top Case A. Case B (braid relation with σ_{top-1} in segment) raises `NotImplementedError` and the caller falls back to the sympy path.

**Empirical speedup** vs the current `markov_peel.tr_M_atomic` (production fast path) on the canonical atom set:

| atom | sympy path | LaurentQ path | rel.diff | speedup |
|------|-----------:|--------------:|---------:|--------:|
| p    |  0.07 s    |  0.00 s       | 0.00e+00 | 29.3×   |
| n    |  0.00 s    |  0.00 s       | 0.00e+00 | 1.3×    |
| D    |  0.08 s    |  0.05 s       | 4.29e-16 | 1.8×    |
| T    |  1.44 s    |  0.68 s       | 1.07e-15 | 2.1×    |
| ³He  |  0.59 s    |  0.35 s       | 1.34e-16 | 1.7×    |
| ⁴He  | 11.14 s    |  4.16 s       | 7.40e-15 | **2.7×**|

All values agree to machine precision (rel diff < 1e-14). Phase-1 implementation reaches Case A on all currently catalogued atomic braids; no Case-B fallback hit in practice.

**Projected impact** at larger A (assuming the ~2.7× scaling holds):

| atom | sympy projected | LaurentQ projected | total wall improvement |
|------|----------------:|-------------------:|------------------------|
| ⁵Li  |   67 s          |   ~25 s            | 67s → 25s (saves 42s) |
| ⁶Li  | 1036 s (17 min) |  ~380 s (~6 min)   | 17 min → 6 min |
| ⁷Li  | ~5 hr           |  ~1.8 hr           | unlocks ⁷Li within reasonable budget |

**Phase-2 follow-ons** (not in this audit's scope):
- Implement Case B (braid relation) natively in LaurentQ
- Implement ocneanu_fallback in LaurentQ
- Wire `tr_M_atomic_lq` as the default `use_fast=True` path (currently parallel module)

## Out-of-scope (this audit)

- ⁷Li mass-table extension (now feasible via Strategy #1 + ~1.8 hr budget; not run in this audit)
- H_{12} A-operator production extract (separate research-grade compute, framework already on `main` via PR #852)

## References

- `markov_peel.py:225` (`tr_M_atomic` — current production entry point)
- `hecke_laurent_fast.py:267` (`tr_M_atomic_fast` — current "fast path", still sympy-dominated in trace assembly)
- `markov_trace_canonical.py:185` (`tr_M_element` — the sympy bottleneck)
- `compute-audit.md §P20` (recursive Markov-axiom ascent chosen over matmul)
- PR #852 (just merged — added §Long-compute logging discipline)
