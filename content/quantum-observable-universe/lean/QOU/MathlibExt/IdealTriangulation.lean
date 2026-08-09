/-
  Ideal tetrahedra and ideal triangulations, with their volume.

  Bean `qou-mlgp` (Mathlib gap), `qou-m015`.

  ═══ THE GAP THIS CLOSES, AND THE ONE IT DOES NOT ═══

  Working on `Vol(5₂)` surfaced something sharper than "unproved":
  **`Vol(5₂) = 3·D(y₁)` was not a statable Lean proposition at all.**  Mathlib has
  no hyperbolic 3-manifolds, and QOU had no volume functor — the only objects
  named "volume" in Lean were decimal literals (`MassDerivation.vol_figure_eight`)
  and the placeholder `HyperbolicVolume : Knot → ℝ := fun k => 0 * (k : ℝ)`
  (`AppendixSurreals/Conjectures.lean`), which returns **zero**.  You cannot prove
  an equation against those; you can only write a false or vacuous one.

  This file supplies the missing *definitional* layer, at the level where the
  corpus already has real content:

  * `IdealTetrahedron` — a shape parameter in the upper half plane;
  * `IdealTetrahedron.volume` — its volume, `D(z)`, in **both** the Lobachevsky
    (angle) form and the dilogarithm form, proved equal via `KummerRadial.kummer`;
  * `IdealTriangulation n` — `n` ideal tetrahedra;
  * `IdealTriangulation.volume` — the sum.

  With that, `volume (5₂ triangulation) = 3·D(y₁)` becomes a **theorem about a
  defined object** rather than a sentence with no subject.

  ═══ ⚠ WHAT IS STILL NOT DEFINED — SAY THIS OUT LOUD ═══

  **The volume of a topological 3-manifold.**  Nothing here connects an
  `IdealTriangulation` to a knot complement.  That connection is Thurston's
  hyperbolisation plus Mostow rigidity (the volume is a topological invariant,
  independent of the triangulation), and it needs hyperbolic 3-manifolds, which
  neither Mathlib nor QOU has.

  So this file makes the *combinatorial-geometric* side statable and provable.
  It does **not** license writing `Vol(S³ ∖ 5₂) = …` for any value: that sentence
  still has no subject.  A reader who takes `IdealTriangulation.volume` for "the
  hyperbolic volume of the knot complement" has assumed exactly the theorem this
  file does not prove.

  Nor is the 5₂ **volume conjecture** touched — Ohtsuki, *Quantum Topol.* **7**
  (2016) 669–735, not formalised here.

  -- Ref: [thurston1978] Ch. 4 (ideal tetrahedra, gluing)
  -- Ref: [milnor1982] (the Lobachevsky volume of an ideal tetrahedron)
  -- Ref: [neumann-zagier1985] eq. (37)–(39)
-/
import QOU.Knot.KummerRadial

namespace QOU.MathlibExt

open Real Complex QOU.Archimedean

/-! ### Ideal tetrahedra -/

/-- An **ideal tetrahedron**, as its shape parameter.

Four ideal vertices on the sphere at infinity, normalised to `0, 1, ∞, z`.  The
condition `0 < Im z` says the tetrahedron is nondegenerate and positively
oriented; degenerate (flat) tetrahedra are exactly the real shapes, and are
excluded. -/
structure IdealTetrahedron where
  /-- The shape parameter. -/
  shape : ℂ
  /-- Nondegenerate and positively oriented. -/
  im_pos : 0 < shape.im

namespace IdealTetrahedron

variable (T : IdealTetrahedron)

/-- The three dihedral angles, one per pair of opposite edges. -/
noncomputable def angle₁ : ℝ := tetAngle₁ T.shape
noncomputable def angle₂ : ℝ := tetAngle₂ T.shape
noncomputable def angle₃ : ℝ := tetAngle₃ T.shape

/-- **The dihedral angles sum to `π`** — the defining property of an *ideal*
tetrahedron, and the reason its angle sum is the Euclidean one. -/
theorem angle_sum : T.angle₁ + T.angle₂ + T.angle₃ = π :=
  tetAngles_sum_eq_pi _ T.im_pos

theorem angle₁_mem : 0 < T.angle₁ ∧ T.angle₁ < π :=
  arg_mem_Ioo_of_im_pos _ T.im_pos

theorem angle₂_mem : 0 < T.angle₂ ∧ T.angle₂ < π :=
  arg_mem_Ioo_of_im_pos _ (tet_im_pos _ T.im_pos).1

theorem angle₃_mem : 0 < T.angle₃ ∧ T.angle₃ < π :=
  arg_mem_Ioo_of_im_pos _ (tet_im_pos _ T.im_pos).2

/-- **The volume of an ideal tetrahedron**: `Λ(α) + Λ(β) + Λ(γ)`.

This is Milnor's formula, and it is a *definition* here — the identification with
a hyperbolic volume in the metric sense is not available, see the module
header. -/
noncomputable def volume : ℝ := BlochWigner_lob T.shape

theorem volume_eq_lob_sum :
    T.volume = Lob T.angle₁ + Lob T.angle₂ + Lob T.angle₃ := rfl

/-- **The volume in dilogarithm form** — Neumann–Zagier eq. (38)/(39).

Equal to the angle form by `KummerRadial.kummer`.  Writing both and calling them
equal is precisely the transport `BlochWignerLobachevsky.lean` used to forbid;
it is licensed now that Kummer is proved on `{Im z > 0}`, where every
`IdealTetrahedron` lives by construction. -/
theorem volume_eq_dilog :
    T.volume = (cLiTwoExt T.shape).im
      + Real.log ‖T.shape‖ * Complex.arg (1 - T.shape) :=
  QOU.Knot.KummerRadial.kummer T.im_pos

/-- The ideal-tetrahedron law of sines, `‖z‖ = sin θ₂ / sin θ₃`. -/
theorem law_of_sines :
    ‖T.shape‖ = Real.sin T.angle₂ / Real.sin T.angle₃ :=
  QOU.Knot.IdealTet.norm_eq_sin_div_sin T.im_pos

end IdealTetrahedron

/-! ### Ideal triangulations -/

/-- An **ideal triangulation** by `n` ideal tetrahedra.

Only the geometric data is carried here — the shapes.  The *combinatorial* data
(face pairings, edge classes) and the gluing equations they impose are not
modelled; see the module header for why that matters and what it costs. -/
structure IdealTriangulation (n : ℕ) where
  /-- The tetrahedra. -/
  tet : Fin n → IdealTetrahedron

namespace IdealTriangulation

variable {n : ℕ} (T : IdealTriangulation n)

/-- **The volume of an ideal triangulation**: the sum of its tetrahedra's
volumes. -/
noncomputable def volume : ℝ := ∑ i, (T.tet i).volume

@[simp] theorem volume_def : T.volume = ∑ i, (T.tet i).volume := rfl

/-- The volume in dilogarithm form, termwise. -/
theorem volume_eq_dilog :
    T.volume = ∑ i, ((cLiTwoExt (T.tet i).shape).im
      + Real.log ‖(T.tet i).shape‖ * Complex.arg (1 - (T.tet i).shape)) :=
  Finset.sum_congr rfl fun i _ => (T.tet i).volume_eq_dilog

/-- A triangulation all of whose tetrahedra have the same shape. -/
noncomputable def const (n : ℕ) (S : IdealTetrahedron) : IdealTriangulation n :=
  ⟨fun _ => S⟩

@[simp] theorem volume_const (n : ℕ) (S : IdealTetrahedron) :
    (const n S).volume = n * S.volume := by
  simp [volume, const]

end IdealTriangulation

end QOU.MathlibExt
