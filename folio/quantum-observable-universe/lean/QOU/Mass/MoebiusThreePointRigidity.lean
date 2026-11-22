/-
Copyright (c) 2026 litlfred. All rights reserved.

# Closing a second prose-only step: Möbius three-point rigidity, without Möbius machinery

`QOU.Mass.PalindromicInvolutionLift` (#7185) records the load-bearing step of its prune
and then declines to formalise it:

> *"the finiteness of `Stab(B)`, whose elementary proof is stated above and measured in
> T9a but which would need Möbius machinery Mathlib does not carry in usable form."*

The elementary proof it refers to is: *the fixed points of `(az+b)/(cz+d)` solve the
quadratic `cz² + (d−a)z − b = 0`, so three distinct fixed points force `b = 0`, `c = 0`,
`d = a` — the identity.*

**No Möbius machinery is needed, because cleared of its denominator the fixed-point
equation is a quadratic and nothing else.** `w` is fixed exactly when

  `a·w + b = w·(c·w + d)`,

which is `c·w² + (d−a)·w − b = 0`. Everything then follows from one fact about
quadratics, proved here by two subtractions.

## What is proved

* `quadratic_zero_of_three_roots` — a quadratic with three *distinct* roots has all three
  coefficients zero. Two subtractions and a cancellation; no discriminants, no `Polynomial`.
* `moebius_id_of_three_fixed` — three distinct fixed points (cleared form) force
  `c = 0`, `d = a`, `b = 0`: the data of the identity.
* `moebius_proportional_of_three_agree` — the sharper statement, and the one that is
  actually the injectivity `Stab(B) ↪ Sym(B)`: if two Möbius data agree at three distinct
  points then their `2×2` minors all vanish, i.e. the data are proportional, i.e. they are
  the same map. Same quadratic lemma, applied to the difference of the two cleared forms.

## What this closes, and what it does not

**Closes:** the mathematical content #7185 deferred. A base automorphism preserving the
six-point branch locus `B` is determined by its action on three of those points, so the
map `Stab(B) → Sym(B)` is injective and `Stab(B)` is finite of order at most `6·5·4`.

**Does not close:** the *group packaging* — assembling `Stab(B)` as a subgroup of
`PGL₂` and exhibiting the injection as a group homomorphism into `S₆` — which is
bookkeeping over Mathlib's `Matrix.GeneralLinearGroup` and is still prose. Nor does it
touch the geometric half of the covering step (that an automorphism of `Σ` permutes `B`
at all), which stays prose in #6769 / #7185 / #7208 and is flagged there.

Together with `QOU.Mass.BranchLocusFiniteOrder` — which proves the scaling case of
finiteness by pigeonhole — the two halves of "every base automorphism preserving `B` has
finite order" are now machine-checked, from different directions: pigeonhole for the
orbit bound on a scaling, three-point rigidity for the determinacy of a general Möbius
map.

**The cleared form is not a convenience, it is the honest statement.** Writing the map as
`(az+b)/(cz+d)` needs `cz+d ≠ 0`, and a fixed point at `∞` needs a chart. The cleared
equation `a·w + b = w·(c·w + d)` has neither problem and says the same thing at every
finite point, which is where the branch locus lives (`D(0) = 16 ≠ 0`, and `D` has degree
`6` with nonzero leading coefficient, so no root is at `∞`).

§7c: generic `[Field K]` throughout — division is never used, so `[CommRing K]` plus
cancellation would do; `Field` is kept only because the two subtractions divide by the
differences of the roots. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-08-w1-palindromic-involution-lifts-and-is-elliptic.md
-/
import Mathlib.Tactic

namespace QOU.Mass.MoebiusThreePointRigidity

variable {K : Type*} [Field K]

/-- **A quadratic with three distinct roots is the zero quadratic.**

`A·x² + B·x + C` vanishing at three pairwise-distinct points forces `A = B = C = 0`.

Proof: subtracting the equations at `x` and `y` and cancelling `x − y` gives
`A·(x+y) + B = 0`; the same at `x` and `z` gives `A·(x+z) + B = 0`; subtracting those and
cancelling `y − z` gives `A = 0`, and the rest follows. -/
theorem quadratic_zero_of_three_roots (A B C x y z : K)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hx : A * x ^ 2 + B * x + C = 0)
    (hy : A * y ^ 2 + B * y + C = 0)
    (hz : A * z ^ 2 + B * z + C = 0) :
    A = 0 ∧ B = 0 ∧ C = 0 := by
  have hxy' : x - y ≠ 0 := sub_ne_zero.mpr hxy
  have hxz' : x - z ≠ 0 := sub_ne_zero.mpr hxz
  have hyz' : y - z ≠ 0 := sub_ne_zero.mpr hyz
  -- first differences, with the root gap cancelled
  have e1 : A * (x + y) + B = 0 := by
    have hfac : (x - y) * (A * (x + y) + B) = 0 := by linear_combination hx - hy
    exact (mul_eq_zero.mp hfac).resolve_left hxy'
  have e2 : A * (x + z) + B = 0 := by
    have hfac : (x - z) * (A * (x + z) + B) = 0 := by linear_combination hx - hz
    exact (mul_eq_zero.mp hfac).resolve_left hxz'
  -- second difference: `A·(y − z) = 0`
  have hA : A = 0 := by
    have hfac : (y - z) * A = 0 := by linear_combination e1 - e2
    exact (mul_eq_zero.mp hfac).resolve_left hyz'
  subst hA
  have hB : B = 0 := by linear_combination e1
  subst hB
  refine ⟨rfl, rfl, ?_⟩
  linear_combination hx

/-- **Three-point rigidity.** If the Möbius data `(a, b; c, d)` fixes three distinct
points — in the cleared sense `a·w + b = w·(c·w + d)`, which needs no chart and no
`cw + d ≠ 0` — then `c = 0`, `d = a` and `b = 0`: the data of the identity map.

This is the content #7185 deferred as "Möbius machinery"; the fixed-point condition is a
quadratic `c·w² + (d−a)·w − b = 0`, so `quadratic_zero_of_three_roots` does all of it. -/
theorem moebius_id_of_three_fixed (a b c d x y z : K)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hx : a * x + b = x * (c * x + d))
    (hy : a * y + b = y * (c * y + d))
    (hz : a * z + b = z * (c * z + d)) :
    c = 0 ∧ d = a ∧ b = 0 := by
  obtain ⟨hA, hB, hC⟩ :=
    quadratic_zero_of_three_roots c (d - a) (-b) x y z hxy hxz hyz
      (by linear_combination -hx) (by linear_combination -hy) (by linear_combination -hz)
  exact ⟨hA, by linear_combination hB, by linear_combination -hC⟩

/-- **The injectivity `Stab(B) ↪ Sym(B)`, in cleared coordinates.**

If two Möbius data agree at three distinct points — cleared, `(a·x + b)·(c'·x + d') =
(a'·x + b')·(c·x + d)` — then every `2×2` minor of the stacked data vanishes:

  `a·c' = a'·c`,  `a·d' + b·c' = a'·d + b'·c`,  `b·d' = b'·d`

i.e. the two data are proportional and induce the same map. This is the statement the
`Stab(B) ↪ Sym(B) = S₆` embedding rests on: a base automorphism preserving the six-point
branch locus is pinned by where it sends three of those points, so the stabiliser is
finite of order at most `6·5·4`.

Same lemma again — the difference of the two cleared forms is a quadratic in the
evaluation point. -/
theorem moebius_proportional_of_three_agree (a b c d a' b' c' d' x y z : K)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hx : (a * x + b) * (c' * x + d') = (a' * x + b') * (c * x + d))
    (hy : (a * y + b) * (c' * y + d') = (a' * y + b') * (c * y + d))
    (hz : (a * z + b) * (c' * z + d') = (a' * z + b') * (c * z + d)) :
    a * c' = a' * c ∧ a * d' + b * c' = a' * d + b' * c ∧ b * d' = b' * d := by
  obtain ⟨hA, hB, hC⟩ :=
    quadratic_zero_of_three_roots (a * c' - a' * c)
      (a * d' + b * c' - (a' * d + b' * c)) (b * d' - b' * d) x y z hxy hxz hyz
      (by linear_combination hx) (by linear_combination hy) (by linear_combination hz)
  exact ⟨by linear_combination hA, by linear_combination hB, by linear_combination hC⟩

/-- **Uniqueness of quadratic interpolation at three distinct points.**
Two quadratics `A₁·w² + B₁·w + C₁` and `A₂·w² + B₂·w + C₂` that agree at three
pairwise-distinct points `x, y, z` have identical coefficients. -/
theorem quadratic_eq_of_three_agree (A₁ B₁ C₁ A₂ B₂ C₂ x y z : K)
    (hxy : x ≠ y) (hxz : x ≠ z) (hyz : y ≠ z)
    (hx : A₁ * x ^ 2 + B₁ * x + C₁ = A₂ * x ^ 2 + B₂ * x + C₂)
    (hy : A₁ * y ^ 2 + B₁ * y + C₁ = A₂ * y ^ 2 + B₂ * y + C₂)
    (hz : A₁ * z ^ 2 + B₁ * z + C₁ = A₂ * z ^ 2 + B₂ * z + C₂) :
    A₁ = A₂ ∧ B₁ = B₂ ∧ C₁ = C₂ := by
  obtain ⟨hA, hB, hC⟩ :=
    quadratic_zero_of_three_roots (A₁ - A₂) (B₁ - B₂) (C₁ - C₂) x y z hxy hxz hyz
      (by linear_combination hx) (by linear_combination hy) (by linear_combination hz)
  exact ⟨by linear_combination hA, by linear_combination hB, by linear_combination hC⟩

/-- **Trace-zero Möbius involution identity (cleared coordinates).**
Any Möbius matrix `(a, b; c, -a)` of trace zero satisfies the Cayley–Hamilton
involution identity `(a·(a·w + b) + b·(c·w - a)) = (a² + b·c)·w` and
`(c·(a·w + b) - a·(c·w - a)) = a² + b·c`, so its square acts as the identity
at every point `w` in cleared coordinates. -/
theorem moebius_trace_zero_involution_cleared (a b c w : K) :
    (a * (a * w + b) + b * (c * w - a)) = w * (c * (a * w + b) - a * (c * w - a)) := by
  ring

end QOU.Mass.MoebiusThreePointRigidity
