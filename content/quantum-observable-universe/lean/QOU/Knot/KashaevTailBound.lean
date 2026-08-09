/-
  GAUSSIAN DECAY AWAY FROM THE SADDLE — bean `qou-fybg`, step 3 (tails).

  `KashaevArgmax` shows the Kashaev terms peak at `k* = ⌊5N/6⌋`.  Laplace's
  method needs more than that: it needs the terms to FALL OFF fast enough that
  everything outside a `√N`-window is negligible.  This file supplies the decay,
  and the whole of it comes from one fact about one function.

  `f(θ) = log(2 sin θ)` is CONCAVE on `(0, π)` — `f″ = −csc² < 0` — and vanishes
  at `θ* = 5π/6` with `f′(θ*) = cot θ* = −√3`.  Concavity therefore puts `f`
  below its tangent at `θ*`:

      TANGENT   f(θ) ≤ −√3 (θ − θ*)                 for every θ ∈ (0, π)

  and that is what makes the RIGHT tail Gaussian: summing `−√3(θ_j − θ*)` over
  `j = k*+1 … k` is an arithmetic progression, so the exponent is QUADRATIC in
  the distance,

      kashaevProd N (k*+d) ≤ kashaevProd N k* · exp(−√3 π d(d−1)/N)

  which is `e^{−c d²/N}` — the Gaussian of width `√N` that the theta-function
  sum in `hasSum_gaussian_theta` is waiting for.

  THE LEFT TAIL NEEDS THE OPPOSITE INEQUALITY.  There the terms are RISING
  towards the saddle, so what is needed is a LOWER bound on `f` — and the
  tangent gives an upper one.  Concavity is the wrong way round.  What works is
  a SECANT: `cot` is antitone, so `cot ≤ cot(2π/3) = −1/√3` on `[2π/3, θ*]`, and
  integrating that back from `θ*` (where `f` vanishes) gives

      SECANT    f(θ) ≥ (θ* − θ)/√3                  for θ ∈ [2π/3, θ*]

  hence `kashaevProd N (b−d) ≤ kashaevProd N b · exp(−π d(d−1)/(√3 N))` for
  `b ≤ 5N/6`.  Same arithmetic progression, run backwards; the constant is
  `1/√3` rather than `√3` because a secant is shallower than the tangent, and
  the bound is confined to `θ ≥ 2π/3` because a secant is only valid on the
  window it was drawn across.  Both tails are proved here (Parts 3 and 4).

  WHY THE NAIVE BOUND IS NOT ENOUGH.  Each ratio `(2 sin θ_{k*+i})²` is `< 1`
  and they decrease, so `∏_{i≤d} ≤ (2 sin θ_{k*+1})^{2d}`.  That is only
  `e^{−c d/N}` — exponential in `d/N`, not `d²/N` — and it does not confine the
  sum to a `√N`-window.  The gain comes from using that the factors keep
  shrinking, i.e. from the linear bound on `f`, not from the first factor alone.

  -- Ref: [manuscript] QOU/Knot/KashaevArgmax.lean
  -- Ref: [manuscript] QOU/Knot/LobTaylorSaddle.lean
  -- Ref: [manuscript] QOU/MathlibExt/GaussianThetaSum.lean
-/
import QOU.Knot.KashaevArgmax
import QOU.Knot.LobTaylorSaddle
import QOU.MathlibExt.TrapezoidRule
import Mathlib.Analysis.Calculus.MeanValue

namespace QOU.Knot.FigureEightVolume

open Real

/-! ## Part 1 — `cot` is antitone on `(0, π)` -/

/-- `cot` is antitone on any `[c,d] ⊂ (0, π)`: its derivative is `−csc² < 0`. -/
theorem cot_antitoneOn {c d : ℝ} (hc : 0 < c) (hd : d < π) :
    AntitoneOn (fun θ => Real.cos θ / Real.sin θ) (Set.Icc c d) := by
  have hmem : ∀ x ∈ Set.Icc c d, 0 < x ∧ x < π := by
    intro x hx
    rw [Set.mem_Icc] at hx
    exact ⟨lt_of_lt_of_le hc hx.1, lt_of_le_of_lt hx.2 hd⟩
  refine antitoneOn_of_deriv_nonpos (convex_Icc c d) ?_ ?_ ?_
  · intro x hx
    obtain ⟨h0, hpi⟩ := hmem x hx
    exact ((QOU.MathlibExt.hasDerivAt_cos_div_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hpi))).continuousAt).continuousWithinAt
  · intro x hx
    rw [interior_Icc, Set.mem_Ioo] at hx
    obtain ⟨h0, hpi⟩ := hmem x (Set.mem_Icc.mpr ⟨le_of_lt hx.1, le_of_lt hx.2⟩)
    exact (QOU.MathlibExt.hasDerivAt_cos_div_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hpi))).differentiableAt.differentiableWithinAt
  · intro x hx
    rw [interior_Icc, Set.mem_Ioo] at hx
    obtain ⟨h0, hpi⟩ := hmem x (Set.mem_Icc.mpr ⟨le_of_lt hx.1, le_of_lt hx.2⟩)
    have hs : Real.sin x ≠ 0 := ne_of_gt (Real.sin_pos_of_pos_of_lt_pi h0 hpi)
    rw [(QOU.MathlibExt.hasDerivAt_cos_div_sin hs).deriv]
    have : (0 : ℝ) < Real.sin x ^ 2 := pow_pos (Real.sin_pos_of_pos_of_lt_pi h0 hpi) 2
    have : (0 : ℝ) < 1 / Real.sin x ^ 2 := by positivity
    linarith

/-! ## Part 2 — the tangent and secant bounds at `θ* = 5π/6` -/

/-- **Tangent bound (concavity).**  `log(2 sin θ) ≤ −√3 (θ − 5π/6)` on `(0, π)`.
Equality exactly at `θ*`; this is the whole source of the right tail's
Gaussian decay. -/
theorem log_two_sin_le_tangent {θ : ℝ} (h0 : 0 < θ) (hπ : θ < π) :
    Real.log (2 * Real.sin θ) ≤ -Real.sqrt 3 * (θ - 5 * π / 6) := by
  have hpi := Real.pi_pos
  have hs3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs3nn : (0 : ℝ) ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  have hcotstar : Real.cos (5 * π / 6) / Real.sin (5 * π / 6) = -Real.sqrt 3 :=
    cot_five_pi_div_six
  have hstar0 : (0 : ℝ) < 5 * π / 6 := by linarith
  have hstarpi : (5 : ℝ) * π / 6 < π := by linarith
  -- `u θ = log(2 sin θ) + √3 (θ − θ*)`, with `u θ* = 0` and `u′ = cot θ + √3`
  have hu : ∀ x, 0 < x → x < π →
      HasDerivAt (fun y => Real.log (2 * Real.sin y) + Real.sqrt 3 * (y - 5 * π / 6))
        (Real.cos x / Real.sin x + Real.sqrt 3) x := by
    intro x hx0 hxpi
    have h1 := QOU.MathlibExt.hasDerivAt_log_two_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi hx0 hxpi))
    have h2 : HasDerivAt (fun y : ℝ => Real.sqrt 3 * (y - 5 * π / 6)) (Real.sqrt 3) x := by
      simpa using ((hasDerivAt_id x).sub_const (5 * π / 6)).const_mul (Real.sqrt 3)
    exact h1.add h2
  have hustar : Real.log (2 * Real.sin (5 * π / 6))
      + Real.sqrt 3 * (5 * π / 6 - 5 * π / 6) = 0 := by
    rw [sin_five_pi_div_six]; norm_num
  rcases le_total θ (5 * π / 6) with hle | hle
  · -- rising up to `θ*`
    have hmono : MonotoneOn
        (fun y => Real.log (2 * Real.sin y) + Real.sqrt 3 * (y - 5 * π / 6))
        (Set.Icc θ (5 * π / 6)) := by
      refine monotoneOn_of_deriv_nonneg (convex_Icc _ _) ?_ ?_ ?_
      · intro x hx
        rw [Set.mem_Icc] at hx
        exact (hu x (lt_of_lt_of_le h0 hx.1)
          (lt_of_le_of_lt hx.2 hstarpi)).continuousAt.continuousWithinAt
      · intro x hx
        rw [interior_Icc, Set.mem_Ioo] at hx
        exact (hu x (lt_trans h0 hx.1)
          (lt_trans hx.2 hstarpi)).differentiableAt.differentiableWithinAt
      · intro x hx
        rw [interior_Icc, Set.mem_Ioo] at hx
        have hx0 : 0 < x := lt_trans h0 hx.1
        have hxpi : x < π := lt_trans hx.2 hstarpi
        rw [(hu x hx0 hxpi).deriv]
        have hanti := cot_antitoneOn (c := x) (d := 5 * π / 6) hx0 hstarpi
          (Set.mem_Icc.mpr ⟨le_rfl, le_of_lt hx.2⟩)
          (Set.mem_Icc.mpr ⟨le_of_lt hx.2, le_rfl⟩) (le_of_lt hx.2)
        dsimp only at hanti
        rw [hcotstar] at hanti
        linarith
    have := hmono (Set.mem_Icc.mpr ⟨le_rfl, hle⟩)
      (Set.mem_Icc.mpr ⟨hle, le_rfl⟩) hle
    dsimp only at this
    rw [hustar] at this
    linarith
  · -- falling after `θ*`
    have hanti : AntitoneOn
        (fun y => Real.log (2 * Real.sin y) + Real.sqrt 3 * (y - 5 * π / 6))
        (Set.Icc (5 * π / 6) θ) := by
      refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) ?_ ?_ ?_
      · intro x hx
        rw [Set.mem_Icc] at hx
        exact (hu x (lt_of_lt_of_le hstar0 hx.1)
          (lt_of_le_of_lt hx.2 hπ)).continuousAt.continuousWithinAt
      · intro x hx
        rw [interior_Icc, Set.mem_Ioo] at hx
        exact (hu x (lt_trans hstar0 hx.1)
          (lt_trans hx.2 hπ)).differentiableAt.differentiableWithinAt
      · intro x hx
        rw [interior_Icc, Set.mem_Ioo] at hx
        have hx0 : 0 < x := lt_trans hstar0 hx.1
        have hxpi : x < π := lt_trans hx.2 hπ
        rw [(hu x hx0 hxpi).deriv]
        have hmono := cot_antitoneOn (c := 5 * π / 6) (d := x) hstar0 hxpi
          (Set.mem_Icc.mpr ⟨le_rfl, le_of_lt hx.1⟩)
          (Set.mem_Icc.mpr ⟨le_of_lt hx.1, le_rfl⟩) (le_of_lt hx.1)
        dsimp only at hmono
        rw [hcotstar] at hmono
        linarith
    have := hanti (Set.mem_Icc.mpr ⟨le_rfl, hle⟩)
      (Set.mem_Icc.mpr ⟨hle, le_rfl⟩) hle
    dsimp only at this
    rw [hustar] at this
    linarith

/-! ## Part 3 — the right tail is Gaussian -/

/-- One step of the right tail: past the saddle the ratio is at most
`exp(−2√3 (θ − θ*))`. -/
theorem kashaevProd_succ_le_exp {N k : ℕ} (hN : N ≠ 0) (hkN : k + 1 < N) :
    kashaevProd N (k + 1)
      ≤ kashaevProd N k
        * Real.exp (-(2 * Real.sqrt 3) * (((k : ℝ) + 1) * π / N - 5 * π / 6)) := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hkR : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
  have hθ0 : 0 < ((k : ℝ) + 1) * π / N := by positivity
  have hθpi : ((k : ℝ) + 1) * π / N < π := by
    rw [div_lt_iff₀ hNR]
    have : (k : ℝ) + 1 < (N : ℝ) := by exact_mod_cast hkN
    nlinarith
  have hs : 0 < Real.sin (((k : ℝ) + 1) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi hθ0 hθpi
  have htan := log_two_sin_le_tangent hθ0 hθpi
  have hkey : (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2
      ≤ Real.exp (-(2 * Real.sqrt 3) * (((k : ℝ) + 1) * π / N - 5 * π / 6)) := by
    have hpos : (0 : ℝ) < 2 * Real.sin (((k : ℝ) + 1) * π / N) := by linarith
    have hlog : Real.log ((2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2)
        ≤ -(2 * Real.sqrt 3) * (((k : ℝ) + 1) * π / N - 5 * π / 6) := by
      rw [Real.log_pow]
      push_cast
      nlinarith [htan]
    calc (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2
        = Real.exp (Real.log ((2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2)) :=
          (Real.exp_log (by positivity)).symm
      _ ≤ _ := Real.exp_le_exp.mpr hlog
  rw [kashaevProd_succ]
  exact mul_le_mul_of_nonneg_left hkey (kashaevProd_nonneg N k)

/-- **The right tail is Gaussian.**  `kashaevProd N (k*+d) ≤ kashaevProd N k* ·
exp(−√3 π d(d−1)/N)`.

The exponent is quadratic in `d` because the tangent bound at `θ*` makes the
per-step penalty grow LINEARLY: summing an arithmetic progression is where the
`d²` comes from.  Bounding every factor by the first would give only `e^{−cd/N}`
and would not confine the sum to a `√N`-window. -/
theorem kashaevProd_right_tail {N : ℕ} (hN : 6 ≤ N) (d : ℕ) (hd : 5 * N / 6 + d < N) :
    kashaevProd N (5 * N / 6 + d)
      ≤ kashaevProd N (5 * N / 6)
        * Real.exp (-(Real.sqrt 3 * π * (d : ℝ) * ((d : ℝ) - 1) / N)) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3nn : (0 : ℝ) ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  -- `5N/6 < k*+1`, so the `j`-th step past the saddle is at least `(j−1)h` beyond it
  have hdiv := Nat.div_add_mod (5 * N) 6
  have hmod : 5 * N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  induction d with
  | zero => simp
  | succ n ih =>
      have hn : 5 * N / 6 + n < N := by omega
      have hstep := kashaevProd_succ_le_exp (N := N) (k := 5 * N / 6 + n) hN0 (by omega)
      have hprev := ih hn
      -- the step's angle is at least `n·h` past `θ*`
      have hgap : ((5 * N / 6 + n : ℕ) : ℝ) + 1 - 5 * (N : ℝ) / 6 ≥ (n : ℝ) := by
        have h1 : (6 : ℝ) * ((5 * N / 6 : ℕ) : ℝ) + 6 > 5 * (N : ℝ) := by
          have : 6 * (5 * N / 6) + 6 > 5 * N := by omega
          exact_mod_cast this
        push_cast
        linarith
      have hangle : -(2 * Real.sqrt 3)
            * (((5 * N / 6 + n : ℕ) : ℝ) + 1) * π / N - (-(2 * Real.sqrt 3)) * (5 * π / 6)
          ≤ -(2 * Real.sqrt 3) * (n : ℝ) * π / N := by
        -- keep the two `π/N` terms SEPARATE, matching the goal's monomials:
        -- `linarith` compares ring-normal forms, and `(X+1−n)·π/N` vs
        -- `(X+1)·π/N − n·π/N` only agree after that split is made explicit.
        have hfrac : 5 * π / 6
            ≤ ((((5 * N / 6 + n : ℕ)) : ℝ) + 1) * π / N - (n : ℝ) * π / N := by
          have hX : 5 * (N : ℝ) / 6 ≤ ((5 * N / 6 + n : ℕ) : ℝ) + 1 - (n : ℝ) := by
            linarith [hgap]
          rw [div_sub_div_same, le_div_iff₀ hNR]
          nlinarith [hX, hpi.le]
        have hpos : (0 : ℝ) ≤ 2 * Real.sqrt 3 := by positivity
        have h2 : 2 * Real.sqrt 3 * (5 * π / 6)
            ≤ 2 * Real.sqrt 3
              * (((((5 * N / 6 + n : ℕ)) : ℝ) + 1) * π / N - (n : ℝ) * π / N) :=
          mul_le_mul_of_nonneg_left hfrac hpos
        ring_nf at h2 ⊢
        linarith
      have hexp : Real.exp (-(2 * Real.sqrt 3)
            * ((((5 * N / 6 + n : ℕ)) : ℝ) + 1) * π / N - (-(2 * Real.sqrt 3)) * (5 * π / 6))
          ≤ Real.exp (-(2 * Real.sqrt 3) * (n : ℝ) * π / N) := Real.exp_le_exp.mpr hangle
      have hstep' : kashaevProd N (5 * N / 6 + n + 1)
          ≤ kashaevProd N (5 * N / 6 + n)
            * Real.exp (-(2 * Real.sqrt 3) * (n : ℝ) * π / N) := by
        refine le_trans hstep ?_
        refine mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _)
        refine le_trans (le_of_eq ?_) hexp
        congr 1
        ring
      have hgoal : kashaevProd N (5 * N / 6 + n + 1)
          ≤ kashaevProd N (5 * N / 6)
            * (Real.exp (-(Real.sqrt 3 * π * (n : ℝ) * ((n : ℝ) - 1) / N))
               * Real.exp (-(2 * Real.sqrt 3) * (n : ℝ) * π / N)) := by
        rw [← mul_assoc]
        refine le_trans hstep' ?_
        exact mul_le_mul_of_nonneg_right hprev (le_of_lt (Real.exp_pos _))
      refine le_trans hgoal ?_
      rw [← Real.exp_add]
      refine mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr (le_of_eq ?_))
        (kashaevProd_nonneg N _)
      push_cast
      field_simp
      ring_nf

/-! ## Part 4 — the left tail, from a SECANT bound

Concavity is the wrong way round on the left: the terms are rising towards the
saddle, so what is needed is a LOWER bound on `f = log(2 sin)`, and the tangent
gives an upper one.  A secant does the job on a bounded window — `cot` is
antitone, so `cot ≤ cot(2π/3) = −1/√3` on `[2π/3, θ*]`, and integrating that
back from `θ*` (where `f` vanishes) gives `f(θ) ≥ (θ* − θ)/√3` there. -/

/-- `cot(2π/3) = −1/√3`. -/
theorem cot_two_pi_div_three :
    Real.cos (2 * π / 3) / Real.sin (2 * π / 3) = -(1 / Real.sqrt 3) := by
  have h1 : (2 : ℝ) * π / 3 = π - π / 3 := by ring
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  rw [h1, Real.cos_pi_sub, Real.sin_pi_sub, Real.cos_pi_div_three,
    Real.sin_pi_div_three]
  field_simp

/-- **Secant bound.**  `log(2 sin θ) ≥ (5π/6 − θ)/√3` on `[2π/3, 5π/6]`.
The left-hand counterpart of `log_two_sin_le_tangent`, and the reason the left
tail is Gaussian too. -/
theorem le_log_two_sin_secant {θ : ℝ} (h1 : 2 * π / 3 ≤ θ) (h2 : θ ≤ 5 * π / 6) :
    (5 * π / 6 - θ) / Real.sqrt 3 ≤ Real.log (2 * Real.sin θ) := by
  have hpi := Real.pi_pos
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have h23 : (0 : ℝ) < 2 * π / 3 := by linarith
  have hstarpi : (5 : ℝ) * π / 6 < π := by linarith
  have hθ0 : 0 < θ := lt_of_lt_of_le h23 h1
  have hθpi : θ < π := lt_of_le_of_lt h2 hstarpi
  -- `v y = log(2 sin y) + (y − θ*)/√3`, with `v θ* = 0` and `v′ = cot y + 1/√3`
  have hv : ∀ x, 0 < x → x < π →
      HasDerivAt (fun y => Real.log (2 * Real.sin y) + (y - 5 * π / 6) / Real.sqrt 3)
        (Real.cos x / Real.sin x + 1 / Real.sqrt 3) x := by
    intro x hx0 hxpi
    have hA := QOU.MathlibExt.hasDerivAt_log_two_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi hx0 hxpi))
    have hB : HasDerivAt (fun y : ℝ => (y - 5 * π / 6) / Real.sqrt 3)
        (1 / Real.sqrt 3) x := by
      simpa using ((hasDerivAt_id x).sub_const (5 * π / 6)).div_const (Real.sqrt 3)
    exact hA.add hB
  have hvstar : Real.log (2 * Real.sin (5 * π / 6))
      + (5 * π / 6 - 5 * π / 6) / Real.sqrt 3 = 0 := by
    rw [sin_five_pi_div_six]; norm_num
  have hanti : AntitoneOn
      (fun y => Real.log (2 * Real.sin y) + (y - 5 * π / 6) / Real.sqrt 3)
      (Set.Icc θ (5 * π / 6)) := by
    refine antitoneOn_of_deriv_nonpos (convex_Icc _ _) ?_ ?_ ?_
    · intro x hx
      rw [Set.mem_Icc] at hx
      exact (hv x (lt_of_lt_of_le hθ0 hx.1)
        (lt_of_le_of_lt hx.2 hstarpi)).continuousAt.continuousWithinAt
    · intro x hx
      rw [interior_Icc, Set.mem_Ioo] at hx
      exact (hv x (lt_trans hθ0 hx.1)
        (lt_trans hx.2 hstarpi)).differentiableAt.differentiableWithinAt
    · intro x hx
      rw [interior_Icc, Set.mem_Ioo] at hx
      have hx0 : 0 < x := lt_trans hθ0 hx.1
      have hxpi : x < π := lt_trans hx.2 hstarpi
      rw [(hv x hx0 hxpi).deriv]
      -- `cot x ≤ cot(2π/3) = −1/√3`, since `x ≥ 2π/3` and `cot` is antitone
      have hx23 : 2 * π / 3 ≤ x := le_trans h1 (le_of_lt hx.1)
      have hcot := cot_antitoneOn (c := 2 * π / 3) (d := x) h23 hxpi
        (Set.mem_Icc.mpr ⟨le_rfl, hx23⟩) (Set.mem_Icc.mpr ⟨hx23, le_rfl⟩) hx23
      dsimp only at hcot
      rw [cot_two_pi_div_three] at hcot
      linarith
  have hle := hanti (Set.mem_Icc.mpr ⟨le_rfl, h2⟩)
    (Set.mem_Icc.mpr ⟨h2, le_rfl⟩) h2
  dsimp only at hle
  rw [hvstar] at hle
  have hrw : (5 * π / 6 - θ) / Real.sqrt 3 = -((θ - 5 * π / 6) / Real.sqrt 3) := by
    ring
  rw [hrw]
  linarith

/-- One step of the left tail: below the saddle the ratio is at least
`exp(2(θ* − θ)/√3)`. -/
theorem kashaevProd_succ_ge_exp {N k : ℕ} (hN : N ≠ 0)
    (hlo : 2 * N ≤ 3 * (k + 1)) (hhi : 6 * (k + 1) ≤ 5 * N) :
    kashaevProd N k
        * Real.exp (2 * (5 * π / 6 - ((k : ℝ) + 1) * π / N) / Real.sqrt 3)
      ≤ kashaevProd N (k + 1) := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hloR : 2 * (N : ℝ) ≤ 3 * ((k : ℝ) + 1) := by exact_mod_cast hlo
  have hhiR : 6 * ((k : ℝ) + 1) ≤ 5 * (N : ℝ) := by exact_mod_cast hhi
  have h1 : 2 * π / 3 ≤ ((k : ℝ) + 1) * π / N := by
    rw [le_div_iff₀ hNR]; nlinarith
  have h2 : ((k : ℝ) + 1) * π / N ≤ 5 * π / 6 := by
    rw [div_le_iff₀ hNR]; nlinarith
  have hθ0 : 0 < ((k : ℝ) + 1) * π / N := lt_of_lt_of_le (by linarith) h1
  have hθpi : ((k : ℝ) + 1) * π / N < π := lt_of_le_of_lt h2 (by linarith)
  have hs : 0 < Real.sin (((k : ℝ) + 1) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi hθ0 hθpi
  have hsec := le_log_two_sin_secant h1 h2
  have hkey : Real.exp (2 * (5 * π / 6 - ((k : ℝ) + 1) * π / N) / Real.sqrt 3)
      ≤ (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 := by
    have hlog : 2 * (5 * π / 6 - ((k : ℝ) + 1) * π / N) / Real.sqrt 3
        ≤ Real.log ((2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2) := by
      rw [Real.log_pow]
      push_cast
      have hmul := mul_le_mul_of_nonneg_left hsec (by norm_num : (0 : ℝ) ≤ 2)
      ring_nf at hmul ⊢
      linarith
    calc Real.exp (2 * (5 * π / 6 - ((k : ℝ) + 1) * π / N) / Real.sqrt 3)
        ≤ Real.exp (Real.log ((2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2)) :=
          Real.exp_le_exp.mpr hlog
      _ = (2 * Real.sin (((k : ℝ) + 1) * π / N)) ^ 2 :=
          Real.exp_log (by positivity)
  rw [kashaevProd_succ]
  exact mul_le_mul_of_nonneg_left hkey (kashaevProd_nonneg N k)

/-- **The left tail is Gaussian too.**  For `b ≤ 5N/6` and `d` steps back that
stay above `2π/3`,

    kashaevProd N (b−d) ≤ kashaevProd N b · exp(−π d(d−1)/(√3 N)).

The step-`d` gain is `θ* − θ_{b−d}`, which is at least `d·h` precisely because
`b ≤ 5N/6` — the same arithmetic progression as the right tail, run backwards,
with `1/√3` in place of `√3` because a secant is shallower than the tangent. -/
theorem kashaevProd_left_tail {N b : ℕ} (hN : N ≠ 0) (hb : 6 * b ≤ 5 * N)
    (d : ℕ) (hd : d ≤ b) (hlo : 2 * N ≤ 3 * (b - d)) :
    kashaevProd N (b - d)
      ≤ kashaevProd N b
        * Real.exp (-(π * (d : ℝ) * ((d : ℝ) - 1) / (Real.sqrt 3 * (N : ℝ)))) := by
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hbR : 6 * (b : ℝ) ≤ 5 * (N : ℝ) := by exact_mod_cast hb
  induction d with
  | zero => simp
  | succ n ih =>
      have hn : n ≤ b := by omega
      have hlon : 2 * N ≤ 3 * (b - n) := by omega
      have hprev := ih hn hlon
      -- one more step back, from `b − n − 1` to `b − n`
      have hsucc : b - (n + 1) + 1 = b - n := by omega
      have hstep := kashaevProd_succ_ge_exp (N := N) (k := b - (n + 1)) hN
        (by omega) (by omega)
      rw [hsucc] at hstep
      have hcast : ((b - (n + 1) : ℕ) : ℝ) + 1 = ((b - n : ℕ) : ℝ) := by
        have : (b - (n + 1) : ℕ) + 1 = (b - n : ℕ) := by omega
        exact_mod_cast congrArg (Nat.cast : ℕ → ℝ) this
      rw [hcast] at hstep
      -- the gain at this step is at least `n·h`
      have hgain : 2 * ((n : ℝ) * π / N) / Real.sqrt 3
          ≤ 2 * (5 * π / 6 - ((b - n : ℕ) : ℝ) * π / N) / Real.sqrt 3 := by
        have hbn : ((b - n : ℕ) : ℝ) + (n : ℝ) ≤ 5 * (N : ℝ) / 6 := by
          have h1 : ((b - n : ℕ) : ℝ) + (n : ℝ) = (b : ℝ) := by
            have : (b - n : ℕ) + n = b := by omega
            exact_mod_cast congrArg (Nat.cast : ℕ → ℝ) this
          rw [h1]; linarith
        have hfrac : ((b - n : ℕ) : ℝ) * π / N + (n : ℝ) * π / N ≤ 5 * π / 6 := by
          rw [← add_div, div_le_iff₀ hNR]
          nlinarith [hbn, hpi.le]
        have hnum : 2 * ((n : ℝ) * π / N)
            ≤ 2 * (5 * π / 6 - ((b - n : ℕ) : ℝ) * π / N) := by linarith
        have h := mul_le_mul_of_nonneg_right hnum
          (le_of_lt (inv_pos.mpr hs3))
        simpa [div_eq_mul_inv] using h
      have hchain : kashaevProd N (b - (n + 1))
          * Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3)
          ≤ kashaevProd N (b - n) :=
        le_trans (mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hgain)
          (kashaevProd_nonneg N _)) hstep
      -- divide through and fold the two exponentials together
      have hpos : (0 : ℝ) < Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3) :=
        Real.exp_pos _
      have hbound : kashaevProd N (b - (n + 1))
          ≤ kashaevProd N b
            * Real.exp (-(π * (n : ℝ) * ((n : ℝ) - 1) / (Real.sqrt 3 * (N : ℝ))))
            * Real.exp (-(2 * ((n : ℝ) * π / N) / Real.sqrt 3)) := by
        rw [Real.exp_neg (2 * ((n : ℝ) * π / N) / Real.sqrt 3)]
        calc kashaevProd N (b - (n + 1))
            = kashaevProd N (b - (n + 1))
              * Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3)
              * (Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3))⁻¹ := by
                field_simp
          _ ≤ kashaevProd N (b - n)
              * (Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3))⁻¹ :=
                mul_le_mul_of_nonneg_right hchain (by positivity)
          _ ≤ kashaevProd N b
              * Real.exp (-(π * (n : ℝ) * ((n : ℝ) - 1) / (Real.sqrt 3 * (N : ℝ))))
              * (Real.exp (2 * ((n : ℝ) * π / N) / Real.sqrt 3))⁻¹ :=
                mul_le_mul_of_nonneg_right hprev (by positivity)
      refine le_trans hbound (le_of_eq ?_)
      rw [mul_assoc, ← Real.exp_add]
      congr 1
      have hs3ne : Real.sqrt 3 ≠ 0 := ne_of_gt hs3
      have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNR
      push_cast
      field_simp
      ring_nf

end QOU.Knot.FigureEightVolume
