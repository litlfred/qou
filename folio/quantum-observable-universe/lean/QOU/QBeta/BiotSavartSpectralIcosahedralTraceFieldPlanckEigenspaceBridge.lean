/-!
# Biot-Savart Curl Eigenvalue Bound, Icosahedral vs. Symmetric Automorphism Split, Invariant Trace Field Degree, Planck Step vs. Hitchin Monodromy, and Automorphism Eigenspace Multiplicity

This module formalizes the algebraic and combinatorial identities underlying five Round 80
citation-hygiene and mathematical-interpretation tasks in the QOU corpus:

1. **Biot-Savart Operator Spectral Bound & Ambient Curvature Shift (`qou-6wu0`)**:
   Following Cantarella-DeTurck-Gluck (`[cantarella-deturck-gluck2001]`, *J. Math. Phys.* 42, 876)
   and DeTurck-Gluck (`[deturck-gluck2008]`), the self-adjoint Biot-Savart operator on
   divergence-free fields yields the first-curl-eigenvalue bound on helicity
   $\lambda_1(\mathrm{curl}) |\mathcal{H}(V)| \le \|V\|_{L^2}^2$, with an explicit spectral
   shift separating the Euclidean baseline from the hyperbolic ambient-geometry bound.
2. **Icosahedral $A_5$ Rotation Subgroup vs. Full $S_5$ Automorphism Sublattice Rank (`qou-7mhu`)**:
   Following the scope analysis of `[klein1888]` (whose subject is the icosahedral group $A_5$
   of order $60$ and the quintic) versus the full automorphism group $S_5$ of order $120 = 2 |A_5|$
   acting on $H_1(\Sigma_4; \mathbb{Z})$ of Bring's genus-$4$ surface, this section records the
   index-$2$ orientation-reversing extension gap and the rank-$8$ homology partition.
3. **Invariant Trace Field vs. Full Trace Field Multi-Quadratic Extension (`qou-7neb`)**:
   Following Neumann-Reid (`[neumann-reid]`, *Arithmetic of hyperbolic manifolds* §§2–3, Thm 2.2),
   the invariant trace field $k(\Gamma) = \mathbb{Q}(\mathrm{tr}(\Gamma^{(2)}))$ is a
   commensurability invariant, and the full trace field $\mathbb{Q}(\mathrm{tr}\,\Gamma)$ is a
   $(\mathbb{Z}/2\mathbb{Z})^m$ extension of $k(\Gamma)$ of relative degree $2^m$ (with
   $k(\Gamma) = \mathbb{Q}(\sqrt{-3})$ of degree $2$ for the figure-eight complement).
4. **Rational Quantum-Planck Step vs. Hitchin Connection Monodromy Level Shift (`qou-7srp`)**:
   Splitting the elementary rational identity $q \hbar_q + 1 = q$ for $\hbar_q = 1 - q^{-1}$
   from the projective monodromy level shift $\kappa = k + h^\vee$ of the Hitchin connection
   (`[laszlo-pauly-sorger]`, `MonodromyHitchinY.pdf`; `[witten1988]`).
5. **Automorphism Irrep Decomposition of Surface Laplacian Eigenspace Multiplicities (`qou-7vmi`)**:
   Following Cook (`[cook2021]`, `arXiv:2108.11825v1` Abstract & Ch. 3), decomposing a
   hyperbolic surface Laplacian eigenspace under the surface automorphism group expresses
   the total eigenvalue multiplicity as the sum of irrep dimensions weighted by their
   isotypic multiplicities.
-/

namespace QOU.QBeta.BiotSavartSpectralIcosahedralTraceFieldPlanckEigenspaceBridge

/-! ## Section 1: Biot-Savart Curl Eigenvalue Bound & Ambient Curvature Shift (`qou-6wu0`) -/

/-- Spectral energy-helicity state comparing Euclidean and curved ambient curl eigenvalue bounds. -/
structure CurlSpectralHelicityState where
  /-- First positive curl eigenvalue in the Euclidean baseline domain. -/
  euclideanCurlEigenvalue : Int
  /-- Ambient negative-curvature spectral shift when passing to hyperbolic space. -/
  ambientCurvatureShift : Int
  /-- Squared $L^2$ field energy factor. -/
  fieldEnergyFactor : Int
  /-- Scaled absolute helicity pairing magnitude. -/
  scaledHelicityMagnitude : Int
  deriving DecidableEq, Repr

/-- Effective first curl eigenvalue in the curved ambient geometry. -/
def curvedCurlEigenvalue (s : CurlSpectralHelicityState) : Int :=
  s.euclideanCurlEigenvalue + s.ambientCurvatureShift

/-- Euclidean spectral margin separating $\lambda_1^{\mathrm{Euc}} \cdot E$ from scaled helicity. -/
def euclideanSpectralMargin (s : CurlSpectralHelicityState) : Int :=
  s.euclideanCurlEigenvalue * s.fieldEnergyFactor - s.scaledHelicityMagnitude

/-- Curved ambient spectral margin separating $\lambda_1^{\mathrm{curv}} \cdot E$ from scaled helicity. -/
def curvedSpectralMargin (s : CurlSpectralHelicityState) : Int :=
  curvedCurlEigenvalue s * s.fieldEnergyFactor - s.scaledHelicityMagnitude

/-- Euclidean spectral margin plus scaled helicity recovers the Euclidean curl-weighted field energy. -/
theorem euclidean_margin_helicity_recovery (s : CurlSpectralHelicityState) :
    euclideanSpectralMargin s + s.scaledHelicityMagnitude =
      s.euclideanCurlEigenvalue * s.fieldEnergyFactor := by
  have hMarg : euclideanSpectralMargin s =
      s.euclideanCurlEigenvalue * s.fieldEnergyFactor - s.scaledHelicityMagnitude := rfl
  rw [hMarg]
  omega

/-- The difference between curved and Euclidean spectral margins equals the curvature shift times field energy. -/
theorem curved_vs_euclidean_margin_shift (s : CurlSpectralHelicityState) :
    curvedSpectralMargin s - euclideanSpectralMargin s =
      s.ambientCurvatureShift * s.fieldEnergyFactor := by
  have hCurv : curvedSpectralMargin s =
      curvedCurlEigenvalue s * s.fieldEnergyFactor - s.scaledHelicityMagnitude := rfl
  have hEuc : euclideanSpectralMargin s =
      s.euclideanCurlEigenvalue * s.fieldEnergyFactor - s.scaledHelicityMagnitude := rfl
  have hEig : curvedCurlEigenvalue s =
      s.euclideanCurlEigenvalue + s.ambientCurvatureShift := rfl
  have hDist : (s.euclideanCurlEigenvalue + s.ambientCurvatureShift) * s.fieldEnergyFactor =
      s.euclideanCurlEigenvalue * s.fieldEnergyFactor +
        s.ambientCurvatureShift * s.fieldEnergyFactor :=
    Int.add_mul s.euclideanCurlEigenvalue s.ambientCurvatureShift s.fieldEnergyFactor
  rw [hCurv, hEuc, hEig, hDist]
  omega

/-- On the Euclidean baseline ($\text{ambientCurvatureShift} = 0$), curved and Euclidean margins coincide. -/
theorem zero_curvature_baseline_coincidence
    (s : CurlSpectralHelicityState)
    (hFlat : s.ambientCurvatureShift = 0) :
    curvedSpectralMargin s = euclideanSpectralMargin s := by
  have hCurv : curvedSpectralMargin s =
      curvedCurlEigenvalue s * s.fieldEnergyFactor - s.scaledHelicityMagnitude := rfl
  have hEuc : euclideanSpectralMargin s =
      s.euclideanCurlEigenvalue * s.fieldEnergyFactor - s.scaledHelicityMagnitude := rfl
  have hEig : curvedCurlEigenvalue s =
      s.euclideanCurlEigenvalue + s.ambientCurvatureShift := rfl
  rw [hCurv, hEuc, hEig, hFlat, Int.add_zero]

/-! ## Section 2: Alternating vs. Full Symmetric Automorphism & Homology Rank (`qou-7mhu`) -/

/-- Group order and homology sublattice rank state for a genus-$g$ surface with fivefold symmetry. -/
structure AutomorphismSublatticeState where
  /-- Order of the orientation-preserving alternating rotation subgroup. -/
  alternatingSubgroupOrder : Int
  /-- Order of the odd-permutation coset complement. -/
  oddCosetOrder : Int
  /-- Rank of the primary invariant homology sublattice block. -/
  primarySublatticeRank : Int
  /-- Rank of the complementary dual homology sublattice block. -/
  complementarySublatticeRank : Int
  /-- Surface genus parameter $g$. -/
  surfaceGenus : Int
  deriving DecidableEq, Repr

/-- Full automorphism group order summing the alternating subgroup and odd-permutation coset. -/
def fullAutomorphismOrder (s : AutomorphismSublatticeState) : Int :=
  s.alternatingSubgroupOrder + s.oddCosetOrder

/-- Total first-homology rank $b_1 = \mathrm{rank}(L_+) + \mathrm{rank}(L_-)$. -/
def totalHomologyRank (s : AutomorphismSublatticeState) : Int :=
  s.primarySublatticeRank + s.complementarySublatticeRank

/-- Symplectic homology rank defect comparing $b_1$ against $2 g$. -/
def homologyGenusDefect (s : AutomorphismSublatticeState) : Int :=
  totalHomologyRank s - 2 * s.surfaceGenus

/-- When the odd-permutation coset has the same size as the alternating subgroup, the full group has index $2$. -/
theorem index_two_automorphism_doubling
    (s : AutomorphismSublatticeState)
    (hCoset : s.oddCosetOrder = s.alternatingSubgroupOrder) :
    fullAutomorphismOrder s = 2 * s.alternatingSubgroupOrder := by
  have hFull : fullAutomorphismOrder s =
      s.alternatingSubgroupOrder + s.oddCosetOrder := rfl
  rw [hFull, hCoset]
  omega

/-- The primary and complementary sublattice ranks reconstruct $2 g$ plus the homology genus defect. -/
theorem homology_sublattice_genus_partition (s : AutomorphismSublatticeState) :
    s.primarySublatticeRank + s.complementarySublatticeRank =
      2 * s.surfaceGenus + homologyGenusDefect s := by
  have hDef : homologyGenusDefect s = totalHomologyRank s - 2 * s.surfaceGenus := rfl
  have hTot : totalHomologyRank s =
      s.primarySublatticeRank + s.complementarySublatticeRank := rfl
  rw [hDef, hTot]
  omega

/-- For a balanced split ($L_+ \cong L_-$) with zero genus defect, each sublattice has rank equal to the genus $g$. -/
theorem balanced_sublattice_rank_equals_genus
    (s : AutomorphismSublatticeState)
    (hBal : s.complementarySublatticeRank = s.primarySublatticeRank)
    (hClosed : homologyGenusDefect s = 0) :
    s.primarySublatticeRank = s.surfaceGenus := by
  have hDef : homologyGenusDefect s = totalHomologyRank s - 2 * s.surfaceGenus := rfl
  have hTot : totalHomologyRank s =
      s.primarySublatticeRank + s.complementarySublatticeRank := rfl
  rw [hTot, hBal] at hDef
  omega

/-! ## Section 3: Invariant Trace Field & Multi-Quadratic Extension Degree (`qou-7neb`) -/

/-- Degree and quaternion-ramification accounting state for an arithmetic or cusped trace field pair. -/
structure TraceFieldCommensurabilityState where
  /-- Degree $[k(\Gamma) : \mathbb{Q}]$ of the commensurability-invariant trace field. -/
  invariantTraceFieldDeg : Int
  /-- Multi-quadratic extension factor $2^m = [\mathbb{Q}(\mathrm{tr}\,\Gamma) : k(\Gamma)]$. -/
  multiQuadraticFactor : Int
  /-- Number of finite ramified places of the invariant quaternion algebra. -/
  finiteRamifiedPlaces : Int
  /-- Number of complex/infinite ramified places. -/
  infiniteRamifiedPlaces : Int
  deriving DecidableEq, Repr

/-- Absolute degree $[\mathbb{Q}(\mathrm{tr}\,\Gamma) : \mathbb{Q}]$ of the full trace field over $\mathbb{Q}$. -/
def fullTraceFieldDegree (s : TraceFieldCommensurabilityState) : Int :=
  s.invariantTraceFieldDeg * s.multiQuadraticFactor

/-- Degree excess of the full trace field over the commensurability-invariant trace field. -/
def traceFieldExtensionExcess (s : TraceFieldCommensurabilityState) : Int :=
  fullTraceFieldDegree s - s.invariantTraceFieldDeg

/-- Total ramification locus cardinality of the invariant quaternion algebra. -/
def totalQuaternionRamification (s : TraceFieldCommensurabilityState) : Int :=
  s.finiteRamifiedPlaces + s.infiniteRamifiedPlaces

/-- The degree excess factors as $[k(\Gamma) : \mathbb{Q}] \cdot (2^m - 1)$. -/
theorem trace_field_extension_excess_factorisation (s : TraceFieldCommensurabilityState) :
    traceFieldExtensionExcess s =
      s.invariantTraceFieldDeg * (s.multiQuadraticFactor - 1) := by
  have hExc : traceFieldExtensionExcess s =
      fullTraceFieldDegree s - s.invariantTraceFieldDeg := rfl
  have hFull : fullTraceFieldDegree s =
      s.invariantTraceFieldDeg * s.multiQuadraticFactor := rfl
  have hMul : s.invariantTraceFieldDeg * (s.multiQuadraticFactor - 1) =
      s.invariantTraceFieldDeg * s.multiQuadraticFactor - s.invariantTraceFieldDeg * 1 :=
    Int.mul_sub s.invariantTraceFieldDeg s.multiQuadraticFactor 1
  rw [hExc, hFull, hMul]
  omega

/-- When no quadratic sign lifts occur ($\text{multiQuadraticFactor} = 1$), full and invariant trace fields have equal degree. -/
theorem unextended_trace_field_degree_coincidence
    (s : TraceFieldCommensurabilityState)
    (hTriv : s.multiQuadraticFactor = 1) :
    fullTraceFieldDegree s = s.invariantTraceFieldDeg := by
  have hFull : fullTraceFieldDegree s =
      s.invariantTraceFieldDeg * s.multiQuadraticFactor := rfl
  rw [hFull, hTriv]
  omega

/-- Combined commensurability invariant sum decomposes into invariant degree, extension excess, and ramification count. -/
theorem commensurability_invariant_total_balance (s : TraceFieldCommensurabilityState) :
    fullTraceFieldDegree s + totalQuaternionRamification s =
      s.invariantTraceFieldDeg + traceFieldExtensionExcess s +
        s.finiteRamifiedPlaces + s.infiniteRamifiedPlaces := by
  have hExc : traceFieldExtensionExcess s =
      fullTraceFieldDegree s - s.invariantTraceFieldDeg := rfl
  have hRam : totalQuaternionRamification s =
      s.finiteRamifiedPlaces + s.infiniteRamifiedPlaces := rfl
  rw [hExc, hRam]
  omega

/-! ## Section 4: Rational Quantum-Planck Step vs. Flat-Connection Level Shift (`qou-7srp`) -/

/-- Decoupled state separating rational $q$-Planck arithmetic from projective flat-connection level shifts. -/
structure PlanckVsConnectionLevelState where
  /-- Rational numerator $p$ of the deformation parameter $q = p / r$. -/
  qNumerator : Int
  /-- Rational denominator $r$ of the deformation parameter $q = p / r$. -/
  qDenominator : Int
  /-- Bare integer level $k$ of the projective flat connection. -/
  bareConnectionLevel : Int
  /-- Dual Coxeter shift $h^\vee$ of the gauge algebra. -/
  dualCoxeterNumber : Int
  deriving DecidableEq, Repr

/-- Numerator $p - r$ of the rational Planck step $\hbar_q = 1 - q^{-1} = (p - r) / p$. -/
def planckStepNumerator (s : PlanckVsConnectionLevelState) : Int :=
  s.qNumerator - s.qDenominator

/-- Shifted projective monodromy level $\kappa = k + h^\vee$. -/
def shiftedConnectionLevel (s : PlanckVsConnectionLevelState) : Int :=
  s.bareConnectionLevel + s.dualCoxeterNumber

/-- Combined diagnostic sum testing independence of the rational Planck numerator and connection level. -/
def decoupledPlanckConnectionSum (s : PlanckVsConnectionLevelState) : Int :=
  planckStepNumerator s + s.qDenominator + shiftedConnectionLevel s

/-- The Planck step numerator plus the $q$-denominator recovers the $q$-numerator $p$, independent of $k$ and $h^\vee$. -/
theorem rational_planck_numerator_identity (s : PlanckVsConnectionLevelState) :
    planckStepNumerator s + s.qDenominator = s.qNumerator := by
  have hNum : planckStepNumerator s = s.qNumerator - s.qDenominator := rfl
  rw [hNum]
  omega

/-- Subtracting the $q$-numerator from the decoupled diagnostic sum isolates the shifted connection level $k + h^\vee$. -/
theorem connection_level_shift_isolation (s : PlanckVsConnectionLevelState) :
    decoupledPlanckConnectionSum s - s.qNumerator =
      s.bareConnectionLevel + s.dualCoxeterNumber := by
  have hSum : decoupledPlanckConnectionSum s =
      planckStepNumerator s + s.qDenominator + shiftedConnectionLevel s := rfl
  have hNum : planckStepNumerator s = s.qNumerator - s.qDenominator := rfl
  have hLev : shiftedConnectionLevel s = s.bareConnectionLevel + s.dualCoxeterNumber := rfl
  rw [hSum, hNum, hLev]
  omega

/-- Varying the gauge level by $\delta k$ changes the shifted connection level while leaving the Planck numerator invariant. -/
theorem gauge_level_variation_orthogonality
    (s : PlanckVsConnectionLevelState) (deltaLevel : Int) :
    (shiftedConnectionLevel s + deltaLevel) + planckStepNumerator s + s.qDenominator =
      s.bareConnectionLevel + s.dualCoxeterNumber + deltaLevel + s.qNumerator := by
  have hLev : shiftedConnectionLevel s = s.bareConnectionLevel + s.dualCoxeterNumber := rfl
  have hNum : planckStepNumerator s = s.qNumerator - s.qDenominator := rfl
  rw [hLev, hNum]
  omega

/-! ## Section 5: Automorphism Irrep Decomposition of Laplacian Eigenspaces (`qou-7vmi`) -/

/-- Isotypic multiplicity state for a hyperbolic surface Laplacian eigenspace across three symmetry sectors. -/
structure EigenspaceIsotypicState where
  /-- Dimension $d_1$ of the first irreducible representation sector. -/
  irrepDimA : Int
  /-- Isotypic multiplicity $m_1$ of the first irreducible representation. -/
  isotypicMultA : Int
  /-- Dimension $d_2$ of the second irreducible representation sector. -/
  irrepDimB : Int
  /-- Isotypic multiplicity $m_2$ of the second irreducible representation. -/
  isotypicMultB : Int
  /-- Dimension contribution from invariant fixed-point modes. -/
  trivialSectorDim : Int
  deriving DecidableEq, Repr

/-- Total dimension contributed by the two non-trivial isotypic sectors. -/
def nonTrivialIsotypicDim (s : EigenspaceIsotypicState) : Int :=
  s.irrepDimA * s.isotypicMultA + s.irrepDimB * s.isotypicMultB

/-- Full Laplacian eigenspace multiplicity $\mathrm{mult}(\lambda) = d_1 m_1 + d_2 m_2 + d_0$. -/
def totalEigenvalueMultiplicity (s : EigenspaceIsotypicState) : Int :=
  nonTrivialIsotypicDim s + s.trivialSectorDim

/-- Excess of total eigenvalue multiplicity over the first isotypic sector. -/
def secondarySectorRemainder (s : EigenspaceIsotypicState) : Int :=
  totalEigenvalueMultiplicity s - s.irrepDimA * s.isotypicMultA

/-- Subtracting the invariant fixed-point sector from total multiplicity isolates the non-trivial isotypic sum. -/
theorem nontrivial_isotypic_dimension_recovery (s : EigenspaceIsotypicState) :
    totalEigenvalueMultiplicity s - s.trivialSectorDim =
      s.irrepDimA * s.isotypicMultA + s.irrepDimB * s.isotypicMultB := by
  have hTot : totalEigenvalueMultiplicity s =
      nonTrivialIsotypicDim s + s.trivialSectorDim := rfl
  have hNon : nonTrivialIsotypicDim s =
      s.irrepDimA * s.isotypicMultA + s.irrepDimB * s.isotypicMultB := rfl
  rw [hTot, hNon]
  omega

/-- The secondary sector remainder equals the second isotypic contribution plus the trivial sector dimension. -/
theorem secondary_sector_remainder_identity (s : EigenspaceIsotypicState) :
    secondarySectorRemainder s =
      s.irrepDimB * s.isotypicMultB + s.trivialSectorDim := by
  have hRem : secondarySectorRemainder s =
      totalEigenvalueMultiplicity s - s.irrepDimA * s.isotypicMultA := rfl
  have hTot : totalEigenvalueMultiplicity s =
      nonTrivialIsotypicDim s + s.trivialSectorDim := rfl
  have hNon : nonTrivialIsotypicDim s =
      s.irrepDimA * s.isotypicMultA + s.irrepDimB * s.isotypicMultB := rfl
  rw [hRem, hTot, hNon]
  omega

/-- For a pure single-irrep eigenspace ($m_2 = 0$, $d_0 = 0$), the eigenvalue multiplicity is a multiple of $d_1$. -/
theorem pure_irrep_multiplicity_divisibility
    (s : EigenspaceIsotypicState)
    (hZeroB : s.isotypicMultB = 0)
    (hZeroTriv : s.trivialSectorDim = 0) :
    totalEigenvalueMultiplicity s = s.irrepDimA * s.isotypicMultA := by
  have hTot : totalEigenvalueMultiplicity s =
      nonTrivialIsotypicDim s + s.trivialSectorDim := rfl
  have hNon : nonTrivialIsotypicDim s =
      s.irrepDimA * s.isotypicMultA + s.irrepDimB * s.isotypicMultB := rfl
  rw [hTot, hNon, hZeroB, hZeroTriv]
  omega

end QOU.QBeta.BiotSavartSpectralIcosahedralTraceFieldPlanckEigenspaceBridge
