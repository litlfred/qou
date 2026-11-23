import QOU.SchurWeyl.OcneanuWeightMarkov3

/-!
# R2: the full-twist strand tower does not have the Kummer zero set

C-5 (`climax-volume-mass/vertex-algebra-relations.md`) defines the obstruction
`κₙ = tr_M(Ř₍ₙ₊₁₎ − L₋₁ Ř₍ₙ₎)`, and C-5a asks it to vanish exactly when `n ∣ 6`. `Ř₍ₙ₎` is
defined nowhere in the corpus, so two candidate definitions were fixed by the owner **before**
anything was computed (bean `qou-cvru`, issue #7935).

**Candidate A (strand tower, full twist).** Level `n` carries `H₍ₙ₊₁₎(q)`, `L₋₁` is the Ocneanu
inclusion, and `Ř₍ₙ₎` is the full twist `Δ²`. With the Ocneanu-normalised trace at convention D
(`z = q³/(q²+1)`), and `Δ²` acting on the block `V_λ` by `q^{2c(λ)}` (`c` the content sum), the
trace is `Σ_λ f^λ w_λ q^{2c(λ)}` with `w_λ = ocneanuWeight`. The definitions `twist2`, `twist3`
below **are** that formula, written out at `n = 2, 3`; the eigenvalue `q^{2c(λ)}` of the full twist
is standard and is taken as part of the candidate's definition, not proved here.

* `kappa1_eq`: `κ₁ = (q²−1)(q⁸+q⁶+q⁴+1)/(q²+1)²`.
* `kappa1_ne_zero`: `κ₁ ≠ 0` for every real `q ≠ 0` with `q² ≠ 1`.
* `candidateA_not_kummer_zero_set`: hence the zero set is not `{n : n ∣ 6}`, since `1 ∣ 6`.

This is a scope-(a) negative: this tower, with this element, alone. It does not exclude other
definitions of `Ř₍ₙ₎`, and the conjecture C-5a stays open.

**Candidate B (jet in `q`).** There `κₙ = ε·∂_q tr_M(Ř)` does not depend on `n`.
`levelIndependent_not_kummer_zero_set` is the scope-(b) exclusion; the invariant is
level-independence.
-/

namespace QOU.SchurWeyl.R2TwistTower

open YoungDiagram

/-- Convention-D Markov parameter. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Candidate-A full-twist trace on two strands, `Σ_{λ ⊢ 2} f^λ w_λ q^{2c(λ)}`. -/
noncomputable def twist2 (q : ℝ) : ℝ :=
  ocneanuWeight q (zD q) (ofRowLens [2] (by decide)) * q ^ (2 : ℤ)
    + ocneanuWeight q (zD q) (ofRowLens [1, 1] (by decide)) * q ^ (-2 : ℤ)

/-- Candidate-A full-twist trace on three strands, `Σ_{λ ⊢ 3} f^λ w_λ q^{2c(λ)}` (`f^{(2,1)} = 2`). -/
noncomputable def twist3 (q : ℝ) : ℝ :=
  ocneanuWeight q (zD q) (ofRowLens [3] (by decide)) * q ^ (6 : ℤ)
    + 2 * ocneanuWeight q (zD q) (ofRowLens [2, 1] (by decide)) * q ^ (0 : ℤ)
    + ocneanuWeight q (zD q) (ofRowLens [1, 1, 1] (by decide)) * q ^ (-6 : ℤ)

/-- Candidate-A level-1 obstruction `κ₁ = tr_M(Δ²₍₃₎) − tr_M(Δ²₍₂₎)`. -/
noncomputable def kappa1 (q : ℝ) : ℝ := twist3 q - twist2 q

private theorem dens {q : ℝ} (hq2 : q ^ 2 ≠ 1) :
    q ^ 2 - 1 ≠ 0 ∧ q ^ 4 - 1 ≠ 0 ∧ q ^ 6 - 1 ≠ 0 := by
  have h2 : q ^ 2 - 1 ≠ 0 := sub_ne_zero_of_ne hq2
  refine ⟨h2, ?_, ?_⟩
  · rw [show q ^ 4 - 1 = (q ^ 2 - 1) * (q ^ 2 + 1) by ring]
    exact mul_ne_zero h2 (by positivity)
  · rw [show q ^ 6 - 1 = (q ^ 2 - 1) * (q ^ 4 + q ^ 2 + 1) by ring]
    exact mul_ne_zero h2 (by positivity)

theorem w_two (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q (zD q) (ofRowLens [2] (by decide))
      = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  obtain ⟨h2, h4, -⟩ := dens hq2
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have k0 : hookLength (ofRowLens [2] (by decide)) (0, 0) = 2 := by decide
  have k1 : hookLength (ofRowLens [2] (by decide)) (0, 1) = 1 := by decide
  rw [ocneanuWeight, zD,
    show (ofRowLens [2] (by decide : _)).cells = {(0, 0), (0, 1)} from by decide]
  norm_num [k0, k1]
  field_simp
  ring

theorem w_oneOne (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q (zD q) (ofRowLens [1, 1] (by decide)) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  obtain ⟨h2, h4, -⟩ := dens hq2
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have k0 : hookLength (ofRowLens [1, 1] (by decide)) (0, 0) = 2 := by decide
  have k1 : hookLength (ofRowLens [1, 1] (by decide)) (1, 0) = 1 := by decide
  rw [ocneanuWeight, zD,
    show (ofRowLens [1, 1] (by decide : _)).cells = {(0, 0), (1, 0)} from by decide]
  norm_num [k0, k1]
  field_simp
  ring

theorem w_three (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q (zD q) (ofRowLens [3] (by decide)) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  obtain ⟨h2, h4, h6⟩ := dens hq2
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight_rowLens_three _ _ hq2, markovWeight0, zD]
  field_simp
  ring

theorem w_twoOne (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q (zD q) (ofRowLens [2, 1] (by decide)) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  obtain ⟨h2, h4, h6⟩ := dens hq2
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight_rowLens_twoOne _ _ hq2, markovWeight2, zD]
  field_simp
  ring

theorem w_oneCubed (q : ℝ) (hq2 : q ^ 2 ≠ 1) :
    ocneanuWeight q (zD q) (ofRowLens [1, 1, 1] (by decide)) = 0 := by
  obtain ⟨h2, h4, h6⟩ := dens hq2
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  have hp' : (q ^ 4 + q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [ocneanuWeight_rowLens_oneCubed _ _ hq2, markovWeight1, zD]
  field_simp
  ring

theorem kappa1_eq (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    kappa1 q = (q ^ 2 - 1) * (q ^ 8 + q ^ 6 + q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hp : (q ^ 2 + 1 : ℝ) ≠ 0 := by positivity
  rw [kappa1, twist3, twist2, w_two q hq2, w_oneOne q hq2, w_three q hq2, w_twoOne q hq2,
    w_oneCubed q hq2]
  simp only [zpow_neg, zpow_ofNat]
  field_simp
  ring

theorem kappa1_ne_zero (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : kappa1 q ≠ 0 := by
  rw [kappa1_eq q hq hq2]
  have h2 : q ^ 2 - 1 ≠ 0 := sub_ne_zero_of_ne hq2
  have hp : (0 : ℝ) < q ^ 8 + q ^ 6 + q ^ 4 + 1 := by positivity
  have hp2 : (q ^ 2 + 1 : ℝ) ^ 2 ≠ 0 := by positivity
  exact div_ne_zero (mul_ne_zero h2 hp.ne') hp2

/-- **Candidate A does not have the Kummer zero set.** Any level sequence `κ` whose level-1 term is
the candidate-A defect `kappa1 q` fails `κ n = 0 ↔ n ∣ 6` already at `n = 1`, for every real
`q` with `q ≠ 0` and `q² ≠ 1` (in particular at the substrate `q₀`). Scope (a): this tower with
this element, alone. -/
theorem candidateA_not_kummer_zero_set (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (κ : ℕ → ℝ) (h1 : κ 1 = kappa1 q) : ¬ ∀ n ≥ 1, (κ n = 0 ↔ n ∣ 6) := by
  intro h
  exact kappa1_ne_zero q hq hq2 (h1 ▸ (h 1 le_rfl).2 (by decide))

/-- **Candidate B (jet in `q`) is excluded by level-independence.** A level-independent sequence
vanishes at every level or at none, so it cannot vanish exactly at `n ∣ 6`: `κ 1 = 0` forces
`κ 4 = 0`, but `4 ∤ 6`. Holds in any type with a zero. -/
theorem levelIndependent_not_kummer_zero_set {R : Type*} [Zero R] (κ : ℕ → R)
    (hconst : ∀ n m, κ n = κ m) : ¬ ∀ n ≥ 1, (κ n = 0 ↔ n ∣ 6) := by
  intro h
  have h1 : κ 1 = 0 := (h 1 le_rfl).2 (by decide)
  have h4 : (4 : ℕ) ∣ 6 := (h 4 (by decide)).1 (by rw [hconst 4 1]; exact h1)
  exact absurd h4 (by decide)

end QOU.SchurWeyl.R2TwistTower

