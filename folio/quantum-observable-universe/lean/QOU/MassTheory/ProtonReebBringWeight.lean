/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Quaternion
import Mathlib.Tactic

/-!
# The Reeb weight on the proton weight space, from the Bring-cone Reeb triad

Audit: `docs/audits/2026-11-21-proton-two-twelve-count-survey.md` §5. Issue #8967.

This is the second concrete realisation of the Reeb part `R` in the corpus. The first, the
KZ Euler contraction, is in `ProtonReebKZWeight`.

`QOU/BringCone.lean` models the Reeb triad as right multiplication `M_u p = p·u` by the pure
units `u ∈ {i, j, k}` of `ℍ = Quaternion R`. Right multiplication commutes with left
multiplication, so the `M_u` are linear for the **left** complex structure. In the left
basis `{1, j}`, `ℍ = ℂ·1 ⊕ ℂ·j`, and `M_i` is diagonal with eigenvalues `+i` on `1` and
`−i` on `j`:

* `reebI_one`: `M_i 1 = i · 1`;
* `reebI_j`: `M_i j = −(i · j)`.

This is the per-strand `C²` of `ProtonWeightSpaceDim`: `e₁ ↦ 1` and `e₂ ↦ j`. The
`K`-weight direction is `u = i`.

`R` is a vector field, so it acts on three strands by the Leibniz rule,
`R = Σ_s M_i^{(s)}`. A state with `d` copies of `e₂` is then an eigenvector with eigenvalue
`(3 − 2d)·i`. So `R∘R = −(3 − 2d)²` on it.

## Results

* `reebEigen_sq_proton`: on every proton state (`d = 1`), `R∘R = −1`. So `R∘R` is scalar on
  `W_p`, `k = 1`, and `τ_{W_p}(R∘R) = −3`.
* `reeb_trace_proton_ne_neg_twelve`: `−k²·3 ≠ −12` at `k = 1`.
* `weight_ne_two`: on three strands, `|3 − 2d|` is odd for every `d`, so no weight space
  has `k = 2`. This is a parity invariant (scope (b) within this realisation).
* `weight_odd_of_odd`: the same holds for any odd number of strands.

The Reeb direction `u` is a recorded open freedom (`BringCone.lean`, "a gap for the
owner"). For `u ≠ ±i`, `R` does not preserve `W_p`; that case is in the sympy twin, not here.

Base ring: any `CommRing` for the quaternion lemmas (§7c). Integer arithmetic otherwise.
No empirical number.
-/

namespace QOU.MassTheory.ProtonReebBringWeight

section Quaternion

variable {R : Type*} [CommRing R]

/-- `i`, `j` in `ℍ`. -/
def qi : Quaternion R := ⟨0, 1, 0, 0⟩
def qj : Quaternion R := ⟨0, 0, 1, 0⟩

/-- `M_i 1 = i·1`: weight `+i` on `e₁ = 1` (left complex structure). -/
theorem reebI_one : (1 : Quaternion R) * qi = qi * 1 := by
  ext <;> simp [qi]

/-- `M_i j = −(i·j)`: weight `−i` on `e₂ = j`. -/
theorem reebI_j : (qj : Quaternion R) * qi = -(qi * qj) := by
  ext <;> simp [qi, qj]

/-- `M_i ∘ M_i = −1`, as in `BringCone.reebM_i_sq`. -/
theorem reebI_sq (p : Quaternion R) : p * qi * qi = -p := by
  ext <;> simp [qi]

end Quaternion

/-! ## Three strands -/

/-- The eight basis states; `true` marks an `e₂`. -/
def states : List (List Bool) :=
  [[false, false, false], [false, false, true], [false, true, false], [true, false, false],
   [false, true, true], [true, false, true], [true, true, false], [true, true, true]]

/-- Number of `e₂` factors. -/
def numD (s : List Bool) : ℕ := (s.filter id).length

/-- The Leibniz eigenvalue of `R`, divided by `i`: `+1` per `e₁`, `−1` per `e₂`. -/
def reebEigen (s : List Bool) : ℤ := (s.map fun b => if b then (-1 : ℤ) else 1).sum

theorem reebEigen_eq (s : List Bool) : reebEigen s = (s.length : ℤ) - 2 * numD s := by
  induction s with
  | nil => simp [reebEigen, numD]
  | cons b s ih =>
    cases b <;> simp_all [reebEigen, numD] <;> ring

/-- The proton states: one `e₂`. -/
def protonStates : List (List Bool) := states.filter fun s => numD s = 1

theorem protonStates_length : protonStates.length = 3 := by decide

/-- `R∘R = −(eigen)²`. On every proton state this is `−1`. -/
theorem reebEigen_sq_proton : ∀ s ∈ protonStates, -(reebEigen s) ^ 2 = -1 := by decide

/-- `τ_{W_p}(R∘R) = −k²·3 = −3`, not `−12`. -/
theorem reeb_trace_proton :
    (protonStates.map fun s => -(reebEigen s) ^ 2).sum = -3 := by decide

theorem reeb_trace_proton_ne_neg_twelve :
    (protonStates.map fun s => -(reebEigen s) ^ 2).sum ≠ -12 := by decide

/-- On three strands no state has `k² = 4`: the weights are `±1, ±3`. -/
theorem weight_ne_two : ∀ s ∈ states, (reebEigen s) ^ 2 ≠ 4 := by decide

/-- For any odd number `n` of strands and any `d ≤ n`, `(n − 2d)² ≠ 4`. -/
theorem weight_odd_of_odd (n d : ℕ) (hn : n % 2 = 1) : ((n : ℤ) - 2 * d) ^ 2 ≠ 4 := by
  intro h
  have h2 : ((n : ℤ) - 2 * d - 2) * ((n : ℤ) - 2 * d + 2) = 0 := by linear_combination h
  rcases mul_eq_zero.1 h2 with h3 | h3 <;> omega

end QOU.MassTheory.ProtonReebBringWeight
