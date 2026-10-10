import Mathlib.Tactic

/-!
# The ζ₄ bar-parity swap: translating bar-even ↔ bar-odd

The **explicit translator** between the mass (bar-even, `cosh`-like) and the
decay/binding (bar-odd, `sinh`-like) faces.  Complements the σ-parity *split*
(`QOU.QBeta.EkParitySplit`, which projects onto the two faces) and the ζ₄
f-map constraints — this file states the **swap map** they both use implicitly.

For any `x` in a field, put the two bar-parity shapes
$$\mathrm{barEven}(x) = x + x^{-1}\ (\cosh\text{-like}),\qquad
  \mathrm{barOdd}(x) = x - x^{-1}\ (\sinh\text{-like}),$$
symmetric / antisymmetric under the bar involution `x ↦ x⁻¹`.  A **quarter-turn
`x ↦ ζx`** by a primitive fourth root of unity (`ζ² = -1`) exchanges them:
$$\mathrm{barEven}(\zeta x) = \zeta\,\mathrm{barOdd}(x),\qquad
  \mathrm{barOdd}(\zeta x) = \zeta\,\mathrm{barEven}(x).$$

This is the algebraic `cosh ↔ sinh` realization `cosh(t) = -i\,\sinh(t+i\pi/2)`
(`x = eᵗ`, `ζ = e^{iπ/2} = i`): even ↔ odd is `Re ↔ Im` of the complex volume
`CVol = Vol + i·CS` (mass = `Re`/bar-even, decay=binding = `Im`/bar-odd), and the
translator is multiplication by `ζ₄ = i`.

**The swap is an algebraic / geometric-side operation, not an off-axis
continuation of the evaluation.**  Here `ζ` multiplies the (already complex)
*shape / coefficient* variable `x` — the geometric tetrahedron shape
(`z = e^{iπ/3}` for `4₁`) or the cyclotomic/Habiro coefficient — **not** the real
substrate evaluation point `q₀`.  So the bar-odd (decay/binding) object is
obtained by ζ₄-transporting the *solved* bar-even (geometric) object
**algebraically**, and then evaluating at the **same real `q₀`**.  No analytic
continuation of the `q₀` evaluation off the real axis is needed: the `ζ = i`
lives in the fibre/coefficient (where `c_k` legitimately live), while the
archimedean constraint `Im q₀ = 0` binds only the evaluation point.  This is why
the c₃ bar-odd `S` is "complex" (a `ζ₄` coefficient factor) yet observed at real
`q₀` — the transport happens on the algebraic/geometric side, the evaluation
stays real.

**Not a ζ₄-residue claim (coordination, §8 flip-flop guard).** This is a
functional-argument **swap** `x ↦ ζx`, orthogonal to the *residue* question
already settled by `QOU.QBeta.Zeta4Residue` (`QBetaZeta4ResidueRefutation`):
there `Φ₄ = q²+1` is proved **not** to divide the odd carrier, so the odd channel
has **no ζ₄-residue / no pole at `q = i`**.  Nothing here reopens that — the swap
`barEven(ζx) = ζ·barOdd(x)` is a parity-grading identity in the *argument*, not a
pole/divisibility statement in `q`, and it wires no `c_k`.

Generic field, no archimedean structure (§7c). No `c_k` wired.

-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md
-- Ref: [manuscript] docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md
-/

namespace QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-- Bar-even (`cosh`-like) shape: `x + x⁻¹`, fixed by the bar involution. -/
def barEven (x : R) : R := x + x⁻¹

/-- Bar-odd (`sinh`-like) shape: `x − x⁻¹`, negated by the bar involution. -/
def barOdd (x : R) : R := x - x⁻¹

/-- `barEven` is invariant under the bar involution `x ↦ x⁻¹`. -/
theorem barEven_bar (x : R) : barEven x⁻¹ = barEven x := by
  simp [barEven, add_comm]

/-- `barOdd` is negated by the bar involution `x ↦ x⁻¹`. -/
theorem barOdd_bar (x : R) : barOdd x⁻¹ = -barOdd x := by
  simp [barOdd]

/-- The inverse of a primitive fourth root of unity is its negative: `ζ⁻¹ = -ζ`. -/
theorem inv_eq_neg_of_sq_eq_neg_one {ζ : R} (hζ : ζ ^ 2 = -1) : ζ⁻¹ = -ζ := by
  -- `ζ * (-ζ) = -(ζ * ζ) = -(ζ ^ 2) = -(-1) = 1`, spelled with `mul_neg`/`pow_two`.
  have h1 : ζ * (-ζ) = 1 := by rw [mul_neg, ← pow_two, hζ, neg_neg]
  exact inv_eq_of_mul_eq_one_right h1

/-- **ζ₄ swap, even → odd.** With `ζ² = -1`, the quarter-turn `x ↦ ζx` carries the
bar-EVEN (mass) shape to `ζ` times the bar-ODD (decay/binding) shape. -/
theorem barEven_zeta_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barEven (ζ * x) = ζ * barOdd x := by
  have hζinv := inv_eq_neg_of_sq_eq_neg_one hζ
  simp only [barEven, barOdd, mul_inv, hζinv]
  ring

/-- **ζ₄ swap, odd → even.** The companion: the quarter-turn carries the bar-ODD
shape to `ζ` times the bar-EVEN shape. -/
theorem barOdd_zeta_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barOdd (ζ * x) = ζ * barEven x := by
  have hζinv := inv_eq_neg_of_sq_eq_neg_one hζ
  simp only [barEven, barOdd, mul_inv, hζinv]
  ring

/-- Two quarter-turns (`ζ²x = -x`) negate the bar-even shape — the `ζ₄` period-4
rotation `even → ζ·odd → -even → -ζ·odd → even`. -/
theorem barEven_zeta_sq_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barEven (ζ * (ζ * x)) = -barEven x := by
  rw [barEven_zeta_mul hζ, barOdd_zeta_mul hζ, ← mul_assoc, ← pow_two, hζ]
  ring

/-- **Rapidities add (cosh law).** Composing turns multiplies the arguments; the
bar-even (mass / `cosh`) shape obeys the addition formula. Generic bar-involution
multiplicativity — lives with `barEven`/`barOdd` (moved here from the cusp module). -/
theorem barEven_mul (x y : R) :
    2 * barEven (x * y) = barEven x * barEven y + barOdd x * barOdd y := by
  simp only [barEven, barOdd, mul_inv]
  ring

/-- **Rapidities add (sinh law).** The bar-odd (decay–binding / `sinh`) companion
of `barEven_mul`. -/
theorem barOdd_mul (x y : R) :
    2 * barOdd (x * y) = barOdd x * barEven y + barEven x * barOdd y := by
  simp only [barEven, barOdd, mul_inv]
  ring

end QOU.QBeta.BarParityZeta4Swap
