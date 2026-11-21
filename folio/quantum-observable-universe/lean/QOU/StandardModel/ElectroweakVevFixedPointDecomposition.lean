import Mathlib.Tactic
import QOU.Conjectures.WeakSpectralCompleteness
import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.Archimedean.BringSchwingerNormalizationDerivation

/-!
# QOU.StandardModel.ElectroweakVevFixedPointDecomposition — what the electroweak vev
# fixed point does and does not derive

`QOU.StandardModel.ElectroweakBringSchwingerBridge` carries the formula

  `N_v = 1/α_v = q·([2]_q/2)·[4]_q[6]_q[8]_q + 1/π − α_v·H·(1 − ℏ_q²·α_v)`,
  `H = [2]_q/(8π)`, `ℏ_q = 1 − q⁻¹`,

as the conjecture class `ElectroweakVevFixedPointClass`. This module takes the
formula apart and records, piece by piece, what follows from proved corpus
results and what is a separate hypothesis. Audit:
`docs/audits/2026-11-20-ew-vev-fixed-point-derivation.md`.

## Results

1. **Carrier product (proved, generic `CommRing`).** The leading coefficients
   `a_n` of the two-eigenvalue reduction `σⁿ = a_n σ + b_n`
   (`QOU.Conjectures.heckeCoeff`) on the three electroweak carriers
   `σ₁⁴, σ₃⁶, σ₅⁸` satisfy
   `a₄ a₆ a₈ · (q + q⁻¹)³ = (q⁴ − q⁻⁴)(q⁶ − q⁻⁶)(q⁸ − q⁻⁸)`
   (`carrier_coeff_product`), i.e. `a₄a₆a₈ = (h/[2]_q)³·[4]_q[6]_q[8]_q`
   over a field (`carrier_coeff_product_qInt`). So the factor `[4][6][8]` is the
   `σ₁σ₃σ₅`-coefficient of the carrier word up to the fixed scale `(h/[2]_q)³`.
   The prefactor `q·[2]_q/2` of the formula is **not** produced by this route.

2. **Zero-mode counting rule (proved no-go for a single rule).** The EM sector's
   zero mode `2/(3π)` is `b₁(Σ₄)/Area(Σ₄)` (surface genus). The EW sector's `1/π`
   is `2·Σ g(carrier)/Area(Σ₄)` (carrier Seifert genera). Applied across sectors,
   the carrier rule gives `4/(3π) ≠ 2/(3π)` for EM (`carrierRule_em_ne`) and the
   surface rule gives `2/(3π) ≠ 1/π` for EW (`surfaceRule_ew_ne`). No one of the
   two rules gives both values (`no_single_zero_mode_rule`).

3. **Loop sign is a binary datum (proved).** For the same `(T, G, q, c, α)` the
   `s = +1` and `s = −1` relations both hold only if `c·α = 1`
   (`loop_sign_both_imp`). The EM relation is `s = +1`; the EW relation is
   `s = −1`. No corpus result selects `s = −1` for the EW sector.

4. **Well-posedness of the fixed point (proved).** For the cubic shape
   `P(α) = c·H·α³ − H·α² + T·α − 1` with `T > 0`, `H ≥ 0`, `c ≥ 0`, `4H < T²`,
   there is exactly one root in `(0, 2/T)` (`ewShapeCubic_existsUnique_root`), and
   `ewFixedPointCubic` has this shape (`ewFixedPointCubic_eq_shape`). So once the
   relation is assumed, it pins `α_v` uniquely in that window.

5. **Decomposition of the conjecture (conditional).** `EwVevHypotheses` splits
   `ElectroweakVevFixedPointClass` into six named hypotheses: additive assembly,
   tree term, zero mode, loop sign, loop parameter, and the self-consistency
   `α_loop = 1/N_v`. `ewVevHypotheses_imp_class` derives the old class from them.
   `EwVevHypotheses` has no instance.
-/

namespace QOU.StandardModel.EwVevDecomposition

open QOU.Conjectures (HeckeScalars heckeCoeff heckeCoeff_closed)
open QOU.Archimedean (gaussBonnetArea firstBetti bringZeroModeValue)
open QOU.Archimedean.BringSchwingerNormalizationDerivation
  (habiroNorm IsUnifiedBringFixedPoint)

/-! ## Section 1: The carrier product `[4]_q[6]_q[8]_q` -/

section CarrierProduct

variable {R : Type*} [CommRing R]

/-- **Carrier product, numerator form.** For Hecke scalars `q·q⁻¹ = 1`, the leading
coefficients of `σ⁴, σ⁶, σ⁸` in the two-eigenvalue reduction satisfy
`a₄ a₆ a₈ (q + q⁻¹)³ = (q⁴ − q⁻⁴)(q⁶ − q⁻⁶)(q⁸ − q⁻⁸)`. -/
theorem carrier_coeff_product (h : HeckeScalars R) :
    (heckeCoeff h 4).1 * (heckeCoeff h 6).1 * (heckeCoeff h 8).1 * (h.q + h.qi) ^ 3 =
      (h.q ^ 4 - h.qi ^ 4) * (h.q ^ 6 - h.qi ^ 6) * (h.q ^ 8 - h.qi ^ 8) := by
  have e4 := (heckeCoeff_closed h 4).1
  have e6 := (heckeCoeff_closed h 6).1
  have e8 := (heckeCoeff_closed h 8).1
  have n4 : (-h.qi) ^ 4 = h.qi ^ 4 := by ring
  have n6 : (-h.qi) ^ 6 = h.qi ^ 6 := by ring
  have n8 : (-h.qi) ^ 8 = h.qi ^ 8 := by ring
  rw [n4] at e4
  rw [n6] at e6
  rw [n8] at e8
  calc
    (heckeCoeff h 4).1 * (heckeCoeff h 6).1 * (heckeCoeff h 8).1 * (h.q + h.qi) ^ 3
        = ((heckeCoeff h 4).1 * (h.q + h.qi)) * ((heckeCoeff h 6).1 * (h.q + h.qi)) *
            ((heckeCoeff h 8).1 * (h.q + h.qi)) := by ring
    _ = (h.q ^ 4 - h.qi ^ 4) * (h.q ^ 6 - h.qi ^ 6) * (h.q ^ 8 - h.qi ^ 8) := by
        rw [e4, e6, e8]

end CarrierProduct

section CarrierProductField

variable {K : Type*} [Field K]

/-- Balanced quantum integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)` written with an explicit
inverse `qi`, over a field. -/
def balQ (q qi : K) (n : ℕ) : K := (q ^ n - qi ^ n) / (q - qi)

/-- **Carrier product, quantum-integer form.** With `h = q − q⁻¹ ≠ 0`,
`a₄ a₆ a₈ · [2]_q³ = h³ · [4]_q [6]_q [8]_q`. -/
theorem carrier_coeff_product_qInt (hs : HeckeScalars K) (hh : hs.q - hs.qi ≠ 0) :
    (heckeCoeff hs 4).1 * (heckeCoeff hs 6).1 * (heckeCoeff hs 8).1 * (hs.q + hs.qi) ^ 3 =
      (hs.q - hs.qi) ^ 3 * (balQ hs.q hs.qi 4 * balQ hs.q hs.qi 6 * balQ hs.q hs.qi 8) := by
  rw [carrier_coeff_product hs]
  unfold balQ
  field_simp

end CarrierProductField

/-! ## Section 2: Zero-mode counting rules -/

/-- Seifert genus of the torus knot `T(p, r)` (`gcd(p, r) = 1`): `(p − 1)(r − 1)/2`. -/
def torusKnotSeifertGenus (p r : ℕ) : ℕ := (p - 1) * (r - 1) / 2

/-- The EM carriers `T(2,9)` and `T(3,5)` both have Seifert genus `4`. -/
theorem emCarrier_genera :
    torusKnotSeifertGenus 2 9 = 4 ∧ torusKnotSeifertGenus 3 5 = 4 := by decide

/-- Carrier-genus rule: `2 · (sum of carrier Seifert genera) / Area(Σ₄)`. This is the
rule that defines `ewBringZeroMode`. -/
noncomputable def carrierRuleZeroMode (G : ℝ) : ℝ := 2 * G / gaussBonnetArea 4

/-- Surface-genus rule: `b₁(Σ_g) / Area(Σ_g) = 2g / (4π(g − 1))`. This is the rule
that defines the EM value `bringZeroModeValue = 2/(3π)` at `g = 4`. -/
noncomputable def surfaceRuleZeroMode (g : ℝ) : ℝ := firstBetti g / gaussBonnetArea g

theorem carrierRule_ew : carrierRuleZeroMode (ewSeifertGenusSum : ℝ) = ewBringZeroMode := rfl

theorem surfaceRule_em : surfaceRuleZeroMode 4 = bringZeroModeValue := by
  unfold surfaceRuleZeroMode firstBetti gaussBonnetArea bringZeroModeValue
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- The carrier rule on the EM carriers `{T(2,9), T(3,5)}` gives `4/(3π)`. -/
theorem carrierRule_em :
    carrierRuleZeroMode ((torusKnotSeifertGenus 2 9 : ℝ) + torusKnotSeifertGenus 3 5) =
      4 / (3 * Real.pi) := by
  rw [emCarrier_genera.1, emCarrier_genera.2]
  unfold carrierRuleZeroMode gaussBonnetArea
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  push_cast
  field_simp
  ring

/-- The carrier rule does not give the EM zero mode `2/(3π)`. -/
theorem carrierRule_em_ne :
    carrierRuleZeroMode ((torusKnotSeifertGenus 2 9 : ℝ) + torusKnotSeifertGenus 3 5) ≠
      bringZeroModeValue := by
  rw [carrierRule_em]
  unfold bringZeroModeValue
  have hπ : 0 < Real.pi := Real.pi_pos
  intro h
  have h3 : (0 : ℝ) < 3 * Real.pi := by positivity
  rw [div_eq_div_iff h3.ne' h3.ne'] at h
  nlinarith

/-- The surface rule does not give the EW zero mode `1/π`. -/
theorem surfaceRule_ew_ne : surfaceRuleZeroMode 4 ≠ ewBringZeroMode := by
  rw [surfaceRule_em, ewBringZeroMode_eq_one_div_pi]
  unfold bringZeroModeValue
  have hπ : 0 < Real.pi := Real.pi_pos
  intro h
  have h3 : (0 : ℝ) < 3 * Real.pi := by positivity
  rw [div_eq_div_iff h3.ne' hπ.ne'] at h
  nlinarith

/-- **No single counting rule.** Neither the carrier-genus rule nor the surface-genus
rule reproduces both sector zero modes (`2/(3π)` for EM, `1/π` for EW). -/
theorem no_single_zero_mode_rule :
    carrierRuleZeroMode ((torusKnotSeifertGenus 2 9 : ℝ) + torusKnotSeifertGenus 3 5) ≠
        bringZeroModeValue ∧
      surfaceRuleZeroMode 4 ≠ ewBringZeroMode :=
  ⟨carrierRule_em_ne, surfaceRule_ew_ne⟩

/-! ## Section 3: The loop sign is a binary datum -/

/-- If the unified Bring fixed-point relation holds with both signs `s = −1` and
`s = +1` at the same data, with `α ≠ 0` and `H(q) ≠ 0`, then `c·α = 1`. So away from
`c·α = 1` the sign of the loop term is not fixed by the rest of the relation. -/
theorem loop_sign_both_imp (T G q c α : ℝ) (hα : α ≠ 0) (hH : habiroNorm q ≠ 0)
    (hm : IsUnifiedBringFixedPoint (-1) T G q c α)
    (hp : IsUnifiedBringFixedPoint 1 T G q c α) : c * α = 1 := by
  unfold IsUnifiedBringFixedPoint at hm hp
  have h0 : 2 * α * habiroNorm q * (1 - c * α) = 0 := by linear_combination hm - hp
  have h2 : (2 : ℝ) * α * habiroNorm q ≠ 0 := by
    have : (2 : ℝ) ≠ 0 := by norm_num
    exact mul_ne_zero (mul_ne_zero this hα) hH
  have h1 : 1 - c * α = 0 := by
    rcases mul_eq_zero.mp h0 with h | h
    · exact absurd h h2
    · exact h
  linarith

/-! ## Section 4: Well-posedness of the fixed point -/

/-- The cubic shape `P(α) = c·H·α³ − H·α² + T·α − 1`. -/
def ewShapeCubic (T H c α : ℝ) : ℝ := c * H * α ^ 3 - H * α ^ 2 + T * α - 1

/-- `ewFixedPointCubic` has the shape `ewShapeCubic` with `T = T_EW`, `H = H(q)`,
`c = ℏ_q²`. -/
theorem ewFixedPointCubic_eq_shape (q α : ℝ) :
    ewFixedPointCubic q α =
      ewShapeCubic (ewFixedPointConst q) (ewHabiroNorm q) ((ewHbarQ q) ^ 2) α := by
  unfold ewFixedPointCubic ewShapeCubic
  ring

/-- `P` is strictly increasing on `[0, 2/T]` when `T > 0`, `H ≥ 0`, `c ≥ 0`,
`4H < T²`. -/
theorem ewShapeCubic_strictMonoOn {T H c : ℝ} (hT : 0 < T) (hH : 0 ≤ H) (hc : 0 ≤ c)
    (hHT : 4 * H < T ^ 2) :
    StrictMonoOn (ewShapeCubic T H c) (Set.Icc 0 (2 / T)) := by
  intro a ha b hb hab
  have hab4 : a + b ≤ 4 / T := by
    have : (4 : ℝ) / T = 2 / T + 2 / T := by ring
    rw [this]; linarith [ha.2, hb.2]
  have h1 : H * (a + b) ≤ H * (4 / T) := mul_le_mul_of_nonneg_left hab4 hH
  have h2 : H * (4 / T) < T := by
    have e : H * (4 / T) = 4 * H / T := by ring
    rw [e, div_lt_iff₀ hT]
    nlinarith
  have h3 : 0 ≤ c * H * (b ^ 2 + a * b + a ^ 2) :=
    mul_nonneg (mul_nonneg hc hH)
      (by nlinarith [mul_nonneg ha.1 hb.1, sq_nonneg a, sq_nonneg b])
  have hK : 0 < c * H * (b ^ 2 + a * b + a ^ 2) - H * (a + b) + T := by linarith
  have hd : ewShapeCubic T H c b - ewShapeCubic T H c a =
      (b - a) * (c * H * (b ^ 2 + a * b + a ^ 2) - H * (a + b) + T) := by
    unfold ewShapeCubic; ring
  have : 0 < (b - a) * (c * H * (b ^ 2 + a * b + a ^ 2) - H * (a + b) + T) :=
    mul_pos (by linarith) hK
  linarith

/-- **Existence and uniqueness.** Under `T > 0`, `H ≥ 0`, `c ≥ 0`, `4H < T²`, the cubic
`P` has exactly one root in `(0, 2/T)`. -/
theorem ewShapeCubic_existsUnique_root {T H c : ℝ} (hT : 0 < T) (hH : 0 ≤ H) (hc : 0 ≤ c)
    (hHT : 4 * H < T ^ 2) :
    ∃! α : ℝ, α ∈ Set.Ioo 0 (2 / T) ∧ ewShapeCubic T H c α = 0 := by
  set t : ℝ := 2 / T with ht
  have htpos : 0 < t := by positivity
  have htT : t * T = 2 := by rw [ht]; field_simp
  have hHt : H * t ^ 2 < 1 := by
    have e : H * t ^ 2 * T ^ 2 = 4 * H := by
      have : H * t ^ 2 * T ^ 2 = H * (t * T) ^ 2 := by ring
      rw [this, htT]; ring
    by_contra hcon
    push_neg at hcon
    have hT2 : 0 < T ^ 2 := by positivity
    nlinarith
  have hP0 : ewShapeCubic T H c 0 = -1 := by unfold ewShapeCubic; ring
  have hPt : 0 < ewShapeCubic T H c t := by
    have hct : 0 ≤ c * H * t ^ 3 := by positivity
    have : ewShapeCubic T H c t = c * H * t ^ 3 - H * t ^ 2 + t * T - 1 := by
      unfold ewShapeCubic; ring
    rw [this, htT]
    linarith
  have hcont : ContinuousOn (ewShapeCubic T H c) (Set.Icc 0 t) := by
    have : Continuous (ewShapeCubic T H c) := by
      unfold ewShapeCubic; fun_prop
    exact this.continuousOn
  have hmem : (0 : ℝ) ∈ Set.Ioo (ewShapeCubic T H c 0) (ewShapeCubic T H c t) := by
    rw [hP0]; exact ⟨by norm_num, hPt⟩
  obtain ⟨α, hα, hPα⟩ := intermediate_value_Ioo htpos.le hcont hmem
  refine ⟨α, ⟨hα, hPα⟩, ?_⟩
  rintro β ⟨hβ, hPβ⟩
  have hmono := ewShapeCubic_strictMonoOn hT hH hc hHT
  exact hmono.injOn ⟨hβ.1.le, hβ.2.le⟩ ⟨hα.1.le, hα.2.le⟩ (hPβ.trans hPα.symm)

/-- **Conditional uniqueness of the EW vev root.** Under the conjecture class, with the
numerical side conditions `T_EW > 0` and `4H < T_EW²`, any `α_v < 2/T_EW` is the
unique root of `ewFixedPointCubic` in `(0, 2/T_EW)`. -/
theorem ew_vev_unique_in_window (q α_v : ℝ) [inst : ElectroweakVevFixedPointClass q α_v]
    (hT : 0 < ewFixedPointConst q) (hHT : 4 * ewHabiroNorm q < (ewFixedPointConst q) ^ 2)
    (hH : 0 ≤ ewHabiroNorm q) (hwin : α_v < 2 / ewFixedPointConst q) (β : ℝ)
    (hβ : β ∈ Set.Ioo 0 (2 / ewFixedPointConst q)) (hPβ : ewFixedPointCubic q β = 0) :
    β = α_v := by
  have hroot := (ew_vev_is_fixed_point_root q α_v).1
  rw [ewFixedPointCubic_eq_shape] at hroot hPβ
  obtain ⟨γ, _, huniq⟩ :=
    ewShapeCubic_existsUnique_root hT hH (sq_nonneg (ewHbarQ q)) hHT
  have e1 := huniq β ⟨hβ, hPβ⟩
  have e2 := huniq α_v ⟨⟨inst.alpha_v_pos, hwin⟩, hroot⟩
  rw [e1, e2]

/-! ## Section 5: Decomposition of `ElectroweakVevFixedPointClass` -/

/-- **Six named hypotheses (§3b-cond, NO instance).** Each field is one separable
claim. Tiers (audit doc): `assembly` and `self_consistency` are conjectural model
structure; `tree` is conjectural (the `[4][6][8]` factor is carrier-reachable by
`carrier_coeff_product_qInt`, the prefactor `q·[2]_q/2` is not); `zero_mode` is a
choice between counting rules (`no_single_zero_mode_rule`); `sign` and `c_loop` are
selections (`loop_sign_both_imp`; the corpus skein contraction
`hecke_skein_bar_contraction` gives `h²`, not `ℏ_q²`). -/
class EwVevHypotheses (q Nv treeTerm zeroMode s c αloop : ℝ) : Prop where
  /-- `N_v` is positive. -/
  Nv_pos : 0 < Nv
  /-- Additive assembly: tree + zero mode + one-loop term. -/
  assembly : Nv = treeTerm + zeroMode + s * αloop * ewHabiroNorm q * (1 - c * αloop)
  /-- Tree term identification. -/
  tree : treeTerm = ewDressedTreeComplexity q
  /-- Zero mode = carrier-genus rule. -/
  zero_mode : zeroMode = carrierRuleZeroMode (ewSeifertGenusSum : ℝ)
  /-- Loop sign `s = −1`. -/
  sign : s = -1
  /-- Loop deformation parameter `c = ℏ_q²`. -/
  c_loop : c = (ewHbarQ q) ^ 2
  /-- Self-consistency: the loop coupling is `1/N_v`. -/
  self_consistency : αloop * Nv = 1

/-- **The six hypotheses imply the original conjecture class.** -/
theorem ewVevHypotheses_imp_class (q Nv treeTerm zeroMode s c αloop : ℝ)
    [hyp : EwVevHypotheses q Nv treeTerm zeroMode s c αloop] :
    ElectroweakVevFixedPointClass q αloop := by
  have hNv := hyp.Nv_pos
  have hsc := hyp.self_consistency
  have hαpos : 0 < αloop := by
    by_contra hcon
    push_neg at hcon
    nlinarith
  have hα : αloop ≠ 0 := hαpos.ne'
  have hinv : 1 / αloop = Nv := by
    field_simp
    linarith
  refine ⟨hαpos, ?_⟩
  unfold IsElectroweakVevFixedPoint ewFixedPointConst
  rw [hinv, hyp.assembly, hyp.tree, hyp.zero_mode, carrierRule_ew, hyp.sign, hyp.c_loop]
  ring

end QOU.StandardModel.EwVevDecomposition
