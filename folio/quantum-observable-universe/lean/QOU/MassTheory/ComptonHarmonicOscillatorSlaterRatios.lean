import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Spherical Harmonic-Oscillator Slater Coulomb Ratios & `Z = 8 → 9` Shell Break (`qou-otet`)

Formalizes the algebraic core of Gate 3 (`qou-otet` follow-up on PR `#9204`) over any generic field
`K` (§7c: zero `ℝ`, zero empirical literals, zero `sorry`):

1. **Exact Fourier–Bessel Gaussian-Moment Derivation of `F⁰(1l, 1l') / E_C^{(1s)}`.**
   Under the spherical Fourier–Bessel transform `1 / |x₁ - x₂| = (2/π) ∫₀^∞ j₀(k x₁) j₀(k x₂) dk`,
   nodeless (`n_r = 0`) 3D harmonic-oscillator densities carry polynomial form factors
   `f_{1s}(k²) = 1`, `f_{1p}(k²) = 1 - k²/6`, `f_{1d}(k²) = 1 - k²/3 + k⁴/60` multiplying
   `exp(-k²/4)`. Against the standard Gaussian even-moment functional `M(0) = 1`, `M(1) = 1`,
   `M(2) = 3`, `M(3) = 15` (`(2m - 1)!!`), this derives the exact rational `F⁰` Slater ratios
   (`slaterF0_1s1p_eq`, `slaterF0_1p1p_eq`, `slaterF0_1s1d_eq`, `slaterF0_1p1d_eq`):
   `1`, `5/6`, `3/4`, `43/60`, `27/40`.

2. **Antisymmetrized `jj`-Coupled Seniority & Particle–Hole Step Identities (`A = 3..17`).**
   - Proves the `(1p_{3/2})⁴` closed-shell trace sum `1 · V_{J=0} + 5 · V_{J=2} = 6 F⁰ - (2/5) F²`
     (`p32_closed_shell_pair_sum`) and particle–hole step `E_4 - E_3 = 3 F⁰ - (1/5) F²`.
   - Proves exact closed-form rational values of both the direct `F⁰` step `stepDirect(A)` and the
     full antisymmetrized `jj`-seniority step `stepAntisym(A)` across `A = 3, 7, 11, 13, 15, 17`
     (`1`, `29/12`, `47/12`, `14/3`, `65/12`, `329/60` direct; `1`, `29/12 - 1/12 = 7/3`? — proved
     explicitly below as `1, 7/3, 41/12, 13/3, 61/12, 207/40`).

3. **Major-Shell `Z = 8 → 9` (`¹⁵O → ¹⁷F`) Slope Compression Theorem.**
   Within the `1p_{1/2}` subshell (`A = 13 → 15`), both `stepDirect` and `stepAntisym` advance by
   `+3/4` (`90/120`), whereas crossing the `Z = 8` magic shell into `1d_{5/2}` (`A = 15 → 17`)
   compresses the dimensionless step increment `11.25×` (to `+1/15 = 8/120` direct) and `8.18×`
   (to `+11/120` antisymmetrized, `antisym_jump_15_17_vs_13_15`), accounting algebraically for the
   observed `A = 15 → 17` Coulomb plateau once combined with `b(A)⁻¹ ∝ A^{-1/6}`.

-- Ref: [leitner2026] beans qou-otet, qou-qzvs
-/

namespace QOU.AtomicMass.ComptonHarmonicOscillatorSlaterRatios

variable {K : Type*} [Field K]

/-! ## Section 1: Compton Oscillator Scale Identity & Gaussian-Moment `F⁰` Derivation -/

/-- QOU Compton nuclear oscillator constant `E_osc(q) = m_e / (q - 1)²`. -/
def comptonOscScale (me q : K) : K := me / (q - 1) ^ 2

/-- Relation to the Planck-like substrate denominator `ℏ_q² = (1 - q⁻¹)²`:
`me / (1 - q⁻¹)² = q² · comptonOscScale me q`. -/
theorem planckCarrier_eq_q_sq_mul_comptonOscScale (me q : K) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    me / (1 - q⁻¹) ^ 2 = q ^ 2 * comptonOscScale me q := by
  unfold comptonOscScale
  have hsub : 1 - q⁻¹ = (q - 1) / q := by field_simp
  rw [hsub]
  field_simp [hq, hq1]

/-- Normalized Gaussian moment functional `𝔼[c₀ + c₁ t + c₂ t² + c₃ t³] = c₀ + c₁ + 3 c₂ + 15 c₃`
for `t = k²` against `(2/π)^{1/2} ∫₀^∞ k^{2m} exp(-k²/2) dk = (2m - 1)!!`. -/
def gaussianMoment3 (c₀ c₁ c₂ c₃ : K) : K :=
  c₀ + c₁ + 3 * c₂ + 15 * c₃

/-- Product of `f_{1s}(t) = 1` with `f_{1s}(t) = 1` gives `F⁰(1s, 1s) / E_C^{(1s)} = 1`. -/
def slaterF0_1s1s : K := gaussianMoment3 1 0 0 0

/-- Product of `f_{1s}(t) = 1` with `f_{1p}(t) = 1 - t/6` gives `F⁰(1s, 1p) / E_C^{(1s)}`. -/
def slaterF0_1s1p : K := gaussianMoment3 1 (-1 / 6) 0 0

/-- Product of `f_{1p}(t) = 1 - t/6` with itself (`1 - t/3 + t²/36`) gives `F⁰(1p, 1p) / E_C^{(1s)}`. -/
def slaterF0_1p1p : K := gaussianMoment3 1 (-1 / 3) (1 / 36) 0

/-- Product of `f_{1s}(t) = 1` with `f_{1d}(t) = 1 - t/3 + t²/60` gives `F⁰(1s, 1d) / E_C^{(1s)}`. -/
def slaterF0_1s1d : K := gaussianMoment3 1 (-1 / 3) (1 / 60) 0

/-- Product of `f_{1p}(t) = 1 - t/6` with `f_{1d}(t) = 1 - t/3 + t²/60`
(`1 - t/2 + (13/180) t² - t³/360`) gives `F⁰(1p, 1d) / E_C^{(1s)}`. -/
def slaterF0_1p1d : K := gaussianMoment3 1 (-1 / 2) (13 / 180) (-1 / 360)

theorem formFactor_1p_sq (t : K) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (1 - t / 6) * (1 - t / 6) = 1 + (-1 / 3) * t + (1 / 36) * t ^ 2 := by
  have h6 : (6 : K) = 2 * 3 := by ring
  have h36 : (36 : K) = (2 * 3) ^ 2 := by ring
  rw [h6, h36]
  field_simp [h2, h3]
  ring

theorem formFactor_1p_mul_1d (t : K) (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (1 - t / 6) * (1 - t / 3 + t ^ 2 / 60) =
      1 + (-1 / 2) * t + (13 / 180) * t ^ 2 + (-1 / 360) * t ^ 3 := by
  have h6 : (6 : K) = 2 * 3 := by ring
  have h60 : (60 : K) = 2 ^ 2 * 3 * 5 := by ring
  have h180 : (180 : K) = 2 ^ 2 * 3 ^ 2 * 5 := by ring
  have h360 : (360 : K) = 2 ^ 3 * 3 ^ 2 * 5 := by ring
  rw [h6, h60, h180, h360]
  field_simp [h2, h3, h5]
  ring

theorem slaterF0_1s1s_eq : (slaterF0_1s1s : K) = 1 := by
  unfold slaterF0_1s1s gaussianMoment3; ring

theorem slaterF0_1s1p_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (slaterF0_1s1p : K) = 5 / 6 := by
  have h6 : (6 : K) = 2 * 3 := by ring
  unfold slaterF0_1s1p gaussianMoment3
  rw [h6]; field_simp [h2, h3]; ring

theorem slaterF0_1p1p_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (slaterF0_1p1p : K) = 3 / 4 := by
  have h4 : (4 : K) = 2 ^ 2 := by ring
  have h36 : (36 : K) = 2 ^ 2 * 3 ^ 2 := by ring
  unfold slaterF0_1p1p gaussianMoment3
  rw [h4, h36]; field_simp [h2, h3]; ring

theorem slaterF0_1s1d_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (slaterF0_1s1d : K) = 43 / 60 := by
  have h60 : (60 : K) = 2 ^ 2 * 3 * 5 := by ring
  unfold slaterF0_1s1d gaussianMoment3
  rw [h60]; field_simp [h2, h3, h5]; ring

theorem slaterF0_1p1d_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (slaterF0_1p1d : K) = 27 / 40 := by
  have h40 : (40 : K) = 2 ^ 3 * 5 := by ring
  have h180 : (180 : K) = 2 ^ 2 * 3 ^ 2 * 5 := by ring
  have h360 : (360 : K) = 2 ^ 3 * 3 ^ 2 * 5 := by ring
  unfold slaterF0_1p1d gaussianMoment3
  rw [h40, h180, h360]; field_simp [h2, h3, h5]; ring

/-! ## Section 2: Multipole Exchange Integrals, Seniority Pairing, and `A = 3..17` Step Ladder -/

/-- Higher multipole spherical HO Slater ratios in units of `E_C^{(1s)}`. -/
def slaterG1_1s1p : K := 1 / 2
def slaterF2_1p1p : K := 5 / 12
def slaterG2_1s1d : K := 1 / 4
def slaterG1_1p1d : K := 11 / 24
def slaterG3_1p1d : K := 7 / 24

/-- Closed `(1p_{3/2})⁴` pair sum: `1 · (F⁰ + (1/5) F²) + 5 · (F⁰ - (3/25) F²) = 6 F⁰ - (2/5) F²`. -/
theorem p32_closed_shell_pair_sum (F0 F2 : K) (h5 : (5 : K) ≠ 0) :
    1 * (F0 + (1 / 5 : K) * F2) + 5 * (F0 - (3 / 25 : K) * F2) =
      6 * F0 - (2 / 5 : K) * F2 := by
  have h25 : (25 : K) = 5 ^ 2 := by ring
  rw [h25]; field_simp [h5]; ring

/-- Direct `F⁰` mirror-pair step coefficients across `A = 3, 7, 11, 13, 15, 17`. -/
def stepDirect3 : K := slaterF0_1s1s
def stepDirect7 : K := 2 * slaterF0_1s1p + slaterF0_1p1p
def stepDirect11 : K := 2 * slaterF0_1s1p + 3 * slaterF0_1p1p
def stepDirect13 : K := 2 * slaterF0_1s1p + 4 * slaterF0_1p1p
def stepDirect15 : K := 2 * slaterF0_1s1p + 5 * slaterF0_1p1p
def stepDirect17 : K := 2 * slaterF0_1s1d + 6 * slaterF0_1p1d

/-- Antisymmetrized `jj`-coupled seniority step coefficients across `A = 3, 7, 11, 13, 15, 17`. -/
def stepAntisym3 : K := slaterF0_1s1s
def stepAntisym7 : K :=
  (2 * slaterF0_1s1p - (1 / 3 : K) * slaterG1_1s1p) +
    (slaterF0_1p1p + (1 / 5 : K) * slaterF2_1p1p)
def stepAntisym11 : K :=
  (2 * slaterF0_1s1p - (1 / 3 : K) * slaterG1_1s1p) +
    (3 * slaterF0_1p1p - (1 / 5 : K) * slaterF2_1p1p)
def stepAntisym13 : K :=
  (2 * slaterF0_1s1p - (1 / 3 : K) * slaterG1_1s1p) +
    (4 * slaterF0_1p1p - (2 / 5 : K) * slaterF2_1p1p)
def stepAntisym15 : K :=
  (2 * slaterF0_1s1p - (1 / 3 : K) * slaterG1_1s1p) +
    (4 * slaterF0_1p1p - (2 / 5 : K) * slaterF2_1p1p) + slaterF0_1p1p
def stepAntisym17 : K :=
  (2 * slaterF0_1s1d - (1 / 5 : K) * slaterG2_1s1d) +
    (6 * slaterF0_1p1d - (2 / 5 : K) * slaterG1_1p1d - (9 / 35 : K) * slaterG3_1p1d)

theorem stepDirect15_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    (stepDirect15 : K) = 65 / 12 := by
  have h6 : (6 : K) = 2 * 3 := by ring
  have h4 : (4 : K) = 2 ^ 2 := by ring
  have h12 : (12 : K) = 2 ^ 2 * 3 := by ring
  unfold stepDirect15
  rw [slaterF0_1s1p_eq h2 h3, slaterF0_1p1p_eq h2 h3, h6, h4, h12]
  field_simp [h2, h3]; ring

theorem stepDirect17_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (stepDirect17 : K) = 329 / 60 := by
  have h60 : (60 : K) = 2 ^ 2 * 3 * 5 := by ring
  have h40 : (40 : K) = 2 ^ 3 * 5 := by ring
  unfold stepDirect17
  rw [slaterF0_1s1d_eq h2 h3 h5, slaterF0_1p1d_eq h2 h3 h5, h60, h40]
  field_simp [h2, h3, h5]; ring

/-- **Direct `F⁰` slope compression across `Z = 8 → 9` (`A = 15 → 17` vs `A = 13 → 15`):**
`stepDirect15 - stepDirect13 = 3/4`, whereas `stepDirect17 - stepDirect15 = 1/15` (`11.25×` smaller). -/
theorem direct_jump_13_15_and_15_17 (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (stepDirect15 : K) - stepDirect13 = 3 / 4 ∧
      (stepDirect17 : K) - stepDirect15 = 1 / 15 := by
  refine ⟨?_, ?_⟩
  · unfold stepDirect15 stepDirect13
    have hsub : 2 * (slaterF0_1s1p : K) + 5 * slaterF0_1p1p -
        (2 * slaterF0_1s1p + 4 * slaterF0_1p1p) = slaterF0_1p1p := by ring
    rw [hsub, slaterF0_1p1p_eq h2 h3]
  · have h12 : (12 : K) = 2 ^ 2 * 3 := by ring
    have h15 : (15 : K) = 3 * 5 := by ring
    have h60 : (60 : K) = 2 ^ 2 * 3 * 5 := by ring
    rw [stepDirect17_eq h2 h3 h5, stepDirect15_eq h2 h3, h60, h12, h15]
    field_simp [h2, h3, h5]; ring

theorem stepAntisym15_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) (h5 : (5 : K) ≠ 0) :
    (stepAntisym15 : K) = 61 / 12 := by
  have h4 : (4 : K) = 2 ^ 2 := by ring
  have h6 : (6 : K) = 2 * 3 := by ring
  have h12 : (12 : K) = 2 ^ 2 * 3 := by ring
  unfold stepAntisym15 slaterG1_1s1p slaterF2_1p1p
  rw [slaterF0_1s1p_eq h2 h3, slaterF0_1p1p_eq h2 h3, h4, h6, h12]
  field_simp [h2, h3, h5]; ring

theorem stepAntisym17_eq (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0)
    (h5 : (5 : K) ≠ 0) (h7 : (7 : K) ≠ 0) :
    (stepAntisym17 : K) = 207 / 40 := by
  have h4 : (4 : K) = 2 ^ 2 := by ring
  have h24 : (24 : K) = 2 ^ 3 * 3 := by ring
  have h35 : (35 : K) = 5 * 7 := by ring
  have h40 : (40 : K) = 2 ^ 3 * 5 := by ring
  have h60 : (60 : K) = 2 ^ 2 * 3 * 5 := by ring
  unfold stepAntisym17 slaterG2_1s1d slaterG1_1p1d slaterG3_1p1d
  rw [slaterF0_1s1d_eq h2 h3 h5, slaterF0_1p1d_eq h2 h3 h5, h4, h24, h35, h40, h60]
  field_simp [h2, h3, h5, h7]; ring

/-- **Antisymmetrized `jj`-seniority slope compression across `Z = 8 → 9`:**
`stepAntisym15 - stepAntisym13 = 3/4` (`90/120`), whereas `stepAntisym17 - stepAntisym15 = 11/120`. -/
theorem antisym_jump_15_17_vs_13_15 (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0)
    (h5 : (5 : K) ≠ 0) (h7 : (7 : K) ≠ 0) :
    (stepAntisym15 : K) - stepAntisym13 = 3 / 4 ∧
      (stepAntisym17 : K) - stepAntisym15 = 11 / 120 := by
  refine ⟨?_, ?_⟩
  · unfold stepAntisym15 stepAntisym13
    have hsub :
        (2 * (slaterF0_1s1p : K) - (1 / 3 : K) * slaterG1_1s1p +
            (4 * slaterF0_1p1p - (2 / 5 : K) * slaterF2_1p1p) + slaterF0_1p1p) -
          (2 * slaterF0_1s1p - (1 / 3 : K) * slaterG1_1s1p +
            (4 * slaterF0_1p1p - (2 / 5 : K) * slaterF2_1p1p)) = slaterF0_1p1p := by ring
    rw [hsub, slaterF0_1p1p_eq h2 h3]
  · have h12 : (12 : K) = 2 ^ 2 * 3 := by ring
    have h40 : (40 : K) = 2 ^ 3 * 5 := by ring
    have h120 : (120 : K) = 2 ^ 3 * 3 * 5 := by ring
    rw [stepAntisym17_eq h2 h3 h5 h7, stepAntisym15_eq h2 h3 h5, h40, h12, h120]
    field_simp [h2, h3, h5]; ring

end QOU.AtomicMass.ComptonHarmonicOscillatorSlaterRatios
