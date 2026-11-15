# γγ production climbing the strand-count tower: results

Recipe: `preregistration.md`, committed (4544d19380) before the probe was written or run. Producer: `gg_ntower_probe.py`. Exact arithmetic over ℚ(q); values at the proton pin q₀ with mpmath at 60 dps. Witness: `gg-ntower.witness.json`. Issue #7727. Wall time 8422 s (≈ 2 h 20 min). Almost all of it was spent on sign analysis of the n = 9 rational functions.

Nothing is ranked or selected. Nothing is compared with Q_β, CODATA, AME or any mass. The selection rule stays open (bean `qou-99qc`).

## Checks: 5/5 pass

| check | what it confirms | result |
|---|---|---|
| C1 | The seminormal matrices satisfy the Hecke and braid relations exactly, on every two-row shape up to n = 9. | pass |
| C2 | The convention-D weights y_λ = [λ₁−λ₂+1]_q/[2]_qⁿ equal the corpus's `y_lambda_symbolic` for n = 3..6, they sum to 1, and tr σ = z_D. | pass |
| C3 | The character formula for closing a strand satisfies E(a) = a and E(aσ_m b) = z·ab, for m = 3..5. | pass |
| C4 | Shift s = 0 reproduces the same-strand table: χ_(2,1)(V³) − 2 = −h⁴(3+h²), and the survivors at q₀ for k ≤ 6 are exactly k = 3, 6. | pass |
| C5 | Shift s = +1 has the same characters as σ₀σ_k⁻¹ (the Lean telescoping identity). | pass |

## Reading 3 at every level, at q₀

Notation: s is the shift between successive collisions, and k is the number of collisions. "Fails at" lists the levels m whose two-row characters include a negative one. V = σ_iσ_{i+1}⁻¹ is the vertex used for selection. U = σ_iσ_{i+1} is the bare photon product.

| s | strands n | V: admissible k | V: fails at | U: admissible k | U: fails at |
|---|---|---|---|---|---|
| 0 | 3 | 3, 6 | k ∉ 3ℤ at level 3 | 3, 6 | k ∉ 3ℤ at level 3 |
| +1 | k + 2 | 4, 5, 6, 7 | k ≤ 3, top level only | 3, 4, 5, 6, 7 | k ≤ 2, top level only |
| −1 | k + 2 | none | every k; for k ≥ 3 at most levels | none | every k ≥ 3 at every level |
| +2 | 2k + 1 | none | every k ≥ 2 at every level | none | every k ≥ 2 at every level |
| −2 | 2k + 1 | none | every k ≥ 2 at every level | none | every k ≥ 2 at every level |
| +3 | 3k | none | every k ≥ 2 at every level | none | every k ≥ 2 at every level |

**Outcome (ii) for every placement that actually climbs.** No shift other than s = 0 and s = +1 gives an admissible element for any k up to n = 9, for either vertex. The s = +1 passes do not count as collisions. By the Lean identity, W_k^(+1) = σ₀σ_k⁻¹: two crossings at opposite ends, and whether they pass depends only on how far apart those two crossings sit.

**Outcome (iii) occurs.** For example, V with s = +1 and k = 2, 3, and V with s = −1 and k = 2, 4, 6, fail at the top level but pass once closed down to three strands. So "reading 3 at every level" is strictly stronger than testing only the closed-down element. No element passed at the top level and then failed lower down.

## The h-expansion against the same-strand table

Three collisions, closed down to 3 strands. For each character the table gives its value at q = 1 and the first power of t = q − 1 (equivalently of h) at which it moves away from that value.

| s | V: χ_(3) at q=1, order | V: χ_(2,1) at q=1, order | U: χ_(3) | U: χ_(2,1) |
|---|---|---|---|---|
| 0 (V³) | 1, never moves | 2, **h⁴** | 1, h¹ | 2, never moves |
| +1 | 1/2, h¹ | 0, h¹ | 1/2, h¹ | 0, never moves |
| −1 | 1/4, h² | **−1/4**, h² | 1/4, h¹ | **−1/4**, h¹ |
| ±2, +3 | 1/16, h² | **−1/16**, h² | 1/16, h¹ | **−1/16**, h¹ |

**Comparison: differ, for every climbing placement.** The same-strand core V³ is the identity at q = 1, and its (2,1) character first moves at h⁴. Every climbing placement moves at h¹ or h². More importantly, for s = −1, ±2 and +3 the (2,1) character is **already negative at q = 1**. So the failure of reading 3 there is a plain-permutation, order-zero fact, not a q-deformation effect. It holds on all of q > 1: numerator and denominator have no root in (1, ∞), so the (2,1) character is negative for every q > 1, for both vertices.

Shifts +2, −2 and +3 give identical closed-down values. Closing the extra strands turns each overlapping collision into a scalar times a shorter word, and those coincide.

## What this says, and what it does not

- Placing each successive γγ collision on new strands, then closing those strands by the convention-D Markov trace, does **not** give a confined three-strand element for any shift tested, up to 9 strands. This is a scope-(a) negative: it is about this construction (fixed vertex, rigid shift, top closing), not about climbing the tower in general.
- Confinement in the corpus's sense needs the three collisions to share their three strands (s = 0). That is the same-strand h-tower that already existed.
- Not tested: placements that are not a rigid shift, closing from the bottom, pair creation by Jones projections (two strands per collision), quark letters, gluons, or two nucleons. These were not pre-registered and none is adopted.
