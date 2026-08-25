/-
  Ohtsuki's 5₂ critical point **is** the corpus's saddle cubic.

  Bean `qou-thmb`; probe `qbeta_5two_route71_ohtsuki_critical_point_probe.py`
  (5 gates, 80 dps, all passing).

  ═══ THE SOURCE ═══

  T. Ohtsuki, *On the asymptotic expansion of the Kashaev invariant of the 5₂
  knot*, Quantum Topol. **7** (2016) 669–735, DOI 10.4171/QT/83
  (`library/104171-qt-83/10.4171-qt-83.pdf`, blob `632e54ac`).  The 5₂ volume conjecture is a
  **published theorem** there — §3 is the saddle point method, §4 the Poisson
  summation, §5 the proof of Theorem 1.1.

  His potential (p. 671) is

      V̂(x,y) = Li₂(xy) + Li₂(1/(xy)) + Li₂(y) − Li₂(1/y) − Li₂(1/x) − Li₂(1)

  and its critical-point system, at `ħ → 0` (Appendix C, the display before
  (77)), is

      (1 − x)·y = 1,        x·(y − 1)² = 1.

  ═══ WHAT THIS FILE PROVES ═══

  Eliminating `y` from that system gives `x³ = (1−x)²` (`ohtsuki_elim`), and

      `x³ = (1−x)²`   is   `y² = (1−y)³`   under   `x = 1 − y`

  (`ohtsuki_cubic_iff_saddle_cubic`) — the corpus's own 5₂ saddle cubic, carried
  since Route 1 and the subject of the whole `qou-xblo` lane.  The exchange is
  the reflection `z ↦ 1 − z`, which is already a Lean theorem for the Rogers
  dilogarithm here (`FiveTwoComplexPentagon.cRogersL_add_one_sub`).

  Everything below is **polynomial**: stated over a `CommRing`, no field, no
  division, no analysis.  `ohtsuki_elim` in particular needs no `1 − x ≠ 0`
  side condition — the cofactor identity absorbs it.

  ═══ WHAT THIS FILE DOES NOT PROVE ═══

  **The volume.**  Route 71's G3 checks numerically that `Im V̂` at the *complex*
  critical point equals `Vol(5₂)`, matching the corpus's SnapPy HP 50-dps
  constant to its full recorded precision (residual `4.9e-50`).  That is a
  transcendental evaluation of a regulator and is **not** formalized here or
  anywhere in the corpus.

  **The volume conjecture.**  The asymptotic `(2π/N)·log ⟨5₂⟩_N → Vol(5₂)` is
  Ohtsuki's 67-page theorem.  None of it is in Lean.

  ⚠ And note G4: the *real* critical point gives `Im V̂ = 1.7668…`, **not** the
  volume.  The geometric solution is the complex one.  Nothing algebraic here
  selects it; branch selection is analytic input.

  **The 5₂ sum rule is PROVED**:
  `FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule` and
  `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.  It does not give
  the volume: `D` cancels identically on the Galois orbit.

  -- Ref: [ohtsuki2016] https://doi.org/10.4171/QT/83
-/
import QOU.QBeta.FiveTwoSaddleSumRule

namespace QOU.QBeta.FiveTwo.Ohtsuki

/-! ### The elimination -/

/-- **Ohtsuki's critical-point system eliminates to `x³ = (1−x)²`.**

From `(1−x)·y = 1` and `x·(y−1)² = 1`.  Over any commutative ring, and with **no
non-vanishing hypothesis**: the identity

    `x³ − (1−x)² = (1−x)²·(x(y−1)² − 1) − x·(x + (1−x)(y−1))·((1−x)y − 1)`

does the elimination directly.  The mechanism is `(1−x)(y−1) = x`, which is `h1`
rearranged. -/
theorem ohtsuki_elim {R : Type*} [CommRing R] {x y : R}
    (h1 : (1 - x) * y = 1) (h2 : x * (y - 1) ^ 2 = 1) :
    x ^ 3 = (1 - x) ^ 2 := by
  linear_combination (1 - x) ^ 2 * h2 - x * (x + (1 - x) * (y - 1)) * h1

/-- The step the elimination turns on: `(1−x)(y−1) = x` is exactly `(1−x)y = 1`
rearranged.  Recorded separately because it is the whole content. -/
theorem one_sub_mul_sub_one {R : Type*} [CommRing R] {x y : R}
    (h1 : (1 - x) * y = 1) : (1 - x) * (y - 1) = x := by
  linear_combination h1

/-! ### The identification with the corpus's saddle cubic -/

/-- **The two cubics are negatives of each other under `x = 1 − y`.**

`(1−x)³ − 2(1−x)² + 3(1−x) − 1 = −(x³ − x² + 2x − 1)`.  One `ring`. -/
theorem saddle_poly_of_ohtsuki_poly {R : Type*} [CommRing R] (x : R) :
    (1 - x) ^ 3 - 2 * (1 - x) ^ 2 + 3 * (1 - x) - 1
      = -(x ^ 3 - x ^ 2 + 2 * x - 1) := by
  ring

/-- `x³ = (1−x)²` in expanded form. -/
theorem ohtsuki_cubic_iff {R : Type*} [CommRing R] (x : R) :
    x ^ 3 = (1 - x) ^ 2 ↔ x ^ 3 - x ^ 2 + 2 * x - 1 = 0 := by
  constructor <;> intro h <;> linear_combination h

/-- **THE IDENTIFICATION.**  `x` is an Ohtsuki critical point iff `1 − x` is a
root of the corpus's 5₂ saddle cubic.

`FiveTwoSaddleSumRule.cubic_iff_sq_eq_cube` already gives
`y³ − 2y² + 3y − 1 = 0 ↔ y² = (1−y)³`, so this says the two branch equations —
Ohtsuki's `x³ = (1−x)²` and the corpus's `y² = (1−y)³` — are the same equation
in coordinates differing by `z ↦ 1 − z`. -/
theorem ohtsuki_cubic_iff_saddle_cubic {R : Type*} [CommRing R] (x : R) :
    x ^ 3 = (1 - x) ^ 2
      ↔ (1 - x) ^ 3 - 2 * (1 - x) ^ 2 + 3 * (1 - x) - 1 = 0 := by
  rw [ohtsuki_cubic_iff, saddle_poly_of_ohtsuki_poly, neg_eq_zero]

/-- The same, phrased in the `y² = (1−y)³` form the corpus carries: setting
`y = 1 − x`, Ohtsuki's equation is the corpus's branch equation verbatim. -/
theorem ohtsuki_cubic_iff_sq_eq_cube {R : Type*} [CommRing R] (x : R) :
    x ^ 3 = (1 - x) ^ 2 ↔ (1 - x) ^ 2 = (1 - (1 - x)) ^ 3 := by
  constructor <;> intro h <;> linear_combination -h

/-- **End to end**: a solution of Ohtsuki's critical-point system hands you a
root of the corpus's saddle cubic, namely `1 − x`.

This is the bridge from Ohtsuki's volume-conjecture saddle to the data
`SaddleRoots` bundles — with the caveat, stated in the module header and gated as
G4 of Route 71, that *which* root is the geometric one is analytic input that no
algebraic statement here supplies. -/
theorem saddle_cubic_of_ohtsuki_system {R : Type*} [CommRing R] {x y : R}
    (h1 : (1 - x) * y = 1) (h2 : x * (y - 1) ^ 2 = 1) :
    (1 - x) ^ 3 - 2 * (1 - x) ^ 2 + 3 * (1 - x) - 1 = 0 :=
  (ohtsuki_cubic_iff_saddle_cubic x).mp (ohtsuki_elim h1 h2)

end QOU.QBeta.FiveTwo.Ohtsuki
