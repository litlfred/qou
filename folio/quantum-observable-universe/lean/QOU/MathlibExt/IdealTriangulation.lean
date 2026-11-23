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

  * `IdealTetrahedron` — a shape parameter in the upper half plane, carried as a
    point of Mathlib's `UpperHalfPlane` (`ℍ`) since bean `qou-m8xt`;
  * `IdealTetrahedron.volume` — its volume, `D(z)`, in **both** the Lobachevsky
    (angle) form and the dilogarithm form, proved equal via `KummerRadial.kummer`;
  * `IdealTriangulation n` — `n` ideal tetrahedra;
  * `IdealTriangulation.volume` — the sum;
  * edge parameters `z, z′ = 1/(1−z), z″ = 1 − 1/z` with `z·z′·z″ = −1`, and the
    **gluing equations** in both their product form (`SatisfiesEdgeEquations`)
    and their angle / Casson–Rivin form (`SatisfiesAngleEquations`).

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
import Mathlib.Analysis.Complex.UpperHalfPlane.Basic

namespace QOU.MathlibExt

open Real Complex QOU.Archimedean
open scoped UpperHalfPlane

/-! ### Ideal tetrahedra -/

/-- An **ideal tetrahedron**, as its shape parameter.

Four ideal vertices on the sphere at infinity, normalised to `0, 1, ∞, z`.  The
condition `0 < Im z` says the tetrahedron is nondegenerate and positively
oriented; degenerate (flat) tetrahedra are exactly the real shapes, and are
excluded.

The shape is a point of Mathlib's upper half plane `ℍ` (bean `qou-m8xt`), so the
positivity is carried by the type rather than by a separate field: `im_pos` below is
`UpperHalfPlane.im_pos`, and `shape_ne_zero` is `UpperHalfPlane.ne_zero`.  Wherever a
complex number is expected, `T.shape` coerces to `(T.shape : ℂ)`. -/
structure IdealTetrahedron where
  /-- The shape parameter, a point of the upper half plane. -/
  shape : ℍ

namespace IdealTetrahedron

/-- Build an ideal tetrahedron from a complex shape with positive imaginary part. -/
def ofIm (z : ℂ) (hz : 0 < z.im) : IdealTetrahedron := ⟨UpperHalfPlane.mk z hz⟩

@[simp] theorem ofIm_shape (z : ℂ) (hz : 0 < z.im) : ((ofIm z hz).shape : ℂ) = z := rfl

variable (T : IdealTetrahedron)

/-- **Nondegenerate and positively oriented** — `UpperHalfPlane.im_pos`, read through the
coercion `ℍ → ℂ`. -/
theorem im_pos : 0 < (T.shape : ℂ).im := T.shape.im_pos

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
      + Real.log ‖(T.shape : ℂ)‖ * Complex.arg (1 - T.shape) :=
  QOU.Knot.KummerRadial.kummer T.im_pos

/-- The ideal-tetrahedron law of sines, `‖z‖ = sin θ₂ / sin θ₃`. -/
theorem law_of_sines :
    ‖(T.shape : ℂ)‖ = Real.sin T.angle₂ / Real.sin T.angle₃ :=
  QOU.Knot.IdealTet.norm_eq_sin_div_sin T.im_pos

/-! #### Edge parameters

Each of the three edge-pairs carries its own shape: `z`, `z′ = 1/(1−z)`,
`z″ = 1 − 1/z`.  These are what the gluing equations multiply. -/

/-- The three edge parameters, indexed to match `angle`. -/
noncomputable def param : Fin 3 → ℂ
  | 0 => T.shape
  | 1 => 1 / (1 - T.shape)
  | 2 => 1 - 1 / T.shape

@[simp] theorem param_zero : T.param 0 = T.shape := rfl
@[simp] theorem param_one : T.param 1 = 1 / (1 - T.shape) := rfl
@[simp] theorem param_two : T.param 2 = 1 - 1 / T.shape := rfl

theorem shape_ne_zero : (T.shape : ℂ) ≠ 0 := T.shape.ne_zero

theorem one_sub_shape_ne_zero : (1 : ℂ) - T.shape ≠ 0 :=
  QOU.Knot.IdealTet.one_sub_ne_zero T.im_pos

/-- **`z · z′ · z″ = −1`** — pure algebra, and the source of the `π` in the angle
sum. -/
theorem param_prod : T.param 0 * T.param 1 * T.param 2 = -1 :=
  tet_shape_prod _ T.shape_ne_zero T.one_sub_shape_ne_zero

/-- Every edge parameter lies in the upper half plane: the upper half plane is
preserved by the two Möbius maps. -/
theorem param_im_pos : ∀ i, 0 < (T.param i).im
  | 0 => T.im_pos
  | 1 => (tet_im_pos _ T.im_pos).1
  | 2 => (tet_im_pos _ T.im_pos).2

/-- The argument of the `i`-th edge parameter is the `i`-th dihedral angle. -/
theorem arg_param : ∀ i, (T.param i).arg = ![T.angle₁, T.angle₂, T.angle₃] i
  | 0 => rfl
  | 1 => rfl
  | 2 => rfl

/-! #### Relabelling, and volume invariance

`z ↦ 1/(1−z)` does not change the tetrahedron — it changes which edge-pair is
called "first".  The three dihedral angles are **cyclically permuted**, so the
volume is unchanged.  This is not a coincidence to be checked numerically; it is
`Lob a + Lob b + Lob c` being symmetric under cycling its arguments. -/

/-- `1/(1 − 1/(1−z)) = 1 − 1/z`: the second edge parameter of the rotated
tetrahedron is the third of the original. -/
theorem shape_cycle₂ (hz0 : (T.shape : ℂ) ≠ 0) (h1z : (1:ℂ) - T.shape ≠ 0) :
    (1 : ℂ) / (1 - 1 / (1 - T.shape)) = 1 - 1 / T.shape := by
  have h : (1:ℂ) - 1 / (1 - T.shape) = -(T.shape : ℂ) / (1 - T.shape) := by
    field_simp; ring
  rw [h]
  field_simp
  ring

/-- `1 − 1/(1/(1−z)) = z`: the third edge parameter of the rotated tetrahedron is
the first of the original.

Needs **no** non-vanishing hypothesis, which the unused-variable linter caught:
Lean's `1/0 = 0` makes both sides `1` in the degenerate case `1 − z = 0`, so the
identity holds unconditionally. -/
theorem shape_cycle₃ :
    (1 : ℂ) - 1 / (1 / (1 - T.shape)) = T.shape := by
  field_simp
  ring

/-- The same tetrahedron, relabelled: shape `1/(1−z)`. -/
noncomputable def rotate : IdealTetrahedron :=
  ofIm (1 / (1 - T.shape)) (tet_im_pos _ T.im_pos).1

@[simp] theorem rotate_shape : (T.rotate.shape : ℂ) = 1 / (1 - T.shape) := rfl

/-- **The dihedral angles cycle under relabelling.** -/
theorem rotate_angles :
    T.rotate.angle₁ = T.angle₂ ∧ T.rotate.angle₂ = T.angle₃
      ∧ T.rotate.angle₃ = T.angle₁ := by
  refine ⟨rfl, ?_, ?_⟩
  · show tetAngle₂ (1 / (1 - T.shape)) = tetAngle₃ T.shape
    unfold tetAngle₂ tetAngle₃
    rw [T.shape_cycle₂ T.shape_ne_zero T.one_sub_shape_ne_zero]
  · show tetAngle₃ (1 / (1 - T.shape)) = tetAngle₁ T.shape
    unfold tetAngle₃ tetAngle₁
    rw [T.shape_cycle₃]

/-- **The volume is invariant under relabelling** — the three `Λ` terms are
merely permuted. -/
@[simp] theorem volume_rotate : T.rotate.volume = T.volume := by
  obtain ⟨h1, h2, h3⟩ := T.rotate_angles
  rw [volume_eq_lob_sum, volume_eq_lob_sum, h1, h2, h3]
  ring

end IdealTetrahedron

/-! ### Ideal triangulations -/

/-- An **ideal triangulation** by `n` ideal tetrahedra.

Only the geometric data is carried here — the shapes.  The *combinatorial* data
(face pairings, edge classes) lives separately in `GluingData`, and the
conditions it imposes are `SatisfiesEdgeEquations` / `SatisfiesAngleEquations`
below.  Neither certifies that the triangulation is *of* a given manifold; see
the module header. -/
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
      + Real.log ‖((T.tet i).shape : ℂ)‖ * Complex.arg (1 - (T.tet i).shape)) :=
  Finset.sum_congr rfl fun i _ => (T.tet i).volume_eq_dilog

/-- A triangulation all of whose tetrahedra have the same shape. -/
noncomputable def const (n : ℕ) (S : IdealTetrahedron) : IdealTriangulation n :=
  ⟨fun _ => S⟩

@[simp] theorem volume_const (n : ℕ) (S : IdealTetrahedron) :
    (const n S).volume = n * S.volume := by
  simp [volume, const]

end IdealTriangulation

/-! ### Gluing equations

The combinatorics of *how* the tetrahedra are glued, expressed as exponent data:
for each edge class `k`, each tetrahedron `i` and each edge-pair `j`, how many
times that edge-pair is glued around `k`.

Two conditions are recorded, and they are **not equivalent**:

* `SatisfiesEdgeEquations` — the full gluing equation, `∏ param^exp = 1`.  This
  constrains modulus *and* argument.
* `SatisfiesAngleEquations` — the dihedral angles around each edge sum to `2π`.
  This is the *angle-structure* condition (Casson–Rivin, and what the corpus's
  m004/L6a4 polytopes encode).  It is the argument half only.

⚠ Neither condition, alone or together, certifies that a triangulation **is** a
triangulation of a given manifold.  That is topology, and is not modelled here —
see the module header. -/

/-- Edge-gluing exponent data: `exp k i j` is the multiplicity with which the
`j`-th edge-pair of tetrahedron `i` meets edge class `k`. -/
structure GluingData (n e : ℕ) where
  /-- The exponents. -/
  exp : Fin e → Fin n → Fin 3 → ℕ

variable {n e : ℕ}

/-- **The edge gluing equations**, in product form. -/
def SatisfiesEdgeEquations (T : IdealTriangulation n) (G : GluingData n e) : Prop :=
  ∀ k, (∏ i, ∏ j, (T.tet i).param j ^ G.exp k i j) = 1

/-- **The angle (Casson–Rivin) form**: the dihedral angles around each edge sum
to `2π`. -/
def SatisfiesAngleEquations (T : IdealTriangulation n) (G : GluingData n e) : Prop :=
  ∀ k, (∑ i, ∑ j, (G.exp k i j : ℝ) * ![(T.tet i).angle₁, (T.tet i).angle₂,
    (T.tet i).angle₃] j) = 2 * π

/-- Every edge parameter is nonzero, so the products above are units. -/
theorem param_ne_zero (T : IdealTriangulation n) (i : Fin n) (j : Fin 3) :
    (T.tet i).param j ≠ 0 := by
  intro h
  have := (T.tet i).param_im_pos j
  rw [h] at this
  simp at this

end QOU.MathlibExt
