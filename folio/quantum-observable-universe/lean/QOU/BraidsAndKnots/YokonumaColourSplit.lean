import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Commute.Defs

/-!
# Colour splitting of a Yokonuma–Hecke crossing

In the two-colour Yokonuma–Hecke algebra (Chlouveraki–Poulain d'Andecy presentation),
a crossing generator `g` and the same-colour idempotent `e = ½(1 + t_i t_{i+1})` satisfy

  `g * g = 1 + h * e * g`,  `e * e = e`,  `e * g = g * e`,

with `h = q - q⁻¹` central. This file proves, over an arbitrary (not necessarily
commutative) ring, that the relation splits by colour:

* on the same-colour sector `e`, the crossing `e * g` satisfies the Hecke quadratic
  `(e g)² = e + h (e g)`;
* on the mixed-colour sector `1 - e`, the crossing `(1 - e) * g` is an involution:
  `((1 - e) g)² = 1 - e`.

So a crossing between differently coloured strands has square one, with no further
scalar. This matches the involution `J` with `½(σ + σ⁻¹) = ([2]/2) J` that the
weak-vertex analysis assigns to a u–d crossing. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.YokonumaColourSplit

variable {R : Type*} [Ring R]

/-- On the same-colour sector the crossing satisfies the Hecke quadratic. -/
theorem sameColour_hecke (g e h : R)
    (hg : g * g = 1 + h * e * g) (he : e * e = e) (hc : e * g = g * e)
    (hhe : h * e = e * h) :
    (e * g) * (e * g) = e + h * (e * g) := by
  calc (e * g) * (e * g) = e * (g * e) * g := by simp only [mul_assoc]
    _ = e * (e * g) * g := by rw [hc]
    _ = (e * e) * (g * g) := by simp only [mul_assoc]
    _ = e * (1 + h * e * g) := by rw [he, hg]
    _ = e + (e * h) * e * g := by rw [mul_add, mul_one]; simp only [mul_assoc]
    _ = e + h * (e * g) := by rw [← hhe, mul_assoc h e e, he]; simp only [mul_assoc]

/-- On the mixed-colour sector the crossing is an involution. -/
theorem mixedColour_involution (g e h : R)
    (hg : g * g = 1 + h * e * g) (he : e * e = e) (hc : e * g = g * e)
    (hhe : h * e = e * h) :
    ((1 - e) * g) * ((1 - e) * g) = 1 - e := by
  have hc' : (1 - e) * g = g * (1 - e) := by
    rw [sub_mul, mul_sub, one_mul, mul_one, hc]
  have hidem : (1 - e) * (1 - e) = 1 - e := by
    rw [sub_mul, mul_sub, mul_sub, one_mul, one_mul, mul_one, he, sub_self, sub_zero]
  have hkill : (1 - e) * (e * h) = 0 := by
    rw [← mul_assoc, sub_mul, one_mul, he, sub_self, zero_mul]
  calc ((1 - e) * g) * ((1 - e) * g) = (1 - e) * (g * (1 - e)) * g := by
        simp only [mul_assoc]
    _ = (1 - e) * ((1 - e) * g) * g := by rw [hc']
    _ = ((1 - e) * (1 - e)) * (g * g) := by simp only [mul_assoc]
    _ = (1 - e) * (1 + h * e * g) := by rw [hidem, hg]
    _ = (1 - e) + ((1 - e) * (h * e)) * g := by
        rw [mul_add, mul_one]; simp only [mul_assoc]
    _ = 1 - e := by rw [hhe, hkill, zero_mul, add_zero]

end QOU.BraidsAndKnots.YokonumaColourSplit
