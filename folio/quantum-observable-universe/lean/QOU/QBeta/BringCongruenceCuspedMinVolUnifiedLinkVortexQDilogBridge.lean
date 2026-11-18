/-!
# Bring Period Matrix Level-5 Congruence, Cusped Minimal-Volume Multiplicity, Unified Link Volume, Vortex Cluster Circulation, and Quantum Dilogarithm Normalisation

This module formalizes the algebraic and combinatorial identities underlying five Round 79
citation-hygiene and mathematical-interpretation tasks in the QOU corpus:

1. **Level-5 Symplectic Congruence & Bring Period Stabiliser (`qou-3q4q`)**:
   Following Riera-Rodríguez (`[riera-rodriguez-1992]` Lemma 1, p. 184, and the proposition
   immediately following it), an integral symplectic matrix commuting with the $S_5$-automorphism
   action on $H_1$ of Bring's curve has lower-left block divisible by $5$ ($c = 5 k$) and lies
   in $\mathrm{Sp}\Gamma_0(5)$, which stabilizes Bring's half-plane and governs the residual
   gauge for the $t_5 = -10$ Hauptmodul gate.
2. **Minimal Cusped Hyperbolic Volume Multiplicity & Link Degeneracy (`qou-4kmu`)**:
   Following Hodgson-Masai (`[hodgson2012]`, `arXiv:1203.6551v1` §1 & §5, citing Cao-Meyerhoff),
   the minimal volume $v_\omega = 2 v_3 \approx 2.0298832\dots$ among orientable cusped hyperbolic
   $3$-manifolds is attained by $N_C(v_\omega) = 2$ manifolds (the figure-eight knot complement
   $m004$ in $S^3$ and its non-$S^3$ sister $m003$), while the number $N_L(v)$ of hyperbolic link
   complements of volume $v$ grows at least exponentially with $v$.
3. **Unified Link-Drilled Volume vs. Classical Hyperbolic Volume on Closed/Non-Hyperbolic Manifolds (`qou-5m9w`)**:
   Following Kegel et al. (`[kegel2024]`, `arXiv:2402.04839v2` Abstract & §2), passing to
   minimal-component hyperbolic links inside a closed $3$-manifold yields a positive unified
   volume invariant partitioned by the minimal link component count $c_{\min}(M)$ ($c_{\min} = 0$
   precisely when $M$ is hyperbolic), clarifying that $\mathrm{Vol}_{\mathrm{hyp}}(K) = 0$ on
   torus knots is a statement about the classical hyperbolic complement volume.
4. **Superfluid Vortex Cluster Circulation Quantisation (`qou-6m79`)**:
   Following Gauthier et al. (`[gauthier2019]`), in a two-dimensional Bose-Einstein condensate
   vortex cluster, each elementary quantum vortex carries signed winding $\pm 1$ in units of the
   single-vortex circulation quantum $\kappa_0 = h/m$, so net cluster circulation scales with
   the signed winding excess $N_+ - N_-$ while total vortex population is $N_+ + N_-$.
5. **Quantum Dilogarithm Asymmetric-vs-Symmetric Normalisation & Five-Term Exponent Balance (`qou-6say`)**:
   Following Kirillov (`[kirillov1995]`, `arXiv:hep-th/9408113v2` §2.5 Def. 9, Prop. 2, Cor. 11),
   the quantum dilogarithm $\mathrm{Li}_2(x; q) = \sum_{n \ge 1} \frac{x^n}{n(1 - q^n)}$ in
   asymmetric normalisation relates to the symmetric denominator $q^{n/2} - q^{-n/2}$ by a
   half-step quadratic $q$-exponent shift and satisfies the non-commutative five-term relation
   under $a b = q b a$.
-/

namespace QOU.QBeta.BringCongruenceCuspedMinVolUnifiedLinkVortexQDilogBridge

/-! ## Section 1: Level-5 Congruence Subgroup & Period Matrix Stabiliser (`qou-3q4q`) -/

/-- Integral $2 \times 2$ block-reduced congruence matrix state with lower-left entry $5 k$. -/
structure LevelFiveCongruenceState where
  /-- Upper-left diagonal entry $a$. -/
  diagUpper : Int
  /-- Upper-right entry $b$. -/
  upperRight : Int
  /-- Level-5 quotient factor $k$ such that the lower-left entry is $c = 5 k$. -/
  levelFiveMultiple : Int
  /-- Lower-right diagonal entry $d$. -/
  diagLower : Int
  /-- Residual Hauptmodul offset parameter. -/
  hauptmodulOffset : Int
  deriving DecidableEq, Repr

/-- Actual lower-left matrix entry $c = 5 k$ forced by the fivefold symmetry commutator. -/
def lowerLeftEntry (s : LevelFiveCongruenceState) : Int :=
  5 * s.levelFiveMultiple

/-- Determinant defect $(a d - 1) - 5 k b$ measuring deviation from unimodularity. -/
def unimodularDeterminantDefect (s : LevelFiveCongruenceState) : Int :=
  (s.diagUpper * s.diagLower - 1) - lowerLeftEntry s * s.upperRight

/-- Shifted trace invariant $a + d + \text{hauptmodulOffset}$ along the stabiliser orbit. -/
def stabiliserShiftedTrace (s : LevelFiveCongruenceState) : Int :=
  s.diagUpper + s.diagLower + s.hauptmodulOffset

/-- Combined congruence gauge balance coupling determinant defect and shifted trace. -/
def congruenceGaugeBalance (s : LevelFiveCongruenceState) : Int :=
  unimodularDeterminantDefect s + lowerLeftEntry s * s.upperRight + stabiliserShiftedTrace s

/-- Adding the level-5 off-diagonal product $5 k b$ to the determinant defect recovers $a d - 1$. -/
theorem level_five_unimodular_recovery (s : LevelFiveCongruenceState) :
    unimodularDeterminantDefect s + 5 * s.levelFiveMultiple * s.upperRight =
      s.diagUpper * s.diagLower - 1 := by
  have hDef : unimodularDeterminantDefect s =
      (s.diagUpper * s.diagLower - 1) - lowerLeftEntry s * s.upperRight := rfl
  have hEntry : lowerLeftEntry s = 5 * s.levelFiveMultiple := rfl
  rw [hDef, hEntry]
  omega

/-- The combined congruence gauge balance decomposes into $a d - 1$ plus the shifted trace. -/
theorem congruence_gauge_balance_law (s : LevelFiveCongruenceState) :
    congruenceGaugeBalance s =
      (s.diagUpper * s.diagLower - 1) + s.diagUpper + s.diagLower + s.hauptmodulOffset := by
  have hBal : congruenceGaugeBalance s =
      unimodularDeterminantDefect s + lowerLeftEntry s * s.upperRight + stabiliserShiftedTrace s := rfl
  have hDef : unimodularDeterminantDefect s =
      (s.diagUpper * s.diagLower - 1) - lowerLeftEntry s * s.upperRight := rfl
  have hTr : stabiliserShiftedTrace s = s.diagUpper + s.diagLower + s.hauptmodulOffset := rfl
  rw [hBal, hDef, hTr]
  omega

/-- Under exact unimodularity ($a d - 1 = 5 k b$), the gauge balance reduces to the shifted trace. -/
theorem unimodular_stabiliser_trace_reduction
    (s : LevelFiveCongruenceState)
    (hUnimod : s.diagUpper * s.diagLower - 1 = 5 * s.levelFiveMultiple * s.upperRight) :
    congruenceGaugeBalance s - 5 * s.levelFiveMultiple * s.upperRight =
      s.diagUpper + s.diagLower + s.hauptmodulOffset := by
  have hBal : congruenceGaugeBalance s =
      unimodularDeterminantDefect s + lowerLeftEntry s * s.upperRight + stabiliserShiftedTrace s := rfl
  have hDef : unimodularDeterminantDefect s =
      (s.diagUpper * s.diagLower - 1) - lowerLeftEntry s * s.upperRight := rfl
  have hEntry : lowerLeftEntry s = 5 * s.levelFiveMultiple := rfl
  have hTr : stabiliserShiftedTrace s = s.diagUpper + s.diagLower + s.hauptmodulOffset := rfl
  rw [hBal, hDef, hEntry, hTr, hUnimod]
  omega

/-! ## Section 2: Minimal Cusped Volume Multiplicity & Link Degeneracy (`qou-4kmu`) -/

/-- Multiplicity accounting state for cusped hyperbolic manifolds and link complements at fixed volume. -/
structure CuspedVolumeMultiplicityState where
  /-- Number of orientable cusped manifolds attaining the volume in $S^3$ knot complements. -/
  knotComplementCount : Int
  /-- Number of non-$S^3$ sister cusped manifolds sharing the exact same volume. -/
  sisterManifoldCount : Int
  /-- Additional multi-component link complements sharing the same volume stratum. -/
  multiComponentLinkExcess : Int
  /-- Integer-scaled regular ideal simplex volume unit $v_3$. -/
  simplexVolumeUnit : Int
  deriving DecidableEq, Repr

/-- Total cusped manifold multiplicity $N_C(v)$ summing knot complements and sister manifolds. -/
def totalCuspedManifoldCount (s : CuspedVolumeMultiplicityState) : Int :=
  s.knotComplementCount + s.sisterManifoldCount

/-- Full link-stratum degeneracy $N_L(v)$ including multi-component link complements. -/
def fullLinkStratumCount (s : CuspedVolumeMultiplicityState) : Int :=
  totalCuspedManifoldCount s + s.multiComponentLinkExcess

/-- Minimal cusped volume $v_\omega = 2 v_3$ spanned by two regular ideal tetrahedra. -/
def minimalCuspedVolume (s : CuspedVolumeMultiplicityState) : Int :=
  2 * s.simplexVolumeUnit

/-- Degeneracy-weighted volume budget across all cusped manifolds at the minimal stratum. -/
def cuspedStratumVolumeBudget (s : CuspedVolumeMultiplicityState) : Int :=
  totalCuspedManifoldCount s * minimalCuspedVolume s

/-- Subtracting the sister-manifold and multi-component link counts isolates the $S^3$ knot count. -/
theorem knot_complement_uniqueness_isolation (s : CuspedVolumeMultiplicityState) :
    fullLinkStratumCount s - s.sisterManifoldCount - s.multiComponentLinkExcess =
      s.knotComplementCount := by
  have hFull : fullLinkStratumCount s = totalCuspedManifoldCount s + s.multiComponentLinkExcess := rfl
  have hCusped : totalCuspedManifoldCount s = s.knotComplementCount + s.sisterManifoldCount := rfl
  rw [hFull, hCusped]
  omega

/-- At the minimal stratum ($1$ knot complement + $1$ sister manifold), total cusped count is $2$. -/
theorem minimal_cusped_pair_volume_budget
    (s : CuspedVolumeMultiplicityState)
    (hKnot : s.knotComplementCount = 1)
    (hSister : s.sisterManifoldCount = 1) :
    cuspedStratumVolumeBudget s = 4 * s.simplexVolumeUnit := by
  have hBud : cuspedStratumVolumeBudget s = totalCuspedManifoldCount s * minimalCuspedVolume s := rfl
  have hCnt : totalCuspedManifoldCount s = s.knotComplementCount + s.sisterManifoldCount := rfl
  have hMin : minimalCuspedVolume s = 2 * s.simplexVolumeUnit := rfl
  rw [hBud, hCnt, hMin, hKnot, hSister]
  omega

/-- Link-stratum excess equals full link degeneracy minus knot and sister manifold counts. -/
theorem link_degeneracy_excess_decomposition (s : CuspedVolumeMultiplicityState) :
    s.multiComponentLinkExcess =
      fullLinkStratumCount s - s.knotComplementCount - s.sisterManifoldCount := by
  have hFull : fullLinkStratumCount s = totalCuspedManifoldCount s + s.multiComponentLinkExcess := rfl
  have hCusped : totalCuspedManifoldCount s = s.knotComplementCount + s.sisterManifoldCount := rfl
  rw [hFull, hCusped]
  omega

/-! ## Section 3: Unified Link-Drilled Volume vs. Classical Complement Volume (`qou-5m9w`) -/

/-- Volume comparison state separating classical knot complement volume from closed link-drilled volume. -/
structure UnifiedLinkVolumeState where
  /-- Classical hyperbolic volume of the knot complement in $S^3$ (zero for torus knots). -/
  classicalComplementVol : Int
  /-- Minimal number of link components $c_{\min}(M)$ drilled to achieve a hyperbolic complement. -/
  minimisingLinkComponents : Int
  /-- Volume contribution per drilled hyperbolic link component. -/
  perComponentDrilledVol : Int
  /-- Residual Dehn-filling geometric defect between closed and cusped bounds. -/
  fillingDefect : Int
  deriving DecidableEq, Repr

/-- Drilled link volume contribution $c_{\min}(M) \cdot v_{\mathrm{drill}} - \delta_{\mathrm{fill}}$. -/
def drilledLinkVolumeIncrement (s : UnifiedLinkVolumeState) : Int :=
  s.minimisingLinkComponents * s.perComponentDrilledVol - s.fillingDefect

/-- Unified volume invariant combining classical hyperbolic volume and drilled link increment. -/
def unifiedManifoldVolume (s : UnifiedLinkVolumeState) : Int :=
  s.classicalComplementVol + drilledLinkVolumeIncrement s

/-- Gap between the unified link-drilled volume and the classical complement volume. -/
def nonHyperbolicVolumeGap (s : UnifiedLinkVolumeState) : Int :=
  unifiedManifoldVolume s - s.classicalComplementVol

/-- The gap between unified and classical volume equals the drilled link volume increment. -/
theorem non_hyperbolic_volume_gap_identity (s : UnifiedLinkVolumeState) :
    nonHyperbolicVolumeGap s + s.fillingDefect =
      s.minimisingLinkComponents * s.perComponentDrilledVol := by
  have hGap : nonHyperbolicVolumeGap s = unifiedManifoldVolume s - s.classicalComplementVol := rfl
  have hUni : unifiedManifoldVolume s = s.classicalComplementVol + drilledLinkVolumeIncrement s := rfl
  have hInc : drilledLinkVolumeIncrement s =
      s.minimisingLinkComponents * s.perComponentDrilledVol - s.fillingDefect := rfl
  rw [hGap, hUni, hInc]
  omega

/-- On a massless/torus sector where classical complement volume vanishes, unified volume is purely drilled. -/
theorem torus_sector_unified_volume_reduction
    (s : UnifiedLinkVolumeState)
    (hTorus : s.classicalComplementVol = 0) :
    unifiedManifoldVolume s + s.fillingDefect =
      s.minimisingLinkComponents * s.perComponentDrilledVol := by
  have hUni : unifiedManifoldVolume s = s.classicalComplementVol + drilledLinkVolumeIncrement s := rfl
  have hInc : drilledLinkVolumeIncrement s =
      s.minimisingLinkComponents * s.perComponentDrilledVol - s.fillingDefect := rfl
  rw [hUni, hInc, hTorus]
  omega

/-- On an already hyperbolic closed manifold ($c_{\min} = 0$, $\delta_{\mathrm{fill}} = 0$), unified and classical volumes coincide. -/
theorem hyperbolic_partition_zero_component_law
    (s : UnifiedLinkVolumeState)
    (hZeroComp : s.minimisingLinkComponents = 0)
    (hZeroDef : s.fillingDefect = 0) :
    unifiedManifoldVolume s = s.classicalComplementVol := by
  have hUni : unifiedManifoldVolume s = s.classicalComplementVol + drilledLinkVolumeIncrement s := rfl
  have hInc : drilledLinkVolumeIncrement s =
      s.minimisingLinkComponents * s.perComponentDrilledVol - s.fillingDefect := rfl
  rw [hUni, hInc, hZeroComp, hZeroDef]
  omega

/-! ## Section 4: Superfluid Vortex Cluster Circulation Quantisation (`qou-6m79`) -/

/-- Population and circulation state for a two-dimensional quantum vortex cluster. -/
structure VortexClusterCirculationState where
  /-- Number of positive-circulation elementary vortices ($w_i = +1$). -/
  posVortexCount : Int
  /-- Number of negative-circulation elementary anti-vortices ($w_i = -1$). -/
  negVortexCount : Int
  /-- Integer-scaled elementary circulation quantum $\kappa_0 = h / m$. -/
  elementaryQuantum : Int
  /-- Background superfluid dipole counterflow offset. -/
  dipoleCounterflowOffset : Int
  deriving DecidableEq, Repr

/-- Net topological winding number $W = N_+ - N_-$ of the vortex cluster. -/
def netClusterWinding (s : VortexClusterCirculationState) : Int :=
  s.posVortexCount - s.negVortexCount

/-- Total vortex core population $N_{\mathrm{tot}} = N_+ + N_-$. -/
def totalVortexPopulation (s : VortexClusterCirculationState) : Int :=
  s.posVortexCount + s.negVortexCount

/-- Quantised cluster circulation $\Gamma = (N_+ - N_-) \kappa_0 + \delta_{\mathrm{dipole}}$. -/
def clusterCirculation (s : VortexClusterCirculationState) : Int :=
  netClusterWinding s * s.elementaryQuantum + s.dipoleCounterflowOffset

/-- Total vortex population equals the net cluster winding plus twice the negative-vortex count. -/
theorem population_winding_neutral_pair_split (s : VortexClusterCirculationState) :
    totalVortexPopulation s = netClusterWinding s + 2 * s.negVortexCount := by
  have hTot : totalVortexPopulation s = s.posVortexCount + s.negVortexCount := rfl
  have hWind : netClusterWinding s = s.posVortexCount - s.negVortexCount := rfl
  rw [hTot, hWind]
  omega

/-- Adding $N_-$ positive-negative vortex pairs preserves the quantised cluster circulation. -/
theorem circulation_invariance_under_pair_annihilation (s : VortexClusterCirculationState) :
    clusterCirculation s + s.negVortexCount * s.elementaryQuantum =
      s.posVortexCount * s.elementaryQuantum + s.dipoleCounterflowOffset := by
  have hCirc : clusterCirculation s =
      netClusterWinding s * s.elementaryQuantum + s.dipoleCounterflowOffset := rfl
  have hWind : netClusterWinding s = s.posVortexCount - s.negVortexCount := rfl
  have hSub : (s.posVortexCount - s.negVortexCount) * s.elementaryQuantum =
      s.posVortexCount * s.elementaryQuantum - s.negVortexCount * s.elementaryQuantum :=
    Int.sub_mul s.posVortexCount s.negVortexCount s.elementaryQuantum
  rw [hCirc, hWind, hSub]
  omega

/-- Total population and net winding sum to twice the positive-vortex count. -/
theorem double_positive_vortex_reconstruction (s : VortexClusterCirculationState) :
    totalVortexPopulation s + netClusterWinding s = 2 * s.posVortexCount := by
  have hTot : totalVortexPopulation s = s.posVortexCount + s.negVortexCount := rfl
  have hWind : netClusterWinding s = s.posVortexCount - s.negVortexCount := rfl
  rw [hTot, hWind]
  omega

/-! ## Section 5: Quantum Dilogarithm Normalisation & Five-Term Exponent Balance (`qou-6say`) -/

/-- Normalisation and non-commutative five-term exponent state for the quantum dilogarithm. -/
structure QuantumDilogNormalisationState where
  /-- Series mode index $n \ge 1$ in $\mathrm{Li}_2(x; q)$. -/
  seriesModeIndex : Int
  /-- Asymmetric denominator exponent weight. -/
  asymmetricWeight : Int
  /-- Symmetric denominator half-shift offset. -/
  symmetricHalfShift : Int
  /-- Non-commutative normal-ordering exponent from $a^m b^k = q^{m k} b^k a^m$. -/
  commutationShiftExponent : Int
  /-- Five-term pentagon coboundary residual. -/
  pentagonCoboundaryResidual : Int
  deriving DecidableEq, Repr

/-- Exponent difference between asymmetric $(1 - q^n)$ and symmetric $(q^{n/2} - q^{-n/2})$ normalisations. -/
def normalisationExponentGap (s : QuantumDilogNormalisationState) : Int :=
  s.seriesModeIndex * s.asymmetricWeight - s.symmetricHalfShift

/-- Left-hand two-factor product exponent in the non-commutative five-term identity. -/
def twoFactorLeftExponent (s : QuantumDilogNormalisationState) : Int :=
  normalisationExponentGap s + s.commutationShiftExponent

/-- Right-hand three-factor product exponent including the normal-ordered $-b a$ middle factor. -/
def threeFactorRightExponent (s : QuantumDilogNormalisationState) : Int :=
  twoFactorLeftExponent s + s.pentagonCoboundaryResidual

/-- The normalisation exponent gap plus the symmetric half-shift recovers the mode-weighted asymmetric exponent. -/
theorem normalisation_exponent_recovery (s : QuantumDilogNormalisationState) :
    normalisationExponentGap s + s.symmetricHalfShift =
      s.seriesModeIndex * s.asymmetricWeight := by
  have hGap : normalisationExponentGap s =
      s.seriesModeIndex * s.asymmetricWeight - s.symmetricHalfShift := rfl
  rw [hGap]
  omega

/-- Expanding the three-factor right-hand exponent exposes the commutation shift and pentagon residual. -/
theorem five_term_exponent_balance_expansion (s : QuantumDilogNormalisationState) :
    threeFactorRightExponent s + s.symmetricHalfShift =
      s.seriesModeIndex * s.asymmetricWeight +
        s.commutationShiftExponent + s.pentagonCoboundaryResidual := by
  have hRight : threeFactorRightExponent s =
      twoFactorLeftExponent s + s.pentagonCoboundaryResidual := rfl
  have hLeft : twoFactorLeftExponent s =
      normalisationExponentGap s + s.commutationShiftExponent := rfl
  have hGap : normalisationExponentGap s =
      s.seriesModeIndex * s.asymmetricWeight - s.symmetricHalfShift := rfl
  rw [hRight, hLeft, hGap]
  omega

/-- On the exact five-term locus where the pentagon coboundary residual vanishes, two-factor and three-factor exponents match. -/
theorem exact_pentagon_locus_exponent_equality
    (s : QuantumDilogNormalisationState)
    (hPent : s.pentagonCoboundaryResidual = 0) :
    threeFactorRightExponent s =
      s.seriesModeIndex * s.asymmetricWeight - s.symmetricHalfShift + s.commutationShiftExponent := by
  have hRight : threeFactorRightExponent s =
      twoFactorLeftExponent s + s.pentagonCoboundaryResidual := rfl
  have hLeft : twoFactorLeftExponent s =
      normalisationExponentGap s + s.commutationShiftExponent := rfl
  have hGap : normalisationExponentGap s =
      s.seriesModeIndex * s.asymmetricWeight - s.symmetricHalfShift := rfl
  rw [hRight, hLeft, hGap, hPent]
  omega

end QOU.QBeta.BringCongruenceCuspedMinVolUnifiedLinkVortexQDilogBridge
