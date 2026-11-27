import Mathlib.Tactic
import QOU.MassTheory.ColorSpectralCubicGeometry
import QOU.MassTheory.DilationBranchLocusRigidity
import QOU.MassTheory.PalindromicInvolutionLift
import QOU.MassTheory.MoebiusThreePointRigidity

/-!
# The stabiliser of the colour branch locus, in homogeneous coordinates

Issue #9083, part 2. The W1 wall (bean `qou-d8de`) asks which base automorphisms
preserve the branch locus `B` of the colour cubic. The corpus answers it in the affine
`z`-line, one map shape per file:

* `DilationBranchLocusRigidity.dilation_scaling_rigid` — `z ↦ l·z` (#6769);
* `PalindromicInvolutionLift.inversion_rigid` — `z ↦ l/z` (#7185);
* `MoebiusThreePointRigidity.moebius_id_of_three_fixed` — a general Möbius map with
  three fixed points, whose header notes that "a fixed point at `∞` needs a chart".

On `ℙ¹` with coordinates `[z:w]` these are one question about a `2×2` matrix acting
on the binary sextic

  `D(z,w) = 16z⁶ + 24z⁵w + 35z⁴w² + 50z³w³ + 35z²w⁴ + 24zw⁵ + 16w⁶`.

## What is proved

* `sextic_swap` — `D(z,w) = D(w,z)` over any commutative ring. This is the palindromic
  symmetry `z⁶D(1/z) = D(z)` without the hypothesis `z ≠ 0`.
* `sextic_dehom`, `sextic_infinity` — `D(z,1)` is the corpus `branchSextic z`, and
  `D(1,0) = 16 ≠ 0`, so `∞` is an ordinary point and not a branch point.
* `diagonal_rigid` — `diag(α, β)` with `α ≠ 0` preserves `D` up to a scalar only if
  `β = α`. The two corpus results are this lemma read on the two coordinates:
  `dilation_rigid_of_diagonal` and `inversion_rigid_of_diagonal` re-derive
  `dilation_scaling_rigid` and `inversion_rigid` from it, because an inversion is the
  swap (which fixes `D`) composed with a diagonal map.
* `binaryQuadratic_zero_of_three_lines` and `scalar_of_three_eigenlines` — a `2×2`
  matrix with three pairwise independent eigenvectors is scalar. A fixed point of the
  Möbius map is an eigenline, so this is three-point rigidity including fixed points
  at `∞`. `moebius_id_of_three_fixed_of_eigenlines` re-derives the affine statement by
  setting `w = 1`.

What stays prose, as in the corpus: that an automorphism of the colour curve covering
a base map permutes `B` (the covering step).
-/

namespace QOU.Mass.BranchLocusStabiliser

section Sextic
variable {R : Type*} [CommRing R]

/-- The colour branch sextic as a binary form. -/
def sextic (z w : R) : R :=
  16*z^6 + 24*z^5*w + 35*z^4*w^2 + 50*z^3*w^3 + 35*z^2*w^4 + 24*z*w^5 + 16*w^6

/-- **The palindromic symmetry is the coordinate swap.** No `z ≠ 0` hypothesis. -/
theorem sextic_swap (z w : R) : sextic z w = sextic w z := by unfold sextic; ring

/-- The affine chart `w = 1` gives the corpus sextic. -/
theorem sextic_dehom (z : R) :
    sextic z 1 = ColorSpectralCubicGeometry.branchSextic z := by
  unfold sextic ColorSpectralCubicGeometry.branchSextic; ring

/-- At `∞ = [1:0]` the sextic is `16`: `∞` is not a branch point. -/
theorem sextic_infinity : sextic (1 : R) 0 = 16 := by unfold sextic; ring

/-- Homogeneity of degree six. -/
theorem sextic_smul (c z w : R) : sextic (c*z) (c*w) = c^6 * sextic z w := by
  unfold sextic; ring

end Sextic

section Diagonal
variable {K : Type*} [Field K] [CharZero K]

/-- **Diagonal rigidity.** Under `diag(α, β)` the sextic's coefficients of `z⁶` and
`z⁵w` become `16α⁶` and `24α⁵β`. If these are `c·16` and `c·24` and `α ≠ 0`, then
`β = α`: the map is a scalar on `ℙ¹`. -/
theorem diagonal_rigid {α β c : K} (hα : α ≠ 0)
    (h6 : 16 * α^6 = c * 16) (h5 : 24 * α^5 * β = c * 24) : β = α := by
  have hc : c = α^6 := by linear_combination -h6 / 16
  subst hc
  have : α^5 * (β - α) = 0 := by linear_combination h5 / 24
  rcases mul_eq_zero.mp this with h | h
  · exact absurd (pow_eq_zero_iff (by norm_num) |>.mp h) hα
  · linear_combination h

open Polynomial in
/-- `dilation_scaling_rigid` from `diagonal_rigid`: `z ↦ l z` is `diag(l, 1)` read on
the coordinate `w` (constant term and linear term of the dehomogenised sextic). -/
theorem dilation_rigid_of_diagonal (l c : K)
    (h : (DilationBranchLocusRigidity.branchSexticPoly : K[X]).comp (C l * X)
      = C c * DilationBranchLocusRigidity.branchSexticPoly) :
    l = 1 ∧ c = 1 := by
  rw [DilationBranchLocusRigidity.branchSexticPoly_comp_scale,
    DilationBranchLocusRigidity.C_mul_branchSexticPoly] at h
  have h0 := congrArg (fun p : K[X] => p.coeff 0) h
  have h1 := congrArg (fun p : K[X] => p.coeff 1) h
  simp only [coeff_add, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C] at h0 h1
  norm_num at h0 h1
  have hl : l = 1 := diagonal_rigid (α := (1 : K)) (β := l) (c := c) one_ne_zero
    (by rw [h0]; ring) (by linear_combination h1)
  exact ⟨hl, h0⟩

open Polynomial in
/-- `inversion_rigid` from `diagonal_rigid`: `z ↦ l/z` is the swap (which fixes the
sextic, `sextic_swap`) followed by `diag(l, 1)`, read on the top two coefficients. -/
theorem inversion_rigid_of_diagonal (l c : K)
    (h : (PalindromicInvolutionLift.invSexticPoly l : K[X])
      = C c * DilationBranchLocusRigidity.branchSexticPoly) :
    l = 1 ∧ c = 1 := by
  rw [DilationBranchLocusRigidity.C_mul_branchSexticPoly] at h
  have h6 := congrArg (fun p : K[X] => p.coeff 6) h
  have h5 := congrArg (fun p : K[X] => p.coeff 5) h
  unfold PalindromicInvolutionLift.invSexticPoly at h6 h5
  simp only [coeff_add, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C] at h6 h5
  norm_num at h6 h5
  have hl : l = 1 := diagonal_rigid (α := (1 : K)) (β := l) (c := c) one_ne_zero
    (by rw [h6]; ring) (by linear_combination h5)
  exact ⟨hl, h6⟩

end Diagonal

section Eigenlines
variable {K : Type*} [Field K]

/-- **A binary quadratic with three pairwise independent zeros vanishes.** The lines
`[zᵢ : wᵢ]` may include `∞ = [1:0]`; no chart is chosen. Cramer's rule on the
`3×3` system, whose determinant is the product of the three `2×2` minors. -/
theorem binaryQuadratic_zero_of_three_lines {A B C z₁ w₁ z₂ w₂ z₃ w₃ : K}
    (h12 : z₁*w₂ - z₂*w₁ ≠ 0) (h13 : z₁*w₃ - z₃*w₁ ≠ 0) (h23 : z₂*w₃ - z₃*w₂ ≠ 0)
    (e₁ : A*z₁^2 + B*z₁*w₁ + C*w₁^2 = 0)
    (e₂ : A*z₂^2 + B*z₂*w₂ + C*w₂^2 = 0)
    (e₃ : A*z₃^2 + B*z₃*w₃ + C*w₃^2 = 0) :
    A = 0 ∧ B = 0 ∧ C = 0 := by
  have hΔ : (z₁*w₂ - z₂*w₁) * (z₁*w₃ - z₃*w₁) * (z₂*w₃ - z₃*w₂) ≠ 0 :=
    mul_ne_zero (mul_ne_zero h12 h13) h23
  have hA : A * ((z₁*w₂ - z₂*w₁) * (z₁*w₃ - z₃*w₁) * (z₂*w₃ - z₃*w₂)) = 0 := by
    linear_combination (w₂*w₃*(z₂*w₃ - z₃*w₂)) * e₁ - (w₁*w₃*(z₁*w₃ - z₃*w₁)) * e₂
      + (w₁*w₂*(z₁*w₂ - z₂*w₁)) * e₃
  have hB : B * ((z₁*w₂ - z₂*w₁) * (z₁*w₃ - z₃*w₁) * (z₂*w₃ - z₃*w₂)) = 0 := by
    linear_combination (-(z₂*w₃ - z₃*w₂)*(z₂*w₃ + z₃*w₂)) * e₁
      + ((z₁*w₃ - z₃*w₁)*(z₁*w₃ + z₃*w₁)) * e₂
      - ((z₁*w₂ - z₂*w₁)*(z₁*w₂ + z₂*w₁)) * e₃
  have hC : C * ((z₁*w₂ - z₂*w₁) * (z₁*w₃ - z₃*w₁) * (z₂*w₃ - z₃*w₂)) = 0 := by
    linear_combination (z₂*z₃*(z₂*w₃ - z₃*w₂)) * e₁ - (z₁*z₃*(z₁*w₃ - z₃*w₁)) * e₂
      + (z₁*z₂*(z₁*w₂ - z₂*w₁)) * e₃
  exact ⟨(mul_eq_zero.mp hA).resolve_right hΔ, (mul_eq_zero.mp hB).resolve_right hΔ,
    (mul_eq_zero.mp hC).resolve_right hΔ⟩

/-- **Three eigenlines force a scalar.** `[z:w]` is fixed by `M = (a b; c d)` exactly
when `M(z,w)` is proportional to `(z,w)`, i.e. `(a z + b w) w = (c z + d w) z`. Three
pairwise independent fixed lines force `b = c = 0` and `d = a`. -/
theorem scalar_of_three_eigenlines {a b c d z₁ w₁ z₂ w₂ z₃ w₃ : K}
    (h12 : z₁*w₂ - z₂*w₁ ≠ 0) (h13 : z₁*w₃ - z₃*w₁ ≠ 0) (h23 : z₂*w₃ - z₃*w₂ ≠ 0)
    (f₁ : (a*z₁ + b*w₁) * w₁ = (c*z₁ + d*w₁) * z₁)
    (f₂ : (a*z₂ + b*w₂) * w₂ = (c*z₂ + d*w₂) * z₂)
    (f₃ : (a*z₃ + b*w₃) * w₃ = (c*z₃ + d*w₃) * z₃) :
    c = 0 ∧ d = a ∧ b = 0 := by
  obtain ⟨hA, hB, hC⟩ := binaryQuadratic_zero_of_three_lines (A := c) (B := d - a) (C := -b)
    h12 h13 h23 (by linear_combination -f₁) (by linear_combination -f₂)
    (by linear_combination -f₃)
  exact ⟨hA, by linear_combination hB, by linear_combination -hC⟩

/-- `moebius_id_of_three_fixed` is the chart `w = 1` of `scalar_of_three_eigenlines`. -/
theorem moebius_id_of_three_fixed_of_eigenlines (a b c d x y z : K)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hx : a * x + b = x * (c * x + d))
    (hy : a * y + b = y * (c * y + d))
    (hz : a * z + b = z * (c * z + d)) :
    c = 0 ∧ d = a ∧ b = 0 :=
  scalar_of_three_eigenlines (w₁ := 1) (w₂ := 1) (w₃ := 1)
    (by simpa using sub_ne_zero.mpr hxy) (by simpa using sub_ne_zero.mpr hxz)
    (by simpa using sub_ne_zero.mpr hyz)
    (by linear_combination hx) (by linear_combination hy) (by linear_combination hz)

end Eigenlines

end QOU.Mass.BranchLocusStabiliser
