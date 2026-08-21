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

## What is NOT proved here (honest wall, tracked as a bean, NOT stubbed)

The **general** two-point case (`x, y` with distinct horizontal parts) is the
genuine content of bean `qou-0a0z` and is NOT closed in this file — it is left as
a precise `-- GAP:` note, not a `sorry` and not a fabricated instance, per
AGENTS.md ("if you cannot close a derivation, CREATE A BEAN — not a `sorry`").
The obstruction is purely the Euclidean *endpoint algebra*: the geodesic through
two points with distinct horizontal parts is a boundary-centred semicircle whose
two ideal endpoints `ξ, η ∈ ∂H³` must be computed (centre on `{z=0}`, radius from
the perpendicular bisector) before an inversion `ξ ↦ 0`, `η ↦ ∞` straightens the
geodesic to a vertical line, which a final horizontal translation lands on the
z-axis.  Every ISOMETRY ingredient that route needs is already derived and
composes via `IsDHIsometry.comp`; only the semicircle-endpoint construction and
the verification that the composite lands `x, y` on the z-axis remain.  This file
stays 100 % sorry-free; the `HypMinimizerUnique` conjecture in
`HyperbolicGeodesic` is left untouched (no fabricated instance).

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

/-! ### WALL-2, general case — HONEST GAP (bean `qou-0a0z`, NOT stubbed)

The general two-point normalization — `x, y ∈ H³` with **distinct** horizontal
parts — is NOT proved here.  It is not a `sorry` and not a fabricated
`HypMinimizerUnique` instance; it is an explicit gap, tracked as bean `qou-0a0z`.

`-- GAP:` The isometry infrastructure is complete: `IsDHIsometry.comp` (above)
composes the WALL-1 boundary-similarity generators (`dilationIsom`,
`horizTranslationIsom`, `heightFixingLinearIsom`) with the boundary inversion
(`boundaryInversionIsom`), and every one of those is already a derived
`dH`-isometry.  What remains is the Euclidean **endpoint algebra**, which involves
square roots and has no ready Mathlib lemma:

  1. the geodesic through `x, y` (distinct horizontal parts) is the semicircle in
     the vertical plane `V` spanned by `x, y, e_z`, centred at the point
     `c ∈ V ∩ {z = 0}` equidistant (Euclidean) from `x` and `y`, of radius
     `R = ‖x − c‖`;  its two ideal endpoints are `ξ, η = c ± R·û` for the unit
     horizontal direction `û` of `V`;
  2. a horizontal translation by `−ξ` sends `ξ ↦ 0`;  the boundary inversion
     `inversion 0 1` sends `0 ↦ ∞` and `η − ξ ↦ (η − ξ)/‖η − ξ‖²`, so the
     geodesic becomes the vertical line through that image;
  3. a final horizontal translation lands that vertical line on the z-axis.

The composite `Φ` is then an `IsDHIsometry` by `IsDHIsometry.comp`, and — because
`x, y` lie on their geodesic and `Φ` maps that geodesic to the z-axis — `Φ x` and
`Φ y` land on `zAxis`.  Closing this needs (1) a Lean construction of `c, R, û`
with the perpendicular-bisector / boundary-intersection identities, and (2) the
image-coordinate verification.  Deferred to bean `qou-0a0z`. -/

end QOU.Archimedean
