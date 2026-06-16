# Wenzl tower at ζ_n — level-k SU(2) Verlinde extension probe (FALSIFIED)

**Date:** 2026-06-01
**Branch:** `claude/qbeta-habiro-phi8-interference-2026-06-01` (PR #1625)
**Probe script:** [`computations/qbeta/qbeta_habiro_wenzl_tower_zeta_n.py`](../../computations/qbeta/qbeta_habiro_wenzl_tower_zeta_n.py)
**Witness:** [`computations/qbeta/qbeta-habiro-wenzl-tower-zeta-n.witness.json`](../../computations/qbeta/qbeta-habiro-wenzl-tower-zeta-n.witness.json)
**Master ledger entry:** [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
**Status:** **FALSIFIED at levels k=4 and k=6** — the level-2 Wenzl pattern at q = ζ_4 (u = ζ_8, M=7) does **not** extend to a tower of categorical witnesses indexed by the level-k SU(2) Verlinde truncation.

---

## TL;DR

PR #1625 identified a universal cancellation
`S_7(u = ζ_8) = 0` across all three atomic-step Habiro pairs (D−n,
³He−D, ⁴He−³He), interpreted as the level-2 SU(2) Wenzl projector
kernel at q = ζ_4. This probe tested the natural prediction that a
**tower** of analogous cancellations holds at each level k:

> `S_{2(k+2)−1}(u = ζ_{2(k+2)}) = 0` for k = 2, 4, 6, 8

| Level k | u-root ζ_n, n=2(k+2) | Predicted M | Feasible pairs | Hold? | Verdict |
|---|---|---|---|---|---|
| 2 | ζ_8 | 7 | 3 / 3 | **3 / 3** | **CONFIRMED** (baseline) |
| 4 | ζ_12 | 11 | 3 / 3 | 0 / 3 | **FALSIFIED** |
| 6 | ζ_16 | 15 | 2 / 3 | 0 / 2 | **FALSIFIED** |
| 8 | ζ_20 | 19 | 0 / 3 | — | INFEASIBLE (no data) |

At level k=4 (q = ζ_6, u = ζ_12), the predicted boundary M=11 produces
no cancellation in any pair: `|S_11(ζ_12)|` ranges from ≈ 30 to ≈ 860
across the three pairs. The level-6 case is similarly broken.

The integer-normalisation auxiliary prediction `(ζ; ζ)_{n−1} = n` DOES
hold cleanly (`(ζ_8;ζ_8)_7 = 8`, `(ζ_12;ζ_12)_11 = 12`, `(ζ_16;ζ_16)_15 = 16`
all exact), but this is a pure cyclotomic identity independent of the
Habiro Δa_m structure — it does **not** force the partial sum to
vanish.

**Conclusion:** the level-2 cancellation at M=7 must have a more
specific structural origin than a generic level-k SU(2) Wenzl
truncation. Likely candidates:

1. **q = ζ_4 = i is special.** At q = i, q² = −1, q⁴ = 1 — the Hecke
   generator has order 4, and (σ_i)² = q + q⁻¹ = 0, i.e. the
   Temperley–Lieb / Jones-Wenzl projector collapses at a very low
   level. None of the higher ζ_n give q with this property.
2. **A Φ_8-specific algebraic coincidence in the Δa_m sequence.** The
   companion probe `qbeta-habiro-delta-am-partial-sum-scan` shows the
   interference cancellation is between `Sm_prev(ζ_8)` and
   `marginal(ζ_8) = Δa_7 · (ζ_8;ζ_8)_7` — the specific structure of
   the Δa_m polynomials modulo Φ_8 may not have an analogue at higher
   cyclotomics.
3. **Even-vs-odd parity of (k+2).** Levels k=2 and k=6 give k+2 even;
   levels k=4 and k=8 give k+2 even too. So parity is not the
   distinguisher.
4. **The level-2 baseline may itself be a redundancy of a different
   identity** (e.g. tied to the Φ_8² universality at higher M
   documented in PR #1618), not a fresh structural witness.

The FALSIFICATION should be treated as a negative result for the
"tower of categorical witnesses" framing — k=2 is a standalone
algebraic identity, not the first term of a sequence.

---

## Methodology

For each (pair, level_k):

1. Build `S_M(u) = Σ_{m=0}^M Δa_m(u) · (u;u)_m` as integer polynomial
   in `u`.
2. Compute the cyclotomic polynomial `Φ_n(u)` for `n = 2(k+2)`.
3. Symbolic test: does `Φ_n(u)` divide `S_{M-1}(u)`? Does it divide
   `S_M(u)`?
4. Numeric test at 50-dps mpmath: evaluate `|S_{M-1}(ζ_n)|`,
   `|S_M(ζ_n)|`, `(ζ_n;ζ_n)_{M}`. Cancellation is asserted iff
   `|S_M(ζ_n)| ~ 10^{-40}` AND `|S_{M-1}(ζ_n)|` is not (the M=M_first
   discriminator).

Δa_m data sources (same as the level-2 probe):

- `habiro-coefficients-atomic.witness.json` — p, n, D up to m=8 / 12.
- `/tmp/he3.json`, `/tmp/he4.json` — ³He (m≤15), ⁴He (m≤17), from
  PR #1618 branch.

Pair M_max:

| Pair | M_max | Levels with M ≤ M_max |
|---|---|---|
| D − n | 12 | k=2 (M=7) ✓, k=4 (M=11) ✓ |
| ³He − D | 12 | same as D − n |
| ⁴He − ³He | 15 | k=2, k=4, k=6 (M=15) ✓ |

Level k=8 needs M=19 which exceeds every pair's M_max; declared
INFEASIBLE.

---

## Numerical evidence

### Level k=2 (baseline, CONFIRMED)

| Pair | `|S_6(ζ_8)|` | `|S_7(ζ_8)|` |
|---|---|---|
| D − n | 1.60 × 10⁶ | 1.77 × 10⁻⁴⁴ |
| ³He − D | 7.43 × 10⁷ | 7.00 × 10⁻⁴³ |
| ⁴He − ³He | 1.33 × 10⁹ | 1.46 × 10⁻⁴¹ |

`(ζ_8;ζ_8)_7 = 8` exactly. All three pairs symbolically pass: Φ_8(u)
divides S_7, does not divide S_6. **3 / 3 hold ⇒ CONFIRMED.**

### Level k=4 (ζ_12, FALSIFIED)

| Pair | `|S_10(ζ_12)|` | `|S_11(ζ_12)|` | Predicted? |
|---|---|---|---|
| D − n | 2037.5 | **54.65** | Expected ≈ 0; got 54 |
| ³He − D | 2.16 × 10⁷ | **30.09** | Expected ≈ 0; got 30 |
| ⁴He − ³He | 1.20 × 10⁹ | **859.31** | Expected ≈ 0; got 860 |

`(ζ_12;ζ_12)_11 = 12` exactly (numerically and symbolically as
`8 − 4·(−1)^{2/3} + 4·(−1)^{1/3}` which simplifies to 12). Φ_12(u)
divides **neither** S_10 nor S_11 in any pair. **0 / 3 hold ⇒ FALSIFIED.**

Notably the `|S_11(ζ_12)|` values are dramatically smaller than the
preceding `|S_10(ζ_12)|`, which suggests Δa_11 contributes a partial
cancellation at ζ_12, but **far from the full cancellation predicted**.

### Level k=6 (ζ_16, FALSIFIED — feasible pairs)

| Pair | `|S_14(ζ_16)|` | `|S_15(ζ_16)|` |
|---|---|---|
| ³He − D | 89.96 | **99.33** |
| ⁴He − ³He | 7.41 × 10⁶ | **354.33** |

`(ζ_16;ζ_16)_15 = 16` exactly. Φ_16(u) divides neither S_14 nor S_15.
**0 / 2 hold ⇒ FALSIFIED.** For ³He − D, the `|S_15|` is even
slightly LARGER than `|S_14|`, indicating no cancellation tendency at
all.

### Level k=8 (INFEASIBLE)

All three pairs have M_max ≤ 15; the predicted M = 19 is unreachable
without extending the Habiro coefficient computation up to m=19+ for
⁴He (currently m=17), and recomputing ³He up through m=19+. The probe
script flags this level INFEASIBLE.

---

## Why was the level-2 case verified but the tower fails?

This is the key question. Two structural observations from the
falsification:

1. **q = ζ_4 = i has σ_i² = q + q⁻¹ = 0.** At q = ζ_4, the Hecke
   generator squares to zero — i.e. (σ_i − q)(σ_i + q⁻¹) = 0 reads
   (σ_i − i)(σ_i + i) = σ_i² + 1 = 0, but combined with the actual
   Hecke relation σ_i² = (q − q⁻¹)σ_i + 1 = (i − (−i))σ_i + 1 =
   2i σ_i + 1. Wait — let me recompute. q − q⁻¹ at q = i is
   i − (−i) = 2i, so σ_i² = 2i σ_i + 1. At q = i this is not σ² = 0;
   the special algebraic feature is elsewhere. The level-2 baseline
   reasoning needs a more careful derivation — the cancellation may
   be a Φ_8 algebraic coincidence in the specific Δa_m sequence,
   not a generic Verlinde truncation.

2. **|S_M_{k>2}(ζ_n)| are still small relative to |S_{M-1}|.** For
   k=4, the ratios are
   `|S_11|/|S_10|` ≈ 54/2037 ≈ 0.027 (D−n),
   ≈ 30/2.16e7 ≈ 1.4 × 10⁻⁶ (³He−D),
   ≈ 859/1.2e9 ≈ 7 × 10⁻⁷ (⁴He−³He).
   So Φ_n-divisibility-style suppression IS happening, just not to
   exact zero. This suggests a **softer** structural identity than
   exact cancellation — possibly an approximate Verlinde projection
   modulo higher-order terms — but the probe is testing exact
   divisibility, which is the relevant categorical statement.

3. **|S_15(ζ_16)| for ³He − D is LARGER than |S_14(ζ_16)|.** The ³He
   − D pair completely breaks the pattern at level k=6. No suppression
   at all.

The cleanest interpretation: **level-2 at ζ_8 is a structural
identity specific to that root of unity**, not the first member of a
ζ_n tower. Other plausible classifications (e.g. tied to the unique
m=8 Pochhammer boundary, or to the Φ_8² universality at M=12/15
documented in PR #1618) remain open.

---

## Implications for PR #1625

The level-2 SU(2) Wenzl identification at ζ_8 / M=7 **stands as a
narrow algebraic identity** with proven universality across the three
atomic pairs. It is **not** a fresh categorical witness in a tower
indexed by Verlinde level; the natural extrapolation fails at the
first new level.

Suggested PR #1625 framing edits:
- Soften any "tower of categorical witnesses" language in
  `prop:full-pole-structure-mass-trace` related blocks.
- Re-frame the level-2 case as "Φ_8 algebraic coincidence at q = i
  for the specific atomic-pair Δa_m sequence" rather than as "level-k
  SU(2) Wenzl prediction with k=2 baseline".
- Keep the M=7 cancellation as an empirical universality across the
  three atomic pairs (still useful for Q_β diagnostics), but do not
  claim it predicts higher-k analogues.

---

## Auxiliary observation: (ζ_n; ζ_n)_{n-1} = n integer normalization

A satellite finding: at every tested cyclotomic, the q-Pochhammer
boundary normalization is

    (ζ_n; ζ_n)_{n-1} = n  exactly (n = 8, 12, 16)

This is a clean identity (it's the classical formula
`(ζ_n; ζ_n)_{n−1} = n` for primitive n-th roots of unity — the
Pochhammer is the constant term of the cyclotomic polynomial
multiplied by `(-1)^{n-1}` factors, and reduces to n). It holds
independently of Δa_m and does NOT imply the Δa_m partial sum
vanishes. It IS however a useful diagnostic that the cyclotomic
boundary is correctly identified.

---

## Pushed commit SHA

See top of `docs/coordination/1ppq-qbeta.md` for the canonical
ledger pointer.
