/-!
# Round 70: Hyperbolic Green Kernel Decay, Conormal Signed Euler Characteristic, Type-B Folded Trace Bar-Invariance, Causal Eigenvalue Splitting, and Genus-1 Free Cumulant Decomposition

This module formalizes the finite-dimensional algebraic identities underlying five
source-citation audit items:

1. `qou-ut4e` (`[deturck-gluck2008]`, `parent: qou-aqfj`, `2026-08-01-em-linking-reads-round1.md`):
   On hyperbolic $3$-space $\mathbb{H}^3$, the scalar Green operator kernel is
   $\varphi_0(\alpha) = (-\frac{1}{4\pi})(\coth \alpha - 1)$ rather than $(-\frac{1}{4\pi})\coth \alpha$;
   subtracting the asymptotic unit constant removes the non-decaying baseline so the numerator
   $(\cosh \alpha - \sinh \alpha) = e^{-\alpha}$ decays at infinity, while the shifted Laplacian
   linking kernel is $\varphi(\alpha) = (-\frac{1}{4\pi})\operatorname{csch} \alpha$.
2. `qou-uwcc` (`[rossmann-invariant-eigendistributions-2]`, `parent: qou-19m0`, `alg:delta-lambda-closure`):
   For a conormal-variety homology decomposition with even-degree dimension $e_+$ and odd-degree
   dimension $e_-$, the signed Euler characteristic $\Delta_\lambda = e_+ - e_-$ and the total
   unsigned dimension $M_\lambda = e_+ + e_-$ satisfy $M_\lambda - \Delta_\lambda = 2 e_-$ and
   $M_\lambda + \Delta_\lambda = 2 e_+$.
3. `qou-v56q` (`[geck-lambropoulou-2004]`, `parent: qou-1qhv`, `conj:type-b-folding-cpt`):
   For a type-B folded trace functional parameterized by $(z, y_+, y_-)$ with weights $(a, b)$,
   bar-conjugation exchanges $(y_+, y_-) \mapsto (y_-, y_+)$; the bar-asymmetry defect is
   $(a - b)(y_+ - y_-)$, which vanishes identically when $a = b$.
4. `qou-vfl4` (`[finster2021]`, `parent: qou-vva9`, `rem:cfs-comparison-summary`):
   Causal-Lagrangian two-eigenvalue polarization $(\lambda_+ - \lambda_-)^2 + 4\lambda_+\lambda_- = (\lambda_+ + \lambda_-)^2$
   and quadratic-norm difference factorization $g^2 - s^2 = (g - s)(g + s)$.
5. `qou-vo5j` (`[sniady2006asymptotics]`, `parent: qou-19m0`, `QOU.BraidsAndKnots.DeltaLambdaDReduction`):
   Normalized character polynomial genus decomposition $\widehat{\Sigma}_3 = R_4 + R_2$ at $n = 4$:
   subtracting the genus-$0$ free cumulant term $R_4$ from $\widehat{\Sigma}_3$ isolates the genus-$1$
   correction $R_2$, and for $R_4(c) = c^3 - 3c$, $R_2(c) = 2c$ their sum factors as
   $c^3 - c = c(c - 1)(c + 1)$.
-/

namespace QOU.QBeta.HyperbolicGreenConormalFoldedTraceRound70

/-- `qou-ut4e`: Unshifted hyperbolic kernel numerator $u + v$ where $u = e^\alpha$ and $v = e^{-\alpha}$
represent the growing and decaying exponential modes of $\cosh \alpha$. -/
def hyperbolicKernelUnshiftedNumerator (u v : Int) : Int :=
  u + v

/-- `qou-ut4e`: Asymptotic baseline numerator $u - v$ corresponding to the unit floor $\sinh \alpha$. -/
def hyperbolicKernelAsymptoticBaseline (u v : Int) : Int :=
  u - v

/-- `qou-ut4e`: Subtracting the asymptotic baseline numerator $u - v$ from the unshifted numerator
$u + v$ cancels the growing mode $u$ and isolates $2v = 2e^{-\alpha}$, enforcing decay at infinity
(`[deturck-gluck2008]`). -/
theorem hyperbolicKernelSubtracted_isolates_decaying_mode (u v : Int) :
    hyperbolicKernelUnshiftedNumerator u v - hyperbolicKernelAsymptoticBaseline u v = 2 * v := by
  dsimp [hyperbolicKernelUnshiftedNumerator, hyperbolicKernelAsymptoticBaseline]
  omega

/-- `qou-uwcc`: Signed homology Euler characteristic $\Delta = e_+ - e_-$ of a conormal-variety
fiber with even-degree rank $e_+$ and odd-degree rank $e_-$. -/
def conormalSignedCharacteristic (eEven eOdd : Int) : Int :=
  eEven - eOdd

/-- `qou-uwcc`: Total unsigned homology multiplicity $M = e_+ + e_-$ of a conormal-variety fiber. -/
def conormalUnsignedMultiplicity (eEven eOdd : Int) : Int :=
  eEven + eOdd

/-- `qou-uwcc`: The difference between the unsigned homology multiplicity and the signed
characteristic equals twice the odd-degree rank $2 e_-$ (`[rossmann-invariant-eigendistributions-2]`). -/
theorem conormalUnsigned_sub_signed_eq_two_mul_odd (eEven eOdd : Int) :
    conormalUnsignedMultiplicity eEven eOdd - conormalSignedCharacteristic eEven eOdd = 2 * eOdd := by
  dsimp [conormalUnsignedMultiplicity, conormalSignedCharacteristic]
  omega

/-- `qou-v56q`: Type-B folded trace linear combination $z + a \cdot y_+ + b \cdot y_-$ with strand
parameter $z$ and signed loop parameters $(y_+, y_-)$. -/
def foldedTypeBTraceFunctional (z a b yPos yNeg : Int) : Int :=
  z + a * yPos + b * yNeg

/-- `qou-v56q`: Bar-conjugation asymmetry defect of a type-B folded trace under the involution
exchanging $(y_+, y_-) \mapsto (y_-, y_+)$. -/
def foldedTypeBBarAsymmetryDefect (z a b yPos yNeg : Int) : Int :=
  foldedTypeBTraceFunctional z a b yPos yNeg - foldedTypeBTraceFunctional z a b yNeg yPos

/-- `qou-v56q`: The bar-conjugation asymmetry defect factors as $(a - b)(y_+ - y_-)$, independent
of the base parameter $z$ (`[geck-lambropoulou-2004]`). -/
theorem foldedTypeBBarAsymmetryDefect_factored (z a b yPos yNeg : Int) :
    foldedTypeBBarAsymmetryDefect z a b yPos yNeg = (a - b) * (yPos - yNeg) := by
  dsimp [foldedTypeBBarAsymmetryDefect, foldedTypeBTraceFunctional]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
  omega

/-- `qou-v56q`: When the positive and negative loop weights are symmetric ($a = b$), the type-B
folded trace is strictly bar-invariant (`[geck-lambropoulou-2004]`). -/
theorem foldedTypeBBarAsymmetryDefect_symmetric_zero (z a yPos yNeg : Int) :
    foldedTypeBBarAsymmetryDefect z a a yPos yNeg = 0 := by
  rw [foldedTypeBBarAsymmetryDefect_factored]
  omega

/-- `qou-vfl4`: Causal-Lagrangian eigenvalue-difference squared $(\lambda_+ - \lambda_-)^2$. -/
def causalEigenvalueDifferenceSq (lamPos lamNeg : Int) : Int :=
  (lamPos - lamNeg) * (lamPos - lamNeg)

/-- `qou-vfl4`: Quadratic-norm difference $g^2 - s^2$ between two-point coupling amplitude $g$
and $L^1$ norm $s$. -/
def causalQuadraticNormDifference (g s : Int) : Int :=
  g * g - s * s

/-- `qou-vfl4`: Polarization identity relating the squared eigenvalue difference and determinant
term $4\lambda_+\lambda_-$ to the squared trace $(\lambda_+ + \lambda_-)^2$ (`[finster2021]`). -/
theorem causalEigenvalueDifferenceSq_polarization (lamPos lamNeg : Int) :
    causalEigenvalueDifferenceSq lamPos lamNeg + 4 * (lamPos * lamNeg) =
      (lamPos + lamNeg) * (lamPos + lamNeg) := by
  dsimp [causalEigenvalueDifferenceSq]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_comm lamNeg lamPos]
  omega

/-- `qou-vfl4`: Factorization of the quadratic-norm difference $g^2 - s^2 = (g - s)(g + s)$
(`[finster2021]`). -/
theorem causalQuadraticNormDifference_factored (g s : Int) :
    causalQuadraticNormDifference g s = (g - s) * (g + s) := by
  dsimp [causalQuadraticNormDifference]
  rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm s g]
  omega

/-- `qou-vo5j`: Genus-$0$ fourth free-cumulant polynomial $R_4(c) = c^3 - 3c$ evaluated on a
normalized cycle parameter $c$. -/
def freeCumulantGenusZeroR4 (c : Int) : Int :=
  c * c * c - 3 * c

/-- `qou-vo5j`: Genus-$1$ second free-cumulant correction $R_2(c) = 2c$ at $n = 4$. -/
def freeCumulantGenusOneR2 (c : Int) : Int :=
  2 * c

/-- `qou-vo5j`: Normalized character polynomial $\widehat{\Sigma}_3(c) = R_4(c) + R_2(c)$ at $n = 4$. -/
def normalizedCharacterSigmaHat3 (c : Int) : Int :=
  freeCumulantGenusZeroR4 c + freeCumulantGenusOneR2 c

/-- `qou-vo5j`: Combining the genus-$0$ term $R_4(c) = c^3 - 3c$ and the genus-$1$ correction
$R_2(c) = 2c$ yields the falling-factorial product $\widehat{\Sigma}_3(c) = c(c - 1)(c + 1)$
(`[sniady2006asymptotics]`). -/
theorem normalizedCharacterSigmaHat3_factored (c : Int) :
    normalizedCharacterSigmaHat3 c = c * (c - 1) * (c + 1) := by
  dsimp [normalizedCharacterSigmaHat3, freeCumulantGenusZeroR4, freeCumulantGenusOneR2]
  rw [Int.mul_sub, Int.mul_one, Int.mul_add, Int.mul_one, Int.sub_mul]
  omega

end QOU.QBeta.HyperbolicGreenConormalFoldedTraceRound70
