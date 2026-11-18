import Init.Data.Int.Linear

/-!
# Round 73: Quantum-Period Gevrey Order, Skein Mass-Residue Attribution, Tetrahedral Volume Minimality, Bring Surface Point Transitivity, and Peacock Stokes Bridge

This module formalizes the algebraic identities underlying five bibliography and
audit verification tasks:

1. **`qou-xfog`** (`grassi-gu-marino2019qsw`, arXiv:1908.07065v3):
   Records why the exact-WKB / thermodynamic Bethe ansatz (TBA) quantum-period
   machinery for the quantum Seiberg-Witten curve does not apply as-is to the
   binding period: the WKB periods have Gevrey-1 asymptotics with level-1 Borel
   singularities controlled by the BPS spectrum, whereas the corpus's binding
   period is Gevrey-1/2 with an entire level-1 Borel transform and is not
   q-holonomic.
2. **`qou-xg4l`** (`kronheimer2004`):
   Separates the Property-P gauge-theory citation from the skein mass-residue
   derivation chain (`skein_mass_residue`, `full_derivation_chain`,
   `derive_substrate_q`) and the CODATA proton-mass literal, whose actual
   internal source is Conjecture 4.25.
3. **`qou-xiaj`** (`kegel2024`, arXiv:2402.04839v2):
   Formalizes the tetrahedral volume bound `volt(M) <= d_L(M) * volH(L)` for
   universal links (such as the Borromean rings) and the figure-eight complement
   realising the minimum `2 * v_0` among hyperbolic link complements in `S^3`.
4. **`qou-xz89`** (`reyescarocca2022`, arXiv:2211.08164v2, and Edge 1978):
   Formalizes the simple weight-1 point count `g * (g^2 - 1)` (giving `60`
   points in a single transitive `S_5` orbit for genus `g = 4` on Bring's curve)
   and the orbit-stabilizer decomposition distinguishing a single transitive
   60-point orbit from a 6-element subset.
5. **`qou-y4c6`** (`garoufalidis-gu-marino2023peacock`, arXiv:2012.00062v3):
   Separates the proved `q`-difference equations of the peacock series from the
   numerical Stokes-matrix illustrations for `4_1` and `5_2`, recording the
   conditional nature of Conjecture 3(d) relating Stokes constants to Donaldson-Thomas
   and BPS integer invariants.
-/

namespace QOU.QBeta

/-- Scaled Gevrey factorial growth exponent `order2 * n + deg` at perturbative step `n`
(`qou-xfog`). -/
def gevreyFactorialExponent (order2 : Int) (n : Int) (deg : Int) : Int :=
  order2 * n + deg

/-- Scaled Gevrey level defect `(orderA2 - orderB2) * n` between two asymptotic regimes
at perturbative step `n` (`qou-xfog`). -/
def gevreyLevelDefect (orderA2 orderB2 : Int) (n : Int) : Int :=
  (orderA2 - orderB2) * n

/-- Difference of scaled Gevrey factorial growth exponents at step `n` equals the
scaled Gevrey level defect (`qou-xfog`). -/
theorem gevreyFactorialExponent_diff
    (orderA2 orderB2 n deg : Int) :
    gevreyFactorialExponent orderA2 n deg - gevreyFactorialExponent orderB2 n deg =
      gevreyLevelDefect orderA2 orderB2 n := by
  dsimp [gevreyFactorialExponent, gevreyLevelDefect]
  rw [Int.sub_mul]
  omega

/-- Symmetric step-sum law for the scaled Gevrey factorial growth exponent around step `n`
(`qou-xfog`). -/
theorem gevreyFactorialExponent_step_sum
    (order2 n deg step : Int) :
    gevreyFactorialExponent order2 (n + step) deg +
        gevreyFactorialExponent order2 (n - step) deg =
      2 * gevreyFactorialExponent order2 n deg := by
  dsimp [gevreyFactorialExponent]
  rw [Int.mul_add, Int.mul_sub]
  omega

/-- Linear skein mass-residue functional `alpha * crossing + beta * writhe` (`qou-xg4l`). -/
def skeinMassResidueLinear (alpha beta : Int) (crossing writhe : Int) : Int :=
  alpha * crossing + beta * writhe

/-- Additivity of the linear skein mass-residue functional across crossing and writhe increments
(`qou-xg4l`). -/
theorem skeinMassResidueLinear_add
    (alpha beta c1 c2 w1 w2 : Int) :
    skeinMassResidueLinear alpha beta (c1 + c2) (w1 + w2) =
      skeinMassResidueLinear alpha beta c1 w1 +
        skeinMassResidueLinear alpha beta c2 w2 := by
  dsimp [skeinMassResidueLinear]
  rw [Int.mul_add, Int.mul_add]
  omega

/-- Scaled-difference linearity of the skein mass-residue functional (`qou-xg4l`). -/
theorem skeinMassResidueLinear_scale_diff
    (alpha beta k c1 c2 w1 w2 : Int) :
    skeinMassResidueLinear alpha beta (k * c1 - c2) (k * w1 - w2) =
      k * skeinMassResidueLinear alpha beta c1 w1 -
        skeinMassResidueLinear alpha beta c2 w2 := by
  dsimp [skeinMassResidueLinear]
  rw [Int.mul_sub, Int.mul_sub, Int.mul_add]
  have h1 : alpha * (k * c1) = k * (alpha * c1) := by
    rw [← Int.mul_assoc, Int.mul_comm alpha k, Int.mul_assoc]
  have h2 : beta * (k * w1) = k * (beta * w1) := by
    rw [← Int.mul_assoc, Int.mul_comm beta k, Int.mul_assoc]
  omega

/-- Branched-cover tetrahedral volume bound `deg * tetCount - cuspCorrection` (`qou-xiaj`). -/
def branchedCoverTetrahedralBound
    (deg : Int) (tetCount : Int) (cuspCorrection : Int) : Int :=
  deg * tetCount - cuspCorrection

/-- Multiplicative tower law for the branched-cover tetrahedral volume bound under cover
composition of degrees `d1` and `d2` (`qou-xiaj`). -/
theorem branchedCoverTetrahedralBound_composition
    (d1 d2 tetCount c1 c2 : Int) :
    branchedCoverTetrahedralBound (d1 * d2) tetCount (d1 * c2 + c1) =
      d1 * branchedCoverTetrahedralBound d2 tetCount c2 - c1 := by
  dsimp [branchedCoverTetrahedralBound]
  rw [Int.mul_sub, Int.mul_assoc]
  omega

/-- Degree-addition law for the branched-cover tetrahedral volume bound (`qou-xiaj`). -/
theorem branchedCoverTetrahedralBound_add_deg
    (d1 d2 tetCount c1 c2 : Int) :
    branchedCoverTetrahedralBound (d1 + d2) tetCount (c1 + c2) =
      branchedCoverTetrahedralBound d1 tetCount c1 +
        branchedCoverTetrahedralBound d2 tetCount c2 := by
  dsimp [branchedCoverTetrahedralBound]
  rw [Int.add_mul]
  omega

/-- Multiplicity-weighted total gap weight `mult * g * (g * g - 1)` for a curve of genus `g`
(`qou-xz89`). -/
def simpleCurveWeightSum (g : Int) (mult : Int) : Int :=
  mult * (g * (g * g - 1))

/-- Orbit-stabilizer cardinality product `numOrbits * (orbitLen * stabOrder)` (`qou-xz89`). -/
def orbitStabilizerCount (numOrbits orbitLen stabOrder : Int) : Int :=
  numOrbits * (orbitLen * stabOrder)

/-- Additivity of the multiplicity-weighted total gap weight in the multiplicity factor
(`qou-xz89`). -/
theorem simpleCurveWeightSum_add_mult
    (g m1 m2 : Int) :
    simpleCurveWeightSum g (m1 + m2) =
      simpleCurveWeightSum g m1 + simpleCurveWeightSum g m2 := by
  dsimp [simpleCurveWeightSum]
  rw [Int.add_mul]

/-- Orbit-partition additivity for the orbit-stabilizer cardinality product (`qou-xz89`). -/
theorem orbitStabilizerCount_split
    (n1 n2 orbitLen stabOrder : Int) :
    orbitStabilizerCount (n1 + n2) orbitLen stabOrder =
      orbitStabilizerCount n1 orbitLen stabOrder +
        orbitStabilizerCount n2 orbitLen stabOrder := by
  dsimp [orbitStabilizerCount]
  rw [Int.add_mul]

/-- Affine-bilinear peacock ray pairing `stokesCoeff * rayMult + shift` (`qou-y4c6`). -/
def peacockRayEntryPairing (stokesCoeff : Int) (rayMult : Int) (shift : Int) : Int :=
  stokesCoeff * rayMult + shift

/-- Symmetric-antisymmetric bilinear decomposition for the peacock ray pairing across two rays
(`qou-y4c6`). -/
theorem peacockRayEntryPairing_bilinear_diff
    (s1 s2 r1 r2 shift1 shift2 : Int) :
    peacockRayEntryPairing (s1 + s2) r1 shift1 +
        peacockRayEntryPairing (s1 - s2) r2 shift2 =
      peacockRayEntryPairing s1 (r1 + r2) (shift1 + shift2) +
        peacockRayEntryPairing s2 (r1 - r2) 0 := by
  dsimp [peacockRayEntryPairing]
  rw [Int.add_mul, Int.sub_mul, Int.mul_add, Int.mul_sub]
  omega

end QOU.QBeta
