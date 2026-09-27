/-
# Corollaries of the Habiro-tail (★) identity (bean qou-cmx4)

`HabiroTailStar.star` is now proved sorry-free at every order, so the
structure it exposes is available as theorems rather than as
witness-cited compute. This file pins the **algebraic** consequences:

* `That` — the right-hand side of (★) as a named object,
  `T̂_n(q) = (q;q)_n² · Σ_{k≤n} q^{k(n+1)}·[n,k]_q`;
* `star_That` — (★) restated through it;
* `That_split` — the **transient structure**: the `k = 0` term is
  exactly `1`, so `T̂_n = (q;q)_n²·(1 + q^{n+1}·S_n)`. Every correction
  to the leading `(q;q)_n²` carries a factor `q^{n+1}` — this is the
  algebraic source of the transient behaviour measured in the compute;
* `qPoch_succ` — the recursion `(q;q)_{n+1} = (q;q)_n·(1 − q^{n+1})`
  whose limit is the residue `c∞ = (q̃;q̃)_∞²`;
* small-`n` evaluations (`That_zero`, `That_one`).

**Scope, stated honestly.** The two *analytic* facts —
`c∞ = (q̃;q̃)_∞²` as a convergent infinite product, and the pole ladder
at `w = −q₀ᵏ` — are limit statements about the archimedean evaluation
and are NOT proved here; they remain compute-cited
(`qbeta-5two-gbar-pole-ladder.witness.json`, Padé-located at rel
4.6e-11 for k=1). What this file supplies is their algebraic
skeleton: the finite-order recursion and the `q^{n+1}` transient
factor that those limits are taken of. No archimedean construct
appears, so everything stays pre-wall over a generic `Field R`
(§7c).
-/
import QOU.QBeta.HabiroTailStar

namespace QOU.QBeta.HabiroTailStar

open Finset

variable {R : Type*} [Field R]

/-- The right-hand side of (★), up to its sign:
`T̂_n(q) = (q;q)_n² · Σ_{k≤n} q^{k(n+1)}·[n,k]_q`. -/
noncomputable def That (q : R) (n : ℕ) : R :=
  qPoch q n ^ 2 * ∑ k ∈ range (n + 1), q ^ (k * (n + 1)) * gaussBinom q n k

/-- (★) restated through `That`: the Masbaum tail, normalised, is
`(−1)ⁿ·T̂_n` at the bar-inverted argument. -/
theorem star_That (a : R) (ha : a ≠ 0) (n : ℕ) :
    masbaumC a n * qPoch (a ^ 2) n ^ 2 * a ^ (-(5 * (n : ℤ) ^ 2 + 7 * n))
      = (-1) ^ n * That (a ^ 2)⁻¹ n := by
  rw [That, ← mul_assoc]
  exact star a ha n

/-- The Pochhammer recursion — the finite-order step whose limit is the
Borel residue `c∞ = (q;q)_∞²`. -/
lemma qPoch_succ (q : R) (n : ℕ) :
    qPoch q (n + 1) = qPoch q n * (1 - q ^ (n + 1)) := by
  simp only [qPoch, Finset.prod_range_succ]

/-- **Transient structure.** The `k = 0` term of the (★) sum is exactly
`1`, so every correction to the leading `(q;q)_n²` carries a factor
`q^{n+1}`:
`T̂_n = (q;q)_n²·(1 + q^{n+1}·Σ_{k<n} q^{k(n+1)}·[n,k+1]_q)`. -/
theorem That_split (q : R) (n : ℕ) :
    That q n = qPoch q n ^ 2
      * (1 + q ^ (n + 1)
          * ∑ k ∈ range n, q ^ (k * (n + 1)) * gaussBinom q n (k + 1)) := by
  rw [That, Finset.sum_range_succ']
  congr 1
  rw [Finset.mul_sum]
  simp only [gaussBinom_zero, Nat.zero_mul, pow_zero, mul_one]
  rw [add_comm]
  congr 1
  refine Finset.sum_congr rfl ?_
  intro k _
  have : (k + 1) * (n + 1) = (n + 1) + k * (n + 1) := by ring
  rw [this, pow_add]
  ring

/-- `T̂_0 = 1`. -/
@[simp] lemma That_zero (q : R) : That q 0 = 1 := by
  simp [That, qPoch]

/-- `T̂_1 = (1 − q)²·(1 + q²)`. -/
lemma That_one (q : R) : That q 1 = (1 - q) ^ 2 * (1 + q ^ 2) := by
  simp [That, qPoch, Finset.sum_range_succ, gaussBinom]

end QOU.QBeta.HabiroTailStar
