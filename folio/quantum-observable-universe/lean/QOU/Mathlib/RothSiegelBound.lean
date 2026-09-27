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
import QOU.Mathlib.RothSelection

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

/-- **The condition count is positive.**  `i = 0` sits in the box with weight `0`, which is `≤ μ`
exactly when `ε ≤ 1/2`; and the integral basis is nonempty because `[K:ℚ] ≥ 1`.  This is the one
hypothesis of `exists_auxiliary_polynomial_int` that is not a growth estimate — Siegel's lemma
needs at least one equation to solve. -/
theorem card_prod_pos (r : Fin m → ℕ) {ε : ℚ} (hε2 : ε ≤ 1 / 2) (hm : 0 < m) :
    0 < Fintype.card ({i // i ∈ (idxBoxF r).filter
        (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))}
      × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) := by
  classical
  have hmQ : (0 : ℚ) < (m : ℚ) := by exact_mod_cast hm
  have hμ0 : (0 : ℚ) ≤ (m : ℚ) / 2 - ε * (m : ℚ) := by nlinarith
  have hzero : (0 : Fin m →₀ ℕ) ∈ (idxBoxF r).filter
      (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ)) := by
    rw [Finset.mem_filter]
    exact ⟨(mem_idxBoxF r 0).mpr (fun h => Nat.zero_le _), by simpa [idxWeight] using hμ0⟩
  rw [Fintype.card_prod]
  refine Nat.mul_pos (Fintype.card_pos_iff.mpr ⟨⟨0, hzero⟩⟩) ?_
  rw [card_chooseBasisIndex_eq_finrank]
  exact Module.finrank_pos

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

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **`Γ_m`'s height clause, reduced to a checkable inequality.**  The clause is about
`⌈siegelHeight⌉`, which is opaque; this replaces it by the explicit bound of `siegelHeight_le_pow`,
so what a parameter choice has to verify is an inequality between named quantities.

Nothing is lost by the replacement in the direction that matters: `siegelHeight ≤ Y` gives
`⌈siegelHeight⌉ ≤ ⌈Y⌉`, so the explicit inequality is *sufficient*.  It is not necessary, and a
parameter family that fails it might still satisfy the clause — worth knowing before anyone reads
a failure of `hY` as a failure of the argument. -/
theorem hbound_of_ceil_le [DecidableEq (K →+* ℂ)]
    (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) {B : ℝ} (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hE : 2 * Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
          ≤ Fintype.card {n // n ∈ idxBoxF r})
    (D : ℤ) (e : ℕ)
    (hY : (⌈(2 : ℝ) ^ (∑ h, r h) * max 1 (c K * (2 * B) ^ (∑ h, r h))⌉ : ℤ) ^ e ≤ D) :
    (⌈siegelHeight r α μ⌉ : ℤ) ^ e ≤ D := by
  have h0 : (0 : ℝ) ≤ siegelHeight r α μ := by
    rw [siegelHeight]
    exact Real.rpow_nonneg (by positivity) _
  have hceil : (⌈siegelHeight r α μ⌉ : ℤ)
      ≤ ⌈(2 : ℝ) ^ (∑ h, r h) * max 1 (c K * (2 * B) ^ (∑ h, r h))⌉ :=
    Int.ceil_le_ceil (siegelHeight_le_pow r α μ hB1 hα hE)
  refine le_trans (pow_le_pow_left₀ (Int.ceil_nonneg h0) hceil e) hY

end Exponent

section Integral

/-! ## The obligation, without real logarithms

The remaining condition reads naturally in logs — `log H₀ ≳ m²q·log(4B)/p` — but that form is
painful to formalise and, it turns out, unnecessary.  Exponentiating throughout leaves a purely
**integer** inequality:

    C₀^{mq} · W^{2m²q}  ≤  H₀^p

with `C₀` any integer above `c K` and `W` any integer above `4B`.  Both are constants of `K` and
`α`; neither involves `r`, `N` or the heights.  So "choose `H₀` large" is a single arithmetic
condition on `H₀` that a parameter family can be checked against directly, with no analysis.

`ceil_siegelHeight_le` turns the height bound into `⌈siegelHeight⌉ ≤ C₀·W^{Σr}`, and
`pow_le_pow_of_height` is the arithmetic: `Σr ≤ 2m·r₀` (from `sum_rothDegrees_le` once `r₀ ≥ 1`)
makes the exponent `Σr·mq` at most `2m²q·r₀`, which the condition on `H₀` then dominates once
raised to `r₀`.
-/

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **The auxiliary polynomial's height, as an integer power.**  `⌈siegelHeight⌉ ≤ C₀·W^{Σr}` for
any integers `C₀ ≥ max(1, c K)` and `W ≥ max(1, 4B)`. -/
theorem ceil_siegelHeight_le [DecidableEq (K →+* ℂ)]
    (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) {B : ℝ} (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hE : 2 * Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
          ≤ Fintype.card {n // n ∈ idxBoxF r})
    {C₀ W : ℤ} (hC₀1 : 1 ≤ C₀) (hC₀ : c K ≤ (C₀ : ℝ)) (hW : 4 * B ≤ (W : ℝ)) :
    (⌈siegelHeight r α μ⌉ : ℤ) ≤ C₀ * W ^ (∑ h, r h) := by
  have hB0 : (1 : ℝ) ≤ 2 * B := by linarith
  have hC₀R : (1 : ℝ) ≤ (C₀ : ℝ) := by exact_mod_cast hC₀1
  have hmax : max 1 (c K * (2 * B) ^ (∑ h, r h)) ≤ (C₀ : ℝ) * (2 * B) ^ (∑ h, r h) := by
    refine max_le ?_ (mul_le_mul_of_nonneg_right hC₀ (by positivity))
    have h2 : (1 : ℝ) ≤ (2 * B) ^ (∑ h, r h) := one_le_pow₀ hB0
    nlinarith
  have h2 : (2 : ℝ) ^ (∑ h, r h) * max 1 (c K * (2 * B) ^ (∑ h, r h))
      ≤ (2 : ℝ) ^ (∑ h, r h) * ((C₀ : ℝ) * (2 * B) ^ (∑ h, r h)) :=
    mul_le_mul_of_nonneg_left hmax (by positivity)
  have hpow : ((2 : ℝ) ^ (∑ h, r h)) * ((2 : ℝ) ^ (∑ h, r h)) = (4 : ℝ) ^ (∑ h, r h) := by
    rw [← mul_pow]
    norm_num
  have h3 : (2 : ℝ) ^ (∑ h, r h) * ((C₀ : ℝ) * (2 * B) ^ (∑ h, r h))
      = (C₀ : ℝ) * (4 * B) ^ (∑ h, r h) := by
    rw [mul_pow, mul_pow, ← hpow]
    ring
  have h4 : (C₀ : ℝ) * (4 * B) ^ (∑ h, r h) ≤ (C₀ : ℝ) * (W : ℝ) ^ (∑ h, r h) :=
    mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (by linarith) hW _) (by linarith)
  have h1 := siegelHeight_le_pow r α μ hB1 hα hE
  refine Int.ceil_le.mpr ?_
  push_cast
  linarith

/-- **The arithmetic.**  `A ≤ C₀·W^S` with `S ≤ 2m·r₀` and `C₀^{mq}·W^{2m²q} ≤ H₀^p` gives
`A^{mq} ≤ H₀^{r₀p}` — the height clause, from a condition on `H₀` alone. -/
theorem pow_le_pow_of_height {A C₀ W H₀ : ℤ} {S r₀ m q p : ℕ}
    (hA0 : 0 ≤ A) (hA : A ≤ C₀ * W ^ S) (hC₀1 : 1 ≤ C₀) (hW1 : 1 ≤ W)
    (hS : S ≤ 2 * m * r₀) (hr₀ : 1 ≤ r₀)
    (hH : C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ H₀ ^ p) :
    A ^ (m * q) ≤ H₀ ^ (r₀ * p) := by
  have hC₀0 : (0 : ℤ) ≤ C₀ := le_trans zero_le_one hC₀1
  have hW0 : (0 : ℤ) ≤ W := le_trans zero_le_one hW1
  have hbase : (0 : ℤ) ≤ C₀ ^ (m * q) * W ^ (2 * m * m * q) := by positivity
  -- the left side, expanded
  have hL : A ^ (m * q) ≤ C₀ ^ (m * q) * W ^ (S * (m * q)) := by
    calc A ^ (m * q) ≤ (C₀ * W ^ S) ^ (m * q) := pow_le_pow_left₀ hA0 hA _
      _ = C₀ ^ (m * q) * W ^ (S * (m * q)) := by rw [mul_pow, ← pow_mul]
  have hexp : S * (m * q) ≤ 2 * m * m * q * r₀ := by nlinarith [hS, Nat.zero_le (m * q)]
  have hL2 : C₀ ^ (m * q) * W ^ (S * (m * q))
      ≤ C₀ ^ (m * q) * W ^ (2 * m * m * q * r₀) :=
    mul_le_mul_of_nonneg_left (pow_le_pow_right₀ hW1 hexp) (by positivity)
  -- the right side, expanded
  have hR : (C₀ ^ (m * q) * W ^ (2 * m * m * q)) ^ r₀ ≤ (H₀ ^ p) ^ r₀ :=
    pow_le_pow_left₀ hbase hH _
  have hRexp : (H₀ ^ p) ^ r₀ = H₀ ^ (r₀ * p) := by rw [← pow_mul, mul_comm]
  have hRL : C₀ ^ (m * q) * W ^ (2 * m * m * q * r₀)
      ≤ (C₀ ^ (m * q) * W ^ (2 * m * m * q)) ^ r₀ := by
    rw [mul_pow, ← pow_mul, ← pow_mul]
    refine mul_le_mul_of_nonneg_right ?_ (by positivity)
    exact pow_le_pow_right₀ hC₀1 (by nlinarith [hr₀, Nat.zero_le (m * q)])
  rw [← hRexp]
  exact le_trans hL (le_trans hL2 (le_trans hRL hR))

/-- `T ≤ H₀` gives `T ≤ H₀^p` for `p ≥ 1`, so a **floor on the selected heights** discharges the
height clause's premise — and the selection already takes a floor. -/
theorem le_pow_of_le {T H₀ : ℤ} {p : ℕ} (hT1 : 1 ≤ T) (hp : 1 ≤ p) (h : T ≤ H₀) :
    T ≤ H₀ ^ p := by
  have hH₀1 : 1 ≤ H₀ := le_trans hT1 h
  calc T ≤ H₀ := h
    _ = H₀ ^ 1 := (pow_one H₀).symm
    _ ≤ H₀ ^ p := pow_le_pow_right₀ hH₀1 hp

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **`Γ_m`'s height clause, from a floor on the heights.**  Everything the clause needs, reduced
to `C₀^{mq}·W^{2m²q} ≤ H₀` — a condition the selection's own floor parameter can be set to.

So the near-circularity is fully resolved in the formal chain, not only in the argument: the
threshold is a constant of `K`, `α`, `m`, `p`, `q`, the selection takes it as its floor, and the
height clause follows. Nothing in it refers to `N`, `r`, or the auxiliary polynomial. -/
theorem hbound_of_height_floor [DecidableEq (K →+* ℂ)]
    (H : Fin m → ℕ) (N : ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) {B : ℝ} (hB1 : 1 ≤ B)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hE : 2 * Fintype.card ({i // i ∈ (idxBoxF (rothDegrees H N)).filter
            (fun i => idxWeight (rothDegrees H N) i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
          ≤ Fintype.card {n // n ∈ idxBoxF (rothDegrees H N)})
    {C₀ W : ℤ} (hC₀1 : 1 ≤ C₀) (hC₀ : c K ≤ (C₀ : ℝ)) (hW1 : 1 ≤ W) (hW : 4 * B ≤ (W : ℝ))
    {p q : ℕ} (hp : 1 ≤ p)
    (hmono : ∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k)
    (hH2 : ∀ h, 2 ≤ H h)
    (hr₀ : ∀ j : Fin m, (j : ℕ) = 0 → 1 ≤ rothDegrees H N j)
    (hfloor : ∀ j : Fin m, (j : ℕ) = 0 →
      C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (H j : ℤ)) :
    ∀ j : Fin m, (j : ℕ) = 0 →
      (⌈siegelHeight (rothDegrees H N) α μ⌉ : ℤ) ^ (m * q)
        ≤ (H j : ℤ) ^ (rothDegrees H N j * p) := by
  intro j hj
  have hsh0 : (0 : ℝ) ≤ siegelHeight (rothDegrees H N) α μ := by
    rw [siegelHeight]
    exact Real.rpow_nonneg (by positivity) _
  have hone : (1 : ℤ) ≤ C₀ ^ (m * q) * W ^ (2 * m * m * q) := by
    have h1 : (1 : ℤ) ≤ C₀ ^ (m * q) := one_le_pow₀ hC₀1
    have h2 : (1 : ℤ) ≤ W ^ (2 * m * m * q) := one_le_pow₀ hW1
    nlinarith
  -- `Σ r ≤ 2m·r₀`, using that the heights increase so `H j` is the smallest
  have hdj : rothDegrees H N j = Nat.log (H j) N := by rw [rothDegrees, if_pos hj]
  have hsum : ∑ h, rothDegrees H N h ≤ 2 * m * rothDegrees H N j := by
    have hb : 1 < H j := lt_of_lt_of_le one_lt_two (hH2 j)
    have hle : ∀ h, H j ≤ H h := fun h => hmono j h (by omega)
    have h1 := sum_rothDegrees_le H N (H j) hb hle
    have h2 := hr₀ j hj
    rw [hdj] at h2 ⊢
    calc ∑ h, rothDegrees H N h ≤ m * (Nat.log (H j) N + 1) := h1
      _ ≤ m * (2 * Nat.log (H j) N) := Nat.mul_le_mul le_rfl (by omega)
      _ = 2 * m * Nat.log (H j) N := by ring
  exact pow_le_pow_of_height (Int.ceil_nonneg hsh0)
    (ceil_siegelHeight_le (rothDegrees H N) α μ hB1 hα hE hC₀1 hC₀ hW)
    hC₀1 hW1 hsum (hr₀ j hj) (le_pow_of_le hone hp (hfloor j hj))

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **All seven clauses of `Γ_m`, at the auxiliary polynomial's own height.**  Not an implication:
the height clause is discharged here, so what comes out is `RothGammaFull` itself, instantiated at
`b = ⌈siegelHeight r α μ⌉` — the very bound Siegel's lemma hands step 1.

This is where the near-circularity finally closes.  `hbound` is a statement about the produced
`H` and `N`, and `b` is a *function* of them, so neither can be a hypothesis of the existential.
The resolution is that the threshold `C₀^{mq}·W^{2m²q}` refers to none of the produced data — it
is a constant of `K`, `α`, `m`, `p`, `q` alone — so it can be handed to the selection as its floor
parameter `T` and recovered afterwards from `T ≤ H j`.  `T` is taken as a parameter above that
threshold rather than equal to it, because later stages impose floors of their own and the
selection can only be given one.

The hypotheses that remain are each a fact about one fixed object:

* `hfloorExp` pins `F` against `m`, `p`, `q` (the `Γ_m` exponent clause, unchanged);
* `hm2 : 2·[K:ℚ] < 4ε²m` is the **doubled** unknowns-beat-conditions threshold, i.e. `m > [K:ℚ]/2ε²`
  — doubled because Siegel's exponent must be ≤ 1, not merely finite, or the height is doubly
  exponential in `Σ r`;
* `hα` bounds the houses of the `α h` by `B`, and `hC₀`/`hW` name integers above `c K` and `4B`.

Nothing here mentions `N`, `r`, or the polynomial. -/
theorem exists_rothGammaFull_auxiliary [DecidableEq (K →+* ℂ)] {S : Set ℕ}
    (hS : ∀ N, ∃ q ∈ S, N ≤ q) (p q F k : ℕ) (hp : 0 < p) (hq : 0 < q) (hF : 1 ≤ F)
    (hfloorExp : q * ((m - 1) * m * (2 * m + 1)) ≤ F * p)
    (α : Fin m → 𝓞 K) {ε : ℚ} (hε : 0 < ε)
    (hm2 : 2 * ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    {C₀ W : ℤ} (hC₀1 : 1 ≤ C₀) (hC₀ : c K ≤ (C₀ : ℝ)) (hW1 : 1 ≤ W) (hW : 4 * B ≤ (W : ℝ))
    (T : ℕ) (hT : C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (T : ℤ)) :
    ∃ (H : Fin m → ℕ) (N : ℕ), (∀ h, H h ∈ S) ∧ N ≠ 0 ∧ (∀ h, 2 ≤ H h) ∧ (∀ h, T ≤ H h) ∧
      (∀ h : Fin m, rothDegrees H N h ≠ 0) ∧ (∀ h : Fin m, (H h) ^ k ≤ N) ∧
      (∀ j k : Fin m, (j : ℕ) ≤ (k : ℕ) → H j ≤ H k) ∧
      RothGammaFull (Equiv.refl (Fin m)) p q F (rothDegrees H N) (fun j => (H j : ℤ))
        ⌈siegelHeight (rothDegrees H N) α ((m : ℚ) / 2 - ε * (m : ℚ))⌉ := by
  classical
  obtain ⟨H, N, hmem, hN, hH2, hTle, hmono, hlarge, hkpow, himp⟩ :=
    exists_rothGammaFull_of_supply hS m p q F
      (fun H N => ⌈siegelHeight (rothDegrees H N) α ((m : ℚ) / 2 - ε * (m : ℚ))⌉) hp hq
      T k hF hfloorExp
  -- the degrees are positive: `p + 2q ≤ p·r h` forces `r h ≠ 0`
  have hrne : ∀ h, rothDegrees H N h ≠ 0 := by
    intro h hcon
    have hh := hlarge h
    rw [hcon, Nat.mul_zero] at hh
    omega
  refine ⟨H, N, hmem, hN, hH2, hTle, hrne, hkpow, hmono, himp ?_⟩
  -- the floor parameter, recovered from the produced heights
  have hfloor : ∀ j : Fin m, (j : ℕ) = 0 →
      C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (H j : ℤ) := by
    intro j _
    exact le_trans hT (Int.ofNat_le.mpr (hTle j))
  exact hbound_of_height_floor H N α ((m : ℚ) / 2 - ε * (m : ℚ)) hB1 hα
    (two_card_prod_le_card_idxBoxF (rothDegrees H N) hrne hε hm2)
    hC₀1 hC₀ hW1 hW hp hmono hH2 (fun j _ => Nat.one_le_iff_ne_zero.mpr (hrne j)) hfloor

end Integral

end MvPolynomial
