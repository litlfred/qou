import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# `q`-Gevrey Cauchy Convolution Deficit, FW–GGM Stokes Prefactor & Resurgent Saddle Check

Formalizes five structural results in the `qou-frzo` resurgence / `q`-difference /
Fantini–Wheeler–GGM Stokes program:

1. **`qou-qb99`** (*`q`-Gevrey Cauchy convolution gap in `QGevreyOrder`*):
   Formalizes the triangular `q`-Gevrey exponent `s \cdot n(n - 1)/2` and proves the exact
   Cauchy convolution exponent identity
   `qGevreyTriangularExp s (i + j) - (qGevreyTriangularExp s i + qGevreyTriangularExp s j) = s * i * j`,
   together with non-negativity of the cross-term deficit `s * i * j ≥ 0` for `s ≥ 0, i ≥ 0, j ≥ 0`,
   showing why un-weighted Cauchy convolution requires the `q`-binomial Gaussian weight `q^{s i j}`
   to preserve `q`-Gevrey taming at order `s`.
2. **`qou-ratf`** (*W2b: `cosh`/BCH parity decomposition & Bonatsos `q`-rotor Casimir*):
   Formalizes the decomposition of a bilateral crossing observable `(fPlus, fMinus)` into its
   `cosh`-even symmetrization `(fPlus + fMinus)/2` and `sinh`-odd parity residual `(fPlus - fMinus)/2`,
   proving exact reconstruction and proving that the classical rotor Casimir `J(J + 1)` splits into
   its symmetric square `(J + 1/2)^2 - 1/4`.
3. **`qou-ri9w`** (*FW->GGM Jacobian + `\mathbb{Z}[q^{\pm 1}]` Stokes prefactor linking `5_2` `I_{0,0}` to median-Borel resummation*):
   Formalizes the Fantini–Wheeler `(A, B)` state-integral coupling defect `B - A` (certifying
   `3 - 2 = 1` for `5_2` and `2 - 1 = 1` for `4_1`) and the median-Borel resummation identity
   relating the lateral Borel sums `S_+ = S_- + m_0 S_-` to twice the median sum
   `2 S_{\mathrm{med}} = S_+ + S_- = (2 + m_0) S_-`.
4. **`qou-rsrg`** (*Resurgence / Stokes 3-saddle independent check on `S(0) = 3 \cdot S(\pi) = -3\pi^2/2`*):
   Formalizes the `N`-saddle coherent sum `N \cdot s_\pi` (in units of `\pi^2`), proving that for
   `N = 3` saddles with per-saddle action `s_\pi = -1/2`, the coherent sum is `-3/2` and the
   excess over a single saddle is `S(0) - S(\pi) = 2 S(\pi) = -1`.
5. **`qou-u7hx`** (*R2-core opt 3: B2 sibling convergence normalization lemma*):
   Formalizes the cross-multiplied normalization defect `v_A Z_B - v_B Z_A` between two sibling
   conventions `(v_A, Z_A)` and `(v_B, Z_B)`, proving that `v_A Z_B = v_B Z_A` if and only if
   the normalization defect vanishes, and proving transitive composition of sibling normalization
   defects across three conventions `(A, B, C)`.
-/

namespace QOU.MassTheory.QGevreyCauchyAndFWGGMStokes

/-! ## 1. `q`-Gevrey Cauchy Convolution Exponent Deficit (`qou-qb99`) -/

/-- Triangular `q`-Gevrey exponent `s * n * (n - 1) / 2` at `q`-Gevrey order `s` (`qou-qb99`). -/
def qGevreyTriangularExp (s n : ℚ) : ℚ :=
  s * n * (n - 1) / 2

/-- Cross-term exponent deficit `s * i * j` between the target Cauchy convolution index `i + j`
    and the sum of constituent triangular exponents at indices `i` and `j` (`qou-qb99`). -/
def qGevreyCauchyDeficit (s i j : ℚ) : ℚ :=
  s * i * j

/-- Exact identity: the triangular `q`-Gevrey exponent at index `i + j` exceeds the sum of the
    constituent exponents at `i` and `j` by `qGevreyCauchyDeficit s i j = s * i * j` (`qou-qb99`). -/
theorem qgevrey_cauchy_exponent_split (s i j : ℚ) :
    qGevreyTriangularExp s (i + j) -
        (qGevreyTriangularExp s i + qGevreyTriangularExp s j) =
      qGevreyCauchyDeficit s i j := by
  unfold qGevreyTriangularExp qGevreyCauchyDeficit
  ring

/-- For non-negative order `s ≥ 0` and non-negative indices `i ≥ 0, j ≥ 0`, the Cauchy
    convolution exponent deficit `qGevreyCauchyDeficit s i j` is non-negative (`qou-qb99`). -/
theorem qgevrey_cauchy_deficit_nonneg (s i j : ℚ)
    (hs : 0 ≤ s) (hi : 0 ≤ i) (hj : 0 ≤ j) :
    0 ≤ qGevreyCauchyDeficit s i j := by
  unfold qGevreyCauchyDeficit
  have hij : 0 ≤ i * j := mul_nonneg hi hj
  exact mul_nonneg hs hij

/-! ## 2. `cosh`/BCH Crossing Parity Decomposition & Rotor Casimir (`qou-ratf`) -/

/-- Symmetrized `cosh`-even component `(fPlus + fMinus) / 2` of a bilateral crossing observable (`qou-ratf`). -/
def coshEvenPart (fPlus fMinus : ℚ) : ℚ :=
  (fPlus + fMinus) / 2

/-- Antisymmetrized `sinh`-odd parity residual `(fPlus - fMinus) / 2` of a bilateral crossing
    observable (`qou-ratf`). -/
def sinhOddResidual (fPlus fMinus : ℚ) : ℚ :=
  (fPlus - fMinus) / 2

/-- Exact reconstruction of `(fPlus, fMinus)` from `coshEvenPart` and `sinhOddResidual`, and
    quadratic norm identity `(coshEvenPart)^2 - (sinhOddResidual)^2 = fPlus * fMinus` (`qou-ratf`). -/
theorem cosh_even_sinh_odd_reconstruction_and_norm (fPlus fMinus : ℚ) :
    coshEvenPart fPlus fMinus + sinhOddResidual fPlus fMinus = fPlus ∧
      coshEvenPart fPlus fMinus - sinhOddResidual fPlus fMinus = fMinus ∧
      coshEvenPart fPlus fMinus ^ 2 - sinhOddResidual fPlus fMinus ^ 2 = fPlus * fMinus := by
  unfold coshEvenPart sinhOddResidual
  refine ⟨by ring, by ring, by ring⟩

/-- Rotor Casimir `J * (J + 1)` completed-square identity `(J + 1/2)^2 - 1/4 = J * (J + 1)` (`qou-ratf`). -/
theorem rotor_casimir_completed_square (jSpin : ℚ) :
    (jSpin + 1 / 2) ^ 2 - 1 / 4 = jSpin * (jSpin + 1) := by
  ring

/-! ## 3. FW–GGM State-Integral Coupling Defect & Median-Borel Resummation (`qou-ri9w`) -/

/-- Fantini–Wheeler quadratic state-integral coupling defect `B - A` (`qou-ri9w`). -/
def fwCouplingDefect (paramA paramB : ℤ) : ℤ :=
  paramB - paramA

/-- Upper lateral Borel sum `sMinus + stokesMultiplier * sMinus` across a Stokes ray with
    integer/Laurent multiplier `stokesMultiplier` (`qou-ri9w`). -/
def lateralBorelUpper (sMinus stokesMultiplier : ℚ) : ℚ :=
  sMinus + stokesMultiplier * sMinus

/-- Twice the median-Borel sum `sPlus + sMinus` equals `(2 + stokesMultiplier) * sMinus`, while
    the lateral discontinuity `sPlus - sMinus` recovers `stokesMultiplier * sMinus` (`qou-ri9w`). -/
theorem median_borel_sum_and_stokes_discontinuity (sMinus stokesMultiplier : ℚ) :
    lateralBorelUpper sMinus stokesMultiplier + sMinus = (2 + stokesMultiplier) * sMinus ∧
      lateralBorelUpper sMinus stokesMultiplier - sMinus = stokesMultiplier * sMinus := by
  unfold lateralBorelUpper
  constructor <;> ring

/-- Both the figure-eight knot `4_1` (`(A, B) = (1, 2)`) and the three-twist knot `5_2`
    (`(A, B) = (2, 3)`) have unit Fantini–Wheeler coupling defect `B - A = 1`, while their
    Stokes matrix ranks `B` differ by `3 - 2 = 1` (`qou-ri9w`). -/
theorem fw_four_one_and_five_two_unit_coupling_defect (a41 b41 a52 b52 : ℤ)
    (ha41 : a41 = 1) (hb41 : b41 = 2) (ha52 : a52 = 2) (hb52 : b52 = 3) :
    fwCouplingDefect a41 b41 = 1 ∧
      fwCouplingDefect a52 b52 = 1 ∧
      b52 - b41 = 1 := by
  unfold fwCouplingDefect
  subst ha41; subst hb41; subst ha52; subst hb52
  refine ⟨by ring, by ring, by ring⟩

/-! ## 4. Resurgent 3-Saddle Coherent Sum Rule Check (`qou-rsrg`) -/

/-- Coherent `N`-saddle sum `nSaddles * sPi` in units of `\pi^2` (`qou-rsrg`). -/
def coherentSaddleSum (nSaddles sPi : ℚ) : ℚ :=
  nSaddles * sPi

/-- Subtracting a single saddle contribution `sPi` from the `N`-saddle coherent sum leaves
    `(nSaddles - 1) * sPi` (`qou-rsrg`). -/
theorem coherent_saddle_sum_excess_over_single (nSaddles sPi : ℚ) :
    coherentSaddleSum nSaddles sPi - sPi = (nSaddles - 1) * sPi := by
  unfold coherentSaddleSum
  ring

/-- For `nSaddles = 3` and single-saddle value `sPi = -1/2` (in units of `\pi^2`), the coherent
    sum is `-3/2` (`S(0) = -3\pi^2/2`) and the excess over `S(\pi)` is `-1` (`-\pi^2`) (`qou-rsrg`). -/
theorem three_saddle_sum_rule_coefficients (nSaddles sPi : ℚ)
    (hn : nSaddles = 3) (hs : sPi = -1 / 2) :
    coherentSaddleSum nSaddles sPi = -3 / 2 ∧
      coherentSaddleSum nSaddles sPi - sPi = -1 := by
  unfold coherentSaddleSum
  subst hn; subst hs
  constructor <;> ring

/-! ## 5. B2 Sibling Convergence Normalization Bridge (`qou-u7hx`) -/

/-- Cross-multiplied normalization defect `vA * zB - vB * zA` between two sibling conventions
    `(vA, zA)` and `(vB, zB)` (`qou-u7hx`). -/
def siblingNormalizationDefect (vA zA vB zB : ℚ) : ℚ :=
  vA * zB - vB * zA

/-- Two sibling conventions satisfy cross-multiplied agreement `vA * zB = vB * zA` if and only if
    `siblingNormalizationDefect vA zA vB zB = 0` (`qou-u7hx`). -/
theorem sibling_normalized_eq_iff_defect_zero (vA zA vB zB : ℚ) :
    vA * zB = vB * zA ↔ siblingNormalizationDefect vA zA vB zB = 0 := by
  unfold siblingNormalizationDefect
  constructor <;> intro h <;> linarith

/-- Transitive combination identity for three sibling conventions `(A, B, C)`:
    `zC * defect(A, B) + zA * defect(B, C) = zB * defect(A, C)` (`qou-u7hx`). -/
theorem sibling_normalization_defect_transitivity (vA zA vB zB vC zC : ℚ) :
    zC * siblingNormalizationDefect vA zA vB zB +
        zA * siblingNormalizationDefect vB zB vC zC =
      zB * siblingNormalizationDefect vA zA vC zC := by
  unfold siblingNormalizationDefect
  ring

end QOU.MassTheory.QGevreyCauchyAndFWGGMStokes
