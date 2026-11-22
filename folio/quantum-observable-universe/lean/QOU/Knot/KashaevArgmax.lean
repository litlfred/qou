/-
  THE SADDLE IS AT k = ⌊5N/6⌋ — exactly, discretely, with no asymptotics.
  Bean `qou-fybg` (the successor to `qou-mlgp`).

  WHAT THIS PROVES.  For `6 ≤ N` and every `k < N`,

      kashaevProd N k  ≤  kashaevProd N ⌊5N/6⌋.

  The largest term of Kashaev's sum `⟨4₁⟩_N = ∑_k kashaevProd N k` sits at
  `k* = ⌊5N/6⌋`, i.e. at `θ* = k*π/N ≈ 5π/6` — the angle where `2 sin θ = 1`.

  WHY IT IS WORTH HAVING SEPARATELY.  `OneLoopPrefactorInvariance` takes the
  saddle condition `2 sin θ* = 1` as a hypothesis and derives everything from
  it (`saddle_forces_cot`, `c_pow_four_eq_third`, `k_sq_eq_half_of_saddle`).
  That condition is usually justified by differentiating the Euler–Maclaurin
  leading term — which needs the expansion, its remainder, and uniformity in
  `k`.  None of that is needed to locate the maximum.  The ratio of successive
  terms is

      kashaevProd N (k+1) / kashaevProd N k  =  (2 sin((k+1)π/N))²

  exactly, so the term sequence rises precisely while `2 sin > 1` and falls
  precisely while `2 sin < 1`.  `2 sin θ = 1` is not an asymptotic
  stationarity condition here; it is the exact crossover of a ratio.

  THE SHAPE IS DOWN–UP–DOWN, NOT UNIMODAL.  `2 sin(jπ/N) < 1` also holds near
  `j = 0`, so the sequence *falls* on `[0, ⌊N/6⌋]` before it rises.  The proof
  handles that region separately: there `kashaevProd N k ≤ kashaevProd N 0 = 1`,
  and `1 ≤ kashaevProd N k*` because the sequence falls from `k*` to `N−1`
  where `kashaevProd N (N−1) = N²` exactly (`kashaevProd_endpoint`).  Writing
  "unimodal" here would be wrong.

  WHAT IT DOES NOT DO.  It locates the maximum; it says nothing about its
  VALUE, about the width of the peak, or about the sum.  `hc` and `hτ` need the
  Hessian too — that is the rest of `qou-fybg`.

  -- Ref: [leitner2026] QOU/Knot/KashaevProdEndpoint.lean
  -- Ref: [leitner2026] QOU/Knot/FigureEightVolumeSaddle.lean
  -- Ref: [leitner2026] QOU/OneLoopPrefactorInvariance.lean
-/
import QOU.Knot.KashaevProdEndpoint

namespace QOU.Knot.FigureEightVolume

open Real

/-! ## Part 1 — where `2 sin θ` crosses 1 -/

/-- `sin θ ≥ 1/2` on `[π/6, 5π/6]`. -/
theorem half_le_sin {θ : ℝ} (h1 : π / 6 ≤ θ) (h2 : θ ≤ 5 * π / 6) :
    1 / 2 ≤ Real.sin θ := by
  have hpi := Real.pi_pos
  rcases le_total θ (π / 2) with h | h
  · have hm := Real.sin_le_sin_of_le_of_le_pi_div_two
      (x := π / 6) (y := θ) (by linarith) (by linarith) (by linarith)
    rwa [Real.sin_pi_div_six] at hm
  · rw [← Real.sin_pi_sub]
    have hm := Real.sin_le_sin_of_le_of_le_pi_div_two
      (x := π / 6) (y := π - θ) (by linarith) (by linarith) (by linarith)
    rwa [Real.sin_pi_div_six] at hm

/-- `sin θ ≤ 1/2` on `[0, π/6]`. -/
theorem sin_le_half_of_le {θ : ℝ} (h0 : 0 ≤ θ) (h : θ ≤ π / 6) :
    Real.sin θ ≤ 1 / 2 := by
  have hpi := Real.pi_pos
  have hm := Real.sin_le_sin_of_le_of_le_pi_div_two
    (x := θ) (y := π / 6) (by linarith) (by linarith) h
  rwa [Real.sin_pi_div_six] at hm

/-- `sin θ ≤ 1/2` on `[5π/6, π]`, by reflection. -/
theorem sin_le_half_of_ge {θ : ℝ} (h : 5 * π / 6 ≤ θ) (hpi : θ ≤ π) :
    Real.sin θ ≤ 1 / 2 := by
  rw [← Real.sin_pi_sub]
  exact sin_le_half_of_le (by linarith) (by linarith)

/-! ## Part 2 — the exact ratio of successive terms -/

/-- **`kashaevProd N (k+1) = kashaevProd N k · (2 sin((k+1)π/N))²`.**
The whole argument is this identity plus where `2 sin` crosses `1`. -/
theorem kashaevProd_succ (N k : ℕ) :
    kashaevProd N (k + 1)
      = kashaevProd N k * (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 := by
  have hcast : ((k + 1 : ℕ) : ℝ) = (k : ℝ) + 1 := by push_cast; ring
  unfold kashaevProd
  rw [Finset.prod_Icc_succ_top (by omega) _, kashaev_factor_eq_sin_sq N (k + 1),
    hcast]

/-- Rising step: `N ≤ 6(k+1) ≤ 5N` puts `(k+1)π/N` in `[π/6, 5π/6]`. -/
theorem kashaevProd_le_succ {N k : ℕ} (hN : N ≠ 0)
    (hlo : (N : ℝ) ≤ 6 * ((k : ℝ) + 1)) (hhi : 6 * ((k : ℝ) + 1) ≤ 5 * N) :
    kashaevProd N k ≤ kashaevProd N (k + 1) := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hθ1 : π / 6 ≤ ((k : ℝ) + 1) * π / N := by
    rw [le_div_iff₀ hNR]; nlinarith
  have hθ2 : ((k : ℝ) + 1) * π / N ≤ 5 * π / 6 := by
    rw [div_le_iff₀ hNR]; nlinarith
  have hs := half_le_sin hθ1 hθ2
  have hS : (1 : ℝ) ≤ (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 := by nlinarith
  rw [kashaevProd_succ]
  nlinarith [kashaevProd_nonneg N k]

/-- Falling step, near `j = 0`: `6(k+1) ≤ N` puts `(k+1)π/N` in `(0, π/6]`. -/
theorem kashaevProd_succ_le_of_small {N k : ℕ} (hN : N ≠ 0)
    (h : 6 * ((k : ℝ) + 1) ≤ N) :
    kashaevProd N (k + 1) ≤ kashaevProd N k := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hkR : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
  have hθ0 : 0 ≤ ((k : ℝ) + 1) * π / N := by positivity
  have hθ : ((k : ℝ) + 1) * π / N ≤ π / 6 := by
    rw [div_le_iff₀ hNR]; nlinarith
  have hs := sin_le_half_of_le hθ0 hθ
  have hs0 : 0 ≤ Real.sin (((k : ℝ) + 1) * π / N) := by
    refine Real.sin_nonneg_of_nonneg_of_le_pi hθ0 ?_
    linarith
  have hS : (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 ≤ 1 := by nlinarith
  rw [kashaevProd_succ]
  nlinarith [kashaevProd_nonneg N k]

/-- Falling step, past the saddle: `5N ≤ 6(k+1)` and `k+1 ≤ N` put
`(k+1)π/N` in `[5π/6, π]`. -/
theorem kashaevProd_succ_le_of_large {N k : ℕ} (hN : N ≠ 0)
    (hle : (k : ℝ) + 1 ≤ N) (h : 5 * (N : ℝ) ≤ 6 * ((k : ℝ) + 1)) :
    kashaevProd N (k + 1) ≤ kashaevProd N k := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hkR : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
  have hθ1 : 5 * π / 6 ≤ ((k : ℝ) + 1) * π / N := by
    rw [le_div_iff₀ hNR]; nlinarith
  have hθ2 : ((k : ℝ) + 1) * π / N ≤ π := by
    rw [div_le_iff₀ hNR]; nlinarith
  have hs := sin_le_half_of_ge hθ1 hθ2
  have hs0 : 0 ≤ Real.sin (((k : ℝ) + 1) * π / N) :=
    Real.sin_nonneg_of_nonneg_of_le_pi (by positivity) hθ2
  have hS : (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 ≤ 1 := by nlinarith
  rw [kashaevProd_succ]
  nlinarith [kashaevProd_nonneg N k]

/-! ## Part 3 — chaining the steps -/

/-- Rising run: `kashaevProd N a ≤ kashaevProd N b` when every step between
lands in the rising window. -/
theorem kashaevProd_le_of_rising {N a b : ℕ} (hN : N ≠ 0) (hab : a ≤ b)
    (h : ∀ j : ℕ, a < j → j ≤ b → (N : ℝ) ≤ 6 * (j : ℝ) ∧ 6 * (j : ℝ) ≤ 5 * N) :
    kashaevProd N a ≤ kashaevProd N b := by
  induction b, hab using Nat.le_induction with
  | base => exact le_rfl
  | succ n hn ih =>
      have hstep := h (n + 1) (by omega) le_rfl
      have hcast : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by push_cast; ring
      rw [hcast] at hstep
      exact le_trans (ih (fun j hj1 hj2 => h j hj1 (by omega)))
        (kashaevProd_le_succ hN hstep.1 hstep.2)

/-- Falling run past the saddle. -/
theorem kashaevProd_le_of_falling {N a b : ℕ} (hN : N ≠ 0) (hab : a ≤ b)
    (hbN : b ≤ N) (h : ∀ j : ℕ, a < j → j ≤ b → 5 * (N : ℝ) ≤ 6 * (j : ℝ)) :
    kashaevProd N b ≤ kashaevProd N a := by
  induction b, hab using Nat.le_induction with
  | base => exact le_rfl
  | succ n hn ih =>
      have hstep := h (n + 1) (by omega) le_rfl
      have hcast : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by push_cast; ring
      rw [hcast] at hstep
      have hnN : (n : ℝ) + 1 ≤ (N : ℝ) := by
        rw [← hcast]; exact_mod_cast hbN
      exact le_trans (kashaevProd_succ_le_of_large hN hnN hstep)
        (ih (by omega) (fun j hj1 hj2 => h j hj1 (by omega)))

/-- Falling run near `j = 0`. -/
theorem kashaevProd_le_of_falling_small {N a b : ℕ} (hN : N ≠ 0) (hab : a ≤ b)
    (h : ∀ j : ℕ, a < j → j ≤ b → 6 * (j : ℝ) ≤ N) :
    kashaevProd N b ≤ kashaevProd N a := by
  induction b, hab using Nat.le_induction with
  | base => exact le_rfl
  | succ n hn ih =>
      have hstep := h (n + 1) (by omega) le_rfl
      have hcast : ((n + 1 : ℕ) : ℝ) = (n : ℝ) + 1 := by push_cast; ring
      rw [hcast] at hstep
      exact le_trans (kashaevProd_succ_le_of_small hN hstep)
        (ih (fun j hj1 hj2 => h j hj1 (by omega)))

/-! ## Part 4 — the argmax -/

/-- **`1 ≤ kashaevProd N ⌊5N/6⌋`.**  The sequence falls from `k*` to `N−1`,
where it equals `N²` exactly. -/
theorem one_le_kashaevProd_argmax {N : ℕ} (hN : 6 ≤ N) :
    1 ≤ kashaevProd N (5 * N / 6) := by
  have hN0 : N ≠ 0 := by omega
  have hNR : (1 : ℝ) ≤ (N : ℝ) := by exact_mod_cast (by omega : 1 ≤ N)
  have hks : 5 * N / 6 < N := by
    rw [Nat.div_lt_iff_lt_mul (by norm_num)]; omega
  have hdiv := Nat.div_add_mod (5 * N) 6
  have hmod : 5 * N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  have hfall : kashaevProd N (N - 1) ≤ kashaevProd N (5 * N / 6) := by
    refine kashaevProd_le_of_falling hN0 (by omega) (by omega) (fun j hj1 _ => ?_)
    have hj : 5 * N < 6 * j := by omega
    exact_mod_cast Nat.le_of_lt hj
  rw [kashaevProd_endpoint hN0] at hfall
  nlinarith

/-- **The largest Kashaev term is at `k = ⌊5N/6⌋`** — the discrete saddle.
`θ* = k*π/N` is within `π/N` of the solution of `2 sin θ = 1` in `(π/2, π)`. -/
theorem kashaevProd_le_argmax {N k : ℕ} (hN : 6 ≤ N) (hkN : k < N) :
    kashaevProd N k ≤ kashaevProd N (5 * N / 6) := by
  have hN0 : N ≠ 0 := by omega
  have hdiv5 := Nat.div_add_mod (5 * N) 6
  have hmod5 : 5 * N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  have hdiv1 := Nat.div_add_mod N 6
  have hmod1 : N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  rcases le_or_gt k (N / 6) with hlow | hlow
  · -- falls to at most `kashaevProd N 0 = 1`, which the argmax dominates
    have h1 : kashaevProd N k ≤ kashaevProd N 0 := by
      refine kashaevProd_le_of_falling_small hN0 (Nat.zero_le k) (fun j _ hj2 => ?_)
      have : 6 * j ≤ N := by omega
      exact_mod_cast this
    rw [kashaevProd_zero] at h1
    exact le_trans h1 (one_le_kashaevProd_argmax hN)
  · rcases le_or_gt k (5 * N / 6) with hmid | hhigh
    · -- rising run from `k` up to `k*`
      refine kashaevProd_le_of_rising hN0 hmid (fun j hj1 hj2 => ?_)
      constructor
      · have : N ≤ 6 * j := by omega
        exact_mod_cast this
      · have : 6 * j ≤ 5 * N := by omega
        exact_mod_cast this
    · -- falling run from `k*` down to `k`
      refine kashaevProd_le_of_falling hN0 (le_of_lt hhigh) (by omega)
        (fun j hj1 _ => ?_)
      have : 5 * N ≤ 6 * j := by omega
      exact_mod_cast this

/-- On the rising arc `[π/6, 5π/6]`, the step multiplier `(2 * Real.sin θ)^2` is at least `1`. -/
theorem two_sin_sq_ge_one_on_rising_arc {θ : ℝ}
    (h1 : π / 6 ≤ θ) (h2 : θ ≤ 5 * π / 6) :
    (1 : ℝ) ≤ (2 * Real.sin θ) ^ 2 := by
  have hs := half_le_sin h1 h2
  nlinarith

end QOU.Knot.FigureEightVolume
