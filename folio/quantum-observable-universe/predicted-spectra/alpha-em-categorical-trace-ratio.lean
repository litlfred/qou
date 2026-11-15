/-
Algebraic identity:
  α_EM = h² / [q · δ_q(T_{2,9}) · δ_q(T_{3,5})]

LaTeX label: `prop:alpha-em-categorical-trace-ratio`
Computational verification (10⁻¹² precision at q_0):
  computations/delta-q-decoration.witness.json

Base ring (AGENTS.md §7c). The whole identity is Laurent in `q, q⁻¹`:
the substrate modulus is carried as a **unit** `q : Rˣ` over a generic
`{R : Type*} [CommRing R]`, so `↑q⁻¹` is a `Units` coercion, not a ring
inverse. Two consequences:

* `q_int` is now the **division-free** symmetric q-integer
  `[n]_q = ∑_{i<n} qⁱ · q⁻⁽ⁿ⁻¹⁻ⁱ⁾ = q^(n-1) + q^(n-3) + ⋯ + q^(−(n−1))`.
  Lemma `q_int_mul_h_skein` proves it satisfies the previous defining
  relation `[n]_q · h = qⁿ − q⁻ⁿ`, so nothing changes wherever `h ≠ 0`
  (which is where the old quotient definition was meaningful at all),
  and the new definition is additionally total.
* The identity itself is stated in the **R[h] multiplicative form**
  `α · (q · [9]_q · [10]_q) = 1  ↔  α · (q · δ₉ · δ₁₀) = h²`
  (`alpha_em_relation_iff`), which holds over any commutative ring in
  which `h` is a unit — no field, no `field_simp`.

A field appears only in the `RatioForm` section, where α_EM is written
as an actual quotient, as the narrative does. That presentation needs
division; the mathematics does not.
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.ArchimedeanUniverse

variable {R : Type*} [CommRing R]

/-- The skein parameter h := q − q⁻¹ in the substrate ring R. -/
def h_skein (q : Rˣ) : R := (q : R) - (↑q⁻¹ : R)

/-- The symmetric q-deformed integer

  `[n]_q = q^(n-1) + q^(n-3) + ⋯ + q^(−(n−1)) = ∑_{i<n} qⁱ · q^(−(n−1−i))`,

written division-free as a Laurent polynomial in `q, q⁻¹`. It satisfies
`[n]_q · (q − q⁻¹) = qⁿ − q⁻ⁿ` (`q_int_mul_h_skein`), which was the
previous *definition* — a quotient, and hence meaningful only when
`h ≠ 0`. -/
def q_int (q : Rˣ) (n : ℕ) : R :=
  ∑ i ∈ Finset.range n, (q : R) ^ i * (↑q⁻¹ : R) ^ (n - 1 - i)

/-- The categorical trace δ_q(T_{2, n}) for the (2, n)-torus knot in
the H_2(q) representation, summing the contributions from the two
irreducible Hecke representations V_(2), V_(1,1) at eigenvalues
q^n and (-q⁻¹)^n. For n odd this simplifies to qⁿ - q⁻ⁿ.
-/
def delta_q_T_2_n (q : Rˣ) (n : ℕ) : R := (q : R) ^ n - (↑q⁻¹ : R) ^ n

/-- The value **assigned** to δ_q(T_{3,5}): `q^10 − q^-10 = h · [10]_q`.

**This is not the trace sum (corrected 2026-11-15).** Summing the actions
of `(σ₁σ₂)^5` over `V_(3)`, `V_(2,1)`, `V_(1,1,1)` gives
`q^10 − 1 + q^-10`, because on the 2-dimensional `V_(2,1)` the element
`σ₁σ₂` has eigenvalues `ω, ω²` (`ω³ = 1`) and its fifth power has trace −1.
So the identities below hold for this assigned value, not for a derived one.
-/
def delta_q_T_3_5 (q : Rˣ) : R := delta_q_T_2_n q 10

/-- **The defining relation of the symmetric q-integer**, division-free:
`[n]_q · h = qⁿ − q⁻ⁿ = δ_q(T_{2,n})`. This is `geom_sum₂_mul`, i.e.
the telescoping identity `(∑_{i<n} xⁱ y^{n−1−i})(x − y) = xⁿ − yⁿ`,
which is pure commutative-ring algebra. -/
theorem q_int_mul_h_skein (q : Rˣ) (n : ℕ) :
    q_int q n * h_skein q = delta_q_T_2_n q n :=
  geom_sum₂_mul (q : R) (↑q⁻¹ : R) n

/-- **The structural core of the α_EM trace-ratio identity**, stated
division-free over an arbitrary commutative ring:

  `δ_q(T_{2,9}) · δ_q(T_{3,5}) = h² · ([9]_q · [10]_q)`.

Every factor of `h` in the categorical (δ) layer is accounted for by
one q-integer in the Bring-complexity layer; the ratio identity below
is nothing more than this, divided through. -/
theorem delta_mul_delta_eq_h_sq_mul_q_int (q : Rˣ) :
    delta_q_T_2_n q 9 * delta_q_T_3_5 q
      = (h_skein q) ^ 2 * (q_int q 9 * q_int q 10) := by
  rw [delta_q_T_3_5, ← q_int_mul_h_skein q 9, ← q_int_mul_h_skein q 10]
  ring

/-- **THE α_EM CATEGORICAL-TRACE-RATIO IDENTITY, division-free (R[h] form).**

Rather than dividing, characterise α_EM by the multiplicative relation
it satisfies. `α` is the inverse of the Bring force-carrier complexity
iff it satisfies the δ-layer relation with an `h²` on the right:

  `α · (q · [9]_q · [10]_q) = 1  ↔  α · (q · δ_q(T_{2,9}) · δ_q(T_{3,5})) = h²`.

Holds over any commutative ring in which the skein parameter `h` is a
unit. The forward direction needs no hypothesis at all; `h` invertible
is used only to cancel `h²` in the reverse direction. -/
theorem alpha_em_relation_iff (q : Rˣ) (α : R) (hh : IsUnit (h_skein q)) :
    α * ((q : R) * q_int q 9 * q_int q 10) = 1
      ↔ α * ((q : R) * delta_q_T_2_n q 9 * delta_q_T_3_5 q)
          = (h_skein q) ^ 2 := by
  rw [delta_q_T_3_5, ← q_int_mul_h_skein q 9, ← q_int_mul_h_skein q 10]
  constructor
  · intro hα
    linear_combination (h_skein q) ^ 2 * hα
  · intro hα
    refine (hh.pow 2).mul_left_cancel ?_
    rw [mul_one]
    linear_combination hα

/-! ## Ratio presentation (a field is needed only to divide)

The narrative writes α_EM as a quotient. A quotient needs division, so
this section — and only this section — is over a field. Both
definitions and the identity are read off from
`delta_mul_delta_eq_h_sq_mul_q_int` above. -/

section RatioForm

variable {K : Type*} [Field K]

/-- The bare formula for α_EM as the inverse of the Bring force-
carrier complexity (per prop:em-coupling-projection):
  α_EM = 1 / (q · [9]_q · [10]_q).
-/
noncomputable def alpha_em_bare (q : Kˣ) : K :=
  1 / ((q : K) * q_int q 9 * q_int q 10)

/-- The categorical-trace-ratio expression for α_EM via the δ_q layer:
  α_EM_via_delta_q := h² / (q · δ_q(T_{2,9}) · δ_q(T_{3,5})).

This is the round-14 algebraic refactoring of α_EM into the
q-dimension layer.
-/
noncomputable def alpha_em_via_delta_q (q : Kˣ) : K :=
  (h_skein q) ^ 2 / ((q : K) * delta_q_T_2_n q 9 * delta_q_T_3_5 q)

/-- The categorical-trace-ratio identity:
  α_EM = h² / (q · δ_q(T_{2,9}) · δ_q(T_{3,5}))

The proof is direct algebraic substitution in R = ℤ[q^±1, h⁻¹]:

  δ_q(T_{2,9}) = q⁹ - q⁻⁹  = h · [9]_q   (q_int_mul_h_skein)
  δ_q(T_{3,5}) = q¹⁰ - q⁻¹⁰ = h · [10]_q (q_int_mul_h_skein)

  Therefore:
  h² / (q · δ_q(T_{2,9}) · δ_q(T_{3,5}))
   = h² / (q · (h · [9]_q) · (h · [10]_q))
   = h² / (q · h² · [9]_q · [10]_q)
   = 1 / (q · [9]_q · [10]_q)
   = α_EM     (by definition)

All of that is the single division-free identity
`delta_mul_delta_eq_h_sq_mul_q_int`; only the final division into a
quotient needs the field.

-- Ref: [leitner2026] §round-12, §round-14 of conj:e-hartree-categorical-derivation
-- Ref: [leitner2026] prop:em-coupling-projection (the bare 1/α formula)
-- Ref: [leitner2026] def:delta-q-decoration
-/
theorem alpha_em_categorical_trace_ratio (q : Kˣ)
    (hq9 : delta_q_T_2_n q 9 ≠ 0)
    (hq10 : delta_q_T_3_5 q ≠ 0) :
    alpha_em_bare q = alpha_em_via_delta_q q := by
  have h9 : q_int q 9 ≠ 0 := by
    intro h0
    exact hq9 (by rw [← q_int_mul_h_skein q 9, h0, zero_mul])
  have h10 : q_int q 10 ≠ 0 := by
    intro h0
    exact hq10 (by rw [delta_q_T_3_5, ← q_int_mul_h_skein q 10, h0, zero_mul])
  have hden1 : (q : K) * q_int q 9 * q_int q 10 ≠ 0 :=
    mul_ne_zero (mul_ne_zero q.ne_zero h9) h10
  have hden2 : (q : K) * delta_q_T_2_n q 9 * delta_q_T_3_5 q ≠ 0 :=
    mul_ne_zero (mul_ne_zero q.ne_zero hq9) hq10
  unfold alpha_em_bare alpha_em_via_delta_q
  rw [div_eq_div_iff hden1 hden2]
  linear_combination (q : K) * delta_mul_delta_eq_h_sq_mul_q_int q

end RatioForm

end QOU.ArchimedeanUniverse
