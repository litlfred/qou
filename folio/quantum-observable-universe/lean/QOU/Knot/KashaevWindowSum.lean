/-
  FROM A POINTWISE GAUSSIAN TO A GAUSSIAN SUM.

  Step 10 controls `log(g_{k'}/g_k)` against `tilt + quadratic` with an error
  that is uniform over the window.  This file does the two mechanical steps
  that turn that into a statement about `∑ g_k`:

    1. **Exponentiate.**  `|log(g_{k'}/g_k) − T| ≤ B` becomes
       `g_k·e^{T−B} ≤ g_{k'} ≤ g_k·e^{T+B}`.  Both directions, from one
       hypothesis.

    2. **Sum.**  Over any finite window `s`,
       `∑_{k'∈s} g_{k'} ≤ g_k·e^{B}·∑_{k'∈s} e^{T(k')}`, and the mirror
       lower bound with `e^{−B}`.

  `T` and `B` are left abstract — `T : ℕ → ℝ` any target and `B` any uniform
  error — so this file is independent of which expansion supplies them.  That
  is deliberate: the same lemmas will serve the tilted-Gaussian target of step
  10 and any sharper target that replaces it later.  Nothing here knows about
  `Λ`, the saddle, or `4₁`.

  What is NOT here: evaluating `∑_{k'∈s} e^{T(k')}`.  That is step 8's job
  (`abs_tsum_gaussian_sub_sqrt_le` and the tilted form), and it needs the
  window extended to all of `ℤ` plus a tail bound — which is step 5's job.

  -- Ref: [leitner2026] QOU/Knot/KashaevRatioExpansion.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaBound.lean
-/
import QOU.Knot.KashaevRatioExpansion
import QOU.Knot.FigureEightVolumeSqueeze

namespace QOU.Knot.FigureEightVolume

open Real

/-- `g_{k'} = g_k · e^{log g_{k'} − log g_k}` — the identity the whole file
rests on, and the only place positivity of both terms is used. -/
theorem kashaevProd_eq_mul_exp {N k k' : ℕ} (hkN : k < N) (hk'N : k' < N) :
    kashaevProd N k'
      = kashaevProd N k
        * Real.exp (Real.log (kashaevProd N k') - Real.log (kashaevProd N k)) := by
  have hpos := kashaevProd_pos hkN
  have hpos' := kashaevProd_pos hk'N
  rw [Real.exp_sub, Real.exp_log hpos', Real.exp_log hpos]
  field_simp

/-- **The exponentiated ratio, both directions.**  `T` is any target and `B`
any bound on the discrepancy; the conclusion brackets `g_{k'}` between two
multiples of `g_k`.

Stated with `T` and `B` abstract so that a sharper expansion can be dropped in
without touching this proof. -/
theorem kashaevProd_bounds_of_log_bound {N k k' : ℕ} (hkN : k < N) (hk'N : k' < N)
    {T B : ℝ}
    (hTB : |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k)) - T| ≤ B) :
    kashaevProd N k * Real.exp (T - B) ≤ kashaevProd N k'
      ∧ kashaevProd N k' ≤ kashaevProd N k * Real.exp (T + B) := by
  have hpos := kashaevProd_pos hkN
  have hd := abs_le.mp hTB
  rw [kashaevProd_eq_mul_exp hkN hk'N]
  constructor
  · exact mul_le_mul_of_nonneg_left
      (Real.exp_le_exp.mpr (by linarith [hd.1])) hpos.le
  · exact mul_le_mul_of_nonneg_left
      (Real.exp_le_exp.mpr (by linarith [hd.2])) hpos.le

/-- **The window sum from above.**  `e^{B}` factors out of every term, so the
whole window is `e^{B}` times the model sum. -/
theorem sum_kashaevProd_le_of_log_bound {N k : ℕ} (hkN : k < N) (s : Finset ℕ)
    {T : ℕ → ℝ} {B : ℝ} (hs : ∀ k' ∈ s, k' < N)
    (h : ∀ k' ∈ s,
      |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k)) - T k'| ≤ B) :
    ∑ k' ∈ s, kashaevProd N k'
      ≤ kashaevProd N k * Real.exp B * ∑ k' ∈ s, Real.exp (T k') := by
  have hpos := kashaevProd_pos hkN
  have hterm : ∀ k' ∈ s, kashaevProd N k'
      ≤ kashaevProd N k * Real.exp B * Real.exp (T k') := by
    intro k' hk'
    have hb := (kashaevProd_bounds_of_log_bound hkN (hs k' hk') (h k' hk')).2
    calc kashaevProd N k' ≤ kashaevProd N k * Real.exp (T k' + B) := hb
      _ = kashaevProd N k * Real.exp B * Real.exp (T k') := by
          rw [Real.exp_add]; ring
  calc ∑ k' ∈ s, kashaevProd N k'
      ≤ ∑ k' ∈ s, kashaevProd N k * Real.exp B * Real.exp (T k') :=
        Finset.sum_le_sum hterm
    _ = kashaevProd N k * Real.exp B * ∑ k' ∈ s, Real.exp (T k') :=
        (Finset.mul_sum _ _ _).symm

/-- **The window sum from below**, the mirror. -/
theorem le_sum_kashaevProd_of_log_bound {N k : ℕ} (hkN : k < N) (s : Finset ℕ)
    {T : ℕ → ℝ} {B : ℝ} (hs : ∀ k' ∈ s, k' < N)
    (h : ∀ k' ∈ s,
      |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k)) - T k'| ≤ B) :
    kashaevProd N k * Real.exp (-B) * ∑ k' ∈ s, Real.exp (T k')
      ≤ ∑ k' ∈ s, kashaevProd N k' := by
  have hpos := kashaevProd_pos hkN
  have hterm : ∀ k' ∈ s, kashaevProd N k * Real.exp (-B) * Real.exp (T k')
      ≤ kashaevProd N k' := by
    intro k' hk'
    have hb := (kashaevProd_bounds_of_log_bound hkN (hs k' hk') (h k' hk')).1
    calc kashaevProd N k * Real.exp (-B) * Real.exp (T k')
        = kashaevProd N k * Real.exp (T k' - B) := by
          rw [mul_assoc, ← Real.exp_add, show -B + T k' = T k' - B from by ring]
      _ ≤ kashaevProd N k' := hb
  calc kashaevProd N k * Real.exp (-B) * ∑ k' ∈ s, Real.exp (T k')
      = ∑ k' ∈ s, kashaevProd N k * Real.exp (-B) * Real.exp (T k') :=
        Finset.mul_sum _ _ _
    _ ≤ ∑ k' ∈ s, kashaevProd N k' := Finset.sum_le_sum hterm

/-- **The sandwich, as a ratio.**  The window sum is within `e^{±B}` of the
model — the form the Laplace step consumes, since `e^{B} → 1` exactly when the
expansion's error does.

No sign hypothesis on `B`.  A first draft carried `0 ≤ B`, on the reasoning
that `e^{B} − 1` had better be nonnegative; it is not needed, because the step
the lower half actually rests on is `e^{B} + e^{−B} ≥ 2`, which holds for EVERY
real `B`.  (And a negative `B` forces `s` empty, since `h` would bound an
absolute value below zero — so both sides are `0` and the statement is true
there too.) -/
theorem sum_kashaevProd_window_sandwich {N k : ℕ} (hkN : k < N) (s : Finset ℕ)
    {T : ℕ → ℝ} {B : ℝ} (hs : ∀ k' ∈ s, k' < N)
    (h : ∀ k' ∈ s,
      |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k)) - T k'| ≤ B) :
    |∑ k' ∈ s, kashaevProd N k'
        - kashaevProd N k * ∑ k' ∈ s, Real.exp (T k')|
      ≤ kashaevProd N k * (Real.exp B - 1) * ∑ k' ∈ s, Real.exp (T k') := by
  have hpos := kashaevProd_pos hkN
  have hup := sum_kashaevProd_le_of_log_bound hkN s hs h
  have hlo := le_sum_kashaevProd_of_log_bound hkN s hs h
  have hS : (0 : ℝ) ≤ ∑ k' ∈ s, Real.exp (T k') :=
    Finset.sum_nonneg fun _ _ => (Real.exp_pos _).le
  have hmul : Real.exp (-B) * Real.exp B = 1 := by
    rw [← Real.exp_add]; simp
  -- `e^B + e^{−B} ≥ 2`, which is what makes the LOWER half of the sandwich
  -- weaker than `e^{−B}` and hence implied by it
  have hsum2 : 2 ≤ Real.exp B + Real.exp (-B) := by
    nlinarith [hmul, sq_nonneg (Real.exp B - 1), Real.exp_pos (-B), Real.exp_pos B]
  have hprod : (0 : ℝ)
      ≤ kashaevProd N k * (∑ k' ∈ s, Real.exp (T k'))
        * (Real.exp B + Real.exp (-B) - 2) :=
    mul_nonneg (mul_nonneg hpos.le hS) (by linarith)
  rw [abs_le]
  exact ⟨by nlinarith [hlo, hprod], by nlinarith [hup]⟩

end QOU.Knot.FigureEightVolume
