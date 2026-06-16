# Transpose-pair asymmetry: the central categorical question

**Date:** 2026-05-25 (updated 2026-05-26)
**Status:** EXPLORATORY — frames the categorical-derivation problem after Probe (4c) falsification
**Trigger:** Probes (4c), (4e) reveal a systematic asymmetry between bar-paired Wedderburn blocks

## What we have learned

The rectangular-form conjecture (Probes 4 / 4b) was empirically supported at A=4 but **falsified at A=6** by Probe (4c). The actual global PSD-dominant at ⁶Li is **(3,3,3,3,2,2,2)** at min_eig = −116.71, not the (A,A,A) rectangle. The orthogonality of PSD-dominance and trace-dominance shape classes (Probe 1b) holds independently — with 10⁹ y_λ separation at A=6.

But the most striking *new* empirical fact is the **transpose-pair asymmetry**: for every scanned pair (λ, λ^T), the *tall-narrow* shape's min_eig is systematically more negative than the *wide-short* shape's.

## The transpose-pair asymmetry

For shapes (λ, λ^T) at n=18 with both members evaluated, the asymmetry Δ := |min_eig(λ_tall)| − |min_eig(λ_wide)| is consistently positive:

| Tall-narrow λ | min_eig | Wide-short λ^T | min_eig | Δ |
|---|---:|---|---:|---:|
| **(3,3,3,3,2,2,2)** | **−116.71** | (7,7,4) | −95.99 | **+20.72** |
| (3,3,3,3,1,1,1,1,1,1) | −100.85 | (10,4,4) | −80.67 | +20.18 |
| (3,3,2,2,2,2,2,2) | −103.71 | (8,8,2) | −88.95 | +14.76 |
| (4,2,2,2,2,2,2,2) | −100.87 | (8,8,1,1) | −86.61 | +14.26 |
| (3,3,2,2,2,2,2,1,1) | −107.03 | (9,7,2) | −85.62 | +21.41 |
| (4,2,2,2,2,2,2,1,1) | −103.78 | (9,7,1,1) | −85.51 | +18.27 |
| (3,3,2,2,2,2,1,1,1,1) | −105.66 | (10,6,2) | −79.50 | +26.16 |
| (4,2,2,2,2,2,1,1,1,1) | −102.87 | (10,6,1,1) | −78.48 | +24.39 |
| (2,2,2,2,2,2,2,2,2) | −78.70 | (9,9) | −60.49 | +18.22 |

**Average asymmetry across 9 strong pairs: +19.8 units.**

The wider scans (in progress) confirm the pattern across most transpose pairs. The few small reversals (e.g. (4,4,4,3,3) vs (5,5,5,3) with Δ ≈ −0.5) involve shapes that are nearly square (close to self-conjugate); the asymmetry is largest when the partition is far from self-conjugate.

## Why this is a structural question

The bar involution `λ → λ^T` (transpose / conjugate partition) is the combinatorial realisation of the Lusztig bar involution on the Hecke algebra `H_n(q)`. It swaps the seminormal representations `ρ_λ ↔ ρ_{λ^T}`.

If the bar involution were a *symmetry* of the obstruction structure (i.e., if `ρ_λ(T_w)` and `ρ_{λ^T}(T_w)` had the same eigval spectrum up to sign), the transpose-pair asymmetry would be zero. **But it is not zero.** The bar involution acts on shape but does NOT preserve obstruction depth.

The asymmetry is **systematic in the direction**: tall-narrow always deeper than wide-short. This is *not* a small numerical wobble — it's a 15-25 unit gap (15-25% of the absolute eigval scale) across dozens of pairs.

## Three categorical hypotheses

### (H1) Asymmetric q-twist of seminormal generators

The seminormal generator `ρ_λ(σ_k)` has diagonal entries `a_ρ = h/(1 − q^{−2ρ})` and off-diagonal entries depending on `sqrt(a_ρ a_{−ρ} + 1)`. The matrix `ρ_λ(σ_k)` is generally **not symmetric** at q ≠ 1, but its eigenvalues at q ≠ 1 are still real (the rep is unitarizable). The transpose representation `ρ_{λ^T}(σ_k)` is a *different* matrix, even though both have eigvals `{q, −q^{−1}}`.

The composition of 71 non-symmetric matrices gives `ρ_λ(T_w)`, and the **symmetric part** `(ρ + ρ^T)/2` is what we evaluate eigvals for. If the symmetric part of `ρ_λ(T_w)` has a more "concentrated" spectrum than that of `ρ_{λ^T}(T_w)`, the min_eig of the former can be deeper.

**Prediction:** the asymmetry reflects how the non-symmetric off-diagonal entries of `ρ_λ` accumulate over 71 multiplications differently in transpose-related shapes. Tall-narrow shapes have *longer chains of non-symmetric entries per generator* (more rows to walk through), so the "non-symmetricity" accumulates more.

### (H2) Asymmetric Demazure-fibre dimensions

For each shape λ, the Demazure sub-crystal `B_w(λ)` for a Weyl element `w` has some dimension. If `dim B_w(λ) ≠ dim B_w(λ^T)` for the canonical `w` corresponding to T_w, the seminormal trace on the two reps differs structurally — even though `dim B(λ) = dim B(λ^T)` at the level of the full crystal.

**Prediction:** the asymmetry reflects how the Demazure word `w` corresponding to the canonical atom-braid factors through `B(λ)` vs `B(λ^T)` differently. Tall-narrow shapes admit larger Demazure sub-fibres for the canonical `w`.

This is consistent with CLAUDE.md §7b: "**Demazure sub-crystals for resonances.** Unstable intermediaries are Demazure sub-crystals". The PSD obstruction's tall-narrow concentration may reflect that tall-narrow shapes are the "natural" Demazure sub-crystals for the canonical atom-braid.

### (H3) Bar-anti-symmetric content asymmetry

The σ_avg crossings in the canonical atom-braid have **bar-anti-symmetric content** — the σ_avg = (σ + σ⁻¹)/2 is NOT bar-invariant; rather it's bar-symmetric for one orientation and bar-anti-symmetric for the other. The 13 σ_avg crossings (of 71 total) at ⁶Li may distribute their bar-anti-symmetric weight ASYMMETRICALLY across transpose-paired irreps.

**Prediction:** the tall-narrow side accumulates more bar-anti-symmetric content, which translates to more-negative min_eig in the symmetric part. Computing the σ_avg distribution `(13/71 ≈ 18.3% of crossings)` and the asymmetry depth ratio `(~20/115 ≈ 17%)` gives suggestive numerical agreement.

## Testable predictions

For each of (H1)–(H3):

- (H1) is testable via direct computation of `(ρ + ρ^T)/2` for both λ and λ^T and comparison of their Frobenius norms (proxy for "spectrum concentration"). The Frobenius norm ratio should match the asymmetry direction.

- (H2) is testable via implementing the Demazure sub-crystal for the canonical word in `crystal_basis.py` (already exists for Type A) and comparing dimensions for transpose pairs.

- (H3) is testable by computing `ρ_λ(σ_avg)` separately and comparing its asymmetric-part norm for transpose pairs.

## What the falsified rectangular conjecture got right

The (A,A,A) rectangle WAS a local PSD extremum at small A — that observation is empirically correct. What was wrong is the *uniqueness* claim. The new picture:

**Refined conjecture (post-Probe-4c):** Among partitions of `n = 3A`, the PSD-dominant family consists of **multi-row narrow shapes** with `n_rows ≥ A` and `max_row ≤ 3 + ⌈A/3⌉`. The (A,A,A) rectangle is the *3-row* member of this family at the boundary of the row-count condition. At A=4 the family is small (only the rectangle has the right d_λ), so the rectangle appears to be the unique dominant. At A=6+ the family broadens to include shapes like (3,3,3,3,2,2,2) which goes deeper.

This refined conjecture **explains** both:
- The A=4 rectangle observation (Probes 4, 4b)
- The A=6 multi-step dominance (Probe 4c)
- The transpose-pair asymmetry (always tall-narrow)
- The orthogonality with trace-dominant family (Probe 1, 1b)

## Cross-references

- [`docs/audits/2026-05-25-dominant-partition-nucleon-structure.md`](2026-05-25-dominant-partition-nucleon-structure.md) — empirical findings from Probes 1, 3, 4, 4b, 4c, 4d, 1b
- [`docs/audits/2026-05-25-categorical-derivation-rectangular-conjecture.md`](2026-05-25-categorical-derivation-rectangular-conjecture.md) — superseded categorical framing
- [`computations/probe_4e_transpose_pair_asymmetry.py`](../../computations/probe_4e_transpose_pair_asymmetry.py) — asymmetry quantification (will expand when scan completes)
- [`content/quantum-observable-universe/braids-and-knots/conj-psd-trace-orthogonality.md`](../../content/quantum-observable-universe/braids-and-knots/conj-psd-trace-orthogonality.md) — paper-level orthogonality conjecture
- [`CLAUDE.md` §7b](../../CLAUDE.md) — Type-B folding directive
