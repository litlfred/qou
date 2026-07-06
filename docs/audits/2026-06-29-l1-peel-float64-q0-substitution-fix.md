# L1 1 ppQ certification — the markov_peel float64 q₀ leak (fixed 2026-06-29)

**Branch:** `claude/l1-1ppq-cross-check-repair-2026-06-29`

## Summary

The live L1 cross-check (`computations/cross_check_trM_1ppb.py`) reported the
four nuclei (deuteron, tritium, ³He, ⁴He) as **DIVERGE** against the 1 ppQ
(1e-15) gate. Root cause: the `markov_peel` producer substituted the **float64**
`q_parameter.Q` (17 digits) into its otherwise-**exact symbolic** atomic
trace, truncating the result to ~16 good digits. Because the nuclei have a
smaller `|tr_M|`, the same absolute float64 noise (~1e-16–1.7e-15) became a
*relative* delta above the 1e-15 gate. Fix: substitute the full 50-digit q₀
(`Q_50_DIGIT_STR`) as a high-precision `sympy.Float`. peel then agrees with the
chi-cache leg at ~1e-19 and all atoms certify at 1 ppQ.

This is the repair of **Defect 1** in
[`2026-06-17-l1-1ppq-certification-gap.md`](2026-06-17-l1-1ppq-certification-gap.md)
("the peel witness is float64-limited"), re-diagnosed against current `main`
(the producer no longer crashes on the color-weighted crossing — that was fixed
between 2026-06-17 and now — and the p/n q-param mismatch has also cleared; the
sole remaining leak was the q₀ substitution).

## The leak, precisely

The atomic trace is built as an **exact** sympy expression in the symbolic
substrate parameter `q`:

```
tr_M_atomic(1, 1, use_fast=False).atoms(sympy.Float)  →  set()   (zero Floats)
```

The color-weighted inter-nucleon crossing `σ − h·(½ − δ/4)·𝟙` emits an exact
symbolic coefficient (`-HA·(½ − d_sym/4)`, `d_sym` = symbolic
`flavor_split_subleading(q)`), so the trace carries no float contamination of
its own. The contamination entered only at the **final numeric evaluation**:

```python
# markov_peel_atomic_witness.py (before)
from q_parameter import Q as Q0                 # 1.1099785955573347  (float64, 17 digits)
tr_at_q0_mpf = mpmath.mpf(str(tr_sym.subs(q_sym, Q0).evalf(50)))
#                                          ^^ float64 q₀ → truncates the exact
#                                             symbolic trace to ~16 digits
```

Substituting a Python `float` into a sympy expression injects a 53-bit `Float`;
every downstream digit past ~16 is noise, regardless of the `.evalf(50)`.

### Measured (deuteron, A=2)

| substitution | `peel_vs_chi` relative delta | verdict |
|---|---|---|
| float64 `q_parameter.Q` (old) | **1.485e-15** | DIVERGE (> 1e-15 gate) |
| 50-digit `Q_50_DIGIT_STR` (new) | **9.13e-20** | certifies at 1 ppQ |

Per-atom old `peel_vs_chi`: deuteron 1.485e-15, ³He 1.936e-15, tritium 1.628e-14
(worst — smallest `|tr_M|` ≈ 0.104 amplifies the fixed float64 absolute noise).

## Why `Q_MP` is not a fix

`qou_substrate.constants` exports `Q_MP = mpf('1.1099785955573347')` — but this
mpf was built from the float64 `Q`, so it too carries only 17 good digits.
`Q_50_DIGIT_STR = '1.1099785955573347198997632204832250266562084087802'` is the
**sole** 50-dps source in the constants module. Any high-precision symbolic
substitution of q₀ must go through the string, not `Q` / `Q_MP`.

## Fix

`computations/markov/markov_peel_atomic_witness.py`:

```python
from q_parameter import Q_50_DIGIT_STR          # 50-digit q₀, NOT float64 Q
_DPS_GUARD  = mpmath.mp.dps + 8
Q0_SYMPY_HP = sp.Float(Q_50_DIGIT_STR, _DPS_GUARD)
...
tr_at_q0_mpf = mpmath.mpf(str(tr_sym.subs(q_sym, Q0_SYMPY_HP).evalf(_DPS_GUARD)))
```

The `add_parameter("q0", …)` witness field now records the 50-digit q₀ as well.

## Scope check — no other live leak

- `markov_peel.tr_M_atomic` (use_fast=False) builds Float-free symbolic traces
  for deuteron **and** tritium (verified `atoms(sympy.Float) == set()`), so the
  Ocneanu fallback in `markov_trace_canonical.py` does **not** inject float64 for
  A≥3. The producer fix is therefore complete for every atom it covers.
- Two `__main__` smoke-test demos (`markov_peel.py`, `markov_trace_canonical.py`)
  substitute the float64 q₀ for a coarse console sanity print only; they do not
  feed any witness. Tidied for consistency but not load-bearing.

## Verification

```bash
python3 computations/markov/markov_peel_atomic_witness.py      # regenerate witness (50-digit q₀)
python3 computations/cross_check_trM_1ppb.py                   # all atoms certify at 1 ppQ
```
