# Categorical derivation of the rectangular-form conjecture

**Date:** 2026-05-25
**Status:** EXPLORATORY — Type-B framing PREDATES Probe (4c) FALSIFICATION; pattern (a) of the conjecture is now disproved at A=6
**Trigger:** Probes (4) and (4b) empirically supported the (A,A,A) rectangle as the unique PSD-dominant Wedderburn block; **Probe (4c) subsequently falsified this** with (3,3,3,3,2,2,2) min_eig = −116.71 beating the rectangle's −96.52 by 20 units

**⚠ Reading note (post-falsification, 2026-05-25):** This document was written to motivate the Type-B fold derivation of the (A,A,A)-rectangle dominance. **Probe (4c) FALSIFIED the rectangular-form conjecture at A=6**: three "almost-rectangular" shapes go up to 20 min_eig units deeper than the rectangle. The framework below is preserved for archival reference but the "rectangle is the symmetric crystal fixed point" prediction is empirically wrong. The right categorical question is now: *what crystal-theoretic structure does (3,3,3,3,2,2,2) realise that (6,6,6) lacks?*

## What the empirical data says

Per [`docs/audits/2026-05-25-dominant-partition-nucleon-structure.md`](2026-05-25-dominant-partition-nucleon-structure.md):

| Atom | A | dominant λ* | min_eig | scaling vs A=4 |
|---|---:|---|---:|---:|
| ⁴He | 4 | (4,4,4) | −20.017 | 1× |
| ⁴He | 4 | (3,3,3,3) | −15.51 | 0.77× (transpose pair) |
| ⁶Li | 6 | (6,6,6) | −95.72 | **4.78×** |
| ⁶Li | 6 | (3,3,3,3,3,3) | −96.52 | **4.83×** (transpose pair) |

Three empirical facts to explain:

1. **The (A,A,A) rectangle and its transpose (3,3,...,3) are both PSD-dominant** with comparable min_eig.
2. **The (A,A,A) rectangle is *uniquely* dominant** — other rectangles ((9,9), 9-row (2,...,2)) and almost-rectangles ((8,8,2), (5,5,5,3)) are less obstructive.
3. **The depth scales steeply with A** — roughly 4.8× from A=4 to A=6, much faster than the d_λ ratio (87,516 / 462 ≈ 189), suggesting it's an *intrinsic* eigenvalue scale, not a dimension artifact.

## Type-B fold framework (AGENTS.md §7b)

The Cartan datum of `sl_n` folds to Type B via the diagram involution. The folded crystal is a *symmetric crystal*:
- B(λ) for the Type-A `sl_{3A}` crystal lives over the lattice with `(3A − 1)` simple roots
- The diagram involution `i ↔ 3A − i` swaps α_i and α_{3A − i}
- A Type-A crystal element T ∈ B(λ) maps under the involution to `evac(T) ∈ B(λ^T)`
- The folded crystal is the orbit space; **fixed points = bar-invariant tableaux**

Predictions of the Type-B framework:

**(P1)** If λ ≠ λ^T, the fold pairs B(λ) and B(λ^T) into a single symmetric crystal of dim 2 · dim B(λ) (if both have the same dim, which transpose forces).

**(P2)** Fixed-point cardinality `|B(λ)^evac|` is the number of bar-self-symmetric tableaux. For (A,A,A) at n=3A, this is a known combinatorial count (related to oscillating tableaux and symmetric SYTs).

**(P3)** The eigenvalue scale of the rep at λ in `H_{3A}(q)` is governed by the Hecke Markov-trace weight on the fixed-point sub-crystal. If `|B(λ)^evac|` grows faster than `|B(λ)|^(1/2)`, the bar-anti-symmetric content concentrates obstructively.

## The (A,A,A) prediction

**Claim (conjectural):** For the (A,A,A) ⊢ 3A rectangle (the A-row form of the Schur-Weyl partner of `n=3A` strands × 3-color-per-nucleon), the Type-B fold has:

1. `dim B(A,A,A) = dim B(3,...,3) = SSYT count of an A×3 rectangle`
2. The number of fixed tableaux is `|B(A,A,A)^evac| = O(A^k)` for some `k ≥ 2` (asymptotic conjecture; needs combinatorial proof)
3. The obstruction depth in `ρ_λ(T_w)` scales as `(A × |B^evac| / dim B)^c` for some exponent `c` — explaining the steep 4.8× growth from A=4 to A=6

## What this audit DOES

- Cites the empirical pattern that demands a categorical explanation
- Frames the Type-B fold as the natural categorical machinery (per AGENTS.md §7b)
- Lists three concrete predictions (P1)–(P3) that follow from the fold structure
- Identifies what would need to be computed (bar-invariant tableau count for (4,4,4), (3,3,3,3), (6,6,6), (3,3,3,3,3,3))

## What this audit does NOT do

- Does NOT prove the conjecture — the actual Δ_(A,A,A) derivation needs Type-B fold implementation (not currently in `crystal_basis.py`)
- Does NOT compute fixed-point cardinalities (`|B(λ)^evac|`) explicitly — the existing `schuetzenberger_evacuation` is Type-A only, but a Type-A-only enumeration of bar-symmetric SSYTs is feasible as a first test
- Does NOT derive the empirical 4.8× scaling — that's the goal, contingent on bar-invariant counts

## First testable derivation (next step)

Use the existing `crystal_basis.py` to enumerate `B((4,4,4))` at `n=12` and count `|{T : evac(T) ∈ B((3,3,3,3))}|`. The Schützenberger evacuation already maps T ∈ B(λ) → evac(T) ∈ B(λ^T) (per Type-A conventions). The "bar-symmetric" content is the diagonal of the pair `(T, evac(T))`.

If `|B(A,A,A) ∪ B(3,...,3)| ≈ 2 · dim B(A,A,A)` (no symmetric collapse) **and** the obstruction min_eig is proportional to `dim · h^2 · (something specific to the A×3 shape)`, we'd have the structural explanation.

This is the next probe in the categorical-derivation thread:

  **Probe (2a) — bar-symmetric tableau counts.** Compute `|{T ∈ B(λ) : evac(T) ∈ B(λ^T)}|` for λ ∈ {(4,4,4), (6,6,6)} via the existing Type-A `schuetzenberger_evacuation`. Check the cardinality matches `dim B(λ)` (i.e., the transpose pair is fully matched by the involution) and whether the orbit count distinguishes (A,A,A) from other shapes.

## Cross-references

- [`computations/crystal_basis.py`](../../computations/crystal_basis.py) — Type-A crystal primitives (kashiwara_lower/raise, evac, demazure)
- [`docs/audits/2026-05-25-dominant-partition-nucleon-structure.md`](2026-05-25-dominant-partition-nucleon-structure.md) — empirical motivation (Probes 1, 3, 4, 4b)
- [`AGENTS.md` §7b](../../AGENTS.md) — Type-B folding for chirality / CPT directive
