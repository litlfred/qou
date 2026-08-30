/-
# The two size estimates `hbound`'s cancellation rests on

`RothSelection` showed `Γ_m`'s last clause is not circular, and proved the half that carries the
argument (`hbound_mono`).  The other half was an asymptotic estimate the arc had not written down:
that `#box` and `‖auxMatrixInt‖` both grow like `exp(c·∑_h r_h)`, so that the `log N` on the two
sides of `b^{mq} ≤ H₀^{r₀p}` cancels.  This file writes it down.

## Where the constant comes from, and why it is a hypothesis

`#box ≤ 2^{Σr}` is immediate — the box is `∏(r_h + 1)`.

`‖auxMatrixInt‖` is the sup norm of the *integral-basis coordinates* of `translateMatrix α i n`.
Bounding a coordinate by a norm is a finite-dimensionality fact with a constant attached, and the
constant depends on the basis, not on `r` or `n` — which is exactly why the estimate factors as
`C · (2B)^{Σr}` with `C` inert.  Mathlib has that comparison as
`NumberField.house.basis_repr_norm_le_const_mul_house`, stated for the reindexed `integralBasis`
with a `private` constant.

`norm_auxMatrixInt_le` takes the comparison as the hypothesis `hC` rather than reaching into that
private constant.  The split is deliberate: the growth in `Σr` is what the cancellation needs and
is proved here unconditionally, while `hC` is a fact about `K` alone that a caller supplies once.
Bundling them would have hidden which half was doing the work.
-/
import QOU.Mathlib.RothAuxiliaryInt
import QOU.Mathlib.RothHouseBound

open NumberField Finset

attribute [local instance] Matrix.seminormedAddCommGroup

namespace MvPolynomial

variable {K : Type*} [Field K] [NumberField K] {m : ℕ}

/-- **The box, in the budget's currency.**  `#box ≤ 2^{Σ r_h}` — the unknown count grows only
exponentially in the total degree. -/
theorem card_idxBoxF_le_two_pow (r : Fin m → ℕ) :
    Fintype.card {n // n ∈ idxBoxF r} ≤ 2 ^ (∑ h, r h) := by
  classical
  rw [Fintype.card_coe, card_idxBoxF, card_idxBox]
  exact prod_succ_le_two_pow_sum r

/-- **The matrix, in the same currency.**  `‖auxMatrixInt‖ ≤ C·(2B)^{Σ r_h}`, with `C` a constant
of `K` and `B` a bound on the `house` of the `α_h`.

`C` is inert in `r`, which is the point: taking logs gives `log‖A‖ ≤ log C + (Σ r_h)·log(2B)`, so
the matrix contributes to `log b` only through `Σ r_h` — and that is what cancels the `log N` in
`Γ_m`'s height clause. -/
theorem norm_auxMatrixInt_le (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ)
    {C B : ℝ} (hC0 : 0 ≤ C) (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hC : ∀ (x : 𝓞 K) (l : Module.Free.ChooseBasisIndex ℤ (𝓞 K)),
      |(((RingOfIntegers.basis K).repr x l : ℤ) : ℝ)|
        ≤ C * house ((algebraMap (𝓞 K) K) x)) :
    ‖auxMatrixInt r α μ‖ ≤ C * (2 * B) ^ (∑ h, r h) := by
  classical
  have hB0 : (0 : ℝ) ≤ 2 * B := by linarith
  have hB1' : (1 : ℝ) ≤ 2 * B := by linarith
  refine (Matrix.norm_le_iff (by positivity)).mpr (fun il n => ?_)
  -- the entry is an integral-basis coordinate of a translate matrix entry
  have hentry : ‖auxMatrixInt r α μ il n‖
      = |(((RingOfIntegers.basis K).repr
          (translateMatrix α (il.1 : Fin m →₀ ℕ) (n : Fin m →₀ ℕ)) il.2 : ℤ) : ℝ)| := by
    rw [auxMatrixInt, Int.norm_eq_abs]
  rw [hentry]
  refine le_trans (hC _ _) ?_
  -- the `house` of the translate matrix entry, bounded by the peeling estimate
  have hhouse : house ((algebraMap (𝓞 K) K)
      (translateMatrix α (il.1 : Fin m →₀ ℕ) (n : Fin m →₀ ℕ)))
      ≤ (2 * B) ^ ((n : Fin m →₀ ℕ).sum fun _ e => e) := by
    rw [translateMatrix_map (algebraMap (𝓞 K) K) α]
    exact seminorm_translateMatrix_le submultSeminorm_house _ hB1 hα _ _ rfl _
  -- and the total degree of a box element is at most `Σ r_h`
  have hdeg : ((n : Fin m →₀ ℕ).sum fun _ e => e) ≤ ∑ h, r h := by
    rw [Finsupp.sum_fintype _ _ (fun _ => rfl)]
    exact Finset.sum_le_sum (fun h _ => (mem_idxBoxF r _).mp n.2 h)
  exact mul_le_mul_of_nonneg_left
    (le_trans hhouse (pow_le_pow_right₀ hB1' hdeg)) hC0

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **The coordinate comparison, discharged from Mathlib.**  `hC` above is not an assumption about
the arc — it is a fact about `K`, and this is it: an integral-basis coordinate of `x` is at most a
constant of `K` times the `house` of `x`.

The constant is `Mathlib`'s `private c`, reached the same way `RothAuxiliary` reaches `c₁`.  Its
value does not matter here; what matters is that it does not depend on `r`, `n` or `α`. -/
theorem abs_basis_repr_le [DecidableEq (K →+* ℂ)]
    (x : 𝓞 K) (l : Module.Free.ChooseBasisIndex ℤ (𝓞 K)) :
    |(((RingOfIntegers.basis K).repr x l : ℤ) : ℝ)|
      ≤ c K * house ((algebraMap (𝓞 K) K) x) := by
  have h := NumberField.house.basis_repr_norm_le_const_mul_house K x ((equivReindex K).symm l)
  have hrepr : ((integralBasis K).reindex (equivReindex K).symm).repr
      ((algebraMap (𝓞 K) K) x) ((equivReindex K).symm l)
      = (((RingOfIntegers.basis K).repr x l : ℤ) : ℚ) := by
    rw [Module.Basis.repr_reindex_apply, Equiv.symm_symm, Equiv.apply_symm_apply,
      integralBasis_repr_apply]
    simp
  rw [hrepr] at h
  simpa using h

open private c c_nonneg from Mathlib.NumberTheory.NumberField.House in
/-- **The matrix bound, unconditional.**  `norm_auxMatrixInt_le` with its one hypothesis supplied
from `abs_basis_repr_le`, so the arc owes nothing here.

Together with `card_idxBoxF_le_two_pow` this is the missing half of `hbound`'s non-circularity:
both `#box` and `‖A‖` are bounded by constants of `K` and `α` raised to `Σ r_h`, so `log b` is
linear in `Σ r_h`, which is what lets the `log N` cancel. -/
theorem norm_auxMatrixInt_le_house [DecidableEq (K →+* ℂ)]
    (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) {B : ℝ} (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B) :
    ‖auxMatrixInt r α μ‖ ≤ c K * (2 * B) ^ (∑ h, r h) :=
  norm_auxMatrixInt_le r α μ (c_nonneg K) hB1 hα (fun x l => abs_basis_repr_le x l)

end MvPolynomial
