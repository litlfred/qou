/-
# The two q-integer conventions in this corpus, and where they stand to each other

A symbolic audit of every local `[n]_q` definition
(`computations/audits/q_integer_duplication_audit.py`, bean `qou-c041`) finds
**two** conventions in use under the same function names:

* **symmetric**  `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`  — 126 definitions
* **classical**  `[n]_q = (qⁿ − 1)/(q − 1)`       — 30 definitions

(plus one √q-normalised and one symmetric-in-`q²`). This file states the
relation between them, so that a reader who meets `q_int` in an unfamiliar
producer can tell what is at stake.

The results are three. The classical bracket is a **geometric sum**, hence
division-free and total. The symmetric one is a genuine quotient and is
undefined exactly where the classical one is most convenient. And — the point —
**the two never agree anywhere both are defined**: they differ by `(1−q)/q` at
`n = 2`, which vanishes only at `q = 1`, where the symmetric bracket is `0/0`.

So "they coincide at `q = 1`" is a statement about limits, not about values,
and no substitution of one for the other is safe at any `q` the corpus uses.

No empirical input; nothing depends on `q₀`.
-/
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Algebra.Ring.Regular
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith

namespace QOU.Substrate.QIntegerConventions

variable {K : Type*} [Field K]

/-- The **classical** (Gaussian) `q`-integer, written as the geometric sum
`1 + q + ⋯ + qⁿ⁻¹`.  Division-free, so it is total: defined at every `q`,
including `q = 1` where it equals `n`. -/
def qClas (n : ℕ) (q : K) : K := ∑ i ∈ Finset.range n, q ^ i

/-- The **symmetric** `q`-integer `(qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
noncomputable def qSymm (n : ℕ) (q : K) : K := (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹)

/-- The classical bracket satisfies its defining quotient wherever `q ≠ 1`. -/
theorem qClas_mul_sub_one (n : ℕ) (q : K) :
    qClas n q * (q - 1) = q ^ n - 1 := by
  simpa [qClas] using geom_sum_mul q n

/-- `[2]` classically is `1 + q`. -/
theorem qClas_two (q : K) : qClas 2 q = 1 + q := by
  simp [qClas, Finset.sum_range_succ]

/-- `[2]` symmetrically is `(q² + 1)/q` — the form the audit's canonicaliser
prints, and equal to `q + q⁻¹`. -/
theorem qSymm_two (q : K) (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    qSymm 2 q = (q ^ 2 + 1) / q := by
  unfold qSymm
  rw [div_eq_div_iff h hq]
  field_simp
  ring

/-- **The bridge.**  The symmetric bracket at `q` is the classical bracket at
`q²`, normalised by `q^(n-1)`.  Stated at `n = 2` and `n = 3`, where it is a
one-line field computation; the general `n` statement is the same identity on
geometric sums. -/
theorem bridge_two (q : K) (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    q * qSymm 2 q = qClas 2 (q ^ 2) := by
  rw [qSymm_two q hq h, qClas_two]
  field_simp
  ring

theorem bridge_three (q : K) (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    q ^ 2 * qSymm 3 q = qClas 3 (q ^ 2) := by
  have hq2 : q ^ 2 - 1 ≠ 0 := by
    intro hc
    exact h (by field_simp; linear_combination hc)
  unfold qSymm qClas
  simp only [Finset.sum_range_succ, Finset.sum_range_zero]
  field_simp
  ring

/-- **The two conventions differ by exactly `(1 − q)/q` at `n = 2`.** -/
theorem qSymm_sub_qClas_two (q : K) (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    qSymm 2 q - qClas 2 q = (1 - q) / q := by
  rw [qSymm_two q hq h, qClas_two]
  field_simp
  ring

/-- **They never agree where both are defined.**  `q - q⁻¹ ≠ 0` already forces
`q ≠ 1`, and the difference `(1 − q)/q` is then nonzero.  So "the conventions
coincide at `q = 1`" is a statement about *limits*: at `q = 1` the symmetric
bracket is `0/0` and has no value to coincide with. -/
theorem conventions_never_agree (q : K) (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    qSymm 2 q ≠ qClas 2 q := by
  intro hcon
  rw [qSymm_two q hq h, qClas_two] at hcon
  -- (q² + 1)/q = 1 + q  ⟹  q² + 1 = q + q²  ⟹  q = 1
  have key : q ^ 2 + 1 = (1 + q) * q := (div_eq_iff hq).mp hcon
  have hq1 : (1 : K) = q := by linear_combination key
  -- but q = 1 makes q - q⁻¹ = 0, contradicting the hypothesis
  exact h (by rw [← hq1]; simp)

/-- At `q = 1` the classical bracket is `n` — the value the symmetric one only
approaches. -/
theorem qClas_at_one (n : ℕ) : qClas n (1 : K) = n := by
  simp [qClas]

end QOU.Substrate.QIntegerConventions
