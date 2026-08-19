# Φ_8 mirror-pair scaling: A=6 refutes the refined `2⌊(A−1)/2⌋` formula

**Date:** 2026-06-01
**Branch:** `claude/qbeta-c3-eigenphase-scaling-map-2026-06-01` (PR #1649)
**Status:** **BOTH scaling laws REFUTED** — original `A−1` and refined `2⌊(A−1)/2⌋` fail on ⁶He−⁶Be.

> **🛑 SUPERSEDED 2026-08-18 — this doc's numbers are computed on the wrong
> object; scoped, not corrected (bean `qou-0ndb`).** The mirror-pair element
> here is `Σ_m Δa_m(X − Y)·(u;u)_m`, formed by subtracting two witnesses'
> Habiro coefficients. Each witness's `a_m` expand *its own
> denominator-cleared numerator* `p = d·t`, so that sum is `d_X·t_X − d_Y·t_Y`,
> not the pair difference — and the denominators are built out of Φ₄ and Φ₈,
> the very factors being measured, to **different powers on each member of a
> pair** (⁶He: Φ₈⁴ vs ⁶Be: Φ₈⁸; ¹⁴O: Φ₈¹⁶ vs ¹⁴C: Φ₈¹²; proton: Φ₈² vs
> neutron: none). Proved sorry-free in
> [`QOU/Habiro/MirrorPairNormalisation.lean`](../../content/quantum-observable-universe/lean/QOU/Habiro/MirrorPairNormalisation.lean)
> (`coeffDiff_at_coincidence`). Differencing the traces instead gives
> `mult(Φ₈) = 2⌊(A−1)/2⌋` on **10/10** pairs with `Φ₁ = Φ₂ = 1` and `Φ₄ = A`.
> Read the tables below as a record of what was measured, not as the pair's
> cyclotomic content. Full analysis, including which specific claims here do
> not survive:
> [`2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md`](2026-08-18-mirror-pair-a-m-differencing-normalisation-defect.md).

> **Both refutations in this doc are gone under the corrected differencing:**
> A=6 measures Φ₈ = 4 (predicted 4) and A=14 measures 12 (predicted 12). The
> doc's `Φ_4 never appears`, `Φ_2 ⟺ even A OR A=1`, and *"no closed form in A
> can capture this"* all fail — Φ₄ = A, Φ₂ ≡ 1, and the refined closed form
> holds 10/10.


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

**Connection to existing magic-shell propositions in the corpus** (per AGENTS.md §"Before declaring 'open' math" corpus-grep — the framework already has this):

- [`prop:categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/mass-endomorphism/categorical-neutrality-saturated-shells.md) — At magic `n ∈ {2, 8, 20, 28, 50, 82, 126}`, the full-twist `Δ²_n` acts as identity on the mass endomorphism Φ_n ⇒ Φ_n is supported on self-conjugate partitions (content sum `c(λ) = 0`).
- [`conj:diagrammatic-double-magic-lr-fusion`](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md) — Double-magic (both Z, N magic) ⇒ LR-fusion of Z-block and N-block is rigid: single self-conjugate Specht module on the diagonal.
- [`prop:magic-numbers-from-q`](../../content/quantum-observable-universe/observations/magic-numbers-from-q.md) — Magic numbers {2, 8, 20, 28} EMERGE from substrate q₀ via Hoefsmit seminormal forms (no empirical magic list used).
- [`conj:homological-shell-condensation`](../../content/quantum-observable-universe/) — Homological / BB-collapse coincidence at the magic ladder.
- **MAG-1 audit** (2026-05-02): all 7 magic numbers numerically verified — self-conjugate partition support on the magic ladder.

**The Φ_8 multiplicity drops are the mirror-pair empirical signature of these propositions:** when a mirror-pair half hits a magic shell, `prop:categorical-neutrality-saturated-shells` restricts that half's Wedderburn support to self-conjugates. The Wenzl-annihilator linear-relation count in the pair-difference decreases ⇒ lower `mult(Φ_8)`.

| Pair | Magic structure | mult(Φ_8) | Refined | Verdict |
|---|---|---|---|---|
| A=3 ³He−³H | Z=2 vs N=2 (odd valence) | 2 | 2 | match |
| A=5 ⁵Li−⁵He | N=2 vs Z=2 (odd valence) | 4 | 4 | match |
| **A=6 ⁶He−⁶Be** | **Z=2 vs N=2 (EVEN valence, 2 paired)** | **2** | **4** | **ANOMALY** |
| A=14 ¹⁴O−¹⁴C | **Z=8 vs N=8 (EVEN valence, 2 paired holes)** | **4** | **12** | **ANOMALY** |

Refined hypothesis: **anomaly = one magic shell per half + EVEN paired valence on the non-magic side**. The paired valence couples to a self-conjugate Wedderburn block, enhancing the contraction. (A=3, A=5 have odd valence, so the contraction is incomplete.)

Candidate empirical invariants (need LR-fused per-block compute to verify):

- The actual Wedderburn-block multiplicities of the canonical Hecke-algebra braid representations for the involved Z, N (require Rust LR bridge per-pair compute)
- The number of "active" partitions λ with first-column ≤ 3 (level-2 Wenzl cutoff) for the pair-specific Markov-trace decomposition AFTER applying the saturated-shells contraction

The right framework is **NOT** a closed-form formula in A — it's the per-block Wenzl-annihilator linear relation count from PR #1625's framing, mediated by per-pair Wedderburn-block content. The probe [`computations/per_pair_wedderburn_enumeration.py`](../../computations/per_pair_wedderburn_enumeration.py) lays out the data; full LR-fused χ_λ evaluation at q = ζ_8 per pair is research-grade and queued.

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
- Mass-table infrastructure: [`computations/_habiro_coefficient_extract.py`](../../computations/_habiro_coefficient_extract.py)
- This branch's extension script: [`computations/extend_even_a_mirror_pair_test.py`](../../computations/extend_even_a_mirror_pair_test.py)
