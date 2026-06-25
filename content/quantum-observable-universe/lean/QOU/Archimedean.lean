import QOU.Archimedean.GroundRing
import QOU.Archimedean.TorusKnot
import QOU.Archimedean.TransferMatrix
import QOU.Archimedean.BetaDecay
import QOU.Archimedean.AxialCoupling
import QOU.Archimedean.OrderingIndependence
import QOU.Archimedean.OptimalNF
import QOU.Archimedean.TMCorrespondence
import QOU.Archimedean.MassGapGm
import QOU.Archimedean.YoungIdempotent
import QOU.Archimedean.MultiGeneratorSpectrum
import QOU.Archimedean.HeckeRep
import QOU.Archimedean.HeckeH3
import QOU.Archimedean.QuotientIdeal
import QOU.Archimedean.NuclearNormalForms
import QOU.Archimedean.HyperbolicVolumeTranscendence
import QOU.Archimedean.PauliWitness
import QOU.Archimedean.SnapPyAxioms
-- Migrated from content-tree extracts (I12 cluster B Lake migrate).
-- NOTE: `NuclearGroebnerReduction` is currently typed over `ℝ`,
-- violating this module's stated `R_q = ℤ[q,q⁻¹]` invariant; refactor
-- to the generic ground ring is open work (see the file's authoring
-- note).
import QOU.Archimedean.NuclearGroebnerReduction
import QOU.Archimedean.WeierstrassProjection
import QOU.Archimedean.metallic_character_knot
import QOU.Archimedean.archimedean
import QOU.Archimedean.noble_gas_characterization
import QOU.Archimedean.BlochWignerUnitCircle
-- Sibling-import cluster wire-in (2026-06-01): content-tree extracts
-- migrated into the Lake build (see
-- docs/audits/2026-06-01-sibling-import-cluster-wire-in-plan.md).
-- COMPILE-PENDING — these files have never been in the build.
import QOU.Archimedean.ClausenFunctionMathlibFiller
import QOU.Archimedean.BlochWignerMathlibFiller
import QOU.Archimedean.TorusKnotGenusFourUnique
import QOU.Archimedean.ForceCarrierBringUniqueness
import QOU.Archimedean.EmCouplingProjection
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.EmSpectralCompleteness
import QOU.Archimedean.MassTowerOpenProblemsClasses
import QOU.Archimedean.ThreeSubstantiveMathlibFillers
import QOU.Archimedean.DilogarithmArchimedeanLimit
import QOU.Archimedean.TypeBFoldedCrystalCombinatorics
import QOU.Archimedean.HyperbolicVolumeIndependence
import QOU.Archimedean.JetOrderIndependence

/-!
# Descartes Universe — Module Index

Re-exports all Descartes universe formalization modules.

**Note to reader**: all Lean proofs in this module work exclusively
over `ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).  Numerical
evaluations at the substrate parameter `q₀ ≈ 1.1098` appear only
in Chapter 7 (Physical Observations) and are NOT part of the
formal proof chain.

## Forward derivation chain

```
GroundRing          ℤ[q,q⁻¹], [n]_q, ℏ_q
  → TorusKnot       τ(r,s), embeddability, 6 knots on Σ₄
  → TransferMatrix   T(𝔴⁺,𝔴⁰), inductive chain, P(q)
  → BetaDecay        T_{β-decay}, F(τ,N), spectral decomposition
  → AxialCoupling    g_A from 3-fold Borromean color average
  → YoungIdempotent  e_{(n)}, Poincaré polynomial, sym/alt eigenvalues
  → OrderingIndep    Q_sym is ordering-independent (Young symmetrizer)
  → MassGapGm        Mass gap over 𝔾_m, torsion obstruction, q-NS bridge
  → MultiGenSpectrum 6×6 product, independent channel evolution
```
-/
