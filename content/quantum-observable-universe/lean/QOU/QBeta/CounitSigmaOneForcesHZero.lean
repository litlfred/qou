import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# The `σ ↦ 1` functional is not an algebra map unless `h = 0`

This is the structural core of the `qou-99qc` fork. Two different linear
functionals are both called `ε` in the corpus:

* the **augmentation** `σᵢ ↦ q`, which IS an algebra homomorphism (the
  one-dimensional `λ = (n)` representation), and is what
  `qbeta_epsnpq_colour_weighted_exclusion_probe.py` uses — it evaluates a word
  as a PRODUCT of per-letter values, which is legitimate only for an algebra
  map;
* the **coordinate sum** `σᵢ ↦ 1`, which is what
  `QOU.Interactions.QBetaCounitTrace.epsNP` computes ("weights every basis
  element by 1"), and which produces `epsNPq = h²/2 − h`.

The lemma below shows these cannot be the same functional at `h ≠ 0`: any
algebra map sending `σ` to `1` forces `h = 0`. So `epsNPq` is not a value of
the multiplicative `ε`, and an exclusion theorem about the multiplicative `ε`
does not constrain it.

The argument is one line and needs no Hecke algebra: it is just the defining
relation `σ² = hσ + 1` pushed through a multiplicative map.
-/

namespace QOU.QBeta.CounitSigmaOne

variable {R : Type*} [CommRing R]

/-- **The obstruction.** If `s` satisfies the Hecke relation `s² = h·s + 1`
    and a multiplicative, unital map sends `s ↦ 1`, then `h = 0`.

    Stated on the image side so no algebra structure is needed: `v` is the
    image of `s`, and multiplicativity gives `v² = h·v + 1` with `v = 1`. -/
theorem h_eq_zero_of_image_one (h v : R) (hv : v = 1)
    (hrel : v ^ 2 = h * v + 1) : h = 0 := by
  subst hv
  have h1 : (1 : R) = h + 1 := by simpa using hrel
  have h2 : h + 1 = 0 + 1 := by rw [zero_add]; exact h1.symm
  exact add_right_cancel h2

/-- The same statement in the contrapositive form used downstream: when
    `h ≠ 0`, no unital multiplicative map can send a Hecke generator to `1`. -/
theorem no_sigma_to_one_of_h_ne_zero (h v : R) (hh : h ≠ 0)
    (hrel : v ^ 2 = h * v + 1) : v ≠ 1 := by
  intro hv
  exact hh (h_eq_zero_of_image_one h v hv hrel)

/-- **The genuine augmentation checks out**: `σ ↦ q` does satisfy the Hecke
    relation when `h = q − q⁻¹`, i.e. `q² = (q − q⁻¹)·q + 1` — here in
    division-free form `q * q = (q * q - 1) + 1`. -/
theorem sigma_to_q_satisfies_hecke (q : R) :
    q ^ 2 = (q ^ 2 - 1) + 1 := by ring

end QOU.QBeta.CounitSigmaOne
