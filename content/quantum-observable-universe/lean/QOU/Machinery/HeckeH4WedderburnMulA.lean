import QOU.Machinery.HeckeH4WedderburnCoord
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4WedderburnMulA — entry-by-entry verification of $A\cdot A^{-1} = 1$ (rows 0–7)

Wedderburn tranche **W3 (part 2 of 3)** (bean `qou-308a`): rows 0–7 of the
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
/-- Row 0 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row0 (q : K) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 0 j = (1 : Matrix (Fin 24) (Fin 24) K) 0 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 0 0 = (1 : Matrix (Fin 24) (Fin 24) K) 0 0
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 0 1 = (1 : Matrix (Fin 24) (Fin 24) K) 0 1
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 2 = (1 : Matrix (Fin 24) (Fin 24) K) 0 2
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 0 3 = (1 : Matrix (Fin 24) (Fin 24) K) 0 3
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 4 = (1 : Matrix (Fin 24) (Fin 24) K) 0 4
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 5 = (1 : Matrix (Fin 24) (Fin 24) K) 0 5
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 6 = (1 : Matrix (Fin 24) (Fin 24) K) 0 6
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 0 7 = (1 : Matrix (Fin 24) (Fin 24) K) 0 7
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 0 8 = (1 : Matrix (Fin 24) (Fin 24) K) 0 8
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 9 = (1 : Matrix (Fin 24) (Fin 24) K) 0 9
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 0 10 = (1 : Matrix (Fin 24) (Fin 24) K) 0 10
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 0 11 = (1 : Matrix (Fin 24) (Fin 24) K) 0 11
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 12 = (1 : Matrix (Fin 24) (Fin 24) K) 0 12
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 13 = (1 : Matrix (Fin 24) (Fin 24) K) 0 13
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 14 = (1 : Matrix (Fin 24) (Fin 24) K) 0 14
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 15 = (1 : Matrix (Fin 24) (Fin 24) K) 0 15
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 16 = (1 : Matrix (Fin 24) (Fin 24) K) 0 16
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 17 = (1 : Matrix (Fin 24) (Fin 24) K) 0 17
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 18 = (1 : Matrix (Fin 24) (Fin 24) K) 0 18
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 19 = (1 : Matrix (Fin 24) (Fin 24) K) 0 19
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 20 = (1 : Matrix (Fin 24) (Fin 24) K) 0 20
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 21 = (1 : Matrix (Fin 24) (Fin 24) K) 0 21
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 22 = (1 : Matrix (Fin 24) (Fin 24) K) 0 22
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 0 23 = (1 : Matrix (Fin 24) (Fin 24) K) 0 23
    rw [Matrix.one_apply_ne (by decide : (0 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow0, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1

set_option maxHeartbeats 8000000 in
/-- Row 1 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row1 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 1 j = (1 : Matrix (Fin 24) (Fin 24) K) 1 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 1 0 = (1 : Matrix (Fin 24) (Fin 24) K) 1 0
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 1 = (1 : Matrix (Fin 24) (Fin 24) K) 1 1
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (3*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 5*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 6*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 5*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 1 2 = (1 : Matrix (Fin 24) (Fin 24) K) 1 2
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 3 = (1 : Matrix (Fin 24) (Fin 24) K) 1 3
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 4 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 4 = (1 : Matrix (Fin 24) (Fin 24) K) 1 4
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 5 = (1 : Matrix (Fin 24) (Fin 24) K) 1 5
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 6*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 1 6 = (1 : Matrix (Fin 24) (Fin 24) K) 1 6
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 7 = (1 : Matrix (Fin 24) (Fin 24) K) 1 7
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 5 + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 + 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 4 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 8 = (1 : Matrix (Fin 24) (Fin 24) K) 1 8
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 9 = (1 : Matrix (Fin 24) (Fin 24) K) 1 9
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 10 = (1 : Matrix (Fin 24) (Fin 24) K) 1 10
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 11 = (1 : Matrix (Fin 24) (Fin 24) K) 1 11
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 12 = (1 : Matrix (Fin 24) (Fin 24) K) 1 12
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 13 = (1 : Matrix (Fin 24) (Fin 24) K) 1 13
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 14 = (1 : Matrix (Fin 24) (Fin 24) K) 1 14
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 15 = (1 : Matrix (Fin 24) (Fin 24) K) 1 15
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 16 = (1 : Matrix (Fin 24) (Fin 24) K) 1 16
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 17 = (1 : Matrix (Fin 24) (Fin 24) K) 1 17
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 18 = (1 : Matrix (Fin 24) (Fin 24) K) 1 18
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 19 = (1 : Matrix (Fin 24) (Fin 24) K) 1 19
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 5 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 4 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 3 + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - (q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ h2
        + ((q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 1 20 = (1 : Matrix (Fin 24) (Fin 24) K) 1 20
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 4*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 + 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 4 + 4*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 5 + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 + 4*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 4 + 3*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 + 3*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 3 - 2*q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 1 21 = (1 : Matrix (Fin 24) (Fin 24) K) 1 21
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 1 22 = (1 : Matrix (Fin 24) (Fin 24) K) 1 22
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 4*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 1 23 = (1 : Matrix (Fin 24) (Fin 24) K) 1 23
    rw [Matrix.one_apply_ne (by decide : (1 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow1, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 5 - 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 5*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 4 - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 3 - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3

set_option maxHeartbeats 8000000 in
/-- Row 2 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row2 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 2 j = (1 : Matrix (Fin 24) (Fin 24) K) 2 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 2 0 = (1 : Matrix (Fin 24) (Fin 24) K) 2 0
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 2 1 = (1 : Matrix (Fin 24) (Fin 24) K) 2 1
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 2 = (1 : Matrix (Fin 24) (Fin 24) K) 2 2
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 2 3 = (1 : Matrix (Fin 24) (Fin 24) K) 2 3
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 4 = (1 : Matrix (Fin 24) (Fin 24) K) 2 4
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 5 = (1 : Matrix (Fin 24) (Fin 24) K) 2 5
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 6 = (1 : Matrix (Fin 24) (Fin 24) K) 2 6
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 2 7 = (1 : Matrix (Fin 24) (Fin 24) K) 2 7
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 2 8 = (1 : Matrix (Fin 24) (Fin 24) K) 2 8
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 9 = (1 : Matrix (Fin 24) (Fin 24) K) 2 9
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 2 10 = (1 : Matrix (Fin 24) (Fin 24) K) 2 10
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + ((q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 2 11 = (1 : Matrix (Fin 24) (Fin 24) K) 2 11
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 12 = (1 : Matrix (Fin 24) (Fin 24) K) 2 12
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 13 = (1 : Matrix (Fin 24) (Fin 24) K) 2 13
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 14 = (1 : Matrix (Fin 24) (Fin 24) K) 2 14
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 15 = (1 : Matrix (Fin 24) (Fin 24) K) 2 15
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 16 = (1 : Matrix (Fin 24) (Fin 24) K) 2 16
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 17 = (1 : Matrix (Fin 24) (Fin 24) K) 2 17
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 18 = (1 : Matrix (Fin 24) (Fin 24) K) 2 18
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 19 = (1 : Matrix (Fin 24) (Fin 24) K) 2 19
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 20 = (1 : Matrix (Fin 24) (Fin 24) K) 2 20
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 21 = (1 : Matrix (Fin 24) (Fin 24) K) 2 21
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 22 = (1 : Matrix (Fin 24) (Fin 24) K) 2 22
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 2 23 = (1 : Matrix (Fin 24) (Fin 24) K) 2 23
    rw [Matrix.one_apply_ne (by decide : (2 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow2, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 3 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row3 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 3 j = (1 : Matrix (Fin 24) (Fin 24) K) 3 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 3 0 = (1 : Matrix (Fin 24) (Fin 24) K) 3 0
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 1 = (1 : Matrix (Fin 24) (Fin 24) K) 3 1
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 2 = (1 : Matrix (Fin 24) (Fin 24) K) 3 2
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 3 = (1 : Matrix (Fin 24) (Fin 24) K) 3 3
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4 + q*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3 + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3 + (q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ + 1) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 3 4 = (1 : Matrix (Fin 24) (Fin 24) K) 3 4
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 5 = (1 : Matrix (Fin 24) (Fin 24) K) 3 5
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 6 = (1 : Matrix (Fin 24) (Fin 24) K) 3 6
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 7 = (1 : Matrix (Fin 24) (Fin 24) K) 3 7
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 8 = (1 : Matrix (Fin 24) (Fin 24) K) 3 8
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 9 = (1 : Matrix (Fin 24) (Fin 24) K) 3 9
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 10 = (1 : Matrix (Fin 24) (Fin 24) K) 3 10
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 11 = (1 : Matrix (Fin 24) (Fin 24) K) 3 11
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 12 = (1 : Matrix (Fin 24) (Fin 24) K) 3 12
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 13 = (1 : Matrix (Fin 24) (Fin 24) K) 3 13
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 14 = (1 : Matrix (Fin 24) (Fin 24) K) 3 14
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 15 = (1 : Matrix (Fin 24) (Fin 24) K) 3 15
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 16 = (1 : Matrix (Fin 24) (Fin 24) K) 3 16
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 17 = (1 : Matrix (Fin 24) (Fin 24) K) 3 17
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 18 = (1 : Matrix (Fin 24) (Fin 24) K) 3 18
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 19 = (1 : Matrix (Fin 24) (Fin 24) K) 3 19
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 20 = (1 : Matrix (Fin 24) (Fin 24) K) 3 20
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 21 = (1 : Matrix (Fin 24) (Fin 24) K) 3 21
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 22 = (1 : Matrix (Fin 24) (Fin 24) K) 3 22
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 3 23 = (1 : Matrix (Fin 24) (Fin 24) K) 3 23
    rw [Matrix.one_apply_ne (by decide : (3 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow3, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 4 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row4 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 4 j = (1 : Matrix (Fin 24) (Fin 24) K) 4 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 4 0 = (1 : Matrix (Fin 24) (Fin 24) K) 4 0
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 1 = (1 : Matrix (Fin 24) (Fin 24) K) 4 1
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 2 = (1 : Matrix (Fin 24) (Fin 24) K) 4 2
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 3 = (1 : Matrix (Fin 24) (Fin 24) K) 4 3
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 4 = (1 : Matrix (Fin 24) (Fin 24) K) 4 4
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + 5*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 7*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + 7*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 4 5 = (1 : Matrix (Fin 24) (Fin 24) K) 4 5
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 6 = (1 : Matrix (Fin 24) (Fin 24) K) 4 6
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 7 = (1 : Matrix (Fin 24) (Fin 24) K) 4 7
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 8 = (1 : Matrix (Fin 24) (Fin 24) K) 4 8
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 9 = (1 : Matrix (Fin 24) (Fin 24) K) 4 9
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 10 = (1 : Matrix (Fin 24) (Fin 24) K) 4 10
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 11 = (1 : Matrix (Fin 24) (Fin 24) K) 4 11
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 12 = (1 : Matrix (Fin 24) (Fin 24) K) 4 12
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 13 = (1 : Matrix (Fin 24) (Fin 24) K) 4 13
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 14 = (1 : Matrix (Fin 24) (Fin 24) K) 4 14
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 15 = (1 : Matrix (Fin 24) (Fin 24) K) 4 15
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 16 = (1 : Matrix (Fin 24) (Fin 24) K) 4 16
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 13*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 17 = (1 : Matrix (Fin 24) (Fin 24) K) 4 17
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 18 = (1 : Matrix (Fin 24) (Fin 24) K) 4 18
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 19 = (1 : Matrix (Fin 24) (Fin 24) K) 4 19
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 5*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 20 = (1 : Matrix (Fin 24) (Fin 24) K) 4 20
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 21 = (1 : Matrix (Fin 24) (Fin 24) K) 4 21
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 22 = (1 : Matrix (Fin 24) (Fin 24) K) 4 22
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 4 23 = (1 : Matrix (Fin 24) (Fin 24) K) 4 23
    rw [Matrix.one_apply_ne (by decide : (4 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow4, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 5 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row5 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 5 j = (1 : Matrix (Fin 24) (Fin 24) K) 5 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 5 0 = (1 : Matrix (Fin 24) (Fin 24) K) 5 0
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 1 = (1 : Matrix (Fin 24) (Fin 24) K) 5 1
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 5 2 = (1 : Matrix (Fin 24) (Fin 24) K) 5 2
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 3 = (1 : Matrix (Fin 24) (Fin 24) K) 5 3
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 4 = (1 : Matrix (Fin 24) (Fin 24) K) 5 4
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 5 = (1 : Matrix (Fin 24) (Fin 24) K) 5 5
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 5 6 = (1 : Matrix (Fin 24) (Fin 24) K) 5 6
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 7 = (1 : Matrix (Fin 24) (Fin 24) K) 5 7
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 8 = (1 : Matrix (Fin 24) (Fin 24) K) 5 8
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 9 = (1 : Matrix (Fin 24) (Fin 24) K) 5 9
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 10 = (1 : Matrix (Fin 24) (Fin 24) K) 5 10
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 11 = (1 : Matrix (Fin 24) (Fin 24) K) 5 11
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 12 = (1 : Matrix (Fin 24) (Fin 24) K) 5 12
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 13 = (1 : Matrix (Fin 24) (Fin 24) K) 5 13
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 14 = (1 : Matrix (Fin 24) (Fin 24) K) 5 14
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 15 = (1 : Matrix (Fin 24) (Fin 24) K) 5 15
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 16 = (1 : Matrix (Fin 24) (Fin 24) K) 5 16
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 17 = (1 : Matrix (Fin 24) (Fin 24) K) 5 17
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 18 = (1 : Matrix (Fin 24) (Fin 24) K) 5 18
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 19 = (1 : Matrix (Fin 24) (Fin 24) K) 5 19
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 5 20 = (1 : Matrix (Fin 24) (Fin 24) K) 5 20
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (-q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 5 21 = (1 : Matrix (Fin 24) (Fin 24) K) 5 21
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 5 22 = (1 : Matrix (Fin 24) (Fin 24) K) 5 22
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 5 23 = (1 : Matrix (Fin 24) (Fin 24) K) 5 23
    rw [Matrix.one_apply_ne (by decide : (5 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow5, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2

set_option maxHeartbeats 8000000 in
/-- Row 6 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row6 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 6 j = (1 : Matrix (Fin 24) (Fin 24) K) 6 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 6 0 = (1 : Matrix (Fin 24) (Fin 24) K) 6 0
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 6 1 = (1 : Matrix (Fin 24) (Fin 24) K) 6 1
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 2 = (1 : Matrix (Fin 24) (Fin 24) K) 6 2
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 6 3 = (1 : Matrix (Fin 24) (Fin 24) K) 6 3
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 4 = (1 : Matrix (Fin 24) (Fin 24) K) 6 4
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 5 = (1 : Matrix (Fin 24) (Fin 24) K) 6 5
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 6 = (1 : Matrix (Fin 24) (Fin 24) K) 6 6
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        ((q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 6 7 = (1 : Matrix (Fin 24) (Fin 24) K) 6 7
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 6 8 = (1 : Matrix (Fin 24) (Fin 24) K) 6 8
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 9 = (1 : Matrix (Fin 24) (Fin 24) K) 6 9
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 6 10 = (1 : Matrix (Fin 24) (Fin 24) K) 6 10
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 6 11 = (1 : Matrix (Fin 24) (Fin 24) K) 6 11
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 12 = (1 : Matrix (Fin 24) (Fin 24) K) 6 12
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 13 = (1 : Matrix (Fin 24) (Fin 24) K) 6 13
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 14 = (1 : Matrix (Fin 24) (Fin 24) K) 6 14
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 15 = (1 : Matrix (Fin 24) (Fin 24) K) 6 15
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 6 16 = (1 : Matrix (Fin 24) (Fin 24) K) 6 16
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 17 = (1 : Matrix (Fin 24) (Fin 24) K) 6 17
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 18 = (1 : Matrix (Fin 24) (Fin 24) K) 6 18
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 19 = (1 : Matrix (Fin 24) (Fin 24) K) 6 19
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 20 = (1 : Matrix (Fin 24) (Fin 24) K) 6 20
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 21 = (1 : Matrix (Fin 24) (Fin 24) K) 6 21
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 6 22 = (1 : Matrix (Fin 24) (Fin 24) K) 6 22
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 6 23 = (1 : Matrix (Fin 24) (Fin 24) K) 6 23
    rw [Matrix.one_apply_ne (by decide : (6 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow6, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 7 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row7 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 7 j = (1 : Matrix (Fin 24) (Fin 24) K) 7 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 7 0 = (1 : Matrix (Fin 24) (Fin 24) K) 7 0
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 7 1 = (1 : Matrix (Fin 24) (Fin 24) K) 7 1
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 2 = (1 : Matrix (Fin 24) (Fin 24) K) 7 2
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 7 3 = (1 : Matrix (Fin 24) (Fin 24) K) 7 3
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 4 = (1 : Matrix (Fin 24) (Fin 24) K) 7 4
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 5 = (1 : Matrix (Fin 24) (Fin 24) K) 7 5
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 6 = (1 : Matrix (Fin 24) (Fin 24) K) 7 6
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 7 7 = (1 : Matrix (Fin 24) (Fin 24) K) 7 7
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        ((q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ + 1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 7 8 = (1 : Matrix (Fin 24) (Fin 24) K) 7 8
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 9 = (1 : Matrix (Fin 24) (Fin 24) K) 7 9
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 7 10 = (1 : Matrix (Fin 24) (Fin 24) K) 7 10
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 7 11 = (1 : Matrix (Fin 24) (Fin 24) K) 7 11
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 12 = (1 : Matrix (Fin 24) (Fin 24) K) 7 12
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 7 13 = (1 : Matrix (Fin 24) (Fin 24) K) 7 13
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 14 = (1 : Matrix (Fin 24) (Fin 24) K) 7 14
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 15 = (1 : Matrix (Fin 24) (Fin 24) K) 7 15
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 7 16 = (1 : Matrix (Fin 24) (Fin 24) K) 7 16
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 17 = (1 : Matrix (Fin 24) (Fin 24) K) 7 17
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 7 18 = (1 : Matrix (Fin 24) (Fin 24) K) 7 18
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 19 = (1 : Matrix (Fin 24) (Fin 24) K) 7 19
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 20 = (1 : Matrix (Fin 24) (Fin 24) K) 7 20
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 21 = (1 : Matrix (Fin 24) (Fin 24) K) 7 21
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 22 = (1 : Matrix (Fin 24) (Fin 24) K) 7 22
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 7 23 = (1 : Matrix (Fin 24) (Fin 24) K) 7 23
    rw [Matrix.one_apply_ne (by decide : (7 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow7, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

end QOU.Machinery.H4
