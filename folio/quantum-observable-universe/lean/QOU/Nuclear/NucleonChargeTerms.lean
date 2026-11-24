import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Can a Coulomb term supply the rest of m_n − m_p? (owner "2y")

Two charge assignments are in the corpus.

* Mirror-odd (the crossing-orientation mechanism of `def:down-quark`): `Q(d) = −Q(u)`.
  `mirror_charges`: then `Q(n) = −Q(p)`; `mirror_neutral_forces_zero`: a neutral neutron forces
  `Q(u) = 0`. `mirror_even_energy_cancels`: any energy that depends on the charge only through an
  even function (for example `c·Q²`) is the same for p and n, so it adds nothing to `m_n − m_p`.
* Adopted Standard-Model charges, `Q(p) = 1`, `Q(n) = 0`: `adopted_selfenergy_sign`: a self-energy
  `c·Q²` with `c > 0` makes `E_n − E_p = −c < 0`. It lowers `m_n − m_p`, so it cannot fill a gap
  where the model value is already below the comparison value.

No measured value appears here.
-/

namespace QOU.QBeta.NucleonChargeTerms

section Generic

variable {R : Type*} [CommRing R]

theorem mirror_charges (a : R) :
    (a + a + -a) = a ∧ (a + -a + -a) = -a := by
  constructor <;> ring

theorem mirror_neutral_forces_zero (a : R) (h : a + -a + -a = 0) : a = 0 := by
  linear_combination -h

theorem mirror_even_energy_cancels (f : R → R) (heven : ∀ x, f (-x) = f x) (a : R) :
    f (a + -a + -a) - f (a + a + -a) = 0 := by
  have h1 : a + -a + -a = -a := by ring
  have h2 : a + a + -a = a := by ring
  rw [h1, h2, heven, sub_self]

end Generic

theorem adopted_selfenergy_sign (c : ℝ) (hc : 0 < c) :
    c * (0 : ℝ) ^ 2 - c * (1 : ℝ) ^ 2 < 0 := by
  nlinarith

end QOU.QBeta.NucleonChargeTerms
