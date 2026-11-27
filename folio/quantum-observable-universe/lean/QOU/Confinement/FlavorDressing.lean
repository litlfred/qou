import QOU.EightfoldWay.FlavorDressingFunctor
import QOU.EightfoldWay.FlavorSplitSubstrateMass
import QOU.EightfoldWay.DressedMassFromSubstrateSplit
import QOU.EightfoldWay.FlavorMassSplittingBound
import QOU.EightfoldWay.PairProductCoefficientBound
import QOU.EightfoldWay.PivotSplitOrder

/-!
# QOU.FlavorDressing — Flavor-dressed quark mass functor

Categorical bridge from the discrete category **Flavor** of quark
flavors to the positive reals carrying dressed-quark mass values.
Derivation of the down–up splitting, conditional on
`conj:flavor-split-aether-mass` lives here; the splitting-only
substrate bound theorem is included.

## Members

- `FlavorDressingFunctor` — typeclass with `μ : Flavor → ℝ` and
  positivity.
- `FlavorSplitSubstrateMass` — Lean class of
  `conj:flavor-split-aether-mass` (no instance).
- `dressed_mass_from_substrate_split` — derivation of
  `μ_d − μ_u = M_N · substrate_split_factor q` from that class and the
  nucleon form of the pair Skein formula (an explicit hypothesis).
- `flavor_mass_splitting_bound` — two-sided substrate bound
  `0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q`.

## References

- [def:flavor-dressing-functor]
- [prop:flavor-dressed-mass-from-aether-split]
- [thm:flavor-mass-splitting-bound]
-/
