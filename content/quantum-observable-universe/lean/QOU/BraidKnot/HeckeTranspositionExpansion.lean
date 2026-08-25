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

**What the file grew into.**  Those steps are now all here, in order: the pair-swap law
(`sigma_comm_transp_pair`), Mathas 3.24(i) (`sigma_comm_addJM`), Jucys's centrality
(`sigma_comm_partialSum_ne`), the telescoping (`addJM_comm`), and — via the identification
`L_k = 1 + A_k` at `d = q − q⁻¹` — **commutativity of the multiplicative family itself**
(`jmRaw_comm`).  The paragraph above was written when only the expansion existed; it is kept because
the sequence it lays out is the one that worked.

**Still not proved here**: `∏Lᵢ = Δ²` beyond `n = 3`, and the spectral half of
`JucysMurphySpectrum` (the seminormal representation).  The general-`λ` twist therefore remains
conditional — commutativity was a necessary step toward it, not a sufficient one.

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

/-- `σ_j` commutes with `T_(l,i)` when `j + 1 < l` — every letter of `T_(l,i)` has index in
`[l, i−1]`, all at distance `≥ 2` above `j`. -/
theorem sigma_comm_transp_below (H : HeckeGenerators R A q) (j l : ℕ) (hjl : j + 1 < l) :
    ∀ i : ℕ, l < i → H.σ j * transp H l i = transp H l i * H.σ j := by
  intro i
  induction i with
  | zero => intro h; omega
  | succ m ih =>
      intro hm
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hm) with heq | hlt
      · subst heq
        rw [transp_self]
        exact H.far j l (by omega)
      · have hlm : l ≠ m := by omega
        have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega)
        have hih := ih hlt
        rw [transp_succ H l m hlm]
        calc H.σ j * (H.σ m * transp H l m * H.σ m)
            = (H.σ j * H.σ m) * transp H l m * H.σ m := by noncomm_ring
          _ = (H.σ m * H.σ j) * transp H l m * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * transp H l m) * H.σ m := by noncomm_ring
          _ = H.σ m * (transp H l m * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * transp H l m * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * transp H l m * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring

/-! ## Mathas 3.24(i), assembled -/

/-- **Mathas 3.24(i)** (the `i > j+1` case): `σ_j` commutes with `A_i`.

Assembled from the three commutation lemmas by splitting `Σ_{l<i} T_(l,i)` on `l`:

| `l` | lemma | ingredient |
|---|---|---|
| `l < j` | `sigma_comm_transp_disjoint` | braid |
| `l ∈ {j, j+1}` | `sigma_comm_transp_pair` — **as a pair** | braid + Hecke |
| `l > j+1` | `sigma_comm_transp_below` | braid |

The middle row is the one that cannot be done term-by-term: neither `T_(j,i)` nor `T_(j+1,i)`
commutes with `σ_j` alone (measured), only their sum does.  That is why the expansion into a **sum**
was the necessary ingredient rather than a convenience. -/
theorem sigma_comm_addJM (H : HeckeGenerators R A q) (d : R) (j i : ℕ) (h : j + 1 < i) :
    H.σ j * addJM H d i = addJM H d i * H.σ j := by
  have hne : j ≠ j + 1 := by omega
  have hsub : ({j, j + 1} : Finset ℕ) ⊆ Finset.range i := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp [Finset.mem_range] <;> omega
  have hpair : ∑ l ∈ ({j, j + 1} : Finset ℕ), transp H l i
      = transp H j i + transp H (j + 1) i := Finset.sum_pair hne
  have hrest : H.σ j * (∑ l ∈ Finset.range i \ {j, j + 1}, transp H l i)
      = (∑ l ∈ Finset.range i \ {j, j + 1}, transp H l i) * H.σ j := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun l hl => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hl
    obtain ⟨hli, hlj, hlj1⟩ := hl
    rcases Nat.lt_or_ge l j with hlt | hge
    · exact sigma_comm_transp_disjoint H j l hlt i h
    · exact sigma_comm_transp_below H j l (by omega) i hli
  rw [addJM_eq_transp_sum, ← Finset.sum_sdiff hsub, hpair]
  rw [mul_smul_comm, smul_mul_assoc, mul_add, add_mul, hrest,
    sigma_comm_transp_pair H j i h]

/-- **3.24(i), the easy direction**: `σ_j` commutes with `A_i` when `i < j`.  Every letter of every
`T_(l,i)` has index `≤ i−1 ≤ j−2`, so `sigma_comm_transp_far` applies term by term. -/
theorem sigma_comm_addJM_small (H : HeckeGenerators R A q) (d : R) (j i : ℕ) (h : i < j) :
    H.σ j * addJM H d i = addJM H d i * H.σ j := by
  rw [addJM_eq_transp_sum, mul_smul_comm, smul_mul_assoc]
  congr 1
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun l hl => ?_
  exact sigma_comm_transp_far H l i j (Finset.mem_range.mp hl) h

/-! ## Partial-sum centrality — Jucys's route

`S_m := Σ_{i ≤ m} A_i`.  Measured in
[`jm_partial_sum_centrality_probe.py`](../../../../../computations/hecke/jm_partial_sum_centrality_probe.py):
`S_m` commutes with `σ_j` for **every `j ≠ m`**, at three values of `q` and three of `d`.

The exception at `j = m` is not an accident: the summation cutoff **splits the pair**
`(A_m, A_{m+1})`, and that pair is exactly what `addJM_sigma_comm_add` handles.  Every other index
commutes with `σ_j` on its own. -/

/-- Partial sum `S_m = Σ_{i ≤ m} A_i` (the `i = 0` term is `0`). -/
def partialSum (H : HeckeGenerators R A q) (d : R) (m : ℕ) : A :=
  ∑ i ∈ Finset.range (m + 1), addJM H d i

/-- **Centrality below the cutoff**: for `j < m`, `σ_j` commutes with `S_m`.

Split `range (m+1)` into `{j, j+1}` and the rest.  The pair is `addJM_sigma_comm_add`; each other
index is `sigma_comm_addJM_small` (below `j`) or `sigma_comm_addJM` (above `j+1`). -/
theorem sigma_comm_partialSum (H : HeckeGenerators R A q) (d : R) (j m : ℕ) (h : j < m) :
    H.σ j * partialSum H d m = partialSum H d m * H.σ j := by
  have hne : j ≠ j + 1 := by omega
  have hsub : ({j, j + 1} : Finset ℕ) ⊆ Finset.range (m + 1) := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp only [Finset.mem_range] <;> omega
  have hpair : ∑ i ∈ ({j, j + 1} : Finset ℕ), addJM H d i
      = addJM H d j + addJM H d (j + 1) := Finset.sum_pair hne
  have hrest : H.σ j * (∑ i ∈ Finset.range (m + 1) \ {j, j + 1}, addJM H d i)
      = (∑ i ∈ Finset.range (m + 1) \ {j, j + 1}, addJM H d i) * H.σ j := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i hi => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hi
    obtain ⟨_, hij, hij1⟩ := hi
    rcases Nat.lt_or_ge i j with hlt | hge
    · exact sigma_comm_addJM_small H d j i hlt
    · exact sigma_comm_addJM H d j i (by omega)
  unfold partialSum
  rw [← Finset.sum_sdiff hsub, hpair, mul_add, add_mul, hrest, addJM_sigma_comm_add]

/-- **Centrality above the cutoff**: for `j > m`, `σ_j` commutes with `S_m` — every index in the sum
is below `j`, so `sigma_comm_addJM_small` applies term by term. -/
theorem sigma_comm_partialSum_above (H : HeckeGenerators R A q) (d : R) (j m : ℕ) (h : m < j) :
    H.σ j * partialSum H d m = partialSum H d m * H.σ j := by
  unfold partialSum
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun i hi => ?_
  exact sigma_comm_addJM_small H d j i (by
    have := Finset.mem_range.mp hi
    omega)

/-- **Jucys's centrality property**: `σ_j` commutes with `S_m` for every `j ≠ m`.

This is the statement the measurement found, now proved.  It is the input to the telescoping
argument `A_m = S_m − S_{m−1}`, which yields commutativity **without ever using** the product half
of 3.24(iii) — the step that `HeckeAdditiveJucysMurphy.addJM_sigma_prod_swap` showed is entangled
with the conclusion. -/
theorem sigma_comm_partialSum_ne (H : HeckeGenerators R A q) (d : R) (j m : ℕ) (h : j ≠ m) :
    H.σ j * partialSum H d m = partialSum H d m * H.σ j := by
  rcases Nat.lt_or_ge j m with hlt | hge
  · exact sigma_comm_partialSum H d j m hlt
  · exact sigma_comm_partialSum_above H d j m (by omega)

/-! ## Word lifting — from letters to the whole transposition

Centrality gives commutation with *generators*.  To telescope we need commutation with `A_i`, which
is a sum of **words** in the generators.  The lift is an induction over `transp`'s own recursion:
`T_(l,i)` is built from `σ_l … σ_{i−1}`, so an element commuting with every `σ_j` for `j < i`
commutes with the whole word.

This is bookkeeping, not new mathematics — but it is what turns `sigma_comm_partialSum_ne` into a
statement about `A_i`. -/

/-- If `X` commutes with every generator `σ_j` for `j < i`, it commutes with `T_(l,i)` — every
letter of that word has index in `[l, i−1]`. -/
theorem comm_transp_of_comm_sigma (H : HeckeGenerators R A q) (X : A) (l : ℕ) :
    ∀ i : ℕ, l < i → (∀ j, j < i → X * H.σ j = H.σ j * X) →
      X * transp H l i = transp H l i * X := by
  intro i
  induction i with
  | zero => intro h; omega
  | succ k ih =>
      intro hl hX
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hl) with heq | hlt
      · subst heq
        rw [transp_self]
        exact hX l (by omega)
      · have hlk : l ≠ k := by omega
        have hk : X * H.σ k = H.σ k * X := hX k (by omega)
        have hih := ih hlt (fun j hj => hX j (by omega))
        rw [transp_succ H l k hlk]
        calc X * (H.σ k * transp H l k * H.σ k)
            = (X * H.σ k) * transp H l k * H.σ k := by noncomm_ring
          _ = (H.σ k * X) * transp H l k * H.σ k := by rw [hk]
          _ = H.σ k * (X * transp H l k) * H.σ k := by noncomm_ring
          _ = H.σ k * (transp H l k * X) * H.σ k := by rw [hih]
          _ = H.σ k * transp H l k * (X * H.σ k) := by noncomm_ring
          _ = H.σ k * transp H l k * (H.σ k * X) := by rw [hk]
          _ = _ := by noncomm_ring

/-- The same lift for `A_i` itself, via the expansion `A_i = d · Σ_{l<i} T_(l,i)`. -/
theorem comm_addJM_of_comm_sigma (H : HeckeGenerators R A q) (d : R) (X : A) (i : ℕ)
    (hX : ∀ j, j < i → X * H.σ j = H.σ j * X) :
    X * addJM H d i = addJM H d i * X := by
  rw [addJM_eq_transp_sum, mul_smul_comm, smul_mul_assoc]
  congr 1
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun l hl => ?_
  exact comm_transp_of_comm_sigma H X l i (Finset.mem_range.mp hl) hX

/-! ## Telescoping — commutativity, without the product half of 3.24(iii)

`A_{m+1} = S_{m+1} − S_m`.  For `i ≤ m` every letter of `A_i` has index `< i ≤ m`, so it misses both
cutoffs `m` and `m+1`; `sigma_comm_partialSum_ne` then applies to each letter and the word lift
carries it to `A_i`.  Both partial sums commute with `A_i`, hence so does their difference.

This is Jucys's argument.  It never touches the product half of Mathas 3.24(iii) — the step that
[`HeckeAdditiveJucysMurphy.addJM_sigma_prod_swap`](HeckeAdditiveJucysMurphy.lean) showed *swaps* the
factors rather than commuting them, and which is entangled with the conclusion it was supposed to
supply. -/

theorem partialSum_succ (H : HeckeGenerators R A q) (d : R) (m : ℕ) :
    partialSum H d (m + 1) = partialSum H d m + addJM H d (m + 1) :=
  Finset.sum_range_succ _ _

/-- **The telescoping step**: `A_i` commutes with `A_{m+1}` whenever `i ≤ m`. -/
theorem addJM_comm_of_le (H : HeckeGenerators R A q) (d : R) (i m : ℕ) (h : i ≤ m) :
    addJM H d i * addJM H d (m + 1) = addJM H d (m + 1) * addJM H d i := by
  have hS1 : partialSum H d (m + 1) * addJM H d i = addJM H d i * partialSum H d (m + 1) :=
    comm_addJM_of_comm_sigma H d _ i fun j hj =>
      (sigma_comm_partialSum_ne H d j (m + 1) (by omega)).symm
  have hS0 : partialSum H d m * addJM H d i = addJM H d i * partialSum H d m :=
    comm_addJM_of_comm_sigma H d _ i fun j hj =>
      (sigma_comm_partialSum_ne H d j m (by omega)).symm
  have hsplit : addJM H d (m + 1) = partialSum H d (m + 1) - partialSum H d m := by
    rw [partialSum_succ]; abel
  rw [hsplit, mul_sub, sub_mul, hS1, hS0]

/-- **The additive Jucys–Murphy elements commute** — for every `d`, and with no hypothesis on `q`
beyond `H`'s own relations. -/
theorem addJM_comm (H : HeckeGenerators R A q) (d : R) (i k : ℕ) :
    addJM H d i * addJM H d k = addJM H d k * addJM H d i := by
  rcases lt_trichotomy i k with hlt | heq | hgt
  · obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
    exact addJM_comm_of_le H d i m (by omega)
  · subst heq; rfl
  · obtain ⟨m, rfl⟩ : ∃ m, i = m + 1 := ⟨i - 1, by omega⟩
    exact (addJM_comm_of_le H d k m (by omega)).symm

/-! ## Back to the multiplicative elements

The corpus's `jmRaw` and the additive family are the *same* object shifted by `1`, once `d` is the
Hecke parameter `h = q − q⁻¹`:

    L_k = 1 + A_k   with   d = q − q⁻¹.

Checking the recursion is one line: `σ_k(1 + A_k)σ_k = σ_kσ_k + σ_k A_k σ_k`, and the Hecke relation
turns the first term into `h·σ_k + 1`, which is exactly the `1` plus the `d·σ_k` that `A_{k+1}`
adds.  This is why the constant `d` had to be free: the value that identifies the two families is
forced, not chosen.

Consequence: **`jmRaw` commutes**, which is the property five direct attacks on `jmRaw` failed to
reach (bean `qou-u9o1`).  The adjacent case `[L_k, L_{k+1}] = 0` — the one case
`HeckeJucysMurphyReduction` could not close and the reason the whole reduction stayed conditional —
falls out with the rest. -/

/-- **The two families coincide up to a shift**: `L_k = 1 + A_k` at `d = q − q⁻¹`. -/
theorem jmRaw_eq_one_add_addJM (H : HeckeGenerators R A q) (k : ℕ) :
    jmRaw H k = 1 + addJM H (q - q⁻¹) k := by
  induction k with
  | zero => simp
  | succ m ih =>
      rw [jmRaw_succ, ih, addJM_succ]
      calc H.σ m * (1 + addJM H (q - q⁻¹) m) * H.σ m
          = H.σ m * H.σ m + H.σ m * addJM H (q - q⁻¹) m * H.σ m := by noncomm_ring
        _ = ((q - q⁻¹) • H.σ m + 1) + H.σ m * addJM H (q - q⁻¹) m * H.σ m := by
              rw [hecke_smul]
        _ = _ := by abel

/-- **The multiplicative Jucys–Murphy elements commute.**

`L_i L_k = L_k L_i` for all `i, k`, unconditionally.  Expanding both as `1 + A`, the cross terms are
`A_i + A_k` on each side and the quadratic term is `addJM_comm`. -/
theorem jmRaw_comm (H : HeckeGenerators R A q) (i k : ℕ) :
    jmRaw H i * jmRaw H k = jmRaw H k * jmRaw H i := by
  rw [jmRaw_eq_one_add_addJM, jmRaw_eq_one_add_addJM]
  calc (1 + addJM H (q - q⁻¹) i) * (1 + addJM H (q - q⁻¹) k)
      = 1 + addJM H (q - q⁻¹) i + addJM H (q - q⁻¹) k
          + addJM H (q - q⁻¹) i * addJM H (q - q⁻¹) k := by noncomm_ring
    _ = 1 + addJM H (q - q⁻¹) k + addJM H (q - q⁻¹) i
          + addJM H (q - q⁻¹) k * addJM H (q - q⁻¹) i := by
        rw [addJM_comm]; abel
    _ = _ := by noncomm_ring

/-- **The adjacent case**, `[L_k, L_{k+1}] = 0` — the one case `HeckeJucysMurphyReduction` could not
close, and the reason its `jmRaw_comm_all_of_all_adjacent` had to take a hypothesis. -/
theorem jmRaw_comm_adjacent (H : HeckeGenerators R A q) (i : ℕ) :
    jmRaw H i * jmRaw H (i + 1) = jmRaw H (i + 1) * jmRaw H i := jmRaw_comm H i (i + 1)

/-- **`HeckeJucysMurphyReduction`'s residual hypothesis, discharged.**  That file reduced full
commutativity to the adjacent pairs and stated the remainder as an assumption; `jmRaw_comm_adjacent`
supplies it, so the reduction now stands unconditionally. -/
theorem jmRaw_comm_all (H : HeckeGenerators R A q) :
    ∀ i j : ℕ, i ≤ j → jmRaw H i * jmRaw H j = jmRaw H j * jmRaw H i :=
  jmRaw_comm_all_of_all_adjacent H (jmRaw_comm_adjacent H)

end QOU.BraidKnot.Hecke
