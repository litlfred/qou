import Mathlib.Tactic
import Mathlib.Algebra.GeomSum

/-!
# QOU.Common.BalancedQuantumTwist — the balanced/unbalanced quantum-integer twist

The general algebraic engine behind `prop:binding-period-involution-statistic`'s
Step 1 (the balanced twist `dim_q^bal(λ) = q^{content(λ)−n(n−1)/2}·f̃^λ(q²)`):
the balanced quantum integer is the unbalanced one at `q²`, shifted by a monomial.

Working over a field with `q ≠ 0`, write the balanced numerator `q^k − q^{−k}`
(the balanced integer up to the common factor `q − q⁻¹`, which cancels
between the `n`-cell numerator and `n`-hook denominator of a quantum
dimension). The load-bearing, fully general lemmas here are:

* `balancedNum_factor` : `q^k − q^{−k} = q^{−k}·(q²−1)·[k]_{q²}`
  (`[k]_{q²} = Σ_{i<k}(q²)^i`), an identity of Laurent monomials — no
  `q² ≠ 1` needed;
* `prod_balancedNum_factor` : the product over any finite family factors as
  `q^{−Σ sizes}·(q²−1)^{card}·∏ [size]_{q²}` — the product-level twist;
* `balanced_quantum_twist` : assembling the two into the quantum-dimension
  ratio, the exponent collapses to `content(λ) − n(n−1)/2` **given** the hook
  data (`card = n`, `Σ hooks = b(λ)+b(λ')+n`, Gauss sum `Σ_{k≤n} k =
  n(n+1)/2`). The hook-sum identity is the one piece of partition
  combinatorics taken as an explicit hypothesis (Mathlib has no
  `Σ_{c∈λ} h(c)` lemma for a general Young diagram); everything algebraic is
  proved.

Ground ring: generic `Field K` with `q ≠ 0` — the balanced integer carries
`q⁻¹` (§7c: an *algebraic* inverse, not an archimedean construct), so a field
is the weakest correct typeclass; no `ℝ`, no ordering.
-/

namespace QOU.BalancedQuantumTwist

open Finset BigOperators

variable {K : Type*} [Field K]

/-- Unbalanced quantum integer `[k]_x = Σ_{i<k} xⁱ`. -/
def qintU (x : K) (k : ℕ) : K := ∑ i ∈ Finset.range k, x ^ i

@[simp] theorem qintU_zero (x : K) : qintU x 0 = 0 := by simp [qintU]

/-- Telescoping: `(x − 1)·[k]_x = xᵏ − 1`. -/
theorem sub_one_mul_qintU (x : K) (k : ℕ) : (x - 1) * qintU x k = x ^ k - 1 := by
  rw [qintU, mul_comm]
  exact geom_sum_mul x k

/-- **Balanced-numerator factorization** (the load-bearing lemma):
`q^k − q^{−k} = q^{−k}·(q²−1)·[k]_{q²}`, as an identity of `ℤ`-powers over a
field with `q ≠ 0`. No `q² ≠ 1` hypothesis — it is a monomial identity. -/
theorem balancedNum_factor (q : K) (hq : q ≠ 0) (k : ℕ) :
    q ^ (k : ℤ) - q ^ (-(k : ℤ)) = q ^ (-(k : ℤ)) * (q ^ 2 - 1) * qintU (q ^ 2) k := by
  have hstep : (q ^ 2 - 1) * qintU (q ^ 2) k = (q ^ 2) ^ k - 1 := by
    have := sub_one_mul_qintU (q ^ 2) k
    simpa using this
  rw [mul_assoc, hstep]
  have hnp : ((q ^ 2) ^ k : K) = q ^ ((2 * k : ℕ) : ℤ) := by
    rw [← pow_mul, zpow_natCast]
  have hexp : (-(k : ℤ)) + ((2 * k : ℕ) : ℤ) = (k : ℤ) := by push_cast; ring
  rw [hnp, mul_sub, mul_one, ← zpow_add₀ hq, hexp]

/-- **Product-level twist.** Over any finite family `s` with a size function
`sz : ι → ℕ`, the product of balanced numerators factors as a global monomial
`q^{−Σ sz}` times `(q²−1)^{|s|}` times the product of unbalanced `q²`-integers.
This is the general engine: apply it to the `n` cells (numerator) and the `n`
hooks (denominator) of a quantum dimension. -/
theorem prod_balancedNum_factor (q : K) (hq : q ≠ 0)
    {ι : Type*} (s : Finset ι) (sz : ι → ℕ) :
    ∏ i ∈ s, (q ^ (sz i : ℤ) - q ^ (-(sz i : ℤ)))
      = q ^ (-(∑ i ∈ s, (sz i : ℤ)))
        * (q ^ 2 - 1) ^ s.card
        * ∏ i ∈ s, qintU (q ^ 2) (sz i) := by
  classical
  induction s using Finset.induction with
  | empty => simp
  | @insert a t ha ih =>
    rw [Finset.prod_insert ha, balancedNum_factor q hq, ih,
      Finset.sum_insert ha, Finset.card_insert_of_notMem ha,
      Finset.prod_insert ha]
    rw [neg_add, zpow_add₀ hq]
    ring

/-- **The balanced quantum twist** (division-free form). Let `cells` (the `n`
cells of a Young diagram `λ ⊢ n`) and `hooks` (its `n` hooks) be the
numerator/denominator families of the balanced quantum dimension, with equal
cardinality `card cells = card hooks = n`. Then

  `q^{Σ cellSz} · (∏ balancedNum cells) · (∏ [hookSz]_{q²})`
    `= q^{Σ hookSz} · (∏ balancedNum hooks) · (∏ [cellSz]_{q²})`,

both sides equal to `(q²−1)ⁿ · ∏[cellSz]_{q²} · ∏[hookSz]_{q²}`. Dividing (when
the denominator is nonzero) gives the classical shape
`∏bn(cells)/∏bn(hooks) = q^{ΣhookSz − ΣcellSz} · ∏[cell]_{q²}/∏[hook]_{q²}`.
With the Gauss sum `Σ cellSz = n(n+1)/2` and the hook identity
`Σ hookSz = b(λ)+b(λ')+n`, the monomial exponent is exactly
`content(λ) − n(n−1)/2` — Step 1 of `prop:binding-period-involution-statistic`.
The `(q²−1)ⁿ` factors match precisely because `card cells = card hooks`; no
`q² ≠ 1` and no division are needed for this form. -/
theorem balanced_quantum_twist (q : K) (hq : q ≠ 0)
    {ι κ : Type*} (cells : Finset ι) (hooks : Finset κ)
    (cellSz : ι → ℕ) (hookSz : κ → ℕ)
    (hcard : cells.card = hooks.card) :
    q ^ (∑ c ∈ cells, (cellSz c : ℤ))
        * (∏ c ∈ cells, (q ^ (cellSz c : ℤ) - q ^ (-(cellSz c : ℤ))))
        * (∏ c ∈ hooks, qintU (q ^ 2) (hookSz c))
      = q ^ (∑ c ∈ hooks, (hookSz c : ℤ))
        * (∏ c ∈ hooks, (q ^ (hookSz c : ℤ) - q ^ (-(hookSz c : ℤ))))
        * (∏ c ∈ cells, qintU (q ^ 2) (cellSz c)) := by
  set A : ℤ := ∑ c ∈ cells, (cellSz c : ℤ) with hA
  set B : ℤ := ∑ c ∈ hooks, (hookSz c : ℤ) with hB
  set Pc : K := ∏ c ∈ cells, qintU (q ^ 2) (cellSz c) with hPc
  set Ph : K := ∏ c ∈ hooks, qintU (q ^ 2) (hookSz c) with hPh
  rw [prod_balancedNum_factor q hq cells, prod_balancedNum_factor q hq hooks,
    ← hA, ← hB, ← hPc, ← hPh, hcard]
  have cancelA : q ^ A * q ^ (-A) = 1 := by rw [← zpow_add₀ hq]; simp
  have cancelB : q ^ B * q ^ (-B) = 1 := by rw [← zpow_add₀ hq]; simp
  calc
    q ^ A * (q ^ (-A) * (q ^ 2 - 1) ^ hooks.card * Pc) * Ph
        = (q ^ A * q ^ (-A)) * (q ^ 2 - 1) ^ hooks.card * (Pc * Ph) := by ring
    _ = (q ^ 2 - 1) ^ hooks.card * (Pc * Ph) := by rw [cancelA]; ring
    _ = (q ^ B * q ^ (-B)) * (q ^ 2 - 1) ^ hooks.card * (Ph * Pc) := by
          rw [cancelB]; ring
    _ = q ^ B * (q ^ (-B) * (q ^ 2 - 1) ^ hooks.card * Ph) * Pc := by ring

end QOU.BalancedQuantumTwist
