/-!
# Gluon-octet × substrate coupling at second order

The `8q` prefactor in the α_EM formula's second-order term
`8q · δ_CS²` factorizes as `8 = dim su(3) · q`.  The integer `8` is
forced by the Borromean volume relation `Vol(B_3) = 8G` (the gluon
octet); the `q` factor is the substrate scaling at second order.

For Hecke algebras on `n` strands the analogous correction would
have prefactor `(n² − 1) · q = dim su(n) · q`.

-- Ref: [manuscript] prop:gluon-octet-substrate-coupling
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.GroupPower.Basic

namespace QOU.WedderburnMass

/-- **`dim su(n) = n² − 1`.**  The gluon-octet count for `n = 3` is `8`. -/
def dim_su (n : ℕ) : ℕ := n * n - 1

theorem dim_su_three : dim_su 3 = 8 := by
  unfold dim_su
  rfl

/-- **`8q` prefactor**: gluon-octet count times substrate parameter. -/
def gluon_substrate_coeff {R : Type*} [CommRing R] (q : R) : R :=
  (dim_su 3 : R) * q

/-- **Theorem (factorization).**  `8q = (dim su(3)) · q = 8 · q`. -/
theorem gluon_substrate_coeff_eq {R : Type*} [CommRing R] (q : R) :
    gluon_substrate_coeff q = 8 * q := by
  unfold gluon_substrate_coeff dim_su
  norm_num

/-- **Generalization**: for Hecke algebras on `n` strands, the
    analogous prefactor is `dim_su(n) · q`. -/
def gluon_substrate_coeff_general
    {R : Type*} [CommRing R] (n : ℕ) (q : R) : R :=
  (dim_su n : R) * q

theorem gluon_substrate_coeff_special
    {R : Type*} [CommRing R] (q : R) :
    gluon_substrate_coeff_general 3 q = gluon_substrate_coeff q := by
  unfold gluon_substrate_coeff_general gluon_substrate_coeff
  rfl

end QOU.WedderburnMass
