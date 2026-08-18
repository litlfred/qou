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
import QOU.MathlibExt.QuadraticIrrationalBadlyApproximable
import QOU.MathlibExt.MarkovTrace
import QOU.MathlibExt.QuantumDilogarithm
import QOU.MathlibExt.QuantumDilogarithmInfinite
import QOU.MathlibExt.FaddeevQuantumDilogarithm
import QOU.MathlibExt.FaddeevPhiBRealIntegral
import QOU.MathlibExt.PhiBProd
import QOU.MathlibExt.PhiBFibreExtension
import QOU.MathlibExt.YekutieliIntegration
import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPEmptyConstraints
import QOU.MathlibExt.SDPRealUniqueness
-- The complex dilogarithm and its analytic continuation off the unit disc.
-- `ComplexDilogarithm` was ORPHANED from this root — `lake build` compiles only
-- `QOU.lean`'s import closure, so a module nothing imports is never checked at
-- all (bean qou-orph). Wiring the chain here puts every theorem below under CI.
import QOU.MathlibExt.ComplexDilogarithm
import QOU.MathlibExt.ComplexDilogarithmSlit
import QOU.MathlibExt.ComplexDilogarithmDeriv
import QOU.MathlibExt.ComplexDilogarithmUnique
import QOU.MathlibExt.ComplexDilogarithmLanden
import QOU.MathlibExt.AlternatingZetaTwo
import QOU.MathlibExt.ComplexDilogarithmBoundary
import QOU.MathlibExt.ComplexDilogarithmOnCut
import QOU.MathlibExt.ComplexDilogarithmInversion
import QOU.MathlibExt.ComplexRogersDilog
-- Scalar implicit function theorem, and two one-variable transport lemmas
-- (a constant pinned off a single point; an integer branch index pinned by a
-- window). All Mathlib gaps; all sorry-free.
import QOU.MathlibExt.ImplicitScalar
import QOU.Archimedean.ConstantOffOnePoint
import QOU.Archimedean.BranchIntegerPinning
-- Weierstrass primary-factor estimate ‖1 - E_p(z)‖ ≤ ‖z‖^{p+1}: the Mathlib-gap
-- infrastructure that closes PI-2 of QOU.Mathlib.HadamardFactorization.
-- Sorry-free, so it is wired here for CI type-checking (unlike
-- HadamardFactorization itself, which still carries PI-3 / the full theorem).
import QOU.Mathlib.WeierstrassFactorEstimate
import QOU.Mathlib.YoungDiagramCard
-- Algebraic skeleton of the Dimofte-Garoufalidis 1-loop invariant: the shape
-- identity ζ+ζ'+ζ''=0, the CUSP-NUMBER-FREE degeneracy of the edge rows, the
-- lattice-basis determinant lemmas, and the proof that the per-cusp factor
-- 2^{(c-1)/2} cancels identically.  Sorry-free, so wired here for CI.
import QOU.OneLoopEdgeLattice
import QOU.OneLoopPrefactorInvariance
-- Borel-Carathéodory inequality: a one-sided bound on Re f gives a two-sided
-- bound on ‖f‖. A genuine Mathlib v4.24.0 gap and a PI-5 prerequisite for
-- QOU.Mathlib.HadamardFactorization. Sorry-free, so wired here for CI.
import QOU.Mathlib.BorelCaratheodory
-- Scoping check for the Hadamard chain: phiBProd is a RATIO whose denominator
-- factor vanishes at an explicit point for every b /= 0, so it is not entire and
-- IsEntireOfOrderLE cannot be assumed for it. Sorry-free.
import QOU.Mathlib.HadamardApplicability
-- Faddeev rigidity: the ratio of two FaddeevPhi solutions is ib- and i/b-periodic
-- (the prefactor cancels), and given an entire ratio that extends from the dense
-- complement of the prefactor zeros to everywhere. Collapses the open input
-- `hibinv` (qou-rp5f) into `hratio` (qou-cons). Sorry-free.
import QOU.Mathlib.FaddeevRatioPeriodic
-- The FaddeevPhi class has NO regularity field, so its solution set absorbs any
-- doubly-periodic factor (lattice indicator included). Hence `hratio` (qou-cons)
-- is not derivable from the class — it is a fact about the analytic Phi_b.
import QOU.Mathlib.FaddeevSolutionSet
-- The hratio "reduction" is circular: given double periodicity, "ratio entire"
-- and "ratio constant" are the same statement. So qou-cons is not a sub-problem
-- of uniqueUpToScalar — it IS uniqueUpToScalar. Sorry-free.
import QOU.Mathlib.RigidityReductionScope
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
import QOU.MathlibExt.CauchyBinet
import QOU.MathlibExt.RankMinor
import QOU.MathlibExt.GramNondegenerate
import QOU.MathlibExt.GroupAlgebraCenter
import QOU.MathlibExt.RepresentationCharacter
import QOU.MathlibExt.QPlancherel
import QOU.MathlibExt.MonoidalCalcVar
import QOU.MathlibExt.QGaussianBinomialPascal
import QOU.MathlibExt.DerivationRankNullity
import QOU.MathlibExt.OctonionDerivations
import QOU.MathlibExt.OctonionDerivationsBound
import QOU.MathlibExt.OctonionDerivationsUpperBound
import QOU.MathlibExt.OctonionDerivationProperties
import QOU.MathlibExt.OctonionSU3RankSix
import QOU.MathlibExt.OctonionSU3Stabilizer
import QOU.MathlibExt.OctonionSU3BracketClosure
import QOU.MathlibExt.OctonionColourActionBaseModule
import QOU.MathlibExt.OctonionComplexStructure
import QOU.StandardModel.ColourStabilizerAction
import QOU.StandardModel.ThetaQcdFramingCp
import QOU.StandardModel.SecondCrossingInvariant
-- Information content of the eightfold-way hypercharge battery: the RH half
-- is entailed by Q (GMN at I3=0 pins Y uniquely, so it discriminates nothing);
-- the LH half is exactly B - L. Reduces the open Y item to one condition.
import QOU.StandardModel.HyperchargeBatteryReduction
-- Lepton number cannot be a Z-grading by smoothing count: the skein relation
-- is inhomogeneous, so imposing the grading annihilates every smoothing and
-- would make L identically 0. Scope-(b); the repair is a FILTRATION
-- (QOU/KnotTheory/Vassiliev), untested. bean qou-kl39
import QOU.StandardModel.LeptonNumberGradingObstruction
-- Stronger: NO function of the unframed knot type reproduces the corpus L
-- table. The unknot is amphichiral, so the nu / nubar rows assign +1 and -1
-- to the SAME knot. The carrier must be chiral, or L must see framing.
import QOU.StandardModel.LeptonNumberCarrierChirality
-- The p/n same-Y test falsifies only an INJECTIVE writhe->Y map, not every
-- function of the writhe (Y = w^2/4 reproduces both rows). Independence needs
-- the converse pattern: equal writhe, different Y.
import QOU.StandardModel.WritheIndependenceCriterion
-- Chiral-fermion braid words from the chi=-6 torus-knot constraint: T(2,n) is the
-- closure of sigma_1^n. L = sign(writhe) matches all 6 corpus rows; the mirror
-- moves every carrier (discharging the chirality obstruction); and the derived
-- writhe-0 pair (baryon vs gluon unit) shows Y = B - L does not factor through w.
import QOU.StandardModel.ChiralFermionBraidWords
-- The strand-twist hypercharge battery reduces to the single equation T = 3Q:
-- the nucleon check is entailed by charge additivity (and states one condition
-- twice), and the '4 of 10,000 survivors' is 1x2x2x1 multiset counting.
import QOU.StandardModel.TwistBatteryVacuity
-- q-difference operator calculus (missing Mathlib infra for the q-difference D-module
-- program): q-Leibniz product rule (clean), monomial q-chain rule (q→q^m), and the
-- composition obstruction (no naive q-chain rule for non-monomial inner functions).
import QOU.MathlibExt.QDifferenceOperator
-- q-character algebra e_{q,c} (Birkhoff-matrix building block, W2): q-characters multiply,
-- and the ratio of two with the same multiplier is q-invariant (elliptic) — the reason the
-- connection matrix is theta-valued.
import QOU.MathlibExt.QCharacter
-- q-Borel theta kernel t_n = q^{C(n,2)} (W2 ∞-Stokes building block): the RSZ q-Borel
-- transform kernel resolving an integral-slope singularity; recurrence t_{n+1}=q^n·t_n.
import QOU.MathlibExt.QBorelKernel
-- [2]_q-adic valuation on the Laurent ring ℤ[q^{±1}] (Mathlib-gap fill, qou-4atn):
-- extends QCollatz.qTwoValuation (Polynomial-only) to the Skein module where the
-- q-Collatz fundamental cycle lives; cycle values v(q⁻¹)=0, v(1+q⁻¹)=1.
import QOU.MathlibExt.LaurentTwoValuation
-- q-Collatz corroboration (qou-4atn): v_[2] strictly descends at the fundamental
-- cycle (non-attractor 1+q⁻¹ → attractor q⁻¹, v drops 1→0) — a live D∞ descent
-- candidate on every D∞ element checked, given the out-of-cone counterexample.
import QOU.AppendixSurreals.collatz_vtwo_cycle_descent
import QOU.HeckeAlgebra
import QOU.Glossary
import QOU.Knot.CuspShapeBarParity
import QOU.Knot.FigureEightDeformedMeridianWinding
import QOU.Knot.RademacherReversible
import QOU.Knot.M004AngleStructure
import QOU.Knot.L6a4AngleStructure
import QOU.Knot.FigureEightSelfDuality
import QOU.Knot.FigureEightVolume
import QOU.Knot.FigureEightVolumeLiterature
import QOU.Knot.NeumannZagierParity
import QOU.Knot.FigureEightQuarticCoefficient
import QOU.Knot.PerNeutronLadder
import QOU.MathlibExt.IdealTriangulation
import QOU.Knot.FiveTwoVolumeConstant
import QOU.Knot.FigureEightTriangulation
import QOU.Knot.AngleStructureUniqueness
import QOU.Knot.IdealTetLawOfSines
import QOU.Knot.KummerDilogHalf
import QOU.Knot.KummerRadial
import QOU.Knot.KummerUnitCircle
import QOU.Knot.RivinConcavity
import QOU.Knot.SymmetricOptimum
import QOU.Knot.WhiteheadVolumeConjecture
import QOU.Knot.KashaevProdEndpoint
import QOU.Knot.KashaevReflectionTrapezoid
import QOU.Knot.KashaevEndpointSplit
import QOU.Knot.LogSincNearZero
import QOU.Knot.LobNearZero
import QOU.Knot.KashaevAsymptotic
import QOU.Knot.KashaevArgmax
import QOU.Knot.LobTaylorSaddle
import QOU.Knot.KashaevTailBound
import QOU.Knot.KashaevPeakValue
import QOU.Knot.KashaevLogAsymptotic
import QOU.Knot.KashaevRatioExpansion
import QOU.Knot.KashaevWindowSum
import QOU.Knot.KashaevWindowIndex
import QOU.Knot.KashaevWindowAssembly
import QOU.Knot.KashaevSaddleWindow
import QOU.Knot.KashaevBeyondWindow
import QOU.Knot.KashaevFullSum
import QOU.Knot.KashaevAsymptoticBounds
import QOU.Knot.KashaevCSigma
import QOU.Knot.WhiteheadSaddleClausen
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
import QOU.MassTheory.ReebLinkingCWF
import QOU.MassTheory.SaturationRhoCap
import QOU.MassTheory.IsospinMirrorInvariance
import QOU.MassTheory.B4CumulantBarEven
import QOU.MassTheory.ConjugationParitySplit
import QOU.MassTheory.ConjugationSymmetricDeltaExcluded
import QOU.MassTheory.PinchedOctahedronDegenerate
import QOU.MassTheory.BindingResidualAmplification
import QOU.MassTheory.FrameAmbiguitySecondOrder
import QOU.MassTheory.MilnorWeightParityConvergence
import QOU.MassTheory.MilnorMagnusCoefficient
import QOU.MassTheory.Mu3BaselineFragility
import QOU.MassTheory.A3PrecisionOrderSeparation
import QOU.MassTheory.A4PrecisionOrderSeparation
import QOU.MassTheory.A3UnitsConsistency
import QOU.MassTheory.BindingWeightMarkovPinning
import QOU.MassTheory.CKnotNonUniversal
import QOU.Mass.MassVolDensity
import QOU.Mass.MixedMultibondMuBarIntegrality
import QOU.Mass.BindingRecurrenceSpectral
import QOU.Mass.BindingClassicalKernel
import QOU.Mass.BindingInteriorMaxObstruction
import QOU.Mass.Lever1Depth2Exclusion
import QOU.Mass.Lever1TauClosedForm
import QOU.Machinery.HeckeTauAssignmentTower
import QOU.Machinery.CoxeterCommutingTransversal
import QOU.Knot.FigureEightVolumeSaddle
import QOU.Mass.BindingTauAnchorClosure
import QOU.Mass.QDifferenceConfluentObstruction
import QOU.Mass.KeystoneBridgeC1Binding
import QOU.Mass.ThetaSlopeArithmetic
import QOU.Mass.DoorVParityNoIdentity
import QOU.Mass.ColorCubicPowerSums
import QOU.Mass.TauQuantumIntegerForm
import QOU.Mass.ColorSpectralCubicGeometry
-- W1 route-1 candidate base operator for the q-difference prolongation D_q: the
-- q-shift/Jackson q-derivative introduces the quantum integer [n]_q (vs classical n,
-- q-free per ColorCubicPowerSums) and degenerates to d/dz at q→1. Candidate operator
-- only — no jet-tower lift, no C1 identification (beaned qou-d8de/xufp/ailp).
import QOU.Mass.QDiffProlongationBaseOperator
-- W1 structural handle: the color spectral cubic is a q-integer curve —
-- C_z(X) = [1]_z X³ + [2]_z X² + [3]_z X + [4]_z (coefficients = quantum integers),
-- the reason the base q-shift acts naturally on Σ. Computed from Σ, independent of C1.
import QOU.Mass.ColorCurveQIntegerForm
-- W1 q-partials of the color cubic + the branch-selection defect: on Σ,
-- Δ_q^z C(X,z) = C(qz,X) — the precise obstruction (X leaves Σ under z↦qz; the
-- correction to a root of C_{qz} is the branch datum D_q must choose).
import QOU.Mass.ColorCurveQPartials
-- W1 sheet structure: Vieta reconstruction (three sheets ↔ q-integer coefficients) and
-- the defect = product of gaps to the shifted sheets, framing branch selection as
-- breaking the S₃ sheet symmetry. The single-valued choice is the monodromy wall.
import QOU.Mass.ColorCurveSheets
-- W1: no single-valued algebraic branch — an irreducible cubic over the function field has
-- no root there (the permanent consequence of the witness's S₃ cover monodromy).
import QOU.Mass.ColorCubicNoBranch
-- Offset question (bean qou-vhv6): the colour-cubic discriminant is degree-6 (6 saddle
-- points), palindromic (q↔q⁻¹), strictly positive on ℝ (no real saddle — SOS certificate).
import QOU.Mass.ColorCubicDiscriminantPositive
-- Offset angle: the k-th Lagrange resolvent is an eigenvector of the C₅/S₃ cyclic shift
-- with eigenvalue ζ⁻ᵏ — the offset angle is the stabilizer root of unity.
import QOU.Mass.LagrangeResolventCyclicEigenvalue
-- Offset magnitude: under the q-integer-curve shift z↦qz the saddle z*↦z*/q, so the offset
-- is −ℏ_q·z*, magnitude |z*|·ℏ_q (ℏ_q=1−q⁻¹, radial; vanishes at q=1).
import QOU.Mass.SaddleQShiftOffset
-- W2: C1 module local exponents at 0 — char poly t²+(q−1)t+(q−1) (= t²−tr·t+det of the
-- companion [[0,1],[1−q,1−q]]), exponent-discriminant (q−1)(q−5). Birkhoff 0-side.
import QOU.Mass.C1ModuleExponents
-- W2 ∞: q-Gevrey growth of the C1 formal solution at ∞ — deg_q(c_n) = ∑_{m<n}(2m+1) = n²
-- (coefficients grow like q^{n²}), the divergence that forces Stokes summation.
import QOU.Mass.C1FormalSolutionGrowth
-- Tube ↔ spectral coordinate bridge: certifies the color-tube-cubic block's
-- prose substitution X = c + z and derives its three Vieta rows from the
-- (q-free) spectral symmetric data. Sorry-free, generic CommRing.
import QOU.Mass.ColorTubeSpectralBridge
import QOU.Mass.HeckeStokesEigenvalues
import QOU.Mass.NaStokesKeystone
import QOU.Mass.BindingHyperbolicRecurrence
import QOU.Mass.BindingQBesselKernel
import QOU.Mass.BindingJacobiAngerBridge
import QOU.Mass.BindingQHermiteOscillator
import QOU.Mass.BindingEigenfunctionTwoTier
import QOU.Mass.QWeberInterpolation
import QOU.Mass.PaddedShapeLevelRational
import QOU.Mass.QPlancherelSubNormalization
import QOU.Mass.AdditiveCorrectionConfinement
import QOU.Mass.QBetaProxyHReduction
import QOU.Mass.RogersSzegoInhabited
import QOU.Mass.SelectionRuleQuantumIntegerForm
import QOU.Mass.JetFiltrationExtensive
import QOU.Mass.LinearChainBondCount
import QOU.Mass.KappaWritheAsymptote
import QOU.Mass.LinearChainBondFactorization
import QOU.Mass.MilnorSignRepObstruction
import QOU.Mass.MilnorIndeterminacyGate
import QOU.Mass.BondChannelClassSelection
-- GAP-A-3 level-selection: §3b conjecture class for the super-exponential tower
-- growth (verified k≤10, faithful proof = Mathlib-gap) + the proved downstream
-- conditional theorem that logarithmic k(A) follows (k∝A / k∝bond-count excluded).
import QOU.Mass.LevelSelectionLogarithmic
import QOU.Calculations
import QOU.HadronicMass
import QOU.AtomicMass
import QOU.QuantumObservableUniverse
import QOU.QuantumObservableUniverses.DilogPentagonAssociator
import QOU.QuantumObservableUniverses.QAnalysis
import QOU.QuantumObservableUniverses.QBetaEnergyDictionary
import QOU.QuantumObservableUniverses.QExpEntire
import QOU.QuantumObservableUniverses.QIntegralTransforms
import QOU.QuantumObservableUniverses.QSchurWeyl
import QOU.SchurWeyl.BurnsideSpan
import QOU.SchurWeyl.HeckeAlgebra
import QOU.SchurWeyl.HeckeCoset
import QOU.SchurWeyl.HeckeDim3
import QOU.SchurWeyl.HeckeDim3Dim
import QOU.SchurWeyl.HeckeDim3Indep
import QOU.SchurWeyl.HeckeInclusion
import QOU.SchurWeyl.HeckeMarkov3
import QOU.SchurWeyl.HeckeWedderburn3
import QOU.SchurWeyl.HoefsmitRep
import QOU.SchurWeyl.HoefsmitRepGeneral
import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.Irreducibility
import QOU.SchurWeyl.SytAdmissible
import QOU.SchurWeyl.YoungTableaux
import QOU.QuantumObservableUniverses.VirtualProjection
import QOU.QuantumObservableUniverses.QDifferentialGeometry
import QOU.LiftingDescent.QuantumCharacteristicClassDisplay
import QOU.ParticleInteractions.HadronDisplay
import QOU.ParticleInteractions.AtomKnot
import QOU.ParticleInteractions.AtomicityRankOneOrderSeparation
import QOU.ParticleInteractions.AtomicityFromSelfDuality
import QOU.ParticleInteractions.AtomicityLieRank
import QOU.ParticleInteractions.AtomicityGroupRank
import QOU.ParticleInteractions.AtomicityRankOneToSingleObject
import QOU.ParticleInteractions.AtomicitySelfDualToSymplectic
import QOU.ParticleInteractions.WignerSU4FromSpinIsospin
import QOU.ParticleInteractions.WeakIsospinT3Grading
import QOU.Elaboration
import QOU.PathIntegrals
import QOU.MobiusEnergy
import QOU.Torsion
import QOU.BringsSurface
import QOU.BringsSurface.OctonionInvariantObstruction
import QOU.BringsSurface.ColourComplexStructure
import QOU.BringsSurface.PentagonTwistAssociator
import QOU.BringsSurface.OctonionCocycle
import QOU.Brings.RamificationParityMonodromy
import QOU.Brings.CategoricalLagrangianDMCubic
import QOU.BringCone
import QOU.QuaternionicElectroweak
import QOU.ArchimedeanUniverse
import QOU.PAdicQuantumGroups
import QOU.GaugeFieldFluidDynamics
import QOU.InformationTheory
-- Sorry-free P-vs-NP information-theoretic bricks.  The counting/decision
-- carrier `QouPNeqNp` is itself sorry-free and axiom-free: its open content
-- is the `faithful` class field, and **no instance is provided**, so every
-- downstream use carries `[QouPNeqNp …]` visibly in its signature.
import QOU.Information.SurrealBudgetGrade
import QOU.Information.CountingDecisionBarrier
import QOU.Information.GCTMultiplicityObstruction
import QOU.Information.MagnitudeAxisBoundary
import QOU.Information.CountingModuliGrade
import QOU.Information.SkeinSurrealGrade
import QOU.Information.PolyGrowthAlgebra
import QOU.Information.MagnitudeTraceCommutator
import QOU.Information.CocenterTraceFactor
import QOU.Information.OuterDerivationResidue
import QOU.Information.HochschildH1
import QOU.Information.SkeinGradeConnective
import QOU.Information.SkeinShadowConjInvariance
import QOU.Information.PNeqNpWallUnification
import QOU.Information.GCTSchurMultiplicity
import QOU.Information.GCTPerRankObstruction
import QOU.LightningPath
import QOU.RepresentationTheory
import QOU.GradedFrobeniusHopf
import QOU.ChannelSeparation
import QOU.Archimedean
import QOU.Archimedean.DilogReflection
import QOU.Archimedean.IdealTetrahedronConcavity
import QOU.Archimedean.LobachevskyDerivative
import QOU.Archimedean.IdealTetrahedronShapeBridge
import QOU.Archimedean.IdealTetrahedronVolumeConcavity
import QOU.Archimedean.LobachevskyMaximum
import QOU.Archimedean.HyperbolicVolumeMeasure
import QOU.Archimedean.HyperbolicVolumeFubini
import QOU.Archimedean.IdealTetrahedronRegion
import QOU.Archimedean.OrthoschemePolarReduction
import QOU.Archimedean.OrthoschemeBaseIntegral
import QOU.Archimedean.OrthoschemeWedgePair
import QOU.Archimedean.OrthoschemeRotation
import QOU.Archimedean.OrthoschemeLambdaSum
import QOU.Archimedean.OrthoschemeTiling
import QOU.Archimedean.DilogPartBBranchPointLimit
import QOU.Archimedean.DilogPartBBranchPhase
import QOU.Archimedean.DilogPartBBranchPointSum
import QOU.Archimedean.DilogPartBEulerTail
import QOU.Archimedean.DilogPartBIteratedLimit
import QOU.Archimedean.DilogPartBBoundarySeed
import QOU.Archimedean.DilogPartBWP1Capstone
import QOU.Archimedean.DilogPartBWP1Refutation
import QOU.Archimedean.DilogPartBFaddeevScaling
import QOU.Archimedean.DilogPartBJointAssembly
import QOU.Archimedean.DilogPartBBorelCantelli
import QOU.Archimedean.DilogPartBWindowMeasure
import QOU.Archimedean.DilogPartBAEAssembly
import QOU.Archimedean.DilogPartBAEFinal
import QOU.Archimedean.DilogNaStokesOrdering
import QOU.Interactions
import QOU.Encounter
import QOU.BraidKnot
-- The Specht irreducibility chain. Historically kept OUT of the umbrella
-- because `SpechtIrreducible` carried an honest `sorry`; it no longer does
-- (`specht_form_nondegenerate` and `specht_isSimple` are both proved), so it
-- belongs in the build closure where CI can see it. Its own imports
-- (`SpechtStandardBasisCore`) still carry the Garnir straightening stub —
-- that is pre-existing and now visible in the package build rather than
-- hidden outside it.
import QOU.BraidKnot.SpechtBaseChange
import QOU.BraidKnot.SpechtIrreducible
import QOU.BraidKnot.SpechtCrossDominance
import QOU.BraidKnot.SpechtCrossKappa
-- Absolute irreducibility (W2 of the Wedderburn epic): the commutant of every
-- simple `k[S_n]`-module is the base field. Sorry-free, so it belongs in the
-- build closure. Pulls `SpechtClassification` in transitively.
import QOU.BraidKnot.SpechtAbsolutelyIrreducible
-- W1+W3 brick 1: the Schur diagonal `dim Hom_G(S^μ, S^μ) = 1`, i.e. the Specht
-- characters are orthonormal over ℚ and not merely orthogonal.
import QOU.BraidKnot.SpechtSchurDiagonal
-- W1+W3 brick 3: `Hom_G(k[G], V) ≃ V` — the multiplicity of an irreducible in the
-- regular representation is its dimension. General; no S_n, no Specht modules.
import QOU.MathlibExt.RegularHom
-- The ofModule/asModule round-trip (bean qou-ltzf): a k[G]-module viewed as a
-- representation and back is itself, k[G]-linearly; simplicity transfers.
import QOU.MathlibExt.OfModuleAsModule
-- W1+W3 brick 4a: the two sides of the Wedderburn dimension count.
import QOU.BraidKnot.SpechtBlockDimension
-- W1+W3 brick 4b: the multiplicity of S^μ in the regular representation is dim S^μ.
import QOU.BraidKnot.SpechtRegularMultiplicity
-- W1+W3 brick 4c: the Specht action map is injective, giving n! <= sum (dim S^mu)^2.
import QOU.BraidKnot.SpechtActionInjective
-- W1+W3 brick 5: the whole split follows from one number, and that number is the
-- combinatorial RSK identity sum_mu (#SYT mu)^2 = n!.
import QOU.BraidKnot.SpechtWedderburnCriterion
-- W1+W3 brick 6: the split UNCONDITIONALLY for n <= 12, via the corpus's own
-- decide-verified RSK/Burnside count. No RSK correspondence, no axiom.
import QOU.BraidKnot.SpechtWedderburnLe12
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
-- The four §3b conjecture-class carriers for the `conj:q-gl-*` blocks.
-- They sat outside the import graph, so `lake build` never compiled them:
-- nothing verified that the open conjectures the paper cites even
-- elaborate. They could not be added before PR #4886 renamed the
-- aggregate's four same-named theorems — importing both was a hard
-- `already declared`.
import QOU.QGeometricLanglands.q_gl_fiber_functor
import QOU.QGeometricLanglands.q_oper_hecke
import QOU.QGeometricLanglands.q_gl_kummer_filtration
import QOU.QGeometricLanglands.q_gl_classical_limit
import QOU.AppendixQValues.ProtonBorromeanAssembly
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
import QOU.MathlibExt.RootsOfUnityProduct
import QOU.MathlibExt.GaussianThetaSum
import QOU.MathlibExt.GaussianShearIntegral
import QOU.MathlibExt.StirlingRobbins
import QOU.MathlibExt.TrapezoidRule
import QOU.MathlibExt.CorrectedTrapezoid
import QOU.MathlibExt.CompositeEulerMaclaurin
import QOU.MathlibExt.SinCubeBounds
import QOU.MathlibExt.TaylorRemainder
import QOU.MathlibExt.GaussianSumBound
import QOU.MathlibExt.GaussianThetaBound
import QOU.MathlibExt.GaussianTiltedSum
import QOU.MathlibExt.GaussianTailBound
import QOU.MathlibExt.GaussianWindowSum
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
import QOU.BraidsAndKnots.TFromTraceCyclicity
-- D15 Pachner–Pentagon (conj:pachner-pentagon-borromean): §3b conjecture-class
-- with sorry-free consumer theorems. Wired so CI type-checks it (not an orphan).
import QOU.BraidsAndKnots.PachnerPentagonBorromean
-- Δ_λ ℓ¹-ceiling: sign-only fixes structurally excluded (Option-E prune, PR #2925).
-- Triangle bound on the per-block binding closure; sorry-free, generic base ring.
import QOU.BraidsAndKnots.DeltaLambdaL1Ceiling
-- Δ_λ = DT-count of Springer 𝓑_λ: the target UNDER-DETERMINES the moduli
-- (dimension forced only mod 2) — sharpens the open substrate-derivation crux
-- (bean qou-ylot); sorry-free, base ring ℤ.
import QOU.BraidsAndKnots.DeltaLambdaDTModuliUnderdetermined
-- Δ_λ = DT/3d-index Euler characteristic, general n (bean qou-bvpp): the n=5
-- anchor's dtEuler=deltaLambda lifted to ALL partitions via the single-degree
-- graded-Euler collapse; sorry-free, base ring ℤ/ℕ (combinatorial).
import QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN
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
-- qou-n1dj: re-sources the `N = 2` hypothesis of the D-forcing chain from the
-- QOU definition's own categorical volume constraint instead of from
-- thm:su2-emergence, whose lean.ref is unresolved and whose Lean carries no
-- rank content. Records both readings of the constraint and which one forces.
import QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo
-- D6-upstream color-tube channel class (conj:inter-nucleon-channel-color-tube):
-- content-bearing §3b-cond weight-tensor class + ε rule + uniform-projection
-- satisfiability witness + T₁ fiber wiring. Wired so CI type-checks it.
import QOU.BraidsAndKnots.InterNucleonChannelColorTube
-- Color-pair isotypic decomposition T₁⊗T₁ = A⊕T₁⊕H (bean ctkw): the Sym²/Alt²
-- Z/2 grading is FORCED by dimension, and the uniform W=1/9 is the
-- isotypy-blind barycentre. Narrows open Q1; no instance. Sorry-free.
import QOU.BraidsAndKnots.ColorPairIsotypicDecomposition
-- Flavor side of W (bean 63n2): isospin selection on the color-pair
-- decomposition. CONDITIONAL on InterfaceExchangeAntisymmetry (class, NO
-- instance); consequence is charge symmetry between pp and nn. Sorry-free.
import QOU.BraidsAndKnots.ColorFlavorIsospinSelection
-- D6 charge conjugation (conj:c-from-color-flavor-swap): C-involution +
-- ε-invariance proved sorry-free; W-invariance as §3b-cond class field;
-- derived generator-data C-invariance. Wired so CI type-checks it.
import QOU.BraidsAndKnots.CFromColorFlavorSwap
-- Post-τ q-Rogers pentagon: α/β substitution algebra, the log² correction
-- term, and the q≠1 analytic-continuation conjecture-class.
import QOU.BraidKnot.QRogersPentagonArchimedean
import QOU.Information.p_bandwidth_bound
import QOU.ParticleInteractions.atomic_lp_stability
import QOU.ParticleInteractions.silver_ratio_beta_decay_null
import QOU.ParticleInteractions.delta_pre_archimedean
import QOU.ParticleInteractions.even_tower_continuant_harmonics
import QOU.FluidDynamics.q_bkm_criterion
import QOU.FluidDynamics.TwoVortexChannelAlgebra
import QOU.QBeta.BarOddLadderShape
-- Anchor-followups cluster (beans qou-o3ta / qou-4g4a): the interface scalar,
-- the Markov-Gram signature, and the Temperley-Lieb tower. Added to the root
-- import list 2026-08-09 -- all three were ORPHANS, compiling only when named
-- explicitly on the lake command line, so a plain `lake build` never checked
-- them and no CI run would have caught a regression in any of them.
import QOU.QBeta.InterfaceScalar
import QOU.QBeta.GramSignature
import QOU.QBeta.TemperleyLiebTower
import QOU.QBeta.WedderburnTraceDecomposition
import QOU.QBeta.MarkovGramDegenerate
import QOU.QBeta.JonesNormalisation
-- 5₂ saddle sum rule lane (bean qou-0yqu). These were orphaned from the
-- library root: `lake build` only builds `QOU.lean`'s import closure, so a
-- module nothing imports is never compiled. See bean qou-orph.
import QOU.QBeta.FiveTwoCyclotomicBloch
import QOU.QBeta.FiveTwoLevelSevenLadder
import QOU.QBeta.FiveTwoRogersExtend
import QOU.QBeta.FiveTwoFiveTermArguments
import QOU.QBeta.FiveTwoRogersReflection
import QOU.QBeta.FiveTwoAbelFiveTerm
-- The Li₂-continuation / scalar-IFT chain this lane rests on is wired at the
-- top of this file (with the other MathlibExt imports), not here — it is
-- general analytic infrastructure, not 5₂ content.
import QOU.Archimedean.LiTwoNegOne
import QOU.QBeta.FiveTwoDiscriminant
import QOU.QBeta.FiveTwoCutAvoidance
import QOU.QBeta.FiveTwoDeformedSaddle
import QOU.QBeta.FiveTwoCurveDeriv
import QOU.QBeta.FiveTwoEnvelopeSum
import QOU.QBeta.FiveTwoEnvelopeAssembly
import QOU.QBeta.FiveTwoBranchByArgument
import QOU.QBeta.FiveTwoArgSector
import QOU.QBeta.FiveTwoRootStructure
import QOU.QBeta.FiveTwoRootLabelling
import QOU.QBeta.FiveTwoBranchPinned
import QOU.QBeta.FiveTwoEnvelopeWiring
import QOU.QBeta.FiveTwoPairSaddle
import QOU.QBeta.FiveTwoBranchPinnedB
import QOU.QBeta.FiveTwoTransport
import QOU.QBeta.FiveTwoEnvelopeInstance
import QOU.QBeta.FiveTwoLevelSevenBridge
import QOU.QBeta.FiveTwoExtendIdentification
import QOU.QBeta.FiveTwoLevelSevenAssembly
import QOU.QBeta.FiveTwoSaddleSumRule
import QOU.QBeta.FiveTwoComplexPentagon
import QOU.QBeta.FiveTwoFlattenedPentagon
import QOU.QBeta.FiveTwoOhtsukiCriticalPoint
import QOU.QBeta.FiveTwoDTSpectrumSplit
import QOU.QBeta.ChiralityGradedCount
import QOU.QBeta.DTChiralityBarInvolutionLink
import QOU.QBeta.QuiverMirrorAutomorphismExcluded
import QOU.QBeta.FiveTwoSaddleCurve
import QOU.QBeta.FiveTwoStokesMatrixIdentities
import QOU.QBeta.FiveTwoSumRuleIntegrand
import QOU.QBeta.HabiroTailStar
import QOU.QBeta.HabiroTailCorollaries
import QOU.QBeta.LevelMixingBridge
import QOU.QBeta.LevelMapValuation
import QOU.QBeta.LeverLogDerivative
import QOU.QBeta.MeridianLinearBarOdd
import QOU.QBeta.ImQDecayLinearResponse
import QOU.QBeta.RationalCoeffRecurrence
import QOU.QBeta.SilverAnchorGrounding
import QOU.QBeta.ReebTowerJacobiAnger
import QOU.QBeta.PhiBSArgumentIdentification
import QOU.QBeta.TauNormalizationChoice
import QOU.QBeta.ModularRayDiagonalPrune
import QOU.QBeta.OhtsukiNZBridgeScale
import QOU.QBeta.WindingGFTransform
import QOU.QBeta.ThetaRealityBound
import QOU.QBeta.AfreeThetaConstraint
import QOU.QBeta.ChannelMeridianIdentification
import QOU.QBeta.CompleteStructureExclusion
import QOU.QBeta.ThetaLipschitzObstruction
import QOU.QBeta.StokesSymmetryConstant
import QOU.QBeta.StokesQZeroDTCount
import QOU.QBeta.StokesSymmetryConstantQZero
-- M2 (conditional BPS characterization) was an umbrella orphan (qou-orph
-- pattern: nothing imported it, so `lake build` never checked it). Importing
-- the M3 conjecture class below pulls the whole M2 chain under CI.
import QOU.QBeta.AomegaM2BPSCohomology
import QOU.QBeta.RouteCM3CategoryIdentification
import QOU.QBeta.UDeformFamilyPruning
import QOU.QBeta.NewtonRealityInvariance
import QOU.QBeta.QBesselContiguityRecurrence
import QOU.QBeta.QBesselBarCovariance
import QOU.QBeta.QBesselQuadraticActionTerm
import QOU.QBeta.QCasoratianAbel
import QOU.QBeta.QCasoratianBarParity
import QOU.QBeta.ZBarParity
import QOU.QBeta.QBetaZeta4ResidueRefutation
import QOU.QBeta.BarParityZeta4Swap
import QOU.QBeta.CuspShapeBarParity
import QOU.QBeta.ArgUPhaseBranchSelection
import QOU.QBeta.CAL3AnchorStructure
import QOU.QBeta.SRigidityPrune
import QOU.QBeta.SLeakZeroCrossing
import QOU.QBeta.SLeakMagnitudeOffsetRatio
import QOU.QBeta.SLeakMagnitudeTaylorRatio
import QOU.QBeta.HopfCubicOddCarrier
import QOU.QBeta.Zeta4DescentCarrier
-- Écalle-acceleration composition collapse: composing a single fixed-order
-- Borel–Leroy transform reaches only ℤ-multiples of its order, never an
-- incommensurate critical time — a genuine multi-level Écalle kernel is needed.
import QOU.QBeta.DLadderAccelerationComposition
-- Bar-parity selection rule of the Ohtsuki κ-tower at the imaginary substrate
-- 2πb²=i·t: even rungs → Re 𝔙 (Vol/mass), odd rungs → Im 𝔙 (bar-odd S / CS).
import QOU.QBeta.OhtsukiTowerBarParity
-- Even-channel arithmetic home: the 4₁ Kashaev saddle Taylor data ∈ ℚ(√3)·π^k
-- (Hessian −√3π; b₁=√3π/54). Counterpart to the odd HopfCubicOddCarrier (KC20).
import QOU.QBeta.Qsqrt3SaddleArithmetic
import QOU.QBeta.H4RouteBBranchingPrune
import QOU.QBeta.QLommelOrderRecurrence
import QOU.QBeta.HoefsmitBBarParity
import QOU.QBeta.StageCSigma3LiftObligation
import QOU.QBeta.CrossingWeightAffine
import QOU.QBeta.SelfDualLocusTargetSpec
import QOU.QBeta.SubstratePeriodsIndependent
import QOU.QBeta.WenzlPochhammerBoundary
-- A_ω uniqueness-leg strip-growth constructor: derives `FaddeevPhiStripGrowth`
-- from the FKV eq-22 compact bound + periodicity + same-divisor. Pulls the whole
-- A_ω uniqueness cone (FaddeevStripGrowthFKV → box-reduction; FaddeevPhiStripGrowth
-- → PhiBProd) into CI so it is typechecked long-term (was orphaned).
import QOU.QBeta.FaddeevStripGrowthConstructor
-- c₃ Berezinian-wall parity constraints: adjoint-scaled cross-terms are bar-EVEN
-- (all bar-even scalings, generalizing #4421), the non-self-adjoint g·γ carrier is
-- realizable + bar-ODD, and the two families disjoin off 2-torsion. Pulls the
-- BerezinianSelfAdjointCrossTerm cone into CI (was orphaned).
import QOU.QBeta.BerezinianCrossTermParity
-- c₃ Berezinian bar-odd isolation: the mass endomorphism 𝓜 = A − t has bar-odd part
-- −(t − σt), so the bar-even diagonal mass A contributes nothing — c₃ is carried entirely
-- by the cross-term t = B·D⁻¹·C (isolates the q_cubic=C1 wall to the cross-term).
import QOU.QBeta.BerezinianBarOddIsolation
-- A=3 magnitude r*≈1.585 is a FREE parameter of the Berezinian cross-term: the even-face
-- correction (A−t)/A with t=B·D⁻¹·C is surjective in the off-block B (crossTerm_magnitude_surjective),
-- while block-diagonal/single-trace data gives correction ≡ 1 (no lift). So the cross-term is the
-- unique lift source but its size is unconstrained — r* is a fit absent the DM-cubic derivation of
-- B,C (qou-jqof). Magnitude complement to the parity bricks (Isolation/CrossTermParity).
import QOU.QBeta.SuperBerezinianA3Magnitude
-- A=3 off-block DERIVATION (sharpens Route 2): the transpose-eigenbasis rotation of the
-- bar-self-adjoint H₃(q) mass endomorphism PINS the off-blocks B=C=(a−b)/2, giving the
-- even-face factor 1−((a−b)/(a+b))² ≤ 1 (magnitudeFactor_le_one, invariant sq_nonneg).
-- So the branching Schur complement is a REDUCTION; the observed lift r*≈1.585>1 is
-- structurally UNREACHABLE (observed_lift_unreachable) and requires the anti-self-adjoint
-- (GGM/Stokes) off-block the branching leaves free (A3LiftFromDerivedOffBlock, no instance).
import QOU.QBeta.A3OffBlockDerivation
-- A=3 anti-self-adjoint lift (qou-jqof): the even-face factor is AFFINE in the single
-- anti-self-adjoint amplitude E — factor = factor_sa − B·D⁻¹·E/A. A lift FORCES E ≠ 0
-- (lift_forces_nonzero_amplitude/amplitude_nonzero); E is free+unique (amplitude_surjective/
-- _injective) ⇒ scope-(a), one real DOF. Deriving E from the DM q-cubic prolongation symbol
-- is the open keystone (DerivedAmplitudeGivesLift, no instance).
import QOU.QBeta.A3AntiSelfAdjointLift
-- DT-index / 3d-index / graded-Euler route is BAR-PARITY excluded from supplying the
-- anti-self-adjoint amplitude E (DT values bar-even integers; E bar-odd) — scope-(b).
import QOU.QBeta.DTIndexAmplitudeE
-- WALL: the LOCAL Stokes/resurgence route cannot supply the A=3 amplitude E —
-- single-slope carrier ⇒ RSZ isoformal dim 0 ⇒ E=0 (no lift, scope-(b)); multi-slope
-- leaves E free ⇒ value lives in the GLOBAL Birkhoff matrix (open successor, no instance).
import QOU.QBeta.StokesAmplitudeE
-- WELL-POSEDNESS of E as a functional of the GLOBAL Birkhoff matrix: (a) the cross-ratio
-- P₀₁P₁₀/(P₀₀P₁₁) is the UNIQUE gauge-invariant (frame-free target); (b) a single entry is
-- gauge-dependent (residual elliptic-unit freedom), so E = the cross-ratio, not an entry.
import QOU.QBeta.BirkhoffAmplitudeWellPosed
-- CONSTRUCTION: the A=3 amplitude E is the frame-free Birkhoff CROSS-RATIO χ(P)
-- (not a bare entry — gauge-movable, ill-posed); cross-ratio elliptic because the exponent
-- multipliers cancel; the WALL is χ(P)'s VALUE (0-exp determined, ∞-exp/closed-form open).
import QOU.QBeta.BirkhoffAmplitudeE
-- c₃ Faddeev tetraplectic→combinatorics reduction backbone: the q²-shift functional
-- equation of the single-lattice product ∏(1+q^{2n+1}x) (telescoping), the recurrence
-- that pins the e_k = q^{k²}/(q²;q²)_k coefficients (Python witness cross-checks k≤6).
import QOU.QBeta.TetraplecticProductRecurrence
-- Concrete H₃(q) Markov-trace functional (NF model: linearity, cyclicity,
-- Hecke σ₀²=hσ₀+1, Markov reduction tr(x·σ₁)=z·tr(x)); cross-checked vs
-- `gram.py` / `pyhecke.trace_formal`. Was an orphan under `Machinery/`.
import QOU.Machinery.MarkovTraceOnHecke
-- Lean schema for the 3-axis (knot, partition, atom) derived-χ catalogue
-- (Python: `derived_chi_catalogue.py`, PR #1952). Type-level cell record +
-- §3b-cond R-matrix-derivation provenance classes; 0 sorries. Was an
-- orphan under `Machinery/` (not imported ⇒ never built by CI).
import QOU.Machinery.DerivedCharacterCatalogue
-- The explicit Wedderburn ladder (ranks 2-3), the tower-induction
-- interface, and the two Mathlib proof_wanted fills (PRs #4054, #4094,
-- #4095, and this branch). Were orphans (not imported ⇒ never built by
-- CI); registered here for coverage. Transitively pulls HeckeH3Characters,
-- HeckeH3BlockRep, HeckeH2Wedderburn, HeckeBraidedCategoryScaffold,
-- MatrixSemisimple.
import QOU.Machinery.HeckeH2WedderburnReal
import QOU.Machinery.HeckeH3Semisimple
import QOU.Machinery.HeckeH3GramNondegeneracy
import QOU.Machinery.HeckeH4AlgebraLaws
import QOU.Machinery.HeckeH4BlockRep
import QOU.Machinery.HeckeH4Characters
import QOU.Machinery.HeckeH4BlockMap22
import QOU.Machinery.HeckeH4BlockMap31
import QOU.Machinery.HeckeH4BlockMap211
import QOU.Machinery.HeckeH4Wedderburn
import QOU.Machinery.HeckeH4Semisimple
import QOU.Machinery.HeckeTowerBasicConstruction
import QOU.Machinery.QuantumTorus
import QOU.Machinery.QuantumTorusAJ
import QOU.Machinery.QuantumTorusDivision
import QOU.Machinery.QuantumTorusSymbol
import QOU.Machinery.StrongAJFigureEight
import QOU.Machinery.AJTorusAnnihilation
import QOU.Machinery.AJMinimality
import QOU.MathlibExt.EndSemisimple
import QOU.HyperellipticQuintic.zeta5_residue_monodromy

import QOU.Archimedean.BorromeanQuark
import QOU.Interactions.QIntegerMassFormula
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.BringEllipticFactor
import QOU.Archimedean.SigmaJGeometricCarrier
import QOU.Archimedean.HodgeWeilRealStructure
-- B2-lift AUTOMATIC (moduli-independent) ingredients, Lean-locked (bean qou-8mbd):
-- Brick 1 nome exponent-group equivariance (τ↦−τ ↔ q↦q⁻¹; τ↦½−τ ↔ q↦−q⁻¹, Z4→GInt units);
-- Brick 2 Weil∘Galois = conj + complete Fix(c)/Fix(F) characterization. No MOC instance (open).
import QOU.Archimedean.B2LiftAutomaticIngredients
import QOU.Archimedean.CanonicalTitsIso
import QOU.Archimedean.TauRhoHodgeShadow
import QOU.Archimedean.TauS5EquivarianceReduction
import QOU.Archimedean.PerLoopMeasureShadowAssembly
import QOU.Archimedean.TauRhoHodgeLiftInterface
-- B2-lift interface SHARPENING (bean qou-demm): collapses the 2-field TauRhoHodgeLift
-- to a single open field PeriodMapWeight (the MOC), deriving equal-split + doubled-total
-- and recording the involution-match + nome-equivariance as automatic. No instance (open).
import QOU.Archimedean.PeriodMapWeightReduction
import QOU.Archimedean.VertexLocalTauModel
import QOU.Archimedean.LiftFromReality
import QOU.Archimedean.TauFunctorTargetSpec
import QOU.Archimedean.DeckRealityEquivariance
import QOU.Archimedean.BorelProperTimeMoment
import QOU.MathlibExt.FrechetShohat
import QOU.Archimedean.BalancedKernelConfluence
import QOU.Archimedean.BalancedMomentConfluence
import QOU.Archimedean.BalancedKernelTightness
import QOU.Archimedean.BalancedCarrierJacobi
import QOU.Archimedean.SWJacksonMomentFactorization
import QOU.Archimedean.SWCoreJacobi
import QOU.Archimedean.TropicalClassTransport
import QOU.Archimedean.AwZeroLocalization
import QOU.AlgebraicSubstrate.SubstrateClockUniqueness
import QOU.AlgebraicSubstrate.PlanckStepAtomicity
import QOU.AlgebraicSubstrate.AtomicityJetIndependence
import QOU.AlgebraicSubstrate.BarReflectionGridSelection
import QOU.AlgebraicSubstrate.DualFrameGaussianExponents
import QOU.Archimedean.BarReflectionGridSelectionReal
import QOU.Archimedean.LoopWeightRealSymmReduction
import QOU.Archimedean.MarkovGramRealSymm
import QOU.Archimedean.MatrixSchurCommutant
import QOU.Archimedean.SchurInvariantFormProportional
import QOU.Archimedean.InvariantFormTransport
import QOU.Archimedean.GaugeGroupThreeScale
import QOU.Archimedean.SchwingerMeasureShape
import QOU.Molecular.PalindromicityOrbitalType
import QOU.Molecular.ShellCapacitySelfSquare
import QOU.Molecular.ShellClosureNfTermCount

import QOU.Conjectures.ShellTransitionKnot
import QOU.Conjectures.KnotFactorFrobeniusPairing
import QOU.Conjectures.WeakSpectralCompleteness
import QOU.Conjectures.MagicNumbersBring
import QOU.Conjectures.QuantumLanglandsDual

-- q-Gevrey / Newton-polygon Mathlib infra (epic qou-7b7v, brick MI-1).
import QOU.Mathlib.QGevreyOrder
-- Elliptic divisor-degree scaffold (epic qou-lbth / bean qou-toqt, brick PI-2):
-- Liouville's third theorem (Σ ord = 0) stated open; f'/f-periodicity + divisor-
-- lattice-periodicity bricks proved sorry-free.
import QOU.Mathlib.EllipticDivisorDegree
import QOU.Mathlib.HadamardFactorization
-- Argument-principle scaffold (epic qou-lbth / bean qou-bmyx, brick PI-3):
-- (1/2πi)∮ f'/f = #zeros − #poles stated open (residue-of-logDeriv = order is the
-- Mathlib gap); #zeros−#poles=Σ ord counting brick + 2πi≠0 proved sorry-free.
-- lean-direct exit 0 (3 intended sorries on the deep theorems); lake build QOU is CI gate.
import QOU.Mathlib.ArgumentPrinciple
-- Identity-I / RSK infrastructure (verified library files; wired in for CI build coverage).
import QOU.Mathlib.PartitionListBridge
import QOU.Mathlib.PartitionsOfBridge
import QOU.Mathlib.StandardYoungTableau
import QOU.Mathlib.RSKBurnsideTarget
import QOU.Mathlib.StandardYoungTableauBot
import QOU.Mathlib.HookLengthFormula
import QOU.Mathlib.ColLenRowLensBridge
import QOU.Mathlib.QHookProduct
import QOU.Mathlib.RSKSubstrateInstances
import QOU.Mathlib.IdentityIHLFBridge
import QOU.Mathlib.SchenstedInsertion
import QOU.Mathlib.SchenstedTableau
import QOU.Mathlib.SchenstedRecording
import QOU.Mathlib.SchenstedRecordingShift
import QOU.Mathlib.SchenstedCellsBridge
import QOU.Mathlib.SchenstedStandardTableau
import QOU.Mathlib.SchenstedStandardGeneric
import QOU.Mathlib.SchenstedPairingMap
-- RSK inverse, brick 1: reverse row insertion and the inversion law.
import QOU.Mathlib.SchenstedReverseRow
-- RSK inverse, brick 2: the reverse cascade and its inversion law.
import QOU.Mathlib.SchenstedReverseCascade
-- RSK inverse, brick 3: word recovery from the tableau plus the row-index record.
import QOU.Mathlib.SchenstedWordRecovery
-- RSK inverse, brick 4: the recording tableau IS the row-index record.
import QOU.Mathlib.SchenstedRecordingIndex
-- RSK inverse, brick 5: reading the row index back off the recording tableau.
import QOU.Mathlib.SchenstedReadback
-- RSK inverse, brick 6: the whole index list, read back off Q.
import QOU.Mathlib.SchenstedReadbackFold
-- RSK inverse, brick 7: the RSK map is injective on words of fixed length.
import QOU.Mathlib.SchenstedRSKInjective
-- RSK inverse, brick 8: RSK separates permutations.
import QOU.Mathlib.SchenstedPermInjective
import QOU.Mathlib.SYTEnumeration
import QOU.Mathlib.SYTEnumerationBridge
import QOU.Mathlib.SYTEnumerationFintype
import QOU.Mathlib.SYTHookFormula
import QOU.Mathlib.SYTHookFormulaBeta
import QOU.Mathlib.SYTHookFormulaBetaProd
import QOU.Mathlib.SYTHookFormulaRows
-- Bean qou-7gei: the >= 3-row corner-removal fact, which discharges the
-- combinatorial hypothesis of QOU.QBeta.TemperleyLiebTower.vanishing_step.
-- Pulls in QOU.Mathlib.YoungDiagramCorner (IsCornerCell / eraseCorner), which
-- the SYT cluster also uses.
import QOU.Mathlib.YoungDiagramThreeRowCorner
-- Ballot numbers m_j(n) = C(n,j) - C(n,j-1): the Mathlib-gap engine shared by
-- the q-Clebsch-Gordan normalisation (qou-0cyu G2) and the Catalan sum (G5).
import QOU.Mathlib.BallotNumbers
import QOU.QBeta.QDimNormalisation
import QOU.MassTheory.MirrorPairBondScaling
import QOU.QBeta.CubicSaddleDiscriminant
import QOU.QBeta.G3RealnessConjugationBrick
import QOU.QBeta.SixOneShapeDiscriminant
import QOU.MassTheory.BarParityClusterObstruction
-- A=4 Brunnian deficit: derived leading data (exact order 6, coeff -96)
-- replacing the MEASURED A=4 leg of MilnorParitySignLaw. Sorry-free.
import QOU.MassTheory.BrunnianDeficitLeadingOrderDerived
-- A=4 interface-operator magnitude: the derived -ln det(I+G) form (spectrum {±√5,±1})
-- is surjective onto (0,∞) in its one free scalar m ⇒ WALL(scope-(a)); naive z scope-(b)
-- excluded. Formalize-first, 0-fit, sorry-free.
import QOU.MassTheory.A4InterfaceMagnitude
import QOU.MassTheory.BindingSaturationCapA4
import QOU.MassTheory.BraneGeometricResummation
-- front-1: the radial handle C_knot = Vol(K)·ρ(K)/ℏ_q² with ρ = tr_M is refuted
-- under every volume reading — Vol ≡ 0 for the literal mass-braid H₉ closures, and
-- a 2.37× anti-correlated residual for the corpus-canonical binding links.
import QOU.MassTheory.VolTHe3RadialHandle
-- prjo: q₀-free ≥3-row extensive cumulant, forward from the proved Δ_λ. Feeds the
-- C(A,k) cluster basis the combinatorial ≥3-row signed-Springer-dim content s_k;
-- re-derives μ₂=0 combinatorially (0-fit match) but gives the (−,+) sign order vs
-- the derived (+,−) window and ratio 2 vs ~9.75. Scope-(a) negative, q₀-free.
import QOU.MassTheory.ThreeRowExtensiveCumulant
-- qou-prjo LEAD-2 (geometric route): transverse NA-Stokes surface-curvature
-- structure + THE WALL (nonzero pairing needs position-dependent transport =
-- the missing surface-2-form data). Forward geometric, sorry-free, magnitude
-- NOT derived.
import QOU.MassTheory.TransverseSurfaceCurvature
-- qou-prjo: a two-block dominance exchange forces a zero (IVT), and "block B
-- overtook block A" and "the total went negative" are the same statement. The
-- per-block dominance data are HYPOTHESES — the f64 numbers are not certified,
-- and the two-block mechanism is realised at n=6 ONLY (n=9 is multi-block
-- cancellation, n=12's total exceeds its largest term). Sorry-free.
import QOU.BraidsAndKnots.ThreeRowSignCrossing
-- qou-prjo: the Wenzl-level stratum degeneracy — s_λ = 0 at integer level r=k for
-- every ℓ(λ) > k. Since r → 2⁺ as q → 1⁺, the whole ℓ≥3 stratum degenerates at
-- q=1, which is WHY the ≥3-row trace is O(10⁻⁵) near q=1. Sorry-free, generic
-- Field K.
import QOU.BraidsAndKnots.WenzlLevelStratum
-- 1-dim Hecke block characters are writhe monomials (chi_triv=q^writhe,
-- chi_sign=(-q⁻¹)^writhe); writhe-0 baryon ⟹ both collapse to 1. Prunes the
-- charm-mass Frobenius block-projection route (block ratio O(1) at balanced
-- writhe). docs/audits/2026-08-02-charm-mass-frobenius-block-projection-negative.md
import QOU.MassTheory.TrivialBlockWrithe
import QOU.BraidKnot.ColoredJonesRecurrence
import QOU.BraidKnot.KnotOperatorRecurrence
-- Resurgent-bridge tranche (Δ_λ sign/magnitude → DT/3d-index unification):
-- descent scaffold, both horns, fgte κ-tower, dri7 bar-odd ladder, DT capstone.
import QOU.Resurgence
import QOU.QBeta.Stokes3LargeOrderAmplitude
import QOU.QBeta.BarOddLadderEdgeSuppression
import QOU.BraidsAndKnots.DeltaLambdaDTIndex
import QOU.BraidsAndKnots.RossmannCCBridge
import QOU.BraidsAndKnots.DeltaLambdaTopDegreeConcentration
import QOU.BraidsAndKnots.DeltaLambdaJetOrderDegreeSelection
import QOU.BraidsAndKnots.DeltaLambdaGradedConcentration
import QOU.BraidsAndKnots.NStatConjugateGeneral
import QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional
-- qou-48is: the Φ_q transfer factors T(d) = S + d·1 all commute, so the chain
-- product — and the readout V̂ = z·M₁₀ + M₁₁ — depends on the crossing
-- coefficients ONLY as a multiset. Consequence: the two ³He arrangements ppn
-- and pnp are EXACTLY degenerate on the bare nucleon chain, so rule (iii) of
-- prop:ground-state-ordering is a tie there, not a strict win. Sorry-free,
-- generic CommRing; derives no binding energy and no ordering.
import QOU.MassTheory.TransferFactorCommute
-- qou-48is (doc-currency, PR #4854): PR #4851's two ordering Lean files were
-- never registered here, so nothing built them. Both verify lean-direct exit 0.
import QOU.MassTheory.CanonicalOrderingSaddle
import QOU.MassTheory.NucleonOrderingSymmetry
-- qou-48is (PR #4855): the A>=4 clause of prop:ground-state-ordering is FALSE —
-- explicit strictly-better arrangement at A=5 (sorted pnnnn beats the prescribed
-- npnnn on BOTH readouts), proved for an interval of q containing the anchor.
import QOU.MassTheory.GroundStateOrderingRefutation
-- qou-prjo (PR: germ gauge covariance): the germ q-curvature F_q = [dq_i, dq_j]
-- is NOT gauge-covariant (connection law, concrete nonzero defect witness), so
-- the transverse NA-Stokes Omega_2 has no basis-independent value; the covariant
-- second-order object (the cup square) is identically a coboundary.
import QOU.MassTheory.GermConnectionGaugeCovariance
-- qou-prjo (doc-currency): PR #4848 / #4849's Lean files were never registered
-- here, so nothing built them. Both verify lean-direct exit 0.
import QOU.MassTheory.GermRootVectorGaugeFixing
import QOU.MassTheory.TransversePairingClusterDecomposition
-- qou-oc4v (§7c split, PR #5113): the depth-stratified FR module was split into
-- an algebraic half ({R : Type*} [Field R]) and an archimedean sibling holding
-- the empirical decimal variance records. Registering the sibling puts BOTH
-- under the build — it imports the algebraic module — so the split does not
-- grow the qou-orph orphan set (lean-orphan-gate). Verifies lean-direct ok=1.
import QOU.BraidKnot.DepthStratifiedFrobeniusReciprocityVariance
-- qou-e4ri (§7c adjudication, PR #5113): ψ_q's ℝ is legitimately archimedean
-- (its Λ_q summands are a Real.rpow weight; the cut-off `N m ≤ X` is an
-- ordering), now recorded in a §7c banner. Was orphaned from this root, so
-- nothing built it. Verifies lean-direct ok=1.
import QOU.AlgebraicSubstrate.QChebyshevFunction
-- qou-q7cm (§7c split): MassComputationChainRoadmap was never registered here,
-- so nothing built it. Registering it also pulls in QOU.TypedCrossingsEncoding
-- (the generic [Field A] theorem split out of it), since the roadmap imports
-- that module. Both verify lean-direct ok=1.
import QOU.MassComputationChainRoadmap
