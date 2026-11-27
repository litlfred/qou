---
# qou-tcl5
title: 'Spanning theorem: Jones normal forms are a basis of TL_n(δ) over any R; then blocks + Ext¹/HH² vanishing'
status: in-progress
type: task
priority: high
tags:
    - term-completeness
    - lean
created_at: 2026-11-27T21:05:00Z
updated_at: 2026-11-27T21:50:00Z
parent: qou-tcl0
---

Owner (Carl, 2026-11-27, thread "Prove when mass and binding terms are complete"):
picked "Spanning theorem in Lean" and "A and B" (also Ext¹ / HH² vanishing), and
"we need to show we have a basis set over any R".

## State of the corpus (measured on main 58947a16b)

Proved, any commutative ring: normal forms span (`TemperleyLiebNormalFormSpanning.span_range_elt_eq_top`),
`card NormalIdx m = catalan (m+1)` (`TemperleyLiebNormalIdxCatalan`), `Σ ballot² = catalan`
(`BallotNumbers.ballot_sq_sum_catalan`), trace nondegenerate iff `[k] ≠ 0`, `3 ≤ k ≤ n+2`
(`TemperleyLiebMarkovNondegenerate.nondegenerate_iff`), Wedderburn at n = 2, 3.
OPEN, named in `TemperleyLiebNormalFormSpanning` §"What is NOT proved": linear independence
of the normal forms for general n.

## Route

1. Independence at δ = 2 over ℚ via the q = 1 spin chain `e = |s⟩⟨s|`, `s = |01⟩ − |10⟩`
   on `(ℚ²)^{⊗N}`. Measured (exact integer arithmetic, scratch probe): for N ≤ 7 the images
   of all Catalan(N) normal forms are independent, and their lexicographically least nonzero
   entries `(out, in)` are pairwise distinct with value ±1 (echelon ⇒ independent).
   The pivot words read as parenthesis words (0 = "(", 1 = ")") recover the diagram.
2. Lift to `ℤ[δ]` by the (δ − 2)-adic specialisation argument, then to any R by base change
   of the presentation (`RingQuot` of the free algebra commutes with `R ⊗ –`).
3. With every `[k]` (k ≤ n+1) a unit: Wedderburn blocks of sizes `ballot(n,k)`, and Ext¹ = 0 /
   HH² = 0. Note: trace nondegeneracy alone does NOT give semisimplicity (`K[x]/(x²)` has a
   nondegenerate trace) — use the JW projectors + the dimension count from 1–2.

## 2026-11-27 update

- Step 1 merged: #9700, `HeckeTemperleyLieb/TemperleyLiebSpinChainTwo.lean` (spinRep, TL(2) over any R).
- Owner choice (via coordinator): use the O_q(SU(2)) PBW basis (#9731,
  `CompactQuantumMetrics/OqSU2PBW.lean`, basis over any commutative R with q a unit) for
  the rank-side dimension counts. Plan: the degree-≤N part of O_q(SU(2)) has rank
  Σ_{2T≤N} (2T+1)², i.e. the matrix-coefficient count behind `multiplet_rank_count`,
  now as a basis statement over any R rather than a sum identity. The TL pivot lemma
  covers the block side.
