/-
  The 4₁ ideal triangulation: two regular tetrahedra, and `volume = VOL_4_1`.

  Bean `qou-m015`, `qou-mlgp`, `qou-kmmr`.

  ═══ WHY 4₁ IS THE CLEAN CASE ═══

  SnapPy: `Manifold('4_1')` has **two** tetrahedra, and *both* have shape

      e^{iπ/3} = 1/2 + (√3/2)i

  — the **regular** ideal tetrahedron, all six dihedral angles `π/3`.  Two things
  follow, and they are what make this file short:

  * `|e^{iπ/3}| = 1`, so the shape is **on the unit circle**, where
    `KummerUnitCircle.blochWigner_lob_exp` already gives
    `BlochWigner_lob(e^{iθ}) = Cl₂(θ)` outright.  No radial argument needed.
  * hence `volume = 2·Cl₂(π/3)`, which is **exactly the corpus's existing
    `VOL_4_1`** (`QOU/Knot/FigureEightVolume.lean`, the `qou-yf47` exact-target
    repair).

  So this file closes a loop: the corpus's 4₁ volume *constant*, the 4₁
  *triangulation*, and the 4₁ volume *conjecture* (already machine-proved in-repo
  as `tendsto_log_kashaev_vol`) all now refer to the same object.

  ═══ THE SHAPE FIELD ═══

  `e^{iπ/3}` is a primitive 6th root of unity, root of `w² − w + 1` — the
  Eisenstein field `ℚ(√−3)`.  Contrast 5₂, whose shape field is `ℚ(√−23)`.  Both
  gluing systems reduce to their shape's minimal polynomial:

  | knot | shapes | field | edge equations reduce to |
  |---|---|---|---|
  | 4₁ | `(w, w)`, `w = e^{iπ/3}` | `ℚ(√−3)` | `w² − w + 1 = 0` |
  | 5₂ | `(y, 1/(1−y), y)` | `ℚ(√−23)` | `y³ − 2y² + 3y − 1 = 0` |

  ═══ ⚠ SCOPE, UNCHANGED ═══

  Nothing here says this is a triangulation *of* `S³ ∖ 4₁`.  That is Thurston
  hyperbolisation plus Mostow rigidity, needing hyperbolic 3-manifolds which
  neither Mathlib nor QOU has.  See `QOU/MathlibExt/IdealTriangulation.lean`.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [milnor1982]
-/
import QOU.MathlibExt.IdealTriangulation
import QOU.Knot.FigureEightVolume

namespace QOU.Knot.FigureEightTri

open Real Complex QOU.Archimedean QOU.MathlibExt

/-- The regular ideal tetrahedron's shape, `e^{iπ/3}`. -/
noncomputable def w : ℂ := Complex.exp (((π / 3 : ℝ) : ℂ) * Complex.I)

theorem w_cube : w ^ 3 = -1 := by
  have h1 : w ^ 3 = Complex.exp (3 * (((π / 3 : ℝ) : ℂ) * Complex.I)) := by
    unfold w; rw [← Complex.exp_nat_mul]; norm_num
  have h2 : (3 : ℂ) * (((π / 3 : ℝ) : ℂ) * Complex.I) = ((π : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [h1, h2]
  exact Complex.exp_pi_mul_I

theorem w_im_pos : 0 < w.im := by
  unfold w
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  simp only [Complex.add_im, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im,
    Complex.I_re, Complex.I_im, mul_zero, zero_add, mul_one, add_zero]
  exact Real.sin_pos_of_pos_of_lt_pi (by positivity) (by linarith [Real.pi_pos])

/-- `w + 1 ≠ 0`.  Note `w = −1` *does* satisfy `w³ = −1`, so the cube alone does
not rule it out — the imaginary part does. -/
theorem w_add_one_ne_zero : w + 1 ≠ 0 := by
  intro h
  have him : (w + 1).im = 0 := by rw [h]; simp
  simp only [Complex.add_im, Complex.one_im, add_zero] at him
  exact absurd him (ne_of_gt w_im_pos)

/-- **The minimal polynomial**: `w² − w + 1 = 0`, so the shape field is `ℚ(√−3)`. -/
theorem w_sq_sub : w ^ 2 - w + 1 = 0 := by
  have hfac : (w + 1) * (w ^ 2 - w + 1) = 0 := by
    have hr : (w + 1) * (w ^ 2 - w + 1) = w ^ 3 + 1 := by ring
    rw [hr, w_cube]; ring
  exact (mul_eq_zero.mp hfac).resolve_left w_add_one_ne_zero

theorem w_ne_zero : w ≠ 0 := Complex.exp_ne_zero _

theorem one_sub_w_ne_zero : (1 : ℂ) - w ≠ 0 :=
  QOU.Knot.IdealTet.one_sub_ne_zero w_im_pos

/-! ### The triangulation -/

/-- The regular ideal tetrahedron. -/
noncomputable def regularTet : IdealTetrahedron := .ofIm w w_im_pos

/-- **The 4₁ ideal triangulation**: two regular tetrahedra, per SnapPy. -/
noncomputable def figureEightTriangulation : IdealTriangulation 2 :=
  IdealTriangulation.const 2 regularTet

/-- All three dihedral angles of the regular tetrahedron are `π/3`. -/
theorem regularTet_angle₁ : regularTet.angle₁ = π / 3 := by
  show tetAngle₁ w = π / 3
  unfold tetAngle₁ w
  exact QOU.Knot.Kummer.arg_exp_mul_I
    ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩

/-- **`volume (4₁ triangulation) = VOL_4_1`.**

Direct from `blochWigner_lob_exp`: the shape is on the unit circle, so its volume
is `Cl₂(π/3)` with no further work, and there are two of them. -/
theorem figureEightTriangulation_volume :
    figureEightTriangulation.volume = QOU.Knot.FigureEightVolume.VOL_4_1 := by
  unfold figureEightTriangulation QOU.Knot.FigureEightVolume.VOL_4_1
  rw [IdealTriangulation.volume_const]
  show (2 : ℝ) * IdealTetrahedron.volume regularTet = _
  unfold IdealTetrahedron.volume regularTet
  show (2 : ℝ) * BlochWigner_lob w = _
  unfold w
  rw [QOU.Knot.Kummer.blochWigner_lob_exp (by positivity) (by linarith [Real.pi_pos])]

/-! ### The gluing equations

SnapPy's two 4₁ **edge** equations are `[2,1,0, 2,1,0]` and `[0,1,2, 0,1,2]`.
With both shapes `w` and parameters `(w, 1/(1−w), 1 − 1/w)`, they read
`w⁴/(1−w)² = 1` and `((1−w)/w²)² = 1`, and **both reduce to `w² − w + 1 = 0`** —
the shape's minimal polynomial, exactly as 5₂'s reduce to its cubic. -/

/-- **Edge 0**: `w⁴ · (1/(1−w))² = 1`. -/
theorem edge_zero : w ^ 4 * (1 / (1 - w)) ^ 2 = 1 := by
  have h := one_sub_w_ne_zero
  field_simp
  linear_combination (norm := ring_nf) (w ^ 2 + w - 1) * w_sq_sub

/-- **Edge 1**: `(1/(1−w)) · (1 − 1/w)² ` squared `= 1`. -/
theorem edge_one : ((1 / (1 - w)) * (1 - 1 / w) ^ 2) ^ 2 = 1 := by
  have h := one_sub_w_ne_zero
  have h0 := w_ne_zero
  field_simp
  linear_combination (norm := ring_nf)
    (-w ^ 4 + w ^ 3 + 2 * w ^ 2 - 3 * w + 1) * w_sq_sub

end QOU.Knot.FigureEightTri
