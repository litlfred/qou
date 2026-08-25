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

/-! ## The pair-swap law — `σ_j` fixes `T_(j,i) + T_(j+1,i)`

This is the mechanism behind Mathas 3.24(i)'s hard half.  For `i > j+1` the sum `Σ_{l<i} T_(l,i)`
has **exactly two** terms `σ_j` can disturb — `l = j` and `l = j+1` — and `σ_j` preserves *their
sum* while fixing every other term individually.

Measured first ([`jm_partial_sum_centrality_probe.py`] and a companion sweep at `n = 6`, `q ∈ {2,3}`,
exact rationals): the pair commutes in every case, while each term **alone** does not.  So this is a
genuine pair phenomenon, not term-by-term commutation. -/

/-- **Pair-swap law**: for `i > j+1`, `σ_j` commutes with `T_(j,i) + T_(j+1,i)`.

Base case `i = j+2`, with `u = σ_j`, `v = σ_{j+1}`: the claim is `u(vuv + v) = (vuv + v)u`.  One
braid move turns `uvu` into `vuv` on each side, leaving `vuv² + uv = v²uv + vu`, and the **Hecke
relation** `v² = hv + 1` expands both to `h·vuv + uv + vu`.  Braid alone is not enough — the Hecke
relation is what makes the leftover terms cancel.

Step `i → i+1`: both transpositions gain the same outer conjugation by `σ_i`, and `σ_j` commutes
with `σ_i` because `i > j+1`. -/
theorem sigma_comm_transp_pair (H : HeckeGenerators R A q) (j : ℕ) :
    ∀ i : ℕ, j + 1 < i →
      H.σ j * (transp H j i + transp H (j + 1) i)
        = (transp H j i + transp H (j + 1) i) * H.σ j := by
  intro i
  induction i with
  | zero => intro h; omega
  | succ m ih =>
      intro hm
      rcases Nat.lt_or_ge (j + 1) m with hlt | hge
      · -- inductive step: m > j+1, both transpositions conjugate by σ_m
        have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega)
        have hjm : j ≠ m := by omega
        have hj1m : j + 1 ≠ m := by omega
        have hih := ih hlt
        rw [transp_succ H j m hjm, transp_succ H (j + 1) m hj1m]
        calc H.σ j * (H.σ m * transp H j m * H.σ m + H.σ m * transp H (j + 1) m * H.σ m)
            = (H.σ j * H.σ m) * (transp H j m + transp H (j + 1) m) * H.σ m := by
              noncomm_ring
          _ = (H.σ m * H.σ j) * (transp H j m + transp H (j + 1) m) * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * (transp H j m + transp H (j + 1) m)) * H.σ m := by noncomm_ring
          _ = H.σ m * ((transp H j m + transp H (j + 1) m) * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * (transp H j m + transp H (j + 1) m) * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * (transp H j m + transp H (j + 1) m) * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring
      · -- base case: m = j+1, so the index is i = j+2
        have hmeq : m = j + 1 := by omega
        subst hmeq
        have hb : H.σ j * H.σ (j + 1) * H.σ j
            = H.σ (j + 1) * H.σ j * H.σ (j + 1) := H.braid j
        have hh : H.σ (j + 1) * H.σ (j + 1) = (q - q⁻¹) • H.σ (j + 1) + 1 := hecke_smul H (j + 1)
        have hj : j ≠ j + 1 := by omega
        rw [transp_succ H j (j + 1) hj, transp_self, transp_self]
        calc H.σ j * (H.σ (j + 1) * H.σ j * H.σ (j + 1) + H.σ (j + 1))
            = (H.σ j * H.σ (j + 1) * H.σ j) * H.σ (j + 1)
                + H.σ j * H.σ (j + 1) := by noncomm_ring
          _ = (H.σ (j + 1) * H.σ j * H.σ (j + 1)) * H.σ (j + 1)
                + H.σ j * H.σ (j + 1) := by rw [hb]
          _ = H.σ (j + 1) * H.σ j * (H.σ (j + 1) * H.σ (j + 1))
                + H.σ j * H.σ (j + 1) := by noncomm_ring
          _ = H.σ (j + 1) * H.σ j * ((q - q⁻¹) • H.σ (j + 1) + 1)
                + H.σ j * H.σ (j + 1) := by rw [hh]
          _ = (q - q⁻¹) • (H.σ (j + 1) * H.σ j * H.σ (j + 1))
                + H.σ (j + 1) * H.σ j + H.σ j * H.σ (j + 1) := by
              simp only [mul_add, mul_one, mul_smul_comm]
          _ = (q - q⁻¹) • (H.σ j * H.σ (j + 1) * H.σ j)
                + H.σ (j + 1) * H.σ j + H.σ j * H.σ (j + 1) := by rw [hb]
          _ = ((q - q⁻¹) • H.σ (j + 1) + 1) * H.σ j * H.σ (j + 1)
                + H.σ (j + 1) * H.σ j := by
              simp only [add_mul, one_mul, smul_mul_assoc]
              rw [← hb]
              noncomm_ring
          _ = (H.σ (j + 1) * H.σ (j + 1)) * H.σ j * H.σ (j + 1)
                + H.σ (j + 1) * H.σ j := by rw [← hh]
          _ = H.σ (j + 1) * (H.σ (j + 1) * H.σ j * H.σ (j + 1))
                + H.σ (j + 1) * H.σ j := by noncomm_ring
          _ = H.σ (j + 1) * (H.σ j * H.σ (j + 1) * H.σ j)
                + H.σ (j + 1) * H.σ j := by rw [← hb]
          _ = _ := by noncomm_ring

/-! ## Disjoint transpositions commute with the generator

The remaining half of 3.24(i): `σ_j` commutes with `T_(l,i)` **individually** whenever `l` and `i`
both miss `{j, j+1}` — the two transpositions are disjoint.

This is not letter-wise obvious: for `l < j < j+1 < i` the word for `T_(l,i)` *contains* both `σ_j`
and `σ_{j+1}`.  Measured first (H₆, exact rationals): 24 disjoint pairs, all commuting, none
failing. -/

/-- `σ_m` commutes with `T_(l,i)` when `m > i` — every letter of `T_(l,i)` has index `≤ i−1`, so all
are at distance `≥ 2` from `m`. -/
theorem sigma_comm_transp_far (H : HeckeGenerators R A q) (l : ℕ) :
    ∀ i m : ℕ, l < i → i < m → H.σ m * transp H l i = transp H l i * H.σ m := by
  intro i
  induction i with
  | zero => intro m h; omega
  | succ k ih =>
      intro m hl hm
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hl) with heq | hlt
      · -- l = k : transp is the generator σ_k
        subst heq
        rw [transp_self]
        exact (H.far l m (by omega)).symm ▸ (H.far l m (by omega))
      · -- l < k : unfold the conjugation
        have hlk : l ≠ k := by omega
        have hfar : H.σ m * H.σ k = H.σ k * H.σ m := (H.far k m (by omega)).symm
        have hih := ih m hlt (by omega)
        rw [transp_succ H l k hlk]
        calc H.σ m * (H.σ k * transp H l k * H.σ k)
            = (H.σ m * H.σ k) * transp H l k * H.σ k := by noncomm_ring
          _ = (H.σ k * H.σ m) * transp H l k * H.σ k := by rw [hfar]
          _ = H.σ k * (H.σ m * transp H l k) * H.σ k := by noncomm_ring
          _ = H.σ k * (transp H l k * H.σ m) * H.σ k := by rw [hih]
          _ = H.σ k * transp H l k * (H.σ m * H.σ k) := by noncomm_ring
          _ = H.σ k * transp H l k * (H.σ k * H.σ m) := by rw [hfar]
          _ = _ := by noncomm_ring

/-- **The hard base case**: `σ_j` commutes with `T_(l,j+2)` for `l < j`.

`T_(l,j+2) = v u X u v` with `u = σ_j`, `v = σ_{j+1}` and `X = T_(l,j)`, and `X` commutes with `v`
by `sigma_comm_transp_far` (every letter of `X` has index `≤ j−1`).  Then two braid moves close it:

    u · v u X u v = (uvu) X u v = (vuv) X u v = v u X (vuv) = v u X (uvu) = v u X u v · u

Only the braid relation is used — no Hecke relation here, in contrast to the pair-swap law. -/
theorem sigma_comm_transp_base (H : HeckeGenerators R A q) (j l : ℕ) (hl : l < j) :
    H.σ j * transp H l (j + 2) = transp H l (j + 2) * H.σ j := by
  have hb : H.σ j * H.σ (j + 1) * H.σ j = H.σ (j + 1) * H.σ j * H.σ (j + 1) := H.braid j
  have hXv : H.σ (j + 1) * transp H l j = transp H l j * H.σ (j + 1) :=
    sigma_comm_transp_far H l j (j + 1) hl (by omega)
  have h1 : l ≠ j + 1 := by omega
  have h2 : l ≠ j := by omega
  rw [show j + 2 = (j + 1) + 1 from rfl, transp_succ H l (j + 1) h1, transp_succ H l j h2]
  calc H.σ j * (H.σ (j + 1) * (H.σ j * transp H l j * H.σ j) * H.σ (j + 1))
      = (H.σ j * H.σ (j + 1) * H.σ j) * transp H l j * (H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = (H.σ (j + 1) * H.σ j * H.σ (j + 1)) * transp H l j
          * (H.σ j * H.σ (j + 1)) := by rw [hb]
    _ = H.σ (j + 1) * H.σ j * (H.σ (j + 1) * transp H l j)
          * (H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = H.σ (j + 1) * H.σ j * (transp H l j * H.σ (j + 1))
          * (H.σ j * H.σ (j + 1)) := by rw [hXv]
    _ = H.σ (j + 1) * H.σ j * transp H l j
          * (H.σ (j + 1) * H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = H.σ (j + 1) * H.σ j * transp H l j
          * (H.σ j * H.σ (j + 1) * H.σ j) := by rw [← hb]
    _ = _ := by noncomm_ring

/-- **Disjoint transpositions commute**: `σ_j` commutes with `T_(l,i)` for `l < j` and `i > j+1`.

Induction on `i` above the base case `i = j+2`: each step conjugates by `σ_{i−1}` with
`i−1 > j+1`, which `σ_j` commutes past by far-commutation. -/
theorem sigma_comm_transp_disjoint (H : HeckeGenerators R A q) (j l : ℕ) (hl : l < j) :
    ∀ i : ℕ, j + 1 < i → H.σ j * transp H l i = transp H l i * H.σ j := by
  intro i
  induction i with
  | zero => intro h; omega
  | succ m ih =>
      intro hm
      rcases Nat.lt_or_ge (j + 1) m with hlt | hge
      · have hli : l ≠ m := by omega
        have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega)
        have hih := ih hlt
        rw [transp_succ H l m hli]
        calc H.σ j * (H.σ m * transp H l m * H.σ m)
            = (H.σ j * H.σ m) * transp H l m * H.σ m := by noncomm_ring
          _ = (H.σ m * H.σ j) * transp H l m * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * transp H l m) * H.σ m := by noncomm_ring
          _ = H.σ m * (transp H l m * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * transp H l m * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * transp H l m * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring
      · have : m = j + 1 := by omega
        subst this
        exact sigma_comm_transp_base H j l hl

end QOU.BraidKnot.Hecke
