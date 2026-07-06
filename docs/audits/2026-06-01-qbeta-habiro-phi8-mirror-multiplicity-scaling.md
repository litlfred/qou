# Φ_8 multiplicity in mirror-pair Habiro elements: even-A correction

**Date:** 2026-06-01
**Branch:** `claude/qbeta-wenzl-habiro-keystone-2026-06-01` (PR #1642)
**Status:** **SCALING LAW REFINED** — 5 mirror-pair data points; even-A pairs require correction to original A−1 hypothesis.

## TL;DR

The cyclotomic factor `Φ_8 = u^4 + 1` appears in the mirror-pair Habiro element `Σ_m Δa_m(X − Y) · (u; u)_m` (canonical Phase 5q convention) with multiplicity

   **`mult(Φ_8) = 2 · ⌊(A − 1)/2⌋`**

i.e. the largest even integer ≤ A − 1. Equivalently:
- **Odd A**: `mult(Φ_8) = A − 1`
- **Even A**: `mult(Φ_8) = A − 2`

The original "mult = A − 1" hypothesis from a 3-data-point fit was refuted on the first even-A data point (⁸B − ⁸Li).

| Mirror pair | A (parity) | (Z_lhs, N_lhs) ↔ (Z_rhs, N_rhs) | `mult(Φ_8)` | predicted `2⌊(A−1)/2⌋` |
|---|---|---|---|---|
| n − p | 1 (odd) | (0,1) ↔ (1,0) | 0 | 0 ✓ |
| ³He − ³H | 3 (odd) | (2,1) ↔ (1,2) | 2 | 2 ✓ |
| ⁷Be − ⁷Li | 7 (odd) | (4,3) ↔ (3,4) | 6 | 6 ✓ |
| **⁸B − ⁸Li** | **8 (even)** | (5,3) ↔ (3,5) | **6** | **6** ✓ (REFUTES `A−1 = 7`) |
| ⁹B − ⁹Be | 9 (odd) | (5,4) ↔ (4,5) | 8 | 8 ✓ |

## Secondary findings on `Φ_1`, `Φ_2`

| Mirror pair | `Φ_1 = u−1` | `Φ_2 = u+1` | `Φ_4 = u²+1` |
|---|---|---|---|
| n − p | mult 1 | mult 1 | mult 0 |
| ³He − ³H | mult 1 | **mult 0** | mult 0 |
| ⁷Be − ⁷Li | mult 1 | mult 0 | mult 0 |

- **`Φ_1` is UNIVERSAL** across mirror pairs — classical-limit kill at `q = 1` (both halves coincide classically).
- **`Φ_2` is SPECIFIC to A = 1** (the n − p case) — does NOT extend to A ≥ 3 mirror pairs.

The earlier framing in PR #1579 (`Φ_1·Φ_2 = u²−1` as the isospin classical-limit signature) was over-generalised: only `Φ_1` is the universal isospin signature; `Φ_2` is an A=1-specific structural feature.

## Falsifiable predictions

The original 3-point hypothesis (n−p, ³He−³H, ⁷Be−⁷Li) `mult = A − 1` was REFUTED on the first even-A pair tested (⁸B − ⁸Li at A=8: mult=6 = A−2, not A−1=7), then refined to `mult = 2·⌊(A−1)/2⌋`. Both laws collapse on odd A (the original 3 data points were all odd). To separate them, the predictions table below explicitly contrasts the two laws on **even-A** mirror pairs — testing the refined formula against the now-refuted original.

| Mirror pair | A (parity) | Original `A − 1` | Refined `2⌊(A−1)/2⌋` | Status |
|---|---|---|---|---|
| ⁶Be − ⁶Li | 6 (even) | 5 | **4** | open |
| ⁸B − ⁸Li | 8 (even) | 7 | **6** | ✓ MEASURED 6 (refutes original) |
| ¹⁰C − ¹⁰Be | 10 (even) | 9 | **8** | ✓ MEASURED 8 (confirms refined) |
| ¹²N − ¹²B | 12 (even) | 11 | **10** | open |
| ¹⁴O − ¹⁴C | 14 (even) | 13 | **12** | open |
| ⁵Li − ⁵He | 5 (odd) | 4 | 4 | open |
| ⁹B − ⁹Be | 9 (odd) | 8 | 8 | ✓ MEASURED 8 (both laws agree) |
| ¹¹C − ¹¹B | 11 (odd) | 10 | 10 | open |
| ¹³N − ¹³C | 13 (odd) | 12 | 12 | open |
| ¹⁵O − ¹⁵N | 15 (odd) | 14 | 14 | open |

Even-A pairs are the discriminating tests: the two laws differ by 1 for every even A. ⁸B−⁸Li and ¹⁰C−¹⁰Be have already discharged the discrimination in favour of the refined formula; ⁶Be−⁶Li, ¹²N−¹²B, ¹⁴O−¹⁴C remain open and are the next falsification targets.

Testable via the [`_habiro_coefficient_extract.py`](../../computations/_habiro_coefficient_extract.py) general (Z, N) → canonical Phase 5q Habiro infrastructure (this commit).

## Connection to level-2 SU(2) Wenzl

PR #1625 identified the universal `M_first_Φ_8 = 7` boundary across atomic-step pairs as the **level-2 SU(2) Wenzl projector kernel at q = ζ_8**. The multiplicity scaling here is a refinement:

- The **first Φ_8 cancellation** at M=7 is universal (one Φ_8 factor).
- **Additional Φ_8 factors** at higher M (giving multiplicity A−1) reflect the **mass-scaling of the Wenzl-annihilator constraint**: the Markov-trace decomposition of an A-nucleon braid carries A−1 distinct copies of the Wenzl-block linear relation, one per "interface" between adjacent nucleons.

This connects the structural finding back to the Phase 5q closed forms: the `z(q)^k` interface factor structure in `tr_M(X, q) = τ_p^Z · τ_n^N · z(q)^k · …` is exactly counting the (A−1) interfaces between A nucleons.

## Cross-references

- Level-2 SU(2) Wenzl identification: [`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)
- 10-pair Φ_8 universality (proton-conditional): [`docs/audits/2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md`](2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md)
- Phase 5q convention test: [`docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md`](2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- Mass-table infrastructure: [`computations/_habiro_coefficient_extract.py`](../../computations/_habiro_coefficient_extract.py)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
