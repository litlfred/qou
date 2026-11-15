/-
# The one-sided flavour vertex is a non-letter element, and it is (almost) forced

Bean `qou-hlx7` (epic `qou-qs0e`). Follows `HelicityCommonSource.lean` (bean `qou-hlx6`),
whose `no_one_sided_letter` proves that a flavour flip acting on ONE eigenline only is a
Hecke letter at no parameter (unless `q² = 1`). This file asks the next question: is
there a NON-letter element of the algebra that does it, and is it canonical?

Fix one letter `s` (`s² = h s + 1`, `h = q − q⁻¹`, `q ≠ 0`, `[2] := q + q⁻¹ ≠ 0`) in a
`K`-algebra `A`, with eigenprojectors `P₊` (eigenvalue `q`) and `P₋` (eigenvalue `−q⁻¹`).

## What this file proves

* `J := P₊ − P₋` satisfies `J² = 1` (`grading_sq`), commutes with `s` (`grading_comm`),
  and `[2]·J = s + s⁻¹` (`two_smul_grading`). It is bar-invariant: the orientation flip
  fixes it (`grading_flip`).
* The **L-only flip** `W_L := P₊ s⁻¹ P₊ + P₋ s P₋` equals `q⁻¹ J` (`oneSidedL_eq`); the
  **R-only flip** `W_R := P₊ s P₊ + P₋ s⁻¹ P₋` equals `q J` (`oneSidedR_eq`). Each acts as
  required on the two eigenlines (`oneSidedL_mul_Pp`, `oneSidedL_mul_Pm`, …), so by
  `no_one_sided_letter` neither is a letter (`oneSidedL_not_letter`).
* **Uniqueness** (`eq_of_eigen_action`): ANY `x ∈ A` with `x P₊ = a P₊`, `x P₋ = b P₋`
  equals `a P₊ + b P₋`. So once "which line, and to which eigenvalue" is fixed, the vertex
  is forced — but the choice of line is not: there are exactly two one-sided flips
  (L-only, R-only), they are mutually inverse (`oneSidedL_mul_oneSidedR`), and the bar
  involution exchanges them (`oneSidedL_flip`). That two-element family is the finding.
* **The corpus already carries `J`.** The mixed `ud` crossing letter `s − h/2` of the
  nucleon word equals `([2]/2)·J` (`ud_letter_eq_grading`). OBSERVATION, not an
  identification: nothing here says this letter IS a weak vertex.
* On the formal-`h` NF algebra (6a's `netFlavour`): `[2]J = σ + σ⁻¹` has net flavour
  `−1 = 0 + (−1)` (`netFlavour_grading`) — the grading reads as the SUM of the two
  flavours, not as either one.

Base ring (§7c): generic `[Field K] [Ring A] [Algebra K A]`; formal-`h` part over
generic `[CommRing R]`. No `ℝ`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.QuarkState.HelicityCommonSource

namespace QOU.QuarkState.OneSidedWeakVertex

open QOU.QuarkState.Helicity

section Abstract

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- The chirality grading `J = P₊ − P₋`. -/
noncomputable def grading (q : K) (s : A) : A := Pp q s - Pm q s

/-- The L-only flavour flip `P₊ s⁻¹ P₊ + P₋ s P₋`. -/
noncomputable def oneSidedL (q : K) (s : A) : A :=
  Pp q s * flip q s * Pp q s + Pm q s * s * Pm q s

/-- The R-only flavour flip `P₊ s P₊ + P₋ s⁻¹ P₋`. -/
noncomputable def oneSidedR (q : K) (s : A) : A :=
  Pp q s * s * Pp q s + Pm q s * flip q s * Pm q s

theorem Pm_mul_Pp (hq : q ≠ 0) (hs : IsLetter q s) : Pm q s * Pp q s = 0 := by
  have e := eigen_plus hq hs
  unfold Pm
  rw [smul_mul_assoc, sub_mul, e, smul_mul_assoc, one_mul, sub_self, smul_zero]

theorem Pm_idem (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    Pm q s * Pm q s = Pm q s := by
  have h1 : Pm q s * (Pp q s + Pm q s) = Pm q s := by rw [Pp_add_Pm hq2, mul_one]
  rwa [mul_add, Pm_mul_Pp hq hs, zero_add] at h1

theorem Pp_comm : s * Pp q s = Pp q s * s := by
  unfold Pp
  rw [mul_smul_comm, smul_mul_assoc, mul_add, add_mul, mul_smul_comm, smul_mul_assoc,
    mul_one, one_mul]

theorem Pm_comm : s * Pm q s = Pm q s * s := by
  unfold Pm
  rw [mul_smul_comm, smul_mul_assoc, mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc,
    mul_one, one_mul]

theorem Pp_eigen_right (hq : q ≠ 0) (hs : IsLetter q s) : Pp q s * s = q • Pp q s := by
  rw [← Pp_comm, eigen_plus hq hs]

theorem Pm_eigen_right (hq : q ≠ 0) (hs : IsLetter q s) : Pm q s * s = (-q⁻¹) • Pm q s := by
  rw [← Pm_comm, eigen_minus hq hs]

/-- **Uniqueness.** An element is determined by its action on the two eigenlines. -/
theorem eq_of_eigen_action (hq2 : q + q⁻¹ ≠ 0) {x : A} {a b : K}
    (ha : x * Pp q s = a • Pp q s) (hb : x * Pm q s = b • Pm q s) :
    x = a • Pp q s + b • Pm q s := by
  calc x = x * (Pp q s + Pm q s) := by rw [Pp_add_Pm hq2, mul_one]
    _ = a • Pp q s + b • Pm q s := by rw [mul_add, ha, hb]

theorem grading_sq (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    grading q s * grading q s = 1 := by
  unfold grading
  rw [sub_mul, mul_sub, mul_sub, Pp_idem hq hq2 hs, Pm_idem hq hq2 hs, Pp_mul_Pm hq hs,
    Pm_mul_Pp hq hs, sub_zero, zero_sub, sub_neg_eq_add, Pp_add_Pm hq2]

theorem grading_comm : s * grading q s = grading q s * s := by
  unfold grading; rw [mul_sub, sub_mul, Pp_comm, Pm_comm]

/-- `[2]·J = s + s⁻¹`. -/
theorem two_smul_grading (hq2 : q + q⁻¹ ≠ 0) :
    (q + q⁻¹) • grading q s = s + flip q s := by
  unfold grading Pp Pm Helicity.flip
  rw [← smul_sub, smul_smul, mul_inv_cancel₀ hq2, one_smul]
  module

/-- The grading is bar-invariant: the orientation flip fixes it. -/
theorem grading_flip : grading q⁻¹ (flip q s) = grading q s := by
  unfold grading; rw [flip_Pp, flip_Pm]

theorem grading_mul_Pp (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    grading q s * Pp q s = Pp q s := by
  unfold grading; rw [sub_mul, Pp_idem hq hq2 hs, Pm_mul_Pp hq hs, sub_zero]

theorem grading_mul_Pm (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    grading q s * Pm q s = -Pm q s := by
  unfold grading; rw [sub_mul, Pm_idem hq hq2 hs, Pp_mul_Pm hq hs, zero_sub]

theorem flip_mul_Pp_right (hq : q ≠ 0) (hs : IsLetter q s) :
    Pp q s * flip q s = q⁻¹ • Pp q s := by
  unfold Helicity.flip
  rw [mul_sub, Pp_eigen_right hq hs, mul_smul_comm, mul_one, ← sub_smul]
  congr 1; ring

theorem flip_mul_Pm_right (hq : q ≠ 0) (hs : IsLetter q s) :
    Pm q s * flip q s = (-q) • Pm q s := by
  unfold Helicity.flip
  rw [mul_sub, Pm_eigen_right hq hs, mul_smul_comm, mul_one, ← sub_smul]
  congr 1; ring

/-- **The L-only flip is `q⁻¹ J`.** -/
theorem oneSidedL_eq (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q s = q⁻¹ • grading q s := by
  unfold oneSidedL grading
  rw [flip_mul_Pp_right hq hs, smul_mul_assoc, Pp_idem hq hq2 hs, Pm_eigen_right hq hs,
    smul_mul_assoc, Pm_idem hq hq2 hs, smul_sub, neg_smul, sub_eq_add_neg]

/-- **The R-only flip is `q J`.** -/
theorem oneSidedR_eq (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedR q s = q • grading q s := by
  unfold oneSidedR grading
  rw [Pp_eigen_right hq hs, smul_mul_assoc, Pp_idem hq hq2 hs, flip_mul_Pm_right hq hs,
    smul_mul_assoc, Pm_idem hq hq2 hs, smul_sub, neg_smul, sub_eq_add_neg]

theorem oneSidedL_mul_Pp (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q s * Pp q s = q⁻¹ • Pp q s := by
  rw [oneSidedL_eq hq hq2 hs, smul_mul_assoc, grading_mul_Pp hq hq2 hs]

theorem oneSidedL_mul_Pm (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q s * Pm q s = (-q⁻¹) • Pm q s := by
  rw [oneSidedL_eq hq hq2 hs, smul_mul_assoc, grading_mul_Pm hq hq2 hs, smul_neg, neg_smul]

theorem oneSidedR_mul_Pp (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedR q s * Pp q s = q • Pp q s := by
  rw [oneSidedR_eq hq hq2 hs, smul_mul_assoc, grading_mul_Pp hq hq2 hs]

theorem oneSidedR_mul_Pm (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedR q s * Pm q s = (-q) • Pm q s := by
  rw [oneSidedR_eq hq hq2 hs, smul_mul_assoc, grading_mul_Pm hq hq2 hs, smul_neg, neg_smul]

/-- **The L-only flip is not a letter** at any parameter, unless `q² = 1`
(via `no_one_sided_letter`). -/
theorem oneSidedL_not_letter (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (hs : IsLetter q s) (hPp : Pp q s ≠ 0) (hPm : Pm q s ≠ 0) {p : K}
    (hx : IsLetter p (oneSidedL q s)) : q ^ 2 = 1 :=
  no_one_sided_letter h2 hq hPp hPm (oneSidedL_mul_Pp hq hq2 hs)
    (oneSidedL_mul_Pm hq hq2 hs) hx

/-- The two one-sided flips are mutually inverse. -/
theorem oneSidedL_mul_oneSidedR (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q s * oneSidedR q s = 1 := by
  rw [oneSidedL_eq hq hq2 hs, oneSidedR_eq hq hq2 hs, smul_mul_smul_comm,
    inv_mul_cancel₀ hq, one_smul, grading_sq hq hq2 hs]

/-- **The bar involution exchanges the two one-sided flips**: the L-only flip of the
flipped letter (at `q⁻¹`) is the R-only flip of the original. -/
theorem oneSidedL_flip (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    oneSidedL q⁻¹ (flip q s) = oneSidedR q s := by
  have hq' : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hq2' : q⁻¹ + q⁻¹⁻¹ ≠ 0 := by rwa [inv_inv, add_comm]
  rw [oneSidedL_eq hq' hq2' (flip_hecke hs), grading_flip, inv_inv, oneSidedR_eq hq hq2 hs]

/-- **The mixed `ud` crossing letter of the nucleon word is `([2]/2)·J`.** -/
theorem ud_letter_eq_grading (h2 : (2 : K) ≠ 0) (hq2 : q + q⁻¹ ≠ 0) :
    s - ((q - q⁻¹) / 2) • (1 : A) = ((q + q⁻¹) / 2) • grading q s := by
  rw [div_eq_mul_inv, div_eq_mul_inv, mul_comm (q + q⁻¹), ← smul_smul (2 : K)⁻¹,
    two_smul_grading hq2, mul_comm, ← smul_smul]
  unfold Helicity.flip
  have : (s : A) = (2 : K)⁻¹ • ((2 : K) • s) := by rw [smul_smul, inv_mul_cancel₀ h2, one_smul]
  conv_lhs => rw [this]
  rw [← smul_sub, two_smul]
  congr 1; abel

/-! ### The one-sided flip IS the letter corrected by the corpus skein difference

`HelicityCommonSource.skein_asym_eq`: `q s − q⁻¹ s⁻¹ = h·[2]·P₊`. So the L-only flip is the
letter minus the normalised skein difference, and the R-only flip is the letter minus the
normalised MIRROR difference. Which side is "one-sided" is exactly which crossing carries
the weight `q`: the L/R bit reduces to that weighting convention. -/

/-- `[2]·W_L = [2]·s − (q s − q⁻¹ s⁻¹)`. -/
theorem two_smul_oneSidedL_eq_skein (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    (q + q⁻¹) • oneSidedL q s = (q + q⁻¹) • s - (q • s - q⁻¹ • Helicity.flip q s) := by
  rw [oneSidedL_eq hq hq2 hs, smul_smul, mul_comm, ← smul_smul, two_smul_grading hq2]
  unfold Helicity.flip
  module

/-- `[2]·W_R = [2]·s − (q⁻¹ s − q s⁻¹)`: the mirror weighting gives the other side. -/
theorem two_smul_oneSidedR_eq_mirror (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) :
    (q + q⁻¹) • oneSidedR q s = (q + q⁻¹) • s - (q⁻¹ • s - q • Helicity.flip q s) := by
  rw [oneSidedR_eq hq hq2 hs, smul_smul, mul_comm, ← smul_smul, two_smul_grading hq2]
  unfold Helicity.flip
  module

end Abstract

/-! ## On 6a's formal-`h` NF algebra: net flavour of the grading -/

section Flavour

open Polynomial QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- `[2]·J = σ + σ⁻¹` reads net flavour `−1 = 0 + (−1)`: the SUM of the flavours. -/
theorem netFlavour_grading (g : Bool) :
    netFlavour (quarkLetter (R := R) g true + quarkLetter g false) = -1 := by
  rw [netFlavour_add, netFlavour_letter, netFlavour_letter]
  simp [flavourShift]

end Flavour

end QOU.QuarkState.OneSidedWeakVertex
