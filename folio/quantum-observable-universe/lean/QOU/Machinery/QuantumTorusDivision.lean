import QOU.Machinery.QuantumTorus
import Mathlib.Algebra.SkewMonoidAlgebra.Support

/-!
# QOU.Machinery.QuantumTorusDivision — skew-Euclidean right-division (NT-T2 brick B3)

**Right-division `f = q·g + r` (deg r < deg g) in the localized quantum torus.**

Brick B3 of the Nguyen–Tran strong-AJ decomposition
(`docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md`, class
**(c)** — *genuine Mathlib gap*).  In the localized torus
`T̃ = R(M)⟨L^±⟩` the coefficient ring is a field, so every nonzero element's
leading L-coefficient is a unit and Euclidean right-division by L-degree
terminates; this is what makes the recurrence ideal `A_K` principal (paper
§1.2).

## Mathlib gap closed (at the pinned toolchain v4.24.0)

Mathlib **has** ring-level `RingTheory.OreLocalization.*` but has **no**
skew-polynomial / Ore-extension ring `R[x;σ,δ]`, **no** skew-Laurent
Euclidean/division algorithm, and **no** noncommutative PID/Euclidean-domain
theory.  So the division algorithm is **hand-built, sorry-free**, here on the
B1/B2 skew-Laurent ring — the `WithBot ℤ` degree calculus and the termination
recursion that the missing Ore theory would otherwise supply are both proved
below (2026-07-20).

## Honest status of this file (§3b, anti-laundering STRICT)

The whole file is now **sorry-free**.  The reduction engine (the real
degree-drop content):

* `reductionQuotient` — the quotient monomial that cancels the `L^e` term.
* `reduction_leading_coeff_match` — its product with `g` matches `f`'s `L^e`
  coefficient exactly (the algebraic heart: uses `coeff_single_mul`, the
  σ-image unit `σ^{e-d}(u)`, and `Ring.inverse_mul_cancel`).
* `reduction_top_coeff_cancel` — hence the one reduction step
  `f - reductionQuotient·g` **kills the `L^e` coefficient**.

The induction/termination layer built on top (the pieces Mathlib does not
provide as Ore-extension theory, discharged directly here):

* `topDeg_lt_of_forall_ge_eq_zero` / `topDeg_eq_bot_iff` — the `WithBot ℤ` /
  `Finset.max` degree calculus.
* `skew_right_division_degree_drop` — one reduction step **strictly drops
  `topDeg`**.  The `L^e` coefficient vanishes (`reduction_top_coeff_cancel`)
  and every higher coefficient vanishes because `topDeg f = e` and the
  reduction monomial `L^{e-d}·g` has top degree `≤ e` (computed directly via
  `coeff_single_mul` + `coeffAt_eq_zero_of_topDeg_lt`).
* `exists_skew_right_division_fuel` / `exists_skew_right_division` — the
  division existence theorem `∃ q r, f = q·g + r ∧ (r = 0 ∨ topDeg r < topDeg g)`,
  by a `ℕ`-fuel induction: each step lowers `topDeg` by `≥ 1`, so a fuel
  bound read off `f`'s finite top degree terminates the recursion.  This is
  the constructive replacement for the (absent) skew-Laurent Euclidean
  algorithm.

Verified lean-direct (`lean QuantumTorusDivision.lean`, exit 0, sorry-free) at
toolchain v4.24.0.

## Base ring (§7c)

Generic `{A : Type*} [CommRing A]` with the σ-action; localization is modelled
by the hypothesis that the divisor's leading coefficient `IsUnit`.  No `ℝ`.
-/

noncomputable section

namespace QOU.Machinery.QuantumTorus

open SkewMonoidAlgebra

variable {A : Type*} [CommRing A] [MulSemiringAction Ldeg A]

/-- `σᵏ` preserves units: if `u` is a unit then so is `(ofAdd k) • u`
    (the action is by ring automorphisms). -/
theorem isUnit_smul_of_isUnit (k : ℤ) {u : A} (hu : IsUnit u) :
    IsUnit ((Multiplicative.ofAdd k) • u) :=
  hu.map (MulSemiringAction.toRingHom Ldeg A (Multiplicative.ofAdd k))

/-- **The reduction quotient monomial.**  To cancel the `L^e` term of `f`
    against a divisor `g` of top L-degree `d` with leading coefficient `u`,
    multiply `g` on the left by
    `L^{e-d} · (coeffAt f e · σ^{e-d}(u)⁻¹)`. -/
def reductionQuotient (f : QuantumTorus A) (d e : ℤ) (u : A) : QuantumTorus A :=
  monomial (e - d)
    (coeffAt f e * Ring.inverse ((Multiplicative.ofAdd (e - d)) • u))

/-- **Leading-coefficient match (PROVED — the reduction engine).**  With
    `u = coeffAt g d` a unit, the `L^e` coefficient of
    `reductionQuotient f d e u · g` equals `coeffAt f e`.  This is the exact
    cancellation identity the skew division is built on. -/
theorem reduction_leading_coeff_match (f g : QuantumTorus A) (d e : ℤ)
    (hu : IsUnit (coeffAt g d)) :
    coeffAt (reductionQuotient f d e (coeffAt g d) * g) e = coeffAt f e := by
  have hidx : (Multiplicative.ofAdd (e - d))⁻¹ * Multiplicative.ofAdd e
      = Multiplicative.ofAdd d := by
    rw [← ofAdd_neg, ← ofAdd_add]; congr 1; ring
  have huσ : IsUnit ((Multiplicative.ofAdd (e - d)) • coeffAt g d) :=
    isUnit_smul_of_isUnit (e - d) hu
  rw [reductionQuotient, monomial, coeffAt, coeff_single_mul, hidx]
  -- goal: coeffAt f e * Ring.inverse (σ • coeffAt g d) * σ • g.coeff (ofAdd d) = coeffAt f e
  show coeffAt f e * Ring.inverse ((Multiplicative.ofAdd (e - d)) • coeffAt g d)
      * (Multiplicative.ofAdd (e - d)) • coeffAt g d = coeffAt f e
  rw [mul_assoc, Ring.inverse_mul_cancel _ huσ, mul_one]

/-- Coefficients are additive under subtraction (`coeff_add` + negation). -/
theorem coeffAt_sub (f h : QuantumTorus A) (e : ℤ) :
    coeffAt (f - h) e = coeffAt f e - coeffAt h e := by
  simp only [coeffAt]
  have hneg : (-h).coeff (Multiplicative.ofAdd e)
      = -(h.coeff (Multiplicative.ofAdd e)) := by
    have hz := coeff_add h (-h) (Multiplicative.ofAdd e)
    rw [add_neg_cancel, coeff_zero] at hz
    linear_combination -hz
  rw [sub_eq_add_neg, coeff_add, hneg, ← sub_eq_add_neg]

/-- **Top-coefficient cancellation (PROVED).**  One reduction step removes the
    `L^e` term: the `L^e` coefficient of `f - reductionQuotient·g` is `0`.
    This is the concrete degree-drop content — the step provably eliminates
    the leading term. -/
theorem reduction_top_coeff_cancel (f g : QuantumTorus A) (d e : ℤ)
    (hu : IsUnit (coeffAt g d)) :
    coeffAt (f - reductionQuotient f d e (coeffAt g d) * g) e = 0 := by
  rw [coeffAt_sub, reduction_leading_coeff_match f g d e hu, sub_self]

/-- **`topDeg` upper bound from vanishing high coefficients.**  If every
    L-coefficient of `f` at exponent `≥ e` vanishes, then `topDeg f < e`.  This
    is the `WithBot ℤ`/`Finset.max` calculus that upgrades a coefficient-level
    cancellation to a strict top-degree drop. -/
theorem topDeg_lt_of_forall_ge_eq_zero (f : QuantumTorus A) {e : ℤ}
    (h : ∀ n : ℤ, e ≤ n → coeffAt f n = 0) : topDeg f < (e : WithBot ℤ) := by
  rw [topDeg]
  rcases (expSupport f).eq_empty_or_nonempty with he | he
  · rw [he, Finset.max_empty]; exact WithBot.bot_lt_coe e
  · rw [← Finset.coe_max' he, WithBot.coe_lt_coe]
    by_contra hle
    push_neg at hle
    have hmem : (expSupport f).max' he ∈ expSupport f := Finset.max'_mem _ he
    rw [mem_expSupport_iff] at hmem
    exact hmem (h _ hle)

/-- **Full degree drop after one step (PROVED).**  When `topDeg g = d`,
    `topDeg f = e`, `d ≤ e` and the leading coefficient of `g` is a unit, one
    reduction step strictly lowers the top L-degree.  Proof: the `L^e`
    coefficient vanishes (`reduction_top_coeff_cancel`) and every higher
    coefficient vanishes because `f`'s top degree is `e` and the reduction
    monomial `L^{e-d}·g` has top degree `≤ e` (computed directly via
    `coeff_single_mul`), so `topDeg_lt_of_forall_ge_eq_zero` applies.
    -- Ref: [leitner2026] NT-T2 brick B3;
    --      docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md -/
theorem skew_right_division_degree_drop (f g : QuantumTorus A) {d e : ℤ}
    (hg : topDeg g = (d : WithBot ℤ)) (hf : topDeg f = (e : WithBot ℤ))
    (hde : d ≤ e) (hu : IsUnit (coeffAt g d)) :
    topDeg (f - reductionQuotient f d e (coeffAt g d) * g) < (e : WithBot ℤ) := by
  apply topDeg_lt_of_forall_ge_eq_zero
  intro n hn
  rcases eq_or_lt_of_le hn with hne | hlt
  · -- n = e: the proved leading-term cancellation.
    rw [← hne]; exact reduction_top_coeff_cancel f g d e hu
  · -- e < n: neither `f` nor the reduction monomial has a coefficient this high.
    rw [coeffAt_sub]
    have hf0 : coeffAt f n = 0 :=
      coeffAt_eq_zero_of_topDeg_lt f (by rw [hf]; exact_mod_cast hlt)
    have hrg0 : coeffAt (reductionQuotient f d e (coeffAt g d) * g) n = 0 := by
      have hidx : (Multiplicative.ofAdd (e - d))⁻¹ * Multiplicative.ofAdd n
          = Multiplicative.ofAdd (n - (e - d)) := by
        rw [← ofAdd_neg, ← ofAdd_add]; congr 1; ring
      have hgc : g.coeff (Multiplicative.ofAdd (n - (e - d))) = 0 :=
        coeffAt_eq_zero_of_topDeg_lt g
          (by rw [hg]; exact_mod_cast (show d < n - (e - d) by omega))
      rw [reductionQuotient, monomial, coeffAt, coeff_single_mul, hidx, hgc,
        smul_zero, mul_zero]
    rw [hf0, hrg0, sub_zero]

/-- `topDeg f = ⊥` exactly for the zero element. -/
theorem topDeg_eq_bot_iff (f : QuantumTorus A) : topDeg f = ⊥ ↔ f = 0 := by
  rw [topDeg, Finset.max_eq_bot, expSupport, Finset.image_eq_empty, support_eq_empty]

/-- **Fuel form of skew right-division.**  If `topDeg f < d + k` (the divisor
    has top degree `d`), then `f = q·g + r` with `r = 0` or `topDeg r < topDeg g`.
    Proof by induction on the fuel `k : ℕ`: each reduction step
    (`skew_right_division_degree_drop`) lowers `topDeg f` by at least one, so
    `k` steps suffice.  This is the concrete termination the (missing) Ore
    Euclidean algorithm would provide. -/
theorem exists_skew_right_division_fuel (g : QuantumTorus A) {d : ℤ}
    (hg : topDeg g = (d : WithBot ℤ)) (hu : IsUnit (coeffAt g d)) :
    ∀ (k : ℕ) (f : QuantumTorus A), topDeg f < ((d + (k : ℤ) : ℤ) : WithBot ℤ) →
      ∃ q r : QuantumTorus A, f = q * g + r ∧ (r = 0 ∨ topDeg r < topDeg g) := by
  intro k
  induction k with
  | zero =>
    intro f hf
    refine ⟨0, f, by rw [zero_mul, zero_add], Or.inr ?_⟩
    rw [hg]; simpa using hf
  | succ k ih =>
    intro f hf
    by_cases hlt : topDeg f < (d : WithBot ℤ)
    · exact ⟨0, f, by rw [zero_mul, zero_add], Or.inr (by rw [hg]; exact hlt)⟩
    · push_neg at hlt
      -- `topDeg f ≠ ⊥`, so `topDeg f = ↑e`; extract the top exponent `e`.
      have hfb : topDeg f ≠ ⊥ := by
        intro hb; rw [hb] at hlt; exact absurd hlt (by simp)
      obtain ⟨e, he⟩ := WithBot.ne_bot_iff_exists.mp hfb
      -- `d ≤ e` (top degree at least the divisor's) and `e ≤ d + k` (from fuel).
      have hde : d ≤ e := by rw [← he] at hlt; exact_mod_cast hlt
      have hek : e ≤ d + (k : ℤ) := by
        rw [← he] at hf
        have h1 : e < d + ((k + 1 : ℕ) : ℤ) := by exact_mod_cast hf
        push_cast at h1; omega
      -- One reduction step strictly drops the degree, keeping it under the
      -- fuel budget for the inductive hypothesis.
      have hdrop := skew_right_division_degree_drop f g hg he.symm hde hu
      have hbound : topDeg (f - reductionQuotient f d e (coeffAt g d) * g)
          < ((d + (k : ℤ) : ℤ) : WithBot ℤ) :=
        lt_of_lt_of_le hdrop (by exact_mod_cast hek)
      obtain ⟨q', r', hqr', hr'⟩ := ih _ hbound
      refine ⟨reductionQuotient f d e (coeffAt g d) + q', r', ?_, hr'⟩
      rw [add_mul, add_assoc, ← hqr']; abel

/-- **Skew-Euclidean right-division (PROVED).**  In the localized torus
    (leading coefficient of `g` a unit) every `f` admits `f = q·g + r` with
    remainder `0` or of strictly smaller L-degree.  Proof: pick a fuel bound
    from the finite top degree of `f` (`topDeg_eq_bot_iff` gives an exponent
    when `f ≠ 0`) and run `exists_skew_right_division_fuel`.
    -- Ref: [leitner2026] NT-T2 brick B3, paper §1.2 (Ã_K principal);
    --      docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md -/
theorem exists_skew_right_division (f g : QuantumTorus A) {d : ℤ}
    (hg : topDeg g = (d : WithBot ℤ)) (hu : IsUnit (coeffAt g d)) :
    ∃ q r : QuantumTorus A, f = q * g + r ∧ (r = 0 ∨ topDeg r < topDeg g) := by
  by_cases hf0 : f = 0
  · exact ⟨0, 0, by rw [hf0, zero_mul, add_zero], Or.inl rfl⟩
  · have hfb : topDeg f ≠ ⊥ := fun hb => hf0 ((topDeg_eq_bot_iff f).mp hb)
    obtain ⟨e, he⟩ := WithBot.ne_bot_iff_exists.mp hfb
    apply exists_skew_right_division_fuel g hg hu ((e - d).toNat + 1) f
    rw [← he]
    have : e < d + (((e - d).toNat + 1 : ℕ) : ℤ) := by
      push_cast; omega
    exact_mod_cast this

end QOU.Machinery.QuantumTorus
