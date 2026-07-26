import QOU.Machinery.HeckeH4WedderburnCoord
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4WedderburnMulB — entry-by-entry verification of $A\cdot A^{-1} = 1$ (rows 8–15)

Wedderburn tranche **W3 (part 2 of 3)** (bean `qou-308a`): rows 8–15 of the
product identity `coordM q * coordMInv q = 1` — one public row lemma per
row, 24 scalar goals each, every goal closed by `linear_combination`
against `mul_inv_cancel₀` with sympy-derived, exactly-verified cofactors
(the `matinv_right` payloads of the design doc §4).

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every lemma is
discharged by computation — no axiom, no `sorry`, no conditional class, no
`native_decide`; the sympy cofactors are *payloads*, re-verified by Lean's
`linear_combination` kernel check.

Base ring (§7c): generic `[Field K]` — inverses are genuinely used; no
archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H4

set_option maxRecDepth 8000

variable {K : Type*} [Field K]

set_option maxHeartbeats 8000000 in
/-- Row 8 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row8 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 8 j = (1 : Matrix (Fin 24) (Fin 24) K) 8 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 8 0 = (1 : Matrix (Fin 24) (Fin 24) K) 8 0
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 1 = (1 : Matrix (Fin 24) (Fin 24) K) 8 1
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 2 = (1 : Matrix (Fin 24) (Fin 24) K) 8 2
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 3 = (1 : Matrix (Fin 24) (Fin 24) K) 8 3
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 4 = (1 : Matrix (Fin 24) (Fin 24) K) 8 4
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 5 = (1 : Matrix (Fin 24) (Fin 24) K) 8 5
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 6 = (1 : Matrix (Fin 24) (Fin 24) K) 8 6
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 7 = (1 : Matrix (Fin 24) (Fin 24) K) 8 7
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 8 = (1 : Matrix (Fin 24) (Fin 24) K) 8 8
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        ((q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 8 9 = (1 : Matrix (Fin 24) (Fin 24) K) 8 9
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 10 = (1 : Matrix (Fin 24) (Fin 24) K) 8 10
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 11 = (1 : Matrix (Fin 24) (Fin 24) K) 8 11
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 8 12 = (1 : Matrix (Fin 24) (Fin 24) K) 8 12
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 8 13 = (1 : Matrix (Fin 24) (Fin 24) K) 8 13
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 14 = (1 : Matrix (Fin 24) (Fin 24) K) 8 14
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 15 = (1 : Matrix (Fin 24) (Fin 24) K) 8 15
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 16 = (1 : Matrix (Fin 24) (Fin 24) K) 8 16
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 8 17 = (1 : Matrix (Fin 24) (Fin 24) K) 8 17
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 8 18 = (1 : Matrix (Fin 24) (Fin 24) K) 8 18
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 19 = (1 : Matrix (Fin 24) (Fin 24) K) 8 19
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 20 = (1 : Matrix (Fin 24) (Fin 24) K) 8 20
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 21 = (1 : Matrix (Fin 24) (Fin 24) K) 8 21
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 22 = (1 : Matrix (Fin 24) (Fin 24) K) 8 22
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 8 23 = (1 : Matrix (Fin 24) (Fin 24) K) 8 23
    rw [Matrix.one_apply_ne (by decide : (8 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow8, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 9 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row9 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 9 j = (1 : Matrix (Fin 24) (Fin 24) K) 9 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 9 0 = (1 : Matrix (Fin 24) (Fin 24) K) 9 0
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 1 = (1 : Matrix (Fin 24) (Fin 24) K) 9 1
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 2 = (1 : Matrix (Fin 24) (Fin 24) K) 9 2
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (-q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 9 3 = (1 : Matrix (Fin 24) (Fin 24) K) 9 3
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 4 = (1 : Matrix (Fin 24) (Fin 24) K) 9 4
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 5 = (1 : Matrix (Fin 24) (Fin 24) K) 9 5
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 6 = (1 : Matrix (Fin 24) (Fin 24) K) 9 6
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 7 = (1 : Matrix (Fin 24) (Fin 24) K) 9 7
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 8 = (1 : Matrix (Fin 24) (Fin 24) K) 9 8
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 9 9 = (1 : Matrix (Fin 24) (Fin 24) K) 9 9
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 9 10 = (1 : Matrix (Fin 24) (Fin 24) K) 9 10
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-2*q ^ 17*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 6*q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 15*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 9*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 13*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 13*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 11*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 3*q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 11*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 10*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 4*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 6*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 3*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
        + (-q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 9 11 = (1 : Matrix (Fin 24) (Fin 24) K) 9 11
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 12 = (1 : Matrix (Fin 24) (Fin 24) K) 9 12
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 13 = (1 : Matrix (Fin 24) (Fin 24) K) 9 13
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 14 = (1 : Matrix (Fin 24) (Fin 24) K) 9 14
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 15 = (1 : Matrix (Fin 24) (Fin 24) K) 9 15
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 9 16 = (1 : Matrix (Fin 24) (Fin 24) K) 9 16
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 17 = (1 : Matrix (Fin 24) (Fin 24) K) 9 17
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 18 = (1 : Matrix (Fin 24) (Fin 24) K) 9 18
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 19 = (1 : Matrix (Fin 24) (Fin 24) K) 9 19
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 20 = (1 : Matrix (Fin 24) (Fin 24) K) 9 20
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 21 = (1 : Matrix (Fin 24) (Fin 24) K) 9 21
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 9 22 = (1 : Matrix (Fin 24) (Fin 24) K) 9 22
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 9 23 = (1 : Matrix (Fin 24) (Fin 24) K) 9 23
    rw [Matrix.one_apply_ne (by decide : (9 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow9, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 10 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row10 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 10 j = (1 : Matrix (Fin 24) (Fin 24) K) 10 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 10 0 = (1 : Matrix (Fin 24) (Fin 24) K) 10 0
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 10 1 = (1 : Matrix (Fin 24) (Fin 24) K) 10 1
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 2 = (1 : Matrix (Fin 24) (Fin 24) K) 10 2
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 10 3 = (1 : Matrix (Fin 24) (Fin 24) K) 10 3
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 4 = (1 : Matrix (Fin 24) (Fin 24) K) 10 4
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 5 = (1 : Matrix (Fin 24) (Fin 24) K) 10 5
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 6 = (1 : Matrix (Fin 24) (Fin 24) K) 10 6
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 10 7 = (1 : Matrix (Fin 24) (Fin 24) K) 10 7
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 10 8 = (1 : Matrix (Fin 24) (Fin 24) K) 10 8
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 9 = (1 : Matrix (Fin 24) (Fin 24) K) 10 9
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 10 10 = (1 : Matrix (Fin 24) (Fin 24) K) 10 10
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        ((q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 18*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 16*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 16*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 7*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 13*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 14*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 10*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 4*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 4*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 1) * mul_inv_cancel₀ h2
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h3
        + (q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 10 11 = (1 : Matrix (Fin 24) (Fin 24) K) 10 11
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 12 = (1 : Matrix (Fin 24) (Fin 24) K) 10 12
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 13 = (1 : Matrix (Fin 24) (Fin 24) K) 10 13
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 14 = (1 : Matrix (Fin 24) (Fin 24) K) 10 14
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 15 = (1 : Matrix (Fin 24) (Fin 24) K) 10 15
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 10 16 = (1 : Matrix (Fin 24) (Fin 24) K) 10 16
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 17 = (1 : Matrix (Fin 24) (Fin 24) K) 10 17
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 18 = (1 : Matrix (Fin 24) (Fin 24) K) 10 18
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 19 = (1 : Matrix (Fin 24) (Fin 24) K) 10 19
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 10 20 = (1 : Matrix (Fin 24) (Fin 24) K) 10 20
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 21 = (1 : Matrix (Fin 24) (Fin 24) K) 10 21
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 22 = (1 : Matrix (Fin 24) (Fin 24) K) 10 22
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 10 23 = (1 : Matrix (Fin 24) (Fin 24) K) 10 23
    rw [Matrix.one_apply_ne (by decide : (10 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow10, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 11 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row11 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 11 j = (1 : Matrix (Fin 24) (Fin 24) K) 11 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 11 0 = (1 : Matrix (Fin 24) (Fin 24) K) 11 0
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 1 = (1 : Matrix (Fin 24) (Fin 24) K) 11 1
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 2 = (1 : Matrix (Fin 24) (Fin 24) K) 11 2
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 3 = (1 : Matrix (Fin 24) (Fin 24) K) 11 3
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 4 = (1 : Matrix (Fin 24) (Fin 24) K) 11 4
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 5 = (1 : Matrix (Fin 24) (Fin 24) K) 11 5
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 6 = (1 : Matrix (Fin 24) (Fin 24) K) 11 6
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 7 = (1 : Matrix (Fin 24) (Fin 24) K) 11 7
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 8 = (1 : Matrix (Fin 24) (Fin 24) K) 11 8
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 9 = (1 : Matrix (Fin 24) (Fin 24) K) 11 9
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 10 = (1 : Matrix (Fin 24) (Fin 24) K) 11 10
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 11 = (1 : Matrix (Fin 24) (Fin 24) K) 11 11
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 11 12 = (1 : Matrix (Fin 24) (Fin 24) K) 11 12
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 13 = (1 : Matrix (Fin 24) (Fin 24) K) 11 13
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 14 = (1 : Matrix (Fin 24) (Fin 24) K) 11 14
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 15 = (1 : Matrix (Fin 24) (Fin 24) K) 11 15
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 16 = (1 : Matrix (Fin 24) (Fin 24) K) 11 16
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 11 17 = (1 : Matrix (Fin 24) (Fin 24) K) 11 17
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 11 18 = (1 : Matrix (Fin 24) (Fin 24) K) 11 18
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 19 = (1 : Matrix (Fin 24) (Fin 24) K) 11 19
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 11 20 = (1 : Matrix (Fin 24) (Fin 24) K) 11 20
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 21 = (1 : Matrix (Fin 24) (Fin 24) K) 11 21
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 22 = (1 : Matrix (Fin 24) (Fin 24) K) 11 22
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 11 23 = (1 : Matrix (Fin 24) (Fin 24) K) 11 23
    rw [Matrix.one_apply_ne (by decide : (11 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow11, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 12 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row12 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 12 j = (1 : Matrix (Fin 24) (Fin 24) K) 12 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 12 0 = (1 : Matrix (Fin 24) (Fin 24) K) 12 0
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 1 = (1 : Matrix (Fin 24) (Fin 24) K) 12 1
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 2 = (1 : Matrix (Fin 24) (Fin 24) K) 12 2
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 3 = (1 : Matrix (Fin 24) (Fin 24) K) 12 3
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 4 = (1 : Matrix (Fin 24) (Fin 24) K) 12 4
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 5 = (1 : Matrix (Fin 24) (Fin 24) K) 12 5
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 6 = (1 : Matrix (Fin 24) (Fin 24) K) 12 6
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 7 = (1 : Matrix (Fin 24) (Fin 24) K) 12 7
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 8 = (1 : Matrix (Fin 24) (Fin 24) K) 12 8
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 12 9 = (1 : Matrix (Fin 24) (Fin 24) K) 12 9
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 10 = (1 : Matrix (Fin 24) (Fin 24) K) 12 10
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 11 = (1 : Matrix (Fin 24) (Fin 24) K) 12 11
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 12 = (1 : Matrix (Fin 24) (Fin 24) K) 12 12
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 12 13 = (1 : Matrix (Fin 24) (Fin 24) K) 12 13
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 13*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 12 14 = (1 : Matrix (Fin 24) (Fin 24) K) 12 14
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 15 = (1 : Matrix (Fin 24) (Fin 24) K) 12 15
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 16 = (1 : Matrix (Fin 24) (Fin 24) K) 12 16
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 17 = (1 : Matrix (Fin 24) (Fin 24) K) 12 17
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 18 = (1 : Matrix (Fin 24) (Fin 24) K) 12 18
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 11*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 12 19 = (1 : Matrix (Fin 24) (Fin 24) K) 12 19
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 20 = (1 : Matrix (Fin 24) (Fin 24) K) 12 20
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 21 = (1 : Matrix (Fin 24) (Fin 24) K) 12 21
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 12 22 = (1 : Matrix (Fin 24) (Fin 24) K) 12 22
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 12 23 = (1 : Matrix (Fin 24) (Fin 24) K) 12 23
    rw [Matrix.one_apply_ne (by decide : (12 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow12, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 13 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row13 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 13 j = (1 : Matrix (Fin 24) (Fin 24) K) 13 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 13 0 = (1 : Matrix (Fin 24) (Fin 24) K) 13 0
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 1 = (1 : Matrix (Fin 24) (Fin 24) K) 13 1
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 2 = (1 : Matrix (Fin 24) (Fin 24) K) 13 2
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 3 = (1 : Matrix (Fin 24) (Fin 24) K) 13 3
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 4 = (1 : Matrix (Fin 24) (Fin 24) K) 13 4
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 5 = (1 : Matrix (Fin 24) (Fin 24) K) 13 5
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 6 = (1 : Matrix (Fin 24) (Fin 24) K) 13 6
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 7 = (1 : Matrix (Fin 24) (Fin 24) K) 13 7
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 8 = (1 : Matrix (Fin 24) (Fin 24) K) 13 8
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 9 = (1 : Matrix (Fin 24) (Fin 24) K) 13 9
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 10 = (1 : Matrix (Fin 24) (Fin 24) K) 13 10
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 11 = (1 : Matrix (Fin 24) (Fin 24) K) 13 11
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 12 = (1 : Matrix (Fin 24) (Fin 24) K) 13 12
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 13 13 = (1 : Matrix (Fin 24) (Fin 24) K) 13 13
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 13 14 = (1 : Matrix (Fin 24) (Fin 24) K) 13 14
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 15 = (1 : Matrix (Fin 24) (Fin 24) K) 13 15
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 16 = (1 : Matrix (Fin 24) (Fin 24) K) 13 16
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 3*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 17 = (1 : Matrix (Fin 24) (Fin 24) K) 13 17
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 18 = (1 : Matrix (Fin 24) (Fin 24) K) 13 18
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 13 19 = (1 : Matrix (Fin 24) (Fin 24) K) 13 19
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 13 20 = (1 : Matrix (Fin 24) (Fin 24) K) 13 20
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 21 = (1 : Matrix (Fin 24) (Fin 24) K) 13 21
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 13 22 = (1 : Matrix (Fin 24) (Fin 24) K) 13 22
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 13 23 = (1 : Matrix (Fin 24) (Fin 24) K) 13 23
    rw [Matrix.one_apply_ne (by decide : (13 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow13, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 14 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row14 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 14 j = (1 : Matrix (Fin 24) (Fin 24) K) 14 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 14 0 = (1 : Matrix (Fin 24) (Fin 24) K) 14 0
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 1 = (1 : Matrix (Fin 24) (Fin 24) K) 14 1
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 2 = (1 : Matrix (Fin 24) (Fin 24) K) 14 2
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 3 = (1 : Matrix (Fin 24) (Fin 24) K) 14 3
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 4 = (1 : Matrix (Fin 24) (Fin 24) K) 14 4
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 5 = (1 : Matrix (Fin 24) (Fin 24) K) 14 5
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 6 = (1 : Matrix (Fin 24) (Fin 24) K) 14 6
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 7 = (1 : Matrix (Fin 24) (Fin 24) K) 14 7
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 8 = (1 : Matrix (Fin 24) (Fin 24) K) 14 8
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 9 = (1 : Matrix (Fin 24) (Fin 24) K) 14 9
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 10 = (1 : Matrix (Fin 24) (Fin 24) K) 14 10
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 11 = (1 : Matrix (Fin 24) (Fin 24) K) 14 11
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 12 = (1 : Matrix (Fin 24) (Fin 24) K) 14 12
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 13 = (1 : Matrix (Fin 24) (Fin 24) K) 14 13
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 14 = (1 : Matrix (Fin 24) (Fin 24) K) 14 14
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        ((q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 14 15 = (1 : Matrix (Fin 24) (Fin 24) K) 14 15
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 14 16 = (1 : Matrix (Fin 24) (Fin 24) K) 14 16
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 17 = (1 : Matrix (Fin 24) (Fin 24) K) 14 17
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 18 = (1 : Matrix (Fin 24) (Fin 24) K) 14 18
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 19 = (1 : Matrix (Fin 24) (Fin 24) K) 14 19
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 14 20 = (1 : Matrix (Fin 24) (Fin 24) K) 14 20
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 14 21 = (1 : Matrix (Fin 24) (Fin 24) K) 14 21
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 14 22 = (1 : Matrix (Fin 24) (Fin 24) K) 14 22
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 14 23 = (1 : Matrix (Fin 24) (Fin 24) K) 14 23
    rw [Matrix.one_apply_ne (by decide : (14 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow14, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2

set_option maxHeartbeats 8000000 in
/-- Row 15 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row15 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 15 j = (1 : Matrix (Fin 24) (Fin 24) K) 15 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 15 0 = (1 : Matrix (Fin 24) (Fin 24) K) 15 0
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 1 = (1 : Matrix (Fin 24) (Fin 24) K) 15 1
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 2 = (1 : Matrix (Fin 24) (Fin 24) K) 15 2
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 3 = (1 : Matrix (Fin 24) (Fin 24) K) 15 3
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 5*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 4 = (1 : Matrix (Fin 24) (Fin 24) K) 15 4
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 5 = (1 : Matrix (Fin 24) (Fin 24) K) 15 5
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 6 = (1 : Matrix (Fin 24) (Fin 24) K) 15 6
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 15 7 = (1 : Matrix (Fin 24) (Fin 24) K) 15 7
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 15 8 = (1 : Matrix (Fin 24) (Fin 24) K) 15 8
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 9 = (1 : Matrix (Fin 24) (Fin 24) K) 15 9
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 15 10 = (1 : Matrix (Fin 24) (Fin 24) K) 15 10
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 9*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 7*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 8*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 15 11 = (1 : Matrix (Fin 24) (Fin 24) K) 15 11
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 12 = (1 : Matrix (Fin 24) (Fin 24) K) 15 12
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 13 = (1 : Matrix (Fin 24) (Fin 24) K) 15 13
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 14 = (1 : Matrix (Fin 24) (Fin 24) K) 15 14
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 15 = (1 : Matrix (Fin 24) (Fin 24) K) 15 15
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (6*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 15 16 = (1 : Matrix (Fin 24) (Fin 24) K) 15 16
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 17 = (1 : Matrix (Fin 24) (Fin 24) K) 15 17
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 18 = (1 : Matrix (Fin 24) (Fin 24) K) 15 18
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 19 = (1 : Matrix (Fin 24) (Fin 24) K) 15 19
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 4*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 20 = (1 : Matrix (Fin 24) (Fin 24) K) 15 20
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 21 = (1 : Matrix (Fin 24) (Fin 24) K) 15 21
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 22 = (1 : Matrix (Fin 24) (Fin 24) K) 15 22
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 15 23 = (1 : Matrix (Fin 24) (Fin 24) K) 15 23
    rw [Matrix.one_apply_ne (by decide : (15 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow15, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

end QOU.Machinery.H4
