/-
# Roth's theorem, step 2: the index at the rational point

Step 1 (`RothAuxiliary`) builds a polynomial `P` of bounded degree and height whose index at
`(α,…,α)` is nearly `m/2`.  Step 3 (`RothRealLadder`) is Roth's Lemma: the index of such a `P` at
a *rational* point `(p₁/q₁,…,p_m/q_m)` is **small**.  Step 2 is the bridge that makes those two
contradict each other: it shows the index at the rational point is **large**, because the
approximations are good.

The mechanism is arithmetic, not analytic, and that is the part this file proves.  A translated
coefficient `coeff i (translate β P)` at a rational point `β_h = p_h/q_h` is a rational number
whose denominator divides `∏_h q_h^{r_h}` — `exists_int_mul_coeff_translate`.  A rational with
that denominator is either `0` or at least `1/∏ q_h^{r_h}` in absolute value —
`eq_zero_of_abs_lt_of_den`.  So *any* bound placing it strictly below `1/∏ q_h^{r_h}` forces it to
vanish, and enough vanishing coefficients is exactly a lower bound on the index
(`le_index_iff_coeff_eq_zero`).  That chain is `le_index_of_abs_lt`.

## What is here and what is not

`le_index_of_abs_lt` takes the smallness of the low-weight coefficients as a **hypothesis**.
Supplying it is the analytic half of step 2 — Taylor expansion of `P` about `α`, using
`translate β P = translate (β − α) (translate α P)`, the index hypothesis at `α` to kill the
low-weight terms of the inner translate, and `|β_h − α| ≤ q_h^{−(2+δ)}` with `r_h · log q_h`
roughly constant to make the surviving terms small.  That is a separate bean; it needs real
logarithms and the height bound on `P`, neither of which this file touches.

Splitting it this way is deliberate.  The arithmetic half is unconditional and short; the
analytic half is where the parameter bookkeeping lives, and stating the interface first means the
bookkeeping has a target to hit rather than being invented alongside its own consumer.  The same
discipline caught correction 26 (the `Θ`-form halves that did not compose).

## The scaling is not slack

`translateMatrix_half_witness` computes `translateMatrix (1/2) 0 (single 0 2) = 1/4`: at
`β = 1/2`, `r = 2` the translated constant term really does have denominator `q^r = 4`.  So the
factor `∏ q_h^{r_h}` in `exists_int_mul_coeff_translate` is attained, and a proof that dropped it
— or replaced it by `∏ q_h^{deg}` for a smaller `deg` — would be false rather than merely weak.
Roth's theorem is a fight over exponents; recording which of them are tight is the only defence
against silently paying one twice, which is what correction 24 turned out to be.

## Generality

Coefficients here are **rational integers**, `P : MvPolynomial (Fin m) ℤ`.  The auxiliary
polynomial of step 1 has coefficients in `𝓞 K` — for that case "small ⇒ zero" is the norm
inequality `|N(x)| ≥ 1` for a non-zero algebraic integer rather than `|z| ≥ 1` for a non-zero
rational integer, and it needs the conjugates of `β` as well.  This file does not claim that
case; it is tracked separately, and the two statements are deliberately not conflated.
-/
import QOU.Mathlib.RothAuxiliaryConstruction

namespace MvPolynomial

open Finset

/-- **Small with a bounded denominator forces zero.**  The mechanism of every "the index at the
rational point is large" argument: a rational whose denominator divides `D` is either `0` or at
least `1/D` in absolute value. -/
theorem eq_zero_of_abs_lt_of_den {x : ℚ} {D : ℤ} (hD : 0 < D) (hden : ∃ z : ℤ, (D : ℚ) * x = z)
    (hlt : |x| < 1 / (D : ℚ)) : x = 0 := by
  obtain ⟨z, hz⟩ := hden
  have hDQ : (0 : ℚ) < (D : ℚ) := by exact_mod_cast hD
  have hzlt : |(z : ℚ)| < 1 := by
    rw [← hz, abs_mul, abs_of_pos hDQ]
    calc (D : ℚ) * |x| < (D : ℚ) * (1 / (D : ℚ)) := mul_lt_mul_of_pos_left hlt hDQ
      _ = 1 := by field_simp
  have hz0 : z = 0 := by
    by_contra hne
    have : (1 : ℚ) ≤ |(z : ℚ)| := by
      rw [← Int.cast_abs]
      exact_mod_cast Int.one_le_abs hne
    linarith
  rw [hz0, Int.cast_zero] at hz
  rcases mul_eq_zero.mp hz with h | h
  · exact absurd h hDQ.ne'
  · exact h

/-- A finite sum of rationals that are each integers is an integer. -/
theorem exists_int_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ)
    (h : ∀ n ∈ s, ∃ z : ℤ, f n = (z : ℚ)) : ∃ z : ℤ, ∑ n ∈ s, f n = (z : ℚ) := by
  classical
  induction s using Finset.induction with
  | empty => exact ⟨0, by simp⟩
  | insert a s ha ih =>
      obtain ⟨za, hza⟩ := h a (Finset.mem_insert_self a s)
      obtain ⟨zs, hzs⟩ := ih (fun n hn => h n (Finset.mem_insert_of_mem hn))
      refine ⟨za + zs, ?_⟩
      rw [Finset.sum_insert ha, hza, hzs]
      push_cast
      ring

/-- **The translate matrix at a rational point has a controlled denominator.**  Scaling by
`∏ q_h^{n_h}` clears it — proved by the same peeling as the height bound, because each linear
factor `X_j + p_j/q_j` contributes exactly one `q_j`. -/
theorem exists_int_mul_translateMatrix {m : ℕ} (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) :
    ∀ (N : ℕ) (n : Fin m →₀ ℕ), (n.sum fun _ e => e) = N → ∀ i : Fin m →₀ ℕ,
      ∃ z : ℤ, (∏ h, (qd h : ℚ) ^ (n h)) *
        translateMatrix (fun h => (pn h : ℚ) / (qd h : ℚ)) i n = z := by
  classical
  intro N
  induction N with
  | zero =>
      intro n hn i
      rw [Finsupp.sum] at hn
      have hn0 : n = 0 := by
        ext a
        by_contra hc
        have hmem : a ∈ n.support := Finsupp.mem_support_iff.mpr (by simpa using hc)
        exact (Finsupp.mem_support_iff.mp hmem) ((Finset.sum_eq_zero_iff.mp hn) a hmem)
      subst hn0
      rw [translateMatrix, monomial_zero', map_one, translate, map_one, coeff_one]
      simp only [Finsupp.coe_zero, Pi.zero_apply, pow_zero, Finset.prod_const_one, one_mul]
      split_ifs
      · exact ⟨1, by norm_num⟩
      · exact ⟨0, by norm_num⟩
  | succ N ih =>
      intro n hn i
      have hne : n ≠ 0 := by intro h; rw [h] at hn; simp at hn
      obtain ⟨j, hj⟩ : ∃ j, n j ≠ 0 := by
        by_contra hc; push_neg at hc; exact hne (Finsupp.ext hc)
      set n' : Fin m →₀ ℕ := n - Finsupp.single j 1 with hn'
      have hle : Finsupp.single j 1 ≤ n :=
        Finsupp.single_le_iff.mpr (Nat.one_le_iff_ne_zero.mpr hj)
      have hsplit : Finsupp.single j 1 + n' = n := add_tsub_cancel_of_le hle
      have hsum' : (n'.sum fun _ e => e) = N := by
        have hadd : ((Finsupp.single j 1 + n').sum fun _ e => e)
            = ((Finsupp.single j 1).sum fun _ e => e) + (n'.sum fun _ e => e) :=
          Finsupp.sum_add_index' (fun _ => rfl) (fun _ _ _ => rfl)
        rw [hsplit, Finsupp.sum_single_index rfl] at hadd
        omega
      -- the product splits off one `q j`
      have hprod : (∏ h, (qd h : ℚ) ^ (n h))
          = (qd j : ℚ) * ∏ h, (qd h : ℚ) ^ (n' h) := by
        conv_lhs => rw [← hsplit]
        have hpt : ∀ h : Fin m,
            ((qd h : ℚ)) ^ ((Finsupp.single j 1 + n' : Fin m →₀ ℕ) h)
              = (if j = h then (qd h : ℚ) else 1) * (qd h : ℚ) ^ (n' h) := by
          intro h
          simp only [Finsupp.coe_add, Pi.add_apply, Finsupp.single_apply, pow_add]
          split_ifs <;> simp
        rw [Finset.prod_congr rfl (fun h _ => hpt h), Finset.prod_mul_distrib,
          Finset.prod_ite_eq]
        simp
      -- peel one occurrence of `X j`
      have hmono : (monomial n 1 : MvPolynomial (Fin m) ℚ) = X j * monomial n' 1 := by
        rw [X, monomial_mul, hsplit, one_mul]
      have htr : translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n 1)
          = (X j + C ((pn j : ℚ) / (qd j : ℚ)))
            * translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n' 1) := by
        rw [hmono, translate, map_mul, aeval_X, ← translate]
      have hcoeff : translateMatrix (fun h => (pn h : ℚ) / (qd h : ℚ)) i n
          = coeff i (X j * translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n' 1))
            + ((pn j : ℚ) / (qd j : ℚ))
              * coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n' 1)) := by
        rw [translateMatrix, htr, add_mul, coeff_add, coeff_C_mul]
      obtain ⟨zB, hzB⟩ := ih n' hsum' i
      rw [translateMatrix] at hzB
      obtain ⟨zA, hzA⟩ : ∃ zA : ℤ, (∏ h, (qd h : ℚ) ^ (n' h)) *
          coeff i (X j * translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n' 1))
            = zA := by
        rw [coeff_X_mul']
        split_ifs
        · exact ih n' hsum' (i - Finsupp.single j 1)
        · exact ⟨0, by ring⟩
      have hqα : (qd j : ℚ) * ((pn j : ℚ) / (qd j : ℚ)) = (pn j : ℚ) := by
        have : (qd j : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (hq j)
        field_simp
      refine ⟨(qd j : ℤ) * zA + (pn j) * zB, ?_⟩
      rw [hprod, hcoeff]
      push_cast
      linear_combination (qd j : ℚ) * hzA + (pn j : ℚ) * hzB
        + ((∏ h, (qd h : ℚ) ^ (n' h))
            * coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (monomial n' 1))) * hqα

/-- **The scaling of `exists_int_mul_translateMatrix` is attained.**  At `β = 1/2` the translated
constant term of `x²` is `1/4`, so the `∏ q_h^{n_h}` really is needed and cannot be lowered. -/
theorem translateMatrix_half_witness :
    translateMatrix (fun _ : Fin 1 => (1 : ℚ) / 2) 0 (Finsupp.single 0 2) = 1 / 4 := by
  have hs : (Finsupp.single (0 : Fin 1) 1 + Finsupp.single (0 : Fin 1) 1)
      = Finsupp.single (0 : Fin 1) 2 := by
    rw [← Finsupp.single_add]
  have hm : (monomial (Finsupp.single (0 : Fin 1) 2) (1 : ℚ)) = X 0 * X 0 := by
    rw [X, monomial_mul, one_mul, hs]
  rw [translateMatrix, hm, translate, map_mul, aeval_X, ← constantCoeff_eq]
  simp only [map_mul, map_add, constantCoeff_X, constantCoeff_C]
  norm_num

/-- **A translated coefficient at a rational point has denominator dividing `∏ q_h^{r_h}`.**  The
degree bound is what converts the per-monomial scaling of `exists_int_mul_translateMatrix` into a
single scaling valid for the whole polynomial. -/
theorem exists_int_mul_coeff_translate {m : ℕ} (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) (P : MvPolynomial (Fin m) ℤ)
    (hdeg : ∀ h, degreeOf h P ≤ r h) (i : Fin m →₀ ℕ) :
    ∃ z : ℤ, (∏ h, (qd h : ℚ) ^ (r h)) *
      coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P))
        = (z : ℚ) := by
  classical
  rw [coeff_translate_eq_sum, Finset.mul_sum]
  refine exists_int_sum _ _ ?_
  intro n hn
  have hnP : n ∈ P.support := support_map_subset (Int.castRingHom ℚ) P hn
  have hnr : ∀ h, n h ≤ r h := fun h => le_trans (monomial_le_degreeOf h hnP) (hdeg h)
  obtain ⟨zn, hzn⟩ :=
    exists_int_mul_translateMatrix pn qd hq (n.sum fun _ e => e) n rfl i
  have hcn : coeff n (map (Int.castRingHom ℚ) P) = ((coeff n P : ℤ) : ℚ) := by
    rw [coeff_map]; rfl
  have hD : (∏ h, (qd h : ℚ) ^ (r h))
      = (∏ h, (qd h : ℚ) ^ (r h - n h)) * (∏ h, (qd h : ℚ) ^ (n h)) := by
    rw [← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl (fun h _ => ?_)
    rw [← pow_add]
    congr 1
    have := hnr h
    omega
  refine ⟨coeff n P * (∏ h, (qd h : ℤ) ^ (r h - n h)) * zn, ?_⟩
  rw [hcn, hD]
  push_cast
  linear_combination
    ((((coeff n P : ℤ) : ℚ)) * (∏ h, (qd h : ℚ) ^ (r h - n h))) * hzn

/-- **Small forces vanishing.**  A translated coefficient at the rational point that is strictly
below `1/∏ q_h^{r_h}` in absolute value is exactly `0`. -/
theorem coeff_translate_eq_zero_of_abs_lt {m : ℕ} (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) (P : MvPolynomial (Fin m) ℤ)
    (hdeg : ∀ h, degreeOf h P ≤ r h) (i : Fin m →₀ ℕ)
    (hlt : |coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P))|
      < 1 / (∏ h, (qd h : ℚ) ^ (r h))) :
    coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P)) = 0 := by
  have hDpos : (0 : ℤ) < ∏ h, (qd h : ℤ) ^ (r h) :=
    Finset.prod_pos (fun h _ => pow_pos (Int.natCast_pos.mpr (Nat.pos_of_ne_zero (hq h))) _)
  have hcast : (((∏ h, (qd h : ℤ) ^ (r h) : ℤ)) : ℚ) = ∏ h, (qd h : ℚ) ^ (r h) := by
    push_cast
    ring
  refine eq_zero_of_abs_lt_of_den hDpos ?_ ?_
  · rw [hcast]
    exact exists_int_mul_coeff_translate pn qd hq r P hdeg i
  · rw [hcast]
    exact hlt

/-- **Step 2, arithmetic half: the index at the rational point is large.**  Every translated
coefficient of weight below `μ` that is small enough vanishes, and enough vanishing is a lower
bound on the index.  The smallness hypothesis is the analytic half, supplied elsewhere. -/
theorem le_index_of_abs_lt {m : ℕ} (pn : Fin m → ℤ) (qd : Fin m → ℕ)
    (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) (P : MvPolynomial (Fin m) ℤ)
    (hdeg : ∀ h, degreeOf h P ≤ r h) (μ : ℚ)
    (hsmall : ∀ i : Fin m →₀ ℕ, idxWeight r i < μ →
      |coeff i (translate (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P))|
        < 1 / (∏ h, (qd h : ℚ) ^ (r h))) :
    ((μ : ℚ) : WithTop ℚ)
      ≤ index r (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P) := by
  classical
  refine (le_index_iff_coeff_eq_zero r _ _ μ).mpr (fun i hi => ?_)
  exact coeff_translate_eq_zero_of_abs_lt pn qd hq r P hdeg i (hsmall i hi)

end MvPolynomial
