import QOU.Descartes.GroundRing
import QOU.Descartes.TorusKnot
import QOU.Descartes.TransferMatrix
import QOU.Descartes.BetaDecay
import QOU.Descartes.AxialCoupling
import QOU.Descartes.OrderingIndependence
import QOU.Descartes.OptimalNF
import QOU.Descartes.TMCorrespondence
import QOU.Descartes.MassGapGm
import QOU.Descartes.YoungIdempotent
import QOU.Descartes.MultiGeneratorSpectrum
import QOU.Descartes.HeckeRep
import QOU.Descartes.HeckeH3
import QOU.Descartes.QuotientIdeal
import QOU.Descartes.NuclearNormalForms
import QOU.Descartes.HyperbolicVolumeTranscendence
import QOU.Descartes.PauliWitness

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
