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
import QOU.Mathlib.RothTaylorBound
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

section Index

open Finsupp in
/-- A finite sum of elements each in the image of a ring hom is in the image. -/
theorem exists_preimage_sum {R S ι : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (t : Finset ι) (g : ι → S) (h : ∀ n ∈ t, ∃ y : R, f y = g n) :
    ∃ y : R, f y = ∑ n ∈ t, g n := by
  classical
  induction t using Finset.induction with
  | empty => exact ⟨0, by simp⟩
  | insert a t ha ih =>
      obtain ⟨ya, hya⟩ := h a (Finset.mem_insert_self a t)
      obtain ⟨yt, hyt⟩ := ih (fun n hn => h n (Finset.mem_insert_of_mem hn))
      refine ⟨ya + yt, ?_⟩
      rw [Finset.sum_insert ha, map_add, hya, hyt]

/-- The per-monomial denominator statement with the degree bound folded in. -/
theorem exists_int_mul_translateMatrix_deg {m : ℕ} (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) {n : Fin m →₀ ℕ} (hnr : ∀ h, n h ≤ r h)
    (i : Fin m →₀ ℕ) :
    ∃ z : ℤ, (∏ h, (qd h : ℚ) ^ (r h)) *
      translateMatrix (fun h => (pn h : ℚ) / (qd h : ℚ)) i n = (z : ℚ) := by
  obtain ⟨zn, hzn⟩ :=
    exists_int_mul_translateMatrix pn qd hq (n.sum fun _ e => e) n rfl i
  have hD : (∏ h, (qd h : ℚ) ^ (r h))
      = (∏ h, (qd h : ℚ) ^ (r h - n h)) * (∏ h, (qd h : ℚ) ^ (n h)) := by
    rw [← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl (fun h _ => ?_)
    rw [← pow_add]
    congr 1
    have := hnr h
    omega
  refine ⟨(∏ h, (qd h : ℤ) ^ (r h - n h)) * zn, ?_⟩
  rw [hD]
  push_cast
  linear_combination (∏ h, (qd h : ℚ) ^ (r h - n h)) * hzn

variable {m : ℕ}

/-- **`∏ q_h^{r_h}` clears the denominator over `𝓞 K` too.**  The rational-point matrix entries are
rational, so the `ℤ` computation is reused verbatim; what changes is only that the coefficients it
is multiplied against are algebraic integers rather than rational ones. -/
theorem exists_ringOfIntegers_mul_coeff_translate (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) (P : MvPolynomial (Fin m) (𝓞 K))
    (hdeg : ∀ h, degreeOf h P ≤ r h) (i : Fin m →₀ ℕ) :
    ∃ y : 𝓞 K, (algebraMap (𝓞 K) K) y
      = ((∏ h, (qd h) ^ (r h) : ℕ) : K)
        * coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
            (map (algebraMap (𝓞 K) K) P)) := by
  classical
  rw [coeff_translate_eq_sum, Finset.mul_sum]
  refine exists_preimage_sum _ _ _ (fun n hn => ?_)
  have hnP : n ∈ P.support := support_map_subset (algebraMap (𝓞 K) K) P hn
  have hnr : ∀ h, n h ≤ r h := fun h => le_trans (monomial_le_degreeOf h hnP) (hdeg h)
  obtain ⟨z, hz⟩ := exists_int_mul_translateMatrix_deg pn qd hq r hnr i
  refine ⟨coeff n P * (z : 𝓞 K), ?_⟩
  have htm : translateMatrix (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ))) i n
      = algebraMap ℚ K (translateMatrix (fun h => (pn h : ℚ) / (qd h : ℚ)) i n) :=
    (translateMatrix_map (algebraMap ℚ K) _ i n).symm
  have hDcast : (((∏ h, (qd h) ^ (r h) : ℕ)) : K)
      = algebraMap ℚ K (∏ h, (qd h : ℚ) ^ (r h)) := by
    push_cast
    simp
  have hz' : (((∏ h, (qd h) ^ (r h) : ℕ)) : K)
      * algebraMap ℚ K (translateMatrix (fun h => (pn h : ℚ) / (qd h : ℚ)) i n)
      = ((z : ℤ) : K) := by
    rw [hDcast, ← map_mul, hz]
    exact map_intCast _ z
  rw [map_mul, coeff_map, htm, map_intCast]
  linear_combination (-((algebraMap (𝓞 K) K) (coeff n P))) * hz'

/-- **Step 2's index lower bound over `𝓞 K`.**  Every low-weight translated coefficient that is
small at `φ₀` and bounded at the other conjugates vanishes, and enough vanishing is a lower bound
on the index.

The hypothesis is a *pair* per coefficient, unlike the `ℤ` case's single bound: `M` at the other
`d−1` conjugates and smallness at `φ₀` measured against `M^{d−1}`.  That asymmetry is the whole
difference between `|N(x)| ≥ 1` and `|z| ≥ 1`. -/
theorem le_index_of_norm_lt (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    (r : Fin m → ℕ) (P : MvPolynomial (Fin m) (𝓞 K)) (hdeg : ∀ h, degreeOf h P ≤ r h)
    (φ₀ : K →+* ℂ) {M : ℝ} {ν : ℚ}
    (hsmall : ∀ i : Fin m →₀ ℕ, idxWeight r i < ν →
      (∀ φ : K →+* ℂ, φ ≠ φ₀ →
          ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
            * ‖φ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
                (map (algebraMap (𝓞 K) K) P)))‖ ≤ M)
        ∧ ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
            * ‖φ₀ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
                (map (algebraMap (𝓞 K) K) P)))‖
            * M ^ (Fintype.card (K →+* ℂ) - 1) < 1) :
    ((ν : ℚ) : WithTop ℚ)
      ≤ index r (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
          (map (algebraMap (𝓞 K) K) P) := by
  classical
  have hDpos : 0 < ∏ h, (qd h) ^ (r h) :=
    Finset.prod_pos (fun h _ => pow_pos (Nat.pos_of_ne_zero (hq h)) _)
  have hDne : ((∏ h, (qd h) ^ (r h) : ℕ)) ≠ 0 := hDpos.ne'
  refine (le_index_iff_coeff_eq_zero r _ _ ν).mpr (fun i hi => ?_)
  obtain ⟨y, hy⟩ := exists_ringOfIntegers_mul_coeff_translate pn qd hq r P hdeg i
  obtain ⟨hother, hlt⟩ := hsmall i hi
  have hnorm : ∀ φ : K →+* ℂ, ‖φ ((algebraMap (𝓞 K) K) y)‖
      = ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
        * ‖φ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
            (map (algebraMap (𝓞 K) K) P)))‖ := by
    intro φ
    rw [hy, map_mul, map_natCast, norm_mul, Complex.norm_natCast]
  have hy0 : y = 0 := by
    refine eq_zero_of_norm_mul_pow_lt_one (φ₀ := φ₀) (M := M) (fun φ hφ => ?_) ?_
    · rw [hnorm φ]; exact hother φ hφ
    · rw [hnorm φ₀]; exact hlt
  rw [hy0, map_zero] at hy
  have hDK : (((∏ h, (qd h) ^ (r h) : ℕ)) : K) ≠ 0 := Nat.cast_ne_zero.mpr hDne
  exact (mul_eq_zero.mp hy.symm).resolve_left hDK

/-- **`‖·‖` on `ℂ` is a submultiplicative seminorm.**  So every estimate in `RothTaylorBound`
applies at a complex embedding of a number field — which is exactly what the `𝓞 K` case needs,
since there the smallness is measured at one embedding while the others carry only the `house`
bound.  Generalising those estimates from `|·|` on `ℝ` to an arbitrary `SubmultSeminorm` was
cheaper than a second copy of the peeling induction, and this is the whole cost of the
`ℂ` case. -/
theorem submultSeminorm_norm_complex : SubmultSeminorm (norm : ℂ → ℝ) :=
  ⟨fun a => norm_nonneg a, norm_zero, le_of_eq norm_one, norm_add_le, norm_mul_le⟩

end Index

section Embedding

variable {m : ℕ}

/-- **An embedding commutes with translation at a rational point.**  `φ` fixes `ℚ`, so the point
does not move under `φ`; only the coefficients do.  That is why the same rational `β` can be used
at every conjugate, and why the `d−1` "other" bounds are about the same polynomial evaluated the
same way. -/
theorem embedding_coeff_translate (φ : K →+* ℂ) (β : Fin m → ℚ)
    (P : MvPolynomial (Fin m) (𝓞 K)) (i : Fin m →₀ ℕ) :
    φ (coeff i (translate (fun h => algebraMap ℚ K (β h)) (map (algebraMap (𝓞 K) K) P)))
      = coeff i (translate (fun h => ((β h : ℚ) : ℂ))
          (map φ (map (algebraMap (𝓞 K) K) P))) := by
  have hfix : ∀ h, φ (algebraMap ℚ K (β h)) = ((β h : ℚ) : ℂ) := by
    intro h
    have hcomp : (φ.comp (algebraMap ℚ K)) = (algebraMap ℚ ℂ) := RingHom.ext_rat _ _
    calc φ (algebraMap ℚ K (β h)) = (φ.comp (algebraMap ℚ K)) (β h) := rfl
      _ = (algebraMap ℚ ℂ) (β h) := by rw [hcomp]
      _ = ((β h : ℚ) : ℂ) := by simp
  have hfun : (fun j => φ (algebraMap ℚ K (β j))) = (fun h => ((β h : ℚ) : ℂ)) := funext hfix
  rw [← coeff_map, map_translate, hfun]

/-- **The trivial bound, at any embedding.**  No smallness is claimed — just the height budget with
the translation point's own size.  This is what each of the `d−1` other conjugates contributes to
`eq_zero_of_norm_mul_pow_lt_one`. -/
theorem norm_embedding_coeff_translate_le (φ : K →+* ℂ) (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (r : Fin m → ℕ) {P : MvPolynomial (Fin m) (𝓞 K)} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H B' : ℝ} (hB1' : 1 ≤ B')
    (hH : ∀ k, house ((algebraMap (𝓞 K) K) (coeff k P)) ≤ H)
    (hβ : ∀ h, ‖((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℂ)‖ ≤ B') (i : Fin m →₀ ℕ) :
    ‖φ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
        (map (algebraMap (𝓞 K) K) P)))‖
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B') ^ (∑ h, r h)) := by
  rw [embedding_coeff_translate]
  refine seminorm_coeff_translate_le submultSeminorm_norm_complex _ hB1' hβ
    (fun h => le_trans (degreeOf_map_le _ _ _) (le_trans (degreeOf_map_le _ _ _) (hdeg h)))
    (fun k => ?_) i
  rw [coeff_map, coeff_map]
  exact le_trans (norm_le_house φ _) (hH k)

/-- **The Taylor bound at the distinguished embedding.**  This is the composition that makes the
assembly honest: `hidx` is step 1's index at `α`, and it is what restricts the sum, so the estimate
genuinely consumes step 1 instead of taking its consequence for granted.

An assembly that instead took the smallness as a hypothesis would type-check and would never use
step 1 at all — the polynomial's defining property would be inert. -/
theorem norm_embedding_coeff_translate_le_index (φ₀ : K →+* ℂ) (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (r : Fin m → ℕ) {P : MvPolynomial (Fin m) (𝓞 K)} (hdeg : ∀ h, degreeOf h P ≤ r h)
    (α : Fin m → 𝓞 K) {H B : ℝ} (hB1 : 1 ≤ B)
    (hH : ∀ k, house ((algebraMap (𝓞 K) K) (coeff k P)) ≤ H)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    {G : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1)
    (hγ : ∀ h, ‖((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℂ)
        - φ₀ ((algebraMap (𝓞 K) K) (α h))‖ ≤ G h)
    {μ : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ)
      ≤ index r (fun h => (algebraMap (𝓞 K) K) (α h)) (map (algebraMap (𝓞 K) K) P))
    (i : Fin m →₀ ℕ) {S : ℝ} (hS0 : 0 ≤ S)
    (hS : ∀ n : Fin m →₀ ℕ, (∀ h, n h ≤ r h) → μ ≤ idxWeight r n →
      (∏ h, (G h) ^ (n h - i h)) ≤ S) :
    ‖φ₀ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
        (map (algebraMap (𝓞 K) K) P)))‖
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * S)) := by
  classical
  rw [embedding_coeff_translate]
  have hsplit : (fun h => ((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℂ))
      = fun j => φ₀ ((algebraMap (𝓞 K) K) (α j))
          + (((((pn j : ℚ) / (qd j : ℚ)) : ℚ) : ℂ) - φ₀ ((algebraMap (𝓞 K) K) (α j))) := by
    funext j
    ring
  rw [hsplit]
  have hidx' : ((μ : ℚ) : WithTop ℚ)
      ≤ index r (fun h => φ₀ ((algebraMap (𝓞 K) K) (α h)))
          (map φ₀ (map (algebraMap (𝓞 K) K) P)) := by
    rw [index_map φ₀ φ₀.injective]
    exact hidx
  refine seminorm_coeff_translate_add_le_index submultSeminorm_norm_complex r
    (fun h => φ₀ ((algebraMap (𝓞 K) K) (α h))) _ hG0 hG1 hγ hB1
    (fun h => le_trans (norm_le_house φ₀ _) (hα h))
    (fun h => le_trans (degreeOf_map_le _ _ _) (le_trans (degreeOf_map_le _ _ _) (hdeg h)))
    (fun k => ?_) hidx' i hS0 hS
  rw [coeff_map, coeff_map]
  exact le_trans (norm_le_house φ₀ _) (hH k)

end Embedding

end MvPolynomial
