import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.AxialDistanceBound

/-!
# QOU.SchurWeyl.OffDiagNonvanishing — `offDiag` vanishes only at the scalar distances

The second of the two lemmas the irreducibility half of SW-5 needs (bean `qou-jfr8`).

`offDiag q (-1) = 0` is a `@[simp]` lemma, so the generator matrix genuinely has vanishing
off-diagonal entries — that is what makes the size-`1` orbits coherent.  The question the
matrix-unit chain asks is whether it can vanish **anywhere else**, because a chain step whose
entry is `0` cannot be promoted by `single_mem_range_of_entry_ne_zero`.

It cannot.  `offDiag q d = 0` forces `d = ±1`, so with
`TableauCells.two_le_natAbs_axialDist` every *admissible* swap has a nonzero entry in at least the
direction its sign allows.

## The identity that does it

On the negative branch `offDiag q d = 1 + a(d)·a(−d)`, and clearing denominators turns
`offDiag q d = 0` into `q^{2d} + q^{−2d} = q^2 + q^{−2}` — the statement that `q^{2d}` and `q^2`
have the same value under `x ↦ x + x⁻¹`.  That map is two-to-one, and the two preimages are
visible as a factorisation:

`A(q²−1)² − q²(A−1)² = −(A − q²)(A·q² − 1)`,  where `A = q^{2d}`.

So either `q^{2d} = q^2` or `q^{2d+2} = 1`, and `zpow_ne_one` turns each into a statement about the
exponent: `d = 1` or `d = −1`.  Nothing about the *size* of `d` is used — the bound `|d| ≥ 2` is
only how the caller rules both out — and no `d ≠ 0` hypothesis is needed either: at `d = 0` the
`else` branch gives `offDiag q 0 = 1`, so the implication is vacuous there.

§7c note: `ℝ` here is genuine — `offDiag` and `seminormalParam` are archimedean by construction.
-/

namespace QOU.SchurWeyl

open TableauCells Seminormal

namespace SeminormalRep

variable (q : ℝ)

/-- **`offDiag` vanishes only at `d = ±1`.**  Equivalently: away from the scalar (same-row /
same-column) distances the off-diagonal entry of the generator matrix is nonzero. -/
theorem offDiag_eq_zero_iff (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {d : ℤ} :
    offDiag q d = 0 → d = 1 ∨ d = -1 := by
  intro hzero
  rcases lt_or_ge d 0 with hneg | hpos
  · -- the interesting branch
    rw [offDiag, if_pos hneg] at hzero
    set A : ℝ := q ^ (2 * d) with hAdef
    have hA0 : A ≠ 0 := zpow_ne_zero _ hq0
    have hA1 : A ≠ 1 := by rw [hAdef]; exact zpow_ne_one hq0 hq2 (by omega)
    have hinv : q ^ (-2 * d) = A⁻¹ := by
      rw [hAdef, ← zpow_neg]; congr 1; ring
    have hnegd : q ^ (-2 * -d) = A := by rw [hAdef]; congr 1; ring
    rw [seminormalParam, seminormalParam, hinv, hnegd] at hzero
    have hd1 : (1 : ℝ) - A⁻¹ ≠ 0 := by
      intro h
      apply hA1
      field_simp at h
      linarith [h]
    have hd2 : (1 : ℝ) - A ≠ 0 := fun h => hA1 (by linarith)
    have hd2' : A - (1 : ℝ) ≠ 0 := fun h => hA1 (by linarith)
    -- clear denominators and factor
    have key : (A - q ^ 2) * (A * q ^ 2 - 1) = 0 := by
      field_simp at hzero
      linear_combination -hzero
    rcases mul_eq_zero.mp key with h | h
    · left
      have : q ^ (2 * d) = q ^ (2 : ℤ) := by rw [← hAdef]; rw [zpow_two, ← pow_two]; linarith
      have hexp : 2 * d = 2 := by
        by_contra hne
        exact zpow_ne_one hq0 hq2 (sub_ne_zero_of_ne hne)
          (by rw [zpow_sub₀ hq0, this, div_self (zpow_ne_zero _ hq0)])
      omega
    · right
      have hpow : q ^ (2 * d + 2) = 1 := by
        rw [zpow_add₀ hq0, ← hAdef]
        rw [show ((2 : ℤ)) = ((2 : ℕ) : ℤ) from rfl, zpow_natCast]
        linarith
      have := zpow_ne_one hq0 hq2 (m := 2 * d + 2)
      by_contra hne
      exact this (by omega) hpow
  · rw [offDiag_of_not_neg q (by omega)] at hzero
    exact absurd hzero one_ne_zero

/-- **Admissible swaps carry a nonzero off-diagonal entry.**  Combines
`TableauCells.two_le_natAbs_axialDist` with `offDiag_eq_zero_iff`: an admissible swap is at
distance `|d| ≥ 2`, and `offDiag` only vanishes at `±1`. -/
theorem offDiag_axialDist_ne_zero {μ : YoungDiagram} (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (T : QOU.Mathlib.StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hadm : TableauCells.SwapAdmissible T k) :
    offDiag q (TableauCells.axialDist T k) ≠ 0 := by
  intro hzero
  have hbound := TableauCells.two_le_natAbs_axialDist T hk hk' hadm
  rcases offDiag_eq_zero_iff q hq0 hq2 hzero with h | h <;> omega

end SeminormalRep

end QOU.SchurWeyl
