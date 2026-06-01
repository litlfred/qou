# Φ_8² Δa_m interference mechanism — coordination ledger

**Branch:** `claude/qbeta-habiro-phi8-interference-2026-06-01`
**PR:** _to be opened_
**Goal:** Identify the categorical mechanism producing the universal `Φ_8² = (u^4+1)²` factor in atomic-step Habiro elements — concretely, what witnesses `ζ_8 = e^(iπ/4)` in the `Δa_m` polynomial interference.

## Why this question

This session (PR #1579 + #1618) established two structural facts:

1. **`Φ_8² = (u^4+1)²` is UNIVERSAL** across atomic-step Habiro elements: (D−n), (³He−D), (⁴He−³He). Convention-invariant (appears in both habiro-witness `include_inter=True` and Phase 5q canonical).
2. **The naive mechanisms are REFUTED:**
   - Strand-doubling chain Φ_{2^{k+1}} — falsified (Φ_16/Φ_32 don't appear)
   - z(q)² interface factor — refuted (z(q)^k Habiro-expands to monomial u^k, no cyclotomic)
   - m=8 Pochhammer boundary — refuted (Φ_8 appears at M=7 already, BEFORE the Pochhammer boundary)

The pre-m=8 `Φ_8` appearance proves the cyclotomic structure lives in the **Δa_m interference itself**, not in any of the three naive sources. The categorical witness of ζ_8 in the Habiro coefficient polynomials is the open question.

## Concrete substructure to investigate

| Quantity | What it is | Habiro depth where Φ_8 enters |
|---|---|---|
| `(u; u)_8` Pochhammer | Mechanical first source of `(1−u^8)` | m = 8 |
| `(u; u)_16` Pochhammer | Mechanical first source of `(1−u^8)²` | m = 16 |
| `Σ Δa_m·(u;u)_m` for (D−n) | OBSERVED: Φ_8 at partial-sum M=7, Φ_8² at M=12 | M = 7 (pre-Pochhammer!) |
| `Σ Δa_m·(u;u)_m` for (³He−D) | OBSERVED: Φ_8² appears | TBD |
| `Σ Δa_m·(u;u)_m` for (⁴He−³He) | OBSERVED: Φ_8² appears | TBD |

The pre-Pochhammer `Φ_8` MUST arise from algebraic relations among the `a_m(X) − a_m(Y)` polynomials directly. These are integer polynomials in `u` with specific structural patterns (small-integer coefficients, partition-function appearance at the top shell — see PR #1579 + #1618 audits).

## Tracks for this branch

1. **Direct Δa_m interference scan.** For each pair, compute the partial sum `S_M = Σ_{m=0..M} Δa_m·(u;u)_m` and factor over ℤ[u]. Identify the smallest M at which Φ_8 enters and which `Δa_m` terms contribute the `(u^4+1)` factor. This reveals the algebraic interference pattern.

2. **Eigenphase-at-ζ_8 categorical search.** Compute Δa_m(ζ_8) for each m. If ζ_8 is a structural root, then `Δa_m(ζ_8) = 0` for some m (or a specific linear combination). Identify the algebraic relation in terms of categorical objects (Hecke character at q^4 = −1, Burau eigenvalue at ζ_8, etc.).

3. **Generating-function analysis.** Treat `Σ_m Δa_m(u)·t^m` as a bivariate generating function. The Φ_8² universality may emerge as a Padé denominator or residue at a specific (u, t) pole.

## Master ledger cross-link

- 1ppQ Q_β master: [`docs/coordination/1ppq-qbeta.md`](1ppq-qbeta.md)
- PR #1579 (merged): commit [`57b5fa2d3a`](https://github.com/litlfred/qou/commit/57b5fa2d3a)
- PR #1618 (in review): [`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](2026-06-01-qbeta-habiro-followup.md)
- Falsification: [`docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md`](../audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
- Mechanism investigation (z(q)² refuted): [`docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md`](../audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)
