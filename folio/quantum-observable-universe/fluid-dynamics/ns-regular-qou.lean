import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
-- Ref: [manuscript] Ch. 7, §ns-regular-qou
-- NS-regular quantum observable universe

/-- Data of a quantum observable universe as used by the NS-regularity
    classification of the sibling `.md`: the substrate parameter and the
    Euler characteristic `χ(A) = tr(κ₀)`.

    **No regularity field.** An earlier version carried `regular : chi = 0`,
    encoding the dichotomy `NS(A) = 0 ⟺ χ(A) = 0`, and a docstring saying
    NS-regularity implies global regularity of classical Navier–Stokes. Both
    are retracted (2026-10-12, owner decision): `NS(A) = κ₀|_Σ` lies in
    `H²(Σ, 𝓑) = 0` for the one-dimensional collision locus `Σ`, so it vanishes
    for every `χ(A)`, and "NS-regular" is a label for the categorical class
    only, with no consequence for classical solutions. A non-degenerate NS
    invariant is open; until one is defined there is no property to encode. -/
structure NSRegularQOU where
  /-- Substrate parameter q > 1. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The Euler characteristic `χ(A) = tr(κ₀)` of the categorical data. -/
  chi : ℤ
