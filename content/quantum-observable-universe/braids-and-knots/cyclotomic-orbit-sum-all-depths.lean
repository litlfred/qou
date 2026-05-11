/-!
# Orbit sum at all depths: parity case-split

`prop:cyclotomic-orbit-sum-all-depths` from
`cyclotomic-orbit-sum-all-depths.md`. Multiplication formula
specialised; parity of n determines whether sum vanishes or
gives a ζ(n) multiple.

Scaffolding only.
-/

import Mathlib.NumberTheory.NumberField.Basic

namespace QOU.BraidKnot.CyclotomicOrbitSumAllDepths

/-- **Theorem (`prop:cyclotomic-orbit-sum-all-depths`).**
    For every n ≥ 2 and N ≥ 2:

      sum_{k=1..N-1} Cl_n(2 π k / N)
        = (N^{1-n} - 1) ζ(n)     for n odd
        = 0                       for n even (trivially)

    where Cl_n is the Glaisher Clausen function (Re Li_n for n
    odd, Im Li_n for n even). -/
theorem orbit_sum_all_depths
    (n : ℕ) (N : ℕ) (hn : 2 ≤ n) (hN : 2 ≤ N) :
    True := by
  -- Ref: classical multiplication formula
  --   Σ_{k=1..N-1} Li_n(ζ_N^k) = (N^{1-n} - 1) ζ(n).
  -- Ref: [manuscript] §prop:cyclotomic-orbit-sum-all-depths
  --   — proof via real/imaginary part extraction by parity.
  -- Ref: [manuscript] §prop:cyclotomic-cl3-orbit-sum-general
  --   — n = 3 case.
  trivial

end QOU.BraidKnot.CyclotomicOrbitSumAllDepths
