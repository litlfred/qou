import BraidKnotOctonion.PieceAGeneral
-- The linear hook sum `Σ_c h(c) = Σ_i C(λ_i,2) + Σ_j C(λ'_j,2) + n`, equivalently
-- `2 Σ_c h(c) = p₂(λ) + p₂(λ')`. Built on PieceAGeneral's arm/leg reflections plus a
-- cells-to-rows decomposition; the conjugation-symmetric form is the input to the
-- Plancherel argument that `Σ_h` is not a shifted symmetric function.
import BraidKnotOctonion.HookSumClosedForm
-- Bridges that hook sum to `QOU.Common.HookSumComplete`, which proves the same
-- identity over a sorted `List ℕ` in truncated ℕ subtraction. Identifies the two
-- hook sums and re-derives the YoungDiagram closed form from the list one, so the
-- duplicate is a checked equivalence rather than two proofs free to drift.
import BraidKnotOctonion.HookSumRegisterBridge
-- Two consequences of that closed form, used to bound the deuteron-wall quantity REV
-- (bean qou-hok7): hook lengths strictly decrease along a row, so each row holds at most
-- one cell of any given hook length; and `min(rowLen 0, colLen 0)^2 <= Σ_c h(c)`, which
-- couples "thickness" back to the hook sum. The second replaces a WRONG bound
-- (`H >= 3r^2-3r+1`, 1168 counterexamples at n <= 22) and is stronger than the
-- `r^2-r+1` a repaired row-plus-column count gives.
import BraidKnotOctonion.HookSumThicknessBound
-- The same hook sum in beta-coordinates (bean qou-hok7): with `beta_i = lambda_i + (L-1-i)`
-- the corpus's `SchurWeyl.betaR`, `2 Sum_i beta_i = 2n + L(L-1)` and
-- `2 Sum_c h(c) = Sum_i beta_i(beta_i+1) - 2 Sum_{i<j}(beta_i - beta_j)`, for EVERY padding
-- `L >= l(mu)`. The REV_n shape free energy is one-body plus two-body in exactly these
-- coordinates, and its energy term enters through the second identity. Verified numerically
-- over every partition of n <= 16 before being proved; the corpus had beta-number PRODUCTS
-- (the hook-formula Vandermonde) but no identity about beta-number SUMS. Also (I'), the
-- general one-body/two-body split `Sum_c g(h(c)) + Sum_{i<j} g(beta_i - beta_j)
-- = Sum_i Sum_{m<=beta_i} g(m)` for ANY g into an AddCommMonoid -- which is SchurWeyl's
-- multiplicative `hookSide_betaR` transported through Multiplicative N, so it costs nothing
-- and gives (II) a SECOND proof, from the hook multiset rather than from the closed form.
import BraidKnotOctonion.HookSumBetaCoordinates
-- Completing the square in those beta-coordinates (bean qou-hok7): with `a_i = 2L-3-4i`,
-- `8 Sum_c h(c) = Sum_i (2 beta_i - a_i)^2 - Sum_i a_i^2`, so the hook sum is a POSITIVE-DEFINITE
-- quadratic whose whole diagram-dependence is one sum of squares. Two consequences: the row
-- deviations `d_i = 2 beta_i - a_i` satisfy `d_i - d_{i+1} = 2(beta_i - beta_{i+1}) - 4`, so they
-- are constant exactly on the staircase; and Cauchy-Schwarz gives the parameter-free floor
-- `(Sum d_i)^2 - L Sum a_i^2 <= 8 L Sum_c h(c)`, where `Sum d_i` is fixed by (n, L) alone. That
-- is the REV_n energy rigidity WITHOUT asymptotics -- PR #7286 had it only as the measured
-- `E ~ ln q_0 (2n)^{3/2} (gbar-2)^2 / 24`. Measured tight: zero gap against H_min at L = k.
import BraidKnotOctonion.HookSumCompletedSquare
-- The staircase's hook lengths in closed form (bean qou-hok7). Presenting delta_k as the
-- sublevel set `{(i,j) : i+j < k}` makes it visibly self-transpose, so `colLen` is free and
-- `hook (i,j) = 2(k-i-j) - 1` falls out -- the hook is constant along antidiagonals, and
-- antidiagonal s carries s+1 cells. `staircase_hookSum` telescopes that into
-- `Sum_c g(h(c)) = Sum_{s<k} (s+1) g(2(k-s)-1)`, which at `g = eps` IS the staircase's
-- beta-side by `betaSide_eq_hookSum`. PR #7294 had this fact only ENUMERATED (k = 1..40).
import BraidKnotOctonion.StaircaseHookMultiset
import BraidKnotOctonion.StaircaseRowDeletedHook
-- The hook sum is a separable QUADRATIC form in the beta-coordinates (bean qou-hok7):
-- composing `two_mul_sum_hookZ_betaForm` with `sum_pair_betaR_sub` leaves no pair term at all,
-- so comparing two shapes of one size gives `2(H(nu) - H(delta_k)) = Sum 2(i-k) u_i + Sum u_i^2`
-- with both terms non-negative. Hence the staircase is the UNIQUE minimiser of the hook sum at
-- triangular n, and REV_n's cost term is a local harmonic penalty on displacement away from the
-- staircase lattice -- quantised, since `Sum u_i^2` is an even integer when `Sum u_i = 0`.
import BraidKnotOctonion.HookSumElasticity
-- Separated groups of rows do not interact (bean qou-hok7). The hook sum splits over any
-- partition of the rows by inspection; the REV_n objective's PAIR term is the only thing that
-- can tie two groups together, and `sum_pairs_split` makes that split exact while
-- `cross_sum_le` bounds the cross part by `|A| * |B| * g R` at separation `R`. With the kernel
-- `eps(m) = -log(1 - q0^(-2m))` geometric, `cross_sum_le_geom` sends it to zero geometrically.
-- That is what turns the maximiser's FREE run position (#7323) into a decomposition: the top
-- block, the run and the bottom block stop interacting, and e_inf becomes a sum of three
-- k-free pieces rather than a single-n measurement.
import BraidKnotOctonion.EdgeDecoupling
--- The maximisation that decomposition leaves behind is over a FINITE set (bean qou-hok7).
--- `e_inf = max over (a, b) of [f a + h (a + b) + g b]` ranges over all pairs of naturals, but
--- the two edge energies are bounded above while the run falls linearly, so `le_of_le_join`
--- confines any pair matching an incumbent to `a + b <= L`. The bound on the edges comes from
--- `sub_le_mul_of_antitone_step` and its downward twin: a sequence with ANTITONE downward steps
--- -- `eps` convex decreasing, in discrete form, proved by induction with no analysis -- has
--- `e a - e (a + D) <= D * delta a` for both signs of `D`, which linearises every pair term and
--- lets the block's pair sum telescope. Both signs matter: keeping only `D > 0` drops the
--- negative pair terms and the bound diverges.
import BraidKnotOctonion.SearchCoercivity
--- Making that finite search DECIDED, and one non-step in the argument (bean qou-hok7).
--- `sup_le_of_supergradient` takes what concavity supplies (a supergradient inequality at a
--- point) together with what the coercivity bound supplies (confinement of any competitive `u`
--- to a box) and returns an explicit upper bound on the objective EVERYWHERE, including outside
--- the box, where it is already below the incumbent. Its load-bearing step is `box_mul_sub_le`,
--- a case split on the sign of the gradient: the linear term is maximised at `hi` when `g >= 0`
--- and at `lo` when `g < 0`. `boundary_charge_eq_zero` and `abs_charge_pos` say why that split
--- is not a refinement -- a coordinate pinned to `lo` with `g < 0` (correct KKT behaviour)
--- contributes EXACTLY ZERO, where charging it `|g| (hi - lo)` contributes strictly positively,
--- and in the measured case the whole factor of 2.25e11 between a 6.4e-12 slack and a useless
--- 1.447 one lives in that case alone.
--- `capped_lt_not_sufficient` is separate and is about evidence rather than about optimisation:
--- a maximum over a CAPPED class is a lower bound on the true maximum, so observing that it
--- falls short of a bound implies nothing about the true one -- only EXCEEDING a bound refutes.
--- The corpus's sole recorded support for G1 (`Xbot(s) <= Xblock(s)`) has exactly that shape.
import BraidKnotOctonion.SupergradientCertificate
--- The sharp-coefficient upper bound M_n <= A sqrt(2n) + O(n^{1/4}) (bean qou-fxym). The pair
--- term is bounded below by tangent lines at 2k per neighbour order k, losing sum_k |eps'(2k)|
--- Delta_k(t); that loss is measured against the WATER-FILLING reference p = max(tau, wall),
--- which is monotone (`shiftDiff_nonpos_of_monotone`, so it loses nothing) and obeys
--- `waterfill_pythagoras`, so the distance to it is paid by the within-row-count energy.
--- `linear_sub_excess_le` is the scalar trade-off; the integrality defect l/4 is why the error
--- is O(n^{1/4}) and not O(1).
import BraidKnotOctonion.HardWallProjection
--- Bounded excess M_n - A sqrt(2n) <= K2 (bean qou-fxym). Both O(n^{1/4}) sources removed:
--- `rounded_pythagoras` (discrete exchange at the ROUNDED water-fill, energy >= sum d^2 - |d|
--- with d integer, so `int_tradeoff` pays each coordinate a convergent omega_i), and
--- `diagonal_exchange` (H = sum over cells of (i+j-1), so an l-row shape pays T_{l-k-1} with no
--- r), capped by `extra_rows_tradeoff`.
import BraidKnotOctonion.RoundedWaterfillExchange
import BraidKnotOctonion.RevBoundedExcessAssembly
import BraidKnotOctonion.LNaturalOptimality
-- The M_1 edge calculus (bean qou-t6hc): Fact A, giving the per-edge sign of
-- P = Cov(Sum|c|, omega_3) >= 0 -- which is pure integer algebra, true of any two
-- contents -- and the 1-Lipschitz diagonal lemma |D(c) - D(c+1)| <= 1, which is
-- what caps the per-edge N/P ratio. Both were flagged "Lean-formalizable, verified
-- exact" in qou-k5r5 and are now proved. They are the floor under the M_1 > 0
-- analysis, NOT a route around it: per-edge arguments are refuted there.
import BraidKnotOctonion.M1EdgeCalculus
import BraidKnotOctonion.BarParityInvariant
import QOU.BraidsAndKnots.BsymLinearChain
import BraidKnotOctonion.ChiralityTopologySelection
import BraidKnotOctonion.WLambdaDefectClosedForm
import BraidKnotOctonion.KeystoneC8SuperExpBound
import BraidKnotOctonion.YoungTableauStandard
import BraidKnotOctonion.WLambdaDefectSubleadingD
import BraidKnotOctonion.WLambdaDefectLadderE
import BraidKnotOctonion.IdentityIContentDecomposition
import BraidKnotOctonion.IdentityIPlancherelInstances
import BraidKnotOctonion.InterfaceOperatorBlockDiagonal
import BraidKnotOctonion.KeystoneC2ContentTranspose
import BraidKnotOctonion.KeystoneC2DimTranspose
import BraidKnotOctonion.KeystoneC2QDimTranspose
import BraidKnotOctonion.KeystoneG2Gate
import BraidKnotOctonion.KeystoneG2LadderGate
import QOU.BraidsAndKnots.KeystoneFpnBracket
import BraidKnotOctonion.KeystoneStandardRepQDim
import BraidKnotOctonion.KeystoneMcKayValueMap
import BraidKnotOctonion.BWVacuumRowConcrete
import BraidKnotOctonion.BWVacuumRowFibre
import BraidKnotOctonion.KeystoneModularTwist
import QCalculus.BWVacuumRowHabiroRigidity
import BraidKnotOctonion.BWVacuumRowStokesMonodromy
import BraidKnotOctonion.BringWPlaneMonodromy
import BraidKnotOctonion.BringWPlaneMonodromyTower
import BraidKnotOctonion.CyclotomicLValueDecomposition
import BraidKnotOctonion.CyclotomicTrilogImaginary
import BraidKnotOctonion.CyclotomicCl3OrbitSum
import BraidKnotOctonion.CyclotomicDepth3DimensionSynthesis
import BraidKnotOctonion.JonquiereCyclotomicTateRationality
import BraidKnotOctonion.CyclotomicOrbitSumAllDepths
import BraidKnotOctonion.CyclotomicDimensionSynthesisAllDepths
import QOU.BraidsAndKnots.QHeckeSeminormalCharacterClosure
import BraidKnotOctonion.BringTrilogImaginaryTateRational
import BraidKnotOctonion.Cl3Zeta5OrbitSum
import BraidKnotOctonion.BringTrilogDepth3Witness
import BraidKnotOctonion.Cl3Zeta5GeometricRealization
import HeckeTemperleyLieb.BWVacuumRowIsHecke
import BraidKnotOctonion.KeystoneSelfDualSpectralNarrowing
import BraidKnotOctonion.KeystonePerronFrobeniusGroundState
import BraidKnotOctonion.KeystonePFTwoBlockWitness
import BraidKnotOctonion.KeystonePFGroundStateIsingInstance
import BraidKnotOctonion.KeystoneValueMapSynthesis
import QOU.BraidsAndKnots.Cl3Zeta5PslqIndependence
import QOU.BraidsAndKnots.KnotIndexedConvolutionGrid
import QOU.BraidsAndKnots.ConfinedParticle
import QOU.BraidsAndKnots.ConfinementCategory
import QOU.BraidsAndKnots.ElectronShell
import QOU.BraidsAndKnots.DressedParticle
import QOU.BraidsAndKnots.LevelSufficiency
import QOU.BraidsAndKnots.ShellClosureStability
import BraidKnotOctonion.ShellNeutrality
import BraidKnotOctonion.MathlibBridge
import QOU.BraidsAndKnots.ConfinementPhaseStratification
import BraidKnotOctonion.ThreeCalibrationInputs
import QOU.BraidsAndKnots.ConfinementLevel
import QOU.BraidsAndKnots.ChiralityWritheRibbon
import QOU.BraidsAndKnots.EigenbasisStructuralLemmas
import QOU.BraidsAndKnots.GradedMarkovTraceFromGSFiltration
import BraidKnotOctonion.ResidueAtRoot
import QOU.BraidsAndKnots.GBSpectralSequence
import QOU.BraidsAndKnots.GradedTraceResidueSplit
import QOU.BraidsAndKnots.GBResidueSpectralSum
import BraidKnotOctonion.JetTowerUniformDeltaMax
import BraidKnotOctonion.PhiQTowerAlgebraicStratification
import HeckeTemperleyLieb.CanonicalKnotIdSDPUniqueness
import BraidKnotOctonion.PSDFeasibilityProxy
import QOU.BraidsAndKnots.HopfBindingK
import QOU.BraidsAndKnots.LightNucleus
import QOU.BraidsAndKnots.WitnessR5Full
import QOU.BraidsAndKnots.Helium3Witness
import QCalculus.HabiroNewtonLadder
import BraidKnotOctonion.AJFigureEight
import BraidKnotOctonion.AJFigureEightCertificate
import BraidKnotOctonion.AJFigureEightTelescope
import BraidKnotOctonion.AJFigureEightAnnihilation
import BraidKnotOctonion.AJTrefoil
import BraidKnotOctonion.AJTrefoilAnnihilation
import QOU.BraidsAndKnots.DeuteronWitness
import QOU.BraidsAndKnots.TritiumWitness
import QOU.BraidsAndKnots.MassFormulaCategorical
import QOU.BraidsAndKnots.NucleusEmptySDPUniqueness
import QOU.BraidsAndKnots.AppliedHelium3Uniqueness
import QOU.BraidsAndKnots.AppliedDeuteronUniqueness
import QOU.BraidsAndKnots.AppliedDeuteronRealSDP
import QOU.BraidsAndKnots.AppliedTritiumUniqueness
import QOU.BraidsAndKnots.AppliedHelium4Uniqueness
import QOU.BraidsAndKnots.AppliedLithium6Uniqueness
import QOU.BraidsAndKnots.AppliedBeryllium9Uniqueness
import QOU.BraidsAndKnots.AppliedBoron11Uniqueness
import QOU.BraidsAndKnots.AppliedCarbon12Uniqueness
import QOU.BraidsAndKnots.AppliedNitrogen14Uniqueness
import QOU.BraidsAndKnots.AppliedOxygen16Uniqueness
import QOU.BraidsAndKnots.PeriodicTableUniqueness
import QOU.BraidsAndKnots.AllKnownIsotopesUniqueness
import QOU.BraidsAndKnots.PerNucleusMassDerivation
import TwistedFrobeniusHopf.frobenius_antipode_unifies
import QOU.BraidsAndKnots.CommutativeCrossingEnergy
import BraidKnotOctonion.nonabelian_stokes_surface_boundary_stokes
-- Sibling-import cluster wire-in (2026-06-01): content-tree extracts
-- migrated into the Lake build (see
-- docs/audits/2026-06-01-sibling-import-cluster-wire-in-plan.md).
-- Six modules renamed snake_case → CamelCase (Lean-4 idiom) with all
-- importers updated in lock-step. COMPILE-PENDING.
import BraidKnotOctonion.BraidLinkTypes
import BraidKnotOctonion.BraidGroupNStrand
import HeckeTemperleyLieb.MarkovAxiomsPrimitive
import HeckeTemperleyLieb.MarkovParameterFibreRank
import BraidKnotOctonion.CrossingEnergyBarParity
import HeckeTemperleyLieb.H3HeckeIdempotents
import HeckeTemperleyLieb.HoefsmitV21CosSymmetrization
import QOU.BraidsAndKnots.QBetaCategoricalPrecisionLadder
import QOU.BraidsAndKnots.QBetaCnAtSilver
import QOU.BraidsAndKnots.QBetaCKRecursionKernelConstraints
import QOU.BraidsAndKnots.QBetaPreArchHeatDepthOneKernel
import BraidKnotOctonion.F3_eps6_leading_eq_neg_2b_cubed
import BraidKnotOctonion.KnotFactorSpectralDerivation
import BraidKnotOctonion.KnotFactorAmphicheiral
import HeckeTemperleyLieb.PlancherelWeightBoundedness
import BraidKnotOctonion.TwoRowStratum
import BraidKnotOctonion.AlphaShiftTorus.AlphaShiftTorusKnot
import HeckeTemperleyLieb.GramSeminormalBlock
import QOU.BraidsAndKnots.GSReductionOrder
import QOU.BraidsAndKnots.MassGapKeystone
import QOU.BraidsAndKnots.MassGapObstruction
import QOU.BraidsAndKnots.CrossingGradedModel
import QOU.BraidsAndKnots.MassGapFrontier
-- Identity-(B) ℂ-free cluster (keystone-carried RT input): the Jucys–Murphy
-- identity coefficient and the regular-representation trace bridge. Wiring these
-- into the umbrella also pulls JucysMurphyCoeff (merged orphaned in #2713) into
-- the CI build.
import HeckeTemperleyLieb.JucysMurphyCoeff
import HeckeTemperleyLieb.RegularRepTrace
import BraidKnotOctonion.RegularRepBlockTrace
-- Δ_λ closure-refutation cluster (sorry-free, previously orphaned). These
-- modules formalize the per-partition binding weight Δ_λ and the failure of the
-- co-Casimir / crystal-graph closure ansätze; they were merged but never imported
-- by this umbrella, so CI never built them and their sorry-free status went
-- unenforced (cf. JucysMurphyCoeff, wired in above after #2713). Wiring them in
-- puts the refutations under the CI build (bean 48yu, #2676).
-- DeltaLambdaSignRule was repaired in this PR: reserved `λ`→`Λ`, added ℝ/`arccos`
-- imports, gave each vacuity-dodge `: trivial` "theorem" an honest disposition
-- (§1a: faithful `sorry`+`-- Ref:` targets, one proved scalar lemma, the character
-- identities documented rather than faked), and isolated it under namespace
-- `QOU.BraidKnot.DeltaLambdaSignRule` to avoid the `Partition` collision with
-- GramSeminormalBlock / PerPartitionKLambda. It now compiles (lean-direct EXIT=0;
-- 3 honest sorry+Ref targets: nStat / sign-rule / Burnside).
import QOU.BraidsAndKnots.DeltaLambdaRefutation
import QOU.BraidsAndKnots.DeltaLambdaExponentKeystone
import QOU.BraidsAndKnots.DeltaLambdaSignRule
import QOU.BraidsAndKnots.PartitionNatBridge
import QOU.BraidsAndKnots.PartitionReindex
-- g_ρ = GS/jet-order (fake-degree) grading: the Δ_λ sign carrier (#3542) +
-- assembly identity Δ_λ = tr(g_ρ) = (−1)^{n(λ)}·dim(λ) + bar-parity selection
-- rule. Pulls the file into the CI build set (was previously un-imported).
import BraidKnotOctonion.PrincipalGradingJetOrder
-- Tier-3 (bean 60iz): Jones value of the Hopf link via the Markov trace +
-- proved stabilisation-invariance (the q-deformed H_n(q) side of the knot
-- invariant; complementary to the q=1 k[S_n] Wedderburn build).
import BraidKnotOctonion.JonesViaMarkovTrace
-- Nuclear quotient braid Jones value (RHS of the open jet-filtered-knot-factor
-- Part-4 conjecture): the (2,k) torus-link Markov-trace values unknot/Hopf/
-- trefoil + the shell-structure Z,N ↦ k∈{1,2,3} classifier. Infra only — builds
-- jonesQuotient, does NOT prove a(Z,N)=J_β̄(q).
import QOU.BraidsAndKnots.JonesNuclearQuotient
-- Provenance of the Q_β c_3 near-match constant -2 = J_Hopf(q=1) via the
-- classical Jones loop factor / V_L(1)=(-2)^(c-1); does NOT close a derivation
-- gap (c_3 is proved measurement-limited), only rigorizes the constant's origin:
import QOU.BraidsAndKnots.JHopfQOneProvenance
-- YT seminormal-sum Mathlib-gap infra (beans qou-cxkc / qou-mcbf / qou-ujfg):
-- the weight layer (a_ρ = h·g_ρ, pairing g_ρ+g_{−ρ}=1) + the cell-geometry
-- layer (content, axial distance) toward the seminormal character sum.
import HeckeTemperleyLieb.SeminormalWeight
import HeckeTemperleyLieb.TableauContent
-- connector (bean qou-tqab): reuses canonical StandardYoungTableau; cellOf +
-- generatorRho supply the (position, ρ) data the character core ranges over.
import HeckeTemperleyLieb.SeminormalCharacterConnector
-- Concrete #SYT counts for small self-conjugate shapes: the hook (2,1) has
-- #SYT = 2, hence c_λ(σ₁) = 1 — the first tabulated character coefficient.
import HeckeTemperleyLieb.SytSmallShapeCounts
-- The full tabulated c_λ ∈ {1,3,8,10} column of symbolic_character_table, proved
-- as #SYT/2 via the seminormal count + the Frame–Robinson–Thrall HLF.
import BraidKnotOctonion.ClambdaColumn
-- Tier-3 (bean 60iz) general-H_n(q) completion: the arbitrary-braid-word Jones
-- value + Markov move II (conjugation invariance), on the sibling-landed
-- IwahoriHeckeAPI element algebra. Move I = IwahoriHeckeAPI.markovTrace_stab_comm;
-- the two moves together make tr_M a link invariant. (Also pulls IwahoriHeckeAPI
-- into the in-build set.)
import HeckeTemperleyLieb.MarkovTraceLinkInvariance
import QOU.BraidsAndKnots.YLambdaQSchur
-- Maschke (RepresentationTheory) ⇒ k[S_n] semisimple: the *existence* half of side-2's
-- block decomposition. First QOU import of Mathlib.RepresentationTheory.* — CI must build it.
import HeckeTemperleyLieb.MaschkeSnSemisimple
import HeckeTemperleyLieb.WedderburnSn
-- ⟨Res^{S₃}_{S₂} V_(2,1), V_(2)⟩ = 1 proved by finite computation (GAP-1 closure
-- path 2, docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md).
import HeckeTemperleyLieb.SpechtBranchingMultiplicityOne
-- Integer-trace prune of the lever-1 "SL₂(ℤ) monodromy" framing: tr B ∈ (2,3) is
-- non-integer, so no integral monodromy realizes it (scope-(b); uploaded-papers
-- audit idea A3, 2026-07-18); the surviving object is an SL₂(ℝ) transfer family.
import BraidKnotOctonion.TrBIntegerTracePrune
import QOU.BraidsAndKnots.HeckeReebHolonomyLaplacian
import QOU.BraidsAndKnots.HeckePresentationBridge

/-!
# BraidKnot — Module Index

Re-exports all formalization modules for the confinement framework:
confined particles, the confinement category, electron shells,
dressing morphisms, level sufficiency, shell-closure stability,
and phase stratification.

## Modules

- ConfinedParticle: (name, level, Markov class, coarse strand count)
- ConfinementCategory: Conf with {unfold, fold, dress} morphisms
- ElectronShell: cabled-strand shell with SDP binding subword
- DressedParticle: codomain of a dressing morphism
- LevelSufficiency: Markov-trace preservation under unfolding
- ShellClosureStability: σ_F monotone, noble-gas terminality
- ShellNeutrality: full-twist θ_n = 1 ↔ κ_λ = 0 ↔ self-conjugate λ
- MathlibBridge: fromMathlib bridge to Mathlib.Combinatorics.Young.YoungDiagram
- ConfinementPhaseStratification: Ω(P) open, local μ constancy
- ChiralityWritheRibbon: a_K = 1 + w·h + O(h²) from ribbon-twist framing
- EigenbasisStructuralLemmas: content/twist eigenbasis L1 (q↦−q parity),
  L2 (bar↔conjugate duality), L3 (framing GF = single-pole rational)
-/
