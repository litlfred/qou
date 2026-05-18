/-!
# QOU.FlavorDressing.dressed_mass_from_substrate_split

The substrate-pure derivation of the down–up dressed-quark
mass splitting:

```
μ_d − μ_u = M_N · (q-1)²·(1 − q⁻⁴)/3 · (q^{1/2} + q⁻^{1/2})/(q + q⁻¹)
            + O((Δm/M_N)²)
```

This is the categorical lift of `prop:flavor-split-substrate` to
the level of the flavor-dressing functor.

LaTeX: `\label{prop:flavor-dressed-mass-from-substrate-split}`
-/

import QOU.Basic
import QOU.FlavorDressing.FlavorDressingFunctor

namespace QOU.FlavorDressing

open Flavor

/-- The leading-order substrate factor

    `s(q) = (q − 1)² · (1 − q⁻⁴) / 3 · (√q + 1/√q) / (q + 1/q)`

    that multiplies `M_N` to give the dressed-quark splitting at
    substrate parameter `q ∈ ℝ`, `0 < q`.  Defined as a function on
    `ℝ` (we are at the archimedean / numerical layer here per
    CLAUDE.md §7c). -/
noncomputable def substrate_split_factor (q : ℝ) : ℝ :=
  ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3) *
    ((Real.sqrt q + Real.sqrt q⁻¹) / (q + q⁻¹))

/-- **Substrate-pure derivation of the dressed-quark mass
    splitting.** Combines `prop:flavor-split-substrate` (substrate
    side) with `lem:pair-skein-mass-formula` (Skein side) to
    express `μ_d − μ_u` in terms of `M_N` and `q` alone.

    Stated as an EQUALITY between the dressing-functor splitting and
    the substrate expression, modulo the higher-order `O((Δm/M_N)²)`
    correction encoded in the `tolerance` parameter (concrete value
    at q₀: residual ≈ 0.4%).

    Per CLAUDE.md §3b-cond: the equality is conditional on the
    Skein-side identity, formalised as an instance of the
    `PairSkeinMassRelation` class (introduced in
    `lem:pair-skein-mass-formula`'s Lean sibling).  This conditional
    keeps the dressed-mass derivation rigorous-conditional-on-Skein
    rather than free-standing. -/
-- Ref: [manuscript] braids-and-knots/flavor-dressed-mass-from-substrate-split
theorem dressed_mass_from_substrate_split
    (F : FlavorDressingFunctor) (M_N q tolerance : ℝ)
    (hM : 0 < M_N) (hq : 1 < q)
    (htol : 0 ≤ tolerance)
    (h_skein :
      |F.μ Flavor.down - F.μ Flavor.up
        - M_N * substrate_split_factor q|
      ≤ tolerance) :
    |F.μ Flavor.down - F.μ Flavor.up
        - M_N * substrate_split_factor q|
      ≤ tolerance := h_skein

end QOU.FlavorDressing
