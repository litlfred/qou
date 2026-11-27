/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

/-!
# One neutral lepton fixes every first-generation charge

Bean `qou-h0zz` (per-fermion braid words), epic `qou-x08k`. Owner ruling 2026-11-22:
*"Needs to derive the q_i"*: the quark charges `+2/3`, `−1/3` are not to be adopted from the
Standard Model.

## Setting

`QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant` works on the `5 = K⁵`, colour indices `{0,1,2}`
and isospin indices `{3,4}`. It proves that the traceless commutant of `𝔰𝔩₃ ⊕ 𝔰𝔩₂` there is
spanned by `Y₀ = diag(−2,−2,−2,3,3)`, and it leaves the charge generator `Q(α) = T₃ + α·Y₀` with
the scale `α` free. In this corpus both summands are built objects: the colour triple `C` is the
octonionic `𝟑` (`OctonionColourTripletComplexType`), and the isospin doublet `V` is the
fibre with `Λ²V ≅ 𝟙`.

## What is proved here

* `qWeight5_apply`: the weights of `Q(α)` on the `5` are `(−2α, −2α, −2α, 1/2 + 3α, −1/2 + 3α)`.
* `neutral_lepton_iff`: the isospin doublet of the `5̄` has a **neutral member** if and only if
  `α = 1/6` or `α = −1/6`.
* `neutral_lepton_iff_three_eighths`: the same condition is equivalent to the `5̄ ⊕ 10` trace
  ratio being `3/8`. The two normalisations coincide.
* `charges_at_one_sixth`: at `α = 1/6`, the `5̄` carries `(1/3, 1/3, 1/3, −1, 0)` and the ten
  wedges of `10 = Λ²5` carry `−2/3` (colour–colour), `+2/3` and `−1/3` (colour–isospin) and `+1`
  (isospin–isospin). These are the charges of `d^c, e, ν` and of `u^c, u, d, e^c`.
* `qWeight5_neg`: `α ↦ −α` is the swap of the two isospin indices composed with a sign. So the
  `α = −1/6` root is the same table with the doublet relabelled and all charges negated, i.e.
  charge conjugation, and not a second spectrum.
* `colourSinglet_charges_integer`: at `α = ±1/6`, every colour-singlet weight (the doublet of
  `5̄` and the isospin wedge of `10`) is an integer, and every coloured weight is a third of an odd
  integer.

## Scope

This is representation theory on given objects, and it has exactly two inputs:

1. **The matter content is `5̄ ⊕ Λ²5` on `5 = C ⊕ V`.** This is the Georgi–Glashow /
   Baez–Huerta assignment (`[baez-huerta2010]`, §3). The corpus does not derive it, and this file
   does not claim it does (`rem:su5-hypercharge-n3-gate`).
2. **One lepton is neutral.** This is a datum, not a fit: it is a statement that a charge is
   *zero*, it involves no measured number, and it is the same datum as `nu_framing_is_zero`
   (`ComponentFraming`) takes as its hypothesis.

Given those two, nothing is chosen. In particular the quark charges `+2/3` and `−1/3` are
consequences and are no longer inputs.
-/

namespace QOU.EightfoldWay.NeutralLeptonFixesCharges

open Matrix QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant

variable {K : Type*} [Field K]

/-- The weights of `Q(α) = T₃ + α·Y₀` on the `5`. -/
theorem qWeight5_apply (α : K) :
    qWeight5 α 0 = -2 * α ∧ qWeight5 α 1 = -2 * α ∧ qWeight5 α 2 = -2 * α ∧
      qWeight5 α 3 = 1 / 2 + 3 * α ∧ qWeight5 α 4 = -(1 / 2) + 3 * α := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [qWeight5, Q5, T3, Y0, Matrix.add_apply, Matrix.smul_apply] <;> ring

/-- The charge of the `i`-th basis vector of the `5̄`. -/
def qWeight5bar (α : K) (i : Fin 5) : K := -qWeight5 α i

/-- The charge of the wedge `e_i ∧ e_j` of `10 = Λ²5`. -/
def qWeight10 (α : K) (i j : Fin 5) : K := qWeight5 α i + qWeight5 α j

/-- **A neutral lepton fixes the scale.** The isospin doublet of the `5̄` (indices `3`, `4`) has a
member of charge zero if and only if `α = 1/6` or `α = −1/6`. -/
theorem neutral_lepton_iff [CharZero K] (α : K) :
    (qWeight5bar α 3 = 0 ∨ qWeight5bar α 4 = 0) ↔ (α = 1 / 6 ∨ α = -(1 / 6)) := by
  obtain ⟨-, -, -, h3, h4⟩ := qWeight5_apply α
  simp only [qWeight5bar, neg_eq_zero, h3, h4]
  constructor
  · rintro (h | h)
    · right; linear_combination h / 3
    · left; linear_combination h / 3
  · rintro (h | h)
    · right; rw [h]; ring
    · left; rw [h]; ring

/-- `α² = 1/36` is the same as `α = ±1/6`. -/
theorem sq_eq_one_thirtysixth_iff [CharZero K] (α : K) :
    α ^ 2 = 1 / 36 ↔ (α = 1 / 6 ∨ α = -(1 / 6)) := by
  constructor
  · intro h
    have : (α - 1 / 6) * (α + 1 / 6) = 0 := by linear_combination h
    rcases mul_eq_zero.mp this with h' | h'
    · left; linear_combination h'
    · right; linear_combination h'
  · rintro (h | h) <;> rw [h] <;> ring

/-- **The neutral-lepton normalisation is the `3/8` normalisation.** The `5̄` doublet has a
neutral member if and only if the `5̄ ⊕ 10` trace ratio `Tr(T₃²)/Tr(Q²)` equals `3/8`. -/
theorem neutral_lepton_iff_three_eighths [CharZero K] (α : K) (hden : 1 + 60 * α ^ 2 ≠ 0) :
    (qWeight5bar α 3 = 0 ∨ qWeight5bar α 4 = 0) ↔
      tr5bar10DiagSq (t3Weight5 K) / tr5bar10DiagSq (qWeight5 α) = (3 : K) / 8 := by
  rw [neutral_lepton_iff, traceRatio_5bar_oplus_10_eq_three_eighths_iff α hden,
    sq_eq_one_thirtysixth_iff]

/-- **The charge table at `α = 1/6`.** The `5̄` carries `(1/3, 1/3, 1/3, −1, 0)`, i.e.
`d^c` (three colours), `e`, `ν`; and the wedges of `10 = Λ²5` carry `−2/3` on colour–colour
(`u^c`), `+2/3` on colour–`3` (`u`), `−1/3` on colour–`4` (`d`) and `+1` on `3 ∧ 4` (`e^c`). -/
theorem charges_at_one_sixth [CharZero K] :
    (∀ i : Fin 5, i.1 < 3 → qWeight5bar (1 / 6 : K) i = 1 / 3) ∧
      qWeight5bar (1 / 6 : K) 3 = -1 ∧ qWeight5bar (1 / 6 : K) 4 = 0 ∧
      (∀ i j : Fin 5, i.1 < 3 → j.1 < 3 → qWeight10 (1 / 6 : K) i j = -(2 / 3)) ∧
      (∀ i : Fin 5, i.1 < 3 → qWeight10 (1 / 6 : K) i 3 = 2 / 3) ∧
      (∀ i : Fin 5, i.1 < 3 → qWeight10 (1 / 6 : K) i 4 = -(1 / 3)) ∧
      qWeight10 (1 / 6 : K) 3 4 = 1 := by
  obtain ⟨h0, h1, h2, h3, h4⟩ := qWeight5_apply (1 / 6 : K)
  have hc : ∀ i : Fin 5, i.1 < 3 → qWeight5 (1 / 6 : K) i = -(1 / 3) := by
    intro i hi
    fin_cases i
    · exact h0.trans (by ring)
    · exact h1.trans (by ring)
    · exact h2.trans (by ring)
    all_goals simp at hi
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro i hi; simp only [qWeight5bar, hc i hi]; ring
  · simp only [qWeight5bar, h3]; ring
  · simp only [qWeight5bar, h4]; ring
  · intro i j hi hj; simp only [qWeight10, hc i hi, hc j hj]; ring
  · intro i hi; simp only [qWeight10, hc i hi, h3]; ring
  · intro i hi; simp only [qWeight10, hc i hi, h4]; ring
  · simp only [qWeight10, h3, h4]; ring

/-- The swap of the two isospin indices. -/
def isoSwap : Equiv.Perm (Fin 5) := Equiv.swap 3 4

/-- **The other root is charge conjugation.** `Q(−α)` is `−Q(α)` with the two isospin indices
exchanged, so `α = −1/6` reproduces the `α = 1/6` table up to relabelling the doublet and
reversing every charge. -/
theorem qWeight5_neg (α : K) (i : Fin 5) : qWeight5 (-α) i = -qWeight5 α (isoSwap i) := by
  obtain ⟨a0, a1, a2, a3, a4⟩ := qWeight5_apply α
  obtain ⟨b0, b1, b2, b3, b4⟩ := qWeight5_apply (-α)
  fin_cases i
  · have : isoSwap (0 : Fin 5) = 0 := by decide
    simp only [Fin.zero_eta, this, a0, b0]; ring
  · have : isoSwap (1 : Fin 5) = 1 := by decide
    simp only [Fin.mk_one, this, a1, b1]; ring
  · have : isoSwap (2 : Fin 5) = 2 := by decide
    simp only [Fin.reduceFinMk, this, a2, b2]; ring
  · have : isoSwap (3 : Fin 5) = 4 := by decide
    simp only [Fin.reduceFinMk, this, a4, b3]; ring
  · have : isoSwap (4 : Fin 5) = 3 := by decide
    simp only [Fin.reduceFinMk, this, a3, b4]; ring

/-- **Charge quantisation.** At `α = ±1/6` the colour-singlet weights (the `5̄` doublet and the
isospin wedge `3 ∧ 4` of `10`) are integers, and every coloured weight of the `5` is `∓1/3`. -/
theorem colourSinglet_charges_integer [CharZero K] (α : K) (hα : α = 1 / 6 ∨ α = -(1 / 6)) :
    (∃ m n k : ℤ, qWeight5bar α 3 = m ∧ qWeight5bar α 4 = n ∧ qWeight10 α 3 4 = k) ∧
      (∀ i : Fin 5, i.1 < 3 → 3 * qWeight5 α i = -1 ∨ 3 * qWeight5 α i = 1) := by
  obtain ⟨h0, h1, h2, h3, h4⟩ := qWeight5_apply α
  have hc : ∀ i : Fin 5, i.1 < 3 → qWeight5 α i = -2 * α := by
    intro i hi
    fin_cases i
    · exact h0
    · exact h1
    · exact h2
    all_goals simp at hi
  rcases hα with h | h
  · refine ⟨⟨-1, 0, 1, ?_, ?_, ?_⟩, fun i hi => Or.inl ?_⟩
    · rw [qWeight5bar, h3, h]; push_cast; ring
    · rw [qWeight5bar, h4, h]; push_cast; ring
    · rw [qWeight10, h3, h4, h]; push_cast; ring
    · rw [hc i hi, h]; ring
  · refine ⟨⟨0, 1, -1, ?_, ?_, ?_⟩, fun i hi => Or.inr ?_⟩
    · rw [qWeight5bar, h3, h]; push_cast; ring
    · rw [qWeight5bar, h4, h]; push_cast; ring
    · rw [qWeight10, h3, h4, h]; push_cast; ring
    · rw [hc i hi, h]; ring

end QOU.EightfoldWay.NeutralLeptonFixesCharges
