/-
# Categorical mass at q = 1, and the energy-to-mass reading of the n–p cell

Two results, both used in
`docs/audits/2026-11-22-np-gap-at-q-one-unit-map.md`.

**Part A (combinatorial core of `def:mass-identity` at q = 1).**
At q = 1 the Jimbo braiding `Ř` on `V ⊗ V`, `V = R²`, is the swap, `K = 1`, and
the framing factor `(1 + q²)^n q^(-n-2w)` is `2^n`. A braid on `n` strands then acts
on `V^{⊗n}` as the permutation operator of its image `π ∈ S_n`; that operator
permutes the basis vectors `e_f`, `f : Fin n → Fin 2`, so its trace is the number
of colourings `f` fixed by `π`. We prove that number is `2^c`, where `c` is the
number of orbits of `⟨π⟩` on the strands, i.e. the number of components of the
braid closure. Since the normalised trace divides by `Tr 1 = 2^n`, the
framing-corrected mass at q = 1 is `2^n · 2^c / 2^n = 2^c`.

Consequence: at q = 1 the categorical mass of a braid class depends only on the
number of components of its closure. Two nucleons closing to three-component
links (the Borromean rings and its mirror) have equal mass at q = 1.

The identification "braid at q = 1 acts by the permutation operator" is the
bridge lemma of `FlipSymmetryAtOneBridge` (PR #8804) and is not re-proved here.

**Part B (the E₀ pole).** With `c_q = 1/(q-1)`, `ℏ_q = 1 - 1/q`,
`E₀ = m c_q² ℏ_q = m/(q(q-1))`. The cell energy `2 E₀ log q` divided by `m` is
bounded below by `2/q²` for `q > 1` (so it does not vanish as `q → 1`), while the
same cell read as a mass through `def:mass-energy` (`𝔈 = 𝔪 c_q²`), i.e. divided by
`c_q²`, equals `2 m ℏ_q log q`, which lies in `[0, 2 m (q-1)²]`.

No empirical input enters any statement here.
-/
import Mathlib.GroupTheory.GroupAction.Quotient
import Mathlib.Algebra.Group.Subgroup.ZPowers.Basic
import Mathlib.SetTheory.Cardinal.Finite
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp

namespace QOU.MassTheory.CategoricalMassAtOne

open scoped Classical

/-! ## Part A -/

variable {n : ℕ}

/-- Colourings of the strands by the two basis vectors of `V = R²` that are fixed
by the strand permutation `π`. These index the fixed basis vectors of the
permutation operator on `V^{⊗n}`. -/
def FixedColouring (π : Equiv.Perm (Fin n)) : Type :=
  {f : Fin n → Fin 2 // ∀ i, f (π i) = f i}

/-- The components of the closure of a braid with permutation `π`: the orbits of
`⟨π⟩` on the strands. -/
abbrev Components (π : Equiv.Perm (Fin n)) : Type :=
  Quotient (MulAction.orbitRel (Subgroup.zpowers π) (Fin n))

lemma fixed_zpow {π : Equiv.Perm (Fin n)} (f : Fin n → Fin 2)
    (hf : ∀ i, f (π i) = f i) (k : ℤ) (i : Fin n) : f ((π ^ k) i) = f i := by
  induction k using Int.induction_on generalizing i with
  | zero => simp
  | succ k ih =>
      rw [zpow_add_one, Equiv.Perm.mul_apply, ih, hf]
  | pred k ih =>
      rw [zpow_sub_one, Equiv.Perm.mul_apply, ih]
      have h := hf (π⁻¹ i)
      simp only [Equiv.Perm.apply_inv_self] at h
      exact h.symm

/-- A fixed colouring is the same thing as a colouring of the components. -/
noncomputable def fixedColouringEquiv (π : Equiv.Perm (Fin n)) :
    FixedColouring π ≃ (Components π → Fin 2) where
  toFun f := Quotient.lift f.1 (by
    intro a b hab
    have hab' : a ∈ MulAction.orbit (Subgroup.zpowers π) b := hab
    obtain ⟨⟨g, hg⟩, rfl⟩ := hab'
    obtain ⟨k, rfl⟩ := Subgroup.mem_zpowers_iff.mp hg
    exact fixed_zpow f.1 f.2 k b)
  invFun g := ⟨fun i => g ⟦i⟧, by
    intro i
    have h : π i ∈ MulAction.orbit (Subgroup.zpowers π) i :=
      ⟨⟨π, Subgroup.mem_zpowers π⟩, rfl⟩
    exact congrArg g (Quotient.sound h)⟩
  left_inv f := by
    rfl
  right_inv g := by
    funext x
    induction x using Quotient.inductionOn
    rfl

/-- **Fixed-colouring count.** The trace of the permutation operator of `π` on
`(R²)^{⊗n}` (the number of fixed basis vectors) is `2 ^ (number of components)`. -/
theorem card_fixedColouring (π : Equiv.Perm (Fin n)) :
    Nat.card (FixedColouring π) = 2 ^ Nat.card (Components π) := by
  rw [Nat.card_congr (fixedColouringEquiv π), Nat.card_fun, Nat.card_eq_fintype_card,
    Fintype.card_fin]

/-- **Mass at q = 1.** Framing factor `2^n` times the normalised trace
`(fixed count) / 2^n` is `2 ^ (number of components)`. -/
theorem mass_at_one (π : Equiv.Perm (Fin n)) :
    (2 : ℚ) ^ n * ((Nat.card (FixedColouring π) : ℚ) / 2 ^ n)
      = 2 ^ Nat.card (Components π) := by
  rw [card_fixedColouring]
  push_cast
  exact mul_div_cancel₀ _ (pow_ne_zero _ two_ne_zero)

/-- **Equal masses at q = 1.** Two braids (possibly on different numbers of strands)
whose closures have the same number of components have equal categorical mass at
q = 1. -/
theorem mass_at_one_eq_of_components {m : ℕ} (π : Equiv.Perm (Fin n))
    (π' : Equiv.Perm (Fin m)) (h : Nat.card (Components π) = Nat.card (Components π')) :
    (2 : ℚ) ^ n * ((Nat.card (FixedColouring π) : ℚ) / 2 ^ n)
      = (2 : ℚ) ^ m * ((Nat.card (FixedColouring π') : ℚ) / 2 ^ m) := by
  rw [mass_at_one, mass_at_one, h]

/-- The framing factor `(1 + q²)^n q^(-n-2w)` of `def:mass-identity` is `2^n` at
q = 1, for every writhe. -/
theorem framing_factor_at_one (w : ℤ) :
    ((1 : ℝ) + 1 ^ 2) ^ n * (1 : ℝ) ^ (-(n : ℤ) - 2 * w) = 2 ^ n := by
  norm_num

/-! ## Part B -/

/-- `E₀ = m c_q² ℏ_q = m / (q (q - 1))` (`energy-scale-planck`). -/
theorem e0_eq (m q : ℝ) (hq : 1 < q) :
    m * (1 / (q - 1)) ^ 2 * (1 - 1 / q) = m / (q * (q - 1)) := by
  have h1 : q - 1 ≠ 0 := by linarith
  have h2 : q ≠ 0 := by linarith
  field_simp

/-- **The cell read as a mass.** Dividing the cell energy `2 E₀ log q` by `c_q²`
(`def:mass-energy`, `𝔈 = 𝔪 c_q²`) gives `2 m ℏ_q log q`. -/
theorem cell_mass_eq (m q : ℝ) (hq : 1 < q) :
    (2 * (m * (1 / (q - 1)) ^ 2 * (1 - 1 / q)) * Real.log q) / (1 / (q - 1)) ^ 2
      = 2 * m * (1 - 1 / q) * Real.log q := by
  have h1 : q - 1 ≠ 0 := by linarith
  field_simp

/-- **The mass reading vanishes at q = 1, to second order.** For `q ≥ 1`,
`0 ≤ ℏ_q log q ≤ (q - 1)²`. -/
theorem hbar_log_bounds (q : ℝ) (hq : 1 ≤ q) :
    0 ≤ (1 - 1 / q) * Real.log q ∧ (1 - 1 / q) * Real.log q ≤ (q - 1) ^ 2 := by
  have hq0 : 0 < q := by linarith
  have hlog0 : 0 ≤ Real.log q := Real.log_nonneg hq
  have hlog1 : Real.log q ≤ q - 1 := Real.log_le_sub_one_of_pos hq0
  have hh0 : 0 ≤ 1 - 1 / q := by
    rw [sub_nonneg, div_le_one hq0]; exact hq
  have hh1 : 1 - 1 / q ≤ q - 1 := by
    have : 1 - 1 / q = (q - 1) / q := by field_simp
    rw [this, div_le_iff₀ hq0]
    nlinarith
  refine ⟨mul_nonneg hh0 hlog0, ?_⟩
  calc (1 - 1 / q) * Real.log q ≤ (q - 1) * (q - 1) :=
        mul_le_mul hh1 hlog1 hlog0 (by linarith)
    _ = (q - 1) ^ 2 := by ring

/-- **The energy reading does not vanish at q = 1.** For `q > 1`, the cell energy
in units of `m`, `2 log q / (q (q - 1))`, is at least `2 / q²`. -/
theorem cell_energy_ratio_ge (q : ℝ) (hq : 1 < q) :
    2 / q ^ 2 ≤ 2 * Real.log q / (q * (q - 1)) := by
  have hq0 : 0 < q := by linarith
  have hq1 : 0 < q - 1 := by linarith
  -- log q ≥ 1 - 1/q = (q - 1)/q
  have hlog : (q - 1) / q ≤ Real.log q := by
    have h := Real.add_one_le_exp (-Real.log q)
    rw [Real.exp_neg, Real.exp_log hq0] at h
    have : (q - 1) / q = 1 - q⁻¹ := by field_simp
    rw [this]; linarith
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  have : 2 * (q * (q - 1)) = 2 * q ^ 2 * ((q - 1) / q) := by field_simp
  rw [this]
  have hq2 : 0 < 2 * q ^ 2 := by positivity
  nlinarith [mul_le_mul_of_nonneg_left hlog hq2.le]

end QOU.MassTheory.CategoricalMassAtOne
