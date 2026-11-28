/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.BringsSurface.BringMapChain
import QOU.Core.LawvereCut
import QOU.MassTheory.EmFormBLoopMeasure
import QOU.MassTheory.EmPhotonJoinRules
import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.StandardModel.ElectroweakVevFixedPointDecomposition
import QOU.StandardModel.ElectroweakVevGaps
import QOU.Transcendental.MassTheory.AlphaEmFormCConditionalContent
import QOU.Transcendental.MassTheory.BringSchwingerNormalizationDerivationReal
import QOU.Transcendental.StandardModel.ElectroweakVevGapsReal

/-!
# Conditional-to-Proved Discharge for the Electroweak Weak Scale (`qou-vhm1`)

This module audits and shrinks the conditional hypothesis surface backing the electroweak vacuum
expectation value row (`v_weak = 246.219644 GeV`, `-29.37 ppb`, `-0.11σ` in `ACCURACY.md` Table
3.4a) by proving every algebraically and combinatorially dischargeable step unconditionally from
the theorems landed on `main` (`BringMapChain`, `EmPhotonJoinRules`, `EmFormBLoopMeasure`,
`AnomalyFreeHyperchargeUniqueness`, and `LawvereCut`), with **zero `sorry`**, **zero custom
axioms**, **zero `[Field]` / `field_simp` markers**, and **zero transcendental tokens**:

1. **Section 1 — Finite `S₅` Regular-Map Discharge of Bring Genus `g = 4`, `χ = -6`, `b₁ = 8`,
   and Zero-Mode Period Cancellation (`BringMapChain`):**
   - Discharges the smooth-surface / triangulation assumption on Bring's curve directly from the
     connected finite `S₅` dart map `(σ, α)` (`BringMapChain.bring_chi`, `bring_genus`,
     `bring_connected`): `V - E + F = 30 - 60 + 24 = -6`, forcing unique genus `g = 4`, first
     Betti number `b₁ = 2 - χ = 8`, and `ewSeifertSum = 1 + 2 + 3 = 6 = -χ`.
   - Proves over any `[CommRing R]` with invertible period symbol `p : Rˣ` that the cleared
     Gauss–Bonnet area `12 p` and total Seifert Betti count `12` satisfy `(12 p) * p⁻¹ = 12`, and
     proves genus-affine counting uniqueness over `[CommRing R] [IsDomain R] [CharZero R]`.

2. **Section 2 — Constructive `[CommRing R]` / `Rˣ` Quantum-Integer Algebra, Chebyshev
   Factorizations, `SU(2)_q` Clebsch–Gordan Decomposition, and Bar-Parity:**
   - Defines `qBalU (q : Rˣ) : ℕ → R` division-free over any `[CommRing R]` via the balanced
     two-term recurrence, proves the exact telescoping law `(q - q⁻¹) [n]_q = qⁿ - q⁻ⁿ`, bar
     invariance `[n]_{q⁻¹} = [n]_q`, and classical specialization `[n]_1 = n`.
   - Proves the exact Chebyshev factorizations of `[2]_q, [4]_q, [6]_q, [8]_q` in `x = q + q⁻¹`,
     the nine-channel `SU(2)_q` Clebsch–Gordan expansion
     `[2]_q [4]_q [6]_q [8]_q = [17]_q + 3[15]_q + 5[13]_q + 7[11]_q + 8[9]_q + 8[7]_q + 7[5]_q + 5[3]_q + 2[1]_q`
     (`384 = 2 × 192` at `q = 1`), and the division-free bar-breaking law
     `twoEwTreeU q⁻¹ * q² = twoEwTreeU q`.

3. **Section 3 — Signed Bar-Odd Vertex Join (`-h²`), `(q+1)² ℏ_q²` Conversion, Constant Form-B
   Measure (`μ_L = μ₁`), and Cleared `SU(2)_L` One-Loop Anti-Screening (`6 b₀ = -19`):**
   - Composes `EmPhotonJoinRules.barOdd_eq` and `EmFormBLoopMeasure.formB_measure_const` with the
     ring identity `(q - q⁻¹)² = (q + 1)² (1 - q⁻¹)²` and proves `6 b₀(SU(2)_L) = -19 < 0` vs
     abelian `6 b₀ > 0` over ordered commutative rings without division.

4. **Section 4 — Constructive `[CommRing R]` Anomaly-Free Hypercharge & `sin²θ_W(0) = 3/8`:**
   - Proves over `[CommRing R] [IsDomain R] [CharZero R]` (with integer-cleared charges `Y = 6 y`)
     that the four perturbative anomaly equations factor as `-18 Y_Q (Y_u + 4 Y_Q) (Y_u - 2 Y_Q)`,
     and that existence of a neutral lepton forces `Y_Q² = 1` and the exact cleared Weinberg trace
     identity `8 * Tr((6 T₃)²) = 3 * Tr((6 Q)²)` (`576 = 576`, i.e. `sin²θ_W(0) = 3/8`).

5. **Section 5 — Ordered-Ring Strict Monotonicity, Uniqueness & Proton-Pinned `LawvereCut.Cut ℚ`
   Rational Interval Certificate (`width = 3 × 10⁻¹⁰`, `0.00114 ppb`):**
   - Proves strict monotonicity and root uniqueness of the cleared `N_v`-cubic
     `N³ - T N² + H N - cH` over any strict ordered commutative ring, and certifies on `ℚ`
     (strictly proton-pinned per owner ruling `2026-11-28`, zero `Real.sqrt`) that every root
     `N ≥ 200` lies inside `ewNvProtonCut = [2624181688191/10¹⁰, 2624181688194/10¹⁰]`.

6. **Section 6 — Minimal Single Physical Bridge Class (`MinimalElectroweakVevBridgeClass`):**
   -Collapses the 9-field `EwVevReducedHypotheses` / 6-field `EwVevHypotheses` hierarchy to a
     3-field irreducible physical kernel (`Nv_pos`, `duality_self_consistency`, `su2_vev_assembly`)
     whose topological (`g = 4`), `SU(2)_L` sign (`s = -1`), and tree (`k = 1`) slots are evaluated
     via proved functions, deriving `EwVevReducedHypotheses`, `EwVevHypotheses`, and
     `ElectroweakVevFixedPointClass` unconditionally, paired with a non-vacuous `def trivialModel`.

-- Ref: [leitner2026] QOU Standard Model electroweak VEV conditional discharge, bean qou-vhm1
-- Ref: [edge1978] Edge, Bring's curve, J. London Math. Soc. 1978
-/

set_option autoImplicit false

namespace QOU.StandardModel
namespace ElectroweakConditionalDischarge

open QOU.BringsSurface.BringMapChain (σ α numCycles_σ numCycles_α numCycles_σα
  bring_chi bring_genus bring_connected)
open QOU.RiemannSurface.CombinatorialMapEuler (numCycles)
open QOU.RiemannSurface.MapGenusNonneg (orbits)
open QOU.Core.LawvereCut (Cut Coev CutEvaluation)
open QOU.MassTheory.EmVertexPairScalarChain (HeckeGen)
open QOU.MassTheory.EmPhotonJoinRules (barOdd_eq)
open QOU.MassTheory.EmFormBLoopMeasure (formBCoeff formBGraph formB_measure_const)
open QOU.Archimedean.BringSchwingerNormalizationDerivation
  (habiroNorm habiroNorm_eq_ewHabiroNorm habiroNorm_eq_rational_mul_zeroModes)
open QOU.Archimedean.AlphaEmFormCConditionalContent (habiroNorm_pos)
open QOU.StandardModel.EwVevDecomposition
  (EwVevHypotheses ewVevHypotheses_imp_class ewShapeCubic_existsUnique_root
   ewFixedPointCubic_eq_shape)
open QOU.StandardModel.EwVevGaps
  (EwVevReducedHypotheses ewVevReduced_imp_hypotheses treeK treeK_one
   perCarrierZeroMode perCarrier_ew oneLoopB0 signRule signRule_su2)

/-! ## Section 1: Finite Regular-Map Discharge of Bring Genus `g = 4`, `χ = -6`, and `b₁ = 8` -/

section BringMapTopologyDischarge

/-- Combinatorial Euler characteristic `V - E + F` of Bring's `{5,4}` regular map on `S₅` darts. -/
noncomputable def bringMapEuler : ℤ :=
  (numCycles σ : ℤ) - numCycles α + numCycles (σ * α)

/-- **Unconditional finite-map Euler theorem:** `bringMapEuler = 30 - 60 + 24 = -6` and the map
has a single connected dart orbit (`orbits σ α = 1`). -/
theorem bringMap_connected_and_euler :
    orbits σ α = 1 ∧
    numCycles σ = 30 ∧ numCycles α = 60 ∧ numCycles (σ * α) = 24 ∧
    bringMapEuler = -6 :=
  ⟨bring_connected, numCycles_σ, numCycles_α, numCycles_σα, bring_chi⟩

/-- **Unique genus `g = 4` forced by `BringMapChain`:** `χ = 2 - 2g` holds if and only if `g = 4`. -/
theorem bringMap_genus_eq_four_iff (g : ℤ) :
    bringMapEuler = 2 - 2 * g ↔ g = 4 := by
  rw [bringMap_connected_and_euler.2.2.2.2]
  omega

/-- First Betti number `b₁ = 2 - χ` read directly off the finite `S₅` regular map. -/
noncomputable def bringMapBettiOne : ℤ := 2 - bringMapEuler

/-- **Unconditional Betti theorem:** `bringMapBettiOne = 8` and the derived genus `(2 - χ) / 2` is `4`. -/
theorem bringMapBettiOne_eq_eight_and_genus_four :
    bringMapBettiOne = 8 ∧ bringMapBettiOne / 2 = 4 := by
  unfold bringMapBettiOne
  rw [bringMap_connected_and_euler.2.2.2.2]
  norm_num

/-- Seifert genus `k - 1` of the 2-component even-twist torus link `T(2, 2k)`. -/
def ewTorusLinkGenus (k : ℕ) : ℕ := k - 1

/-- Total Seifert genus `g_W + g_Z + g_H = 1 + 2 + 3` of `{T(2,4), T(2,6), T(2,8)}`. -/
def ewSeifertSum : ℕ :=
  ewTorusLinkGenus 2 + ewTorusLinkGenus 3 + ewTorusLinkGenus 4

/-- **Topological matching with the finite Bring map:** `ewSeifertSum = 6 = -bringMapEuler`. -/
theorem ewSeifertSum_eq_neg_bringMapEuler :
    ewSeifertSum = 6 ∧ (ewSeifertSum : ℤ) = -bringMapEuler := by
  have hs : ewSeifertSum = 6 := rfl
  refine ⟨hs, ?_⟩
  rw [hs, bringMap_connected_and_euler.2.2.2.2]
  norm_num

/-- Hyperbolic Gauss–Bonnet area coefficient `4(g - 1)` (multiplying the triangle-defect period `p`). -/
def bringAreaCoeff (g : ℤ) : ℤ := 4 * (g - 1)

/-- Over any commutative ring `R` with invertible period symbol `p : Rˣ`, the Bring Gauss–Bonnet
area `12 p` at `g = bringMapBettiOne / 2 = 4` times the electroweak zero-mode `p⁻¹` equals the
total Seifert first-Betti count `2 * ewSeifertSum = 12`, and `b₁ * H = (q + q⁻¹) * Z_EW`. -/
theorem ew_zero_mode_and_habiro_period_cancellation {R : Type*} [CommRing R] (q p : Rˣ) :
    ((bringAreaCoeff (bringMapBettiOne / 2) : ℤ) : R) * (p : R) * (↑p⁻¹ : R) =
      2 * (ewSeifertSum : R) ∧
    (((q : R) + (↑q⁻¹ : R)) * (↑p⁻¹ : R)) * (p : R) = (q : R) + (↑q⁻¹ : R) := by
  have hp : (p : R) * (↑p⁻¹ : R) = 1 := p.val_inv
  have hpi : (↑p⁻¹ : R) * (p : R) = 1 := p.inv_val
  rw [bringMapBettiOne_eq_eight_and_genus_four.2, ewSeifertSum_eq_neg_bringMapEuler.1]
  unfold bringAreaCoeff
  push_cast
  refine ⟨?_, ?_⟩
  · linear_combination 12 * hp
  · linear_combination ((q : R) + (↑q⁻¹ : R)) * hpi

/-- **Domain-level uniqueness of the per-carrier zero-mode rule (`§7c` upgrade of `genusAffine_unique`):**
Over any integral domain of characteristic zero (zero `[Field]` requirement), an affine carrier-genus
rule `a * g_i + b` sums to `8` on the two genus-4 EM carriers and `12` on the genus-`(1,2,3)` EW
carriers if and only if `a = 0` and `b = 4 = g(Bring)`. -/
theorem ew_em_genusAffine_unique_domain {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    (a b : R) :
    ((a * 4 + b) + (a * 4 + b) = 8 ∧
      (a * 1 + b) + (a * 2 + b) + (a * 3 + b) = 12) ↔
    a = 0 ∧ b = 4 := by
  constructor
  · rintro ⟨hem, hew⟩
    have h12 : (12 : R) * a = 0 := by linear_combination 3 * hem - 2 * hew
    have ha : a = 0 := by
      rcases mul_eq_zero.mp h12 with h0 | ha
      · exact absurd h0 (by norm_num)
      · exact ha
    refine ⟨ha, ?_⟩
    have h2 : (2 : R) * (b - 4) = 0 := by rw [ha] at hem; linear_combination hem
    rcases mul_eq_zero.mp h2 with h0 | hb
    · exact absurd h0 (by norm_num)
    · linear_combination hb
  · rintro ⟨rfl, rfl⟩
    constructor <;> ring

end BringMapTopologyDischarge

/-! ## Section 2: Constructive `[CommRing R]` / `Rˣ` Quantum Integers & Clebsch–Gordan Algebra -/

section ConstructiveQuantumIntegerTree

/-- Univariate Chebyshev polynomial sequence `U_{n-1}(x/2)` over any commutative ring `R`:
`chebB x 0 = 0`, `chebB x 1 = 1`, `chebB x (n + 2) = x * chebB x (n + 1) - chebB x n`. -/
def chebB {R : Type*} [CommRing R] (x : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | n + 2 => x * chebB x (n + 1) - chebB x n

/-- Division-free balanced quantum integer `[n]_q` over any `[CommRing R]` for a unit `q : Rˣ`,
defined as `chebB (q + q⁻¹) n`. -/
def qBalU {R : Type*} [CommRing R] (q : Rˣ) (n : ℕ) : R :=
  chebB ((q : R) + (↑q⁻¹ : R)) n

private lemma qBalU_telescoping_pair {R : Type*} [CommRing R] (q : Rˣ) (n : ℕ) :
    (((q : R) - (↑q⁻¹ : R)) * qBalU q n = (q : R) ^ n - (↑q⁻¹ : R) ^ n) ∧
    (((q : R) - (↑q⁻¹ : R)) * qBalU q (n + 1) = (q : R) ^ (n + 1) - (↑q⁻¹ : R) ^ (n + 1)) := by
  induction n with
  | zero =>
    refine ⟨?_, ?_⟩ <;> simp [qBalU, chebB]
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    have hqi : (q : R) * (↑q⁻¹ : R) = 1 := q.val_inv
    calc
      ((q : R) - (↑q⁻¹ : R)) * qBalU q (m + 2)
          = ((q : R) + (↑q⁻¹ : R)) * (((q : R) - (↑q⁻¹ : R)) * qBalU q (m + 1))
              - ((q : R) - (↑q⁻¹ : R)) * qBalU q m := by
            simp only [qBalU, chebB]; ring
      _ = ((q : R) + (↑q⁻¹ : R)) * ((q : R) ^ (m + 1) - (↑q⁻¹ : R) ^ (m + 1))
              - ((q : R) ^ m - (↑q⁻¹ : R) ^ m) := by
            rw [ih.2, ih.1]
      _ = ((q : R) ^ (m + 2) - (↑q⁻¹ : R) ^ (m + 2))
              + ((q : R) * (↑q⁻¹ : R) - 1) * ((q : R) ^ m - (↑q⁻¹ : R) ^ m) := by
            ring
      _ = (q : R) ^ (m + 2) - (↑q⁻¹ : R) ^ (m + 2) := by
            rw [hqi]; ring

/-- **Exact telescoping identity over `[CommRing R]` (`0` division):**
`(q - q⁻¹) · [n]_q = qⁿ - q⁻ⁿ` for every unit `q : Rˣ` and `n : ℕ`. -/
theorem qBalU_telescoping {R : Type*} [CommRing R] (q : Rˣ) (n : ℕ) :
    ((q : R) - (↑q⁻¹ : R)) * qBalU q n = (q : R) ^ n - (↑q⁻¹ : R) ^ n :=
  (qBalU_telescoping_pair q n).1

/-- **Kazhdan–Lusztig bar invariance (`q ↦ q⁻¹`) over `[CommRing R]`:** `[n]_{q⁻¹} = [n]_q`. -/
theorem qBalU_bar {R : Type*} [CommRing R] (q : Rˣ) (n : ℕ) :
    qBalU q⁻¹ n = qBalU q n := by
  unfold qBalU
  rw [inv_inv, add_comm]

private lemma chebB_two_pair {R : Type*} [CommRing R] (n : ℕ) :
    chebB (2 : R) n = (n : R) ∧ chebB (2 : R) (n + 1) = ((n + 1 : ℕ) : R) := by
  induction n with
  | zero => simp [chebB]
  | succ m ih =>
    refine ⟨ih.2, ?_⟩
    simp only [chebB]
    rw [ih.2, ih.1]
    push_cast
    ring

/-- **Classical `q = 1` specialization over `[CommRing R]`:** `qBalU 1 n = n`. -/
theorem qBalU_one {R : Type*} [CommRing R] (n : ℕ) :
    qBalU (1 : Rˣ) n = (n : R) := by
  unfold qBalU
  have h1 : ((1 : Rˣ) : R) + (↑(1 : Rˣ)⁻¹ : R) = (2 : R) := by
    rw [inv_one]; push_cast; ring
  rw [h1]
  exact (chebB_two_pair n).1

/-- **Exact Chebyshev factorizations of the electroweak carrier factors `[2]_q, [4]_q, [6]_q, [8]_q`**
in `x = q + q⁻¹` over any commutative ring `R`. -/
theorem qBalU_ew_chebyshev_factors {R : Type*} [CommRing R] (q : Rˣ) :
    let x : R := (q : R) + (↑q⁻¹ : R)
    qBalU q 2 = x ∧
    qBalU q 4 = x * (x ^ 2 - 2) ∧
    qBalU q 6 = x * (x - 1) * (x + 1) * (x ^ 2 - 3) ∧
    qBalU q 8 = x * (x ^ 2 - 2) * (x ^ 4 - 4 * x ^ 2 + 2) := by
  intro x
  have u0 : chebB x 0 = 0 := rfl
  have u1 : chebB x 1 = 1 := rfl
  have u2 : chebB x 2 = x := by rw [chebB, u1, u0]; ring
  have u3 : chebB x 3 = x ^ 2 - 1 := by rw [chebB, u2, u1]; ring
  have u4 : chebB x 4 = x ^ 3 - 2 * x := by rw [chebB, u3, u2]; ring
  have u5 : chebB x 5 = x ^ 4 - 3 * x ^ 2 + 1 := by rw [chebB, u4, u3]; ring
  have u6 : chebB x 6 = x ^ 5 - 4 * x ^ 3 + 3 * x := by rw [chebB, u5, u4]; ring
  have u7 : chebB x 7 = x ^ 6 - 5 * x ^ 4 + 6 * x ^ 2 - 1 := by rw [chebB, u6, u5]; ring
  have u8 : chebB x 8 = x ^ 7 - 6 * x ^ 5 + 10 * x ^ 3 - 4 * x := by rw [chebB, u7, u6]; ring
  dsimp only [qBalU]
  rw [u2, u4, u6, u8]
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- **Nine-channel `SU(2)_q` Clebsch–Gordan expansion of `[2]_q [4]_q [6]_q [8]_q` over `[CommRing R]`:**
`V₁ ⊗ V₃ ⊗ V₅ ⊗ V₇ ≅ V₁₆ ⊕ 3 V₁₄ ⊕ 5 V₁₂ ⊕ 7 V₁₀ ⊕ 8 V₈ ⊕ 8 V₆ ⊕ 7 V₄ ⊕ 5 V₂ ⊕ 2 V₀`,
with classical dimension identity `2 · 4 · 6 · 8 = 384 = 2 · 192` at `q = 1`. -/
theorem ew_carrier_product_clebsch_gordan {R : Type*} [CommRing R] (q : Rˣ) :
    qBalU q 2 * qBalU q 4 * qBalU q 6 * qBalU q 8 =
      qBalU q 17 + 3 * qBalU q 15 + 5 * qBalU q 13 + 7 * qBalU q 11 +
      8 * qBalU q 9 + 8 * qBalU q 7 + 7 * qBalU q 5 + 5 * qBalU q 3 + 2 * qBalU q 1 := by
  set x : R := (q : R) + (↑q⁻¹ : R)
  have u0 : chebB x 0 = 0 := rfl
  have u1 : chebB x 1 = 1 := rfl
  have u2 : chebB x 2 = x := by rw [chebB, u1, u0]; ring
  have u3 : chebB x 3 = x ^ 2 - 1 := by rw [chebB, u2, u1]; ring
  have u4 : chebB x 4 = x ^ 3 - 2 * x := by rw [chebB, u3, u2]; ring
  have u5 : chebB x 5 = x ^ 4 - 3 * x ^ 2 + 1 := by rw [chebB, u4, u3]; ring
  have u6 : chebB x 6 = x ^ 5 - 4 * x ^ 3 + 3 * x := by rw [chebB, u5, u4]; ring
  have u7 : chebB x 7 = x ^ 6 - 5 * x ^ 4 + 6 * x ^ 2 - 1 := by rw [chebB, u6, u5]; ring
  have u8 : chebB x 8 = x ^ 7 - 6 * x ^ 5 + 10 * x ^ 3 - 4 * x := by rw [chebB, u7, u6]; ring
  have u9 : chebB x 9 = x ^ 8 - 7 * x ^ 6 + 15 * x ^ 4 - 10 * x ^ 2 + 1 := by
    rw [chebB, u8, u7]; ring
  have u10 : chebB x 10 = x ^ 9 - 8 * x ^ 7 + 21 * x ^ 5 - 20 * x ^ 3 + 5 * x := by
    rw [chebB, u9, u8]; ring
  have u11 : chebB x 11 = x ^ 10 - 9 * x ^ 8 + 28 * x ^ 6 - 35 * x ^ 4 + 15 * x ^ 2 - 1 := by
    rw [chebB, u10, u9]; ring
  have u12 : chebB x 12 = x ^ 11 - 10 * x ^ 9 + 36 * x ^ 7 - 56 * x ^ 5 + 35 * x ^ 3 - 6 * x := by
    rw [chebB, u11, u10]; ring
  have u13 : chebB x 13 =
      x ^ 12 - 11 * x ^ 10 + 45 * x ^ 8 - 84 * x ^ 6 + 70 * x ^ 4 - 21 * x ^ 2 + 1 := by
    rw [chebB, u12, u11]; ring
  have u14 : chebB x 14 =
      x ^ 13 - 12 * x ^ 11 + 55 * x ^ 9 - 120 * x ^ 7 + 126 * x ^ 5 - 56 * x ^ 3 + 7 * x := by
    rw [chebB, u13, u12]; ring
  have u15 : chebB x 15 =
      x ^ 14 - 13 * x ^ 12 + 66 * x ^ 10 - 165 * x ^ 8 + 210 * x ^ 6 - 126 * x ^ 4 +
        28 * x ^ 2 - 1 := by
    rw [chebB, u14, u13]; ring
  have u16 : chebB x 16 =
      x ^ 15 - 14 * x ^ 13 + 78 * x ^ 11 - 220 * x ^ 9 + 330 * x ^ 7 - 252 * x ^ 5 +
        84 * x ^ 3 - 8 * x := by
    rw [chebB, u15, u14]; ring
  have u17 : chebB x 17 =
      x ^ 16 - 15 * x ^ 14 + 91 * x ^ 12 - 286 * x ^ 10 + 495 * x ^ 8 - 462 * x ^ 6 +
        210 * x ^ 4 - 36 * x ^ 2 + 1 := by
    rw [chebB, u16, u15]; ring
  change chebB x 2 * chebB x 4 * chebB x 6 * chebB x 8 =
    chebB x 17 + 3 * chebB x 15 + 5 * chebB x 13 + 7 * chebB x 11 +
    8 * chebB x 9 + 8 * chebB x 7 + 7 * chebB x 5 + 5 * chebB x 3 + 2 * chebB x 1
  rw [u1, u2, u3, u4, u5, u6, u7, u8, u9, u11, u13, u15, u17]
  ring

/-- Doubled electroweak dressed tree complexity `2 N_v^tree(q) = q [2]_q [4]_q [6]_q [8]_q`
defined division-free over any commutative ring `R`. -/
def twoEwTreeU {R : Type*} [CommRing R] (q : Rˣ) : R :=
  (q : R) * qBalU q 2 * qBalU q 4 * qBalU q 6 * qBalU q 8

/-- **Division-free bar-breaking law (`§7c` upgrade of `ElectroweakVevGaps.ewTreeF_bar`):**
`twoEwTreeU q⁻¹ * q² = twoEwTreeU q` over every commutative ring `R`, with `twoEwTreeU 1 = 384`. -/
theorem twoEwTreeU_bar_and_classical {R : Type*} [CommRing R] (q : Rˣ) :
    twoEwTreeU q⁻¹ * (q : R) ^ 2 = twoEwTreeU q ∧ twoEwTreeU (1 : Rˣ) = 384 := by
  refine ⟨?_, ?_⟩
  · unfold twoEwTreeU
    rw [qBalU_bar, qBalU_bar, qBalU_bar, qBalU_bar]
    have hqi : (↑q⁻¹ : R) * (q : R) = 1 := q.inv_val
    linear_combination ((q : R) * qBalU q 2 * qBalU q 4 * qBalU q 6 * qBalU q 8) * hqi
  · unfold twoEwTreeU
    rw [qBalU_one, qBalU_one, qBalU_one, qBalU_one]
    push_cast
    norm_num

end ConstructiveQuantumIntegerTree

/-! ## Section 3: Bar-Odd Vertex Join `-h²`, `(q+1)² ℏ_q²`, Form-B Measure, & `SU(2)_L` `6 b₀ = -19` -/

section LoopJoinMeasureAndBetaSign

/-- **Division-free skein-to-Habiro square bridge (`(q - q⁻¹)² = (q + 1)² (1 - q⁻¹)²`)** over
any `[CommRing R]` with unit `q : Rˣ`, together with position-blind bar-odd 2-vertex contraction
(`EmPhotonJoinRules.barOdd_eq`) and constant all-loop measure (`EmFormBLoopMeasure.formB_measure_const`). -/
theorem barOdd_join_habiro_bridge_and_const_measure
    {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (q : Rˣ) (g g' : HeckeGen (A := A) ((q : R) - (↑q⁻¹ : R)))
    (μ₁ : R) (μ : ℕ → R)
    (hcan : ∀ L, IsLeftRegular (formBGraph (qBalU q 2) ((q : R) - (↑q⁻¹ : R)) L))
    (hc : ∀ L,
      formBGraph (qBalU q 2) ((q : R) - (↑q⁻¹ : R)) L * μ L =
        formBCoeff (qBalU q 2) ((q : R) - (↑q⁻¹ : R)) μ₁ L) :
    ((q : R) - (↑q⁻¹ : R)) ^ 2 = ((q : R) + 1) ^ 2 * (1 - (↑q⁻¹ : R)) ^ 2 ∧
    -((g.σ - g.σinv) * (g'.σ - g'.σinv)) =
      algebraMap R A (-(((q : R) - (↑q⁻¹ : R)) ^ 2)) ∧
    (∀ L, μ L = μ₁) := by
  have hlin : (q : R) - (↑q⁻¹ : R) = ((q : R) + 1) * (1 - (↑q⁻¹ : R)) := by
    linear_combination q.val_inv
  refine ⟨by rw [hlin]; ring, barOdd_eq g g', formB_measure_const _ _ μ₁ μ hcan hc⟩

/-- Denominator-cleared one-loop gauge beta coefficient `6 b₀ = -22 C_A + 2 (2 Σ T_Weyl) + (2 Σ T_scalar)`
over any commutative ring `R` (`CA = 2`, `twoWeylT = 12`, `twoScalarT = 1` for SM `SU(2)_L`). -/
def sixOneLoopB0 {R : Type*} [CommRing R] (CA twoWeylT twoScalarT : R) : R :=
  -22 * CA + 2 * twoWeylT + twoScalarT

/-- **Cleared `SU(2)_L` anti-screening vs abelian screening over ordered commutative rings:**
`6 b₀(SU(2)_L) = -19 < 0` (forcing loop sign `s = -1`), whereas any abelian sector (`C_A = 0`)
with `0 < twoWeylT` and `0 ≤ twoScalarT` has `0 < 6 b₀` (forcing `s = +1`). -/
theorem sixOneLoopB0_su2_neg_and_abelian_pos
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (twoWeylT twoScalarT : K) (hw : 0 < twoWeylT) (hs : 0 ≤ twoScalarT) :
    sixOneLoopB0 (2 : K) 12 1 = -19 ∧
    sixOneLoopB0 (2 : K) 12 1 < 0 ∧
    0 < sixOneLoopB0 (0 : K) twoWeylT twoScalarT := by
  have hsu2 : sixOneLoopB0 (2 : K) 12 1 = -19 := by unfold sixOneLoopB0; ring
  refine ⟨hsu2, ?_, ?_⟩
  · rw [hsu2]; norm_num
  · unfold sixOneLoopB0; linarith

end LoopJoinMeasureAndBetaSign

/-! ## Section 4: Constructive `[CommRing R]` Anomaly-Free Hypercharge & `sin²θ_W(0) = 3/8` -/

section ConstructiveAnomalyWeinberg

/-- Five integer-scaled hypercharges `Y = 6 y` on one generation of `SU(3) × SU(2)` Weyl states
over a commutative ring `R`, eliminating all fractional denominators. -/
structure ClearedCharges (R : Type*) where
  /-- Scaled quark-doublet charge `Y_Q = 6 y_Q` (`= ±1` on SM). -/
  YQ : R
  /-- Scaled up-singlet charge `Y_u = 6 y_u` (`= ∓4` on SM). -/
  Yu : R
  /-- Scaled down-singlet charge `Y_d = 6 y_d` (`= ±2` on SM). -/
  Yd : R
  /-- Scaled lepton-doublet charge `Y_L = 6 y_L` (`= ∓3` on SM). -/
  YL : R
  /-- Scaled charged-lepton-singlet charge `Y_e = 6 y_e` (`= ±6` on SM). -/
  Ye : R

/-- Four cleared perturbative anomaly polynomials (`[SU(3)]²U(1)`, `[SU(2)]²U(1)`, `[grav]²U(1)`, `U(1)³`). -/
def ClearedAnomalyFree {R : Type*} [CommRing R] (c : ClearedCharges R) : Prop :=
  2 * c.YQ + c.Yu + c.Yd = 0 ∧
  3 * c.YQ + c.YL = 0 ∧
  6 * c.YQ + 3 * c.Yu + 3 * c.Yd + 2 * c.YL + c.Ye = 0 ∧
  6 * c.YQ ^ 3 + 3 * c.Yu ^ 3 + 3 * c.Yd ^ 3 + 2 * c.YL ^ 3 + c.Ye ^ 3 = 0

/-- Chiral hypercharge ratio family over `[CommRing R]`. -/
def IsClearedChiral {R : Type*} [CommRing R] (c : ClearedCharges R) : Prop :=
  c.YL = -3 * c.YQ ∧ c.Ye = 6 * c.YQ ∧
    ((c.Yu = -4 * c.YQ ∧ c.Yd = 2 * c.YQ) ∨ (c.Yu = 2 * c.YQ ∧ c.Yd = -4 * c.YQ))

/-- Cleared neutral-lepton condition: one member of the `L` doublet (`6 T₃ = ±3`) has `6 Q = 0`. -/
def HasClearedNeutralLepton {R : Type*} [CommRing R] (c : ClearedCharges R) : Prop :=
  3 + c.YL = 0 ∨ -3 + c.YL = 0

/-- Sum of `(6 T₃)²` across the 15 Weyl states of one generation: `6(9+9) + 2(9+9)`?
Each doublet member has `2 T₃ = ±1`, so `6 T₃ = ±3` and `(6 T₃)² = 9` across the `6 + 2 = 8`
doublet states (`8 × 9 = 72`), matching `36 * Tr(T₃²) = 36 * 2 = 72`. -/
def clearedTraceSixT3Sq {R : Type*} [CommRing R] : R :=
  6 * (3 : R) ^ 2 + 2 * (3 : R) ^ 2

/-- Sum of `(6 Q)² = (6 T₃ + Y)²` across the 15 Weyl states (`Tr(T₃ Y) = 0` on doublets):
`72 + (6 Y_Q² + 3 Y_u² + 3 Y_d² + 2 Y_L² + Y_e²)`. -/
def clearedTraceSixChargeSq {R : Type*} [CommRing R] (c : ClearedCharges R) : R :=
  clearedTraceSixT3Sq +
    (6 * c.YQ ^ 2 + 3 * c.Yu ^ 2 + 3 * c.Yd ^ 2 + 2 * c.YL ^ 2 + c.Ye ^ 2)

/-- **Domain-level anomaly-freedom & `sin²θ_W(0) = 3/8` uniqueness (`0` `[Field]`, `0` `field_simp`):**
Over any integral domain `R` of characteristic zero, `ClearedAnomalyFree c` together with
`HasClearedNeutralLepton c` forces `IsClearedChiral c`, `c.YQ ^ 2 = 1` (`y_Q = ±1/6`), and the
exact cleared Weinberg trace identity `8 * clearedTraceSixT3Sq = 3 * clearedTraceSixChargeSq c`
(`8 × 72 = 3 × 192 = 576`, i.e. `sin²θ_W(0) = Tr(T₃²) / Tr(Q²) = 3 / 8`). -/
theorem cleared_anomalyFree_neutral_forces_three_eighths
    {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    (c : ClearedCharges R) (ha : ClearedAnomalyFree c) (hn : HasClearedNeutralLepton c) :
    IsClearedChiral c ∧
    c.YQ ^ 2 = 1 ∧
    8 * (clearedTraceSixT3Sq : R) = 3 * clearedTraceSixChargeSq c := by
  rcases ha with ⟨h3, h2, hg, hc⟩
  have hL : c.YL = -3 * c.YQ := by linear_combination h2
  have hd : c.Yd = -2 * c.YQ - c.Yu := by linear_combination h3
  have he : c.Ye = 6 * c.YQ := by linear_combination hg - 3 * h3 - 2 * h2
  have hfac : -18 * c.YQ * (c.Yu + 4 * c.YQ) * (c.Yu - 2 * c.YQ) = 0 := by
    have hcub :
        6 * c.YQ ^ 3 + 3 * c.Yu ^ 3 + 3 * c.Yd ^ 3 + 2 * c.YL ^ 3 + c.Ye ^ 3 =
          -18 * c.YQ * (c.Yu + 4 * c.YQ) * (c.Yu - 2 * c.YQ) := by
      rw [hL, hd, he]; ring
    rw [← hcub]; exact hc
  have hYQ_sq : c.YQ ^ 2 = 1 := by
    rcases hn with hn1 | hn2
    · rw [hL] at hn1
      have h3q : (3 : R) * (1 - c.YQ) = 0 := by linear_combination hn1
      rcases mul_eq_zero.mp h3q with h0 | hq1
      · exact absurd h0 (by norm_num)
      · have hq : c.YQ = 1 := by linear_combination -hq1
        rw [hq]; ring
    · rw [hL] at hn2
      have h3q : (3 : R) * (1 + c.YQ) = 0 := by linear_combination -hn2
      rcases mul_eq_zero.mp h3q with h0 | hq1
      · exact absurd h0 (by norm_num)
      · have hq : c.YQ = -1 := by linear_combination hq1
        rw [hq]; ring
  have hYQ_ne : c.YQ ≠ 0 := by
    intro h0
    rw [h0] at hYQ_sq
    norm_num at hYQ_sq
  have h18_ne : (-18 : R) ≠ 0 := by norm_num
  have hprod : (c.Yu + 4 * c.YQ) * (c.Yu - 2 * c.YQ) = 0 := by
    have h' : (-18 * c.YQ) * ((c.Yu + 4 * c.YQ) * (c.Yu - 2 * c.YQ)) = 0 := by
      linear_combination hfac
    rcases mul_eq_zero.mp h' with hleft | hright
    · exact absurd hleft (mul_ne_zero h18_ne hYQ_ne)
    · exact hright
  have hch : IsClearedChiral c := by
    rcases mul_eq_zero.mp hprod with hu1 | hu2
    · refine ⟨hL, he, Or.inl ⟨by linear_combination hu1, by linear_combination hd - hu1⟩⟩
    · refine ⟨hL, he, Or.inr ⟨by linear_combination hu2, by linear_combination hd - hu2⟩⟩
  refine ⟨hch, hYQ_sq, ?_⟩
  unfold clearedTraceSixChargeSq clearedTraceSixT3Sq
  rcases hch with ⟨_, _, ⟨hu, hd'⟩ | ⟨hu, hd'⟩⟩ <;>
    · rw [hL, he, hu, hd']
      have htr :
          6 * c.YQ ^ 2 + 3 * (-4 * c.YQ) ^ 2 + 3 * (2 * c.YQ) ^ 2 +
            2 * (-3 * c.YQ) ^ 2 + (6 * c.YQ) ^ 2 = 120 * c.YQ ^ 2 := by ring
      have htr' :
          6 * c.YQ ^ 2 + 3 * (2 * c.YQ) ^ 2 + 3 * (-4 * c.YQ) ^ 2 +
            2 * (-3 * c.YQ) ^ 2 + (6 * c.YQ) ^ 2 = 120 * c.YQ ^ 2 := by ring
      first
      | (rw [htr, hYQ_sq]; norm_num)
      | (rw [htr', hYQ_sq]; norm_num)

end ConstructiveAnomalyWeinberg

/-! ## Section 5: Ordered-Ring Monotonicity & Proton-Pinned `LawvereCut.Cut ℚ` Certificate -/

section OrderedRingAndProtonCut

/-- Denominator-cleared weak-scale fixed-point cubic in `N = N_v = 1 / α_v`:
`ewClearedVevCubic T H cH N = N³ - T N² + H N - cH` (`cH = ℏ_q² H`). -/
def ewClearedVevCubic {K : Type*} [CommRing K] (T H cH N : K) : K :=
  N ^ 3 - T * N ^ 2 + H * N - cH

/-- **Strict monotonicity above `B` over any strict ordered commutative ring (`0` `[Field]`):**
Whenever `0 ≤ B`, `0 ≤ H`, and `4 * T ≤ 6 * B` (e.g. `B = 200`, `T ≤ 300`),
`ewClearedVevCubic T H cH` is strictly increasing on `{N : K | B ≤ N}`. -/
theorem ewClearedVevCubic_strictMono_above
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {T H cH B : K} (hB : 0 ≤ B) (hH : 0 ≤ H) (hTB : 4 * T ≤ 6 * B)
    {N₁ N₂ : K} (hN1 : B ≤ N₁) (hlt : N₁ < N₂) :
    ewClearedVevCubic T H cH N₁ < ewClearedVevCubic T H cH N₂ := by
  have hdiff :
      ewClearedVevCubic T H cH N₂ - ewClearedVevCubic T H cH N₁ =
        (N₂ - N₁) * (N₂ ^ 2 + N₁ * N₂ + N₁ ^ 2 - T * (N₂ + N₁) + H) := by
    unfold ewClearedVevCubic; ring
  have hsub_pos : 0 < N₂ - N₁ := sub_pos.mpr hlt
  have hsum_nonneg : 0 ≤ N₂ + N₁ := by linarith
  have h3sum : 0 ≤ 3 * (N₂ + N₁) - 4 * T := by linarith
  have h4quad : 0 < 4 * (N₂ ^ 2 + N₁ * N₂ + N₁ ^ 2 - T * (N₂ + N₁)) := by
    have hid :
        4 * (N₂ ^ 2 + N₁ * N₂ + N₁ ^ 2 - T * (N₂ + N₁)) =
          (N₂ - N₁) ^ 2 + (N₂ + N₁) * (3 * (N₂ + N₁) - 4 * T) := by ring
    rw [hid]
    have hsq : 0 < (N₂ - N₁) ^ 2 := sq_pos_of_pos hsub_pos
    have hmul : 0 ≤ (N₂ + N₁) * (3 * (N₂ + N₁) - 4 * T) := mul_nonneg hsum_nonneg h3sum
    linarith
  have hquad : 0 < N₂ ^ 2 + N₁ * N₂ + N₁ ^ 2 - T * (N₂ + N₁) + H := by linarith
  have hprod : 0 < (N₂ - N₁) * (N₂ ^ 2 + N₁ * N₂ + N₁ ^ 2 - T * (N₂ + N₁) + H) :=
    mul_pos hsub_pos hquad
  linarith

/-- **Root uniqueness & sign-change bracketing over any strict ordered commutative ring:**
Under `0 ≤ B`, `0 ≤ H`, `4 * T ≤ 6 * B`, any two roots `≥ B` coincide, and if
`ewClearedVevCubic T H cH lo < 0 < ewClearedVevCubic T H cH hi` with `B ≤ lo` and `B ≤ hi`,
every root `N ≥ B` satisfies `lo < N ∧ N < hi`. -/
theorem ewClearedVevCubic_unique_and_bracket
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {T H cH B lo hi : K} (hB : 0 ≤ B) (hH : 0 ≤ H) (hTB : 4 * T ≤ 6 * B)
    (hloB : B ≤ lo) (hhiB : B ≤ hi)
    (hlo : ewClearedVevCubic T H cH lo < 0)
    (hhi : 0 < ewClearedVevCubic T H cH hi) :
    (∀ N₁ N₂ : K, B ≤ N₁ → B ≤ N₂ →
      ewClearedVevCubic T H cH N₁ = 0 → ewClearedVevCubic T H cH N₂ = 0 → N₁ = N₂) ∧
    (∀ N : K, B ≤ N → ewClearedVevCubic T H cH N = 0 → lo < N ∧ N < hi) := by
  refine ⟨?_, ?_⟩
  · intro N₁ N₂ h1 h2 hr1 hr2
    rcases lt_trichotomy N₁ N₂ with hlt | heq | hgt
    · have hm := ewClearedVevCubic_strictMono_above (cH := cH) hB hH hTB h1 hlt
      linarith
    · exact heq
    · have hm := ewClearedVevCubic_strictMono_above (cH := cH) hB hH hTB h2 hgt
      linarith
  · intro N hN hr
    refine ⟨?_, ?_⟩
    · by_contra hle
      push_neg at hle
      rcases lt_or_eq_of_le hle with hlt | rfl
      · have hm := ewClearedVevCubic_strictMono_above (cH := cH) hB hH hTB hN hlt
        linarith
      · linarith
    · by_contra hge
      push_neg at hge
      rcases lt_or_eq_of_le hge with hlt | rfl
      · have hm := ewClearedVevCubic_strictMono_above (cH := cH) hB hH hTB hhiB hlt
        linarith
      · linarith

/-- Lower endpoint of the proton-pinned `LawvereCut.Cut ℚ` interval for `N_v(q₀)`
(`2624181688191 / 10¹⁰`, strictly proton-pinned per owner ruling `2026-11-28`). -/
def ewNvProtonLo : ℚ := 2624181688191 / 10000000000

/-- Upper endpoint of the proton-pinned `LawvereCut.Cut ℚ` interval for `N_v(q₀)`
(`2624181688194 / 10¹⁰`, width `3 × 10⁻¹⁰`, relative width `0.00114 ppb`). -/
def ewNvProtonHi : ℚ := 2624181688194 / 10000000000

/-- Constructive `LawvereCut.Cut ℚ` observable bracketing proton-pinned `N_v(q₀)` via `Cut.ev`. -/
def ewNvProtonCut : Cut ℚ :=
  Cut.ofInterval ewNvProtonLo ewNvProtonHi (by unfold ewNvProtonLo ewNvProtonHi; norm_num)

/-- **Proton-pinned `LawvereCut` interval certificate (`0` `Real.sqrt`, `0` `field_simp`):**
1. `ewNvProtonCut` has certified resolution `3 / 10¹⁰` (`Cut.WithinResolution`, via `ev` alone);
2. For every `(T, H, cH : ℚ)` in the certified proton-pin enclosure
   `T ∈ [262418473706849/10¹², 262418473706851/10¹²]`,
   `H ∈ [312543141/3906250000, 80011044097/10¹²]`,
   `cH ∈ [392741669/5×10¹¹, 785483339/10¹²]`,
   `ewClearedVevCubic T H cH ewNvProtonLo < 0 < ewClearedVevCubic T H cH ewNvProtonHi` and every
   root `N ≥ 200` lies strictly inside `ewNvProtonCut` (`ewNvProtonCut.Contains N`);
3. Under `[Coev E]`, any observable whose cut contains `x` and `y` pins `x = y` uniquely. -/
theorem ewNvProton_cut_certified :
    ewNvProtonCut.WithinResolution (3 / 10000000000) ∧
    (∀ T H cH : ℚ,
      262418473706849 / 1000000000000 ≤ T → T ≤ 262418473706851 / 1000000000000 →
      312543141 / 3906250000 ≤ H → H ≤ 80011044097 / 1000000000000 →
      392741669 / 500000000000 ≤ cH → cH ≤ 785483339 / 1000000000000 →
      ewClearedVevCubic T H cH ewNvProtonLo < 0 ∧
      0 < ewClearedVevCubic T H cH ewNvProtonHi ∧
      ∀ N : ℚ, 200 ≤ N → ewClearedVevCubic T H cH N = 0 → ewNvProtonCut.Contains N) ∧
    (∀ {R : Type*} (E : CutEvaluation R ℚ) [Coev E] (r : R) (x y : ℚ),
      (E.cut r).Contains x → (E.cut r).Contains y → x = y) := by
  refine ⟨?_, ?_, fun E _ r x y hx hy => Coev.unique_value E r hx hy⟩
  · have hres :=
      Cut.ofInterval_withinResolution ewNvProtonLo ewNvProtonHi
        (by unfold ewNvProtonLo ewNvProtonHi; norm_num)
    have hwidth : ewNvProtonHi - ewNvProtonLo ≤ 3 / 10000000000 := by
      unfold ewNvProtonLo ewNvProtonHi; norm_num
    exact hres.mono hwidth
  · intro T H cH hTlo hThi hHlo hHhi hcHlo hcHhi
    have hlo_bound :
        ewClearedVevCubic (262418473706849 / 1000000000000) (80011044097 / 1000000000000)
          (392741669 / 500000000000) ewNvProtonLo < 0 := by
      unfold ewClearedVevCubic ewNvProtonLo; norm_num
    have hhi_bound :
        0 < ewClearedVevCubic (262418473706851 / 1000000000000) (312543141 / 3906250000)
          (785483339 / 1000000000000) ewNvProtonHi := by
      unfold ewClearedVevCubic ewNvProtonHi; norm_num
    have hlo_sq : 0 ≤ ewNvProtonLo ^ 2 := sq_nonneg _
    have hlo_pos : 0 ≤ ewNvProtonLo := by unfold ewNvProtonLo; norm_num
    have hhi_sq : 0 ≤ ewNvProtonHi ^ 2 := sq_nonneg _
    have hhi_pos : 0 ≤ ewNvProtonHi := by unfold ewNvProtonHi; norm_num
    have hlo_le :
        ewClearedVevCubic T H cH ewNvProtonLo ≤
          ewClearedVevCubic (262418473706849 / 1000000000000) (80011044097 / 1000000000000)
            (392741669 / 500000000000) ewNvProtonLo := by
      unfold ewClearedVevCubic
      have ht : (262418473706849 / 1000000000000) * ewNvProtonLo ^ 2 ≤ T * ewNvProtonLo ^ 2 :=
        mul_le_mul_of_nonneg_right hTlo hlo_sq
      have hh : H * ewNvProtonLo ≤ (80011044097 / 1000000000000) * ewNvProtonLo :=
        mul_le_mul_of_nonneg_right hHhi hlo_pos
      linarith
    have hhi_ge :
        ewClearedVevCubic (262418473706851 / 1000000000000) (312543141 / 3906250000)
            (785483339 / 1000000000000) ewNvProtonHi ≤
          ewClearedVevCubic T H cH ewNvProtonHi := by
      unfold ewClearedVevCubic
      have ht : T * ewNvProtonHi ^ 2 ≤ (262418473706851 / 1000000000000) * ewNvProtonHi ^ 2 :=
        mul_le_mul_of_nonneg_right hThi hhi_sq
      have hh : (312543141 / 3906250000) * ewNvProtonHi ≤ H * ewNvProtonHi :=
        mul_le_mul_of_nonneg_right hHlo hhi_pos
      linarith
    have hlo_neg : ewClearedVevCubic T H cH ewNvProtonLo < 0 := lt_of_le_of_lt hlo_le hlo_bound
    have hhi_pos_val : 0 < ewClearedVevCubic T H cH ewNvProtonHi := lt_of_lt_of_le hhi_bound hhi_ge
    refine ⟨hlo_neg, hhi_pos_val, ?_⟩
    intro N hN hr
    have hH0 : (0 : ℚ) ≤ H := by linarith
    have hTB : 4 * T ≤ 6 * (200 : ℚ) := by linarith
    have hbr :=
      (ewClearedVevCubic_unique_and_bracket (B := (200 : ℚ)) (by norm_num) hH0 hTB
        (by unfold ewNvProtonLo; norm_num) (by unfold ewNvProtonHi; norm_num)
        hlo_neg hhi_pos_val).2 N hN hr
    exact ⟨fun a ha => le_trans ha (le_of_lt hbr.1), fun b hb => le_trans (le_of_lt hbr.2) hb⟩

end OrderedRingAndProtonCut

/-! ## Section 6: Minimal Irreducible Physical Bridge Class (`MinimalElectroweakVevBridgeClass`) -/

section MinimalBridgeReduction

/-- **Irreducible physical bridge hypothesis (`§3b-cond`, zero global instances):**
After discharging Bring genus `g = bringMapBettiOne / 2 = 4` (`BringMapChain`), the `SU(2)_L`
anti-screening sign `signRule (oneLoopB0 2 6 (1/2)) = -1`, and cubic root existence/uniqueness,
the entire `EwVevReducedHypotheses` / `EwVevHypotheses` / `ElectroweakVevFixedPointClass` tower
reduces to this 3-field physical self-consistency kernel (`qou-rpt1` / `qou-myxi`). -/
class MinimalElectroweakVevBridgeClass (q Nv α_v : ℝ) : Prop where
  /-- Crossing count `N_v = v / m_p` is strictly positive. -/
  Nv_pos : 0 < Nv
  /-- Loop-coupling self-consistency `α_v · N_v = 1`. -/
  duality_self_consistency : α_v * Nv = 1
  /-- `SU(2)_L` anti-screened `k = 1` dressed-tree + Bring-map zero-mode self-consistency assembly. -/
  su2_vev_assembly :
    Nv =
      treeK q 1 +
      perCarrierZeroMode 3 ((bringMapBettiOne / 2 : ℤ) : ℝ) +
      signRule (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)) *
        α_v * ewHabiroNorm q * (1 - (ewHbarQ q) ^ 2 * α_v)

/-- **Master Conditional Reduction Theorem (`MinimalElectroweakVevBridgeClass` ⇒ all 3 EW classes):**
Under `[MinimalElectroweakVevBridgeClass q Nv α_v]`, `EwVevReducedHypotheses`, `EwVevHypotheses`,
`ElectroweakVevFixedPointClass q α_v`, and `ewFixedPointCubic q α_v = 0` all follow unconditionally
without `sorry`. -/
theorem minimalEwBridge_discharges_legacy_classes (q Nv α_v : ℝ)
    [inst : MinimalElectroweakVevBridgeClass q Nv α_v] :
    EwVevReducedHypotheses
      q Nv (treeK q 1) (perCarrierZeroMode 3 4)
      (signRule (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)))
      ((ewHbarQ q) ^ 2) α_v (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)) 1 ∧
    EwVevHypotheses
      q Nv (treeK q 1) (perCarrierZeroMode 3 4)
      (signRule (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)))
      ((ewHbarQ q) ^ 2) α_v ∧
    ElectroweakVevFixedPointClass q α_v ∧
    ewFixedPointCubic q α_v = 0 := by
  have hg4 : ((bringMapBettiOne / 2 : ℤ) : ℝ) = 4 := by
    rw [bringMapBettiOne_eq_eight_and_genus_four.2]
    norm_num
  have hred :
      EwVevReducedHypotheses
        q Nv (treeK q 1) (perCarrierZeroMode 3 4)
        (signRule (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)))
        ((ewHbarQ q) ^ 2) α_v (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)) 1 :=
    { Nv_pos := inst.Nv_pos
      assembly := by rw [← hg4]; exact inst.su2_vev_assembly
      tree := rfl
      dressing_exponent := rfl
      zero_mode := rfl
      sector_group := rfl
      sign_rule := rfl
      c_loop := rfl
      self_consistency := inst.duality_self_consistency }
  have hhyp :
      EwVevHypotheses
        q Nv (treeK q 1) (perCarrierZeroMode 3 4)
        (signRule (oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)))
        ((ewHbarQ q) ^ 2) α_v :=
    @ewVevReduced_imp_hypotheses _ _ _ _ _ _ _ _ 1 hred
  have hcls : ElectroweakVevFixedPointClass q α_v :=
    @ewVevHypotheses_imp_class _ _ _ _ _ _ _ hhyp
  have hcub : ewFixedPointCubic q α_v = 0 :=
    (@ew_vev_is_fixed_point_root q α_v hcls).1
  exact ⟨hred, hhyp, hcls, hcub⟩

/-- **Non-vacuity / consistency witness (`def`, NEVER `instance` — `lean-generation` §5):**
Exhibits an explicit `(q = 2, Nv, α_v)` satisfying `MinimalElectroweakVevBridgeClass` without
registering any global typeclass instance. -/
noncomputable def trivialModelMinimalEwBridge :
    ∃ (q Nv α_v : ℝ), MinimalElectroweakVevBridgeClass q Nv α_v := by
  let q : ℝ := 2
  have hq_pos : 0 < q := by dsimp only [q]; norm_num
  have hqsub : q - q⁻¹ ≠ 0 := by dsimp only [q]; norm_num
  have hhab_eq : habiroNorm q = ewHabiroNorm q := habiroNorm_eq_ewHabiroNorm q hqsub
  have hH_pos : 0 < ewHabiroNorm q := by rw [← hhab_eq]; exact habiroNorm_pos hq_pos
  have hH_z : ewHabiroNorm q = ((q + q⁻¹) / 8) * ewBringZeroMode := by
    rw [← hhab_eq]; exact (habiroNorm_eq_rational_mul_zeroModes q).2
  have hH_z' : ewHabiroNorm q = (5 / 16) * ewBringZeroMode := by
    rw [hH_z]; dsimp only [q]; norm_num
  have hz_pos : 0 < ewBringZeroMode := by linarith
  have htree_pos : 10 < ewDressedTreeComplexity q := by
    unfold ewDressedTreeComplexity ewBareCrossingComplexity
    rw [QOU.QInteger.qIntBal_def, QOU.QInteger.qIntBal_def,
        QOU.QInteger.qIntBal_def, QOU.QInteger.qIntBal_def]
    dsimp only [q]
    norm_num
  have hT_pos : 0 < ewFixedPointConst q := by
    unfold ewFixedPointConst; linarith
  have hHT : 4 * ewHabiroNorm q < (ewFixedPointConst q) ^ 2 := by
    unfold ewFixedPointConst
    rw [hH_z']
    nlinarith
  obtain ⟨α_v, ⟨hα_in, hα_root⟩, _⟩ :=
    ewShapeCubic_existsUnique_root hT_pos (le_of_lt hH_pos) (sq_nonneg (ewHbarQ q)) hHT
  have hα_pos : 0 < α_v := hα_in.1
  have hα_ne : α_v ≠ 0 := ne_of_gt hα_pos
  have hfp : IsElectroweakVevFixedPoint q α_v := by
    rw [ewFixedPoint_iff_cubic q α_v hα_ne, ewFixedPointCubic_eq_shape]
    exact hα_root
  let Nv : ℝ := 1 / α_v
  have hNv_pos : 0 < Nv := one_div_pos.mpr hα_pos
  have hsc : α_v * Nv = 1 := mul_one_div_cancel hα_ne
  have hg4 : ((bringMapBettiOne / 2 : ℤ) : ℝ) = 4 := by
    rw [bringMapBettiOne_eq_eight_and_genus_four.2]; norm_num
  refine ⟨q, Nv, α_v, { Nv_pos := hNv_pos, duality_self_consistency := hsc, su2_vev_assembly := ?_ }⟩
  rw [hg4, treeK_one, perCarrier_ew, signRule_su2]
  unfold IsElectroweakVevFixedPoint ewFixedPointConst at hfp
  dsimp only [Nv]
  linarith

end MinimalBridgeReduction

end ElectroweakConditionalDischarge
end QOU.StandardModel
