/-
  The reflection collapses to a TRAPEZOID REMAINDER — bean `qou-mlgp` (A).

  WHAT THIS PROVES.  `QOU.Knot.FigureEightVolume.sum_log_two_sin_reflect` gives
  the exact reflection `s_k + s_{N−1−k} = −log N`.  Substituting the conjectured
  expansion

      s_k = (N/π)·Λ(θ) − ½·log(2N sin θ) + ε_k,       θ = kπ/N,  h = π/N

  every term cancels and what is left is

      ε_k + ε_{N−1−k} = ½[f(θ) + f(θ+h)] − (1/h)·∫_θ^{θ+h} f,   f = log(2 sin)

  the TRAPEZOID REMAINDER on a single cell.  That was measured to 40 digits in
  `computations/probes/kashaev_reflection_probe.py`; `kashaevErr_add_reflect`
  below makes it a theorem.

  WHY IT MATTERS.  A trapezoid remainder is `O(h²·sup|f''|)` — for `f''=−csc²`,
  `O(h² csc²θ)` in the interior.  So the SYMMETRIC half of (A)'s error is one
  order better than the `O(1/N)` being claimed, and the entire difficulty of (A)
  is in the ANTISYMMETRIC half.  This also converts the structural diagnosis in
  `KashaevProdEndpoint.lean` — that the missing ingredient is the trapezoid
  correction `(f(a)+f(b))/2` rather than any sharpening of the rectangle-rule
  constants — from an analogy into a derivation.

  THE THREE INPUTS, all already in this corpus:
    * `sum_log_two_sin_reflect`   the exact reflection            (KashaevProdEndpoint)
    * `Lob_pi_sub`                `Λ(π−t) = −Λ(t)`, proved below from
                                  `Cl_2_neg` + `Cl_2_add_two_pi`
    * `hasDerivAt_Lob`            `Λ' = −log(2 sin)`              (LobachevskyDerivative)
  the last feeding `integral_log_two_sin`, the fundamental theorem of calculus
  step, which is what turns `Λ(θ+h) − Λ(θ)` into `−∫_θ^{θ+h} f`.

  WHAT IS STILL NOT PROVED.  The ANTISYMMETRIC half.  Numerically it is the
  Euler–Maclaurin `B₂` term `ε_k = −(π/12N)·cot θ + O(1/N³)` (7 digits, five `θ`,
  three `N`), but proving it needs the singular `j = 0` endpoint, where
  `log(2 sin) → −∞` and Stirling rather than Euler–Maclaurin supplies the
  `−½log N`.  The reflection cannot reach it: it pairs `k` with `N−1−k` and both
  endpoints sit outside that pairing.

  -- Ref: [leitner2026] QOU/Knot/KashaevProdEndpoint.lean
  -- Ref: [leitner2026] QOU/Archimedean/LobachevskyDerivative.lean
  -- Ref: [leitner2026] computations/probes/kashaev_reflection_probe.py
-/
import QOU.Knot.KashaevProdEndpoint
import QOU.Archimedean.LobachevskyDerivative

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- **`Λ(π − t) = −Λ(t)`.**  From `Λ(t) = Cl₂(2t)/2`, `2π`-periodicity and
oddness of `Cl₂`: `Cl₂(2π − 2t) = Cl₂(−2t) = −Cl₂(2t)`. -/
theorem Lob_pi_sub (t : ℝ) : Lob (π - t) = -Lob t := by
  unfold Lob
  rw [show 2 * (π - t) = -(2 * t) + 2 * π by ring, Cl_2_add_two_pi, Cl_2_neg]
  ring

/-- **`∫_a^b log(2 sin t) dt = Λ(a) − Λ(b)`** for `0 < a ≤ b < π`.

The fundamental theorem of calculus against `hasDerivAt_Lob` (`Λ' = −log(2 sin)`
on `(0, π)`), with the sign flipped out. -/
theorem integral_log_two_sin {a b : ℝ} (ha : 0 < a) (hb : b < π) (hab : a ≤ b) :
    ∫ t in a..b, Real.log (2 * Real.sin t) = Lob a - Lob b := by
  have hmem : ∀ x ∈ Set.uIcc a b, 0 < x ∧ x < π := by
    intro x hx
    rw [Set.uIcc_of_le hab, Set.mem_Icc] at hx
    exact ⟨lt_of_lt_of_le ha hx.1, lt_of_le_of_lt hx.2 hb⟩
  have hderiv : ∀ x ∈ Set.uIcc a b,
      HasDerivAt Lob (-Real.log (2 * Real.sin x)) x := by
    intro x hx
    obtain ⟨h1, h2⟩ := hmem x hx
    exact hasDerivAt_Lob h1 h2
  have hcont : ContinuousOn (fun t : ℝ => -Real.log (2 * Real.sin t))
      (Set.uIcc a b) := by
    intro x hx
    obtain ⟨h1, h2⟩ := hmem x hx
    have hsin : 0 < Real.sin x := Real.sin_pos_of_pos_of_lt_pi h1 h2
    have : ContinuousAt (fun t : ℝ => -Real.log (2 * Real.sin t)) x := by
      refine ContinuousAt.neg (ContinuousAt.log ?_ (by positivity))
      exact (continuous_const.mul Real.continuous_sin).continuousAt
    exact this.continuousWithinAt
  have hkey := intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv
    hcont.intervalIntegrable
  rw [intervalIntegral.integral_neg] at hkey
  linarith

/-- `s_k = −∑_{j=1}^{k} log(2 sin(jπ/N))`. -/
noncomputable def kashaevLogSum (N k : ℕ) : ℝ :=
  -∑ j ∈ Finset.Ico 1 (k + 1), Real.log (2 * Real.sin ((j : ℝ) * π / N))

/-- The conjectured main term `(N/π)Λ(θ) − ½log(2N sin θ)` of `s_k`. -/
noncomputable def kashaevMainTerm (N k : ℕ) : ℝ :=
  ((N : ℝ) / π) * Lob ((k : ℝ) * π / N)
    - Real.log (2 * N * Real.sin ((k : ℝ) * π / N)) / 2

/-- The error `ε_k` in the conjectured expansion of `s_k`. -/
noncomputable def kashaevErr (N k : ℕ) : ℝ :=
  kashaevLogSum N k - kashaevMainTerm N k

/-- **`ε_k + ε_{N−1−k}` is exactly the trapezoid remainder on `[θ, θ+h]`.**

    ε_k + ε_{N−1−k} = ½[f(θ) + f(θ+h)] − (1/h)·∫_θ^{θ+h} f,   f = log(2 sin)

with `θ = kπ/N`, `h = π/N`, so `θ+h = (k+1)π/N` and `1/h = N/π`.  An identity,
for every `N` and every `0 < k` with `k+1 < N` — no asymptotics anywhere.

Hence the symmetric half of `qou-mlgp` (A)'s error is a trapezoid remainder,
`O(h²csc²θ)` in the interior, and all of (A)'s remaining difficulty is
antisymmetric. -/
theorem kashaevErr_add_reflect {N k : ℕ} (hk0 : 0 < k) (hkN : k + 1 < N) :
    kashaevErr N k + kashaevErr N (N - 1 - k)
      = (Real.log (2 * Real.sin ((k : ℝ) * π / N))
          + Real.log (2 * Real.sin (((k : ℝ) + 1) * π / N))) / 2
        - ((N : ℝ) / π) * ∫ t in ((k : ℝ) * π / N)..(((k : ℝ) + 1) * π / N),
            Real.log (2 * Real.sin t) := by
  have hN : N ≠ 0 := by omega
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hpi : (0 : ℝ) < π := Real.pi_pos
  have hkR : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk0
  have hk1R : (k : ℝ) + 1 < (N : ℝ) := by exact_mod_cast hkN
  -- the two angles and their basic position
  have hθ0 : 0 < (k : ℝ) * π / N := by positivity
  have hθ'0 : 0 < ((k : ℝ) + 1) * π / N := by positivity
  have hθ'lt : ((k : ℝ) + 1) * π / N < π := by
    rw [div_lt_iff₀ hNR]
    nlinarith
  have hθlt : (k : ℝ) * π / N < π := by
    rw [div_lt_iff₀ hNR]
    nlinarith
  have hθle : (k : ℝ) * π / N ≤ ((k : ℝ) + 1) * π / N := by
    have hd : (0 : ℝ) < π / N := div_pos hpi hNR
    have hgap : ((k : ℝ) + 1) * π / N - (k : ℝ) * π / N = π / N := by
      field_simp
      ring
    linarith
  have hsin : 0 < Real.sin ((k : ℝ) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi hθ0 hθlt
  have hsin' : 0 < Real.sin (((k : ℝ) + 1) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi hθ'0 hθ'lt
  -- (i) the reflection, on the log-sums
  have hidx : (N - 1 - k) + 1 = N - k := by omega
  have hLogSum : kashaevLogSum N k + kashaevLogSum N (N - 1 - k)
      = -Real.log N := by
    unfold kashaevLogSum
    rw [hidx]
    have := sum_log_two_sin_reflect hN (by omega : k < N)
    linarith
  -- (ii) the reflected angle
  have hcast : ((N - 1 - k : ℕ) : ℝ) = (N : ℝ) - 1 - (k : ℝ) := by
    have h1 : k ≤ N - 1 := by omega
    have h2 : 1 ≤ N := by omega
    rw [Nat.cast_sub h1, Nat.cast_sub h2, Nat.cast_one]
  have hangle : ((N - 1 - k : ℕ) : ℝ) * π / N = π - ((k : ℝ) + 1) * π / N := by
    rw [hcast]
    field_simp
    ring
  have hsinref : Real.sin (((N - 1 - k : ℕ) : ℝ) * π / N)
      = Real.sin (((k : ℝ) + 1) * π / N) := by
    rw [hangle, Real.sin_pi_sub]
  have hlobref : Lob (((N - 1 - k : ℕ) : ℝ) * π / N)
      = -Lob (((k : ℝ) + 1) * π / N) := by
    rw [hangle, Lob_pi_sub]
  -- (iii) the main terms
  have hMain : kashaevMainTerm N k + kashaevMainTerm N (N - 1 - k)
      = ((N : ℝ) / π) * (Lob ((k : ℝ) * π / N) - Lob (((k : ℝ) + 1) * π / N))
        - Real.log (2 * N * Real.sin ((k : ℝ) * π / N)) / 2
        - Real.log (2 * N * Real.sin (((k : ℝ) + 1) * π / N)) / 2 := by
    unfold kashaevMainTerm
    rw [hsinref, hlobref]
    ring
  -- (iv) peel the `log N` out of each `log(2N sin)`
  have hsplit : ∀ s : ℝ, 0 < s →
      Real.log (2 * N * s) = Real.log N + Real.log (2 * s) := by
    intro s hs
    rw [show (2 : ℝ) * N * s = (N : ℝ) * (2 * s) by ring]
    exact Real.log_mul (ne_of_gt hNR) (by positivity)
  rw [hsplit _ hsin, hsplit _ hsin'] at hMain
  -- (v) the fundamental theorem of calculus
  rw [integral_log_two_sin hθ0 hθ'lt hθle]
  -- (vi) assemble
  unfold kashaevErr
  rw [show kashaevLogSum N k - kashaevMainTerm N k
        + (kashaevLogSum N (N - 1 - k) - kashaevMainTerm N (N - 1 - k))
      = (kashaevLogSum N k + kashaevLogSum N (N - 1 - k))
        - (kashaevMainTerm N k + kashaevMainTerm N (N - 1 - k)) by ring]
  rw [hLogSum, hMain]
  ring

end QOU.Knot.FigureEightVolume
