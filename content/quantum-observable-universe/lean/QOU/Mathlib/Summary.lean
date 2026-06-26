import QOU.Mathlib.SpectralSequence
import QOU.Mathlib.HeckeAlgebra
import QOU.Mathlib.WenzlBridgeConcrete
import QOU.Mathlib.RSKBridge
import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.ArchimedeanRealization
import QOU.Mathlib.NonAbelianStokes
import QOU.Mathlib.PermutationEnumeration
import QOU.Mathlib.UpstreamSubstrateBridge

/-!
# QOU.Mathlib.Summary — capstone import + master discharge

Capstone file importing the full upstream `QOU.Mathlib.*`
infrastructure and providing a master discharge theorem
packaging everything into a single downstream-consumable
handle.

**Use case**: Downstream files needing the upstream
substrate-axiom layer discharged need only

  `import QOU.Mathlib.Summary`
  `open QOU.Mathlib.Summary`

and then consume `MasterUpstream.complete` to get the
aggregate result.

## File index

| File | Contents |
|---|---|
| `SpectralSequence.lean` | `E_r` page library + `CollapsesAt` + `GBFiltrationCollapsesAtE2` class + convergence + `GBSpectralConvergesToWedderburn` |
| `HeckeAlgebra.lean` | Generic `IwahoriHeckeAlgebra n q` + `MarkovTrace` + `WedderburnDecomposition` + concrete H_2/H_3 carriers + multiplication + Markov trace + Wedderburn projectors + concrete `MarkovTraceRecursionWithMul` H_1→H_2, H_2→H_3 instances + canonical_lift hook + HnCarrier ↔ H{2,3}Carrier conversions |
| `WenzlBridgeConcrete.lean` | Cohorts n=2..8 with Σd² = n! proved + dim_q closed forms + 7 hook-formula derivations + 4 substrate-q corollaries + recursive `cohortDimqValues` + `BurnsideIdentity` over `Nat.Partition` + 7 `CohortRSKWitness` instances + n=9/10 hook tables + n=9 expected SYT counts |
| `RSKBridge.lean` | `RSKBijection` class + `BurnsideFromRSK` derivation + `CohortRSKWitness` |
| `ArchimedeanRealization.lean` | `q_zero ≈ 1.10998` + positivity + `evalAtQZero` ring-hom + `ratPolyEvalAtQZero` + `ArchimedeanRealizationFunctor` class |
| `NonAbelianStokes.lean` | `NonAbelianStokes` class + `piecewiseAffineLineIntegral` + concatenation rule + `braidSurfaceMultTrace` + concrete `YekutieliFiniteSliceMultTrace` + `LieAlgebraStructure` with bilinearity + `bracket_antisym` proved + `LieAlgebraOneForm/TwoForm` + `gaugeCovariantDerivative` + `LieValuedStokes` |
| `PermutationEnumeration.lean` | `Fin n.factorial ≃ Equiv.Perm (Fin n)` + sanity at n=0..6 + `simpleTransposition` + concrete `sigma_i_in_S{3,4}` + `simpleTransposition_sq` + `coxeterLength` + `lengthFn` + 11 concrete length theorems |
| `UpstreamSubstrateBridge.lean` | 7 substrate-axiom bridges + `complete_upstream_discharge` aggregate |

## Master discharge theorem

`MasterUpstream.complete` packages all 7 substrate axioms in
one statement.  Downstream files needing any of them can pick
them out by destructuring the conjunction.
-/

namespace QOU.Mathlib.Summary

open QOU.Mathlib.SpectralSequence
open QOU.Mathlib.HeckeAlgebra
open QOU.Mathlib.WenzlBridgeConcrete
open QOU.Mathlib.RSKBridge
open QOU.Mathlib.ArchimedeanRealization
open QOU.Mathlib.NonAbelianStokes
open QOU.Mathlib.PermutationEnumeration
open QOU.Mathlib.UpstreamSubstrateBridge

/-! ### Master discharge

    Re-export `complete_upstream_discharge` under a clean name. -/

/-- **Master upstream discharge theorem** — the full substrate-
    axiom suite bundled in one statement.  Wraps
    `UpstreamSubstrateBridge.complete_upstream_discharge`. -/
theorem master_upstream_complete (R : Type u) [CommRing R]
    (q : R) (q_ℝ z : ℝ) (G : Type u) [Group G] (z_G : G) :
    (∃ S : SpectralSequence R, CollapsesAtE2 S) ∧
    (∃ W2 : WedderburnIsomorphism R 2 q, True) ∧
    (∃ W3 : WedderburnIsomorphism R 3 q, True) ∧
    (∃ M1 : MarkovTraceRecursionWithMul ℝ 1 q_ℝ z, True) ∧
    (∃ M2 : MarkovTraceRecursionWithMul ℝ 2 q_ℝ z, True) ∧
    (∃ Y : YekutieliFiniteSliceMultTrace G z_G, True) ∧
    (q_zero > 1) :=
  complete_upstream_discharge R q q_ℝ z G z_G

/-- **Sanity inventory** — confirms the 8 upstream files
    contribute interlocking content.  This theorem is a
    documentation handle: every named class / instance below
    is in scope and consumable. -/
theorem inventory_check (R : Type u) [CommRing R] (q : R) :
    -- Spectral sequence
    Nonempty (GBFiltrationCollapsesAtE2 R) ∧
    -- Hecke algebra
    Nonempty (IwahoriHeckeAlgebra R 2 q) ∧
    Nonempty (WedderburnIsomorphism R 2 q) ∧
    -- Permutation enumeration (concrete sigma)
    coxeterLength sigma1_in_S3 = 1 ∧
    coxeterLength sigma2_in_S4 = 1 :=
  ⟨⟨inferInstance⟩, ⟨inferInstance⟩, ⟨inferInstance⟩,
   coxeterLength_sigma1_in_S3, coxeterLength_sigma2_in_S4⟩

end QOU.Mathlib.Summary
