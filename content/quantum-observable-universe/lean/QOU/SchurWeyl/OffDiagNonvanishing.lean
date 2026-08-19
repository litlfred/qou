import QOU.SchurWeyl.SeminormalRep

/-!
# QOU.SchurWeyl.OffDiagNonvanishing — `offDiag` does not vanish at admissible distances

The input SW-5's connectivity argument turned out to need (bean `qou-qyy0`).

`offDiag q d = if d < 0 then 1 + a(d)·a(−d) else 1` is the plain `1` on the non-negative branch,
but on the negative branch it **can** vanish — `offDiag q (−1) = 0`, which `genMat_ne_scalar`'s
docstring already flags.  Since `axialDist (s_k·T) k = −axialDist T k`, each admissible swap gives
only *one* oriented matrix unit for free, and one orientation per edge does not reach every ordered
pair.  What rescues it is that the vanishing happens at `|d| = 1` **and nowhere else** over `ℝ`.

## Why `|d| = 1` is the whole exceptional set

Write `y = q² > 0`.  The vanishing condition `1 + a(d)·a(−d) = 0` is, after clearing denominators,

    (y − 1)² · y^{d−1} = (1 − y^d)²

which is invariant under `d ↦ −d` (multiply through by `y^{2d}`), so both signs reduce to
`e = |d|`.  Factoring `y^e − 1 = (y − 1)·S` with `S = 1 + y + ⋯ + y^{e−1}` turns it into
`y^{e−1} = S²`.  The sum contains the `i = 0` term `1` and the `i = e−1` term `y^{e−1}`, **distinct
exactly when `e ≥ 2`**, so `S ≥ 1 + y^{e−1}` and `S² ≥ 1 + 2y^{e−1} + y^{2e−2} > y^{e−1}`.

At `e = 1` the two terms coincide: `S = 1`, `S² = 1 = y⁰`, equality — which *is*
`offDiag q (−1) = 0`.  So the exceptional case is not special `q`, it is the size-1 orbit.

This is load-bearing mathematics rather than bookkeeping: were `offDiag` to vanish at an admissible
distance, the tableaux reachable in one direction would span an invariant subspace and the
seminormal representation would not be irreducible.

Verified in exact rational arithmetic before formalising (121 rationals × 12 distances: no
vanishing at `|d| ≥ 2`, and the reduction above matched the direct form on every sample).

LaTeX label: `lem:offdiag-nonvanishing`
-/

namespace QOU.SchurWeyl

namespace SeminormalRep

open Seminormal

/-- **The geometric-sum inequality that drives everything.**  For `y > 0`, `y ≠ 1` and `m ≥ 1`,

    (y − 1)² · y^m  <  (y^{m+1} − 1)².

The `m ≥ 1` is essential and is exactly where the size-1 orbit is excluded: at `m = 0` both sides
are `(y − 1)²` and the inequality becomes an equality. -/
theorem sq_geom_lt (y : ℝ) (hy : 0 < y) (hy1 : y ≠ 1) (m : ℕ) (hm : 1 ≤ m) :
    (y - 1) ^ 2 * y ^ m < (y ^ (m + 1) - 1) ^ 2 := by
  have hS : (∑ i ∈ Finset.range (m + 1), y ^ i) * (y - 1) = y ^ (m + 1) - 1 :=
    geom_sum_mul y (m + 1)
  -- the sum dominates `1 + y ^ m`: those are two *distinct* of its terms
  have hsub : ({0, m} : Finset ℕ) ⊆ Finset.range (m + 1) := by
    intro i hi
    simp only [Finset.mem_insert, Finset.mem_singleton] at hi
    rcases hi with rfl | rfl <;> simp [Finset.mem_range]
  have hpair : ∑ i ∈ ({0, m} : Finset ℕ), y ^ i = 1 + y ^ m := by
    rw [Finset.sum_pair (by omega : (0 : ℕ) ≠ m)]
    simp
  have hlow : 1 + y ^ m ≤ ∑ i ∈ Finset.range (m + 1), y ^ i := by
    rw [← hpair]
    exact Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => by positivity)
  have hym : 0 < y ^ m := by positivity
  -- hence `y ^ m < S ^ 2`
  have hSsq : y ^ m < (∑ i ∈ Finset.range (m + 1), y ^ i) ^ 2 := by
    have h1 : (1 + y ^ m) ^ 2 ≤ (∑ i ∈ Finset.range (m + 1), y ^ i) ^ 2 := by
      have hnn : (0 : ℝ) ≤ 1 + y ^ m := by positivity
      nlinarith [hlow, hnn]
    nlinarith [hym, h1]
  -- and `(y − 1)² > 0`, so multiplying preserves the strict inequality
  have hne : (0 : ℝ) < (y - 1) ^ 2 := by
    have : y - 1 ≠ 0 := sub_ne_zero_of_ne hy1
    positivity
  calc (y - 1) ^ 2 * y ^ m
      < (y - 1) ^ 2 * (∑ i ∈ Finset.range (m + 1), y ^ i) ^ 2 := by
        exact (mul_lt_mul_iff_right₀ hne).mpr hSsq
    _ = (y ^ (m + 1) - 1) ^ 2 := by rw [← hS]; ring

/-- `y ^ k ≠ 1` for `y > 0`, `y ≠ 1`, `k ≥ 1` — the denominator is not degenerate. -/
theorem pow_ne_one_of_pos (y : ℝ) (hy : 0 < y) (hy1 : y ≠ 1) {k : ℕ} (hk : 1 ≤ k) :
    y ^ k ≠ 1 := by
  rcases lt_or_gt_of_ne hy1 with hlt | hgt
  · exact ne_of_lt (pow_lt_one₀ hy.le hlt (by omega))
  · exact ne_of_gt (one_lt_pow₀ hgt (by omega))

/-- **The determinant factor does not vanish below `−1`.**  `1 + a(d)·a(−d) ≠ 0` whenever
`d ≤ −2`.  Everything reduces, after clearing denominators, to `sq_geom_lt`. -/
theorem one_add_param_mul_neg_ne_zero_of_le (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    {d : ℤ} (hd : d ≤ -2) :
    1 + seminormalParam q d * seminormalParam q (-d) ≠ 0 := by
  obtain ⟨m, rfl⟩ : ∃ m : ℕ, d = -((m : ℤ) + 2) := ⟨(-d - 2).toNat, by omega⟩
  set y : ℝ := q ^ 2 with hy_def
  have hy : 0 < y := by positivity
  have hy1 : y ≠ 1 := hq2
  set Y : ℝ := y ^ (m + 2) with hY_def
  have hY1 : Y ≠ 1 := pow_ne_one_of_pos y hy hy1 (by omega)
  have hY0 : (0 : ℝ) < Y := by positivity
  -- rewrite the two `zpow` denominators as `Y` and `Y⁻¹`
  have hpow : q ^ (-2 * (-((m : ℤ) + 2))) = Y := by
    rw [hY_def, hy_def, ← zpow_natCast (q ^ 2) (m + 2), ← zpow_natCast q 2, ← zpow_mul]
    congr 1
  have hpow' : q ^ (-2 * -(-((m : ℤ) + 2))) = Y⁻¹ := by
    rw [show (-2 * -(-((m : ℤ) + 2))) = -(-2 * (-((m : ℤ) + 2))) by ring, zpow_neg, hpow]
  -- the algebraic identity
  have hden : y * (Y - 1) ^ 2 ≠ 0 := by
    have : Y - 1 ≠ 0 := sub_ne_zero_of_ne hY1
    positivity
  have hkey : 1 + seminormalParam q (-((m : ℤ) + 2)) * seminormalParam q (-(-((m : ℤ) + 2)))
      = (y * (Y - 1) ^ 2 - (y - 1) ^ 2 * Y) / (y * (Y - 1) ^ 2) := by
    rw [seminormalParam, seminormalParam, hpow, hpow']
    have hYs : Y - 1 ≠ 0 := sub_ne_zero_of_ne hY1
    have hYs' : 1 - Y ≠ 0 := fun h => hYs (by linarith [sub_eq_zero.mp h])
    have hq0' : q ≠ 0 := hq0
    field_simp [hy_def]
    ring
  rw [hkey]
  refine div_ne_zero ?_ hden
  -- the numerator is `y · ((Y−1)² − (y−1)²·y^{m+1})`, positive by `sq_geom_lt`
  have hlt : (y - 1) ^ 2 * y ^ (m + 1) < (y ^ (m + 1 + 1) - 1) ^ 2 :=
    sq_geom_lt y hy hy1 (m + 1) (by omega)
  have hYm : Y = y ^ (m + 1 + 1) := by rw [hY_def]
  have hfac : (y - 1) ^ 2 * Y = y * ((y - 1) ^ 2 * y ^ (m + 1)) := by
    rw [hYm]; ring
  have hpos : 0 < y * (Y - 1) ^ 2 - (y - 1) ^ 2 * Y := by
    rw [hfac, hYm]
    nlinarith [hlt, hy]
  exact ne_of_gt hpos

/-- **`offDiag` does not vanish at an admissible distance.**  For real `q` that is not a root of
unity and `|d| ≥ 2`, both orientations of a size-2 orbit carry a nonzero off-diagonal entry — so a
`SwapStep` supplies matrix units in *both* directions, not just one. -/
theorem offDiag_ne_zero_of_two_le_abs (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {d : ℤ}
    (hd : 2 ≤ |d|) : offDiag q d ≠ 0 := by
  rcases le_or_gt 0 d with hsign | hsign
  · rw [offDiag_of_not_neg q (by omega)]
    exact one_ne_zero
  · have hd2 : d ≤ -2 := by
      rcases abs_cases d with ⟨he, _⟩ | ⟨he, _⟩ <;> omega
    rw [offDiag, if_pos hsign]
    exact one_add_param_mul_neg_ne_zero_of_le q hq0 hq2 hd2

end SeminormalRep

/-! ## Admissible swaps have `|d| ≥ 2`

`offDiag_ne_zero_of_two_le_abs` needs `|d| ≥ 2`, and `SwapAdmissible` is stated as *different row
and different column*.  Getting from one to the other is the **converse** of
`SytSwapTransport.swapAdmissible_of_sq_axialDist_ne_one`, and it is not free: `axialDist_trichotomy`
is a disjunction, so it does not exclude an admissible pair from also sitting at distance `±1`.
The exclusion is the same squeezed-corner argument that proves `axialDist_ne_zero`. -/

namespace TableauCells

variable {μ : YoungDiagram}

open QOU.Mathlib (StandardYoungTableau)

/-- **An admissible pair is never at distance `+1`.**  If the cells of `k` and `k+1` share neither
row nor column and their contents differ by one, the corner completing their rectangle lies in `μ`
and carries an entry strictly between `k` and `k+1`. -/
theorem axialDist_ne_one_of_admissible (T : StandardYoungTableau μ) {k : ℕ}
    (hk : k ∈ Set.Icc 1 μ.cells.card) (hk' : k + 1 ∈ Set.Icc 1 μ.cells.card)
    (hadm : SwapAdmissible T k) : axialDist T k ≠ 1 := by
  have hμ₁ : ((cellOf T k).1, (cellOf T k).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T hk
  have hμ₂ : ((cellOf T (k + 1)).1, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← YoungDiagram.mem_cells]; simpa using cellOf_mem T hk'
  have he₁ : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hk
  have he₂ : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hk'
  intro hone
  have hcontent : ((cellOf T (k + 1)).2 : ℤ) - ((cellOf T (k + 1)).1 : ℤ)
      = ((cellOf T k).2 : ℤ) - ((cellOf T k).1 : ℤ) + 1 := by
    have := hone
    simp only [axialDist, axialDistance, cellContent] at this
    omega
  have hrow := hadm.1
  have hcol := hadm.2
  rcases Nat.lt_or_ge (cellOf T k).1 (cellOf T (k + 1)).1 with hlt | hge
  · -- `k` strictly above `k+1`, hence strictly left too: the corner `(i₁, j₂)` is squeezed
    have hjlt : (cellOf T k).2 < (cellOf T (k + 1)).2 := by omega
    have hcorner : ((cellOf T k).1, (cellOf T (k + 1)).2) ∈ μ :=
      μ.up_left_mem (le_of_lt hlt) (le_refl _) hμ₂
    have hlo : T.entry (cellOf T k).1 (cellOf T k).2
        < T.entry (cellOf T k).1 (cellOf T (k + 1)).2 := T.row_strict hjlt hcorner
    have hhi : T.entry (cellOf T k).1 (cellOf T (k + 1)).2
        < T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 := T.toSsyt.col_strict hlt hμ₂
    omega
  · -- `k+1` strictly above `k`; the column disequality forces it strictly left as well
    have hilt : (cellOf T (k + 1)).1 < (cellOf T k).1 := by omega
    have hjlt : (cellOf T (k + 1)).2 < (cellOf T k).2 := by omega
    have hcorner : ((cellOf T (k + 1)).1, (cellOf T k).2) ∈ μ :=
      μ.up_left_mem (le_of_lt hilt) (le_refl _) hμ₁
    have hlo : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2
        < T.entry (cellOf T (k + 1)).1 (cellOf T k).2 := T.row_strict hjlt hcorner
    have hhi : T.entry (cellOf T (k + 1)).1 (cellOf T k).2
        < T.entry (cellOf T k).1 (cellOf T k).2 := T.toSsyt.col_strict hilt hμ₁
    omega

/-- **An admissible pair has `|d| ≥ 2`.**  Distance `0` is `axialDist_ne_zero`, distance `+1` is
the lemma above, and distance `−1` follows from it applied to the swapped tableau — which is
admissible (`swapAdmissible_swapTableau`) and carries the negated distance
(`axialDist_swapTableau`). -/
theorem two_le_abs_axialDist_of_admissible (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    2 ≤ |axialDist T k| := by
  have hkI : k ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by omega, hkn⟩
  have h0 : axialDist T k ≠ 0 := axialDist_ne_zero T hkI hkI'
  have h1 : axialDist T k ≠ 1 := axialDist_ne_one_of_admissible T hkI hkI' hadm
  have hm1 : axialDist T k ≠ -1 := by
    intro hcon
    have hswapadm : SwapAdmissible (swapTableau T k hk hkn hadm) k :=
      swapAdmissible_swapTableau T hk hkn hadm
    have hswapd : axialDist (swapTableau T k hk hkn hadm) k = 1 := by
      rw [axialDist_swapTableau T hk hkn hadm, hcon]; ring
    exact axialDist_ne_one_of_admissible _ hkI hkI' hswapadm hswapd
  rcases abs_cases (axialDist T k) with ⟨he, _⟩ | ⟨he, _⟩ <;> omega

end TableauCells

end QOU.SchurWeyl
