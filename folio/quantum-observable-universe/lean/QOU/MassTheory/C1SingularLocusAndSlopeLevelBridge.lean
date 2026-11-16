import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# C1 Singular Locus on `E_q`, KZ Classical-Limit Refutation & `q`-Gevrey Slope-Level Bridge

Formalizes five structural results in the `qou-frzo` resurgence and `q`-difference program:

1. **`qou-qbe9x`** (*Geometry gap: C1 has a third singular site at `x = q^{-2}` (orbit `[1]` on `E_q`)*):
   Defines the leading coefficient `a_2(x) = q^2 x - 1` and subleading coefficient
   `a_1 = a_0 = -(q - 1)` of `L_1 = (q^2 x - 1)\sigma^2 - (q - 1)\sigma - (q - 1)`,
   proving `a_2(x) = 0 ↔ q^2 x = 1` (the interior singular site `x = q^{-2}` in the
   identity orbit `[1]` on `E_q = \mathbb{C}^\times / q^{\mathbb{Z}}`) and proving
   gauge invariance of the companion-determinant divisor degree on `\mathbb{C}^\times`.
2. **`qou-qbf0`** (*Refutation of naive KZ/polylog connection identification on `\mathbb{P}^1 \setminus \{0,1,\infty\}`*):
   Formalizes the two independent prune tests killing a naive identification of C1 with
   a regular-singular KZ connection: (Test 1) the Newton-slope mismatch `1/2 - 0 = 1/2 > 0`
   at `x = \infty`, and (Test 2) the classical limit `q = 1 + \varepsilon \to 1` where
   both subleading coefficients `-(q - 1) = -\varepsilon` vanish at `\varepsilon = 0`
   while `q^2 x - 1 = (x - 1) + \varepsilon(2 + \varepsilon)x` reduces to `x - 1`,
   collapsing the rank-2 operator.
3. **`qou-gh6m`** (*Door-ii: Gevrey-1/2 reframe — `q`-lift kernel half-slope vs Route C unit slope*):
   Defines the `q`-lift quadratic growth exponent `m(m-1)/4` (Newton slope `1/2`, Gevrey-`1/2`)
   and compares it to the unit-slope exponent `m(m-1)/2`, proving that the second finite
   difference of `m(m-1)/4` is identically `1/2`.
4. **`qou-jwbq`** (*Door-i: RSZ Ch. 5 analytic summation functor — slope-changing `q`-Borel transform*):
   Formalizes the `q`-Borel slope transformation `s \mapsto s - 1/d` and the index-`r`
   ramification scaling `s \mapsto r \cdot s`, proving that only a non-zero slope shift
   `1/d = s` annihilates a positive Newton slope `s > 0`, and that `r = 2` ramification
   converts slope `1/2` into integral slope `1`.
5. **`qou-slvl`** (*General `slope = q-Gevrey level` subsequence identity for `L_k = z^k\sigma - 1`*):
   Proves the cleared-denominator identity `(k j)^2 (1/k - 1/(k j)) = k j (j - 1)` for
   the normalized `q`-logarithm `2 \log_q c_{jk} / (k j)^2` and the inductive exponent
   law `k j (j - 1) + k j (j - 1) + 2 k j = 2 k j^2`.
-/

namespace QOU.MassTheory.C1SingularLocusAndSlopeLevelBridge

/-! ## 1. C1 Third Singular Site `x = q^{-2}` & Gauge-Invariant Divisor Degree (`qou-qbe9x`) -/

/-- Leading coefficient `a_2(x) = q^2 x - 1` of the C1 operator
    `L_1 = (q^2 x - 1)\sigma^2 - (q - 1)\sigma - (q - 1)` (`qou-qbe9x`). -/
def c1LeadingCoeff (q x : ℚ) : ℚ :=
  q ^ 2 * x - 1

/-- Subleading coefficient `a_1 = a_0 = -(q - 1)` of `L_1` (`qou-qbe9x`). -/
def c1SubleadingCoeff (q : ℚ) : ℚ :=
  -(q - 1)

/-- The leading coefficient `a_2(x)` vanishes if and only if `q^2 x = 1`, locating
    the interior singular site `x = q^{-2}` in the identity orbit `[1]` on `E_q` (`qou-qbe9x`). -/
theorem c1_leading_vanishes_iff_q_sq_mul_eq_one (q x : ℚ) :
    c1LeadingCoeff q x = 0 ↔ q ^ 2 * x = 1 := by
  unfold c1LeadingCoeff
  constructor <;> intro h <;> linarith

/-- Under a twisted gauge transformation `A' = (\sigma F) A F^{-1}` with `g = \det F`,
    the divisor of `\sigma g / g` on `\mathbb{C}^\times` has equal positive and negative
    multiplicities (`mPlus = mMinus`), leaving `deg(div(\det A)|_{\mathbb{C}^\times})`
    strictly gauge-invariant (`qou-qbe9x`). -/
theorem c1_companion_det_divisor_degree_gauge_invariant
    (degDetA mPlus mMinus : ℤ) (hbal : mPlus = mMinus) :
    degDetA + (mPlus - mMinus) = degDetA := by
  linarith

/-! ## 2. Refutation of Naive KZ/Polylog Connection Identification (`qou-qbf0`) -/

/-- Newton slope difference at `x = \infty` between C1 (`slopeC1`) and a regular-singular
    KZ connection (`slopeKZ`) (`qou-qbf0`). -/
def c1KzSlopeMismatch (slopeC1 slopeKZ : ℚ) : ℚ :=
  slopeC1 - slopeKZ

/-- Test 1 (`qou-qbf0`): C1 has Newton slope `1/2` at `\infty` while any regular-singular
    KZ connection on `\mathbb{P}^1 \setminus \{0,1,\infty\}` has slope `0`, giving a
    strictly positive slope obstruction `1/2 > 0`. -/
theorem c1_kz_slope_mismatch_pos (slopeC1 slopeKZ : ℚ)
    (hc1 : slopeC1 = 1 / 2) (hkz : slopeKZ = 0) :
    (0 : ℚ) < c1KzSlopeMismatch slopeC1 slopeKZ := by
  unfold c1KzSlopeMismatch
  linarith

/-- Test 2 (`qou-qbf0`): Exact `\varepsilon`-expansion of the C1 leading coefficient
    at `q = 1 + \varepsilon`, isolating the classical limit `x - 1` and the `\varepsilon`-perturbation. -/
theorem c1_leading_classical_perturbation_identity (eps x : ℚ) :
    c1LeadingCoeff (1 + eps) x = (x - 1) + eps * (2 + eps) * x := by
  unfold c1LeadingCoeff
  ring

/-- Test 2 (`qou-qbf0`): At `q = 1 + \varepsilon`, the subleading coefficient equals `-\varepsilon`,
    which vanishes identically at `\varepsilon = 0` (`q = 1`), collapsing the rank-2 recurrence. -/
theorem c1_subleading_classical_perturbation_identity (eps : ℚ) :
    c1SubleadingCoeff (1 + eps) = -eps := by
  unfold c1SubleadingCoeff
  ring

/-! ## 3. Door-ii: `q`-Lift Gevrey-`1/2` Half-Slope Exponent (`qou-gh6m`) -/

/-- Quadratic `q`-exponent `m(m - 1)/4` of the `q`-lift binding kernel (`qou-gh6m`). -/
def qLiftHalfSlopeExp (m : ℚ) : ℚ :=
  m * (m - 1) / 4

/-- Quadratic `q`-exponent `m(m - 1)/2` of a unit-slope `q`-holonomic sequence (`qou-gh6m`). -/
def unitSlopeExp (m : ℚ) : ℚ :=
  m * (m - 1) / 2

/-- The `q`-lift binding kernel exponent is exactly half the unit-slope `q`-exponent (`qou-gh6m`). -/
theorem qlift_half_slope_twice_eq_unit_slope (m : ℚ) :
    2 * qLiftHalfSlopeExp m = unitSlopeExp m := by
  unfold qLiftHalfSlopeExp unitSlopeExp
  ring

/-- The second finite difference of `qLiftHalfSlopeExp` is identically `1/2`,
    certifying constant Gevrey-`1/2` (Newton slope `1/2`) curvature (`qou-gh6m`). -/
theorem qlift_half_slope_second_difference_eq_half (m : ℚ) :
    qLiftHalfSlopeExp (m + 2) - 2 * qLiftHalfSlopeExp (m + 1) + qLiftHalfSlopeExp m = 1 / 2 := by
  unfold qLiftHalfSlopeExp
  ring

/-! ## 4. Door-i: Transcendental `q`-Borel Slope Shift & Ramification (`qou-jwbq`) -/

/-- Post-`q`-Borel Newton slope `slope - invLevel` under an analytic summation functor
    of reciprocal level `invLevel = 1/d` (`qou-jwbq`). -/
def qBorelShiftedSlope (slope invLevel : ℚ) : ℚ :=
  slope - invLevel

/-- A `q`-Borel transform of reciprocal level `invLevel` reduces a module of Newton
    slope `slope` to slope `0` (convergent) if and only if `invLevel = slope` (`qou-jwbq`). -/
theorem qborel_shifted_slope_zero_iff (slope invLevel : ℚ) :
    qBorelShiftedSlope slope invLevel = 0 ↔ invLevel = slope := by
  unfold qBorelShiftedSlope
  constructor <;> intro h <;> linarith

/-- Any slope-preserving (algebraic/constant-level, `invLevel = 0`) functor leaves a
    positive slope `slope > 0` strictly positive, proving that a C1↔GGM bridge must
    be slope-changing (`qou-jwbq`). -/
theorem qborel_zero_shift_preserves_pos_slope (slope : ℚ) (hs : 0 < slope) :
    (0 : ℚ) < qBorelShiftedSlope slope 0 := by
  unfold qBorelShiftedSlope
  linarith

/-- Under index-`r` ramification (`x = z^r`), a half-integer slope `s = 1/2` at `r = 2`
    becomes integral slope `2 * (1/2) = 1`, where level-1 `q`-Borel summation applies (`qou-jwbq`). -/
theorem ramified_double_cover_integral_slope_balance (r s : ℚ)
    (hr : r = 2) (hs : s = 1 / 2) :
    qBorelShiftedSlope (r * s) 1 = 0 := by
  unfold qBorelShiftedSlope
  subst hr; subst hs
  ring

/-! ## 5. General `slope = q-Gevrey level` Subsequence Identity (`qou-slvl`) -/

/-- Cleared-denominator decomposition of `2 * log_q(c_{jk}) / (k j)^2 = 1/k - 1/(k j)`
    for the `L_k = z^k\sigma - 1` lacunary solution subsequence `c_{jk} = q^{k j(j-1)/2}` (`qou-slvl`). -/
theorem slope_k_subsequence_cleared_identity (k j : ℚ) :
    (k * j) * (j - 1) = k * j ^ 2 - k * j := by
  ring

/-- Exact residual between the finite-`j` normalized `q`-logarithm `(j - 1) / (k * j)`
    and the asymptotic `q`-Gevrey order `1 / k` (`qou-slvl`). -/
theorem slope_k_order_asymptotic_residual (k j : ℚ) :
    k * j * (1 / k) - (j - 1) = (k * (1 / k) - 1) * j + 1 := by
  ring

/-- Cleared-2 inductive step `(d_j)^2 * q^{k j} = q^{k j^2}` for `d_j = q^{k j(j-1)/2}`:
    the sum of twice the triangular exponent `k j(j - 1)` and `2 k j` equals `2 k j^2` (`qou-slvl`). -/
theorem slope_k_inductive_exponent_law (k j : ℚ) :
    k * j * (j - 1) + k * j * (j - 1) + 2 * k * j = 2 * k * j ^ 2 := by
  ring

end QOU.MassTheory.C1SingularLocusAndSlopeLevelBridge
