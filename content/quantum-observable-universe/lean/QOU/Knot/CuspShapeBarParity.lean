import QOU.QBeta.BarParityZeta4Swap

/-!
# Cusp-shape bar-parity: the figure-eight modulus split `𝔙 = Vol + i·CS`

The cusp shape of the figure-eight knot `4₁` is `ω = e^{iπ/3}`, a primitive
sixth root of unity — a root of the cyclotomic polynomial `Φ₆(z) = z² − z + 1`,
with trace field `ℚ(√−3)`.  Splitting `ω` along the bar involution `x ↦ x⁻¹`
(`QOU.QBeta.BarParityZeta4Swap`) recovers the complex-volume grading
`𝔙 = Vol + i·CS`:

* **bar-even** (`cosh`-like, real / Vol side): `barEven ω = ω + ω⁻¹ = 1`
  — the *rational* part, `2cos(π/3) = 1`;
* **bar-odd** (`sinh`-like, imaginary / CS side): `barOdd ω = ω − ω⁻¹ = 2ω − 1`
  with `barOdd ω ^ 2 = −3` — the `√−3` cusp modulus, `(2i·sin(π/3))² = −3`.

So the exceptional divisor / cusp shape is reached along the **bar-odd**
direction (the Chern–Simons / `Im 𝔙` axis), while its bar-even shadow is the
rational Volume normalisation.  This is the algebraic core of "the meridian is
at the exceptional divisor": the meridian is the bar-odd (boost) cycle.

## Boost / rapidity structure — "one meridian turn = one knot operation"

The meridian holonomy is multiplication by the substrate `q` (one turn = one
`R`-matrix application = one crossing).  Under the bar split:

* `q` sits on the **boost hyperbola** `barEven q ² − barOdd q ² = 4`
  (the `cosh² − sinh² = 1` identity, ×4) — one turn is a *hyperbolic* rotation,
  not a compact spin;
* composing turns multiplies the holonomies `q ↦ q·q'`, and this **adds
  rapidity**: the bar-even/bar-odd shapes obey the `cosh`/`sinh` addition laws
  `2·barEven(qq') = barEven q · barEven q' + barOdd q · barOdd q'` (and the odd
  companion).  Additive rapidity ⇔ multiplicative holonomy.

At a real substrate `q₀ > 1` the turn is a genuine boost of rapidity `ln q₀`
(`≈ 0.104`); only at a root of unity (`|q| = 1`) is it a compact `U(1)` spin.
That real-vs-compact split is the fibre-vs-observable `Im q` wall — the bar-odd
`sinh` axis carries the boost, exactly the axis along which the cusp shape sits
(`barOdd ω ^ 2 = −3`).  The archimedean rapidity `ln q₀` lives on the `ℝ`
specialisation side; everything here is generic-field (§7c), no `c_k` wired.

-- Ref: [manuscript] content/quantum-observable-universe/braids-and-knots/approach-to-exceptional-divisor.md
-- Ref: [manuscript] docs/audits/2026-07-11-planck-tick-disqualifier.md
-/

namespace QOU.Knot.CuspShapeBarParity

open QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-- From `Φ₆(ω) = 0` (`ω² − ω + 1 = 0`), the bar-involution image is
`ω⁻¹ = 1 − ω`.  (No `ω ≠ 0` hypothesis needed: `ω·(1−ω) = 1` gives the inverse.) -/
theorem cusp_inv {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : ω⁻¹ = 1 - ω := by
  have hmul : ω * (1 - ω) = 1 := by linear_combination -hω
  exact inv_eq_of_mul_eq_one_right hmul

/-- **Bar-even (Vol) side is rational:** `barEven ω = 1` (`= 2cos(π/3)`).
The Volume normalisation of the figure-eight cusp shape. -/
theorem cusp_barEven {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : barEven ω = 1 := by
  rw [barEven, cusp_inv hω]; ring

/-- **Bar-odd (CS) side squares to `−3`:** `barOdd ω ^ 2 = −3`, the `√−3` cusp
modulus of the figure-eight (`(2i·sin(π/3))² = −3`).  The Chern–Simons /
`Im 𝔙` component of the complex volume. -/
theorem cusp_barOdd_sq {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : barOdd ω ^ 2 = -3 := by
  rw [barOdd, cusp_inv hω]
  linear_combination (4 : R) * hω

/-- The bar-odd cusp shape is `2ω − 1` explicitly (the antisymmetric part). -/
theorem cusp_barOdd_eq {ω : R} (hω : ω ^ 2 - ω + 1 = 0) : barOdd ω = 2 * ω - 1 := by
  rw [barOdd, cusp_inv hω]; ring

/-- **Boost hyperbola.** The meridian holonomy `q` (any nonzero field element)
satisfies `barEven q ² − barOdd q ² = 4` — the `cosh² − sinh² = 1` identity.
One meridian turn is a hyperbolic rotation. -/
theorem holonomy_hyperbola {q : R} (hq : q ≠ 0) :
    barEven q ^ 2 - barOdd q ^ 2 = 4 := by
  simp only [barEven, barOdd]
  field_simp
  ring

/-- **Rapidities add (cosh law).** Composing meridian turns multiplies the
holonomies; the bar-even (mass / `cosh`) shape obeys the addition formula. -/
theorem barEven_mul (x y : R) :
    2 * barEven (x * y) = barEven x * barEven y + barOdd x * barOdd y := by
  simp only [barEven, barOdd, mul_inv]
  ring

/-- **Rapidities add (sinh law).** The bar-odd (decay–binding / `sinh`)
companion of `barEven_mul`. -/
theorem barOdd_mul (x y : R) :
    2 * barOdd (x * y) = barOdd x * barEven y + barEven x * barOdd y := by
  simp only [barEven, barOdd, mul_inv]
  ring

/-- **Cusp bar-parity split (paper statement).** The figure-eight cusp shape
`ω` (root of `Φ₆`) splits under the bar involution into a rational Volume part
`barEven ω = 1` and a `√−3` Chern–Simons part `barOdd ω ^ 2 = −3` — the
`𝔙 = Vol + i·CS` grading of the complex volume, realised algebraically. -/
theorem cusp_barParity_split {ω : R} (hω : ω ^ 2 - ω + 1 = 0) :
    barEven ω = 1 ∧ barOdd ω ^ 2 = -3 :=
  ⟨cusp_barEven hω, cusp_barOdd_sq hω⟩

end QOU.Knot.CuspShapeBarParity
