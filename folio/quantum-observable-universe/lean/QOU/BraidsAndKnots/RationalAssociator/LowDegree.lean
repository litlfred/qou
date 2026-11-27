import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.Module

/-!
# A rational Drinfeld associator modulo degree 3

Bean `qou-3fdg` (stage 1 of the rational-associator plan, under epic `qou-dk7p`).

Drinfeld's associator equations for `φ = φ(A, B)` are, with the Drinfeld–Kohno generators
`tᵢⱼ` of `𝔱₃` and `𝔱₄` (Drinfeld 1990; Bar-Natan 1998, *On associators and the
Grothendieck–Teichmüller group I*):

* inversion: `φ(A, B) · φ(B, A) = 1`;
* pentagon (in `Û(𝔱₄)`):
  `φ(t₁₂, t₂₃ + t₂₄) · φ(t₁₃ + t₂₃, t₃₄) = φ(t₂₃, t₃₄) · φ(t₁₂ + t₁₃, t₂₄ + t₃₄) · φ(t₁₂, t₂₃)`;
* hexagon (in `Û(𝔱₃)`, with `μ = 1` and the inverse rewritten by inversion):
  `e^{(t₁₃ + t₂₃)/2} = φ(t₁₃, t₁₂) · e^{t₁₃/2} · φ(t₂₃, t₁₃) · e^{t₂₃/2} · φ(t₁₂, t₂₃)`.

This file treats these equations **modulo degree 3**. Instead of building the quotient
`Û(𝔱ₙ)/(degree ≥ 3)` we state each result in an arbitrary `ℚ`-algebra `R` holding elements
`tᵢⱼ` that satisfy the Drinfeld–Kohno relations the equation needs, and in which every word of
length three in the `tᵢⱼ` vanishes (`Trunc3`). The universal such algebra is
`U(𝔱ₙ)/(degree ≥ 3)`, so these statements are the degree-≤ 2 associator equations. They hold
verbatim in every representation that satisfies the hypotheses.

Results, all over `ℚ` and sorry-free:

* `inversion`, `pentagon`: `φ_c = 1 + c·[A, B]` satisfies inversion and the pentagon modulo
  degree 3 for **every** `c ∈ ℚ`. The pentagon uses only the two "disjoint" relations
  `[t₁₂, t₃₄] = [t₁₃, t₂₄] = 0`.
* `hexagon_iff`: the hexagon modulo degree 3 holds **iff** `(c − 1/24)·[t₁₂, t₂₃] = 0`. So
  `c = 1/24` is forced whenever `[t₁₂, t₂₃] ≠ 0`, which is the case in `U(𝔱₃)`.
* `hexagon`: hence `φ = 1 + (1/24)[A, B]` is a rational associator modulo degree 3.

`φ_c` is group-like modulo degree 3: it is `exp(c·[A, B])` truncated, and `c·[A, B]` is a Lie
element. No analysis, limit or numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Every word of length three in elements of `S` vanishes: the algebra is truncated at
degree 3 with respect to `S`. -/
def Trunc3 (S : Set R) : Prop := ∀ {x y z : R}, x ∈ S → y ∈ S → z ∈ S → x * y * z = 0

/-- The candidate associator modulo degree 3, `φ_c(a, b) = 1 + c·[a, b]`. -/
def phi (c : ℚ) (a b : R) : R := 1 + c • (a * b - b * a)

/-- The exponential truncated at degree 3: `exp(x) = 1 + x + x²/2`, applied to `x/2`. -/
def expHalf (x : R) : R := 1 + (1 / 2 : ℚ) • x + (1 / 8 : ℚ) • (x * x)

/-- Inversion `φ_c(a, b) · φ_c(b, a) = 1` modulo degree 3, for every `c`. -/
theorem inversion (c : ℚ) {a b : R} (h : Trunc3 ({a, b} : Set R)) :
    phi c a b * phi c b a = 1 := by
  unfold Trunc3 at h
  simp only [phi, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, ← mul_assoc, zero_mul, smul_zero, sub_zero, smul_sub,
    h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
  module

/-- The pentagon modulo degree 3 holds for every `c`. Only the disjoint Drinfeld–Kohno
relations `[t₁₂, t₃₄] = 0` and `[t₁₃, t₂₄] = 0` are used. -/
theorem pentagon (c : ℚ) {t12 t13 t14 t23 t24 t34 : R}
    (h : Trunc3 ({t12, t13, t14, t23, t24, t34} : Set R))
    (d1 : Commute t12 t34) (d2 : Commute t13 t24) :
    phi c t12 (t23 + t24) * phi c (t13 + t23) t34 =
      phi c t23 t34 * phi c (t12 + t13) (t24 + t34) * phi c t12 t23 := by
  unfold Trunc3 at h
  have e1 := d1.eq
  have e2 := d2.eq
  simp only [phi, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, ← mul_assoc, smul_zero, sub_zero, add_zero, smul_add, smul_sub,
    h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
  rw [e1, e2]
  module

/-- The hexagon modulo degree 3, reduced to one coefficient: given the `𝔱₃` relations
`[t₁₂, t₁₃ + t₂₃] = 0` and `[t₁₃, t₁₂ + t₂₃] = 0`, the hexagon for `φ_c` holds iff
`(c − 1/24)·[t₁₂, t₂₃] = 0`. -/
theorem hexagon_iff (c : ℚ) {t12 t13 t23 : R} (h : Trunc3 ({t12, t13, t23} : Set R))
    (c1 : Commute t12 (t13 + t23)) (c2 : Commute t13 (t12 + t23)) :
    expHalf (t13 + t23) =
        phi c t13 t12 * expHalf t13 * phi c t23 t13 * expHalf t23 * phi c t12 t23 ↔
      (c - 1 / 24) • (t12 * t23 - t23 * t12) = 0 := by
  unfold Trunc3 at h
  have e1 := c1.eq
  have e2 := c2.eq
  simp only [mul_add, add_mul] at e1 e2
  have e2' : t23 * t13 = t13 * t12 + t13 * t23 - t12 * t13 := by rw [e2]; simp
  have e1' : t12 * t13 = t13 * t12 + t23 * t12 - t12 * t23 := by rw [← e1]; simp
  have key :
      expHalf (t13 + t23) -
          phi c t13 t12 * expHalf t13 * phi c t23 t13 * expHalf t23 * phi c t12 t23 =
        (-3 : ℚ) • ((c - 1 / 24) • (t12 * t23 - t23 * t12)) := by
    simp only [phi, expHalf, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm,
      one_mul, mul_one, ← mul_assoc, smul_zero, sub_zero, add_zero, smul_add,
      smul_sub, h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
    rw [e2', e1']
    module
  rw [← sub_eq_zero, key, smul_eq_zero]
  norm_num

/-- **A rational associator modulo degree 3.** `φ = 1 + (1/24)[A, B]` satisfies the hexagon
modulo degree 3. Together with `inversion` and `pentagon` (at `c = 1/24`) it is a rational
Drinfeld associator modulo degree 3. -/
theorem hexagon {t12 t13 t23 : R} (h : Trunc3 ({t12, t13, t23} : Set R))
    (c1 : Commute t12 (t13 + t23)) (c2 : Commute t13 (t12 + t23)) :
    expHalf (t13 + t23) =
      phi (1 / 24) t13 t12 * expHalf t13 * phi (1 / 24) t23 t13 * expHalf t23 *
        phi (1 / 24) t12 t23 :=
  (hexagon_iff (1 / 24) h c1 c2).2 (by simp)

end QOU.BraidsAndKnots.RationalAssociator
