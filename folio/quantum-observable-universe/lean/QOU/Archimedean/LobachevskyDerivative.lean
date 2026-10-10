/-
  The Lobachevsky derivative bridge: `Λ' = −log(2 sin t)` and `Λ'' = −cot t`
  (bean `qou-idvt`, tier T1-remainder).

  WHAT WAS ACTUALLY MISSING.  `qou-idvt` scoped T1 as "build the Lobachevsky
  function `Λ` on top of the existing `Cl₂`".  Most of that already exists and
  the bean's note that the corpus has "no Lobachevsky function" is stale:

    * `QOU.Archimedean.Lob t = Cl_2 (2*t) / 2`         (BlochWignerLobachevsky)
    * `Lob_neg`, `Lob_zero`, `Lob_pi_div_two`, `Lob_pi`          (same file)
    * `QOU.Knot.hasDerivAt_Cl_2_series` — `Cl₂'(θ) = −log(2 sin(θ/2))` on
      `(0, 2π)`, sorry-free                                     (Knot/Clausen)

  What genuinely did not exist is the DERIVATIVE OF `Λ` ITSELF, and its second
  derivative.  That is this file, and it is a chain rule away from the above —
  `Λ(t) = Cl₂(2t)/2` differentiates to `Λ'(t) = Cl₂'(2t) = −log(2 sin t)`, the
  factor 2 from the chain rule cancelling the 1/2 in the definition.  This is
  what makes `Λ` the primitive `Λ(x) = −∫₀ˣ log|2 sin t| dt` that the bean's T1
  asks for, rather than merely a rescaled `Cl₂`.

  WHY IT IS THE PIECE WORTH HAVING.  `QOU/Archimedean/IdealTetrahedronConcavity`
  proves the ideal-tetrahedron Hessian is negative definite (T3-core), but it
  does so for a Hessian whose entries are WRITTEN IN `cot` — the identification
  `Λ'' = −cot` lives only in that file's docstring, as prose.  `Lob_second_deriv`
  below turns that prose into a theorem, so the concavity work is about `Λ` and
  not about an unnamed function that happens to have those second derivatives.

  WHAT THIS DOES NOT DO.  It does not close `qou-krvm` (iv).  Still open, and
  unchanged by this file:

    * T2 — `Vol(α,β,γ) = Λ(α) + Λ(β) + Λ(γ)` as the ideal-tetrahedron volume.
      That is a GEOMETRIC identification (that this sum is the hyperbolic volume
      of the simplex), not an analytic one; nothing here supplies it.
    * T3-plumbing — "Hessian negative definite ⇒ strictly concave" needs
      Mathlib's `C²` second-derivative-test machinery.

  So this file is a link in the chain, not the chain.  Per the bean's GUARD, no
  concavity claim is axiomatised here: what is not proved is left absent, not
  assumed.

  Domain note: `(0, π)` throughout, which is where an ideal-tetrahedron dihedral
  angle lives (`AngleTriple.hα` etc. give exactly `0 < α` and `α < π`), and
  exactly where `sin t > 0` makes `log (2 sin t)` real and `cot t` finite.

  Archimedean (ℝ): logs, `sin`, ordering — §7c.

  -- Ref: [thurston1978] Ch. 7 (Λ and the ideal-simplex volume)
  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
-/

import Mathlib.Tactic
import QOU.Archimedean.BlochWignerLobachevsky
import QOU.Knot.Clausen

namespace QOU.Archimedean

open Real

/-- **`Λ'(t) = −log(2 sin t)` on `(0, π)`.**

The chain rule through `Λ(t) = Cl₂(2t)/2`: the inner derivative `2` cancels the
outer `1/2`, and `Cl₂'(2t) = −log(2 sin(2t/2)) = −log(2 sin t)`.

This is the statement that `Λ` is the primitive `Λ(x) = −∫₀ˣ log|2 sin t| dt` in
the standard normalisation — the form in which the Lobachevsky function is
usually defined, recovered here from the `Cl₂` series rather than assumed. -/
theorem hasDerivAt_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt Lob (-Real.log (2 * Real.sin t)) t := by
  have h2t0 : 0 < 2 * t := by linarith
  have h2tπ : 2 * t < 2 * π := by linarith
  have hCl : HasDerivAt Cl_2 (-Real.log (2 * Real.sin (2 * t / 2))) (2 * t) :=
    QOU.Knot.hasDerivAt_Cl_2_series h2t0 h2tπ
  rw [show 2 * t / 2 = t by ring] at hCl
  have hinner : HasDerivAt (fun s : ℝ => 2 * s) 2 t := by
    simpa using (hasDerivAt_id t).const_mul (2 : ℝ)
  have hcomp : HasDerivAt (fun s : ℝ => Cl_2 (2 * s))
      (-Real.log (2 * Real.sin t) * 2) t := hCl.comp t hinner
  have hdiv := hcomp.div_const 2
  have hval : (-Real.log (2 * Real.sin t) * 2) / 2 = -Real.log (2 * Real.sin t) := by
    ring
  rw [hval] at hdiv
  exact hdiv

/-- `Λ` is differentiable on `(0, π)`. -/
theorem differentiableAt_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    DifferentiableAt ℝ Lob t :=
  (hasDerivAt_Lob h0 hπ).differentiableAt

/-- `deriv Λ t = −log(2 sin t)` on `(0, π)`, the `deriv`-form of
`hasDerivAt_Lob`. -/
theorem deriv_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    deriv Lob t = -Real.log (2 * Real.sin t) :=
  (hasDerivAt_Lob h0 hπ).deriv

/-- **`(−log(2 sin ·))' = −cot`.**  The derivative of `Λ'`, stated on its own so
the second-derivative fact is available without unfolding `Λ`.

`d/dt −log(2 sin t) = −(2 cos t)/(2 sin t) = −cos t / sin t`. -/
theorem hasDerivAt_neg_log_two_sin {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt (fun s : ℝ => -Real.log (2 * Real.sin s))
      (-(Real.cos t / Real.sin t)) t := by
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi h0 hπ
  have hne : 2 * Real.sin t ≠ 0 := by positivity
  have hbase : HasDerivAt (fun s : ℝ => 2 * Real.sin s) (2 * Real.cos t) t := by
    simpa using (Real.hasDerivAt_sin t).const_mul (2 : ℝ)
  have hlog := (hbase.log hne).neg
  have hval : -(2 * Real.cos t / (2 * Real.sin t)) = -(Real.cos t / Real.sin t) := by
    field_simp
  rw [hval] at hlog
  exact hlog

/-- **`Λ''(t) = −cot t` on `(0, π)`.**

This is the identity `IdealTetrahedronConcavity` states in prose and uses to
write the ideal-tetrahedron Hessian

    f_αα = −(cot α + cot γ),  f_αβ = −cot γ,  f_ββ = −(cot β + cot γ)

for `f(α,β) = Λ(α) + Λ(β) + Λ(π−α−β)`.  Proving it here is what makes that
Hessian the Hessian **of the Lobachevsky volume sum**, rather than of an
unnamed function with the right second derivatives.

Stated via `EqOn` on the open interval so that `deriv (deriv Lob)` may be
rewritten along it: `deriv Λ` agrees with `−log(2 sin ·)` throughout `(0, π)`,
and differentiating that gives `−cot`. -/
theorem hasDerivAt_deriv_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    HasDerivAt (deriv Lob) (-(Real.cos t / Real.sin t)) t := by
  have hEq : Set.EqOn (deriv Lob) (fun s : ℝ => -Real.log (2 * Real.sin s))
      (Set.Ioo 0 π) := fun s hs => deriv_Lob hs.1 hs.2
  exact (hasDerivAt_neg_log_two_sin h0 hπ).congr_of_eventuallyEq
    (Filter.eventuallyEq_of_mem (isOpen_Ioo.mem_nhds ⟨h0, hπ⟩) hEq)

/-- `Λ''(t) = −cot t`, in `deriv`-of-`deriv` form. -/
theorem deriv_deriv_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) :
    deriv (deriv Lob) t = -(Real.cos t / Real.sin t) :=
  (hasDerivAt_deriv_Lob h0 hπ).deriv

/-- **`Λ` is strictly concave-ish pointwise: `Λ'' < 0` on `(0, π/2)`.**

`−cot t < 0` exactly when `cos t > 0`, i.e. on `(0, π/2)`.  Recorded because it
is the sign that drives the diagonal entries `f_αα = −(cot α + cot γ) < 0`; note
`Λ''` is *positive* on `(π/2, π)`, so `Λ` alone is NOT concave on `(0, π)` —
concavity of the tetrahedron volume comes from the SUM, via
`cot_add_cot_pos`, not from `Λ` termwise.  Stating this guards against the
plausible-but-false reading that `Λ` is concave. -/
theorem deriv_deriv_Lob_neg {t : ℝ} (h0 : 0 < t) (hπ : t < π / 2) :
    deriv (deriv Lob) t < 0 := by
  have hπ' : t < π := by linarith [Real.pi_pos]
  rw [deriv_deriv_Lob h0 hπ']
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi h0 hπ'
  have hc : 0 < Real.cos t := Real.cos_pos_of_mem_Ioo ⟨by linarith [Real.pi_pos], hπ⟩
  have : 0 < Real.cos t / Real.sin t := div_pos hc hs
  linarith

/-- **`Λ'' > 0` on `(π/2, π)`** — the companion to `deriv_deriv_Lob_neg`, making
the non-concavity of `Λ` on `(0, π)` explicit rather than implied. -/
theorem deriv_deriv_Lob_pos {t : ℝ} (h0 : π / 2 < t) (hπ : t < π) :
    0 < deriv (deriv Lob) t := by
  have h0' : 0 < t := by linarith [Real.pi_pos]
  rw [deriv_deriv_Lob h0' hπ]
  have hs : 0 < Real.sin t := Real.sin_pos_of_pos_of_lt_pi h0' hπ
  have hc : Real.cos t < 0 := Real.cos_neg_of_pi_div_two_lt_of_lt h0 (by linarith)
  have : Real.cos t / Real.sin t < 0 := div_neg_of_neg_of_pos hc hs
  linarith

end QOU.Archimedean
