import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic

/-!
# The algebraic Gauss–Manin connection of a Weierstrass family (epic `08a2`, milestone M2)

Let `R` be a commutative ring carrying a derivation `∂` (only its values on the two coefficients
are used, so they enter as plain elements `d₂ = ∂g₂`, `d₃ = ∂g₃`). Take the family

  `E : y² = f(x)`,  `f = 4x³ − g₂x − g₃`,  `Δ = g₂³ − 27g₃²`.

A differential `Q(x)·dx/y³` is *cohomologous* to `a·ω + b·η`, where `ω = dx/y` and `η = x·dx/y`,
when the difference is exact, i.e. equal to `d(P(x)/y) = (P′f − ½Pf′)·dx/y³` for a polynomial `P`.
Since `ω = f·dx/y³` and `η = x f·dx/y³`, after doubling to avoid `½` that reads

  `2Q = 2(a + bx)·f + 2P′f − Pf′`   (`Cohom f (2Q) a b`).

`∂` acts on coefficients and fixes `x`. Since `∂y = ∂f/(2y)`,

  `∂ω = −½ ∂f·dx/y³`,  `∂η = −½ x ∂f·dx/y³`.

**Proved here, sorry-free, over any commutative ring.** With `N₁ = d₂g₂² − 18d₃g₃` and
`N₂ = 3d₂g₃ − 2d₃g₂`:

* `gm_omega`: `4Δ·∂ω ≡ −N₁·ω − 6N₂·η`;
* `gm_eta`: `8Δ·∂η ≡ g₂N₂·ω + 2N₁·η`.

So over `R[Δ⁻¹, ½]` the connection matrix in the basis `(ω, η)` is

  `∇ = (1/(4Δ)) · [[−N₁, −6N₂], [½g₂N₂, N₁]]`,

and `gm_trace_zero` records that its trace vanishes. That is what it must be, since `∇` preserves
the cup product `⟨ω, η⟩`, which is a constant.

Every identity is a polynomial identity, checked by `ring`. Nothing here uses `ℝ`, `ℂ`, `π`
or a period. **What this is not:** it does not prove that `ω, η` form a basis of `H¹_dR` (the
standard fact that the classes are independent and span), and it says nothing about the
categorical side. Applying it to the Tate curve with `∂ = q d/dq` needs the Ramanujan system
(milestone M2b).

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure (R2 / Φ, epic 08a2)
-/

set_option autoImplicit false

namespace QOU.GaussManin
namespace WeierstrassConnection

open Polynomial

variable {R : Type*} [CommRing R]

/-- `f = 4x³ − g₂x − g₃`. -/
noncomputable def weier (g₂ g₃ : R) : R[X] := 4 * X ^ 3 - C g₂ * X - C g₃

/-- `∂f = −d₂x − d₃`, the derivation applied to the coefficients of `f`. -/
noncomputable def dWeier (d₂ d₃ : R) : R[X] := -(C d₂ * X) - C d₃

/-- The discriminant `Δ = g₂³ − 27g₃²`. -/
def disc (g₂ g₃ : R) : R := g₂ ^ 3 - 27 * g₃ ^ 2

/-- `N₁ = d₂g₂² − 18d₃g₃`. -/
def N₁ (g₂ g₃ d₂ d₃ : R) : R := d₂ * g₂ ^ 2 - 18 * d₃ * g₃

/-- `N₂ = 3d₂g₃ − 2d₃g₂`. -/
def N₂ (g₂ g₃ d₂ d₃ : R) : R := 3 * d₂ * g₃ - 2 * d₃ * g₂

/-- `Q₂·dx/(2y³)` is cohomologous to `a·ω + b·η`: the difference is `d(P/y)`. -/
def Cohom (f Q₂ : R[X]) (a b : R) : Prop :=
  ∃ P : R[X], Q₂ = 2 * (C a + C b * X) * f + 2 * derivative P * f - P * derivative f

theorem derivative_weier (g₂ g₃ : R) : derivative (weier g₂ g₃) = 12 * X ^ 2 - C g₂ := by
  unfold weier
  simp only [derivative_sub, derivative_mul, derivative_X_pow, derivative_C, derivative_X,
    derivative_ofNat]
  simp only [Nat.cast_ofNat, map_ofNat, zero_mul, zero_add, mul_one, sub_zero]
  ring

/-- **Gauss–Manin on `ω`.** `4Δ·∂ω ≡ −N₁·ω − 6N₂·η`. -/
theorem gm_omega (g₂ g₃ d₂ d₃ : R) :
    Cohom (weier g₂ g₃) (-(C (4 * disc g₂ g₃)) * dWeier d₂ d₃)
      (-N₁ g₂ g₃ d₂ d₃) (-6 * N₂ g₂ g₃ d₂ d₃) := by
  refine ⟨C (-2 * g₂ * N₂ g₂ g₃ d₂ d₃) + C (-2 * N₁ g₂ g₃ d₂ d₃) * X
    + C (12 * N₂ g₂ g₃ d₂ d₃) * X ^ 2, ?_⟩
  rw [derivative_weier]
  simp only [derivative_add, derivative_C, derivative_mul, derivative_X, derivative_X_pow,
    zero_add, zero_mul, mul_one, Nat.cast_ofNat, map_ofNat]
  simp only [weier, dWeier, disc, N₁, N₂, map_mul, map_sub, map_neg, map_pow, map_ofNat]
  ring

/-- **Gauss–Manin on `η`.** `8Δ·∂η ≡ g₂N₂·ω + 2N₁·η`. -/
theorem gm_eta (g₂ g₃ d₂ d₃ : R) :
    Cohom (weier g₂ g₃) (-(C (8 * disc g₂ g₃)) * X * dWeier d₂ d₃)
      (g₂ * N₂ g₂ g₃ d₂ d₃) (2 * N₁ g₂ g₃ d₂ d₃) := by
  refine ⟨C (6 * g₃ * N₂ g₂ g₃ d₂ d₃) + C (2 * g₂ * N₂ g₂ g₃ d₂ d₃) * X
    + C (-4 * N₁ g₂ g₃ d₂ d₃) * X ^ 2, ?_⟩
  rw [derivative_weier]
  simp only [derivative_add, derivative_C, derivative_mul, derivative_X, derivative_X_pow,
    zero_add, zero_mul, mul_one, Nat.cast_ofNat, map_ofNat]
  simp only [weier, dWeier, disc, N₁, N₂, map_mul, map_sub, map_neg, map_pow, map_ofNat]
  ring

/-- The connection matrix, scaled by `8Δ` so that its entries are in `R`:
rows are `∂ω`, `∂η` in the basis `(ω, η)`. -/
def gmMatrix (g₂ g₃ d₂ d₃ : R) : Matrix (Fin 2) (Fin 2) R :=
  !![-2 * N₁ g₂ g₃ d₂ d₃, -12 * N₂ g₂ g₃ d₂ d₃; g₂ * N₂ g₂ g₃ d₂ d₃, 2 * N₁ g₂ g₃ d₂ d₃]

/-- `∇` preserves the cup product, so its trace is zero. -/
theorem gm_trace_zero (g₂ g₃ d₂ d₃ : R) : (gmMatrix g₂ g₃ d₂ d₃).trace = 0 := by
  simp [gmMatrix, Matrix.trace_fin_two]

end WeierstrassConnection
end QOU.GaussManin
