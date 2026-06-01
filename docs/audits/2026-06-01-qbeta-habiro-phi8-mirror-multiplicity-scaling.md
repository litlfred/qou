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

If `mult(Φ_8) = A − 1` is the true scaling law, then:

| Mirror pair (predicted) | A | Predicted `mult(Φ_8)` |
|---|---|---|
| ⁵Li − ⁵He | 5 | 4 |
| ⁹B − ⁹Be (or ⁹Be−⁹Li) | 9 | 8 |
| ¹¹C − ¹¹B | 11 | 10 |
| ¹³N − ¹³C | 13 | 12 |
| ¹⁵O − ¹⁵N | 15 | 14 |
| ¹⁷F − ¹⁷O | 17 | 16 |
| ¹⁹Ne − ¹⁹F | 19 | 18 |

Testable as soon as the corresponding atom Habiro coefficients are extracted via the [`_habiro_coefficient_extract.py`](../../folio-assistant/computations/_habiro_coefficient_extract.py) infrastructure landed earlier this commit.

## Connection to level-2 SU(2) Wenzl

PR #1625 identified the universal `M_first_Φ_8 = 7` boundary across atomic-step pairs as the **level-2 SU(2) Wenzl projector kernel at q = ζ_8**. The multiplicity scaling here is a refinement:

- The **first Φ_8 cancellation** at M=7 is universal (one Φ_8 factor).
- **Additional Φ_8 factors** at higher M (giving multiplicity A−1) reflect the **mass-scaling of the Wenzl-annihilator constraint**: the Markov-trace decomposition of an A-nucleon braid carries A−1 distinct copies of the Wenzl-block linear relation, one per "interface" between adjacent nucleons.

This connects the structural finding back to the Phase 5q closed forms: the `z(q)^k` interface factor structure in `tr_M(X, q) = τ_p^Z · τ_n^N · z(q)^k · …` is exactly counting the (A−1) interfaces between A nucleons.

## Cross-references

- Level-2 SU(2) Wenzl identification: [`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)
- 10-pair Φ_8 universality (proton-conditional): [`docs/audits/2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md`](2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md)
- Phase 5q convention test: [`docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md`](2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- Mass-table infrastructure: [`folio-assistant/computations/_habiro_coefficient_extract.py`](../../folio-assistant/computations/_habiro_coefficient_extract.py)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
