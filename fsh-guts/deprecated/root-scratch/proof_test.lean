import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

def IsOrderThreeTermRec {K : Type*} [Field K] (b a : ℕ → K) : Prop :=
  ∀ n, a (n + 2) = b n * a (n + 1) - a n

theorem two_root_geometric {K : Type*} [Field K] (r s α β : K) (hrs : r * s = 1) :
    IsOrderThreeTermRec (fun _ => r + s) (fun n => α * r ^ n + β * s ^ n) := by
  intro n
  dsimp
  simp only [pow_succ']
  linear_combination (-(α * r ^ n + β * s ^ n)) * hrs
