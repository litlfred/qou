import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.CasimirNStability — n-stability selects the bare count

Formalises the selection principle of the `N_⊙` construction for
[`conj:casimir-epsilon-vacuum`](../../../quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
(audit `docs/audits/2026-05-31-casimir-n-unknot-construction.md`).

The Casimir prefactor is a single physical number, so the mode-count
functional evaluated on the `n`-component vacuum (n disjoint unknots)
must have a **cutoff-independent relative substrate deviation** —
"n-stability". Among the candidate trace functionals:

* the **bare disjoint-component count** `N(n) = n` is q-independent —
  n-stable and mode-counting (admissible, and by `nStable_unique`
  the unique such functional once the single-mode value is fixed to
  `1` by the Hoefsmit normalisation `Geom_ε(1·⊙) = ε/ℏ_q²`);
* the **Jones value of the n-unlink** `δ^{n−1}`, with quantum
  dimension `δ = √q + (√q)⁻¹`, fails n-stability for every
  `q > 0, q ≠ 1` (its relative deviation grows with the cutoff);
* the **normalised Markov trace** `≡ 1` is stable but content-free —
  it does not count modes.

The fourth candidate of the audit (the unnormalised Wenzl sum
`Σ_λ y_λ`) requires the partition-weight family and is covered
numerically by `casimir-n-unknot-construction.witness.json`; it
diverges in `n` and is inadmissible for the same reason as the Jones
value.

The file is stated over `ℝ` because it uses ordering. The square root
`√q` is a symbol `s` (`s > 0`, `s² = q`) rather than `Real.sqrt` (bean
`qou-dk7p`).
-/

namespace QOU.AppendixSurreals

/-- n-stability (cutoff admissibility) of a vacuum trace functional
`F : ℕ → ℝ → ℝ` (value at mode-cutoff `n`, substrate parameter `q`):
the relative substrate deviation is independent of the cutoff. In
division-free form: `F m q · F n 1 = F n q · F m 1` for all cutoffs.
A single-number observable cannot depend on where the mode tower is
truncated. -/
def NStable (F : ℕ → ℝ → ℝ) (q : ℝ) : Prop :=
  ∀ m n : ℕ, F m q * F n 1 = F n q * F m 1

/-- Mode-counting normalisation: at the classical point `q = 1` the
functional counts the vacuum's disjoint components. -/
def CountsModes (F : ℕ → ℝ → ℝ) : Prop :=
  ∀ n : ℕ, F n 1 = n

/-- The bare disjoint-component count `N(n) = n`, independent of `q`. -/
def bareCount (n : ℕ) (_q : ℝ) : ℝ := n

/-- The Jones value of the `n`-unlink: `δ^{n−1}` with quantum dimension
`δ = √q + (√q)⁻¹`. The function takes the square root `s = √q` itself as its
argument (`s > 0`, `s² = q`), so no `Real.sqrt` is needed; `s = 1` is the
classical point `q = 1` (bean `qou-dk7p`). -/
noncomputable def unlinkJones (n : ℕ) (s : ℝ) : ℝ :=
  (s + s⁻¹) ^ (n - 1)

/-- The normalised Markov trace of any identity braid: constant `1`. -/
def normalizedTrace (_n : ℕ) (_q : ℝ) : ℝ := 1

/-- The bare count counts modes. -/
theorem bareCount_countsModes : CountsModes bareCount := fun _ => rfl

/-- The bare count is n-stable at every substrate parameter: its
relative substrate deviation is identically zero. -/
theorem bareCount_nStable (q : ℝ) : NStable bareCount q := by
  intro m n
  unfold bareCount
  ring

/-- The normalised trace is (vacuously) stable… -/
theorem normalizedTrace_nStable (q : ℝ) : NStable normalizedTrace q := by
  intro m n
  rfl

/-- …but content-free: it does not count modes. -/
theorem normalizedTrace_not_countsModes : ¬ CountsModes normalizedTrace := by
  intro h
  have h2 := h 2
  norm_num [normalizedTrace] at h2

/-- The quantum dimension at the classical point: `δ = 1 + 1⁻¹ = 2` at `s = √1 = 1`. -/
theorem quantumDim_one : (1 : ℝ) + (1 : ℝ)⁻¹ = 2 := by
  norm_num

/-- `δ = 2` forces the classical point: for `0 < s` (the square root of `q`),
`s + s⁻¹ = 2 ↔ s = 1`, since `δ − 2 = (s − 1)²/s`. With `s² = q`, `s = 1` is `q = 1`. -/
theorem quantumDim_eq_two_iff (s : ℝ) (hs : 0 < s) :
    s + s⁻¹ = 2 ↔ s = 1 := by
  have hs0 : s ≠ 0 := ne_of_gt hs
  constructor
  · intro h
    have hexp : s * s + 1 = 2 * s := by
      have := congrArg (· * s) h
      simp only [add_mul, inv_mul_cancel₀ hs0] at this
      linarith
    have hsq : (s - 1) ^ 2 = 0 := by linear_combination hexp
    have := sq_eq_zero_iff.mp hsq
    linarith
  · rintro rfl
    norm_num

/-- The Jones value of the n-unlink fails n-stability away from the
classical point: comparing cutoffs `1` and `2` forces `δ = 2`, i.e. `s = 1`. -/
theorem unlinkJones_not_nStable (s : ℝ) (hs : 0 < s) (hs1 : s ≠ 1) :
    ¬ NStable unlinkJones s := by
  intro h
  have h12 := h 1 2
  simp only [unlinkJones, inv_one] at h12
  norm_num at h12
  exact hs1 ((quantumDim_eq_two_iff s hs).mp h12.symm)

/-- **Uniqueness.** An n-stable, mode-counting functional whose
single-mode value is `1` (the Hoefsmit normalisation: one unknot
contributes relative count `1`) is the bare count. -/
theorem nStable_unique (F : ℕ → ℝ → ℝ) (q : ℝ)
    (hS : NStable F q) (hC : CountsModes F) (h1 : F 1 q = 1) :
    ∀ n : ℕ, F n q = bareCount n q := by
  intro n
  have h := hS n 1
  rw [hC 1, hC n, h1] at h
  simpa [bareCount] using h

/-- **The selection, packaged.** Among the three concrete candidates,
the bare count is the unique one that both counts modes and is
n-stable; the Jones value fails stability and the normalised trace
fails counting. The parameter is the square root `s = √q` (`s > 0`,
`s ≠ 1`, i.e. `q ≠ 1`); the bare count and the normalised trace do not depend on
it. (The Wenzl-sum candidate is covered numerically by
the witness; see the module docstring.) -/
theorem bareCount_unique_admissible (s : ℝ) (hs : 0 < s) (hs1 : s ≠ 1) :
    (CountsModes bareCount ∧ NStable bareCount s)
      ∧ ¬ NStable unlinkJones s
      ∧ ¬ CountsModes normalizedTrace :=
  ⟨⟨bareCount_countsModes, bareCount_nStable s⟩,
    unlinkJones_not_nStable s hs hs1,
    normalizedTrace_not_countsModes⟩

end QOU.AppendixSurreals
