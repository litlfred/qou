/-
# The four-shape octahedron **degenerates** at the pinched (torus-knot) crossing

`2509.02354` (McPhail-Snyder–Reshetikhin) §4 assigns a crossing's ideal octahedron four ideal
tetrahedra with shape-logs `ζ⁰_r, ζ⁰_t, ζ⁰_l, ζ⁰_b` (eq 4.11–4.14), functions of the six
`χ`-coloring log-parameters `β₁, β₂, β₁', β₂', μ₁, μ₂`:

```
ζ⁰_r = ε(β₂' − β₁)              ζ⁰_t = ε(β₂ − β₁ − μ₁)
ζ⁰_l = ε(β₂ − β₁' + μ₂ − μ₁)    ζ⁰_b = ε(β₂' − β₁' + μ₂)
```

The bar-even second-elementary-symmetric form `e₂ = Σ_{i<j} ζ⁰_i ζ⁰_j` is the object the corpus
identified as the carrier of the deuteron's bar-even binding coefficient `g₂` (the octahedral `e₂`
finite part, `octahedral_e2_coloring_quadratic_probe.py`).

**The deuteron closure `σ₁³` is the trefoil `T(2,3)`, a torus knot — its crossings are *pinched***
(§5.2, Def 5.3: the incoming over/under eigenspaces coincide). At a pinched crossing the *standard*
log-coloring (§5.2, eq 5.7) is

```
β₁ = β,   β₂ = β + μ₁,   β₁' = β + μ₂,   β₂' = β.
```

This file proves — as a pure `CommRing` identity (§7c: generic `R`, no `ℝ`; the archimedean
evaluation is downstream) — that **at the standard pinch all four shape-logs vanish**, hence
`e₁ = 0` and `e₂ = 0`. So the "four-shape octahedron" has **no four-distinct-shape content at the
pinched trefoil**: the four ideal tetrahedra collapse to the single degenerate shape
(`ζ⁰_j = 0 ⇔ e^{2πiζ⁰_j} = 1`), and the octahedral `e₂` that was posited to carry `g₂` is
identically zero there.

Consequence for the `g₂`/`r` chase: the bar-even coefficient `g₂` cannot be the naive octahedral
`e₂` of the four MSR shape-logs (that is `0` in the pinched limit that actually applies). The
`−h²` established from the boundary rep (`trefoil_octahedral_shape_from_rep_probe.py`) is the
**eigenspace cross-ratio** of the crossing, a *different* invariant from the four `ζ⁰_j` shapes —
it is not an MSR tetrahedron shape, so an amplitude built on it (e.g. the lifted dilogarithm) is a
plausible-but-not-rigorously-assigned object. See the companion probe/audit for the one principled
evaluation of that amplitude (`Re L = ¼ ln(1+h²)`, giving `r ≈ −2.1%`, wrong sign vs the measured
`+0.87%`).

This file does **not** derive `g₂` or `r`; it makes precise, and machine-checks, the degeneracy that
sharpens the honest wall.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

-- The four shape-log definitions share one uniform 7-argument `χ`-coloring signature
-- (§4.11–4.14); not every shape-log mentions every coordinate, which is expected.
set_option linter.unusedVariables false

namespace QOU.MassTheory.PinchedOctahedron

variable {R : Type*} [CommRing R]

/-- MSR eq (4.11): the **right** tetrahedron shape-log. -/
def zeta0_r (ε β₁ β₂ β₁' β₂' μ₁ μ₂ : R) : R := ε * (β₂' - β₁)

/-- MSR eq (4.12): the **top** tetrahedron shape-log. -/
def zeta0_t (ε β₁ β₂ β₁' β₂' μ₁ μ₂ : R) : R := ε * (β₂ - β₁ - μ₁)

/-- MSR eq (4.13): the **left** tetrahedron shape-log. -/
def zeta0_l (ε β₁ β₂ β₁' β₂' μ₁ μ₂ : R) : R := ε * (β₂ - β₁' + μ₂ - μ₁)

/-- MSR eq (4.14): the **bottom** tetrahedron shape-log. -/
def zeta0_b (ε β₁ β₂ β₁' β₂' μ₁ μ₂ : R) : R := ε * (β₂' - β₁' + μ₂)

/-- The bar-odd linear order `e₁ = Σ ζ⁰_j`. -/
def e1 (r t l b : R) : R := r + t + l + b

/-- The bar-even quadratic order `e₂ = Σ_{i<j} ζ⁰_i ζ⁰_j` — the posited carrier of `g₂`. -/
def e2 (r t l b : R) : R := r*t + r*l + r*b + t*l + t*b + l*b

/-! ## The standard pinched log-coloring collapses every shape-log

Substituting the standard pinch (eq 5.7) `β₁ = β`, `β₂ = β + μ₁`, `β₁' = β + μ₂`, `β₂' = β`
into each shape-log yields `0`, for **any** `ε` and **any** meridian log-parameters `μ₁, μ₂`. -/

@[simp] theorem zeta0_r_pinch (ε β μ₁ μ₂ : R) :
    zeta0_r ε β (β + μ₁) (β + μ₂) β μ₁ μ₂ = 0 := by
  dsimp [zeta0_r]
  ring

@[simp] theorem zeta0_t_pinch (ε β μ₁ μ₂ : R) :
    zeta0_t ε β (β + μ₁) (β + μ₂) β μ₁ μ₂ = 0 := by
  dsimp [zeta0_t]
  ring

@[simp] theorem zeta0_l_pinch (ε β μ₁ μ₂ : R) :
    zeta0_l ε β (β + μ₁) (β + μ₂) β μ₁ μ₂ = 0 := by
  dsimp [zeta0_l]
  ring

@[simp] theorem zeta0_b_pinch (ε β μ₁ μ₂ : R) :
    zeta0_b ε β (β + μ₁) (β + μ₂) β μ₁ μ₂ = 0 := by
  dsimp [zeta0_b]
  ring

/-- **The octahedral `e₁` vanishes at the standard pinch.** -/
theorem e1_pinch (ε β μ₁ μ₂ : R) :
    e1 (zeta0_r ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_t ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_l ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_b ε β (β + μ₁) (β + μ₂) β μ₁ μ₂) = 0 := by
  dsimp [e1, zeta0_r, zeta0_t, zeta0_l, zeta0_b]
  ring

/-- **The octahedral `e₂` (posited carrier of `g₂`) vanishes identically at the standard pinch.**
So the four-shape octahedron has no four-distinct-shape content at the pinched trefoil, and `g₂`
cannot be this `e₂`. -/
theorem e2_pinch (ε β μ₁ μ₂ : R) :
    e2 (zeta0_r ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_t ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_l ε β (β + μ₁) (β + μ₂) β μ₁ μ₂)
       (zeta0_b ε β (β + μ₁) (β + μ₂) β μ₁ μ₂) = 0 := by
  dsimp [e2, zeta0_r, zeta0_t, zeta0_l, zeta0_b]
  ring

/-! ## The octahedral gluing constraint (holds off the pinch too)

Independently of the pinch, the four MSR shape-logs satisfy the octahedron edge-gluing
`ζ⁰_r + ζ⁰_l = ζ⁰_t + ζ⁰_b` identically (equivalently `z_r z_l = z_t z_b`). This is the structural
reason the collapse is simultaneous: the four are not independent. -/

theorem octahedral_constraint (ε β₁ β₂ β₁' β₂' μ₁ μ₂ : R) :
    zeta0_r ε β₁ β₂ β₁' β₂' μ₁ μ₂ + zeta0_l ε β₁ β₂ β₁' β₂' μ₁ μ₂
      = zeta0_t ε β₁ β₂ β₁' β₂' μ₁ μ₂ + zeta0_b ε β₁ β₂ β₁' β₂' μ₁ μ₂ := by
  dsimp [zeta0_r, zeta0_l, zeta0_t, zeta0_b]
  ring

/-- Under the octahedral edge-gluing relation `r + l = t + b`, the linear sum
`e1 r t l b` equals `2 * (r + l)` and `(e1 r t l b) ^ 2 - 2 * e2 r t l b` equals
the sum of squares `r ^ 2 + t ^ 2 + l ^ 2 + b ^ 2`. -/
theorem e1_glued_and_quad_sum_sq (r t l b : R) (hglue : r + l = t + b) :
    e1 r t l b = 2 * (r + l) ∧
      (e1 r t l b) ^ 2 - 2 * e2 r t l b = r ^ 2 + t ^ 2 + l ^ 2 + b ^ 2 := by
  dsimp [e1, e2]
  constructor
  · linear_combination hglue
  · ring

end QOU.MassTheory.PinchedOctahedron
