/-
  H1: the hyperbolic volume measure on upper half-space `H³`.

  THE GAP THIS STARTS FILLING.  Mathlib has NO hyperbolic geometry.  Measured
  over the restored olean tree (6990 modules, `lake-cache/qou-v4-24-0`):

      modules matching *hyperbol*            0
      modules matching *clausen* / *lobachev* 0
      `UpperHalfPlane`                        Analysis/Complex only

  and that one hit is the **2-dimensional modular-forms** upper half plane -- a
  complex domain with an `SL₂` action, carrying no Riemannian metric, no volume
  form, no geodesics.  It neither is, nor generalises to, a hyperbolic-geometry
  library.  So `qou-idvt` T2 ("the ideal tetrahedron's volume IS the Λ-sum")
  cannot even be STATED against current Mathlib.  Bean `qou-5gai` tiers the fill
  H1-H5; this file is H1, the measure itself.

  WHAT IS HERE.  The upper half-space and the measure `dx dy dz / z³`, with the
  facts that make it a legitimate object to integrate against: the density is
  measurable, strictly positive exactly on `H³`, and the measure is supported
  there (the complement is null).  That last one is the non-vacuity check --
  a measure that turned out to be zero, or to charge the boundary, would make
  every later statement meaningless.

  WHAT IS *NOT* HERE -- read before citing.

  * **No metric, no isometries, no geodesics.**  This is the volume MEASURE
    only.  H2 (`qou-5gai`) is the invariance package -- horizontal translation
    and, the substantive one, dilation `(x,y,z) ↦ (λx,λy,λz)`, under which
    Lebesgue scales by `λ³` and the density by `1/λ³` so the two cancel.  Until
    H2 is proved, NOTHING here justifies calling this measure "the hyperbolic
    volume" beyond the name: it is `dx dy dz / z³`, and its claim to be
    hyperbolic rests on invariances not yet established.
  * **No ideal tetrahedron** (H3), and **no `Vol = Λ-sum`** (H4 = `qou-idvt`
    T2).  In particular this file does NOT connect to
    `IdealTetrahedronVolumeConcavity.volChart`, which remains DEFINED as the
    Λ-sum and analytic in content.
  * **`qou-7y3g` and `qou-krvm` (iv) are untouched.**
  * **Nothing wired.**  No mass, binding, or substrate claim.

  ROUTE CHECKED AND REJECTED -- the tetraplectic structure.  The corpus's
  `bring_tetraplectic` / `EkParitySplit` / `TetraplecticProductRecurrence` do
  carry a "volume form", so it is worth saying why it is not a shortcut here:
  the tetraplectic `Ω` is a **4-form on the real-4-dimensional Bring cone**
  `C(𝓑) ⊂ ℂ⁵`, built by averaging over `S₅` to make `L²(M, Ω)` decompose into
  `S₅`-irreps, and the corpus's formal tetraplectic content is the **c₃ Faddeev
  q-series reduction** (`e_k(q,q³,…) = q^{k²}/(q²;q²)_k`).  Different manifold,
  different dimension, different geometry -- it is not the Riemannian volume of
  an ideal simplex in `H³` and supplies no part of H4.  (`Vol(4₁)` does appear
  in the tetraplectic orbit via the c₃ carrier `S = c₃ + Vol(4₁)`, but per
  AGENTS.md §"Defined residual ≠ derived decomposition" that residual is a
  DEFINITION and the `−Vol(4₁)` identification is not derived, so it is not a
  route to hyperbolic volume either.)  Recorded so the next agent does not
  re-walk it.

  Archimedean (ℝ): Lebesgue measure, ordering -- §7c.

  -- Ref: [thurston1978] Ch. 1 (the upper half-space model)
  -- Ref: [manuscript] beans qou-5gai (H1), qou-idvt (T2), qou-7y3g
-/

import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.MeasureTheory.Measure.WithDensity

namespace QOU.Archimedean.HyperbolicVolume

open MeasureTheory Set

/-- **Upper half-space**, the domain of the `H³` model: points of `ℝ³` with
positive last coordinate. -/
def upperHalfSpace : Set (ℝ × ℝ × ℝ) := {p | 0 < p.2.2}

theorem isOpen_upperHalfSpace : IsOpen upperHalfSpace :=
  isOpen_lt continuous_const (continuous_snd.comp continuous_snd)

theorem measurableSet_upperHalfSpace : MeasurableSet upperHalfSpace :=
  isOpen_upperHalfSpace.measurableSet

/-- The hyperbolic density `1/z³`.  Outside the upper half-space `z ≤ 0`, where
`ENNReal.ofReal` sends the (non-positive) value to `0` -- so the measure below
is automatically supported on `H³` rather than needing a cutoff. -/
noncomputable def hypDensity (p : ℝ × ℝ × ℝ) : ENNReal :=
  ENNReal.ofReal (1 / p.2.2 ^ 3)

theorem measurable_hypDensity : Measurable hypDensity := by
  unfold hypDensity
  exact ENNReal.measurable_ofReal.comp
    ((measurable_const.div ((measurable_snd.comp measurable_snd).pow_const 3)))

/-- **The hyperbolic volume measure** `dV = dx dy dz / z³` on the upper
half-space model.

The name records the intent; the JUSTIFICATION that this is the hyperbolic
volume is the invariance package H2 (`qou-5gai`), not proved here. -/
noncomputable def hypVolume : Measure (ℝ × ℝ × ℝ) :=
  volume.withDensity hypDensity

theorem hypVolume_apply {s : Set (ℝ × ℝ × ℝ)} (hs : MeasurableSet s) :
    hypVolume s = ∫⁻ p in s, hypDensity p :=
  withDensity_apply hypDensity hs

/-! ### Non-vacuity: the density is positive exactly on `H³`, and the measure
lives there.

Without these the object could be the zero measure, or could charge the
boundary, and every later statement built on it would be meaningless. -/

/-- The density is strictly positive on the upper half-space. -/
theorem hypDensity_pos {p : ℝ × ℝ × ℝ} (hp : p ∈ upperHalfSpace) : 0 < hypDensity p := by
  have hz : 0 < p.2.2 := hp
  unfold hypDensity
  rw [ENNReal.ofReal_pos]
  positivity

/-- The density vanishes off the upper half-space, so `hypVolume` is supported
on `H³` with no cutoff needed. -/
theorem hypDensity_eq_zero {p : ℝ × ℝ × ℝ} (hp : p ∉ upperHalfSpace) : hypDensity p = 0 := by
  have hz : p.2.2 ≤ 0 := not_lt.mp hp
  unfold hypDensity
  rw [ENNReal.ofReal_eq_zero]
  rcases lt_or_eq_of_le hz with h | h
  · have h3 : Odd 3 := ⟨1, by norm_num⟩
    have hcube : p.2.2 ^ 3 < 0 := h3.pow_neg h
    exact le_of_lt (div_neg_of_pos_of_neg one_pos hcube)
  · rw [h]; norm_num

/-- **The complement of `H³` is `hypVolume`-null.**  The measure is genuinely a
measure ON the upper half-space. -/
theorem hypVolume_compl_eq_zero : hypVolume upperHalfSpaceᶜ = 0 := by
  rw [hypVolume_apply measurableSet_upperHalfSpace.compl,
    setLIntegral_eq_zero_iff measurableSet_upperHalfSpace.compl measurable_hypDensity]
  filter_upwards with p hp using hypDensity_eq_zero hp

end QOU.Archimedean.HyperbolicVolume
