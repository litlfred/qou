import Mathlib.Algebra.Quaternion
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-!
# Quaternionic electroweak alignment — SU(2)_L × SU(2)_R on the flavor doublet

An **honest** formalization of the Morita quaternionic-electroweak picture over
the Bring tetraplectic boundary.  The flavor doublet is modelled as a single
quaternion (its 4 real d.o.f. = the 2 complex d.o.f. of a standard SU(2)
doublet).  The gauge group `SU(2)` is realized as the **unit quaternions**
(`normSq = 1`), *not* the full quaternion algebra — this is the correction to
the earlier draft, whose actions took arbitrary quaternions and so modelled the
whole algebra, overclaiming the gauge structure.

What is actually **proved** here is exactly the group-action content:

* `IsSU2.mul` / `IsSU2.one` — the unit quaternions are closed under
  multiplication and contain the identity (the `SU(2) ≅ S³` group);
* `su2L_normSq` / `su2R_normSq` — the left and right actions are
  **norm-preserving** (isometric / unitary): the defining property of a genuine
  gauge action, and the substance the arbitrary-algebra version could not state;
* `su2L_su2R_commute` — the two factors `SU(2)_L` and `SU(2)_R` act
  independently (they commute);
* `u1Y_isSU2` — the hypercharge phase `U(1)_Y` sits inside `SU(2)` as the
  `i`-plane circle subgroup.

Per the §7c base-ring convention the algebraic group/action content is stated
over a generic `{R : Type*} [CommRing R]`; only the hypercharge phase `u1Y`,
which uses `Real.cos`/`Real.sin`, specializes to `ℝ`.

The *identification* of this algebraic structure with the physical electroweak
sector is interpretive — see `rem:tetraplectic-su2-gauge-reading` and
`mass-theory/hoefsmit-ew-cell-content.md` (Morita 1982; Cederwall–Preitschopf).
No physical claim beyond the group-action content is asserted by this file.
-/

namespace QOU.Tetraplectic

section GenericRing

variable {R : Type*} [CommRing R]

/-- The flavor-doublet space: a single quaternion over `R`. -/
abbrev FlavorDoublet (R : Type*) [CommRing R] := Quaternion R

/-- `SU(2)` realized as the unit quaternions (`normSq q = 1`). -/
def IsSU2 (q : Quaternion R) : Prop := Quaternion.normSq q = 1

/-- Group closure: the product of two unit quaternions is a unit quaternion. -/
theorem mul {g h : Quaternion R} (hg : IsSU2 g) (hh : IsSU2 h) :
    IsSU2 (g * h) := by
  unfold IsSU2 at hg hh ⊢
  rw [map_mul, hg, hh, mul_one]

/-- The identity quaternion lies in `SU(2)`. -/
theorem one : IsSU2 (1 : Quaternion R) := by
  unfold IsSU2
  rw [map_one]

/-- Left gauge action `SU(2)_L`. -/
def su2L (g psi : Quaternion R) : Quaternion R := g * psi

/-- Right gauge action `SU(2)_R`. -/
def su2R (g psi : Quaternion R) : Quaternion R := psi * g

/-- **`SU(2)_L` acts by isometries** — a unit-quaternion left action preserves
the flavor norm, the defining property of a unitary gauge action. -/
theorem su2L_normSq {g : Quaternion R} (hg : IsSU2 g) (psi : Quaternion R) :
    Quaternion.normSq (su2L g psi) = Quaternion.normSq psi := by
  unfold su2L
  unfold IsSU2 at hg
  rw [map_mul, hg, one_mul]

/-- **`SU(2)_R` acts by isometries.** -/
theorem su2R_normSq {g : Quaternion R} (hg : IsSU2 g) (psi : Quaternion R) :
    Quaternion.normSq (su2R g psi) = Quaternion.normSq psi := by
  unfold su2R
  unfold IsSU2 at hg
  rw [map_mul, hg, mul_one]

/-- **`SU(2)_L × SU(2)_R` commute** — the two gauge factors act independently.
This is associativity of quaternion multiplication, now genuinely between the
two group copies (left- vs right-multiplication). -/
theorem su2L_su2R_commute (gL gR psi : Quaternion R) :
    su2L gL (su2R gR psi) = su2R gR (su2L gL psi) := by
  simp only [su2L, su2R, mul_assoc]

end GenericRing

section Archimedean

/-- The hypercharge phase `U(1)_Y` at angle `θ`: a unit quaternion in the
`i`-plane.  Archimedean (uses `Real.cos`/`Real.sin`), hence stated over `ℝ`. -/
noncomputable def u1Y (θ : ℝ) : Quaternion ℝ := ⟨Real.cos θ, Real.sin θ, 0, 0⟩

/-- `U(1)_Y ⊂ SU(2)`: the hypercharge phase is a unit quaternion. -/
theorem u1Y_isSU2 (θ : ℝ) : IsSU2 (u1Y θ) := by
  simp only [IsSU2, u1Y, Quaternion.normSq_def']
  ring_nf
  exact Real.cos_sq_add_sin_sq θ

end Archimedean

end QOU.Tetraplectic
