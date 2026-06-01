# Φ_8 mirror-pair scaling: A=6 refutes the refined `2⌊(A−1)/2⌋` formula

**Date:** 2026-06-01
**Branch:** `claude/qbeta-c3-eigenphase-scaling-map-2026-06-01` (PR #1649)
**Status:** **BOTH scaling laws REFUTED** — original `A−1` and refined `2⌊(A−1)/2⌋` fail on ⁶He−⁶Be.

## TL;DR

Extracting canonical Phase 5q Habiro coefficients for ⁶He (Z=2, N=4) and pairing with the already-extracted ⁶Be (Z=4, N=2) yields:

```
⁶He − ⁶Be (A=6) mirror-pair Habiro element factorization (mod ℤ[u]):
  Φ_1 = u−1  multiplicity 1
  Φ_2 = u+1  multiplicity 1
  Φ_4 = u²+1  multiplicity 0
  Φ_8 = u⁴+1  multiplicity 2
```

Both prior scaling laws predicted `mult(Φ_8) ≥ 4` for A=6:

| Law | Predicted A=6 | Observed | Verdict |
|---|---|---|---|
| Original `A−1` | 5 | 2 | REFUTES |
| Refined `2⌊(A−1)/2⌋` | 4 | 2 | REFUTES |

The refined formula's first prediction beyond the data it was fit on is wrong.

## Updated data (10 mirror-pair data points — extended 2026-06-01 PM)

| Pair | A | Φ_1 | Φ_2 | Φ_4 | Φ_8 | (Z_lhs, N_lhs) ↔ (Z_rhs, N_rhs) | Refined match |
|---|---|---|---|---|---|---|---|
| n − p | 1 | 1 | 1 | 0 | 0 | (0,1) ↔ (1,0) | ✓ |
| ³He − ³H | 3 | 1 | 0 | 0 | 2 | (2,1) ↔ (1,2) | ✓ |
| ⁵Li − ⁵He | 5 | 1 | 0 | 0 | 4 | (3,2) ↔ (2,3) | ✓ |
| **⁶He − ⁶Be** | **6** | **1** | **1** | **0** | **2** | (2,4) ↔ (4,2) | **✗** (predicted 4) |
| ⁷Be − ⁷Li | 7 | 1 | 0 | 0 | 6 | (4,3) ↔ (3,4) | ✓ |
| ⁸B − ⁸Li | 8 | 1 | 1 | 0 | 6 | (5,3) ↔ (3,5) | ✓ |
| ⁹B − ⁹Be | 9 | 1 | 0 | 0 | 8 | (5,4) ↔ (4,5) | ✓ |
| ¹⁰C − ¹⁰Be | 10 | 1 | 1 | 0 | 8 | (6,4) ↔ (4,6) | ✓ |
| ¹²N − ¹²B | 12 | 1 | 1 | 0 | 10 | (7,5) ↔ (5,7) | ✓ |
| **¹⁴O − ¹⁴C** | **14** | **1** | **1** | **0** | **4** | (8,6) ↔ (6,8) | **✗** (predicted 12) |

**Refined formula's score: 8/10 match, 2 anomalies at A=6 and A=14.**

The A=14 anomaly is particularly striking — `mult(Φ_8)` DROPS from 10 (at A=12) to 4 (at A=14), proving the multiplicity is genuinely non-monotonic in A. No closed form in A can capture this — the right framework is the per-block Wenzl-annihilator linear-relation count.

## Patterns that survive 8 data points

**Holds (with NO exceptions):**

- **`Φ_1` multiplicity ≡ 1**: universal across all 8 mirror pairs. The `q=1` classical-limit kill is structural.
- **`Φ_4 = u²+1` never appears**: multiplicity 0 in all 8 pairs.
- **Φ_2 ⟺ even A**: Φ_2 appears iff A is even, with one anomaly:
  - Even A (1, 6, 8, 10): Φ_2 = 1 — appears
  - Odd A (3, 5, 7, 9): Φ_2 = 0 — absent
  - Wait: A=1 is *odd* but Φ_2 = 1. So the correct statement is Φ_2 ⟺ even-A OR A=1. (Equivalently: Φ_2 ⟺ A ≢ 3 mod 4? Let's check: A=1: 1≡1 mod 4 ✓; A=3: 3≡3 mod 4, Φ_2=0 ✓; A=5: 5≡1 mod 4, Φ_2=0 ✗ — not 1 mod 4 explanation.) The cleanest description is just the table.

**Refuted (REFINED FORMULA):**

The refined `mult(Φ_8) = 2⌊(A−1)/2⌋` matched all earlier data but fails on A=6 (predicts 4, observed 2).

**Odd-A pattern (holds across A=1,3,5,7,9):**

`mult(Φ_8) = A − 1` works for ALL 5 odd-A mirror pairs.

**Even-A pattern (sub-stable):**

| A | mult(Φ_8) | A − 2 | A − 4 |
|---|---|---|---|
| 6 | 2 | 4 | 2 |
| 8 | 6 | 6 | 4 |
| 10 | 8 | 8 | 6 |

A=6: matches `A−4`. A=8, 10: match `A−2`. The "even-A" formula is itself not uniform.

## Hypotheses for what's actually going on

The Wedderburn-block structure at q = ζ_8 (level-2 SU(2) Wenzl) determines which partitions λ contribute to the Markov-trace decomposition. The Φ_8 multiplicity counts the **number of distinct Wenzl-block linear relations** the pair-difference triggers, which depends on the Wedderburn-block content of the canonical braid representations for the specific Z, N values — not just A.

Candidate invariants (from current data) that might explain the irregularity:

- `|N − Z|` (isospin component): equals 1 for all odd-A pairs (mult = A−1) and 2 for all even-A pairs (mult irregular)
- The actual Wedderburn-block multiplicities of the canonical Hecke-algebra braid representations for the involved Z, N
- The number of "active" partitions λ with first-column ≤ 3 (level-2 Wenzl cutoff) for the pair-specific Markov-trace decomposition

The right framework is **NOT** a closed-form formula in A — it's the per-block Wenzl-annihilator linear relation count from PR #1625's framing, mediated by per-pair Wedderburn-block content.

## Implication for PR #1642 ledger

The refined-formula claim in [`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`](2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md) needs a third revision:

| Revision | Status |
|---|---|
| Original `mult = A − 1` (3 data points) | REFUTED at A=8 |
| Refined `2⌊(A−1)/2⌋` (5 data points) | REFUTED at A=6 (this audit) |
| Open: per-block Wenzl-annihilator linear-relation count | the real categorical question |

The pattern-fitting approach is structurally inadequate. The data should be interpreted through the level-2 SU(2) Wenzl annihilator decomposition (PR #1625 framing + the Wenzl-Δa_m reframing identified in the T3 exploration for this branch).

## Cross-references

- Mirror-pair-multiplicity-scaling audit (origin of original + refined formula): [`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`](2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md)
- Level-2 SU(2) Wenzl identification (PR #1625): [`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`](2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)
- Mass-table infrastructure: [`folio-assistant/computations/_habiro_coefficient_extract.py`](../../folio-assistant/computations/_habiro_coefficient_extract.py)
- This branch's extension script: [`folio-assistant/computations/extend_even_a_mirror_pair_test.py`](../../folio-assistant/computations/extend_even_a_mirror_pair_test.py)
