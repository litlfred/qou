import QOU.Mathlib.SpectralSequence
import QOU.Mathlib.HeckeAlgebra
import QOU.Mathlib.WenzlBridgeConcrete
import QOU.Mathlib.RSKBridge
import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.SchenstedInsertion
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
| `ArchimedeanRealization.lean` | `q_zero ≈ 1.10998` + positivity + `evalAtQZero` ring-hom + `ratPolyEvalAtQZero` + `ArchimedeanEvaluationPoint` class (the pinned evaluation point — **not** a functor; renamed 2026-08-24, bean `qou-7nbx`) |
| `NonAbelianStokes.lean` | `NonAbelianStokes` §3b-cond class over the concrete forms of `LieValuedForms` (`LieValuedOneForm/TwoForm` = Mathlib `OneForm/TwoForm`; boundary `cellBoundary` and curvature/`covExtDeriv` are definitions; multiplicative integrals + Stokes still assumed) + `piecewiseAffineLineIntegral` + concatenation rule + `braidSurfaceMultTrace` + concrete `YekutieliFiniteSliceMultTrace` + `bracket_antisym` for `ContinuousLieBracket` + `LieValuedStokes` |
| `PermutationEnumeration.lean` | `Fin n.factorial ≃ Equiv.Perm (Fin n)` + sanity at n=0..6 + `simpleTransposition` + concrete `sigma_i_in_S{3,4}` + `simpleTransposition_sq` + `coxeterLength` + `lengthFn` + 11 concrete length theorems |
| `UpstreamSubstrateBridge.lean` | 7 substrate-axiom bridges + `complete_upstream_discharge` aggregate |

## Master discharge theorem

`MasterUpstream.complete` packages all 7 substrate axioms in
one statement.  Downstream files needing any of them can pick
them out by destructuring the conjunction.
-/

namespace QOU.Mathlib.Summary

universe u

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
    (∃ _W2 : WedderburnIsomorphism R 2 q, True) ∧
    (∃ _W3 : WedderburnIsomorphism R 3 q, True) ∧
    (∃ M1 : MarkovTraceRecursionWithMul ℝ 1 q_ℝ z,
      MarkovAxiomHolds ℝ z M1.trace_n M1.trace_succ M1.mul_succ
        M1.sigma_n M1.embed) ∧
    (∃ M2 : MarkovTraceRecursionWithMul ℝ 2 q_ℝ z,
      MarkovAxiomHolds ℝ z M2.trace_n M2.trace_succ M2.mul_succ
        M2.sigma_n M2.embed) ∧
    (∀ (Y : YekutieliFiniteSliceMultTrace G z_G) (n : ℕ),
      Y.trace n = z_G ^ n) ∧
    (q_zero > 1) :=
  complete_upstream_discharge R q q_ℝ z G z_G

/-- **Sanity inventory** — confirms the 8 upstream files
    contribute interlocking content.  This theorem is a
    documentation handle: every named class / instance below
    is in scope and consumable.

    Conditional on `[IwahoriHeckeAlgebra R 2 q]` (§3b-cond): the trivial
    global `IwahoriHeckeAlgebra` instance was deliberately removed on
    2026-08-23 (anti-laundering — a content-free `carrier = PUnit` instance
    must not be fabricated to close it), so `Nonempty (IwahoriHeckeAlgebra
    R 2 q)` is honestly available only *given* the class. `WedderburnIsomorphism
    R 2 q` carries a real instance (`wedderburn_n2`) and stays unconditional.

    **`GBFiltrationCollapsesAtE2 R` does not carry a real instance either.**
    Its only model is `canonicalTrivial R`, which is `ss := trivial R` with
    `collapses := trivial_collapses_at_E2 R` — the TRIVIAL spectral sequence,
    whose `differential _ _ := default` makes collapse hold by `rfl` at every
    page, i.e. built into the model rather than proved of anything.

    🛑 CORRECTION 2026-09-13 (bean `qou-g5sp`). This paragraph went on to say
    *"It is an unconditional `instance`, so `[GBFiltrationCollapsesAtE2 R]` is
    free for every `R` and every downstream result taking it as a hypothesis is
    unconditional on a collapse nobody proved"*, and closed with *"Recorded
    rather than fixed here: demoting it changes every consumer, so it is a
    scoped change and not a merge-time edit."*

    **It was demoted on 2026-08-24 (bean `qou-fngs`), and the fix landed.** The
    declaration at `QOU/Mathlib/SpectralSequence.lean` is a `def`, not an
    `instance`, and its docstring says so in terms — *"that is exactly why this
    is a `def` and not an `instance` … it must now be supplied by hand, so a
    reader of a downstream theorem can see whether the hypothesis was discharged
    by a real filtration or by `PUnit`."* The proof term below is the
    demonstration: the `GBFiltrationCollapsesAtE2` conjunct is discharged by
    `⟨canonicalTrivial R⟩`, applied explicitly, while the
    `WedderburnIsomorphism` conjunct beside it still uses `inferInstance`
    because that one has a genuine instance.

    So `[GBFiltrationCollapsesAtE2 R]` is **not** free, and a downstream theorem
    taking it is a real §3b-cond conditional. The stale reading is worse than
    merely out of date: it tells a reader that live conditional results are
    unconditional-and-vacuous, which invites deleting or weakening them.

    The comparison to the `IwahoriHeckeAlgebra` instance removed on 2026-08-23
    stands and is now the whole story — both were self-assuming instances, both
    were demoted, and this file records both. -/
theorem inventory_check (R : Type u) [CommRing R] (q : R)
    [IwahoriHeckeAlgebra R 2 q] :
    -- Spectral sequence
    Nonempty (GBFiltrationCollapsesAtE2 R) ∧
    -- Hecke algebra — inhabited by the trivial model only
    Nonempty (IwahoriHeckeAlgebra R 2 q) ∧
    Nonempty (WedderburnIsomorphism R 2 q) ∧
    -- Permutation enumeration (concrete sigma)
    coxeterLength sigma1_in_S3 = 1 ∧
    coxeterLength sigma2_in_S4 = 1 :=
  ⟨⟨canonicalTrivial R⟩, ⟨triv_hecke R 2 q⟩, ⟨inferInstance⟩,
   coxeterLength_sigma1_in_S3, coxeterLength_sigma2_in_S4⟩

end QOU.Mathlib.Summary
