import Mathlib.Tactic

/-!
# Yekutieli Non-Abelian Integration — discrete holonomy layer

This file builds the **discrete / lattice** core of Yekutieli's non-abelian
multiplicative integration: the *path-ordered product* (holonomy) of a path
presented as an ordered list of segment transports, and the *plaquette
holonomy* / discrete curvature of a square loop.

## What is and isn't formalised here

* **Formalised, sorry-free (algebraic layer).** The path-ordered product is
  a non-commutative `List.prod` in a monoid/group; its structural laws —
  concatenation multiplicativity (`holonomy_append`, the composition law of
  the non-abelian line integral), the empty/singleton evaluations, and the
  reverse-path inverse (`holonomy_reverse_map_inv`) — are proved outright.
  The *plaquette holonomy* of a square loop and the **flatness of a pure-gauge
  (exact) connection** (`loopHolonomyPureGauge_eq_one`) — the discrete
  non-abelian analogue of "the curvature of an exact connection vanishes",
  i.e. `d² = 0` at lattice level — are proved by group telescoping.

* **NOT formalised (the continuum, genuinely not in Mathlib).** The
  path-ordered *exponential* `P exp ∫_γ A` as the mesh→0 limit of these
  ordered products, the smooth curvature 2-form `F = dA + A ∧ A`, and the
  continuum non-abelian Stokes theorem on surfaces. These are the analytic
  statements the [`yekutieli_leading_coefficient`](../Archimedean/yekutieli_leading_coefficient.lean)
  lemma still carries as the axiomatised `YekutieliStokesNormalisation`
  class. This file is the foundational algebraic layer *below* that class,
  not a discharge of it (AGENTS.md "Axiomatization is NOT a Proof").

## References

- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian
  multiplicative integration and Stokes' theorem on surfaces.
- Ref: [manuscript] quantum-observable-universe/brings-surface/yekutieli-leading-coefficient.md

**Base ring (§7c).** Purely algebraic: a generic non-commutative `Monoid` /
`Group` `G`. No `ℝ`, no ordering, no `Real.*` — the discrete holonomy is an
ordered product, independent of any archimedean structure.
-/

namespace QOU.MathlibExt.YekutieliIntegration

variable {G : Type*}

/-- **Path-ordered product (discrete non-abelian line integral).**

    The holonomy of a path presented as an ordered list of segment
    transports `[g₀, g₁, …, g_{n-1}]` is their ordered product
    `g₀ * g₁ * … * g_{n-1}` — segments composed in path order.  This is the
    discrete / lattice realisation of the path-ordered exponential
    `P exp ∫_γ A`; the continuum limit (mesh → 0) is analytic and is *not*
    formalised here. -/
def holonomy [Monoid G] (segs : List G) : G := segs.prod

@[simp] theorem holonomy_nil [Monoid G] : holonomy ([] : List G) = 1 := rfl

@[simp] theorem holonomy_singleton [Monoid G] (g : G) : holonomy [g] = g :=
  List.prod_singleton

@[simp] theorem holonomy_cons [Monoid G] (g : G) (segs : List G) :
    holonomy (g :: segs) = g * holonomy segs := by
  simp [holonomy]

/-- **Concatenation multiplicativity** — the composition law of the
    non-abelian line integral: the holonomy of a path split into an initial
    piece `p` followed by `q` is the ordered product of the two holonomies.
    This is the discrete non-abelian Stokes composition along paths. -/
theorem holonomy_append [Monoid G] (p q : List G) :
    holonomy (p ++ q) = holonomy p * holonomy q := by
  simp [holonomy, List.prod_append]

/-- **Reverse path gives the inverse holonomy.**  Traversing the path
    backwards with each segment transport inverted yields the inverse of the
    forward holonomy — the discrete statement that the holonomy of `γ⁻¹` is
    `(hol γ)⁻¹`. -/
theorem holonomy_reverse_map_inv [Group G] (segs : List G) :
    holonomy ((segs.map (·⁻¹)).reverse) = (holonomy segs)⁻¹ := by
  simp [holonomy, List.prod_inv_reverse]

/-- **Plaquette holonomy of a pure-gauge (exact) connection.**

    Assign group elements `h₀, h₁, h₂, h₃` to the four vertices of a square
    and take the connection to be *exact / pure gauge*: the transport along
    the edge from vertex `i` to vertex `j` is `hⱼ * hᵢ⁻¹` (a discrete
    gradient).  The boundary holonomy of the square loop
    `v₀ → v₁ → v₂ → v₃ → v₀` is the ordered product of the four edge
    transports. -/
def loopHolonomyPureGauge [Group G] (h₀ h₁ h₂ h₃ : G) : G :=
  holonomy [h₀ * h₃⁻¹, h₃ * h₂⁻¹, h₂ * h₁⁻¹, h₁ * h₀⁻¹]

/-- **Flatness of a pure-gauge connection** — the discrete non-abelian
    `d² = 0` / Stokes flatness: an exact (pure-gauge) connection has trivial
    plaquette holonomy, so its discrete curvature vanishes.  Proved by group
    telescoping. -/
theorem loopHolonomyPureGauge_eq_one [Group G] (h₀ h₁ h₂ h₃ : G) :
    loopHolonomyPureGauge h₀ h₁ h₂ h₃ = 1 := by
  unfold loopHolonomyPureGauge holonomy
  simp only [List.prod_cons, List.prod_nil, mul_one]
  group

/-- **Discrete curvature defect** of a square plaquette: the boundary
    holonomy itself, measured against the identity.  The connection is *flat*
    at the plaquette iff this equals `1`; `loopHolonomyPureGauge_eq_one` says
    every exact connection is flat. -/
def IsFlatPlaquette [Group G] (boundary : G) : Prop := boundary = 1

theorem isFlatPlaquette_pureGauge [Group G] (h₀ h₁ h₂ h₃ : G) :
    IsFlatPlaquette (loopHolonomyPureGauge h₀ h₁ h₂ h₃) :=
  loopHolonomyPureGauge_eq_one h₀ h₁ h₂ h₃

/-- The trivial (constant) loop is flat. -/
@[simp] theorem isFlatPlaquette_one [Group G] : IsFlatPlaquette (1 : G) := rfl

/-- **Flatness is closed under composition.**  Concatenating two flat loops
    multiplies their holonomies (`holonomy_append`); the composite is flat.
    A surface tiled by flat plaquettes therefore has flat boundary. -/
theorem isFlatPlaquette_mul [Group G] {a b : G}
    (ha : IsFlatPlaquette a) (hb : IsFlatPlaquette b) :
    IsFlatPlaquette (a * b) := by
  simp only [IsFlatPlaquette] at *
  rw [ha, hb, mul_one]

/-- **Gauge invariance of flatness.**  A gauge transformation acts on a
    based-loop holonomy by conjugation `b ↦ u * b * u⁻¹`; the curvature
    defect is gauge-*covariant*, so its vanishing (flatness) is
    gauge-*invariant*. -/
theorem isFlatPlaquette_conj [Group G] (u : G) {b : G}
    (hb : IsFlatPlaquette b) : IsFlatPlaquette (u * b * u⁻¹) := by
  simp only [IsFlatPlaquette] at *
  rw [hb]; group

/-- **Abelian degeneration** (`CommMonoid`): the path-ordering of the
    holonomy collapses — reordering the segments (deforming the path in the
    commutative limit) leaves the holonomy unchanged.  This is the classical
    limit where Yekutieli's non-abelian Stokes reduces to ordinary
    (abelian) Stokes and the surface-ordering is irrelevant. -/
theorem holonomy_perm [CommMonoid G] {p q : List G} (h : p.Perm q) :
    holonomy p = holonomy q := by
  simp only [holonomy]; exact h.prod_eq

end QOU.MathlibExt.YekutieliIntegration
