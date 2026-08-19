import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.HoefsmitRepGeneral

/-!
# `QOU.SchurWeyl.QJucysMurphyEigen` — the `q`-Jucys–Murphy eigenvalue (bean `qou-t8qh`)

Ram (1997) Thm 4.1: on the seminormal representation the Jucys–Murphy element `L_k` acts
**diagonally**, with eigenvalue `q^{2·cellContent}` at the cell holding the corresponding value.

This is the one input still missing from `QJucysMurphy.barSymJMSum_block_eigenvalue` — the last
real `sorry` in the SchurWeyl tree.  (Its other blocker, `hoefsmit_seminormal_rep`, is proved.)

## The crux, and why the theorem is true

The recursion is pure conjugation, `L_{k+1} = σ_k L_k σ_k`, so the inductive step conjugates a
diagonal matrix `D` by `S = genMat q (k+1)`.  For that to stay diagonal the off-diagonal of
`S · D · S` must vanish, and on a size-`2` orbit it is

  `offDiag(-d) · (a(d)·q^{2c} + a(-d)·q^{2(c+d)})`,

with `a = seminormalParam` and `d` the axial distance.  The bracket is **identically zero**:

  `1/(1 - q^{-2d}) = -q^{2d}/(1 - q^{2d})`,

which is `seminormalParam_weighted_cancel` below.  On a size-`1` orbit `S` is already diagonal with
entry `a(±1)`, and `a(1) = q`, `a(-1) = -q⁻¹`, so `a(d)² = q^{2d}` — exactly the content shift.

Base ring `ℝ` (the seminormal parameters are archimedean, §7c).
-/

namespace QOU.SchurWeyl

namespace Seminormal

/-- **The weighted cancellation behind the JM eigenvalue.**  Weighting the two seminormal
parameters of a size-`2` orbit by the `q^{2·content}` of their own cells makes them cancel:

  `a(d)·q^{2c} + a(-d)·q^{2(c+d)} = 0`.

This is exactly the off-diagonal of `S · D · S` on that orbit, so it is what keeps the conjugate
of a diagonal matrix diagonal — the inductive step of Ram's Theorem 4.1. -/
theorem seminormalParam_weighted_cancel (q : ℝ) (hq : q ≠ 0) {d : ℤ}
    (hd : q ^ (2 * d) ≠ 1) (c : ℤ) :
    seminormalParam q d * q ^ (2 * c) + seminormalParam q (-d) * q ^ (2 * (c + d)) = 0 := by
  have hx0 : q ^ (2 * d) ≠ 0 := zpow_ne_zero _ hq
  have hx1 : 1 - q ^ (2 * d) ≠ 0 := sub_ne_zero_of_ne (Ne.symm hd)
  have hneg : q ^ (-2 * d : ℤ) = (q ^ (2 * d))⁻¹ := by
    rw [show (-2 * d : ℤ) = -(2 * d) by ring, zpow_neg]
  have hcd : q ^ (2 * (c + d)) = q ^ (2 * c) * q ^ (2 * d) := by
    rw [show (2 * (c + d) : ℤ) = 2 * c + 2 * d by ring, zpow_add₀ hq]
  rw [seminormalParam, seminormalParam, hneg, hcd,
    show (-2 * -d : ℤ) = 2 * d by ring]
  -- make the two powers opaque; what is left is an identity in `x`, `y`, `q`
  set x := q ^ (2 * d) with hxdef
  set y := q ^ (2 * c) with hydef
  have hxi1 : 1 - x⁻¹ ≠ 0 := by
    intro h
    apply hx1
    have hx : x⁻¹ = 1 := by linarith [h]
    have := congrArg (fun t => x * t) hx
    simp only [mul_inv_cancel₀ hx0, mul_one] at this
    linarith [this]
  -- the bracket vanishes: (1 - x⁻¹)⁻¹ = -x·(1 - x)⁻¹
  have hbr : (1 - x⁻¹)⁻¹ + x * (1 - x)⁻¹ = 0 := by
    have hxi : (1 - x⁻¹) = (x - 1) * x⁻¹ := by field_simp
    have h2 : (x - 1)⁻¹ = -(1 - x)⁻¹ := by
      rw [show x - 1 = -(1 - x) by ring, inv_neg]
    rw [hxi, mul_inv, inv_inv, h2]
    ring
  linear_combination ((q - q⁻¹) * y) * hbr

/-- **Size-`1` orbit: the scalar squares to the content shift.**  At axial distance `±1` the
generator acts by the scalar `a(±1)` (`q` resp. `-q⁻¹`), and its square is `q^{2d}` — exactly the
factor by which `q^{2·content}` changes when the content moves by `d`.  This is the inadmissible
branch of the inductive step. -/
theorem seminormalParam_sq_of_one (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q 1 ^ 2 = q ^ (2 * (1 : ℤ)) := by
  rw [seminormalParam_one q hq hq2]
  norm_num [← zpow_natCast]

theorem seminormalParam_sq_of_neg_one (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q (-1) ^ 2 = q ^ (2 * (-1 : ℤ)) := by
  rw [seminormalParam_neg_one q hq hq2]
  rw [show (2 * (-1 : ℤ)) = -2 by ring, zpow_neg]
  field_simp

/-- The inadmissible branch in one statement: for `d = ±1`, `a(d)² · q^{2c} = q^{2(c+d)}`. -/
theorem seminormalParam_sq_mul (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {d : ℤ}
    (hd : d = 1 ∨ d = -1) (c : ℤ) :
    seminormalParam q d ^ 2 * q ^ (2 * c) = q ^ (2 * (c + d)) := by
  have hcd : q ^ (2 * (c + d)) = q ^ (2 * c) * q ^ (2 * d) := by
    rw [show (2 * (c + d) : ℤ) = 2 * c + 2 * d by ring, zpow_add₀ hq]
  rcases hd with rfl | rfl
  · rw [hcd, seminormalParam_sq_of_one q hq hq2]; ring
  · rw [hcd, seminormalParam_sq_of_neg_one q hq hq2]; ring

/-! ## The full entry-level inductive step

Both entries of `S · D · S` on a size-`2` orbit reduce to the *same* cancellation. Writing
`c` for the content seen by `D` at `T` and `c + d` for the one at `s·T`:

* the **off-diagonal** is `offDiag(d) · (a(d)q^{2c} + a(-d)q^{2(c+d)})`, which is `0`;
* the **diagonal** is `a(d)²q^{2c} + offDiag(-d)offDiag(d)·q^{2(c+d)}`, and using
  `offDiag_mul_neg` (`offDiag(d)offDiag(-d) = 1 + a(d)a(-d)`) it collapses to
  `a(d)·(a(d)q^{2c} + a(-d)q^{2(c+d)}) + q^{2(c+d)} = q^{2(c+d)}`.

So one identity governs the whole step — which is why the induction closes.
-/

open SeminormalRep in
/-- **Off-diagonal entry of the step vanishes.** -/
theorem jmStep_offDiag (q : ℝ) (hq : q ≠ 0) {d : ℤ} (hd : q ^ (2 * d) ≠ 1) (c : ℤ) :
    offDiag q d * q ^ (2 * c) * seminormalParam q d
      + seminormalParam q (-d) * q ^ (2 * (c + d)) * offDiag q d = 0 := by
  have hcancel := seminormalParam_weighted_cancel q hq hd c
  linear_combination offDiag q d * hcancel

open SeminormalRep in
/-- **Diagonal entry of the step is the shifted content.**  `a(d)²q^{2c}` plus the
off-diagonal round trip equals `q^{2(c+d)}` exactly. -/
theorem jmStep_diag (q : ℝ) (hq : q ≠ 0) {d : ℤ} (hd0 : d ≠ 0) (hd : q ^ (2 * d) ≠ 1)
    (c : ℤ) :
    seminormalParam q d ^ 2 * q ^ (2 * c)
        + offDiag q (-d) * offDiag q d * q ^ (2 * (c + d))
      = q ^ (2 * (c + d)) := by
  have hcancel := seminormalParam_weighted_cancel q hq hd c
  have hprod : offDiag q d * offDiag q (-d)
      = 1 + seminormalParam q d * seminormalParam q (-d) := offDiag_mul_neg q hd0
  linear_combination seminormalParam q d * hcancel + q ^ (2 * (c + d)) * hprod

end Seminormal

end QOU.SchurWeyl
