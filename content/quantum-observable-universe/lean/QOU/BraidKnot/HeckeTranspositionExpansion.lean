import QOU.BraidKnot.HeckeAdditiveJucysMurphy

/-!
# The sum-of-transpositions expansion — the missing ingredient, and it needs no new axioms

`HeckeAdditiveJucysMurphy` established that the product half of Mathas 3.24(iii) does **not** follow
from the JM recursion in either convention, and that the classical proofs reach it through the
explicit expansion of `L_k` as a sum of transpositions.  The probe
[`jm_partial_sum_centrality_probe.py`](../../../../../computations/hecke/jm_partial_sum_centrality_probe.py)
then found that Jucys's **centrality** argument avoids the product half entirely, but still needs
that same expansion.

So the expansion is the one missing ingredient.  This file supplies it.

## No new axioms

It would be tempting to add transposition elements to `HeckeGenerators` as new fields with defining
relations — and that would be an **axiomatisation**, exactly what the anti-laundering rule targets.
It is unnecessary: in a braid presentation the transposition element is a **conjugate of a
generator**,

    T_(i,k)  =  σ_{k−1} ⋯ σ_{i+1} · σ_i · σ_{i+1} ⋯ σ_{k−1}

which recursively is `T_(i,k+1) = σ_k T_(i,k) σ_k` with `T_(k,k+1) = σ_k`.  That is a *definition*
built from the existing generators, so nothing is assumed.

## The expansion

`addJM_eq_transp_sum` : `A_k = d · Σ_{i<k} T_(i,k)`.

With this corpus's recursion `A_{k+1} = σ_k A_k σ_k + d·σ_k` the coefficients come out **uniform**
— every transposition carries the same `d`.  (Mathas's recursion puts `q⁻¹` outside both terms and
so yields *geometric* coefficients `q^{-1}, q^{-2}, …`; the two families differ, and this file
proves the expansion for the one this corpus actually uses rather than transcribing his.)

## What this unlocks, and what it does not

It is the input Jucys's argument needs: conjugating a transposition by `σ_j` **permutes** the index
pair, so `σ_j` fixes the sum `Σ_{i<k} T_(i,k)` whenever `j` and `j+1` both miss `k` — which is
3.24(i), and in turn feeds the centrality of the partial sums and the telescoping.

**Not proved here**: the conjugation-permutation law itself, hence not 3.24(i), centrality, or
commutativity.  This file provides the object and its expansion only.  `JucysMurphySpectrum` remains
untouched and the general-`λ` twist remains conditional.

Refs:
- [wenzl1988] Hecke algebra representations.
-/

namespace QOU.BraidKnot.Hecke

open Finset

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-- **The transposition element `T_(i,k)`**, defined as a conjugate of a generator — no new axioms.
`T_(k,k+1) = σ_k`, and `T_(i,k+1) = σ_k T_(i,k) σ_k` for `i < k`. -/
def transp (H : HeckeGenerators R A q) (i : ℕ) : ℕ → A
  | 0 => 1
  | (k + 1) => if i = k then H.σ k else H.σ k * transp H i k * H.σ k

@[simp] theorem transp_self (H : HeckeGenerators R A q) (k : ℕ) :
    transp H k (k + 1) = H.σ k := by
  rw [transp]; simp

theorem transp_succ (H : HeckeGenerators R A q) (i k : ℕ) (h : i ≠ k) :
    transp H i (k + 1) = H.σ k * transp H i k * H.σ k := by
  rw [transp]; simp [h]

/-- `T_(k−1,k) = σ_{k−1}` — the adjacent transposition is the generator itself. -/
theorem transp_pred (H : HeckeGenerators R A q) (k : ℕ) :
    transp H k (k + 1) = H.σ k := transp_self H k

/-- **The sum-of-transpositions expansion**: `A_k = d · Σ_{i<k} T_(i,k)`.

Induction on `k`.  The step is exactly the recursion: conjugating each `T_(i,k)` by `σ_k` produces
`T_(i,k+1)`, and the extra `d·σ_k` supplies the new top term `T_(k,k+1)`.

Note the **uniform** coefficient `d` — a consequence of this corpus's recursion
`A_{k+1} = σ_k A_k σ_k + d·σ_k`, which places `d` on the new term only.  Mathas's recursion places
`q⁻¹` outside both terms and yields geometric coefficients instead. -/
theorem addJM_eq_transp_sum (H : HeckeGenerators R A q) (d : R) (k : ℕ) :
    addJM H d k = d • ∑ i ∈ range k, transp H i k := by
  induction k with
  | zero => simp [addJM]
  | succ m ih =>
      rw [addJM_succ, ih, Finset.sum_range_succ]
      have hterm : ∀ i ∈ range m, transp H i (m + 1) = H.σ m * transp H i m * H.σ m := by
        intro i hi
        exact transp_succ H i m (by
          have := Finset.mem_range.mp hi
          omega)
      rw [Finset.sum_congr rfl hterm, transp_self]
      calc H.σ m * (d • ∑ i ∈ range m, transp H i m) * H.σ m + d • H.σ m
          = d • (H.σ m * (∑ i ∈ range m, transp H i m) * H.σ m) + d • H.σ m := by
            rw [mul_smul_comm, smul_mul_assoc]
        _ = d • (∑ i ∈ range m, H.σ m * transp H i m * H.σ m) + d • H.σ m := by
            rw [Finset.mul_sum, Finset.sum_mul]
        _ = _ := by rw [← smul_add]

end QOU.BraidKnot.Hecke
