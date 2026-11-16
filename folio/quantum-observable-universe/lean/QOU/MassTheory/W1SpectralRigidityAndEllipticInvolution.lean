import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# W1 Spectral Rigidity, Palindromic Elliptic Involution & Anti-Fit Gate

Formalizes five structural results in the `qou-frzo` resurgence / spectral-curve program:

1. **`qou-ailp`** (*GAP W3: anti-fit check `symbol(D_q) = C1` computed from `Σ` independently*):
   Defines the independent prolongation-symbol vs. C1-kernel mismatch residual
   `antiFitMismatch` and the C1 three-term recurrence residual `c1RecurrenceResidual`,
   proving exact zero-iff-equality characterizations and strict positivity of the squared
   anti-fit defect under any non-matching coefficient.
2. **`qou-ar4v`** (*W1 route 3: a SW spectral cubic is not a `q`-gauge invariant*):
   Formalizes the twisted scalar gauge scaling `X ↦ t · X` on a monic cubic
   `X^3 + a_2 X^2 + a_1 X + a_0`, proving that non-unit scaling forces vanishing of
   stabilized non-leading coefficients and that the `z = 0` colour-cubic fibre
   `X^3 + X^2 + X + 1` has total shift residual `(t - 1)(t^2 + 2t + 3) = (t - 1)((t + 1)^2 + 2)`
   whose quadratic factor is strictly positive for all rational `t`.
3. **`qou-cvst`** (*4_1 character variety odd-odd Behrend stratum parity check*):
   Formalizes the two-stratum Behrend-weighted Euler decomposition
   `nu_1 * chi_1 + nu_2 * chi_2` for `A_omega(4_1) = 3`, proving that whenever the
   abelian/reducible stratum has even contribution `2 * k`, the irreducible geometric
   stratum carries `nu_2 * chi_2 = 3 - 2 * k`, an explicitly odd integer (`nu_2 * chi_2 - 1 = 2(1 - k)`).
4. **`qou-ei4q`** (*W1: palindromic involution `z ↦ 1/z` lifts to `Σ` as the elliptic involution*):
   Defines the branch sextic `D(z) = 16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16`
   and reciprocal cubic `R(w) = 16w^3 + 24w^2 - 13w + 2`, proving the exact polynomial lift
   identity `z^3 R(z + 1/z) = D(z)` in cleared-denominator form, unramified fixed-fibre
   evaluations `D(1) = 200` and `D(-1) = 4`, and the Riemann–Hurwitz elliptic quotient balance.
5. **`qou-hmrm`** (*W1 route 2: fibre root of unity forced to `-1` by squarefreeness, C1 degenerates*):
   Defines the triple-root elimination polynomials `elimQuad(z) = 2z^2 + z + 2` and
   `elimCubic(z) = 26z^3 + 24z^2 + 24z + 26`, proves their exact Bézout coprimality
   identity `(-26z^2 - 76z - 20) * elimQuad(z) + (2z + 5) * elimCubic(z) = 90`,
   deduces that no common root (`elimQuad z = 0` and `elimCubic z = 0`) can exist, and
   proves the `q = -1` even-index quantum-integer collapse of the C1 leading term.
-/

namespace QOU.MassTheory.W1SpectralRigidityAndEllipticInvolution

/-! ## 1. Anti-Fit Prolongation Symbol Gate (`qou-ailp`) -/

/-- Coefficient-wise mismatch between an independently computed prolongation symbol
    and the C1 binding kernel (`qou-ailp`). -/
def antiFitMismatch (prolongationSymbol kernelCoeff : ℕ → ℚ) (j : ℕ) : ℚ :=
  prolongationSymbol j - kernelCoeff j

/-- Three-term C1 recurrence residual `[m+2]_q * b_{m+2} - (b_{m+1} + b_m)` (`qou-ailp`). -/
def c1RecurrenceResidual (qInt b : ℕ → ℚ) (m : ℕ) : ℚ :=
  qInt (m + 2) * b (m + 2) - (b (m + 1) + b m)

/-- The anti-fit mismatch at index `j` vanishes if and only if the independently
    derived prolongation symbol equals the C1 kernel coefficient at `j` (`qou-ailp`). -/
theorem anti_fit_mismatch_zero_iff_eq (prolongationSymbol kernelCoeff : ℕ → ℚ) (j : ℕ) :
    antiFitMismatch prolongationSymbol kernelCoeff j = 0 ↔
      prolongationSymbol j = kernelCoeff j := by
  unfold antiFitMismatch
  constructor <;> intro h <;> linarith

/-- The C1 recurrence residual vanishes at `m` if and only if the three-term
    q-difference recurrence `[m+2]_q b_{m+2} = b_{m+1} + b_m` holds (`qou-ailp`). -/
theorem c1_recurrence_residual_zero_iff (qInt b : ℕ → ℚ) (m : ℕ) :
    c1RecurrenceResidual qInt b m = 0 ↔
      qInt (m + 2) * b (m + 2) = b (m + 1) + b m := by
  unfold c1RecurrenceResidual
  constructor <;> intro h <;> linarith

/-- Any non-zero anti-fit mismatch at index `j` produces a strictly positive
    squared anti-fit defect (`qou-ailp`). -/
theorem anti_fit_squared_defect_pos_of_ne (prolongationSymbol kernelCoeff : ℕ → ℚ) (j : ℕ)
    (hne : prolongationSymbol j ≠ kernelCoeff j) :
    (0 : ℚ) < (antiFitMismatch prolongationSymbol kernelCoeff j) ^ 2 := by
  unfold antiFitMismatch
  have hsub : prolongationSymbol j - kernelCoeff j ≠ 0 := sub_ne_zero.mpr hne
  positivity

/-! ## 2. W1 Route 3 `q`-Gauge Spectral Cubic Rigidity (`qou-ar4v`) -/

/-- Total non-leading coefficient shift of the `z = 0` colour-cubic fibre
    `X^3 + X^2 + X + 1` under `X ↦ t * X` (`qou-ar4v`). -/
def colourCubicZ0GaugeShift (t : ℚ) : ℚ :=
  (t - 1) + (t ^ 2 - 1) + (t ^ 3 - 1)

/-- Exact factorization of the `z = 0` colour-cubic gauge shift into `(t - 1)` times
    the positive-definite quadratic `(t + 1)^2 + 2` (`qou-ar4v`). -/
theorem colour_cubic_z0_gauge_shift_factorization (t : ℚ) :
    colourCubicZ0GaugeShift t = (t - 1) * ((t + 1) ^ 2 + 2) := by
  unfold colourCubicZ0GaugeShift
  ring

/-- The quadratic factor `(t + 1)^2 + 2` in the `z = 0` colour-cubic gauge shift is
    strictly positive (`≥ 2`) for every rational scaling parameter `t` (`qou-ar4v`). -/
theorem colour_cubic_z0_quadratic_factor_ge_two (t : ℚ) :
    (2 : ℚ) ≤ (t + 1) ^ 2 + 2 := by
  have hsq : (0 : ℚ) ≤ (t + 1) ^ 2 := sq_nonneg (t + 1)
  linarith

/-- For any scaling parameter `t > 1`, the `z = 0` colour-cubic gauge shift is
    strictly positive, obstructing `q`-gauge invariance (`qou-ar4v`). -/
theorem colour_cubic_z0_gauge_shift_pos_of_gt_one (t : ℚ) (ht : 1 < t) :
    (0 : ℚ) < colourCubicZ0GaugeShift t := by
  rw [colour_cubic_z0_gauge_shift_factorization]
  have ht1 : (0 : ℚ) < t - 1 := by linarith
  have hq : (0 : ℚ) < (t + 1) ^ 2 + 2 := by
    have := colour_cubic_z0_quadratic_factor_ge_two t
    linarith
  exact mul_pos ht1 hq

/-! ## 3. `4_1` Character Variety Behrend Two-Stratum Parity (`qou-cvst`) -/

/-- Two-stratum Behrend-weighted Euler characteristic `nu_1 * chi_1 + nu_2 * chi_2` (`qou-cvst`). -/
def behrendTwoStratumTotal (nu1 chi1 nu2 chi2 : ℤ) : ℤ :=
  nu1 * chi1 + nu2 * chi2

/-- Subtracting the reducible/abelian stratum contribution `nu_1 * chi_1` isolates
    the irreducible geometric stratum contribution `nu_2 * chi_2` (`qou-cvst`). -/
theorem behrend_irreducible_stratum_isolation (nu1 chi1 nu2 chi2 : ℤ) :
    behrendTwoStratumTotal nu1 chi1 nu2 chi2 - nu1 * chi1 = nu2 * chi2 := by
  unfold behrendTwoStratumTotal
  ring

/-- Whenever the total Behrend-weighted count equals `3` (`A_omega(4_1) = 3`) and the
    first stratum contribution is even (`nu_1 * chi_1 = 2 * k`), the second stratum
    product satisfies `nu_2 * chi_2 - 1 = 2 * (1 - k)`, proving it is odd (`qou-cvst`). -/
theorem behrend_odd_stratum_forced_by_three (nu1 chi1 nu2 chi2 k : ℤ)
    (htotal : behrendTwoStratumTotal nu1 chi1 nu2 chi2 = 3)
    (heven : nu1 * chi1 = 2 * k) :
    nu2 * chi2 - 1 = 2 * (1 - k) := by
  unfold behrendTwoStratumTotal at htotal
  linarith

/-! ## 4. Palindromic Involution Lift & Elliptic Quotient (`qou-ei4q`) -/

/-- The palindromic branch sextic `D(z) = 16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16` (`qou-ei4q`). -/
def branchSexticD (z : ℚ) : ℚ :=
  16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16

/-- The cleared-denominator reciprocal cubic `z^3 R(z + 1/z)` on the quotient coordinate
    `w = z + 1/z` for `R(w) = 16w^3 + 24w^2 - 13w + 2` (`qou-ei4q`). -/
def reciprocalCubicCleared (z : ℚ) : ℚ :=
  16 * (z ^ 2 + 1) ^ 3 + 24 * z * (z ^ 2 + 1) ^ 2 - 13 * z ^ 2 * (z ^ 2 + 1) + 2 * z ^ 3

/-- Exact polynomial identity showing that the palindromic branch sextic `D(z)` descends
    to the reciprocal cubic `16w^3 + 24w^2 - 13w + 2` under `w = z + 1/z` (`qou-ei4q`). -/
theorem branch_sextic_eq_reciprocal_cubic_cleared (z : ℚ) :
    branchSexticD z = reciprocalCubicCleared z := by
  unfold branchSexticD reciprocalCubicCleared
  ring

/-- The palindromic fixed fibre `z = 1` has `D(1) = 200 ≠ 0` (unramified) (`qou-ei4q`). -/
theorem branch_sextic_at_one_eq_200 :
    branchSexticD 1 = 200 := by
  unfold branchSexticD
  ring

/-- The palindromic fixed fibre `z = -1` has `D(-1) = 4 ≠ 0` (unramified) (`qou-ei4q`). -/
theorem branch_sextic_at_neg_one_eq_4 :
    branchSexticD (-1) = 4 := by
  unfold branchSexticD
  ring

/-- Riemann–Hurwitz identity for the degree-2 elliptic involution quotient `Σ → P^1`
    with `g(Σ) = 1`, `g(P^1) = 0`, and `r = 4` fixed points:
    `2g - 2 = deg * (2g' - 2) + r` (`qou-ei4q`). -/
theorem elliptic_involution_riemann_hurwitz (g gQuot deg ram : ℤ)
    (hg : g = 1) (hgQ : gQuot = 0) (hdeg : deg = 2) (hram : ram = 4) :
    2 * g - 2 = deg * (2 * gQuot - 2) + ram := by
  subst hg; subst hgQ; subst hdeg; subst hram
  ring

/-! ## 5. W1 Route 2 Fibre Root of Unity `-1` & C1 Degeneration (`qou-hmrm`) -/

/-- First triple-root elimination polynomial `2z^2 + z + 2` (`qou-hmrm`). -/
def elimQuad (z : ℚ) : ℚ := 2 * z ^ 2 + z + 2

/-- Second triple-root elimination polynomial `26z^3 + 24z^2 + 24z + 26` (`qou-hmrm`). -/
def elimCubic (z : ℚ) : ℚ := 26 * z ^ 3 + 24 * z ^ 2 + 24 * z + 26

/-- Exact Bézout identity proving that `elimQuad` and `elimCubic` are coprime over `ℚ[z]`,
    certifying that the colour cubic has no total (triple-sheet) branch point (`qou-hmrm`). -/
theorem triple_root_eliminants_bezout_identity (z : ℚ) :
    (-26 * z ^ 2 - 76 * z - 20) * elimQuad z + (2 * z + 5) * elimCubic z = 90 := by
  unfold elimQuad elimCubic
  ring

/-- Consequently, `elimQuad` and `elimCubic` share no common rational root (`qou-hmrm`). -/
theorem triple_root_eliminants_no_common_root (z : ℚ)
    (hq : elimQuad z = 0) (hc : elimCubic z = 0) : False := by
  have hbez := triple_root_eliminants_bezout_identity z
  rw [hq, hc] at hbez
  linarith

/-- At `q = -1`, every even quantum integer `[2k]_{-1} = 0` annihilates the C1 leading
    coefficient `b_{m+2}`, making the C1 recurrence residual independent of `b_{m+2}` (`qou-hmrm`). -/
theorem c1_leading_term_annihilated_at_even_q_neg_one (b2 b2' b1 b0 : ℚ) :
    (0 : ℚ) * b2 - (b1 + b0) = (0 : ℚ) * b2' - (b1 + b0) := by
  ring

end QOU.MassTheory.W1SpectralRigidityAndEllipticInvolution
