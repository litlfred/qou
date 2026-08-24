/-
  **Gauss's lemma for disjoint variable groups** — the integrality step of Mahler §6.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only for the first three sections;
  the last imports `QOU/Mathlib/SeparatedHeight.lean` for the disjoint-coefficient identity.

  ═══ WHY THIS EXISTS ═══

  §6 writes the auxiliary polynomial's Wronskian as `W = C · U* · V**` with `W` integral and
  `U*, V**` merely rational, and invokes Gauss to replace them by *integral* `U, V` with
  `W = U·V`.  §7 then bounds their heights by `max(|U|, |V|) ≤ |W|`, and that argument —
  "any coefficient of `U` times any coefficient of `V` is a coefficient of `W`, and a
  non-zero integer has absolute value at least 1" — is `abs_coeff_le_of_mul_separated` in
  `QOU/Mathlib/SeparatedHeight.lean`.

  ⚠ **Integrality is load-bearing there, not bookkeeping.**  Over `ℚ` a coefficient of `V`
  can be arbitrarily small and the step is false.  So the induction hypothesis, which is
  about integer polynomials, cannot be applied to the factors of a *minimum* representation
  — which lives over `ℚ` because shortening divides by a coefficient — until this is done.

  ⚠ Mathlib has `Polynomial.content` and `IsPrimitive` for **one** variable only; there is
  no `MvPolynomial` counterpart.  So the content theory below is built here.

  ═══ THE DISJOINT CASE IS MUCH EASIER THAN THE GENERAL ONE ═══

  General Gauss needs unique factorisation.  In *disjoint* variable groups it needs neither:
  `coeff (i ⊞ j) (U·V) = uᵢ·vⱼ` exactly, so if `U` is scaled to be primitive and integral, the
  denominator of every `vⱼ` divides every coefficient of `U`, hence divides their gcd, hence
  is `1`.  No Bézout, no factorisation — one gcd argument.
-/
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.RingTheory.Localization.Integer
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Data.Rat.Defs
import Mathlib.RingTheory.Int.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Data.Rat.Lemmas
import QOU.Mathlib.SeparatedHeight
import QOU.Mathlib.SeparatedWronskian

namespace MvPolynomial

variable {σ : Type*}

/-! ### Clearing denominators -/

/-- **A rational polynomial has an integral multiple.**

`IsLocalization.exist_integer_multiples` supplies a common denominator for the finitely many
coefficients; `Finsupp.mapRange` over `Rat.num` then builds the integral polynomial without
any choice, because the numerator map is already correct at every coefficient — including the
ones outside the support, where it returns `0`. -/
theorem exists_int_scaling (U : MvPolynomial σ ℚ) :
    ∃ b : ℤ, b ≠ 0 ∧ ∃ A : MvPolynomial σ ℤ,
      map (Int.castRingHom ℚ) A = C (b : ℚ) * U := by
  classical
  obtain ⟨b, hb⟩ :=
    IsLocalization.exist_integer_multiples (nonZeroDivisors ℤ) U.support U.coeff
  have hb0 : (b : ℤ) ≠ 0 := nonZeroDivisors.coe_ne_zero b
  have hden : ∀ i, ((b : ℤ) : ℚ) * U.coeff i = ((((b : ℤ) : ℚ) * U.coeff i).num : ℚ) := by
    intro i
    by_cases hi : i ∈ U.support
    · obtain ⟨r, hr⟩ := RingHom.mem_range.mp (hb i hi)
      have hval : ((b : ℤ) : ℚ) * U.coeff i = (r : ℚ) := by
        have h2 := hr.symm
        rw [Algebra.smul_def] at h2
        simpa using h2
      rw [hval]
      simp
    · rw [notMem_support_iff.mp hi, mul_zero]
      simp
  refine ⟨(b : ℤ), hb0,
    Finsupp.mapRange (fun q : ℚ => (((b : ℤ) : ℚ) * q).num) (by simp) U, ?_⟩
  ext i
  rw [coeff_map, coeff_C_mul]
  show ((((((b : ℤ) : ℚ) * U.coeff i).num) : ℤ) : ℚ) = ((b : ℤ) : ℚ) * U.coeff i
  exact (hden i).symm

/-! ### Content -/

/-- The **content** of an integer polynomial: the gcd of its coefficients.

Mathlib has this for `Polynomial` only. -/
noncomputable def intContent (p : MvPolynomial σ ℤ) : ℤ := p.support.gcd p.coeff

theorem intContent_dvd_coeff (p : MvPolynomial σ ℤ) (i : σ →₀ ℕ) :
    intContent p ∣ p.coeff i := by
  classical
  by_cases hi : i ∈ p.support
  · exact Finset.gcd_dvd hi
  · rw [notMem_support_iff.mp hi]
    exact dvd_zero _

theorem intContent_ne_zero {p : MvPolynomial σ ℤ} (hp : p ≠ 0) : intContent p ≠ 0 := by
  classical
  intro h
  refine hp ?_
  ext i
  by_cases hi : i ∈ p.support
  · have := Finset.gcd_eq_zero_iff.mp h i hi
    simpa using this
  · simpa using notMem_support_iff.mp hi

/-- **The primitive part.**

`p = content · q` with `q` primitive, where primitivity is stated as "every common divisor of
the coefficients is a unit" — which is what the Gauss argument below consumes, and avoids
having to define `IsPrimitive` for `MvPolynomial` at all. -/
theorem exists_primitive_part (p : MvPolynomial σ ℤ) (hp : p ≠ 0) :
    ∃ q : MvPolynomial σ ℤ, C (intContent p) * q = p ∧
      ∀ n : ℤ, (∀ i, n ∣ q.coeff i) → IsUnit n := by
  classical
  have hc : intContent p ≠ 0 := intContent_ne_zero hp
  refine ⟨Finsupp.mapRange (fun a : ℤ => a / intContent p) (by simp) p, ?_, ?_⟩
  · ext i
    rw [coeff_C_mul]
    show intContent p * (p.coeff i / intContent p) = p.coeff i
    exact Int.mul_ediv_cancel' (intContent_dvd_coeff p i)
  · intro n hn
    have hcoe : ∀ i, MvPolynomial.coeff i
        (Finsupp.mapRange (fun a : ℤ => a / intContent p) (by simp) p :
            MvPolynomial σ ℤ) = p.coeff i / intContent p :=
      fun i => Finsupp.mapRange_apply
    have hdvd : ∀ i, intContent p * n ∣ p.coeff i := by
      intro i
      obtain ⟨k, hk⟩ := hn i
      rw [hcoe] at hk
      refine ⟨k, ?_⟩
      have h1 : p.coeff i = intContent p * (p.coeff i / intContent p) :=
        (Int.mul_ediv_cancel' (intContent_dvd_coeff p i)).symm
      rw [h1, hk, mul_assoc]
    obtain ⟨k, hk⟩ : intContent p * n ∣ intContent p :=
      Finset.dvd_gcd (fun i _ => hdvd i)
    have heq : intContent p * 1 = intContent p * (n * k) := by
      rw [mul_one]
      conv_lhs => rw [hk]
      ring
    exact isUnit_of_mul_eq_one n k (mul_left_cancel₀ hc heq).symm

/-- **A rational polynomial has a primitive integral scaling.** -/
theorem exists_primitive_scaling (U : MvPolynomial σ ℚ) (hU : U ≠ 0) :
    ∃ (l : ℚ) (U' : MvPolynomial σ ℤ), l ≠ 0 ∧
      map (Int.castRingHom ℚ) U' = C l * U ∧
      ∀ n : ℤ, (∀ i, n ∣ U'.coeff i) → IsUnit n := by
  classical
  obtain ⟨b, hb0, A, hA⟩ := exists_int_scaling U
  have hAne : A ≠ 0 := by
    intro h
    rw [h, map_zero] at hA
    have : (C (b : ℚ) : MvPolynomial σ ℚ) * U = 0 := hA.symm
    rcases mul_eq_zero.mp this with h1 | h1
    · exact hb0 (by exact_mod_cast (C_eq_zero.mp h1))
    · exact hU h1
  obtain ⟨q, hq, hprim⟩ := exists_primitive_part A hAne
  have hc : intContent A ≠ 0 := intContent_ne_zero hAne
  refine ⟨(b : ℚ) / ((intContent A : ℤ) : ℚ), q, ?_, ?_, hprim⟩
  · have hcQ : ((intContent A : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hc
    have hbQ : ((b : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hb0
    exact div_ne_zero hbQ hcQ
  · have hmap : C ((intContent A : ℤ) : ℚ) * map (Int.castRingHom ℚ) q
        = map (Int.castRingHom ℚ) A := by
      conv_rhs => rw [← hq]
      rw [map_mul, map_C]
      rfl
    rw [hA] at hmap
    have hcQ : ((intContent A : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hc
    have hCne : (C ((intContent A : ℤ) : ℚ) : MvPolynomial σ ℚ) ≠ 0 :=
      fun h => hcQ (C_eq_zero.mp h)
    refine mul_left_cancel₀ hCne ?_
    rw [hmap, ← mul_assoc, ← C_mul,
      show ((intContent A : ℤ) : ℚ) * (((b : ℤ) : ℚ) / ((intContent A : ℤ) : ℚ))
          = ((b : ℤ) : ℚ) from by rw [mul_comm, div_mul_cancel₀ _ hcQ]]

/-! ### The disjoint-groups Gauss step

⚠ From here the module is **not** Mathlib-only: it uses `coeff_sumElim_rename_mul` from
`QOU/Mathlib/SeparatedHeight.lean`, the identity `coeff (i ⊞ j) (U·V) = uᵢ·vⱼ` that makes the
disjoint case elementary. -/

/-- If an integer multiple of a rational is an integer, the rational's denominator divides
that multiplier. -/
theorem den_dvd_of_mul_int {n m : ℤ} {x : ℚ} (h : (n : ℚ) * x = (m : ℚ)) :
    ((x.den : ℤ)) ∣ n := by
  rcases eq_or_ne n 0 with rfl | hn
  · exact dvd_zero _
  · have hnQ : ((n : ℤ) : ℚ) ≠ 0 := Int.cast_ne_zero.mpr hn
    have hx : x = ((m : ℚ) / (n : ℚ)) := by
      field_simp
      linarith [h]
    rw [hx, ← Rat.divInt_eq_div]
    exact Rat.den_dvd m n

/-- **Gauss's lemma for disjoint variable groups.**

If `W` has integer coefficients and, over `ℚ`, factors as a product of a polynomial in the
`x`-variables and one in the `y`-variables, then the two factors can be rescaled by a single
rational `l` to become integral.

⚠ The proof needs neither unique factorisation nor Bézout, and that is a consequence of the
groups being **disjoint**: `coeff (i ⊞ j) (U·V) = uᵢ·vⱼ` exactly, so once `U` is scaled to be
primitive and integral, the denominator of each `vⱼ` divides *every* coefficient of `U'`,
hence divides their gcd, hence is `1`.  In shared variables the coefficients mix and none of
this is available. -/
theorem exists_integral_separated_factors {τ : Type*}
    (U : MvPolynomial σ ℚ) (V : MvPolynomial τ ℚ) (hU : U ≠ 0)
    (W : MvPolynomial (σ ⊕ τ) ℤ)
    (hW : map (Int.castRingHom ℚ) W
        = (rename Sum.inl U : MvPolynomial (σ ⊕ τ) ℚ) * rename Sum.inr V) :
    ∃ (l : ℚ) (U' : MvPolynomial σ ℤ) (V' : MvPolynomial τ ℤ), l ≠ 0 ∧
      map (Int.castRingHom ℚ) U' = C l * U ∧
      map (Int.castRingHom ℚ) V' = C l⁻¹ * V := by
  classical
  obtain ⟨l, U', hl, hU', hprim⟩ := exists_primitive_scaling U hU
  -- every coefficient of `C l⁻¹ * V` is an integer
  have hden : ∀ j : τ →₀ ℕ, (l⁻¹ * V.coeff j).den = 1 := by
    intro j
    have hdvd : ∀ i : σ →₀ ℕ, ((l⁻¹ * V.coeff j).den : ℤ) ∣ U'.coeff i := by
      intro i
      refine den_dvd_of_mul_int (m := W.coeff (Finsupp.sumElim i j)) ?_
      have hcU : ((U'.coeff i : ℤ) : ℚ) = l * U.coeff i := by
        have := congrArg (coeff i) hU'
        rwa [coeff_map, coeff_C_mul] at this
      have hcW : ((W.coeff (Finsupp.sumElim i j) : ℤ) : ℚ) = U.coeff i * V.coeff j := by
        have := congrArg (coeff (Finsupp.sumElim i j)) hW
        rwa [coeff_map, coeff_sumElim_rename_mul] at this
      rw [hcU, hcW, mul_comm l (U.coeff i), mul_assoc, ← mul_assoc l, mul_inv_cancel₀ hl,
        one_mul]
    have := hprim ((l⁻¹ * V.coeff j).den : ℤ) hdvd
    have hpos : 0 < ((l⁻¹ * V.coeff j).den : ℤ) := by
      exact_mod_cast (l⁻¹ * V.coeff j).pos
    rcases Int.isUnit_iff.mp this with h1 | h1
    · exact_mod_cast h1
    · omega
  refine ⟨l, U', Finsupp.mapRange (fun q : ℚ => (l⁻¹ * q).num) (by simp) V, hl, hU', ?_⟩
  ext j
  rw [coeff_map, coeff_C_mul]
  show ((((l⁻¹ * V.coeff j).num) : ℤ) : ℚ) = l⁻¹ * V.coeff j
  have h1 := Rat.num_div_den (l⁻¹ * V.coeff j)
  rw [hden j] at h1
  simpa using h1

/-- **The factorisation is exact over `ℤ`.**

`exists_integral_separated_factors` produces integral factors; this says their product is `W`
on the nose, not merely up to a rational.  That is Mahler's `W = U·V`, and it is what
`abs_coeff_le_of_mul_separated` consumes — the height step needs the product to *be* `W`. -/
theorem exists_integral_separated_factorization {τ : Type*}
    (U : MvPolynomial σ ℚ) (V : MvPolynomial τ ℚ) (hU : U ≠ 0)
    (W : MvPolynomial (σ ⊕ τ) ℤ)
    (hW : map (Int.castRingHom ℚ) W
        = (rename Sum.inl U : MvPolynomial (σ ⊕ τ) ℚ) * rename Sum.inr V) :
    ∃ (l : ℚ) (U' : MvPolynomial σ ℤ) (V' : MvPolynomial τ ℤ), l ≠ 0 ∧
      map (Int.castRingHom ℚ) U' = C l * U ∧
      map (Int.castRingHom ℚ) V' = C l⁻¹ * V ∧
      (rename Sum.inl U' : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr V' = W := by
  obtain ⟨l, U', V', hl, hU'', hV''⟩ := exists_integral_separated_factors U V hU W hW
  refine ⟨l, U', V', hl, hU'', hV'', ?_⟩
  have hinj : Function.Injective (map (Int.castRingHom ℚ) :
      MvPolynomial (σ ⊕ τ) ℤ → MvPolynomial (σ ⊕ τ) ℚ) :=
    map_injective _ (fun a b h => Int.cast_injective h)
  refine hinj ?_
  have e1 : (rename Sum.inl (C l * U) : MvPolynomial (σ ⊕ τ) ℚ)
      = C l * rename Sum.inl U := by rw [map_mul, rename_C]
  have e2 : (rename Sum.inr (C l⁻¹ * V) : MvPolynomial (σ ⊕ τ) ℚ)
      = C l⁻¹ * rename Sum.inr V := by rw [map_mul, rename_C]
  rw [hW, map_mul, map_rename, map_rename, hU'', hV'', e1, e2, mul_mul_mul_comm,
    ← C_mul, mul_inv_cancel₀ hl, C_1, one_mul]

/-! ### Transporting to the integral factor

The induction hypothesis is stated about an *integer* polynomial, so its hypotheses have to be
checked of `U'` rather than of the rational Wronskian `U'` was built from.  All three transports
are one-liners, and all three go in the easy direction. -/

/-- A change of coefficient ring along an injective map does not move degrees. -/
theorem degreeOf_map_of_injective {R S : Type*} [CommSemiring R] [CommSemiring S]
    {f : R →+* S} (hf : Function.Injective f) (p : MvPolynomial σ R) (j : σ) :
    degreeOf j (map f p) = degreeOf j p := by
  classical
  rw [degreeOf_eq_sup j (map f p), degreeOf_eq_sup j p, support_map_of_injective p hf]

/-- Degrees transport to the integral factor.  `≤` suffices, which is why the scaling costs
nothing here: `degreeOf_C_mul_le` is the only step. -/
theorem degreeOf_integral_factor_le {p : MvPolynomial σ ℚ} {q : MvPolynomial σ ℤ} {l : ℚ}
    (hq : map (Int.castRingHom ℚ) q = C l * p) (j : σ) {D : ℕ} (hp : degreeOf j p ≤ D) :
    degreeOf j q ≤ D := by
  have h1 : degreeOf j q = degreeOf j (map (Int.castRingHom ℚ) q) :=
    (degreeOf_map_of_injective (fun a b h => Int.cast_injective h) q j).symm
  rw [h1, hq]
  exact le_trans (degreeOf_C_mul_le p j l) hp

/-- Non-vanishing transports to the integral factor. -/
theorem integral_factor_ne_zero {p : MvPolynomial σ ℚ} {q : MvPolynomial σ ℤ} {l : ℚ}
    (hl : l ≠ 0) (hp : p ≠ 0) (hq : map (Int.castRingHom ℚ) q = C l * p) : q ≠ 0 := by
  intro h
  rw [h, map_zero] at hq
  exact mul_ne_zero (fun hc => hl (C_eq_zero.mp hc)) hp hq.symm


/-! ### The separated Wronskian, made integral

⚠ From here the module also uses `QOU/Mathlib/SeparatedWronskian.lean`. -/

/-- **§6, assembled.**  The separated Wronskian of a representation of an *integer* polynomial
has integral factors whose product is the determinant taken over `ℤ`.

The determinant on the right is formed from `P` itself, over `ℤ`; `map_det_pderivList` is what
identifies it with the `ℚ`-valued one the representation produces. -/
theorem exists_integral_wronskian_factors {τ : Type*} {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial τ ℚ)
    (P : MvPolynomial (σ ⊕ τ) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) :
    ∃ (l : ℚ) (U' : MvPolynomial σ ℤ) (V' : MvPolynomial τ ℤ), l ≠ 0 ∧
      map (Int.castRingHom ℚ) U' = C l * mvGenWronskian Dx φ ∧
      map (Int.castRingHom ℚ) V' = C l⁻¹ * mvGenWronskian Dy ψ ∧
      (rename Sum.inl U' : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr V'
        = (Matrix.of fun i j =>
            pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det := by
  refine exists_integral_separated_factorization _ _ hWx _ ?_
  rw [map_det_pderivList, hP, det_separated_wronskian]

/-- **§7's height step, with integrality supplied.**

`H(U') ≤ H(W)` and `H(V') ≤ H(W)` for the integral factors above.  This is the inequality the
induction hypothesis needs on the `x`-factor, and the reason §6 does Gauss at all: over `ℚ`
the argument — "a non-zero coefficient has absolute value at least 1" — is false. -/
theorem abs_coeff_integral_wronskian_factor_le {τ : Type*}
    {U' : MvPolynomial σ ℤ} {V' : MvPolynomial τ ℤ} {W : MvPolynomial (σ ⊕ τ) ℤ}
    (hfact : (rename Sum.inl U' : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr V' = W)
    (hV' : V' ≠ 0) {B : ℤ} (hB : ∀ n, |coeff n W| ≤ B) (i : σ →₀ ℕ) :
    |coeff i U'| ≤ B :=
  abs_coeff_le_of_mul_separated hV' (by rw [hfact]; exact hB) i


/-- §7's height step for the **right** factor.  Mirror of the previous theorem; the
non-vanishing hypothesis swaps sides, because the argument picks a non-zero coefficient of the
*other* factor. -/
theorem abs_coeff_integral_wronskian_factor_le_right {τ : Type*}
    {U' : MvPolynomial σ ℤ} {V' : MvPolynomial τ ℤ} {W : MvPolynomial (σ ⊕ τ) ℤ}
    (hfact : (rename Sum.inl U' : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr V' = W)
    (hU' : U' ≠ 0) {B : ℤ} (hB : ∀ n, |coeff n W| ≤ B) (j : τ →₀ ℕ) :
    |coeff j V'| ≤ B :=
  abs_coeff_le_of_mul_separated_right hU' (by rw [hfact]; exact hB) j


/-! ### Next

§6 and §7's height step are assembled: from an **integer** auxiliary polynomial and a
**rational** separated representation, `exists_integral_wronskian_factors` produces integral
Wronskian factors whose product is the `ℤ`-determinant, and
`abs_coeff_integral_wronskian_factor_le` bounds their heights by its height.

What that leaves is assembling `hres` (`QOU/Mathlib/RothOperatorFamily.lean`) from the
induction hypothesis, and every ingredient now exists:

1. **The index side is free.**  `index_C_mul` says `index (C l * Wx) = index Wx`, so bounding
   the index of the *integral* factor `U'` — which is what `RothLemmaUniform` does — bounds
   the index of `Wx` itself.  The scaling is invisible here; it only ever mattered for heights.
2. **The height side** is `abs_coeff_integral_wronskian_factor_le` above, together with
   `abs_coeff_mvGenWronskian_le` bounding the determinant's own height.
3. **The degree side** is `degreeOf_mvGenWronskian_le`, transported through `map` and the
   scaling.

⚠ None of those is a new idea; the work is bookkeeping across three modules, and it needs a
home importing both this module and `RothLemmaStatement`. -/



end MvPolynomial
