/-
  THE JOIN: the Kashaev term's own logarithm, asymptotically.

  Two arcs meet here.

  * `qou-mlgp` (A) produced `kashaev_log_sum_asymptotic` — the Euler–Maclaurin
    expansion **with its constant** of the log-sine sum
        `s_k = ∑_{j≤k} log(2 sin(jπ/N))  =  −(N/π)Λ(θ_k) + ½log(2N sin θ_k)
                                            + (π/12N)·cot θ_k + O(1/N²)`
    where `θ_k = kπ/N`.

  * `qou-fybg` steps 1–5 produced the tail bounds, which are all stated
    *relative to* the peak term `g_{k*} = kashaevProd N (5N/6)`.  Nothing in
    them evaluates `g_{k*}` itself; they say only "the sum is `Θ(√N)` copies of
    the peak".

  The bridge is `log_kashaevProd : log g_k = 2 s_k`, so the expansion of `s_k`
  doubles into an expansion of `log g_k`.  That is this file's first theorem,
  and it is the entire content of the join — everything else here is
  bookkeeping: the sum's index set is written `Icc 1 k` on one side and
  `Ico 1 (k+1)` on the other, and the summand's angle is `j·(π/N)` on one side
  and `j·π/N` on the other.

  The second theorem specialises to the saddle.  `k* = ⌊5N/6⌋` does **not**
  give `θ_{k*} = 5π/6` exactly — it misses by `δ ∈ (−π/N, 0]` — so the Taylor
  expansion of `Λ` at the saddle (`abs_Lob_taylor_saddle`) is needed to pay for
  the offset.  It costs `O(1/N)`, not `O(1/N²)`: the `N` in front of `Λ`
  amplifies the quadratic term `√3 δ²/2 ≍ 1/N²` back up to `1/N`.  That is not
  slack in the argument — it is the true size of the correction, and it is why
  the constant `c_σ` is only visible after the `√N` from the Gaussian window is
  divided out.

  -- Ref: [leitner2026] QOU/Knot/KashaevAsymptotic.lean
  -- Ref: [leitner2026] QOU/Knot/LobTaylorSaddle.lean
-/
import QOU.Knot.KashaevAsymptotic
import QOU.Knot.FigureEightVolumeSaddle
import QOU.Knot.LobTaylorSaddle

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- **The join.**  `log(kashaevProd N k)` is twice the log-sine sum, so the
Euler–Maclaurin expansion of the latter doubles into an expansion of the
former — with the same `O(1/N²)` error, doubled.

This is the first statement in the development that expands the Kashaev term
itself rather than a ratio of Kashaev terms. -/
theorem log_kashaevProd_asymptotic {N k : ℕ} (hk : 1 ≤ k) (hkN : k < N)
    (hN : 4 ≤ N) :
    |Real.log (kashaevProd N k)
        - (-(2 * (N : ℝ) / π) * Lob ((k : ℝ) * π / N)
           + Real.log (2 * N * Real.sin ((k : ℝ) * π / N))
           + (π / (6 * N)) * (Real.cos ((k : ℝ) * π / N)
                              / Real.sin ((k : ℝ) * π / N)))|
      ≤ 2 * (1 / (144 * (k : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
             + (π / N) ^ 2 / (12 * Real.sin ((k : ℝ) * π / N) ^ 2)) := by
  -- the two index sets agree
  have hIcc : Finset.Icc 1 k = Finset.Ico 1 (k + 1) := by
    ext j; simp only [Finset.mem_Icc, Finset.mem_Ico]; omega
  -- and so do the two ways of writing the angle
  have hsum : ∑ j ∈ Finset.Icc 1 k, Real.log (2 * Real.sin ((j : ℝ) * (π / N)))
      = ∑ j ∈ Finset.Ico 1 (k + 1),
          Real.log (2 * Real.sin ((j : ℝ) * π / N)) := by
    rw [hIcc]
    exact Finset.sum_congr rfl fun j _ => by rw [mul_div_assoc]
  have hbase := kashaev_log_sum_asymptotic hk hkN hN
  rw [log_kashaevProd hkN, hsum]
  set S := ∑ j ∈ Finset.Ico 1 (k + 1), Real.log (2 * Real.sin ((j : ℝ) * π / N))
    with hSdef
  set L := Lob ((k : ℝ) * π / N) with hLdef
  set G := Real.log (2 * N * Real.sin ((k : ℝ) * π / N)) with hGdef
  set C := Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N) with hCdef
  have hkey : (2 : ℝ) * S - (-(2 * (N : ℝ) / π) * L + G + (π / (6 * N)) * C)
      = 2 * (S - (-((N : ℝ) / π) * L + G / 2 + (π / (12 * N)) * C)) := by
    field_simp
    ring
  rw [hkey, abs_mul, abs_two]
  linarith

/-- **At the saddle.**  For `k` within one step of `5N/6` — which `⌊5N/6⌋` is —
the expansion above can be re-centred on the exact saddle angle `5π/6`, paying
`O(1/N)` for the offset.

The hypothesis is stated as a bound on `|θ_k − 5π/6|` rather than as
`k = ⌊5N/6⌋`, because that is what the proof uses and because both `⌊5N/6⌋`
and `⌈5N/6⌉` satisfy it. -/
theorem log_kashaevProd_saddle {N k : ℕ} (hk : 1 ≤ k) (hkN : k < N) (hN : 4 ≤ N)
    {M : ℝ} (hM : ∀ t ∈ Set.uIcc (5 * π / 6) ((k : ℝ) * π / N),
        1 / Real.sin t ^ 2 ≤ M)
    (hoff : |(k : ℝ) * π / N - 5 * π / 6| ≤ π / N) :
    |Real.log (kashaevProd N k)
        - (-(2 * (N : ℝ) / π) * Lob (5 * π / 6)
           + Real.log (2 * N * Real.sin ((k : ℝ) * π / N))
           + (π / (6 * N)) * (Real.cos ((k : ℝ) * π / N)
                              / Real.sin ((k : ℝ) * π / N)))|
      ≤ 2 * (1 / (144 * (k : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
             + (π / N) ^ 2 / (12 * Real.sin ((k : ℝ) * π / N) ^ 2))
        + (2 * (N : ℝ) / π) * (Real.sqrt 3 * (π / N) ^ 2 / 2
                               + M * (π / N) ^ 3 / 6) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hbase := log_kashaevProd_asymptotic hk hkN hN
  -- `θ_k ∈ (0, π)` because `1 ≤ k < N`; so is `5π/6`; so is everything between
  have hk1 : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hkNr : (k : ℝ) < N := by exact_mod_cast hkN
  have hθ0 : 0 < (k : ℝ) * π / N := by positivity
  have hθπ : (k : ℝ) * π / N < π := by
    rw [div_lt_iff₀ hNpos]
    nlinarith
  have hmem : ∀ x ∈ Set.uIcc (5 * π / 6) ((k : ℝ) * π / N), 0 < x ∧ x < π := by
    intro x hx
    rw [Set.mem_uIcc] at hx
    rcases hx with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> constructor <;> linarith
  -- Taylor at the saddle, with the linear term absent (`Λ'(5π/6) = 0`)
  have htay := abs_Lob_taylor_saddle (θ := (k : ℝ) * π / N) (M := M) hmem hM
  set θ := (k : ℝ) * π / N with hθdef
  set d := θ - 5 * π / 6 with hddef
  -- the offset is at most one step
  have hd : |d| ≤ π / N := hoff
  have hdsq : d ^ 2 ≤ (π / N) ^ 2 := by
    have := abs_nonneg d
    nlinarith [sq_abs d, div_pos hpi hNpos]
  have hdcube : |d| ^ 3 ≤ (π / N) ^ 3 := by
    have h0 : (0 : ℝ) ≤ |d| := abs_nonneg d
    gcongr
  -- so re-centring `Λ` costs at most `√3(π/N)²/2 + M(π/N)³/6`
  -- `M` dominates `1/sin²` at the saddle itself, where that is `4`
  have hMnn : 0 ≤ M := by
    have h5 : (5 : ℝ) * π / 6 ∈ Set.uIcc (5 * π / 6) θ := Set.left_mem_uIcc
    have h := hM _ h5
    rw [sin_five_pi_div_six] at h
    norm_num at h
    linarith
  have hs3 : (0 : ℝ) ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  have hLob : |Lob θ - Lob (5 * π / 6)|
      ≤ Real.sqrt 3 * (π / N) ^ 2 / 2 + M * (π / N) ^ 3 / 6 := by
    have h1 : |Lob θ - (Lob (5 * π / 6) + Real.sqrt 3 * (d ^ 2 / 2))|
        ≤ M * |d| ^ 3 / 6 := htay
    have h2 : |Real.sqrt 3 * (d ^ 2 / 2)| ≤ Real.sqrt 3 * (π / N) ^ 2 / 2 := by
      rw [abs_of_nonneg (by positivity)]
      nlinarith
    have h3 : M * |d| ^ 3 / 6 ≤ M * (π / N) ^ 3 / 6 := by nlinarith
    calc |Lob θ - Lob (5 * π / 6)|
        = |(Lob θ - (Lob (5 * π / 6) + Real.sqrt 3 * (d ^ 2 / 2)))
            + Real.sqrt 3 * (d ^ 2 / 2)| := by congr 1; ring
      _ ≤ |Lob θ - (Lob (5 * π / 6) + Real.sqrt 3 * (d ^ 2 / 2))|
            + |Real.sqrt 3 * (d ^ 2 / 2)| := abs_add_le _ _
      _ ≤ M * (π / N) ^ 3 / 6 + Real.sqrt 3 * (π / N) ^ 2 / 2 := by linarith
      _ = Real.sqrt 3 * (π / N) ^ 2 / 2 + M * (π / N) ^ 3 / 6 := by ring
  -- and the `Λ` term carries the prefactor `2N/π`
  set G := Real.log (2 * N * Real.sin θ) with hGdef
  set C := Real.cos θ / Real.sin θ with hCdef
  set E := 2 * (1 / (144 * (k : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
             + (π / N) ^ 2 / (12 * Real.sin θ ^ 2)) with hEdef
  have hsplit : Real.log (kashaevProd N k)
        - (-(2 * (N : ℝ) / π) * Lob (5 * π / 6) + G + (π / (6 * N)) * C)
      = (Real.log (kashaevProd N k)
          - (-(2 * (N : ℝ) / π) * Lob θ + G + (π / (6 * N)) * C))
        + (2 * (N : ℝ) / π) * (Lob (5 * π / 6) - Lob θ) := by
    ring
  rw [hsplit]
  refine le_trans (abs_add_le _ _) ?_
  have hpre : |(2 * (N : ℝ) / π) * (Lob (5 * π / 6) - Lob θ)|
      ≤ (2 * (N : ℝ) / π) * (Real.sqrt 3 * (π / N) ^ 2 / 2
                             + M * (π / N) ^ 3 / 6) := by
    rw [abs_mul, abs_of_pos (by positivity : (0 : ℝ) < 2 * (N : ℝ) / π),
      abs_sub_comm]
    exact mul_le_mul_of_nonneg_left hLob (by positivity)
  linarith

end QOU.Knot.FigureEightVolume
