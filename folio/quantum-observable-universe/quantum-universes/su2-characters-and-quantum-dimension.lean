import Mathlib.Tactic

/-!
# `SU(2)` characters, and the quantum dimension as one evaluation of them

Sibling of `ex:su2-characters-and-quantum-dimension`. The character of the
`(n+1)`-dimensional irreducible representation `V_n` of `SU(2)`, as a function of
the torus variable `x`, is

    ch(V_n)(x) = xⁿ + xⁿ⁻² + ⋯ + x⁻ⁿ = x⁻ⁿ · (1 + x² + ⋯ + x²ⁿ).

Two evaluations of it are the two "dimensions" the paper distinguishes:

* at `x = 1`: the ordinary dimension `n + 1` (`su2Character_one`);
* at `x = q`: the quantum dimension `[n+1]_q = (q^{n+1} − q^{−n−1})/(q − q^{−1})`
  (`su2Character_mul_q_sub`), so `dim_q(V_1) = q + q⁻¹ = [2]_q`
  (`su2Character_fundamental`).

The character has `n + 1` terms; the quantum dimension is a single number obtained
from all of them. Over a generic field (§7c); the sums are finite geometric sums,
so the only hypothesis is `x ≠ 0`. No `sorry`.

-- Ref: [fulton-harris1991] https://doi.org/10.1007/978-1-4612-0979-9
-/

namespace QOU.Examples

open Finset

variable {K : Type*} [Field K]

/-- The character of `V_n` at `x`, written as `x⁻ⁿ · Σ_{i=0}^{n} x^{2i}`. -/
def su2Character (n : ℕ) (x : K) : K :=
  x⁻¹ ^ n * ∑ i ∈ range (n + 1), (x ^ 2) ^ i

/-- **At `x = 1` the character is the dimension `n + 1`.** -/
theorem su2Character_one (n : ℕ) : su2Character n (1 : K) = (n : K) + 1 := by
  simp [su2Character]

/-- **Multiplied by `q − q⁻¹`, the character at `q` is `q^{n+1} − q^{−(n+1)}`**: the
character is the symmetric quantum integer `[n+1]_q`. -/
theorem su2Character_mul_q_sub (n : ℕ) (q : K) (hq : q ≠ 0) :
    (q - q⁻¹) * su2Character n q = q ^ (n + 1) - q⁻¹ ^ (n + 1) := by
  unfold su2Character
  have hgeom : (∑ i ∈ range (n + 1), (q ^ 2) ^ i) * (q ^ 2 - 1) = (q ^ 2) ^ (n + 1) - 1 :=
    geom_sum_mul (q ^ 2) (n + 1)
  have hq2 : q - q⁻¹ = q⁻¹ * (q ^ 2 - 1) := by field_simp
  calc (q - q⁻¹) * (q⁻¹ ^ n * ∑ i ∈ range (n + 1), (q ^ 2) ^ i)
      = q⁻¹ ^ (n + 1) * ((∑ i ∈ range (n + 1), (q ^ 2) ^ i) * (q ^ 2 - 1)) := by
        rw [hq2, pow_succ]; ring
    _ = q⁻¹ ^ (n + 1) * ((q ^ 2) ^ (n + 1) - 1) := by rw [hgeom]
    _ = q ^ (n + 1) - q⁻¹ ^ (n + 1) := by
        rw [mul_sub, mul_one, ← pow_mul, inv_pow, ← div_eq_inv_mul]
        congr 1
        rw [div_eq_iff (pow_ne_zero _ hq)]
        ring

/-- **The fundamental representation: `dim_q(V_1) = q + q⁻¹ = [2]_q`.** -/
theorem su2Character_fundamental (q : K) (hq : q ≠ 0) : su2Character 1 q = q + q⁻¹ := by
  simp [su2Character, Finset.sum_range_succ]
  field_simp
  ring

/-- The trivial representation has character `1`. -/
theorem su2Character_zero (q : K) : su2Character 0 q = 1 := by
  simp [su2Character]

end QOU.Examples
