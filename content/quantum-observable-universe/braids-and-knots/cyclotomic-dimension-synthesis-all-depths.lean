/-!
# Dimension synthesis at all depths and primes

`prop:cyclotomic-dimension-synthesis-all-depths` from
`cyclotomic-dimension-synthesis-all-depths.md`. Parity-dependent
dimension formula.

Scaffolding only.
-/

import Mathlib.NumberTheory.NumberField.Basic

namespace QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths

/-- Predicted dimension: parity-dependent.
    n odd:  (K - 3) / 2
    n even: (K - 1) / 2 -/
def predictedDim (n : ℕ) (K : ℕ) : ℕ :=
  if n % 2 = 1 then (K - 3) / 2 else (K - 1) / 2

/-- **Theorem (`prop:cyclotomic-dimension-synthesis-all-depths`).**
    Upper bound (unconditional):

      dim_ℚ V_{n, K} ≤
        (K - 3) / 2  if n odd, prime K ≥ 5
        (K - 1) / 2  if n even, prime K ≥ 3

    Lower bound: unconditional theorem at n = 2 via Bloch-Suslin
    (`prop:depth-2-identification-bloch-suslin`); Beilinson-
    conditional at n ≥ 3. -/
theorem dimension_synthesis_all_depths
    (n : ℕ) (K : ℕ) (hn : 2 ≤ n) (hK : 3 ≤ K) (hK_prime : Nat.Prime K) :
    True := by
  -- Ref: [manuscript] §prop:jonquiere-cyclotomic-tate-rationality
  --   (Theorem E): Tate part collapses.
  -- Ref: [manuscript] §prop:cyclotomic-orbit-sum-all-depths
  --   (Theorem F): orbit-sum reduction with parity case-split.
  -- Ref: [manuscript] §prop:borel-partial-resolution
  --   — Borel rank for cyclotomic Q(ζ_K).
  -- Ref: [manuscript] §prop:cyclotomic-depth3-dimension-synthesis
  --   — n = 3 case (PR #635 round 4).
  -- Ref: [manuscript] §prop:depth-2-identification-bloch-suslin
  --   — n = 2 unconditional via Bloch-Suslin.
  -- Ref: Beilinson conjecture (conditional for n ≥ 3 lower bound).
  trivial

end QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths
