import Mathlib.RingTheory.HahnSeries.Multiplication
import QOU.AppendixSurreals.Asymptotics

/-!
# QOU.AppendixSurreals.HahnOmegaOrder — a Mathlib model for `OmegaOrder`

`OmegaOrder` (`Asymptotics.lean`) axiomatises the ω-adic leading-exponent
valuation. Until now it had **no instance anywhere in this tree**, so every
`[OmegaOrder]`-conditional result was untested for satisfiability. A class that
asserts a great deal but has never been shown consistent is not much better than
one that asserts nothing — the defect bean `qou-ffwk` is about, one level up.

This file supplies the model: **Hahn series** `HahnSeries Γ R` over a domain,
with `Ow := HahnSeries.orderTop`. Bean `qou-x20w`.

## What had to be built

Mathlib exposes `orderTop` and proves multiplicativity only as an **inequality**,
`orderTop_add_le_mul : x.orderTop + y.orderTop ≤ (x * y).orderTop`. `Ow_mul` is
an *equality*, so `orderTop_mul` below derives it from `HahnSeries.order_mul`
(which is the equality, on the un-topped `order`, and needs both factors
non-zero and `R` to have no zero divisors) together with the two zero cases.
The zero cases are where the domain hypothesis earns its place a second time:
`x * y = 0` has to follow from `x = 0 ∨ y = 0`, or the `⊤` bookkeeping does not
match up.

## What this does and does not settle

It settles that `OmegaOrder`'s four axioms are **jointly consistent**, and it
does so over a carrier with genuine non-archimedean content rather than a
degenerate one — `HahnSeries ℤ ℝ` has elements of every integer order.

It does **not** give a surreal model, and in particular it does not make
`SpectralNormalForm` witnessed. That class needs `IsInfinitesimal` and
`IsFinite`, hence `[SurrealField K]`, and `SurrealField` requires an element
exceeding every natural — so its model has to be a specific non-archimedean
*ordered field* with a birthday function, which is a separate construction. See
`Asymptotics.lean`'s history note for what remains.

## Base ring (§7c)

Fully generic, with **no real-field type anywhere**: `Γ` is any linearly
ordered cancellative additive monoid, `R` any commutative domain, and the
scalars `S` any commutative ring acting on `R`. Nothing here is ordered against
a numerical substrate value and no archimedean construct is used. Surreal
callers instantiate `S` at the reals; this module does not have to know that,
which is also what keeps it clear of the §7c mixed-regime rule.
-/

namespace QOU.AppendixSurreals

open HahnSeries

universe u v s

variable {Γ : Type v} {R : Type u} {S : Type s}

section OrderTopMul

variable [AddCommMonoid Γ] [LinearOrder Γ] [IsOrderedCancelAddMonoid Γ]
variable [CommRing R] [IsDomain R]

/-- **`orderTop` is multiplicative over a domain.**

Mathlib proves only `orderTop_add_le_mul`, the inequality. The equality that
`OmegaOrder.Ow_mul` states follows from `HahnSeries.order_mul` on the non-zero
part, plus the two zero cases — and those need `R` to be a domain a second time,
so that `x * y = 0` forces `x = 0 ∨ y = 0` and the `⊤` bookkeeping matches. -/
theorem orderTop_mul (x y : HahnSeries Γ R) :
    (x * y).orderTop = x.orderTop + y.orderTop := by
  by_cases hx : x = 0
  · simp [hx]
  by_cases hy : y = 0
  · simp [hy]
  have hxy : x * y ≠ 0 := mul_ne_zero hx hy
  rw [← order_eq_orderTop_of_ne_zero hx, ← order_eq_orderTop_of_ne_zero hy,
      ← order_eq_orderTop_of_ne_zero hxy, order_mul hx hy]
  rfl

end OrderTopMul

/-- **Hahn series model for `OmegaOrder`.**

`Ow` is the leading exponent `orderTop`, with `⊤` at zero. The four axioms:

* `Ow_zero` — `orderTop 0 = ⊤` by definition;
* `Ow_mul` — `orderTop_mul` above;
* `Ow_algebraMap_mul` — a scalar with non-zero image is a constant series, whose
  `orderTop` is `0`, so multiplying by it shifts the leading exponent by `0`.
  This is the axiom that was previously phrased with `SurrealField.ofReal`; over
  a general algebra it is `algebraMap`, and the two agree on any `SurrealField`
  instantiated at the reals.

Deliberately **not** a global `instance`: it is a witness that the axioms are
consistent, and registering it would let typeclass resolution silently pick the
Hahn valuation for an unrelated `K`. Callers name it. -/
noncomputable def hahnOmegaOrder
    [AddCommMonoid Γ] [LinearOrder Γ] [IsOrderedCancelAddMonoid Γ]
    [CommRing R] [IsDomain R] [CommRing S] [Algebra S R] :
    OmegaOrder (HahnSeries Γ R) S Γ where
  Ow := HahnSeries.orderTop
  Ow_zero := by simp
  Ow_mul := orderTop_mul
  Ow_algebraMap_mul r x hr := by
    have hC : (algebraMap S (HahnSeries Γ R)) r = C (algebraMap S R r) := rfl
    have hr' : algebraMap S R r ≠ 0 := by
      intro h
      exact hr (by rw [hC, h, map_zero])
    have hzero : ((algebraMap S (HahnSeries Γ R)) r).orderTop = 0 := by
      rw [hC, C_apply, orderTop_single hr']
      rfl
    rw [orderTop_mul, hzero, zero_add]

end QOU.AppendixSurreals
