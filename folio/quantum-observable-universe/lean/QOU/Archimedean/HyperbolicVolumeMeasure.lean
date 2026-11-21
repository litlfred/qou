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

  THE CARRIER IS `Fin 3 → ℝ`, AND THE CHOICE IS LOAD-BEARING.  An earlier
  revision of this file used `ℝ × ℝ × ℝ`; that was migrated here because the
  Prod carrier cannot support H2 at all.  Measured 2026-08-08, each row an
  `infer_instance` run against the restored cache:

      volume on `ℝ × ℝ × ℝ`  : `IsAddHaarMeasure` FAILS to synthesize, as does
                               `IsAddRightInvariant`; `Measure.Haar.Prod` does
                               not exist.  Fubini (`lintegral_prod`) does work.
      volume on `Fin 3 → ℝ`  : `IsAddHaarMeasure`, `IsAddRightInvariant`,
                               `finrank = 3`, `addHaar_smul` ALL available; and
                               Fubini still works, via
                               `measurePreserving_piFinSuccAbove`, which splits
                               one coordinate off measure-preservingly.

  So Pi has BOTH and Prod has only Fubini.  H2's dilation invariance needs
  `addHaar_smul` (Lebesgue's `λ³` against the density's `1/λ³`), so on Prod it
  was not merely awkward but unavailable.  **Do not "simplify" this back to
  `ℝ × ℝ × ℝ`** -- that is the trap this migration exists to close.  Tracked in
  bean `qou-5gai`.

  WHAT IS *NOT* HERE -- read before citing.

  * **H2 is PARTLY done.**  Proved: **dilation** (`hypVolume_smul`) -- `λ³` from
    Lebesgue against `1/λ³` from the density, cancelling exactly, the exponent
    forced by `finrank ℝ (Fin 3 → ℝ) = 3` rather than chosen -- and **horizontal
    translation** (`hypVolume_add_left`), where the `v 2 = 0` hypothesis is
    essential rather than technical, since a *vertical* translation genuinely
    is not an isometry.  Together these are the boundary's similarity group.
    **Update (2026-11-20, bean `qou-h2mb`):** inversion in the unit sphere and
    height-fixing linear maps with `|det| = 1` (vertical-axis rotations) are now
    proved in `QOU.Archimedean.HyperbolicVolumeInversion`
    (`hypVolume_inversion_image`, `hypVolume_linear_image`).  The paragraph
    below is the state before that file.
    **Still missing (before 2026-11-20):** the rest of the isometry group of `H³`, i.e. the Möbius
    action of `PSL₂(ℂ)` -- in particular inversion, which is the generator that
    makes the group act transitively and is not reachable from these two.  So
    the measure is **not** yet known invariant under all hyperbolic isometries.
    **No metric, no geodesics, no isometry group** is defined here at all.

    **Cross-ref (T2 metric backfill).**  A genuine metric now DOES exist:
    `QOU.Archimedean.HyperbolicMetric.dH` derives the hyperbolic *distance* as an
    infimum of path lengths, and `HyperbolicIsometryInversion.dH_boundaryInversion`
    proves the boundary INVERSION is a `dH`-isometry (the transitive generator).
    This does NOT transfer to `hypVolume` for free -- the volume's invariance under
    inversion is a separate change-of-variables computation on this measure, still
    to be done -- but the isometry itself is no longer missing, only its action on
    THIS measure.  (`dH`, the two isometries, and geodesics live in the
    `EuclideanSpace ℝ (Fin 3)` carrier, which -- unlike this `Fin 3 → ℝ` -- carries
    the inner product the metric needs.)
  * **No ideal tetrahedron** (H3), and **no `Vol = Λ-sum`** (H4 = `qou-idvt`
    T2).  In particular this file does NOT connect to
    `IdealTetrahedronVolumeConcavity.volChart`, which remains DEFINED as the
    Λ-sum and analytic in content.
  * **`qou-7y3g` and `qou-krvm` (iv) are untouched.**
  * **Nothing wired.**  No mass, binding, or substrate claim.

  ROUTE CHECKED AND REJECTED -- the tetraplectic structure.  The corpus's
  `def:bring-cone-tetraplectic-structure` / `EkParitySplit` /
  `TetraplecticProductRecurrence` do
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
  -- Ref: [leitner2026] beans qou-5gai (H1), qou-idvt (T2), qou-7y3g
-/

import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.MeasureTheory.Measure.WithDensity
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

namespace QOU.Archimedean.HyperbolicVolume

open MeasureTheory Set
open scoped Pointwise

/-- **Upper half-space**, the domain of the `H³` model: points of `ℝ³` with
positive last coordinate. -/
def upperHalfSpace : Set (Fin 3 → ℝ) := {p | 0 < p 2}

theorem isOpen_upperHalfSpace : IsOpen upperHalfSpace :=
  isOpen_lt continuous_const (continuous_apply 2)

theorem measurableSet_upperHalfSpace : MeasurableSet upperHalfSpace :=
  isOpen_upperHalfSpace.measurableSet

/-- The hyperbolic density `1/z³`.  Outside the upper half-space `z ≤ 0`, where
`ENNReal.ofReal` sends the (non-positive) value to `0` -- so the measure below
is automatically supported on `H³` rather than needing a cutoff. -/
noncomputable def hypDensity (p : Fin 3 → ℝ) : ENNReal :=
  ENNReal.ofReal (1 / p 2 ^ 3)

theorem measurable_hypDensity : Measurable hypDensity := by
  unfold hypDensity
  exact ENNReal.measurable_ofReal.comp
    (measurable_const.div ((measurable_pi_apply 2).pow_const 3))

/-- **The hyperbolic volume measure** `dV = dx dy dz / z³` on the upper
half-space model.

The name records the intent; the JUSTIFICATION that this is the hyperbolic
volume is the invariance package H2 (`qou-5gai`), not proved here. -/
noncomputable def hypVolume : Measure (Fin 3 → ℝ) :=
  volume.withDensity hypDensity

theorem hypVolume_apply {s : Set (Fin 3 → ℝ)} (hs : MeasurableSet s) :
    hypVolume s = ∫⁻ p in s, hypDensity p :=
  withDensity_apply hypDensity hs

/-! ### Non-vacuity: the density is positive exactly on `H³`, and the measure
lives there.

Without these the object could be the zero measure, or could charge the
boundary, and every later statement built on it would be meaningless. -/

/-- The density is strictly positive on the upper half-space. -/
theorem hypDensity_pos {p : Fin 3 → ℝ} (hp : p ∈ upperHalfSpace) : 0 < hypDensity p := by
  have hz : 0 < p 2 := hp
  unfold hypDensity
  rw [ENNReal.ofReal_pos]
  positivity

/-- The density vanishes off the upper half-space, so `hypVolume` is supported
on `H³` with no cutoff needed. -/
theorem hypDensity_eq_zero {p : Fin 3 → ℝ} (hp : p ∉ upperHalfSpace) : hypDensity p = 0 := by
  have hz : p 2 ≤ 0 := not_lt.mp hp
  unfold hypDensity
  rw [ENNReal.ofReal_eq_zero]
  rcases lt_or_eq_of_le hz with h | h
  · have h3 : Odd 3 := ⟨1, by norm_num⟩
    have hcube : p 2 ^ 3 < 0 := h3.pow_neg h
    exact le_of_lt (div_neg_of_pos_of_neg one_pos hcube)
  · rw [h]; norm_num

/-- **The complement of `H³` is `hypVolume`-null.**  The measure is genuinely a
measure ON the upper half-space. -/
theorem hypVolume_compl_eq_zero : hypVolume upperHalfSpaceᶜ = 0 := by
  rw [hypVolume_apply measurableSet_upperHalfSpace.compl,
    setLIntegral_eq_zero_iff measurableSet_upperHalfSpace.compl measurable_hypDensity]
  filter_upwards with p hp using hypDensity_eq_zero hp

/-! ### H2 — dilation invariance

**This is what earns the measure its name.**  `dx dy dz / z³` is not
distinguished among densities by anything above; what makes it *hyperbolic* is
that it is invariant under the isometries of `H³`.  Dilation is the substantive
one: Lebesgue scales by `λ³`, the density `1/z³` by `1/λ³`, and the two cancel
EXACTLY.  Nothing about the exponent `3` is chosen for convenience -- it is
forced by `finrank ℝ (Fin 3 → ℝ) = 3`, which is precisely why the Prod carrier
could not host this proof. -/

/-- Scaling pulls a clean factor out of the density: `1/(λz)³ = (1/λ³)·(1/z³)`. -/
theorem hypDensity_smul {r : ℝ} (hr : 0 < r) (p : Fin 3 → ℝ) :
    hypDensity (r • p) = ENNReal.ofReal (1 / r ^ 3) * hypDensity p := by
  unfold hypDensity
  have hsmul : (r • p) 2 = r * p 2 := by simp
  rw [hsmul, ← ENNReal.ofReal_mul (by positivity)]
  congr 1
  field_simp

/-- **H2 (dilation) — `hypVolume` is invariant under `p ↦ r • p` for `r > 0`.**

The `λ³` from Lebesgue and the `1/λ³` from the density cancel. Proved by
transporting the integral along `Measure.map_addHaar_smul`, which is available
only because the carrier is `Fin 3 → ℝ`. -/
theorem hypVolume_smul {r : ℝ} (hr : 0 < r) {s : Set (Fin 3 → ℝ)}
    (hs : MeasurableSet s) : hypVolume (r • s) = hypVolume s := by
  have hr0 : r ≠ 0 := ne_of_gt hr
  have hD : Measurable (fun p : Fin 3 → ℝ => r • p) := measurable_id.const_smul r
  have hrs : MeasurableSet (r • s) := by
    rw [show r • s = (fun p : Fin 3 → ℝ => r⁻¹ • p) ⁻¹' s by
      ext p
      simp only [Set.mem_smul_set, Set.mem_preimage]
      constructor
      · rintro ⟨y, hy, rfl⟩; rwa [inv_smul_smul₀ hr0]
      · exact fun h => ⟨r⁻¹ • p, h, by rw [smul_inv_smul₀ hr0]⟩]
    exact hs.preimage (measurable_id.const_smul r⁻¹)
  -- the constant Lebesgue contributes under scaling
  set c : ENNReal := ENNReal.ofReal |((r : ℝ) ^ Module.finrank ℝ (Fin 3 → ℝ))⁻¹| with hc
  have hmap : Measure.map (fun p : Fin 3 → ℝ => r • p) volume = c • volume :=
    Measure.map_addHaar_smul volume hr0
  -- transport the integral along the map
  have key : ∫⁻ y in r • s, hypDensity y ∂(Measure.map (fun p : Fin 3 → ℝ => r • p) volume)
      = ∫⁻ x in (fun p : Fin 3 → ℝ => r • p) ⁻¹' (r • s), hypDensity (r • x) ∂volume :=
    setLIntegral_map hrs measurable_hypDensity hD
  have hpre : (fun p : Fin 3 → ℝ => r • p) ⁻¹' (r • s) = s := by
    ext p
    simp only [Set.mem_preimage, Set.mem_smul_set]
    constructor
    · rintro ⟨q, hq, hqe⟩
      rwa [smul_right_injective _ hr0 hqe] at hq
    · exact fun hp => ⟨p, hp, rfl⟩
  rw [hpre, hmap] at key
  -- left side: pull the constant out of the scaled measure
  rw [Measure.restrict_smul, lintegral_smul_measure] at key
  -- right side: pull the constant out of the density
  have hrhs : ∫⁻ x in s, hypDensity (r • x) ∂volume
      = ENNReal.ofReal (1 / r ^ 3) * ∫⁻ x in s, hypDensity x ∂volume := by
    rw [← lintegral_const_mul _ measurable_hypDensity]
    exact lintegral_congr fun x => hypDensity_smul hr x
  rw [hrhs] at key
  -- the two constants are equal, and finite-nonzero, so they cancel
  have hceq : c = ENNReal.ofReal (1 / r ^ 3) := by
    rw [hc]
    congr 1
    rw [show Module.finrank ℝ (Fin 3 → ℝ) = 3 by simp, abs_of_pos (by positivity)]
    field_simp
  rw [hceq, smul_eq_mul] at key
  have hne : ENNReal.ofReal (1 / r ^ 3) ≠ 0 := by
    simp [ENNReal.ofReal_eq_zero]; positivity
  have htop : ENNReal.ofReal (1 / r ^ 3) ≠ ⊤ := ENNReal.ofReal_ne_top
  rw [hypVolume_apply hrs, hypVolume_apply hs]
  exact (ENNReal.mul_right_inj hne htop).mp key

/-! ### H2 — horizontal translation invariance

The other generator of the boundary's similarity group, and the easier one: a
translation `(x,y,z) ↦ (x+a, y+b, z)` leaves `z` alone, so the density does not
see it at all, and Lebesgue is translation-invariant.  Note this is `H³`'s
horizontal translation only -- moving the whole picture VERTICALLY is not an
isometry and is not claimed. -/

/-- A translation that fixes the height leaves the density unchanged. -/
theorem hypDensity_add_left {v : Fin 3 → ℝ} (hv : v 2 = 0) (p : Fin 3 → ℝ) :
    hypDensity (v + p) = hypDensity p := by
  unfold hypDensity
  have h : (v + p) 2 = p 2 := by simp [hv]
  rw [h]

/-- **H2 (horizontal translation) — `hypVolume` is invariant under `p ↦ v + p`
whenever `v` has zero height.**

The `v 2 = 0` hypothesis is essential and not a technicality: a *vertical*
translation genuinely changes hyperbolic volume (it is not an isometry of `H³`),
so the density's dependence on `z` is exactly what must be protected here. -/
theorem hypVolume_add_left {v : Fin 3 → ℝ} (hv : v 2 = 0) {s : Set (Fin 3 → ℝ)}
    (hs : MeasurableSet s) :
    hypVolume ((fun p : Fin 3 → ℝ => v + p) ⁻¹' s) = hypVolume s := by
  have hT : Measurable (fun p : Fin 3 → ℝ => v + p) := measurable_const_add v
  have hmap : Measure.map (fun p : Fin 3 → ℝ => v + p) volume = volume :=
    (measurePreserving_add_left volume v).map_eq
  have key : ∫⁻ y in s, hypDensity y ∂(Measure.map (fun p : Fin 3 → ℝ => v + p) volume)
      = ∫⁻ x in (fun p : Fin 3 → ℝ => v + p) ⁻¹' s, hypDensity (v + x) ∂volume :=
    setLIntegral_map hs measurable_hypDensity hT
  rw [hmap] at key
  have hdens : ∫⁻ x in (fun p : Fin 3 → ℝ => v + p) ⁻¹' s, hypDensity (v + x) ∂volume
      = ∫⁻ x in (fun p : Fin 3 → ℝ => v + p) ⁻¹' s, hypDensity x ∂volume :=
    lintegral_congr fun x => hypDensity_add_left hv x
  rw [hdens] at key
  rw [hypVolume_apply (hs.preimage hT), hypVolume_apply hs]
  exact key.symm

/-! ### H4 step 1 — the vertical integral

The first step of Milnor's volume computation, and the one that makes the whole
approach work: integrating `dz/z³` up a vertical line CONVERGES, and collapses
the three-dimensional hyperbolic volume to a two-dimensional Euclidean integral
over the base.  See `qou-5gai` H4-1.

This is stated and proved here because it is self-contained -- it needs neither
the ideal-tetrahedron region (H3) nor Fubini.  Assembling it into
`Vol = ∫∫ dA / (2(R² - d²))` is H4-2, which does. -/

/-- **The vertical hyperbolic integral converges**, with the elementary value
`∫_{z₀}^{∞} z^{-3} dz = 1/(2 z₀²)`. -/
theorem integral_Ioi_rpow_neg_three {z₀ : ℝ} (hz : 0 < z₀) :
    ∫ z in Ioi z₀, z ^ (-3 : ℝ) = 1 / (2 * z₀ ^ 2) := by
  rw [integral_Ioi_rpow_of_lt (by norm_num) hz, show (-3 : ℝ) + 1 = -2 by norm_num,
    Real.rpow_neg hz.le]
  have h2 : z₀ ^ (2 : ℝ) = z₀ ^ (2 : ℕ) := by
    rw [← Real.rpow_natCast z₀ 2]; norm_num
  rw [h2]
  have hz2 : (z₀ : ℝ) ^ (2 : ℕ) ≠ 0 := by positivity
  field_simp

/-- The same integral at the **hemisphere height** `z₀ = √(R² - d²)`, which is
the form H4 actually consumes: over a base point at distance `d` from the centre
of a hemisphere of radius `R`, the vertical fibre contributes
`1 / (2(R² - d²))`.

Summing this over the base triangle is what produces the Λ-sum; that summation
is H4-2/H4-3 and is NOT done here. -/
theorem integral_Ioi_hemisphere {R d : ℝ} (hd : 0 ≤ d) (hdR : d < R) :
    ∫ z in Ioi (Real.sqrt (R ^ 2 - d ^ 2)), z ^ (-3 : ℝ) = 1 / (2 * (R ^ 2 - d ^ 2)) := by
  have hR : 0 < R := lt_of_le_of_lt hd hdR
  have hpos : 0 < R ^ 2 - d ^ 2 := by nlinarith
  rw [integral_Ioi_rpow_neg_three (Real.sqrt_pos.mpr hpos), Real.sq_sqrt hpos.le]

end QOU.Archimedean.HyperbolicVolume
