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

## Mathlib gap (verified at the pinned toolchain v4.24.0)

Mathlib **has** ring-level `RingTheory.OreLocalization.*` but has **no**
skew-polynomial / Ore-extension ring `R[x;σ,δ]`, **no** skew-Laurent
Euclidean/division algorithm, and **no** noncommutative PID/Euclidean-domain
theory.  So the division algorithm is hand-built here on the B1/B2
skew-Laurent ring.

## Honest status of this file (§3b, anti-laundering STRICT)

What is **proved sorry-free** (the reduction engine — the real degree-drop
content):

* `reductionQuotient` — the quotient monomial that cancels the `L^e` term.
* `reduction_leading_coeff_match` — its product with `g` matches `f`'s `L^e`
  coefficient exactly (the algebraic heart: uses `coeff_single_mul`, the
  σ-image unit `σ^{e-d}(u)`, and `Ring.inverse_mul_cancel`).
* `reduction_top_coeff_cancel` — hence the one reduction step
  `f - reductionQuotient·g` **kills the `L^e` coefficient**.

What is stated with a **real proposition + `sorry` + `-- Ref: [manuscript]`**
(the genuinely-missing Mathlib pieces — NOT vacuous `True`, NOT a
conclusion-as-field class):

* `skew_right_division_degree_drop` — the full **`topDeg` strictly drops**
  after one step.  The `L^e` coefficient is proved to vanish
  (`reduction_top_coeff_cancel`); what remains open is the `topDeg`
  monotonicity calculus over `WithBot ℤ` (`topDeg (x - y) ≤ max …`,
  `topDeg (single·g) ≤ k + topDeg g` from `support_single_mul_subset`) —
  routine but unbuilt for `SkewMonoidAlgebra`.
* `exists_skew_right_division` — the division existence theorem
  `∃ q r, f = q·g + r ∧ (r = 0 ∨ topDeg r < topDeg g)`.  Assembling the
  quotient by **well-founded recursion on `topDeg`** is the Ore-extension
  gap above; the per-step engine it would iterate is the proved
  `reduction_top_coeff_cancel`.

Per the anti-laundering rule this file therefore does **NOT** claim
skew-Euclidean division is proved in Lean — only the reduction step is.  The
wall is recorded in the workplan (NT-T4 gate) and in these two docstrings.

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

/-- **Full degree drop after one step (STATED — `topDeg` monotonicity gap).**
    When `topDeg g = d`, `topDeg f = e`, `d ≤ e` and the leading coefficient of
    `g` is a unit, one reduction step strictly lowers the top L-degree.  The
    `L^e` coefficient is proved to vanish (`reduction_top_coeff_cancel`); the
    remaining content — that no higher coefficient is created, i.e. the
    `topDeg (x - y) ≤ max (topDeg x) (topDeg y)` and
    `topDeg (single·g) ≤ k + topDeg g` calculus over `WithBot ℤ` — is routine
    but unbuilt for `SkewMonoidAlgebra` at v4.24.0.
    -- Ref: [manuscript] NT-T2 brick B3;
    --      docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md -/
theorem skew_right_division_degree_drop (f g : QuantumTorus A) {d e : ℤ}
    (hg : topDeg g = (d : WithBot ℤ)) (hf : topDeg f = (e : WithBot ℤ))
    (hde : d ≤ e) (hu : IsUnit (coeffAt g d)) :
    topDeg (f - reductionQuotient f d e (coeffAt g d) * g) < (e : WithBot ℤ) := by
  -- The engine is proved: `reduction_top_coeff_cancel` gives the `L^e`
  -- coefficient = 0.  The `WithBot ℤ` degree-monotonicity that upgrades this
  -- to a strict `topDeg` drop is the Mathlib gap.
  -- Ref: [manuscript]
  sorry

/-- **Skew-Euclidean right-division (STATED — Ore-extension recursion gap).**
    In the localized torus (leading coefficient of `g` a unit) every `f`
    admits `f = q·g + r` with remainder of strictly smaller L-degree.  The
    per-step reduction is the proved `reduction_top_coeff_cancel`; assembling
    the quotient by well-founded recursion on `topDeg` is the genuine v4.24.0
    Mathlib gap (no Ore extension / skew-Laurent Euclidean algorithm).
    -- Ref: [manuscript] NT-T2 brick B3, paper §1.2 (Ã_K principal);
    --      docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md -/
theorem exists_skew_right_division (f g : QuantumTorus A) {d : ℤ}
    (hg : topDeg g = (d : WithBot ℤ)) (hu : IsUnit (coeffAt g d)) :
    ∃ q r : QuantumTorus A, f = q * g + r ∧ (r = 0 ∨ topDeg r < topDeg g) := by
  -- Iterating `reductionQuotient` / `reduction_top_coeff_cancel` by
  -- well-founded recursion on `topDeg f`; the recursion framework is unbuilt.
  -- Ref: [manuscript]
  sorry

end QOU.Machinery.QuantumTorus
