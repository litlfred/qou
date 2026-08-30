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

section Exponent

/-! ## Siegel's exponent, and why the counting threshold needs a factor of two

`siegelHeight` is `(#box · ‖A‖)^ρ` with `ρ = #E/(#box − #E)`.  The two size estimates above make
the *base* well behaved — both factors are `C^{Σr}` — but that is worth nothing while `ρ` is
unbounded, and the counting condition proved so far only gives `#E < #box`, hence
`#box − #E ≥ 1` and `ρ ≤ #E`.  With `#E` itself exponential in `Σr`, that bound makes
`siegelHeight` **doubly** exponential and the whole argument fails.

The fix is a factor of two in the threshold: asking `2·deg α < 4ε²m` instead of `deg α < 4ε²m`
gives `2·#E ≤ #box`, hence `ρ ≤ 1` and `siegelHeight ≤ #box·‖A‖`.  "Take `m` large" becomes
`m > deg α/(2ε²)` rather than `m > deg α/(4ε²)` — a factor of two in `m`, bought to avoid a
double exponential.  Worth stating because the weaker threshold is the one the variance argument
naturally produces, and it is not enough.
-/

/-- **The threshold with room to spare.**  `2·deg α < 4ε²m` makes the vanishing conditions at most
half the unknowns, which is what bounds Siegel's exponent. -/
theorem two_card_prod_le_card_idxBoxF (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0) {ε : ℚ} (hε : 0 < ε)
    (hm : 2 * ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ)) :
    2 * Fintype.card ({i // i ∈ (idxBoxF r).filter
          (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
      ≤ Fintype.card {n // n ∈ idxBoxF r} := by
  have h := nsmul_fintypeCard_idxWeight_lt r hr (2 * Module.finrank ℚ K) hε (by push_cast; exact_mod_cast hm)
  rw [Fintype.card_prod, card_chooseBasisIndex_eq_finrank]
  calc 2 * (Fintype.card {i // i ∈ (idxBoxF r).filter
          (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))} * Module.finrank ℚ K)
      = 2 * Module.finrank ℚ K * Fintype.card {i // i ∈ (idxBoxF r).filter
          (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))} := by ring
    _ ≤ Fintype.card {n // n ∈ idxBoxF r} := le_of_lt h

/-- **Siegel's exponent is at most one**, and then the height is at most its base. -/
theorem siegelHeight_le_base (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ)
    (hE : 2 * Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
          ≤ Fintype.card {n // n ∈ idxBoxF r}) :
    siegelHeight r α μ
      ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ) * max 1 ‖auxMatrixInt r α μ‖ := by
  classical
  have hbox : 1 ≤ Fintype.card {n // n ∈ idxBoxF r} := by
    rw [Fintype.card_coe, card_idxBoxF]
    exact card_idxBox_pos r
  have hboxR : (1 : ℝ) ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ) := by exact_mod_cast hbox
  have hnorm : (1 : ℝ) ≤ max 1 ‖auxMatrixInt r α μ‖ := le_max_left _ _
  have hX1 : (1 : ℝ) ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ)
      * max 1 ‖auxMatrixInt r α μ‖ := by nlinarith
  have hden : (0 : ℝ) < (Fintype.card {n // n ∈ idxBoxF r} : ℝ)
      - (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
          × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ) := by
    have : (2 : ℝ) * (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)
        ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ) := by exact_mod_cast hE
    nlinarith [Nat.cast_nonneg (α := ℝ) (Fintype.card
      ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K)))]
  have hrho : (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)
      / ((Fintype.card {n // n ∈ idxBoxF r} : ℝ)
        - (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)) ≤ 1 := by
    rw [div_le_one hden]
    have : (2 : ℝ) * (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)
        ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ) := by exact_mod_cast hE
    linarith
  rw [siegelHeight]
  calc ((Fintype.card {n // n ∈ idxBoxF r} : ℝ) * max 1 ‖auxMatrixInt r α μ‖) ^ _
      ≤ ((Fintype.card {n // n ∈ idxBoxF r} : ℝ) * max 1 ‖auxMatrixInt r α μ‖) ^ (1 : ℝ) :=
        Real.rpow_le_rpow_of_exponent_le hX1 hrho
    _ = (Fintype.card {n // n ∈ idxBoxF r} : ℝ) * max 1 ‖auxMatrixInt r α μ‖ :=
        Real.rpow_one _

open private c c_nonneg from Mathlib.NumberTheory.NumberField.House in
/-- **The auxiliary polynomial's height, explicitly.**  Combining the exponent bound with the two
size estimates: `siegelHeight ≤ 2^{Σr}·max(1, c(K)·(2B)^{Σr})`.

Taking logs, `log(siegelHeight) ≤ (Σ r_h)·log 2 + max(0, log c(K) + (Σ r_h)·log(2B))` — **linear in
`Σ r_h`, with every constant independent of `r`**.  That is the statement `Γ_m`'s height clause
needs, and the one whose absence made `hbound` look circular. -/
theorem siegelHeight_le_pow [DecidableEq (K →+* ℂ)]
    (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) {B : ℝ} (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hE : 2 * Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
          ≤ Fintype.card {n // n ∈ idxBoxF r}) :
    siegelHeight r α μ ≤ (2 : ℝ) ^ (∑ h, r h) * max 1 (c K * (2 * B) ^ (∑ h, r h)) := by
  refine le_trans (siegelHeight_le_base r α μ hE) ?_
  have h1 : (Fintype.card {n // n ∈ idxBoxF r} : ℝ) ≤ (2 : ℝ) ^ (∑ h, r h) := by
    exact_mod_cast card_idxBoxF_le_two_pow r
  have h2 : max 1 ‖auxMatrixInt r α μ‖ ≤ max 1 (c K * (2 * B) ^ (∑ h, r h)) :=
    max_le_max le_rfl (norm_auxMatrixInt_le_house r α μ hB1 hα)
  have h3 : (0 : ℝ) ≤ max 1 ‖auxMatrixInt r α μ‖ := le_trans zero_le_one (le_max_left _ _)
  have h4 : (0 : ℝ) ≤ (2 : ℝ) ^ (∑ h, r h) := by positivity
  exact mul_le_mul h1 h2 h3 h4

end Exponent

end MvPolynomial
