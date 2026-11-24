import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.QBeta.SixOneShapeDiscriminant — the four-shape discriminant of 6₁ (Stevedore)

The 6-crossing continuation of `CubicSaddleDiscriminant` (5₂, three saddles → −23).
The GGM state-integral saddle curve is worked explicitly only for 4₁ and 5₂
(`library/arxiv-2012.00062v3/2012.00062v3.pdf` §§5–6); the 6-crossing knots appear there only as
q-series. So the faithful 6-crossing datum is taken from the **hyperbolic
geometry** instead of GGM: the shape parameter `z` of the Stevedore knot 6₁
(4-tetrahedron triangulation) generates a degree-4 field with minimal polynomial

`x⁴ − 3x³ + 6x² − 5x + 2`   (SnapPy shape, PARI `algdep`-verified: `|p(z)| < 10⁻⁶⁰`
at 100-digit precision),

whose four roots are the Galois conjugates of `z` — the four geometric shapes (the
6₁ analogue of the three 5₂ saddles). Their **discriminant is `257`** (prime), the
6₁ arithmetic fingerprint (the analogue of `−23` for 5₂). This file proves, over a
generic commutative ring:

* `disc_eq_root_diff_sq_quartic` — the quartic discriminant as the square of the
  product of the six pairwise root differences, written in the elementary
  symmetric functions `e₁,…,e₄` (`ring`);
* `six_one_shape_diff_sq` — for the four roots of the 6₁ shape polynomial (Vieta
  `e₁=3, e₂=6, e₃=5, e₄=2`) the product of the squared pairwise differences is
  `257`: the geometric (shape-difference) form of the 6₁ field discriminant.

(For the record, `algdep` also gives the 6₂ shape field `x⁵−3x⁴+5x³−5x²+4x−1`,
discriminant `1777` (prime); 6₃, being amphichiral, has a larger shape field.)

Generic `CommRing` (§7c); the transcendental hyperbolic data (`Vol(6₁) ≈ 3.16396`)
is archimedean and lives in the witness. Source: SnapPy `Manifold('6_1')`
(the shape) + PARI/GP `algdep` (the minimal polynomial); the discriminant identity
is a ring identity independent of the source.
-/

namespace QOU.QBeta.SixOneShapeDiscriminant

variable {R : Type*} [CommRing R]

/-- **Quartic discriminant as the product of squared root differences.** For any
four ring elements (the four shapes), the square of the product of their six
pairwise differences equals the quartic discriminant written in the elementary
symmetric functions `e₁ = Σyᵢ`, `e₂ = Σyᵢyⱼ`, `e₃ = Σyᵢyⱼyₖ`, `e₄ = ∏yᵢ`. -/
theorem disc_eq_root_diff_sq_quartic (y₁ y₂ y₃ y₄ e₁ e₂ e₃ e₄ : R)
    (h1 : y₁ + y₂ + y₃ + y₄ = e₁)
    (h2 : y₁*y₂ + y₁*y₃ + y₁*y₄ + y₂*y₃ + y₂*y₄ + y₃*y₄ = e₂)
    (h3 : y₁*y₂*y₃ + y₁*y₂*y₄ + y₁*y₃*y₄ + y₂*y₃*y₄ = e₃)
    (h4 : y₁*y₂*y₃*y₄ = e₄) :
    ((y₁ - y₂) * (y₁ - y₃) * (y₁ - y₄) * (y₂ - y₃) * (y₂ - y₄) * (y₃ - y₄)) ^ 2
      = -27*e₁^4*e₄^2 + 18*e₁^3*e₂*e₃*e₄ - 4*e₁^3*e₃^3 - 4*e₁^2*e₂^3*e₄
        + e₁^2*e₂^2*e₃^2 + 144*e₁^2*e₂*e₄^2 - 6*e₁^2*e₃^2*e₄ - 80*e₁*e₂^2*e₃*e₄
        + 18*e₁*e₂*e₃^3 - 192*e₁*e₃*e₄^2 + 16*e₂^4*e₄ - 4*e₂^3*e₃^2
        - 128*e₂^2*e₄^2 + 144*e₂*e₃^2*e₄ - 27*e₃^4 + 256*e₄^3 := by
  subst h1 h2 h3 h4
  ring

/-- **The four 6₁ shape differences square to `257`.** For the four roots of the
6₁ shape polynomial `x⁴ − 3x³ + 6x² − 5x + 2` (Vieta `Σy = 3`, `Σyᵢyⱼ = 6`,
`Σyᵢyⱼyₖ = 5`, `∏y = 2`), the product of their squared pairwise differences is the
field discriminant `257` — the geometric (shape-difference) form of the 6₁
arithmetic fingerprint, the 6-crossing analogue of `five_two_saddle_diff_sq = −23`. -/
theorem six_one_shape_diff_sq (y₁ y₂ y₃ y₄ : R)
    (h1 : y₁ + y₂ + y₃ + y₄ = 3)
    (h2 : y₁*y₂ + y₁*y₃ + y₁*y₄ + y₂*y₃ + y₂*y₄ + y₃*y₄ = 6)
    (h3 : y₁*y₂*y₃ + y₁*y₂*y₄ + y₁*y₃*y₄ + y₂*y₃*y₄ = 5)
    (h4 : y₁*y₂*y₃*y₄ = 2) :
    ((y₁ - y₂) * (y₁ - y₃) * (y₁ - y₄) * (y₂ - y₃) * (y₂ - y₄) * (y₃ - y₄)) ^ 2
      = 257 := by
  have key := disc_eq_root_diff_sq_quartic y₁ y₂ y₃ y₄ 3 6 5 2 h1 h2 h3 h4
  rw [key]
  norm_num

end QOU.QBeta.SixOneShapeDiscriminant
