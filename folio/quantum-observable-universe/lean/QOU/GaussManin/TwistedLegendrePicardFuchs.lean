import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic

/-!
# The twisted Legendre family and its Picard–Fuchs equation (epic `08a2`, germ route G2)

Germ route (owner ruling 2026-11-28 01:55Z). `HeckeBurauCusp` showed that at `q² = −1` the
Hecke fundamental representation of `B₃` is the elliptic monodromy. Away from that point, reduced
Burau is the monodromy of a *twisted* period (Kohno, `library/kohno1987-aif`):

  `I(λ) = ∫ Φ dx`,   `Φ = f^{−α}`,   `f = x(x − 1)(x − λ)`.

At `α = ½` the integrand is `dx/y` on the Legendre curve `y² = x(x−1)(x−λ)`. This file proves the
algebraic half of that statement for every `α`: the twisted Gauss–Manin (Picard–Fuchs) equation.

**The computation.** Treat `Φ` formally, with `∂_x Φ = −α (f′/f) Φ`,
`∂_λ Φ = α/(x − λ) Φ` and `∂²_λ Φ = α(α+1)/(x − λ)² Φ`. A twisted form `gΦ dx` is exact when
`g = d(hΦ)/(Φ dx) = h′ − α h f′/f`. With `u = x − λ`, `N = α x(x−1)` and `h = N/u`, the identity

  `λ(1−λ)·∂²_λΦ + 2α(1−2λ)·∂_λΦ − α(3α−1)·Φ = ∂_x(hΦ)`

becomes, after multiplying by `u²/Φ`, the polynomial identity `picardFuchs_twisted` (proved by
`ring`, over any commutative ring):

  `λ(1−λ)α(α+1) + 2α²(1−2λ)·u − α(3α−1)·u² = N′u − N − α²f′`.

So `I(λ)` satisfies the Gauss hypergeometric equation
`λ(1−λ)I″ + (c − (a+b+1)λ)I′ − abI = 0` with `(a, b, c) = (α, 3α − 1, 2α)`
(`gauss_parameters`). At `α = ½` it is `(½, ½, 1)`, the Legendre Picard–Fuchs equation of the
elliptic family (`legendre_at_half`). All three exponent differences are `±(1 − 2α)`
(`exponent_differences`), so the Schwarz map of the family is a triangle map with three equal
angles `π|1 − 2α|`. At `α = ½` they are all `0`, which gives the ideal triangle of `Γ(2)`.

**Scope.** All of this is algebra: `α` and `λ` are ring elements and `Φ` is a formal symbol.
Proved here: the identity, and the reading of `(a, b, c)`. Not proved here: that `∫ Φ dx` over a
twisted cycle exists and has Burau monodromy at `t = e^{∓2πiα}` (Kohno; analytic, so it belongs
in `QOU/Transcendental/`), and how `α` relates to the Hecke `q` beyond `q² = −1 ↔ α = ½`.
Nothing here gives `GermPeriodShare` an instance.

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure (R2 / Φ, epic 08a2)
-/

set_option autoImplicit false

namespace QOU.GaussManin
namespace TwistedLegendrePicardFuchs

open Polynomial

variable {R : Type*} [CommRing R]

/-- `u = x − λ`. -/
noncomputable def u (lam : R) : R[X] := X - C lam

/-- `f = x(x − 1)(x − λ)`. -/
noncomputable def f (lam : R) : R[X] := X * (X - 1) * u lam

/-- `N = α x(x − 1)`, the numerator of the exact-form primitive `h = N/u`. -/
noncomputable def N (α : R) : R[X] := C α * (X * (X - 1))

/-- **The twisted Picard–Fuchs identity**, multiplied by `u²/Φ`. -/
theorem picardFuchs_twisted (α lam : R) :
    C (lam * (1 - lam) * α * (α + 1)) + C (2 * α ^ 2 * (1 - 2 * lam)) * u lam
      - C (α * (3 * α - 1)) * u lam ^ 2
      = derivative (N α) * u lam - N α - C (α ^ 2) * derivative (f lam) := by
  simp only [N, f, u, derivative_mul, derivative_C, derivative_X,
    derivative_one, zero_mul, zero_add, sub_zero, mul_one, one_mul, map_mul, map_sub,
    map_add, map_pow, map_one, map_ofNat]
  ring

/-- With the Gauss parameters `(a, b, c) = (α, 3α − 1, 2α)`, the `I′` coefficient
`c − (a+b+1)λ` is `2α(1 − 2λ)`. The `I` coefficient `ab = α(3α − 1)` matches by definition. -/
theorem gauss_parameters (α lam : R) :
    (2 * α) - (α + (3 * α - 1) + 1) * lam = 2 * α * (1 - 2 * lam) := by ring

/-- At `α = ½` the parameters are `(½, ½, 1)` and `ab = ¼`: the Legendre equation
`λ(1−λ)I″ + (1 − 2λ)I′ − ¼I = 0`. -/
theorem legendre_at_half {K : Type*} [Field K] [CharZero K] :
    3 * (1 / 2 : K) - 1 = 1 / 2 ∧ 2 * (1 / 2 : K) = 1 ∧ (1 / 2 : K) * (3 * (1 / 2) - 1) = 1 / 4 := by
  refine ⟨by ring, by ring, by ring⟩

/-- The exponent differences `1 − c` (at `0`), `c − a − b` (at `1`) and `b − a` (at `∞`) are
`1 − 2α`, `1 − 2α` and `−(1 − 2α)`. -/
theorem exponent_differences (α : R) :
    2 * α - α - (3 * α - 1) = 1 - 2 * α ∧ (3 * α - 1) - α = -(1 - 2 * α) := by
  refine ⟨by ring, by ring⟩

end TwistedLegendrePicardFuchs
end QOU.GaussManin
