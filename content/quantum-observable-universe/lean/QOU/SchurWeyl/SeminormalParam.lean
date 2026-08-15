import QOU.SchurWeyl.HoefsmitRep

/-!
# `QOU.SchurWeyl.SeminormalParam` — the axial-distance parameter of the seminormal block
(bean `qou-gjg6`, step (i)/(ii) infrastructure)

`HoefsmitRep.lean` provides `seminormalBlock q a`, the `2 × 2` building block of every
size-`2` `s_i`-orbit of Young's seminormal form, with **one free parameter** `a`.  The
general-`λ` construction needs that parameter as an explicit function of the *axial
distance* `d = axialDistance (cell of i) (cell of i+1)`.  This file supplies it:

  `seminormalParam q d = (q - q⁻¹) / (1 - q ^ (-2 * d))`

and proves the three facts that make it the right function.

## Why this is the correct parameter

It is fixed, not fitted.  The concrete `(2,1)` matrix `S1` was built by hand in
`HoefsmitRep.lean` to satisfy the braid relation with `S0`, and its `(0,0)` entry is
`-1 / (q³ + q)`.  In the tableau `[[1,2],[3]]` the entry `2` sits in cell `(0,1)`
(content `1`) and `3` in cell `(1,0)` (content `-1`), so `σ_1` acts with axial distance
`d = -1 - 1 = -2`, and

  `seminormalParam q (-2) = (q - q⁻¹) / (1 - q⁴) = -1 / (q³ + q)`.

`S1_eq_seminormalParam` below records that agreement, so the general formula is
*anchored* on an independently-verified instance rather than asserted.

## What is delivered

* `seminormalParam` — the axial-distance rational function.
* `seminormalParam_one` / `seminormalParam_neg_one` — `a(1) = q`, `a(-1) = -q⁻¹`.
  These are the **size-1 orbit** eigenvalues: when `i` and `i+1` share a row the axial
  distance is `+1` and the generator acts by `q`; when they share a column it is `-1`
  and the generator acts by `-q⁻¹`.  So the single formula covers the scalar orbits and
  the `2 × 2` orbits uniformly — there is no case split in the *parameter*, only in the
  block size.
* `seminormalParam_add_neg` — `a(d) + a(-d) = q - q⁻¹`, i.e. the two diagonal entries of
  a size-`2` block are `a(d)` and `a(-d)`, matching `seminormalBlock`'s trace.  This is
  what makes the block *symmetric under exchanging the two tableaux of the orbit*.
* `S1_eq_seminormalParam` — the anchor: `S1 q = seminormalBlock q (seminormalParam q (-2))`.

## Scope

This is infrastructure for the general-`λ` seminormal representation
(`hoefsmit_seminormal_rep`, still a `-- Ref:`-cited `sorry`).  It supplies the parameter
function of steps (i)–(ii) of that construction.  Step (iii) — the generic size-`6`
`S₃`-orbit braid identity — is proved in
[`Orbit6Braid.lean`](Orbit6Braid.lean) (`genA_genB_braid`), which consumes this
parameter.  What remains of bean `qou-gjg6` is the orbit enumeration and block assembly.

Refs:
- [hoefsmit1974] Hoefsmit, PhD thesis (UBC 1974) — the seminormal form.
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373 — the axial-distance formulas.
-/

namespace QOU.SchurWeyl

open Hecke Matrix

namespace Seminormal

variable (q : ℝ)

/-- **The axial-distance parameter of the seminormal block.**  For an `s_i`-orbit whose
axial distance is `d`, the `(0,0)` entry of the seminormal matrix of `σ_i` is

  `a(d) = (q - q⁻¹) / (1 - q^{-2d})`.

At `d = 1` (entries in the same row) this is `q`; at `d = -1` (same column) it is `-q⁻¹`;
at `d = -2` it is the `(0,0)` entry of the hand-built `(2,1)` matrix `S1`. -/
noncomputable def seminormalParam (d : ℤ) : ℝ := (q - q⁻¹) / (1 - q ^ (-2 * d))

/-- **Same-row orbit**: axial distance `1` gives the eigenvalue `q`. -/
theorem seminormalParam_one (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q 1 = q := by
  have hne : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
  have hz : q ^ (-2 * (1 : ℤ)) = (q ^ 2)⁻¹ := by
    norm_num [zpow_neg, ← zpow_natCast]
  have h1 : (1 : ℝ) - q ^ (-2 * (1 : ℤ)) = (q ^ 2 - 1) / q ^ 2 := by
    rw [hz]; field_simp
  rw [seminormalParam, h1]
  field_simp

/-- **Same-column orbit**: axial distance `-1` gives the eigenvalue `-q⁻¹`. -/
theorem seminormalParam_neg_one (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q (-1) = -q⁻¹ := by
  have hne : (1 : ℝ) - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq2)
  have h1 : (1 : ℝ) - q ^ (-2 * (-1 : ℤ)) = 1 - q ^ 2 := by
    norm_num [← zpow_natCast]
  rw [seminormalParam, h1]
  field_simp
  ring

/-- Algebraic core of `seminormalParam_add_neg`: `c/(1-x) + c/(1-x⁻¹) = c`, since
`1 - x⁻¹ = -(1-x)/x` turns the second summand into `-cx/(1-x)`. -/
private theorem add_inv_aux {c x : ℝ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) :
    c / (1 - x) + c / (1 - x⁻¹) = c := by
  have h1 : (1 : ℝ) - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hx1)
  have h2 : (1 : ℝ) - x⁻¹ ≠ 0 := by
    rw [sub_ne_zero]
    intro hcon
    exact hx1 (by rw [← inv_inv x, ← hcon, inv_one])
  rw [div_add_div _ _ h1 h2, div_eq_iff (mul_ne_zero h1 h2)]
  field_simp
  ring

/-- **The two diagonal entries of a size-`2` orbit are `a(d)` and `a(-d)`**, and they sum
to `q - q⁻¹` — exactly the trace of `seminormalBlock`.  So a size-`2` orbit is the block
`seminormalBlock q (a d)`, whose lower-right entry `(q - q⁻¹) - a d` is `a (-d)`: the same
formula read from the partner tableau, whose axial distance is `-d`. -/
theorem seminormalParam_add_neg (d : ℤ) (hq : q ≠ 0) (h : q ^ (-2 * d) ≠ 1) :
    seminormalParam q d + seminormalParam q (-d) = q - q⁻¹ := by
  have hx0 : q ^ (-2 * d) ≠ 0 := zpow_ne_zero _ hq
  have hpow : q ^ (-2 * -d) = (q ^ (-2 * d))⁻¹ := by
    rw [show (-2 : ℤ) * -d = -(-2 * d) by ring, zpow_neg]
  rw [seminormalParam, seminormalParam, hpow]
  exact add_inv_aux hx0 h

/-- **The three parameters of a `⟨s_k, s_{k+1}⟩`-orbit satisfy one relation.**

At distances `p`, `r` and their sum — the only distances that occur across such an orbit
(`TableauCells.axialDist_succ_swapTableau`, `axialDist_swapTableau_word_left`) — the three
values are not independent:

  `a(p+r)·(a(p) + a(r) - (q - q⁻¹)) = a(p)·a(r)`

This is `Orbit6.seminormalParam_mul_rel` stated directly on `seminormalParam` rather than on
the multiplicative coordinates `x = q^{-2p}`, `y = q^{-2r}`, so it can be used where the
distances are read off tableaux rather than chosen.  It is the sole algebraic input the
braid relation needs beyond `seminormalParam_add_neg`. -/
theorem seminormalParam_rel (p r : ℤ) (hq : q ≠ 0) (hp : q ^ (-2 * p) ≠ 1)
    (hr : q ^ (-2 * r) ≠ 1) (hpr : q ^ (-2 * (p + r)) ≠ 1) :
    seminormalParam q (p + r) * (seminormalParam q p + seminormalParam q r - (q - q⁻¹))
      = seminormalParam q p * seminormalParam q r := by
  have hsplit : q ^ (-2 * (p + r)) = q ^ (-2 * p) * q ^ (-2 * r) := by
    rw [← zpow_add₀ hq]
    congr 1
    ring
  have h1 : (1 : ℝ) - q ^ (-2 * p) ≠ 0 := sub_ne_zero.mpr (Ne.symm hp)
  have h2 : (1 : ℝ) - q ^ (-2 * r) ≠ 0 := sub_ne_zero.mpr (Ne.symm hr)
  have h3 : (1 : ℝ) - q ^ (-2 * p) * q ^ (-2 * r) ≠ 0 := by
    rw [← hsplit]; exact sub_ne_zero.mpr (Ne.symm hpr)
  rw [seminormalParam, seminormalParam, seminormalParam, hsplit]
  field_simp
  ring

/-- **Anchor.**  The hand-built `(2,1)` matrix `S1` — constructed in `HoefsmitRep.lean` to
satisfy the braid relation with `S0`, independently of any axial-distance formula — is the
generic block at the parameter this file predicts.  In `[[1,2],[3]]` the entry `2` has
content `1` and `3` has content `-1`, so `σ_1` acts with axial distance `-2`.

The hypothesis `q² ≠ 1` is necessary, not cosmetic: at `q = ±1` the numerator `q - q⁻¹`
and the denominator `1 - q⁴` both vanish, so `seminormalParam q (-2)` evaluates to `0`
(Lean's `0 / 0`), while `S1`'s `(0,0)` entry is `-1 / (2q) ≠ 0`.  That is the Hecke
algebra degenerating to the group algebra, where the seminormal form is not given by this
formula. -/
theorem S1_eq_seminormalParam (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    S1 q = seminormalBlock q (seminormalParam q (-2)) := by
  have h4 : (1 : ℝ) - q ^ (-2 * (-2 : ℤ)) = 1 - q ^ 4 := by
    norm_num [← zpow_natCast]
  have hne4 : (1 : ℝ) - q ^ 4 ≠ 0 := by
    intro hcon
    apply hq2
    have h2 : (q ^ 2 - 1) * (q ^ 2 + 1) = 0 := by nlinarith [hcon]
    rcases mul_eq_zero.mp h2 with h | h
    · linarith
    · nlinarith [sq_nonneg q]
  have hden : q ^ 3 + q ≠ 0 := by
    have hfac : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [hfac]
    exact mul_ne_zero hq (by positivity)
  have hparam : seminormalParam q (-2) = -1 / (q ^ 3 + q) := by
    rw [seminormalParam, h4]
    field_simp
    ring
  rw [hparam]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [S1, seminormalBlock]; try field_simp; try ring)

end Seminormal

end QOU.SchurWeyl
