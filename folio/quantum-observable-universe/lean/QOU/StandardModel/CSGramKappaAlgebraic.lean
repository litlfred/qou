import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation

/-!
# The Chern–Simons Gram ratio `κ` is algebraic: `π` cancels

Bean `qou-wkgp`. `def:cs-gram-determinant-ratio` defines `κ = det G^cl_CS / det G^q_CS`, the
ratio of the classical and `q`-deformed `2 × 2` Chern–Simons Gram matrices of the force-carrier
pair `T(2,9)`, `T(3,5)`. The entries (`fine-structure-data.md`,
`computations/meson_em_sinh_closed_form.py`) are, for a torus knot `T(m, n)`,

    G_ii = π²(m²−1)(n²−1)/(12 m n) + π² s²/(m n)²,   s = (m−1)(n−1)  (self-linking),
    G_12 = π² ℓ² / (m₁ n₁ m₂ n₂),                    ℓ = m₁ n₂ − m₂ n₁   (linking),

with the classical matrix at the integers `(2, 9, 3, 5)` and the `q`-deformed one at the quantum
integers `([2], [9], [3], [5])`. (The producer writes `|ℓ|`; only `ℓ²` enters, so the sign is
irrelevant.)

**Every entry is `π²` times a rational function of `(m₁, n₁, m₂, n₂)`.** So `π⁴` factors out
of both determinants and cancels in the ratio:

* `gram_eq_smul`: `G = p • A` with `p = π²` and `A` rational in the inputs.
* `kappa_p_free`: `det(p • A_cl) / det(p • A_q) = det A_cl / det A_q` for any `p ≠ 0`.
* `detA_classical`: `det A(2, 9, 3, 5) = 605/972`, so `det G^cl = (605/972) π⁴`, matching the
  recorded `60.630144…`.
* `kappa_eq`: `κ = (605/972) / det A([2], [9], [3], [5])`.

So `κ` is an **algebraic** quantity, a rational function of `q` evaluated at `q₀`. It needs no
`π`, no transcendental input and no Plancherel identification to be defined. The open question
of bean `qou-wkgp` is now only *why* this rational function has the value it has, i.e. whether
it equals some Hecke/Plancherel product. That identification remains unproved, and the fallback
for stating it is a hypothesis class at common `n = 3` with integer `S₃`-character exponents.

Algebraic over any field; the `p` here is `π²` in the application. No measured values.
-/

namespace QOU.StandardModel.CSGramKappa

open Matrix

variable {K : Type*} [Field K]

/-- The `π`-free part of the CS Gram matrix of a pair of torus knots `T(m₁,n₁)`, `T(m₂,n₂)`. -/
def gramA (m₁ n₁ m₂ n₂ : K) : Matrix (Fin 2) (Fin 2) K :=
  !![(m₁ ^ 2 - 1) * (n₁ ^ 2 - 1) / (12 * m₁ * n₁) + ((m₁ - 1) * (n₁ - 1)) ^ 2 / (m₁ * n₁) ^ 2,
     (m₁ * n₂ - m₂ * n₁) ^ 2 / (m₁ * n₁ * m₂ * n₂);
     (m₁ * n₂ - m₂ * n₁) ^ 2 / (m₁ * n₁ * m₂ * n₂),
     (m₂ ^ 2 - 1) * (n₂ ^ 2 - 1) / (12 * m₂ * n₂) + ((m₂ - 1) * (n₂ - 1)) ^ 2 / (m₂ * n₂) ^ 2]

/-- The CS Gram matrix as the corpus defines it, with `p = π²`. -/
def gramCS (p m₁ n₁ m₂ n₂ : K) : Matrix (Fin 2) (Fin 2) K :=
  !![p * (m₁ ^ 2 - 1) * (n₁ ^ 2 - 1) / (12 * m₁ * n₁) + p * ((m₁ - 1) * (n₁ - 1)) ^ 2 / (m₁ * n₁) ^ 2,
     p * (m₁ * n₂ - m₂ * n₁) ^ 2 / (m₁ * n₁ * m₂ * n₂);
     p * (m₁ * n₂ - m₂ * n₁) ^ 2 / (m₁ * n₁ * m₂ * n₂),
     p * (m₂ ^ 2 - 1) * (n₂ ^ 2 - 1) / (12 * m₂ * n₂) + p * ((m₂ - 1) * (n₂ - 1)) ^ 2 / (m₂ * n₂) ^ 2]

/-- **`G = π² · A`.** -/
theorem gram_eq_smul (p m₁ n₁ m₂ n₂ : K) : gramCS p m₁ n₁ m₂ n₂ = p • gramA m₁ n₁ m₂ n₂ := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [gramCS, gramA] <;> ring

/-- **`π` cancels in the ratio.** -/
theorem kappa_p_free (p a₁ b₁ c₁ d₁ a₂ b₂ c₂ d₂ : K) (hp : p ≠ 0) :
    (gramCS p a₁ b₁ c₁ d₁).det / (gramCS p a₂ b₂ c₂ d₂).det =
      (gramA a₁ b₁ c₁ d₁).det / (gramA a₂ b₂ c₂ d₂).det := by
  rw [gram_eq_smul, gram_eq_smul, det_smul, det_smul, Fintype.card_fin]
  have hp2 : p ^ 2 ≠ 0 := pow_ne_zero 2 hp
  rw [mul_div_mul_left _ _ hp2]

/-- **The classical determinant:** `det A(2, 9, 3, 5) = 605/972`. -/
theorem detA_classical [CharZero K] : (gramA (2 : K) 9 3 5).det = 605 / 972 := by
  rw [det_fin_two]
  simp [gramA]
  norm_num

/-- **`κ` as a rational function of the quantum integers.** With `p = π² ≠ 0`, the CS Gram
ratio of `def:cs-gram-determinant-ratio` is `(605/972) / det A([2], [9], [3], [5])`. -/
theorem kappa_eq [CharZero K] (p q2 q9 q3 q5 : K) (hp : p ≠ 0) :
    (gramCS p 2 9 3 5).det / (gramCS p q2 q9 q3 q5).det =
      (605 / 972) / (gramA q2 q9 q3 q5).det := by
  rw [kappa_p_free p _ _ _ _ _ _ _ _ hp, detA_classical]

end QOU.StandardModel.CSGramKappa
