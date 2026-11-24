/-
The interface kernel: `T^k = f k • T + f (k-1) • 1` in any ring where
`T^2 = A*T + 1`, with `f` the alternating recursion.

This is the algebraic half of the derivation measured in
`computations/interface_kernel_derivation_probe.py`. Paired with
`QOU.Knot.JetGradePromotion` -- a generator meeting no existing inversion
raises every filtration grade by exactly one -- it fixes the single-interface
kernel of the generating function `G_E(x) = Σ_g (mass at grade g) x^g` as

    R_k(q, x) = f k * x + f (k-1)

with no fitted constant.

What is proved here is the RING IDENTITY. Nothing about knots, binding, or
generating functions is asserted -- the file is `Semiring`-generic and does
not mention `q`. The Hecke relation enters only as the hypothesis
`hT : T^2 = A*T + 1`, so any `A` in any commutative semiring works, and the
specialisation `A = q - q⁻¹` happens downstream where the archimedean wall
allows it (§7c: no gratuitous `ℝ`).

`splitCoeff` is named for what it measures. In the reduction, the
length-decreasing branch is the only one that splits a term across two
grades, and `f (k-1)` is exactly the weight it carries: `promoCoeff = f k`
rides at grade +1, `splitCoeff = f (k-1)` stays behind. Bounding that
contribution was the open item; this computes it instead.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.Knot.InterfaceKernel

variable {R : Type*} [CommSemiring R]

/-- The alternating recursion `f 0 = 0`, `f 1 = 1`, `f (k+2) = A * f (k+1) + f k`.

Over `ℤ[q,q⁻¹]` with `A = q - q⁻¹` its characteristic roots are `q` and `-q⁻¹`
-- the two Hecke eigenvalues -- because `A^2 + 4 = (q + q⁻¹)^2`. That fact is
archimedean-flavoured and is deliberately NOT stated here; see `discriminant`
below for the ring-generic version of it. -/
def f (A : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | (k + 2) => A * f A (k + 1) + f A k

@[simp] theorem f_zero (A : R) : f A 0 = 0 := rfl
@[simp] theorem f_one (A : R) : f A 1 = 1 := rfl
@[simp] theorem f_two (A : R) : f A 2 = A := by simp [f]

theorem f_succ_succ (A : R) (k : ℕ) : f A (k + 2) = A * f A (k + 1) + f A k := rfl

/-- The coefficient that RIDES to grade +1 under one more crossing. -/
abbrev promoCoeff (A : R) (k : ℕ) : R := f A k

/-- The coefficient LEFT BEHIND at the original grade -- the split weight.

This is the quantity the arc set out to bound. It is not bounded here, it is
identified: it is `f (k-1)`, exactly. -/
abbrev splitCoeff (A : R) (k : ℕ) : R := f A (k - 1)

/-- **The interface identity.** In any commutative semiring, if `T` satisfies
the Hecke relation `T^2 = A*T + 1`, then every power of `T` is a linear
combination of `T` and `1` with the recursion's coefficients:

    `T^(k+1) = f (k+1) * T + f k`

Induction on `k` in two-step form: the `k+2` case rewrites `T^(k+2)` as
`T^(k+1) * T`, applies the hypothesis twice, and closes by `ring` against the
defining recursion. -/
theorem pow_eq (A T : R) (hT : T ^ 2 = A * T + 1) :
    ∀ k : ℕ, T ^ (k + 1) = f A (k + 1) * T + f A k
  | 0 => by simp
  | 1 => by
      have : T ^ 2 = A * T + 1 := hT
      simpa [f] using this
  | (k + 2) => by
      have ih := pow_eq A T hT (k + 1)
      have hpow : T ^ (k + 2 + 1) = T ^ (k + 1 + 1) * T := by ring
      rw [hpow, ih]
      have hsq : (f A (k + 2) * T + f A (k + 1)) * T
               = f A (k + 2) * T ^ 2 + f A (k + 1) * T := by ring
      rw [hsq, hT, f_succ_succ A (k + 1), f_succ_succ A k]
      ring

/-! ### The closed form

`pow_eq` above is `Semiring`-generic and holds for every `k`. The closed form
needs inverses, so it is stated over a `Field` with `q ≠ 0` -- an §7c-legitimate
specialisation (the base-ring table lists `Field`/`GroupWithZero` for exactly
this), and still not `ℝ`: no ordering, no `Real.sqrt`, no archimedean anything.

Stated multiplied through by `q + q⁻¹` so no division appears in the statement
and no `q + q⁻¹ ≠ 0` hypothesis is needed. Over `ℤ[q,q⁻¹]` this is the
alternating (balanced) q-integer, and the two `q`-powers appearing are the
Hecke eigenvalues `q` and `-q⁻¹`. -/

variable {K : Type*} [Field K]

/-- **The closed form, for every `k`.** With `A = q - q⁻¹`,

    `f A k * (q + q⁻¹) = q^k - (-1)^k * (q⁻¹)^k`.

The two terms are the `k`-th powers of the Hecke eigenvalues `q` and `-q⁻¹`,
which are exactly the roots of the recursion's characteristic polynomial
`t^2 - A t - 1` -- `A^2 + 4 = (q + q⁻¹)^2` is what makes them come out
rational in `q` rather than involving a genuine square root. -/
theorem f_closed_form (q : K) (hq : q ≠ 0) :
    ∀ k : ℕ, f (q - q⁻¹) k * (q + q⁻¹) = q ^ k - (-1) ^ k * (q⁻¹) ^ k
  | 0 => by simp
  | 1 => by simp [f]
  | (k + 2) => by
      have ih1 := f_closed_form q hq (k + 1)
      have ih0 := f_closed_form q hq k
      have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
      -- the two cancellations that make the alternating sum telescope
      have h1 : q * q⁻¹ ^ (k + 1) = q⁻¹ ^ k := by
        rw [pow_succ, ← mul_assoc, mul_comm q (q⁻¹ ^ k), mul_assoc, hqq, mul_one]
      have h2 : q⁻¹ * q ^ (k + 1) = q ^ k := by
        rw [pow_succ, ← mul_assoc, mul_comm q⁻¹ (q ^ k), mul_assoc, mul_comm q⁻¹ q,
            hqq, mul_one]
      rw [f_succ_succ, add_mul, mul_assoc, ih1, ih0]
      have expand : (q - q⁻¹) * (q ^ (k + 1) - (-1) ^ (k + 1) * q⁻¹ ^ (k + 1))
                  + (q ^ k - (-1) ^ k * q⁻¹ ^ k)
          = q * q ^ (k + 1) - (-1) ^ k * (q⁻¹ * q⁻¹ ^ (k + 1))
            + ((-1) ^ k * (q * q⁻¹ ^ (k + 1)) - q⁻¹ * q ^ (k + 1))
            + (q ^ k - (-1) ^ k * q⁻¹ ^ k) := by
        rw [pow_succ ((-1 : K)) k]; ring
      have hneg : ((-1 : K)) ^ (k + 2) = (-1) ^ k := by
        rw [pow_succ, pow_succ]; ring
      rw [expand, h1, h2, hneg]
      ring

end QOU.Knot.InterfaceKernel
