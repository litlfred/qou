/-
# `𝓞 K`'s replacement for "a non-zero integer has absolute value at least one"

`RothRationalIndex` closed step 2 over `ℤ` on one fact: a non-zero rational with denominator
dividing `D` is at least `1/D` in absolute value.  Step 1's auxiliary polynomial has coefficients
in `𝓞 K`, and there the fact is false — an algebraic integer can be as small as you like at a
given archimedean place.  What survives is the **product** over all places, `|N(x)| ≥ 1`, and that
is a genuinely different statement with a genuinely different consequence.

## Why this is not a generalisation of the `ℤ` case

Over `ℤ` smallness at the one place forces vanishing.  Over `𝓞 K` it does not: `x` may be tiny at
`φ₀` and enormous elsewhere, with the product still at least `1`.  Vanishing needs smallness at
`φ₀` **and** a bound at every other place, and the trade is quantitative —

    ‖φ₀ x‖ · M^{d−1} < 1   ⟹   x = 0,

where `M` bounds the other `d−1` conjugates.  So the `𝓞 K` argument has an input the `ℤ` argument
does not: a bound on the conjugates, which is exactly what step 1's `house` estimate supplies and
what `norm_le_house` converts into per-embedding form.  Keeping the two cases separate rather than
attempting one statement covering both is deliberate; they have different hypotheses because they
are different theorems.

## What Mathlib supplies and what it does not

`Algebra.norm_eq_prod_embeddings` gives `N(x) = ∏_σ σ(x)` over `K →ₐ[ℚ] ℂ`, and
`Algebra.norm_ne_zero_iff` gives `N(x) ≠ 0` for `x ≠ 0` in `𝓞 K`.  Neither the product form over
`K →+* ℂ` (which is what `house` is stated against) nor the `1 ≤ ∏_φ ‖φ x‖` consequence is
available directly; `prod_norm_embeddings_eq_abs_norm` and `one_le_prod_norm_embeddings` build
them.  `NumberField.InfinitePlace.prod_eq_abs_norm` is the same identity re-indexed by infinite
places with multiplicities, which is the wrong shape here — `house` is a max over embeddings, not
over places, so re-indexing would have to be undone immediately.
-/
import QOU.Mathlib.RothRationalIndex
import Mathlib.NumberTheory.NumberField.House
import Mathlib.NumberTheory.NumberField.Norm
import Mathlib.RingTheory.Norm.Transitivity

open NumberField Finset

namespace MvPolynomial

variable {K : Type*} [Field K] [NumberField K]

/-- **The product formula over embeddings.**  `∏_φ ‖φ x‖ = |N_{K/ℚ}(x)|`, indexed by ring
homomorphisms `K →+* ℂ` — the indexing `house` uses. -/
theorem prod_norm_embeddings_eq_abs_norm (x : K) :
    ∏ φ : K →+* ℂ, ‖φ x‖ = |((Algebra.norm ℚ x : ℚ) : ℝ)| := by
  have key : ‖(algebraMap ℚ ℂ) (Algebra.norm ℚ x)‖ = ‖∏ σ : K →ₐ[ℚ] ℂ, σ x‖ :=
    congr_arg (‖·‖) (Algebra.norm_eq_prod_embeddings ℚ ℂ x)
  have hL : ‖(algebraMap ℚ ℂ) (Algebra.norm ℚ x)‖ = |((Algebra.norm ℚ x : ℚ) : ℝ)| := by
    rw [eq_ratCast]; simp
  have hR : ‖∏ σ : K →ₐ[ℚ] ℂ, σ x‖ = ∏ φ : K →+* ℂ, ‖φ x‖ := by
    rw [norm_prod]
    exact (Fintype.prod_equiv RingHom.equivRatAlgHom (fun f : K →+* ℂ => ‖f x‖)
      (fun φ : K →ₐ[ℚ] ℂ => ‖φ x‖) (fun _ => by simp [RingHom.equivRatAlgHom_apply])).symm
  rw [← hR, ← key, hL]

/-- **The replacement for `1 ≤ |z|`.**  A non-zero algebraic integer has `∏_φ ‖φ x‖ ≥ 1` — the
product, not any single factor. -/
theorem one_le_prod_norm_embeddings {x : 𝓞 K} (hx : x ≠ 0) :
    1 ≤ ∏ φ : K →+* ℂ, ‖φ (x : K)‖ := by
  rw [prod_norm_embeddings_eq_abs_norm, ← Algebra.coe_norm_int]
  have hn : Algebra.norm ℤ x ≠ 0 := Algebra.norm_ne_zero_iff.mpr hx
  have h1 : (1 : ℤ) ≤ |Algebra.norm ℤ x| := Int.one_le_abs hn
  have h2 : (1 : ℝ) ≤ |((Algebra.norm ℤ x : ℤ) : ℝ)| := by
    rw [← Int.cast_abs]; exact_mod_cast h1
  simpa using h2

/-- **Small at one place, bounded at the others, forces zero.**  The `𝓞 K` analogue of
`eq_zero_of_abs_lt_of_den`, and note the extra input: `M` must bound *every other* conjugate.  Over
`ℤ` there are no other conjugates and the hypothesis is vacuous, which is why the `ℤ` statement
looks simpler than it is. -/
theorem eq_zero_of_norm_mul_pow_lt_one {x : 𝓞 K} {φ₀ : K →+* ℂ} {M : ℝ}
    (hother : ∀ φ : K →+* ℂ, φ ≠ φ₀ → ‖φ (x : K)‖ ≤ M)
    (hlt : ‖φ₀ (x : K)‖ * M ^ (Fintype.card (K →+* ℂ) - 1) < 1) : x = 0 := by
  classical
  by_contra hx
  have h1 := one_le_prod_norm_embeddings hx
  have hsplit : (∏ φ : K →+* ℂ, ‖φ (x : K)‖)
      = ‖φ₀ (x : K)‖ * ∏ φ ∈ Finset.univ.erase φ₀, ‖φ (x : K)‖ :=
    (Finset.mul_prod_erase _ _ (Finset.mem_univ φ₀)).symm
  have hcard : (Finset.univ.erase φ₀).card = Fintype.card (K →+* ℂ) - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ φ₀), Finset.card_univ]
  have hbound : (∏ φ ∈ Finset.univ.erase φ₀, ‖φ (x : K)‖)
      ≤ M ^ (Fintype.card (K →+* ℂ) - 1) := by
    calc (∏ φ ∈ Finset.univ.erase φ₀, ‖φ (x : K)‖)
        ≤ ∏ _φ ∈ Finset.univ.erase φ₀, M :=
          Finset.prod_le_prod (fun φ _ => norm_nonneg _)
            (fun φ hφ => hother φ (Finset.ne_of_mem_erase hφ))
      _ = M ^ (Fintype.card (K →+* ℂ) - 1) := by rw [Finset.prod_const, hcard]
  have hφ0 : (0 : ℝ) ≤ ‖φ₀ (x : K)‖ := norm_nonneg _
  have := mul_le_mul_of_nonneg_left hbound hφ0
  rw [← hsplit] at this
  linarith

/-- **`house` bounds every conjugate.**  The bridge from step 1's height estimate, which is stated
with `house`, to the per-embedding bounds `eq_zero_of_norm_mul_pow_lt_one` consumes. -/
theorem norm_le_house (φ : K →+* ℂ) (x : K) : ‖φ x‖ ≤ house x := by
  rw [house_eq_sup']
  have h : (‖φ x‖₊ : ℝ) ≤ ((Finset.univ.sup' Finset.univ_nonempty
      (fun ψ : K →+* ℂ => ‖ψ x‖₊) : NNReal) : ℝ) := by
    exact_mod_cast Finset.le_sup' (fun ψ : K →+* ℂ => ‖ψ x‖₊) (Finset.mem_univ φ)
  simpa using h

end MvPolynomial
