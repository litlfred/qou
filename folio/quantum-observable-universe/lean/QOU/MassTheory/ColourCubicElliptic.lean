import MathlibExt.ColourCubicHomogeneous
import Mathlib.Tactic

/-!
# The colour cubic is the elliptic curve `y² + xy + y = x³ − x − 2`

The homogenised colour cubic `h₃(X, z, w) = 0` (`QOU.Mass.ColourCubicHomogeneous`) is a plane
cubic. This file gives an explicit birational map, with an explicit inverse, between it and the
Weierstrass curve

  `E : y² + xy + y = x³ − x − 2`,

which is the curve with Cremona label 50a1 (conductor 50). All statements are polynomial
identities over a generic commutative ring, with field corollaries.

**The map.** With `L = 2X + 2z + w`,

  `x = −(X + z + 3w) / L`,   `y = (4X² + 4Xw − 2Xz + w² − wz − 6z²) / L²`.

It is the projection from the rational point `[1 : −1 : 0]` (the slope parameter is
`t = (X + z)/w`), followed by sending the second rational point `t = −1/2` of the resulting
quartic to infinity and a Weierstrass change of variables.

* `elliptic_of_colour` — `E(x, y)·L⁴ = 25·L·h₃`, cleared of denominators. So the map sends every
  point of `h₃ = 0` with `L ≠ 0` to `E`.
* `colour_of_elliptic` — the inverse
  `[X : z : w] = [x³ − 2x − 4 : −x³ + xy + x + 3y + 1 : −(2x + 1)(y − 1)]`
  satisfies `h₃ = −5(x³ − 2x − 4)(y − 1)·E(x, y)`.
* `forward_inverse_x`, `forward_inverse_L`, `forward_inverse_y` — forward ∘ inverse is the
  identity on `E` wherever `y ≠ 1` and `5` is invertible.
* `inverse_forward_cross_*` — inverse ∘ forward is the identity on `h₃ = 0` up to the projective
  scalar: the three 2×2 minors of the pair (inverse ∘ forward, identity) are multiples of `h₃`.

**What this does and does not establish.** Over a field in which `5 ≠ 0` (in particular over `ℚ`)
the two curves are birationally equivalent. They are in fact isomorphic, by a *linear* map:
`QOU.Mass.ColourCubicProjectiveIso` proves `E(M·v) = 25·h₃(v)` for an explicit 3×3 matrix `M`
with `det M = −25` (correction 2026-11-22: this file previously said the isomorphism was not
formalised). That file also gives `E` as a Mathlib `WeierstrassCurve` with `c₄ = 25`,
`c₆ = 1475`, `Δ = −1250`, `j = −25/2`, and a bijection between the points of `h₃ = 0` and
Mathlib's group of points of `E`. The Cremona label itself is a database fact; what is proved is
that `E` has the invariants the label records.

The corpus places the elliptic factor of the Jacobian of Bring's curve in the `ℚ`-isogeny class
50a (`docs/audits/2026-07-18-bring-s4-elliptic-factor-genus-and-period-block.md`). This file shows
the colour cover is a curve in that same class. It does not construct a map from Bring's curve to
the colour cubic.

Base ring §7c: `CommRing` identities, plus `Field` corollaries.

-- Ref: [leitner2026] computations/probes/colour_cubic_braid_monodromy_probe.py
-/

namespace QOU.Mass.ColourCubicElliptic

open QOU.Mass.ColourCubicHomogeneous

section Generic

variable {R : Type*} [CommRing R]

/-- The Weierstrass polynomial of `y² + xy + y = x³ − x − 2` (Cremona 50a1). -/
def weier (x y : R) : R := y ^ 2 + x * y + y - x ^ 3 + x + 2

/-- The line `L = 2X + 2z + w`; its points on the cubic go to the point at infinity of `E`. -/
def lineL (X z w : R) : R := 2 * X + 2 * z + w

/-- Numerator of the `x`-coordinate: `x = numX / L`. -/
def numX (X z w : R) : R := -(X + z + 3 * w)

/-- Numerator of the `y`-coordinate: `y = numY / L²`. -/
def numY (X z w : R) : R :=
  4 * X ^ 2 + 4 * X * w - 2 * X * z + w ^ 2 - w * z - 6 * z ^ 2

/-- **Forward map, cleared.** `E(numX/L, numY/L²)·L⁴ = 25·L·h₃`. -/
theorem elliptic_of_colour (X z w : R) :
    let L := lineL X z w
    let P := numX X z w
    let Q := numY X z w
    Q ^ 2 + P * Q * L + Q * L ^ 2 - P ^ 3 * L + P * L ^ 3 + 2 * L ^ 4
      = 25 * L * colourCubicHom X z w := by
  simp only []
  unfold lineL numX numY colourCubicHom; ring

/-- Inverse map, first coordinate. -/
def invX (x _y : R) : R := x ^ 3 - 2 * x - 4
/-- Inverse map, second coordinate. -/
def invZ (x y : R) : R := -x ^ 3 + x * y + x + 3 * y + 1
/-- Inverse map, third coordinate. -/
def invW (x y : R) : R := -(2 * x + 1) * (y - 1)

/-- **Inverse map.** `h₃(inverse(x, y)) = −5(x³ − 2x − 4)(y − 1)·E(x, y)`. -/
theorem colour_of_elliptic (x y : R) :
    colourCubicHom (invX x y) (invZ x y) (invW x y)
      = -5 * (x ^ 3 - 2 * x - 4) * (y - 1) * weier x y := by
  unfold colourCubicHom invX invZ invW weier; ring

/-- Forward ∘ inverse, the line: `L(inverse(x, y)) = 5(y − 1)`. -/
theorem forward_inverse_L (x y : R) :
    lineL (invX x y) (invZ x y) (invW x y) = 5 * (y - 1) := by
  unfold lineL invX invZ invW; ring

/-- Forward ∘ inverse, `x`: `numX(inverse(x, y)) = x·L(inverse(x, y))` identically. -/
theorem forward_inverse_x (x y : R) :
    numX (invX x y) (invZ x y) (invW x y) = x * lineL (invX x y) (invZ x y) (invW x y) := by
  unfold numX lineL invX invZ invW; ring

/-- Forward ∘ inverse, `y`: `numY(inverse) − y·L(inverse)² = −25(y − 1)·E(x, y)`. -/
theorem forward_inverse_y (x y : R) :
    numY (invX x y) (invZ x y) (invW x y) - y * lineL (invX x y) (invZ x y) (invW x y) ^ 2
      = -25 * (y - 1) * weier x y := by
  unfold numY lineL invX invZ invW weier; ring

/-- Inverse ∘ forward, homogenised (degree 6): first coordinate. -/
def backX (X z w : R) : R :=
  numX X z w ^ 3 - 2 * numX X z w * lineL X z w ^ 2 - 4 * lineL X z w ^ 3
/-- Inverse ∘ forward, homogenised: second coordinate. -/
def backZ (X z w : R) : R :=
  -numX X z w ^ 3 + numX X z w * numY X z w + numX X z w * lineL X z w ^ 2
    + 3 * numY X z w * lineL X z w + lineL X z w ^ 3
/-- Inverse ∘ forward, homogenised: third coordinate. -/
def backW (X z w : R) : R :=
  -(2 * numX X z w + lineL X z w) * (numY X z w - lineL X z w ^ 2)

/-- Inverse ∘ forward is the identity, minor `(X, z)`: `backX·z − backZ·X = −25(X + z)·h₃`. -/
theorem inverse_forward_cross_Xz (X z w : R) :
    backX X z w * z - backZ X z w * X = -25 * (X + z) * colourCubicHom X z w := by
  unfold backX backZ numX numY lineL colourCubicHom; ring

/-- Inverse ∘ forward, minor `(X, w)`: `backX·w − backW·X = −25w·h₃`. -/
theorem inverse_forward_cross_Xw (X z w : R) :
    backX X z w * w - backW X z w * X = -25 * w * colourCubicHom X z w := by
  unfold backX backW numX numY lineL colourCubicHom; ring

/-- Inverse ∘ forward, minor `(z, w)`: `backZ·w − backW·z = 25w·h₃`. -/
theorem inverse_forward_cross_zw (X z w : R) :
    backZ X z w * w - backW X z w * z = 25 * w * colourCubicHom X z w := by
  unfold backZ backW numX numY lineL colourCubicHom; ring

end Generic

section Field

variable {K : Type*} [Field K]

/-- **The forward map lands on `E`.** Over any field, a point of `h₃ = 0` off the line `L = 0`
maps to a point of `y² + xy + y = x³ − x − 2`. -/
theorem weier_of_colour {X z w : K} (h : colourCubicHom X z w = 0) (hL : lineL X z w ≠ 0) :
    weier (numX X z w / lineL X z w) (numY X z w / lineL X z w ^ 2) = 0 := by
  have key := elliptic_of_colour X z w
  simp only [] at key
  rw [h, mul_zero] at key
  unfold weier
  field_simp
  linear_combination key

/-- **The inverse lands on the colour cubic.** -/
theorem colour_of_weier {x y : K} (h : weier x y = 0) :
    colourCubicHom (invX x y) (invZ x y) (invW x y) = 0 := by
  rw [colour_of_elliptic, h, mul_zero]

/-- **Forward ∘ inverse = identity on `E`**, where `y ≠ 1` and `5 ≠ 0`. -/
theorem forward_inverse {x y : K} (h : weier x y = 0) (hy : y ≠ 1) (h5 : (5 : K) ≠ 0) :
    numX (invX x y) (invZ x y) (invW x y) / lineL (invX x y) (invZ x y) (invW x y) = x ∧
    numY (invX x y) (invZ x y) (invW x y) / lineL (invX x y) (invZ x y) (invW x y) ^ 2 = y := by
  have hL : lineL (invX x y) (invZ x y) (invW x y) ≠ 0 := by
    rw [forward_inverse_L]; exact mul_ne_zero h5 (sub_ne_zero.mpr hy)
  refine ⟨?_, ?_⟩
  · rw [div_eq_iff hL, forward_inverse_x]
  · rw [div_eq_iff (pow_ne_zero 2 hL)]
    have := forward_inverse_y x y
    rw [h, mul_zero] at this
    linear_combination this

end Field

end QOU.Mass.ColourCubicElliptic
