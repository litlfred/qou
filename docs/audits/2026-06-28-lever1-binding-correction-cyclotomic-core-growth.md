# Lever-1 fibre kernel, Stage 7: the binding correction has a universal (q−1)² × Φ_d tower and a GROWING non-cyclotomic core

**Date:** 2026-06-28
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)` for the binding genfun)
**Compute:** [`computations/substrate/lever1_binding_correction_cyclotomic_structure.py`](../../computations/substrate/lever1_binding_correction_cyclotomic_structure.py)
**Witness:** [`computations/substrate/lever1-binding-correction-cyclotomic-structure.witness.json`](../../computations/substrate/lever1-binding-correction-cyclotomic-structure.witness.json)
**Precedes:** this audit's two predecessors —
[`2026-06-27-lever1-qinvolution-cyclotomic-kernel.md`](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md) (Stage 1, the factorizations to m=8)
and [`2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md`](2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md) (Stage 6).
**Serves:** `kehn` (Q_β / m_n c_k closure via a Habiro element), `s5bb` (Habiro-element keystone blocker).

## What this stage does

Stages 3–6 proved the binding period `S(m) = Σ_{λ⊢m} dim_q(λ)` and its correction towers are **not**
finite low-order q-difference operators and **not** single low-order q-hypergeometric elements. The
productive remaining attack named there is the **direct cyclotomic (Habiro) structure** of the
additive correction `D(m) := S(m) − (S(m−1) + [m−1]_q·S(m−2))`.

`D(m)` clears to a Laurent polynomial in `q` (denominators are pure `q^k`), so it admits an **exact**
cyclotomic factorization over ℚ:

```
  D(m)·q^{a_m}  =  c_m · (q−1)^{2} · ∏_d Φ_d(q)^{e_{m,d}} · R_m(q),
```

with `R_m` the non-cyclotomic core. This stage computes that factorization symbolically through
`m = 11` (`S(m)` up to `m=11` via the shared cached `young_qdim`), answering two decidable questions.

## Result

| m | cyclotomic factors (besides (q−1)²) | non-cyclotomic core degree | (q−1)-order |
|---|---|---:|---:|
| 4 | Φ₃ | 0 | 2 |
| 5 | Φ₂² Φ₃ Φ₆ | 0 | 2 |
| 6 | Φ₅ | **8** | 2 |
| 7 | Φ₃² Φ₅ | **10** | 2 |
| 8 | Φ₃ Φ₅ Φ₇ | **14** | 2 |
| 9 | Φ₄ Φ₇ | **28** | 2 |
| 10 | Φ₃ Φ₇ Φ₉ | **34** | 2 |
| 11 | Φ₃ Φ₅ Φ₆ Φ₉ | **46** | 2 |

The `m = 4..8` factorizations reproduce the merged 2026-06-27 audit's Stage-1 listing exactly
(`D(4)=(q−1)²Φ₃`, `D(5)=2(q−1)²Φ₂²Φ₃Φ₆`, `D(6)=(q−1)²Φ₅·deg-8`, `D(7)=4(q−1)²Φ₃²Φ₅·deg-10`,
`D(8)=(q−1)²Φ₃Φ₅Φ₇·deg-14`) — a cross-check that the machinery is correct.

Three derived, parameter-free structural facts:

1. **Universal `(q−1)²` prefactor — confirmed through `m = 11`** (Stage 1 had it through `m = 8`).
   Every `D(m)` vanishes to exactly second order at `q = 1`: the deviation from the classical
   involution recursion is `O((q−1)²) = O(h²)`, a pure fibre / q-deformation effect.

2. **Φ_d first-appearance rule (clean for odd `d`).** The smallest `m` at which `Φ_d | D(m)`:
   `Φ₃` at `m=4`, `Φ₅` at `m=6`, `Φ₇` at `m=8`, `Φ₉` at `m=10` — i.e. for odd `d`, `Φ_d` first
   divides `D(d+1)` (`first_m − d = 1`). A derived constraint any candidate kernel must satisfy.
   (Even `d` is less regular: `Φ₂` at `m=5`, `Φ₄` at `m=9`, `Φ₆` at `m=5`.)

3. **The non-cyclotomic core GROWS** — `deg R_m = 0, 0, 8, 10, 14, 28, 34, 46` for `m = 4..11`,
   monotone increasing from `m = 6`. So `D(m)` is **not** a finite cyclotomic object: it has an
   essential, growing non-cyclotomic core. That growing core is the genuine cyclotomic-completion
   (Habiro-ring) content — exactly what one expects given Stages 3–6 found no finite low-order
   operator, and it is the object any candidate binding Habiro element must reproduce.

## Interpretation and scope (AGENTS.md refuted-claim discipline)

- **Positive, derived (structural):** the `(q−1)²` prefactor (through `m=11`), the odd-`d`
  `Φ_d ↦ D(d+1)` first-appearance rule, and the monotone core-degree growth. These are exact facts.
- **Bounded-`MMAX` observation, NOT a proved (b)-exclusion:** "the core grows without bound / `D(m)`
  is not a finite cyclotomic object" is supported by monotone growth through `m = 11` but is not a
  theorem. It is recorded as strong empirical evidence, not a structural exclusion (no proved
  invariant forbids the core stabilising at some larger `m`). The Habiro-ring class is **not**
  refuted; it is the indicated home of the object.

## Methodology note (a bug caught and fixed)

The first cut of this probe classified factors with a name-matching heuristic and **silently dropped
the non-cyclotomic core** (it reported `D(6)` core degree 0, contradicting the merged 2026-06-27
audit's deg-8 cofactor). The discrepancy was caught precisely because `D(4), D(5)` matched the prior
audit while `D(6)` did not — a corpus cross-check, per the AGENTS.md "before declaring" disciplines.
The classifier was rewritten to use **exact polynomial division** (strip `q^k`, divide out each `Φ_d`
to full multiplicity, the remainder *is* the core); the corrected output reproduces the prior audit's
factorizations at `m = 4..8` and extends them to `m = 11`. The Stage-6 q-hypergeometric probe is
unaffected (it operates on exact `D(m)`/`L_m` values, not on this factorization).

## Next decidable step (not run here)

Characterize the **growing core `R_m`** itself: its degree sequence (8, 10, 14, 28, 34, 46) and
whether the `R_m` are palindromic (the 2026-06-27 audit noted the `D(7)` deg-10 cofactor is
palindromic) — i.e. whether the core, after removing the cyclotomic tower, carries its own
bar-symmetric / Habiro structure, or is the irreducible transcendental residue that pins the element
to the full cyclotomic completion rather than any finite sub-object.
