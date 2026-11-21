/-
  `log ⟨4₁⟩_N`, ABSOLUTELY — the sandwich stops being relative to the peak.

  Everything in `KashaevTailBound` bounds `⟨4₁⟩_N` as a multiple of the peak
  term `g_{k*}`, and `KashaevPeakValue` evaluates `log g_{k*}`.  This file adds
  the two steps that turn that pair into a statement about `log ⟨4₁⟩_N` alone:

  1. **Take logs of the sandwich.**  Pure monotonicity — the only content is
     that both sides are positive, which `sq_le_kashaevProd_argmax` supplies
     for the peak and `kashaev_pos` for the invariant.

  2. **Make the peak value concrete at `k*`.**  `log_kashaevProd_saddle` is
     stated for any `k` within `π/N` of the saddle and any `M` dominating
     `1/sin²` in between.  At `k* = ⌊5N/6⌋` both are explicit: the offset is
     `rπ/(6N)` where `r = 5N mod 6 ≤ 5`, and `M = 4` because
     `half_le_sin` gives `sin ≥ ½` on the whole of `[π/6, 5π/6]`.

  Note which direction the offset goes.  `⌊5N/6⌋ ≤ 5N/6`, so `θ_{k*} ≤ 5π/6`
  always — the saddle index approaches the saddle angle from BELOW, never from
  above.  That is what puts the whole interval inside `[π/6, 5π/6]` and lets
  `half_le_sin` apply unchanged.

  -- Ref: [leitner2026] QOU/Knot/KashaevPeakValue.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevTailBound.lean
-/
import QOU.Knot.KashaevPeakValue
import QOU.Knot.KashaevArgmax
import QOU.Knot.KashaevTailBound

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- The peak term is positive — it is at least `N²`. -/
theorem kashaevProd_argmax_pos {N : ℕ} (hN : 6 ≤ N) :
    0 < kashaevProd N (5 * N / 6) := by
  have h := sq_le_kashaevProd_argmax hN
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  nlinarith

/-! ## The saddle index, concretely

`k* = ⌊5N/6⌋` sits at angle `θ_{k*} = k*π/N = 5π/6 − rπ/(6N)` with
`r = 5N mod 6 ∈ [0, 5]`.  Three facts follow, and all three are what
`log_kashaevProd_saddle` asks for. -/

/-- `θ_{k*} = 5π/6 − rπ/(6N)`: the saddle index undershoots the saddle angle by
exactly the remainder's share of one step. -/
theorem argmax_angle_eq {N : ℕ} (hN : 1 ≤ N) :
    ((5 * N / 6 : ℕ) : ℝ) * π / N
      = 5 * π / 6 - ((5 * N % 6 : ℕ) : ℝ) * π / (6 * N) := by
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hq : (6 : ℝ) * ((5 * N / 6 : ℕ) : ℝ) + ((5 * N % 6 : ℕ) : ℝ)
      = 5 * (N : ℝ) := by
    have h := Nat.div_add_mod (5 * N) 6
    exact_mod_cast congrArg (fun n : ℕ => (n : ℝ)) h
  have hqval : ((5 * N / 6 : ℕ) : ℝ)
      = (5 * (N : ℝ) - ((5 * N % 6 : ℕ) : ℝ)) / 6 := by linarith
  rw [hqval]
  field_simp

/-- The offset is at most one step, as `log_kashaevProd_saddle` requires. -/
theorem argmax_offset_le {N : ℕ} (hN : 1 ≤ N) :
    |((5 * N / 6 : ℕ) : ℝ) * π / N - 5 * π / 6| ≤ π / N := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hr : ((5 * N % 6 : ℕ) : ℝ) ≤ 5 := by
    have h : 5 * N % 6 ≤ 5 := by omega
    exact_mod_cast h
  have hr0 : (0 : ℝ) ≤ ((5 * N % 6 : ℕ) : ℝ) := Nat.cast_nonneg _
  rw [argmax_angle_eq hN, show 5 * π / 6 - ((5 * N % 6 : ℕ) : ℝ) * π / (6 * N)
      - 5 * π / 6 = -(((5 * N % 6 : ℕ) : ℝ) * π / (6 * N)) by ring,
    abs_neg, abs_of_nonneg (by positivity)]
  rw [div_le_div_iff₀ (by positivity) hNpos]
  nlinarith [mul_nonneg (mul_nonneg hpi.le hNpos.le)
    (by linarith : (0 : ℝ) ≤ 6 - ((5 * N % 6 : ℕ) : ℝ))]

/-- `θ_{k*} ∈ [π/6, 5π/6]`, so `half_le_sin` applies to the whole interval
between it and the saddle — and hence `M = 4` works. -/
theorem argmax_angle_mem {N : ℕ} (hN : 6 ≤ N) :
    π / 6 ≤ ((5 * N / 6 : ℕ) : ℝ) * π / N
      ∧ ((5 * N / 6 : ℕ) : ℝ) * π / N ≤ 5 * π / 6 := by
  have hpi := Real.pi_pos
  have hN6 : (6 : ℝ) ≤ N := by exact_mod_cast hN
  have hNpos : (0 : ℝ) < N := by linarith
  have hr : ((5 * N % 6 : ℕ) : ℝ) ≤ 5 := by
    have h : 5 * N % 6 ≤ 5 := by omega
    exact_mod_cast h
  have hr0 : (0 : ℝ) ≤ ((5 * N % 6 : ℕ) : ℝ) := Nat.cast_nonneg _
  rw [argmax_angle_eq (by omega : 1 ≤ N)]
  constructor
  · -- `rπ/(6N) ≤ 5π/36 ≤ 5π/6 − π/6`
    have hstep : ((5 * N % 6 : ℕ) : ℝ) * π / (6 * N) ≤ 5 * π / 36 := by
      rw [div_le_div_iff₀ (by positivity) (by norm_num)]
      nlinarith
    linarith
  · have : (0 : ℝ) ≤ ((5 * N % 6 : ℕ) : ℝ) * π / (6 * N) := by positivity
    linarith

/-- **The peak value, with every constant explicit.**  `log_kashaevProd_saddle`
instantiated at `k = ⌊5N/6⌋` and `M = 4`.

`M = 4` is not an estimate: `1/sin²` is exactly `4` at the saddle and smaller
everywhere else on `[π/6, 5π/6]`, so it is the sharp constant for this
interval. -/
theorem log_kashaevProd_argmax {N : ℕ} (hN : 6 ≤ N) :
    |Real.log (kashaevProd N (5 * N / 6))
        - (-(2 * (N : ℝ) / π) * Lob (5 * π / 6)
           + Real.log (2 * N * Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N))
           + (π / (6 * N)) * (Real.cos (((5 * N / 6 : ℕ) : ℝ) * π / N)
                              / Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N)))|
      ≤ 2 * (1 / (144 * ((5 * N / 6 : ℕ) : ℝ) ^ 2) + 7 / 12 * (π / N) ^ 2
             + (π / N) ^ 2
               / (12 * Real.sin (((5 * N / 6 : ℕ) : ℝ) * π / N) ^ 2))
        + (2 * (N : ℝ) / π) * (Real.sqrt 3 * (π / N) ^ 2 / 2
                               + 4 * (π / N) ^ 3 / 6) := by
  obtain ⟨hlo, hhi⟩ := argmax_angle_mem hN
  refine log_kashaevProd_saddle (k := 5 * N / 6) (by omega) (by omega) (by omega)
    ?_ (argmax_offset_le (by omega))
  intro t ht
  rw [Set.mem_uIcc] at ht
  have ht2 : π / 6 ≤ t ∧ t ≤ 5 * π / 6 := by
    rcases ht with ⟨ha, hb⟩ | ⟨ha, hb⟩ <;> constructor <;> linarith
  have hst : (1 : ℝ) / 2 ≤ Real.sin t := half_le_sin ht2.1 ht2.2
  have hsq : (0 : ℝ) < Real.sin t ^ 2 := by nlinarith
  rw [div_le_iff₀ hsq]
  nlinarith

/-! ## Taking logs of the sandwich

`kashaev_le_argmax_mul` and `le_kashaev` bracket `⟨4₁⟩_N` between two multiples
of the peak.  Logging turns the multiples into additive constants. -/

/-- The explicit constant from `kashaev_le_argmax_mul`, named so it can be
logged. -/
noncomputable def kashaevUpperConst (N w : ℕ) : ℝ :=
  (w : ℝ) / (N : ℝ) ^ 2
  + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
    / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))
  + (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
  + (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2)

/-- It is at least `4` — the two window terms alone contribute that much. -/
theorem four_le_kashaevUpperConst {N w : ℕ} (hN : 6 ≤ N) (hD : 2 ≤ 5 * N / 6 - w) :
    4 ≤ kashaevUpperConst N w := by
  have hpi := Real.pi_pos
  have hD2 : (2 : ℝ) ≤ ((5 * N / 6 - w : ℕ) : ℝ) := by exact_mod_cast hD
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have h1 : (0 : ℝ) ≤ (w : ℝ) / (N : ℝ) ^ 2 := by positivity
  have h2 : (0 : ℝ) ≤ (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
      / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)) := by
    apply div_nonneg (by positivity)
    have : (0 : ℝ) ≤ ((5 * N / 6 - w : ℕ) : ℝ) - 1 := by linarith
    positivity
  have h3 : (0 : ℝ) ≤ Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2 := by positivity
  have h4 : (0 : ℝ) ≤ Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2 := by positivity
  unfold kashaevUpperConst
  linarith

/-- **`⟨4₁⟩_N` from above, additively.** -/
theorem log_kashaev_le {N w : ℕ} (hN : 6 ≤ N) (hw1 : 6 * w ≤ 5 * N)
    (hw2 : 2 * N + 3 ≤ 3 * w) (hwk : w ≤ 5 * N / 6) (hD : 2 ≤ 5 * N / 6 - w) :
    Real.log (kashaev N)
      ≤ Real.log (kashaevProd N (5 * N / 6)) + Real.log (kashaevUpperConst N w) := by
  have hg := kashaevProd_argmax_pos hN
  have hC : (0 : ℝ) < kashaevUpperConst N w := by
    have := four_le_kashaevUpperConst hN hD
    linarith
  have hK := kashaev_le_argmax_mul hN hw1 hw2 hwk hD
  have hKC : kashaev N ≤ kashaevProd N (5 * N / 6) * kashaevUpperConst N w := by
    unfold kashaevUpperConst
    exact hK
  have h := Real.log_le_log (kashaev_pos N (by omega)) hKC
  rwa [Real.log_mul (ne_of_gt hg) (ne_of_gt hC)] at h

/-- **`⟨4₁⟩_N` from below, additively.**  `log(m·e^{−1}) = log m − 1`. -/
theorem le_log_kashaev {N m : ℕ} (hN : 6 ≤ N) (hm1 : 1 ≤ m) (hm : m ≤ 5 * N / 6)
    (hsq : Real.sqrt 3 * π * (m : ℝ) ^ 2 ≤ N) :
    Real.log (kashaevProd N (5 * N / 6)) + Real.log m - 1
      ≤ Real.log (kashaev N) := by
  have hg := kashaevProd_argmax_pos hN
  have hmr : (1 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm1
  have hle := le_kashaev hN hm hsq
  have hpos : (0 : ℝ) < kashaevProd N (5 * N / 6) * ((m : ℝ) * Real.exp (-1)) := by
    have : (0 : ℝ) < (m : ℝ) * Real.exp (-1) := by positivity
    exact mul_pos hg this
  have h := Real.log_le_log hpos hle
  rw [Real.log_mul (ne_of_gt hg) (by positivity),
    Real.log_mul (by positivity) (Real.exp_ne_zero _), Real.log_exp] at h
  linarith

end QOU.Knot.FigureEightVolume
