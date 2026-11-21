/-
Copyright (c) 2026 litlfred. All rights reserved.

# C1's ∞ Newton edge forces a quadratic extension (W2 stage S2, partial)

`L1 = (q²x−1)σ² − (q−1)σ − (q−1)`. Reading `deg_x` of the coefficients gives
`deg a₂ = 1`, `deg a₁ = 0`, `deg a₀ = 0`, hence Newton points `(0,1), (1,1), (2,0)`
at `∞` and the single edge `(2,0)→(0,1)` of slope `½` (independently reproducing
the edge recorded in `2026-08-01-c1-inf-slope-half-rsz-stokes.md`).

The edge height at `i = 1` is `½`, **not a lattice point**, so `i = 1` sits
strictly above the edge and contributes nothing. Only the endpoints do:

* `i = 2` contributes the `x`-leading coefficient of `a₂`, namely `q²`;
* `i = 0` contributes the `x`-constant coefficient of `a₀`, namely `−(q−1)`.

So the **characteristic equation of the edge** is `q²t² − (q−1) = 0`, i.e.
`t² = (q−1)/q²`.

This file proves that equation has **no solution with `t` a rational function of
`q`** — a quadratic extension is genuinely forced. Since `q²` is already a
square, that reduces to: `q − 1` is not a square in `ℚ[q]`. The argument is a
degree parity: `f² = q − 1` would need `2·deg f = 1`.

**Scope — deliberately narrow.** This is about the *characteristic equation of
the Newton edge*. It is **NOT** the identification of RSZ's `A₁, A₂`. Per RSZ
§3.3 (Astérisque 355, p. 39, `library/arxiv-0903.0853v3/0903.0853v3.pdf`), `A₁, A₂` are the leading
matrices of the **two slope components** `P₁, P₂`, and `B₁, B₂` are *one* `d`-th
root of each — not two roots of a single object. Identifying `A₁, A₂` for C1
requires the slope decomposition and is the remaining part of stage S2
(`qou-qbr3`). Nothing here claims that identification.

For the record, the same RSZ passage is what makes the multiplier count `2`: the
obstructions are indexed by **residues mod `d`**, giving `d` obstructions in
`Mat_{r₁,r₂}(ℂ)`; with `d = 2`, `r₁ = r₂ = 1` that is `ℂ²`.

§7c: `ℚ[X]` — pure algebra over a domain; no ordering, nothing archimedean.
Sorry-free. No fit; nothing wired; no Stokes multiplier computed.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (§3.3 p. 39)
-- Ref: [leitner2026] docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas

namespace QOU.QBeta

open Polynomial

/-- The Newton-edge characteristic polynomial in the unknown `t`, with the `q`-side
written additively: the edge equation is `q²t² = (q−1)`, so after clearing the
(already square) `q²` the question is whether `X − 1` is a square. -/
noncomputable def newtonEdgeConstant : Polynomial ℚ := X - C 1

@[simp] theorem newtonEdgeConstant_natDegree : newtonEdgeConstant.natDegree = 1 := by
  simpa [newtonEdgeConstant] using natDegree_X_sub_C (1 : ℚ)

theorem newtonEdgeConstant_ne_zero : newtonEdgeConstant ≠ 0 :=
  X_sub_C_ne_zero (1 : ℚ)

/-- **The ramification is not removable.** `q − 1` is not a square in `ℚ[q]`:
`f² = q − 1` would force `2·natDegree f = 1`, impossible. Hence the Newton-edge
equation `q²t² = q − 1` has no solution `t` in `ℚ(q)` (the `q²` is already a
square, so a solution there would give one here), and the slope-½ edge genuinely
requires adjoining `√(q−1)`. -/
theorem not_isSquare_newtonEdgeConstant :
    ¬ ∃ f : Polynomial ℚ, f * f = newtonEdgeConstant := by
  rintro ⟨f, hf⟩
  have hf0 : f ≠ 0 := by
    intro h
    rw [h, zero_mul] at hf
    exact newtonEdgeConstant_ne_zero hf.symm
  have hdeg : (f * f).natDegree = 1 := by
    rw [hf, newtonEdgeConstant_natDegree]
  rw [natDegree_mul hf0 hf0] at hdeg
  omega

/-- Restated in Mathlib's `IsSquare` form. -/
theorem not_isSquare_X_sub_one : ¬ IsSquare (newtonEdgeConstant) := by
  rintro ⟨f, hf⟩
  exact not_isSquare_newtonEdgeConstant ⟨f, hf.symm⟩

/-! ### The weight lattice of C1's `∞`: half-integral, up to the deck sign

    This narrows *where C1's q-bridge weight lives* without computing it.

    The q-bridge weight is multiplicative and lives on `E_q = ℂ*/q^ℤ`
    (`QOU.Mathlib.QAlienBridge`, proved there rather than assumed).  The question
    left open was which multiplicative group it lies in.  The slope-`½` edge
    answers it, by the following chain — with the one non-Lean step named:

    1. **[standard q-difference theory, not proved here]** a slope with
       denominator `s` has ramification index `s`; for C1 at `∞`, `s = 2`, so the
       resolving variable is `ζ` with `ζ² = x`.  This is not a fresh assumption:
       PR #4721's degree-budget computation independently found that *ramify,
       then level 2* is the only pairing whose leftover is sub-quadratic
       (`QOU.QBeta.ramified_qBorel_budget`, `m² = m(m−1) + m`).
    2. **[proved below]** the dilation `x ↦ q·x` therefore lifts to `ζ ↦ c·ζ`
       with `c² = q`, and `q` is **not a square** in `ℚ[q]` — so the lift does not
       exist over the base field; it needs the quadratic extension `ℚ(q)(√q)`.
    3. **[proved below]** any two lifts differ by exactly a sign, so the deck
       group `ℤ/2` *is* the whole ambiguity.
    4. **[proved below]** even powers of the lift descend to the base
       (`c^{2k} = q^k`) while odd powers do not (`c^{2k+1} = c·q^k`).  So the
       group generated by the lift is `q^ℤ ⊔ c·q^ℤ` — index 2 over `q^ℤ`.

    **Reading — CORRECTED 2026-08-08.**  The *algebra* below is about the
    **dilation lift** `c² = q`, and that is exactly what it proves: the group the
    lift generates is `q^{½ℤ}`, index 2 over `q^ℤ`, with the deck sign as the
    whole remaining ambiguity.  That statement stands.

    An earlier version of this note glossed it as *"C1's `∞` q-bridge weight lies
    in `q^{½ℤ}`"*.  **That gloss does not follow**, and inherits a silent
    `q^{1/4}`: the parameter that actually indexes the Stokes sectors is
    `T_theta = ±√(q−1)/q^{3/4}` (theta-normalised canonical solutions,
    `computations/qbeta/c3_w2_c1_theta_canonical.py`), **not** the Newton edge
    root `T_edge = ±√(q−1)/q`, and `q^{3/4} ∉ q^{½ℤ}`.  That script carries a
    section headed *"read this before citing `B = ±sqrt(q-1)/q`"* recording the
    distinction, and notes the edge root provably does not satisfy the indicial
    equation.  Read the results below as statements about the dilation lift —
    which is what they are — and not about the sector parameter.

    **What this is not.**  It does not compute the weight, does not exhibit an
    analytic q-difference module satisfying the bridge relation, and does not
    supply a Stokes multiplier.  It says which group the answer lives in, which
    is a constraint on any future computation, not the computation.  The
    remaining step is the analytic q-Borel/Laplace construction (bean
    `qou-vkg5`). -/

/-- **`q` is not a square in `ℚ[q]`.**  Same degree parity as
    `not_isSquare_newtonEdgeConstant`: `f² = q` would force `2·natDegree f = 1`.

    Consequence: the dilation `x ↦ q·x` does **not** lift to the slope-2 ramified
    cover over the base field — the lift requires adjoining `√q`.  So C1's `∞`
    weight cannot be a power of `q` with integer exponent. -/
theorem not_isSquare_dilationFactor :
    ¬ ∃ f : Polynomial ℚ, f * f = (X : Polynomial ℚ) := by
  rintro ⟨f, hf⟩
  have hf0 : f ≠ 0 := by
    intro h
    rw [h, zero_mul] at hf
    exact X_ne_zero hf.symm
  have hdeg : (f * f).natDegree = 1 := by
    rw [hf, natDegree_X]
  rw [natDegree_mul hf0 hf0] at hdeg
  omega

/-- **The lift is unique up to the deck sign.**  Two lifts of the dilation to the
    ramified cover differ by `±1`, so the deck group `ℤ/2` is exactly the
    ambiguity in the weight — no more, no less. -/
theorem dilationLift_unique_up_to_sign {R : Type*} [CommRing R] [IsDomain R]
    {q c d : R} (hc : c ^ 2 = q) (hd : d ^ 2 = q) : d = c ∨ d = -c := by
  have h : (d - c) * (d + c) = 0 := by
    have hdc : d ^ 2 = c ^ 2 := by rw [hc, hd]
    calc (d - c) * (d + c) = d ^ 2 - c ^ 2 := by ring
      _ = 0 := by rw [hdc, sub_self]
  rcases mul_eq_zero.mp h with h | h
  · exact Or.inl (sub_eq_zero.mp h)
  · exact Or.inr (eq_neg_of_add_eq_zero_left h)

/-- **Even powers of the lift descend to the base**: `c^{2k} = q^k`. -/
theorem dilationLift_pow_two_mul {R : Type*} [CommMonoid R] {q c : R}
    (hc : c ^ 2 = q) (k : ℕ) : c ^ (2 * k) = q ^ k := by
  rw [pow_mul, hc]

/-- **Odd powers do not**: `c^{2k+1} = c·q^k`.  With
    `dilationLift_pow_two_mul` this says the group generated by the lift is
    `q^ℤ ⊔ c·q^ℤ` — index 2 over `q^ℤ`, i.e. the weight lattice is `½ℤ`. -/
theorem dilationLift_pow_two_mul_add_one {R : Type*} [CommMonoid R] {q c : R}
    (hc : c ^ 2 = q) (k : ℕ) : c ^ (2 * k + 1) = c * q ^ k := by
  rw [pow_succ, dilationLift_pow_two_mul hc, mul_comm]

end QOU.QBeta
