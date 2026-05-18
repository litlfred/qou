/-!
# QOU.FlavorDressing.flavor_mass_splitting_bound

Two-sided substrate bound on the down–up dressed-quark splitting:

```
0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q
```

with ℏ_q = (q − 1)/q, h_q = q − q⁻¹, [2]_q = q + q⁻¹.

The lower bound is positivity; the upper bound follows from the
algebraic identity

```
(q − 1)²(1 − q⁻⁴)/3 = (1/3) · ℏ_q² · h_q · [2]_q
```

at non-zero `q` (no spurious `q²` factor — see direct expansion
in the lemma `substrate_to_bound_ratio` below).

LaTeX: `\label{thm:flavor-mass-splitting-bound}`
-/

import QOU.Basic
import QOU.FlavorDressing.FlavorDressingFunctor
import QOU.FlavorDressing.DressedMassFromSubstrateSplit

namespace QOU.FlavorDressing

open Flavor

/-- The substrate ratio `(q − 1)²(1 − q⁻⁴)/3` over the bound
    factor `ℏ_q² · h_q · [2]_q` equals exactly `1/3` for any
    non-zero `q`.  This algebraic identity is the engine of the
    upper bound; stated over a generic `Field R` per the
    repository's base-ring convention (CLAUDE.md §7c) — the
    identity is a rational-function fact with no archimedean
    content.  The downstream inequality `flavor_mass_splitting_bound`
    keeps its `ℝ` specialisation because it uses ordering. -/
-- Ref: [manuscript] braids-and-knots/flavor-mass-splitting-bound
theorem substrate_to_bound_ratio {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq4 : q^4 ≠ 1) :
    ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3)
    / (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹))
      = 1 / 3 := by
  -- The identity holds because both numerator and denominator
  -- share the factor (q − 1)² (q⁴ − 1)/q⁴, and their ratio is
  -- the constant 1/3.  Full proof deferred: requires
  -- `field_simp` + `ring` with hypotheses on q ≠ 0 and q⁴ ≠ 1.
  -- Ref: [manuscript] braids-and-knots/flavor-mass-splitting-bound
  --      § "Proof sketch" — upper-bound algebra.
  sorry

/-- **Substrate bound on the dressed-quark splitting.**
    For substrate parameter `q > 1`, nucleon average mass `M_N > 0`,
    and any `FlavorDressingFunctor F` satisfying the derivation
    identity of `prop:flavor-dressed-mass-from-substrate-split`,
    the down–up splitting satisfies the two-sided substrate bound

      0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q

    where ℏ_q = (q − 1)/q, h_q = q − q⁻¹, [2]_q = q + q⁻¹.

    The strict lower bound expresses positivity of the substrate
    factor at q > 1; the strict upper bound uses the algebraic
    identity `substrate_to_bound_ratio` plus the Skein-side
    adjustment factor `(q^{1/2}+q⁻^{1/2})/(q+q⁻¹) < 1` at q > 1.

    **Conditional content:** the realised value of `μ_d − μ_u`
    sits at about 1/3 of the upper bound at q = q₀; the theorem
    does NOT claim tightness.  Tightness would require a finer
    substrate factor incorporating the Skein adjustment
    explicitly. -/
-- Ref: [manuscript] braids-and-knots/flavor-mass-splitting-bound
theorem flavor_mass_splitting_bound
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    (hM : 0 < M_N) (hq : 1 < q)
    (h_derive :
      F.μ Flavor.down - F.μ Flavor.up
        = M_N * substrate_split_factor q) :
    0 < F.μ Flavor.down - F.μ Flavor.up ∧
    F.μ Flavor.down - F.μ Flavor.up
      < M_N * (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹)) := by
  -- The positivity half is a positivity argument on the substrate
  -- factor (and the Skein-adjustment factor √q + 1/√q is positive
  -- at q > 0); the upper half follows from `substrate_to_bound_ratio`
  -- (factor of 1/3 between the substrate factor and the bound
  -- factor at non-zero q) plus the Skein-side factor
  -- (√q + 1/√q)/(q + q⁻¹) < 1 at q > 1, yielding a *strict* bound.
  -- The derivation hypothesis now uses `substrate_split_factor`
  -- from the sibling file so the bound is consistent with the
  -- physical splitting in `flavor-dressed-mass-from-substrate-split.lean`
  -- per Gemini #696 medium feedback.
  -- Full proof deferred pending the supporting lemma above.
  -- Ref: [manuscript] braids-and-knots/flavor-mass-splitting-bound
  --      § "Proof sketch".
  sorry

end QOU.FlavorDressing
