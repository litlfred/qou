/-
# HyperbolicGeodesic.lean (C3) — the honest wall, and the conditional
# totally-geodesic classification.

With the metric `dH` and the two boundary isometries now DERIVED
(`HyperbolicMetric`, `HyperbolicIsometryReflection`,
`HyperbolicIsometryInversion`), this file states what remains genuinely open —
geodesic existence + uniqueness in `H³` — as a **content-bearing class**, and
proves, *conditional on it*, that the fixed set of
each boundary isometry is totally geodesic.  That is the vertical-plane /
hemisphere classification Thurston cites: here it is DERIVED from the isometries
plus the single named uniqueness hypothesis, not adopted.

## What is a minimizer here (`IsHypMinimizer`)

A constant-speed length-minimiser: an admissible path whose length equals `dH x
y` and whose hyperbolic speed `‖γ'‖/z` is constant along `[0,1]`.  Constant speed
pins the CANONICAL parametrisation — the geodesic one — so that uniqueness is the
*true* geodesic-uniqueness statement (unique up to nothing), not the false
"unique up to reparametrisation".  A length-minimiser can always be reparametrised
to constant speed without changing its length, so this is the standard geodesic
convention, not a restriction of content.

## The wall (`HypMinimizerUnique`) — since CLOSED

**Status update:** the class is now inhabited without assumption —
`hypMinimizerUnique_derived` (`QOU.Archimedean.HyperbolicGeodesicUniqueness`,
sorry-free) and the instance `instHypMinimizerUnique`
(`QOU.Archimedean.TotallyGeodesicUnconditional`). The paragraph below is the
original statement of the wall, kept as the record of what was proved.

`HypMinimizerUnique` axiomatises exactly ONE proposition: between two points of
`H³` a constant-speed minimiser is unique (pointwise).  This is the real Mathlib-
scale gap — Mathlib 4.24.0 has no hyperbolic Riemannian geometry, no geodesics,
no `exp`, no uniqueness theorem — and it is stated as an open `class` with a
content-bearing field and **no instance**.  It is a *primary* conjecture (its
signature binds no other conjecture class).  Per AGENTS.md this is honest
representation of an open problem, NOT laundering: the field states the genuine
uniqueness proposition, and no trivial instance is fabricated to "close" it.

  * **Existence** of such minimisers is *also* open (same wall).  The
    classification below is therefore conditional AND vacuous-safe: it says only
    that IF a minimiser between two face points exists, its segment stays in the
    face.  It fabricates no minimiser.

## What is DERIVED (sorry-free, modulo the class hypothesis)

`fixedSet_isTotallyGeodesic` — for any `dH`-isometry `φ` that is involutive, the
fixed set `{p | φ p = p}` is totally geodesic: given `x, y ∈ Fix(φ)` and a
minimiser `γ`, the image `φ ∘ γ` is again a minimiser between the same endpoints
(here `φ` fixes them), so by uniqueness `γ t = (φ∘γ) t = φ(γ t)`, i.e. `γ t ∈
Fix(φ)`.  Instantiated at the vertical reflection and at a boundary inversion,
this gives the two Thurston families:

  * `verticalPlaneFix_isTotallyGeodesic` — the vertical plane `Fix(reflection)`;
  * `hemisphereFix_isTotallyGeodesic` — the hemisphere `Fix(inversion c R)`.

Only the `[HypMinimizerUnique]` hypothesis is used; `#print axioms` on these
shows it and no `sorryAx`.

## Drain accounting (what this whole T2 tranche changes)

DERIVED now: the metric `dH` (an inf of path lengths, not an adopted `ds²`), and
both isometries.  CITED/OPEN now: **only** minimizer existence + uniqueness (the
`HypMinimizerUnique` conjecture).  The unused exhaustiveness half of the old
`GeodesicFaceH3` citation ("these are the ONLY totally-geodesic surfaces") is not
part of the obligation and is dropped.

Archimedean (ℝ): `‖·‖`, ordering — §7c.

  -- Ref: [thurston1978] Ch. 2 §2.3 p. 12 (geodesics), §2.1 p. 10 (two-planes)
  -- Ref: [ratcliffe] §4.6–4.7 (geodesics and totally-geodesic surfaces of `H³`)
  -- Ref: [benedetti-petronio] §A ; [milnor1982] Appendix
  -- Ref: [leitner2026] beans qou-473l (T2 C3), qou-idvt (T2), qou-r111 (the
  --   geodesic-uniqueness wall)
-/

import QOU.Archimedean.HyperbolicIsometryReflection
import QOU.Archimedean.HyperbolicIsometryInversion

namespace QOU.Archimedean

open QOU.Archimedean.HyperbolicMetric EuclideanGeometry
open scoped ENNReal

/-- **Hyperbolic (local) speed** of a path `γ` at `t`: the line element `‖γ'‖/z`
whose integral is `pathLenH`. -/
noncomputable def hypSpeed (γ : ℝ → E) (t : ℝ) : ℝ := ‖deriv γ t‖ / (γ t) 2

/-- **A constant-speed length-minimiser** from `x` to `y`: an admissible path of
minimal hyperbolic length whose speed is constant along `[0,1]`.  Constant speed
is the canonical (geodesic) parametrisation — see the file header. -/
structure IsHypMinimizer (γ : ℝ → E) (x y : E) : Prop where
  admissible : AdmissiblePath γ x y
  minimal : pathLenH γ 0 1 = dH x y
  constSpeed : ∀ s ∈ Set.Icc (0 : ℝ) 1, ∀ t ∈ Set.Icc (0 : ℝ) 1, hypSpeed γ s = hypSpeed γ t

/-- **Totally geodesic** (minimiser-convexity form): every minimiser between two
points of `S` has its whole segment `γ([0,1])` inside `S`.  This is the only form
statable without a Riemannian second fundamental form; it is exactly the property
the classification proves. -/
def IsTotallyGeodesic (S : Set E) : Prop :=
  ∀ x ∈ S, ∀ y ∈ S, ∀ γ : ℝ → E, IsHypMinimizer γ x y → ∀ t ∈ Set.Icc (0 : ℝ) 1, γ t ∈ S

/-- **THE WALL — geodesic uniqueness in `H³`, an open conjecture.**  Between two
points of `H³`, a constant-speed minimiser is unique (pointwise on `[0,1]`).

This is the one genuinely open, Mathlib-scale input of the whole T2 development.
It is axiomatised as a `class` with a **content-bearing** field — a real
`∀`-quantified equality, the honest uniqueness proposition — and is deliberately
given **NO instance**: the open state is a content-bearing carrier with no
witness, per AGENTS.md §3b-tax.  It is a *primary* conjecture (no other
conjecture class appears in its signature).  Existence of minimisers is part of
the same wall and is likewise not asserted. -/
class HypMinimizerUnique : Prop where
  unique : ∀ x ∈ upperH, ∀ y ∈ upperH, ∀ γ δ : ℝ → E,
    IsHypMinimizer γ x y → IsHypMinimizer δ x y →
    ∀ t ∈ Set.Icc (0 : ℝ) 1, γ t = δ t

/-- **The fixed set of an involutive `dH`-isometry is totally geodesic**
(conditional on `HypMinimizerUnique`).

Given `x, y ∈ Fix(φ)` and a minimiser `γ` between them, the image `φ ∘ γ` is again
a minimiser between the same endpoints — `φ` preserves admissibility, length
(`pathLenH_comp`), and constant speed (`speed_comp`), and fixes `x, y`.  By
uniqueness `γ t = (φ ∘ γ) t = φ (γ t)`, so `γ t ∈ Fix(φ)`.  A GENUINE conditional
derivation: it uses the isometry structure and the named uniqueness hypothesis,
and derives — never assumes — the conclusion. -/
theorem fixedSet_isTotallyGeodesic [HypMinimizerUnique] {φ : E → E}
    (h : IsDHIsometry φ) {x y : E} (hx : φ x = x) (hy : φ y = y)
    {γ : ℝ → E} (hγ : IsHypMinimizer γ x y) {t : ℝ} (ht : t ∈ Set.Icc (0 : ℝ) 1) :
    φ (γ t) = γ t := by
  have h0 : (0 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by constructor <;> norm_num
  have h1 : (1 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by constructor <;> norm_num
  -- endpoints lie in `H³` (they are values of an admissible path).
  have hxu : x ∈ upperH := by
    have := hγ.admissible.mem 0 h0; rwa [hγ.admissible.source] at this
  have hyu : y ∈ upperH := by
    have := hγ.admissible.mem 1 h1; rwa [hγ.admissible.target] at this
  -- the image path is again a minimiser from `x` to `y`.
  have hδadm : AdmissiblePath (φ ∘ γ) x y := by
    have hc := h.admissiblePath_comp hγ.admissible
    rwa [hx, hy] at hc
  have hδmin : IsHypMinimizer (φ ∘ γ) x y := by
    refine ⟨hδadm, ?_, ?_⟩
    · rw [h.pathLenH_comp hγ.admissible.diff hγ.admissible.mem]; exact hγ.minimal
    · intro s hs t' ht'
      have es : hypSpeed (φ ∘ γ) s = hypSpeed γ s :=
        h.speed_comp hγ.admissible.diff hγ.admissible.mem hs
      have et : hypSpeed (φ ∘ γ) t' = hypSpeed γ t' :=
        h.speed_comp hγ.admissible.diff hγ.admissible.mem ht'
      rw [es, et]; exact hγ.constSpeed s hs t' ht'
  -- pointwise uniqueness: `γ t = (φ ∘ γ) t = φ (γ t)`.
  exact (HypMinimizerUnique.unique x hxu y hyu γ (φ ∘ γ) hγ hδmin t ht).symm

/-! ### The two Thurston families, as fixed sets of the derived isometries -/

/-- The **vertical plane** as the fixed set of the vertical reflection — the
Euclidean plane `{x = 0}` (all heights), a genuine vertical geodesic plane. -/
def verticalPlaneFix : Set E := {p | verticalReflection p = p}

/-- **The vertical plane is totally geodesic** (conditional on the geodesic-
uniqueness wall) — DERIVED from `dH_verticalReflection`'s isometry via
`fixedSet_isTotallyGeodesic`. -/
theorem verticalPlaneFix_isTotallyGeodesic [HypMinimizerUnique] :
    IsTotallyGeodesic verticalPlaneFix := by
  intro x hx y hy γ hγ t ht
  exact fixedSet_isTotallyGeodesic verticalReflectionIsom hx hy hγ ht

/-- The **hemisphere** as the fixed set of a boundary inversion — the Euclidean
sphere `{‖p - c‖ = R}` centred at the boundary point `c`; its `H³` part is the
hemisphere Thurston classifies. -/
def hemisphereFix (c : E) (R : ℝ) : Set E := {p | inversion c R p = p}

/-- **The hemisphere is totally geodesic** (conditional on the geodesic-
uniqueness wall) — DERIVED from `dH_boundaryInversion`'s isometry via
`fixedSet_isTotallyGeodesic`. -/
theorem hemisphereFix_isTotallyGeodesic [HypMinimizerUnique] {c : E} (hc : c 2 = 0)
    {R : ℝ} (hR : 0 < R) : IsTotallyGeodesic (hemisphereFix c R) := by
  intro x hx y hy γ hγ t ht
  exact fixedSet_isTotallyGeodesic (boundaryInversionIsom hc hR)
    hx hy hγ ht

end QOU.Archimedean
