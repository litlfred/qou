/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Gevrey growth of the C1 formal solution at ∞ (W2 Stokes signature)

W2 ∞-side brick (bean `qou-xufp`). The C1 module `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` has, at
`∞`, the formal power-series solution `f(x) = ∑ cₙ x^{−n}` with (witness
`computations/qbeta/c3_w2_inf_formal_solution.witness.json`):

  `c_{m+1} = c_m·(1 + (q−1)q^m + (q−1)q^{2m})`,  `c_0 = 1`.

The ratio `c_{m+1}/c_m` has q-degree `2m+1`, so the q-degree of `cₙ` is
`d_n = ∑_{m<n}(2m+1)`. This file proves `d_n = n²` — i.e. the coefficients grow like
`q^{n²}`. That divergence is the ∞ Stokes signature: the formal series does not converge
and must be q-Borel/Laplace summed; the sector-difference of the sums is the Stokes
multiplier datum `U ∈ ℂ²` (the RSZ-wild residual, beaned).

**Order convention — corrected 2026-08-08.** This docstring previously called `q^{n²}`
"the q-Gevrey-½ divergence". Under the definition this corpus actually formalised,
`QOU.Mathlib.QGevreyOrder.IsQGevreyOrder q s a` ⟺ `‖aₙ‖ ∼ Cⁿ q^{s n²/2}`, the growth
`q^{n²}` has order **2**, not ½ — proved there as `qSquare_gaussian_order_two`, sitting
next to `routeB_gaussian_order_half` (`q^{m²/4}`, order ½) so the two are visible
together. Both conventions exist in the literature (order `s` as `q^{s n²/2}`, used here
and by RSZ for the Newton-polygon slope, versus order `s` as `q^{n²/(2s)}`), and they are
inverses. The `½` cannot be read off `q^{n²}` under the formalised one. Which label is
*intended* is an owner call — flagged, not silently flipped — and it matters because the
Door-i / route-A isoclinicity obstruction is carried across files by that number
(`ThetaSlopeArithmetic.c1Slope`, a **definition** there rather than a derivation).

**Scope.** The growth-degree identity `∑_{m<n}(2m+1) = n²` (= `deg_q cₙ`), plus — added
2026-08-08 — the *derivation* of the ratio degree it used to assume. `natDegree_c1MultPoly`
proves the per-step multiplier `1 + (q−1)qᵐ + (q−1)q^{2m}`, read as a `Polynomial ℤ` in `q`,
has degree exactly `2m+1`; `natDegree_c1CoeffPoly` then chains that through `natDegree_mul`
to `deg_q cₙ = n²` **from the recursion** rather than from a docstring claim. What is still
taken from the witness is the recursion itself.
The Stokes summation is NOT here. §7c: `ℕ` degrees. Sorry-free. No fit; nothing wired.

-- Ref: [manuscript] docs/audits/2026-08-01-c1-inf-slope-half-rsz-stokes.md (W2 ∞)
-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§4-5, summation/Stokes)
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas

namespace QOU.Mass.C1FormalSolutionGrowth

open Finset

/-- **q-degree of the `n`-th C1 formal coefficient**, `d_n = ∑_{m<n}(2m+1)`, from the
ratio degree `deg_q(c_{m+1}/c_m) = 2m+1`. -/
def c1FormalDeg (n : ℕ) : ℕ := ∑ m ∈ range n, (2 * m + 1)

/-- **Gaussian growth**: `deg_q(cₙ) = n²`. The C1 formal solution at ∞ has coefficients of
q-degree `n²`, i.e. growth `q^{n²}` — the divergent (q-Gevrey) behaviour that forces Stokes
summation. Under `QOU.Mathlib.QGevreyOrder.IsQGevreyOrder` that is order **2**; see the
order-convention note in the module docstring. Proof: the sum of the first `n` odd numbers
is `n²`. -/
theorem c1FormalDeg_eq_sq (n : ℕ) : c1FormalDeg n = n ^ 2 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [c1FormalDeg, Finset.sum_range_succ, ← c1FormalDeg, ih]
    ring

/-- The growth is strictly super-linear for `n ≥ 2` (`n² > c·n` eventually) — a divergent
formal series, confirming the ∞ singularity is irregular (not Fuchsian). Stated as the
per-step increment `d_{n+1} − d_n = 2n+1`, which is unbounded. -/
theorem c1FormalDeg_step (n : ℕ) : c1FormalDeg (n + 1) = c1FormalDeg n + (2 * n + 1) := by
  rw [c1FormalDeg, Finset.sum_range_succ, ← c1FormalDeg]


/-! ## The ratio degree, derived

`c1FormalDeg_eq_sq` above assumes `deg_q(c_{m+1}/c_m) = 2m+1`. That assumption is
discharged here: reading the multiplier as a polynomial in `q` over `ℤ` makes the degree a
theorem, and `natDegree_mul` chains it to `n²` directly from the recursion — so the `n²` no
longer rests on the docstring.

The `m = 0` case is the only wrinkle: there `(q−1)qᵐ` and `(q−1)q^{2m}` coincide, so the
leading coefficient is `2` rather than `1`. The degree is still `2m+1 = 1`, but the
argument has to branch. -/

open Polynomial

noncomputable def c1MultPoly (m : ℕ) : Polynomial ℤ :=
  1 + (X - 1) * X ^ m + (X - 1) * X ^ (2 * m)

private lemma c1MultPoly_eq (m : ℕ) :
    c1MultPoly m = 1 + (X ^ (m + 1) - X ^ m) + (X ^ (2 * m + 1) - X ^ (2 * m)) := by
  rw [c1MultPoly]; ring

private lemma coeff_c1MultPoly (m k : ℕ) :
    (c1MultPoly m).coeff k
      = (if k = 0 then (1:ℤ) else 0)
        + ((if k = m + 1 then (1:ℤ) else 0) - (if k = m then (1:ℤ) else 0))
        + ((if k = 2 * m + 1 then (1:ℤ) else 0) - (if k = 2 * m then (1:ℤ) else 0)) := by
  rw [c1MultPoly_eq]
  simp [coeff_add, coeff_sub, coeff_one, coeff_X_pow]

lemma coeff_c1MultPoly_top (m : ℕ) : (c1MultPoly m).coeff (2 * m + 1) ≠ 0 := by
  rw [coeff_c1MultPoly]
  rcases Nat.eq_zero_or_pos m with hm | hm
  · subst hm; norm_num
  · have h1 : 2 * m + 1 ≠ 0 := by omega
    have h2 : 2 * m + 1 ≠ m + 1 := by omega
    have h3 : 2 * m + 1 ≠ m := by omega
    have h5 : 2 * m + 1 ≠ 2 * m := by omega
    have h6 : 2 * m ≠ m := by omega
    simp [h1, h2, h3, h5, h6]

theorem natDegree_c1MultPoly (m : ℕ) : (c1MultPoly m).natDegree = 2 * m + 1 := by
  refine natDegree_eq_of_le_of_coeff_ne_zero ?_ (coeff_c1MultPoly_top m)
  rw [natDegree_le_iff_coeff_eq_zero]
  intro N hN
  rw [coeff_c1MultPoly]
  have h1 : N ≠ 0 := by omega
  have h2 : N ≠ m + 1 := by omega
  have h3 : N ≠ m := by omega
  have h4 : N ≠ 2 * m + 1 := by omega
  have h5 : N ≠ 2 * m := by omega
  simp [h1, h2, h3, h4, h5]

lemma c1MultPoly_ne_zero (m : ℕ) : c1MultPoly m ≠ 0 :=
  fun h => coeff_c1MultPoly_top m (by rw [h]; simp)

noncomputable def c1CoeffPoly : ℕ → Polynomial ℤ
  | 0 => 1
  | (m + 1) => c1CoeffPoly m * c1MultPoly m

lemma c1CoeffPoly_ne_zero (n : ℕ) : c1CoeffPoly n ≠ 0 := by
  induction n with
  | zero => simp [c1CoeffPoly]
  | succ k ih => exact mul_ne_zero ih (c1MultPoly_ne_zero k)

theorem natDegree_c1CoeffPoly (n : ℕ) : (c1CoeffPoly n).natDegree = n ^ 2 := by
  induction n with
  | zero => simp [c1CoeffPoly]
  | succ k ih =>
    rw [c1CoeffPoly, natDegree_mul (c1CoeffPoly_ne_zero k) (c1MultPoly_ne_zero k),
        ih, natDegree_c1MultPoly]
    ring

end QOU.Mass.C1FormalSolutionGrowth
