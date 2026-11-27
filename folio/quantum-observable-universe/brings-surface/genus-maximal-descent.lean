import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum.Basic


/-!
# QOU.Archimedean.genus_maximal_descent — Genus-maximal descent

The Descartes condition χ(A) = -6 forces the base Riemann surface
to have genus g = 4, given the Gauss–Bonnet relation 2(1 − g) = χ as a
hypothesis. The Hurwitz bound |Aut(Σ)| ≤ 84(g − 1) = 252 then applies at g = 4.
It holds for every g ≥ 2, so it does not single out g = 4; the name "maximal"
is historical (round-trip audit pass 2, C16).

LaTeX label: `prop:genus-maximal-descent`

## References

- [leitner2026] §6-archimedean-universe/genus-maximal-descent
-/

namespace QOU.Archimedean

/-- **Genus-maximal descent**: from the Descartes condition χ = -6 and
    the Gauss-Bonnet / Riemann-Roch formula 2(1 - g) = χ, the genus of
    the base curve is g = 4.

    Both χ = −6 and the Gauss–Bonnet relation are carried as fields, so
    the structure assumes the link between the categorical Euler
    characteristic and the genus; it does not derive it.
    |S₅| = 120 ≤ 84(g − 1) = 252 when g = 4, which is not a maximality
    statement.

    LaTeX: `\label{prop:genus-maximal-descent}` -/
structure GenusMaximalDescent where
  /-- The Euler characteristic of the algebra object. -/
  eulerChar : ℤ
  /-- The genus of the base Riemann surface. -/
  genus : ℤ
  /-- Descartes condition: χ = -6. -/
  euler_eq : eulerChar = -6
  /-- Gauss-Bonnet / Riemann-Roch: 2(1 - g) = χ. -/
  gauss_bonnet : 2 * (1 - genus) = eulerChar

/-- From χ = -6 and 2(1 - g) = χ, the genus is 4. -/
-- Ref: [leitner2026] Chapter 6, §Genus-maximal descent
theorem genus_eq_four (D : GenusMaximalDescent) : D.genus = 4 := by
  have h1 := D.gauss_bonnet
  have h2 := D.euler_eq
  linarith

/-- The Hurwitz bound for genus 4: |Aut(Σ)| ≤ 84(g - 1) = 252.
    Since |S₅| = 120, the S₅ automorphism group fits within the bound. -/
-- Ref: [leitner2026] Chapter 6, §Genus-maximal descent
theorem hurwitz_bound_genus_four : 84 * (4 - 1) = (252 : ℤ) := by
  norm_num

/-- S₅ has order 120, which is within the Hurwitz bound of 252 for g = 4. -/
-- Ref: [leitner2026] Chapter 6, §Genus-maximal descent
theorem s5_within_hurwitz : (120 : ℤ) ≤ 84 * (4 - 1) := by
  norm_num

/-- χ = −6 together with 2(1 − g) = χ determines g = 4. This is
    uniqueness of g, not maximality: the Hurwitz bound is not used. -/
-- Ref: [leitner2026] Chapter 6, §Genus-maximal descent
theorem genus_unique (g : ℤ) (hgb : 2 * (1 - g) = -6) : g = 4 := by
  linarith

end QOU.Archimedean
