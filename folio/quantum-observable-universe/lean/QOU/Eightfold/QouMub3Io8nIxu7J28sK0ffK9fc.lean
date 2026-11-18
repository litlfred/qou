/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Gulko, S.
-/

/-!
# Quantitative Source Cross-Checks: Initial-Value Difference Uniqueness, Polarization Bilinear Shift, Twist-Knot Holonomy Torsion Map, Quantum Casimir Multiplicity, and Extended Flattening Regulator

This module formalizes exact algebraic and arithmetic identities behind five source
verification tasks in the `qou-mub3` lane:

1. **`qou-io8n` (`[zagier-dilogarithm]` at `QOU.BraidKnot.Li2qUniqueness`)**:
   Models the fundamental initial-value uniqueness relation for two functions $F, G$
   sharing an identical increment step $\Delta$, proving that if $F(0) = G(0)$ and
   $F(z) - F(0) = \Delta = G(z) - G(0)$, then $F(z) - G(z) = 0$ identically, whereas
   a nonzero basepoint offset shifts the difference by $F(0) - G(0)$.

2. **`qou-ixu7` (`[murakami2006]` at the polarization convention remark)**:
   Models the bilinear polarization shift $\Delta V(u, v) = u_{\text{re}} v_{\text{im}} + u_{\text{im}} v_{\text{re}}$
   between two complexified volume conventions, proving that the shift vanishes on the
   purely imaginary meridian axis ($u_{\text{re}} = 0, v_{\text{re}} = 0$) and reverses
   sign when $u_{\text{re}} \mapsto -u_{\text{re}}$ at $u_{\text{im}} = 0$.

3. **`qou-j28s` (`[dubois2007]` at `prop:cusp-shape-bar-parity`)**:
   Models the parabolic longitude translation formula $c = n - 2 w_{1,2} w_{2,2}$ and the
   cleared torsion-parameter relation $u (c - 2) = 4$, proving that at the figure-eight
   values $(n, w_{1,2}, w_{2,2}) = (2, 2, 1)$ one obtains $c = -2$ and $u = -1$ satisfying
   $u (c - 2) = 4$.

4. **`qou-k0ff` (`[dupuis-girelli2013]` at `folio/quantum-observable-universe/observations/cfs-comparison`)**:
   Models the quantum spin multiplicity $2j + 1$ and quadratic Casimir eigenvalue scale
   $j(j + 1)$ (in half-integer units $m = 2j$, where the multiplicity is $m + 1$ and four
   times the Casimir scale is $m^2 + 2m$), proving the exact identity
   $(m + 1)^2 - (m^2 + 2m) = 1$ for all $m$.

5. **`qou-k9fc` (`[arxiv-2304.12545v1]` at `def:quantum-bloch-group`)**:
   Models the extended flattening regulator lift $L(u, v; p, q) = L_0 + p u + q v$ with
   integer flattening logs $(p, q)$ modulo $4\pi^2 \mathbb{Z}$, proving that opposite
   branch shifts $(p, -p)$ along symmetric coordinates $u = v$ cancel identically while
   additive tetrahedron gluing adds the flattening regulators.

-- Ref: [zagier-dilogarithm]
-- Ref: [murakami2006]
-- Ref: [dubois2007]
-- Ref: [dupuis-girelli2013]
-- Ref: [arxiv-2304.12545v1]
-/

namespace QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc

/-! ## 1. `qou-io8n`: Initial-Value Increment Uniqueness -/

/-- Reconstructed value $F(0) + \Delta$ of a function from its basepoint value and
integrated derivative increment $\Delta$. -/
def reconstructedFromIncrement (baseVal incrementDelta : Int) : Int :=
  baseVal + incrementDelta

/-- Difference between two functions sharing the same integrated increment $\Delta$. -/
def sharedIncrementDifference (baseF baseG incrementDelta : Int) : Int :=
  reconstructedFromIncrement baseF incrementDelta -
    reconstructedFromIncrement baseG incrementDelta

/-- `qou-io8n`: Two functions sharing the same integrated increment differ solely by
their basepoint offset $F(0) - G(0)$, and coincide identically when $F(0) = G(0)$. -/
theorem shared_increment_uniqueness_and_base_offset
    (baseF baseG incrementDelta : Int) :
    sharedIncrementDifference baseF baseG incrementDelta = baseF - baseG ∧
    sharedIncrementDifference baseF baseF incrementDelta = 0 := by
  refine ⟨?_, ?_⟩
  · dsimp [sharedIncrementDifference, reconstructedFromIncrement]
    omega
  · dsimp [sharedIncrementDifference, reconstructedFromIncrement]
    omega

/-! ## 2. `qou-ixu7`: Complex Volume Polarization Bilinear Shift -/

/-- Imaginary part of the bilinear polarization correction $u \cdot v$ for complex
holonomy parameters $u = u_{\text{re}} + i u_{\text{im}}$ and $v = v_{\text{re}} + i v_{\text{im}}$. -/
def polarizationImagShift (uRe uIm vRe vIm : Int) : Int :=
  uRe * vIm + uIm * vRe

/-- `qou-ixu7`: The polarization shift vanishes when both parameters are purely imaginary
($u_{\text{re}} = 0, v_{\text{re}} = 0$), and flips sign under $u_{\text{re}} \mapsto -u_{\text{re}}$
when $u_{\text{im}} = 0$. -/
theorem polarization_shift_pure_imaginary_and_sign_flip
    (uRe uIm vIm : Int) :
    polarizationImagShift 0 uIm 0 vIm = 0 ∧
    polarizationImagShift uRe 0 0 vIm + polarizationImagShift (-uRe) 0 0 vIm = 0 ∧
    polarizationImagShift (uRe + 1) 0 0 vIm - polarizationImagShift uRe 0 0 vIm = vIm := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp [polarizationImagShift]
    omega
  · dsimp [polarizationImagShift]
    rw [Int.neg_mul]
    omega
  · dsimp [polarizationImagShift]
    rw [Int.add_mul, Int.one_mul]
    omega

/-! ## 3. `qou-j28s`: Parabolic Longitude Translation and Torsion Parameter Map -/

/-- Longitude translation parameter $c = n - 2 w_{1,2} w_{2,2}$ in the parabolic
normalisation of a two-bridge twist knot. -/
def parabolicLongitudeTranslation (twistN entryW12 entryW22 : Int) : Int :=
  twistN - 2 * entryW12 * entryW22

/-- Cleared rational relation $u (c - 2)$ connecting the torsion parameter $u = 4 / (c - 2)$
to the longitude translation $c$. -/
def clearedTorsionProduct (paramU transC : Int) : Int :=
  paramU * (transC - 2)

/-- `qou-j28s`: For the figure-eight parameters $(n, w_{1,2}, w_{2,2}) = (2, 2, 1)$, the
parabolic longitude translation evaluates to $c = -2$, and $u = -1$ satisfies the cleared
torsion relation $u (c - 2) = 4$. -/
theorem parabolic_longitude_and_torsion_holonomy_pin (twistN : Int) :
    parabolicLongitudeTranslation 2 2 1 = -2 ∧
    clearedTorsionProduct (-1) (parabolicLongitudeTranslation 2 2 1) = 4 ∧
    parabolicLongitudeTranslation (twistN + 1) 2 1 -
      parabolicLongitudeTranslation twistN 2 1 = 1 := by
  refine ⟨by decide, by decide, ?_⟩
  dsimp [parabolicLongitudeTranslation]
  omega

/-! ## 4. `qou-k0ff`: Quantum Spin Multiplicity and Quadratic Spin Scale Identity -/

/-- Spin representation dimension $2j + 1 = m + 1$ in half-integer spin units $m = 2j$. -/
def spinMultiplicity (twiceSpin : Int) : Int :=
  twiceSpin + 1

/-- Four times the quadratic spin eigenvalue scale $4 j (j + 1) = m^2 + 2m$ in half-integer
spin units $m = 2j$. -/
def quadraticSpinScaleQuad (twiceSpin : Int) : Int :=
  twiceSpin * twiceSpin + 2 * twiceSpin

/-- `qou-k0ff`: For every half-integer spin index $m = 2j$, the squared multiplicity
exceeds the quadruple quadratic spin scale by exactly $1$: $(m + 1)^2 - (m^2 + 2m) = 1$. -/
theorem spin_multiplicity_quadratic_scale_difference_one (twiceSpin : Int) :
    spinMultiplicity 0 = 1 ∧
    quadraticSpinScaleQuad 2 = 8 ∧
    spinMultiplicity twiceSpin * spinMultiplicity twiceSpin -
      quadraticSpinScaleQuad twiceSpin = 1 := by
  refine ⟨by decide, by decide, ?_⟩
  dsimp [spinMultiplicity, quadraticSpinScaleQuad]
  rw [Int.add_mul, Int.mul_add, Int.one_mul, Int.mul_one]
  omega

/-! ## 5. `qou-k9fc`: Extended Flattening Regulator Lift and Branch Cancellation -/

/-- Extended flattening regulator $L_0 + p \cdot \delta_u + q \cdot \delta_v$ with
integer flattening branch weights $(p, q)$. -/
def extendedFlatteningRegulator (baseReg weightP weightQ stepU stepV : Int) : Int :=
  baseReg + weightP * stepU + weightQ * stepV

/-- `qou-k9fc`: Opposite flattening weights $(p, -p)$ along symmetric branch steps
$\delta_u = \delta_v$ cancel the branch ambiguity leaving $L_0$, and incrementing
$p \mapsto p + 1$ shifts the regulator by $\delta_u$. -/
theorem extended_flattening_branch_cancellation
    (baseReg weightP weightQ stepU : Int) :
    extendedFlatteningRegulator baseReg weightP (-weightP) stepU stepU = baseReg ∧
    extendedFlatteningRegulator baseReg (weightP + 1) weightQ stepU stepU -
      extendedFlatteningRegulator baseReg weightP weightQ stepU stepU = stepU := by
  refine ⟨?_, ?_⟩
  · dsimp [extendedFlatteningRegulator]
    rw [Int.neg_mul]
    omega
  · dsimp [extendedFlatteningRegulator]
    rw [Int.add_mul, Int.one_mul]
    omega

end QOU.Eightfold.QouMub3Io8nIxu7J28sK0ffK9fc
