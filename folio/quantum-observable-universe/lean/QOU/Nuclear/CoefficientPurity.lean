import Mathlib.Algebra.BigOperators.NatAntidiagonal
import Mathlib.LinearAlgebra.Dimension.Finrank
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas

/-!
# QOU.ShellCondensation.CoefficientPurity

Formalize-first step for the reading of `conj:homological-shell-condensation` as
Hochschild cohomology `HH^*(H_n, M)` with coefficients in a bimodule `M`, filtered
by Coxeter length (bean `qou-6qbv`).

Input not formalized here (Mathlib has no Hochschild cohomology): `H_n(q)` is
semisimple, hence separable, in characteristic 0 at real `q > 1`, so
`HH^k(H_n, M) = 0` for every `k ≥ 1` and every bimodule `M`.
-- Ref: [weibel1994] https://doi.org/10.1017/CBO9781139644136 Thm 9.2.11

1. `offDiag_vanish_of_higher_vanish`: on a first-quadrant limit page whose
   abutment vanishes in every positive degree, every entry with `q > 0` vanishes.
   So under the separability input the literal statement of the conjecture holds
   for every `n` and every `M`: it selects nothing.

2. `finrank_add_le_of_pure`: what is left is degree 0, where the limit page is the
   associated graded of `H = M^A ≤ V = M`. Purity in degree 0 (all of `H` in
   filtration degree 0, i.e. `H ≤ F⁰` and `H ⊓ F¹ = ⊥`) forces
   `dim H + dim F¹ ≤ dim F⁰`, so `dim H ≤ dim (F⁰ / F¹)`. For `M = H_n` and
   `M = H_n^*` the weight-0 slice `F⁰ / F¹` is spanned by `T_1` (resp. `T_1^*`),
   one-dimensional, while `dim M^A` is the number of partitions of `n`; so purity
   fails for every `n ≥ 2`.
-/

namespace QOU.ShellCondensation.CoefficientPurity

open Finset

/-- **Literal vanishing is automatic.** If the abutment is zero in every positive
    total degree, every entry above the bottom row of a first-quadrant page is zero. -/
theorem offDiag_vanish_of_higher_vanish (E : ℕ → ℕ → ℕ)
    (hH : ∀ k, 0 < k → ∑ x ∈ antidiagonal k, E x.1 x.2 = 0) :
    ∀ p q, 0 < q → E p q = 0 := by
  intro p q hq
  have h := hH (p + q) (by omega)
  have hmem : (p, q) ∈ antidiagonal (p + q) := by simp
  exact (Finset.sum_eq_zero_iff.mp h) (p, q) hmem

/-- **Purity in degree 0 bounds the invariants by the weight-0 slice.** -/
theorem finrank_add_le_of_pure {K V : Type*} [Field K] [AddCommGroup V] [Module K V]
    [FiniteDimensional K V] (H F0 F1 : Submodule K V) (hF : F1 ≤ F0)
    (hlow : H ≤ F0) (hhigh : H ⊓ F1 = ⊥) :
    Module.finrank K H + Module.finrank K F1 ≤ Module.finrank K F0 := by
  have h1 := Submodule.finrank_sup_add_finrank_inf_eq H F1
  rw [hhigh, finrank_bot, add_zero] at h1
  rw [← h1]
  exact Submodule.finrank_mono (sup_le hlow hF)

end QOU.ShellCondensation.CoefficientPurity
