import BraidKnotOctonion.HydrogenCaptureWeightSpace
import Mathlib.Algebra.FreeAlgebra
import Mathlib.LinearAlgebra.Span.Defs


/-!
# Hydrogen capture: the χ_(3) factorisation and the translated mirror (#8804 §46)

Setting as in `HydrogenCaptureWeightSpace`: Jimbo `Ř` on `(C²)^{⊗4}`, `h = q − q⁻¹`,
`σ⁻¹ = σ − h`; `F(O₊)`, `F(O₋)` are `Fplus16`, `Fminus16` (proton on strands `0–2`) and
`S = F(O₊) + F(O₋)`. The cabled capture is `K_L = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹` (`capKL`).

A **proton element** is any `x` in the free algebra on `s₀, s₁` (`Proton R`): every word in
`σ₀^{±1}, σ₁^{±1}` and every linear combination of words, in particular every product of photons
`γ(φ) = 1 + φ₀s₀ + φ₁s₁ + φ₀₁s₀s₁⁻¹` (owner ruling) and gluon words. `evL16 x` places it on strands
`0–2` (`s_i ↦ σ_i`); `evR16 x` translates it to strands `1–3` (`s_i ↦ σ_{i+1}`).

**Results (generic field `R`, only `q ≠ 0`).**
* `S_factorises`: `S(evL16 x · K_L) = χ_(3)(x) · S(K_L)` for every proton element `x`, where
  `χ_(3)` is the character `s_i ↦ q` (`chi3`). `capture_S`: `S(K_L) = −h²[3]_q/q²`.
* `S_photon_pair`: for `x = γ(φ)γ(ψ)g`,
  `S = (1 + qφ₀ + qφ₁ + φ₀₁)(1 + qψ₀ + qψ₁ + ψ₀₁) · χ_(3)(g) · S(K_L)`, with `χ_(3)(g) = 1, 1, q, q²`
  for `g = 1, s₀s₁⁻¹, s₁, s₁s₀` (`S_arm_1`, `S_arm_V`, `S_arm_S1`, `S_arm_S1S0`).
* `mirror_plus`, `mirror_minus`: with the proton TRANSLATED and the capture reflected
  (`K_R = (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`, the probe's right placement),
  `O₊(right) = −O₋(left)` and `O₋(right) = −O₊(left)` for every proton element.
  `CapturePlacement` (sibling branch) proves the corresponding statement for the REFLECTED word
  (`σ_i ↦ σ_{2−i}`, `FplusR_flip`, `FminusR_flip`); the two differ because the photon's fourth term
  `σ₀σ₁⁻¹` reflects to `σ₂σ₁⁻¹`, not to the ruled `σ₁σ₂⁻¹`. Here the translated form follows from
  the same five-dimensional reduction as (i).

**Mechanism.** On each four-dimensional weight space the proton algebra acts through the span of
`1, s₀, s₁, s₀s₁, s₁s₀`, because `s₀s₁s₀ = q³ − q²s₀ − q²s₁ + qs₀s₁ + qs₁s₀` there (`noAntisym`:
`(C²)^{⊗3}` has no `(1³)` part). `L` is that span on the four blocks at once; `evQ_mem` shows every
proton element lies in it, and `L_factorises`, `L_mirror_plus`, `L_mirror_minus` check the
identities on the five basis elements. The `(3)`-entry of the one-zero block is `χ_(3)` (`evQ_33`).
The capture blocks are computed exactly (`KAL`, `KBL`, `KAR`, `KBR`). No numerical value enters.

Not covered: the adjacent capture `σ₂⁻²`, which does not commute with `σ₁`.
-/

namespace QOU.BraidsAndKnots.HydrogenCaptureFactorisation

open Matrix QOU.BraidsAndKnots.HydrogenCaptureWeightSpace

variable {R : Type*} [Field R]

set_option linter.unusedVariables false

/-- The two proton letters `s₀, s₁` on the four weight-space blocks at once:
component `0` = one-zero space, proton left (`σ₀, σ₁`); `1` = one-one space, proton left;
`2` = one-zero space, proton right (`σ₁, σ₂`); `3` = one-one space, proton right. -/
def genQ (q : R) : Fin 2 → (Fin 4 → Matrix (Fin 4) (Fin 4) R)
  | 0 => ![A0 q, B0 q, A1 q, B1 q]
  | 1 => ![A1 q, B1 q, A2 q, B2 q]


theorem p01_AL (q : R) (hq : q ≠ 0) : A0 q * A1 q = !![(0), (0), (1), (0); (q), (0), ((q^2 - 1) / q), (0); (0), (q), (q^2 - 1), (0); (0), (0), (0), (q^2)] := by matTac
theorem p10_AL (q : R) (hq : q ≠ 0) : A1 q * A0 q = !![(0), (q), (0), (0); (0), (0), (q), (0); (1), ((q^2 - 1) / q), (q^2 - 1), (0); (0), (0), (0), (q^2)] := by matTac
theorem t010_AL (q : R) (hq : q ≠ 0) : A0 q * A1 q * A0 q = !![(0), (0), (q), (0); (0), (q), (q^2 - 1), (0); (q), (q^2 - 1), (q^3 - q), (0); (0), (0), (0), (q^3)] := by
  rw [p01_AL q hq]; matTac
theorem t101_AL (q : R) (hq : q ≠ 0) : A1 q * A0 q * A1 q = !![(0), (0), (q), (0); (0), (q), (q^2 - 1), (0); (q), (q^2 - 1), (q^3 - q), (0); (0), (0), (0), (q^3)] := by
  rw [p10_AL q hq]; matTac
theorem rel_AL (q : R) (hq : q ≠ 0) : A0 q * A1 q * A0 q
    = q ^ 3 • (1 : Matrix (Fin 4) (Fin 4) R) - q ^ 2 • A0 q - q ^ 2 • A1 q + q • (A0 q * A1 q) + q • (A1 q * A0 q) := by
  rw [t010_AL q hq, p01_AL q hq, p10_AL q hq]; matTac

theorem p01_BL (q : R) (hq : q ≠ 0) : B0 q * B1 q = !![(q^2), (0), (0), (0); (0), (0), (q), (0); (0), (0), (0), (q); (0), (1), ((q^2 - 1) / q), (q^2 - 1)] := by matTac
theorem p10_BL (q : R) (hq : q ≠ 0) : B1 q * B0 q = !![(q^2), (0), (0), (0); (0), (0), (0), (1); (0), (q), (0), ((q^2 - 1) / q); (0), (0), (q), (q^2 - 1)] := by matTac
theorem t010_BL (q : R) (hq : q ≠ 0) : B0 q * B1 q * B0 q = !![(q^3), (0), (0), (0); (0), (0), (0), (q); (0), (0), (q), (q^2 - 1); (0), (q), (q^2 - 1), (q^3 - q)] := by
  rw [p01_BL q hq]; matTac
theorem t101_BL (q : R) (hq : q ≠ 0) : B1 q * B0 q * B1 q = !![(q^3), (0), (0), (0); (0), (0), (0), (q); (0), (0), (q), (q^2 - 1); (0), (q), (q^2 - 1), (q^3 - q)] := by
  rw [p10_BL q hq]; matTac
theorem rel_BL (q : R) (hq : q ≠ 0) : B0 q * B1 q * B0 q
    = q ^ 3 • (1 : Matrix (Fin 4) (Fin 4) R) - q ^ 2 • B0 q - q ^ 2 • B1 q + q • (B0 q * B1 q) + q • (B1 q * B0 q) := by
  rw [t010_BL q hq, p01_BL q hq, p10_BL q hq]; matTac

theorem p01_AR (q : R) (hq : q ≠ 0) : A1 q * A2 q = !![(q^2), (0), (0), (0); (0), (0), (0), (1); (0), (q), (0), ((q^2 - 1) / q); (0), (0), (q), (q^2 - 1)] := by matTac
theorem p10_AR (q : R) (hq : q ≠ 0) : A2 q * A1 q = !![(q^2), (0), (0), (0); (0), (0), (q), (0); (0), (0), (0), (q); (0), (1), ((q^2 - 1) / q), (q^2 - 1)] := by matTac
theorem t010_AR (q : R) (hq : q ≠ 0) : A1 q * A2 q * A1 q = !![(q^3), (0), (0), (0); (0), (0), (0), (q); (0), (0), (q), (q^2 - 1); (0), (q), (q^2 - 1), (q^3 - q)] := by
  rw [p01_AR q hq]; matTac
theorem t101_AR (q : R) (hq : q ≠ 0) : A2 q * A1 q * A2 q = !![(q^3), (0), (0), (0); (0), (0), (0), (q); (0), (0), (q), (q^2 - 1); (0), (q), (q^2 - 1), (q^3 - q)] := by
  rw [p10_AR q hq]; matTac
theorem rel_AR (q : R) (hq : q ≠ 0) : A1 q * A2 q * A1 q
    = q ^ 3 • (1 : Matrix (Fin 4) (Fin 4) R) - q ^ 2 • A1 q - q ^ 2 • A2 q + q • (A1 q * A2 q) + q • (A2 q * A1 q) := by
  rw [t010_AR q hq, p01_AR q hq, p10_AR q hq]; matTac

theorem p01_BR (q : R) (hq : q ≠ 0) : B1 q * B2 q = !![(0), (q), (0), (0); (0), (0), (q), (0); (1), ((q^2 - 1) / q), (q^2 - 1), (0); (0), (0), (0), (q^2)] := by matTac
theorem p10_BR (q : R) (hq : q ≠ 0) : B2 q * B1 q = !![(0), (0), (1), (0); (q), (0), ((q^2 - 1) / q), (0); (0), (q), (q^2 - 1), (0); (0), (0), (0), (q^2)] := by matTac
theorem t010_BR (q : R) (hq : q ≠ 0) : B1 q * B2 q * B1 q = !![(0), (0), (q), (0); (0), (q), (q^2 - 1), (0); (q), (q^2 - 1), (q^3 - q), (0); (0), (0), (0), (q^3)] := by
  rw [p01_BR q hq]; matTac
theorem t101_BR (q : R) (hq : q ≠ 0) : B2 q * B1 q * B2 q = !![(0), (0), (q), (0); (0), (q), (q^2 - 1), (0); (q), (q^2 - 1), (q^3 - q), (0); (0), (0), (0), (q^3)] := by
  rw [p10_BR q hq]; matTac
theorem rel_BR (q : R) (hq : q ≠ 0) : B1 q * B2 q * B1 q
    = q ^ 3 • (1 : Matrix (Fin 4) (Fin 4) R) - q ^ 2 • B1 q - q ^ 2 • B2 q + q • (B1 q * B2 q) + q • (B2 q * B1 q) := by
  rw [t010_BR q hq, p01_BR q hq, p10_BR q hq]; matTac

theorem hecke_A0 (q : R) (hq : q ≠ 0) : A0 q * A0 q = (q - q⁻¹) • A0 q + 1 := by matTac
theorem hecke_A1 (q : R) (hq : q ≠ 0) : A1 q * A1 q = (q - q⁻¹) • A1 q + 1 := by matTac
theorem hecke_A2 (q : R) (hq : q ≠ 0) : A2 q * A2 q = (q - q⁻¹) • A2 q + 1 := by matTac

theorem hecke (q : R) (hq : q ≠ 0) (i : Fin 2) :
    genQ q i * genQ q i = (q - q⁻¹) • genQ q i + 1 := by
  funext j; fin_cases i <;> fin_cases j <;> simp only [genQ, Pi.mul_apply, Pi.add_apply,
    Pi.smul_apply, Pi.one_apply] <;> simp <;>
  first | exact hecke_A0 q hq | exact hecke_A1 q hq | exact hecke_A2 q hq

theorem braid01 (q : R) (hq : q ≠ 0) :
    genQ q 1 * genQ q 0 * genQ q 1 = genQ q 0 * genQ q 1 * genQ q 0 := by
  funext j; fin_cases j <;> simp [genQ]
  · rw [t101_AL q hq, t010_AL q hq]
  · rw [t101_BL q hq, t010_BL q hq]
  · rw [t101_AR q hq, t010_AR q hq]
  · rw [t101_BR q hq, t010_BR q hq]

/-- On `(C²)^{⊗3}` there is no `(1³)` component, so `s₀s₁s₀` is a combination of the other five
basis words of the three-strand Hecke algebra (on all four blocks, with equal coefficients). -/
theorem noAntisym (q : R) (hq : q ≠ 0) :
    genQ q 0 * genQ q 1 * genQ q 0
      = q ^ 3 • (1 : Fin 4 → Matrix (Fin 4) (Fin 4) R) - q ^ 2 • genQ q 0 - q ^ 2 • genQ q 1
        + q • (genQ q 0 * genQ q 1) + q • (genQ q 1 * genQ q 0) := by
  funext j; fin_cases j <;> simp only [genQ, Pi.mul_apply, Pi.add_apply, Pi.sub_apply,
    Pi.smul_apply, Pi.one_apply] <;> simp
  · exact rel_AL q hq
  · exact rel_BL q hq
  · exact rel_AR q hq
  · exact rel_BR q hq



/-! ### The capture blocks, step by step -/

theorem kAL_s5 (q : R) (hq : q ≠ 0) :
    wordA q [(2, true)] = !![((1) / q), (0), (0), (0); (0), ((1) / q), (0), (0); (0), (0), ((1 - q^2) / q), (1); (0), (0), (1), (0)] := by
  simp only [wordA, gA, mul_one]; matTac
theorem kAL_s4 (q : R) (hq : q ≠ 0) :
    wordA q [(1, true), (2, true)] = !![((1) / q^2), (0), (0), (0); (0), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), ((1) / q), (0), (0); (0), (0), ((1) / q), (0)] := by
  rw [show wordA q [(1, true), (2, true)] = gA q (1, true) * wordA q [(2, true)] from rfl, kAL_s5 q hq]
  simp only [gA]; matTac
theorem kAL_s3 (q : R) (hq : q ≠ 0) :
    wordA q [(0, true), (1, true), (2, true)] = !![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); ((1) / q^2), (0), (0), (0); (0), ((1) / q^2), (0), (0); (0), (0), ((1) / q^2), (0)] := by
  rw [show wordA q [(0, true), (1, true), (2, true)] = gA q (0, true) * wordA q [(1, true), (2, true)] from rfl, kAL_s4 q hq]
  simp only [gA]; matTac
theorem kAL_s2 (q : R) (hq : q ≠ 0) :
    wordA q [(0, true), (0, true), (1, true), (2, true)] = !![((q^4 - q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^4 - 2*q^2 + 1) / q^2), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), ((1) / q^3), (0), (0); (0), (0), ((1) / q^3), (0)] := by
  rw [show wordA q [(0, true), (0, true), (1, true), (2, true)] = gA q (0, true) * wordA q [(0, true), (1, true), (2, true)] from rfl, kAL_s3 q hq]
  simp only [gA]; matTac
theorem kAL_s1 (q : R) (hq : q ≠ 0) :
    wordA q [(1, true), (0, true), (0, true), (1, true), (2, true)] = !![((q^4 - q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 2) / q^3), ((q^4 - 2*q^2 + 1) / q^2), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), (0), ((1) / q^4), (0)] := by
  rw [show wordA q [(1, true), (0, true), (0, true), (1, true), (2, true)] = gA q (1, true) * wordA q [(0, true), (0, true), (1, true), (2, true)] from rfl, kAL_s2 q hq]
  simp only [gA]; matTac
theorem kAL_s0 (q : R) (hq : q ≠ 0) :
    wordA q [(2, true), (1, true), (0, true), (0, true), (1, true), (2, true)] = !![((q^4 - q^2 + 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1 - q^2) / q^3); ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 2) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^6 - 2*q^4 + q^2 + 1) / q^4), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)] := by
  rw [show wordA q [(2, true), (1, true), (0, true), (0, true), (1, true), (2, true)] = gA q (2, true) * wordA q [(1, true), (0, true), (0, true), (1, true), (2, true)] from rfl, kAL_s1 q hq]
  simp only [gA]; matTac

theorem kAR_s5 (q : R) (hq : q ≠ 0) :
    wordA q [(0, true)] = !![((1 - q^2) / q), (1), (0), (0); (1), (0), (0), (0); (0), (0), ((1) / q), (0); (0), (0), (0), ((1) / q)] := by
  simp only [wordA, gA, mul_one]; matTac
theorem kAR_s4 (q : R) (hq : q ≠ 0) :
    wordA q [(1, true), (0, true)] = !![((1 - q^2) / q^2), ((1) / q), (0), (0); ((1 - q^2) / q), (0), ((1) / q), (0); (1), (0), (0), (0); (0), (0), (0), ((1) / q^2)] := by
  rw [show wordA q [(1, true), (0, true)] = gA q (1, true) * wordA q [(0, true)] from rfl, kAR_s5 q hq]
  simp only [gA]; matTac
theorem kAR_s3 (q : R) (hq : q ≠ 0) :
    wordA q [(2, true), (1, true), (0, true)] = !![((1 - q^2) / q^3), ((1) / q^2), (0), (0); ((1 - q^2) / q^2), (0), ((1) / q^2), (0); ((1 - q^2) / q), (0), (0), ((1) / q^2); (1), (0), (0), (0)] := by
  rw [show wordA q [(2, true), (1, true), (0, true)] = gA q (2, true) * wordA q [(1, true), (0, true)] from rfl, kAR_s4 q hq]
  simp only [gA]; matTac
theorem kAR_s2 (q : R) (hq : q ≠ 0) :
    wordA q [(2, true), (2, true), (1, true), (0, true)] = !![((1 - q^2) / q^4), ((1) / q^3), (0), (0); ((1 - q^2) / q^3), (0), ((1) / q^3), (0); ((q^4 - q^2 + 1) / q^2), (0), (0), ((1 - q^2) / q^3); ((1 - q^2) / q), (0), (0), ((1) / q^2)] := by
  rw [show wordA q [(2, true), (2, true), (1, true), (0, true)] = gA q (2, true) * wordA q [(2, true), (1, true), (0, true)] from rfl, kAR_s3 q hq]
  simp only [gA]; matTac
theorem kAR_s1 (q : R) (hq : q ≠ 0) :
    wordA q [(1, true), (2, true), (2, true), (1, true), (0, true)] = !![((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((q^6 - q^2 + 1) / q^4), (0), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^3), (0), ((1) / q^3), (0); ((1 - q^2) / q^2), (0), (0), ((1) / q^3)] := by
  rw [show wordA q [(1, true), (2, true), (2, true), (1, true), (0, true)] = gA q (1, true) * wordA q [(2, true), (2, true), (1, true), (0, true)] from rfl, kAR_s2 q hq]
  simp only [gA]; matTac
theorem kAR_s0 (q : R) (hq : q ≠ 0) :
    wordA q [(0, true), (1, true), (2, true), (2, true), (1, true), (0, true)] = !![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((1 - q^2) / q^4), (0), ((1) / q^4), (0); ((1 - q^2) / q^3), (0), (0), ((1) / q^4)] := by
  rw [show wordA q [(0, true), (1, true), (2, true), (2, true), (1, true), (0, true)] = gA q (0, true) * wordA q [(1, true), (2, true), (2, true), (1, true), (0, true)] from rfl, kAR_s1 q hq]
  simp only [gA]; matTac

theorem kBL_s5 (q : R) (hq : q ≠ 0) :
    wordB q [(2, true)] = !![((1 - q^2) / q), (1), (0), (0); (1), (0), (0), (0); (0), (0), ((1) / q), (0); (0), (0), (0), ((1) / q)] := by
  simp only [wordB, gB, mul_one]; matTac
theorem kBL_s4 (q : R) (hq : q ≠ 0) :
    wordB q [(1, true), (2, true)] = !![((1 - q^2) / q^2), ((1) / q), (0), (0); ((1 - q^2) / q), (0), ((1) / q), (0); (1), (0), (0), (0); (0), (0), (0), ((1) / q^2)] := by
  rw [show wordB q [(1, true), (2, true)] = gB q (1, true) * wordB q [(2, true)] from rfl, kBL_s5 q hq]
  simp only [gB]; matTac
theorem kBL_s3 (q : R) (hq : q ≠ 0) :
    wordB q [(0, true), (1, true), (2, true)] = !![((1 - q^2) / q^3), ((1) / q^2), (0), (0); ((1 - q^2) / q^2), (0), ((1) / q^2), (0); ((1 - q^2) / q), (0), (0), ((1) / q^2); (1), (0), (0), (0)] := by
  rw [show wordB q [(0, true), (1, true), (2, true)] = gB q (0, true) * wordB q [(1, true), (2, true)] from rfl, kBL_s4 q hq]
  simp only [gB]; matTac
theorem kBL_s2 (q : R) (hq : q ≠ 0) :
    wordB q [(0, true), (0, true), (1, true), (2, true)] = !![((1 - q^2) / q^4), ((1) / q^3), (0), (0); ((1 - q^2) / q^3), (0), ((1) / q^3), (0); ((q^4 - q^2 + 1) / q^2), (0), (0), ((1 - q^2) / q^3); ((1 - q^2) / q), (0), (0), ((1) / q^2)] := by
  rw [show wordB q [(0, true), (0, true), (1, true), (2, true)] = gB q (0, true) * wordB q [(0, true), (1, true), (2, true)] from rfl, kBL_s3 q hq]
  simp only [gB]; matTac
theorem kBL_s1 (q : R) (hq : q ≠ 0) :
    wordB q [(1, true), (0, true), (0, true), (1, true), (2, true)] = !![((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((q^6 - q^2 + 1) / q^4), (0), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^3), (0), ((1) / q^3), (0); ((1 - q^2) / q^2), (0), (0), ((1) / q^3)] := by
  rw [show wordB q [(1, true), (0, true), (0, true), (1, true), (2, true)] = gB q (1, true) * wordB q [(0, true), (0, true), (1, true), (2, true)] from rfl, kBL_s2 q hq]
  simp only [gB]; matTac
theorem kBL_s0 (q : R) (hq : q ≠ 0) :
    wordB q [(2, true), (1, true), (0, true), (0, true), (1, true), (2, true)] = !![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((1 - q^2) / q^4), (0), ((1) / q^4), (0); ((1 - q^2) / q^3), (0), (0), ((1) / q^4)] := by
  rw [show wordB q [(2, true), (1, true), (0, true), (0, true), (1, true), (2, true)] = gB q (2, true) * wordB q [(1, true), (0, true), (0, true), (1, true), (2, true)] from rfl, kBL_s1 q hq]
  simp only [gB]; matTac

theorem kBR_s5 (q : R) (hq : q ≠ 0) :
    wordB q [(0, true)] = !![((1) / q), (0), (0), (0); (0), ((1) / q), (0), (0); (0), (0), ((1 - q^2) / q), (1); (0), (0), (1), (0)] := by
  simp only [wordB, gB, mul_one]; matTac
theorem kBR_s4 (q : R) (hq : q ≠ 0) :
    wordB q [(1, true), (0, true)] = !![((1) / q^2), (0), (0), (0); (0), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), ((1) / q), (0), (0); (0), (0), ((1) / q), (0)] := by
  rw [show wordB q [(1, true), (0, true)] = gB q (1, true) * wordB q [(0, true)] from rfl, kBR_s5 q hq]
  simp only [gB]; matTac
theorem kBR_s3 (q : R) (hq : q ≠ 0) :
    wordB q [(2, true), (1, true), (0, true)] = !![((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); ((1) / q^2), (0), (0), (0); (0), ((1) / q^2), (0), (0); (0), (0), ((1) / q^2), (0)] := by
  rw [show wordB q [(2, true), (1, true), (0, true)] = gB q (2, true) * wordB q [(1, true), (0, true)] from rfl, kBR_s4 q hq]
  simp only [gB]; matTac
theorem kBR_s2 (q : R) (hq : q ≠ 0) :
    wordB q [(2, true), (2, true), (1, true), (0, true)] = !![((q^4 - q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^4 - 2*q^2 + 1) / q^2), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), ((1) / q^3), (0), (0); (0), (0), ((1) / q^3), (0)] := by
  rw [show wordB q [(2, true), (2, true), (1, true), (0, true)] = gB q (2, true) * wordB q [(2, true), (1, true), (0, true)] from rfl, kBR_s3 q hq]
  simp only [gB]; matTac
theorem kBR_s1 (q : R) (hq : q ≠ 0) :
    wordB q [(1, true), (2, true), (2, true), (1, true), (0, true)] = !![((q^4 - q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 2) / q^3), ((q^4 - 2*q^2 + 1) / q^2), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1); (0), (0), ((1) / q^4), (0)] := by
  rw [show wordB q [(1, true), (2, true), (2, true), (1, true), (0, true)] = gB q (1, true) * wordB q [(2, true), (2, true), (1, true), (0, true)] from rfl, kBR_s2 q hq]
  simp only [gB]; matTac
theorem kBR_s0 (q : R) (hq : q ≠ 0) :
    wordB q [(0, true), (1, true), (2, true), (2, true), (1, true), (0, true)] = !![((q^4 - q^2 + 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1 - q^2) / q^3); ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 2) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^6 - 2*q^4 + q^2 + 1) / q^4), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)] := by
  rw [show wordB q [(0, true), (1, true), (2, true), (2, true), (1, true), (0, true)] = gB q (0, true) * wordB q [(1, true), (2, true), (2, true), (1, true), (0, true)] from rfl, kBR_s1 q hq]
  simp only [gB]; matTac

def KAL (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((q^4 - q^2 + 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1 - q^2) / q^3); ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 2) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^6 - 2*q^4 + q^2 + 1) / q^4), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]
def KBL (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((1 - q^2) / q^4), (0), ((1) / q^4), (0); ((1 - q^2) / q^3), (0), (0), ((1) / q^4)]
def KAR (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((q^8 - q^2 + 1) / q^6), ((1 - q^2) / q^5), ((1 - q^2) / q^4), ((1 - q^2) / q^3); ((1 - q^2) / q^5), ((1) / q^4), (0), (0); ((1 - q^2) / q^4), (0), ((1) / q^4), (0); ((1 - q^2) / q^3), (0), (0), ((1) / q^4)]
def KBR (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![((q^4 - q^2 + 1) / q^6), ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 1) / q^4), ((1 - q^2) / q^3); ((q^4 - 2*q^2 + 1) / q^5), ((q^4 - 2*q^2 + 2) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((1 - q^2) / q^2); ((q^4 - 2*q^2 + 1) / q^4), ((q^4 - 2*q^2 + 1) / q^3), ((q^6 - 2*q^4 + q^2 + 1) / q^4), ((1 - q^2) / q); ((1 - q^2) / q^3), ((1 - q^2) / q^2), ((1 - q^2) / q), (1)]

/-! ### The five-dimensional image of the proton algebra -/

/-- Images of `1, s₀, s₁, s₀s₁, s₁s₀` on the four blocks. -/
def bQ (q : R) : Fin 5 → (Fin 4 → Matrix (Fin 4) (Fin 4) R) :=
  ![1, genQ q 0, genQ q 1, genQ q 0 * genQ q 1, genQ q 1 * genQ q 0]

/-- Their span. -/
def L (q : R) : Submodule R (Fin 4 → Matrix (Fin 4) (Fin 4) R) :=
  Submodule.span R (Set.range (bQ q))

theorem bQ_mem (q : R) (k : Fin 5) : bQ q k ∈ L q := Submodule.subset_span ⟨k, rfl⟩

theorem bQ0 (q : R) : bQ q 0 = 1 := rfl
theorem bQ1 (q : R) : bQ q 1 = genQ q 0 := rfl
theorem bQ2 (q : R) : bQ q 2 = genQ q 1 := rfl
theorem bQ3 (q : R) : bQ q 3 = genQ q 0 * genQ q 1 := rfl
theorem bQ4 (q : R) : bQ q 4 = genQ q 1 * genQ q 0 := rfl

/-- `L` is stable under left multiplication by each proton letter. -/
theorem gen_mul_mem (q : R) (hq : q ≠ 0) (i : Fin 2) {v : Fin 4 → Matrix (Fin 4) (Fin 4) R}
    (hv : v ∈ L q) : genQ q i * v ∈ L q := by
  induction hv using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨k, rfl⟩ := hx
    have m := bQ_mem q
    have hrel : genQ q 0 * (genQ q 1 * genQ q 0) = q ^ 3 • bQ q 0 - q ^ 2 • bQ q 1 - q ^ 2 • bQ q 2
        + q • bQ q 3 + q • bQ q 4 := by
      rw [← mul_assoc, noAntisym q hq]; rfl
    have hrel' : genQ q 1 * (genQ q 0 * genQ q 1) = q ^ 3 • bQ q 0 - q ^ 2 • bQ q 1
        - q ^ 2 • bQ q 2 + q • bQ q 3 + q • bQ q 4 := by
      rw [← mul_assoc, braid01 q hq, noAntisym q hq]; rfl
    have rmem : q ^ 3 • bQ q 0 - q ^ 2 • bQ q 1 - q ^ 2 • bQ q 2 + q • bQ q 3 + q • bQ q 4 ∈ L q :=
      add_mem (add_mem (sub_mem (sub_mem (Submodule.smul_mem _ _ (m 0)) (Submodule.smul_mem _ _ (m 1)))
        (Submodule.smul_mem _ _ (m 2))) (Submodule.smul_mem _ _ (m 3))) (Submodule.smul_mem _ _ (m 4))
    fin_cases i <;> fin_cases k
    · simpa [bQ] using m 1
    · show genQ q 0 * genQ q 0 ∈ L q
      rw [hecke q hq 0, ← bQ1, ← bQ0]
      exact add_mem (Submodule.smul_mem _ _ (m 1)) (m 0)
    · simpa [bQ] using m 3
    · show genQ q 0 * (genQ q 0 * genQ q 1) ∈ L q
      rw [← mul_assoc, hecke q hq 0, add_mul, one_mul, smul_mul_assoc, ← bQ3, ← bQ2]
      exact add_mem (Submodule.smul_mem _ _ (m 3)) (m 2)
    · show genQ q 0 * (genQ q 1 * genQ q 0) ∈ L q
      rw [hrel]; exact rmem
    · simpa [bQ] using m 2
    · simpa [bQ] using m 4
    · show genQ q 1 * genQ q 1 ∈ L q
      rw [hecke q hq 1, ← bQ2, ← bQ0]
      exact add_mem (Submodule.smul_mem _ _ (m 2)) (m 0)
    · show genQ q 1 * (genQ q 0 * genQ q 1) ∈ L q
      rw [hrel']; exact rmem
    · show genQ q 1 * (genQ q 1 * genQ q 0) ∈ L q
      rw [← mul_assoc, hecke q hq 1, add_mul, one_mul, smul_mul_assoc, ← bQ4, ← bQ1]
      exact add_mem (Submodule.smul_mem _ _ (m 4)) (m 1)
  | zero => rw [mul_zero]; exact zero_mem _
  | add x y _ _ hx hy => rw [mul_add]; exact add_mem hx hy
  | smul a x _ hx => rw [mul_smul_comm]; exact Submodule.smul_mem _ a hx

/-! ### Proton elements: the free algebra on `s₀, s₁` -/

/-- A proton element: any noncommutative polynomial in `s₀, s₁` (inverses are `s − h`). -/
abbrev Proton (R : Type*) [Field R] := FreeAlgebra R (Fin 2)

/-- The four weight-space blocks of a proton element. -/
def evQ (q : R) : Proton R →ₐ[R] (Fin 4 → Matrix (Fin 4) (Fin 4) R) := FreeAlgebra.lift R (genQ q)

theorem evQ_mul_mem (q : R) (hq : q ≠ 0) (x : Proton R) :
    ∀ v ∈ L q, evQ q x * v ∈ L q := by
  refine FreeAlgebra.induction R (Fin 2) ?_ ?_ ?_ ?_ x
  · intro r v hv
    rw [AlgHom.commutes, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
    exact Submodule.smul_mem _ r hv
  · intro i v hv
    rw [evQ, FreeAlgebra.lift_ι_apply]; exact gen_mul_mem q hq i hv
  · intro a b ha hb v hv
    rw [map_mul, mul_assoc]; exact ha _ (hb v hv)
  · intro a b ha hb v hv
    rw [map_add, add_mul]; exact add_mem (ha v hv) (hb v hv)

/-- Every proton element lies in the five-dimensional span `L`. -/
theorem evQ_mem (q : R) (hq : q ≠ 0) (x : Proton R) : evQ q x ∈ L q := by
  simpa using evQ_mul_mem q hq x 1 (by simpa [bQ] using bQ_mem q 0)

/-- `χ_(3)`: the one-dimensional character `s_i ↦ q` of the proton algebra. -/
def chi3 (q : R) : Proton R →ₐ[R] R := FreeAlgebra.lift R (fun _ => q)

/-- Row `3` of the one-zero block, proton left (proton strands all `1`, electron `0`) is
`χ_(3)` times a unit row. -/
theorem evQ_row3 (q : R) (x : Proton R) (t : Fin 4) :
    evQ q x 0 3 t = if t = 3 then chi3 q x else 0 := by
  revert t
  refine FreeAlgebra.induction R (Fin 2) ?_ ?_ ?_ ?_ x
  · intro r t
    rw [AlgHom.commutes, AlgHom.commutes]
    fin_cases t <;> simp [Algebra.algebraMap_eq_smul_one]
  · intro i t
    simp only [evQ, chi3, FreeAlgebra.lift_ι_apply]
    fin_cases i <;> fin_cases t <;> simp [genQ, A0, A1]
  · intro a b ha hb t
    rw [map_mul, map_mul, Pi.mul_apply, Matrix.mul_apply]
    simp only [ha, ite_mul, zero_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true, hb]
    split_ifs <;> simp
  · intro a b ha hb t
    rw [map_add, map_add, Pi.add_apply, Matrix.add_apply, ha, hb]
    split_ifs <;> simp

theorem evQ_33 (q : R) (x : Proton R) : evQ q x 0 3 3 = chi3 q x := by simp [evQ_row3]


/-! ### The capture on the weight spaces -/

/-- The cabled capture with the proton on strands `0–2`: `K_L = (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹`. -/
def capKL : List Letter := [(2, true), (1, true), (0, true), (0, true), (1, true), (2, true)]
/-- Its reflection, proton on strands `1–3`: `K_R = (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`. -/
def capKR : List Letter := [(0, true), (1, true), (2, true), (2, true), (1, true), (0, true)]

theorem wordA_capKL (q : R) (hq : q ≠ 0) : wordA q capKL = KAL q := kAL_s0 q hq
theorem wordB_capKL (q : R) (hq : q ≠ 0) : wordB q capKL = KBL q := kBL_s0 q hq
theorem wordA_capKR (q : R) (hq : q ≠ 0) : wordA q capKR = KAR q := kAR_s0 q hq
theorem wordB_capKR (q : R) (hq : q ≠ 0) : wordB q capKR = KBR q := kBR_s0 q hq

/-- The exact orientation sum of the capture alone (weight-space form). -/
theorem SK_val (q : R) (hq : q ≠ 0) :
    FplusL (KBL q) + FminusL (KAL q) = -((q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6 := by
  simp [FplusL, FminusL, KAL, KBL]; field_simp; ring

set_option hygiene false in
macro "basisTac" : tactic => `(tactic| (fin_cases k <;> (
  simp [bQ, genQ, p01_AL q hq, p10_AL q hq, p01_BL q hq, p10_BL q hq, p01_AR q hq, p10_AR q hq,
    p01_BR q hq, p10_BR q hq, FplusL, FminusL, Matrix.mul_apply, Fin.sum_univ_four,
    A0, A1, A2, B0, B1, B2, KAL, KBL, KAR, KBR, Matrix.one_apply]) <;>
  (try field_simp) <;> (try ring_nf) <;> (try simp)))

/-- **(i) on the weight spaces.** For every element of `L`, the orientation sum with the capture
is the `(3)`-entry times the capture's own orientation sum. -/
theorem L_factorises (q : R) (hq : q ≠ 0) {v : Fin 4 → Matrix (Fin 4) (Fin 4) R} (hv : v ∈ L q) :
    FplusL (v 1 * KBL q) + FminusL (v 0 * KAL q)
      = v 0 3 3 * (-((q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6) := by
  induction hv using Submodule.span_induction with
  | mem x hx => obtain ⟨k, rfl⟩ := hx; basisTac
  | zero => simp [FplusL, FminusL]
  | add x y _ _ hx hy =>
    simp only [FplusL, FminusL, Pi.add_apply, Matrix.add_mul, Matrix.add_apply] at hx hy ⊢
    linear_combination hx + hy
  | smul a x _ hx =>
    simp only [FplusL, FminusL, Pi.smul_apply, Matrix.smul_mul, Matrix.smul_apply,
      smul_eq_mul] at hx ⊢
    linear_combination a * hx

/-- **(ii) on the weight spaces**, first half (translated proton, reflected capture). -/
theorem L_mirror_plus (q : R) (hq : q ≠ 0) {v : Fin 4 → Matrix (Fin 4) (Fin 4) R} (hv : v ∈ L q) :
    (v 3 * KBR q) 0 0 + (v 3 * KBR q) 1 1 + (v 3 * KBR q) 2 2
      = (v 0 * KAL q) 0 0 + (v 0 * KAL q) 1 1 + (v 0 * KAL q) 2 2 := by
  induction hv using Submodule.span_induction with
  | mem x hx => obtain ⟨k, rfl⟩ := hx; basisTac
  | zero => simp
  | add x y _ _ hx hy =>
    simp only [Pi.add_apply, Matrix.add_mul, Matrix.add_apply] at hx hy ⊢
    linear_combination hx + hy
  | smul a x _ hx =>
    simp only [Pi.smul_apply, Matrix.smul_mul, Matrix.smul_apply, smul_eq_mul] at hx ⊢
    linear_combination a * hx

/-- **(ii) on the weight spaces**, second half. -/
theorem L_mirror_minus (q : R) (hq : q ≠ 0) {v : Fin 4 → Matrix (Fin 4) (Fin 4) R} (hv : v ∈ L q) :
    (v 2 * KAR q) 1 1 + (v 2 * KAR q) 2 2 + (v 2 * KAR q) 3 3
      = (v 1 * KBL q) 1 1 + (v 1 * KBL q) 2 2 + (v 1 * KBL q) 3 3 := by
  induction hv using Submodule.span_induction with
  | mem x hx => obtain ⟨k, rfl⟩ := hx; basisTac
  | zero => simp
  | add x y _ _ hx hy =>
    simp only [Pi.add_apply, Matrix.add_mul, Matrix.add_apply] at hx hy ⊢
    linear_combination hx + hy
  | smul a x _ hx =>
    simp only [Pi.smul_apply, Matrix.smul_mul, Matrix.smul_apply, smul_eq_mul] at hx ⊢
    linear_combination a * hx

/-! ### The sixteen-dimensional space -/

/-- A proton element on `(C²)^{⊗4}`, proton on strands `0–2`: `s_i ↦ σ_i`. -/
def evL16 (q : R) : Proton R →ₐ[R] Matrix (Fin 16) (Fin 16) R :=
  FreeAlgebra.lift R (fun i => gen16 q i.val)
/-- The translated proton, strands `1–3`: `s_i ↦ σ_{i+1}`. -/
def evR16 (q : R) : Proton R →ₐ[R] Matrix (Fin 16) (Fin 16) R :=
  FreeAlgebra.lift R (fun i => gen16 q (i.val + 1))

theorem emb_of {m : ℕ} (f : Proton R →ₐ[R] Matrix (Fin 16) (Fin 16) R)
    (g : Proton R →ₐ[R] Matrix (Fin 4) (Fin 4) R) (E : Matrix (Fin 16) (Fin 4) R)
    (h1 : ∀ i, f (FreeAlgebra.ι R i) * E = E * g (FreeAlgebra.ι R i)) (x : Proton R) :
    f x * E = E * g x := by
  refine FreeAlgebra.induction R (Fin 2) ?_ ?_ ?_ ?_ x
  · intro r; rw [AlgHom.commutes, AlgHom.commutes]
    simp [Algebra.algebraMap_eq_smul_one]
  · exact h1
  · intro a b ha hb; rw [map_mul, map_mul, Matrix.mul_assoc, hb, ← Matrix.mul_assoc, ha, Matrix.mul_assoc]
  · intro a b ha hb; rw [map_add, map_add, Matrix.add_mul, Matrix.mul_add, ha, hb]

/-- The `j`-th block of `evQ`, as an algebra map. -/
def evQj (q : R) (j : Fin 4) : Proton R →ₐ[R] Matrix (Fin 4) (Fin 4) R :=
  (Pi.evalAlgHom R (fun _ : Fin 4 => Matrix (Fin 4) (Fin 4) R) j).comp (evQ q)

theorem evQj_apply (q : R) (j : Fin 4) (x : Proton R) : evQj q j x = evQ q x j := rfl

theorem evQj_ι (q : R) (j : Fin 4) (i : Fin 2) : evQj q j (FreeAlgebra.ι R i) = genQ q i j := by
  simp [evQj, evQ, FreeAlgebra.lift_ι_apply]

theorem embLA (q : R) (x : Proton R) : evL16 q x * EA = EA * evQ q x 0 := by
  rw [← evQj_apply]; refine emb_of (m := 0) _ _ _ (fun i => ?_) x
  rw [evQj_ι]; simp only [evL16, FreeAlgebra.lift_ι_apply]
  fin_cases i
  · exact embA0 q
  · exact embA1 q
theorem embLB (q : R) (x : Proton R) : evL16 q x * EB = EB * evQ q x 1 := by
  rw [← evQj_apply]; refine emb_of (m := 0) _ _ _ (fun i => ?_) x
  rw [evQj_ι]; simp only [evL16, FreeAlgebra.lift_ι_apply]
  fin_cases i
  · exact embB0 q
  · exact embB1 q
theorem embRA (q : R) (x : Proton R) : evR16 q x * EA = EA * evQ q x 2 := by
  rw [← evQj_apply]; refine emb_of (m := 0) _ _ _ (fun i => ?_) x
  rw [evQj_ι]; simp only [evR16, FreeAlgebra.lift_ι_apply]
  fin_cases i
  · exact embA1 q
  · exact embA2 q
theorem embRB (q : R) (x : Proton R) : evR16 q x * EB = EB * evQ q x 3 := by
  rw [← evQj_apply]; refine emb_of (m := 0) _ _ _ (fun i => ?_) x
  rw [evQj_ι]; simp only [evR16, FreeAlgebra.lift_ι_apply]
  fin_cases i
  · exact embB1 q
  · exact embB2 q

theorem diagA_mul (N K : Matrix (Fin 16) (Fin 16) R) (X KX : Matrix (Fin 4) (Fin 4) R)
    (hN : N * EA = EA * X) (hK : K * EA = EA * KX) (k : Fin 4) :
    (N * K) (idxA k) (idxA k) = (X * KX) k k := by
  rw [← mul_EA (N * K) (idxA k) k, Matrix.mul_assoc, hK, ← Matrix.mul_assoc, hN, Matrix.mul_assoc,
    EA_mul_apply]
theorem diagB_mul (N K : Matrix (Fin 16) (Fin 16) R) (X KX : Matrix (Fin 4) (Fin 4) R)
    (hN : N * EB = EB * X) (hK : K * EB = EB * KX) (k : Fin 4) :
    (N * K) (idxB k) (idxB k) = (X * KX) k k := by
  rw [← mul_EB (N * K) (idxB k) k, Matrix.mul_assoc, hK, ← Matrix.mul_assoc, hN, Matrix.mul_assoc,
    EB_mul_apply]

/-- `K_L` on the full space. -/
def KL16 (q : R) : Matrix (Fin 16) (Fin 16) R := word16 q capKL
/-- `K_R` on the full space. -/
def KR16 (q : R) : Matrix (Fin 16) (Fin 16) R := word16 q capKR

/-- **The capture alone:** `S(K_L) = −h²[3]_q/q²`. -/
theorem capture_S (q : R) (hq : q ≠ 0) :
    Fplus16 (KL16 q) + Fminus16 (KL16 q) = -((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2 := by
  rw [KL16, F16_reduction q hq, wordA_capKL q hq, wordB_capKL q hq, SK_val q hq]
  field_simp

/-- **(i) The χ_(3) factorisation, for every proton element.**
`S(N_L(x)·K_L) = χ_(3)(x) · S(K_L)`. -/
theorem S_factorises (q : R) (hq : q ≠ 0) (x : Proton R) :
    Fplus16 (evL16 q x * KL16 q) + Fminus16 (evL16 q x * KL16 q)
      = chi3 q x * (Fplus16 (KL16 q) + Fminus16 (KL16 q)) := by
  have hK : Fplus16 (KL16 q) + Fminus16 (KL16 q) = FplusL (KBL q) + FminusL (KAL q) := by
    rw [KL16, F16_reduction q hq, wordA_capKL q hq, wordB_capKL q hq]
  rw [hK, SK_val q hq]
  have hKA : KL16 q * EA = EA * KAL q := by rw [KL16, embA_word q hq, wordA_capKL q hq]
  have hKB : KL16 q * EB = EB * KBL q := by rw [KL16, embB_word q hq, wordB_capKL q hq]
  have hI := L_factorises q hq (evQ_mem q hq x)
  rw [evQ_33] at hI
  have b1 := diagB_mul _ _ _ _ (embLB q x) hKB 3
  have b2 := diagB_mul _ _ _ _ (embLB q x) hKB 2
  have b3 := diagB_mul _ _ _ _ (embLB q x) hKB 1
  have a0 := diagA_mul _ _ _ _ (embLA q x) hKA 0
  have a1 := diagA_mul _ _ _ _ (embLA q x) hKA 1
  have a2 := diagA_mul _ _ _ _ (embLA q x) hKA 2
  simp only [idxA, idxB, Matrix.cons_val] at b1 b2 b3 a0 a1 a2
  simp only [FplusL, FminusL] at hI
  rw [Fplus16_eq, Fminus16_eq, b1, b2, b3, a0, a1, a2]
  linear_combination hI

/-- `F(O₊)` with the proton on strands `1–3` (electron strand `0`). -/
def protZerosR (s : Fin 16) : ℕ :=
  ((List.range' 1 3).filter (fun j => !s.val.testBit j)).length
def rTab : Fin 16 → ℕ := ![3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0, 0]
theorem zerosR_eq : ∀ s, protZerosR s = rTab s := by decide
def FplusR16 (W : Matrix (Fin 16) (Fin 16) R) : R :=
  ∑ s, if protZerosR s = 2 then (((zerosBelow 4 s : ℕ) : R) - 2) * W s s else 0
def FminusR16 (W : Matrix (Fin 16) (Fin 16) R) : R :=
  ∑ s, if protZerosR s = 1 then (((zerosBelow 4 s : ℕ) : R) - 2) * W s s else 0
theorem FplusR16_eq (W : Matrix (Fin 16) (Fin 16) R) : FplusR16 W = W 2 2 + W 4 4 + W 8 8 := by
  simp only [FplusR16, zeros4_eq, zerosR_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, rTab, Fin.succ]
  norm_num; ring
theorem FminusR16_eq (W : Matrix (Fin 16) (Fin 16) R) :
    FminusR16 W = -(W 7 7 + W 11 11 + W 13 13) := by
  simp only [FminusR16, zeros4_eq, zerosR_eq, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp [zTab, rTab, Fin.succ]
  norm_num; ring

/-- **(ii) Mirror, first half, for every proton element:** `O₊(right) = −O₋(left)`, with the
proton block translated (`s_i ↦ σ_{i+1}`) and the capture reflected. -/
theorem mirror_plus (q : R) (hq : q ≠ 0) (x : Proton R) :
    FplusR16 (evR16 q x * KR16 q) = -Fminus16 (evL16 q x * KL16 q) := by
  have hKA : KL16 q * EA = EA * KAL q := by rw [KL16, embA_word q hq, wordA_capKL q hq]
  have hKB : KR16 q * EB = EB * KBR q := by rw [KR16, embB_word q hq, wordB_capKR q hq]
  have hI := L_mirror_plus q hq (evQ_mem q hq x)
  have b0 := diagB_mul _ _ _ _ (embRB q x) hKB 0
  have b1 := diagB_mul _ _ _ _ (embRB q x) hKB 1
  have b2 := diagB_mul _ _ _ _ (embRB q x) hKB 2
  have a0 := diagA_mul _ _ _ _ (embLA q x) hKA 0
  have a1 := diagA_mul _ _ _ _ (embLA q x) hKA 1
  have a2 := diagA_mul _ _ _ _ (embLA q x) hKA 2
  simp only [idxA, idxB, Matrix.cons_val] at b0 b1 b2 a0 a1 a2
  rw [FplusR16_eq, Fminus16_eq, b0, b1, b2, a0, a1, a2]
  linear_combination hI

/-- **(ii) Mirror, second half:** `O₋(right) = −O₊(left)`. -/
theorem mirror_minus (q : R) (hq : q ≠ 0) (x : Proton R) :
    FminusR16 (evR16 q x * KR16 q) = -Fplus16 (evL16 q x * KL16 q) := by
  have hKA : KR16 q * EA = EA * KAR q := by rw [KR16, embA_word q hq, wordA_capKR q hq]
  have hKB : KL16 q * EB = EB * KBL q := by rw [KL16, embB_word q hq, wordB_capKL q hq]
  have hI := L_mirror_minus q hq (evQ_mem q hq x)
  have a1 := diagA_mul _ _ _ _ (embRA q x) hKA 1
  have a2 := diagA_mul _ _ _ _ (embRA q x) hKA 2
  have a3 := diagA_mul _ _ _ _ (embRA q x) hKA 3
  have b1 := diagB_mul _ _ _ _ (embLB q x) hKB 1
  have b2 := diagB_mul _ _ _ _ (embLB q x) hKB 2
  have b3 := diagB_mul _ _ _ _ (embLB q x) hKB 3
  simp only [idxA, idxB, Matrix.cons_val] at a1 a2 a3 b1 b2 b3
  rw [FminusR16_eq, Fplus16_eq, a1, a2, a3, b1, b2, b3]
  linear_combination -hI

/-! ### Photons and the four gluon arms -/

/-- The letter `s_i` in the free algebra. -/
def sF (i : Fin 2) : Proton R := FreeAlgebra.ι R i
/-- Its inverse image `s_i − h` (Hecke relation `σ⁻¹ = σ − h`). -/
def sFinv (q : R) (i : Fin 2) : Proton R := FreeAlgebra.ι R i - algebraMap R (Proton R) (q - q⁻¹)

/-- The photon (owner ruling): `γ(φ₀, φ₁, φ₀₁) = 1 + φ₀s₀ + φ₁s₁ + φ₀₁s₀s₁⁻¹`. -/
def photonF (q a b c : R) : Proton R := 1 + a • sF 0 + b • sF 1 + c • (sF 0 * sFinv q 1)

/-- The photon placed on strands `0–2` is `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` on `(C²)^{⊗4}`. -/
theorem evL16_photon (q a b c : R) :
    evL16 q (photonF q a b c)
      = 1 + a • g16 q (0, false) + b • g16 q (1, false) + c • (g16 q (0, false) * g16 q (1, true)) := by
  simp [photonF, sF, sFinv, evL16, g16, Algebra.algebraMap_eq_smul_one]

/-- The translated photon, strands `1–3`: `1 + φ₀σ₁ + φ₁σ₂ + φ₀₁σ₁σ₂⁻¹`. -/
theorem evR16_photon (q a b c : R) :
    evR16 q (photonF q a b c)
      = 1 + a • g16 q (1, false) + b • g16 q (2, false) + c • (g16 q (1, false) * g16 q (2, true)) := by
  simp [photonF, sF, sFinv, evR16, g16, Algebra.algebraMap_eq_smul_one]

theorem chi3_photon (q : R) (hq : q ≠ 0) (a b c : R) :
    chi3 q (photonF q a b c) = 1 + q * a + q * b + c := by
  simp [photonF, sF, sFinv, chi3]; field_simp

/-- Gluon arm `V = s₀s₁⁻¹`. -/
def gluonV (q : R) : Proton R := sF 0 * sFinv q 1
/-- Gluon arm `s₁`. -/
def gluonS1 : Proton R := sF 1
/-- Gluon arm `s₁s₀`. -/
def gluonS1S0 : Proton R := sF 1 * sF 0

theorem chi3_gluonV (q : R) (hq : q ≠ 0) : chi3 q (gluonV q) = 1 := by
  simp [gluonV, sF, sFinv, chi3]; field_simp
theorem chi3_gluonS1 (q : R) : chi3 q (gluonS1 : Proton R) = q := by simp [gluonS1, sF, chi3]
theorem chi3_gluonS1S0 (q : R) : chi3 q (gluonS1S0 : Proton R) = q ^ 2 := by
  simp [gluonS1S0, sF, chi3]; ring

/-- **(i) for a general γγ collision and any gluon element `g`.** -/
theorem S_photon_pair (q : R) (hq : q ≠ 0) (a b c a' b' c' : R) (g : Proton R) :
    let W := evL16 q (photonF q a b c * photonF q a' b' c' * g) * KL16 q
    Fplus16 W + Fminus16 W
      = (1 + q * a + q * b + c) * (1 + q * a' + q * b' + c') * chi3 q g
        * (-((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2) := by
  intro W
  rw [S_factorises q hq, capture_S q hq, map_mul, map_mul, chi3_photon q hq, chi3_photon q hq]

theorem S_arm_1 (q : R) (hq : q ≠ 0) (a b c a' b' c' : R) :
    let W := evL16 q (photonF q a b c * photonF q a' b' c') * KL16 q
    Fplus16 W + Fminus16 W = (1 + q * a + q * b + c) * (1 + q * a' + q * b' + c')
        * (-((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2) := by
  intro W
  have := S_photon_pair q hq a b c a' b' c' 1
  simp only [mul_one, map_one] at this
  exact this

theorem S_arm_V (q : R) (hq : q ≠ 0) (a b c a' b' c' : R) :
    let W := evL16 q (photonF q a b c * photonF q a' b' c' * gluonV q) * KL16 q
    Fplus16 W + Fminus16 W = (1 + q * a + q * b + c) * (1 + q * a' + q * b' + c')
        * (-((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2) := by
  intro W
  rw [S_photon_pair q hq, chi3_gluonV q hq, mul_one]

theorem S_arm_S1 (q : R) (hq : q ≠ 0) (a b c a' b' c' : R) :
    let W := evL16 q (photonF q a b c * photonF q a' b' c' * gluonS1) * KL16 q
    Fplus16 W + Fminus16 W = (1 + q * a + q * b + c) * (1 + q * a' + q * b' + c') * q
        * (-((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2) := by
  intro W
  rw [S_photon_pair q hq, chi3_gluonS1]

theorem S_arm_S1S0 (q : R) (hq : q ≠ 0) (a b c a' b' c' : R) :
    let W := evL16 q (photonF q a b c * photonF q a' b' c' * gluonS1S0) * KL16 q
    Fplus16 W + Fminus16 W = (1 + q * a + q * b + c) * (1 + q * a' + q * b' + c') * q ^ 2
        * (-((q - q⁻¹) ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2)) / q ^ 2) := by
  intro W
  rw [S_photon_pair q hq, chi3_gluonS1S0]

/-- At the derived γγ weights `φ₀₁ = qh`, `ψ₀₁ = −q⁻¹h` the photon factor is `1`, as for `V³`. -/
theorem chi3_derived_pair (q : R) (hq : q ≠ 0) :
    chi3 q (photonF q 0 0 (q * (q - q⁻¹)) * photonF q 0 0 (-(q - q⁻¹) / q)) = 1 := by
  rw [map_mul, chi3_photon q hq, chi3_photon q hq]; field_simp; ring

end QOU.BraidsAndKnots.HydrogenCaptureFactorisation
