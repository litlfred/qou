/-
# HyperbolicNormalization.lean (WALL-2) — two-point normalization to the z-axis.

The reduction step that carries geodesic uniqueness between two arbitrary points
of `H³` down to the already-derived z-axis case (`HyperbolicGeodesicZAxis`,
`dH_zpt`).  Concretely: for `x, y ∈ H³` there is a `dH`-isometry `Φ` — a finite
composition of the WALL-1 boundary-similarity generators (dilation, horizontal
translation, height-fixing rotation) together with at most one boundary inversion
(`HyperbolicIsometryInversion`) — carrying both `Φ x` and `Φ y` onto the z-axis
`{(0,0,z) : z > 0}`.

## What is built here

* **`IsDHIsometry.comp`** — the composition of two `dH`-isometries is a
  `dH`-isometry.  The derivative composes (`HasFDerivAt.comp`), the conformal
  factor multiplies, the height scales by the product — so the line element
  `‖v‖/z` is preserved by the composite exactly as by each factor.  This is the
  reusable interface that lets a *finite composition* of the WALL-1 / inversion
  generators be presented as a single `IsDHIsometry` (hence a single
  `dH`-preserving map, `dH_le` inherited).
* **`zAxis`** — the z-axis `{p | p₀ = 0 ∧ p₁ = 0 ∧ 0 < p₂}`, with `zpt a ∈ zAxis`.
* **`exists_normalization_vertical` (DERIVED, sorry-free)** — the
  shared-horizontal case.  When `x, y` already share their two horizontal
  coordinates (`x₀ = y₀`, `x₁ = y₁`) they lie on a common *vertical* line, and the
  single horizontal translation `p ↦ p + (zpt x₂ − x)` (its height offset is
  `x₂ − x₂ = 0`, so it is genuinely horizontal) carries BOTH onto the z-axis — `x`
  onto `zpt x₂` unconditionally, `y` onto `zpt y₂` using the shared-horizontal
  hypothesis.  No inversion is needed: the boundary-similarity group fixes `∞` and
  so maps vertical lines to vertical lines, which is exactly enough here.

* **`invImage_horiz_collapse` + `exists_normalization_general` (DERIVED,
  sorry-free)** — the general case, `x, y` with DISTINCT horizontal parts (bean
  `qou-0a0z`, CLOSED).  A three-map composition `Φ = T₃ ∘ T₂ ∘ T₁` carries both
  onto the z-axis: `T₁` a horizontal translation sending `x` to `(0,0,x₂)`; `T₂`
  the boundary inversion at the geodesic's near ideal endpoint `ξ = (c−R)·u`
  (`u = w/d` the unit horizontal difference, `c = (d²+y₂²−x₂²)/(2d)`,
  `R = √(c²+x₂²)`); `T₃` a horizontal translation.  The endpoint algebra is
  handled by the single sphere identity `‖p − ξ‖² = 2R·(α − (c−R))`, which
  collapses coords `0,1` of BOTH inversion images to the same value — NO explicit
  ideal-endpoint construction of the geodesic is needed, only that both interior
  points lie on the Euclidean sphere `‖· − c·u‖ = R`.
* **`exists_normalization` (DERIVED, sorry-free)** — the unconditional statement,
  by case split on shared vs distinct horizontal parts.

## Discipline

This file is 100 % sorry-free (`#print axioms` on every theorem shows only
`propext, Classical.choice, Quot.sound` — no `sorryAx`).  The
`HypMinimizerUnique` conjecture in `HyperbolicGeodesic` is left untouched: the
z-axis reduction is a genuine derivation, NOT a fabricated instance.

Archimedean (ℝ): `‖·‖`, ordering `0 < z` — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.4 (isometries of the upper half-space model;
  --   reduction to the vertical geodesic by a boundary inversion)
  -- Ref: [milnor1982] §1 (the boundary similarity group + inversion generate
  --   the isometry group; two-point transitivity onto the z-axis)
  -- Ref: [ratcliffe] §4.6 (similarities and inversions are hyperbolic isometries)
  -- Ref: [manuscript] beans qou-0a0z (T2 WALL-2 two-point normalization),
  --   qou-473l (T2), qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicGeodesicZAxis
import QOU.Archimedean.HyperbolicIsometryInversion
import QOU.Archimedean.HyperbolicIsometryAffine

namespace QOU.Archimedean.HyperbolicMetric

namespace IsDHIsometry

/-- **Composition of `dH`-isometries is a `dH`-isometry.**  If `ψ` and `φ` are
each conformal-with-the-same-factor-on-the-height, so is `ψ ∘ φ`: its Fréchet
derivative is the composite `Dψ(φ p) ∘ Dφ(p)` (chain rule), its conformal factor
is the PRODUCT `lam_ψ(φ p) · lam_φ(p)` (norms scale by the product), and its
height scales by the SAME product (`hheight` composed).  So the line element
`‖v‖/z` — preserved pointwise by each factor — is preserved by the composite.
This lets a finite composition of the WALL-1 generators and a boundary inversion
be handled as a single `IsDHIsometry`. -/
def comp {φ ψ : E → E} (hψ : IsDHIsometry ψ) (hφ : IsDHIsometry φ) :
    IsDHIsometry (ψ ∘ φ) where
  Dφ := fun p => (hψ.Dφ (φ p)).comp (hφ.Dφ p)
  lam := fun p => hψ.lam (φ p) * hφ.lam p
  hderiv := fun p hp => (hψ.hderiv (φ p) (hφ.maps hp)).comp p (hφ.hderiv p hp)
  hlam := fun p hp => mul_pos (hψ.hlam (φ p) (hφ.maps hp)) (hφ.hlam p hp)
  hconf := fun p hp v => by
    rw [ContinuousLinearMap.comp_apply, hψ.hconf (φ p) (hφ.maps hp) (hφ.Dφ p v),
      hφ.hconf p hp v]; ring
  hheight := fun p hp => by
    show (ψ (φ p)) 2 = hψ.lam (φ p) * hφ.lam p * (p 2)
    rw [hψ.hheight (φ p) (hφ.maps hp), hφ.hheight p hp]; ring

end IsDHIsometry

end QOU.Archimedean.HyperbolicMetric

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric EuclideanGeometry
open scoped ENNReal

/-- **The z-axis of `H³`** — the vertical geodesic `{(0,0,z) : z > 0}`, the target
of the normalization.  A point is on it iff both horizontal coordinates vanish and
the height is positive. -/
def zAxis : Set E := {p : E | p 0 = 0 ∧ p 1 = 0 ∧ 0 < p 2}

@[simp] theorem mem_zAxis {p : E} : p ∈ zAxis ↔ p 0 = 0 ∧ p 1 = 0 ∧ 0 < p 2 := Iff.rfl

/-- The `0`-coordinate of a z-axis point `zpt a = (0,0,a)` vanishes. -/
@[simp] theorem zpt_coord0 (a : ℝ) : (zpt a) 0 = 0 := by
  rw [zpt, EuclideanSpace.single_apply, if_neg (by decide)]

/-- The `1`-coordinate of a z-axis point `zpt a = (0,0,a)` vanishes. -/
@[simp] theorem zpt_coord1 (a : ℝ) : (zpt a) 1 = 0 := by
  rw [zpt, EuclideanSpace.single_apply, if_neg (by decide)]

/-- **`zpt a` is on the z-axis** for `a > 0`: its horizontal coordinates vanish and
its height is `a > 0`. -/
theorem zpt_mem_zAxis {a : ℝ} (ha : 0 < a) : zpt a ∈ zAxis :=
  ⟨zpt_coord0 a, zpt_coord1 a, by rw [zpt_height]; exact ha⟩

/-! ### WALL-2, vertical (shared-horizontal) case — DERIVED

When `x` and `y` already share their two horizontal coordinates they lie on a
common vertical line, and the single horizontal translation
`p ↦ p + (zpt x₂ − x)` carries both onto the z-axis.  Its offset `b = zpt x₂ − x`
has height `(zpt x₂ − x)₂ = x₂ − x₂ = 0`, so it is a genuine horizontal
translation (`zAxisShift_height`), hence a `dH`-isometry
(`horizTranslationIsom`).  The images are computed coordinatewise: `x` maps to
`(0,0,x₂)` unconditionally (the offset was chosen to zero `x`'s horizontal part);
`y` maps to `(0,0,y₂)` because `y` shares that horizontal part. -/

/-- **WALL-2 — vertical (shared-horizontal) two-point normalization (DERIVED,
sorry-free).**  If `x, y ∈ H³` have equal horizontal coordinates (`x₀ = y₀`,
`x₁ = y₁`), a single `dH`-isometry (the horizontal translation by `zpt x₂ − x`)
carries both onto the z-axis. -/
theorem exists_normalization_vertical {x y : E} (hx : x ∈ upperH) (hy : y ∈ upperH)
    (h0 : x 0 = y 0) (h1 : x 1 = y 1) :
    ∃ (Φ : E → E), ∃ _ : IsDHIsometry Φ, Φ x ∈ zAxis ∧ Φ y ∈ zAxis := by
  refine ⟨fun p => p + (zpt (x 2) - x),
    horizTranslationIsom (zAxisShift_height x), ?_, ?_⟩
  · -- `Φ x = x + (zpt x₂ − x) = (0,0,x₂)`, unconditionally on the z-axis
    refine ⟨?_, ?_, ?_⟩
    · show (x + (zpt (x 2) - x)) 0 = 0
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_coord0]; ring
    · show (x + (zpt (x 2) - x)) 1 = 0
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_coord1]; ring
    · show 0 < (x + (zpt (x 2) - x)) 2
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_height]
      have h : x 2 + (x 2 - x 2) = x 2 := by ring
      rw [h]; exact hx
  · -- `Φ y = y + (zpt x₂ − x) = (0,0,y₂)`, using the shared horizontal part
    refine ⟨?_, ?_, ?_⟩
    · show (y + (zpt (x 2) - x)) 0 = 0
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_coord0]
      rw [← h0]; ring
    · show (y + (zpt (x 2) - x)) 1 = 0
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_coord1]
      rw [← h1]; ring
    · show 0 < (y + (zpt (x 2) - x)) 2
      simp only [PiLp.add_apply, PiLp.sub_apply, zpt_height]
      have h : y 2 + (x 2 - x 2) = y 2 := by ring
      rw [h]; exact hy

/-! ### Coordinate helpers for the boundary-inversion computation

The general two-point normalization uses a boundary inversion; verifying that the
two interior points land on a common vertical line reduces to two elementary
coordinate identities on `E = EuclideanSpace ℝ (Fin 3)`:

* `distSq_coords` — `dist p q ² = Σⱼ (pⱼ − qⱼ)²`, the Pythagorean expansion, so a
  Euclidean-sphere condition `‖p − O‖ = R` becomes polynomial in the coordinates;
* `inversion_coord` — the `j`-th coordinate of `inversion c R p` is
  `(R/dist p c)²·(pⱼ − cⱼ) + cⱼ`, extracted from the `+ᵥ`/`•ᵥ` definition exactly
  as `HyperbolicIsometryInversion` does for the height coordinate. -/

/-- **Pythagorean coordinate expansion of the squared Euclidean distance** on
`H³`'s carrier: `dist p q² = (p₀−q₀)² + (p₁−q₁)² + (p₂−q₂)²`.  This turns a
Euclidean-sphere membership `‖p − O‖ = R` into a polynomial identity in the
coordinates, which is what the inversion-image computation consumes. -/
theorem distSq_coords (p q : E) :
    dist p q ^ 2 = (p 0 - q 0) ^ 2 + (p 1 - q 1) ^ 2 + (p 2 - q 2) ^ 2 := by
  rw [EuclideanSpace.dist_eq, Real.sq_sqrt (by positivity), Fin.sum_univ_three]
  simp only [Real.dist_eq, sq_abs]

/-- **The `j`-th coordinate of a boundary inversion.**  `EuclideanGeometry.inversion
c R p = (R/dist p c)²·(p − c) + c`, so coordinatewise
`(inversion c R p)ⱼ = (R/dist p c)²·(pⱼ − cⱼ) + cⱼ`.  Same extraction as
`boundaryInversionIsom.hheight`, but for a general coordinate `j` rather than the
height. -/
theorem inversion_coord (c : E) (R : ℝ) (p : E) (j : Fin 3) :
    (inversion c R p) j = (R / dist p c) ^ 2 * (p j - c j) + c j := by
  have hexp : inversion c R p = (R / dist p c) ^ 2 • (p - c) + c := by
    rw [show inversion c R p = (R / dist p c) ^ 2 • (p -ᵥ c) +ᵥ c from rfl,
      vsub_eq_sub, vadd_eq_add]
  rw [hexp, PiLp.add_apply, PiLp.smul_apply, PiLp.sub_apply, smul_eq_mul]

/-! ### The boundary-inversion horizontal-collapse lemma

The geometric heart of the general case.  Two interior points whose horizontal
parts are (possibly different) multiples `α` of a common unit horizontal
direction `u` and which both lie on a Euclidean sphere centred at `O = c·u` on the
boundary have, after the boundary inversion at the near ideal endpoint
`ξ = (c−R)·u`, coordinates `0` and `1` collapsed to the SAME value `K·uⱼ`,
`K = (c−R) + ρ²/(2R)` — INDEPENDENT of the point.  A later horizontal translation
by `−K·u` then lands both on the z-axis.

The mechanism is the single algebraic identity `‖p − ξ‖² = 2R·(α − (c−R))` valid
for `p` on the sphere: the inversion factor `ρ²/‖p−ξ‖²` times the horizontal
displacement `(α−(c−R))·u` telescopes to `ρ²/(2R)·u`, erasing the point's own `α`. -/

/-- **Boundary-inversion horizontal collapse.**  Let `u` be a unit horizontal
vector (`u₂ = 0`, `u₀²+u₁² = 1`), `R, ρ > 0`, and let `p` have horizontal part
`α·u` (i.e. `p₀ = α·u₀`, `p₁ = α·u₁`), height `β`, and lie on the sphere centred at
`O = c·u` of radius `R`.  Then the boundary inversion at `ξ = (c−R)·u` sends both
horizontal coordinates of `p` to `K·uⱼ` with `K = (c−R) + ρ²/(2R)`, a value
independent of `p`.  (`p ≠ ξ` — automatic for an interior point, whose height is
positive while `ξ` is on the boundary.) -/
theorem invImage_horiz_collapse
    (u : E) (hu2 : u 2 = 0) (hu01 : (u 0) ^ 2 + (u 1) ^ 2 = 1)
    (c R ρ α β : ℝ) (hR : 0 < R) (_hρ : 0 < ρ)
    (p : E) (hp0 : p 0 = α * u 0) (hp1 : p 1 = α * u 1) (hp2 : p 2 = β)
    (hcirc : dist p (c • u) ^ 2 = R ^ 2)
    (hpξ : p ≠ (c - R) • u) :
    (inversion ((c - R) • u) ρ p) 0 = ((c - R) + ρ ^ 2 / (2 * R)) * u 0 ∧
    (inversion ((c - R) • u) ρ p) 1 = ((c - R) + ρ ^ 2 / (2 * R)) * u 1 := by
  set ξ : E := (c - R) • u with hξdef
  have hξ0 : ξ 0 = (c - R) * u 0 := by rw [hξdef, PiLp.smul_apply, smul_eq_mul]
  have hξ1 : ξ 1 = (c - R) * u 1 := by rw [hξdef, PiLp.smul_apply, smul_eq_mul]
  have hξ2 : ξ 2 = 0 := by rw [hξdef, PiLp.smul_apply, smul_eq_mul, hu2, mul_zero]
  have hO0 : (c • u) 0 = c * u 0 := by rw [PiLp.smul_apply, smul_eq_mul]
  have hO1 : (c • u) 1 = c * u 1 := by rw [PiLp.smul_apply, smul_eq_mul]
  have hO2 : (c • u) 2 = 0 := by rw [PiLp.smul_apply, smul_eq_mul, hu2, mul_zero]
  -- circle condition in coordinates: `(α − c)² + β² = R²`
  have hcirc' : (α - c) ^ 2 + β ^ 2 = R ^ 2 := by
    rw [distSq_coords, hp0, hp1, hp2, hO0, hO1, hO2] at hcirc
    nlinarith [hcirc, hu01]
  -- the telescoping identity `‖p − ξ‖² = 2R·(α − (c−R))`
  have hdξ : dist p ξ ^ 2 = 2 * R * (α - (c - R)) := by
    rw [distSq_coords, hp0, hp1, hp2, hξ0, hξ1, hξ2]
    nlinarith [hcirc', hu01]
  have hdξpos : 0 < dist p ξ ^ 2 := by
    have : dist p ξ ≠ 0 := by rw [dist_ne_zero]; exact hpξ
    positivity
  have hαpos : 0 < α - (c - R) := by nlinarith [hdξ ▸ hdξpos, hR]
  refine ⟨?_, ?_⟩
  · rw [inversion_coord, hp0, hξ0, div_pow, hdξ]; field_simp; ring
  · rw [inversion_coord, hp1, hξ1, div_pow, hdξ]; field_simp; ring

/-! ### WALL-2, general (distinct-horizontal) case — DERIVED

The genuine content of bean `qou-0a0z`.  When `x, y` have DISTINCT horizontal
parts, a three-map composition carries both onto the z-axis:

* **`T1`** the horizontal translation `p ↦ p + (zpt x₂ − x)` (as in the vertical
  case) sends `x` to `(0,0,x₂)` and `y` to `w + (0,0,y₂)` with `w` the horizontal
  difference, `d = ‖w‖ > 0`;
* **`T2`** the boundary inversion at the near ideal endpoint
  `ξ = (c−R)·u` (`u = w/d`, `c = (d²+y₂²−x₂²)/(2d)`, `R = √(c²+x₂²)`), which by
  `invImage_horiz_collapse` collapses coords `0,1` of BOTH image points to the
  same `K·uⱼ`;
* **`T3`** the horizontal translation by `−K·u`, zeroing both horizontal
  coordinates.

Every factor is a derived `dH`-isometry (`horizTranslationIsom`,
`boundaryInversionIsom`); `IsDHIsometry.comp` assembles the composite, and
positive height is inherited from `IsDHIsometry.maps`. -/

set_option maxHeartbeats 800000 in
/-- **WALL-2 — general (distinct-horizontal) two-point normalization (DERIVED,
sorry-free).**  If `x, y ∈ H³` have DISTINCT horizontal parts
(`(y₀−x₀)² + (y₁−x₁)² > 0`), a `dH`-isometry (a horizontal translation, then a
boundary inversion at the geodesic's near ideal endpoint, then a horizontal
translation) carries both onto the z-axis. -/
theorem exists_normalization_general {x y : E} (hx : x ∈ upperH) (hy : y ∈ upperH)
    (hne : 0 < (y 0 - x 0) ^ 2 + (y 1 - x 1) ^ 2) :
    ∃ (Φ : E → E), ∃ _ : IsDHIsometry Φ, Φ x ∈ zAxis ∧ Φ y ∈ zAxis := by
  have hapos : (0:ℝ) < x 2 := hx
  have hbpos : (0:ℝ) < y 2 := hy
  -- scalars
  set dsq := (y 0 - x 0) ^ 2 + (y 1 - x 1) ^ 2 with hdsq
  have hdsqpos : 0 < dsq := hne
  set d := Real.sqrt dsq with hddef
  have hdpos : 0 < d := Real.sqrt_pos.mpr hdsqpos
  have hdne : d ≠ 0 := ne_of_gt hdpos
  have hd2 : d ^ 2 = dsq := Real.sq_sqrt (le_of_lt hdsqpos)
  set c := (dsq + (y 2) ^ 2 - (x 2) ^ 2) / (2 * d) with hcdef
  have h2dc : 2 * d * c = dsq + (y 2) ^ 2 - (x 2) ^ 2 := by
    rw [hcdef]; field_simp
  set Rsq := c ^ 2 + (x 2) ^ 2 with hRsqdef
  have hRsqpos : 0 < Rsq := by
    have : 0 < (x 2) ^ 2 := pow_pos hapos 2
    have := sq_nonneg c; rw [hRsqdef]; linarith
  set R := Real.sqrt Rsq with hRdef
  have hRpos : 0 < R := Real.sqrt_pos.mpr hRsqpos
  have hR2 : R ^ 2 = Rsq := Real.sq_sqrt (le_of_lt hRsqpos)
  -- horizontal unit direction `u = w / d`
  set hw : E := (y - x) - zpt ((y - x) 2) with hhwdef
  have hhw0 : hw 0 = y 0 - x 0 := by
    rw [hhwdef, PiLp.sub_apply, zpt_coord0, sub_zero, PiLp.sub_apply]
  have hhw1 : hw 1 = y 1 - x 1 := by
    rw [hhwdef, PiLp.sub_apply, zpt_coord1, sub_zero, PiLp.sub_apply]
  have hhw2 : hw 2 = 0 := by
    rw [hhwdef, PiLp.sub_apply, zpt_height, PiLp.sub_apply, sub_self]
  set u : E := d⁻¹ • hw with hudef
  have hu0 : u 0 = (y 0 - x 0) / d := by
    rw [hudef, PiLp.smul_apply, smul_eq_mul, hhw0, div_eq_inv_mul]
  have hu1 : u 1 = (y 1 - x 1) / d := by
    rw [hudef, PiLp.smul_apply, smul_eq_mul, hhw1, div_eq_inv_mul]
  have hu2 : u 2 = 0 := by
    rw [hudef, PiLp.smul_apply, smul_eq_mul, hhw2, mul_zero]
  have hu01 : (u 0) ^ 2 + (u 1) ^ 2 = 1 := by
    rw [hu0, hu1, div_pow, div_pow, ← add_div, hd2]
    exact div_self (ne_of_gt hdsqpos)
  -- the images `A' = T1 x` and `B' = T1 y`, K, and the two translations
  set b1 : E := zpt (x 2) - x with hb1def
  have hb1h : b1 2 = 0 := zAxisShift_height x
  set K := (c - R) + (1:ℝ) ^ 2 / (2 * R) with hKdef
  set b3 : E := (-K) • u with hb3def
  have hb3h : b3 2 = 0 := by rw [hb3def, PiLp.smul_apply, smul_eq_mul, hu2, mul_zero]
  -- ξ 2 = 0 (inversion centre is on the boundary)
  have hξ2 : ((c - R) • u) 2 = 0 := by rw [PiLp.smul_apply, smul_eq_mul, hu2, mul_zero]
  -- `A' = T1 x = zpt x₂`
  have hAeq : x + b1 = zpt (x 2) := by rw [hb1def, add_sub_cancel]
  -- `B' = T1 y` coordinates
  have hBeq0 : (y + b1) 0 = y 0 - x 0 := by
    rw [hb1def, PiLp.add_apply, PiLp.sub_apply, zpt_coord0, zero_sub]; ring
  have hBeq1 : (y + b1) 1 = y 1 - x 1 := by
    rw [hb1def, PiLp.add_apply, PiLp.sub_apply, zpt_coord1, zero_sub]; ring
  have hBeq2 : (y + b1) 2 = y 2 := by
    rw [hb1def, PiLp.add_apply, PiLp.sub_apply, zpt_height]; ring
  -- collapse on A' (α = 0)
  have hAcirc : dist (zpt (x 2)) (c • u) ^ 2 = R ^ 2 := by
    rw [distSq_coords, zpt_coord0, zpt_coord1, zpt_height,
      show (c • u) 0 = c * u 0 from by rw [PiLp.smul_apply, smul_eq_mul],
      show (c • u) 1 = c * u 1 from by rw [PiLp.smul_apply, smul_eq_mul],
      show (c • u) 2 = 0 from by rw [PiLp.smul_apply, smul_eq_mul, hu2, mul_zero],
      hR2, hRsqdef]
    nlinarith [hu01]
  have hAne : zpt (x 2) ≠ (c - R) • u := by
    intro h; have : (zpt (x 2)) 2 = ((c - R) • u) 2 := by rw [h]
    rw [zpt_height, hξ2] at this; exact (ne_of_gt hapos) this
  have hAcol := invImage_horiz_collapse u hu2 hu01 c R 1 0 (x 2) hRpos one_pos
    (zpt (x 2)) (by rw [zpt_coord0]; ring) (by rw [zpt_coord1]; ring) (zpt_height _)
    hAcirc hAne
  -- collapse on B' (α = d)
  have hBcirc : dist (y + b1) (c • u) ^ 2 = R ^ 2 := by
    rw [distSq_coords, hBeq0, hBeq1, hBeq2,
      show (c • u) 0 = c * u 0 from by rw [PiLp.smul_apply, smul_eq_mul],
      show (c • u) 1 = c * u 1 from by rw [PiLp.smul_apply, smul_eq_mul],
      show (c • u) 2 = 0 from by rw [PiLp.smul_apply, smul_eq_mul, hu2, mul_zero],
      hu0, hu1, hR2, hRsqdef]
    field_simp
    nlinarith [hu01, hd2, h2dc, sq_nonneg (y 0 - x 0), sq_nonneg (y 1 - x 1)]
  have hBne : y + b1 ≠ (c - R) • u := by
    intro h; have : (y + b1) 2 = ((c - R) • u) 2 := by rw [h]
    rw [hBeq2, hξ2] at this; exact (ne_of_gt hbpos) this
  have hBcol := invImage_horiz_collapse u hu2 hu01 c R 1 d (y 2) hRpos one_pos
    (y + b1) (by rw [hBeq0, hu0]; field_simp) (by rw [hBeq1, hu1]; field_simp)
    hBeq2 hBcirc hBne
  -- assemble Φ = T3 ∘ T2 ∘ T1
  have hb30 : b3 0 = (-K) * u 0 := by rw [hb3def, PiLp.smul_apply, smul_eq_mul]
  have hb31 : b3 1 = (-K) * u 1 := by rw [hb3def, PiLp.smul_apply, smul_eq_mul]
  have hΦ : IsDHIsometry
      ((fun p => p + b3) ∘ (inversion ((c - R) • u) 1) ∘ (fun p => p + b1)) :=
    ((horizTranslationIsom hb3h).comp (boundaryInversionIsom hξ2 one_pos)).comp
      (horizTranslationIsom hb1h)
  refine ⟨_, hΦ, ?_, ?_⟩
  · -- Φ x ∈ zAxis
    refine ⟨?_, ?_, hΦ.maps hx⟩
    · simp only [Function.comp_apply, hAeq, PiLp.add_apply, hAcol.1, hb30, hKdef]; ring
    · simp only [Function.comp_apply, hAeq, PiLp.add_apply, hAcol.2, hb31, hKdef]; ring
  · -- Φ y ∈ zAxis
    refine ⟨?_, ?_, hΦ.maps hy⟩
    · simp only [Function.comp_apply, PiLp.add_apply, hBcol.1, hb30, hKdef]; ring
    · simp only [Function.comp_apply, PiLp.add_apply, hBcol.2, hb31, hKdef]; ring

/-! ### WALL-2, full two-point normalization — DERIVED (bean `qou-0a0z`, CLOSED)

The two cases combine into the unconditional statement: ANY two points of `H³`
can be carried onto the z-axis by a `dH`-isometry.  If they share their horizontal
part, the single horizontal translation of `exists_normalization_vertical`
suffices; otherwise the horizontal-difference is nonzero and
`exists_normalization_general` applies.  No `HypMinimizerUnique` instance is
fabricated — the reduction is a genuine derivation. -/

/-- **WALL-2 — full two-point normalization to the z-axis (DERIVED, sorry-free).**
For ANY `x, y ∈ H³` there is a `dH`-isometry `Φ` carrying both `Φ x` and `Φ y`
onto the z-axis.  The shared-horizontal case reuses the single translation of
`exists_normalization_vertical`; the distinct-horizontal case is the boundary-
inversion construction of `exists_normalization_general`.  This is the geometric
reduction that carries geodesic uniqueness between two arbitrary points down to
the already-derived z-axis case (`dH_zpt`). -/
theorem exists_normalization {x y : E} (hx : x ∈ upperH) (hy : y ∈ upperH) :
    ∃ (Φ : E → E), ∃ _ : IsDHIsometry Φ, Φ x ∈ zAxis ∧ Φ y ∈ zAxis := by
  by_cases h : x 0 = y 0 ∧ x 1 = y 1
  · exact exists_normalization_vertical hx hy h.1 h.2
  · refine exists_normalization_general hx hy ?_
    rw [not_and_or] at h
    rcases h with h0 | h1
    · have hz : y 0 - x 0 ≠ 0 := sub_ne_zero.mpr (Ne.symm h0)
      have hpos : 0 < (y 0 - x 0) ^ 2 := by positivity
      nlinarith [sq_nonneg (y 1 - x 1)]
    · have hz : y 1 - x 1 ≠ 0 := sub_ne_zero.mpr (Ne.symm h1)
      have hpos : 0 < (y 1 - x 1) ^ 2 := by positivity
      nlinarith [sq_nonneg (y 0 - x 0)]

end QOU.Archimedean
