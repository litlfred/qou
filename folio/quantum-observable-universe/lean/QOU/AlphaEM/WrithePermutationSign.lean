import Mathlib.Tactic
import Mathlib.GroupTheory.Perm.Cycle.Type

/-!
# `(−1)^{writhe}` is the sign of the braid's permutation

`ι = (−1)^{writhe} · C` (`ChargeConjugationTrace`). This file identifies the sign
`(−1)^{writhe}` with the sign of the permutation a braid word induces on its strands,
and so with `(−1)^{n − c}`, where `c` counts the cycles of that permutation (the
components of the closure).

On `B₂` this is `(−1)^{2 − c}`: odd writhe exactly for knots. On `B₃` it is
`(−1)^{3 − c}`: odd writhe exactly for two-component links. So `(−1)^{writhe}` agrees
with "knots are fermions" on `T(2,n)` and disagrees with it on three strands: the
electron `σ₀σ₁σ₀` (Hopf link, `c = 2`) has odd writhe, and `T(3,5) = (σ₀σ₁)⁵` (a knot)
has even writhe.
-/

namespace QOU.AlphaEM.WrithePerm

open Equiv

/-- A letter `(i, sign)` of a braid word on `n + 1` strands. -/
abbrev Letter (n : ℕ) := Fin n × Bool

/-- The transposition a letter induces on the strands (the sign does not matter). -/
def perm {n : ℕ} : Letter n → Perm (Fin (n + 1))
  | (i, _) => swap i.castSucc i.succ

/-- The permutation of a braid word. -/
def wordPerm {n : ℕ} (w : List (Letter n)) : Perm (Fin (n + 1)) := (w.map perm).prod

/-- **The permutation sign of a braid word is `(−1)^{length}`**, i.e. `(−1)^{writhe}`. -/
theorem sign_wordPerm {n : ℕ} (w : List (Letter n)) :
    Perm.sign (wordPerm w) = (-1) ^ w.length := by
  induction w with
  | nil => simp [wordPerm]
  | cons l w ih =>
    obtain ⟨i, b⟩ := l
    have hne : i.castSucc ≠ i.succ := Fin.castSucc_lt_succ i |>.ne
    simp only [wordPerm, List.map_cons, List.prod_cons, map_mul] at ih ⊢
    rw [ih, perm, Perm.sign_swap hne, List.length_cons, pow_succ]
    exact mul_comm _ _

/-- Number of cycles of a permutation of `Fin m`, fixed points included
(the number of components of a braid closure). -/
def numCycles {m : ℕ} (σ : Perm (Fin m)) : ℕ := σ.cycleType.card + (m - σ.support.card)

/-- **Sign and cycle count:** `sign σ = (−1)^{m + c}`, equivalently `(−1)^{m − c}`. -/
theorem sign_eq_neg_one_pow_numCycles {m : ℕ} (σ : Perm (Fin m)) :
    Perm.sign σ = (-1) ^ (m + numCycles σ) := by
  have hs : σ.support.card ≤ m := by simpa using Finset.card_le_univ σ.support
  rw [Perm.sign_of_cycleType, Perm.sum_cycleType, numCycles]
  have : m + (σ.cycleType.card + (m - σ.support.card)) =
      (σ.support.card + σ.cycleType.card) + 2 * (m - σ.support.card) := by omega
  rw [this, pow_add _ (σ.support.card + σ.cycleType.card), pow_mul, neg_one_sq,
    one_pow, mul_one]

/-- **Writhe parity counts components.** For a word on `m` strands,
`(−1)^{writhe} = (−1)^{m + c}` with `c` the number of components of the closure. -/
theorem writhe_parity_eq_components {n : ℕ} (w : List (Letter n)) :
    ((-1 : ℤˣ) ^ w.length) = (-1) ^ ((n + 1) + numCycles (wordPerm w)) := by
  rw [← sign_wordPerm, sign_eq_neg_one_pow_numCycles]

/-- The electron `σ₀σ₁σ₀` has odd permutation sign; `(σ₀σ₁)⁵` has even sign. -/
theorem electron_sign :
    Perm.sign (wordPerm ([(0, true), (1, true), (0, true)] : List (Letter 2))) = -1 := by
  rw [sign_wordPerm]; decide

theorem t35_sign :
    Perm.sign (wordPerm ((List.replicate 5 [((0 : Fin 2), true), (1, true)]).flatten)) = 1 := by
  rw [sign_wordPerm]; decide

/-- The electron word closes to two components, `(σ₀σ₁)⁵` to one. -/
theorem electron_two_components :
    numCycles (wordPerm ([(0, true), (1, true), (0, true)] : List (Letter 2))) = 2 := by
  decide

theorem t35_one_component :
    numCycles (wordPerm ((List.replicate 5 [((0 : Fin 2), true), (1, true)]).flatten)) = 1 := by
  decide

end QOU.AlphaEM.WrithePerm

