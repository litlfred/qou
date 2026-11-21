/-
  `σ₀σ₁σ₀` is not a scalar multiple of a product of two photons, for every `q`.

  Companion to `docs/audits/2026-11-21-electron-word-gs-interactions.md` (§C2c).
  That study found, by a Gröbner basis at eight fixed rational values of `q`
  (including the proton `q₀`), that `γ(φ)·γ(ψ) = c·σ₀σ₁σ₀` has no solution with
  `c ≠ 0`; the run over `ℚ(q)` did not finish. This module proves it for every
  `q`, with no exceptional values.

  **Statement.** Let `K` be a field, `A` a `K`-algebra, `h ∈ K`, and `x, y ∈ A`
  with `y` a unit, satisfying the Hecke relations `x² = h x + 1`, `y² = h y + 1`,
  the braid relation `x y x = y x y`, and such that the six words
  `1, x, y, xy, yx, xyx` are linearly independent. Then for all photon weights
  `φ, ψ` and all `c ∈ K`,
      `γ(φ) · γ(ψ) = c · xyx  →  c = 0`,
  where `γ` is the corpus photon `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`
  (`QOU.Photon.photon`). In `H₃(q)` take `x = σ₀`, `y = σ₁`, `h = q − q⁻¹`: the
  hypotheses hold for every invertible `q` (the standard basis), so no value of
  `q` is exceptional — not roots of unity, not `q² = −1`, not `h = 0`.

  **Proof idea.** `σ₁⁻¹ = σ₁ − h`, so `γ(φ) = 1 + a x + b y + e xy` with
  `a = φ₀ − hφ₀₁`, `b = φ₁`, `e = φ₀₁`. Write `γ = α + β y` with `α = 1 + a x`,
  `β = b + e x` in the commutative subalgebra `K[x]`. The product equation splits
  over the left `K[x]`-basis `1, y, yx` into
      `αα' + b'β = 0`,  `αβ' + (1 + h b')β = 0`,  `β(a' + e'x) = c x`.
  From these, `c x δ = 0` for `δ = b'β' − (1 + h b')α'` (an explicit polynomial
  certificate, `core` below), so `c ≠ 0` forces `δ = 0`, i.e. `b'² = h b' + 1`
  and `e' = a'b'`. Then `a' + e'x = a'(1 + b'x)` and `(1 + b'x)(b' − x) = 0`, so
  `c x (b' − x) = 0`, whose constant coefficient is `−c`. Hence `c = 0`.

  Generic field `K` (§7c); no ordering, no Real construct.

  -- Ref: [leitner2026] predicted-spectra, def:photon;
  --      docs/audits/2026-11-21-electron-word-gs-interactions.md §C2c
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Module
import QOU.Photon

namespace QOU.BraidKnot.LongestWordNotTwoPhoton

open QOU.Photon

/-- **Scalar core.** The six coefficient equations of
    `(1 + a x + b y + e xy)(1 + a' x + b' y + e' xy) = c · xyx` in the standard
    basis of `H₃` force `c = 0`, over any field and for every `h`. -/
theorem core {K : Type*} [Field K] (h a b e a' b' e' c : K)
    (e1 : 1 + a * a' + b * b' = 0)
    (e2 : a + a' + h * a * a' + e * b' = 0)
    (e3 : b + b' + h * b * b' + a * e' = 0)
    (e4 : e + e' + a * b' + h * (a * e' + e * b') = 0)
    (e5 : b * a' + e * e' = 0)
    (e6 : b * e' + e * a' + h * e * e' = c) :
    c = 0 := by
  by_contra hc
  -- `c · δ₁ = 0` and `c · (δ₀ + h δ₁) = 0`, where `δ = (δ₀, δ₁)`.
  have k1 : c * (b' * e' - a' - h * a' * b') = 0 := by
    linear_combination (a' * b' + e' ^ 2) * e1 + (e' * (a' + b' + e' * h)) * e2
      + (-(a' * (e' + 1))) * e3 + (-(a' ^ 2 + a' * e' * h + e')) * e4
      + (-b' ^ 2 + b' * h + 1) * e5 + (a' * b' * h + a' - b' * e') * e6
  have k2 : c * ((b' ^ 2 - h * b' - 1) + h * (b' * e' - a' - h * a' * b')) = 0 := by
    linear_combination (e' * (a' + b' + e' * h)) * e1
      + (a' * b' + a' * e' * h + b' * e' * h + e' ^ 2 * h ^ 2 + e' ^ 2) * e2
      + (-(a' ^ 2 + a' * e' * h + e')) * e3
      + (-(a' ^ 2 * h + a' * e' * h ^ 2 + a' * e' + a' + e' * h)) * e4
      + (a' * b' * h + a' - b' * e') * e5
      + (a' * b' * h ^ 2 + a' * h - b' ^ 2 - b' * e' * h + b' * h + 1) * e6
  have d1 : b' * e' - a' - h * a' * b' = 0 := (mul_eq_zero.mp k1).resolve_left hc
  have d0' := (mul_eq_zero.mp k2).resolve_left hc
  have d0 : b' ^ 2 - h * b' - 1 = 0 := by linear_combination d0' - h * d1
  -- `b'(e' − a'b') = δ₁ − a'δ₀ = 0` and `b'(b' − h) = 1`, so `e' = a'b'`.
  have he : e' = a' * b' := by
    linear_combination (b' - h) * d1 - (b' - h) * a' * d0 - (e' - a' * b') * d0
  -- Finally `c = b'·e5 − (e6) − a'e·δ₀ + (e' − a'b')(b − b'e + eh)`.
  apply hc
  linear_combination (-1 : K) * e6 + b' * e5 - a' * e * d0
    + (b - b' * e + e * h) * he

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- Inverse of a Hecke generator: `y² = h y + 1` gives `y⁻¹ = y − h`. -/
theorem inv_eq (h : K) (y : Aˣ) (hy : (y : A) * y = h • (y : A) + 1) :
    ((y⁻¹ : Aˣ) : A) = (y : A) - h • (1 : A) := by
  have hy' : (y : A) * ((y : A) - h • (1 : A)) = 1 := by
    rw [mul_sub, hy, mul_smul_comm, mul_one]; abel
  calc ((y⁻¹ : Aˣ) : A) = ((y⁻¹ : Aˣ) : A) * ((y : A) * ((y : A) - h • (1 : A))) := by
        rw [hy', mul_one]
    _ = (y : A) - h • (1 : A) := by rw [← mul_assoc, Units.inv_mul, one_mul]

/-- The photon in straight coordinates: `γ(φ) = 1 + (φ₀ − hφ₀₁)x + φ₁y + φ₀₁xy`. -/
theorem photon_straight (h : K) (x : A) (y : Aˣ) (hy : (y : A) * y = h • (y : A) + 1)
    (φ : Colour K) :
    photon x y φ = 1 + (φ.phi0 - h * φ.phi01) • x + φ.phi1 • (y : A)
      + φ.phi01 • (x * (y : A)) := by
  simp only [photon, vertex, inv_eq h y hy, mul_sub, mul_smul_comm, mul_one]
  module

/-- Product of two straight-coordinate elements, reduced to the standard basis
    `1, x, y, xy, yx, xyx` by the Hecke and braid relations. -/
theorem mul_straight (h : K) (x y : A)
    (hx : x * x = h • x + 1) (hy : y * y = h • y + 1) (hbr : x * y * x = y * x * y)
    (a b e a' b' e' : K) :
    (1 + a • x + b • y + e • (x * y)) * (1 + a' • x + b' • y + e' • (x * y))
      = (1 + a * a' + b * b') • (1 : A)
        + (a + a' + h * a * a' + e * b') • x
        + (b + b' + h * b * b' + a * e') • y
        + (e + e' + a * b' + h * (a * e' + e * b')) • (x * y)
        + (b * a' + e * e') • (y * x)
        + (b * e' + e * a' + h * e * e') • (x * y * x) := by
  have hxxy : x * (x * y) = h • (x * y) + y := by
    rw [← mul_assoc, hx, add_mul, smul_mul_assoc, one_mul]
  have hyxy : y * (x * y) = x * y * x := by rw [hbr, mul_assoc]
  have hxyx : x * y * x = x * (y * x) := mul_assoc _ _ _
  have hxyy : x * y * y = h • (x * y) + x := by
    rw [mul_assoc, hy, mul_add, mul_smul_comm, mul_one]
  have hxyxy : x * y * (x * y) = h • (x * y * x) + y * x := by
    calc x * y * (x * y) = y * x * y * y := by rw [← hbr]; simp only [mul_assoc]
      _ = y * x * (y * y) := by simp only [mul_assoc]
      _ = h • (y * x * y) + y * x := by rw [hy, mul_add, mul_smul_comm, mul_one]
      _ = h • (x * y * x) + y * x := by rw [hbr]
  simp only [add_mul, mul_add, one_mul, mul_one, smul_mul_assoc, mul_smul_comm]
  rw [hx, hy, hxxy, hyxy, hxyy, hxyxy, mul_assoc x y x]
  module

/-- **`σ₀σ₁σ₀` is not a scalar multiple of a two-photon product.** In any
    `K`-algebra containing Hecke generators `x, y` (with `y` a unit) on which the
    six words `1, x, y, xy, yx, xyx` are independent — in particular `H₃(q)` for
    every invertible `q`, with `h = q − q⁻¹` — the equation
    `γ(φ) · γ(ψ) = c · xyx` holds only with `c = 0`. -/
theorem photon_mul_photon_ne_smul_longest (h : K) (x : A) (y : Aˣ)
    (hx : x * x = h • x + 1) (hy : (y : A) * y = h • (y : A) + 1)
    (hbr : x * y * x = y * x * y)
    (hind : LinearIndependent K ![(1 : A), x, (y : A), x * y, y * x, x * y * x])
    (φ ψ : Colour K) (c : K)
    (hprod : photon x y φ * photon x y ψ = c • (x * (y : A) * x)) :
    c = 0 := by
  rw [photon_straight h x y hy, photon_straight h x y hy,
    mul_straight h x y hx hy hbr] at hprod
  set a := φ.phi0 - h * φ.phi01
  set a' := ψ.phi0 - h * ψ.phi01
  set b := φ.phi1
  set b' := ψ.phi1
  set e := φ.phi01
  set e' := ψ.phi01
  have hsum : (1 + a * a' + b * b') • (1 : A) + (a + a' + h * a * a' + e * b') • x
      + (b + b' + h * b * b' + a * e') • (y : A)
      + (e + e' + a * b' + h * (a * e' + e * b')) • (x * (y : A))
      + (b * a' + e * e') • ((y : A) * x)
      + (b * e' + e * a' + h * e * e' - c) • (x * (y : A) * x) = 0 := by
    rw [← sub_eq_zero.mpr hprod]; module
  have hz := (Fintype.linearIndependent_iff.mp hind)
    ![1 + a * a' + b * b', a + a' + h * a * a' + e * b', b + b' + h * b * b' + a * e',
      e + e' + a * b' + h * (a * e' + e * b'), b * a' + e * e',
      b * e' + e * a' + h * e * e' - c]
    (by simpa [Fin.sum_univ_six] using hsum)
  exact core h a b e a' b' e' c (by simpa using hz 0) (by simpa using hz 1)
    (by simpa using hz 2) (by simpa using hz 3) (by simpa using hz 4)
    (sub_eq_zero.mp (by simpa using hz 5))

end QOU.BraidKnot.LongestWordNotTwoPhoton
