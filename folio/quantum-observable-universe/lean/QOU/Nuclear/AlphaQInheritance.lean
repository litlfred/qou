import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# Q-value of alpha emission: what is inherited from the binding law

For any binding function `B : ℤ → ℤ → R` (proton number, neutron number) over a
commutative ring and any alpha-cluster binding `Bα : R`, the alpha Q-value is

  `Q B Bα Z N = B (Z-2) (N-2) + Bα - B Z N`.

* `qalpha_error_split`: the difference of two such Q-values (a model and a
  reference) splits exactly into an alpha-cluster part `Bα - Bα'` and a part
  carried by the slope of the binding law along the alpha line.
* `qalpha_const_of_affine_isospin`: if `B Z N = c * (Z + N) + g (N - Z)` for any
  function `g`, then `Q` takes the single value `Bα - 4 c` at every `(Z, N)`.
  Such a law cannot separate alpha emitters from alpha-stable nuclei.

Pure algebra; no measured values appear. The numerical comparison lives in
`computations/probes/alpha_qalpha_inheritance/`.
-/

namespace QOU.Nuclear.AlphaQInheritance

variable {R : Type*} [CommRing R]

/-- Alpha Q-value of the parent `(Z, N)` for binding law `B` and cluster binding `Bα`. -/
def Q (B : ℤ → ℤ → R) (Bα : R) (Z N : ℤ) : R := B (Z - 2) (N - 2) + Bα - B Z N

/-- Binding slope along the alpha line: `B Z N - B (Z-2) (N-2)`. -/
def alphaSlope (B : ℤ → ℤ → R) (Z N : ℤ) : R := B Z N - B (Z - 2) (N - 2)

theorem Q_eq (B : ℤ → ℤ → R) (Bα : R) (Z N : ℤ) :
    Q B Bα Z N = Bα - alphaSlope B Z N := by
  unfold Q alphaSlope; ring

/-- Exact split of a Q-value error into the alpha-cluster part and the
inherited alpha-line-slope part. -/
theorem qalpha_error_split (B B' : ℤ → ℤ → R) (Bα Bα' : R) (Z N : ℤ) :
    Q B Bα Z N - Q B' Bα' Z N
      = (Bα - Bα') - (alphaSlope B Z N - alphaSlope B' Z N) := by
  unfold Q alphaSlope; ring

/-- A binding law that is affine in mass number plus any function of `N - Z`
has the constant alpha-line slope `4 c`. -/
theorem alphaSlope_affine_isospin (c : R) (g : ℤ → R) (Z N : ℤ) :
    alphaSlope (fun z n => c * ((z + n : ℤ) : R) + g (n - z)) Z N = 4 * c := by
  unfold alphaSlope
  have h : (N - 2) - (Z - 2) = N - Z := by ring
  simp only [h]
  push_cast
  ring

/-- Under such a law the alpha Q-value is one number for every parent. -/
theorem qalpha_const_of_affine_isospin (c Bα : R) (g : ℤ → R) (Z N Z' N' : ℤ) :
    Q (fun z n => c * ((z + n : ℤ) : R) + g (n - z)) Bα Z N
      = Q (fun z n => c * ((z + n : ℤ) : R) + g (n - z)) Bα Z' N' := by
  rw [Q_eq, Q_eq, alphaSlope_affine_isospin, alphaSlope_affine_isospin]

end QOU.Nuclear.AlphaQInheritance
