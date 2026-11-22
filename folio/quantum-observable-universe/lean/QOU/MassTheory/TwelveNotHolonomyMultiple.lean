import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# The 12 is not a `q`-independent multiple of the holonomy eigen-shift

Under the holonomy connection `∇ = hol − 1`, `hol = (σ₀σ₁⁻¹)³`, the nucleon eigen-shift `μ` has
`|μ|² = h⁴[3]_q` and block form `2 Re μ = −h⁴[3]_q`, `h = q − q⁻¹`
(`HolonomyConnectionSplit.two_add_c1_eq`). The n − p difference of `tr(𝒟²)` is
`2 q⁻¹ (1 − q⁻¹) h⁴ [3]_q` (sympy, `mn_d2_np_difference_probe.py`; not proved here).

Every one of these vanishes at `q = 1`. So no `κ` independent of `q` makes `κ · f(q) = 12` for all
`q` where `f` is defined, if the domain contains `q = 1`. This does **not** exclude a `q`-dependent
`κ`, nor a 12 coming from a term of ℒ outside this class.

Stated over a generic field `R` (§7c). No empirical input.
-/

namespace QOU.MassTheory.TwelveNotHolonomyMultiple

variable {R : Type*} [Field R]

/-- `h⁴[3]_q` with `h = q − q⁻¹`, `[3]_q = q² + 1 + q⁻²`: the modulus squared of `μ`. -/
def muNormSq (q : R) : R := (q - q⁻¹) ^ 4 * (q ^ 2 + 1 + q⁻¹ ^ 2)

/-- The n − p difference of `tr(𝒟²)`, in its closed form. -/
def deltaNP (q : R) : R := 2 * q⁻¹ * (1 - q⁻¹) * muNormSq q

theorem muNormSq_one : muNormSq (1 : R) = 0 := by simp [muNormSq]

theorem deltaNP_one : deltaNP (1 : R) = 0 := by simp [deltaNP, muNormSq_one]

/-- Any `f` vanishing at `1` is not a `q`-independent rescaling of a nonzero constant `c`
on a domain containing `1`. -/
theorem not_const_mul_of_vanish_one (f : R → R) (hf : f 1 = 0) (c : R) (hc : c ≠ 0)
    (S : Set R) (h1 : (1 : R) ∈ S) : ¬ ∃ κ : R, ∀ q ∈ S, κ * f q = c := by
  rintro ⟨κ, hκ⟩
  have := hκ 1 h1
  rw [hf, mul_zero] at this
  exact hc this.symm

theorem twelve_not_mul_muNormSq (h12 : (12 : R) ≠ 0) (S : Set R) (h1 : (1 : R) ∈ S) :
    ¬ ∃ κ : R, ∀ q ∈ S, κ * muNormSq q = 12 :=
  not_const_mul_of_vanish_one _ muNormSq_one 12 h12 S h1

theorem twelve_not_mul_deltaNP (h12 : (12 : R) ≠ 0) (S : Set R) (h1 : (1 : R) ∈ S) :
    ¬ ∃ κ : R, ∀ q ∈ S, κ * deltaNP q = 12 :=
  not_const_mul_of_vanish_one _ deltaNP_one 12 h12 S h1

end QOU.MassTheory.TwelveNotHolonomyMultiple
