/-
  The exact endpoint of the Kashaev product: `kashaevProd N (N-1) = N²`.

  WHAT THIS IS FOR — `qou-mlgp` (A).  `QOU.Knot.abs_deviation_le` bounds the
  Riemann-sum deviation of `∑_{j≤k} log(2 sin(jπ/N))` from the Clausen
  primitive, and `tendsto_master_error` sends that bound to `0`.  It is enough
  for the volume conjecture at LEADING order (`tendsto_log_kashaev_vol`), but
  its error is `O(log N / N)` on `(π/N)·∑`, i.e. `O(log N)` on the sum itself,
  and the one-loop correction

      s_k = (N/π)·Λ(kπ/N) − ½·log(2N·sin(kπ/N)) + O(1/N),
      s_k := −∑_{j=1}^k log(2 sin(jπ/N))

  is ITSELF `O(log N)`.  So the existing estimate cannot see it.

  WHY THAT IS STRUCTURAL AND NOT A LOOSE CONSTANT.  `abs_deviation_le` is built
  from `sum_log_sin_le_integral_Icc` / `integral_le_sum_log_sin_Icc`, a
  RECTANGLE-RULE sandwich: on each cell the monotonicity of `log(2 sin)` bounds
  the sample by the integral.  A rectangle rule has `O(h·Var)` error per cell by
  construction, and no sharpening of its constants reaches `O(h²)`.  Getting
  `O(1/N)` needs the TRAPEZOID/Euler–Maclaurin correction `(f(a)+f(b))/2`, a
  structurally different comparison, together with a separate treatment of the
  `j = 0` endpoint where `log(2 sin) → −∞`.  That endpoint is exactly where both
  the `log N` and the `½` in the correction come from.

  WHAT THIS FILE CONTRIBUTES.  The exact value any such refinement must
  reproduce at the far endpoint.  From `QOU.MathlibExt.prod_two_sin_pi_div`
  (`∏_{j=1}^{N-1} 2 sin(jπ/N) = N`),

      kashaevProd N (N-1) = N²,        equivalently   s_{N-1} = −log N.

  It is exact for every `N ≥ 1` — no asymptotics — so it is a hard constraint
  on the constant in the refined expansion rather than evidence for it.  Put
  the refined expansion at `k = N-1`: `Λ(π) = 0` and `sin(π(N-1)/N) = sin(π/N)`,
  so it must return `−½log(2N sin(π/N)) + O(1/N) = −log N + O(1/N)` — which is
  the identity below, and fixes the additive constant that would otherwise be
  free.

  -- Ref: [manuscript] QOU/MathlibExt/RootsOfUnityProduct.lean
  -- Ref: [manuscript] QOU/Knot/Clausen.lean          (the O(log N) estimate)
  -- Ref: [manuscript] computations/probes/one_loop_c_sigma_tetrahedral_probe.py
-/
import QOU.Knot.FigureEightVolume
import QOU.MathlibExt.RootsOfUnityProduct

namespace QOU.Knot.FigureEightVolume

open Real

/-- Each Kashaev factor is a squared sine: `2 - 2cos(2πj/N) = (2 sin(πj/N))²`. -/
theorem kashaev_factor_eq_sin_sq (N j : ℕ) :
    2 - 2 * Real.cos (2 * π * j / N) = (2 * Real.sin ((j : ℝ) * π / N)) ^ 2 := by
  have h := Real.sin_sq_eq_half_sub ((j : ℝ) * π / N)
  have harg : 2 * ((j : ℝ) * π / N) = 2 * π * j / N := by ring
  rw [harg] at h
  nlinarith [h]

/-- **`kashaevProd N (N-1) = N²`** — exact, for every `N ≠ 0`.

The far endpoint of the Kashaev product in closed form, from
`∏_{j=1}^{N-1} 2 sin(jπ/N) = N`.  Equivalently `s_{N-1} = −log N`. -/
theorem kashaevProd_endpoint {N : ℕ} (hN : N ≠ 0) :
    kashaevProd N (N - 1) = (N : ℝ) ^ 2 := by
  classical
  have hIcc : Finset.Icc 1 (N - 1) = Finset.Ico 1 N := by
    ext j
    simp only [Finset.mem_Icc, Finset.mem_Ico]
    omega
  unfold kashaevProd
  rw [hIcc]
  calc ∏ j ∈ Finset.Ico 1 N, (2 - 2 * Real.cos (2 * π * j / N))
      = ∏ j ∈ Finset.Ico 1 N, (2 * Real.sin ((j : ℝ) * π / N)) ^ 2 :=
        Finset.prod_congr rfl (fun j _ => kashaev_factor_eq_sin_sq N j)
    _ = (∏ j ∈ Finset.Ico 1 N, (2 * Real.sin ((j : ℝ) * π / N))) ^ 2 :=
        Finset.prod_pow _ _ _
    _ = (N : ℝ) ^ 2 := by
        rw [QOU.MathlibExt.prod_two_sin_pi_div N hN]

/-- The same as a statement about `s_k`: `s_{N-1} = −log N`, where
`s_k = −∑_{j=1}^k log(2 sin(jπ/N))`.  This is the value the refined
Euler–Maclaurin expansion must return at `k = N-1`. -/
theorem sum_log_two_sin_endpoint {N : ℕ} (hN : N ≠ 0) :
    ∑ j ∈ Finset.Ico 1 N, Real.log (2 * Real.sin ((j : ℝ) * π / N))
      = Real.log N := by
  classical
  have hpos : ∀ j ∈ Finset.Ico 1 N, (0 : ℝ) < 2 * Real.sin ((j : ℝ) * π / N) := by
    intro j hj
    rw [Finset.mem_Ico] at hj
    have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
    have hjpos : (0 : ℝ) < (j : ℝ) * π / N := by
      have : (0 : ℝ) < (j : ℝ) := by exact_mod_cast hj.1
      positivity
    have hjlt : (j : ℝ) * π / N < π := by
      rw [div_lt_iff₀ hNR]
      have : (j : ℝ) < N := by exact_mod_cast hj.2
      nlinarith [Real.pi_pos]
    have := Real.sin_pos_of_pos_of_lt_pi hjpos hjlt
    linarith
  rw [← Real.log_prod _ _ (fun j hj => ne_of_gt (hpos j hj))]
  rw [QOU.MathlibExt.prod_two_sin_pi_div N hN]

end QOU.Knot.FigureEightVolume
