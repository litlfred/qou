import Mathlib.Tactic.LinearCombination

/-!
# Lagrange resolvent — cyclic eigenvalue (offset angle from the C₅ stabilizer)

The **rigorous tier-1** of the torus-knot → q-Bring offset question (bean
`qou-vhv6`): the *angle* of the offset is fixed by the embedding's cyclic
stabilizer root of unity, independently of any (still-open) magnitude closure.

On Bring's surface the base coordinates `x₀,…,x₄` are diagonalized by the
`C₅ ⊂ S₅` cyclic action via the Lagrange-resolvent DFT
`w_k = (1/√5) Σ_j ζ₅^{kj} x_j`. Writing `w := ζ₅^k` (a 5th root of unity, since
`ζ₅⁵ = 1`), the cyclic shift `x_j ↦ x_{j+1}` acts on the (unnormalized) k-th
resolvent by multiplication by `w`:

  `w · (x₁ + w x₂ + w² x₃ + w³ x₄ + w⁴ x₀) = x₀ + w x₁ + w² x₂ + w³ x₃ + w⁴ x₄`.

I.e. the k-th resolvent is an **eigenvector of the cyclic shift with eigenvalue
`ζ₅^{-k}`** (equivalently `ζ₅^k · (shift·w_k) = w_k`). The offset's argument
therefore advances by `arg(ζ₅^{-k}) = -2πk/5` under the C₅ action — the angle is
a stabilizer root of unity, exactly as claimed. (The trefoil colour channel uses
the S₃ cube-root sub-DFT, `w = ζ₃`; the `w⁵ = 1` below specializes to `w³ = 1`
via the same identity with the length-3 resolvent.)

§7c: stated over a generic `CommRing R` with `w` a formal 5th root of unity — no
archimedean input. Derived, not fitted: a one-line `linear_combination` identity
over `w⁵ = 1`.

Bean `qou-vhv6`; companion to `QOU.Mass.ColorCubicDiscriminantPositive` (which
establishes that the 6 saddle points are strictly complex, so the offset angle
is nonzero and this eigenvalue phase is the object that carries it).
-/

namespace QOU.Mass

/-- **Cyclic eigenvalue of the Lagrange resolvent.** For `w` a formal 5th root of
unity (`w⁵ = 1`), the cyclic shift `x_j ↦ x_{j+1}` multiplies the k-th resolvent
`w_k = x₀ + w x₁ + w² x₂ + w³ x₃ + w⁴ x₄` (with `w = ζ₅^k`) by `w`:
`w · (shift · w_k) = w_k`. Hence the resolvent is an eigenvector of the shift
with eigenvalue `w⁻¹ = ζ₅^{-k}` — the offset angle is the stabilizer root of
unity. -/
theorem lagrangeResolvent_cyclic_eigenvalue {R : Type*} [CommRing R]
    (w x0 x1 x2 x3 x4 : R) (hw : w ^ 5 = 1) :
    w * (x1 + w * x2 + w ^ 2 * x3 + w ^ 3 * x4 + w ^ 4 * x0)
      = x0 + w * x1 + w ^ 2 * x2 + w ^ 3 * x3 + w ^ 4 * x4 := by
  linear_combination x0 * hw

/-- **Cube-root (colour-channel) specialization.** For `w³ = 1` the same identity
holds for the length-3 resolvent — the trefoil colour channel's S₃ sub-DFT,
whose stabilizer phase is `ζ₃ = e^{2πi/3}`. -/
theorem colourResolvent_cyclic_eigenvalue {R : Type*} [CommRing R]
    (w x0 x1 x2 : R) (hw : w ^ 3 = 1) :
    w * (x1 + w * x2 + w ^ 2 * x0) = x0 + w * x1 + w ^ 2 * x2 := by
  linear_combination x0 * hw

/-- **Vanishing difference form of `colourResolvent_cyclic_eigenvalue` (`qou-3ral`).**
For `w ^ 3 = 1` in a commutative ring `R`,
`w * (x1 + w * x2 + w ^ 2 * x0) - (x0 + w * x1 + w ^ 2 * x2) = 0`. -/
theorem colourResolvent_cyclic_eigenvalue_sub_eq_zero {R : Type*} [CommRing R]
    (w x0 x1 x2 : R) (hw : w ^ 3 = 1) :
    w * (x1 + w * x2 + w ^ 2 * x0) - (x0 + w * x1 + w ^ 2 * x2) = 0 :=
  sub_eq_zero.mpr (colourResolvent_cyclic_eigenvalue w x0 x1 x2 hw)

end QOU.Mass
