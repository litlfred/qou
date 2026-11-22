import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.StandardModel.ElectroweakBringSchwingerBridge — Electroweak Analog of the Bring Genus
# Zero-Mode (`1/π`), 1-Loop Schwinger Fixed-Point Cubic, and Torus-Link Trace Polynomials `P_m(h)`

This module formalizes the exact algebraic and geometric core of the **Electroweak Analog of the
Bring Genus + 1-Loop Schwinger Fixed-Point Correction** for the electroweak torus-link triplet
`{W± = T(2,4), Z⁰ = T(2,6), H = T(2,8)}`, parallel to `QOU.Archimedean.EmCouplingBringZeroMode`
and `QOU.AlphaEM.FormLadder` (Epic `qou-rgj8`, Bean `qou-ewbs`):

1. **Section 1 — 2-Strand Torus-Link Plancherel Trace Polynomials `P_m(h)` (`m = 2, 3, 4`) and
   Quantum-Dimension Dressing `([2]_q / 2)² = 1 + h²/4`**:
   - Defines the binomial trace polynomials `P_m(h) = ∑_{j=0}^m (1/2) C(m+j, 2j) h^{2j}` for
     `m = 1, 2, 3, 4` (`P₂` for `W = T(2,4)`, `P₃` for `Z = T(2,6)`, `P₄` for `H = T(2,8)`),
     cleared of denominators as `twoMulP m h = 2 P_m(h)` over any commutative ring `R`.
   - Proves the exact Laurent/Chebyshev trace identities over any commutative ring `R` with unit `q`:
     `(q + q⁻¹) · (2 P_m(q - q⁻¹)) = q^{2m+1} + q^{-(2m+1)}` for `m = 1, 2, 3, 4`
     (`twoMulP1_laurent`, `twoMulP2_laurent`, `twoMulP3_laurent`, `twoMulP4_laurent`).
   - Proves the quantum-dimension dressing identity `([2]_q)² = (q - q⁻¹)² + 4`, equivalently
     `([2]_q / 2)² = 1 + h²/4` (`qInt2_sq_eq_h_sq_add_four`), and the exact anchor-reconciliation
     identity (`higgs_W_Z_anchor_reconciliation`): when the `W → Z` genus step satisfies
     `m_Z · P₂(h) · 4 = m_W · P₃(h) · [2]_q²`, the `W`-anchored Higgs mass expression
     `m_W · (P₄/P₂) · (6/5) · ([2]_q/2)` and the `Z`-anchored Higgs mass expression
     `m_Z · (P₄/P₃) · (6/5) · (2/[2]_q)` are **identically equal**.

2. **Section 2 — Electroweak Seifert Genus Sum (`1 + 2 + 3 = 6`) and Bring Surface Zero-Mode (`1/π`)**:
   - The three sub-saturating even-twist torus links `W = T(2,4)`, `Z = T(2,6)`, `H = T(2,8)`
     have Seifert genera `g_W = 1`, `g_Z = 2`, `g_H = 3`, whose sum is `G_EW = 1 + 2 + 3 = 6`
     (`ewSeifertGenusSum_eq_six`), matching the absolute Euler characteristic `|χ(Σ₄)| = 2g - 2 = 6`
     of Bring's genus-4 surface (`bringTilingEuler = -6`).
   - Proves unconditionally (`ewBringZeroMode_eq_one_div_pi`, `ewBringZeroMode_eq_three_halves_bringZeroMode`)
     that the total Seifert first-Betti count `2(g_W + g_Z + g_H) = 12` divided by the Bring
     Gauss–Bonnet surface area `Area(Σ₄) = 4π(g - 1) = 12π` equals `1 / π = (3/2) · (2/(3π))`.
   - Also states the division-free commutative-ring relation `IsEWGenusTerm g G_EW p T`
     (`4 · p · (g - 1) · T = 2 · G_EW`, parallel to `QOU.AlphaEM.FormLadder.IsGenusTerm`).

3. **Section 3 — Electroweak 1-Loop Schwinger Fixed-Point Cubic (`N_v = v / m_p`)**:
   - Defines the quantum-dimension-dressed electroweak tree complexity
     `ewTreeComplexity q = q · ([2]_q / 2) · [4]_q · [6]_q · [8]_q` and the constant term
     `ewFixedPointConst q = ewTreeComplexity q + 1 / π`.
   - Defines the electroweak self-consistency relation (`IsElectroweakVevFixedPoint q α_v`, with
     `α_v = 1 / N_v = m_p / v`):
     `1 / α_v = T_EW - α_v · H · (1 - h² · α_v)` (`H = [2]_q / (8π)`, `h = 1 - q⁻¹`),
     and proves sorry-free (`ewFixedPoint_iff_cubic`) that for any `α_v ≠ 0`, this fixed-point
     equation is equivalent to the characteristic cubic
     `P_EW(α_v) = h² H α_v³ - H α_v² + T_EW α_v - 1 = 0`.
   - Packages the open physical conjecture as a content-bearing §3b-cond typeclass
     `ElectroweakVevFixedPointClass` with **no global instance**.
-/

namespace QOU.StandardModel

open QOU.Archimedean (bringZeroModeValue gaussBonnetArea firstBetti bringTilingEuler
  bringTilingEuler_eq bringSurfaceArea bringSurfaceArea_eq_gaussBonnet)
open QOU.QInteger (qIntBal)

/-! ## Section 1: 2-Strand Torus-Link Trace Polynomials `P_m(h)` and `W`/`Z` Anchor Reconciliation -/

section TracePolynomials

variable {R : Type*} [CommRing R]

/-- Doubled binomial trace polynomial `2 · P_m(h) = ∑_{j=0}^m C(m+j, 2j) h^{2j}` for `m = 1..4`,
defined division-free over any commutative ring `R`:
- `m = 1` (`T(2,2)` Hopf link): `2 P₁(h) = 1 + h²`
- `m = 2` (`W± = T(2,4)`):      `2 P₂(h) = 1 + 3 h² + h⁴`
- `m = 3` (`Z⁰ = T(2,6)`):      `2 P₃(h) = 1 + 6 h² + 5 h⁴ + h⁶`
- `m = 4` (`H  = T(2,8)`):      `2 P₄(h) = 1 + 10 h² + 15 h⁴ + 7 h⁶ + h⁸` -/
def twoMulP : ℕ → R → R
  | 0, _ => 1
  | 1, h => 1 + h ^ 2
  | 2, h => 1 + 3 * h ^ 2 + h ^ 4
  | 3, h => 1 + 6 * h ^ 2 + 5 * h ^ 4 + h ^ 6
  | 4, h => 1 + 10 * h ^ 2 + 15 * h ^ 4 + 7 * h ^ 6 + h ^ 8
  | _ + 5, _ => 0

/-- Binomial coefficients of `2 P₂(h)` match `C(2+j, 2j)` for `j = 0, 1, 2`: `(1, 3, 1)`. -/
theorem twoMulP2_binomial_coeffs :
    Nat.choose (2 + 0) 0 = 1 ∧ Nat.choose (2 + 1) 2 = 3 ∧ Nat.choose (2 + 2) 4 = 1 := by
  decide

/-- Binomial coefficients of `2 P₃(h)` match `C(3+j, 2j)` for `j = 0, 1, 2, 3`: `(1, 6, 5, 1)`. -/
theorem twoMulP3_binomial_coeffs :
    Nat.choose (3 + 0) 0 = 1 ∧ Nat.choose (3 + 1) 2 = 6 ∧
    Nat.choose (3 + 2) 4 = 5 ∧ Nat.choose (3 + 3) 6 = 1 := by
  decide

/-- Binomial coefficients of `2 P₄(h)` match `C(4+j, 2j)` for `j = 0..4`: `(1, 10, 15, 7, 1)`. -/
theorem twoMulP4_binomial_coeffs :
    Nat.choose (4 + 0) 0 = 1 ∧ Nat.choose (4 + 1) 2 = 10 ∧
    Nat.choose (4 + 2) 4 = 15 ∧ Nat.choose (4 + 3) 6 = 7 ∧
    Nat.choose (4 + 4) 8 = 1 := by
  decide

/-- **2-strand quantum dimension vs Hecke parameter identity (division-free)**:
`(q + q⁻¹)² = (q - q⁻¹)² + 4` whenever `q · q⁻¹ = 1`. Dividing by `4` gives
`([2]_q / 2)² = 1 + h²/4`. -/
theorem qInt2_sq_eq_h_sq_add_four (q qi : R) (hinv : q * qi = 1) :
    (q + qi) ^ 2 = (q - qi) ^ 2 + 4 := by
  calc
    (q + qi) ^ 2 = (q - qi) ^ 2 + 4 * (q * qi) := by ring
    _ = (q - qi) ^ 2 + 4 * 1 := by rw [hinv]
    _ = (q - qi) ^ 2 + 4 := by ring

/-- **Closed-form Laurent identity for `m = 1` (`T(2,2)`)**:
`(q + q⁻¹) · 2 P₁(q - q⁻¹) = q³ + q⁻³`. -/
theorem twoMulP1_laurent (q qi : R) (hinv : q * qi = 1) :
    (q + qi) * twoMulP 1 (q - qi) = q ^ 3 + qi ^ 3 := by
  unfold twoMulP
  calc
    (q + qi) * (1 + (q - qi) ^ 2)
        = (q ^ 3 + qi ^ 3) + (q + qi) * (1 - q * qi) := by ring
    _ = (q ^ 3 + qi ^ 3) + (q + qi) * (1 - 1) := by rw [hinv]
    _ = q ^ 3 + qi ^ 3 := by ring

/-- **Closed-form Laurent identity for `m = 2` (`W± = T(2,4)`)**:
`(q + q⁻¹) · 2 P₂(q - q⁻¹) = q⁵ + q⁻⁵`. -/
theorem twoMulP2_laurent (q qi : R) (hinv : q * qi = 1) :
    (q + qi) * twoMulP 2 (q - qi) = q ^ 5 + qi ^ 5 := by
  unfold twoMulP
  have h1 : q * qi = 1 := hinv
  have h2 : q ^ 2 * qi ^ 2 = 1 := by
    calc q ^ 2 * qi ^ 2 = (q * qi) ^ 2 := by ring
    _ = 1 := by rw [h1]; ring
  calc
    (q + qi) * (1 + 3 * (q - qi) ^ 2 + (q - qi) ^ 4)
        = (q ^ 5 + qi ^ 5)
          + (q ^ 3 + qi ^ 3) * (3 - 3 * (q * qi))
          + (q + qi) * (1 - 3 * (q * qi) + 2 * (q ^ 2 * qi ^ 2)) := by ring
    _ = q ^ 5 + qi ^ 5 := by rw [h1, h2]; ring

/-- **Closed-form Laurent identity for `m = 3` (`Z⁰ = T(2,6)`)**:
`(q + q⁻¹) · 2 P₃(q - q⁻¹) = q⁷ + q⁻⁷`. -/
theorem twoMulP3_laurent (q qi : R) (hinv : q * qi = 1) :
    (q + qi) * twoMulP 3 (q - qi) = q ^ 7 + qi ^ 7 := by
  unfold twoMulP
  have h1 : q * qi = 1 := hinv
  have h2 : q ^ 2 * qi ^ 2 = 1 := by
    calc q ^ 2 * qi ^ 2 = (q * qi) ^ 2 := by ring
    _ = 1 := by rw [h1]; ring
  have h3 : q ^ 3 * qi ^ 3 = 1 := by
    calc q ^ 3 * qi ^ 3 = (q * qi) ^ 3 := by ring
    _ = 1 := by rw [h1]; ring
  calc
    (q + qi) * (1 + 6 * (q - qi) ^ 2 + 5 * (q - qi) ^ 4 + (q - qi) ^ 6)
        = (q ^ 7 + qi ^ 7)
          + (q ^ 5 + qi ^ 5) * (5 - 5 * (q * qi))
          + (q ^ 3 + qi ^ 3) * (6 - 15 * (q * qi) + 9 * (q ^ 2 * qi ^ 2))
          + (q + qi) * (1 - 6 * (q * qi) + 10 * (q ^ 2 * qi ^ 2) - 5 * (q ^ 3 * qi ^ 3)) := by ring
    _ = q ^ 7 + qi ^ 7 := by rw [h1, h2, h3]; ring

/-- **Closed-form Laurent identity for `m = 4` (`H = T(2,8)`)**:
`(q + q⁻¹) · 2 P₄(q - q⁻¹) = q⁹ + q⁻⁹`. -/
theorem twoMulP4_laurent (q qi : R) (hinv : q * qi = 1) :
    (q + qi) * twoMulP 4 (q - qi) = q ^ 9 + qi ^ 9 := by
  unfold twoMulP
  have h1 : q * qi = 1 := hinv
  have h2 : q ^ 2 * qi ^ 2 = 1 := by
    calc q ^ 2 * qi ^ 2 = (q * qi) ^ 2 := by ring
    _ = 1 := by rw [h1]; ring
  have h3 : q ^ 3 * qi ^ 3 = 1 := by
    calc q ^ 3 * qi ^ 3 = (q * qi) ^ 3 := by ring
    _ = 1 := by rw [h1]; ring
  have h4 : q ^ 4 * qi ^ 4 = 1 := by
    calc q ^ 4 * qi ^ 4 = (q * qi) ^ 4 := by ring
    _ = 1 := by rw [h1]; ring
  calc
    (q + qi) * (1 + 10 * (q - qi) ^ 2 + 15 * (q - qi) ^ 4 + 7 * (q - qi) ^ 6 + (q - qi) ^ 8)
        = (q ^ 9 + qi ^ 9)
          + (q ^ 7 + qi ^ 7) * (7 - 7 * (q * qi))
          + (q ^ 5 + qi ^ 5) * (15 - 35 * (q * qi) + 20 * (q ^ 2 * qi ^ 2))
          + (q ^ 3 + qi ^ 3) * (10 - 45 * (q * qi) + 63 * (q ^ 2 * qi ^ 2) - 28 * (q ^ 3 * qi ^ 3))
          + (q + qi) * (1 - 10 * (q * qi) + 30 * (q ^ 2 * qi ^ 2) - 35 * (q ^ 3 * qi ^ 3)
              + 14 * (q ^ 4 * qi ^ 4)) := by ring
    _ = q ^ 9 + qi ^ 9 := by rw [h1, h2, h3, h4]; ring

/-- **Exact reconciliation of the `W`-anchored and `Z`-anchored Higgs mass formulas**:
Under the quantum-dimension-dressed `Z/W` relation
`m_Z · P₂ · 4 = m_W · P₃ · q2²` (i.e. `m_Z / m_W = (P₃ / P₂) · ([2]_q / 2)²`),
the `W`-anchored Higgs prediction `m_W · (P₄ / P₂) · ([2]_q / 2) · C` and the
`Z`-anchored Higgs prediction `m_Z · (P₄ / P₃) · (2 / [2]_q) · C` satisfy the cleared
identity
`(m_W · P₄ · q2 · C) · (P₃ · q2) = (m_Z · P₄ · 4 · C) · P₂`
over any commutative ring `R`, for any common loop/cardinality factor `C`. -/
theorem higgs_W_Z_anchor_reconciliation
    (mW mZ P2 P3 P4 q2 C : R)
    (hZW : mZ * P2 * 4 = mW * P3 * q2 ^ 2) :
    (mW * P4 * q2 * C) * (P3 * q2) = (mZ * P4 * 4 * C) * P2 := by
  calc
    (mW * P4 * q2 * C) * (P3 * q2) = (mW * P3 * q2 ^ 2) * (P4 * C) := by ring
    _ = (mZ * P2 * 4) * (P4 * C) := by rw [← hZW]
    _ = (mZ * P4 * 4 * C) * P2 := by ring

end TracePolynomials

/-! ## Section 2: Electroweak Seifert Genus Sum (`1 + 2 + 3 = 6`) and Bring Zero-Mode (`1/π`) -/

/-- Seifert genus of the 2-component even-twist torus link `T(2, 2k)`: `g(T(2, 2k)) = k - 1`. -/
def seifertGenusTorusLink2 (k : ℕ) : ℕ := k - 1

/-- The Seifert genera of the electroweak triplet `{W = T(2,4), Z = T(2,6), H = T(2,8)}`
are `(1, 2, 3)`. -/
theorem ewTriplet_seifertGenera :
    seifertGenusTorusLink2 2 = 1 ∧
    seifertGenusTorusLink2 3 = 2 ∧
    seifertGenusTorusLink2 4 = 3 := by
  refine ⟨rfl, rfl, rfl⟩

/-- The total Seifert genus of the sub-saturating electroweak triplet `{T(2,4), T(2,6), T(2,8)}`
is `g_W + g_Z + g_H = 1 + 2 + 3 = 6`. -/
def ewSeifertGenusSum : ℕ :=
  seifertGenusTorusLink2 2 + seifertGenusTorusLink2 3 + seifertGenusTorusLink2 4

theorem ewSeifertGenusSum_eq_six : ewSeifertGenusSum = 6 := rfl

/-- **Topological coincidence on Bring's genus-4 surface**:
the sum of Seifert genera of the electroweak triplet (`1 + 2 + 3 = 6`) equals the absolute
Euler characteristic `-χ(Σ₄) = 2g - 2 = 6` derived from the `(2,4,5)` hyperbolic tiling of
Bring's surface (`bringTilingEuler = -6`). -/
theorem ewSeifertGenusSum_eq_neg_bringTilingEuler :
    (ewSeifertGenusSum : ℤ) = -bringTilingEuler := by
  rw [ewSeifertGenusSum_eq_six, bringTilingEuler_eq]
  norm_num

/-- Division-free genus relation for an electroweak sector of total Seifert genus `G_EW` on a
surface of genus `g` (with `p` standing for `π`), generalizing `QOU.AlphaEM.FormLadder.IsGenusTerm`:
`4 · p · (g - 1) · T = 2 · G_EW`. -/
def IsEWGenusTerm {R : Type*} [CommRing R] (g G_EW p T : R) : Prop :=
  4 * p * (g - 1) * T = 2 * G_EW

/-- At Bring genus `g = 4` and electroweak Seifert genus sum `G_EW = 6`, the cleared relation reads
`12 · p · T = 12`. -/
theorem isEWGenusTerm_four_six_iff {R : Type*} [CommRing R] (p T : R) :
    IsEWGenusTerm 4 6 p T ↔ 12 * p * T = 12 := by
  unfold IsEWGenusTerm
  have e1 : (4 : R) * p * (4 - 1) * T = 12 * p * T := by ring
  have e2 : (2 : R) * 6 = 12 := by norm_num
  rw [e1, e2]

/-- Over any commutative ring `R`, any `T` satisfying `p · T = 1` (i.e. `T = 1/π`) satisfies
`IsEWGenusTerm 4 6 p T`. -/
theorem isEWGenusTerm_four_six_of_mul_eq_one {R : Type*} [CommRing R] (p T : R)
     (h : p * T = 1) : IsEWGenusTerm 4 6 p T := by
  rw [isEWGenusTerm_four_six_iff]
  calc
    12 * p * T = 12 * (p * T) := by ring
    _ = 12 * 1 := by rw [h]
    _ = 12 := by ring

/-- **The Archimedean electroweak Bring zero-mode**:
the ratio of the total Seifert first-Betti count `2(g_W + g_Z + g_H) = 2 · 6 = 12` to the
Bring surface Gauss–Bonnet area `Area(Σ₄) = 4π(4 - 1) = 12π`. -/
noncomputable def ewBringZeroMode : ℝ :=
  (2 * (ewSeifertGenusSum : ℝ)) / gaussBonnetArea 4

/-- **Unconditional theorem:** `ewBringZeroMode = 1 / π`. -/
theorem ewBringZeroMode_eq_one_div_pi :
    ewBringZeroMode = 1 / Real.pi := by
  unfold ewBringZeroMode gaussBonnetArea
  rw [ewSeifertGenusSum_eq_six]
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- **Unconditional theorem:** `ewBringZeroMode` is also equal to the Seifert first-Betti sum
`12` divided by the explicit `(2,4,5)`-tiling area `bringSurfaceArea = 240 · (π - 19π/20) = 12π`,
and equals `(3 / 2) · bringZeroModeValue` (`(3/2) · 2/(3π) = 1/π`). -/
theorem ewBringZeroMode_eq_three_halves_bringZeroMode :
    (2 * (ewSeifertGenusSum : ℝ)) / bringSurfaceArea = ewBringZeroMode ∧
    ewBringZeroMode = (3 / 2 : ℝ) * bringZeroModeValue := by
  refine ⟨?_, ?_⟩
  · rw [bringSurfaceArea_eq_gaussBonnet]; rfl
  · rw [ewBringZeroMode_eq_one_div_pi]
    unfold bringZeroModeValue
    have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
    field_simp

/-! ## Section 3: Electroweak 1-Loop Schwinger Fixed-Point Cubic (`N_v = v / m_p`) -/

/-- Bare electroweak crossing complexity `q · [4]_q · [6]_q · [8]_q` on `ℝ`
(Table 1 of `electroweak-higgs-torus-link-triplet-table1-data.md`). -/
noncomputable def ewBareCrossingComplexity (q : ℝ) : ℝ :=
  q * qIntBal q 4 * qIntBal q 6 * qIntBal q 8

/-- Quantum-dimension-dressed electroweak tree complexity
`N_v^tree(q) = q · ([2]_q / 2) · [4]_q · [6]_q · [8]_q`. -/
noncomputable def ewDressedTreeComplexity (q : ℝ) : ℝ :=
  ewBareCrossingComplexity q * (qIntBal q 2 / 2)

/-- The constant part `T_EW(q) = q · ([2]_q / 2) · [4]_q · [6]_q · [8]_q + 1 / π` of the
electroweak self-consistency relation: the dressed tree complexity plus the proved Bring
Seifert-Hodge zero-mode `ewBringZeroMode = 1 / π`. -/
noncomputable def ewFixedPointConst (q : ℝ) : ℝ :=
  ewDressedTreeComplexity q + ewBringZeroMode

/-- The shared Bring harmonic-1-form normalization `H = [2]_q / (8π)` (`8π = π · b₁(Σ₄)`). -/
noncomputable def ewHabiroNorm (q : ℝ) : ℝ :=
  qIntBal q 2 / (8 * Real.pi)

/-- The Habiro deformation parameter `ℏ_q = 1 - q⁻¹`. -/
noncomputable def ewHbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- **Electroweak self-consistency (fixed-point) relation** for the inverse weak-scale crossing
count `α_v = 1 / N_v = m_p / v` at substrate parameter `q`:
`1 / α_v = T_EW(q) - α_v · H · (1 - ℏ_q² · α_v)`. -/
def IsElectroweakVevFixedPoint (q α_v : ℝ) : Prop :=
  1 / α_v = ewFixedPointConst q - α_v * ewHabiroNorm q * (1 - (ewHbarQ q) ^ 2 * α_v)

/-- The characteristic electroweak cubic
`P_EW(α_v) = ℏ_q² · H · α_v³ - H · α_v² + T_EW · α_v - 1`. -/
noncomputable def ewFixedPointCubic (q α_v : ℝ) : ℝ :=
  (ewHbarQ q) ^ 2 * ewHabiroNorm q * α_v ^ 3 - ewHabiroNorm q * α_v ^ 2
    + ewFixedPointConst q * α_v - 1

/-- **Genuine algebraic derivation (sorry-free):** For any nonzero `α_v`, the electroweak
self-consistency relation `IsElectroweakVevFixedPoint q α_v` is equivalent to `α_v` being a root
of the characteristic cubic `ewFixedPointCubic q α_v = 0`. -/
theorem ewFixedPoint_iff_cubic (q α_v : ℝ) (hα : α_v ≠ 0) :
    IsElectroweakVevFixedPoint q α_v ↔ ewFixedPointCubic q α_v = 0 := by
  unfold IsElectroweakVevFixedPoint ewFixedPointCubic
  rw [div_eq_iff hα]
  constructor
  · intro h; linear_combination -h
  · intro h; linear_combination -h

/-- **Conjecture carrier (§3b-cond, primary, content-bearing, NO instance).**
`ElectroweakVevFixedPointClass q α_v` packages the open physical claim that the inverse
electroweak crossing count `α_v = m_p / v` is a positive real root of the Bring Seifert-Hodge +
1-loop Schwinger self-consistency relation `IsElectroweakVevFixedPoint q α_v`. -/
class ElectroweakVevFixedPointClass (q α_v : ℝ) : Prop where
  /-- The inverse weak crossing count `α_v = m_p / v` is positive. -/
  alpha_v_pos : 0 < α_v
  /-- `α_v` satisfies the Bring zero-mode + 1-loop Schwinger self-consistent fixed point. -/
  fixed_point : IsElectroweakVevFixedPoint q α_v

/-- **Conditional theorem (§3b-cond):** Under `[ElectroweakVevFixedPointClass q α_v]`, `α_v` is a
root of the characteristic cubic `ewFixedPointCubic q α_v = 0`, and the constant term decomposes
with the exact Bring zero-mode `1 / π`. -/
theorem ew_vev_is_fixed_point_root (q α_v : ℝ)
    [inst : ElectroweakVevFixedPointClass q α_v] :
    ewFixedPointCubic q α_v = 0 ∧
    ewFixedPointConst q = ewDressedTreeComplexity q + 1 / Real.pi := by
  refine ⟨?_, ?_⟩
  · have hα : α_v ≠ 0 := ne_of_gt inst.alpha_v_pos
    exact (ewFixedPoint_iff_cubic q α_v hα).mp inst.fixed_point
  · unfold ewFixedPointConst
    rw [ewBringZeroMode_eq_one_div_pi]

end QOU.StandardModel
