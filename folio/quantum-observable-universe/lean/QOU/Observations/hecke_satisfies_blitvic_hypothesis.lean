import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Tactic
import QOU.SchurWeyl.MarkovTraceUnique

/-!
# QOU.Observations.hecke_satisfies_blitvic_hypothesis

Content block
[`prop:hecke-satisfies-blitvic-hypothesis`](../../../quantum-observable-universe/braids-and-knots/hecke-satisfies-blitvic-hypothesis.md).

**The centred Hecke generators do NOT satisfy Blitvić's pair-partition
hypothesis.** Blitvić's hypothesis needs every odd centred moment to vanish.
This file computes the third centred moment of a single generator under any
`K`-linear trace with `tr 1 = 1` and `tr σ = z`:

  `tr((σ − z)³) = (h² + 1) z + h − 3 h z² − 3 z + 2 z³`,  `h = q − q⁻¹`,

and shows it is `−357/250 ≠ 0` at `q = 2` under convention D
(`z = q³/(q² + 1)`). Every Markov trace on the Hecke tower of this repo
(`QOU.SchurWeyl.HeckeCoset.MarkovTraceFamily`) restricts to such a trace on
`H₁(q)`, so the conclusion applies to the Jones–Markov trace itself.

An earlier version of this file derived odd vanishing from a conditional class
(a "Wick recursion") and from a Markov axiom `tr(x σₙ) = z tr(x)` stated for
**all** `x` and `n`. Both are refuted by the computation here: the Markov
axiom for all `x` would force `tr(σ²) = z²`, while the quadratic relation gives
`tr(σ²) = h z + 1`.

The centred variance `tr((σ − z)²) = h z + 1 − z²` is also proved.

Base ring (§7c): a generic field `K`; `ℚ` only for the evaluation at `q = 2`.
Sorry-free, no axioms beyond Mathlib's.

## References

- [blitvic2012] Blitvić, *The (q,t)-Gaussian process*, J. Funct. Anal.
  DOI:10.1016/j.jfa.2012.08.006.
-/

namespace QOU.Observations

open Polynomial

/-- A Hecke generator `s` with `s² = h•s + 1` and a `K`-linear trace with
`tr 1 = 1`, `tr s = z`. -/
structure HeckeGenTrace (K A : Type*) [Field K] [Ring A] [Algebra K A] where
  s : A
  h : K
  z : K
  tr : A →ₗ[K] K
  quad : s * s = h • s + 1
  tr_one : tr 1 = 1
  tr_s : tr s = z

namespace HeckeGenTrace

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] (H : HeckeGenTrace K A)

/-- The centred generator `s − z•1`. -/
def centred : A := H.s - algebraMap K A H.z

theorem aeval_p : aeval H.s (X ^ 2 - C H.h * X - 1 : K[X]) = 0 := by
  simp only [map_sub, map_mul, aeval_X, aeval_C, map_one, pow_two]
  rw [H.quad, Algebra.smul_def]; abel

theorem tr_aeval_linear (a b : K) : H.tr (aeval H.s (C a * X + C b)) = a * H.z + b := by
  simp only [map_add, map_mul, aeval_X, aeval_C, Algebra.algebraMap_eq_smul_one,
    smul_mul_assoc, one_mul, map_smul, H.tr_s, H.tr_one, smul_eq_mul, mul_one]

theorem centred_eq : H.centred = aeval H.s (X - C H.z) := by
  simp [centred]

/-- **Centred variance.** `tr((s − z)²) = h z + 1 − z²`. -/
theorem centred_sq : H.tr (H.centred * H.centred) = H.h * H.z + 1 - H.z ^ 2 := by
  have key : (X - C H.z) * (X - C H.z) =
      (X ^ 2 - C H.h * X - 1 : K[X]) + (C (H.h - 2 * H.z) * X + C (1 + H.z ^ 2)) := by
    simp only [map_sub, map_mul, map_add, map_pow, map_one, map_ofNat]; ring
  rw [centred_eq, ← map_mul, key, map_add, H.aeval_p, zero_add, H.tr_aeval_linear]
  ring

/-- **Centred third moment.**
`tr((s − z)³) = (h² + 1) z + h − 3 h z² − 3 z + 2 z³`. -/
theorem centred_cube :
    H.tr (H.centred * H.centred * H.centred)
      = (H.h ^ 2 + 1) * H.z + H.h - 3 * H.h * H.z ^ 2 - 3 * H.z + 2 * H.z ^ 3 := by
  have key : (X - C H.z) * (X - C H.z) * (X - C H.z) =
      (X + C H.h - C (3 * H.z)) * (X ^ 2 - C H.h * X - 1 : K[X])
        + (C (H.h ^ 2 + 1 - 3 * H.z * H.h + 3 * H.z ^ 2) * X
            + C (H.h - 3 * H.z - H.z ^ 3)) := by
    simp only [map_sub, map_mul, map_add, map_pow, map_one, map_ofNat]; ring
  rw [centred_eq, ← map_mul, ← map_mul, key, map_add, map_mul, H.aeval_p, mul_zero,
    zero_add, H.tr_aeval_linear]
  ring

end HeckeGenTrace

/-- At `q = 2` (so `h = 3/2`, and under convention D `z = q³/(q²+1) = 8/5`) the
centred third moment is `−357/250 ≠ 0`. -/
theorem centred_cube_at_two (A : Type*) [Ring A] [Algebra ℚ A] (H : HeckeGenTrace ℚ A)
    (hh : H.h = 2 - 2⁻¹) (hz : H.z = 2 ^ 3 / (2 ^ 2 + 1)) :
    H.tr (H.centred * H.centred * H.centred) = -357 / 250 := by
  rw [H.centred_cube, hh, hz]; norm_num


/-- `−357/250 ≠ 0`: the third centred moment at `q = 2` does not vanish, so the
odd-moment condition of Blitvić's hypothesis fails. -/
theorem centred_cube_at_two_ne_zero (A : Type*) [Ring A] [Algebra ℚ A]
    (H : HeckeGenTrace ℚ A) (hh : H.h = 2 - 2⁻¹) (hz : H.z = 2 ^ 3 / (2 ^ 2 + 1)) :
    H.tr (H.centred * H.centred * H.centred) ≠ 0 := by
  rw [centred_cube_at_two A H hh hz]; norm_num

open QOU.SchurWeyl in
/-- **Every Markov trace gives such a trace.** For a Markov trace family `T` on
the Hecke tower with parameter `z`, the generator `σ₀ ∈ H₁(q)` and `T.tr 1`
satisfy the hypotheses of `HeckeGenTrace` with `h = q − q⁻¹`. -/
noncomputable def ofMarkovTrace {K : Type*} [Field K] {q z : K} (hq : q ≠ 0)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ z) :
    HeckeGenTrace K (Hecke K q q⁻¹ 1) where
  s := Hecke.σ K q q⁻¹ 1 (Fin.last 0)
  h := q - q⁻¹
  z := z
  tr := T.tr 1
  quad := by
    rw [Hecke.σ_quadratic, mul_inv_cancel₀ hq, one_smul]
  tr_one := T.tr_one 1
  tr_s := T.param_eq

open QOU.SchurWeyl in
/-- **The Jones–Markov trace at `q = 2`, convention D, has a nonzero third
centred moment.** -/
theorem markovTrace_centred_cube_ne_zero
    (T : HeckeCoset.MarkovTraceFamily ℚ 2 2⁻¹ (2 ^ 3 / (2 ^ 2 + 1))) :
    (ofMarkovTrace (by norm_num) T).tr
      ((ofMarkovTrace (by norm_num) T).centred * (ofMarkovTrace (by norm_num) T).centred
        * (ofMarkovTrace (by norm_num) T).centred) ≠ 0 :=
  centred_cube_at_two_ne_zero _ _ rfl rfl

end QOU.Observations
