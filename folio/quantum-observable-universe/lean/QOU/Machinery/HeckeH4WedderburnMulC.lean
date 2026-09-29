import QOU.Machinery.HeckeH4WedderburnCoord
import QOU.Machinery.HeckeH4WedderburnMulA
import QOU.Machinery.HeckeH4WedderburnMulB
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4WedderburnMulC — entry-by-entry verification of $A\cdot A^{-1} = 1$ (rows 16–23)

Wedderburn tranche **W3 (part 3 of 3)** (bean `qou-308a`): rows 16–23 of the
product identity `coordM q * coordMInv q = 1` — one public row lemma per
row, 24 scalar goals each, every goal closed by `linear_combination`
against `mul_inv_cancel₀` with sympy-derived, exactly-verified cofactors
(the `matinv_right` payloads of the design doc §4).

This part also **assembles** the two matrix identities:
`coordM_mul_coordMInv : A·A⁻¹ = 1` from the 24 row lemmas, and
`coordMInv_mul_coordM : A⁻¹·A = 1` by `Matrix.mul_eq_one_comm` (square
matrices over a commutative ring — one verified side suffices for both,
cheaper than a second 576-goal sweep and equally explicit).

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
/-- Row 16 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row16 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 16 j = (1 : Matrix (Fin 24) (Fin 24) K) 16 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 16 0 = (1 : Matrix (Fin 24) (Fin 24) K) 16 0
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 1 = (1 : Matrix (Fin 24) (Fin 24) K) 16 1
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 2 = (1 : Matrix (Fin 24) (Fin 24) K) 16 2
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 3 = (1 : Matrix (Fin 24) (Fin 24) K) 16 3
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 4 = (1 : Matrix (Fin 24) (Fin 24) K) 16 4
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 5 = (1 : Matrix (Fin 24) (Fin 24) K) 16 5
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 6 = (1 : Matrix (Fin 24) (Fin 24) K) 16 6
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 7 = (1 : Matrix (Fin 24) (Fin 24) K) 16 7
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 8 = (1 : Matrix (Fin 24) (Fin 24) K) 16 8
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - (q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ h2
        + ((q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 16 9 = (1 : Matrix (Fin 24) (Fin 24) K) 16 9
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 10 = (1 : Matrix (Fin 24) (Fin 24) K) 16 10
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 11 = (1 : Matrix (Fin 24) (Fin 24) K) 16 11
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 16 12 = (1 : Matrix (Fin 24) (Fin 24) K) 16 12
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 13 = (1 : Matrix (Fin 24) (Fin 24) K) 16 13
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 14 = (1 : Matrix (Fin 24) (Fin 24) K) 16 14
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 15 = (1 : Matrix (Fin 24) (Fin 24) K) 16 15
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 16 = (1 : Matrix (Fin 24) (Fin 24) K) 16 16
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + ((q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 16 17 = (1 : Matrix (Fin 24) (Fin 24) K) 16 17
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 18 = (1 : Matrix (Fin 24) (Fin 24) K) 16 18
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 19 = (1 : Matrix (Fin 24) (Fin 24) K) 16 19
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 20 = (1 : Matrix (Fin 24) (Fin 24) K) 16 20
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 21 = (1 : Matrix (Fin 24) (Fin 24) K) 16 21
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 22 = (1 : Matrix (Fin 24) (Fin 24) K) 16 22
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 16 23 = (1 : Matrix (Fin 24) (Fin 24) K) 16 23
    rw [Matrix.one_apply_ne (by decide : (16 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow16, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 17 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row17 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 17 j = (1 : Matrix (Fin 24) (Fin 24) K) 17 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 17 0 = (1 : Matrix (Fin 24) (Fin 24) K) 17 0
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 1 = (1 : Matrix (Fin 24) (Fin 24) K) 17 1
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 2 = (1 : Matrix (Fin 24) (Fin 24) K) 17 2
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 3 = (1 : Matrix (Fin 24) (Fin 24) K) 17 3
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 4 = (1 : Matrix (Fin 24) (Fin 24) K) 17 4
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 5 = (1 : Matrix (Fin 24) (Fin 24) K) 17 5
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 6 = (1 : Matrix (Fin 24) (Fin 24) K) 17 6
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 7 = (1 : Matrix (Fin 24) (Fin 24) K) 17 7
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 8 = (1 : Matrix (Fin 24) (Fin 24) K) 17 8
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 9 = (1 : Matrix (Fin 24) (Fin 24) K) 17 9
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 10 = (1 : Matrix (Fin 24) (Fin 24) K) 17 10
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 11 = (1 : Matrix (Fin 24) (Fin 24) K) 17 11
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 17 12 = (1 : Matrix (Fin 24) (Fin 24) K) 17 12
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 13 = (1 : Matrix (Fin 24) (Fin 24) K) 17 13
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 14 = (1 : Matrix (Fin 24) (Fin 24) K) 17 14
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 15 = (1 : Matrix (Fin 24) (Fin 24) K) 17 15
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 16 = (1 : Matrix (Fin 24) (Fin 24) K) 17 16
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 17 17 = (1 : Matrix (Fin 24) (Fin 24) K) 17 17
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 17 18 = (1 : Matrix (Fin 24) (Fin 24) K) 17 18
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 19 = (1 : Matrix (Fin 24) (Fin 24) K) 17 19
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 20 = (1 : Matrix (Fin 24) (Fin 24) K) 17 20
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 21 = (1 : Matrix (Fin 24) (Fin 24) K) 17 21
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 22 = (1 : Matrix (Fin 24) (Fin 24) K) 17 22
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 17 23 = (1 : Matrix (Fin 24) (Fin 24) K) 17 23
    rw [Matrix.one_apply_ne (by decide : (17 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow17, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 18 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row18 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 18 j = (1 : Matrix (Fin 24) (Fin 24) K) 18 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 18 0 = (1 : Matrix (Fin 24) (Fin 24) K) 18 0
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 1 = (1 : Matrix (Fin 24) (Fin 24) K) 18 1
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 2 = (1 : Matrix (Fin 24) (Fin 24) K) 18 2
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 3 = (1 : Matrix (Fin 24) (Fin 24) K) 18 3
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 6*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 6) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 4 = (1 : Matrix (Fin 24) (Fin 24) K) 18 4
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 5 = (1 : Matrix (Fin 24) (Fin 24) K) 18 5
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 6 = (1 : Matrix (Fin 24) (Fin 24) K) 18 6
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 7 = (1 : Matrix (Fin 24) (Fin 24) K) 18 7
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 8 = (1 : Matrix (Fin 24) (Fin 24) K) 18 8
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 9 = (1 : Matrix (Fin 24) (Fin 24) K) 18 9
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 10 = (1 : Matrix (Fin 24) (Fin 24) K) 18 10
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 11 = (1 : Matrix (Fin 24) (Fin 24) K) 18 11
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 7*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 12 = (1 : Matrix (Fin 24) (Fin 24) K) 18 12
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 18 13 = (1 : Matrix (Fin 24) (Fin 24) K) 18 13
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 18 14 = (1 : Matrix (Fin 24) (Fin 24) K) 18 14
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 15 = (1 : Matrix (Fin 24) (Fin 24) K) 18 15
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 16 = (1 : Matrix (Fin 24) (Fin 24) K) 18 16
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 3*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 6*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 17 = (1 : Matrix (Fin 24) (Fin 24) K) 18 17
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 18 = (1 : Matrix (Fin 24) (Fin 24) K) 18 18
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + ((q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 18 19 = (1 : Matrix (Fin 24) (Fin 24) K) 18 19
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 20 = (1 : Matrix (Fin 24) (Fin 24) K) 18 20
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 21 = (1 : Matrix (Fin 24) (Fin 24) K) 18 21
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 18 22 = (1 : Matrix (Fin 24) (Fin 24) K) 18 22
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 18 23 = (1 : Matrix (Fin 24) (Fin 24) K) 18 23
    rw [Matrix.one_apply_ne (by decide : (18 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow18, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 19 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row19 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 19 j = (1 : Matrix (Fin 24) (Fin 24) K) 19 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 19 0 = (1 : Matrix (Fin 24) (Fin 24) K) 19 0
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 1 = (1 : Matrix (Fin 24) (Fin 24) K) 19 1
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 19 2 = (1 : Matrix (Fin 24) (Fin 24) K) 19 2
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 3 = (1 : Matrix (Fin 24) (Fin 24) K) 19 3
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 4 = (1 : Matrix (Fin 24) (Fin 24) K) 19 4
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 5 = (1 : Matrix (Fin 24) (Fin 24) K) 19 5
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 6*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 4*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
        + (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 19 6 = (1 : Matrix (Fin 24) (Fin 24) K) 19 6
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 7 = (1 : Matrix (Fin 24) (Fin 24) K) 19 7
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 8 = (1 : Matrix (Fin 24) (Fin 24) K) 19 8
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 9 = (1 : Matrix (Fin 24) (Fin 24) K) 19 9
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 10 = (1 : Matrix (Fin 24) (Fin 24) K) 19 10
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 16*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 15*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 5*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 7*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 7*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 11 = (1 : Matrix (Fin 24) (Fin 24) K) 19 11
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 12 = (1 : Matrix (Fin 24) (Fin 24) K) 19 12
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 13 = (1 : Matrix (Fin 24) (Fin 24) K) 19 13
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 14 = (1 : Matrix (Fin 24) (Fin 24) K) 19 14
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 19 15 = (1 : Matrix (Fin 24) (Fin 24) K) 19 15
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 16 = (1 : Matrix (Fin 24) (Fin 24) K) 19 16
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 17 = (1 : Matrix (Fin 24) (Fin 24) K) 19 17
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 18 = (1 : Matrix (Fin 24) (Fin 24) K) 19 18
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 19 = (1 : Matrix (Fin 24) (Fin 24) K) 19 19
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 16*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 15*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 9*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 4*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 15*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 16*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 22*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 18*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 23*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 16*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 18*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 9*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 10*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 10*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 4*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 14*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 4*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 13*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 7*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 4*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 1) * mul_inv_cancel₀ h2
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h3
        + (q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 19 20 = (1 : Matrix (Fin 24) (Fin 24) K) 19 20
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 6*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 19 21 = (1 : Matrix (Fin 24) (Fin 24) K) 19 21
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 19 22 = (1 : Matrix (Fin 24) (Fin 24) K) 19 22
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 19 23 = (1 : Matrix (Fin 24) (Fin 24) K) 19 23
    rw [Matrix.one_apply_ne (by decide : (19 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow19, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 5*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2

set_option maxHeartbeats 8000000 in
/-- Row 20 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row20 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 20 j = (1 : Matrix (Fin 24) (Fin 24) K) 20 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 20 0 = (1 : Matrix (Fin 24) (Fin 24) K) 20 0
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 1 = (1 : Matrix (Fin 24) (Fin 24) K) 20 1
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 20 2 = (1 : Matrix (Fin 24) (Fin 24) K) 20 2
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 3 = (1 : Matrix (Fin 24) (Fin 24) K) 20 3
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 4 = (1 : Matrix (Fin 24) (Fin 24) K) 20 4
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 5 = (1 : Matrix (Fin 24) (Fin 24) K) 20 5
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 20 6 = (1 : Matrix (Fin 24) (Fin 24) K) 20 6
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 7 = (1 : Matrix (Fin 24) (Fin 24) K) 20 7
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 8 = (1 : Matrix (Fin 24) (Fin 24) K) 20 8
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 9 = (1 : Matrix (Fin 24) (Fin 24) K) 20 9
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 10 = (1 : Matrix (Fin 24) (Fin 24) K) 20 10
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 11 = (1 : Matrix (Fin 24) (Fin 24) K) 20 11
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 12 = (1 : Matrix (Fin 24) (Fin 24) K) 20 12
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 13 = (1 : Matrix (Fin 24) (Fin 24) K) 20 13
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 14 = (1 : Matrix (Fin 24) (Fin 24) K) 20 14
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 20 15 = (1 : Matrix (Fin 24) (Fin 24) K) 20 15
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 16 = (1 : Matrix (Fin 24) (Fin 24) K) 20 16
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 17 = (1 : Matrix (Fin 24) (Fin 24) K) 20 17
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 18 = (1 : Matrix (Fin 24) (Fin 24) K) 20 18
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 19 = (1 : Matrix (Fin 24) (Fin 24) K) 20 19
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 20 20 = (1 : Matrix (Fin 24) (Fin 24) K) 20 20
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 2*q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ + 1) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 20 21 = (1 : Matrix (Fin 24) (Fin 24) K) 20 21
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 20 22 = (1 : Matrix (Fin 24) (Fin 24) K) 20 22
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 20 23 = (1 : Matrix (Fin 24) (Fin 24) K) 20 23
    rw [Matrix.one_apply_ne (by decide : (20 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow20, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2

set_option maxHeartbeats 8000000 in
/-- Row 21 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row21 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 21 j = (1 : Matrix (Fin 24) (Fin 24) K) 21 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 21 0 = (1 : Matrix (Fin 24) (Fin 24) K) 21 0
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 1 = (1 : Matrix (Fin 24) (Fin 24) K) 21 1
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 2 = (1 : Matrix (Fin 24) (Fin 24) K) 21 2
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 3 = (1 : Matrix (Fin 24) (Fin 24) K) 21 3
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 4 = (1 : Matrix (Fin 24) (Fin 24) K) 21 4
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 5 = (1 : Matrix (Fin 24) (Fin 24) K) 21 5
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 6 = (1 : Matrix (Fin 24) (Fin 24) K) 21 6
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 7 = (1 : Matrix (Fin 24) (Fin 24) K) 21 7
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 8 = (1 : Matrix (Fin 24) (Fin 24) K) 21 8
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 9 = (1 : Matrix (Fin 24) (Fin 24) K) 21 9
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 10 = (1 : Matrix (Fin 24) (Fin 24) K) 21 10
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 4*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 11 = (1 : Matrix (Fin 24) (Fin 24) K) 21 11
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 12 = (1 : Matrix (Fin 24) (Fin 24) K) 21 12
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 13 = (1 : Matrix (Fin 24) (Fin 24) K) 21 13
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 21 14 = (1 : Matrix (Fin 24) (Fin 24) K) 21 14
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 15 = (1 : Matrix (Fin 24) (Fin 24) K) 21 15
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 16 = (1 : Matrix (Fin 24) (Fin 24) K) 21 16
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 17 = (1 : Matrix (Fin 24) (Fin 24) K) 21 17
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 18 = (1 : Matrix (Fin 24) (Fin 24) K) 21 18
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 21 19 = (1 : Matrix (Fin 24) (Fin 24) K) 21 19
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + 3*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 20 = (1 : Matrix (Fin 24) (Fin 24) K) 21 20
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 21 = (1 : Matrix (Fin 24) (Fin 24) K) 21 21
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + 5*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 4*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 21 22 = (1 : Matrix (Fin 24) (Fin 24) K) 21 22
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 21 23 = (1 : Matrix (Fin 24) (Fin 24) K) 21 23
    rw [Matrix.one_apply_ne (by decide : (21 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow21, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 22 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row22 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 22 j = (1 : Matrix (Fin 24) (Fin 24) K) 22 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 22 0 = (1 : Matrix (Fin 24) (Fin 24) K) 22 0
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 1 = (1 : Matrix (Fin 24) (Fin 24) K) 22 1
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-2*q ^ 17*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 16*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 6*q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 5*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 9*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 6*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 9*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 7*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 2 = (1 : Matrix (Fin 24) (Fin 24) K) 22 2
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 3 = (1 : Matrix (Fin 24) (Fin 24) K) 22 3
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 4 = (1 : Matrix (Fin 24) (Fin 24) K) 22 4
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 5 = (1 : Matrix (Fin 24) (Fin 24) K) 22 5
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 7*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 8*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 6*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 7*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 22 6 = (1 : Matrix (Fin 24) (Fin 24) K) 22 6
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 7 = (1 : Matrix (Fin 24) (Fin 24) K) 22 7
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 + q ^ 11*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 2*q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 2*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 2*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 2*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 2*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 8 = (1 : Matrix (Fin 24) (Fin 24) K) 22 8
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 9 = (1 : Matrix (Fin 24) (Fin 24) K) 22 9
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 10 = (1 : Matrix (Fin 24) (Fin 24) K) 22 10
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 11 = (1 : Matrix (Fin 24) (Fin 24) K) 22 11
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 5*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 5*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 3*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 12 = (1 : Matrix (Fin 24) (Fin 24) K) 22 12
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 13 = (1 : Matrix (Fin 24) (Fin 24) K) 22 13
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 14 = (1 : Matrix (Fin 24) (Fin 24) K) 22 14
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 5*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 7*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 8*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 6*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 7*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 4*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 22 15 = (1 : Matrix (Fin 24) (Fin 24) K) 22 15
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 16 = (1 : Matrix (Fin 24) (Fin 24) K) 22 16
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 17 = (1 : Matrix (Fin 24) (Fin 24) K) 22 17
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 + 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*q⁻¹ ^ 2 - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 18 = (1 : Matrix (Fin 24) (Fin 24) K) 22 18
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 19 = (1 : Matrix (Fin 24) (Fin 24) K) 22 19
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 15*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 5*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 7*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 8*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 6*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 7*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 4*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ hq
        + (q ^ 17*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 15*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 6*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 13*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 13*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 10*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 11*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 11*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 4*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 9*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 3*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 6*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
        + (q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 + q ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 22 20 = (1 : Matrix (Fin 24) (Fin 24) K) 22 20
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 16*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 2*q ^ 15*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 4*q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 5*q ^ 13*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 7*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 6*q ^ 11*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - 2*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 7*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 6*q ^ 9*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 6*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - 4*q ^ 7*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2 - 3*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 + 2*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4 - q ^ 5*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 4) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 21 = (1 : Matrix (Fin 24) (Fin 24) K) 22 21
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 22 22 = (1 : Matrix (Fin 24) (Fin 24) K) 22 22
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 9*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 10*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 8*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 4*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 16*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 12*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 10*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 5*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 8*q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 6*q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 4*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 22 23 = (1 : Matrix (Fin 24) (Fin 24) K) 22 23
    rw [Matrix.one_apply_ne (by decide : (22 : Fin 24) ≠ 23)]
    simp only [coordM, coordMInv, coordMRow22, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 17*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 2*q ^ 16*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 6*q ^ 15*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 5*q ^ 14*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 9*q ^ 13*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 6*q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 9*q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 6*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 7*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + 4*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 3*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq

set_option maxHeartbeats 8000000 in
/-- Row 23 of $A\cdot A^{-1} = 1$ (24 scalar goals, sorry-free). -/
theorem coordM_mul_coordMInv_row23 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    ∀ j, (coordM q * coordMInv q) 23 j = (1 : Matrix (Fin 24) (Fin 24) K) 23 j := by
  intro j
  fin_cases j
  · show (coordM q * coordMInv q) 23 0 = (1 : Matrix (Fin 24) (Fin 24) K) 23 0
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 0)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 1 = (1 : Matrix (Fin 24) (Fin 24) K) 23 1
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 1)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 3*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (-q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
  · show (coordM q * coordMInv q) 23 2 = (1 : Matrix (Fin 24) (Fin 24) K) 23 2
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 2)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 3 = (1 : Matrix (Fin 24) (Fin 24) K) 23 3
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 3)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 4 = (1 : Matrix (Fin 24) (Fin 24) K) 23 4
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 4)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 5 = (1 : Matrix (Fin 24) (Fin 24) K) 23 5
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 5)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - 2*q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + q ^ 2 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (2*q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + 3*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 23 6 = (1 : Matrix (Fin 24) (Fin 24) K) 23 6
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 6)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 7 = (1 : Matrix (Fin 24) (Fin 24) K) 23 7
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 7)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 8 = (1 : Matrix (Fin 24) (Fin 24) K) 23 8
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 8)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 9 = (1 : Matrix (Fin 24) (Fin 24) K) 23 9
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 9)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 10 = (1 : Matrix (Fin 24) (Fin 24) K) 23 10
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 10)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 11 = (1 : Matrix (Fin 24) (Fin 24) K) 23 11
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 11)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 3*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 12 = (1 : Matrix (Fin 24) (Fin 24) K) 23 12
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 12)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 13 = (1 : Matrix (Fin 24) (Fin 24) K) 23 13
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 13)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 14 = (1 : Matrix (Fin 24) (Fin 24) K) 23 14
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 14)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - (q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 23 15 = (1 : Matrix (Fin 24) (Fin 24) K) 23 15
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 15)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 16 = (1 : Matrix (Fin 24) (Fin 24) K) 23 16
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 16)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 10*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 9*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 8*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 7*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + q ^ 6*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 4*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 17 = (1 : Matrix (Fin 24) (Fin 24) K) 23 17
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 17)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 18 = (1 : Matrix (Fin 24) (Fin 24) K) 23 18
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 18)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2) * mul_inv_cancel₀ hq
  · show (coordM q * coordMInv q) 23 19 = (1 : Matrix (Fin 24) (Fin 24) K) 23 19
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 19)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 8*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹*q⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 3*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (-q ^ 12*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 8*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - 2*q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ - q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2 - q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h2
        + (-q ^ 4*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2) * mul_inv_cancel₀ h4
  · show (coordM q * coordMInv q) 23 20 = (1 : Matrix (Fin 24) (Fin 24) K) 23 20
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 20)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 9*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - 2*q ^ 7*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3 - q ^ 5*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 3) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 23 21 = (1 : Matrix (Fin 24) (Fin 24) K) 23 21
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 21)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    ring1
  · show (coordM q * coordMInv q) 23 22 = (1 : Matrix (Fin 24) (Fin 24) K) 23 22
    rw [Matrix.one_apply_ne (by decide : (23 : Fin 24) ≠ 22)]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (-q ^ 11*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 9*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - 2*q ^ 7*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ - q ^ 5*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
  · show (coordM q * coordMInv q) 23 23 = (1 : Matrix (Fin 24) (Fin 24) K) 23 23
    rw [Matrix.one_apply_eq]
    simp only [coordM, coordMInv, coordMRow23, coordMInvRow0, coordMInvRow1, coordMInvRow2, coordMInvRow3, coordMInvRow4, coordMInvRow5, coordMInvRow6, coordMInvRow7, coordMInvRow8, coordMInvRow9, coordMInvRow10, coordMInvRow11, coordMInvRow12, coordMInvRow13, coordMInvRow14, coordMInvRow15, coordMInvRow16, coordMInvRow17, coordMInvRow18, coordMInvRow19, coordMInvRow20, coordMInvRow21, coordMInvRow22, coordMInvRow23,
      Matrix.mul_apply, sum_univ_24, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val', Matrix.cons_val, Fin.isValue]
    linear_combination (norm := ring1)
        (2*q ^ 4*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 3*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ ^ 2 + 2*q ^ 2*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q*(q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹*q⁻¹ + (q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ hq
        + (q ^ 14*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 12*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 3*q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + 2*q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹ ^ 2*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 4*(q ^ 4 + 1)⁻¹ + q ^ 2*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + (q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h2
        + (q ^ 10*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 8*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹ + q ^ 6*(q ^ 2 + 1)⁻¹*(q ^ 4 + 1)⁻¹) * mul_inv_cancel₀ h3
        + (1) * mul_inv_cancel₀ h4

/-- **$A\cdot A^{-1} = 1$ (sorry-free)** — the symbolic inverse is verified
    entry-by-entry by Lean (576 scalar goals via the 24 row lemmas). -/
theorem coordM_mul_coordMInv (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    coordM q * coordMInv q = 1 := by
  ext i j
  fin_cases i
  · exact coordM_mul_coordMInv_row0 q h2 h3 h4 j
  · exact coordM_mul_coordMInv_row1 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row2 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row3 q hq h2 j
  · exact coordM_mul_coordMInv_row4 q hq h2 h3 j
  · exact coordM_mul_coordMInv_row5 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row6 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row7 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row8 q hq h2 h3 j
  · exact coordM_mul_coordMInv_row9 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row10 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row11 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row12 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row13 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row14 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row15 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row16 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row17 q hq h2 h3 j
  · exact coordM_mul_coordMInv_row18 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row19 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row20 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row21 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row22 q hq h2 h3 h4 j
  · exact coordM_mul_coordMInv_row23 q hq h2 h3 h4 j

/-- **$A^{-1}\cdot A = 1$ (sorry-free)** — by `Matrix.mul_eq_one_comm` from
    the verified right identity (square matrices over a commutative ring). -/
theorem coordMInv_mul_coordM (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    coordMInv q * coordM q = 1 :=
  Matrix.mul_eq_one_comm.mp (coordM_mul_coordMInv q hq h2 h3 h4)

end QOU.Machinery.H4
