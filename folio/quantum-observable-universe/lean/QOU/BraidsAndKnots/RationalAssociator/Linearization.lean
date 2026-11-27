import Mathlib.RingTheory.TwoSidedIdeal.Basic
import Mathlib.Tactic.NoncommRing

/-!
# Linearization of the associator equations in the top degree

Bean `qou-3fdg` (stage 2b of the rational-associator plan, under epic `qou-dk7p`).

Bar-Natan (*On associators and the Grothendieck–Teichmüller group I*, 1998, §4) extends an
associator one degree at a time: `Φ_m = Φ_{m-1} + φ_m` with `φ_m` homogeneous of degree `m`,
working modulo degree `m + 1`. The equations for `φ_m` are then "non-homogeneous linear, with a
constant term determined algebraically from `Φ_{m-1}`". This file proves that statement
abstractly.

Setting: a ring `R`, a two-sided ideal `I` (the augmentation ideal: positive degree), and an
additive subgroup `J ⊆ I` (the top degree `m`, inside the algebra truncated at degree `m + 1`)
with `J · I = I · J = 0`. Every factor of an associator equation has the form `a + x` with
`a ≡ 1 (mod I)` (the value of `Φ_{m-1}` or of a fixed exponential) and `x ∈ J` (the value of
`φ_m`, or `0`). Then

  `(a + x)(b + y) = ab + (x + y)`,

so a product of perturbed factors is the unperturbed product plus the **sum** of the
perturbations. Consequently (`pentagon_linear`, `hexagon_linear`, `inversion_linear`) each
equation for `Φ_{m-1} + φ_m` equals the equation for `Φ_{m-1}` plus a `ℤ`-linear expression in
the substituted copies of `φ_m`, the linearized operator at `Φ = 1`, which does not depend on
`Φ_{m-1}`. No analysis, limit or numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

variable {R : Type*} [Ring R] (I : TwoSidedIdeal R) (J : AddSubgroup R)

/-- `J` is a top-degree layer for `I`: `J ⊆ I` and `J` is annihilated by `I` on both sides. -/
structure IsTop : Prop where
  le : ∀ x ∈ J, x ∈ I
  mul_left : ∀ x ∈ J, ∀ z ∈ I, x * z = 0
  mul_right : ∀ x ∈ J, ∀ z ∈ I, z * x = 0

variable {I J}

theorem one_sub_mul_mem {a b : R} (ha : a - 1 ∈ I) (hb : b - 1 ∈ I) : a * b - 1 ∈ I := by
  have : a * b - 1 = (a - 1) * (b - 1) + (a - 1) + (b - 1) := by noncomm_ring
  rw [this]
  exact I.add_mem (I.add_mem (I.mul_mem_right _ _ ha) ha) hb

/-- **First-order perturbation.** `(a + x)(b + y) = ab + (x + y)`. -/
theorem mul_perturb (hJ : IsTop I J) {a b x y : R} (ha : a - 1 ∈ I) (hb : b - 1 ∈ I)
    (hx : x ∈ J) (hy : y ∈ J) : (a + x) * (b + y) = a * b + (x + y) := by
  have h1 : a * y = y := by
    have := hJ.mul_right y hy (a - 1) ha
    rw [sub_mul, one_mul, sub_eq_zero] at this; exact this
  have h2 : x * b = x := by
    have := hJ.mul_left x hx (b - 1) hb
    rw [mul_sub, mul_one, sub_eq_zero] at this; exact this
  have h3 : x * y = 0 := hJ.mul_left x hx y (hJ.le y hy)
  rw [mul_add, add_mul, add_mul, h1, h2, h3]
  abel

/-- A perturbed factor times an unperturbed one: `(a + x) e = ae + x`. -/
theorem mul_perturb_unit (hJ : IsTop I J) {a e x : R} (ha : a - 1 ∈ I) (he : e - 1 ∈ I)
    (hx : x ∈ J) : (a + x) * e = a * e + x := by
  simpa using mul_perturb hJ ha he hx J.zero_mem

/-- Three factors: `(a + x)(b + y)(c + z) = abc + (x + y + z)`. -/
theorem mul_perturb₃ (hJ : IsTop I J) {a b c x y z : R} (ha : a - 1 ∈ I) (hb : b - 1 ∈ I)
    (hc : c - 1 ∈ I) (hx : x ∈ J) (hy : y ∈ J) (hz : z ∈ J) :
    (a + x) * (b + y) * (c + z) = a * b * c + (x + y + z) := by
  rw [mul_perturb hJ ha hb hx hy,
    mul_perturb hJ (one_sub_mul_mem ha hb) hc (J.add_mem hx hy) hz]

/-- **Linearized pentagon.** For factors `aᵢ + xᵢ` (`aᵢ` the substituted lower-degree part,
`xᵢ` the substituted top-degree part), the pentagon defect
`(a₄+x₄)(a₂+x₂)(a₀+x₀) − (a₁+x₁)(a₃+x₃)` equals the defect of the `aᵢ` plus
`x₄ + x₂ + x₀ − x₁ − x₃`. -/
theorem pentagon_linear (hJ : IsTop I J) {a0 a1 a2 a3 a4 x0 x1 x2 x3 x4 : R}
    (h0 : a0 - 1 ∈ I) (h1 : a1 - 1 ∈ I) (h2 : a2 - 1 ∈ I) (h3 : a3 - 1 ∈ I) (h4 : a4 - 1 ∈ I)
    (k0 : x0 ∈ J) (k1 : x1 ∈ J) (k2 : x2 ∈ J) (k3 : x3 ∈ J) (k4 : x4 ∈ J) :
    (a4 + x4) * (a2 + x2) * (a0 + x0) - (a1 + x1) * (a3 + x3) =
      (a4 * a2 * a0 - a1 * a3) + (x4 + x2 + x0 - x1 - x3) := by
  rw [mul_perturb₃ hJ h4 h2 h0 k4 k2 k0, mul_perturb hJ h1 h3 k1 k3]
  abel

/-- **Linearized hexagon** (Drinfeld's form, inverse replaced via inversion):
`E = Φ₁ e₁ Φ₂ e₂ Φ₃` with fixed exponential factors `e₁, e₂ ≡ 1` and the left side `E`
unperturbed. The defect changes by `−(x₁ + x₂ + x₃)`. -/
theorem hexagon_linear (hJ : IsTop I J) {E a1 a2 a3 e1 e2 x1 x2 x3 : R}
    (h1 : a1 - 1 ∈ I) (h2 : a2 - 1 ∈ I) (h3 : a3 - 1 ∈ I) (he1 : e1 - 1 ∈ I) (he2 : e2 - 1 ∈ I)
    (k1 : x1 ∈ J) (k2 : x2 ∈ J) (k3 : x3 ∈ J) :
    E - (a1 + x1) * e1 * (a2 + x2) * e2 * (a3 + x3) =
      (E - a1 * e1 * a2 * e2 * a3) - (x1 + x2 + x3) := by
  have m1 := one_sub_mul_mem h1 he1
  have m2 := one_sub_mul_mem m1 h2
  have m3 := one_sub_mul_mem m2 he2
  rw [mul_perturb_unit hJ h1 he1 k1, mul_perturb hJ m1 h2 k1 k2,
    mul_perturb_unit hJ m2 he2 (J.add_mem k1 k2), mul_perturb hJ m3 h3 (J.add_mem k1 k2) k3]
  abel

/-- **Linearized inversion.** `(a + x)(b + y) − 1 = (ab − 1) + (x + y)`. -/
theorem inversion_linear (hJ : IsTop I J) {a b x y : R} (ha : a - 1 ∈ I) (hb : b - 1 ∈ I)
    (hx : x ∈ J) (hy : y ∈ J) : (a + x) * (b + y) - 1 = (a * b - 1) + (x + y) := by
  rw [mul_perturb hJ ha hb hx hy]; abel

end QOU.BraidsAndKnots.RationalAssociator
