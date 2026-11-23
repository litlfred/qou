import QOU.SchurWeyl.OcneanuWeight
import QOU.SchurWeyl.OcneanuWeightBranching
import QOU.SchurWeyl.HeckeMarkov3

/-!
# QOU.SchurWeyl.OcneanuWeightMarkov3 — the general-`n` weight reproduces the proved `n = 3` weights

`OcneanuWeight` defines the closed form `ocneanuWeight q z μ` over a generic `[Field R]`.  This file
evaluates it on the three Young diagrams of size `3` and checks it against `HeckeMarkov3`'s
`markovWeight0/1/2` — the weights that file *proves* satisfy the normalisation and both Markov
relations.  It also records the normalisation `Σ_λ d_λ w_λ = 1` at `n = 3` and at `n = 4`.

This is the derive-then-check step for the general-`n` formula: a wrong closed form fails here.
It is **not** a proof of the Markov property at general `n` — see `OcneanuWeight`'s docstring for
what is and is not claimed, and `computations/schurweyl/ocneanu_weight_general_n.py` for the
exact-arithmetic derivation and its out-of-sample validation through `n = 6`.

## Base ring (§7c)

Genuinely archimedean, and deliberately separated from the generic definition: `markovWeight0/1/2`
are `ℝ`-valued, and the denominator non-vanishing facts (`q² + 1 ≠ 0`, `q⁴ + q² + 1 ≠ 0`,
`q⁴ + 1 ≠ 0`) are discharged by `positivity`, which needs the ordering.  Over a general field those
would have to become hypotheses; nothing else here would change.

LaTeX label: `thm:ocneanu-weight-markov3`
-/

namespace QOU.SchurWeyl

open YoungDiagram

/-- Hook lengths of the one-cell diagram. -/
private theorem hook_one : hookLength (ofRowLens [1] (by decide)) (0, 0) = 1 := by decide

/-- Hook lengths of the row `(3)`: `3, 2, 1`. -/
private theorem hook_three :
    hookLength (ofRowLens [3] (by decide)) (0, 0) = 3 ∧
      hookLength (ofRowLens [3] (by decide)) (0, 1) = 2 ∧
      hookLength (ofRowLens [3] (by decide)) (0, 2) = 1 := by decide

/-- Hook lengths of the hook `(2,1)`: `3, 1, 1`. -/
private theorem hook_twoOne :
    hookLength (ofRowLens [2, 1] (by decide)) (0, 0) = 3 ∧
      hookLength (ofRowLens [2, 1] (by decide)) (0, 1) = 1 ∧
      hookLength (ofRowLens [2, 1] (by decide)) (1, 0) = 1 := by decide

/-- Hook lengths of the column `(1³)`: `3, 2, 1`. -/
private theorem hook_oneCubed :
    hookLength (ofRowLens [1, 1, 1] (by decide)) (0, 0) = 3 ∧
      hookLength (ofRowLens [1, 1, 1] (by decide)) (1, 0) = 2 ∧
      hookLength (ofRowLens [1, 1, 1] (by decide)) (2, 0) = 1 := by decide

/-- `q² − 1 ≠ 0`, `q⁴ − 1 ≠ 0`, `q⁶ − 1 ≠ 0` — the hook denominators occurring at `n ≤ 3`. -/
private theorem hook_dens {q : ℝ} (hq2 : q ^ 2 ≠ 1) :
    q ^ 2 - 1 ≠ 0 ∧ q ^ 4 - 1 ≠ 0 ∧ q ^ 6 - 1 ≠ 0 ∧ q ^ 8 - 1 ≠ 0 := by
  have h2 : q ^ 2 - 1 ≠ 0 := sub_ne_zero_of_ne hq2
  have hp : (0:ℝ) < q ^ 2 + 1 := by positivity
  have hp' : (0:ℝ) < q ^ 4 + q ^ 2 + 1 := by positivity
  have hp'' : (0:ℝ) < q ^ 4 + 1 := by positivity
  have h4 : q ^ 4 - 1 ≠ 0 := by
    have h : q ^ 4 - 1 = (q ^ 2 - 1) * (q ^ 2 + 1) := by ring
    rw [h]; exact mul_ne_zero h2 (ne_of_gt hp)
  refine ⟨h2, h4, ?_, ?_⟩
  · have h : q ^ 6 - 1 = (q ^ 2 - 1) * (q ^ 4 + q ^ 2 + 1) := by ring
    rw [h]; exact mul_ne_zero h2 (ne_of_gt hp')
  · have h : q ^ 8 - 1 = (q ^ 4 - 1) * (q ^ 4 + 1) := by ring
    rw [h]; exact mul_ne_zero h4 (ne_of_gt hp'')

/-- The one-cell diagram: `w_{(1)} = 1`, the `n = 1` normalisation. -/
theorem ocneanuWeight_rowLens_one (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [1] (by decide)) = 1 := by
  obtain ⟨h2, -, -, -⟩ := hook_dens hq2
  rw [ocneanuWeight,
    show (ofRowLens [1] (by decide : _)).cells = {(0, 0)} from by decide]
  norm_num [hook_one]
  field_simp

/-- **`n = 3`, trivial block.**  The general-`n` closed form reproduces the proved
`markovWeight0`. -/
theorem ocneanuWeight_rowLens_three (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [3] (by decide)) = markovWeight0 q z := by
  obtain ⟨h2, h4, h6, h8⟩ := hook_dens hq2
  obtain ⟨k0, k1, k2⟩ := hook_three
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight, markovWeight0,
    show (ofRowLens [3] (by decide : _)).cells = {(0, 0), (0, 1), (0, 2)} from by decide]
  norm_num [k0, k1, k2]
  field_simp
  ring

/-- **`n = 3`, two-dimensional block.**  The general-`n` closed form reproduces the proved
`markovWeight2`. -/
theorem ocneanuWeight_rowLens_twoOne (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [2, 1] (by decide)) = markovWeight2 q z := by
  obtain ⟨h2, h4, h6, h8⟩ := hook_dens hq2
  obtain ⟨k0, k1, k2⟩ := hook_twoOne
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight, markovWeight2,
    show (ofRowLens [2, 1] (by decide : _)).cells = {(0, 0), (0, 1), (1, 0)} from by decide]
  norm_num [k0, k1, k2]
  field_simp
  ring

/-- **`n = 3`, sign block.**  The general-`n` closed form reproduces the proved `markovWeight1`. -/
theorem ocneanuWeight_rowLens_oneCubed (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [1, 1, 1] (by decide)) = markovWeight1 q z := by
  obtain ⟨h2, h4, h6, h8⟩ := hook_dens hq2
  obtain ⟨k0, k1, k2⟩ := hook_oneCubed
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight, markovWeight1,
    show (ofRowLens [1, 1, 1] (by decide : _)).cells = {(0, 0), (1, 0), (2, 0)} from by decide]
  norm_num [k0, k1, k2]
  field_simp
  ring

/-! ### Normalisation `Σ_λ d_λ w_λ = 1`

The identity `tr_M(1) = 1`, since the identity's character in block `λ` is `d_λ`.  At `n = 3` this
is `markovWeights_one` transported along the three theorems above; at `n = 4` it is an
**out-of-sample** check on the closed form — the `n = 4` data pinned the framing monomial by a
different route (the branching identity plus the `q`-Jucys–Murphy Markov relations), and no `n = 4`
weight is asserted anywhere in this repository's Lean. -/

/-- **Normalisation at `n = 3`:** `w_{(3)} + 2 w_{(2,1)} + w_{(1³)} = 1`. -/
theorem ocneanuWeight_normalisation_three (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [3] (by decide))
        + 2 * ocneanuWeight q z (ofRowLens [2, 1] (by decide))
        + ocneanuWeight q z (ofRowLens [1, 1, 1] (by decide)) = 1 := by
  rw [ocneanuWeight_rowLens_three q z hq2, ocneanuWeight_rowLens_twoOne q z hq2,
    ocneanuWeight_rowLens_oneCubed q z hq2, markovWeight0, markovWeight1, markovWeight2]
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

/-- Hook lengths of the five partitions of `4`. -/
private theorem hook_four :
    hookLength (ofRowLens [4] (by decide)) (0, 0) = 4 ∧
      hookLength (ofRowLens [4] (by decide)) (0, 1) = 3 ∧
      hookLength (ofRowLens [4] (by decide)) (0, 2) = 2 ∧
      hookLength (ofRowLens [4] (by decide)) (0, 3) = 1 := by decide

private theorem hook_threeOne :
    hookLength (ofRowLens [3, 1] (by decide)) (0, 0) = 4 ∧
      hookLength (ofRowLens [3, 1] (by decide)) (0, 1) = 2 ∧
      hookLength (ofRowLens [3, 1] (by decide)) (0, 2) = 1 ∧
      hookLength (ofRowLens [3, 1] (by decide)) (1, 0) = 1 := by decide

private theorem hook_twoTwo :
    hookLength (ofRowLens [2, 2] (by decide)) (0, 0) = 3 ∧
      hookLength (ofRowLens [2, 2] (by decide)) (0, 1) = 2 ∧
      hookLength (ofRowLens [2, 2] (by decide)) (1, 0) = 2 ∧
      hookLength (ofRowLens [2, 2] (by decide)) (1, 1) = 1 := by decide

private theorem hook_twoOneOne :
    hookLength (ofRowLens [2, 1, 1] (by decide)) (0, 0) = 4 ∧
      hookLength (ofRowLens [2, 1, 1] (by decide)) (0, 1) = 1 ∧
      hookLength (ofRowLens [2, 1, 1] (by decide)) (1, 0) = 2 ∧
      hookLength (ofRowLens [2, 1, 1] (by decide)) (2, 0) = 1 := by decide

private theorem hook_oneFour :
    hookLength (ofRowLens [1, 1, 1, 1] (by decide)) (0, 0) = 4 ∧
      hookLength (ofRowLens [1, 1, 1, 1] (by decide)) (1, 0) = 3 ∧
      hookLength (ofRowLens [1, 1, 1, 1] (by decide)) (2, 0) = 2 ∧
      hookLength (ofRowLens [1, 1, 1, 1] (by decide)) (3, 0) = 1 := by decide

/-- **Normalisation at `n = 4`** (out of sample):
`w_{(4)} + 3 w_{(3,1)} + 2 w_{(2,2)} + 3 w_{(2,1,1)} + w_{(1⁴)} = 1`,
the coefficients being the standard-tableau dimensions `1, 3, 2, 3, 1`. -/
theorem ocneanuWeight_normalisation_four (q z : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q z (ofRowLens [4] (by decide))
        + 3 * ocneanuWeight q z (ofRowLens [3, 1] (by decide))
        + 2 * ocneanuWeight q z (ofRowLens [2, 2] (by decide))
        + 3 * ocneanuWeight q z (ofRowLens [2, 1, 1] (by decide))
        + ocneanuWeight q z (ofRowLens [1, 1, 1, 1] (by decide)) = 1 := by
  obtain ⟨h2, h4, h6, h8⟩ := hook_dens hq2
  obtain ⟨a0, a1, a2, a3⟩ := hook_four
  obtain ⟨b0, b1, b2, b3⟩ := hook_threeOne
  obtain ⟨c0, c1, c2, c3⟩ := hook_twoTwo
  obtain ⟨d0, d1, d2, d3⟩ := hook_twoOneOne
  obtain ⟨e0, e1, e2, e3⟩ := hook_oneFour
  rw [ocneanuWeight, ocneanuWeight, ocneanuWeight, ocneanuWeight, ocneanuWeight,
    show (ofRowLens [4] (by decide : _)).cells = {(0, 0), (0, 1), (0, 2), (0, 3)} from by decide,
    show (ofRowLens [3, 1] (by decide : _)).cells = {(0, 0), (0, 1), (0, 2), (1, 0)} from by decide,
    show (ofRowLens [2, 2] (by decide : _)).cells = {(0, 0), (0, 1), (1, 0), (1, 1)} from by decide,
    show (ofRowLens [2, 1, 1] (by decide : _)).cells = {(0, 0), (0, 1), (1, 0), (2, 0)} from by decide,
    show (ofRowLens [1, 1, 1, 1] (by decide : _)).cells = {(0, 0), (1, 0), (2, 0), (3, 0)}
      from by decide]
  norm_num [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3, d0, d1, d2, d3, e0, e1, e2, e3]
  field_simp
  ring

/-! ### Cross-check: the general two-row formula against the proved `n = 3` weight

`OcneanuWeightBranching.schurPrincipal_twoRow` gives the two-row weight at every `(m,k)` by a
telescoping of the hook-content product.  At `(m,k) = (2,1)` that general formula must reproduce
`markovWeight2`, which was proved independently against the Markov relations.  The chain below runs
through both — `markovWeight2 = ocneanuWeight (ofRowLens [2,1])` (the `n = 3` theorem), then the
bridge, then the general two-row closed form — so an off-by-one anywhere in the telescoping would
fail here. -/
theorem markovWeight2_conventionD (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) :
    markovWeight2 q (q ^ 3 / (q ^ 2 + 1)) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have hq21 : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hdiag : twoRow 2 1 (by omega) = ofRowLens [2, 1] (by decide) := rfl
  rw [← ocneanuWeight_rowLens_twoOne q (q ^ 3 / (q ^ 2 + 1)) hq2, ← hdiag,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    schurPrincipal_twoRow (q ^ 2) hgen (by omega), card_twoRow]
  norm_num [Finset.sum_range_succ]
  field_simp
  ring


/-- **Direct `n = 3` Markov weight sum identity, Plancherel `(1, 0)` values, and `(1, 1/3)` values (`qou-bsec`).**
For every `q, z : ℝ`, `markovWeight0 q z + 2 * markovWeight2 q z + markovWeight1 q z = 1`,
at `(q, z) = (1, 0)` the weights equal `(1/6, 1/6, 1/3)`, and at `(q, z) = (1, 1/3)` they equal `(10/27, 1/27, 8/27)`. -/
theorem markovWeights_three_sum_and_classical_values (q z : ℝ) :
    markovWeight0 q z + 2 * markovWeight2 q z + markovWeight1 q z = 1 ∧
      markovWeight0 1 0 = 1 / 6 ∧
      markovWeight1 1 0 = 1 / 6 ∧
      markovWeight2 1 0 = 1 / 3 ∧
      markovWeight0 1 (1 / 3) = 10 / 27 ∧
      markovWeight1 1 (1 / 3) = 1 / 27 ∧
      markovWeight2 1 (1 / 3) = 8 / 27 := by
  refine ⟨?_,
    by rw [markovWeight0]; norm_num,
    by rw [markovWeight1]; norm_num,
    by rw [markovWeight2]; norm_num,
    by rw [markovWeight0]; norm_num,
    by rw [markovWeight1]; norm_num,
    by rw [markovWeight2]; norm_num⟩
  rw [markovWeight0, markovWeight1, markovWeight2]
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

end QOU.SchurWeyl
