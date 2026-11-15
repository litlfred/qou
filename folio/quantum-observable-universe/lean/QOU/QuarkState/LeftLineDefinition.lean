/-
# The left line (owner ruling, 2026-11-15) and its derived consequences

Bean `qou-wkcd` (epic `qou-qs0e`, blocks `qou-hlx7`). The owner's ruling, verbatim:
*"Define left = the line on which the positive-crossing generator σ acts with eigenvalue
of size > 1"*.

This is a DEFINITION, a named model term (`leftLine`). Everything else in this file is
derived from it. The definition needs an absolute value, so it lives over an ordered
field. On the generic fibre there is no such line, because the root relabelling
`q ↦ −q⁻¹` and bar both exchange the two candidates (`WeakChiralityRootLabel.lean`).

## Consequences proved here

0. **It is a function of the generator, not of the parameter label**
   (`leftLine_neg_inv`). Labelling the generator's eigenvalues by `q` or by `−q⁻¹` gives
   the same line when `|q| ≠ 1`. So the definition does not depend on the D-H1 labelling.
1. **Flavour-blind** (`flip_eigenline_left`). The inverse generator `σ⁻¹`, whose
   parameter is `q⁻¹`, has `leftLine q σ` as one of its own two eigenlines. So `u_L`
   and `d_L` lie on one line. The criterion is applied ONCE, to `σ`. Applying it to
   each letter separately is what entangled chirality with flavour (`modLine_flip`, 9a).
2. **The weak vertex** `weakVertex` is the one-sided flip that acts on the left line
   (`W_L` if `|q| > 1`, `W_R` otherwise). On the left line it acts as `σ⁻¹`
   (`weakVertex_mul_leftLine`). On the right line it acts as `σ`
   (`weakVertex_mul_rightLine`). So it changes flavour on the left line only.
3. **Universality**: one line, `leftLine q σ`, serves every flavour letter
   (`leftLine_eigen_sigma`, `leftLine_eigen_flip`).
4. **Regime dependence** (`leftLine_eq_Pp_iff`): `leftLine = P₊` iff `|q| > 1`, given
   the two lines are distinct. If `|q| < 1` held elsewhere, left would be `P₋` there.
5. **Mirror** (`leftLine_mirror`): the spatial mirror makes `σ⁻¹` the positive
   crossing, at parameter `q⁻¹`. Its left line is the original RIGHT line. So the
   handedness is (orientation of space) × (which side of `|q| = 1`).
6. **Well-posedness: "positive-crossing generator" excludes `−σ⁻¹`**
   (`neg_flip_ne_braid_image`). Suppose an index character `χ` exists, an algebra map
   sending each positive generator to `q > 0`; for `H_n(q)` this is `σ_i ↦ q`. Then
   every braid word maps to `q^{writhe} > 0`, while `−σ⁻¹` maps to `−q⁻¹ < 0`. So
   `−σ⁻¹` (the swap automorphism's image of `σ`) is the image of no braid word. The
   existence of `χ` on `H_n` is cited, not built here.

## Not established

That `weakVertex` IS the physical weak coupling (scope (a)). The definition fixes a
name; it does not identify any object with any physical one.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.WeakChiralityRootLabel

namespace QOU.QuarkState.LeftLine

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex
  QOU.QuarkState.WeakChiralityRootLabel

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Ring A] [Algebra K A]
variable {q : K} {σ : A}

/-- **Owner ruling 2026-11-15 (definition).** The left line is the eigenline on which the
positive-crossing generator `σ` (a letter at parameter `q`) acts with eigenvalue of size
`> 1`. At `|q| = 1` neither eigenvalue qualifies; the `else` branch is then only a
default, and the label-independence lemma below excludes that case. -/
noncomputable def leftLine (q : K) (σ : A) : A := modLine q σ

/-- The complementary (right) line. -/
noncomputable def rightLine (q : K) (σ : A) : A := if 1 < |q| then Pm q σ else Pp q σ

/-- The one-sided flip on the left line. -/
noncomputable def weakVertex (q : K) (σ : A) : A :=
  if 1 < |q| then oneSidedL q σ else oneSidedR q σ

theorem leftLine_of_one_lt (h : 1 < |q|) : leftLine q σ = Pp q σ := if_pos h

theorem leftLine_of_not_one_lt (h : ¬ 1 < |q|) : leftLine q σ = Pm q σ := if_neg h

theorem rightLine_of_one_lt (h : 1 < |q|) : rightLine q σ = Pm q σ := if_pos h

theorem rightLine_of_not_one_lt (h : ¬ 1 < |q|) : rightLine q σ = Pp q σ := if_neg h

theorem leftLine_add_rightLine (hq2 : q + q⁻¹ ≠ 0) :
    leftLine q σ + rightLine q σ = 1 := by
  by_cases h : 1 < |q|
  · rw [leftLine_of_one_lt h, rightLine_of_one_lt h, Pp_add_Pm hq2]
  · rw [leftLine_of_not_one_lt h, rightLine_of_not_one_lt h, add_comm, Pp_add_Pm hq2]

/-- **0. Label independence.** -/
theorem leftLine_neg_inv (hq : q ≠ 0) (h1 : |q| ≠ 1) :
    leftLine (-q⁻¹) σ = leftLine q σ :=
  modLine_neg_inv hq h1

/-- **1. Flavour-blind**: the left line of `σ` is an eigenline of `σ⁻¹`. -/
theorem flip_eigenline_left :
    leftLine q σ = Pp q⁻¹ (flip q σ) ∨ leftLine q σ = Pm q⁻¹ (flip q σ) := by
  by_cases h : 1 < |q|
  · left; rw [leftLine_of_one_lt h, flip_Pp]
  · right; rw [leftLine_of_not_one_lt h, flip_Pm]

/-- **3. Universality**, generator: `σ` acts on the left line by a scalar. -/
theorem leftLine_eigen_sigma (hq : q ≠ 0) (hs : IsLetter q σ) :
    ∃ c : K, σ * leftLine q σ = c • leftLine q σ := by
  by_cases h : 1 < |q|
  · exact ⟨q, by rw [leftLine_of_one_lt h, eigen_plus hq hs]⟩
  · exact ⟨-q⁻¹, by rw [leftLine_of_not_one_lt h, eigen_minus hq hs]⟩

/-- **3. Universality**, other flavour: `σ⁻¹` acts on the same line by a scalar. -/
theorem leftLine_eigen_flip (hq : q ≠ 0) (hs : IsLetter q σ) :
    ∃ c : K, flip q σ * leftLine q σ = c • leftLine q σ := by
  by_cases h : 1 < |q|
  · exact ⟨q⁻¹, by rw [leftLine_of_one_lt h, flip_eigen_plus hq hs]⟩
  · exact ⟨-q, by rw [leftLine_of_not_one_lt h, flip_eigen_minus hq hs]⟩

/-- **2. On the left line the weak vertex acts as `σ⁻¹`** (it changes flavour there). -/
theorem weakVertex_mul_leftLine (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    weakVertex q σ * leftLine q σ = flip q σ * leftLine q σ := by
  unfold weakVertex
  by_cases h : 1 < |q|
  · rw [if_pos h, leftLine_of_one_lt h, oneSidedL_mul_Pp hq hq2 hs, flip_eigen_plus hq hs]
  · rw [if_neg h, leftLine_of_not_one_lt h, oneSidedR_mul_Pm hq hq2 hs,
      flip_eigen_minus hq hs]

/-- **2. On the right line the weak vertex acts as `σ`** (no flavour change). -/
theorem weakVertex_mul_rightLine (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    weakVertex q σ * rightLine q σ = σ * rightLine q σ := by
  unfold weakVertex
  by_cases h : 1 < |q|
  · rw [if_pos h, rightLine_of_one_lt h, oneSidedL_mul_Pm hq hq2 hs, eigen_minus hq hs]
  · rw [if_neg h, rightLine_of_not_one_lt h, oneSidedR_mul_Pp hq hq2 hs, eigen_plus hq hs]

/-- **4. Regime dependence**: `leftLine = P₊` iff `|q| > 1`. -/
theorem leftLine_eq_Pp_iff (hne : Pp q σ ≠ Pm q σ) : leftLine q σ = Pp q σ ↔ 1 < |q| := by
  by_cases h : 1 < |q|
  · simp [leftLine_of_one_lt h, h]
  · rw [leftLine_of_not_one_lt h]
    exact ⟨fun e => absurd e.symm hne, fun e => absurd e h⟩

/-- **5. Mirror**: with `σ⁻¹` as the positive crossing (parameter `q⁻¹`), the left line
is the original right line. -/
theorem leftLine_mirror (h1 : |q| ≠ 1) (hq : q ≠ 0) :
    leftLine q⁻¹ (flip q σ) = rightLine q σ := by
  have hpos : 0 < |q| := abs_pos.mpr hq
  by_cases h : 1 < |q|
  · have : ¬ 1 < |q⁻¹| := by
      rw [abs_inv]; exact not_lt.mpr (inv_lt_one_of_one_lt₀ h).le
    rw [leftLine_of_not_one_lt this, rightLine_of_one_lt h, flip_Pm]
  · have hlt : |q| < 1 := lt_of_le_of_ne (not_lt.mp h) h1
    have : 1 < |q⁻¹| := by rw [abs_inv]; exact (one_lt_inv₀ hpos).mpr hlt
    rw [leftLine_of_one_lt this, rightLine_of_not_one_lt h, flip_Pp]

/-! ### 6. `−σ⁻¹` is not the image of any braid word -/

/-- An index character sends `σ⁻¹` to `q⁻¹`. -/
theorem index_flip (χ : A →ₐ[K] K) (hχ : χ σ = q) : χ (flip q σ) = q⁻¹ := by
  unfold Helicity.flip
  rw [map_sub, hχ, map_smul, map_one, smul_eq_mul, mul_one]
  ring

/-- Every product of letters valued `q` or `q⁻¹` by the index character is positive. -/
theorem index_prod_pos (χ : A →ₐ[K] K) (hq : 0 < q) (l : List A)
    (hl : ∀ y ∈ l, χ y = q ∨ χ y = q⁻¹) : 0 < χ l.prod := by
  induction l with
  | nil => simp
  | cons a t ih =>
    rw [List.prod_cons, map_mul]
    have ht : 0 < χ t.prod := ih fun y hy => hl y (List.mem_cons_of_mem a hy)
    rcases hl a List.mem_cons_self with h | h <;> rw [h]
    · exact mul_pos hq ht
    · exact mul_pos (inv_pos.mpr hq) ht

/-- **Well-posedness.** Given an index character with `χ σ = q > 0`, no braid word
(a product of letters each sent to `q` or `q⁻¹`) equals `−σ⁻¹`. -/
theorem neg_flip_ne_braid_image (χ : A →ₐ[K] K) (hq : 0 < q) (hχ : χ σ = q) (l : List A)
    (hl : ∀ y ∈ l, χ y = q ∨ χ y = q⁻¹) : l.prod ≠ -flip q σ := by
  intro h
  have hp := index_prod_pos χ hq l hl
  rw [h, map_neg, index_flip χ hχ] at hp
  have : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

end QOU.QuarkState.LeftLine
