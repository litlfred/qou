import BraidKnotOctonion.GluingData
import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Shape parameters and the edge gluing equations, flat shapes allowed

A shape parameter is any `z ∈ ℂ ∖ {0, 1}`; its three edge parameters are `z`, `1/(1−z)` and
`1 − 1/z`, with product `−1`. The edge gluing equations `∏ param^exp = 1` are stated over
these. All of this is algebra over `ℂ`: no positivity, no volume.

Split out of `QOU/Transcendental/BraidKnotOctonion/FlatTetrahedra.lean` (strangler split,
bean `qou-dk7p`). The volume of a shape (the Bloch–Wigner function), the embedding of
`IdealTetrahedron` and the flat-volume theorems stay behind the boundary.

-- Ref: [thurston1978] Ch. 4
-- Ref: [neumann-zagier1985]
-/

namespace QOU.Knot.FlatTet

open QOU.MathlibExt

/-- A **shape parameter**: any `z ∈ ℂ ∖ {0,1}`.  Unlike `IdealTetrahedron` this does
**not** require `0 < Im z`, so flat (real) shapes are permitted. -/
structure Shape where
  /-- The shape parameter. -/
  z : ℂ
  /-- Excluded so the edge parameters are genuine units. -/
  ne_zero : z ≠ 0
  /-- Excluded so `1/(1−z)` is a genuine unit. -/
  ne_one : z ≠ 1

namespace Shape

variable (S : Shape)

theorem one_sub_ne_zero : (1 : ℂ) - S.z ≠ 0 := sub_ne_zero.mpr (Ne.symm S.ne_one)

/-- The three edge parameters, same convention as `IdealTetrahedron.param`. -/
noncomputable def param : Fin 3 → ℂ
  | 0 => S.z
  | 1 => 1 / (1 - S.z)
  | 2 => 1 - 1 / S.z

@[simp] theorem param_zero : S.param 0 = S.z := rfl
@[simp] theorem param_one : S.param 1 = 1 / (1 - S.z) := rfl
@[simp] theorem param_two : S.param 2 = 1 - 1 / S.z := rfl

/-- **Every edge parameter is nonzero** — from `z ≠ 0, 1` alone.

`IdealTriangulation.param_ne_zero` proves the same thing from `param_im_pos`, i.e. from
positivity.  Positivity is not what makes the parameters units. -/
theorem param_ne_zero : ∀ i, S.param i ≠ 0
  | 0 => S.ne_zero
  | 1 => by
      simp only [param_one]
      exact one_div_ne_zero S.one_sub_ne_zero
  | 2 => by
      simp only [param_two]
      intro h
      have h1 : (1 : ℂ) = 1 / S.z := sub_eq_zero.mp h
      rw [eq_div_iff S.ne_zero, one_mul] at h1
      exact S.ne_one h1

/-- **`z · z′ · z″ = −1`** — pure algebra, no positivity. -/
theorem param_prod : S.param 0 * S.param 1 * S.param 2 = -1 := by
  simp only [param_zero, param_one, param_two]
  have h0 := S.ne_zero
  have h1 := S.one_sub_ne_zero
  field_simp
  ring

/-- A shape is **flat** when it is real — the degenerate tetrahedron. -/
def IsFlat : Prop := S.z.im = 0

end Shape

/-- A collection of `n` shapes, flat ones allowed. -/
structure ShapedTriangulation (n : ℕ) where
  /-- The shapes. -/
  tet : Fin n → Shape

variable {n e : ℕ}

/-- **The edge gluing equations**, stated over possibly-flat shapes.  Same formula as
`MathlibExt.SatisfiesEdgeEquations`, without the positivity requirement. -/
def ShapedTriangulation.SatisfiesEdgeEquations
    (T : ShapedTriangulation n) (G : GluingData n e) : Prop :=
  ∀ k, (∏ i, ∏ j, (T.tet i).param j ^ G.exp k i j) = 1

/-! ### The trefoil shapes (SnapPy `3₁`: shapes `−1` and `2`) -/

/-- The trefoil's first shape, `z₀ = −1`.  **Rational**, hence flat. -/
noncomputable def trefoilShape₀ : Shape :=
  ⟨-1, by norm_num, by norm_num⟩

/-- The trefoil's second shape, `z₁ = 2`.  **Rational**, hence flat. -/
noncomputable def trefoilShape₁ : Shape :=
  ⟨2, by norm_num, by norm_num⟩

/-- The trefoil's two-tetrahedron shape data. -/
noncomputable def trefoilTriangulation : ShapedTriangulation 2 :=
  ⟨![trefoilShape₀, trefoilShape₁]⟩

end QOU.Knot.FlatTet
