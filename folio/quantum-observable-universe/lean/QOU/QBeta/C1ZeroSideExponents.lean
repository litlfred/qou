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
`P = Y₀⁻¹ Y_∞`. That matrix is now **obtained**
(`computations/qbeta/c3_w2_c1_connection_matrix.py`), though the Stokes
multipliers still are not — see below.

### Correction (2026-08-07): the "degenerate basis" negative was WRONG

An earlier revision of this file recorded that a first numerical attempt found
the `0`-side basis degenerate — normalised determinant `|det|/max²` of `2.4e-18`
at the matching point — and blamed the normalisation `e_t(z) = θ_p(z)/θ_p(z/t)`
for "placing the two conjugate exponents ~17 orders of magnitude apart". **That
diagnosis is impossible, and has been refuted.** Three separate errors:

* `p = √q` is **real**, so `θ_p` has real coefficients and
  `θ_p(conj w) = conj θ_p(w)`. The exponents are a **conjugate pair**
  (`conjugate_pair_iff` below), so for real `z`,
  `|θ_p(z/t₂)| = |θ_p(conj(z/t₁))| = |θ_p(z/t₁)|`, hence
  `|e_{t₁}(z)| = |e_{t₂}(z)|` **exactly**. Measured ratio is `1.0`. A `1e17`
  disparity between the two columns cannot occur.
* **`|det|/max²` is not a conditioning measure.** The Casoratian satisfies
  `W(pz) = −(q−1)·W(z)/(p⁴z²−1)` exactly (verified to `1e-150`), so it decays
  under outward propagation for purely analytic reasons while the columns stay
  independent. The scale-invariant measure `|det|/(‖col₀‖·‖col₁‖) = |sin∠|`
  comes out `0.59 … 0.72` across the disc.
* **The bases do share a domain.** `h` being *entire in `1/z`* means it converges
  for every `z ≠ 0`; with the `0`-side radius `1` the two overlap on the whole
  punctured disc and match directly. The propagation that lost the conditioning
  was never required.

Also worth recording: `P(pz) = P(z)` is **automatic** for any two fundamental
matrices of one system (`Y₀(pz) = A(z)Y₀(z)` and `Y_∞(pz) = A(z)Y_∞(z)`, so `A`
cancels). It is a correctness check on the numerics and was never evidence of
anything — including in the attempt that read its "passing" as meaningful.

### What the connection matrix looks like

`P = [[c₊, c₋], [conj c₊, conj c₋]]`, elliptic per entry to `1e-27 … 1e-55`,
with `c₋` carrying **simple poles exactly on `z ∈ T·p^ℤ`** (the zeros of
`θ_p(−z/T)`).

**Still open, and not claimed:** `c₊` is *not* an exact constant — its
`z`-variation is precision-independent and grows with `q`, so "connection
constant" is a `q → 1` statement only; the law behind that variation is
unidentified; and the **Stokes multipliers are still not extracted**. Having the
connection matrix is a prerequisite for them, not the same thing.

So: the exponents below are solid, the geometry of the indicial equation is
settled, and the connection matrix exists. The multipliers are the open work.

### The pole divisor

`c₊` has simple poles at `[−1]` and `[−T]`; `c₋` at `[−1]` and `[+T]`, where
`T = √(q−1)/q^{3/4}`. All of them are zeros of a `θ_p`, whose zero set is the
single orbit `−p^ℤ` — see `QOU/QBeta/C1ConnectionPoles.lean` (sorry-free, `⊇`
direction) and `computations/qbeta/c3_w2_c1_pole_divisor.py`. The `[−1]` pole
comes from the **common** numerator `θ_p(z)` of the character `e_t` above, so it
sits in both columns and is an artifact of *this* normalisation, not connection
data.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_theta_canonical.py
-- Ref: [manuscript] computations/qbeta/c3_w2_c1_connection_matrix.py
-- Ref: [manuscript] computations/qbeta/c3_w2_c1_pole_divisor.py
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
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
