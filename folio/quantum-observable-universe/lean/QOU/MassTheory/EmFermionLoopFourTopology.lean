/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.MassTheory.BringSchwingerNormalizationDerivation

/-!
# Four-Topology `EmFermionLoop` Bar-Hermitian Cancellation and Weight-3 Period Span (`§7c` Generic)

This module formalizes the pure algebraic (`[CommRing A]`, `[CommRing K]`, `[Field K]`) half of
beans `qou-9y43` and `qou-l4t2`, separated from the archimedean `ℝ` fixed-point module
`QOU.Archimedean.AlphaEmTwoLoopBlochSchwinger` per `AGENTS.md` §7c:

1. **Section 1 — Four-Topology `EmFermionLoop` Bar-Hermitian Cancellation (`[CommRing A]` / `[Field K]`):**
   Resolves the single-chirality gap documented in `2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md`:
   - For any Hecke generator `σ` (`σ * σ_inv = 1`, `σ² = h * σ + 1`), `σ_inv = σ - h` and
     `σ_inv² = 1 - h * σ + h²` (`hecke_inv_sq_expansion`).
   - Summing over all four signed chiral 2-vertex crossing topologies `(ε₁, ε₂) ∈ {+1, -1}²`
     (`m_pm + m_mp - m_pp - m_mm`) cancels the first-order chiral tadpoles `± h * m_sig`
     identically for **every** `m_sig : K` and yields exact unit coefficient `-1 * h²` in
     `1 - h² * α` (`four_topology_bar_hermitian_moment_sum`).
   - Specializing to the `U_q(sl₂)` singlet tadpole `m₁(q) = q³ / (q² + 1)` on `e₋ ⊗ I₂` recovers
     both exact rational excesses `(q⁴ - q²) / (q² + 1)` and `(1 - q²) / (q⁴ + q²)` and proves
     their negative sum equals `-(hHecke q)²` (`uq_sl2_singlet_four_topology_sum`).
   - Relates the half-averaged skein vertex `(hHecke q / 2)²` to `((q + 1) / 2)² * (hbarQ q)²`
     (`half_averaged_skein_sq_eq_hbarQ_sq`).

2. **Section 2 — Petermann–Sommerfield Weight-3 Period Decomposition (`[Field K]`):**
   Formalizes the exact rational combination `197/144 + (1/12) π² - (1/2) π² ln 2 + (3/4) ζ(3)`
   in the abstract 4-element period basis `(1, π², π² ln 2, ζ₃)` (`petermannSommerfield_cleared_eq`).
-/

set_option autoImplicit false

namespace QOU.Archimedean
namespace EmFermionLoopFourTopology

open QOU.Archimedean.BringSchwingerNormalizationDerivation
  (hHecke hbarQ singletSameChiralityExcess)

/-! ## Section 1: Four-Topology `EmFermionLoop` Bar-Hermitian Moment Cancellation (`§7c`) -/

section FourTopologyMomentCancellation

/-- **Inverse-Square Hecke Expansion over Any Commutative Ring**:
Given `σ, σ_inv, h : A` satisfying `σ * σ_inv = 1` and `σ ^ 2 = h * σ + 1`, the inverse satisfies
`σ_inv = σ - h` and its square satisfies `σ_inv ^ 2 = 1 - h * σ + h ^ 2`. -/
theorem hecke_inv_sq_expansion {A : Type*} [CommRing A]
    (σ σ_inv h : A) (hinv : σ * σ_inv = 1) (hhecke : σ ^ 2 = h * σ + 1) :
    σ_inv = σ - h ∧ σ_inv ^ 2 = 1 - h * σ + h ^ 2 := by
  have hdiff : σ_inv = σ - h := by
    have h1 : σ - σ_inv = h :=
      (BringSchwingerNormalizationDerivation.hecke_skein_bar_contraction
        σ σ_inv h 0 hinv hhecke).1
    linear_combination -h1
  refine ⟨hdiff, ?_⟩
  calc
    σ_inv ^ 2 = (σ - h) ^ 2 := by rw [hdiff]
    _ = σ ^ 2 - 2 * h * σ + h ^ 2 := by ring
    _ = (h * σ + 1) - 2 * h * σ + h ^ 2 := by rw [hhecke]
    _ = 1 - h * σ + h ^ 2 := by ring

/-- **Four-Topology Bar-Hermitian Moment Cancellation Theorem (`[CommRing K]`)**:
For any commutative ring `K`, skein parameter `h : K`, and first-moment tadpole `m_sig : K`, if
the four chiral 2-vertex topologies evaluate via the Hecke relations (`m_pm = 1`, `m_mp = 1`,
`m_pp = h * m_sig + 1`, `m_mm = 1 - h * m_sig + h ^ 2`), then:
1. `(m_pp - 1) = h * m_sig` and `(m_mm - 1) = -h * m_sig + h ^ 2`,
2. the signed 4-topology sum `m_pm + m_mp - m_pp - m_mm` cancels `m_sig` identically and equals
   `-h ^ 2`, and
3. the dressed 1-loop factor `1 + α * (m_pm + m_mp - m_pp - m_mm)` equals `1 - h ^ 2 * α`
   with exact unit coefficient `1`. -/
theorem four_topology_bar_hermitian_moment_sum {K : Type*} [CommRing K]
    (h m_sig α : K) :
    let m_pm : K := 1
    let m_mp : K := 1
    let m_pp : K := h * m_sig + 1
    let m_mm : K := 1 - h * m_sig + h ^ 2
    m_pp - 1 = h * m_sig ∧
    m_mm - 1 = -h * m_sig + h ^ 2 ∧
    m_pm + m_mp - m_pp - m_mm = -h ^ 2 ∧
    1 + α * (m_pm + m_mp - m_pp - m_mm) = 1 - h ^ 2 * α := by
  dsimp only
  refine ⟨by ring, by ring, by ring, by ring⟩

/-- The `U_q(sl₂)` singlet under–under 2-vertex moment excess
`m(σ₂⁻²) - 1 = (1 - q²) / (q⁴ + q²)` from
`2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md` Finding 2. -/
def singletUnderChiralityExcess {K : Type*} [Field K] (q : K) : K :=
  (1 - q ^ 2) / (q ^ 4 + q ^ 2)

/-- **Exact `U_q(sl₂)` Singlet Four-Topology Resolution (`[Field K]`)**:
For any `q : K` with `q ≠ 0` and `q ^ 2 + 1 ≠ 0`, setting the 1-vertex singlet tadpole to
`m₁ = q ^ 3 / (q ^ 2 + 1)` reproduces `singletSameChiralityExcess q = (q⁴ - q²) / (q² + 1)`
for `(+,+)`, `singletUnderChiralityExcess q = (1 - q²) / (q⁴ + q²)` for `(-,-)`, and proves
that `-singletSameChiralityExcess q - singletUnderChiralityExcess q = -(hHecke q) ^ 2`. -/
theorem uq_sl2_singlet_four_topology_sum {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let m1 : K := q ^ 3 / (q ^ 2 + 1)
    hHecke q * m1 = singletSameChiralityExcess q ∧
    -(hHecke q * m1) + (hHecke q) ^ 2 = singletUnderChiralityExcess q ∧
    -singletSameChiralityExcess q - singletUnderChiralityExcess q = -(hHecke q) ^ 2 := by
  dsimp only
  have hq4 : q ^ 4 + q ^ 2 ≠ 0 := by
    have hfac : q ^ 4 + q ^ 2 = q ^ 2 * (q ^ 2 + 1) := by ring
    rw [hfac]
    exact mul_ne_zero (pow_ne_zero 2 hq) hq2
  refine ⟨?_, ?_, ?_⟩
  · unfold hHecke singletSameChiralityExcess
    field_simp
  · unfold hHecke singletUnderChiralityExcess
    field_simp
    ring
  · unfold singletSameChiralityExcess singletUnderChiralityExcess hHecke
    field_simp
    ring

/-- **Half-Averaged vs Un-Averaged Skein Vertex Bridge (`[Field K]`)**:
Comparing the un-averaged skein vertex `S = hHecke q` (`-S * S_bar = -(hHecke q)²`) with the
half-averaged vertex `S / 2` (`-(S/2)*(S_bar/2) = -(hHecke q)² / 4`):
`(hHecke q / 2) ^ 2 = ((q + 1) / 2) ^ 2 * (hbarQ q) ^ 2` (which approaches `(hbarQ q)²` as `q → 1`). -/
theorem half_averaged_skein_sq_eq_hbarQ_sq {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    (hHecke q / 2) ^ 2 = ((q + 1) / 2) ^ 2 * (hbarQ q) ^ 2 := by
  unfold hHecke hbarQ
  field_simp
  ring

end FourTopologyMomentCancellation

/-! ## Section 2: Petermann–Sommerfield Weight-3 Period Decomposition (`[Field K]`) -/

section PetermannSommerfieldPeriodSpan

/-- Abstract weight-3 mixed-Tate / Bloch-`B₃` period basis carrier `(1, π², π² ln 2, ζ₃)`
over a field `K` (`char K ≠ 2, 3`), representing the `ℚ`-linear combination
`c₀ + c₁ · π² + c₂ · (π² ln 2) + c₃ · ζ₃`. -/
structure Weight3PeriodBasis (K : Type*) where
  /-- Value representing `π²` (`6 ζ(2)`). -/
  piSq : K
  /-- Value representing `π² ln 2`. -/
  piSqLn2 : K
  /-- Value representing `ζ(3)` (`Li₃(1)`). -/
  zeta3 : K

/-- The Petermann (1957) – Sommerfield (1957) 2-loop QED Schwinger coefficient
`C_PS = 197/144 + (1/12) π² - (1/2) π² ln 2 + (3/4) ζ(3)` evaluated on `Weight3PeriodBasis K`. -/
def petermannSommerfieldCoeff {K : Type*} [Field K] (B : Weight3PeriodBasis K) : K :=
  (197 : K) / 144 + B.piSq / 12 - B.piSqLn2 / 2 + (3 : K) / 4 * B.zeta3

/-- **Cleared-Denominator Period-Span Identity (`144 · C_PS`)**:
Over any field `K` in which `144 ≠ 0`, `144 * petermannSommerfieldCoeff B` equals the integer
linear combination `197 + 12 * B.piSq - 72 * B.piSqLn2 + 108 * B.zeta3`. -/
theorem petermannSommerfield_cleared_eq {K : Type*} [Field K]
    (B : Weight3PeriodBasis K) (h144 : (144 : K) ≠ 0) :
    144 * petermannSommerfieldCoeff B =
      197 + 12 * B.piSq - 72 * B.piSqLn2 + 108 * B.zeta3 := by
  unfold petermannSommerfieldCoeff
  have h12 : (12 : K) ≠ 0 := by
    intro h0; apply h144; calc (144 : K) = 12 * 12 := by norm_num
      _ = 0 := by rw [h0]; ring
  have h2 : (2 : K) ≠ 0 := by
    intro h0; apply h12; calc (12 : K) = 6 * 2 := by norm_num
      _ = 0 := by rw [h0]; ring
  have h4 : (4 : K) ≠ 0 := by
    intro h0; apply h12; calc (12 : K) = 3 * 4 := by norm_num
      _ = 0 := by rw [h0]; ring
  field_simp
  ring

end PetermannSommerfieldPeriodSpan

end EmFermionLoopFourTopology
end QOU.Archimedean
