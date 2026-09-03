import QOU.BraidKnot.HeckeBoundedAdditiveJM
import QOU.BraidKnot.HeckeTranspositionExpansion

/-!
# The transposition expansion on the bounded presentation

Tranche 2 of porting `jmRaw_comm` (bean `qou-t1kv`).  This is the bound-heavy half: the
sum-of-transpositions expansion of the additive Jucys–Murphy family, and the three commutation
lemmas that make `σ_j` commute with `A_i`.

## The bounds, derived per lemma

`transpB H l i` is a word in `σ_l … σ_{i−1}`, so it is well-formed for `i < n`.

| lemma | relation used | bound |
|---|---|---|
| `transpB_self` / `transpB_succ` | **none** | — |
| `addJMB_eq_transpB_sum` | **none** | — |
| `sigma_comm_transpB_pair` | `braid j`, `hecke (j+1)`, `far j m` | `i < n` |
| `sigma_comm_transpB_far` | `far · m` | `m + 1 < n` |
| `sigma_comm_transpB_base` | `braid j`, and `far` via the previous | `j + 2 < n` |
| `sigma_comm_transpB_disjoint` | `far j m`, and the base case | `i < n` |
| `sigma_comm_transpB_below` | `far j m`, `far j l` | `i < n` |

The expansion `A_k = d · Σ_{i<k} T_(i,k)` needs **no bound at all** — it is the two recursions and
`Finset` algebra, with no Hecke, braid or far relation anywhere.  That is the same phenomenon as
`runB_peel_bot` in the full-twist port, and it is worth stating: the sum expansion, which is the
*conceptual* heart of the argument, is relation-free.  What costs bounds is only the commutation.

`sigma_comm_transpB_far` is the one lemma whose bound is on a **different index** than the
statement's `i`: it commutes `σ_m` past `T_(l,i)` for `m > i`, so it is `m`, not `i`, that has to be
a generator.
-/

namespace QOU.BraidKnot.Hecke

open Finset

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-! ## §1  The transposition element -/

/-- **The transposition `T_(i,k)`** on a bounded presentation, as a conjugate of a generator. -/
def transpB (H : HeckeGeneratorsBelow R A q n) (i : ℕ) : ℕ → A
  | 0 => 1
  | (k + 1) => if i = k then H.σ k else H.σ k * transpB H i k * H.σ k

@[simp] theorem transpB_self (H : HeckeGeneratorsBelow R A q n) (k : ℕ) :
    transpB H k (k + 1) = H.σ k := by
  rw [transpB]; simp

theorem transpB_succ (H : HeckeGeneratorsBelow R A q n) (i k : ℕ) (h : i ≠ k) :
    transpB H i (k + 1) = H.σ k * transpB H i k * H.σ k := by
  rw [transpB]; simp [h]

@[simp] theorem transpB_toBelow (H : HeckeGenerators R A q) (n i : ℕ) :
    ∀ k, transpB (H.toBelow n) i k = transp H i k
  | 0 => rfl
  | (k + 1) => by
      by_cases h : i = k
      · subst h; rw [transpB_self, transp_self, toBelow_σ]
      · rw [transpB_succ (H.toBelow n) i k h, transp_succ H i k h, transpB_toBelow H n i k,
          toBelow_σ]

/-- **The sum-of-transpositions expansion**: `A_k = d · Σ_{i<k} T_(i,k)`.

**No bound.**  Two recursions and `Finset` algebra — no Hecke, braid or far relation is used. -/
theorem addJMB_eq_transpB_sum (H : HeckeGeneratorsBelow R A q n) (d : R) (k : ℕ) :
    addJMB H d k = d • ∑ i ∈ range k, transpB H i k := by
  induction k with
  | zero => simp [addJMB]
  | succ m ih =>
      rw [addJMB_succ, ih, Finset.sum_range_succ]
      have hterm : ∀ i ∈ range m, transpB H i (m + 1) = H.σ m * transpB H i m * H.σ m := by
        intro i hi
        exact transpB_succ H i m (by have := Finset.mem_range.mp hi; omega)
      rw [Finset.sum_congr rfl hterm, transpB_self]
      calc H.σ m * (d • ∑ i ∈ range m, transpB H i m) * H.σ m + d • H.σ m
          = d • (H.σ m * (∑ i ∈ range m, transpB H i m) * H.σ m) + d • H.σ m := by
            rw [mul_smul_comm, smul_mul_assoc]
        _ = d • (∑ i ∈ range m, H.σ m * transpB H i m * H.σ m) + d • H.σ m := by
            rw [Finset.mul_sum, Finset.sum_mul]
        _ = _ := by rw [← smul_add]

/-! ## §2  The pair-swap law -/

/-- **Pair-swap law**: for `i > j+1`, `σ_j` commutes with `T_(j,i) + T_(j+1,i)`.

The base case needs the **Hecke** relation at `j+1` as well as the braid relation at `j`; both are
covered by `i < n`, since the base sits at `i = j + 2`. -/
theorem sigma_comm_transpB_pair (H : HeckeGeneratorsBelow R A q n) (j : ℕ) :
    ∀ i : ℕ, j + 1 < i → i < n →
      H.σ j * (transpB H j i + transpB H (j + 1) i)
        = (transpB H j i + transpB H (j + 1) i) * H.σ j := by
  intro i
  induction i with
  | zero => intro h _; omega
  | succ m ih =>
      intro hm hmn
      rcases Nat.lt_or_ge (j + 1) m with hlt | hge
      · have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega) (by omega)
        have hjm : j ≠ m := by omega
        have hj1m : j + 1 ≠ m := by omega
        have hih := ih hlt (by omega)
        rw [transpB_succ H j m hjm, transpB_succ H (j + 1) m hj1m]
        calc H.σ j * (H.σ m * transpB H j m * H.σ m + H.σ m * transpB H (j + 1) m * H.σ m)
            = (H.σ j * H.σ m) * (transpB H j m + transpB H (j + 1) m) * H.σ m := by
              noncomm_ring
          _ = (H.σ m * H.σ j) * (transpB H j m + transpB H (j + 1) m) * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * (transpB H j m + transpB H (j + 1) m)) * H.σ m := by noncomm_ring
          _ = H.σ m * ((transpB H j m + transpB H (j + 1) m) * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * (transpB H j m + transpB H (j + 1) m) * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * (transpB H j m + transpB H (j + 1) m) * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring
      · have hmeq : m = j + 1 := by omega
        subst hmeq
        have hb : H.σ j * H.σ (j + 1) * H.σ j
            = H.σ (j + 1) * H.σ j * H.σ (j + 1) := H.braid j (by omega)
        have hh : H.σ (j + 1) * H.σ (j + 1) = (q - q⁻¹) • H.σ (j + 1) + 1 :=
          heckeB_smul H (j + 1) (by omega)
        have hj : j ≠ j + 1 := by omega
        rw [transpB_succ H j (j + 1) hj, transpB_self, transpB_self]
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

/-! ## §3  Disjoint transpositions -/

/-- `σ_m` commutes with `T_(l,i)` when `m > i`.  The bound is on `m`, not `i`. -/
theorem sigma_comm_transpB_far (H : HeckeGeneratorsBelow R A q n) (l : ℕ) :
    ∀ i m : ℕ, l < i → i < m → m + 1 < n →
      H.σ m * transpB H l i = transpB H l i * H.σ m := by
  intro i
  induction i with
  | zero => intro m h _; omega
  | succ k ih =>
      intro m hl hm hmn
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hl) with heq | hlt
      · subst heq
        rw [transpB_self]
        exact (H.far l m (by omega) hmn).symm ▸ (H.far l m (by omega) hmn)
      · have hlk : l ≠ k := by omega
        have hfar : H.σ m * H.σ k = H.σ k * H.σ m := (H.far k m (by omega) hmn).symm
        have hih := ih m hlt (by omega) hmn
        rw [transpB_succ H l k hlk]
        calc H.σ m * (H.σ k * transpB H l k * H.σ k)
            = (H.σ m * H.σ k) * transpB H l k * H.σ k := by noncomm_ring
          _ = (H.σ k * H.σ m) * transpB H l k * H.σ k := by rw [hfar]
          _ = H.σ k * (H.σ m * transpB H l k) * H.σ k := by noncomm_ring
          _ = H.σ k * (transpB H l k * H.σ m) * H.σ k := by rw [hih]
          _ = H.σ k * transpB H l k * (H.σ m * H.σ k) := by noncomm_ring
          _ = H.σ k * transpB H l k * (H.σ k * H.σ m) := by rw [hfar]
          _ = _ := by noncomm_ring

/-- **The hard base case**: `σ_j` commutes with `T_(l,j+2)` for `l < j`.  Braid only, no Hecke. -/
theorem sigma_comm_transpB_base (H : HeckeGeneratorsBelow R A q n) (j l : ℕ) (hl : l < j)
    (hjn : j + 2 < n) :
    H.σ j * transpB H l (j + 2) = transpB H l (j + 2) * H.σ j := by
  have hb : H.σ j * H.σ (j + 1) * H.σ j = H.σ (j + 1) * H.σ j * H.σ (j + 1) :=
    H.braid j (by omega)
  have hXv : H.σ (j + 1) * transpB H l j = transpB H l j * H.σ (j + 1) :=
    sigma_comm_transpB_far H l j (j + 1) hl (by omega) (by omega)
  have h1 : l ≠ j + 1 := by omega
  have h2 : l ≠ j := by omega
  rw [show j + 2 = (j + 1) + 1 from rfl, transpB_succ H l (j + 1) h1, transpB_succ H l j h2]
  calc H.σ j * (H.σ (j + 1) * (H.σ j * transpB H l j * H.σ j) * H.σ (j + 1))
      = (H.σ j * H.σ (j + 1) * H.σ j) * transpB H l j * (H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = (H.σ (j + 1) * H.σ j * H.σ (j + 1)) * transpB H l j
          * (H.σ j * H.σ (j + 1)) := by rw [hb]
    _ = H.σ (j + 1) * H.σ j * (H.σ (j + 1) * transpB H l j)
          * (H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = H.σ (j + 1) * H.σ j * (transpB H l j * H.σ (j + 1))
          * (H.σ j * H.σ (j + 1)) := by rw [hXv]
    _ = H.σ (j + 1) * H.σ j * transpB H l j
          * (H.σ (j + 1) * H.σ j * H.σ (j + 1)) := by noncomm_ring
    _ = H.σ (j + 1) * H.σ j * transpB H l j
          * (H.σ j * H.σ (j + 1) * H.σ j) := by rw [← hb]
    _ = _ := by noncomm_ring

/-- **Disjoint transpositions commute**: `σ_j` commutes with `T_(l,i)` for `l < j` and `i > j+1`. -/
theorem sigma_comm_transpB_disjoint (H : HeckeGeneratorsBelow R A q n) (j l : ℕ) (hl : l < j) :
    ∀ i : ℕ, j + 1 < i → i < n → H.σ j * transpB H l i = transpB H l i * H.σ j := by
  intro i
  induction i with
  | zero => intro h _; omega
  | succ m ih =>
      intro hm hmn
      rcases Nat.lt_or_ge (j + 1) m with hlt | hge
      · have hli : l ≠ m := by omega
        have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega) (by omega)
        have hih := ih hlt (by omega)
        rw [transpB_succ H l m hli]
        calc H.σ j * (H.σ m * transpB H l m * H.σ m)
            = (H.σ j * H.σ m) * transpB H l m * H.σ m := by noncomm_ring
          _ = (H.σ m * H.σ j) * transpB H l m * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * transpB H l m) * H.σ m := by noncomm_ring
          _ = H.σ m * (transpB H l m * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * transpB H l m * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * transpB H l m * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring
      · have hme : m = j + 1 := by omega
        subst hme
        exact sigma_comm_transpB_base H j l hl (by omega)

/-- `σ_j` commutes with `T_(l,i)` when `j + 1 < l`. -/
theorem sigma_comm_transpB_below (H : HeckeGeneratorsBelow R A q n) (j l : ℕ) (hjl : j + 1 < l) :
    ∀ i : ℕ, l < i → i < n → H.σ j * transpB H l i = transpB H l i * H.σ j := by
  intro i
  induction i with
  | zero => intro h _; omega
  | succ m ih =>
      intro hm hmn
      rcases Nat.eq_or_lt_of_le (Nat.lt_succ_iff.mp hm) with heq | hlt
      · subst heq
        rw [transpB_self]
        exact H.far j l (by omega) (by omega)
      · have hlm : l ≠ m := by omega
        have hfar : H.σ j * H.σ m = H.σ m * H.σ j := H.far j m (by omega) (by omega)
        have hih := ih hlt (by omega)
        rw [transpB_succ H l m hlm]
        calc H.σ j * (H.σ m * transpB H l m * H.σ m)
            = (H.σ j * H.σ m) * transpB H l m * H.σ m := by noncomm_ring
          _ = (H.σ m * H.σ j) * transpB H l m * H.σ m := by rw [hfar]
          _ = H.σ m * (H.σ j * transpB H l m) * H.σ m := by noncomm_ring
          _ = H.σ m * (transpB H l m * H.σ j) * H.σ m := by rw [hih]
          _ = H.σ m * transpB H l m * (H.σ j * H.σ m) := by noncomm_ring
          _ = H.σ m * transpB H l m * (H.σ m * H.σ j) := by rw [hfar]
          _ = _ := by noncomm_ring

end QOU.BraidKnot.Hecke
