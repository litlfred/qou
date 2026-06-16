# Gram / NF precision audit — the 111/100 rational-q approximation

**Date:** 2026-06-16
**Branch:** `claude/youthful-faraday-5snwms` (PR #2355)
**Trigger:** A "NO FLOAT64" pass on the σ_F electron-shell chain surfaced
an apparent ~1e-5 discrepancy in the H₃(q) Gram matrix.

## TL;DR

- The canonical **float64 `G` is correct** — computed at the true
  substrate q₀ = `1.1099785955573347…`. It is **not** buggy.
- The discrepancy was a **q mismatch**, not a reduction bug: the
  exact-Fraction path (`hm_exact`, `nf_of_word(exact=True)`,
  `markov_trace_combo(exact=True)`, `_*_FRAC` constants) evaluates at the
  **rational approximation q = 111/100 = 1.11**, which is ≈ 2e-4 away
  from q₀, with z ≈ `4993/10000` ≈ 1e-4 away from the true
  z = 1/(q^½+q^−½).
- Initial mis-diagnosis: an earlier commit on this branch
  (`fd4edb62`) claimed `_reduce_nf` produced a wrong NF and that `G`
  diverged from the "rigorous" NF on 19/36 entries. **That was wrong** —
  the "rigorous" reference was `nf_of_word(exact=True)`, i.e. the
  111/100 path. `_build_gram` was reverted unchanged; the float `G`
  was right all along. This document is the correction of record.
- **Added (the genuine fix):** `pyhecke.gram.gram_matrix_mp` / `tr_m_mp`
  / `z_mp` — a float64-free Gram/trace at the **true q₀**, 50-dps mpmath,
  cross-checked to `G` at 1.1e-16.

## Why two q's exist

`pyhecke.gram` carries two parallel evaluation paths:

| Path | q | z | Arithmetic | Purpose |
|------|---|---|-----------|---------|
| **float** (`hm`, `nf_tr`, `G`, `TR_M`) | q₀ = 1.1099786 (true substrate) | irrational, f64 | float64 | numeric Gram/trace |
| **exact-Fraction** (`hm_exact`, `nf_of_word(exact=True)`, `_*_FRAC`) | 111/100 = 1.11 | 4993/10000 | exact ℚ | exact-rational *structural* checks |
| **mp (new)** (`gram_matrix_mp`, `tr_m_mp`, `z_mp`) | q₀ (true substrate) | irrational, 50-dps | mpmath | float64-free high-precision Gram/trace |

The Fraction path's q = 111/100 is a deliberate exact-rational
*structural* convenience (NF reduction stays in ℚ), **not** a
high-precision substrate value. `gram.markov_trace_combo`'s own docstring
already states the exact mode agrees with the float mode only to ~1e-4
(the z-truncation), "the float path is the more accurate."

## Footgun

Reading `exact=True` as "exact ⇒ high precision" is wrong: it is exact
*rational arithmetic at q = 1.11*. At the L2 100× precision goals
(ppb-level) a 2e-4 q error is fatal. Consumers needing precision must use
the **float** path (`G`, `nf_tr`) or the new **mp** path
(`gram_matrix_mp`, `tr_m_mp`), never the Fraction path.

## Live consumers of the 111/100 / 4993 approximation

Surveyed via `grep -rn '111, 100|_Q_FRAC|_H_FRAC|_Z_FRAC|4993|exact=True'`:

| File | Use | Precision-critical? |
|------|-----|---------------------|
| `tools/pyhecke/python/pyhecke/atom.py` | `build_atom_nf_exact`, `nf_channel_exact` (uses `_H_FRAC`, `_Q_FRAC`, `_TR_M_FRAC`, `_*_EIG_FRAC`) | **Audit needed** — if these feed production masses/binding they are at q=1.11. The float `build_atom_nf` (true q₀) is the numeric path. |
| `tools/pyhecke/python/pyhecke/gram.py` | the Fraction path itself + new audit note | by design (structural) |
| `computations/hecke_core_legacy.py` | re-imports `_*_FRAC` | legacy |
| `computations/hadron_knot_table.py` | `HeckeEngine(111, 100)` | knot-table; verify if numeric-precision-critical |
| `tools/pyhecke/tests/test_markov_combo.py`, `test_gram_values.py` | assert the 111/100 / 4993 values | intentional (tests the approximate path) |
| `computations/_deprecated/*` | many `Fraction(111,100)` | deprecated, out of scope |

## Recommendation

1. **Do NOT "fix" `G`** — it is correct at q₀. (Done: `_build_gram`
   left unchanged.)
2. **Use the new mp accessors** wherever a float64-free, true-q₀,
   high-precision Gram/trace is needed (e.g. clarabel-MPFR LP duals).
3. **Follow-up (separate, owner's call):** audit `atom.py`'s exact path
   consumers — if `build_atom_nf_exact` / `nf_channel_exact` results flow
   into any precision-critical production value, either (a) document that
   they are structural-only at q=1.11, or (b) add a true-q₀ mp variant.
   This is NOT done here; it needs blast-radius review.

## Cross-check evidence

```
gram_matrix_mp (true q₀, 50-dps) vs float64 G : max |Δ| = 1.1e-16   ✓
exact nf_of_word(e⁻²) σ₀-coeff = 2321/11100 = 0.2090991   (q = 1.11)
float nf_of_word(e⁻²) σ₀-coeff = 0.20906032               (q = q₀)
h(q₀) = q₀ − q₀⁻¹ = 0.20906032 ;  h(111/100) = 2321/11100 = 0.2090991
```

The 0.2090991 vs 0.20906032 gap (≈ 3.9e-5) is exactly h(1.11) − h(q₀) —
a q difference, not a reduction error.

## Blast-radius verdict (2026-06-16)

Per the owner's "audit whether the exact path feeds precision-critical
production" directive:

| Consumer | q used | Precision-critical? | Verdict |
|----------|--------|---------------------|---------|
| **L1/L2 precision pipeline** (`mass_binding_dashboard.py` → `q_parameter.Q`; `mass_table_comprehensive.py` → `Q_50_DIGIT_STR`) | **q₀** (true) | yes — the headline goals | **CLEAN** — uses q₀, never 1.11 |
| `build_atom_nf_exact` / `nf_channel_exact` (atom.py exact path) | 111/100 | — | **No production call sites** (re-exported but uncalled); dead in production |
| `hadron_knot_table.py` (`HeckeEngine(111,100)`) → `hadron-knot-table.witness.json` | 111/100 | appendix illustration (B_MeV @ 4 dp) | **Only live exposure**; appendix knot table, NOT a precision-goal claim. ~2e-4 q error ⇒ sub-keV on few-MeV binding. |

**Bottom line:** no precision-critical production value is at the wrong
q. The 111/100 approximation is confined to (a) a dead exact-rational
atom path and (b) the appendix `hadron-knot-table` witness. The headline
L1/L2 precision goals are unaffected.

**Optional low-priority follow-up:** repoint `hadron_knot_table.py` at
q₀ so the appendix table sits at the canonical substrate.

**Attempted + reverted (2026-06-16):** `HeckeEngine(11099786, 10000000)`
(exact-rational q₀) is **intractable** — the exact-Fraction engine
(`hecke/hecke_engine.py`) blows up at high-denominator q (q₀^k has
denominator 10^{7k}, so products of traced volumes across ~40 generators
become thousand-digit Fractions and the 19-atom table never terminates).
The 111/100 is therefore a *deliberate tractability choice* for the
exact-rational engine, not an oversight. The genuine q₀ route is the
**float/mpmath path** (`pyhecke.build_atom_nf` /
`atom_per_generator_volumes` at q₀), which would require rerouting
`hadron_knot_table.py`'s volume computation off the rational engine — a
moderate refactor that changes the witness values/structure. Left for a
separate owner-scoped task; the table is not precision-critical. The
script now carries an explanatory comment + this pointer (the printed
`q = …` header already shows q₀ via the imported `Q`, while the engine
internally used 1.11 — also documented).
