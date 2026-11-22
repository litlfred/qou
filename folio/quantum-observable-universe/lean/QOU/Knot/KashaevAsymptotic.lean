/-
  THE ASSEMBLY — bean `qou-mlgp` (A), closed.

  WHAT THIS PROVES.  For `1 ≤ k < N`, `4 ≤ N`, with `h = π/N` and `θ = kπ/N`,

      | ∑_{j=1}^{k} log(2 sin(jπ/N))
          − ( −(N/π)·Λ(θ) + ½·log(2N sin θ) + (π/12N)·cot θ ) |
        ≤  1/(144k²) + (7/12)·h² + h²/(12 sin²θ)

  equivalently, for `s_k = −∑_{j≤k} log(2 sin(jπ/N))`,

      s_k = (N/π)·Λ(θ) − ½·log(2N sin θ) − (π/12N)·cot θ + O(1/N²)

  with an EXPLICIT constant.  This is the statement gap (A) named: the
  `O(log N) → O(1)` sharpening of `abs_deviation_le`, and then some — the
  error here is `O(1/N²)`, four orders better than what the corpus had, and
  the `−½log(2N sin θ)` constant is now derived rather than fitted.

  THE FIVE PIECES, all proved elsewhere in this corpus, all sorry-free.

    ρ − 1/12k    Robbins' refinement of Stirling, BOTH sides
                 (`MathlibExt/StirlingRobbins.lean`).  The one-sided
                 `1/(12k)` is not enough: it is exactly the size of the term
                 it must cancel against, so the two-sided bracket
                 `1/(12k+1) ≤ ρ ≤ 1/(12k)` is what makes the residue
                 `O(1/k²)`.
    δ/h          Λ near zero WITH ITS CONSTANT (`Knot/LobNearZero.lean`).
                 This is where `−½log(2N sin θ)` comes from.
    logSinc h/2  the `h`-endpoint of the trapezoid (`Knot/LogSincNearZero.lean`).
    (h/12)·g₁(h) the `h`-endpoint of the `B₂` correction (same file).
    E            the composite Euler–Maclaurin remainder, with the
                 OSCILLATION bound `(h³/12)(g₂(a) − g₂(b))` that telescopes
                 for monotone `g₂` (`MathlibExt/CompositeEulerMaclaurin.lean`,
                 `Knot/LogSincNearZero.lean` for `AntitoneOn g₂`).

  WHY THE SINGULARITY IS NOT A PROBLEM.  The sum is never approximated near
  `j = 0`.  `sum_log_two_sin_split` removes the singular part EXACTLY —
  `∑ log(2 sin jh) = k·log 2h + log k! + ∑ logSinc jh` — leaving a bounded,
  smooth summand for Euler–Maclaurin and handing the singular part to
  Stirling.  Nothing is expanded through `log(2 sin) → −∞`.

  NUMERICS.  `computations/probes/kashaev_assembly_bound_probe.py` checks the
  bound over `N ∈ [8, 512]` and five `θ`, the exact five-term decomposition to
  1e-59, and each term against its own bound.  The bound holds with 50×–20000×
  slack; the true residual is `O(1/N³)` (the `O(1/N²)` proved here is not
  sharp, by one order, for parity reasons this proof does not exploit).

  -- Ref: [leitner2026] QOU/Knot/KashaevEndpointSplit.lean
  -- Ref: [leitner2026] QOU/Knot/LogSincNearZero.lean
  -- Ref: [leitner2026] QOU/Knot/LobNearZero.lean
  -- Ref: [leitner2026] QOU/MathlibExt/StirlingRobbins.lean
  -- Ref: [leitner2026] QOU/MathlibExt/CompositeEulerMaclaurin.lean
  -- Ref: [leitner2026] computations/probes/kashaev_assembly_bound_probe.py
-/
import QOU.Knot.LobNearZero
import QOU.MathlibExt.StirlingRobbins

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- **Robbins, centred.**  `log k! − (k log k − k + ½log k + ½log 2π)` sits
within `1/(144k²)` of `1/(12k)`.  Both Robbins inequalities are needed: the
`1/(12k)` is not an error term here, it CANCELS against `(h/12)·(1/θ)`. -/
theorem abs_robbins_centred {k : ℕ} (hk : k ≠ 0) :
    |(Real.log (Nat.factorial k)
        - ((k : ℝ) * Real.log k - k + Real.log k / 2 + Real.log (2 * π) / 2))
      - 1 / (12 * (k : ℝ))| ≤ 1 / (144 * (k : ℝ) ^ 2) := by
  have hkR : (0 : ℝ) < k := by exact_mod_cast Nat.pos_of_ne_zero hk
  have hup := QOU.MathlibExt.log_factorial_le_stirling_robbins hk
  have hlo := QOU.MathlibExt.le_log_factorial_stirling_robbins hk
  rw [abs_le]
  constructor
  · have h1 : (0 : ℝ) < 12 * (k : ℝ) + 1 := by linarith
    have h2 : (0 : ℝ) < 12 * (k : ℝ) := by linarith
    have hdiff : 1 / (12 * (k : ℝ) + 1) - 1 / (12 * (k : ℝ))
        = -(1 / ((12 * (k : ℝ)) * (12 * (k : ℝ) + 1))) := by
      field_simp
      ring
    have hmono : 1 / ((12 * (k : ℝ)) * (12 * (k : ℝ) + 1)) ≤ 1 / (144 * (k : ℝ) ^ 2) := by
      rw [div_le_div_iff₀ (by positivity) (by positivity)]
      nlinarith
    linarith
  · have hnn : (0 : ℝ) ≤ 1 / (144 * (k : ℝ) ^ 2) := by positivity
    linarith

/-- The composite Euler–Maclaurin oscillation bound, simplified: since
`sin h < h` the `h`-end of `g₂ = 1/x² − 1/sin²x` is `≤ 0`, and `1/θ² ≥ 0`, so
the whole oscillation is at most `1/sin²θ`.  Stated over bare reals so the
main proof can apply it without dragging its context into `nlinarith`. -/
private theorem osc_bound_le {h θ S T : ℝ} (hh0 : 0 < h) (hθ0 : 0 < θ)
    (hS : 0 < S) (hT : 0 < T) (hSh : S < h) :
    h ^ 2 / 12 * ((1 / h ^ 2 - 1 / S ^ 2) - (1 / θ ^ 2 - 1 / T ^ 2))
      ≤ h ^ 2 / (12 * T ^ 2) := by
  have hS2 : (0 : ℝ) < S ^ 2 := pow_pos hS 2
  have hh2 : (0 : ℝ) < h ^ 2 := pow_pos hh0 2
  have hθ2 : (0 : ℝ) < θ ^ 2 := pow_pos hθ0 2
  have hT2 : (0 : ℝ) < T ^ 2 := pow_pos hT 2
  have h1 : S ^ 2 ≤ h ^ 2 := by nlinarith
  have h2 : 1 / h ^ 2 ≤ 1 / S ^ 2 := one_div_le_one_div_of_le hS2 h1
  have h3 : (0 : ℝ) ≤ 1 / θ ^ 2 := le_of_lt (by positivity)
  have hkey : (1 / h ^ 2 - 1 / S ^ 2) - (1 / θ ^ 2 - 1 / T ^ 2) ≤ 1 / T ^ 2 := by
    linarith
  calc h ^ 2 / 12 * ((1 / h ^ 2 - 1 / S ^ 2) - (1 / θ ^ 2 - 1 / T ^ 2))
      ≤ h ^ 2 / 12 * (1 / T ^ 2) :=
        mul_le_mul_of_nonneg_left hkey (by linarith)
    _ = h ^ 2 / (12 * T ^ 2) := by rw [mul_one_div, div_div]

/-- **The assembly.**  `∑_{j=1}^{k} log(2 sin(jπ/N))` equals
`−(N/π)Λ(θ) + ½log(2N sin θ) + (π/12N)cot θ` up to `O(1/N²)`, with an explicit
constant.  See the file header for the five pieces. -/
theorem kashaev_log_sum_asymptotic {N k : ℕ} (hk : 1 ≤ k) (hkN : k < N) (hN : 4 ≤ N) :
    |(∑ j ∈ Finset.Ico 1 (k + 1), Real.log (2 * Real.sin ((j : ℝ) * π / N)))
        - (-((N : ℝ) / π) * Lob ((k : ℝ) * π / N)
           + Real.log (2 * N * Real.sin ((k : ℝ) * π / N)) / 2
           + (π / (12 * N)) * (Real.cos ((k : ℝ) * π / N)
                               / Real.sin ((k : ℝ) * π / N)))|
      ≤ 1 / (144 * (k : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
        + (π / N) ^ 2 / (12 * Real.sin ((k : ℝ) * π / N) ^ 2) := by
  -- ## numeric preliminaries
  obtain ⟨m, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, (Nat.succ_pred_eq_of_pos hk).symm⟩
  have hcast : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by push_cast; ring
  simp only [hcast]
  have hmnn : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
  have hN0 : N ≠ 0 := by omega
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hN4 : (4 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
  have hkR : (0 : ℝ) < ((m : ℝ) + 1) := by positivity
  have hpi : (0 : ℝ) < π := Real.pi_pos
  set h : ℝ := π / N with hhdef
  have hh0 : 0 < h := by rw [hhdef]; positivity
  have hh1 : h ≤ 1 := by
    rw [hhdef, div_le_one hNR]
    linarith [Real.pi_le_four]
  set θ : ℝ := ((m : ℝ) + 1) * π / N with hθdef
  have hθh : θ = ((m : ℝ) + 1) * h := by rw [hθdef, hhdef]; ring
  have hθ0 : 0 < θ := by rw [hθh]; positivity
  have hθpi : θ < π := by
    rw [hθdef, div_lt_iff₀ hNR]
    have : ((m : ℝ) + 1) < (N : ℝ) := by exact_mod_cast hkN
    nlinarith
  have hsinθ : 0 < Real.sin θ := Real.sin_pos_of_pos_of_lt_pi hθ0 hθpi
  have hsinh : 0 < Real.sin h :=
    Real.sin_pos_of_pos_of_lt_pi hh0 (lt_of_le_of_lt hh1 (by linarith [Real.two_le_pi]))
  -- ## the three remainders, as definitions
  set ρ : ℝ := Real.log (Nat.factorial (m + 1))
      - (((m : ℝ) + 1) * Real.log ((m : ℝ) + 1) - ((m : ℝ) + 1)
         + Real.log ((m : ℝ) + 1) / 2 + Real.log (2 * π) / 2) with hρdef
  set δ : ℝ := Lob h - (h - h * Real.log (2 * h)) with hδdef
  set E : ℝ := (∑ i ∈ Finset.range (m + 1), logSinc (h + (i : ℝ) * h))
      - ((1 / h) * (∫ x in h..θ, logSinc x) + (logSinc h + logSinc θ) / 2
         + (h / 12) * ((Real.cos θ / Real.sin θ - 1 / θ)
                       - (Real.cos h / Real.sin h - 1 / h))) with hEdef
  -- make the abbreviations OPAQUE: `E`'s body carries an integral and a sum,
  -- and leaving it as a `let` sends `positivity`/`linarith` into `whnf` on it.
  clear_value E δ ρ θ h
  -- ## the exact identity
  have hreindex : (∑ j ∈ Finset.Ico 1 ((m + 1) + 1), logSinc ((j : ℝ) * π / N))
      = ∑ i ∈ Finset.range (m + 1), logSinc (h + (i : ℝ) * h) := by
    rw [Finset.sum_Ico_eq_sum_range]
    have hlen : (m + 1) + 1 - 1 = m + 1 := by omega
    rw [hlen]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    congr 1
    push_cast
    rw [hhdef]
    ring
  have hsplit := sum_log_two_sin_split (N := N) (k := m + 1) hN0 hkN
  simp only [hcast] at hsplit
  have hhθ : h ≤ θ := by rw [hθh]; nlinarith
  have hEMint : (∫ x in h..θ, logSinc x)
      = (Lob h - Lob θ)
        - (θ * Real.log (2 * θ) - θ - (h * Real.log (2 * h) - h)) :=
    integral_logSinc_eq hh0 hθpi hhθ
  -- the log identities that make everything an atom
  have hlogθ : Real.log θ = Real.log ((m : ℝ) + 1) + Real.log h := by
    rw [hθh, Real.log_mul (ne_of_gt hkR) (ne_of_gt hh0)]
  have hlog2θ : Real.log (2 * θ) = Real.log 2 + Real.log ((m : ℝ) + 1) + Real.log h := by
    rw [Real.log_mul two_ne_zero (ne_of_gt hθ0), hlogθ]; ring
  have hlog2h : Real.log (2 * h) = Real.log 2 + Real.log h :=
    Real.log_mul two_ne_zero (ne_of_gt hh0)
  have hlogh : Real.log h = Real.log π - Real.log N := by
    rw [hhdef, Real.log_div (ne_of_gt hpi) (ne_of_gt hNR)]
  have hlog2piN : Real.log (2 * π / N) = Real.log 2 + Real.log π - Real.log N := by
    rw [Real.log_div (by positivity) (ne_of_gt hNR),
      Real.log_mul two_ne_zero (ne_of_gt hpi)]
  have hlog2pi : Real.log (2 * π) = Real.log 2 + Real.log π :=
    Real.log_mul two_ne_zero (ne_of_gt hpi)
  have hlog2Nsin : Real.log (2 * N * Real.sin θ)
      = Real.log 2 + Real.log N + Real.log (Real.sin θ) := by
    rw [Real.log_mul (by positivity) (ne_of_gt hsinθ),
      Real.log_mul two_ne_zero (ne_of_gt hNR)]
  have hlogSincθ : logSinc θ = Real.log (Real.sin θ) - Real.log θ := rfl
  -- assemble
  have hident :
      (∑ j ∈ Finset.Ico 1 ((m + 1) + 1), Real.log (2 * Real.sin ((j : ℝ) * π / N)))
        - (-((N : ℝ) / π) * Lob θ + Real.log (2 * N * Real.sin θ) / 2
           + (π / (12 * N)) * (Real.cos θ / Real.sin θ))
      = (ρ - 1 / (12 * ((m : ℝ) + 1))) + δ / h + logSinc h / 2
        - (h / 12) * (Real.cos h / Real.sin h - 1 / h) + E := by
    have hE' : (∑ i ∈ Finset.range (m + 1), logSinc (h + (i : ℝ) * h))
        = (1 / h) * (∫ x in h..θ, logSinc x) + (logSinc h + logSinc θ) / 2
          + (h / 12) * ((Real.cos θ / Real.sin θ - 1 / θ)
                        - (Real.cos h / Real.sin h - 1 / h)) + E := by
      rw [hEdef]; ring
    have hρ' : Real.log (Nat.factorial (m + 1))
        = ((m : ℝ) + 1) * Real.log ((m : ℝ) + 1) - ((m : ℝ) + 1)
          + Real.log ((m : ℝ) + 1) / 2 + Real.log (2 * π) / 2 + ρ := by
      rw [hρdef]; ring
    have hδ' : Lob h = h - h * Real.log (2 * h) + δ := by rw [hδdef]; ring
    rw [hsplit, hreindex, hE', hEMint, hδ', hlogSincθ, hρ', hlog2θ, hlog2h,
      hlogθ, hlog2piN, hlog2pi, hlog2Nsin, hlogh, hθh]
    have hNpi : (N : ℝ) / π = 1 / h := by rw [hhdef]; field_simp
    have hpi12 : π / (12 * (N : ℝ)) = h / 12 := by rw [hhdef]; ring
    rw [hNpi, hpi12]
    have hkne : ((m : ℝ) + 1) ≠ 0 := ne_of_gt hkR
    have hhne : h ≠ 0 := ne_of_gt hh0
    have hsne : Real.sin (((m : ℝ) + 1) * h) ≠ 0 := by rw [← hθh]; exact ne_of_gt hsinθ
    have hsnh : Real.sin h ≠ 0 := ne_of_gt hsinh
    have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNR
    have hpine : π ≠ 0 := ne_of_gt hpi
    field_simp
    ring
  rw [hident]
  -- ## the five bounds
  have hb1 : |ρ - 1 / (12 * ((m : ℝ) + 1))| ≤ 1 / (144 * ((m : ℝ) + 1) ^ 2) := by
    have hr := abs_robbins_centred (k := m + 1) (Nat.succ_ne_zero m)
    simp only [hcast] at hr
    rw [hρdef]
    exact hr
  have hb2 : |δ / h| ≤ h ^ 2 / 3 := by
    have hδb := abs_Lob_sub_near_zero hh0 hh1
    rw [← hδdef] at hδb
    rw [abs_div, abs_of_pos hh0, div_le_iff₀ hh0]
    calc |δ| ≤ h ^ 3 / 3 := hδb
      _ = h ^ 2 / 3 * h := by ring
  have hb3 : |logSinc h / 2| ≤ h ^ 2 / 6 := by
    have := abs_logSinc_le hh0 hh1
    rw [abs_div, abs_of_pos (by norm_num : (0:ℝ) < 2)]
    rw [div_le_iff₀ (by norm_num : (0:ℝ) < 2)]
    linarith
  have hb4 : |(h / 12) * (Real.cos h / Real.sin h - 1 / h)| ≤ h ^ 2 / 12 := by
    have hd := abs_logSinc_deriv_le hh0 hh1
    rw [abs_mul, abs_of_pos (by positivity : (0:ℝ) < h / 12)]
    calc h / 12 * |Real.cos h / Real.sin h - 1 / h| ≤ h / 12 * h :=
          mul_le_mul_of_nonneg_left hd (by positivity)
      _ = h ^ 2 / 12 := by ring
  have hb5 : |E| ≤ h ^ 2 / (12 * Real.sin θ ^ 2) := by
    have hθsum : h + (m : ℝ) * h = θ := by rw [hθh]; ring
    have hEM := abs_sum_logSinc_sub_euler_maclaurin hh0 m (by rw [hθsum]; exact hθpi)
    rw [hθsum] at hEM
    rw [hEdef]
    exact le_trans hEM (osc_bound_le hh0 hθ0 hsinh hsinθ (Real.sin_lt hh0))
  -- ## combine
  have hrw : (π / (N : ℝ)) ^ 2 = h ^ 2 := by rw [hhdef]
  have hrw2 : (π / (N : ℝ)) ^ 2 / (12 * Real.sin θ ^ 2)
      = h ^ 2 / (12 * Real.sin θ ^ 2) := by rw [hhdef]
  rw [abs_le] at hb1 hb2 hb3 hb4 hb5 ⊢
  try clear hident
  try clear hsplit
  try clear hreindex
  try clear hEMint
  try clear hEdef
  try clear hρdef
  try clear hδdef
  try clear hhdef
  try clear hθdef
  constructor
  · linarith [hb1.1, hb2.1, hb3.1, hb4.1, hb5.1, hrw, hrw2]
  · linarith [hb1.2, hb2.2, hb3.2, hb4.2, hb5.2, hrw, hrw2]

end QOU.Knot.FigureEightVolume
