import QOU.BraidKnot.HeckeBoundedTransposition

/-!
# `jmRaw_comm` on the bounded presentation — the last item on `qou-t1kv`

Tranche 3, assembling the transposition machinery into Jucys's telescoping argument and landing
**`jmRawB_comm`**: the Jucys–Murphy elements of a bounded presentation commute.

## The final bound is the natural one

`jmRawB_comm` holds for `i < n` and `k < n` — exactly "both `Lᵢ` and `L_k` are elements of
`H_n(q)`".  Nothing stronger is needed, and nothing weaker suffices: `L_i` is a word in
`σ₀ … σ_{i−1}`, so `i < n` is already forced for it to be well-formed.

## Bounds, and the four lemmas that need none

| lemma | bound |
|---|---|
| `sigma_comm_addJMB` | `i < n` |
| `sigma_comm_addJMB_small` | `j + 1 < n` |
| `sigma_comm_partialSumB` | `m < n` |
| `sigma_comm_partialSumB_above` | `j + 1 < n` |
| `sigma_comm_partialSumB_ne` | `m < n` **and** `j + 1 < n` |
| `comm_transpB_of_comm_sigma` | **none** |
| `comm_addJMB_of_comm_sigma` | **none** |
| `partialSumB_succ` | **none** |
| `addJMB_comm_of_le` | `m + 1 < n` |
| `addJMB_comm` | `i < n`, `k < n` |

`sigma_comm_partialSumB_ne` is the only place needing **two** bounds, and for a real reason: it
splits on `j < m` versus `j > m`, and the two branches constrain different indices.  A single
hypothesis would have been wrong on one side.

## Why this route rather than the product half

Jucys's telescoping argument — `A_{m+1} = S_{m+1} − S_m` — never touches the product half of
Mathas 3.24(iii), which `addJMB_sigma_prod_swap` shows only *swaps* the factors and is entangled
with the conclusion it was meant to supply.  The bounded port inherits that virtue unchanged.
-/

namespace QOU.BraidKnot.Hecke

open Finset

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-! ## §1  `σ_j` commutes with `A_i` -/

/-- **Mathas 3.24(i)**, the `i > j+1` case: `σ_j` commutes with `A_i`.

Split `Σ_{l<i} T_(l,i)` on `l`: below `j` it is `disjoint`, above `j+1` it is `below`, and the two
middle terms commute only **as a pair**. -/
theorem sigma_comm_addJMB (H : HeckeGeneratorsBelow R A q n) (d : R) (j i : ℕ)
    (h : j + 1 < i) (hin : i < n) :
    H.σ j * addJMB H d i = addJMB H d i * H.σ j := by
  have hne : j ≠ j + 1 := by omega
  have hsub : ({j, j + 1} : Finset ℕ) ⊆ Finset.range i := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp [Finset.mem_range] <;> omega
  have hpair : ∑ l ∈ ({j, j + 1} : Finset ℕ), transpB H l i
      = transpB H j i + transpB H (j + 1) i := Finset.sum_pair hne
  have hrest : H.σ j * (∑ l ∈ Finset.range i \ {j, j + 1}, transpB H l i)
      = (∑ l ∈ Finset.range i \ {j, j + 1}, transpB H l i) * H.σ j := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun l hl => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hl
    obtain ⟨hli, hlj, hlj1⟩ := hl
    rcases Nat.lt_or_ge l j with hlt | hge
    · exact sigma_comm_transpB_disjoint H j l hlt i h hin
    · exact sigma_comm_transpB_below H j l (by omega) i hli hin
  rw [addJMB_eq_transpB_sum, ← Finset.sum_sdiff hsub, hpair]
  rw [mul_smul_comm, smul_mul_assoc, mul_add, add_mul, hrest,
    sigma_comm_transpB_pair H j i h hin]

/-- **3.24(i), the easy direction**: `σ_j` commutes with `A_i` when `i < j`. -/
theorem sigma_comm_addJMB_small (H : HeckeGeneratorsBelow R A q n) (d : R) (j i : ℕ)
    (h : i < j) (hjn : j + 1 < n) :
    H.σ j * addJMB H d i = addJMB H d i * H.σ j := by
  rw [addJMB_eq_transpB_sum, mul_smul_comm, smul_mul_assoc]
  congr 1
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun l hl => ?_
  exact sigma_comm_transpB_far H l i j (Finset.mem_range.mp hl) h hjn

/-! ## §2  Partial-sum centrality -/

/-- Partial sum `S_m = Σ_{i ≤ m} A_i`. -/
def partialSumB (H : HeckeGeneratorsBelow R A q n) (d : R) (m : ℕ) : A :=
  ∑ i ∈ Finset.range (m + 1), addJMB H d i

/-- **Centrality below the cutoff**: for `j < m`, `σ_j` commutes with `S_m`. -/
theorem sigma_comm_partialSumB (H : HeckeGeneratorsBelow R A q n) (d : R) (j m : ℕ)
    (h : j < m) (hmn : m < n) :
    H.σ j * partialSumB H d m = partialSumB H d m * H.σ j := by
  have hne : j ≠ j + 1 := by omega
  have hsub : ({j, j + 1} : Finset ℕ) ⊆ Finset.range (m + 1) := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp only [Finset.mem_range] <;> omega
  have hpair : ∑ i ∈ ({j, j + 1} : Finset ℕ), addJMB H d i
      = addJMB H d j + addJMB H d (j + 1) := Finset.sum_pair hne
  have hrest : H.σ j * (∑ i ∈ Finset.range (m + 1) \ {j, j + 1}, addJMB H d i)
      = (∑ i ∈ Finset.range (m + 1) \ {j, j + 1}, addJMB H d i) * H.σ j := by
    rw [Finset.mul_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i hi => ?_
    simp only [Finset.mem_sdiff, Finset.mem_range, Finset.mem_insert,
      Finset.mem_singleton, not_or] at hi
    obtain ⟨him, hij, hij1⟩ := hi
    rcases Nat.lt_or_ge i j with hlt | hge
    · exact sigma_comm_addJMB_small H d j i hlt (by omega)
    · exact sigma_comm_addJMB H d j i (by omega) (by omega)
  unfold partialSumB
  rw [← Finset.sum_sdiff hsub, hpair, mul_add, add_mul, hrest,
    addJMB_sigma_comm_add H d j (by omega)]

/-- **Centrality above the cutoff**: for `j > m`, `σ_j` commutes with `S_m`. -/
theorem sigma_comm_partialSumB_above (H : HeckeGeneratorsBelow R A q n) (d : R) (j m : ℕ)
    (h : m < j) (hjn : j + 1 < n) :
    H.σ j * partialSumB H d m = partialSumB H d m * H.σ j := by
  unfold partialSumB
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun i hi => ?_
  exact sigma_comm_addJMB_small H d j i (by have := Finset.mem_range.mp hi; omega) hjn

/-- **Jucys's centrality property**: `σ_j` commutes with `S_m` for every `j ≠ m`.

Two bounds, because the two branches constrain different indices. -/
theorem sigma_comm_partialSumB_ne (H : HeckeGeneratorsBelow R A q n) (d : R) (j m : ℕ)
    (h : j ≠ m) (hmn : m < n) (hjn : j + 1 < n) :
    H.σ j * partialSumB H d m = partialSumB H d m * H.σ j := by
  rcases Nat.lt_or_ge j m with hlt | hge
  · exact sigma_comm_partialSumB H d j m hlt hmn
  · exact sigma_comm_partialSumB_above H d j m (by omega) hjn

/-! ## §3  Word lifting — no bounds needed -/

/-- If `X` commutes with every `σ_j` for `j < i`, it commutes with `T_(l,i)`.

**No bound**: this is `transpB`'s recursion and the hypothesis, with no relation of `H` used. -/
theorem comm_transpB_of_comm_sigma (H : HeckeGeneratorsBelow R A q n) (X : A) (l : ℕ) :
    ∀ i : ℕ, l < i → (∀ j, j < i → X * H.σ j = H.σ j * X) →
      X * transpB H l i = transpB H l i * X := by
  intro i
  induction i with
  | zero => intro h; omega
  | succ k ih =>
      intro hl hX
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hl) with heq | hlt
      · subst heq
        rw [transpB_self]
        exact hX l (by omega)
      · have hlk : l ≠ k := by omega
        have hk : X * H.σ k = H.σ k * X := hX k (by omega)
        have hih := ih hlt (fun j hj => hX j (by omega))
        rw [transpB_succ H l k hlk]
        calc X * (H.σ k * transpB H l k * H.σ k)
            = (X * H.σ k) * transpB H l k * H.σ k := by noncomm_ring
          _ = (H.σ k * X) * transpB H l k * H.σ k := by rw [hk]
          _ = H.σ k * (X * transpB H l k) * H.σ k := by noncomm_ring
          _ = H.σ k * (transpB H l k * X) * H.σ k := by rw [hih]
          _ = H.σ k * transpB H l k * (X * H.σ k) := by noncomm_ring
          _ = H.σ k * transpB H l k * (H.σ k * X) := by rw [hk]
          _ = _ := by noncomm_ring

/-- The same lift for `A_i`.  **No bound** — it rides on the relation-free sum expansion. -/
theorem comm_addJMB_of_comm_sigma (H : HeckeGeneratorsBelow R A q n) (d : R) (X : A) (i : ℕ)
    (hX : ∀ j, j < i → X * H.σ j = H.σ j * X) :
    X * addJMB H d i = addJMB H d i * X := by
  rw [addJMB_eq_transpB_sum, mul_smul_comm, smul_mul_assoc]
  congr 1
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun l hl => ?_
  exact comm_transpB_of_comm_sigma H X l i (Finset.mem_range.mp hl) hX

/-! ## §4  Telescoping -/

theorem partialSumB_succ (H : HeckeGeneratorsBelow R A q n) (d : R) (m : ℕ) :
    partialSumB H d (m + 1) = partialSumB H d m + addJMB H d (m + 1) :=
  Finset.sum_range_succ _ _

/-- **The telescoping step**: `A_i` commutes with `A_{m+1}` whenever `i ≤ m`. -/
theorem addJMB_comm_of_le (H : HeckeGeneratorsBelow R A q n) (d : R) (i m : ℕ)
    (h : i ≤ m) (hmn : m + 1 < n) :
    addJMB H d i * addJMB H d (m + 1) = addJMB H d (m + 1) * addJMB H d i := by
  have hS1 : partialSumB H d (m + 1) * addJMB H d i = addJMB H d i * partialSumB H d (m + 1) :=
    comm_addJMB_of_comm_sigma H d _ i fun j hj =>
      (sigma_comm_partialSumB_ne H d j (m + 1) (by omega) hmn (by omega)).symm
  have hS0 : partialSumB H d m * addJMB H d i = addJMB H d i * partialSumB H d m :=
    comm_addJMB_of_comm_sigma H d _ i fun j hj =>
      (sigma_comm_partialSumB_ne H d j m (by omega) (by omega) (by omega)).symm
  have hsplit : addJMB H d (m + 1) = partialSumB H d (m + 1) - partialSumB H d m := by
    rw [partialSumB_succ]; abel
  rw [hsplit, mul_sub, sub_mul, hS1, hS0]

/-- **The additive Jucys–Murphy elements commute**, for every `d`. -/
theorem addJMB_comm (H : HeckeGeneratorsBelow R A q n) (d : R) (i k : ℕ)
    (hin : i < n) (hkn : k < n) :
    addJMB H d i * addJMB H d k = addJMB H d k * addJMB H d i := by
  rcases lt_trichotomy i k with hlt | heq | hgt
  · obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
    exact addJMB_comm_of_le H d i m (by omega) (by omega)
  · subst heq; rfl
  · obtain ⟨m, rfl⟩ : ∃ m, i = m + 1 := ⟨i - 1, by omega⟩
    exact (addJMB_comm_of_le H d k m (by omega) (by omega)).symm

/-! ## §5  Back to the multiplicative elements -/

/-- **The two families coincide up to a shift**: `L_k = 1 + A_k` at `d = q − q⁻¹`. -/
theorem jmRawB_eq_one_add_addJMB (H : HeckeGeneratorsBelow R A q n) (k : ℕ) (hkn : k < n) :
    jmRawB H k = 1 + addJMB H (q - q⁻¹) k := by
  induction k with
  | zero => simp
  | succ m ih =>
      rw [jmRawB_succ, ih (by omega), addJMB_succ]
      calc H.σ m * (1 + addJMB H (q - q⁻¹) m) * H.σ m
          = H.σ m * H.σ m + H.σ m * addJMB H (q - q⁻¹) m * H.σ m := by noncomm_ring
        _ = ((q - q⁻¹) • H.σ m + 1) + H.σ m * addJMB H (q - q⁻¹) m * H.σ m := by
              rw [heckeB_smul H m (by omega)]
        _ = _ := by abel

/-- **The multiplicative Jucys–Murphy elements commute** on a bounded presentation.

`Lᵢ L_k = L_k Lᵢ` for all `i, k < n` — the last item of `qou-t1kv`.  Expanding both as `1 + A`, the
cross terms are `A_i + A_k` on each side and the quadratic term is `addJMB_comm`. -/
theorem jmRawB_comm (H : HeckeGeneratorsBelow R A q n) (i k : ℕ) (hin : i < n) (hkn : k < n) :
    jmRawB H i * jmRawB H k = jmRawB H k * jmRawB H i := by
  rw [jmRawB_eq_one_add_addJMB H i hin, jmRawB_eq_one_add_addJMB H k hkn]
  calc (1 + addJMB H (q - q⁻¹) i) * (1 + addJMB H (q - q⁻¹) k)
      = 1 + addJMB H (q - q⁻¹) i + addJMB H (q - q⁻¹) k
          + addJMB H (q - q⁻¹) i * addJMB H (q - q⁻¹) k := by noncomm_ring
    _ = 1 + addJMB H (q - q⁻¹) k + addJMB H (q - q⁻¹) i
          + addJMB H (q - q⁻¹) k * addJMB H (q - q⁻¹) i := by
        rw [addJMB_comm H _ i k hin hkn]; abel
    _ = _ := by noncomm_ring

/-- **The adjacent case**, `[L_k, L_{k+1}] = 0`. -/
theorem jmRawB_comm_adjacent (H : HeckeGeneratorsBelow R A q n) (i : ℕ) (h : i + 1 < n) :
    jmRawB H i * jmRawB H (i + 1) = jmRawB H (i + 1) * jmRawB H i :=
  jmRawB_comm H i (i + 1) (by omega) h

/-- Recovers the unbounded `jmRaw_comm` through the downcast. -/
theorem jmRaw_comm_of_below (H : HeckeGenerators R A q) (i k : ℕ) :
    jmRaw H i * jmRaw H k = jmRaw H k * jmRaw H i := by
  have := jmRawB_comm (H.toBelow (i + k + 1)) i k (by omega) (by omega)
  rwa [jmRawB_toBelow, jmRawB_toBelow] at this

/-- The commutator difference of two unbounded Jucys-Murphy elements vanishes (`qou-l1gv`). -/
theorem jmRaw_comm_sub_eq_zero (H : HeckeGenerators R A q) (i k : ℕ) :
    jmRaw H i * jmRaw H k - jmRaw H k * jmRaw H i = 0 := by
  rw [jmRaw_comm_of_below H i k, sub_self]

/-! ## §6  The payoff: the JM elements of the 2-dimensional block commute -/

section StdThree

variable {K : Type*} [Field K]

/-- **`L₁` and `L₂` commute on the 2-dimensional `(2,1)` representation of `H₃(q)`.**

Unreachable from `jmRaw_comm`: `stdTwo_no_stable_extension` proves the unbounded presentation
cannot host this representation at all. -/
theorem stdTwoBelow3_jmRaw_comm (q : K) (hq : q ≠ 0) (i k : ℕ) (hi : i < 3) (hk : k < 3) :
    jmRawB (stdTwoBelow3 q hq) i * jmRawB (stdTwoBelow3 q hq) k
      = jmRawB (stdTwoBelow3 q hq) k * jmRawB (stdTwoBelow3 q hq) i :=
  jmRawB_comm (stdTwoBelow3 q hq) i k hi hk

end StdThree

end QOU.BraidKnot.Hecke
