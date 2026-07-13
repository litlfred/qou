import Mathlib.Tactic
import QOU.Common.BalancedQuantumTwist
import QOU.Common.HookSumComplete

/-!
# QOU.Common.TwistUnconditional — the balanced quantum-dimension twist, unconditional

Wires the general hook-sum identity (`QOU.HookSumComplete.hookSum_eq`, proved for
every sorted partition) into `QOU.BalancedQuantumTwist.balanced_quantum_twist`,
whose hook-exponent was previously supplied by the caller as a hypothesis. The
adapter instantiates the abstract twist for a concrete partition `λ` (a
weakly-decreasing `List ℕ`):

* **cells** = `range n` (the `n` numerator factors `[1], …, [n]`), `cellSz = (·+1)`;
* **hooks** = `cellsOf λ`, the sigma-Finset of `(row, col)` cells, `hookSz = hookLen`;
* the two families have equal cardinality `n = |λ|` (`card_cellsOf`);
* the hook exponent `Σ hookSz` collapses to `Σ_c h(c) = b(λ') + b(λ) + n` by
  `hookSum_eq` — a **proved theorem**, not an assumption.

The result `partition_twist` is therefore the balanced quantum-dimension twist with
the hook exponent given explicitly by `colSum λ + bStat λ + n`, with **no hook-sum
hypothesis remaining** — only the (structural) sortedness of the partition.
-/

namespace QOU.TwistUnconditional

open Finset QOU.BalancedQuantumTwist QOU.HookSumComplete

variable {K : Type*} [Field K]

/-- The cells of `λ` as a sigma-Finset of `(row, col)` pairs. -/
def cellsOf (l : List ℕ) : Finset ((_ : ℕ) × ℕ) :=
  (Finset.range l.length).sigma (fun i => Finset.range (l.getD i 0))

/-- Hook length of a cell `(i, j)`: `arm + leg + 1`. -/
def hookLenP (l : List ℕ) (c : (_ : ℕ) × ℕ) : ℕ :=
  (l.getD c.1 0 - 1 - c.2) + (colLen l c.2 - 1 - c.1) + 1

/-- The sum of hook lengths over the cells equals `hookSum` (Fubini over the sigma). -/
theorem sum_hookLenP (l : List ℕ) : ∑ c ∈ cellsOf l, hookLenP l c = hookSum l := by
  unfold cellsOf hookLenP hookSum
  rw [Finset.sum_sigma]

/-- The cell count of `λ` is `|λ| = l.sum`. -/
theorem card_cellsOf (l : List ℕ) : (cellsOf l).card = l.sum := by
  unfold cellsOf
  rw [Finset.card_sigma]
  simp only [Finset.card_range]
  exact sum_range_getD l

/-- **The unconditional balanced quantum-dimension twist for a partition.** For any
weakly-decreasing `λ` (a `List ℕ`) with column bound `M`, and `q ≠ 0` over a field,
the balanced-numerator twist holds with the hook exponent given by the **proved**
value `colSum λ M + bStat λ + l.sum = b(λ') + b(λ) + n` — the previously-hypothesised
hook-sum is now discharged by `hookSum_eq`. -/
theorem partition_twist (q : K) (hq : q ≠ 0) (l : List ℕ) (M : ℕ)
    (hsort : ∀ a b, a ≤ b → b < l.length → l.getD b 0 ≤ l.getD a 0)
    (hM : ∀ i ∈ Finset.range l.length, l.getD i 0 ≤ M) :
    q ^ (∑ c ∈ Finset.range l.sum, ((c + 1 : ℕ) : ℤ))
        * (∏ c ∈ Finset.range l.sum,
            (q ^ ((c + 1 : ℕ) : ℤ) - q ^ (-((c + 1 : ℕ) : ℤ))))
        * (∏ c ∈ cellsOf l, qintU (q ^ 2) (hookLenP l c))
      = q ^ ((colSum l M + bStat l + l.sum : ℕ) : ℤ)
        * (∏ c ∈ cellsOf l,
            (q ^ ((hookLenP l c : ℕ) : ℤ) - q ^ (-((hookLenP l c : ℕ) : ℤ))))
        * (∏ c ∈ Finset.range l.sum, qintU (q ^ 2) (c + 1)) := by
  have hcard : (Finset.range l.sum).card = (cellsOf l).card := by
    rw [Finset.card_range, card_cellsOf]
  have htwist := balanced_quantum_twist q hq (Finset.range l.sum) (cellsOf l)
    (fun c => c + 1) (hookLenP l) hcard
  have hexp : (∑ c ∈ cellsOf l, ((hookLenP l c : ℕ) : ℤ))
      = ((colSum l M + bStat l + l.sum : ℕ) : ℤ) := by
    rw [← Nat.cast_sum, sum_hookLenP, hookSum_eq l M hsort hM]
  rw [hexp] at htwist
  exact htwist

end QOU.TwistUnconditional
