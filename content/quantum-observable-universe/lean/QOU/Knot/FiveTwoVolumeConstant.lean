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
  ⟨fiveTwoShape, fiveTwoShape_im_pos⟩

/-- **The 5₂ ideal triangulation**: three tetrahedra of shape `y₁`. -/
noncomputable def fiveTwoTriangulation : QOU.MathlibExt.IdealTriangulation 3 :=
  QOU.MathlibExt.IdealTriangulation.const 3 fiveTwoTet

/-- **`volume (5₂ triangulation) = VOL_5_2`** — the statement that could not
previously be written, now a theorem. -/
theorem fiveTwoTriangulation_volume : fiveTwoTriangulation.volume = VOL_5_2 := by
  unfold fiveTwoTriangulation VOL_5_2
  rw [QOU.MathlibExt.IdealTriangulation.volume_const]
  norm_num [fiveTwoTet, QOU.MathlibExt.IdealTetrahedron.volume]

/-- And in dilogarithm form. -/
theorem fiveTwoTriangulation_volume_dilog :
    fiveTwoTriangulation.volume
      = 3 * ((QOU.MathlibExt.cLiTwoExt fiveTwoShape).im
        + Real.log ‖fiveTwoShape‖ * Complex.arg (1 - fiveTwoShape)) := by
  rw [fiveTwoTriangulation_volume, VOL_5_2_eq_dilog]

end QOU.Knot.FiveTwoVolume
