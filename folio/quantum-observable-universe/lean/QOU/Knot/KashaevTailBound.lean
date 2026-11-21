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

  WHAT THE FILE CONTAINS, in order.  Parts 1–2 are the pointwise inequalities
  (`cot` antitone; the tangent and the secant).  Parts 3–4 are the two tails.
  Parts 5–6 turn the tails into UPPER bounds on the sum over each region, and
  Part 6 handles the stretch below the secant's window with no analysis at all
  (the down–up–down shape dominates it by its endpoints).  Parts 7–8 are the
  matching LOWER bounds, which need the tangent again — on the rising side
  concavity finally points the right way, so Part 7 carries NO window.

  Part 9 recombines them.  `sum_kashaevProd_le_split` bounds
  `∑_{k<N} kashaevProd N k` above by the three regions' bounds (an exact
  three-way split of `Finset.range N`, plus one order-reversing reindex to move
  the distance-indexed window sum onto an interval), and `le_sum_kashaevProd`
  bounds it BELOW by `e^{−1}·m·g_{k*}` whenever `√3πm² ≤ N`.  The lower bound
  needs no decomposition at all — dropping terms only helps.

  Parts 10–11 collapse the below-window region against the peak — `N² ≤ g_{k*}`
  and `g_w ≤ g_{k*}e^{−x}` with `e^{−x} ≤ 1/x` — and assemble
  `kashaev_le_argmax_mul`:

      ⟨4₁⟩_N ≤ g_{k*}·( w/N² + w√3N/(πD(D−1)) + (2 + ½√(√3N)) + (2 + ½√(N/√3)) )

  with `D = k*−w`.  Together with `le_kashaev` the invariant is now bounded on
  BOTH sides by explicit multiples of its own largest term.

  WHAT IS STILL MISSING.  The bounds are RELATIVE to `g_{k*}`; nothing here
  evaluates `g_{k*}` itself.  Turning them into `c_σ` means feeding
  `log g_{k*} = 2·s_{k*}` through `kashaev_log_sum_asymptotic`, and that join is
  untouched.  The constant is also left as an expression rather than a numeral:
  collapsing it needs `√3 ≤ 1.8`, `π ≥ 3.14` and a threshold on `N`, which this
  statement deliberately avoids.

  -- Ref: [leitner2026] QOU/Knot/KashaevArgmax.lean
  -- Ref: [leitner2026] QOU/Knot/LobTaylorSaddle.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaSum.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianSumBound.lean
-/
import QOU.Knot.KashaevArgmax
import QOU.Knot.LobTaylorSaddle
import QOU.MathlibExt.TrapezoidRule
import QOU.MathlibExt.GaussianSumBound
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

/-! ## Part 5 — the upper half-sum is `O(√N)` times its largest term

This is where the `N^{3/2}` comes from.  `log_kashaev_le_log_add` already gives
`⟨4₁⟩_N ≤ N · g_{k*}` — enough for the exponential growth RATE and nothing
finer.  Feeding the Gaussian tail into `sum_exp_neg_mul_mul_pred_le` replaces
that `N` by `2 + ½√(N/√3)`, and `√(N/√3)` is exactly the Laplace factor the
tetrahedral probe measures. -/

/-- **The sum from the saddle upward is `O(√N)` times its largest term.** -/
theorem sum_kashaevProd_right_le {N : ℕ} (hN : 6 ≤ N) :
    ∑ k ∈ Finset.Ico (5 * N / 6) N, kashaevProd N k
      ≤ kashaevProd N (5 * N / 6)
        * (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have ha : (0 : ℝ) < Real.sqrt 3 * π / N := by positivity
  rw [Finset.sum_Ico_eq_sum_range]
  have hrw : ∀ i : ℕ,
      Real.sqrt 3 * π * (i : ℝ) * ((i : ℝ) - 1) / N
        = Real.sqrt 3 * π / N * (i : ℝ) * ((i : ℝ) - 1) := by
    intro i; field_simp
  have hterm : ∀ i ∈ Finset.range (N - 5 * N / 6),
      kashaevProd N (5 * N / 6 + i)
        ≤ kashaevProd N (5 * N / 6)
          * Real.exp (-(Real.sqrt 3 * π / N * (i : ℝ) * ((i : ℝ) - 1))) := by
    intro i hi
    rw [Finset.mem_range] at hi
    have h := kashaevProd_right_tail hN i (by omega)
    rwa [hrw i] at h
  refine le_trans (Finset.sum_le_sum hterm) ?_
  rw [← Finset.mul_sum]
  refine mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _)
  have hb := QOU.MathlibExt.sum_exp_neg_mul_mul_pred_le
    (a := Real.sqrt 3 * π / N) ha (N - 5 * N / 6)
  have hval : π / (Real.sqrt 3 * π / N) = (N : ℝ) / Real.sqrt 3 := by
    field_simp
  rwa [hval] at hb

/-- **The window below the saddle is `O(√N)` times its largest term too.**

Stated by DISTANCE `d` from the saddle rather than by index `k`, which is how
`kashaevProd_left_tail` is indexed — so no reindexing is needed and the
Gaussian sum bound applies directly.  The set `{k* − d : d < m}` is
`Ico (k*−m+1) (k*+1)`; saying so is not needed to state or use the bound.

The window hypothesis `2N ≤ 3(k*−m)` is the secant's domain `θ ≥ 2π/3`, so `m`
reaches about `N/6` — far wider than the `√N` that matters. -/
theorem sum_kashaevProd_left_window_le {N : ℕ} (hN : 6 ≤ N) (m : ℕ)
    (hm : m ≤ 5 * N / 6) (hw : 2 * N ≤ 3 * (5 * N / 6 - m)) :
    ∑ d ∈ Finset.range m, kashaevProd N (5 * N / 6 - d)
      ≤ kashaevProd N (5 * N / 6)
        * (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have ha : (0 : ℝ) < π / (Real.sqrt 3 * N) := by positivity
  have hbk : 6 * (5 * N / 6) ≤ 5 * N := by
    have hd := Nat.div_add_mod (5 * N) 6
    omega
  have hrw : ∀ d : ℕ,
      π * (d : ℝ) * ((d : ℝ) - 1) / (Real.sqrt 3 * (N : ℝ))
        = π / (Real.sqrt 3 * (N : ℝ)) * (d : ℝ) * ((d : ℝ) - 1) := by
    intro d; field_simp
  have hterm : ∀ d ∈ Finset.range m,
      kashaevProd N (5 * N / 6 - d)
        ≤ kashaevProd N (5 * N / 6)
          * Real.exp (-(π / (Real.sqrt 3 * (N : ℝ)) * (d : ℝ) * ((d : ℝ) - 1))) := by
    intro d hd
    rw [Finset.mem_range] at hd
    have h := kashaevProd_left_tail (N := N) (b := 5 * N / 6) hN0 hbk d
      (by omega) (by omega)
    rwa [hrw d] at h
  refine le_trans (Finset.sum_le_sum hterm) ?_
  rw [← Finset.mul_sum]
  refine mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _)
  have hb := QOU.MathlibExt.sum_exp_neg_mul_mul_pred_le
    (a := π / (Real.sqrt 3 * (N : ℝ))) ha m
  have hval : π / (π / (Real.sqrt 3 * (N : ℝ))) = Real.sqrt 3 * (N : ℝ) := by
    field_simp
  rwa [hval] at hb

/-! ## Part 6 — the region below the secant window

`sum_kashaevProd_left_window_le` reaches down only to `θ = 2π/3`; below that the
secant is no longer valid.  What is there instead is the DOWN–UP–DOWN shape:
the sequence falls on `[0, ⌊N/6⌋]` and rises on `[⌈N/6⌉, w]`, so every term is
dominated by one of the two ENDS of that stretch.  No analysis is needed, only
the monotonicity runs from `KashaevArgmax`. -/

/-- Below the window, every term is dominated by an endpoint: `g_k ≤ max 1 g_w`
for `k ≤ w ≤ 5N/6`.  `1 = kashaevProd N 0` covers the falling stretch and `g_w`
the rising one. -/
theorem kashaevProd_le_max_of_le {N k w : ℕ} (hN : N ≠ 0) (hkw : k ≤ w)
    (hw : 6 * w ≤ 5 * N) :
    kashaevProd N k ≤ max 1 (kashaevProd N w) := by
  rcases le_or_gt (6 * k) N with hlow | hhigh
  · have h := kashaevProd_le_of_falling_small hN (Nat.zero_le k) (fun j _ hj2 => by
      have hj : 6 * j ≤ N := by omega
      exact_mod_cast hj)
    rw [kashaevProd_zero] at h
    exact le_trans h (le_max_left _ _)
  · have h := kashaevProd_le_of_rising hN hkw (fun j hj1 hj2 => ⟨by
      have hj : N ≤ 6 * j := by omega
      exact_mod_cast hj, by
      have hj : 6 * j ≤ 5 * N := by omega
      exact_mod_cast hj⟩)
    exact le_trans h (le_max_right _ _)

/-- **The whole region below the secant window is at most `w · max 1 g_w`.**

That is `O(N)` times an endpoint value, not `O(√N)` times the peak — but the
endpoint `g_w` is itself exponentially below the peak (`kashaevProd_left_tail`
at distance `k* − w ≈ N/6`), so the region contributes `O(1)` relative to
`g_{k*}` rather than `O(√N)`.  Turning that into a single numeric constant is
arithmetic over `e^{−x} ≤ 1/x` and `N² ≤ g_{k*}`; it is NOT done here, and this
lemma alone does not bound `⟨4₁⟩_N`. -/
theorem sum_kashaevProd_below_window_le {N w : ℕ} (hN : N ≠ 0) (hw : 6 * w ≤ 5 * N) :
    ∑ k ∈ Finset.range w, kashaevProd N k
      ≤ (w : ℝ) * max 1 (kashaevProd N w) := by
  calc ∑ k ∈ Finset.range w, kashaevProd N k
      ≤ ∑ _k ∈ Finset.range w, max 1 (kashaevProd N w) :=
        Finset.sum_le_sum (fun k hk =>
          kashaevProd_le_max_of_le hN (le_of_lt (Finset.mem_range.mp hk)) hw)
    _ = (w : ℝ) * max 1 (kashaevProd N w) := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]

/-- `N² ≤ kashaevProd N ⌊5N/6⌋` — the peak dominates the exact endpoint value
`kashaevProd N (N−1) = N²`.  Sharper than `one_le_kashaevProd_argmax`, and it
is what makes the `k ≤ N/6` terms (each `≤ 1`) negligible against the peak. -/
theorem sq_le_kashaevProd_argmax {N : ℕ} (hN : 6 ≤ N) :
    ((N : ℝ)) ^ 2 ≤ kashaevProd N (5 * N / 6) := by
  have hN0 : N ≠ 0 := by omega
  have hks : 5 * N / 6 < N := by
    rw [Nat.div_lt_iff_lt_mul (by norm_num)]; omega
  have hdiv := Nat.div_add_mod (5 * N) 6
  have hmod : 5 * N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  have hfall : kashaevProd N (N - 1) ≤ kashaevProd N (5 * N / 6) := by
    refine kashaevProd_le_of_falling hN0 (by omega) (by omega) (fun j hj1 _ => ?_)
    have hj : 5 * N < 6 * j := by omega
    exact_mod_cast Nat.le_of_lt hj
  rwa [kashaevProd_endpoint hN0] at hfall

/-! ## Part 7 — the first LOWER bound: the peak is not a spike

Everything above bounds the terms from ABOVE, which gives an upper bound on
`⟨4₁⟩_N` and therefore an inequality, not a value.  Laplace needs the other
side: the terms near the peak must stay LARGE over a `√N`-wide stretch, or the
sum could be `g_{k*}` and nothing more.

The bound needed is the mirror image, and the surprise is that it needs no new
analysis.  Below `θ*` the terms are rising, so a LOWER bound on `g_{k*−d}` needs
an UPPER bound on the accumulated `log(2 sin)` — and that is exactly what the
TANGENT gives.  Concavity, which pointed the wrong way for the upper bound on
the left, points the right way here.  In particular there is NO WINDOW: the
tangent bound is global on `(0, π)`, so this holds for every `d ≤ k*`. -/

/-- **Lower bound below the saddle.**  `g_{k*−d} ≥ g_{k*}·exp(−√3π d(d+1)/N)`,
for every `d ≤ k*`.

Note `d(d+1)`, not `d(d−1)`: bounding from below costs one step more than
bounding from above, because the `d`-th step back is at most `(d+1)h` from `θ*`
rather than at least `(d−1)h`. -/
theorem kashaevProd_ge_left {N : ℕ} (hN : 6 ≤ N) (d : ℕ) (hd : d ≤ 5 * N / 6) :
    kashaevProd N (5 * N / 6)
        * Real.exp (-(Real.sqrt 3 * π * (d : ℝ) * ((d : ℝ) + 1) / N))
      ≤ kashaevProd N (5 * N / 6 - d) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hks : 5 * N / 6 < N := by
    rw [Nat.div_lt_iff_lt_mul (by norm_num)]; omega
  have hdiv := Nat.div_add_mod (5 * N) 6
  have hmod : 5 * N % 6 < 6 := Nat.mod_lt _ (by norm_num)
  induction d with
  | zero => simp
  | succ n ih =>
      have hn : n ≤ 5 * N / 6 := by omega
      have hprev := ih hn
      -- the tangent step, read downwards
      have hstep := kashaevProd_succ_le_exp (N := N) (k := 5 * N / 6 - (n + 1))
        hN0 (by omega)
      have hcast : ((5 * N / 6 - (n + 1) : ℕ) : ℝ) + 1 = ((5 * N / 6 - n : ℕ) : ℝ) := by
        have h : (5 * N / 6 - (n + 1) : ℕ) + 1 = (5 * N / 6 - n : ℕ) := by omega
        exact_mod_cast congrArg (Nat.cast : ℕ → ℝ) h
      have hsucc : 5 * N / 6 - (n + 1) + 1 = 5 * N / 6 - n := by omega
      rw [hsucc, hcast] at hstep
      -- the `n`-th step back is at most `(n+1)h` from `θ*`; this is the ONLY
      -- inequality in the induction, and it is `hfrac` scaled by `2√3`
      have hks1 : 5 * (N : ℝ) / 6 ≤ ((5 * N / 6 - n : ℕ) : ℝ) + ((n : ℝ) + 1) := by
        have h : ((5 * N / 6 - n : ℕ) : ℝ) + (n : ℝ) = ((5 * N / 6 : ℕ) : ℝ) := by
          have : (5 * N / 6 - n : ℕ) + n = 5 * N / 6 := by omega
          exact_mod_cast congrArg (Nat.cast : ℕ → ℝ) this
        have h2 : 6 * ((5 * N / 6 : ℕ) : ℝ) + 6 > 5 * (N : ℝ) := by
          have : 6 * (5 * N / 6) + 6 > 5 * N := by omega
          exact_mod_cast this
        linarith
      have hfrac : 5 * π / 6
          ≤ ((5 * N / 6 - n : ℕ) : ℝ) * π / N + ((n : ℝ) + 1) * π / N := by
        rw [← add_div, le_div_iff₀ hNR]
        nlinarith [hks1, hpi.le]
      have h2 := mul_le_mul_of_nonneg_left hfrac
        (by positivity : (0 : ℝ) ≤ 2 * Real.sqrt 3)
      -- divide the step through
      have hE : (0 : ℝ) < Real.exp (-(2 * Real.sqrt 3)
          * (((5 * N / 6 - n : ℕ) : ℝ) * π / N - 5 * π / 6)) := Real.exp_pos _
      have hdown : kashaevProd N (5 * N / 6 - n)
          * (Real.exp (-(2 * Real.sqrt 3)
              * (((5 * N / 6 - n : ℕ) : ℝ) * π / N - 5 * π / 6)))⁻¹
          ≤ kashaevProd N (5 * N / 6 - (n + 1)) := by
        have h := mul_le_mul_of_nonneg_right hstep (le_of_lt (inv_pos.mpr hE))
        rwa [mul_inv_cancel_right₀ (ne_of_gt hE)] at h
      refine le_trans ?_ hdown
      rw [← Real.exp_neg]
      push_cast
      calc kashaevProd N (5 * N / 6)
            * Real.exp (-(Real.sqrt 3 * π * ((n : ℝ) + 1) * ((n : ℝ) + 1 + 1) / N))
          ≤ kashaevProd N (5 * N / 6)
            * (Real.exp (-(Real.sqrt 3 * π * (n : ℝ) * ((n : ℝ) + 1) / N))
               * Real.exp (-(-(2 * Real.sqrt 3)
                   * (((5 * N / 6 - n : ℕ) : ℝ) * π / N - 5 * π / 6)))) := by
            refine mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _)
            rw [← Real.exp_add]
            refine Real.exp_le_exp.mpr ?_
            ring_nf at h2 ⊢
            linarith
        _ = kashaevProd N (5 * N / 6)
              * Real.exp (-(Real.sqrt 3 * π * (n : ℝ) * ((n : ℝ) + 1) / N))
            * Real.exp (-(-(2 * Real.sqrt 3)
                * (((5 * N / 6 - n : ℕ) : ℝ) * π / N - 5 * π / 6))) := by ring
        _ ≤ kashaevProd N (5 * N / 6 - n)
            * Real.exp (-(-(2 * Real.sqrt 3)
                * (((5 * N / 6 - n : ℕ) : ℝ) * π / N - 5 * π / 6))) :=
            mul_le_mul_of_nonneg_right hprev (le_of_lt (Real.exp_pos _))

/-! ## Part 8 — the sum below the saddle is at least `m` terms' worth

The mirror of Part 5/6's upper bounds.  It needs no integral comparison and no
Gaussian integral: the exponent `d(d+1)` is monotone in `d`, so every term of
`∑_{d<m}` is at least the LAST one, and the sum is at least `m` copies of it.
Choosing `m ≈ √(N/(√3π))` makes that last term `≥ e^{−1}`, so the sum is
`≥ e^{−1}·m·g_{k*}` — the `√N` from below. -/

/-- **Lower bound for the window sum**, the mirror of
`sum_kashaevProd_left_window_le`.  Every term is at least the last. -/
theorem le_sum_kashaevProd_left {N : ℕ} (hN : 6 ≤ N) (m : ℕ) (hm : m ≤ 5 * N / 6) :
    kashaevProd N (5 * N / 6)
        * ((m : ℝ) * Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N)))
      ≤ ∑ d ∈ Finset.range m, kashaevProd N (5 * N / 6 - d) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hterm : ∀ d ∈ Finset.range m,
      kashaevProd N (5 * N / 6)
          * Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N))
        ≤ kashaevProd N (5 * N / 6 - d) := by
    intro d hd
    rw [Finset.mem_range] at hd
    have hdm : (d : ℝ) * ((d : ℝ) + 1) ≤ (m : ℝ) * ((m : ℝ) - 1) := by
      have h1 : (d : ℝ) + 1 ≤ (m : ℝ) := by exact_mod_cast hd
      have h0 : (0 : ℝ) ≤ (d : ℝ) := Nat.cast_nonneg d
      nlinarith
    have hmono : Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N))
        ≤ Real.exp (-(Real.sqrt 3 * π * (d : ℝ) * ((d : ℝ) + 1) / N)) := by
      refine Real.exp_le_exp.mpr ?_
      rw [neg_le_neg_iff, div_le_div_iff_of_pos_right hNR]
      nlinarith [mul_le_mul_of_nonneg_left hdm (mul_nonneg hs3.le hpi.le)]
    refine le_trans (mul_le_mul_of_nonneg_left hmono (kashaevProd_nonneg N _)) ?_
    exact kashaevProd_ge_left hN d (by omega)
  have hcard := Finset.card_nsmul_le_sum (Finset.range m)
    (fun d => kashaevProd N (5 * N / 6 - d))
    (kashaevProd N (5 * N / 6)
      * Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N))) hterm
  rw [Finset.card_range, nsmul_eq_mul] at hcard
  calc kashaevProd N (5 * N / 6)
        * ((m : ℝ) * Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N)))
      = (m : ℝ) * (kashaevProd N (5 * N / 6)
          * Real.exp (-(Real.sqrt 3 * π * (m : ℝ) * ((m : ℝ) - 1) / N))) := by ring
    _ ≤ _ := hcard

/-- **The `√N` from below.**  When `√3·π·m² ≤ N` the last term is `≥ e^{−1}`, so
the window sum is at least `e^{−1}·m·g_{k*}`.  Taking `m ≈ √(N/(√3π))` makes
that `≥ c√N·g_{k*}` — the matching side of `sum_kashaevProd_right_le`.

The caller chooses `m`; picking it as an explicit floor-of-a-square-root is
Nat arithmetic that would obscure the one inequality doing the work. -/
theorem le_sum_kashaevProd_left_of_sq {N m : ℕ} (hN : 6 ≤ N) (hm : m ≤ 5 * N / 6)
    (hsq : Real.sqrt 3 * π * (m : ℝ) ^ 2 ≤ N) :
    kashaevProd N (5 * N / 6) * ((m : ℝ) * Real.exp (-1))
      ≤ ∑ d ∈ Finset.range m, kashaevProd N (5 * N / 6 - d) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hmR : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
  refine le_trans ?_ (le_sum_kashaevProd_left hN m hm)
  refine mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _)
  refine mul_le_mul_of_nonneg_left ?_ hmR
  refine Real.exp_le_exp.mpr ?_
  rw [neg_le_neg_iff, div_le_one hNR]
  have hmm : (m : ℝ) * ((m : ℝ) - 1) ≤ (m : ℝ) ^ 2 := by nlinarith
  nlinarith [mul_le_mul_of_nonneg_left hmm (mul_nonneg hs3.le hpi.le), hsq]

/-! ## Part 9 — recombination

The window sums are indexed by DISTANCE from the saddle (which is what made the
Gaussian bounds apply with no reindexing); `⟨4₁⟩_N` is indexed by `k`.  Moving
between them is one order-reversing reindex, and then the three regions are an
exact three-way split of `Finset.range N`. -/

/-- The distance-indexed window sum IS the interval sum, reflected. -/
theorem sum_kashaevProd_Icc_eq {N w : ℕ} (hw : w ≤ 5 * N / 6) :
    ∑ k ∈ Finset.Icc w (5 * N / 6), kashaevProd N k
      = ∑ d ∈ Finset.range (5 * N / 6 - w + 1), kashaevProd N (5 * N / 6 - d) := by
  have h1 : Finset.Icc w (5 * N / 6) = Finset.Ico w (5 * N / 6 + 1) :=
    (Finset.Ico_succ_right_eq_Icc w (5 * N / 6)).symm
  rw [h1, Finset.sum_Ico_eq_sum_range]
  have h2 : 5 * N / 6 + 1 - w = 5 * N / 6 - w + 1 := by omega
  rw [h2, ← Finset.sum_range_reflect (fun i => kashaevProd N (w + i))
    (5 * N / 6 - w + 1)]
  refine Finset.sum_congr rfl (fun j hj => ?_)
  rw [Finset.mem_range] at hj
  congr 1
  omega

/-- **The three regions, recombined.**  An exact split of `Finset.range N` into
`[0, w)`, `[w, k*]` and `(k*, N)`, each bounded by the corresponding lemma.

Every piece here is sorry-free, but the first summand is `O(N)·max 1 g_w`, NOT
`O(√N)·g_{k*}` — collapsing it needs the numeric constant recorded in the bean
(`e^{−x} ≤ 1/x` against `D = k*−w ≈ N/6`, threshold `N ≥ 62`).  So this is a
bound on `⟨4₁⟩_N` in three named pieces, not the `C√N·g_{k*}` statement.

`hw2` is `2N + 3 ≤ 3w`, one step stricter than the secant window's `2N ≤ 3w`:
the middle region here is the CLOSED `[w, k*]`, so the distance-indexed sum runs
to `d = k*−w`, which lands at `w` — and the window has to hold there too. -/
theorem sum_kashaevProd_le_split {N w : ℕ} (hN : 6 ≤ N) (hw1 : 6 * w ≤ 5 * N)
    (hw2 : 2 * N + 3 ≤ 3 * w) (hwk : w ≤ 5 * N / 6) :
    ∑ k ∈ Finset.range N, kashaevProd N k
      ≤ (w : ℝ) * max 1 (kashaevProd N w)
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2) := by
  have hN0 : N ≠ 0 := by omega
  have hks : 5 * N / 6 < N := by
    rw [Nat.div_lt_iff_lt_mul (by norm_num)]; omega
  -- exact split `range N = [0,w) ⊎ [w,k*] ⊎ (k*,N)`
  have hsplit : ∑ k ∈ Finset.range N, kashaevProd N k
      = (∑ k ∈ Finset.range w, kashaevProd N k)
        + (∑ k ∈ Finset.Icc w (5 * N / 6), kashaevProd N k)
        + ∑ k ∈ Finset.Ico (5 * N / 6 + 1) N, kashaevProd N k := by
    have e2 : Finset.Icc w (5 * N / 6) = Finset.Ico w (5 * N / 6 + 1) :=
      (Finset.Ico_succ_right_eq_Icc w (5 * N / 6)).symm
    have s1 := Finset.sum_Ico_consecutive (fun k => kashaevProd N k)
      (Nat.zero_le w) (show w ≤ N by omega)
    have s2 := Finset.sum_Ico_consecutive (fun k => kashaevProd N k)
      (show w ≤ 5 * N / 6 + 1 by omega) (show 5 * N / 6 + 1 ≤ N by omega)
    rw [e2, Finset.range_eq_Ico]
    linarith [s1, s2]
  rw [hsplit]
  have hbelow := sum_kashaevProd_below_window_le (N := N) (w := w) hN0 hw1
  have hmid : ∑ k ∈ Finset.Icc w (5 * N / 6), kashaevProd N k
      ≤ kashaevProd N (5 * N / 6)
        * (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2) := by
    rw [sum_kashaevProd_Icc_eq hwk]
    exact sum_kashaevProd_left_window_le hN (5 * N / 6 - w + 1) (by omega) (by omega)
  have hright : ∑ k ∈ Finset.Ico (5 * N / 6 + 1) N, kashaevProd N k
      ≤ kashaevProd N (5 * N / 6)
        * (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2) := by
    refine le_trans ?_ (sum_kashaevProd_right_le hN)
    refine Finset.sum_le_sum_of_subset_of_nonneg ?_ (fun k _ _ => kashaevProd_nonneg N k)
    intro k hk
    rw [Finset.mem_Ico] at hk ⊢
    omega
  linarith

/-- **The whole sum, from below.**  `⟨4₁⟩_N ≥ e^{−1}·m·g_{k*}` whenever
`√3·π·m² ≤ N`; taking `m ≈ √(N/(√3π))` makes that `≥ c√N·g_{k*}`.

Nearly free once `sum_kashaevProd_Icc_eq` exists: the window sum is a sub-sum of
the whole sum and every term is nonnegative.  Unlike the upper bound, this needs
NO region decomposition — dropping terms only helps. -/
theorem le_sum_kashaevProd {N m : ℕ} (hN : 6 ≤ N) (hm : m ≤ 5 * N / 6)
    (hsq : Real.sqrt 3 * π * (m : ℝ) ^ 2 ≤ N) :
    kashaevProd N (5 * N / 6) * ((m : ℝ) * Real.exp (-1))
      ≤ ∑ k ∈ Finset.range N, kashaevProd N k := by
  have hks : 5 * N / 6 < N := by
    rw [Nat.div_lt_iff_lt_mul (by norm_num)]; omega
  refine le_trans (le_sum_kashaevProd_left_of_sq hN hm hsq) ?_
  rcases Nat.eq_zero_or_pos m with hm0 | hmpos
  · subst hm0
    simpa using Finset.sum_nonneg (fun k _ => kashaevProd_nonneg N k)
  have heq : ∑ d ∈ Finset.range m, kashaevProd N (5 * N / 6 - d)
      = ∑ k ∈ Finset.Icc (5 * N / 6 - m + 1) (5 * N / 6), kashaevProd N k := by
    rw [sum_kashaevProd_Icc_eq (N := N) (w := 5 * N / 6 - m + 1) (by omega)]
    -- `congr 1` here would leave a FINSET equation, which omega cannot touch;
    -- rewrite the range's argument instead
    have hr : 5 * N / 6 - (5 * N / 6 - m + 1) + 1 = m := by omega
    rw [hr]
  rw [heq]
  refine Finset.sum_le_sum_of_subset_of_nonneg ?_
    (fun k _ _ => kashaevProd_nonneg N k)
  intro k hk
  rw [Finset.mem_Icc] at hk
  rw [Finset.mem_range]
  omega

/-! ### The same two statements, phrased for `⟨4₁⟩_N`

`kashaev N` is DEFINITIONALLY `∑ k ∈ Finset.range N, kashaevProd N k`, so these
are the two theorems above with no proof at all — but they are the ones to cite,
because they say "the Kashaev invariant" rather than "a sum". -/

/-- `⟨4₁⟩_N ≥ e^{−1}·m·g_{k*}` when `√3πm² ≤ N`. -/
theorem le_kashaev {N m : ℕ} (hN : 6 ≤ N) (hm : m ≤ 5 * N / 6)
    (hsq : Real.sqrt 3 * π * (m : ℝ) ^ 2 ≤ N) :
    kashaevProd N (5 * N / 6) * ((m : ℝ) * Real.exp (-1)) ≤ kashaev N :=
  le_sum_kashaevProd hN hm hsq

/-- `⟨4₁⟩_N` bounded above by the three regions. -/
theorem kashaev_le_split {N w : ℕ} (hN : 6 ≤ N) (hw1 : 6 * w ≤ 5 * N)
    (hw2 : 2 * N + 3 ≤ 3 * w) (hwk : w ≤ 5 * N / 6) :
    kashaev N
      ≤ (w : ℝ) * max 1 (kashaevProd N w)
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2) :=
  sum_kashaevProd_le_split hN hw1 hw2 hwk

/-! ## Part 10 — collapsing the below-window region against the peak

`sum_kashaevProd_below_window_le` bounds that region by `w·max 1 g_w`, which is
`O(N)` times an ENDPOINT value.  Two facts turn it into `O(1)` times the PEAK:

  * `N² ≤ g_{k*}` (`sq_le_kashaevProd_argmax`), so the `1` costs `g_{k*}/N²`;
  * `g_w ≤ g_{k*}·e^{−x}` with `x = πD(D−1)/(√3N)`, `D = k*−w`
    (`kashaevProd_left_tail`), and `e^{−x} ≤ 1/x`.

`e^{−x} ≤ 1/x` rather than a threshold on `N` is deliberate: it is `x ≤ e^x`,
one line from `Real.add_one_le_exp`, and it keeps the statement free of any
"for `N` large enough". -/

/-- `e^{−x} ≤ 1/x` for `x > 0` — from `x + 1 ≤ e^x`. -/
theorem exp_neg_le_one_div {x : ℝ} (hx : 0 < x) : Real.exp (-x) ≤ 1 / x := by
  rw [Real.exp_neg, ← one_div]
  exact one_div_le_one_div_of_le hx (by linarith [Real.add_one_le_exp x])

/-- The endpoint value that dominates the below-window region, against the
peak: `max 1 g_w ≤ g_{k*}·(1/N² + √3N/(πD(D−1)))`, `D = k*−w`. -/
theorem max_one_kashaevProd_le {N w : ℕ} (hN : 6 ≤ N)
    (hw1 : 6 * w ≤ 5 * N) (hw2 : 2 * N ≤ 3 * w) (hwk : w ≤ 5 * N / 6)
    (hD : 2 ≤ 5 * N / 6 - w) :
    max 1 (kashaevProd N w)
      ≤ kashaevProd N (5 * N / 6) / (N : ℝ) ^ 2
        + kashaevProd N (5 * N / 6)
          * (Real.sqrt 3 * (N : ℝ)
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
  have hN0 : N ≠ 0 := by omega
  have hpi := Real.pi_pos
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN0
  have hs3 : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hbk : 6 * (5 * N / 6) ≤ 5 * N := by
    have hd := Nat.div_add_mod (5 * N) 6
    omega
  have hDR : (2 : ℝ) ≤ ((5 * N / 6 - w : ℕ) : ℝ) := by exact_mod_cast hD
  have hxpos : (0 : ℝ) < π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)
      / (Real.sqrt 3 * (N : ℝ)) := by
    have h1 : (0 : ℝ) < ((5 * N / 6 - w : ℕ) : ℝ) := by linarith
    have h2 : (0 : ℝ) < ((5 * N / 6 - w : ℕ) : ℝ) - 1 := by linarith
    positivity
  have hgw : kashaevProd N w
      ≤ kashaevProd N (5 * N / 6)
        * Real.exp (-(π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)
            / (Real.sqrt 3 * (N : ℝ)))) := by
    have h := kashaevProd_left_tail (N := N) (b := 5 * N / 6) hN0 hbk
      (5 * N / 6 - w) (by omega) (by omega)
    rwa [show 5 * N / 6 - (5 * N / 6 - w) = w from by omega] at h
  have hgw' : kashaevProd N w
      ≤ kashaevProd N (5 * N / 6)
        * (Real.sqrt 3 * (N : ℝ)
           / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
    refine le_trans hgw (mul_le_mul_of_nonneg_left ?_ (kashaevProd_nonneg N _))
    refine le_trans (exp_neg_le_one_div hxpos) (le_of_eq ?_)
    field_simp
  have hone : (1 : ℝ) ≤ kashaevProd N (5 * N / 6) / (N : ℝ) ^ 2 := by
    rw [le_div_iff₀ (by positivity)]
    simpa using sq_le_kashaevProd_argmax hN
  have hsecond : (0 : ℝ) ≤ kashaevProd N (5 * N / 6)
      * (Real.sqrt 3 * (N : ℝ)
         / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
    have h1 : (0 : ℝ) < ((5 * N / 6 - w : ℕ) : ℝ) := by linarith
    have h2 : (0 : ℝ) < ((5 * N / 6 - w : ℕ) : ℝ) - 1 := by linarith
    have h3 : (0 : ℝ) ≤ Real.sqrt 3 * (N : ℝ)
        / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)) := by
      positivity
    exact mul_nonneg (kashaevProd_nonneg N _) h3
  have hfirst : (0 : ℝ) ≤ kashaevProd N (5 * N / 6) / (N : ℝ) ^ 2 := by
    have := kashaevProd_nonneg N (5 * N / 6)
    positivity
  refine max_le ?_ ?_
  · linarith [hone, hsecond]
  · linarith [hgw', hfirst]

/-- **The below-window region, against the peak.**  Everything below the secant
window costs at most `g_{k*}·(w/N² + w√3N/(πD(D−1)))`, `D = k*−w`.

Both summands are `O(1)`: `w ≤ N` makes the first `≤ 1/N`, and `D ≈ N/6` makes
the second `≈ 36√3/π ≈ 20`.  Stated with `D` explicit rather than collapsed to a
numeral, so no threshold on `N` is smuggled in. -/
theorem sum_kashaevProd_below_window_le_argmax {N w : ℕ} (hN : 6 ≤ N)
    (hw1 : 6 * w ≤ 5 * N) (hw2 : 2 * N ≤ 3 * w) (hwk : w ≤ 5 * N / 6)
    (hD : 2 ≤ 5 * N / 6 - w) :
    ∑ k ∈ Finset.range w, kashaevProd N k
      ≤ kashaevProd N (5 * N / 6)
        * ((w : ℝ) / (N : ℝ) ^ 2
           + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
  have hN0 : N ≠ 0 := by omega
  have hwR : (0 : ℝ) ≤ (w : ℝ) := Nat.cast_nonneg w
  have hmax := max_one_kashaevProd_le hN hw1 hw2 hwk hD
  refine le_trans (sum_kashaevProd_below_window_le hN0 hw1) ?_
  calc (w : ℝ) * max 1 (kashaevProd N w)
      ≤ (w : ℝ) * (kashaevProd N (5 * N / 6) / (N : ℝ) ^ 2
          + kashaevProd N (5 * N / 6)
            * (Real.sqrt 3 * (N : ℝ)
               / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)))) :=
        mul_le_mul_of_nonneg_left hmax hwR
    _ = kashaevProd N (5 * N / 6)
        * ((w : ℝ) / (N : ℝ) ^ 2
           + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
        ring

/-! ## Part 11 — `⟨4₁⟩_N` against its own largest term, both sides -/

/-- **`⟨4₁⟩_N ≤ g_{k*}·C(N,w)`**, with `C` an explicit expression and no
threshold on `N`.

Every summand of `C` is `O(√N)` or better: `w/N² ≤ 1/N`; the `D`-term is
`≈ 36√3/π ≈ 20` at `D ≈ N/6`; the two window terms are the `√N`.  Collapsing
`C` to a single numeral needs `√3 ≤ 1.8`, `π ≥ 3.14` and a threshold — which is
exactly what this statement avoids, at the cost of being longer to read. -/
theorem kashaev_le_argmax_mul {N w : ℕ} (hN : 6 ≤ N) (hw1 : 6 * w ≤ 5 * N)
    (hw2 : 2 * N + 3 ≤ 3 * w) (hwk : w ≤ 5 * N / 6) (hD : 2 ≤ 5 * N / 6 - w) :
    kashaev N
      ≤ kashaevProd N (5 * N / 6)
        * ((w : ℝ) / (N : ℝ) ^ 2
           + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))
           + (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
           + (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2)) := by
  have hwR : (0 : ℝ) ≤ (w : ℝ) := Nat.cast_nonneg w
  have hmax := max_one_kashaevProd_le hN hw1 (by omega) hwk hD
  have hbelow : (w : ℝ) * max 1 (kashaevProd N w)
      ≤ kashaevProd N (5 * N / 6)
        * ((w : ℝ) / (N : ℝ) ^ 2
           + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))) := by
    calc (w : ℝ) * max 1 (kashaevProd N w)
        ≤ (w : ℝ) * (kashaevProd N (5 * N / 6) / (N : ℝ) ^ 2
            + kashaevProd N (5 * N / 6)
              * (Real.sqrt 3 * (N : ℝ)
                 / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)))) :=
          mul_le_mul_of_nonneg_left hmax hwR
      _ = _ := by ring
  refine le_trans (kashaev_le_split hN hw1 hw2 hwk) ?_
  have hring : kashaevProd N (5 * N / 6)
        * ((w : ℝ) / (N : ℝ) ^ 2
           + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
             / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1))
           + (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
           + (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2))
      = kashaevProd N (5 * N / 6)
          * ((w : ℝ) / (N : ℝ) ^ 2
             + (w : ℝ) * (Real.sqrt 3 * (N : ℝ))
               / (π * ((5 * N / 6 - w : ℕ) : ℝ) * (((5 * N / 6 - w : ℕ) : ℝ) - 1)))
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt (Real.sqrt 3 * (N : ℝ)) / 2)
        + kashaevProd N (5 * N / 6) * (2 + Real.sqrt ((N : ℝ) / Real.sqrt 3) / 2) := by
    ring
  rw [hring]
  linarith [hbelow]

end QOU.Knot.FigureEightVolume
