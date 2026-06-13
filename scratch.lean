import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import QOU.BraidKnot.CrystalRMatrixSubLemma
import QOU.BraidKnot.CrystalGraphRealization

namespace QOU.BraidKnot.OperatorValuedCombiner

universe u

class WenzlAOperator (R : Type u) [CommRing R] (q : R)
    [CrystalGraphRealization R q] where
  combinerValue : ℕ → R
  lrWeight : ℕ → R
  branching_recursion : ∀ A : ℕ, 2 ≤ A →
    combinerValue (A + 1) = lrWeight A * combinerValue A

namespace WenzlAOperator

def iteratedCombinerValue
    {R : Type u} [CommRing R] {q : R}
    [CrystalGraphRealization R q]
    (W : WenzlAOperator R q) : ℕ → R :=
  Nat.rec (W.combinerValue 2) (fun n prev => W.lrWeight (n + 2) * prev)

theorem operator_valued_combiner_convergence
    {R : Type u} [CommRing R] {q : R}
    [CrystalGraphRealization R q]
    [W : WenzlAOperator R q] :
    ∀ n : ℕ, W.combinerValue (n + 2) = iteratedCombinerValue W n := by
  intro n
  induction n with
  | zero => rfl
  | succ k ih =>
    have h : W.combinerValue (k + 2 + 1) = W.lrWeight (k + 2) * W.combinerValue (k + 2) :=
      W.branching_recursion (k + 2) (by omega)
    have eq_idx : k + 1 + 2 = k + 2 + 1 := by omega
    rw [eq_idx]
    rw [h]
    rw [ih]
    rfl

end WenzlAOperator
end QOU.BraidKnot.OperatorValuedCombiner
