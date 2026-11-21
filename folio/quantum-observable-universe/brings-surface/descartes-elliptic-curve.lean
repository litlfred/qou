import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt


/-!
# QOU.Archimedean.descartes_elliptic_curve — The Descartes elliptic curve E_q

The color elliptic fiber of Bring's surface at spacetime ratio
z = s - s⁻¹ (s = √q) is the elliptic curve

  E_q : y² = x³ + p(q)·x + r(q)

with Weierstrass coefficients expressible in q.  The discriminant
Δ(q) < 0 at the substrate parameter, giving one real component.
The curve degenerates at q = 1 (classical limit) and acquires a
cusp at q = 1/φ² (golden ratio threshold).

LaTeX label: `prop:descartes-elliptic-curve`

## References

- [leitner2026] §5/descartes-elliptic-curve

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- The first Weierstrass coefficient p(q) of the Descartes elliptic curve.

    p(q) = 2(q² - q + 1)/(3q) + (q - 1)/(3√q) -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
noncomputable def weierstrass_p (q : ℝ) : ℝ :=
  2 * (q ^ 2 - q + 1) / (3 * q) + (q - 1) / (3 * q ^ (1/2 : ℝ))

/-- The second Weierstrass coefficient r(q) of the Descartes elliptic curve.

    r(q) = 20(q-1)³/(27q^{3/2}) + 5(q-1)²/(9q) + 5(√q - 1/√q)/9 + 20/27 -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
noncomputable def weierstrass_r (q : ℝ) : ℝ :=
  20 * (q - 1) ^ 3 / (27 * q ^ (3/2 : ℝ))
  + 5 * (q - 1) ^ 2 / (9 * q)
  + 5 * (q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))) / 9
  + 20 / 27

/-- The discriminant Δ of a Weierstrass curve y² = x³ + px + r. -/
noncomputable def weierstrass_discriminant (p r : ℝ) : ℝ :=
  -16 * (4 * p ^ 3 + 27 * r ^ 2)

/-- The j-invariant of a Weierstrass curve `y² = x³ + px + r`:
    `j = -1728·(4p)³ / Δ`, where `Δ` is the `weierstrass_discriminant`
    `-16(4p³ + 27r²)`. -/
noncomputable def j_invariant (p r : ℝ) : ℝ :=
  -1728 * (4 * p) ^ 3 / weierstrass_discriminant p r

/- **Descartes elliptic curve** (Proposition):

    The color elliptic fiber of Bring's surface at spacetime ratio
    z = s - s⁻¹ (s = √q) is the elliptic curve E_q with Weierstrass
    coefficients p(q) and r(q).

    The proof proceeds by substituting z = s - s⁻¹ into the color
    cubic X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0, applying the
    standard Weierstrass shift X = x - (z+1)/3, and simplifying. -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
/-- **Color-cubic ↦ Weierstrass substitution.**

    **Was an axiom; proved 2026-11-15.** With `s = q^{1/2} > 0` we have
    `s² = q`, `q^{3/2} = q·s` and `q^{-1/2} = s⁻¹`; after that the two
    identities are rational-function identities in `s`, closed by
    `field_simp; ring`. -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
theorem descartes_elliptic_curve (q : ℝ) (hq : 0 < q) :
    let s := q ^ (1/2 : ℝ)
    let z := s - s⁻¹
    let p_z := 2/3 * z ^ 2 + 1/3 * z + 2/3
    let r_z := 20/27 * z ^ 3 + 5/9 * z ^ 2 + 5/9 * z + 20/27
    p_z = weierstrass_p q ∧ r_z = weierstrass_r q := by
  intro s z p_z r_z
  have hspos : 0 < s := Real.rpow_pos_of_pos hq _
  have hsne : s ≠ 0 := ne_of_gt hspos
  have hs2 : s ^ 2 = q := by
    show (q ^ (1/2 : ℝ)) ^ 2 = q
    rw [← Real.sqrt_eq_rpow]; exact Real.sq_sqrt hq.le
  have h12 : q ^ (1/2 : ℝ) = s := rfl
  have h32 : q ^ (3/2 : ℝ) = q * s := by
    rw [show (3/2:ℝ) = 1 + 1/2 by norm_num, Real.rpow_add hq, Real.rpow_one]
  have hneg : q ^ (-(1/2 : ℝ)) = s⁻¹ := Real.rpow_neg hq.le _
  refine ⟨?_, ?_⟩
  · simp only [p_z, z, weierstrass_p]
    rw [h12]
    clear_value s
    subst hs2
    field_simp
    ring
  · simp only [r_z, z, weierstrass_r]
    rw [h32, hneg, h12]
    clear_value s
    subst hs2
    field_simp

/-- At the classical limit q = 1, the curve degenerates to
    y² = x³ + (2/3)x + 20/27. -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
theorem classical_limit_p : weierstrass_p 1 = 2/3 := by
  unfold weierstrass_p
  -- Ref: [leitner2026] §5/descartes-elliptic-curve
  -- At q = 1: first term = 2·(1-1+1)/(3·1) = 2/3, second term = 0/(3·1) = 0.
  simp [Real.one_rpow]

/- The golden ratio degeneration: r(q) has factor (s² + s - 1)
    which vanishes at s = 1/φ, i.e. q = 1/φ² = (3 - √5)/2. -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
/-- **Golden-ratio degeneration of `r(q)`.**  At `q = 1/φ²` the factor
    `(s² + s − 1)` vanishes, so `r(q) = 0` (cusp).

    **Was an axiom; proved 2026-09-04.**  The `rpow` occurrences are the only
    real obstacle and they all collapse at this `q`: with `φ² = φ + 1` we have
    `q = (1/φ)²`, hence `q ^ (1/2) = 1/φ` by `Real.sqrt_sq`,
    `q ^ (3/2) = q · (1/φ)` by `Real.rpow_add`, and `q ^ (−1/2) = φ` by
    `Real.rpow_neg`.  What remains is a polynomial identity in `√5` that is
    *exactly* zero once `√5 ^ n` is reduced for `n = 2 … 6` — both the rational
    part and the `√5` part cancel, which is the algebraic content of `s − s⁻¹
    = −1` at the golden section. -/
-- Ref: [leitner2026] §5/descartes-elliptic-curve
theorem golden_ratio_degeneration :
    weierstrass_r (1 / ((1 + Real.sqrt 5) / 2) ^ 2) = 0 := by
  have h5 : (0:ℝ) ≤ 5 := by norm_num
  have hs5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt h5
  set φ : ℝ := (1 + Real.sqrt 5) / 2 with hφ
  have hφpos : (0:ℝ) < φ := by rw [hφ]; nlinarith [Real.sqrt_nonneg 5]
  have hφne : φ ≠ 0 := ne_of_gt hφpos
  have hφ2 : φ ^ 2 = φ + 1 := by rw [hφ]; nlinarith [hs5]
  set q : ℝ := 1 / φ ^ 2 with hq
  have hqpos : (0:ℝ) < q := by rw [hq]; positivity
  have hqsq : q = (1/φ) ^ 2 := by rw [hq]; field_simp
  have hsq : q ^ (1/2 : ℝ) = 1 / φ := by
    rw [← Real.sqrt_eq_rpow, hqsq, Real.sqrt_sq (by positivity)]
  have h32 : q ^ (3/2 : ℝ) = q * (1/φ) := by
    rw [show (3/2:ℝ) = 1 + 1/2 by norm_num, Real.rpow_add hqpos, Real.rpow_one, hsq]
  have hneg : q ^ (-(1/2 : ℝ)) = φ := by
    rw [Real.rpow_neg hqpos.le, hsq]; field_simp
  unfold weierstrass_r
  rw [h32, hsq, hneg, hq]
  field_simp
  have p3 : Real.sqrt 5 ^ 3 = 5 * Real.sqrt 5 := by
    have e : Real.sqrt 5 ^ 3 = Real.sqrt 5 ^ 2 * Real.sqrt 5 := by ring
    rw [e, hs5]
  have p4 : Real.sqrt 5 ^ 4 = 25 := by
    have e : Real.sqrt 5 ^ 4 = (Real.sqrt 5 ^ 2) ^ 2 := by ring
    rw [e, hs5]; norm_num
  have p5 : Real.sqrt 5 ^ 5 = 25 * Real.sqrt 5 := by
    have e : Real.sqrt 5 ^ 5 = (Real.sqrt 5 ^ 2) ^ 2 * Real.sqrt 5 := by ring
    rw [e, hs5]; norm_num
  have p6 : Real.sqrt 5 ^ 6 = 125 := by
    have e : Real.sqrt 5 ^ 6 = (Real.sqrt 5 ^ 2) ^ 3 := by ring
    rw [e, hs5]; norm_num
  rw [hφ]
  ring_nf
  rw [p3, p4, p5, p6, hs5]
  ring

end QOU.Archimedean
