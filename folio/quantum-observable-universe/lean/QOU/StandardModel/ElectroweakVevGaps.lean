import Mathlib.Tactic
import QOU.StandardModel.ElectroweakVevFixedPointDecomposition

/-!
# QOU.StandardModel.ElectroweakVevGaps — derivation attempts for the four open slots of the
# electroweak vev fixed point

`QOU.StandardModel.EwVevDecomposition.EwVevHypotheses` splits the electroweak vev fixed point

  `N_v = q·([2]_q/2)·[4]_q[6]_q[8]_q + 1/π − α·H·(1 − ℏ_q²·α)`,  `α = 1/N_v`,

into named hypotheses. This module attempts each open slot and records what follows.
Audit: `docs/audits/2026-11-20-ew-vev-gaps.md`; probe:
`computations/probes/ew_vev_gaps_probe.py`; beans `qou-rpt1`, `qou-myxi`.

## Results

1. **Tree prefactor, bar parity (proved, generic field).** The balanced quantum integer is
   bar-invariant (`qIntF_bar`), and the tree term satisfies `T(q⁻¹)·q² = T(q)`
   (`ewTreeF_bar`). So `T` is bar-invariant only if `q² = 1` or `T = 0`
   (`ewTreeF_bar_invariant_imp`). The factor `q` therefore cannot come from any expression
   in bar-invariant data (quantum integers, quantum dimensions): it needs a bar-breaking
   source. The EM tree `q[9][10]` carries the same factor (`emTreeF_bar`).

2. **Tree prefactor, dressing exponent (proved, ordered).** For `q > 1`, `[2]_q/2 > 1`
   (`dressing_gt_one`), so the family `T_k = q([2]/2)^k[4][6][8]` is strictly increasing in
   `k` (`treeK_strictMono`). The two candidate rules found force `k = 0` (the EM tree rule
   `q·∏[n_i]` applied uniformly) or `k = 3` (one ratio `[2]/2` per extra link component);
   the published value is `k = 1`. No rule forcing `k = 1` was found.

3. **Zero-mode counting rule (proved, reduction).** The rule
   `Z = n_carriers · g(Σ₄) / Area(Σ₄)` gives `2/(3π)` at the two EM carriers
   (`perCarrier_em`) and `1/π` at the three EW carriers (`perCarrier_ew`). It is the unique
   rule of the form `Z = Σ_i (a·g_i + b) / Area` (affine in the carrier Seifert genus) that
   gives both values (`genusAffine_unique`). It was found by solving against the two corpus
   values, so it shows the two values are mutually consistent under one rule; it does not
   derive either.

4. **Loop sign (proved arithmetic, reduction).** With the one-loop coefficient
   `b₀ = −(11/3)C_A + (2/3)ΣT(Weyl) + (1/3)ΣT(complex scalar)`, the SM `SU(2)_L` content
   gives `b₀ = −19/6` (`b0_su2_sm`), and any abelian group with a charged fermion gives
   `b₀ > 0` (`b0_abelian_pos`). The rule `s = −sgn b₀` gives `s = −1` for `SU(2)_L` and
   `s = +1` for an abelian group (`signRule_su2`, `signRule_abelian`). This reduces the sign to
   the hypothesis that the vev sector's loop is the `SU(2)_L` loop.

5. **Loop coupling (proved identity + incompatibility).** For a loop coupling `κ` not tied to
   `N_v`, `N(κ) − N(κ') = −H(κ − κ')(1 − c(κ + κ'))` (`loopShift_identity`), so the
   comparison constrains `κ` only through that difference. The `SU(2)_L` reading of item 4
   would put the gauge coupling `α₂ > 1/30` in the loop; the self-consistency
   `κ·N_v = 1` with `N_v > 100` forces `κ < 1/100`. The two cannot hold together
   (`su2_coupling_not_selfConsistent`).

6. **Reduced decomposition (conditional).** `EwVevReducedHypotheses` replaces the zero-mode
   and sign fields of `EwVevHypotheses` by the uniform per-carrier rule and the `b₀` sign
   rule plus a sector assignment, and makes the dressing exponent an explicit field.
   `ewVevReduced_imp_hypotheses` derives `EwVevHypotheses`. It has no instance.
-/

namespace QOU.StandardModel.EwVevGaps

open QOU.QInteger (qIntBal)
open QOU.Archimedean (gaussBonnetArea bringZeroModeValue)
open QOU.StandardModel.EwVevDecomposition
  (EwVevHypotheses carrierRuleZeroMode carrierRule_ew)

/-! ## Section 1: bar parity of the tree term -/

section BarParity

variable {K : Type*} [Field K]

/-- Balanced quantum integer over a field, `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
def qIntF (q : K) (n : ℕ) : K := (q ^ n - q⁻¹ ^ n) / (q - q⁻¹)

/-- `[n]_q` is invariant under the bar involution `q ↦ q⁻¹`. -/
theorem qIntF_bar (q : K) (n : ℕ) : qIntF q⁻¹ n = qIntF q n := by
  unfold qIntF
  rw [inv_inv]
  rw [show q⁻¹ ^ n - q ^ n = -(q ^ n - q⁻¹ ^ n) by ring,
    show q⁻¹ - q = -(q - q⁻¹) by ring, neg_div_neg_eq]

/-- The electroweak tree term `q·([2]_q/2)·[4]_q[6]_q[8]_q` over a field. -/
def ewTreeF (q : K) : K := q * (qIntF q 2 / 2) * qIntF q 4 * qIntF q 6 * qIntF q 8

/-- The EM tree term `q·[9]_q[10]_q` over a field. -/
def emTreeF (q : K) : K := q * qIntF q 9 * qIntF q 10

/-- **Bar ratio of the EW tree.** `T(q⁻¹)·q² = T(q)` for `q ≠ 0`. -/
theorem ewTreeF_bar (q : K) (hq : q ≠ 0) : ewTreeF q⁻¹ * q ^ 2 = ewTreeF q := by
  unfold ewTreeF
  rw [qIntF_bar, qIntF_bar, qIntF_bar, qIntF_bar]
  field_simp

/-- **Bar ratio of the EM tree.** `T_EM(q⁻¹)·q² = T_EM(q)` for `q ≠ 0`. -/
theorem emTreeF_bar (q : K) (hq : q ≠ 0) : emTreeF q⁻¹ * q ^ 2 = emTreeF q := by
  unfold emTreeF
  rw [qIntF_bar, qIntF_bar]
  field_simp

/-- **The tree term is not bar-invariant.** If `T(q⁻¹) = T(q) ≠ 0` then `q² = 1`. So for
`q² ≠ 1` the factor `q` cannot be produced by any expression in bar-invariant data. -/
theorem ewTreeF_bar_invariant_imp (q : K) (hq : q ≠ 0) (hT : ewTreeF q ≠ 0)
    (hbar : ewTreeF q⁻¹ = ewTreeF q) : q ^ 2 = 1 := by
  have h := ewTreeF_bar q hq
  rw [hbar] at h
  have h' : ewTreeF q * (q ^ 2 - 1) = 0 := by linear_combination h
  rcases mul_eq_zero.mp h' with h0 | h0
  · exact absurd h0 hT
  · linear_combination h0

end BarParity

/-! ## Section 2: the dressing exponent -/

/-- The tree family `T_k(q) = q·([2]_q/2)^k·[4]_q[6]_q[8]_q` on `ℝ`; `k = 1` is the
published tree (`treeK_one`). -/
noncomputable def treeK (q : ℝ) (k : ℕ) : ℝ := ewBareCrossingComplexity q * (qIntBal q 2 / 2) ^ k

theorem treeK_one (q : ℝ) : treeK q 1 = ewDressedTreeComplexity q := by
  unfold treeK ewDressedTreeComplexity
  rw [pow_one]

/-- For `q > 1`, `([2]_q/2) > 1`, written with `[2]_q = q + q⁻¹`. -/
theorem dressing_gt_one (q : ℝ) (hq : 1 < q) : 1 < (q + q⁻¹) / 2 := by
  have hq0 : 0 < q := by linarith
  have h : 2 < q + q⁻¹ := by
    have hinv : q⁻¹ = 1 / q := by rw [one_div]
    rw [hinv, ← sub_pos]
    have : q + 1 / q - 2 = (q - 1) ^ 2 / q := by field_simp; ring
    rw [this]
    exact div_pos (by nlinarith) hq0
  linarith

/-- **The exponent is not inert.** With `D = [2]_q/2 > 1` and a positive bare product `B`,
`k ↦ B·D^k` is strictly increasing; in particular `T_0 < T_1 < T_3`. -/
theorem treeK_strictMono_of (B D : ℝ) (hB : 0 < B) (hD : 1 < D) :
    StrictMono (fun k : ℕ => B * D ^ k) := by
  intro m n hmn
  exact mul_lt_mul_of_pos_left (pow_lt_pow_right₀ hD hmn) hB

theorem treeK_strictMono (q : ℝ) (hB : 0 < ewBareCrossingComplexity q)
    (hD : 1 < qIntBal q 2 / 2) : treeK q 0 < treeK q 1 ∧ treeK q 1 < treeK q 3 := by
  have hm := treeK_strictMono_of _ _ hB hD
  exact ⟨hm (by norm_num), hm (by norm_num)⟩

/-! ## Section 3: a uniform zero-mode counting rule -/

/-- Per-carrier rule: `Z = n · g / Area(Σ_g)` (each carrier contributes `g/Area`,
i.e. `dim H^{1,0}(Σ_g) / Area`). -/
noncomputable def perCarrierZeroMode (n g : ℝ) : ℝ := n * g / gaussBonnetArea g

/-- At the two EM carriers on `Σ₄` the per-carrier rule gives `2/(3π)`. -/
theorem perCarrier_em : perCarrierZeroMode 2 4 = bringZeroModeValue := by
  unfold perCarrierZeroMode gaussBonnetArea bringZeroModeValue
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- At the three EW carriers on `Σ₄` the per-carrier rule gives `1/π`. -/
theorem perCarrier_ew : perCarrierZeroMode 3 4 = ewBringZeroMode := by
  rw [ewBringZeroMode_eq_one_div_pi]
  unfold perCarrierZeroMode gaussBonnetArea
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- **Uniqueness among genus-affine rules.** Suppose each carrier of Seifert genus `g_i`
contributes `a·g_i + b` (then divided by the common area). The EM carriers have genera
`4, 4` and must total `8`; the EW carriers have genera `1, 2, 3` and must total `12`. Then
`a = 0` and `b = 4`: the contribution is independent of the carrier genus and equals
`g(Σ₄) = 4`. -/
theorem genusAffine_unique {K : Type*} [Field K] [CharZero K] (a b : K)
    (hem : (a * 4 + b) + (a * 4 + b) = 8)
    (hew : (a * 1 + b) + (a * 2 + b) + (a * 3 + b) = 12) : a = 0 ∧ b = 4 := by
  have h12 : (12 : K) * a = 0 := by linear_combination 3 * hem - 2 * hew
  have ha : a = 0 := by
    rcases mul_eq_zero.mp h12 with h | h
    · exact absurd h (by norm_num)
    · exact h
  refine ⟨ha, ?_⟩
  rw [ha] at hem
  have h2 : (2 : K) * (b - 4) = 0 := by linear_combination hem
  rcases mul_eq_zero.mp h2 with h | h
  · exact absurd h (by norm_num)
  · linear_combination h

/-! ## Section 4: the loop sign from the one-loop coefficient -/

section LoopSign

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- One-loop gauge coefficient `b₀ = −(11/3)C_A + (2/3)·ΣT(Weyl) + (1/3)·ΣT(complex scalar)`
(positive = screening). -/
def oneLoopB0 (CA weylT scalarT : K) : K :=
  -(11 / 3) * CA + (2 / 3) * weylT + (1 / 3) * scalarT

/-- **SM `SU(2)_L`.** `C_A = 2`; twelve left-handed Weyl doublets (three generations of one
lepton doublet and three coloured quark doublets) with `T = 1/2`; one complex Higgs doublet
with `T = 1/2`. Then `b₀ = −19/6`. -/
theorem b0_su2_sm : oneLoopB0 (2 : K) (12 * (1 / 2)) (1 / 2) = -(19 / 6) := by
  unfold oneLoopB0; ring

/-- **Abelian groups screen.** With `C_A = 0`, some charged Weyl fermion (`weylT > 0`) and
`scalarT ≥ 0`, `b₀ > 0`. -/
theorem b0_abelian_pos (weylT scalarT : K) (hw : 0 < weylT) (hs : 0 ≤ scalarT) :
    0 < oneLoopB0 (0 : K) weylT scalarT := by
  unfold oneLoopB0; nlinarith

/-- Sign rule: anti-screening (`b₀ < 0`) gives `s = −1`, otherwise `s = +1`. -/
def signRule (b : K) : K := if b < 0 then -1 else 1

theorem signRule_su2 : signRule (oneLoopB0 (2 : K) (12 * (1 / 2)) (1 / 2)) = -1 := by
  rw [b0_su2_sm]; unfold signRule; rw [if_pos (by norm_num)]

theorem signRule_abelian (weylT scalarT : K) (hw : 0 < weylT) (hs : 0 ≤ scalarT) :
    signRule (oneLoopB0 (0 : K) weylT scalarT) = 1 := by
  unfold signRule; rw [if_neg (not_lt.mpr (b0_abelian_pos weylT scalarT hw hs).le)]

end LoopSign

/-! ## Section 5: the loop coupling -/

/-- **Loop-shift identity (generic commutative ring).** For
`N(κ) = T − κ·H·(1 − c·κ)`, `N(κ) − N(κ') = −H·(κ − κ')·(1 − c·(κ + κ'))`. -/
theorem loopShift_identity {R : Type*} [CommRing R] (T H c κ κ' : R) :
    (T - κ * H * (1 - c * κ)) - (T - κ' * H * (1 - c * κ')) =
      -H * (κ - κ') * (1 - c * (κ + κ')) := by
  ring

/-- **The `SU(2)_L` reading and the self-consistency are incompatible.** If the loop coupling
is a gauge coupling `α₂ > 1/30` and also satisfies `α₂·N_v = 1` with `N_v > 100`, there is a
contradiction. (`1/30 < α₂` and `100 < N_v` are physical inputs: `α₂ ≈ 0.0339` from `G_F` and
`m_W`; `N_v = v/m_p ≈ 262.4`.) -/
theorem su2_coupling_not_selfConsistent (α₂ Nv : ℝ) (h2 : 1 / 30 < α₂) (hN : 100 < Nv)
    (hsc : α₂ * Nv = 1) : False := by
  nlinarith

/-! ## Section 6: reduced decomposition -/

/-- **Reduced hypotheses (§3b-cond, NO instance).** Compared with `EwVevHypotheses`:
the zero mode is the uniform per-carrier rule at three carriers (which also gives the EM
value, `perCarrier_em`); the sign is the `b₀` rule applied to the sector's group, with the
assignment of the `SU(2)_L` content made an explicit field; the dressing exponent `k` is an
explicit field (`k = 1` is a per-sector dispatch, no rule found). `tree`, `c_loop` and
`self_consistency` are unchanged. -/
class EwVevReducedHypotheses (q Nv treeTerm zeroMode s c αloop b0 : ℝ) (k : ℕ) : Prop where
  Nv_pos : 0 < Nv
  assembly : Nv = treeTerm + zeroMode + s * αloop * ewHabiroNorm q * (1 - c * αloop)
  /-- Tree term in the exponent family. -/
  tree : treeTerm = treeK q k
  /-- Dressing exponent: open dispatch (`qou-rpt1`). -/
  dressing_exponent : k = 1
  /-- Uniform per-carrier zero-mode rule, three carriers on `Σ₄`. -/
  zero_mode : zeroMode = perCarrierZeroMode 3 4
  /-- Sector assignment: the loop dressing the vev sector is the SM `SU(2)_L` loop. -/
  sector_group : b0 = oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2)
  /-- Sign rule `s = −sgn b₀`. -/
  sign_rule : s = signRule b0
  c_loop : c = (ewHbarQ q) ^ 2
  self_consistency : αloop * Nv = 1

/-- **The reduced hypotheses imply `EwVevHypotheses`.** -/
theorem ewVevReduced_imp_hypotheses (q Nv treeTerm zeroMode s c αloop b0 : ℝ) (k : ℕ)
    [hyp : EwVevReducedHypotheses q Nv treeTerm zeroMode s c αloop b0 k] :
    EwVevHypotheses q Nv treeTerm zeroMode s c αloop := by
  refine ⟨hyp.Nv_pos, hyp.assembly, ?_, ?_, ?_, hyp.c_loop, hyp.self_consistency⟩
  · rw [hyp.tree, hyp.dressing_exponent, treeK_one]
  · rw [hyp.zero_mode, perCarrier_ew, carrierRule_ew]
  · rw [hyp.sign_rule, hyp.sector_group, signRule_su2]

end QOU.StandardModel.EwVevGaps
