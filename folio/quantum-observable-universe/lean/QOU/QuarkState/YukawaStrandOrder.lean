import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# Strand order and Yukawa strengths of the right-handed singlet channels

Bean `qou-99qc`. Owner (Carl, 2026-11-21) adopted the right-handed singlet of #8694: the `−q⁻¹`
line `s = q·ud − du` of the Jimbo crossing on matter ⊗ Higgs (`RightHandedSingletChannel.lean`).
Owner asked to *"derive order + strengths"*. Pre-registered in
`computations/probes/qbeta_yukawa_strand_order/PREREGISTRATION.md` (commit `0629a1398d`).

Basis of `V ⊗ V`: `uu, ud, du, dd` = indices `0, 1, 2, 3`. `Rc` is the corpus crossing (the
matrix of `ChargedCurrentW.Rc`, #8638, and `RightHandedSingletChannel.Rc`, re-stated so this file
depends on Mathlib only). "Matter-left" means matter is the first tensor factor; "Higgs-left"
means the Higgs is. The vev slot of `Φ = (φ⁺, φ⁰)` is `d`, of `Φ̃ = (φ⁰*, φ⁻)` is `u`.

## Results (generic field `K`, §7c)

**Strand order — NOT forced.**
1. `Cc_Rc_Cc` : charge conjugation `C` (`u ↔ d` on both strands) conjugates the crossing to the
   strand-flipped crossing, `C·Ř·C = P·Ř·P`. So the singlet projector of the other order is
   `C·P_R·C` (`PRflip_eq_conj`), and the order exchanges the two vev entries
   (`PRflip_diag`): `q²/(q²+1) ↔ 1/(q²+1)`, which is also `q ↦ q⁻¹` (`entry_bar`).
2. `weak_kills_singlet_both` : the weak insertion `−h·P_L` annihilates the singlet in both
   orders. The owner-ruled `leftLine`/`rightLine` are defined on a letter, not on a choice of
   tensor factor, so the left-handed vertex does not select an order.
3. `ptrR_PR`, `ptrR_scalar_iff`, `ptrR_PR_K`, `ptrL_PR_Kinv` : the pivotal partial trace over the
   Higgs strand with weight `diag(a, b)` is `diag(b·q²/(q²+1), a/(q²+1))` on the matter strand; it
   is a scalar (a module map) iff `a = q²·b`, and with the bare `K = diag(q, q⁻¹)` it is
   `[2]⁻¹·1`. The mirror statement (left trace, `K⁻¹`) holds for the Higgs-left order. This
   reduction is order-free and flavour-blind, but it sums over BOTH Higgs slots: it does not use
   the vacuum. With the vacuum and the owner-ruled `tr e_H = 1` (vev weight `1`, #8694
   `vev_charge_zero_of_trace_one`) the reduction is the plain compression, which is
   order-dependent (item 1).

**Strengths — NOT derived.** `split` is the #8676 / #8694 form
`(y_d² − y_e²)·c_Φ̃ + (y_ν² − y_u²)·c_Φ`.
* `split_flavourBlind` (`y` depends only on the doublet slot, e.g. any rule through the
  generation label alone, the channel quantum dimension `1`, or the common `tr e_H = 1`): `0`.
* `split_typeOnly` (`y_u = y_d = y_q`, `y_ν = y_e = y_ℓ`): `(y_q² − y_ℓ²)(c_Φ̃ − c_Φ)`;
  `split_typeOnly_matterLeft` gives `−(y_q² − y_ℓ²)(q² − 1)/(q² + 1)`, and
  `split_typeOnly_order_sum` shows the Higgs-left value is its negative.
* `split_balanced` : with the order-free weights `c_Φ = c_Φ̃ = κ`, the split is
  `(y_d² − y_e² + y_ν² − y_u²)·κ`, `0` for type-only strengths.
* `split_order_difference` : matter-left minus Higgs-left is
  `(y_d² − y_e² − y_ν² + y_u²)·(1 − q²)/(q² + 1)`.

## What is NOT claimed

* No strand order is selected; no strength is derived; no MeV number. Which rule fixes the
  strengths, if any, is open. Nothing is compared with `Q_β`.
* That the partial pivotal trace is the right reduction for an energy. It is recorded because it
  is the only order-free reduction found, and it is flavour-blind.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VIII and §XIV (pivotal partial traces)
-/

namespace QOU.QuarkState.YukawaStrandOrder

open Matrix

variable {K : Type*} [Field K]

/-- The Jimbo crossing on `V ⊗ V`. -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- The swap of the two tensor factors. -/
def swap : Matrix (Fin 4) (Fin 4) K := !![1, 0, 0, 0; 0, 0, 1, 0; 0, 1, 0, 0; 0, 0, 0, 1]

/-- Charge conjugation `u ↔ d` on both strands. -/
def Cc : Matrix (Fin 4) (Fin 4) K := !![0, 0, 0, 1; 0, 0, 1, 0; 0, 1, 0, 0; 1, 0, 0, 0]

/-- Right-line projector `P_R = [2]⁻¹(q − Ř)` of the corpus crossing. -/
def PR (q : K) : Matrix (Fin 4) (Fin 4) K :=
  (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 4) (Fin 4) K) - Rc q)

/-- Right-line projector of the strand-flipped crossing `P·Ř·P`. -/
def PRflip (q : K) : Matrix (Fin 4) (Fin 4) K :=
  (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 4) (Fin 4) K) - swap * Rc q * swap)

/-- The singlet of the corpus crossing, `q·ud − du`. -/
def sing (q : K) : Fin 4 → K := ![0, q, -1, 0]

/-- The singlet of the flipped crossing, `q·du − ud`. -/
def singFlip (q : K) : Fin 4 → K := ![0, -1, q, 0]

local macro "mat4" : tactic =>
  `(tactic| (ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> (try field_simp) <;> (try ring)))

/-! ## 1. Charge conjugation relates the two orders -/

theorem Cc_sq : (Cc : Matrix (Fin 4) (Fin 4) K) * Cc = 1 := by
  simp only [Cc]; mat4

/-- **`C·Ř·C = P·Ř·P`.** -/
theorem Cc_Rc_Cc (q : K) : Cc * Rc q * Cc = swap * Rc q * swap := by
  simp only [Cc, Rc, swap]; mat4

/-- The other order's singlet projector is the charge conjugate of this one. -/
theorem PRflip_eq_conj (q : K) : PRflip q = Cc * PR q * Cc := by
  have h1 : (Cc : Matrix (Fin 4) (Fin 4) K) * Cc = 1 := Cc_sq
  rw [PRflip, PR, ← Cc_Rc_Cc, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_sub, Matrix.sub_mul,
    Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one, h1]

/-- The flipped crossing has the flipped singlet as its `−q⁻¹` line. -/
theorem flip_mulVec_singFlip (q : K) (hq : q ≠ 0) :
    (swap * Rc q * swap) *ᵥ singFlip q = (-q⁻¹) • singFlip q := by
  ext i; fin_cases i <;>
    simp [swap, Rc, singFlip, mulVec, dotProduct, Fin.sum_univ_four, Matrix.mul_apply] <;>
    field_simp <;> ring

/-- **The two orders swap the vev entries.** Corpus order: `ud ↦ q²/(q²+1)`, `du ↦ 1/(q²+1)`;
flipped order: the reverse. -/
theorem PRflip_diag (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    PR q 1 1 = q ^ 2 / (q ^ 2 + 1) ∧ PR q 2 2 = 1 / (q ^ 2 + 1) ∧
      PRflip q 1 1 = 1 / (q ^ 2 + 1) ∧ PRflip q 2 2 = q ^ 2 / (q ^ 2 + 1) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp [PR, PRflip, Rc, swap, Matrix.one_apply, Matrix.mul_apply, Fin.sum_univ_four] <;>
    field_simp <;> ring

/-- The swap of entries is `q ↦ q⁻¹`. -/
theorem entry_bar (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    q⁻¹ ^ 2 / (q⁻¹ ^ 2 + 1) = 1 / (q ^ 2 + 1) := by
  have h4 : q⁻¹ ^ 2 + 1 = (q ^ 2 + 1) / q ^ 2 := by field_simp; ring
  rw [h4, inv_pow, div_div_eq_mul_div]; field_simp

/-! ## 2. The left-handed vertex does not select an order -/

/-- **The weak insertion `−h·(1 − P_R)` kills the singlet in both orders.** -/
theorem weak_kills_singlet_both (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (-(q - q⁻¹)) • (1 - PR q) *ᵥ sing q = 0 ∧
      (-(q - q⁻¹)) • (1 - PRflip q) *ᵥ singFlip q = 0 := by
  constructor <;> (ext i; fin_cases i <;>
    simp [PR, PRflip, Rc, swap, sing, singFlip, mulVec, dotProduct, Fin.sum_univ_four,
      Matrix.one_apply, Matrix.sub_apply, Matrix.mul_apply] <;>
    field_simp <;> (try ring_nf) <;> simp)

/-! ## 3. Pivotal partial traces: the order-free reduction does not use the vacuum -/

/-- Right partial trace with weight `diag(a, b)` on the second (Higgs) strand:
`(id ⊗ tr)((1 ⊗ diag(a, b))·M)`. Index `(i, s) ↦ 2i + s`. -/
def ptrR (M : Matrix (Fin 4) (Fin 4) K) (a b : K) : Matrix (Fin 2) (Fin 2) K :=
  fun i j => a * M ⟨2 * i.val, by omega⟩ ⟨2 * j.val, by omega⟩ +
    b * M ⟨2 * i.val + 1, by omega⟩ ⟨2 * j.val + 1, by omega⟩

/-- Left partial trace with weight `diag(a, b)` on the first (Higgs) strand. Index
`(s, i) ↦ 2s + i`. -/
def ptrL (M : Matrix (Fin 4) (Fin 4) K) (a b : K) : Matrix (Fin 2) (Fin 2) K :=
  fun i j => a * M ⟨i.val, by omega⟩ ⟨j.val, by omega⟩ +
    b * M ⟨2 + i.val, by omega⟩ ⟨2 + j.val, by omega⟩

/-- **Matter-left reduction:** `diag(b·q²/(q²+1), a/(q²+1))`. -/
theorem ptrR_PR (q a b : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ptrR (PR q) a b = !![b * q ^ 2 / (q ^ 2 + 1), 0; 0, a / (q ^ 2 + 1)] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [ptrR, PR, Rc, Matrix.one_apply] <;> field_simp <;> ring

/-- **The reduction is a scalar (flavour-blind module map) iff `a = q²·b`.** -/
theorem ptrR_scalar_iff (q a b : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ptrR (PR q) a b 0 0 = ptrR (PR q) a b 1 1 ↔ a = q ^ 2 * b := by
  rw [ptrR_PR q a b hq h2]
  simp only [Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons]
  constructor
  · intro h; field_simp at h; linear_combination -h
  · intro h; rw [h]; field_simp

/-- **With the bare pivot `K = diag(q, q⁻¹)` the matter-left reduction is `[2]⁻¹·1`.** -/
theorem ptrR_PR_K (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ptrR (PR q) q q⁻¹ = (q + q⁻¹)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) K) := by
  rw [ptrR_PR q q q⁻¹ hq h2]
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.one_apply] <;> field_simp <;> ring

/-- **Higgs-left: the left trace with `K⁻¹ = diag(q⁻¹, q)` on the Higgs strand is `[2]⁻¹·1`.**
In this order the corpus crossing acts on Higgs ⊗ matter, so its projector is `PR q`. -/
theorem ptrL_PR_Kinv (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ptrL (PR q) q⁻¹ q = (q + q⁻¹)⁻¹ • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have hq2 : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [ptrL, PR, Rc, Matrix.one_apply] <;> field_simp <;> ring

/-- **The vacuum breaks the balance.** Restricting the right reduction to the vev slot with the
owner-ruled weight `1` (`tr e_H = 1`) returns the plain entries: `Φ` (vev `d`) gives the matter
`u` slot `q²/(q²+1)`, `Φ̃` (vev `u`) gives the matter `d` slot `1/(q²+1)`; they differ unless
`q² = 1`. -/
theorem vev_restricted_entries (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ptrR (PR q) 0 1 0 0 = q ^ 2 / (q ^ 2 + 1) ∧ ptrR (PR q) 1 0 1 1 = 1 / (q ^ 2 + 1) := by
  rw [ptrR_PR q 0 1 hq h2, ptrR_PR q 1 0 hq h2]
  simp

/-! ## 4. The split under each strength rule -/

/-- The split `(y_d² − y_e²)·c_Φ̃ + (y_ν² − y_u²)·c_Φ` (#8676 / #8694). -/
def split (yu yd yn ye cPhi cConj : K) : K :=
  yd ^ 2 * cConj + yn ^ 2 * cPhi - yu ^ 2 * cPhi - ye ^ 2 * cConj

/-- Matter-left weights `(c_Φ, c_Φ̃) = (q²/(q²+1), 1/(q²+1))`. -/
def splitML (q yu yd yn ye : K) : K := split yu yd yn ye (q ^ 2 / (q ^ 2 + 1)) (1 / (q ^ 2 + 1))

/-- Higgs-left weights `(c_Φ, c_Φ̃) = (1/(q²+1), q²/(q²+1))`. -/
def splitHL (q yu yd yn ye : K) : K := split yu yd yn ye (1 / (q ^ 2 + 1)) (q ^ 2 / (q ^ 2 + 1))

/-- **Flavour-blind strengths give `0`, in either order.** Strengths depending only on the
doublet slot (`y_u = y_ν = a`, `y_d = y_e = b`) cover every rule through the generation label,
the channel quantum dimension or the common `tr e_H = 1` normalisation (`a = b`). -/
theorem split_flavourBlind (a b cPhi cConj : K) : split a b a b cPhi cConj = 0 := by
  unfold split; ring

/-- **Type-only strengths:** `(y_q² − y_ℓ²)(c_Φ̃ − c_Φ)`. -/
theorem split_typeOnly (yq yl cPhi cConj : K) :
    split yq yq yl yl cPhi cConj = (yq ^ 2 - yl ^ 2) * (cConj - cPhi) := by
  unfold split; ring

theorem split_typeOnly_matterLeft (q yq yl : K) (h2 : q ^ 2 + 1 ≠ 0) :
    splitML q yq yq yl yl = -((yq ^ 2 - yl ^ 2) * ((q ^ 2 - 1) / (q ^ 2 + 1))) := by
  unfold splitML split; field_simp; ring

/-- **The type-only split is odd under the order swap.** -/
theorem split_typeOnly_order_sum (q yq yl : K) (h2 : q ^ 2 + 1 ≠ 0) :
    splitML q yq yq yl yl + splitHL q yq yq yl yl = 0 := by
  unfold splitML splitHL split; field_simp; ring

/-- **Order-free (balanced) weights:** `(y_d² − y_e² + y_ν² − y_u²)·κ`. -/
theorem split_balanced (yu yd yn ye κ : K) :
    split yu yd yn ye κ κ = (yd ^ 2 - ye ^ 2 + yn ^ 2 - yu ^ 2) * κ := by
  unfold split; ring

theorem split_balanced_typeOnly (yq yl κ : K) : split yq yq yl yl κ κ = 0 := by
  unfold split; ring

/-- **Matter-left minus Higgs-left.** -/
theorem split_order_difference (q yu yd yn ye : K) (h2 : q ^ 2 + 1 ≠ 0) :
    splitML q yu yd yn ye - splitHL q yu yd yn ye =
      (yd ^ 2 - ye ^ 2 - yn ^ 2 + yu ^ 2) * ((1 - q ^ 2) / (q ^ 2 + 1)) := by
  unfold splitML splitHL split; field_simp; ring

/-- At `q = 1` the two orders agree (both weights `½`). -/
theorem split_order_agree_at_one (yu yd yn ye : K) (h2 : (1 : K) ^ 2 + 1 ≠ 0) :
    splitML 1 yu yd yn ye = splitHL 1 yu yd yn ye := by
  unfold splitML splitHL split; ring

end QOU.QuarkState.YukawaStrandOrder
