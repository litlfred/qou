import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Mass.LinearChainBondCount — the θ_λ multiplicity as the linear-chain bond count

The atomic braid is a **linear chain** of `A` nucleon blocks (braid recipe: blocks
joined by inter-nucleon crossings at generators `3k−1`). Two combinatorial facts,
proved here, fix the θ_λ body-order multiplicity `M_n = (n−1)` with **no fit**:

- a linear `n`-chain has exactly `(n−1)` inter-nucleon bonds (`chainBonds`);
- summing the bond count over all consecutive `n`-sub-clusters of an `A`-chain,
  `Σ_{k<A} (A−k)·k`, equals `C(A+1,3) = (A−1)·A·(A+1)/6`
  (`linear_chain_cluster_measure`, stated `×6` to stay in `ℕ`).

Only the **combinatorial multiplicity** is formalised here. The binding *magnitude*
`B(K)=m_e·Σ(n−1)·Vol_n(K)` (which reproduces ³H to 0.16%) is empirical — it multiplies
these counts by hyperbolic link volumes + `m_e`, and is **not** a Lean claim.
-/

namespace QOU.Mass

open Finset

/-- The number of inter-nucleon bonds in a linear chain of `n` nucleons is `n−1`. -/
def chainBonds (n : ℕ) : ℕ := n - 1

@[simp] theorem chainBonds_two : chainBonds 2 = 1 := rfl
@[simp] theorem chainBonds_three : chainBonds 3 = 2 := rfl

/-- **Aggregate cluster measure of the linear `A`-chain.**  Summing the bond count
    `(n−1)` over the `(A−n+1)` consecutive `n`-sub-clusters, for `n = 2..A`, equals
    `C(A+1,3)`.  Reindexed by `k = n−1` this is `Σ_{k<A} (A−k)·k`; stated `×6` to
    avoid `ℕ` division.  (E.g. `A=4`: `0+3+4+3 = 10 = C(5,3)`.) -/
theorem linear_chain_cluster_measure (A : ℕ) :
    6 * ∑ k ∈ Finset.range A, (A - k) * k = (A - 1) * A * (A + 1) := by
  induction A with
  | zero => simp
  | succ n ih =>
      -- rewrite (n+1−k) = (n−k)+1 on range (n+1), then split the sum
      have hcong :
          ∑ k ∈ Finset.range (n + 1), (n + 1 - k) * k
            = (∑ k ∈ Finset.range (n + 1), (n - k) * k)
              + ∑ k ∈ Finset.range (n + 1), k := by
        rw [← Finset.sum_add_distrib]
        refine Finset.sum_congr rfl (fun k hk => ?_)
        rw [Finset.mem_range] at hk
        rw [Nat.succ_sub (Nat.lt_succ_iff.mp hk), Nat.succ_mul]
      -- the (n−k) sum loses its top (k = n) term since (n−n) = 0
      have hpeel :
          ∑ k ∈ Finset.range (n + 1), (n - k) * k
            = ∑ k ∈ Finset.range n, (n - k) * k := by
        rw [Finset.sum_range_succ, Nat.sub_self, Nat.zero_mul, add_zero]
      -- 6·Σ_{k<n+1} k = 3·(n+1)·n  (Gauss, ×3)
      have hsix : 6 * ∑ k ∈ Finset.range (n + 1), k = 3 * ((n + 1) * n) := by
        have hg := Finset.sum_range_id_mul_two (n + 1)   -- (Σ)*2 = (n+1)*(n+1−1)
        rw [Nat.add_sub_cancel] at hg                    -- (n+1−1) → n
        calc 6 * ∑ k ∈ Finset.range (n + 1), k
            = 3 * ((∑ k ∈ Finset.range (n + 1), k) * 2) := by ring
          _ = 3 * ((n + 1) * n) := by rw [hg]
      rw [hcong, hpeel, Nat.mul_add, ih, hsix, Nat.add_sub_cancel]
      -- goal: (n−1)·n·(n+1) + 3·((n+1)·n) = n·(n+1)·(n+2)
      rcases n with _ | m
      · rfl
      · simp only [Nat.add_sub_cancel]   -- (m+1)−1 → m
        ring

/-- The `A = 2` (deuteron) chain: one bond. -/
example : chainBonds 2 = 1 := rfl

/-- Sanity: the aggregate measure at `A = 4` is `C(5,3) = 10` (×6 = 60). -/
example : 6 * ∑ k ∈ Finset.range 4, (4 - k) * k = 60 := by
  rw [linear_chain_cluster_measure]

end QOU.Mass
