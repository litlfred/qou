import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.ComputeDegree
import Mathlib.Tactic.LinearCombination

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
* `Ctil_no_four_real_roots`, `Ctil_has_nonreal_root` — `C̃` has a non-real root,
  proved from scratch via the explicit 16-term discriminant identity (see the
  section below); no `sorry`, no axiom.
* `C6core_offcircle_root` — `C₆` has a root off the unit circle (**derived**, via
  the reciprocal transform, from `Ctil_has_nonreal_root` alone).
* `C6core_non_cyclotomic` — `C₆` is **not** a product of cyclotomic polynomials
  (**derived** from `C6core_offcircle_root`).  Crucially this uses only the *easy*
  direction of Kronecker's dichotomy — every root of a product of cyclotomics is a
  root of unity, hence norm 1 (`cyclotomic.dvd_X_pow_sub_one` +
  `Complex.norm_eq_one_of_pow_eq_one`, both in Mathlib) — and does **not** need the
  hard Kronecker converse.

## The former residual gap — now closed (fully sorry-free)

`Ctil_has_nonreal_root` (`C̃` has a non-real root) was previously the file's
single `sorry`.  It is now **proved** with no `sorry` and no axiom.  Mathlib has
no quartic-discriminant `= ∏_{i<j}(rᵢ−rⱼ)²` bridge, so the fact is derived from
scratch:

* `Ctil_no_four_real_roots` — for reals `a,b,c,d` with the Vieta data of `C̃`
  (`Σ = −4`, `Σ₂ = 2`, `Σ₃ = 10`, `Π = −8`), the Vandermonde square
  `∏_{i<j}(rᵢ−rⱼ)²` equals the explicit **16-term** discriminant polynomial in the
  elementary symmetric functions (a pure `ring` identity), which at those Vieta
  values is `Δ(C̃) = −44208 < 0`; a Vandermonde square of reals is `≥ 0`, so no
  four reals are the roots of `C̃`.
* `Ctil_has_nonreal_root` — `C̃` is monic of degree 4, hence over `ℂ` it splits
  into four roots `a,b,c,d` (`IsAlgClosed.splits_codomain`,
  `eq_prod_roots_of_monic_of_splits_id`, `Multiset.card_eq_four`).  Were all four
  real, Vieta feeds `Ctil_no_four_real_roots` to a contradiction; so some root has
  nonzero imaginary part.

Consequently the entire **Tier-2, n = 6** non-cyclotomicity chain is sorry-free.
The full Tier-2 claim — `D(n)` non-cyclotomic for *all* `n ≥ 6` — is
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

set_option maxHeartbeats 4000000 in
/-- Quartic discriminant identity `∏_{i<j}(rᵢ−rⱼ)² = Δ(C̃)` written in the
    elementary symmetric functions of `a,b,c,d` (16 terms; a pure `ring`
    identity), evaluated at the Vieta values of `C̃`: if four reals are the
    roots of `C̃` (`Σ = −4`, `Σ₂ = 2`, `Σ₃ = 10`, `Π = −8`) then their
    Vandermonde square equals `Δ(C̃) = −44208 < 0` (`Ctil_disc`) — impossible,
    since a Vandermonde square of reals is `≥ 0`.  Hence `C̃` has no four real
    roots. -/
theorem Ctil_no_four_real_roots (a b c d : ℝ)
    (h1 : a + b + c + d = -4)
    (h2 : a*b + a*c + a*d + b*c + b*d + c*d = 2)
    (h3 : a*b*c + a*b*d + a*c*d + b*c*d = 10)
    (h4 : a*b*c*d = -8) : False := by
  have hk : ((a-b)*(a-c)*(a-d)*(b-c)*(b-d)*(c-d))^2 =
    -27*(a + b + c + d)^4*(a*b*c*d)^2 + 18*(a + b + c + d)^3*(a*b + a*c + a*d + b*c + b*d + c*d)*(a*b*c + a*b*d + a*c*d + b*c*d)*(a*b*c*d) - 4*(a + b + c + d)^3*(a*b*c + a*b*d + a*c*d + b*c*d)^3 - 4*(a + b + c + d)^2*(a*b + a*c + a*d + b*c + b*d + c*d)^3*(a*b*c*d) + (a + b + c + d)^2*(a*b + a*c + a*d + b*c + b*d + c*d)^2*(a*b*c + a*b*d + a*c*d + b*c*d)^2 + 144*(a + b + c + d)^2*(a*b + a*c + a*d + b*c + b*d + c*d)*(a*b*c*d)^2 - 6*(a + b + c + d)^2*(a*b*c + a*b*d + a*c*d + b*c*d)^2*(a*b*c*d) - 80*(a + b + c + d)*(a*b + a*c + a*d + b*c + b*d + c*d)^2*(a*b*c + a*b*d + a*c*d + b*c*d)*(a*b*c*d) + 18*(a + b + c + d)*(a*b + a*c + a*d + b*c + b*d + c*d)*(a*b*c + a*b*d + a*c*d + b*c*d)^3 - 192*(a + b + c + d)*(a*b*c + a*b*d + a*c*d + b*c*d)*(a*b*c*d)^2 + 16*(a*b + a*c + a*d + b*c + b*d + c*d)^4*(a*b*c*d) - 4*(a*b + a*c + a*d + b*c + b*d + c*d)^3*(a*b*c + a*b*d + a*c*d + b*c*d)^2 - 128*(a*b + a*c + a*d + b*c + b*d + c*d)^2*(a*b*c*d)^2 + 144*(a*b + a*c + a*d + b*c + b*d + c*d)*(a*b*c + a*b*d + a*c*d + b*c*d)^2*(a*b*c*d) - 27*(a*b*c + a*b*d + a*c*d + b*c*d)^4 + 256*(a*b*c*d)^3 := by
    ring
  have hval : ((a-b)*(a-c)*(a-d)*(b-c)*(b-d)*(c-d))^2 = -44208 := by rw [hk, h1, h2, h3, h4]; norm_num
  have hpos : (0:ℝ) ≤ ((a-b)*(a-c)*(a-d)*(b-c)*(b-d)*(c-d))^2 := sq_nonneg _
  rw [hval] at hpos
  norm_num at hpos

/-- **`C̃` has a non-real root** (sorry-free).  `C̃ = X⁴+4X³+2X²−10X−8` is monic
    of degree 4, so over `ℂ` it splits into four roots `a,b,c,d`
    (`IsAlgClosed.splits_codomain` + `eq_prod_roots_of_monic_of_splits_id`).  If
    all four were real, Vieta gives `Σ = −4, Σ₂ = 2, Σ₃ = 10, Π = −8`, whence
    `Ctil_no_four_real_roots` derives `False` from `Δ(C̃) = −44208 < 0`.  So some
    root has nonzero imaginary part.  This is the classical fact
    `Δ < 0 ⇒` non-real root, here proved from scratch (Mathlib has no quartic
    discriminant bridge) via the explicit 16-term symmetric identity. -/
theorem Ctil_has_nonreal_root :
    ∃ y : ℂ, Ctilℂ y = 0 ∧ y.im ≠ 0 := by
  by_contra hcon
  push_neg at hcon
  set P : ℂ[X] := X ^ 4 + C 4 * X ^ 3 + C 2 * X ^ 2 - C 10 * X - C 8 with hPdef
  have hPeval : ∀ y : ℂ, P.eval y = Ctilℂ y := by
    intro y
    rw [hPdef]
    simp only [Ctilℂ, eval_add, eval_sub, eval_mul, eval_pow, eval_C, eval_X]
  have hPmonic : P.Monic := by rw [hPdef]; monicity!
  have hPdeg : P.natDegree = 4 := by rw [hPdef]; compute_degree!
  have hsplit : Splits (RingHom.id ℂ) P := IsAlgClosed.splits_codomain P
  have hcard : P.roots.card = 4 := by rw [splits_iff_card_roots.mp hsplit, hPdeg]
  obtain ⟨a, b, c, d, hroots⟩ := Multiset.card_eq_four.mp hcard
  have hfacP : P = (X - C a) * (X - C b) * (X - C c) * (X - C d) := by
    have h := eq_prod_roots_of_monic_of_splits_id hPmonic hsplit
    rw [hroots] at h
    simp only [Multiset.insert_eq_cons, Multiset.map_cons, Multiset.map_singleton,
      Multiset.prod_cons, Multiset.prod_singleton] at h
    rw [h]; ring
  have hf : ∀ y : ℂ, Ctilℂ y = (y - a) * (y - b) * (y - c) * (y - d) := by
    intro y
    rw [← hPeval, hfacP]
    simp only [eval_mul, eval_sub, eval_X, eval_C]
  have hia : a.im = 0 := hcon a (by rw [hf]; ring)
  have hib : b.im = 0 := hcon b (by rw [hf]; ring)
  have hic : c.im = 0 := hcon c (by rw [hf]; ring)
  have hidd : d.im = 0 := hcon d (by rw [hf]; ring)
  have hae : a = (a.re : ℂ) := by apply Complex.ext <;> simp [hia]
  have hbe : b = (b.re : ℂ) := by apply Complex.ext <;> simp [hib]
  have hce : c = (c.re : ℂ) := by apply Complex.ext <;> simp [hic]
  have hde : d = (d.re : ℂ) := by apply Complex.ext <;> simp [hidd]
  set α := a.re with hαdef
  set β := b.re with hβdef
  set γ := c.re with hγdef
  set δ := d.re with hδdef
  have hr : ∀ x : ℝ, x^4 + 4*x^3 + 2*x^2 - 10*x - 8 = (x-α)*(x-β)*(x-γ)*(x-δ) := by
    intro x
    have h := hf (x : ℂ)
    rw [hae, hbe, hce, hde] at h
    simp only [Ctilℂ] at h
    refine Complex.ofReal_injective ?_
    push_cast
    linear_combination h
  refine Ctil_no_four_real_roots α β γ δ ?_ ?_ ?_ ?_
  · linear_combination (1/2) * hr 0 - (1/2) * hr 1 - (1/6) * hr (-1) + (1/6) * hr 2
  · linear_combination hr 0 - (1/2) * hr 1 - (1/2) * hr (-1)
  · linear_combination -(1/2) * hr 0 + hr 1 - (1/3) * hr (-1) - (1/6) * hr 2
  · linear_combination -hr 0

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
