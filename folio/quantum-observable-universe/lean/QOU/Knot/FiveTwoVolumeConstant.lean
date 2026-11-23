/-
  `VOL_5_2` — the exact transcendental constant, in two equivalent forms.

  Bean `qou-kmmr` / `qou-m015`.

  ═══ WHY THIS FILE EXISTS: THE 4₁ PRECEDENT ═══

  `QOU/Knot/FigureEightVolumeLiterature.lean` records the lesson bluntly.  The
  figure-eight volume conjecture could not be stated truthfully while `VOL_4_1`
  was "a truncated rational decimal ≈ 1e-30 away from `2·Cl₂(π/3)`, **making the
  statement literally false**".  Bean `qou-yf47` repaired it by *defining*

      VOL_4_1 := 2 · Cl₂(π/3)

  — the exact transcendental target — after which the limit theorem became
  statable, and then provable.

  **5₂ has no such constant.**  What the corpus holds is a decimal from SnapPy
  (`qou-mass/_internal/knot_volumes.py`, `_SNAPPY_HP_50`) and, in Lean,
  either decimal literals (`MassDerivation.vol_figure_eight`) or the outright
  placeholder `HyperbolicVolume : Knot → ℝ := fun k => 0 * (k : ℝ)`
  (`AppendixSurreals/Conjectures.lean`).  Any exact statement about `Vol(5₂)`
  written against those is false or vacuous, for exactly the reason `qou-yf47`
  identified.

  This file supplies the missing constant, in the same style.

  ═══ WHAT IS DEFINED, AND WHAT IS PROVED ═══

  `fiveTwoShape` — the root of `X³ − 2X² + 3X − 1` with positive imaginary part,
  built from `SaddleRoots.ofRealRoot` on the real root supplied by the
  intermediate value theorem.  `VOL_5_2 := 3 · BlochWigner_lob fiveTwoShape`.

  Proved here:

  * `fiveTwoShape_cubic`, `fiveTwoShape_im_pos` — it really is that root;
  * `VOL_5_2_eq_dilog` — **the payoff**, immediate from `KummerRadial.kummer`:

        VOL_5_2 = 3 · ( Im (cLiTwoExt y₁) + log‖y₁‖ · arg(1 − y₁) )

    so the constant has both an *angle* form (Lobachevsky, geometric) and a
    *dilogarithm* form (analytic).  Before Kummer, writing both and calling them
    equal would have been exactly the transport `BlochWignerLobachevsky.lean`
    forbade.

  ═══ ⚠ WHAT IS **NOT** PROVED ═══

  **That `VOL_5_2` is the hyperbolic volume of the 5₂ knot complement.**  That is
  the *geometric* factor, cited to the literature exactly as `VOL_4_1` cites
  Thurston/Milnor.

  The gap has been *narrowed but not closed*.  `QOU/MathlibExt/IdealTriangulation.lean`
  now supplies `IdealTetrahedron` / `IdealTriangulation` with a `volume`, so
  `fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2` **is** a
  theorem about a defined object (below).  What is still missing is the step from
  a triangulation to a **topological 3-manifold** — Thurston hyperbolisation plus
  Mostow rigidity — which needs hyperbolic 3-manifolds, which neither Mathlib nor
  QOU has.  So `Vol(S³ ∖ 5₂) = …` remains a sentence with no subject.
  Beans `qou-m015` / `qou-krvm`.

  Numerically `VOL_5_2 = 2.8281220883307831627638988092766349427709813173006…`,
  agreeing with the corpus's SnapPy HP 50-dps constant to its full recorded
  precision (Route 71, residual `4.9e-50`) and extended there to 79 dps.  That
  agreement is a **control on the definition**, not a proof of the geometric
  identification.

  Nor is the 5₂ **volume conjecture** (the Kashaev asymptotic) touched: that is
  Ohtsuki, *Quantum Topol.* **7** (2016) 669–735, and is not formalised here.

  -- Ref: [thurston1978], [milnor1982], [neumann-zagier1985]
  -- Ref: [ohtsuki2016] https://doi.org/10.4171/QT/83
-/
import QOU.Knot.KummerRadial
import QOU.QBeta.FiveTwoComplexPentagon
import QOU.MathlibExt.IdealTriangulation

namespace QOU.Knot.FiveTwoVolume

open Real Complex QOU.Archimedean QOU.QBeta.FiveTwoComplexPentagon

/-! ### The shape -/

/-- The real root of the saddle cubic in `(0,1)`, from the intermediate value
theorem. -/
noncomputable def realRoot : ℝ := Classical.choose SaddleRoots.exists_real_root

theorem realRoot_spec :
    0 < realRoot ∧ realRoot < 1 ∧ realRoot ^ 3 - 2 * realRoot ^ 2 + 3 * realRoot - 1 = 0 :=
  Classical.choose_spec SaddleRoots.exists_real_root

/-- The 5₂ root data, built from that real root. -/
noncomputable def saddle : SaddleRoots :=
  SaddleRoots.ofRealRoot realRoot_spec.1 realRoot_spec.2.1 realRoot_spec.2.2

/-- **The 5₂ shape parameter** `y₁`: the root of `X³ − 2X² + 3X − 1` with
positive imaginary part. -/
noncomputable def fiveTwoShape : ℂ := saddle.a

theorem fiveTwoShape_im_pos : 0 < fiveTwoShape.im := saddle.him

theorem fiveTwoShape_cubic :
    fiveTwoShape ^ 3 - 2 * fiveTwoShape ^ 2 + 3 * fiveTwoShape - 1 = 0 :=
  saddle.cubic_a

/-! ### The constant -/

/-- **`VOL_5_2`, exactly** — three ideal tetrahedra of shape `y₁`, in the
Lobachevsky (angle) form.

Defined, not derived: this is the exact transcendental target that `VOL_4_1`'s
`qou-yf47` repair established as the corpus's convention.  The identification
with the hyperbolic volume of `S³ ∖ 5₂` is cited, not proved — see the module
header. -/
noncomputable def VOL_5_2 : ℝ := 3 * BlochWigner_lob fiveTwoShape

/-- **The dilogarithm form of `VOL_5_2`.**

Immediate from `KummerRadial.kummer` at `y₁`.  Before Kummer this equation could
not have been written down: `BlochWigner_lob` is built from `arg`s and
`BlochWignerLobachevsky.lean` explicitly forbade transporting dilogarithm facts
onto it.  That prohibition is now lifted on `{Im z > 0}`, and `y₁` is there. -/
theorem VOL_5_2_eq_dilog :
    VOL_5_2 = 3 * ((QOU.MathlibExt.cLiTwoExt fiveTwoShape).im
      + Real.log ‖fiveTwoShape‖ * Complex.arg (1 - fiveTwoShape)) := by
  unfold VOL_5_2
  rw [QOU.Knot.KummerRadial.kummer fiveTwoShape_im_pos]

/-- Both forms at once, as the pair a reader most likely wants. -/
theorem VOL_5_2_two_forms :
    VOL_5_2 = 3 * (Lob (tetAngle₁ fiveTwoShape) + Lob (tetAngle₂ fiveTwoShape)
        + Lob (tetAngle₃ fiveTwoShape))
      ∧ VOL_5_2 = 3 * ((QOU.MathlibExt.cLiTwoExt fiveTwoShape).im
        + Real.log ‖fiveTwoShape‖ * Complex.arg (1 - fiveTwoShape)) :=
  ⟨rfl, VOL_5_2_eq_dilog⟩

/-- The three dihedral angles of the 5₂ tetrahedron sum to `π` — a consistency
check that `fiveTwoShape` is a genuine ideal-tetrahedron shape. -/
theorem fiveTwoShape_angles_sum :
    tetAngle₁ fiveTwoShape + tetAngle₂ fiveTwoShape + tetAngle₃ fiveTwoShape = π :=
  tetAngles_sum_eq_pi _ fiveTwoShape_im_pos

/-- The ideal-tetrahedron law of sines at the 5₂ shape:
`‖y₁‖ = sin θ₂ / sin θ₃`. -/
theorem fiveTwoShape_law_of_sines :
    ‖fiveTwoShape‖ = Real.sin (tetAngle₂ fiveTwoShape) / Real.sin (tetAngle₃ fiveTwoShape) :=
  QOU.Knot.IdealTet.norm_eq_sin_div_sin fiveTwoShape_im_pos

/-! ### The 5₂ triangulation, as a defined object

`QOU/MathlibExt/IdealTriangulation.lean` supplies the layer that was missing:
an `IdealTetrahedron` (a shape in the upper half plane) and an
`IdealTriangulation` (finitely many of them) with a `volume`.  Against that,
the statements below are theorems about a **defined object**, not sentences with
no subject.

⚠ Still nothing about `S³ ∖ 5₂`.  Connecting an `IdealTriangulation` to a knot
complement is Thurston hyperbolisation plus Mostow rigidity, and needs hyperbolic
3-manifolds, which neither Mathlib nor QOU has.  See that file's header. -/

/-- The 5₂ ideal tetrahedron: shape `y₁`. -/
noncomputable def fiveTwoTet : QOU.MathlibExt.IdealTetrahedron :=
  .ofIm fiveTwoShape fiveTwoShape_im_pos

/-- **The 5₂ ideal triangulation**, with SnapPy's actual shapes.

⚠ **CORRECTION (2026-08-09).**  An earlier version of this file defined the
triangulation as `const 3 fiveTwoTet` — three tetrahedra all of shape `y₁`.
**That is wrong**, and SnapPy says so: `Manifold('5_2').tetrahedra_shapes` gives

    tet 0 : 0.78492014550 + 1.30714127868i   = y₁
    tet 1 : 0.12256116688 + 0.74486176662i   = 1/(1 − y₁)   ← NOT y₁
    tet 2 : 0.78492014550 + 1.30714127868i   = y₁

The middle tetrahedron carries the *second edge parameter* of `y₁`, not `y₁`.

The volume claim survives — but as a **theorem now, not an assumption**: the
relabelling `z ↦ 1/(1−z)` cyclically permutes the three dihedral angles
(`IdealTetrahedron.rotate_angles`), so `Λ(θ₁)+Λ(θ₂)+Λ(θ₃)` is unchanged
(`volume_rotate`).  That is why `Vol = 3·D(y₁)` despite the shapes differing.

Recorded because the earlier version was a guess that happened to give the right
number for a reason it did not state. -/
noncomputable def fiveTwoTriangulation : QOU.MathlibExt.IdealTriangulation 3 :=
  ⟨![fiveTwoTet, fiveTwoTet.rotate, fiveTwoTet]⟩

@[simp] theorem fiveTwoTriangulation_tet_zero :
    fiveTwoTriangulation.tet 0 = fiveTwoTet := rfl

@[simp] theorem fiveTwoTriangulation_tet_one :
    fiveTwoTriangulation.tet 1 = fiveTwoTet.rotate := rfl

@[simp] theorem fiveTwoTriangulation_tet_two :
    fiveTwoTriangulation.tet 2 = fiveTwoTet := rfl

/-- The middle tetrahedron's shape is `1/(1 − y₁)`, matching SnapPy. -/
theorem fiveTwoTriangulation_middle_shape :
    ((fiveTwoTriangulation.tet 1).shape : ℂ) = 1 / (1 - fiveTwoShape) := rfl

/-- **`volume (5₂ triangulation) = VOL_5_2`.**

Not by assuming the shapes are equal — they are not — but because the volume is
invariant under the relabelling that relates them. -/
theorem fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2 := by
  unfold fiveTwoTriangulation VOL_5_2
  simp only [QOU.MathlibExt.IdealTriangulation.volume, Fin.sum_univ_three,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.cons_val_two, Matrix.tail_cons,
    QOU.MathlibExt.IdealTetrahedron.volume_rotate]
  show QOU.MathlibExt.IdealTetrahedron.volume fiveTwoTet
      + QOU.MathlibExt.IdealTetrahedron.volume fiveTwoTet
      + QOU.MathlibExt.IdealTetrahedron.volume fiveTwoTet = _
  unfold QOU.MathlibExt.IdealTetrahedron.volume fiveTwoTet
  rw [QOU.MathlibExt.IdealTetrahedron.ofIm_shape]
  ring

/-- And in dilogarithm form. -/
theorem fiveTwoTriangulation_volume_dilog :
    fiveTwoTriangulation.volume
      = 3 * ((QOU.MathlibExt.cLiTwoExt fiveTwoShape).im
        + Real.log ‖fiveTwoShape‖ * Complex.arg (1 - fiveTwoShape)) := by
  rw [fiveTwoTriangulation_volume, VOL_5_2_eq_dilog]

/-! ### The edge gluing equations ARE the saddle cubic

SnapPy's three 5₂ **edge** equations (`Manifold('5_2').gluing_equations()`, the
first `N = 3` rows; the remaining two are cusp equations and carry negative
exponents, so they need `ℤ`-valued data this API does not model):

    [1,0,1, 1,2,0, 1,0,1]
    [0,1,1, 0,0,2, 0,1,1]
    [1,1,0, 1,0,0, 1,1,0]

Reducing each `∏ z^a (z′)^b (z″)^c − 1` over `ℚ(y)`:

* edges **0** and **2** have numerator `−(y³ − 2y² + 3y − 1)` — **exactly the
  saddle cubic**;
* edge **1** is `(z·z′·z″)² = (−1)² = 1`, identically, needing no cubic at all.

So the geometric gluing condition and the algebraic branch equation
`y² = (1−y)³` that this entire lane is built on are **the same equation**.  That
is not a coincidence noticed numerically — it is what the reduction below
proves. -/

/-- SnapPy's three 5₂ edge-gluing equations, as exponent data. -/
def fiveTwoGluing : QOU.MathlibExt.GluingData 3 3 :=
  ⟨![![![1, 0, 1], ![1, 2, 0], ![1, 0, 1]],
    ![![0, 1, 1], ![0, 0, 2], ![0, 1, 1]],
    ![![1, 1, 0], ![1, 0, 0], ![1, 1, 0]]]⟩

theorem fiveTwoShape_ne_zero : fiveTwoShape ≠ 0 :=
  QOU.Knot.IdealTet.ne_zero_of_im_pos fiveTwoShape_im_pos

theorem one_sub_fiveTwoShape_ne_zero : (1 : ℂ) - fiveTwoShape ≠ 0 :=
  QOU.Knot.IdealTet.one_sub_ne_zero fiveTwoShape_im_pos

/-- The branch form of the cubic: `y² = (1−y)³`. -/
theorem fiveTwoShape_sq_eq_cube : fiveTwoShape ^ 2 = (1 - fiveTwoShape) ^ 3 :=
  (QOU.QBeta.FiveTwo.cubic_iff_sq_eq_cube _).mp fiveTwoShape_cubic

/-- **Edge 0** reduces to the saddle cubic: `y²·z′·(z″)⁴ = 1` iff `y² = (1−y)³`. -/
theorem edge_zero :
    fiveTwoShape ^ 2 * (1 / (1 - fiveTwoShape)) * (1 - 1 / fiveTwoShape) ^ 4 = 1 := by
  have hy := fiveTwoShape_ne_zero
  have h1y := one_sub_fiveTwoShape_ne_zero
  field_simp
  linear_combination (norm := ring_nf) (fiveTwoShape - 1) * fiveTwoShape_cubic

/-- **Edge 1** holds identically — it is `(z·z′·z″)² = (−1)² = 1`, and needs no
cubic at all. -/
theorem edge_one :
    fiveTwoShape ^ 2 * (1 / (1 - fiveTwoShape)) ^ 2 * (1 - 1 / fiveTwoShape) ^ 2 = 1 := by
  have hy := fiveTwoShape_ne_zero
  have h1y := one_sub_fiveTwoShape_ne_zero
  field_simp
  ring

/-- **Edge 2** reduces to the saddle cubic: `y²·(z′)³ = 1` iff `y² = (1−y)³`. -/
theorem edge_two :
    fiveTwoShape ^ 2 * (1 / (1 - fiveTwoShape)) ^ 3 = 1 := by
  have h1y := one_sub_fiveTwoShape_ne_zero
  field_simp
  linear_combination (norm := ring_nf) fiveTwoShape_cubic

end QOU.Knot.FiveTwoVolume
