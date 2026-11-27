import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Nuclear.QHankelGreenIdentity — the algebraic half of q-Hankel orthogonality

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27); bean `qou-t3nx`.
The Coulomb shape-factor probe `computations/probes/coulomb_shape_factor_qbessel_probe.py`
uses the Hahn–Exton q-Bessel function `J_ν(x; Q)`, `Q = p²`, on the Jackson lattice
`x = p^k`, `k ∈ ℤ`, and checks numerically the Koelink–Swarttouw orthogonality

    Σ_{k ∈ ℤ} p^{2k} J_ν(p^k) J_ν(p^{k+m}) = δ_{m0}.

This file proves the part of that statement that is algebra, over any field.

## Results

* `hahnExton_qdifference`: the Hahn–Exton series `S(y) = Σ c_j y^j`, with
  `c_j (1 − Q^j)(1 − a Q^{j−1}) = −Q^j c_{j−1}` and `a = Q^{ν+1}`, satisfies, as a formal power
  series, `a S(Q²y) − (Q + a) S(Q y) + Q S(y) + Q² y S(Q y) = 0`.
* `jacobi_form`: on the lattice `y = Q^k`, writing `F_k = t^k s_k` with `t² = Q^ν`, that
  q-difference equation is the symmetric second-order equation
  `t (F_{k+1} + F_{k−1}) − (1 + t²) F_k = −Q^k F_k`. The weight `Q^k = p^{2k}` is the
  q-Hankel measure `x² d_p x / x` of the probe.
* `green_window`: the discrete Green identity. For two solutions of
  `t (F_{k+1} + F_{k−1}) − (1 + t²) F_k = −λ w_k F_k` with eigenvalues `λ, μ`,
  `(μ − λ) Σ_{k=m}^{m+N−1} w_k F_k G_k = t (D_{m+N−1} − D_{m−1})`,
  where `D_k = F_{k+1} G_k − F_k G_{k+1}` is the Casoratian.
* `dilate_eigen` and `qhankel_window`: the dilate `k ↦ F_{k+n}` solves the same equation with
  eigenvalue `Q^n`, so for any lattice window
  `(Q^n − Q^m) Σ_k Q^k F_{k+m} F_{k+n} = t (D_{top} − D_{bottom})`.

Convention check (not a proof input): the probe's own `hahn_exton_on_lattice` values
`J_{1/2}(p^k; p²)` satisfy `jacobi_form` with `t = p^{1/2}`, `Q = p²` to 80 digits at a test
step. The base is `Q = p² = q₀⁻²`, the inverse of the sphere side's Jackson base `q²`.

So q-Hankel orthogonality for `m ≠ n` is exactly the statement that the Casoratian boundary
terms vanish as the window grows to all of `ℤ`, and `Q^n ≠ Q^m` is the only algebraic input.

## Not established (analytic; belongs in `QOU/Transcendental/`)

* That the lattice values `s_k = S(Q^k)` of the convergent series satisfy the hypothesis of
  `jacobi_form` (evaluating a power series is analytic).
* That the boundary Casoratians tend to `0` at `k → ±∞`, which gives orthogonality.
* The normalisation `Σ_k Q^k F_k² = 1` and completeness (q-Hankel inversion).

Base field generic (§7c); `t` plays `Q^{ν/2}`, and nothing requires `ν` real.
No empirical value enters any proof. Sorry-free.

-- Ref: [koelink-swarttouw-1994] https://doi.org/10.1006/jmaa.1994.1330
-/

namespace QOU.Nuclear.QHankel

open Finset

variable {K : Type*} [Field K]

/-! ### The formal q-difference equation of the Hahn–Exton series -/

/-- **Hahn–Exton q-difference equation (formal).** -/
theorem hahnExton_qdifference (Q a : K) (c : ℕ → K)
    (hc : ∀ j, c (j + 1) * ((1 - Q ^ (j + 1)) * (1 - a * Q ^ j)) = -(Q ^ (j + 1) * c j)) :
    a • PowerSeries.rescale (Q ^ 2) (PowerSeries.mk c) -
        (Q + a) • PowerSeries.rescale Q (PowerSeries.mk c) + Q • PowerSeries.mk c +
      Q ^ 2 • (PowerSeries.X * PowerSeries.rescale Q (PowerSeries.mk c)) = 0 := by
  ext n
  simp only [map_add, map_sub, PowerSeries.coeff_smul, PowerSeries.coeff_rescale,
    PowerSeries.coeff_mk, map_zero, smul_eq_mul]
  cases n with
  | zero => simp; ring
  | succ j =>
    rw [PowerSeries.coeff_succ_X_mul, PowerSeries.coeff_rescale, PowerSeries.coeff_mk]
    linear_combination (Q * 1) * hc j

/-! ### The symmetric (Jacobi) form on the lattice -/

/-- **Symmetric form.** If `t² s_{k+2} − (1 + t² − Q^{k+1}) s_{k+1} + s_k = 0` on `ℤ` and
`F_k = t^k s_k`, then `t (F_{k+1} + F_{k−1}) − (1 + t²) F_k = −Q^k F_k`. -/
theorem jacobi_form (Q t : Kˣ) (s : ℤ → K)
    (hs : ∀ k : ℤ, (t : K) ^ 2 * s (k + 2) - (1 + (t : K) ^ 2 - ((Q ^ (k + 1) : Kˣ) : K)) * s (k + 1)
      + s k = 0) (k : ℤ) :
    (t : K) * (((t ^ (k + 1) : Kˣ) : K) * s (k + 1) + ((t ^ (k - 1) : Kˣ) : K) * s (k - 1)) -
        (1 + (t : K) ^ 2) * (((t ^ k : Kˣ) : K) * s k) =
      -(((Q ^ k : Kˣ) : K) * (((t ^ k : Kˣ) : K) * s k)) := by
  have h := hs (k - 1)
  rw [show k - 1 + 2 = k + 1 by ring, show k - 1 + 1 = k by ring] at h
  have e1 : ((t ^ (k + 1) : Kˣ) : K) = ((t ^ k : Kˣ) : K) * t := by
    rw [zpow_add_one, Units.val_mul]
  have e2 : ((t ^ k : Kˣ) : K) = ((t ^ (k - 1) : Kˣ) : K) * t := by
    rw [← Units.val_mul, ← zpow_add_one, sub_add_cancel]
  rw [e1, e2]
  linear_combination ((t ^ (k - 1) : Kˣ) : K) * (t : K) * h

/-! ### The discrete Green identity -/

/-- The Casoratian `D_k = F_{k+1} G_k − F_k G_{k+1}`. -/
def casoratian (F G : ℤ → K) (k : ℤ) : K := F (k + 1) * G k - F k * G (k + 1)

/-- **Discrete Green identity on a window.** -/
theorem green_window (t lam mu : K) (w F G : ℤ → K)
    (hF : ∀ k, t * (F (k + 1) + F (k - 1)) - (1 + t ^ 2) * F k = -(lam * w k * F k))
    (hG : ∀ k, t * (G (k + 1) + G (k - 1)) - (1 + t ^ 2) * G k = -(mu * w k * G k))
    (m : ℤ) (N : ℕ) :
    (mu - lam) * ∑ i ∈ range N, w (m + i) * F (m + i) * G (m + i) =
      t * (casoratian F G (m + N - 1) - casoratian F G (m - 1)) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [sum_range_succ, mul_add, ih]
    have h1 := hF (m + N)
    have h2 := hG (m + N)
    simp only [casoratian, Nat.cast_succ] at *
    rw [show m + (N + 1 : ℤ) - 1 + 1 = m + N + 1 by ring, show m + (N + 1 : ℤ) - 1 = m + N by ring,
      show m + (N : ℤ) - 1 + 1 = m + N by ring]
    linear_combination F (m + N) * h2 - G (m + N) * h1

/-! ### Dilates and the q-Hankel window -/

/-- **Dilation shifts the eigenvalue.** If `F` solves the lattice equation with weight `Q^k` and
eigenvalue `1`, the dilate `k ↦ F_{k+n}` solves it with eigenvalue `Q^n`. -/
theorem dilate_eigen (Q : Kˣ) (t : K) (F : ℤ → K)
    (hF : ∀ k, t * (F (k + 1) + F (k - 1)) - (1 + t ^ 2) * F k = -(((Q ^ k : Kˣ) : K) * F k))
    (n k : ℤ) :
    t * (F (k + 1 + n) + F (k - 1 + n)) - (1 + t ^ 2) * F (k + n) =
      -(((Q ^ n : Kˣ) : K) * ((Q ^ k : Kˣ) : K) * F (k + n)) := by
  have h := hF (k + n)
  rw [show k + n + 1 = k + 1 + n by ring, show k + n - 1 = k - 1 + n by ring] at h
  rw [h, ← Units.val_mul, ← zpow_add, add_comm n k]

/-- **The q-Hankel window identity.** For a lattice solution `F` (weight `Q^k`), and two
dilates `m, n`, the weighted inner product over any window equals a difference of two
Casoratians. When `Q^n ≠ Q^m`, orthogonality of the dilates is exactly the vanishing of the
boundary terms. -/
theorem qhankel_window (Q : Kˣ) (t : K) (F : ℤ → K)
    (hF : ∀ k, t * (F (k + 1) + F (k - 1)) - (1 + t ^ 2) * F k = -(((Q ^ k : Kˣ) : K) * F k))
    (m n a : ℤ) (N : ℕ) :
    (((Q ^ n : Kˣ) : K) - ((Q ^ m : Kˣ) : K)) *
        ∑ i ∈ range N, ((Q ^ (a + i) : Kˣ) : K) * F (a + i + m) * F (a + i + n) =
      t * (casoratian (fun k => F (k + m)) (fun k => F (k + n)) (a + N - 1) -
        casoratian (fun k => F (k + m)) (fun k => F (k + n)) (a - 1)) := by
  refine green_window t _ _ (fun k => ((Q ^ k : Kˣ) : K)) (fun k => F (k + m))
    (fun k => F (k + n)) ?_ ?_ a N
  · intro k; have := dilate_eigen Q t F hF m k; simp only at this ⊢; linear_combination this
  · intro k; have := dilate_eigen Q t F hF n k; simp only at this ⊢; linear_combination this

end QOU.Nuclear.QHankel
