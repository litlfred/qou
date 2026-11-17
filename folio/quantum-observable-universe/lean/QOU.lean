-- Quantum Observable Universe — Lean 4 Formalization
--
import QOU.AlgebraicSubstrate.QGenericBase
import QOU.AlgebraicSubstrate.QGenericBaseReal
import QOU.AlgebraicSubstrate.TwistSignTorsor
import QOU.BringsSurface.CoveringDegreeRamification
import QOU.Eightfold.AmbientInvolutionDoesNotDecideType
import QOU.Eightfold.CommutativeImageDegeneration
import QOU.Eightfold.ConnectedSumAnnihilator
import QOU.Eightfold.ContactDistributionRank
import QOU.Eightfold.HyperbolicVolumeFormType
import QOU.Eightfold.IndecomposableQuotientPrune
import QOU.Eightfold.SelfDualSectorConfinement
import QOU.Eightfold.OctonionicSu3RankObstruction
import QOU.Eightfold.FlavourColourDiscriminator
import QOU.Eightfold.ObstructionClassForcesComplexType
import QOU.Eightfold.ObstructionH2
import QOU.Eightfold.ObstructionH2Mathlib
import QOU.Eightfold.GaloisOrbitTransport
import QOU.Eightfold.IntertwinerFromGenerators
import QOU.Eightfold.PointwiseAgreementOnReduced
import QOU.Eightfold.GaugeAnsatzNesting
import QOU.Eightfold.PtolemyTwist
import QOU.Eightfold.SubgroupExtensionObstruction
-- This project formalizes the mathematical content of the QOU manuscript.
-- Each chapter has a corresponding Lean file.
--
-- Status tracking:
--   - Unproved goals are marked with placeholder tactics
--   - `proof-objects.json` in the repo root tracks formalization status
--   - LeanBlueprint macros in the LaTeX source link to declarations here

-- NOTE: Fred2005 has moved to folio/fred2005-formal-groups/lean/
-- import Fred2005

import QOU.Basic
import QOU.MathlibExt
import QOU.MathlibExt.QuadraticIrrationalBadlyApproximable
import QOU.MathlibExt.MarkovTrace
import QOU.MathlibExt.HeckeToTemperleyLieb
import QOU.MathlibExt.TraceRadicalNondegenerate
import QOU.MathlibExt.TemperleyLiebSpanning
import QOU.MathlibExt.TemperleyLiebWedderburn
import QOU.MathlibExt.TemperleyLiebNormalForm
import QOU.MathlibExt.TemperleyLiebClosure
import QOU.MathlibExt.TemperleyLiebWordBlocks
import QOU.MathlibExt.TemperleyLiebThresholdBridge
import QOU.MathlibExt.TemperleyLiebDeltaRule
import QOU.MathlibExt.MacdonaldTelescope
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
import QOU.MathlibExt.BraidedSlide
import QOU.MathlibExt.RightDualIsoUnique
import QOU.MathlibExt.Ribbon
import QOU.MathlibExt.RigidTensorDual
import QOU.MathlibExt.BraidedTensorDual
import QOU.MathlibExt.BraidedQuantumDimension
import QOU.MathlibExt.PivotalCategory
import QOU.MathlibExt.TwistedQuantumDimension
import QOU.MathlibExt.SphericalCategory
import QOU.MathlibExt.GramNondegenerate
import QOU.MathlibExt.GroupAlgebraCenter
import QOU.MathlibExt.RepresentationCharacter
import QOU.MathlibExt.QPlancherel
import QOU.MathlibExt.MonoidalCalcVar
import QOU.MathlibExt.QGaussianBinomialPascal
import QOU.MathlibExt.DerivationRankNullity
import QOU.MathlibExt.Dolbeault
import QOU.MathlibExt.OctonionDerivations
import QOU.MathlibExt.OctonionDerivationsBound
import QOU.MathlibExt.OctonionDerivationsUpperBound
import QOU.MathlibExt.OctonionDerivationProperties
import QOU.MathlibExt.OctonionSU3RankSix
import QOU.MathlibExt.OctonionSU3Stabilizer
import QOU.MathlibExt.OctonionSU3BracketClosure
import QOU.MathlibExt.OctonionColourActionBaseModule
import QOU.MathlibExt.OctonionComplexStructure
import QOU.QuantumObservableUniverse.CalculusDimensionObstruction
import QOU.QuantumObservableUniverse.SelfDualityDegree
import QOU.StandardModel.ColourStabilizerAction
import QOU.StandardModel.ColourBridge
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
-- `WedderburnConstruction` builds the block-diagonal embedding that
-- `QOU/HeckeAlgebra/Wedderburn.lean` had left `opaque`.  On the natural index
-- `Sigma lam, Fin (f^lam) x Fin (f^lam)` the assembly is an ordinary def and is
-- injective, with footprint [propext, Classical.choice, Quot.sound].  Only
-- landing in `Fin (n!)` needs the RSK identity, which is isolated there as the
-- explicit hypothesis `RSKDimIdentity` (bean qou-usol).  The `opaque` it
-- replaced was deleted on 2026-09-05 (bean qou-kp2z); nothing had consumed it.
import QOU.HeckeAlgebra.WedderburnConstruction
-- `WedderburnTrace` compares the two traces on that embedding: the regular one
-- weights each block by `f^lam` (`blockDiagonal_trace`), the Markov one by
-- `y_lam(q_0)`, and the difference is entirely in the coefficients.  Sharp: they
-- agree on every decomposition only if the coefficients agree (bean qou-kp2z).
import QOU.HeckeAlgebra.WedderburnTrace
-- `WedderburnUnconditional` discharges the RSK hypothesis outright from
-- `QOU.Mathlib.rskBurnsideHolds` (Schensted, axiom-clean), so
-- `wedderburnEmbedTotal` is injective with no axiom and no hypothesis at all.
-- It does NOT reclaim the name `wedderburnEmbed`: the bridge probe guards that
-- no reference to the retired opaque survives (bean qou-yos9).
import QOU.HeckeAlgebra.WedderburnUnconditional
-- `SeminormalDimSmall` computes f^lam at named partitions via the hook-length
-- formula -- (2,1) and (2,2) are 2, (1,1) is 1 -- which is what lets the
-- WedderburnTrace results be instantiated at (2,1) rather than left conditional
-- on a classical value the corpus had not written down (bean qou-v7ms).
import QOU.HeckeAlgebra.SeminormalDimSmall
import QOU.Glossary
import QOU.KZ.AssociatorKZ
import QOU.KZ.BlockResidues
import QOU.KZ.Drinfeld.Assoc
import QOU.KZ.Drinfeld.Braiding
import QOU.KZ.Drinfeld.Braided
import QOU.KZ.Drinfeld.Hexagon
import QOU.KZ.Drinfeld.Category
import QOU.KZ.Drinfeld.Duals
import QOU.KZ.Drinfeld.Admissible
import QOU.KZ.Drinfeld.Kron
import QOU.KZ.Drinfeld.Legs
import QOU.KZ.Drinfeld.Monoidal
import QOU.KZ.Drinfeld.Casimir
import QOU.KZ.Drinfeld.Natural
import QOU.KZ.Drinfeld.Pentagon
import QOU.KZ.Drinfeld.Reindex
import QOU.KZ.Drinfeld.Transport
import QOU.KZ.Drinfeld.Whisker
import QOU.KZ.Flat2D
import QOU.KZ.FuchsianAnalytic
import QOU.KZ.FuchsianConvergence
import QOU.KZ.FuchsianFormal
import QOU.KZ.FuchsianParam
import QOU.KZ.GLnKZ
import QOU.KZ.GLnResidues
import QOU.KZ.KZ4
import QOU.KZ.KZComplex
import QOU.KZ.KZCorner
import QOU.KZ.KZEdge
import QOU.KZ.DrinfeldAssociator
import QOU.KZ.KZFunctorial
import QOU.KZ.KZHalfMonodromy
import QOU.KZ.KZHexagon
import QOU.KZ.KZHexagonCentral
import QOU.KZ.KZIntertwine
import QOU.KZ.KZPentagon
import QOU.KZ.KZShift
import QOU.KZ.KZShiftPhi
import QOU.KZ.NonResonantInt
import QOU.KZ.SmallHbar
import QOU.KZ.ZigZag
import QOU.Knot.CuspShapeBarParity
import QOU.Knot.FigureEightDeformedMeridianWinding
import QOU.Knot.RademacherReversible
import QOU.Knot.M004AngleStructure
import QOU.Knot.L6a4AngleStructure
import QOU.Knot.FigureEightSelfDuality
import QOU.Knot.FigureEightVolume
import QOU.Knot.FigureEightVolumeLiterature
import QOU.Knot.NeumannZagierParity
import QOU.Knot.MortonFranksWilliams
import QOU.Knot.HomflySkeinReference
import QOU.Knot.FigureEightQuarticCoefficient
import QOU.Knot.PerNeutronLadder
import QOU.MathlibExt.IdealTriangulation
import QOU.MathlibExt.ManifoldVolumeBridge
import QOU.MathlibExt.ManifoldVolumePositive
import QOU.MathlibExt.BraidGroup
import QOU.Knot.FiveTwoVolumeConstant
import QOU.Knot.FiveTwoAngleSum
import QOU.Knot.FiveTwoNinthPower
import QOU.Knot.FiveTwoVolumeChord
import QOU.Knot.FiveTwoShapeBounds
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
import QOU.Knot.WhiteheadLowerRate
import QOU.KnotTheory
import QOU.KnotTheory.Brunnian
import QOU.KnotRegistry
import QOU.MassDerivation
-- Also brings QOU.Mass.ChainTraceFactor under the umbrella; nothing had
-- imported it, so it was invisible to blueprint/doc-gen import walks.
import QOU.Mass.IntraOrderingInvariance
import QOU.Mass.FreeEnergyReadingIsSigned
import QOU.MassTheory.MarginalRatioExtensivity
import QOU.MassTheory.BondFactorClassicalFloor
import QOU.MassTheory.TwoRowTwoColumnCollision
import QOU.MassTheory.TraceConventionGate
import QOU.MassTheory.NeutronProtonEMSign
import QOU.MassTheory.BarParityExclusion
import QOU.MassTheory.SU4SupermultipletGate
import QOU.MassTheory.BodyOrderCumulant
import QOU.MassTheory.CrossingCountAffine
import QOU.MassTheory.CoulombFromCrossingCounts
import QOU.MassTheory.BondChargeRule
import QOU.MassTheory.BondArcTheorems
import QOU.MassTheory.PairIsospinAssignment
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
import QOU.Mass.GroupoidTerminalDichotomy
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
import QOU.Mass.SWPeriodSuperExponential
import QOU.Mass.SumSYTEqInvolution
import QOU.Mathlib.YoungLatticeUpOperator
import QOU.Mathlib.SkewSYTMaxCorner
import QOU.Mathlib.SkewSYTBranchingBijection
import QOU.Mathlib.SkewBranchingSum
import QOU.Mathlib.SkewBranchingTwoOne
import QOU.Mass.WStdSuperExponential
import QOU.Mathlib.YoungLatticeExchange
import QOU.Mathlib.YoungLatticeCornerCount
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
-- 3D-realizability cap on max-contact coordination: a pairwise-equidistant family
-- has at most finrank members, so the complete contact graph K_A is realizable in
-- ℝ³ only for A ≤ 4. Replaces the EMPIRICAL premise ("saturation is observed")
-- that CoordinationSaturation's complete-graph exclusion rested on.
import QOU.Mass.EquidistantCoordinationCap
import QOU.Mass.StrandLayoutForcesChain
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
import QOU.SchurWeyl.PiBlockSeparation
import QOU.SchurWeyl.HeckeProductSurjective
import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.SpinSectorMeasure
import QOU.SchurWeyl.HeckeSemisimpleGeneral
import QOU.SchurWeyl.HeckeSemisimpleReal
import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.SchurWeyl.HeckeCarrierSemisimple
import QOU.SchurWeyl.HeckeCarrierSemisimpleReal
import QOU.SchurWeyl.GenericParameter
import QOU.SchurWeyl.GenericParameterReal
import QOU.SchurWeyl.HeckeWedderburnDataGeneral
import QOU.SchurWeyl.HeckeAlgebra
import QOU.OrientedSkein.HeckeCrossing
import QOU.OrientedSkein.SkeinDatum
import QOU.OrientedSkein.MarkovClosure
import QOU.OrientedSkein.BraidedClosure
import QOU.OrientedSkein.OS.Syntax
import QOU.OrientedSkein.OS.Category
import QOU.OrientedSkein.OS.Monoidal
import QOU.OrientedSkein.OS.Datum
import QOU.OrientedSkein.OS.Interpret
import QOU.OrientedSkein.OS.Universal
import QOU.OrientedSkein.OS.NonVacuity
import QOU.OrientedSkein.OS.Unique
import QOU.OrientedSkein.Model.GLnRMatrix
import QOU.OrientedSkein.Model.GLnTrace
import QOU.OrientedSkein.Model.GLnCrossCheck
import QOU.OrientedSkein.Model.GLnDatum
import QOU.OrientedSkein.Model.GLnLift
import QOU.OrientedSkein.Model.GLnClosure
import QOU.OrientedSkein.Model.GLnClosureLift
import QOU.OrientedSkein.Model.GLnFaithful
import QOU.OrientedSkein.Model.GLnOSFaithful
import QOU.SchurWeyl.HeckeCoset
import QOU.SchurWeyl.HeckeDim3
import QOU.SchurWeyl.HeckeDim3Dim
import QOU.SchurWeyl.HeckeDim3Indep
import QOU.SchurWeyl.HeckeInclusion
import QOU.SchurWeyl.HeckeMarkov3
import QOU.SchurWeyl.HeckeWedderburn3
import QOU.SchurWeyl.HoefsmitRep
import QOU.SchurWeyl.SeminormalParamAnchorReal
import QOU.SchurWeyl.HoefsmitRepGeneral
import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.ContentCasimir
import QOU.SchurWeyl.QJucysMurphyEigen
import QOU.SchurWeyl.SeminormalContentCasimir
import QOU.SchurWeyl.AxialDistanceBound
import QOU.SchurWeyl.MatRepEquiv
import QOU.SchurWeyl.SeminormalInequivalence
import QOU.SchurWeyl.OffDiagNonvanishing
import QOU.SchurWeyl.SeminormalRangeTop
import QOU.SchurWeyl.Irreducibility
import QOU.SchurWeyl.SytAdmissible
-- Umbrella gap found by the sibling PR #5282 (`claude/hoefsmit-finish-2026-08-18`):
-- the general-lambda tree sat OUTSIDE the umbrella's import closure, so nothing
-- type-checked it here.  HoefsmitRepGeneral pulls SeminormalRep -> TableauCells ->
-- SeminormalParam transitively; these three are not in that cone and need naming.
import QOU.SchurWeyl.Orbit3Braid
import QOU.SchurWeyl.Orbit6Braid
import QOU.SchurWeyl.HeckeWedderburnData3
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
import QOU.BraidsAndKnots.WignerSU4FromSpinIsospin
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
import QOU.Brings.HeckeMapFaceSize
import QOU.Brings.S5CharactersOnBringDeformations
import QOU.Brings.WignerTargetEquivariance
import QOU.Brings.BringConeLinkEulerNumber
import QOU.BringCone
import QOU.BringConeIcosahedral
import QOU.BringConeGauge
import QOU.BringConeSplitChirality
import QOU.BringLatticeSpan
import QOU.BringLatticeSpanFiniteQuotient
import QOU.StandardModel.Gen1QuarkRays
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
import QOU.Information.WeylCentre
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
import QOU.Archimedean.CatalanClausenBridge
import QOU.Archimedean.IdealTetrahedronConcavity
import QOU.Archimedean.LobachevskyDerivative
import QOU.Archimedean.IdealTetrahedronShapeBridge
import QOU.Archimedean.IdealTetrahedronVolumeConcavity
import QOU.Archimedean.LobachevskyMaximum
import QOU.Archimedean.LobMonotonicity
import QOU.Archimedean.BlochWignerNonneg
import QOU.Archimedean.BlochWignerPositive
import QOU.Archimedean.HyperbolicVolumeMeasure
import QOU.Archimedean.HyperbolicQuotient
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
import QOU.BraidKnot.SpechtWedderburnGeneral
import QOU.BraidKnot.CentralC2Transport
import QOU.BraidKnot.SpechtCentralC2Scalar
import QOU.BraidKnot.SnIsotypicSpechtSplitInstance
import QOU.BraidKnot.WedderburnUnconditional
import QOU.BraidKnot.ExplicitCentralIdempotent
import QOU.BraidKnot.ContentSqSumBridge
import QOU.BraidKnot.PlancherelSnDataGeneral
import QOU.BraidKnot.KeystoneDefectGeneral
import QOU.BraidKnot.KeystoneN5LevelSixSuffices
import QOU.BraidsAndKnots.SecondMomentKernelVanishes
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
import QOU.Braiding.MarkovTraceClassicalLimit
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
import QOU.Information.DimqRegularisationIdentities
import QOU.Information.EulerCharacteristicOfHochschild
import QOU.GrothendieckChern
import QOU.ParticleInteractions.atomic_lp_stability
import QOU.ParticleInteractions.silver_ratio_beta_decay_null
import QOU.ParticleInteractions.delta_pre_archimedean
import QOU.ParticleInteractions.even_tower_continuant_harmonics
import QOU.FluidDynamics.q_bkm_criterion
import QOU.FluidDynamics.TwoVortexChannelAlgebra
import QOU.FluidDynamics.LambCalculus
import QOU.FluidDynamics.LambCalculusArchimedean
import QOU.QBeta.BarOddLadderShape
-- Anchor-followups cluster (beans qou-o3ta / qou-4g4a): the interface scalar,
-- the Markov-Gram signature, and the Temperley-Lieb tower. Added to the root
-- import list 2026-08-09 -- all three were ORPHANS, compiling only when named
-- explicitly on the lake command line, so a plain `lake build` never checked
-- them and no CI run would have caught a regression in any of them.
import QOU.QBeta.InterfaceScalar
import QOU.QBeta.GramSignature
import QOU.QBeta.PairingSeesCommutator
import QOU.QBeta.GluonVertexPsdParity
import QOU.QBeta.TemperleyLiebTower
import QOU.QBeta.WedderburnTraceDecomposition
import QOU.QBeta.MarkovGramDegenerate
import QOU.QBeta.MarkovTraceQuotient
import QOU.QBeta.TLTowerRadicalDescent
import QOU.QBeta.TraceNondegeneracyInsufficient
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
import QOU.QBeta.DilogTheory
import QOU.Archimedean.BlochRigidity.Reflection
import QOU.QBeta.DilogTheoryArchimedean
import QOU.QBeta.ToddDilogExpansion
import QOU.QBeta.BarEvenJet
import QOU.QBeta.BarEvenJetArchimedean
import QOU.QBeta.FaddeevCompactCurve
import QOU.Archimedean.IdealTetVolumeRigidity
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
import QOU.QBeta.LadderPhaseMirrorCovariance
import QOU.QBeta.RadicalPairingIsSignRep
import QOU.QBeta.LadderRungAmplification
import QOU.QBeta.QBetaZeta4ResidueRefutation
import QOU.QBeta.BarParityZeta4Swap
import QOU.QBeta.CuspShapeBarParity
import QOU.QBeta.ArgUPhaseBranchSelection
import QOU.QBeta.CAL3AnchorStructure
import QOU.QBeta.SRigidityPrune
import QOU.QBeta.HolonomySpectrumSignObstruction
import QOU.QBeta.ImQCannotSupplyEllipticGenerator
import QOU.QBeta.BringEllipticCurveJInvariant
import QOU.QBeta.JetTowerBlindToDecay
import QOU.QBeta.TraceRealSpectrumComplex
import QOU.QBeta.TracelessDifferenceEllipticity
import QOU.QBeta.DiscriminantCurveInQ
import QOU.QBeta.TraceBlindSector
import QOU.QBeta.BondDecayRates
import QOU.QBeta.EigenphaseCarrierClassicalLimit
import QOU.QBeta.MonodromyTraceInvariance
import QOU.QBeta.CosineParametrisationUnfalsifiable
import QOU.QBeta.DecayFunctionalUnification
import QOU.QBeta.DeltaSTwoRowCharacterVanishes
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
-- A=3 amplitude bar-odd/unit-modulus Pythagorean bridge: the carrier E=χ(P) is √−1
-- (bar-odd σE=−E + unit-modulus E·σE=1 ⇒ E²=−1), so the affine lift's modulus is a
-- quadrature fs²+s²; resolves the "real E vs unit phase" type tension, relocates the
-- magnitude datum to the transverse slope s (qou-prjo). Conditional §3b, no instance.
import QOU.QBeta.BirkhoffBarOddPythagorasBridge
-- A=3 branching ↔ modulus-bridge composition: the branching reduction 1−x², the transverse
-- leg 2x, and the lift 1+x² form a Pythagorean triple (lift = 2 − factor_sa); the branching's
-- own x is too small to supply r*=1.585 (scope-(a) negative — s is genuinely transverse).
import QOU.QBeta.A3BranchingModulusReflection
-- qou-prjo: canonical discretization of the Yekutieli surface 2-form on the trefoil (genus-1)
-- Seifert surface — ∑ V_ij ⁅A_i,A_j⁆; only the skew (intersection) part of the Seifert form
-- survives, so the trefoil term = a single germ q-curvature ⁅A_a,A_b⁆, zero iff the handles
-- commute (abelian H₂ ⇒ 0; nonzero only at the non-commutative germ/interface level).
import QOU.QBeta.YekutieliTrefoilDiscretization
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
import QOU.Machinery.QuantumTorusQDifference
import QOU.Machinery.QuantumTorusAJ
import QOU.Machinery.QuantumTorusDivision
import QOU.Machinery.QuantumTorusSymbol
import QOU.Machinery.StrongAJFigureEight
import QOU.Machinery.AJTorusAnnihilation
import QOU.Machinery.AJMinimality
import QOU.MathlibExt.EndSemisimple
import QOU.HyperellipticQuintic.zeta5_residue_monodromy

import QOU.Archimedean.BorromeanQuark
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.BringZeroModeClausenWitness
import QOU.Archimedean.ArchimedeanLimitDomain
import QOU.Archimedean.BlochSuslinComplex
import QOU.Archimedean.BlochWignerFiveTermInstance
import QOU.Archimedean.BlochRigidity.Algebra
import QOU.Archimedean.BlochRigidity.Abstract
import QOU.Archimedean.BlochRigidity.ComplexAlgebra
import QOU.Archimedean.BlochRigidity.Derivative
import QOU.Archimedean.BlochRigidity.Growth
import QOU.Archimedean.BlochRigidity.Holomorphic
import QOU.Archimedean.BlochRigidity.Instance
import QOU.Archimedean.BlochRigidity.IntegrationBridge
import QOU.Archimedean.BlochRigidity.LinearSections
import QOU.Archimedean.BlochRigidity.ReebPlane
import QOU.Archimedean.BlochRigidity.Regularity
import QOU.Archimedean.BlochRigidity.Rigidity
import QOU.Archimedean.BlochRigidity.Smooth
import QOU.Archimedean.BlochRigidity.Vanishing
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
import QOU.Archimedean.GramDetRatioCongruence
import QOU.Archimedean.SchwingerMeasureShape
import QOU.Molecular.KnotConvolutedTensor
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
-- RSK inverse, brick 9: the row-level RIGHT inverse (redoing an undoing).
import QOU.Mathlib.SchenstedRowRightInverse
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
-- RSK inverse, brick 10: the cascade-level RIGHT inverse (non-deleting branch).
import QOU.Mathlib.SchenstedCascadeRightInverse
-- RSK inverse, brick 11: what the reverse cascade preserves (and what needs a corner).
import QOU.Mathlib.SchenstedUninsertInvariants
-- RSK inverse, brick 12a: where reverse row insertion writes (the reverse of rowInsert_bump_eq_set).
import QOU.Mathlib.SchenstedReverseRowIndex
-- RSK inverse, brick 13: the reverse cascade keeps columns strict, at a corner.
import QOU.Mathlib.SchenstedCascadeColStrict
-- RSK inverse, brick 14: the recovered word rebuilds the tableau (word-level surjectivity).
import QOU.Mathlib.SchenstedWordSurjectivity
-- RSK inverse, brick 15: insertion always creates a corner; brick 14's hypotheses are satisfiable.
import QOU.Mathlib.SchenstedCornersAlong
-- RSK inverse, brick 16: a row holding a maximum entry is a corner (the Q-side keystone).
import QOU.Mathlib.SchenstedMaxCorner
-- RSK inverse, brick 18: CornersAlong reduces to a condition on shapes alone.
import QOU.Mathlib.SchenstedShapeRun
-- RSK inverse, brick 20: addable-cell sequences peel back as corners.
import QOU.Mathlib.SchenstedAddable
-- RSK inverse, brick 23: the counting bridge from column-strictness.
import QOU.Mathlib.SchenstedStandardCount
import QOU.Mathlib.SchenstedReinsertRow
import QOU.Mathlib.SchenstedRecordingTrunc
import QOU.Mathlib.SchenstedRSKSurjective
import QOU.Mathlib.SchenstedListOfSYT
import QOU.Mathlib.SchenstedRecordingOfSYT
import QOU.Mathlib.SchenstedSYTRoundTrip
import QOU.Mathlib.SchenstedWordOfPermSurj
import QOU.Mathlib.SchenstedShapeOfPositions
import QOU.Mathlib.SchenstedRSKPairSurjective
import QOU.Mathlib.SchenstedRSKPairInjective
import QOU.Mathlib.SchenstedRSKEquiv
import QOU.Mathlib.SchenstedPartitionShape
import QOU.Mathlib.SchenstedRSKBurnside
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
-- Bean qou-wtny (SW-3): addable cells, and #addable = #removable + 1 -- the
-- diagonal of DU - UD = I on the Young lattice. One input to the remaining
-- `hup` hypothesis of QOU.Mathlib.BurnsideViaBranching.
import QOU.Mathlib.YoungDiagramAddable
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

-- ═══ qou-glnl / qou-glhi / qou-fr7j — the gluing-equation lane ═══
-- Every module of this lane was ORPHANED until now: nothing imported them, so
-- `lake build` (whose default target is `QOU` plus its transitive import closure)
-- never compiled them and no gate would have noticed them breaking.  Caught by
-- `lean-orphan-audit.ts --diff`, which exits 1 on all eleven.  Each was verified
-- per-module by name during development, which is exactly the check that hides
-- this defect: naming a module builds it whether or not anything imports it.
import QOU.Knot.GluingBridge
import QOU.Knot.SixOneCertified
import QOU.Knot.GeneratedCusp
import QOU.Knot.GeneratedCertified
import QOU.Knot.GeneratedGluingHigh
import QOU.Knot.GeneratedCertifiedHigh
-- ═══ qou-hypr / qou-bday — the surreal birthday lane ═══
-- Same defect, same cause.  DiophantineBirthday itself was already in the tree and
-- also orphaned, so registering it here is a fix to pre-existing state rather than
-- to this arc's additions.
import QOU.AppendixSurreals.BirthdayFaithful
import QOU.AppendixSurreals.DiophantineBirthday
import QOU.AppendixSurreals.DiophantineBirthdayScope
import QOU.AppendixSurreals.DiophantineBirthdayTrajectory
import QOU.AppendixSurreals.GonshorConvergence
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
-- qou-br3w — staged for upstream Mathlib: the index of a multivariate polynomial at a
-- point, the first missing Thue-Siegel-Roth prerequisite.  Depends on nothing from QOU
-- (Mathlib imports only), so it lifts out verbatim when a Mathlib PR is possible; it is
-- registered here so the orphan gate covers it in the meantime.
import QOU.Mathlib.RothIndex
-- qou-br3w — staged for upstream Mathlib: generalized (m x m) Wronskians.  Mathlib has the
-- two-polynomial case only; genWronskian_two pins the generalisation to it.
import QOU.Mathlib.GenWronskian
-- qou-br3w — staged for upstream Mathlib: the same in SEVERAL variables, which is what
-- Roth's lemma actually consumes (its auxiliary polynomial is multivariate).  The operator
-- family is an explicit parameter because in several variables there is no canonical row.
import QOU.Mathlib.MvGenWronskian
-- qou-sq3h -- staged for upstream Mathlib: restriction of a multivariate polynomial to a
-- line, with the chain rule d/dt f(a+tc) = (D^c f)(a+tc).  The bridge for the generic-line
-- route to BOUNDED-ORDER generalized Wronskians, which MvGenWronskian's converse cannot
-- reach (it argues from the origin, and bounded-order Wronskians can vanish there).
import QOU.Mathlib.LineRestriction
-- qou-sq3h -- staged for upstream Mathlib: the directional generalized Wronskian
-- det((D^c)^i f_j), whose rows carry order 0..m-1 by construction, and its equivalence with
-- independence of line restrictions.  Reduces the bounded-order problem to a question about
-- the DIRECTION alone; the base point drops out.
import QOU.Mathlib.DirectionalWronskian
-- qou-sq3h -- staged for upstream Mathlib: the BOUNDED-ORDER generalized Wronskian
-- criterion, the form Roth's lemma consumes, proved at m = 2 (operator family (id, d_k),
-- orders 0 and 1).  Mirrors the univariate m = 2 converse, with totalDegree for natDegree
-- and IsRelPrime for Bezout coprimality.
import QOU.Mathlib.BoundedOrderWronskian
-- qou-4lbh -- staged for upstream Mathlib: Wronskians of SEPARATED polynomials.  For
-- P = sum_k phi_k(x) psi_k(y) with the variable groups disjoint, the mixed generalized
-- Wronskian factors into an x-Wronskian times a y-Wronskian -- the engine of Roth's lemma's
-- induction on the number of variables.
import QOU.Mathlib.SeparatedWronskian
-- qou-4lbh -- staged for upstream Mathlib: the m = 1 height bound for Roth's lemma.
-- Elementary: lead((qX-p)^k) = q^k and a divisor's leading coefficient divides, so
-- q^k <= |lead P|.  Corrects the recorded assessment that the base case needed Mahler
-- measure -- that is required for bounding heights of FACTORS in the induction step, which
-- goes the other way.
import QOU.Mathlib.RothHeightBound
-- qou-4lbh -- staged for upstream Mathlib: M(X - a) = max(1, |a|), Jensen's formula for a
-- single root, connecting Mathlib's circleAverage_log_norm_sub_const_eq_posLog to
-- mahlerMeasure.  Cornerstone of the Jensen form, and the measurement that reversed this
-- arc's recommendation from "bare-hands Gelfond" to "fill the bridge upstream".
import QOU.Mathlib.MahlerJensen
-- Heights of a disjoint-variable product.  For separated variables the coefficients of a
-- product ARE the products of the coefficients, so the height is exactly multiplicative —
-- which makes the height half of Roth's induction step elementary rather than a Gelfond
-- application, correcting bean qou-4lbh's third prediction of where the cost sits.
import QOU.Mathlib.SeparatedHeight
-- Heights of products and determinants of multivariate polynomials over ℤ.  A product
-- costs a factor of the SUPPORT SIZE, not only the heights, and the determinant bound
-- m!·(S·B)^m is what turns a height bound on an auxiliary polynomial into one on its
-- generalized Wronskian.  All of it is the easy direction; Gelfond is the other one.
import QOU.Mathlib.MvPolynomialHeight
-- The height of a generalized Wronskian, composed end to end:
--   H(mvGenWronskian D f) ≤ m!·(S·(d^L·B))^m.
-- Not Mathlib-only: it needs mvGenWronskian.  Its two dependencies are, so the three
-- lift together.
import QOU.Mathlib.WronskianHeight
-- The index across a disjoint-variable product: index (U(x)·V(y)) = index U + index V,
-- exactly.  The index analogue of SeparatedHeight, and what Roth's induction on the
-- number of variables splits on.  The ≤ direction is the half that needs IsDomain.
import QOU.Mathlib.SeparatedIndex
-- The m = 1 case of Roth's lemma stated against `index`, which is what the induction
-- consumes.  RothHeightBound proved the corresponding statement about Taylor
-- coefficients; nothing connected the two, because index lives on MvPolynomial and the
-- height bound on Polynomial.  This module is that connection.
import QOU.Mathlib.RothBaseCase
-- The index of a generalized Wronskian, composed end to end:
--   ∑ᵢ index (f i) ≤ index (mvGenWronskian D f) + m·C.
-- The index counterpart of WronskianHeight.  index_det_ge alone does NOT give this —
-- it bounds a determinant by its entries, not by the f.
import QOU.Mathlib.WronskianIndex
-- The interface of Roth's induction step, composed and CHECKED in Lean rather than
-- asserted in prose: the separated Wronskian's index splits exactly, and each factor's
-- height is bounded by the whole's.  Both compositions are one-liners — which is the
-- point: if the claimed interface were wrong they would not typecheck.
import QOU.Mathlib.RothInductionStep
-- The STATEMENT of Roth's lemma (a def, not a theorem — only m = 1 is proved), plus the
-- m = 1 case.  Settles the indexing question: keep the variable type general and carry
-- the ordering as an Equiv σ (Fin m), so the base case lands at Unit with no transport.
import QOU.Mathlib.RothLemmaStatement
-- Separated representations: every polynomial in two variable groups is a finite sum
-- ∑ₖ φₖ(x)·ψₖ(y).  The audit against the statement found this missing — every piece of
-- the separated machinery TAKES such a representation and nothing produced one.
import QOU.Mathlib.SeparatedRepresentation
-- The arithmetic core of Roth's-lemma recursion: Mahler §13's case split, isolated from
-- the polynomial content.  The induction step is NOT linear — it extracts a square-root
-- bound — which is what the arc's linear form was missing.
import QOU.Mathlib.RothRecursionArith
-- §13's operator family, CONSTRUCTED: row μ contributes a fixed list, column ν contributes
-- ν copies of the distinguished variable, so the cost is uniform in the row and grows in the
-- column — exactly what sum_max_le_index_det's permutation step needs.  This closes the COST
-- half of the recursion's missing input; the determinant's non-vanishing is still open.
import QOU.Mathlib.RothOperatorFamily
-- The variable split σ ≃ Fin n ⊕ Unit induced by an ordering σ ≃ Fin (n+1), and the transport
-- of index, RothGrowth and degreeOf across it.  Connects Roth's lemma's STATEMENT (one degree
-- vector, one ordering) to the split form every operator-family result is written for.
import QOU.Mathlib.RothVariableSplit
import QOU.Mathlib.RothRealLadder
import QOU.Mathlib.RothGammaProducer
import QOU.Mathlib.RothAuxiliaryPolynomial
import QOU.Mathlib.RothHouseBound
import QOU.Mathlib.RothAuxiliaryConstruction
import QOU.Mathlib.RothAuxiliary
-- Roth's theorem step 2, arithmetic half: a translated coefficient at a rational
-- point has denominator dividing prod q_h^{r_h}, so any bound below its reciprocal
-- forces it to vanish -- which is a lower bound on the index there, the statement
-- Roth's Lemma (step 3) contradicts.  The analytic half (Taylor expansion about
-- alpha) is deliberately left as a hypothesis; see the module header.
import QOU.Mathlib.RothRationalIndex
-- The two facts step 2's smallness hypothesis is built from: Taylor's theorem in
-- the form Roth needs (translating by alpha then gamma is translating by alpha+gamma,
-- so the index at alpha deletes the low-weight terms of the expansion at alpha+gamma),
-- and a translateMatrix bound that TRACKS the power of gamma the entry carries.
-- RothAuxiliaryPolynomial's (2B)^{|n|} is the wrong shape here: step 2's whole content
-- is that gamma = beta - alpha is tiny, and that bound throws it away.
import QOU.Mathlib.RothTaylorBound
-- Produces the constant S the Taylor bound was left waiting on, and closes step 2.
-- Two weightings meet here: the index gap is weighted by 1/r_h, the sizes by log q_h,
-- and r_h * T_h >= K is exactly what converts one into the other.  That is Roth's
-- normalisation r_h log q_h ~ L in the only form the estimate needs -- the same fact
-- RothGammaProducer discharges for Gamma_m's growth clause.
import QOU.Mathlib.RothIndexGap
-- Step 4: steps 2 and 3 collide.  Both bound the SAME number -- the index of the
-- auxiliary polynomial at the rational point -- one from below, one from above, and
-- Roth's theorem is that for the right parameters they cannot both hold.  Nothing was
-- mathematically missing; what was missing is that the two had never been written in
-- one place, so nothing forced their interfaces to agree (algebraMap vs Int.castRingHom,
-- and Gamma_m's p,q against the numerators and denominators of the approximations, which
-- are unrelated despite the shared letters).
import QOU.Mathlib.RothContradiction
-- The two-sided normalisation step 4's inequality needs -- and the finding that
-- rothDegrees already satisfies it.  r_h = log_{H_h} N puts r_h log H_h within
-- log H_h of log N on BOTH sides, so Gamma_m's growth clause (which consumes the
-- lower half) and step 4's inequality (which needs both) were never using different
-- normalisations.  The worry that opened qou-ujl8 was unfounded; recording that they
-- coincide is the fix, not a record reconciling them.
import QOU.Mathlib.RothNormalisation
-- O_K's replacement for "a non-zero integer has absolute value at least one".
-- Over Z smallness at the one place forces vanishing; over O_K it does not -- an
-- algebraic integer can be tiny at one place and enormous elsewhere with |N(x)| >= 1
-- intact.  Vanishing needs smallness at phi_0 AND a bound at every other conjugate,
-- so the O_K case has an input the Z case does not.  Not a generalisation: a
-- different theorem with different hypotheses.
import QOU.Mathlib.RothAlgebraicInteger
-- Step 2 over O_K, assembled: the Taylor bound at phi_0 and the height budget at
-- the other d-1 conjugates meet the vanishing criterion.  The two enter the final
-- inequality DIFFERENTLY -- phi_0 linearly, the conjugate bound raised to the d-1 --
-- so slack in conjBound costs d-1 times as much, which is why it is named.  Over Z
-- the asymmetry vanishes because d = 1; that is a fact about the shape, not a route
-- from one vanishing criterion to the other.
import QOU.Mathlib.RothAssembly
-- ROUTE A: the auxiliary polynomial over Z, so that step 1 can reach step 3 at all.
-- RothAuxiliary builds it over O_K (that is what Mathlib's number-field Siegel lemma
-- produces) while Roth's Lemma requires MvPolynomial sigma Z through InRothPolySet, so
-- those two never composed.  The join is made here on the Z side, which is cheaper:
-- Siegel over Z is in Mathlib and everything from step 2 onward already works over Z.
-- One O_K-linear vanishing condition is finrank Q K integer ones, so deg(alpha) comes
-- back into the count and "take m large" becomes m > deg(alpha)/(4 eps^2).
import QOU.Mathlib.RothAuxiliaryInt
-- THE CHAIN CLOSES: steps 1 -> 2 -> 3 -> 4 with the coefficient rings agreeing.
-- Two pieces of glue, both small enough to be invisible and large enough to be wrong:
-- Siegel states its height bound over R while InRothPolySet wants an integer, so the
-- ceiling is taken (the only direction that is a consequence rather than an assertion);
-- and step 1 proves the index over K while step 2 consumes it over R, so it transports
-- along a real embedding -- which is a real hypothesis, being the statement that the
-- alpha_h are REAL algebraic numbers, and the composition refuses to typecheck without one.
import QOU.Mathlib.RothIntegerChain
-- THE PARAMETER SELECTION -- the one piece of the arc that CONSTRUCTS data rather
-- than composing supplied hypotheses, and the only place the "infinitely many
-- solutions" assumption is consumed.  Greedy recursion: pick a denominator past a
-- threshold, raise it to a power, pick another past THAT.  The max against a floor is
-- load-bearing -- without it a later height could land below the floor and Gamma_m's
-- two_le would fail on every index but the first.  At floor 2^F it discharges clause 3
-- as well, which is the clause that bites hardest (m = 2 needed H = 1024 for it).
import QOU.Mathlib.RothSelection
-- The two size estimates hbound's non-circularity rests on, and which RothSelection
-- could only state: #box <= 2^{sum r_h} and ||auxMatrixInt|| <= c(K) (2B)^{sum r_h}.
-- Both constants are inert in r, so log b is LINEAR in sum r_h -- which is what lets
-- the log N on the two sides of b^{mq} <= H_0^{r_0 p} cancel.  The coordinate-vs-house
-- comparison is Mathlib's basis_repr_norm_le_const_mul_house, so the arc assumes nothing.
import QOU.Mathlib.RothSiegelBound
-- The exchange between the two currencies the chain is stated in.  The selection produces
-- heights and a threshold N; roth_contradiction_of_normalisation consumes real constants
-- cH, theta, L' and one inequality.  Every conversion turns out to be a FLOOR on the heights
-- or a POWER of them below N -- exactly the selection's own parameters.  The normalisation
-- slack eta is 1/k from (H h)^k <= N, and height_le_mul_den is what makes a floor on the
-- heights serve as a floor on the DENOMINATORS, which is what hpt actually constrains.
import QOU.Mathlib.RothFinalAssembly
-- Multivariate content over ℤ and the primitive part — Mathlib has Polynomial.content and
-- IsPrimitive for ONE variable only.  Half of Mahler §6's Gauss step, which is what lets the
-- induction hypothesis (about INTEGER polynomials) reach the factors of a minimum separated
-- representation (which lives over ℚ, because shortening divides by a coefficient).
import QOU.Mathlib.SeparatedGauss
-- Applying the induction hypothesis to the x-factor: §6's Gauss makes the rational Wronskian
-- integral, RothLemmaUniform at m−1 applies to THAT, and index_C_mul carries the bound back
-- because the scaling does not move the index.  Discharges the x half of RothOperatorFamily's
-- `hres`.
import QOU.Mathlib.RothInductionHypothesis
import QOU.Mathlib.KazhdanLusztigBasis
import QOU.Mathlib.ConcentratedColumnCollapse
import QOU.Mathlib.StandardYoungCountInstance

-- The p-n interface bar structure, in three files.  `ClosedFormInterfaceFactors`
-- carries the convention-D factors f_pp = z, f_nn = z - h, f_pn and their q-bar
-- behaviour in the square-root variable; `PnInterfaceBarStructure` proves the
-- criterion (the weighted p-n factor is bar-even iff the offset is bar-odd);
-- `PnOffsetBarOddClass` measures what that criterion does and does not select.
-- All three were orphans -- outside QOU.lean's import closure, so invisible to
-- blueprint, doc-gen and every dependency walk, though still compiled by the
-- lakefile glob.  The first two predate this commit (bean qou-kljb).
import QOU.Hecke.ClosedFormInterfaceFactors
import QOU.Hecke.RowCap
import QOU.Hecke.CrossingConvexity
import QOU.Hecke.BindingExtensivity
import QOU.Hecke.LayoutConflict
-- `ContiguousCouplingGraph` asks `LayoutConflict`'s neighbouring question — not
-- how many couplings ONE interface admits, but which nucleon PAIRS a contiguous
-- `3A` layout can couple at all.  The answer is the path `P_A`: a generator
-- crosses two adjacent strands and blocks are three wide, so only consecutive
-- nucleons are reachable.  The binding producer needs the complete graph `K_A`
-- (one inter-nucleon letter per pair), so its word re-embeds on `3A` strands
-- only at `A <= 2`.  Bean `qou-w6x3`; measurement in
-- `computations/probes/binding_word_3A_reembedding_probe.py`.
import QOU.Hecke.ContiguousCouplingGraph
-- `GeometricTailBound` answers "why only the leading order?" for the flavour
-- split: `(1 + h_q^3)` is the first two terms of `1/(1 - h_q^3)`, and summing
-- the whole tail moves the value by `x^2/(1-x)` -- 323x smaller than the gap it
-- would have to close.  Pure ordered-field algebra; the measurement enters only
-- as the hypothesis `K > 1`.
import QOU.Hecke.GeometricTailBound
-- `BoundedDegreeCoulomb` generalises the chain result: by the degree-sum
-- formula a graph with max degree `d` has at most `dn/2` edges, so its share of
-- the `n(n-1)/2` pairs is at most `d/(n-1)`.  Coulomb is quadratic in Z; every
-- edge set the corpus has built (chain d=2, max-contact deltahedra d=5, close
-- packing d=12) is degree-bounded, so none of them can carry it.
import QOU.Hecke.BoundedDegreeCoulomb
-- `SymmetrySignAmGm`: a bond sum is additive in `L = -log b`, so its symmetry
-- term compares `b_pn` against the GEOMETRIC mean of `b_pp`, `b_nn` -- while the
-- construction delivers an ARITHMETIC (convex) one.  AM >= GM, so the sign is
-- backwards structurally.  The crossing weight is `1/(q^2+1)`, which is `1/2`
-- only at `q = 1`; the corpus sits at `1/2 + delta_flavour/4`, 11.7 % above it.
import QOU.Hecke.SymmetrySignAmGm
-- `ChannelRangeGrowthClass`: adding a bond MULTIPLIES the trace by `b < 1`, so
-- the native falloff is `b^d(i,j) = exp(-mu.d(i,j))` -- Yukawa in graph
-- distance.  That puts weak / strong / EM on one axis (the mediator mass) and
-- separates them by GROWTH CLASS: every `mu > 0` gives an extensive pair sum,
-- only `mu = 0` gives `Theta(n^2)`.  Also `L_pp + L_nn = 2 log [2]_q`, so the
-- three rates carry one constraint and one free parameter.
import QOU.Hecke.ChannelRangeGrowthClass
-- `BarWeightFamily`: bar invariance of the p-n interface reduces to
-- `wbar = 1 - w`, ONE equation -- and the family `w_k = q^-k/[2]_{q^k}` meets it
-- for every `k`.  The corpus's averaging rule is the `k = 0` member, pinned only
-- by the unstated assumption that `w` carries no `q`.  `w_1` is the geometric
-- mean (zero symmetry term); `k > 1` is the SEMF-signed region.
import QOU.Hecke.BarWeightFamily
-- `SelfConjugateRowCap`: self-conjugacy forces `ell(lambda) = lambda_1`, so the
-- fibre-dimension cap `ell <= 2` leaves exactly THREE self-conjugate shapes --
-- (1), (2,1), (2,2), all of size <= 4, and none at any level >= 5.  Relevant
-- because `mass-theory`'s Wigner energy `-Delta_W . T(T+1)/A` is built from
-- self-conjugate shadow prices at k = 4 and k = 5.
import QOU.Hecke.SelfConjugateRowCap
-- `IsospinClassSingleton`: `mass-coefficient-shadow-price-proof`'s own rule makes
-- `c(lambda) = 0` the ISOSPIN-type scaling class.  At the quartet level `n = 4`
-- that class has exactly ONE member, `(2,2)` -- so the Wigner coefficient is
-- selected rather than drawn from a menu, which is the one row of
-- `mass-formula-regime-switching-table1-data` its fit-shape QA note does not bite.
import QOU.Hecke.IsospinClassSingleton
import QOU.MassTheory.PnInterfaceBarStructure
import QOU.MassTheory.PnOffsetBarOddClass

-- The two modules created to break the cross-sibling blocker (bean qou-lsib,
-- PR #5505): content-block `.lean` siblings live outside the package globs, so
-- they cannot import one another, and six particle files were each re-declaring
-- the same structures while `positron-knot` could not reach `Electron` at all.
-- Moving the shared declarations into the library tree fixed that -- but the
-- tree is not the build.  Nothing inside QOU.lean's closure imports either
-- module, so `lake build QOU` never compiled them and they sat in the qou-orph
-- orphan population (986 of 2257 modules); their only type-check was the
-- lean-direct run in that PR.  Wiring them here is the other half of the fix.
import QOU.AlgebraicSubstrate.LocalQZetaFunction
import QOU.AlgebraicSubstrate.WignerAxiom
import QOU.Archimedean.ParticleKnots

-- Same fix, same reason, a third module (bean qou-aemx follow-on).
-- `QOU/Observations/centered_hecke_variance_positive.lean` is the canonical
-- declaration for `prop:centered-hecke-variance-positive`, and nothing imported
-- it, so `lake build QOU` never compiled it.  Its block's `.md` was corrected
-- from convention C to convention D on 2026-08-09 -- withdrawing the figure
-- `Var ≈ 0.855` -- and the Lean sibling was not: it kept the C parameter, the
-- withdrawn number, and a pair of positivity axioms that under D hold only on
-- `q ∈ (1, ψ)`.  Nineteen days of drift that a compile would not have caught
-- either, since the old file type-checked fine; but an uncompiled module is one
-- nobody has reason to open.  Wiring it in at least puts it in the build.
import QOU.Observations.centered_hecke_variance_positive

-- Hook-sum / balanced-twist cluster (bean qou-si7d). Four modules that nothing
-- imported, so nothing that WALKS imports -- blueprint, doc-gen, dependency
-- analysis, an import cone rooted at `QOU` -- could see them. They were still
-- compiled: `globs = ["QOU", "QOU.+"]` (bean qou-rc7b) covers the whole tree,
-- and qou-kljb closed on exactly that finding. So this buys visibility, not
-- coverage; do not cite it as the latter.
--
-- `TwistUnconditional` is the one that matters. It discharges a previously
-- HYPOTHESISED hook-sum exponent in the balanced-quantum-twist result using
-- `HookSumComplete.hookSum_eq` -- a real theorem consuming a real dependency,
-- invisible to every import-walking tool until now. Importing it also reaches
-- `QOU.Common.BalancedQuantumTwist`, which nothing else imported either.
--
-- `HookSumGeneral` (the arm half, predecessor of `HookSumComplete`) and
-- `HookSumIdentity` (`decide`-checked small shapes) are kept rather than
-- deleted: the `decide` cases are a cheap INDEPENDENT check of an identity now
-- proved twice in general -- once over `List ℕ` and once over `YoungDiagram`
-- (`QOU.BraidKnot.HookSum`), with `HookSumRegisterBridge` proving the two equal.
--
-- All four verified to compile standalone before wiring (`lean` direct, EXIT=0).
import QOU.Common.TwistUnconditional
import QOU.Common.HookSumGeneral
import QOU.Common.HookSumIdentity
import QOU.Hecke.H2KaehlerDegrees
import QOU.Mass.FormalityBridgeF1
import QOU.MathlibExt.InterleavedWordClosures
import QOU.MathlibExt.UniversalDifferentials
import QOU.Mass.CrossTermFixedPointCount
import QOU.LiftingDescent.CrossedModuleSurfaceHolonomy
import QOU.Mass.CrossTermOrderZeroComponentCount
import QOU.Mass.HeckeQuadraticClassicalShadow
import QOU.Mass.KZUnitModulusPrune
import QOU.Mass.HeckeMonodromy
import QOU.Mass.BraidedStrands
import QOU.Mass.ColourCubicDiscriminant
import QOU.Mass.ColourCubicDiscriminantReal
import QOU.Mass.FigureEightGluingFromMonodromy
import QOU.Mass.FiveTwoGluingFromFareyWord
import QOU.Mass.AffineCumulantSecondDifference
import QOU.Mass.FiveTwoAPolynomialFromFareyWord
import QOU.QBeta.FloorRemainderFromDerivedShapeFields
import QOU.QBeta.PretzelRemainderFromPtolemy
import QOU.Archimedean.VolumeTranscendental
import QOU.MassTheory.BlockMeasureFromFrobeniusPairing
import QOU.MassTheory.BranchingPushforwardMultiplicativity
import QOU.MassTheory.BlockMeasureBindingFormArchimedean
import QOU.MassTheory.InterfaceLetterCrossingMixture
import QOU.MassTheory.CompositionFeasibilityProgram
import QOU.MassTheory.RelativeReebDatum
import QOU.MassTheory.SegmentCollisionDatum
import QOU.MassTheory.ConvolutionFlowParity
import QOU.MassTheory.ConvolutionFlowFibre
import QOU.MassTheory.BringResidueEnergy
import QOU.MassTheory.DeuteronKappaThreeSixteenthsReconciliation
import QOU.Brings.BringConjugationChirality
import QOU.Brings.BringCoverTower
import QOU.Brings.BringDescendingTower
import QOU.Brings.BringUTContactChirality
import QOU.Mass.YangMillsVacuumFlat
import QOU.Mass.InfinitesimalPureBraid
import QOU.Mass.LagrangianKZIdentification
import QOU.Mass.KZPullbackHypothesis
import QOU.Mass.KohnoTwoPoint
import QOU.KZ.Drinfeld.HeckeStrands
import QOU.Mass.LagrangianKZInputs
import QOU.Mass.BridgeADeligneGauge
import QOU.Mass.BridgeADeligneKZ
import QOU.QBeta.BorromeanThreeCuspNZHessian
import QOU.QBeta.McPhailSnyderBridgeExclusion
import QOU.QBeta.MagnitudeAssemblyAndConventionFrameBrick
