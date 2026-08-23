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

/-! ### Next

`exists_primitive_scaling` is half of §6's Gauss step.  The other half is the disjoint-groups
argument itself:

    W integral, map W = (rename inl U) * (rename inr V)
      ⟹  ∃ l ≠ 0, both `C l * U` and `C l⁻¹ * V` integral.

The proof is short given what is above: scale `U` to a primitive integral `U'`, and then for
each coefficient `x` of `C l⁻¹ * V`, note that `(coeff i U') * x` is a coefficient of `W` and
therefore an integer, so `x.den` divides every coefficient of `U'`, hence divides their gcd,
hence is `1`.  The disjoint-coefficient identity it rests on is `coeff_sumElim_rename_mul` in
`QOU/Mathlib/SeparatedHeight.lean`.

⚠ Until that lands, the arc cannot apply the induction hypothesis to the factors of a minimum
representation, because the hypothesis is about **integer** polynomials and a minimum
representation lives over `ℚ`. -/

end MvPolynomial
