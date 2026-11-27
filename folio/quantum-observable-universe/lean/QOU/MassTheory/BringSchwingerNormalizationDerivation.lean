import Mathlib.Tactic
import QOU.MassTheory.EmCouplingBringZeroMode
import HeckeTemperleyLieb.QIntegerCanonical

/-!
# Tiling Derivation of the Bring 1-Loop Normalization, Single-Period Ratios, and Bar-Hermitian Skein Contraction

This module formalizes the unconditional algebraic and topological structure underlying the
one-loop Bring–Schwinger fixed-point equations in the electromagnetic (`QOU.Archimedean.EmCouplingBringZeroMode`)
and electroweak (`QOU.StandardModel.ElectroweakBringSchwingerBridge`) sectors, audits the
three parameter-free Habiro/skein deformation candidates, and isolates the remaining open
physical coupling step in a unified `§3b-cond` typeclass.

## Mathematical Overview

1. **Section 1 — Tiling Derivation of `H = [2]_q / (8π)` and Single Transcendental Period Theorem.**
   Stated here over a field `K` with the period `π` carried as a symbol `p ≠ 0`
   (`habiroNormP`, `habiroNormP_div_bringZeroModeP`, `habiroNormP_div_ewBringZeroModeP`); the
   `ℝ` forms named below are in `QOU.Transcendental.MassTheory.BringSchwingerNormalizationDerivationReal`:
   On Bring's curve `Σ₄`, the `(2,4,5)` hyperbolic triangle tiling (`F = 240`, `E = 360`,
   `V = 114`) forces the Euler characteristic `χ(Σ₄) = bringTilingEuler = -6`, the first Betti
   number `b₁(Σ₄) = 2 - χ(Σ₄) = 8` (`bringTiling_b1`), and the hyperbolic surface area
   `Area(Σ₄) = bringSurfaceArea = 12π`.
   The one-loop normalization `habiroNorm q = (q + q⁻¹) / (8π)` is proved unconditionally to equal
   `(q + q⁻¹) / (π · (2 - bringTilingEuler))` (`habiroNorm_tiling_derived`): the 2-strand quantum
   dimension `[2]_q = q + q⁻¹` averaged over the `b₁(Σ₄) = 8` harmonic 1-cycles of Bring's surface,
   each carrying fundamental period `π`.
   Dividing `habiroNorm q` by the electromagnetic zero-mode `bringZeroModeValue = 2/(3π)` or by the
   electroweak zero-mode `ewBringZeroMode = 1/π` cancels the transcendental period `π` identically
   (`habiroNorm_div_bringZeroModeValue`, `habiroNorm_div_ewBringZeroMode`):
   * `habiroNorm q / bringZeroModeValue = 3 * (q + q⁻¹) / 16`,
   * `habiroNorm q / ewBringZeroMode = (q + q⁻¹) / 8 = (q + q⁻¹) / (2 - bringTilingEuler)`.
   Consequently, both fixed-point cubics depend on **only a single archimedean period** (`π` from
   the `(2,4,5)` triangle angle defect), with exact `q`-rational ratios between the one-loop
   coefficient `H` and the zero-mode shift.

2. **Section 2 — Three-Way Habiro/Skein Parameter Hierarchy and Bar-Hermitian Skein Contraction:**
   Three distinct parameter-free `(q - 1)²`-order quantities appear across the literature and
   existing modules:
   * `hbarQ q = 1 - q⁻¹` (asymmetric Iwahori–Hecke parameter),
   * `deltaHabiroSq q = (q + q⁻¹) - 2 = -(1 - q)(1 - q⁻¹)` (Habiro cyclotomic norm `(q^{1/2} - q^{-1/2})²`),
   * `hHecke q = q - q⁻¹` (balanced Hecke skein parameter from `σ² = h σ + 1`).
   Exact algebraic bridge identities (`hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq`,
   `deltaHabiroSq_eq_q_mul_hbarQ_sq`, `deltaHabiroSq_eq_neg_one_sub_mul_one_sub_inv`) and the strict
   inequality chain `0 < (hbarQ q)² < deltaHabiroSq q < (hHecke q)²` and `4 (hbarQ q)² < (hHecke q)²`
   for all `q > 1` (`habiro_skein_parameter_hierarchy_of_one_lt`) are established.
   Under the Kazhdan–Lusztig bar involution `q ↦ q⁻¹`, `hHecke` is skew-symmetric
   (`hHecke_bar_skew : hHecke q⁻¹ = -hHecke q`), so its bar-Hermitian square is strictly negative:
   `hHecke q * hHecke q⁻¹ = -(hHecke q)² < 0` (`hHecke_bar_hermitian_product`), while the
   asymmetric bar product gives `hbarQ q * hbarQ q⁻¹ = -deltaHabiroSq q < 0`
   (`hbarQ_bar_product_eq_neg_deltaHabiroSq`).
   In any commutative ring containing an invertible Hecke generator `σ` satisfying
   `σ² = h σ + 1`, the inverse is `σ⁻¹ = σ - h`, the skein vertex `S = σ - σ⁻¹` equals the
   central scalar `h`, its bar-conjugate `S̄ = σ⁻¹ - σ` equals `-h`, and their bar-Hermitian
   2-vertex contraction evaluates identically to `1 + α (S · S̄) = 1 - h² α`
   (`hecke_skein_bar_contraction`). By contrast, the raw same-chirality 2-vertex singlet
   moment excess `(q⁴ - q²) / (q² + 1)` is strictly positive for `q > 1` and of first order in
   `q - 1` (`habiro_skein_parameter_hierarchy_of_one_lt`).

3. **Section 3 (in the `ℝ` companion) — Unified Gauge Fixed-Point Homology Class (`§3b-cond`, No Global Instance):**
   The electromagnetic (`s = +1`, abelian screening, genus count `G = 4`) and electroweak
   (`s = -1`, broken non-abelian anti-screening, Seifert genus sum `G = 6`) self-consistency
   relations are unified into `IsUnifiedBringFixedPoint s T_tree G q c_loop α`, proved
   unconditionally equivalent to the characteristic cubic `unifiedBringCubic s T_tree G q c_loop α = 0`
   (`unifiedBringFixedPoint_iff_cubic`). The open physical coupling claim is packaged in the
   hypothesis-carrying typeclass `UnifiedGaugeFixedPointHomologyClass` with no global instance.
-/

namespace QOU.Archimedean
namespace BringSchwingerNormalizationDerivation

open QOU.QInteger (qIntBal)
/-! ## Section 1: Tiling Derivation of `habiroNorm` over a Symbol for the Period

The period `π` enters `habiroNorm` only as a magnitude (an area per harmonic 1-cycle), never as
an angle. Following the roots-of-unity ruling (2026-11-27), it is carried here as a ring symbol
`p ≠ 0` in a field `K` of characteristic zero; every ratio below is `p`-free, which is the
single-period statement. The `ℝ` forms with `p = Real.pi` are in
`QOU.Transcendental.MassTheory.BringSchwingerNormalizationDerivationReal`
(transcendental-boundary strangler, bean `qou-dk7p`). -/

section TilingAndSinglePeriodSymbol

variable {K : Type*} [Field K] [CharZero K]

/-- The 1-loop normalization `H(q) = (q + q⁻¹) / (8p)` with the period carried as a symbol `p`. -/
def habiroNormP (p q : K) : K :=
  (q + q⁻¹) / (8 * p)

/-- The electromagnetic Bring zero-mode `2 / (3p)` over the period symbol `p`. -/
def bringZeroModeP (p : K) : K := 2 / (3 * p)

/-- The electroweak Bring zero-mode `1 / p` over the period symbol `p`. -/
def ewBringZeroModeP (p : K) : K := 1 / p

/-- The denominator `8p` is `p · (2 - χ(Σ₄)) = p · b₁(Σ₄)`, forced by the `(2,4,5)` tiling. -/
theorem habiroNormP_tiling_derived (p q : K) :
    habiroNormP p q = (q + q⁻¹) / (p * ((2 - bringTilingEuler : ℤ) : K)) := by
  unfold habiroNormP
  rw [bringTiling_b1]
  push_cast
  ring

/-- **Single-period theorem, electromagnetic sector**: the ratio of `habiroNormP p q` to the
zero-mode `2/(3p)` is `3 (q + q⁻¹) / 16`, free of `p`. -/
theorem habiroNormP_div_bringZeroModeP (p q : K) (hp : p ≠ 0) :
    habiroNormP p q / bringZeroModeP p = 3 * (q + q⁻¹) / 16 := by
  unfold habiroNormP bringZeroModeP
  field_simp
  ring

/-- **Single-period theorem, electroweak sector**: the ratio of `habiroNormP p q` to the
zero-mode `1/p` is `(q + q⁻¹) / 8 = (q + q⁻¹) / (2 - χ(Σ₄))`, free of `p`. -/
theorem habiroNormP_div_ewBringZeroModeP (p q : K) (hp : p ≠ 0) :
    habiroNormP p q / ewBringZeroModeP p = (q + q⁻¹) / 8 ∧
    habiroNormP p q / ewBringZeroModeP p = (q + q⁻¹) / ((2 - bringTilingEuler : ℤ) : K) := by
  have h1 : habiroNormP p q / ewBringZeroModeP p = (q + q⁻¹) / 8 := by
    unfold habiroNormP ewBringZeroModeP
    field_simp
  refine ⟨h1, ?_⟩
  rw [h1, bringTiling_b1]
  push_cast
  rfl

/-- General `p`-free ratio against a genus-sum zero-mode `2G / (12p)` (area `12p`):
`habiroNormP p q / ((2G)/(12p)) = 3 (q + q⁻¹) / (4G)`. -/
theorem habiroNormP_div_general_zeroMode (p q G : K) (hp : p ≠ 0) (hG : G ≠ 0) :
    habiroNormP p q / ((2 * G) / (12 * p)) = 3 * (q + q⁻¹) / (4 * G) := by
  unfold habiroNormP
  field_simp
  ring

end TilingAndSinglePeriodSymbol


/-! ## Section 2: Three-Way Habiro/Skein Parameter Hierarchy and Bar-Hermitian Skein Contraction -/

section HabiroSkeinHierarchyAndBarInvolution

variable {K : Type*} [Field K]

/-- Asymmetric Iwahori–Hecke deformation parameter `ℏ_q = 1 - q⁻¹`
(used in `em-coupling-fixed-point.lean` and `ElectroweakBringSchwingerBridge.ewHbarQ`). -/
def hbarQ (q : K) : K := 1 - q⁻¹

/-- Balanced Hecke skein parameter `h = q - q⁻¹` from the quadratic relation `σ² = (q - q⁻¹)σ + 1`
(used in `EmCouplingBringZeroMode.lean` and `FormLadderAnchorDominance.lean`). -/
def hHecke (q : K) : K := q - q⁻¹

/-- Habiro's symmetric cyclotomic norm `δ_{\mathrm{Hab}}² = (q + q⁻¹) - 2 = -(1 - q)(1 - q⁻¹)`
(`= (q^{1/2} - q^{-1/2})² = [2]_q - 2`). -/
def deltaHabiroSq (q : K) : K := (q + q⁻¹) - 2

/-- Exact linear conversion between the balanced Hecke parameter `hHecke q = q - q⁻¹` and the
asymmetric parameter `hbarQ q = 1 - q⁻¹`: `hHecke q = (q + 1) * hbarQ q`. -/
theorem hHecke_eq_q_add_one_mul_hbarQ (q : K) (hq : q ≠ 0) :
    hHecke q = (q + 1) * hbarQ q := by
  unfold hHecke hbarQ
  field_simp
  ring

/-- Exact squared conversion: `(hHecke q)² = (q + 1)² * (hbarQ q)²`.
At `q = 1`, `(q + 1)² = 4`, so `(hHecke q)²` is approximately `4.46 × (hbarQ q)²` at `q₀ ≈ 1.11`. -/
theorem hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq (q : K) (hq : q ≠ 0) :
    (hHecke q) ^ 2 = (q + 1) ^ 2 * (hbarQ q) ^ 2 := by
  rw [hHecke_eq_q_add_one_mul_hbarQ q hq]
  ring

/-- Exact conversion between the Habiro cyclotomic norm `deltaHabiroSq q = (q + q⁻¹) - 2`
and `(hbarQ q)²`: `deltaHabiroSq q = q * (hbarQ q)²`. -/
theorem deltaHabiroSq_eq_q_mul_hbarQ_sq (q : K) (hq : q ≠ 0) :
    deltaHabiroSq q = q * (hbarQ q) ^ 2 := by
  unfold deltaHabiroSq hbarQ
  field_simp
  ring

/-- Factorization of `deltaHabiroSq q` as the negative cyclotomic norm `-(1 - q)(1 - q⁻¹)`. -/
theorem deltaHabiroSq_eq_neg_one_sub_mul_one_sub_inv (q : K) (hq : q ≠ 0) :
    deltaHabiroSq q = -((1 - q) * (1 - q⁻¹)) := by
  unfold deltaHabiroSq
  field_simp
  ring

/-- Exact relation between `(hHecke q)²` and `deltaHabiroSq q`:
`(hHecke q)² = deltaHabiroSq q * ((q + q⁻¹) + 2)` (`h² = [2]_q² - 4 = ([2]_q - 2)([2]_q + 2)`). -/
theorem hHecke_sq_eq_deltaHabiroSq_mul (q : K) (hq : q ≠ 0) :
    (hHecke q) ^ 2 = deltaHabiroSq q * ((q + q⁻¹) + 2) := by
  unfold hHecke deltaHabiroSq
  field_simp
  ring

/-- **Kazhdan–Lusztig Bar-Involution Skew-Symmetry of the Hecke Skein Parameter `hHecke`**:
Under the bar involution `q ↦ q⁻¹`, `hHecke q⁻¹ = -hHecke q`. -/
theorem hHecke_bar_skew (q : K) :
    hHecke q⁻¹ = -hHecke q := by
  unfold hHecke
  rw [inv_inv]
  ring

/-- **Bar-Hermitian Product of the Hecke Skein Parameter**:
Pairing `hHecke q` with its bar-conjugate `hHecke q⁻¹` yields `-(hHecke q)²`. -/
theorem hHecke_bar_hermitian_product (q : K) :
    hHecke q * hHecke q⁻¹ = -(hHecke q) ^ 2 := by
  rw [hHecke_bar_skew q]
  ring

/-- **Bar-Hermitian Product of the Asymmetric Parameter `hbarQ`**:
Pairing `hbarQ q = 1 - q⁻¹` with its bar-conjugate `hbarQ q⁻¹ = 1 - q` yields the negative
Habiro cyclotomic norm `-deltaHabiroSq q = (1 - q)(1 - q⁻¹)`. -/
theorem hbarQ_bar_product_eq_neg_deltaHabiroSq (q : K) (hq : q ≠ 0) :
    hbarQ q * hbarQ q⁻¹ = -deltaHabiroSq q := by
  unfold hbarQ
  rw [inv_inv, deltaHabiroSq_eq_neg_one_sub_mul_one_sub_inv q hq]
  ring

/-- **Hecke Skein Algebra Bar-Hermitian 2-Vertex Contraction Theorem**:
In any commutative ring `A` (or the commutative subalgebra generated by a single Hecke
generator `σ`), if `σ` is invertible (`σ * σ_inv = 1`) and satisfies the Hecke quadratic
relation `σ² = h * σ + 1`, then:
1. The inverse is `σ_inv = σ - h`, so the skein vertex `S = σ - σ_inv` equals the scalar `h`,
2. The bar-conjugate skein vertex `S_bar = σ_inv - σ` equals `-h`, and
3. The bar-Hermitian 2-vertex contraction evaluates identically to
   `1 + α * (S * S_bar) = 1 - h ^ 2 * α`. -/
theorem hecke_skein_bar_contraction {A : Type*} [CommRing A]
    (σ σ_inv h α : A) (hinv : σ * σ_inv = 1) (hhecke : σ ^ 2 = h * σ + 1) :
    σ - σ_inv = h ∧
    σ_inv - σ = -h ∧
    1 + α * ((σ - σ_inv) * (σ_inv - σ)) = 1 - h ^ 2 * α := by
  have hdiff : σ - σ_inv = h := by
    calc
      σ - σ_inv = σ * (σ * σ_inv) - σ_inv := by rw [hinv]; ring
      _ = σ ^ 2 * σ_inv - σ_inv := by ring
      _ = (h * σ + 1) * σ_inv - σ_inv := by rw [hhecke]
      _ = h * (σ * σ_inv) := by ring
      _ = h := by rw [hinv]; ring
  have hbar : σ_inv - σ = -h := by
    calc
      σ_inv - σ = -(σ - σ_inv) := by ring
      _ = -h := by rw [hdiff]
  refine ⟨hdiff, hbar, ?_⟩
  rw [hdiff, hbar]
  ring

/-- The raw same-chirality 2-vertex singlet moment excess `m₂(q) - 1 = (q⁴ - q²) / (q² + 1)`
evaluated in `2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md` factors as
`q² (q - 1) (q + 1) / (q² + 1)` (order `(q - 1)¹`, not `-h²`). -/
def singletSameChiralityExcess (q : K) : K :=
  (q ^ 4 - q ^ 2) / (q ^ 2 + 1)

theorem singletSameChiralityExcess_factored (q : K) :
    singletSameChiralityExcess q = q ^ 2 * (q - 1) * (q + 1) / (q ^ 2 + 1) := by
  unfold singletSameChiralityExcess
  ring

end HabiroSkeinHierarchyAndBarInvolution

/-! ## Section 2b: Strict Inequality Hierarchy over Ordered Fields (`q > 1`) -/

section OrderedHabiroSkeinHierarchy

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Strict Hierarchy of the Three Parameter-Free Habiro/Skein Factors for `q > 1`**:
For every `q > 1` in a strict ordered field `R`:
`0 < (hbarQ q)² < deltaHabiroSq q < (hHecke q)²`, `4 * (hbarQ q)² < (hHecke q)²`,
and the bar-Hermitian skein contraction `hHecke q * hHecke q⁻¹ = -(hHecke q)² < 0` is strictly
negative while the raw same-chirality singlet excess `singletSameChiralityExcess q > 0` has the
opposite sign. -/
theorem habiro_skein_parameter_hierarchy_of_one_lt (q : R) (hq1 : 1 < q) :
    0 < (hbarQ q) ^ 2 ∧
    (hbarQ q) ^ 2 < deltaHabiroSq q ∧
    deltaHabiroSq q < (hHecke q) ^ 2 ∧
    4 * (hbarQ q) ^ 2 < (hHecke q) ^ 2 ∧
    hHecke q * hHecke q⁻¹ < 0 ∧
    0 < singletSameChiralityExcess q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hqsub : 0 < q - 1 := sub_pos.mpr hq1
  have hhbar_pos : 0 < hbarQ q := by
    unfold hbarQ
    have : 1 - q⁻¹ = (q - 1) / q := by field_simp
    rw [this]
    exact div_pos hqsub hq0
  have hhbar_sq_pos : 0 < (hbarQ q) ^ 2 := sq_pos_of_pos hhbar_pos
  have hdelta_gt : (hbarQ q) ^ 2 < deltaHabiroSq q := by
    rw [deltaHabiroSq_eq_q_mul_hbarQ_sq q hqne]
    nlinarith
  have hhecke_gt_delta : deltaHabiroSq q < (hHecke q) ^ 2 := by
    rw [deltaHabiroSq_eq_q_mul_hbarQ_sq q hqne, hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq q hqne]
    have hpoly : q < (q + 1) ^ 2 := by
      have : (q + 1) ^ 2 - q = q ^ 2 + q + 1 := by ring
      nlinarith
    nlinarith
  have hq_gt_four : 4 < (q + 1) ^ 2 := by
    have : (q + 1) ^ 2 - 4 = (q - 1) * (q + 3) := by ring
    nlinarith
  have hhecke_gt_four : 4 * (hbarQ q) ^ 2 < (hHecke q) ^ 2 := by
    rw [hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq q hqne]
    nlinarith
  have hbar_neg : hHecke q * hHecke q⁻¹ < 0 := by
    rw [hHecke_bar_hermitian_product q]
    have hhecke_sq_pos : 0 < (hHecke q) ^ 2 := by linarith
    linarith
  have hsinglet_pos : 0 < singletSameChiralityExcess q := by
    rw [singletSameChiralityExcess_factored q]
    apply div_pos
    · exact mul_pos (mul_pos (sq_pos_of_pos hq0) hqsub) (by linarith)
    · positivity
  exact ⟨hhbar_sq_pos, hdelta_gt, hhecke_gt_delta, hhecke_gt_four, hbar_neg, hsinglet_pos⟩

end OrderedHabiroSkeinHierarchy


end BringSchwingerNormalizationDerivation
end QOU.Archimedean
