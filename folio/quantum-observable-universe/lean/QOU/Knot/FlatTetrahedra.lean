/-
  Flat tetrahedra: the gluing equations stated as generally as they are true, and the
  trefoil as a worked degenerate example.

  Beans `qou-m015`, `qou-mlgp`.

  ═══ WHY THIS MODULE EXISTS ═══

  `QOU/MathlibExt/IdealTriangulation.lean` builds everything on `IdealTetrahedron`, whose
  structure field `im_pos : 0 < shape.im` **excludes flat shapes by construction**.  For
  angles and volume that is right — `angle_sum`, `law_of_sines` and `kummer` all genuinely
  need positivity.  For the **gluing equations** it is too strong, and the cost is
  concrete:

  > the fact that the trefoil's flat shapes satisfy its edge equations was not statable.

  Route 75's gate G5 verifies exactly that fact in Python, and it is the sharpest thing
  that lane established:

  * the trefoil `3₁` is a torus knot — Seifert fibred, **not** hyperbolic;
  * its shapes are `z₀ = −1`, `z₁ = 2` — **rational**, both real;
  * they satisfy **every** gluing equation exactly;
  * and the volume is `0`, because every tetrahedron is flat.

  So **the gluing equations alone do not detect hyperbolicity.**  A degenerate solution
  exists and the equations are perfectly happy with it.  What fails is `Im z > 0`.  This
  module makes that statement, and its proof, available in Lean.

  ═══ WHAT GENERALISES AND WHAT DOES NOT ═══

  | statement | needs |
  |---|---|
  | `param`, `param_ne_zero`, `param_prod` (`z z′ z″ = −1`) | `z ≠ 0`, `z ≠ 1` only |
  | `SatisfiesEdgeEquations` | `z ≠ 0`, `z ≠ 1` only |
  | volume `= 0` at a flat shape | `Im z = 0` |
  | `angle_sum`, `law_of_sines`, `kummer`, `SatisfiesAngleEquations` | `Im z > 0`, genuinely |

  The split is the mathematical content, not a packaging choice: the **edge** equations
  descend to flat shapes, the **angle** equations do not.  That is exactly why positivity
  is the hyperbolicity detector and the equations are not.

  ═══ ⚠ SCOPE, UNCHANGED ═══

  Nothing here says any of this is a triangulation *of* a manifold.  That is Thurston
  hyperbolisation plus Mostow rigidity — see `QOU/MathlibExt/IdealTriangulation.lean`.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985]
-/
import QOU.MathlibExt.IdealTriangulation

namespace QOU.Knot.FlatTet

open Real Complex QOU.Archimedean QOU.MathlibExt

/-! ## §1 — a flat tetrahedron has zero volume, for **every** real shape

`QOU/Archimedean/BlochWignerLobachevsky.lean` has `BlochWigner_lob_real_eq_zero`, but
only for `0 < x < 1`.  The trefoil's shapes are `−1` and `2`, both outside that range, so
the restricted form cannot see them.  The vanishing in fact needs no hypothesis at all. -/

/-- The argument of a real number is `0` or `π` — never anything else.  This is the whole
reason a flat tetrahedron has zero volume: `Λ` vanishes at both. -/
theorem arg_ofReal_zero_or_pi (r : ℝ) :
    ((r : ℂ)).arg = 0 ∨ ((r : ℂ)).arg = π := by
  rcases lt_or_ge r 0 with h | h
  · exact Or.inr (Complex.arg_ofReal_of_neg h)
  · exact Or.inl (Complex.arg_ofReal_of_nonneg h)

/-- **A real shape parameter gives zero volume — unconditionally.**

Generalises `BlochWigner_lob_real_eq_zero`, which assumed `0 < x < 1`.  No hypothesis is
needed, and that includes the two junk-value cases: at `x = 1` Lean's `1/0 = 0` makes
`1/(1−x) = 0`, and at `x = 0` it makes `1 − 1/x = 1`; both give `arg = 0`, so the formula
still returns `0`. -/
theorem BlochWigner_lob_ofReal (x : ℝ) : BlochWigner_lob (x : ℂ) = 0 := by
  have h2 : (1 : ℂ) / (1 - (x : ℂ)) = ((1 / (1 - x) : ℝ) : ℂ) := by push_cast; ring
  have h3 : (1 : ℂ) - 1 / (x : ℂ) = ((1 - 1 / x : ℝ) : ℂ) := by push_cast; ring
  refine BlochWigner_lob_eq_zero_of_angles _ (arg_ofReal_zero_or_pi x) ?_ ?_
  · show tetAngle₂ (x : ℂ) = 0 ∨ tetAngle₂ (x : ℂ) = π
    unfold tetAngle₂; rw [h2]; exact arg_ofReal_zero_or_pi _
  · show tetAngle₃ (x : ℂ) = 0 ∨ tetAngle₃ (x : ℂ) = π
    unfold tetAngle₃; rw [h3]; exact arg_ofReal_zero_or_pi _

/-- **Flat ⇒ zero volume**, in the form the geometry layer wants: a shape with vanishing
imaginary part contributes nothing. -/
theorem BlochWigner_lob_eq_zero_of_im_eq_zero {z : ℂ} (hz : z.im = 0) :
    BlochWigner_lob z = 0 := by
  have : z = ((z.re : ℝ) : ℂ) := by
    apply Complex.ext <;> simp [hz]
  rw [this]
  exact BlochWigner_lob_ofReal _

/-! ## §2 — shapes without a positivity requirement

`Shape` is `IdealTetrahedron` minus `im_pos`: any `z ∈ ℂ ∖ {0, 1}`.  Flat shapes are
allowed, which is the entire point. -/

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

/-- The volume contributed by this shape.  Defined for flat shapes too, where it is `0`. -/
noncomputable def volume : ℝ := BlochWigner_lob S.z

/-- A shape is **flat** when it is real — the degenerate tetrahedron. -/
def IsFlat : Prop := S.z.im = 0

/-- **A flat shape has zero volume.** -/
theorem volume_eq_zero_of_flat (h : S.IsFlat) : S.volume = 0 :=
  BlochWigner_lob_eq_zero_of_im_eq_zero h

end Shape

/-- Every `IdealTetrahedron` is a `Shape` — the positivity requirement is dropped, not
contradicted, so all existing results remain available. -/
noncomputable def _root_.QOU.MathlibExt.IdealTetrahedron.toShape
    (T : IdealTetrahedron) : Shape :=
  ⟨T.shape, T.shape_ne_zero, fun h => by
    have := T.im_pos; rw [h] at this; simp at this⟩

@[simp] theorem toShape_z (T : IdealTetrahedron) : T.toShape.z = T.shape := rfl

/-- The two `param`s agree, so nothing proved about `IdealTetrahedron.param` is lost. -/
theorem toShape_param (T : IdealTetrahedron) : ∀ i, T.toShape.param i = T.param i
  | 0 => rfl
  | 1 => rfl
  | 2 => rfl

/-! ## §3 — the gluing equations, over shapes that may be flat -/

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

/-- Total volume — well defined with flat shapes present, which contribute `0`. -/
noncomputable def ShapedTriangulation.volume (T : ShapedTriangulation n) : ℝ :=
  ∑ i, (T.tet i).volume

/-- **If every shape is flat the total volume is zero.** -/
theorem ShapedTriangulation.volume_eq_zero_of_flat (T : ShapedTriangulation n)
    (h : ∀ i, (T.tet i).IsFlat) : T.volume = 0 := by
  unfold ShapedTriangulation.volume
  exact Finset.sum_eq_zero fun i _ => (T.tet i).volume_eq_zero_of_flat (h i)

/-! ## §4 — the trefoil, worked

SnapPy's `3₁` triangulation has two tetrahedra with shapes `−1` and `2`, and edge
exponent rows `[1,2,2, 2,1,2]` and `[1,0,0, 0,1,0]`.  Both edge equations hold, both
shapes are flat, and the volume is `0`. -/

/-- The trefoil's first shape, `z₀ = −1`.  **Rational**, hence flat. -/
noncomputable def trefoilShape₀ : Shape :=
  ⟨-1, by norm_num, by norm_num⟩

/-- The trefoil's second shape, `z₁ = 2`.  **Rational**, hence flat. -/
noncomputable def trefoilShape₁ : Shape :=
  ⟨2, by norm_num, by norm_num⟩

/-- The trefoil's two-tetrahedron shape data. -/
noncomputable def trefoilTriangulation : ShapedTriangulation 2 :=
  ⟨![trefoilShape₀, trefoilShape₁]⟩

/-- **Trefoil edge equation 0**, exponents `[1,2,2, 2,1,2]`:
`z₀ · (z₀′)² · (z₀″)² · (z₁)² · z₁′ · (z₁″)² = 1`. -/
theorem trefoil_edge_zero :
    trefoilShape₀.param 0 * trefoilShape₀.param 1 ^ 2 * trefoilShape₀.param 2 ^ 2
      * (trefoilShape₁.param 0 ^ 2 * trefoilShape₁.param 1 * trefoilShape₁.param 2 ^ 2)
      = 1 := by
  simp only [Shape.param_zero, Shape.param_one, Shape.param_two,
    trefoilShape₀, trefoilShape₁]
  norm_num

/-- **Trefoil edge equation 1**, exponents `[1,0,0, 0,1,0]`: `z₀ · z₁′ = (−1)(−1) = 1`. -/
theorem trefoil_edge_one :
    trefoilShape₀.param 0 * trefoilShape₁.param 1 = 1 := by
  simp only [Shape.param_zero, Shape.param_one, trefoilShape₀, trefoilShape₁]
  norm_num

/-- Both trefoil shapes are flat. -/
theorem trefoil_flat : ∀ i, (trefoilTriangulation.tet i).IsFlat := by
  intro i
  fin_cases i <;>
    simp [trefoilTriangulation, Shape.IsFlat, trefoilShape₀, trefoilShape₁]

/-- **The trefoil triangulation has volume zero** — every tetrahedron is flat. -/
theorem trefoil_volume_zero : trefoilTriangulation.volume = 0 :=
  trefoilTriangulation.volume_eq_zero_of_flat trefoil_flat

/-- **The headline, stated as one theorem: the edge equations do not detect
hyperbolicity.**

The trefoil complement is Seifert fibred, not hyperbolic, yet its shapes satisfy the edge
equations and have volume `0`.  So satisfying the gluing equations is *not* sufficient for
a geometric solution — positivity of the imaginary parts is the missing condition, and it
is exactly what `IdealTetrahedron.im_pos` supplies. -/
theorem edge_equations_do_not_detect_hyperbolicity :
    (trefoilShape₀.param 0 * trefoilShape₁.param 1 = 1)
      ∧ (∀ i, (trefoilTriangulation.tet i).IsFlat)
      ∧ trefoilTriangulation.volume = 0 :=
  ⟨trefoil_edge_one, trefoil_flat, trefoil_volume_zero⟩

end QOU.Knot.FlatTet
