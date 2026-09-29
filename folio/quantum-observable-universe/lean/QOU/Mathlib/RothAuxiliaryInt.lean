/-
# Route A: the auxiliary polynomial over `ℤ`, so that step 1 can reach step 3

`RothAuxiliary` builds the auxiliary polynomial with `𝓞 K` coefficients, because that is what
Mathlib's number-field Siegel lemma produces.  Roth's Lemma (`index_le_rothBound`) requires
`MvPolynomial σ ℤ`, through `InRothPolySet`.  The two do not compose, and no work downstream of
either fixes it — the join has to be made at the coefficient ring.  This file makes it on the `ℤ`
side, which is the cheaper of the two: Siegel over `ℤ` is already in Mathlib, and everything from
step 2 onward already works over `ℤ`.

## Where `deg α` enters, and it does

`sum_smul_eq_zero_iff_repr` is the whole difference.  One `𝓞 K`-linear vanishing condition is
`finrank ℚ K` integer-linear conditions — expand in an integral basis, and the element vanishes
exactly when all its coordinates do.  So the counting condition becomes the classical
`deg α · #conditions < #unknowns`, which is `nsmul_fintypeCard_idxWeight_lt`, and "take `m` large"
becomes `m > deg α/(4ε²)`.

`RothAuxiliaryPolynomial`'s header used to say the degree cancels out of the counting.  That is
true of the `house` engine and false of this route; the note there now says so.

## What is a hypothesis here and why

`hcount` — that the system is underdetermined — rather than derived inline.  It is exactly what
`nsmul_fintypeCard_idxWeight_lt` supplies once `Fintype.card (Free.ChooseBasisIndex ℤ (𝓞 K))` is
identified with `finrank ℚ K`, and `card_chooseBasisIndex_eq_finrank` below does that
identification.  Keeping them separate means the counting lemma is stated in the form the variance
argument proves and the Siegel call is stated in the form Mathlib consumes, with one named bridge
between — rather than one theorem that silently does both and can be wrong in either half.
-/
import QOU.Mathlib.RothAuxiliaryConstruction
import Mathlib.NumberTheory.SiegelsLemma
import Mathlib.NumberTheory.NumberField.Basic

open NumberField Finset

/- Siegel's lemma states its bound against the sup norm on matrices, the same local instance
`Mathlib/NumberTheory/SiegelsLemma.lean` sets. -/
attribute [local instance] Matrix.seminormedAddCommGroup

namespace MvPolynomial

section Map

variable {R S : Type*} [CommRing R] [CommRing S]

/-- `map` commutes with `ofBox`: applying a ring hom to the coefficient vector is applying it to
the polynomial. -/
theorem map_ofBox {m : ℕ} (f : R →+* S) (r : Fin m → ℕ) (c : (Fin m →₀ ℕ) → R) :
    map f (ofBox r c) = ofBox r (fun n => f (c n)) := by
  classical
  rw [ofBox, ofBox, map_sum]
  exact Finset.sum_congr rfl (fun n _ => map_monomial f n (c n))

end Map

section IntegralBasis

variable {K : Type*} [Field K] [NumberField K]

/-- **One `𝓞 K`-linear condition is `deg α` integer ones.**  The element of `𝓞 K` vanishes exactly
when every coordinate in an integral basis does, and the coordinates of a `ℤ`-combination are the
`ℤ`-combinations of the coordinates.  This is the step that puts `finrank ℚ K` into the count. -/
theorem sum_smul_eq_zero_iff_repr {ι : Type*} (s : Finset ι) (c : ι → ℤ) (v : ι → 𝓞 K) :
    (∑ n ∈ s, (c n : 𝓞 K) * v n = 0)
      ↔ ∀ l, ∑ n ∈ s, c n * (RingOfIntegers.basis K).repr (v n) l = 0 := by
  classical
  have hrepr : ∀ l, (RingOfIntegers.basis K).repr (∑ n ∈ s, (c n : 𝓞 K) * v n) l
      = ∑ n ∈ s, c n * (RingOfIntegers.basis K).repr (v n) l := by
    intro l
    rw [map_sum, Finsupp.finset_sum_apply]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [← zsmul_eq_mul, map_zsmul, Finsupp.smul_apply, smul_eq_mul]
  constructor
  · intro h l
    rw [← hrepr l, h, map_zero, Finsupp.coe_zero, Pi.zero_apply]
  · intro h
    have hz : (RingOfIntegers.basis K).repr (∑ n ∈ s, (c n : 𝓞 K) * v n) = 0 := by
      ext l
      rw [hrepr l, h l, Finsupp.coe_zero, Pi.zero_apply]
    exact (map_eq_zero_iff _ (RingOfIntegers.basis K).repr.injective).mp hz

/-- The number of integral-basis coordinates is `deg α`. -/
theorem card_chooseBasisIndex_eq_finrank :
    Fintype.card (Module.Free.ChooseBasisIndex ℤ (𝓞 K)) = Module.finrank ℚ K := by
  rw [← RingOfIntegers.rank K, Module.finrank_eq_card_chooseBasisIndex]

end IntegralBasis

section Siegel

variable {K : Type*} [Field K] [NumberField K] {m : ℕ}

/-- The integer matrix of the vanishing conditions.  Rows are pairs (low-weight multi-index,
integral-basis coordinate); columns are the box of admissible monomials. -/
noncomputable def auxMatrixInt (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) :
    Matrix ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
              × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
           {n // n ∈ idxBoxF r} ℤ :=
  fun il n =>
    (RingOfIntegers.basis K).repr
      (translateMatrix α (il.1 : Fin m →₀ ℕ) (n : Fin m →₀ ℕ)) il.2

/-- **Siegel's height bound for the auxiliary system**, named.

Consumers need to state `Γ_m`'s clauses and the size comparison at the `a` the construction
actually produces — `⌈siegelHeight⌉` — and not universally over all of `R(a; r)`.  Quantifying
over every `(P, a)` instead would be a strictly stronger hypothesis and therefore a weaker
theorem, and it would ask a caller to check `Γ_m` for polynomials the construction never makes. -/
noncomputable def siegelHeight (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ) : ℝ :=
  ((Fintype.card {n // n ∈ idxBoxF r} : ℝ) * max 1 ‖auxMatrixInt r α μ‖)
    ^ ((Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
          × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)
      / ((Fintype.card {n // n ∈ idxBoxF r} : ℝ)
        - (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
            × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)))

/-- **Route A's step 1.**  A non-zero `ℤ`-coefficient polynomial of bounded degree whose index at
`(α₁,…,α_m)` is at least `μ`, with Siegel's height bound on its coefficients.

`hcount` is the classical counting condition `deg α · #conditions < #unknowns`; supply it from
`nsmul_fintypeCard_idxWeight_lt` and `card_chooseBasisIndex_eq_finrank`. -/
theorem exists_auxiliary_polynomial_int (r : Fin m → ℕ) (α : Fin m → 𝓞 K) (μ : ℚ)
    (hpos : 0 < Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
              × Module.Free.ChooseBasisIndex ℤ (𝓞 K)))
    (hcount : Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
                × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
              < Fintype.card {n // n ∈ idxBoxF r}) :
    ∃ P : MvPolynomial (Fin m) ℤ, P ≠ 0 ∧ (∀ h, degreeOf h P ≤ r h) ∧
      ((μ : ℚ) : WithTop ℚ)
        ≤ index r (fun h => (algebraMap (𝓞 K) K) (α h)) (map (algebraMap ℤ K) P) ∧
      ∀ n, |((coeff n P : ℤ) : ℝ)| ≤ siegelHeight r α μ := by
  classical
  obtain ⟨t, ht0, hteq, htnorm⟩ :=
    Int.Matrix.exists_ne_zero_int_vec_norm_le (auxMatrixInt r α μ) hcount hpos
  set c : (Fin m →₀ ℕ) → ℤ := fun n => if h : n ∈ idxBoxF r then t ⟨n, h⟩ else 0 with hc
  -- the solution is a non-zero coefficient vector on the box
  obtain ⟨n₀, hn₀⟩ : ∃ n₀ : {n // n ∈ idxBoxF r}, t n₀ ≠ 0 := by
    by_contra hcon
    push_neg at hcon
    exact ht0 (funext hcon)
  have hcne : c (n₀ : Fin m →₀ ℕ) ≠ 0 := by
    rw [hc]
    simp only [n₀.2, dif_pos]
    exact hn₀
  -- the vanishing conditions, back in `𝓞 K`
  have hvanish : ∀ i ∈ idxBoxF r, idxWeight r i < μ →
      ∑ n ∈ idxBoxF r, (c n : 𝓞 K) * translateMatrix α i n = 0 := by
    intro i hi hlt
    have hifilt : i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ) :=
      Finset.mem_filter.mpr ⟨hi, hlt.le⟩
    rw [sum_smul_eq_zero_iff_repr]
    intro l
    have hrow := congrFun hteq (⟨i, hifilt⟩, l)
    rw [Matrix.mulVec, dotProduct] at hrow
    simp only [Pi.zero_apply] at hrow
    rw [Finset.sum_subtype (s := idxBoxF r) (p := fun n => n ∈ idxBoxF r)
      (fun _ => Iff.rfl) (fun n => c n * (RingOfIntegers.basis K).repr (translateMatrix α i n) l)]
    simp only [hc]
    rw [← hrow]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [dif_pos n.2, auxMatrixInt]
    ring
  refine ⟨ofBox r c, ?_, degreeOf_ofBox_le r c, ?_, ?_⟩
  · intro hzero
    apply hcne
    have := congrArg (coeff (n₀ : Fin m →₀ ℕ)) hzero
    rwa [coeff_ofBox, if_pos n₀.2, coeff_zero] at this
  · rw [map_ofBox]
    refine le_index_ofBox r _ _ μ (fun i hi hlt => ?_)
    have h := hvanish i hi hlt
    have hmap := congrArg (algebraMap (𝓞 K) K) h
    rw [map_sum, map_zero] at hmap
    rw [← hmap]
    refine Finset.sum_congr rfl (fun n _ => ?_)
    rw [map_mul, ← translateMatrix_map (algebraMap (𝓞 K) K) α i n]
    norm_cast
  · intro n
    rw [coeff_ofBox, siegelHeight]
    split_ifs with hmem
    · rw [hc]
      simp only [hmem, dif_pos]
      have h2 := le_trans (norm_le_pi_norm t ⟨n, hmem⟩) htnorm
      simpa [Int.norm_eq_abs] using h2
    · have hb : (0 : ℝ) ≤ ((Fintype.card {n // n ∈ idxBoxF r} : ℝ)
          * max 1 ‖auxMatrixInt r α μ‖) ^ ((Fintype.card
            ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
              × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ)
          / ((Fintype.card {n // n ∈ idxBoxF r} : ℝ)
            - (Fintype.card ({i // i ∈ (idxBoxF r).filter (fun i => idxWeight r i ≤ μ)}
                × Module.Free.ChooseBasisIndex ℤ (𝓞 K)) : ℝ))) :=
        Real.rpow_nonneg (by positivity) _
      simpa using hb

/-- **The counting condition, discharged.**  `deg α · #conditions < #unknowns` from the variance
argument, in the shape Siegel over `ℤ` consumes.  This is where `m > deg α/(4ε²)` lives — and it is
the whole difference between this route and the `house` route, where the degree cancelled. -/
theorem card_prod_lt_card_idxBoxF (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0) {ε : ℚ} (hε : 0 < ε)
    (hm : ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ)) :
    Fintype.card ({i // i ∈ (idxBoxF r).filter
          (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))}
        × Module.Free.ChooseBasisIndex ℤ (𝓞 K))
      < Fintype.card {n // n ∈ idxBoxF r} := by
  rw [Fintype.card_prod, card_chooseBasisIndex_eq_finrank, mul_comm]
  exact nsmul_fintypeCard_idxWeight_lt r hr (Module.finrank ℚ K) hε hm

end Siegel

end MvPolynomial
