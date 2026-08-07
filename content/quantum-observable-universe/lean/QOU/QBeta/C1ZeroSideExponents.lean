import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

/-!
# C1 at `0` — the Fuchsian exponents

The `0`-side of the ramified C1 operator

    L = (p⁴z² − 1)τ² − (p²−1)τ − (p²−1),   τF(z) = F(pz),  q = p²

is **regular singular**: at `z = 0` the coefficient `a₂` is `−1`, so the
indicial equation is

    t² + (q−1)·t + (q−1) = 0

(`t` the eigenvalue of `τ`). This file records what that equation forces.

## What is here

* `zeroSideIndicial` and Vieta: the two exponents multiply to `q − 1` and sum
  to `−(q − 1)`.
* `discriminant_eq` — the discriminant is `(q−1)(q−5)`, which factors. So the
  exponents are a **conjugate pair exactly for `1 < q < 5`**
  (`conjugate_pair_iff`), and the substrate `q₀ ≈ 1.10998` is comfortably
  inside that window — the `0`-side exponents there are genuinely complex, not
  real.
* `abs_sq_eq_q_sub_one` — for a conjugate pair, `|t|² = q − 1`, so
  `|t| = √(q−1)`. Measured at the substrate as
  `0.33163018974662244642` against `√(q−1) = 0.33163018974662244642`
  (20 digits).

## Why this is the whole of it

The point of the `0`-side is to supply one half of the **connection matrix**
`P = Y₀⁻¹ Y_∞`, whose ellipticity `P(pz) = P(z)` would give the Stokes
multipliers. **That is not done, and this file does not pretend otherwise.**

A first numerical attempt (2026-08-07) built both bases and found the
propagated `0`-side basis degenerate: normalised determinant `|det|/max²`
already `2.4e-18` at the matching point and falling to `8.5e-23` after
propagation, i.e. the two solutions are near-parallel as constructed. The
`P(pz) = P(z)` agreement it produced was therefore **vacuous** — a
rank-collapsed matrix satisfies it trivially — and is recorded as a negative,
not a result (bean `qou-wgnx`). The cause is the normalisation
`e_t(z) = θ_p(z)/θ_p(z/t)` placing the two conjugate exponents ~17 orders of
magnitude apart; a stable construction is the open work.

So: the exponents below are solid and the geometry of the indicial equation is
settled. The connection matrix is open.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_theta_canonical.py
-- Ref: [rsz2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-/

namespace QOU.QBeta.C1ZeroSide

/-- The `0`-side indicial polynomial `t² + (q−1)t + (q−1)`. -/
def zeroSideIndicial {R : Type*} [CommRing R] (q t : R) : R :=
  t ^ 2 + (q - 1) * t + (q - 1)

/-- **Vieta.** If `t₁, t₂` are the two exponents then their product is `q − 1`
and their sum is `−(q − 1)`. Stated as: the polynomial factors as
`(t − t₁)(t − t₂)` exactly when those two relations hold. -/
theorem vieta {R : Type*} [CommRing R] (q t₁ t₂ : R) :
    (∀ t : R, zeroSideIndicial q t = (t - t₁) * (t - t₂)) ↔
      (t₁ + t₂ = -(q - 1) ∧ t₁ * t₂ = q - 1) := by
  constructor
  · intro h
    have h0 := h 0
    have h1 := h 1
    unfold zeroSideIndicial at h0 h1
    refine ⟨?_, ?_⟩
    · linear_combination h1 - h0
    · linear_combination -h0
  · rintro ⟨hs, hp⟩ t
    unfold zeroSideIndicial
    linear_combination (t : R) * hs - hp

/-- **The discriminant factors as `(q−1)(q−5)`.** -/
theorem discriminant_eq {R : Type*} [CommRing R] (q : R) :
    (q - 1) ^ 2 - 4 * (q - 1) = (q - 1) * (q - 5) := by ring

/-- **The exponents are a conjugate (non-real) pair exactly for `1 < q < 5`.**

The substrate `q₀ ≈ 1.10998` sits well inside this window, so the `0`-side
exponents there are genuinely complex — the Fuchsian side is not diagonalisable
over `ℝ`. -/
theorem conjugate_pair_iff (q : ℝ) (hq : 1 < q) :
    (q - 1) ^ 2 - 4 * (q - 1) < 0 ↔ q < 5 := by
  rw [discriminant_eq]
  have h1 : 0 < q - 1 := by linarith
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : 0 ≤ (q - 1) * (q - 5) := mul_nonneg h1.le (by linarith)
    linarith
  · intro h
    exact mul_neg_of_pos_of_neg h1 (by linarith)

/-- **For a conjugate pair, `|t|² = q − 1`.**

`t * conj t = |t|²` and Vieta gives the product of the roots as `q − 1`, so the
two exponents lie on the circle of radius `√(q−1)`. Measured at the substrate:
`|t| = 0.33163018974662244642` against `√(q−1) = 0.33163018974662244642`. -/
theorem normSq_eq_q_sub_one (q : ℝ) (t : ℂ)
    (hprod : t * (starRingEnd ℂ) t = (((q - 1 : ℝ)) : ℂ)) :
    Complex.normSq t = q - 1 := by
  have h := Complex.mul_conj t
  rw [hprod] at h
  exact_mod_cast h.symm

/-- The exponents therefore lie on the circle of radius `√(q−1)`: since
`normSq t = |t|²`, the statement above is `|t|² = q − 1`.

Recorded because that same `√(q−1)` is the numerator of the `∞`-side leading
blocks `±√(q−1)/q^{3/4}`. Whether the coincidence of that factor across the two
singular points is structural or accidental is **not** settled here — it is an
observation, and naming it prematurely is exactly the habit this arc has been
correcting. -/
theorem norm_sq_eq_q_sub_one (q : ℝ) (t : ℂ)
    (h : Complex.normSq t = q - 1) : ‖t‖ ^ 2 = q - 1 := by
  rw [← Complex.normSq_eq_norm_sq]
  exact h

end QOU.QBeta.C1ZeroSide
