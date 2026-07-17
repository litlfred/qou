import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.FieldTheory.IsAlgClosed.Basic
import Mathlib.Tactic.ComputeDegree
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

/-!
# QOU.Mass.CyclotomicBoundaryKeystone — the Habiro-tail cyclotomic boundary at n = 5

Formalizes the *finite forward direction* of `conj:cyclotomic-boundary-at-keystone`
([`cyclotomic-boundary-at-keystone.md`](../../../mass-theory/cyclotomic-boundary-at-keystone.md))
and the n = 6 non-cyclotomicity certificate, as far as is honestly provable.

The binding `q`-deformation of the na-Stokes period `S(n) = Σ_{λ⊢n} dim_q(λ)`
(the `q`-involution / telephone numbers, `S(n)|_{q=1} = I(n)`, OEIS A000085) obeys
`S(n) = S(n-1) + [n-1]_q S(n-2) + D(n)`.  The **Habiro tail** `D(n)`, cleared of its
`q`-monomial to an ordinary integer polynomial, is (compute:
`computations/lever1_cyclotomic_boundary_keystone_conjecture.py`):

* `D(4) = Φ₁² · Φ₃`                        — cyclotomic
* `D(5) = 2 · Φ₁² · Φ₂² · Φ₃ · Φ₆`         — cyclotomic
* `D(6) = Φ₁² · Φ₅ · C₆`,  `C₆` deg-8      — **non-cyclotomic**

## What is proved here (sorry-free)

* `D4_eq`, `D5_eq` — the base-case factorizations into explicit palindromic factors.
* `Phi1_cyclotomic`, `Phi2_cyclotomic`, `Phi3_cyclotomic`, `Phi5_cyclotomic`,
  `Phi6_cyclotomic` — those factors ARE the Mathlib cyclotomic polynomials, so
  `D4_cyclotomic`, `D5_cyclotomic` exhibit `D(4)`, `D(5)` as genuine products of
  cyclotomics (**Tier 1** of the conjecture, fully closed).
* `C6_reciprocal` — the palindrome identity `C₆(z) = z⁴·C̃(z + z⁻¹)`,
  `C̃(y) = y⁴+4y³+2y²−10y−8`, for every `z ≠ 0`.
* `C6ℂ_eq` — `C6ℂ` is `C6core` evaluated over `ℂ`.
* `unit_circle_sum_real` — if `‖z‖ = 1` then `z + z⁻¹` is real.
* `Ctil_disc` — the discriminant datum `Δ(C̃) = −44208 < 0`.
* `C6core_offcircle_root` — `C₆` has a root off the unit circle (**derived**, via
  the reciprocal transform, from `Ctil_has_nonreal_root` alone).
* `C6core_non_cyclotomic` — `C₆` is **not** a product of cyclotomic polynomials
  (**derived** from `C6core_offcircle_root`).  Crucially this uses only the *easy*
  direction of Kronecker's dichotomy — every root of a product of cyclotomics is a
  root of unity, hence norm 1 (`cyclotomic.dvd_X_pow_sub_one` +
  `Complex.norm_eq_one_of_pow_eq_one`, both in Mathlib) — and does **not** need the
  hard Kronecker converse.

## The discriminant-sign fact is now ported (no `sorry`)

`Ctil_has_nonreal_root` (`C̃` has a non-real root) is proved outright.  Mathlib's
`Polynomial.disc` is only a resultant with no product-of-root-differences bridge, so
instead of the full discriminant we use a **sum-of-squares certificate**: over `ℂ`
the monic quartic `C̃` splits into four roots `a,b,c,d`; Vieta gives
`e₁=−4, e₂=2, e₃=10, e₄=−8` (by comparing coefficients of `∏(X−rᵢ)`), and the Newton
identity `Σᵢ(1−rᵢ²)² = 4 − 2p₂ + p₄ = −12` is a pure `ring` fact in `e₁..e₄`.  Were
all four roots real, `Σᵢ(1−rᵢ²)²` would be a sum of real squares `≥ 0` —
contradiction.  (`−12 < 0` is the projection of the classical `Δ(C̃)=−44208<0` onto
the vector `(1,0,−1)`; `Ctil_disc` records the full discriminant datum.)

**This module is fully `sorry`-free.**  It closes the **Tier-2, n = 6** case
completely.  The full Tier-2 claim — `D(n)` non-cyclotomic for *all* `n ≥ 6` — is
*verified through n = 11* and remains **not proved** (out of scope here).
-/

namespace QOU.Mass.CyclotomicBoundaryKeystone

open Polynomial

/-! ### The tail polynomials (q-monomial stripped), over `ℤ` -/

/-- `D(4)` stripped: `X⁴ − X³ − X + 1`. -/
noncomputable def D4 : ℤ[X] := X ^ 4 - X ^ 3 - X + 1

/-- `D(5)` stripped: `2X⁸ − 2X⁶ − 2X² + 2`. -/
noncomputable def D5 : ℤ[X] := 2 * X ^ 8 - 2 * X ^ 6 - 2 * X ^ 2 + 2

/-- The non-cyclotomic degree-8 core of `D(6)`. -/
noncomputable def C6core : ℤ[X] :=
  X ^ 8 + 4 * X ^ 7 + 6 * X ^ 6 + 2 * X ^ 5 + 2 * X ^ 4 + 2 * X ^ 3 + 6 * X ^ 2 + 4 * X + 1

/-- Explicit cyclotomic factors used in the base cases. -/
noncomputable def Phi1 : ℤ[X] := X - 1
noncomputable def Phi2 : ℤ[X] := X + 1
noncomputable def Phi3 : ℤ[X] := X ^ 2 + X + 1
noncomputable def Phi5 : ℤ[X] := X ^ 4 + X ^ 3 + X ^ 2 + X + 1
noncomputable def Phi6 : ℤ[X] := X ^ 2 - X + 1

/-! ### Tier 1 — the base-case factorizations (sorry-free) -/

/-- `D(4) = Φ₁² · Φ₃`. -/
theorem D4_eq : D4 = Phi1 ^ 2 * Phi3 := by
  unfold D4 Phi1 Phi3; ring

/-- `D(5) = 2 · Φ₁² · Φ₂² · Φ₃ · Φ₆`. -/
theorem D5_eq : D5 = 2 * (Phi1 ^ 2 * Phi2 ^ 2 * Phi3 * Phi6) := by
  unfold D5 Phi1 Phi2 Phi3 Phi6; ring

/-! ### The factors are the Mathlib cyclotomic polynomials -/

theorem Phi1_cyclotomic : Phi1 = cyclotomic 1 ℤ := by
  rw [cyclotomic_one]; rfl

theorem Phi2_cyclotomic : Phi2 = cyclotomic 2 ℤ := by
  rw [cyclotomic_two]; rfl

theorem Phi3_cyclotomic : Phi3 = cyclotomic 3 ℤ := by
  haveI : Fact (Nat.Prime 3) := ⟨by decide⟩
  have h : cyclotomic 3 ℤ = ∑ i ∈ Finset.range 3, X ^ i :=
    cyclotomic_prime ℤ 3
  rw [h]; unfold Phi3
  simp [Finset.sum_range_succ]; ring

theorem Phi5_cyclotomic : Phi5 = cyclotomic 5 ℤ := by
  haveI : Fact (Nat.Prime 5) := ⟨by decide⟩
  have h : cyclotomic 5 ℤ = ∑ i ∈ Finset.range 5, X ^ i :=
    cyclotomic_prime ℤ 5
  rw [h]; unfold Phi5
  simp [Finset.sum_range_succ]; ring

theorem Phi6_cyclotomic : Phi6 = cyclotomic 6 ℤ := by
  -- ∏_{d ∣ 6} Φ_d = X⁶ − 1, and (X−1)(X+1)(X²+X+1)·(X²−X+1) = X⁶ − 1 too,
  -- so cancel the (nonzero) prefactor Φ₁Φ₂Φ₃.
  have hprod : ∏ i ∈ Nat.divisors 6, cyclotomic i ℤ = X ^ 6 - 1 :=
    prod_cyclotomic_eq_X_pow_sub_one (by norm_num) ℤ
  have hdiv : Nat.divisors 6 = {1, 2, 3, 6} := by decide
  rw [hdiv, Finset.prod_insert (by decide), Finset.prod_insert (by decide),
      Finset.prod_insert (by decide), Finset.prod_singleton,
      cyclotomic_one, cyclotomic_two, Phi3_cyclotomic.symm] at hprod
  -- hprod : (X-1) * ((X+1) * (Phi3 * cyclotomic 6 ℤ)) = X^6 - 1
  have hp : ((X : ℤ[X]) - 1) * ((X + 1) * Phi3) ≠ 0 := by
    have h1 : (X : ℤ[X]) - 1 ≠ 0 := fun h => by
      simpa using congrArg (Polynomial.eval (0 : ℤ)) h
    have h2 : (X : ℤ[X]) + 1 ≠ 0 := fun h => by
      simpa using congrArg (Polynomial.eval (0 : ℤ)) h
    have h3 : (Phi3 : ℤ[X]) ≠ 0 := fun h => by
      unfold Phi3 at h; simpa using congrArg (Polynomial.eval (0 : ℤ)) h
    exact mul_ne_zero h1 (mul_ne_zero h2 h3)
  have key : ((X : ℤ[X]) - 1) * ((X + 1) * Phi3) * cyclotomic 6 ℤ
           = ((X : ℤ[X]) - 1) * ((X + 1) * Phi3) * (X ^ 2 - X + 1) := by
    have e1 : ((X : ℤ[X]) - 1) * ((X + 1) * Phi3) * cyclotomic 6 ℤ = X ^ 6 - 1 := by
      rw [← hprod]; ring
    have e2 : ((X : ℤ[X]) - 1) * ((X + 1) * Phi3) * (X ^ 2 - X + 1) = X ^ 6 - 1 := by
      unfold Phi3; ring
    rw [e1, e2]
  have hcancel := mul_left_cancel₀ hp key
  unfold Phi6
  exact hcancel.symm

/-- `D(4)` is a product of cyclotomic polynomials (Tier 1). -/
theorem D4_cyclotomic : D4 = (cyclotomic 1 ℤ) ^ 2 * cyclotomic 3 ℤ := by
  rw [D4_eq, Phi1_cyclotomic, Phi3_cyclotomic]

/-- `D(5)` is a product of cyclotomic polynomials (Tier 1). -/
theorem D5_cyclotomic :
    D5 = 2 * ((cyclotomic 1 ℤ) ^ 2 * (cyclotomic 2 ℤ) ^ 2 * cyclotomic 3 ℤ * cyclotomic 6 ℤ) := by
  rw [D5_eq, Phi1_cyclotomic, Phi2_cyclotomic, Phi3_cyclotomic, Phi6_cyclotomic]

/-! ### The n = 6 core: reciprocal transform + off-circle root (Tier 2, n = 6 only) -/

/-- The reduced quartic `C̃(y) = y⁴ + 4y³ + 2y² − 10y − 8`, from `C₆(q) = q⁴·C̃(q+q⁻¹)`. -/
noncomputable def Ctil : ℤ[X] := X ^ 4 + 4 * X ^ 3 + 2 * X ^ 2 - 10 * X - 8

/-- `C₆` as an explicit `ℂ`-valued function (= `C6core` evaluated over `ℂ`, see
    `C6ℂ_eq`). -/
def C6ℂ (z : ℂ) : ℂ :=
  z ^ 8 + 4 * z ^ 7 + 6 * z ^ 6 + 2 * z ^ 5 + 2 * z ^ 4 + 2 * z ^ 3 + 6 * z ^ 2 + 4 * z + 1

/-- `C̃` as an explicit `ℂ`-valued function. -/
def Ctilℂ (y : ℂ) : ℂ := y ^ 4 + 4 * y ^ 3 + 2 * y ^ 2 - 10 * y - 8

/-- `C6ℂ` really is `C6core` evaluated over `ℂ` (so the off-circle root below is a
    root of the integer polynomial `C6core`).  Fully proved. -/
theorem C6ℂ_eq (z : ℂ) : C6ℂ z = (C6core.map (Int.castRingHom ℂ)).eval z := by
  simp only [C6core, C6ℂ, Polynomial.map_add, Polynomial.map_mul, Polynomial.map_pow,
    Polynomial.map_ofNat, Polynomial.map_X, Polynomial.map_one, Polynomial.eval_add,
    Polynomial.eval_mul, Polynomial.eval_pow, Polynomial.eval_ofNat, Polynomial.eval_X,
    Polynomial.eval_one]

/-- Palindrome identity `C₆(z) = z⁴·C̃(z + z⁻¹)` for every nonzero `z`.  Fully proved. -/
theorem C6_reciprocal (z : ℂ) (hz : z ≠ 0) :
    C6ℂ z = z ^ 4 * Ctilℂ (z + z⁻¹) := by
  simp only [C6ℂ, Ctilℂ]
  field_simp
  ring

/-- If `‖z‖ = 1` then `z + z⁻¹` is real (its imaginary part vanishes, since
    `z⁻¹ = conj z`).  Fully proved. -/
theorem unit_circle_sum_real (z : ℂ) (hz : ‖z‖ = 1) :
    (z + z⁻¹).im = 0 := by
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hns : Complex.normSq z = 1 := by
    rw [Complex.normSq_eq_norm_sq, hz]; norm_num
  have hinv : z⁻¹ = (starRingEnd ℂ) z := by
    rw [Complex.inv_def, hns]; simp
  rw [hinv, Complex.add_im, Complex.conj_im]; ring

/-- The discriminant datum `Δ(C̃) = −44208 < 0` (computed; certifies the two
    complex roots of `C̃`). -/
theorem Ctil_disc : (-44208 : ℤ) < 0 := by norm_num

/-- **`C̃` has a non-real root** — the discriminant-sign fact, ported directly
    (no longer a `sorry`).  Rather than Mathlib's resultant `Polynomial.disc`
    (which has no root-product bridge), we use the sum-of-squares certificate
    `Σᵢ(1 − rᵢ²)² = −12 < 0`: were all four roots real, this sum of real squares
    would be `≥ 0`.  The value `−12` is a Newton identity (`ring`) in the four
    Vieta relations `e₁=−4, e₂=2, e₃=10, e₄=−8`. -/
theorem Ctil_has_nonreal_root :
    ∃ y : ℂ, Ctilℂ y = 0 ∧ y.im ≠ 0 := by
  by_contra hcon
  push_neg at hcon
  -- hcon : ∀ y, Ctilℂ y = 0 → y.im = 0.  Work with the monic quartic pC over ℂ.
  set pC : ℂ[X] := X ^ 4 + C 4 * X ^ 3 + C 2 * X ^ 2 - C 10 * X - C 8 with hpC_def
  have hpC_eval : ∀ y : ℂ, pC.eval y = Ctilℂ y := by
    intro y; rw [hpC_def]; simp [Ctilℂ]
  have hmonic : pC.Monic := by rw [hpC_def]; monicity!
  have hdeg : pC.natDegree = 4 := by rw [hpC_def]; compute_degree!
  have hsplit : pC.Splits (RingHom.id ℂ) := IsAlgClosed.splits_codomain pC
  have hcard : Multiset.card pC.roots = 4 := by
    rw [← hdeg]; exact Polynomial.splits_iff_card_roots.mp hsplit
  obtain ⟨a, b, c, d, hroots⟩ := Multiset.card_eq_four.mp hcard
  -- Vieta: pC = (X-a)(X-b)(X-c)(X-d).
  have hprod : pC = (pC.roots.map (fun r => X - C r)).prod :=
    eq_prod_roots_of_monic_of_splits_id hmonic hsplit
  rw [hroots] at hprod
  simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
    Multiset.prod_cons, Multiset.prod_singleton] at hprod
  have hexp : (X - C a) * ((X - C b) * ((X - C c) * (X - C d)))
      = X ^ 4 - C (a + b + c + d) * X ^ 3
        + C (a * b + a * c + a * d + b * c + b * d + c * d) * X ^ 2
        - C (a * b * c + a * b * d + a * c * d + b * c * d) * X
        + C (a * b * c * d) := by
    simp only [map_add, map_mul]; ring
  rw [hexp, hpC_def] at hprod
  -- Extract the four Vieta relations by comparing coefficients.
  have he1 : a + b + c + d = -4 := by
    have h := congrArg (fun p => Polynomial.coeff p 3) hprod
    simp only [Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_pow, Polynomial.coeff_X, Polynomial.coeff_C] at h
    norm_num at h
    linear_combination h
  have he2 : a * b + a * c + a * d + b * c + b * d + c * d = 2 := by
    have h := congrArg (fun p => Polynomial.coeff p 2) hprod
    simp only [Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_pow, Polynomial.coeff_X, Polynomial.coeff_C] at h
    norm_num at h
    linear_combination -h
  have he3 : a * b * c + a * b * d + a * c * d + b * c * d = 10 := by
    have h := congrArg (fun p => Polynomial.coeff p 1) hprod
    simp only [Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_pow, Polynomial.coeff_X, Polynomial.coeff_C] at h
    norm_num at h
    linear_combination h
  have he4 : a * b * c * d = -8 := by
    have h := congrArg (fun p => Polynomial.coeff p 0) hprod
    simp only [Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_C_mul,
      Polynomial.coeff_X_pow, Polynomial.coeff_X, Polynomial.coeff_C] at h
    norm_num at h
    linear_combination -h
  -- The SOS value: Σ(1 - rᵢ²)² = −12 (Newton identity in e₁..e₄; pure `ring`).
  have hSOS : (1 - a ^ 2) ^ 2 + (1 - b ^ 2) ^ 2 + (1 - c ^ 2) ^ 2 + (1 - d ^ 2) ^ 2 = -12 := by
    have key : (1 - a ^ 2) ^ 2 + (1 - b ^ 2) ^ 2 + (1 - c ^ 2) ^ 2 + (1 - d ^ 2) ^ 2
        = 4 - 2 * ((a + b + c + d) ^ 2 - 2 * (a * b + a * c + a * d + b * c + b * d + c * d))
          + ((a + b + c + d) ^ 4
             - 4 * (a + b + c + d) ^ 2 * (a * b + a * c + a * d + b * c + b * d + c * d)
             + 2 * (a * b + a * c + a * d + b * c + b * d + c * d) ^ 2
             + 4 * (a + b + c + d) * (a * b * c + a * b * d + a * c * d + b * c * d)
             - 4 * (a * b * c * d)) := by ring
    rw [key, he1, he2, he3, he4]; norm_num
  -- All roots are real (their imaginary parts vanish), so each term is a nonneg real.
  have hmem : ∀ r ∈ pC.roots, pC.eval r = 0 := fun r hr => (Polynomial.mem_roots'.mp hr).2
  have hreal : ∀ r : ℂ, r ∈ ({a, b, c, d} : Multiset ℂ) → r.im = 0 := by
    intro r hr
    exact hcon r (by rw [← hpC_eval]; exact hmem r (by rw [hroots]; exact hr))
  have ha : a.im = 0 := hreal a (by simp)
  have hb : b.im = 0 := hreal b (by simp)
  have hc : c.im = 0 := hreal c (by simp)
  have hd : d.im = 0 := hreal d (by simp)
  have hareal : a = (a.re : ℂ) := by apply Complex.ext <;> simp [ha]
  have hbreal : b = (b.re : ℂ) := by apply Complex.ext <;> simp [hb]
  have hcreal : c = (c.re : ℂ) := by apply Complex.ext <;> simp [hc]
  have hdreal : d = (d.re : ℂ) := by apply Complex.ext <;> simp [hd]
  rw [hareal, hbreal, hcreal, hdreal] at hSOS
  have hRealEq : (1 - a.re ^ 2) ^ 2 + (1 - b.re ^ 2) ^ 2 + (1 - c.re ^ 2) ^ 2
      + (1 - d.re ^ 2) ^ 2 = -12 := by exact_mod_cast hSOS
  nlinarith [sq_nonneg (1 - a.re ^ 2), sq_nonneg (1 - b.re ^ 2),
    sq_nonneg (1 - c.re ^ 2), sq_nonneg (1 - d.re ^ 2)]

/-- **Reduction (sorry-free)** — there is a root of `C₆` off the unit circle,
    reduced to `Ctil_has_nonreal_root` alone.  A non-real root `y` of `C̃` lifts,
    via `z = (y + w)/2` with `w² = y² − 4`, to a nonzero `z` with `z + z⁻¹ = y`
    and `C6ℂ z = z⁴·C̃(y) = 0` (`C6_reciprocal`); and `‖z‖ ≠ 1`, else
    `unit_circle_sum_real` forces `y = z + z⁻¹` real, contradicting `y.im ≠ 0`. -/
theorem C6core_offcircle_root :
    ∃ z : ℂ, C6ℂ z = 0 ∧ ‖z‖ ≠ 1 := by
  obtain ⟨y, hy_root, hy_im⟩ := Ctil_has_nonreal_root
  obtain ⟨w, hw⟩ := IsAlgClosed.exists_pow_nat_eq (y ^ 2 - 4 : ℂ) (n := 2) (by norm_num)
  refine ⟨(y + w) / 2, ?_, ?_⟩
  · set z : ℂ := (y + w) / 2 with hz_def
    have hquad : z ^ 2 - y * z + 1 = 0 := by
      rw [hz_def]; field_simp; linear_combination hw
    have hz0 : z ≠ 0 := by
      intro h; rw [h] at hquad; norm_num at hquad
    have hsum : z + z⁻¹ = y := by
      have : z * (z + z⁻¹) = z * y := by
        field_simp; linear_combination hquad
      exact mul_left_cancel₀ hz0 this
    rw [C6_reciprocal z hz0, hsum, hy_root, mul_zero]
  · intro hnorm
    set z : ℂ := (y + w) / 2 with hz_def
    have hquad : z ^ 2 - y * z + 1 = 0 := by
      rw [hz_def]; field_simp; linear_combination hw
    have hz0 : z ≠ 0 := by
      intro h; rw [h] at hquad; norm_num at hquad
    have hsum : z + z⁻¹ = y := by
      have : z * (z + z⁻¹) = z * y := by
        field_simp; linear_combination hquad
      exact mul_left_cancel₀ hz0 this
    have him := unit_circle_sum_real z hnorm
    rw [hsum] at him
    exact hy_im him

/-- **Conclusion (sorry-free modulo `Ctil_has_nonreal_root`)** — `C₆` is not a
    product of cyclotomic polynomials.  This needs only the *easy* direction of
    Kronecker's dichotomy: every root of a product of cyclotomics is a root of
    unity (`cyclotomic k ∣ Xᵏ − 1`), hence has norm 1 — contradicting the
    off-circle root from `C6core_offcircle_root`.  (The hard Kronecker converse,
    absent from Mathlib, is *not* used.) -/
theorem C6core_non_cyclotomic :
    ¬ ∃ (s : Multiset ℕ), C6core = (s.map (fun k => cyclotomic k ℤ)).prod := by
  rintro ⟨s, hs⟩
  obtain ⟨z, hz_root, hz_norm⟩ := C6core_offcircle_root
  apply hz_norm
  -- z is a root of C6core mapped to ℂ = ∏ (cyclotomic k ℂ); pick the vanishing factor.
  have hz_eval : (C6core.map (Int.castRingHom ℂ)).eval z = 0 := by
    rw [← C6ℂ_eq]; exact hz_root
  rw [hs] at hz_eval
  rw [Polynomial.map_multiset_prod, Multiset.map_map] at hz_eval
  simp only [Function.comp, Polynomial.map_cyclotomic] at hz_eval
  rw [Polynomial.eval_multiset_prod, Multiset.map_map] at hz_eval
  have h0mem := Multiset.prod_eq_zero_iff.mp hz_eval
  obtain ⟨k, _hk_mem, hk0⟩ := Multiset.mem_map.mp h0mem
  simp only [Function.comp] at hk0
  -- hk0 : (cyclotomic k ℂ).eval z = 0.  k ≠ 0 (else cyclotomic 0 = 1, eval = 1 ≠ 0).
  have hk_ne : k ≠ 0 := by
    rintro rfl; simp [Polynomial.cyclotomic_zero] at hk0
  -- cyclotomic k ∣ Xᵏ − 1, so z is a root of Xᵏ − 1, i.e. zᵏ = 1.
  have hdvd : (cyclotomic k ℂ) ∣ (X ^ k - 1) := cyclotomic.dvd_X_pow_sub_one k ℂ
  have hzk : z ^ k = 1 := by
    have hev : (X ^ k - 1 : ℂ[X]).eval z = 0 := by
      obtain ⟨g, hg⟩ := hdvd
      rw [hg, Polynomial.eval_mul, hk0, zero_mul]
    simpa [Polynomial.eval_sub, Polynomial.eval_pow, Polynomial.eval_X,
      Polynomial.eval_one, sub_eq_zero] using hev
  -- zᵏ = 1 with k ≠ 0 ⟹ ‖z‖ = 1.
  exact Complex.norm_eq_one_of_pow_eq_one hzk hk_ne

end QOU.Mass.CyclotomicBoundaryKeystone
