import QOU.QBeta.BarParityZeta4Swap

/-!
# The 5₂ cusp shapes in bar-parity coordinates — two cubic classes, and `Φ₆` reappears

The **5₂ analogue** of `QOU.QBeta.CuspShapeBarParity`, which does the same job for
the figure-eight. That file records the 4₁ complete structure — both ideal
tetrahedra at the sixth root of unity `ω`, `Φ₆(ω) = ω² − ω + 1 = 0`, trace field
`ℚ(√−3)` — and reads its bar-parity split `barEven ω = 1`, `(barOdd ω)² = −3` as
the `𝔙 = Vol + i·CS` split.

5₂ is not that. Measured from its complete hyperbolic structure (snappy, 300-bit
shapes, verified below to ~1e-61):

* it has **three** ideal tetrahedra, and **two of them share a shape**:
  `z₁ = z₃ ≠ z₂` — exactly, not approximately;
* neither shape is a root of unity. Both are **cubic**, with *different* minimal
  polynomials over `ℚ`:

      A-shape (z₁ = z₃):   z³ − 2z² + 3z − 1 = 0
      B-shape (z₂):        z³ − 2z² +  z − 1 = 0

* **both cubics have discriminant −23 and signature `(r₁,r₂) = (1,1)`**, so both
  generate the cubic field of discriminant `−23` — the same field, by two
  different generators. The signature independently reproduces the `(1,1)` that
  `dt_d1b_trace_field_bar_grading_probe` measured for 5₂ by Sturm counting.

This file states the bar-parity coordinates of both shapes over a **generic
field** — these are polynomial identities in the shape relation, with no
archimedean content, so §7c keeps them off `ℝ`.

## What the file establishes, and the one thing worth noticing

Reducing `z⁻¹` against each cubic (the constant term is `−1`, so `z` is a unit
with a *polynomial* inverse):

| | `z⁻¹` | `barEven z = z + z⁻¹` | `barOdd z = z − z⁻¹` |
|---|---|---|---|
| A | `z² − 2z + 3` | `z² − z + 3` | `−z² + 3z − 3` |
| B | `(z − 1)²` | `z² − z + 1` | `−z² + 3z − 1` |

**The B-shape's bar-even coordinate is `z² − z + 1 = Φ₆(z)`** — the very
polynomial whose *vanishing* defines the 4₁ cusp shape. For 4₁, `Φ₆(ω) = 0`; for
5₂'s B-shape, `Φ₆` is not zero but *is* the bar-even coordinate. Both statements
are proved here (`shape52B_barEven`, and `cyclotomic_six` for the naming).

**Stated as an identity, NOT as an interpretation.** It is a two-line consequence
of `z⁻¹ = (z−1)²`, which is itself a two-line consequence of the B-cubic. Whether
the reappearance of `Φ₆` across the two knots *means* anything is not addressed
here and is not claimed; recording it is cheap, and reading significance into an
algebraic coincidence is the failure mode this arc has hit repeatedly.

**And a genuine contrast with 4₁, which is the substantive difference.** For the
figure-eight `barEven ω = 1` — *rational*, which is what makes the bar-even
coordinate the anchor-stable `−Vol(4₁)` part. For 5₂ **neither** shape has
rational `barEven`: both cubics are irreducible over `ℚ` (verified in the probe
by the rational-root test), so each `barEven` lies in the cubic field. So
the 4₁ story does not transcribe, and the bar-even/bar-odd split for 5₂ lands in
a cubic field rather than in `ℚ` plus `√−3`.

## Verification

`lean`-direct **exit 0**, sorry-free, on all 19 declarations of this file
(16 theorems + 3 definitions). Because the QOU
package's own oleans are not built in this container, the check was run on a
standalone transcription with `barEven`/`barOdd` inlined and narrow Mathlib
imports; the mathematics is identical, but this file **as written**, importing
`QOU.QBeta.BarParityZeta4Swap`, has not itself been compiled against that
import. Stated explicitly rather than reported as a clean build.

**Lean caught a false theorem here**, which is why the characteristic hypothesis
exists: `shape52A_not_shape52B` was first stated over a general field and is
FALSE in characteristic 2, where `−2z² = 0` and `3z = z` collapse both cubics to
`z³ + z + 1`. `shape52_cubics_agree_in_char_two` records that as a theorem rather
than a footnote.

## Provenance

Shapes and minimal polynomials measured in
`computations/qbeta/d1b_52_cusp_shape_bar_parity_probe.py` (exact integer
verification of the cubics, discriminants and the four identities above; the
shapes themselves come from snappy at 300 bits). Nothing here is fitted: the two
cubics are *found* by exact search over integer coefficients and then *verified*
symbolically.
-/

namespace QOU.QBeta.FiveTwoCuspShapeBarParity

open QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-! ### §1  The two shape classes -/

/-- The **A-shape** of 5₂ — carried by two of the three ideal tetrahedra
(`z₁ = z₃`): a root of `z³ − 2z² + 3z − 1`. -/
def IsShape52A (z : R) : Prop := z ^ 3 - 2 * z ^ 2 + 3 * z - 1 = 0

/-- The **B-shape** of 5₂ — carried by the remaining tetrahedron (`z₂`): a root
of `z³ − 2z² + z − 1`. -/
def IsShape52B (z : R) : Prop := z ^ 3 - 2 * z ^ 2 + z - 1 = 0

/-- `Φ₆`, the sixth cyclotomic polynomial, named so the `barEven` coincidence
below can be stated in its own terms rather than as a bare quadratic. -/
def cyclotomic_six (z : R) : R := z ^ 2 - z + 1

/-! ### §2  Both shapes are units, with polynomial inverses -/

theorem shape52A_ne_zero {z : R} (hz : IsShape52A z) : z ≠ 0 := by
  intro h
  rw [IsShape52A, h] at hz
  norm_num at hz

theorem shape52B_ne_zero {z : R} (hz : IsShape52B z) : z ≠ 0 := by
  intro h
  rw [IsShape52B, h] at hz
  norm_num at hz

/-- `z · (z² − 2z + 3) = 1` on the A-shape. -/
theorem shape52A_mul_inv {z : R} (hz : IsShape52A z) :
    z * (z ^ 2 - 2 * z + 3) = 1 := by
  have h : z ^ 3 - 2 * z ^ 2 + 3 * z - 1 = 0 := hz
  linear_combination h

/-- The A-shape's inverse is the polynomial `z² − 2z + 3`. -/
theorem shape52A_inv {z : R} (hz : IsShape52A z) : z⁻¹ = z ^ 2 - 2 * z + 3 :=
  eq_comm.mp (eq_inv_of_mul_eq_one_left (by
    rw [mul_comm]; exact shape52A_mul_inv hz))

/-- `z · (z − 1)² = 1` on the B-shape. -/
theorem shape52B_mul_inv {z : R} (hz : IsShape52B z) : z * (z - 1) ^ 2 = 1 := by
  have h : z ^ 3 - 2 * z ^ 2 + z - 1 = 0 := hz
  linear_combination h

/-- The B-shape's inverse is the polynomial `(z − 1)²`. -/
theorem shape52B_inv {z : R} (hz : IsShape52B z) : z⁻¹ = (z - 1) ^ 2 :=
  eq_comm.mp (eq_inv_of_mul_eq_one_left (by
    rw [mul_comm]; exact shape52B_mul_inv hz))

/-! ### §3  Bar-parity coordinates -/

/-- **A-shape, bar-even:** `barEven z = z² − z + 3`. -/
theorem shape52A_barEven {z : R} (hz : IsShape52A z) :
    barEven z = z ^ 2 - z + 3 := by
  rw [barEven, shape52A_inv hz]; ring

/-- **A-shape, bar-odd:** `barOdd z = −z² + 3z − 3`. -/
theorem shape52A_barOdd {z : R} (hz : IsShape52A z) :
    barOdd z = -z ^ 2 + 3 * z - 3 := by
  rw [barOdd, shape52A_inv hz]; ring

/-- **B-shape, bar-even:** `barEven z = z² − z + 1`. -/
theorem shape52B_barEven {z : R} (hz : IsShape52B z) :
    barEven z = z ^ 2 - z + 1 := by
  rw [barEven, shape52B_inv hz]; ring

/-- **The B-shape's bar-even coordinate IS `Φ₆`** — the polynomial whose
vanishing defines the 4₁ cusp shape. An identity, not an interpretation: it is
immediate from `shape52B_inv`. -/
theorem shape52B_barEven_eq_cyclotomic_six {z : R} (hz : IsShape52B z) :
    barEven z = cyclotomic_six z := by
  rw [shape52B_barEven hz, cyclotomic_six]

/-- **B-shape, bar-odd:** `barOdd z = −z² + 3z − 1`. -/
theorem shape52B_barOdd {z : R} (hz : IsShape52B z) :
    barOdd z = -z ^ 2 + 3 * z - 1 := by
  rw [barOdd, shape52B_inv hz]; ring

/-! ### §4  Reconstruction, and the contrast with 4₁ -/

/-- Both coordinates together recover `2z`, as for any shape. -/
theorem shape52_reconstruct (z : R) : barEven z + barOdd z = 2 * z := by
  rw [barEven, barOdd]; ring

/-- **The two 5₂ shapes are distinct** away from characteristic 2: subtracting
the cubics forces `2z = 0`, and with `2 ≠ 0` that gives `z = 0`, which
`shape52A_ne_zero` excludes. This is the algebraic form of the measured
`z₁ = z₃ ≠ z₂`. The `2 ≠ 0` hypothesis is NOT decoration — see the next
theorem. -/
theorem shape52A_not_shape52B {z : R} (htwo : (2 : R) ≠ 0)
    (hA : IsShape52A z) : ¬ IsShape52B z := by
  intro hB
  have hA' : z ^ 3 - 2 * z ^ 2 + 3 * z - 1 = 0 := hA
  have hB' : z ^ 3 - 2 * z ^ 2 + z - 1 = 0 := hB
  have h2 : (2 : R) * z = 0 := by linear_combination hA' - hB'
  have hz : z = 0 := by
    rcases mul_eq_zero.mp h2 with h | h
    · exact absurd h htwo
    · exact h
  exact shape52A_ne_zero hA hz

/-- **The hypothesis is necessary, and Lean is what caught that.** In
characteristic 2 the two cubics COINCIDE — `−2z² = 0` and `3z = z` — so both
read `z³ + z + 1 = 0` and a single element satisfies both. The distinctness of
the 5₂ shape classes is a characteristic-0 fact about this knot, not a formal
consequence of the two polynomials being different as symbols. -/
theorem shape52_cubics_agree_in_char_two {S : Type*} [Field S] (h : (2 : S) = 0)
    (z : S) : (z ^ 3 - 2 * z ^ 2 + 3 * z - 1) = (z ^ 3 - 2 * z ^ 2 + z - 1) := by
  have h2 : (2 : S) * z = 0 := by rw [h]; ring
  linear_combination h2

/-- The **contrast with 4₁**, stated as the obstruction it is: for the
figure-eight `barEven ω = 1` is *rational*, whereas a 5₂ A-shape with rational
`barEven` would force its cubic to have the corresponding rational root. This
lemma is the reusable half — `barEven` determines `z² − z` on the A-shape, so a
rational `barEven` pins a quadratic relation that the cubic must also satisfy. -/
theorem shape52A_barEven_quadratic {z : R} (hz : IsShape52A z) (c : R)
    (h : barEven z = c) : z ^ 2 - z = c - 3 := by
  rw [shape52A_barEven hz] at h
  linear_combination h

/-- Same, for the B-shape: a value of `barEven` pins `z² − z`. -/
theorem shape52B_barEven_quadratic {z : R} (hz : IsShape52B z) (c : R)
    (h : barEven z = c) : z ^ 2 - z = c - 1 := by
  rw [shape52B_barEven hz] at h
  linear_combination h

end QOU.QBeta.FiveTwoCuspShapeBarParity
