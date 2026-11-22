/-
  THE RATIO `g_{k+d}/g_k` AGAINST A GAUSSIAN — gap (B), second half.

  Step 8 (`GaussianThetaBound`) says a Gaussian sum equals its integral with an
  exponentially small error.  To use that on `⟨4₁⟩_N = ∑_k g_k` one first has to
  know that the summand IS a Gaussian, and that is what this file starts.

  Step 5's tail bounds are one-sided: `g_{k*+d} ≤ g_{k*}e^{−√3πd(d−1)/N}` and a
  matching lower bound with a different constant.  They confine the sum to a
  `√N` window and are lossy in the constant by construction — a tangent line
  and a secant line are not the same line.

  Step 6 is a far better tool for this, and it is what the file uses:
  `log_kashaevProd_asymptotic` pins `log g_k` to `O(1/N²)` UNIFORMLY, so the
  difference of two of them pins the ratio to `O(1/N²)` as well, with no
  one-sidedness anywhere.  Taylor-expanding `Λ` about `θ_k` then produces the
  Gaussian:

      log(g_{k'}/g_k) = 2u·log(2 sin θ_k) + (πu²/N)·cot θ_k
                        + [log(2N sin θ_{k'}) − log(2N sin θ_k)]
                        + (π/6N)[cot θ_{k'} − cot θ_k]
                        + O(1/N²) + O(M|u|³/N²),        u = k' − k.

  The quadratic term `(πu²/N)cot θ_k` is the Gaussian: at the saddle
  `cot θ* = −√3`, so `a = √3π/N` — exactly the `a` whose `√(π/a) = √N·3^{−1/4}`
  step 8 evaluates.  **The `3` in `c_σ = 3^{−1/4}` is `Λ″(5π/6)` and nothing
  else.**

  The LINEAR term `2u·log(2 sin θ_k)` does not vanish.  It vanishes only at
  exactly `θ_k = 5π/6`, and `⌊5N/6⌋` misses that by up to `5π/6N`; the term is
  therefore `O(u/N)`, a tilt of the Gaussian rather than a perturbation of it.
  That is not an error to be bounded away — it is a genuine shift of the
  summation centre, and `hasSum_gaussian_theta_tilt` is the reason it costs
  nothing in the end.

  -- Ref: [leitner2026] QOU/Knot/KashaevPeakValue.lean
  -- Ref: [leitner2026] QOU/Knot/LobTaylorSaddle.lean
  -- Ref: [leitner2026] QOU/MathlibExt/GaussianThetaBound.lean
-/
import QOU.Knot.KashaevPeakValue

namespace QOU.Knot.FigureEightVolume

open Real QOU.Archimedean

/-- The error bound of `log_kashaevProd_asymptotic`, named. -/
noncomputable def logKashaevErr (N k : ℕ) : ℝ :=
  2 * (1 / (144 * (k : ℝ) ^ 2) + 7 / 12 * (π / (N : ℝ)) ^ 2
       + (π / (N : ℝ)) ^ 2 / (12 * Real.sin ((k : ℝ) * π / N) ^ 2))

/-- The main term of `log_kashaevProd_asymptotic`, named. -/
noncomputable def logKashaevMain (N k : ℕ) : ℝ :=
  -(2 * (N : ℝ) / π) * Lob ((k : ℝ) * π / N)
  + Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N))
  + (π / (6 * (N : ℝ))) * (Real.cos ((k : ℝ) * π / N)
                           / Real.sin ((k : ℝ) * π / N))

/-- `log_kashaevProd_asymptotic`, in the named form. -/
theorem abs_log_kashaevProd_sub_main_le {N k : ℕ} (hk : 1 ≤ k) (hkN : k < N)
    (hN : 4 ≤ N) :
    |Real.log (kashaevProd N k) - logKashaevMain N k| ≤ logKashaevErr N k :=
  log_kashaevProd_asymptotic hk hkN hN

/-- **The ratio, to `O(1/N²)`.**  Nothing but the triangle inequality applied
to two instances of step 6 — but note what it buys: the bound on the RATIO is
two-sided and uniform, which no tail bound in `KashaevTailBound` is. -/
theorem abs_log_kashaevProd_ratio_le {N k k' : ℕ} (hk : 1 ≤ k) (hkN : k < N)
    (hk' : 1 ≤ k') (hk'N : k' < N) (hN : 4 ≤ N) :
    |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (logKashaevMain N k' - logKashaevMain N k)|
      ≤ logKashaevErr N k + logKashaevErr N k' := by
  have h1 := abs_log_kashaevProd_sub_main_le hk hkN hN
  have h2 := abs_log_kashaevProd_sub_main_le hk' hk'N hN
  have htri : ∀ x y : ℝ, |x - y| ≤ |x| + |y| := fun x y => by
    simpa [sub_eq_add_neg, abs_neg] using abs_add_le x (-y)
  have hrw : (Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (logKashaevMain N k' - logKashaevMain N k)
      = (Real.log (kashaevProd N k') - logKashaevMain N k')
        - (Real.log (kashaevProd N k) - logKashaevMain N k) := by ring
  rw [hrw]
  linarith [htri (Real.log (kashaevProd N k') - logKashaevMain N k')
    (Real.log (kashaevProd N k) - logKashaevMain N k)]

/-- **The Gaussian appears.**  Taylor-expanding `Λ` about `θ_k` turns the
main-term difference into `linear + quadratic`, with the cubic remainder paid
for by `M`, any bound on `1/sin²` between the two angles.

`u = k' − k` is a real number, not a natural: `k'` may sit on either side of
`k`, and the statement is the same in both directions.

The quadratic coefficient `π·cot θ_k/N` is the `a` of a Gaussian `e^{−a u²}`
once `cot θ_k < 0` — which holds throughout `(π/2, π)`, where the saddle
lives. -/
theorem abs_log_kashaevProd_ratio_taylor {N k k' : ℕ} (hk : 1 ≤ k) (hkN : k < N)
    (hk' : 1 ≤ k') (hk'N : k' < N) (hN : 4 ≤ N) {M : ℝ}
    (hmem : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N), 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        1 / Real.sin x ^ 2 ≤ M) :
    |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
           + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
             * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
           + (Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
              - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N)))
           + (π / (6 * (N : ℝ)))
             * (Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
                - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)))|
      ≤ logKashaevErr N k + logKashaevErr N k'
        + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| ^ 3 / (3 * (N : ℝ) ^ 2) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hNne : (N : ℝ) ≠ 0 := ne_of_gt hNpos
  have hpine : π ≠ 0 := ne_of_gt hpi
  have h1 := abs_log_kashaevProd_ratio_le hk hkN hk' hk'N hN
  have h2 := abs_Lob_taylor_two hmem hM
  -- `M ≥ 0`, needed for the cubic bound to be usable
  have hMnn : 0 ≤ M := by
    have hmem0 : ((k : ℝ) * π / N) ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N) :=
      Set.left_mem_uIcc
    have hx := (hmem _ hmem0).1
    have hxπ := (hmem _ hmem0).2
    have hspos : 0 < Real.sin ((k : ℝ) * π / N) :=
      Real.sin_pos_of_pos_of_lt_pi hx hxπ
    have := hM _ hmem0
    have hq : 0 < 1 / Real.sin ((k : ℝ) * π / N) ^ 2 := by positivity
    linarith
  -- the offset in angle is `u·π/N`
  have habs : |(k' : ℝ) * π / N - (k : ℝ) * π / N|
      = |(k' : ℝ) - (k : ℝ)| * (π / N) := by
    rw [show (k' : ℝ) * π / N - (k : ℝ) * π / N = ((k' : ℝ) - (k : ℝ)) * (π / N) by
      ring, abs_mul, abs_of_pos (by positivity : (0 : ℝ) < π / N)]
  rw [habs] at h2
  -- The remainder `R`, written exactly as `abs_Lob_taylor_two` produces it so
  -- that `h2` applies to it verbatim.  No `set` here: `unfold logKashaevMain`
  -- below regenerates raw terms, and a `set` variable and its own body are
  -- distinct atoms to `ring`.
  have hkey : (Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
           + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
             * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
           + (Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
              - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N)))
           + (π / (6 * (N : ℝ)))
             * (Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
                - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)))
      = ((Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
          - (logKashaevMain N k' - logKashaevMain N k))
        + (-(2 * (N : ℝ) / π))
          * (Lob ((k' : ℝ) * π / N)
             - (Lob ((k : ℝ) * π / N)
                - Real.log (2 * Real.sin ((k : ℝ) * π / N))
                  * ((k' : ℝ) * π / N - (k : ℝ) * π / N)
                - (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
                  * (((k' : ℝ) * π / N - (k : ℝ) * π / N) ^ 2 / 2))) := by
    unfold logKashaevMain
    field_simp
    ring
  rw [hkey]
  refine le_trans (abs_add_le _ _) ?_
  have hR : |(-(2 * (N : ℝ) / π))
        * (Lob ((k' : ℝ) * π / N)
           - (Lob ((k : ℝ) * π / N)
              - Real.log (2 * Real.sin ((k : ℝ) * π / N))
                * ((k' : ℝ) * π / N - (k : ℝ) * π / N)
              - (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
                * (((k' : ℝ) * π / N - (k : ℝ) * π / N) ^ 2 / 2)))|
      ≤ M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| ^ 3 / (3 * (N : ℝ) ^ 2) := by
    rw [abs_mul, abs_neg, abs_of_pos (by positivity : (0 : ℝ) < 2 * (N : ℝ) / π)]
    refine le_trans (mul_le_mul_of_nonneg_left h2
      (by positivity : (0 : ℝ) ≤ 2 * (N : ℝ) / π)) (le_of_eq ?_)
    field_simp
    ring
  linarith

/-! ## Absorbing the two non-Gaussian terms

`abs_log_kashaevProd_ratio_taylor` leaves two pieces that are not part of the
Gaussian: the variation of `log(2N sin θ)` and of `cot θ` across the window.
Both are `O(u/N)` and `O(u/N²)` respectively, so both vanish on `|u| ≲ √N` —
but they have to be bounded, not waved at, and the bound is a mean-value
estimate on each.

`K` bounds `|cot|` and `M` bounds `1/sin²`; they are not independent
(`cot² ≤ 1/sin²`, so `K ≤ √M` always works) but keeping them separate avoids
dragging a square root through the arithmetic for no gain. -/

/-- Mean value on `log(2 sin ·)`, whose derivative is `cot`. -/
theorem abs_log_two_sin_sub_le {a b K : ℝ}
    (hmem : ∀ x ∈ Set.uIcc a b, 0 < x ∧ x < π)
    (hK : ∀ x ∈ Set.uIcc a b, |Real.cos x / Real.sin x| ≤ K) :
    |Real.log (2 * Real.sin b) - Real.log (2 * Real.sin a)| ≤ K * |b - a| := by
  have hderiv : ∀ x ∈ Set.uIcc a b,
      HasDerivWithinAt (fun y => Real.log (2 * Real.sin y))
        (Real.cos x / Real.sin x) (Set.uIcc a b) x := by
    intro x hx
    exact (QOU.MathlibExt.hasDerivAt_log_two_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi (hmem x hx).1
        (hmem x hx).2))).hasDerivWithinAt
  have hbound : ∀ x ∈ Set.uIcc a b, ‖Real.cos x / Real.sin x‖ ≤ K := by
    intro x hx; rw [Real.norm_eq_abs]; exact hK x hx
  have h := (convex_uIcc a b).norm_image_sub_le_of_norm_hasDerivWithin_le
    hderiv hbound Set.left_mem_uIcc Set.right_mem_uIcc
  simpa [Real.norm_eq_abs] using h

/-- Mean value on `cot`, whose derivative is `−1/sin²`. -/
theorem abs_cot_sub_le {a b M : ℝ}
    (hmem : ∀ x ∈ Set.uIcc a b, 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.uIcc a b, 1 / Real.sin x ^ 2 ≤ M) :
    |Real.cos b / Real.sin b - Real.cos a / Real.sin a| ≤ M * |b - a| := by
  have hderiv : ∀ x ∈ Set.uIcc a b,
      HasDerivWithinAt (fun y => Real.cos y / Real.sin y)
        (-(1 / Real.sin x ^ 2)) (Set.uIcc a b) x := by
    intro x hx
    exact (QOU.MathlibExt.hasDerivAt_cos_div_sin
      (ne_of_gt (Real.sin_pos_of_pos_of_lt_pi (hmem x hx).1
        (hmem x hx).2))).hasDerivWithinAt
  have hbound : ∀ x ∈ Set.uIcc a b, ‖-(1 / Real.sin x ^ 2)‖ ≤ M := by
    intro x hx
    have hs : 0 < Real.sin x :=
      Real.sin_pos_of_pos_of_lt_pi (hmem x hx).1 (hmem x hx).2
    have hpos : (0 : ℝ) < 1 / Real.sin x ^ 2 := by positivity
    rw [Real.norm_eq_abs, abs_neg, abs_of_pos hpos]
    exact hM x hx
  have h := (convex_uIcc a b).norm_image_sub_le_of_norm_hasDerivWithin_le
    hderiv hbound Set.left_mem_uIcc Set.right_mem_uIcc
  simpa [Real.norm_eq_abs] using h

/-- **The ratio IS a tilted Gaussian.**  Everything but `2u·log(2 sin θ_k)`
(the tilt) and `(πu²/N)·cot θ_k` (the Gaussian) is bounded by terms that vanish
on `|u| ≲ √N`.

This is the statement the Laplace step needs: `g_{k'}/g_k` is
`e^{tilt + quadratic}` times `1 + o(1)`, with the `o(1)` uniform over the
window.  Compare `KashaevTailBound`, where the corresponding statements are
one-sided and carry different constants on the two sides — those can prove
`Θ(√N)` and cannot produce `c_σ`. -/
theorem abs_log_kashaevProd_ratio_gaussian {N k k' : ℕ} (hk : 1 ≤ k)
    (hkN : k < N) (hk' : 1 ≤ k') (hk'N : k' < N) (hN : 4 ≤ N) {M K : ℝ}
    (hmem : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N), 0 < x ∧ x < π)
    (hM : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        1 / Real.sin x ^ 2 ≤ M)
    (hK : ∀ x ∈ Set.uIcc ((k : ℝ) * π / N) ((k' : ℝ) * π / N),
        |Real.cos x / Real.sin x| ≤ K) :
    |(Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
           + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
             * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)))|
      ≤ logKashaevErr N k + logKashaevErr N k'
        + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| ^ 3 / (3 * (N : ℝ) ^ 2)
        + K * π * |(k' : ℝ) - (k : ℝ)| / (N : ℝ)
        + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| / (6 * (N : ℝ) ^ 2) := by
  have hpi := Real.pi_pos
  have hNpos : (0 : ℝ) < N := by
    have : 0 < N := by omega
    exact_mod_cast this
  have hbase := abs_log_kashaevProd_ratio_taylor hk hkN hk' hk'N hN hmem hM
  -- the angle offset
  have hoff : |(k' : ℝ) * π / N - (k : ℝ) * π / N|
      = |(k' : ℝ) - (k : ℝ)| * (π / N) := by
    rw [show (k' : ℝ) * π / N - (k : ℝ) * π / N = ((k' : ℝ) - (k : ℝ)) * (π / N) by
      ring, abs_mul, abs_of_pos (by positivity : (0 : ℝ) < π / N)]
  -- the `N` in `log(2N sin θ)` cancels out of the difference
  have hsk : 0 < Real.sin ((k : ℝ) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi (hmem _ Set.left_mem_uIcc).1
      (hmem _ Set.left_mem_uIcc).2
  have hsk' : 0 < Real.sin ((k' : ℝ) * π / N) :=
    Real.sin_pos_of_pos_of_lt_pi (hmem _ Set.right_mem_uIcc).1
      (hmem _ Set.right_mem_uIcc).2
  have hNsplit : Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
        - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N))
      = Real.log (2 * Real.sin ((k' : ℝ) * π / N))
        - Real.log (2 * Real.sin ((k : ℝ) * π / N)) := by
    rw [show (2 : ℝ) * (N : ℝ) * Real.sin ((k' : ℝ) * π / N)
        = (N : ℝ) * (2 * Real.sin ((k' : ℝ) * π / N)) by ring,
      show (2 : ℝ) * (N : ℝ) * Real.sin ((k : ℝ) * π / N)
        = (N : ℝ) * (2 * Real.sin ((k : ℝ) * π / N)) by ring,
      Real.log_mul (ne_of_gt hNpos) (by positivity),
      Real.log_mul (ne_of_gt hNpos) (by positivity)]
    ring
  -- the two mean-value bounds
  have hlog := abs_log_two_sin_sub_le (a := (k : ℝ) * π / N)
    (b := (k' : ℝ) * π / N) (K := K) hmem hK
  have hcot := abs_cot_sub_le (a := (k : ℝ) * π / N)
    (b := (k' : ℝ) * π / N) (M := M) hmem hM
  rw [hoff] at hlog hcot
  -- assemble
  have hMnn : 0 ≤ M := by
    have hpos : (0 : ℝ) < 1 / Real.sin ((k : ℝ) * π / N) ^ 2 := by positivity
    linarith [hM _ Set.left_mem_uIcc]
  have htri : ∀ x y : ℝ, |x - y| ≤ |x| + |y| := fun x y => by
    simpa [sub_eq_add_neg, abs_neg] using abs_add_le x (-y)
  have hextra : |(Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
        - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N)))
        + (π / (6 * (N : ℝ)))
          * (Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
             - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))|
      ≤ K * π * |(k' : ℝ) - (k : ℝ)| / (N : ℝ)
        + M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| / (6 * (N : ℝ) ^ 2) := by
    refine le_trans (abs_add_le _ _) ?_
    rw [hNsplit, abs_mul, abs_of_pos (by positivity : (0 : ℝ) < π / (6 * (N : ℝ)))]
    have h2 : (π / (6 * (N : ℝ)))
        * |Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
           - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)|
        ≤ M * π ^ 2 * |(k' : ℝ) - (k : ℝ)| / (6 * (N : ℝ) ^ 2) := by
      refine le_trans (mul_le_mul_of_nonneg_left hcot (by positivity)) (le_of_eq ?_)
      field_simp
    have h1 : |Real.log (2 * Real.sin ((k' : ℝ) * π / N))
        - Real.log (2 * Real.sin ((k : ℝ) * π / N))|
        ≤ K * π * |(k' : ℝ) - (k : ℝ)| / (N : ℝ) := by
      refine le_trans hlog (le_of_eq ?_)
      field_simp
    linarith
  have hsp : (Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
        - (2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
           + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
             * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N)))
      = ((Real.log (kashaevProd N k') - Real.log (kashaevProd N k))
          - (2 * ((k' : ℝ) - (k : ℝ)) * Real.log (2 * Real.sin ((k : ℝ) * π / N))
             + (π * ((k' : ℝ) - (k : ℝ)) ^ 2 / (N : ℝ))
               * (Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))
             + (Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
                - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N)))
             + (π / (6 * (N : ℝ)))
               * (Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
                  - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))))
        + ((Real.log (2 * (N : ℝ) * Real.sin ((k' : ℝ) * π / N))
            - Real.log (2 * (N : ℝ) * Real.sin ((k : ℝ) * π / N)))
           + (π / (6 * (N : ℝ)))
             * (Real.cos ((k' : ℝ) * π / N) / Real.sin ((k' : ℝ) * π / N)
                - Real.cos ((k : ℝ) * π / N) / Real.sin ((k : ℝ) * π / N))) := by
    ring
  rw [hsp]
  refine le_trans (abs_add_le _ _) ?_
  linarith

end QOU.Knot.FigureEightVolume
