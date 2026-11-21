import QOU.FlavorDressing.FlavorDressingFunctor
import QOU.FlavorDressing.DressedMassFromSubstrateSplit
import QOU.FlavorDressing.FlavorMassSplittingBound
import QOU.FlavorDressing.PairProductCoefficientBound
import QOU.FlavorDressing.PivotSplitOrder

/-!
# QOU.FlavorDressing — Flavor-dressed quark mass functor

Categorical bridge from the discrete category **Flavor** of quark
flavors to the positive reals carrying dressed-quark mass values.
Substrate-pure derivation of the down–up splitting from
`prop:flavor-split-substrate` lives here; the splitting-only
substrate bound theorem is included.

## Members

- `FlavorDressingFunctor` — typeclass with `μ : Flavor → ℝ` and
  positivity.
- `dressed_mass_from_substrate_split` — closed-form derivation of
  `μ_d − μ_u = M_N · substrate_split_factor q`, conditional on the
  axiomatised Skein-side closed form.
- `flavor_mass_splitting_bound` — two-sided substrate bound
  `0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q`.

## References

- [def:flavor-dressing-functor]
- [prop:flavor-dressed-mass-from-substrate-split]
- [thm:flavor-mass-splitting-bound]
-/
