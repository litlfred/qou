import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical
import QOU.Braiding.WeakVertexT35TraceClosedForm
import QOU.QBeta.HadronChargeLineCoulomb
import QOU.QBeta.WeakVertexTwoTerm
import QOU.Archimedean.EmCouplingBringZeroMode
import QOU.Archimedean.BringSchwingerNormalizationDerivation

/-!
# Unconditional `[10]_q` `T(3,5)` Linchpin, Cartan-Commutant Inner Derivation, and `2 ln t = -α_EM(q)` Hadron-Line Bridge

Beans `qou-15sj`, `qou-ha6c`, `qou-itdn`, `qou-006b` (`Q-Gap-1`).

This module establishes, with `0 sorry` and `0` custom axioms and following `§7c` base-ring
generality (`[CommRing]`, `[Field]`, `[LinearOrder] + [IsStrictOrderedRing]`, specializing to `ℝ`
only where `Real.exp` / `Real.log` cross the archimedean wall):

1. **Section 1 — Genus-4 Diophantine Forcing & Bring Coincidence (`qou-15sj`, `qou-006b`):**
   * Among coprime torus knots `T(p, r)` with `2 ≤ p < r`, the double Seifert genus
     `torusKnotDoubleGenus p r = (p - 1)(r - 1)` equals the forced first Betti number
     `b₁(Σ_Bring) = 2 - bringTilingEuler = 8` (`g = 4`) if and only if `(p, r) ∈ {(2, 9), (3, 5)}`
     (`genus_four_coprime_torus_knot_iff`, `force_carrier_bring_genus_coincidence`).
   * Minimal positive-braid writhes are `w(T_{2,9}) = 9` and `w(T_{3,5}) = 10 = 2 g(T_{3,5}) + 2`,
     whereas the 2-strand meson knots `T(2,3), T(2,5), T(2,7)` have genera `1, 2, 3 < 4`
     (`meson_knots_below_bring_genus`).

2. **Section 2 — Symmetrized Alexander Polynomial `Δ_{T(3,5)}`, Burau Determinant, & `[9]_q [10]_q` (`qou-15sj`):**
   * Division-free `[CommRing R]` Laurent polynomial identities for `Δ_{T(3,5)}(q²)` and
     `Δ_{T(3,5)}(q⁴)`, plus `[Field K]` rational closed forms
     `Δ_{T(3,5)}(q²) = (q - q⁻¹)(q¹⁵ - q⁻¹⁵) / ((q³ - q⁻³)(q⁵ - q⁻⁵))` and
     `Δ_{T(3,5)}(q⁴) = (q² - q⁻²)(q³⁰ - q⁻³⁰) / ((q⁶ - q⁻⁶)(q¹⁰ - q⁻¹⁰))`, relating the strand-period
     denominator `q¹⁰ - q⁻¹⁰ = (q - q⁻¹)[10]_q` (`(q¹⁰ - q⁻¹⁰)(q + q⁻¹)/(q - q⁻¹) = [10]_q [2]_q`)
     directly to the 3-strand reduced Burau determinant `det(I₂ - q¹⁰ M) = 1 + q¹⁰ + q²⁰` computed
     from `QOU.Braiding.WeakVertexT35.stdGen0 * stdGen1` (`burau_det_T35_from_hecke`).
   * Exact Clebsch–Gordan expansion `[9]_q [10]_q = ∑_{k=1}^9 [2k]_q` and classical limit
     `q · [9]_q · [10]_q = 90` at `q = 1`.

3. **Section 3 — 3-Irrep `H₃(q)` Rosso–Jones / HOMFLY-PT Audit & `q = 1` Selectivity (`qou-15sj`, `qou-itdn`):**
   * On `β_{3,5} = (σ₀ σ₁)⁵ ∈ H₃(q)`, the three irreducible characters are `(q¹⁰, -1, q⁻¹⁰)`.
     A `q`-independent weighted sum `w₃ q¹⁰ - w₂₁ + w₁₁₁ q⁻¹⁰` collapses to `q¹⁰ - q⁻¹⁰ = (q - q⁻¹)[10]_q`
     for all `q ≠ 0` **if and only if** `(w₃, w₂₁, w₁₁₁) = (1, 0, -1)` (`t35_weighted_trace_eq_binomial_iff`),
     i.e. the partition-conjugation antisymmetric (`λ ↔ λ'`) top-channel difference, whereas the
     `N = 2` Jones and `N = 3` `sl₃` HOMFLY-PT quantum-dimension traces yield 3-term and 6-term
     Laurent polynomials (`homflySl3_T35_exact`).
   * At `q = 1`, `V_L(1) = (-2)^{c - 1}` separates link component multiplicity `c` (`1, -2, +4` for
     `c = 1, 2, 3`) while remaining blind to nucleon `U(1)_EM` charge (`qou-itdn`).

4. **Section 4 — `U(1)_EM` Cartan-Commutant Inner Derivation `[Q, ·]`, `2 ln t = -α_EM(q)`, `c_em` Pinning, & `E(Q)^conn` Positivity (`qou-ha6c`):**
   * Leibniz, trace-orthogonality, scalar-shift invariance, and gauge-rescaling covariance of the
     inner derivation `δ_Q(X) = [Q, X]` on `WeakVertexTwoTerm`, plus the Hilbert–Schmidt variance
     identity `-(1/2) Tr([Q, P₃]²) = Var_{P₃}(Q) ≥ 0`.
   * Exact Gatermann–Parrilo / Verstichel–van Aggelen Wedderburn semidefinite characterization:
     `I₃ + c_em E(Q)^conn` is positive semidefinite on `W_{±1}` **if and only if**
     `-1 ≤ c_em κ(Q) ≤ 2` (`dressedKernel_posSemidef_iff`).
   * Exact archimedean bridge `2 log t = -α ↔ t = exp(-α/2)`, alternating Taylor jet bounds
     `α - α²/2 ≤ 1 - t² ≤ α - α²/2 + α³/6` for all `α ≥ 0` (`hadronLine_jet_bounds`), and unique
     characterization of the three zero-parameter `c_em` normalization conditions (monodromy
     log-coupling, chordal holonomy jet, and categorical Lagrangian Reeb-scale ratio).
-/

namespace QOU.StandardModel.AlphaEmT35Linchpin

open Matrix
open QOU.QInteger (qIntBal qIntBal_def qIntBalCl qIntBalCl_one)
open QOU.Braiding.WeakVertexT35 (stdGen0 stdGen1 stdGen_M stdGen_M_cubed_eq_one chi21_T35)

/-! ## Section 1: Genus-4 Diophantine Forcing & Bring Coincidence (`qou-15sj`, `qou-006b`) -/

section GenusFourDiophantine

/-- Minimal positive-braid crossing number (writhe) `(p - 1) * r` of the torus knot `T(p, r)`
presented on `p` strands (`p < r`). -/
def torusKnotCrossing (p r : ℕ) : ℕ := (p - 1) * r

/-- Double Seifert genus `2 g(T_{p,r}) = (p - 1) * (r - 1)` of a coprime torus knot `T(p, r)`. -/
def torusKnotDoubleGenus (p r : ℕ) : ℕ := (p - 1) * (r - 1)

/-- Seifert genus `g(T_{p,r}) = (p - 1) * (r - 1) / 2` of a coprime torus knot `T(p, r)`. -/
def torusKnotGenus (p r : ℕ) : ℕ := (p - 1) * (r - 1) / 2

/-- Crossing number `9` and genus `4` of `T(2, 9)`. -/
theorem t29_crossing_and_genus :
    torusKnotCrossing 2 9 = 9 ∧
    torusKnotDoubleGenus 2 9 = 8 ∧
    torusKnotGenus 2 9 = 4 := by
  decide

/-- Crossing number `10`, genus `4`, and balanced Alexander span identity `2 g(T_{3,5}) + 2 = 10`
matching `w(T_{3,5}) = 10` for `T(3, 5)`. -/
theorem t35_crossing_and_genus :
    torusKnotCrossing 3 5 = 10 ∧
    torusKnotDoubleGenus 3 5 = 8 ∧
    torusKnotGenus 3 5 = 4 ∧
    2 * torusKnotGenus 3 5 + 2 = torusKnotCrossing 3 5 := by
  decide

/-- **Genus-4 Coincidence with Bring's Curve `Σ_Bring`:**
Both force-carrier torus knots `T(2, 9)` and `T(3, 5)` have double Seifert genus `8`, matching the
forced first Betti number `2 - bringTilingEuler = 8` (`g(Σ_Bring) = 4`) computed from the `(2,4,5)`
hyperbolic triangle tiling in `QOU.Archimedean.EmCouplingBringZeroMode`. -/
theorem force_carrier_bring_genus_coincidence :
    (torusKnotDoubleGenus 2 9 : ℤ) = 2 - QOU.Archimedean.bringTilingEuler ∧
    (torusKnotDoubleGenus 3 5 : ℤ) = 2 - QOU.Archimedean.bringTilingEuler ∧
    torusKnotGenus 2 9 = torusKnotGenus 3 5 := by
  rw [QOU.Archimedean.bringTiling_b1]
  decide

/-- **Unconditional Diophantine Uniqueness of the Genus-4 Force-Carrier Pair `{T(2,9), T(3,5)}`:**
Among nontrivial torus knots `T(p, r)` presented with `2 ≤ p < r` and `Nat.Coprime p r`, the
genus-4 saturation condition `torusKnotDoubleGenus p r = 8` (`g = 4`) holds if and only if
`(p, r) = (2, 9)` or `(p, r) = (3, 5)`. -/
theorem genus_four_coprime_torus_knot_iff (p r : ℕ) :
    (2 ≤ p ∧ p < r ∧ Nat.Coprime p r ∧ torusKnotDoubleGenus p r = 8) ↔
      (p = 2 ∧ r = 9) ∨ (p = 3 ∧ r = 5) := by
  constructor
  · rintro ⟨hp2, hpr, _, hgen⟩
    unfold torusKnotDoubleGenus at hgen
    have hp_le : p ≤ 3 := by
      by_contra hgt
      have hp3 : 3 ≤ p - 1 := by omega
      have hr4 : 4 ≤ r - 1 := by omega
      have hmul : 12 ≤ (p - 1) * (r - 1) := Nat.mul_le_mul hp3 hr4
      omega
    have hp_cases : p = 2 ∨ p = 3 := by omega
    rcases hp_cases with rfl | rfl
    · left
      exact ⟨rfl, by omega⟩
    · right
      exact ⟨rfl, by omega⟩
  · rintro (⟨rfl, rfl⟩ | ⟨rfl, rfl⟩) <;> decide

/-- **Meson vs Force-Carrier Genus Separation (`qou-15sj` Finding 2):**
The 2-strand odd torus knots `T(2, 3), T(2, 5), T(2, 7)` have genera `1, 2, 3`, strictly below
the Bring force-carrier genus `4`. -/
theorem meson_knots_below_bring_genus :
    torusKnotGenus 2 3 = 1 ∧
    torusKnotGenus 2 5 = 2 ∧
    torusKnotGenus 2 7 = 3 ∧
    torusKnotGenus 2 3 < torusKnotGenus 3 5 ∧
    torusKnotGenus 2 5 < torusKnotGenus 3 5 ∧
    torusKnotGenus 2 7 < torusKnotGenus 3 5 := by
  decide

end GenusFourDiophantine

/-! ## Section 2: Symmetrized Alexander Polynomial `Δ_{T(3,5)}`, Burau Determinant, & `[9]_q [10]_q` -/

section AlexanderAndTreeLaurent

section CommRingDivisionFree

variable {R : Type*} [CommRing R]

/-- Symmetrized Alexander Laurent polynomial of `T(3,5)` at `t = q²`:
`Δ_{T(3,5)}(q²) = q⁸ - q⁶ + q² - 1 + q⁻² - q⁻⁶ + q⁻⁸` (`Φ₁₅(q²) / q⁸`). -/
def deltaT35Laurent (q qinv : R) : R :=
  q ^ 8 - q ^ 6 + q ^ 2 - 1 + qinv ^ 2 - qinv ^ 6 + qinv ^ 8

/-- Symmetrized Alexander Laurent polynomial of `T(3,5)` in the skein convention `t = q⁴`
(`t^{1/2} = q²`):
`Δ_{T(3,5)}(q⁴) = q¹⁶ - q¹² + q⁴ - 1 + q⁻⁴ - q⁻¹² + q⁻¹⁶`. -/
def deltaT35SkeinLaurent (q qinv : R) : R :=
  q ^ 16 - q ^ 12 + q ^ 4 - 1 + qinv ^ 4 - qinv ^ 12 + qinv ^ 16

/-- Division-free balanced Laurent sum for `[9]_q`:
`q⁸ + q⁶ + q⁴ + q² + 1 + q⁻² + q⁻⁴ + q⁻⁶ + q⁻⁸`. -/
def qInt9Laurent (q qinv : R) : R :=
  q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1 + qinv ^ 2 + qinv ^ 4 + qinv ^ 6 + qinv ^ 8

/-- Division-free balanced Laurent sum for `[10]_q`:
`q⁹ + q⁷ + q⁵ + q³ + q + q⁻¹ + q⁻³ + q⁻⁵ + q⁻⁷ + q⁻⁹`. -/
def qInt10Laurent (q qinv : R) : R :=
  q ^ 9 + q ^ 7 + q ^ 5 + q ^ 3 + q + qinv + qinv ^ 3 + qinv ^ 5 + qinv ^ 7 + qinv ^ 9

/-- Exact division-free identity for `[9]_q` over any `CommRing`:
`(q - qinv) * qInt9Laurent q qinv = q⁹ - qinv⁹` whenever `q * qinv = 1`. -/
theorem mul_qInt9Laurent_eq_sub_pow9 (q qinv : R) (hq : q * qinv = 1) :
    (q - qinv) * qInt9Laurent q qinv = q ^ 9 - qinv ^ 9 := by
  unfold qInt9Laurent
  have h0 : q * qinv - 1 = 0 := sub_eq_zero.mpr hq
  linear_combination
    (-q ^ 7 - q ^ 5 - q ^ 3 - q + qinv + qinv ^ 3 + qinv ^ 5 + qinv ^ 7) * h0

/-- Exact division-free identity for `[10]_q` over any `CommRing`:
`(q - qinv) * qInt10Laurent q qinv = q¹⁰ - qinv¹⁰` whenever `q * qinv = 1`. -/
theorem mul_qInt10Laurent_eq_sub_pow10 (q qinv : R) (hq : q * qinv = 1) :
    (q - qinv) * qInt10Laurent q qinv = q ^ 10 - qinv ^ 10 := by
  unfold qInt10Laurent
  have h0 : q * qinv - 1 = 0 := sub_eq_zero.mpr hq
  linear_combination
    (-q ^ 8 - q ^ 6 - q ^ 4 - q ^ 2 + qinv ^ 2 + qinv ^ 4 + qinv ^ 6 + qinv ^ 8) * h0

/-- **Division-Free Symmetrized Alexander Identity at `t = q²` over any `CommRing`:**
`(q³ - q⁻³)(q⁵ - q⁻⁵) Δ_{T(3,5)}(q²) = (q - q⁻¹)(q¹⁵ - q⁻¹⁵)`. -/
theorem deltaT35Laurent_cleared (q qinv : R) (hq : q * qinv = 1) :
    (q ^ 3 - qinv ^ 3) * (q ^ 5 - qinv ^ 5) * deltaT35Laurent q qinv =
      (q - qinv) * (q ^ 15 - qinv ^ 15) := by
  have hqk : ∀ k : ℕ, q ^ k * qinv ^ k = 1 := fun k => by rw [← mul_pow, hq, one_pow]
  have hcancel : ∀ {a b : R}, q ^ 16 * a = q ^ 16 * b → a = b := by
    intro a b hab
    calc
      a = (qinv ^ 16 * q ^ 16) * a := by rw [mul_comm (qinv ^ 16), hqk 16, one_mul]
      _ = qinv ^ 16 * (q ^ 16 * a) := by ring
      _ = qinv ^ 16 * (q ^ 16 * b) := by rw [hab]
      _ = (qinv ^ 16 * q ^ 16) * b := by ring
      _ = b := by rw [mul_comm (qinv ^ 16), hqk 16, one_mul]
  apply hcancel
  have hp3 : q ^ 3 * (q ^ 3 - qinv ^ 3) = q ^ 6 - 1 := by
    calc
      q ^ 3 * (q ^ 3 - qinv ^ 3) = q ^ 6 - q ^ 3 * qinv ^ 3 := by ring
      _ = q ^ 6 - 1 := by rw [hqk 3]
  have hp5 : q ^ 5 * (q ^ 5 - qinv ^ 5) = q ^ 10 - 1 := by
    calc
      q ^ 5 * (q ^ 5 - qinv ^ 5) = q ^ 10 - q ^ 5 * qinv ^ 5 := by ring
      _ = q ^ 10 - 1 := by rw [hqk 5]
  have hp1 : q * (q - qinv) = q ^ 2 - 1 := by
    calc
      q * (q - qinv) = q ^ 2 - q * qinv := by ring
      _ = q ^ 2 - 1 := by rw [hq]
  have hp15 : q ^ 15 * (q ^ 15 - qinv ^ 15) = q ^ 30 - 1 := by
    calc
      q ^ 15 * (q ^ 15 - qinv ^ 15) = q ^ 30 - q ^ 15 * qinv ^ 15 := by ring
      _ = q ^ 30 - 1 := by rw [hqk 15]
  have hpd : q ^ 8 * deltaT35Laurent q qinv =
      q ^ 16 - q ^ 14 + q ^ 10 - q ^ 8 + q ^ 6 - q ^ 2 + 1 := by
    unfold deltaT35Laurent
    calc
      q ^ 8 * (q ^ 8 - q ^ 6 + q ^ 2 - 1 + qinv ^ 2 - qinv ^ 6 + qinv ^ 8) =
          q ^ 16 - q ^ 14 + q ^ 10 - q ^ 8 + q ^ 6 * (q ^ 2 * qinv ^ 2) -
            q ^ 2 * (q ^ 6 * qinv ^ 6) + (q ^ 8 * qinv ^ 8) := by ring
      _ = q ^ 16 - q ^ 14 + q ^ 10 - q ^ 8 + q ^ 6 - q ^ 2 + 1 := by
        rw [hqk 2, hqk 6, hqk 8]; ring
  calc
    q ^ 16 * ((q ^ 3 - qinv ^ 3) * (q ^ 5 - qinv ^ 5) * deltaT35Laurent q qinv) =
        (q ^ 3 * (q ^ 3 - qinv ^ 3)) * (q ^ 5 * (q ^ 5 - qinv ^ 5)) *
          (q ^ 8 * deltaT35Laurent q qinv) := by ring
    _ = (q ^ 6 - 1) * (q ^ 10 - 1) *
          (q ^ 16 - q ^ 14 + q ^ 10 - q ^ 8 + q ^ 6 - q ^ 2 + 1) := by
        rw [hp3, hp5, hpd]
    _ = (q ^ 2 - 1) * (q ^ 30 - 1) := by ring
    _ = (q * (q - qinv)) * (q ^ 15 * (q ^ 15 - qinv ^ 15)) := by rw [hp1, hp15]
    _ = q ^ 16 * ((q - qinv) * (q ^ 15 - qinv ^ 15)) := by ring

/-- **Division-Free Symmetrized Alexander Identity at `t = q⁴` over any `CommRing`:**
`(q⁶ - q⁻⁶)(q¹⁰ - q⁻¹⁰) Δ_{T(3,5)}(q⁴) = (q² - q⁻²)(q³⁰ - q⁻³⁰)`. -/
theorem deltaT35SkeinLaurent_cleared (q qinv : R) (hq : q * qinv = 1) :
    (q ^ 6 - qinv ^ 6) * (q ^ 10 - qinv ^ 10) * deltaT35SkeinLaurent q qinv =
      (q ^ 2 - qinv ^ 2) * (q ^ 30 - qinv ^ 30) := by
  have hq2 : q ^ 2 * qinv ^ 2 = 1 := by
    rw [← mul_pow, hq, one_pow]
  have h := deltaT35Laurent_cleared (q ^ 2) (qinv ^ 2) hq2
  have heq : deltaT35SkeinLaurent q qinv = deltaT35Laurent (q ^ 2) (qinv ^ 2) := by
    unfold deltaT35SkeinLaurent deltaT35Laurent; ring
  rw [heq]
  convert h using 1 <;> ring

/-- Classical `q = 1` evaluations over any `CommRing`:
`Δ_{T(3,5)}(1) = 1`, `[9]_1 = 9`, `[10]_1 = 10`, and `1 · [9]_1 · [10]_1 = 90`. -/
theorem classical_at_one_commRing :
    deltaT35Laurent (1 : R) 1 = 1 ∧
    deltaT35SkeinLaurent (1 : R) 1 = 1 ∧
    qInt9Laurent (1 : R) 1 = 9 ∧
    qInt10Laurent (1 : R) 1 = 10 ∧
    (1 : R) * qInt9Laurent 1 1 * qInt10Laurent 1 1 = 90 := by
  unfold deltaT35Laurent deltaT35SkeinLaurent qInt9Laurent qInt10Laurent
  refine ⟨by ring, by ring, by ring, by ring, by ring⟩

end CommRingDivisionFree

section FieldIdentities

variable {K : Type*} [Field K]

/-- Over a `Field`, `Δ_{T(3,5)}(q²)` equals the rational torus-knot Alexander quotient
`(q - q⁻¹)(q¹⁵ - q⁻¹⁵) / ((q³ - q⁻³)(q⁵ - q⁻⁵))`. -/
theorem deltaT35_at_q_sq (q : K) (hq : q ≠ 0)
    (hq3 : q ^ 3 - (q⁻¹) ^ 3 ≠ 0) (hq5 : q ^ 5 - (q⁻¹) ^ 5 ≠ 0) :
    ((q - q⁻¹) * (q ^ 15 - (q⁻¹) ^ 15)) / ((q ^ 3 - (q⁻¹) ^ 3) * (q ^ 5 - (q⁻¹) ^ 5)) =
      deltaT35Laurent q q⁻¹ := by
  have hden : (q ^ 3 - (q⁻¹) ^ 3) * (q ^ 5 - (q⁻¹) ^ 5) ≠ 0 := mul_ne_zero hq3 hq5
  rw [div_eq_iff hden]
  linear_combination -(deltaT35Laurent_cleared q q⁻¹ (mul_inv_cancel₀ hq))

/-- Over a `Field`, `Δ_{T(3,5)}(q⁴)` equals the rational skein Alexander quotient
`(q² - q⁻²)(q³⁰ - q⁻³⁰) / ((q⁶ - q⁻⁶)(q¹⁰ - q⁻¹⁰))`, whose 5-fold strand-period denominator
factor is `q¹⁰ - q⁻¹⁰ = (q - q⁻¹)[10]_q`. -/
theorem deltaT35_at_q_fourth (q : K) (hq : q ≠ 0)
    (hq6 : q ^ 6 - (q⁻¹) ^ 6 ≠ 0) (hq10 : q ^ 10 - (q⁻¹) ^ 10 ≠ 0) :
    ((q ^ 2 - (q⁻¹) ^ 2) * (q ^ 30 - (q⁻¹) ^ 30)) /
        ((q ^ 6 - (q⁻¹) ^ 6) * (q ^ 10 - (q⁻¹) ^ 10)) =
      deltaT35SkeinLaurent q q⁻¹ := by
  have hden : (q ^ 6 - (q⁻¹) ^ 6) * (q ^ 10 - (q⁻¹) ^ 10) ≠ 0 := mul_ne_zero hq6 hq10
  rw [div_eq_iff hden]
  linear_combination -(deltaT35SkeinLaurent_cleared q q⁻¹ (mul_inv_cancel₀ hq))

/-- **3-Strand Reduced Burau Determinant of `T(3,5)` from `H₃(q)` (`burau_det_T35_from_hecke`):**
For the `(2,1)` Hecke representation `M(q) = stdGen0 q * stdGen1 q` (where `(M q)³ = 1`, so the
inverse 5-period `(M q)⁻⁵` equals `M q`), the characteristic Burau factor `det(1 - q¹⁰ M(q))`
evaluates to `1 + q¹⁰ + q²⁰`, satisfying `(1 - q¹⁰) det(1 - q¹⁰ M(q)) = 1 - q³⁰`. -/
theorem burau_det_T35_from_hecke (q : K) (hq : q ≠ 0) :
    det (1 - (q ^ 10) • (stdGen0 q * stdGen1 q)) = 1 + q ^ 10 + q ^ 20 ∧
    (1 - q ^ 10) * det (1 - (q ^ 10) • (stdGen0 q * stdGen1 q)) = 1 - q ^ 30 := by
  have hdet : det (1 - (q ^ 10) • (stdGen0 q * stdGen1 q)) = 1 + q ^ 10 + q ^ 20 := by
    rw [stdGen_M q hq, det_fin_two]
    simp
    field_simp
  refine ⟨hdet, ?_⟩
  rw [hdet]
  ring

/-- Helper: `(q - q⁻¹) * qIntBal q n = q ^ n - (q⁻¹) ^ n` whenever `q - q⁻¹ ≠ 0`. -/
theorem mul_qIntBal_eq_sub (q : K) (hsub : q - q⁻¹ ≠ 0) (n : ℕ) :
    (q - q⁻¹) * qIntBal q n = q ^ n - (q⁻¹) ^ n := by
  rw [qIntBal_def, mul_div_cancel₀ _ hsub]

/-- Compatibility of `qIntBal q 9` and `qIntBal q 10` with their division-free Laurent polynomials,
plus the denominator factorization `(q¹⁰ - q⁻¹⁰)(q + q⁻¹)/(q - q⁻¹) = [10]_q [2]_q`. -/
theorem qIntBal_9_10_laurent_and_cyclotomic (q : K) (hq : q ≠ 0) (hsub : q - q⁻¹ ≠ 0) :
    qIntBal q 9 = qInt9Laurent q q⁻¹ ∧
    qIntBal q 10 = qInt10Laurent q q⁻¹ ∧
    (q ^ 10 - (q⁻¹) ^ 10) / (q - q⁻¹) = qIntBal q 10 ∧
    ((q ^ 10 - (q⁻¹) ^ 10) * (q + q⁻¹)) / (q - q⁻¹) = qIntBal q 10 * qIntBal q 2 := by
  have h9 : qIntBal q 9 = qInt9Laurent q q⁻¹ := by
    rw [qIntBal_def, div_eq_iff hsub]
    simpa [mul_comm] using (mul_qInt9Laurent_eq_sub_pow9 q q⁻¹ (mul_inv_cancel₀ hq)).symm
  have h10 : qIntBal q 10 = qInt10Laurent q q⁻¹ := by
    rw [qIntBal_def, div_eq_iff hsub]
    simpa [mul_comm] using (mul_qInt10Laurent_eq_sub_pow10 q q⁻¹ (mul_inv_cancel₀ hq)).symm
  have h2 : qIntBal q 2 = q + q⁻¹ := by
    rw [qIntBal_def, div_eq_iff hsub]
    ring
  refine ⟨h9, h10, rfl, ?_⟩
  rw [h2, mul_div_right_comm]
  rfl

/-- **`U_q(sl₂)` Clebsch–Gordan Expansion of `[9]_q [10]_q`:**
In any field `K` (`q ≠ 0`, `q - q⁻¹ ≠ 0`), the force-carrier tree product `[9]_q [10]_q` decomposes
into the sum of the nine even balanced quantum dimensions `[2]_q + [4]_q + ⋯ + [18]_q`. -/
theorem qIntBal_nine_mul_ten_clebsch_gordan (q : K) (hq : q ≠ 0) (hsub : q - q⁻¹ ≠ 0) :
    qIntBal q 9 * qIntBal q 10 =
      qIntBal q 2 + qIntBal q 4 + qIntBal q 6 + qIntBal q 8 + qIntBal q 10 +
        qIntBal q 12 + qIntBal q 14 + qIntBal q 16 + qIntBal q 18 := by
  apply mul_left_cancel₀ (pow_ne_zero 2 hsub)
  have lhs_eq :
      (q - q⁻¹) ^ 2 * (qIntBal q 9 * qIntBal q 10) =
        (q ^ 9 - (q⁻¹) ^ 9) * (q ^ 10 - (q⁻¹) ^ 10) := by
    calc
      (q - q⁻¹) ^ 2 * (qIntBal q 9 * qIntBal q 10) =
          ((q - q⁻¹) * qIntBal q 9) * ((q - q⁻¹) * qIntBal q 10) := by ring
      _ = (q ^ 9 - (q⁻¹) ^ 9) * (q ^ 10 - (q⁻¹) ^ 10) := by
          rw [mul_qIntBal_eq_sub q hsub 9, mul_qIntBal_eq_sub q hsub 10]
  have rhs_eq :
      (q - q⁻¹) ^ 2 *
          (qIntBal q 2 + qIntBal q 4 + qIntBal q 6 + qIntBal q 8 + qIntBal q 10 +
            qIntBal q 12 + qIntBal q 14 + qIntBal q 16 + qIntBal q 18) =
        (q - q⁻¹) *
          ((q ^ 2 - (q⁻¹) ^ 2) + (q ^ 4 - (q⁻¹) ^ 4) + (q ^ 6 - (q⁻¹) ^ 6) +
            (q ^ 8 - (q⁻¹) ^ 8) + (q ^ 10 - (q⁻¹) ^ 10) + (q ^ 12 - (q⁻¹) ^ 12) +
            (q ^ 14 - (q⁻¹) ^ 14) + (q ^ 16 - (q⁻¹) ^ 16) + (q ^ 18 - (q⁻¹) ^ 18)) := by
    calc
      (q - q⁻¹) ^ 2 *
          (qIntBal q 2 + qIntBal q 4 + qIntBal q 6 + qIntBal q 8 + qIntBal q 10 +
            qIntBal q 12 + qIntBal q 14 + qIntBal q 16 + qIntBal q 18) =
          (q - q⁻¹) *
            ((q - q⁻¹) * qIntBal q 2 + (q - q⁻¹) * qIntBal q 4 + (q - q⁻¹) * qIntBal q 6 +
              (q - q⁻¹) * qIntBal q 8 + (q - q⁻¹) * qIntBal q 10 + (q - q⁻¹) * qIntBal q 12 +
              (q - q⁻¹) * qIntBal q 14 + (q - q⁻¹) * qIntBal q 16 + (q - q⁻¹) * qIntBal q 18) := by
        ring
      _ = _ := by
        simp only [mul_qIntBal_eq_sub q hsub]
  rw [lhs_eq, rhs_eq]
  field_simp [hq]
  ring

/-- Classical limit of the guarded force-carrier tree complexity:
`1 * qIntBalCl 1 9 * qIntBalCl 1 10 = 90`. -/
theorem tree_complexity_at_one :
    (1 : K) * qIntBalCl (1 : K) 9 * qIntBalCl (1 : K) 10 = 90 := by
  simp only [qIntBalCl_one]
  norm_num

end FieldIdentities

end AlexanderAndTreeLaurent

/-! ## Section 3: 3-Irrep `H₃(q)` Rosso–Jones / HOMFLY-PT Audit & `q = 1` Selectivity (`qou-15sj`, `qou-itdn`) -/

section RossoJonesAndSelectivity

/-- General 3-irrep weighted trace on `T(3, 5) = (σ₀ σ₁)⁵ ∈ H₃(q)`:
`w₃ χ_{(3)} + w₂₁ χ_{(2,1)} + w₁₁₁ χ_{(1,1,1)}`, using the actual `2 × 2` `(2,1)` representation
from `QOU.Braiding.WeakVertexT35`. -/
noncomputable def t35WeightedTrace {K : Type*} [Field K] (q w3 w21 w111 : K) : K :=
  w3 * q ^ 10 + w21 * ((stdGen0 q * stdGen1 q) ^ 5).trace + w111 * (q⁻¹) ^ 10

/-- Explicit evaluation of `t35WeightedTrace` via `chi21_T35`:
`t35WeightedTrace q w3 w21 w111 = w3 * q¹⁰ - w21 + w111 * q⁻¹⁰`. -/
theorem t35WeightedTrace_eq {K : Type*} [Field K] (q w3 w21 w111 : K) (hq : q ≠ 0) :
    t35WeightedTrace q w3 w21 w111 = w3 * q ^ 10 - w21 + w111 * (q⁻¹) ^ 10 := by
  unfold t35WeightedTrace
  rw [chi21_T35 q hq]
  ring

/-- **Exact Characterization of the `[10]_q` Collapse in `H₃(q)` (`qou-15sj`):**
Over any characteristic-zero field `K`, a `q`-independent weight triple `(w3, w21, w111)` satisfies
`t35WeightedTrace q w3 w21 w111 = q¹⁰ - q⁻¹⁰` (`= (q - q⁻¹)[10]_q`) for all `q ≠ 0` **if and only if**
`(w3, w21, w111) = (1, 0, -1)` — the partition-conjugation antisymmetric (`λ ↔ λ'`) projection
where `(3)' = (1,1,1)` and self-conjugate `(2,1)' = (2,1)` cancels identically. -/
theorem t35_weighted_trace_eq_binomial_iff {K : Type*} [Field K] [CharZero K]
    (w3 w21 w111 : K) :
    (∀ q : K, q ≠ 0 → t35WeightedTrace q w3 w21 w111 = q ^ 10 - (q⁻¹) ^ 10) ↔
      (w3 = 1 ∧ w21 = 0 ∧ w111 = -1) := by
  constructor
  · intro hall
    have h1 := hall 1 one_ne_zero
    rw [t35WeightedTrace_eq 1 w3 w21 w111 one_ne_zero] at h1
    have h2 := hall 2 (by norm_num)
    rw [t35WeightedTrace_eq 2 w3 w21 w111 (by norm_num)] at h2
    have hhalf := hall (1 / 2) (by norm_num)
    rw [t35WeightedTrace_eq (1 / 2) w3 w21 w111 (by norm_num)] at hhalf
    norm_num at h1 h2 hhalf
    have hw21 : w21 = 0 := by
      linear_combination
        -((1048577 : K) / 1046529) * h1 + (1024 / 1046529 : K) * h2 +
          (1024 / 1046529 : K) * hhalf
    have hdiff : w3 - w111 = 2 := by
      linear_combination (1024 / 1048575 : K) * h2 - (1024 / 1048575 : K) * hhalf
    have hw3 : w3 = 1 := by
      linear_combination (1 / 2 : K) * h1 + (1 / 2 : K) * hw21 + (1 / 2 : K) * hdiff
    have hw111 : w111 = -1 := by
      linear_combination (1 / 2 : K) * h1 + (1 / 2 : K) * hw21 - (1 / 2 : K) * hdiff
    exact ⟨hw3, hw21, hw111⟩
  · rintro ⟨rfl, rfl, rfl⟩ q hq
    rw [t35WeightedTrace_eq q 1 0 (-1) hq]
    ring

/-- Under any `N = 2` Temperley–Lieb / Convention-D trace (`w111 = 0`), `t35WeightedTrace` never
collapses to `q¹⁰ - q⁻¹⁰` across `K`. -/
theorem t35_rowCap_excludes_binomial {K : Type*} [Field K] [CharZero K] (w3 w21 : K) :
    ¬ (∀ q : K, q ≠ 0 → t35WeightedTrace q w3 w21 0 = q ^ 10 - (q⁻¹) ^ 10) := by
  intro hall
  have ⟨_, _, h111⟩ := (t35_weighted_trace_eq_binomial_iff w3 w21 0).mp hall
  norm_num at h111

/-- Standard Jones polynomial of `T(3, 5) = 10₁₂₄`: `V_{T(3,5)}(t) = t⁴ + t⁶ - t¹⁰`. -/
def jonesT35 {R : Type*} [CommRing R] (t : R) : R :=
  t ^ 4 + t ^ 6 - t ^ 10

/-- Unframed `U_q(sl₃)` HOMFLY-PT Laurent polynomial of `T(3, 5)` (divided by `[3]_q`, prior to the
writhe framing `q⁻³⁰`): `q¹⁴ + q¹⁰ + q⁸ - 2 - q⁻⁶ + q⁻⁸`. -/
def homflySl3T35Unframed {R : Type*} [CommRing R] (q qinv : R) : R :=
  q ^ 14 + q ^ 10 + q ^ 8 - 2 - qinv ^ 6 + qinv ^ 8

/-- **Exact `U_q(sl₃)` Rosso–Jones / HOMFLY-PT Closed Form for `T(3, 5)`:**
Summing `χ_λ((σ₀ σ₁)⁵)` weighted by the `sl₃` quantum Schur dimensions
`d_{(3)}^{(3)} = [4]_q [5]_q / [2]_q`, `d_{(2,1)}^{(3)} = [2]_q [4]_q`, `d_{(1,1,1)}^{(3)} = 1`
and normalizing by `[3]_q` yields the 6-term Laurent polynomial `homflySl3T35Unframed q q⁻¹`. -/
theorem homflySl3_T35_exact {K : Type*} [Field K] (q : K) (hq : q ≠ 0)
    (hsub : q - q⁻¹ ≠ 0) (hq2 : qIntBal q 2 ≠ 0) (hq3 : qIntBal q 3 ≠ 0) :
    (((qIntBal q 4 * qIntBal q 5 / qIntBal q 2) * q ^ 10 -
        (qIntBal q 2 * qIntBal q 4) + (q⁻¹) ^ 10) / qIntBal q 3) =
      homflySl3T35Unframed q q⁻¹ := by
  have hb2 : qIntBal q 2 = q + q⁻¹ := by
    rw [qIntBal_def, div_eq_iff hsub]; ring
  have hb3 : qIntBal q 3 = q ^ 2 + 1 + (q⁻¹) ^ 2 := by
    rw [qIntBal_def, div_eq_iff hsub]
    field_simp [hq]
    ring
  have hb4 : qIntBal q 4 = (q + q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) := by
    rw [qIntBal_def, div_eq_iff hsub]
    field_simp [hq]
    ring
  have hb5 : qIntBal q 5 = q ^ 4 + q ^ 2 + 1 + (q⁻¹) ^ 2 + (q⁻¹) ^ 4 := by
    rw [qIntBal_def, div_eq_iff hsub]
    field_simp [hq]
    ring
  have hdiv2 : qIntBal q 4 * qIntBal q 5 / qIntBal q 2 =
      (q ^ 2 + (q⁻¹) ^ 2) * (q ^ 4 + q ^ 2 + 1 + (q⁻¹) ^ 2 + (q⁻¹) ^ 4) := by
    rw [div_eq_iff hq2, hb4, hb5, hb2]
    ring
  rw [div_eq_iff hq3, hdiv2, hb2, hb4, hb3]
  unfold homflySl3T35Unframed
  field_simp [hq]
  ring

/-- Classical `q = 1` evaluations of the `N = 2` Jones and `N = 3` HOMFLY-PT invariants of `T(3,5)`:
both equal `1` (single-component knot `c = 1`). -/
theorem jones_and_homflySl3_T35_at_one {R : Type*} [CommRing R] :
    jonesT35 (1 : R) = 1 ∧ homflySl3T35Unframed (1 : R) 1 = 1 := by
  unfold jonesT35 homflySl3T35Unframed
  exact ⟨by ring, by ring⟩

/-- Classical Jones value `V_L(1) = (-2)^{c - 1}` of a `c`-component link (`c ≥ 1`). -/
def classicalJonesAtOne (components : ℕ) : ℤ :=
  (-2 : ℤ) ^ (components - 1)

/-- **`q = 1` Interface Selectivity (`qou-itdn`):**
At `q = 1`, `V_L(1) = (-2)^{c - 1}` separates knots (`c = 1 ↦ 1`: unknot, leptons, `T(2,9)`, `T(3,5)`),
2-component Hopf links (`c = 2 ↦ -2`), and 3-component Borromean links (`c = 3 ↦ +4`), while
remaining identical (`+4`) for proton and neutron `c = 3` carriers; `U(1)_EM` charge separation at
`q = 1` resides strictly on the hadron charge line `HadronChargeLineCoulomb.emEnergy t` (`t ≠ 1`). -/
theorem classicalJonesAtOne_selectivity :
    classicalJonesAtOne 1 = 1 ∧
    classicalJonesAtOne 2 = -2 ∧
    classicalJonesAtOne 3 = 4 ∧
    classicalJonesAtOne 1 ≠ classicalJonesAtOne 2 ∧
    classicalJonesAtOne 1 ≠ classicalJonesAtOne 3 ∧
    classicalJonesAtOne 2 ≠ classicalJonesAtOne 3 := by
  decide

end RossoJonesAndSelectivity

/-! ## Section 4: `U(1)_EM` Cartan-Commutant Inner Derivation, `2 ln t = -α_EM(q)`, & `c_em` Pinning -/

section CartanInnerDerivationAndTwoTerm

/-- Inner derivation `δ_D(X) = [D, X] = D * X - X * D` on `n × n` matrices over a `CommRing`. -/
def innerDeriv {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (D X : Matrix n n R) : Matrix n n R :=
  D * X - X * D

/-- **Leibniz Derivation Law** for `innerDeriv D = [D, ·]`:
`[D, X Y] = [D, X] Y + X [D, Y]`. -/
theorem innerDeriv_leibniz {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (D X Y : Matrix n n R) :
    innerDeriv D (X * Y) = innerDeriv D X * Y + X * innerDeriv D Y := by
  unfold innerDeriv
  noncomm_ring

/-- **Trace Vanishing** of `innerDeriv D X`: `Tr([D, X]) = 0`. -/
theorem trace_innerDeriv_eq_zero {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (D X : Matrix n n R) :
    (innerDeriv D X).trace = 0 := by
  unfold innerDeriv
  rw [Matrix.trace_sub, Matrix.trace_mul_comm, sub_self]

/-- **Cartan-Commutant Orthogonality:** For any `C` in the Cartan commutant (`innerDeriv D C = 0`,
i.e. `D * C = C * D`), `Tr(C * [D, X]) = 0`. -/
theorem trace_mul_innerDeriv_eq_zero_of_comm {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n]
    (D C X : Matrix n n R) (hcomm : D * C = C * D) :
    (C * innerDeriv D X).trace = 0 := by
  unfold innerDeriv
  rw [Matrix.mul_sub, Matrix.trace_sub, ← mul_assoc, ← hcomm, mul_assoc,
    Matrix.trace_mul_comm D (C * X), mul_assoc, sub_self]

/-- Entrywise action of the Cartan inner derivation `δ_{diag(Q)}(X)`:
`([diag(Q), X])_{i,j} = (Q_i - Q_j) X_{i,j}` (off-diagonal charge transfer `ΔQ_{ij}`). -/
theorem innerDeriv_diagonal_apply {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n]
    (Q : n → R) (X : Matrix n n R) (i j : n) :
    innerDeriv (diagonal Q) X i j = (Q i - Q j) * X i j := by
  unfold innerDeriv
  simp [Matrix.sub_apply, Matrix.diagonal_mul, Matrix.mul_diagonal]
  ring

/-- Scalar zero-point shift invariance of the inner derivation: `[D + c • 1, X] = [D, X]`. -/
theorem innerDeriv_shift_scalar {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n]
    (D X : Matrix n n R) (c : R) :
    innerDeriv (D + c • (1 : Matrix n n R)) X = innerDeriv D X := by
  unfold innerDeriv
  simp [add_mul, mul_add]

section WeakVertexGaugeAndPositivity

open QOU.QBeta.WeakVertexTwoTerm (nrm vvT P3 Econn kappa twoTerm)

/-- **Gauge Zero-Point Shift Invariance of `kappa`, `Econn`, and `twoTerm`:**
Shifting `Q ↦ Q + c` (the kernel of `Q ↦ innerDeriv (diagonal Q)`) leaves `kappa q Q`,
`Econn q Q`, and `twoTerm q c_em Qp Qm` identically invariant. -/
theorem weakVertex_shift_invariance {K : Type*} [Field K] [CharZero K]
    (q c_em cp cm : K) (Qp Qm : Fin 3 → K) (hn : nrm q ≠ 0) :
    kappa q (fun i => Qp i + cp) = kappa q Qp ∧
    Econn q (fun i => Qp i + cp) = Econn q Qp ∧
    twoTerm q c_em (fun i => Qp i + cp) (fun i => Qm i + cm) = twoTerm q c_em Qp Qm := by
  have hkp : kappa q (fun i => Qp i + cp) = kappa q Qp := by
    rw [QOU.QBeta.WeakVertexTwoTerm.kappa_eq q _ hn, QOU.QBeta.WeakVertexTwoTerm.kappa_eq q Qp hn]
    unfold nrm at hn ⊢
    field_simp
    ring
  have hkm : kappa q (fun i => Qm i + cm) = kappa q Qm := by
    rw [QOU.QBeta.WeakVertexTwoTerm.kappa_eq q _ hn, QOU.QBeta.WeakVertexTwoTerm.kappa_eq q Qm hn]
    unfold nrm at hn ⊢
    field_simp
    ring
  have hec_p : Econn q (fun i => Qp i + cp) = Econn q Qp := by
    rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq, QOU.QBeta.WeakVertexTwoTerm.Econn_eq, hkp]
  have hec_m : Econn q (fun i => Qm i + cm) = Econn q Qm := by
    rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq, QOU.QBeta.WeakVertexTwoTerm.Econn_eq, hkm]
  refine ⟨hkp, hec_p, ?_⟩
  simp only [twoTerm, QOU.QBeta.WeakVertexTwoTerm.tTwo, hec_p, hec_m]

/-- **Gauge Charge-Scaling Covariance of `twoTerm`:**
Under charge-unit rescaling `Qp ↦ s • Qp`, `Qm ↦ s • Qm` (`s ≠ 0`), `twoTerm` is strictly
scale-invariant under `c_em ↦ s⁻¹ * c_em`:
`twoTerm q (s⁻¹ * c_em) (s • Qp) (s • Qm) = twoTerm q c_em Qp Qm`. -/
theorem twoTerm_gauge_scale_invariance {K : Type*} [Field K] [CharZero K]
    (q c_em s : K) (hs : s ≠ 0) (Qp Qm : Fin 3 → K) :
    twoTerm q (s⁻¹ * c_em) (fun i => s * Qp i) (fun i => s * Qm i) =
      twoTerm q c_em Qp Qm := by
  have hkp : kappa q (fun i => s * Qp i) = s * kappa q Qp := by
    simp [kappa, Matrix.trace_fin_three, Matrix.mul_apply, diagonal]
    ring
  have hkm : kappa q (fun i => s * Qm i) = s * kappa q Qm := by
    simp [kappa, Matrix.trace_fin_three, Matrix.mul_apply, diagonal]
    ring
  have hec_p : Econn q (fun i => s * Qp i) = s • Econn q Qp := by
    rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq, QOU.QBeta.WeakVertexTwoTerm.Econn_eq, hkp, smul_smul]
  have hec_m : Econn q (fun i => s * Qm i) = s • Econn q Qm := by
    rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq, QOU.QBeta.WeakVertexTwoTerm.Econn_eq, hkm, smul_smul]
  simp only [twoTerm, QOU.QBeta.WeakVertexTwoTerm.tTwo, hec_p, hec_m,
    Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul]
  field_simp [hs]

/-- **Cartan Inner-Derivation Hilbert–Schmidt Variance Identity on `P₃`:**
`-(1/2) Tr([diag(Q), P₃]²) = (1/2) ∑_{i,j} ([diag(Q), P₃]_{i,j})² = Tr(diag(Q²) P₃) - (Tr(diag(Q) P₃))²`. -/
theorem innerDeriv_P3_hilbert_schmidt_variance {K : Type*} [Field K] [CharZero K]
    (q : K) (Q : Fin 3 → K) (hn : nrm q ≠ 0) :
    -(1 / 2 : K) * (innerDeriv (diagonal Q) (P3 q) * innerDeriv (diagonal Q) (P3 q)).trace =
      (1 / 2 : K) * ∑ i : Fin 3, ∑ j : Fin 3, (innerDeriv (diagonal Q) (P3 q) i j) ^ 2 ∧
    -(1 / 2 : K) * (innerDeriv (diagonal Q) (P3 q) * innerDeriv (diagonal Q) (P3 q)).trace =
      (diagonal (fun i => (Q i) ^ 2) * P3 q).trace - (diagonal Q * P3 q).trace ^ 2 := by
  have hp3_entry : ∀ i j : Fin 3, P3 q i j = (nrm q)⁻¹ * vvT q i j := fun _ _ => rfl
  have hd_entry : ∀ i j : Fin 3, innerDeriv (diagonal Q) (P3 q) i j =
      (Q i - Q j) * ((nrm q)⁻¹ * vvT q i j) := by
    intro i j
    rw [innerDeriv_diagonal_apply, hp3_entry]
  have hlhs :
      (innerDeriv (diagonal Q) (P3 q) * innerDeriv (diagonal Q) (P3 q)).trace =
        -∑ i : Fin 3, ∑ j : Fin 3, ((Q i - Q j) * ((nrm q)⁻¹ * vvT q i j)) ^ 2 := by
    simp only [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three, hd_entry, vvT,
      Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons]
    ring
  have hrhs1 :
      ∑ i : Fin 3, ∑ j : Fin 3, (innerDeriv (diagonal Q) (P3 q) i j) ^ 2 =
        ∑ i : Fin 3, ∑ j : Fin 3, ((Q i - Q j) * ((nrm q)⁻¹ * vvT q i j)) ^ 2 := by
    simp only [hd_entry]
  refine ⟨by rw [hlhs, hrhs1]; ring, ?_⟩
  rw [hlhs]
  unfold nrm at hn
  simp only [Fin.sum_univ_three, Matrix.trace_fin_three, Matrix.diagonal_mul, hp3_entry, vvT, nrm]
  simp only [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons]
  field_simp [hn]
  ring

/-- **Gatermann–Parrilo Wedderburn Isotypic Decomposition & Frobenius Norm of `E(Q)^conn`:**
`E(Q)^conn = κ(Q) • P₃ + (-κ(Q)/2) • (1 - P₃)` and `Tr((E(Q)^conn)²) = (3/2) κ(Q)²`. -/
theorem Econn_wedderburn_and_trace_sq {K : Type*} [Field K] [CharZero K]
    (q : K) (Q : Fin 3 → K) (hn : nrm q ≠ 0) :
    Econn q Q = kappa q Q • P3 q + (-kappa q Q / 2) • (1 - P3 q) ∧
    (Econn q Q * Econn q Q).trace = (3 / 2 : K) * (kappa q Q) ^ 2 := by
  refine ⟨?_, ?_⟩
  · rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq]
    ext i j
    simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
    ring
  · rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq]
    have hP3_idem := QOU.QBeta.WeakVertexTwoTerm.P3_idem q hn
    have htrP3 := QOU.QBeta.WeakVertexTwoTerm.trace_P3 q hn
    have hsq :
        ((3 / 2 : K) • P3 q - (1 / 2 : K) • (1 : Matrix (Fin 3) (Fin 3) K)) *
          ((3 / 2 : K) • P3 q - (1 / 2 : K) • (1 : Matrix (Fin 3) (Fin 3) K)) =
        (3 / 4 : K) • P3 q + (1 / 4 : K) • (1 : Matrix (Fin 3) (Fin 3) K) := by
      ext i j
      have hij := congr_fun (congr_fun hP3_idem i) j
      simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul,
        one_mul, mul_one, Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply,
        smul_eq_mul]
      rw [hij]
      ring
    rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, hsq, Matrix.trace_smul, Matrix.trace_add,
      Matrix.trace_smul, Matrix.trace_smul, htrP3, Matrix.trace_one, Fintype.card_fin]
    simp only [smul_eq_mul]
    norm_num
    ring

/-- Quadratic form `xᵀ M x = ∑_{i,j} x_i M_{i,j} x_j` on `Fin 3 → F`. -/
def quadForm {F : Type*} [CommRing F] (M : Matrix (Fin 3) (Fin 3) F) (x : Fin 3 → F) : F :=
  ∑ i : Fin 3, ∑ j : Fin 3, x i * M i j * x j

/-- **Exact Gatermann–Parrilo / Verstichel–van Aggelen Positivity Theorem for `1 + c_em • E(Q)^conn`:**
Over any strict ordered field `F`, the dressed two-term commutant kernel
`1 + c_em • Econn q Q` is positive semidefinite on `W_{±1}` (`∀ x, 0 ≤ xᵀ (1 + c_em E^conn) x`)
**if and only if** `-1 ≤ c_em * kappa q Q ∧ c_em * kappa q Q ≤ 2`. -/
theorem dressedKernel_posSemidef_iff {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (q c_em : F) (Q : Fin 3 → F) :
    (∀ x : Fin 3 → F, 0 ≤ quadForm (1 + c_em • Econn q Q) x) ↔
      (-1 ≤ c_em * kappa q Q ∧ c_em * kappa q Q ≤ 2) := by
  have hn_pos : 0 < nrm q := by
    unfold nrm
    positivity
  have hn : nrm q ≠ 0 := ne_of_gt hn_pos
  have hn_expanded : 1 + q ^ 2 + q ^ 4 ≠ 0 := hn
  have hq2_pos : 0 < q ^ 2 + 1 := by positivity
  constructor
  · intro hpsd
    have hv := hpsd ![1, q, q ^ 2]
    have hw := hpsd ![q, -1, 0]
    have hv_eq :
        quadForm (1 + c_em • Econn q Q) ![1, q, q ^ 2] =
          (1 + c_em * kappa q Q) * nrm q := by
      rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq]
      unfold quadForm P3 vvT nrm
      simp [Fin.sum_univ_three]
      field_simp [hn_expanded]
      ring
    have hw_eq :
        quadForm (1 + c_em • Econn q Q) ![q, -1, 0] =
          (1 - c_em * kappa q Q / 2) * (q ^ 2 + 1) := by
      rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq]
      unfold quadForm P3 vvT nrm
      simp [Fin.sum_univ_three]
      field_simp [hn_expanded]
      ring
    rw [hv_eq] at hv
    rw [hw_eq] at hw
    have h1 : 0 ≤ 1 + c_em * kappa q Q := nonneg_of_mul_nonneg_left hv hn_pos
    have h2 : 0 ≤ 1 - c_em * kappa q Q / 2 := nonneg_of_mul_nonneg_left hw hq2_pos
    exact ⟨by linarith, by linarith⟩
  · rintro ⟨hlow, hhigh⟩ x
    have hexpand :
        quadForm (1 + c_em • Econn q Q) x =
          ((1 + c_em * kappa q Q) * (x 0 + q * x 1 + q ^ 2 * x 2) ^ 2 +
            (1 - c_em * kappa q Q / 2) *
              ((q * x 0 - x 1) ^ 2 + (q ^ 2 * x 0 - x 2) ^ 2 + (q ^ 2 * x 1 - q * x 2) ^ 2)) /
            nrm q := by
      rw [QOU.QBeta.WeakVertexTwoTerm.Econn_eq]
      unfold quadForm P3 vvT nrm
      simp [Fin.sum_univ_three]
      field_simp [hn_expanded]
      ring
    rw [hexpand]
    apply div_nonneg _ (le_of_lt hn_pos)
    have ha : 0 ≤ 1 + c_em * kappa q Q := by linarith
    have hb : 0 ≤ 1 - c_em * kappa q Q / 2 := by linarith
    positivity

end WeakVertexGaugeAndPositivity

end CartanInnerDerivationAndTwoTerm

/-! ## Section 5: Archimedean Bridge `2 ln t = -α_EM(q)`, Jet Bounds, & `c_em` Normalizations (`ℝ`) -/

section ArchimedeanHadronLineBridge

/-- Hadron charge-line coupling `t(α) = exp(-α / 2)` on `ℝ` (`Uses Real.exp — archimedean wall`). -/
noncomputable def hadronLineParam (α : ℝ) : ℝ :=
  Real.exp (-α / 2)

theorem hadronLineParam_pos (α : ℝ) : 0 < hadronLineParam α := by
  unfold hadronLineParam
  exact Real.exp_pos _

/-- Exact logarithmic coupling identity: `2 * log (hadronLineParam α) = -α`. -/
theorem two_log_hadronLineParam_eq_neg_alpha (α : ℝ) :
    2 * Real.log (hadronLineParam α) = -α := by
  unfold hadronLineParam
  rw [Real.log_exp]
  ring

/-- **Bidirectional Equivalence (`2 ln t = -α ↔ t = exp(-α / 2)`):**
For any `t > 0`, the `HadronChargeLineCoulomb` pair splitting `2 log t` equals `-α` if and only if
`t = exp(-α / 2)`. -/
theorem two_log_eq_neg_alpha_iff (t α : ℝ) (ht : 0 < t) :
    2 * Real.log t = -α ↔ t = hadronLineParam α := by
  unfold hadronLineParam
  constructor
  · intro h
    have hlog : Real.log t = -α / 2 := by linarith
    rw [← hlog, Real.exp_log ht]
  · rintro rfl
    exact two_log_hadronLineParam_eq_neg_alpha α

/-- Exact hadron-line pair energy and `(pp - nn)` splitting at `t = exp(-α / 2)` (`qou-ha6c`). -/
theorem hadronLine_emEnergy_and_pp_sub_nn (Ef : ℕ → ℕ → ℝ) (hiso : Ef 2 2 = Ef 1 1)
    (α : ℝ) (nA nB : ℕ) :
    QOU.QBeta.HadronChargeLineCoulomb.emEnergy (hadronLineParam α) nA nB =
      -α * ((QOU.QBeta.HadronChargeLineCoulomb.chargeOf nA : ℝ) *
        (QOU.QBeta.HadronChargeLineCoulomb.chargeOf nB : ℝ)) ∧
    (Ef 2 2 + QOU.QBeta.HadronChargeLineCoulomb.emEnergy (hadronLineParam α) 2 2) -
      (Ef 1 1 + QOU.QBeta.HadronChargeLineCoulomb.emEnergy (hadronLineParam α) 1 1) = -α := by
  have ht := hadronLineParam_pos α
  refine ⟨?_, ?_⟩
  · rw [QOU.QBeta.HadronChargeLineCoulomb.log_monodromy _ ht, two_log_hadronLineParam_eq_neg_alpha]
  · rw [QOU.QBeta.HadronChargeLineCoulomb.total_pp_sub_nn Ef hiso _ ht,
      two_log_hadronLineParam_eq_neg_alpha]

/-- Exact double-braiding holonomy square `(hadronLineParam α)² = exp(-α)`. -/
theorem hadronLineParam_sq (α : ℝ) :
    (hadronLineParam α) ^ 2 = Real.exp (-α) := by
  unfold hadronLineParam
  rw [← Real.exp_nat_mul]
  congr 1
  ring

/-- **Rigorous Alternating Taylor Jet Bounds for `1 - t² = 1 - exp(-α)` (`hadronLine_jet_bounds`):**
For every `α ≥ 0`, the double-braiding chordal holonomy defect `1 - (hadronLineParam α)²` satisfies
`α - α²/2 ≤ 1 - t² ≤ α - α²/2 + α³/6` (and `1 - t² ≤ α`). -/
theorem hadronLine_jet_bounds (α : ℝ) (hα : 0 ≤ α) :
    1 - (hadronLineParam α) ^ 2 ≤ α ∧
    α - α ^ 2 / 2 ≤ 1 - (hadronLineParam α) ^ 2 ∧
    1 - (hadronLineParam α) ^ 2 ≤ α - α ^ 2 / 2 + α ^ 3 / 6 := by
  rw [hadronLineParam_sq]
  have h1 : 1 - α ≤ Real.exp (-α) := by
    have := Real.add_one_le_exp (-α)
    linarith
  have hub1 : 1 - Real.exp (-α) ≤ α := by linarith
  have hg2_mono : MonotoneOn (fun x : ℝ => 1 - x + x ^ 2 / 2 - Real.exp (-x)) (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · fun_prop
    · fun_prop
    · intro x hx
      have hderiv : HasDerivAt (fun y : ℝ => 1 - y + y ^ 2 / 2 - Real.exp (-y))
          (-1 + x + Real.exp (-x)) x := by
        have hd1 : HasDerivAt (fun y : ℝ => 1 - y + y ^ 2 / 2) (-1 + x) x := by
          convert ((hasDerivAt_const x (1 : ℝ)).sub (hasDerivAt_id x)).add
            (((hasDerivAt_pow 2 x).div_const 2)) using 1
          ring
        have hd2 : HasDerivAt (fun y : ℝ => Real.exp (-y)) (-Real.exp (-x)) x := by
          simpa using (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_id x).neg
        convert hd1.sub hd2 using 1
        ring
      rw [hderiv.deriv]
      have := Real.add_one_le_exp (-x)
      linarith
  have hg2_nonneg : 0 ≤ 1 - α + α ^ 2 / 2 - Real.exp (-α) := by
    have h0 := hg2_mono (Set.left_mem_Ici) hα hα
    simp at h0
    linarith
  have hg3_mono : MonotoneOn (fun x : ℝ => x - x ^ 2 / 2 + x ^ 3 / 6 - (1 - Real.exp (-x)))
      (Set.Ici 0) := by
    apply monotoneOn_of_deriv_nonneg (convex_Ici 0)
    · fun_prop
    · fun_prop
    · intro x hx
      have hx0 : 0 ≤ x := (Set.mem_Ioi.mp (interior_Ici (a := (0 : ℝ)) ▸ hx)).le
      have hderiv : HasDerivAt (fun y : ℝ => y - y ^ 2 / 2 + y ^ 3 / 6 - (1 - Real.exp (-y)))
          (1 - x + x ^ 2 / 2 - Real.exp (-x)) x := by
        have hd1 : HasDerivAt (fun y : ℝ => y - y ^ 2 / 2 + y ^ 3 / 6)
            (1 - x + x ^ 2 / 2) x := by
          convert ((hasDerivAt_id x).sub ((hasDerivAt_pow 2 x).div_const 2)).add
            ((hasDerivAt_pow 3 x).div_const 6) using 1
          ring
        have hd2 : HasDerivAt (fun y : ℝ => 1 - Real.exp (-y)) (Real.exp (-x)) x := by
          have hexp : HasDerivAt (fun y : ℝ => Real.exp (-y)) (-Real.exp (-x)) x := by
            simpa using (Real.hasDerivAt_exp (-x)).comp x (hasDerivAt_id x).neg
          convert (hasDerivAt_const x (1 : ℝ)).sub hexp using 1
          ring
        exact hd1.sub hd2
      rw [hderiv.deriv]
      have h0 := hg2_mono (Set.left_mem_Ici) hx0 hx0
      simp at h0
      linarith
  have hg3_nonneg : 0 ≤ α - α ^ 2 / 2 + α ^ 3 / 6 - (1 - Real.exp (-α)) := by
    have h0 := hg3_mono (Set.left_mem_Ici) hα hα
    simp at h0
    linarith
  exact ⟨hub1, by linarith, by linarith⟩

/-- **Unique Zero-Parameter `c_em` Pinning Characterization (`cEm_normalization_characterization`):**
Characterizes the three parameter-free normalization conditions fixing `c_em` without empirical input:
1. **Monodromy log-coupling matching:** `c_em = -2 log (hadronLineParam α)` uniquely pins `c_em = α`.
2. **Chordal holonomy defect matching:** `c_em = 1 - (hadronLineParam α)²` uniquely pins
   `c_em = 1 - exp(-α)` (agreeing with `α` to `O(α²)` via `hadronLine_jet_bounds`).
3. **Categorical Lagrangian Reeb-scale matching:** equating the two-term nucleon Coulomb prefactor
   `(1 - q⁻¹)² * (c_em / 3)` (`NucleonQEDCovariance`) to the `CategoricalLagrangian` matter Reeb
   prefactor `(1 - q⁻¹) * (k / 3)` (`1 - q⁻¹ ≠ 0`) uniquely pins `c_em = k / (1 - q⁻¹)`. -/
theorem cEm_normalization_characterization (c_em α q k : ℝ) (hq1 : 1 - q⁻¹ ≠ 0) :
    (c_em = -2 * Real.log (hadronLineParam α) ↔ c_em = α) ∧
    (c_em = 1 - (hadronLineParam α) ^ 2 ↔ c_em = 1 - Real.exp (-α)) ∧
    ((1 - q⁻¹) ^ 2 * (c_em / 3) = (1 - q⁻¹) * (k / 3) ↔ c_em = k / (1 - q⁻¹)) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [show -2 * Real.log (hadronLineParam α) = -(2 * Real.log (hadronLineParam α)) by ring,
      two_log_hadronLineParam_eq_neg_alpha, neg_neg]
  · rw [hadronLineParam_sq]
  · constructor
    · intro h
      have h' : (1 - q⁻¹) * c_em = k := by
        have hmul : (1 - q⁻¹) * ((1 - q⁻¹) * c_em - k) = 0 := by linear_combination 3 * h
        rcases mul_eq_zero.mp hmul with hzero | hsub
        · exact absurd hzero hq1
        · linarith
      rw [eq_div_iff hq1, mul_comm]
      exact h'
    · rintro rfl
      field_simp [hq1]

end ArchimedeanHadronLineBridge

end QOU.StandardModel.AlphaEmT35Linchpin
