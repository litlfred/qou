/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import QOU.MassTheory.EmTwoLoopMeasureConnected

/-!
# A two-loop period that is `ζ(3)`: the flat sunset on a torus quotient of Bring (bean `qou-l4t2`)

Behind the transcendental boundary. Nothing here is computed from data, and the analytic
theorem is carried as a **hypothesis field**, not proved.

## The cited theorem

For a flat torus `ℂ/(ℤ + τℤ)` with scalar Green function
`G(z|τ) = (Im τ/π) Σ'_{(m,n)} e^{2πi(…)}/|mτ + n|²`, the one-loop graph with three propagators
is the Eisenstein series `E₃(τ)` and the two-loop sunset (two vertices joined by three
propagators) is the modular graph function `C_{1,1,1}(τ)`. Then, for every `τ` in the upper
half-plane,

`C_{1,1,1}(τ) = E₃(τ) + ζ(3)`.

Conjectured by D'Hoker–Green–Vanhove; proved by Zagier (in D'Hoker–Green–Vanhove,
*On the modular structure of the genus-one Type II superstring low energy expansion*,
JHEP 08 (2015) 041, arXiv:1502.06698): both sides satisfy `Δ f = 6 E₃` and the difference
is a bounded harmonic function, hence constant; the constant is read off the Laurent
polynomial at the cusp.

## What this module proves (given that field)

1. `sunset_connected_const`: `C_{1,1,1}(τ) − E₃(τ)` does not depend on `τ`, and equals `ζ(3)`.
   So the period is the same for every torus, in particular for every member of the isogeny
   class of the factor `E` of `Jac(Bring) ~ E⁴`, whichever representative is taken.
2. `cover_scaled_period`: pulling back along a degree-`d` map from Bring to a torus quotient
   with the un-normalized pulled-back measure multiplies each two-vertex graph by `d²`; the
   period becomes `d² ζ(3)`, a rational multiple of `ζ(3)`.
3. `genus_one_quotient_degrees_differ`: the torus quotients of Bring have orders
   `2, 4, 4, 6, 6, 12` (`BringSymmetryQuotientGenus.quotient_genus_table`), so the rational
   factor depends on the quotient. The corpus has no rule that picks one. With the
   probability-normalized pulled-back measure the factor is `1` for all of them.
4. `bring_sunset_loop_measure`: packaged as a `LoopMeasure`, the connected part of the
   resulting two-loop measure is `r ζ(3)` for the rational normalization `r` chosen.

Not established here: that the α_EM two-loop slot **is** this sunset (that is the open
modelling identification), the relative normalization against the one-loop `1/(8π)`, and
any statement about the hyperbolic metric of Bring itself, whose sunset is a Maass-spectral
sum with no known closed form.
-/

set_option autoImplicit false

namespace QOU.Transcendental.MassTheory
namespace FlatSunsetConnectedPeriod

open QOU.MassTheory.EmTwoLoopMeasureConnected

/-- Genus-one modular graph data over a parameter type `T` (the upper half-plane), carrying
the Zagier / D'Hoker–Green–Vanhove sunset identity as a hypothesis. -/
structure FlatTorusSunset (T : Type*) where
  /-- The one-loop three-propagator graph, `E₃`. -/
  E3 : T → ℝ
  /-- The two-loop sunset, `C_{1,1,1}`. -/
  C111 : T → ℝ
  /-- The value `ζ(3)`, as an opaque real. -/
  zeta3 : ℝ
  /-- Cited theorem (not proved here): `C_{1,1,1} = E₃ + ζ(3)` for every modulus. -/
  sunset : ∀ τ, C111 τ = E3 τ + zeta3

variable {T : Type*}

/-- The connected sunset period at modulus `τ`. -/
def connectedSunset (S : FlatTorusSunset T) (τ : T) : ℝ := S.C111 τ - S.E3 τ

theorem sunset_connected_eq (S : FlatTorusSunset T) (τ : T) :
    connectedSunset S τ = S.zeta3 := by
  unfold connectedSunset; rw [S.sunset τ]; ring

/-- **Modulus independence.** -/
theorem sunset_connected_const (S : FlatTorusSunset T) (τ τ' : T) :
    connectedSunset S τ = connectedSunset S τ' := by
  rw [sunset_connected_eq, sunset_connected_eq]

/-- **Cover scaling.** If the pulled-back graphs on a degree-`d` cover are `d²` times the
quotient graphs (two vertices, un-normalized pulled-back measure), the connected period on
the cover is `d² ζ(3)`. -/
theorem cover_scaled_period (S : FlatTorusSunset T) (d : ℕ) (τ : T)
    (C' E' : ℝ) (hC : C' = (d : ℝ) ^ 2 * S.C111 τ) (hE : E' = (d : ℝ) ^ 2 * S.E3 τ) :
    C' - E' = (d : ℝ) ^ 2 * S.zeta3 := by
  rw [hC, hE, S.sunset τ]; ring

/-- Orders of the subgroups `H ≤ S₅` with `B/H` a torus (one per conjugacy class):
`⟨(01)⟩, V₄, C₄, C₆, S₃, A₄`. -/
def genusOneQuotientOrders : List ℕ := [2, 4, 4, 6, 6, 12]

/-- The `d²` factors are not all equal, so the un-normalized period depends on the quotient. -/
theorem genus_one_quotient_degrees_differ :
    ∃ a ∈ genusOneQuotientOrders, ∃ b ∈ genusOneQuotientOrders, a ^ 2 ≠ b ^ 2 :=
  ⟨2, by decide, 12, by decide, by decide⟩

/-- **Packaged.** A loop measure whose two-loop weight adds the normalized connected sunset
`r ζ(3)` to the product weight has connected part exactly `r ζ(3)`. -/
def bringSunsetLoopMeasure (S : FlatTorusSunset T) (μ₁ r : ℝ) : LoopMeasure ℝ :=
  ⟨μ₁, μ₁ ^ 2 + r * S.zeta3⟩

theorem bring_sunset_loop_measure (S : FlatTorusSunset T) (μ₁ r : ℝ) :
    connected (bringSunsetLoopMeasure S μ₁ r) = r * S.zeta3 := by
  unfold connected bringSunsetLoopMeasure; ring

end FlatSunsetConnectedPeriod
end QOU.Transcendental.MassTheory
