-- Quantum Observable Universe — Lean 4 Formalization
--
-- This project formalizes the mathematical content of the QOU manuscript.
-- Each chapter has a corresponding Lean file.
--
-- Status tracking:
--   - Unproved goals are marked with placeholder tactics
--   - `proof-objects.json` in the repo root tracks formalization status
--   - LeanBlueprint macros in the LaTeX source link to declarations here

-- NOTE: Fred2005 has moved to content/fred2005-formal-groups/lean/
-- import Fred2005

import QOU.Basic
import QOU.MathlibExt
import QOU.MathlibExt.MarkovTrace
import QOU.MathlibExt.QuantumDilogarithm
import QOU.MathlibExt.QuantumDilogarithmInfinite
import QOU.MathlibExt.FaddeevQuantumDilogarithm
import QOU.MathlibExt.PhiBProd
import QOU.MathlibExt.YekutieliIntegration
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
-- Per Copilot review: `QOU.MathlibExt.SDPRankEquality` is kept
-- OUT of the top-level umbrella while it still has `sorry`
-- placeholders (rank-nullity Mathlib API + Goldman-Tucker
-- categorical axiom).  Downstream code that needs the full
-- rank-equality chain can import it directly:
--   `import QOU.MathlibExt.SDPRankEquality`
-- This keeps QOU's baseline dependency surface clean for
-- consumers who only need the closed (interior + active-empty)
-- cases via `SDPRealUniqueness`.
import QOU.MathlibExt.PosSemidefTraceZero
import QOU.MathlibExt.PosSemidefDiagZero
import QOU.MathlibExt.FrobeniusInnerProduct
import QOU.MathlibExt.QPlancherel
import QOU.MathlibExt.MonoidalCalcVar
import QOU.MathlibExt.QGaussianBinomialPascal
import QOU.HeckeAlgebra
import QOU.Glossary
import QOU.Knot.FigureEightSelfDuality
import QOU.Knot.FigureEightVolume
import QOU.Knot.PerNeutronLadder
import QOU.KnotTheory
import QOU.KnotTheory.Brunnian
import QOU.KnotRegistry
import QOU.MassDerivation
import QOU.MassTheory.TraceConventionGate
import QOU.MassTheory.NeutronProtonEMSign
import QOU.MassTheory.BarParityExclusion
import QOU.MassTheory.SU4SupermultipletGate
import QOU.MassTheory.BodyOrderCumulant
import QOU.MassTheory.ReebPnMagnitude
import QOU.Mass.MassVolDensity
import QOU.Mass.BindingRecurrenceSpectral
import QOU.Mass.Lever1Depth2Exclusion
import QOU.Mass.Lever1TauClosedForm
import QOU.Mass.BindingTauAnchorClosure
import QOU.Mass.ColorCubicPowerSums
import QOU.Mass.TauQuantumIntegerForm
import QOU.Mass.ColorSpectralCubicGeometry
import QOU.Mass.HeckeStokesEigenvalues
import QOU.Mass.NaStokesKeystone
import QOU.Mass.BindingHyperbolicRecurrence
import QOU.Mass.BindingQBesselKernel
import QOU.Mass.BindingJacobiAngerBridge
import QOU.Mass.BindingQHermiteOscillator
import QOU.Mass.BindingEigenfunctionTwoTier
import QOU.Mass.QWeberInterpolation
import QOU.Mass.PaddedShapeLevelRational
import QOU.Mass.AdditiveCorrectionConfinement
import QOU.Mass.QBetaProxyHReduction
import QOU.Mass.RogersSzegoInhabited
import QOU.Mass.SelectionRuleQuantumIntegerForm
import QOU.Mass.JetFiltrationExtensive
import QOU.Mass.LinearChainBondCount
import QOU.Mass.KappaWritheAsymptote
import QOU.Mass.LinearChainBondFactorization
import QOU.Calculations
import QOU.HadronicMass
import QOU.AtomicMass
import QOU.QuantumObservableUniverse
import QOU.QuantumObservableUniverses.QAnalysis
import QOU.QuantumObservableUniverses.QIntegralTransforms
import QOU.QuantumObservableUniverses.QDifferentialGeometry
import QOU.LiftingDescent.QuantumCharacteristicClassDisplay
import QOU.ParticleInteractions.HadronDisplay
import QOU.ParticleInteractions.AtomKnot
import QOU.ParticleInteractions.WignerSU4FromSpinIsospin
import QOU.Elaboration
import QOU.PathIntegrals
import QOU.MobiusEnergy
import QOU.Torsion
import QOU.BringsSurface
import QOU.BringCone
import QOU.QuaternionicElectroweak
import QOU.ArchimedeanUniverse
import QOU.PAdicQuantumGroups
import QOU.GaugeFieldFluidDynamics
import QOU.InformationTheory
import QOU.LightningPath
import QOU.RepresentationTheory
import QOU.GradedFrobeniusHopf
import QOU.ChannelSeparation
import QOU.Archimedean
import QOU.Interactions
import QOU.Encounter
import QOU.BraidKnot
import QOU.FlavorDressing
import QOU.ArchimedeanMassFormula
import QOU.CODATAChain
import QOU.ClassicalLimitObstruction
import QOU.FeynmanPathIntegrals
import QOU.MathConstants
import QOU.PhotonThreading
import QOU.QBirchSwinnertonDyer
import QOU.QCollatz
import QOU.QGeometricLanglands
import QOU.AppendixSurreals
import QOU.AlgebraicSubstrate
import QOU.LiftingDescent
import QOU.LiftingDescent.HomologicalCondensation
import QOU.LiftingDescent.BBStratification
import QOU.MotivesArchimedean
import QOU.MassEndomorphism
import QOU.PhiQPiece
import QOU.Kashaev
import QOU.PhiQJSJ
import QOU.Infra
import QOU.Observations.AlgebraicGnsEmbedding
import QOU.Observations.QCltNonCommutative
import QOU.Observations.TraceLocalityMeetsGsNonLocality
import QOU.MathlibExt.RpowAlgebra
import QOU.Braiding.HnMarkovTrace
import QOU.Braiding.TrMHopfSigma1SqClosedForm
import QOU.Braiding.JonesMobiusDiagonal
import QOU.Braiding.HeckeGenPolyReduction
import QOU.Information.HeckeLogDecomposition
import QOU.JetHorizon
import QOU.MagicShell.DeltaCouplingSubstrateForm
-- Migrated from content-tree extract
-- (`quantum-observable-universes/categorical-dq-squared-proof.lean`).
-- See `AUDIT-REPORT.md §P3` for the open non-vanishing direction.
import QOU.CategoricalDqSquared
import QOU.frobenius_relation
import QOU.dq_squared
import QOU.emergence_to_quantum_flat
import QOU.su2_emergence_dagger_unitarity
import QOU.su2_emergence_volume_determinant
import QOU.frobenius_dagger_positive_definite
import QOU.volume_from_rigidity
import QOU.substrate_radial_coordinate
-- Symmetry-eigenspace selection rules: bar-parity (c₃ ≠ −Vol(4₁), scope-(b)) +
-- sign-positivity (Δ_λ rows B/E). Generic base ring §7c, sorry-free. Wired so
-- CI type-checks it (not an orphan).
import QOU.SelectionRules
import QOU.Braiding.non_self_intersection
-- Keystone geometric-angle fingerprint: the ℓ=1 icosahedral character on the
-- 5-fold rotation is the golden ratio (parameter-free; validates irrepToRotation).
import QOU.BraidsAndKnots.IcosahedralCharacterGoldenRatio
-- D15 Pachner–Pentagon (conj:pachner-pentagon-borromean): §3b conjecture-class
-- with sorry-free consumer theorems. Wired so CI type-checks it (not an orphan).
import QOU.BraidsAndKnots.PachnerPentagonBorromean
-- Δ_λ ℓ¹-ceiling: sign-only fixes structurally excluded (Option-E prune, PR #2925).
-- Triangle bound on the per-block binding closure; sorry-free, generic base ring.
import QOU.BraidsAndKnots.DeltaLambdaL1Ceiling
-- Borromean brane-tower convergence: the TRUE Li₂^q radius bound (|tr_M(β_Bor)|<1
-- ⇒ pair traces < q ∀q>1); sorry-free, over ℚ. Wired so CI type-checks it.
import QOU.BraidsAndKnots.BorromeanTowerConvergence
-- Trace-convention split: convention D (TL/Jones pipeline) ≠ convention C
-- (canonical Wenzl z-trace) at β_Bor, exactly; sorry-free. Wired so CI
-- type-checks it (not an orphan).
import QOU.BraidsAndKnots.BorromeanTraceConventionSplit
-- Canonical trC(β_Bor) derived from the Markov-forced values (rational
-- seminormal (2,1) rep + Cayley–Hamilton + unique weights); sorry-free.
import QOU.BraidsAndKnots.BorromeanCanonicalTraceDerivation
-- Post-τ q-Rogers pentagon: α/β substitution algebra, the log² correction
-- term, and the q≠1 analytic-continuation conjecture-class.
import QOU.BraidKnot.QRogersPentagonArchimedean
import QOU.Information.p_bandwidth_bound
import QOU.ParticleInteractions.atomic_lp_stability
import QOU.ParticleInteractions.silver_ratio_beta_decay_null
import QOU.ParticleInteractions.delta_pre_archimedean
import QOU.FluidDynamics.q_bkm_criterion
import QOU.FluidDynamics.TwoVortexChannelAlgebra
import QOU.QBeta.RationalCoeffRecurrence
import QOU.QBeta.SilverAnchorGrounding
import QOU.QBeta.ReebTowerJacobiAnger
import QOU.QBeta.QBesselContiguityRecurrence
import QOU.QBeta.QBesselBarCovariance
import QOU.QBeta.QBesselQuadraticActionTerm
import QOU.QBeta.QCasoratianAbel
import QOU.QBeta.QCasoratianBarParity
import QOU.QBeta.ZBarParity
import QOU.QBeta.QBetaZeta4ResidueRefutation
import QOU.QBeta.BarParityZeta4Swap
import QOU.QBeta.CAL3AnchorStructure
import QOU.QBeta.SRigidityPrune
import QOU.QBeta.HopfCubicOddCarrier
import QOU.QBeta.Zeta4DescentCarrier
import QOU.QBeta.H4RouteBBranchingPrune
import QOU.QBeta.QLommelOrderRecurrence
import QOU.QBeta.HoefsmitBBarParity
import QOU.QBeta.StageCSigma3LiftObligation
import QOU.QBeta.CrossingWeightAffine
import QOU.QBeta.WenzlPochhammerBoundary
-- Concrete H₃(q) Markov-trace functional (NF model: linearity, cyclicity,
-- Hecke σ₀²=hσ₀+1, Markov reduction tr(x·σ₁)=z·tr(x)); cross-checked vs
-- `gram.py` / `pyhecke.trace_formal`. Was an orphan under `Machinery/`.
import QOU.Machinery.MarkovTraceOnHecke
-- Lean schema for the 3-axis (knot, partition, atom) derived-χ catalogue
-- (Python: `derived_chi_catalogue.py`, PR #1952). Type-level cell record +
-- §3b-cond R-matrix-derivation provenance classes; 0 sorries. Was an
-- orphan under `Machinery/` (not imported ⇒ never built by CI).
import QOU.Machinery.DerivedCharacterCatalogue
import QOU.HyperellipticQuintic.zeta5_residue_monodromy

import QOU.Archimedean.BorromeanQuark
import QOU.Interactions.QIntegerMassFormula
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Molecular.PalindromicityOrbitalType
import QOU.Molecular.ShellCapacitySelfSquare
import QOU.Molecular.ShellClosureNfTermCount

import QOU.Conjectures.ShellTransitionKnot
import QOU.Conjectures.KnotFactorFrobeniusPairing
import QOU.Conjectures.WeakSpectralCompleteness
import QOU.Conjectures.MagicNumbersBring
import QOU.Conjectures.QuantumLanglandsDual

-- Identity-I / RSK infrastructure (verified library files; wired in for CI build coverage).
import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.SchenstedInsertion
import QOU.Mathlib.SYTEnumeration
import QOU.Mathlib.SYTEnumerationBridge
import QOU.Mathlib.SYTEnumerationFintype
import QOU.Mathlib.SYTHookFormula
import QOU.Mathlib.SYTHookFormulaBeta
import QOU.Mathlib.SYTHookFormulaBetaProd
import QOU.Mathlib.SYTHookFormulaRows
