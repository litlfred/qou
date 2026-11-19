import QOU.QBeta.BarParityZeta4Swap
import QOU.QBeta.CuspShapeBarParity
import Mathlib.Tactic.LinearCombination

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

-- Ref: [leitner2026] folio/quantum-observable-universe/braids-and-knots/approach-to-exceptional-divisor.md
-- Ref: [leitner2026] docs/audits/2026-07-11-planck-tick-disqualifier.md
-/

namespace QOU.Knot.CuspShapeBarParity

open QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-! ## Core cusp-shape lemmas — canonical home is `QOU.QBeta.CuspShapeBarParity`

The four core figure-eight cusp lemmas (`inv`, `barEven = 1`, `barOdd ² = −3`,
`barOdd = 2ω − 1`) are proved canonically over the `IsCuspShape` predicate in
[`QOU.QBeta.CuspShapeBarParity`](../QBeta/CuspShapeBarParity.lean)
(`cuspShape_inv` / `cuspShape_barEven` / `cuspShape_barOdd_sq` / `cuspShape_barOdd`),
which additionally proves `cuspShape_cube` / `_sixth` / `_reconstruct` and the golden
shape. This module previously duplicated those four proofs; they are removed and the
one downstream use below (`cusp_barParity_split`) delegates to the canonical lemmas.
The generic bar-involution multiplicativity lemmas `barEven_mul` / `barOdd_mul` have
been moved to their natural home, the base module `QOU.QBeta.BarParityZeta4Swap`
(where `barEven` / `barOdd` are defined); what remains genuinely new here is the
**meridian boost** `holonomy_hyperbola`. -/

/-- **Boost hyperbola.** The meridian holonomy `q` (any nonzero field element)
satisfies `barEven q ² − barOdd q ² = 4` — the `cosh² − sinh² = 1` identity.
One meridian turn is a hyperbolic rotation.

§7c note: the difference is `4·q·q⁻¹`, so the proof is a single explicit
unit witness (`q · q⁻¹ = 1`) rather than a `field_simp` denominator clear.
The `[Field R]` on the section variable is *not* removable here — it is
inherited from `barEven` / `barOdd`, which are defined with the ring
inverse `x⁻¹` in `QOU.QBeta.BarParityZeta4Swap`. -/
theorem holonomy_hyperbola {q : R} (hq : q ≠ 0) :
    barEven q ^ 2 - barOdd q ^ 2 = 4 := by
  simp only [barEven, barOdd]
  linear_combination (4 : R) * mul_inv_cancel₀ hq

/-- **Rapidity addition law (even / `cosh` channel):** composing meridian turns
multiplies the holonomies `q ↦ q · q'`, and the bar-even shapes obey the hyperbolic
cosine addition law `2 · barEven(q · q') = barEven q · barEven q' + barOdd q · barOdd q'`. -/
theorem holonomy_rapidity_add_even (q q' : R) :
    2 * barEven (q * q') = barEven q * barEven q' + barOdd q * barOdd q' :=
  barEven_mul q q'

/-- **Rapidity addition law (odd / `sinh` channel):** composing meridian turns
multiplies the holonomies `q ↦ q · q'`, and the bar-odd shapes obey the hyperbolic
sine addition law `2 · barOdd(q · q') = barOdd q · barEven q' + barEven q · barOdd q'`. -/
theorem holonomy_rapidity_add_odd (q q' : R) :
    2 * barOdd (q * q') = barOdd q * barEven q' + barEven q * barOdd q' :=
  barOdd_mul q q'

/-- **Cusp bar-parity split (paper statement).** The figure-eight cusp shape
`ω` (root of `Φ₆`) splits under the bar involution into a rational Volume part
`barEven ω = 1` and a `√−3` Chern–Simons part `barOdd ω ^ 2 = −3` — the
`𝔙 = Vol + i·CS` grading of the complex volume, realised algebraically. -/
theorem cusp_barParity_split {ω : R} (hω : ω ^ 2 - ω + 1 = 0) :
    barEven ω = 1 ∧ barOdd ω ^ 2 = -3 :=
  ⟨QOU.QBeta.CuspShapeBarParity.cuspShape_barEven hω,
   QOU.QBeta.CuspShapeBarParity.cuspShape_barOdd_sq hω⟩

/-- **Complete figure-eight cusp shape and meridian boost package:** combines the
cusp bar-parity split (`barEven ω = 1`, `barOdd ω ^ 2 = -3`, `barOdd ω = 2ω - 1`)
with the meridian boost hyperbola (`barEven q ^ 2 - barOdd q ^ 2 = 4`) and rapidity
addition laws. -/
theorem cusp_barParity_full_package {ω q q' : R} (hω : ω ^ 2 - ω + 1 = 0) (hq : q ≠ 0) :
    (barEven ω = 1 ∧ barOdd ω ^ 2 = -3 ∧ barOdd ω = 2 * ω - 1) ∧
    barEven q ^ 2 - barOdd q ^ 2 = 4 ∧
    2 * barEven (q * q') = barEven q * barEven q' + barOdd q * barOdd q' ∧
    2 * barOdd (q * q') = barOdd q * barEven q' + barEven q * barOdd q' :=
  ⟨⟨QOU.QBeta.CuspShapeBarParity.cuspShape_barEven hω,
    QOU.QBeta.CuspShapeBarParity.cuspShape_barOdd_sq hω,
    QOU.QBeta.CuspShapeBarParity.cuspShape_barOdd hω⟩,
   holonomy_hyperbola hq,
   holonomy_rapidity_add_even q q',
   holonomy_rapidity_add_odd q q'⟩

end QOU.Knot.CuspShapeBarParity
