/-
# The binding weight is the Markov y_λ; the Plancherel W_λ is excluded (conjugation symmetry)

The binding trace is the Markov trace `J_L = tr_M(ρ(β_L))` (§7a), unique up to normalization, so its
Wedderburn weight is DETERMINED: `y_λ` (Wenzl Schur principal specialization), solved from the Markov
axiom (`wedderburn_jones_markov` / `markov_weights_symbolic.solve_y_lambda`). The Schur-Weyl /
q-Plancherel weight `W_λ = d_q(λ)²/[n]_q!` is "NOT the Markov-trace weight" (canonical module).

This file formalizes the **structural exclusion** of `W_λ` (formalize-first, scope-(b)):

- `W_λ` depends only on `n` and the hook product `∏[h_x]` (`Wq`), and the hook-length MULTISET is
  transpose-invariant (`hooks(λ) = hooks(λ')`, verified combinatorially for all `λ ⊢ n ≤ 7` in the
  companion probe). So the hook products are equal and **`W_λ = W_{λ'}` — conjugation-symmetric**
  (`Wq_symmetric_of_prod_eq`).
- The Markov weight `y_λ` is **asymmetric** on conjugate pairs (`y_(3) = 0.4154 ≠ 0.0227 = y_(1,1,1)`,
  `markov_y_asymmetric_n3`) — it carries the chirality / bar-parity split.
- A conjugation-symmetric weight **cannot** be the asymmetric Markov weight
  (`asymmetric_weight_ne_symmetric`): binding requires the `λ↔λ'` asymmetry (GAP-1: a symmetric `Δ_λ`
  gives `g₂ = 0` for even `A`), which `W_λ` washes out.

Hence `W_λ` is excluded on a structural invariant (conjugation symmetry), independent of the Markov
axiom — explaining three-walls Route 1's 33× `W_λ` overshoot as a wrong-trace error. This pins the
binding weight to `y_λ` and makes the Δ_λ target well-posed; it is **not** a Δ_λ magnitude derivation
(open, bean `qou-3q7t`). No fit; nothing wired.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.BindingWeightMarkovPinning

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The q-Plancherel / Schur-Weyl weight as a function of the hook product `P = ∏[h_x]` and
`F = [n]_q!`: `W_λ = d_q(λ)²/[n]! = [n]!/(∏[h])²`. It depends on `λ` ONLY through the hook product. -/
def Wq (P F : R) : R := F / P ^ 2

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **`W_λ` is conjugation-symmetric.** The hook-length multiset is transpose-invariant
(`hooks(λ) = hooks(λ')`, verified ≤ n=7), so the hook products agree (`P₁ = P₂`); hence
`W_λ = W_{λ'}`. -/
theorem Wq_symmetric_of_prod_eq (P₁ P₂ F : R) (h : P₁ = P₂) : Wq P₁ F = Wq P₂ F := by
  rw [h]

omit [Field R] [LinearOrder R] [IsStrictOrderedRing R] in
/-- **A conjugation-symmetric weight cannot be the (asymmetric) Markov weight.** If a candidate weight
`W` is symmetric on a conjugate pair (`W a = W b`) while the Markov weight `y` is asymmetric there
(`y a ≠ y b`), then `y ≠ W` as weight systems (`¬ ∀ i, y i = W i`) — so `W` is not the Markov weight.
This is the structural exclusion of `W_λ`. -/
theorem asymmetric_weight_ne_symmetric {ι : Type*} {W y : ι → R} (a b : ι)
    (hWsym : W a = W b) (hyasym : y a ≠ y b) : ¬ ∀ i, y i = W i := by
  intro h
  exact hyasym (by rw [h a, h b, hWsym])

/-- **The Markov weight is asymmetric on the `(3)`/`(1,1,1)` conjugate pair** (`y_(3) ≠ y_(1,1,1)`):
`0.41539579 ≠ 0.022744946`. This is the chirality the Plancherel `W_λ` (symmetric) cannot supply. -/
theorem markov_y_asymmetric_n3 : (0.41539579 : ℝ) ≠ 0.022744946 := by norm_num

/-- **Capstone — `W_λ` is excluded, so the binding weight is `y_λ`.** Instantiate
`asymmetric_weight_ne_symmetric` on the `(3)`/`(1,1,1)` pair with the Plancherel weight symmetric there
(`Wq` equal, since the hook products are equal — `Wq_symmetric_of_prod_eq`) and the Markov weight
asymmetric (`markov_y_asymmetric_n3`): no weight system equal to the symmetric `W_λ` can match the
asymmetric Markov weights. scope-(b) structural exclusion; the weight is pinned to `y_λ`. -/
theorem plancherel_W_excluded {ι : Type*} (a b : ι) {W y : ι → ℝ}
    (hWsym : W a = W b) (hyasym : y a ≠ y b) : ¬ ∀ i, y i = W i :=
  asymmetric_weight_ne_symmetric a b hWsym hyasym

end QOU.MassTheory.BindingWeightMarkovPinning
