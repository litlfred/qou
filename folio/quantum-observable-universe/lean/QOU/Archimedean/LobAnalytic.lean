/-
  Λ is real-analytic on `(0, π)` — the obtuse ideal-tetrahedron volume route's
  step-1 CLOSURE (bean `qou-w3eg`, H4-5).

  The acute Milnor Λ-sum is proved; the obtuse case closes by Milnor's
  "analytic continuation" route, whose three steps are

    1. `Λ` real-analytic on `(0, π)`   ← THIS FILE
    2. the base integral real-analytic in the angles `(α, β)`
    3. the identity theorem glues the acute equality onto the whole open simplex.

  Step 1 was previously measured as a Mathlib-gap keystone needing an
  antiderivative-of-analytic theorem Mathlib lacks (bean `qou-w3eg`, step-1a note).
  That measurement was too pessimistic: the corpus's complex-dilogarithm layer
  already carries the harder half of the work, so `Λ` analytic is a COMPOSITION,
  not a primitive construction.  Assembled here from:

    * `QOU.MathlibExt.analyticOnNhd_cLiTwoExt` — `cLiTwoExt` is analytic on the
      open cut-complement `notCut = ℂ ∖ [1,∞)` (holomorphic ⇒ analytic, via
      `DifferentiableOn.analyticOnNhd`).
    * `QOU.Knot.Kummer.exp_mem_notCut` — the punctured unit circle sits in `notCut`.
    * `QOU.Knot.Kummer.im_cLiTwoExt_exp` — `Im cLiTwoExt(e^{iθ}) = Cl₂(θ)` on `(0,2π)`.
    * `Lob t = Cl₂(2t)/2` (`QOU.Archimedean.Lob`).

  So on `(0, π)`, `Λ t = Im cLiTwoExt(e^{2it}) / 2`, and the right-hand side is
  the entire `exp` precomposed with a real-analytic linear map, then the
  ℂ-analytic `cLiTwoExt` restricted to ℝ, then the ℝ-linear `Im` — analytic by
  composition, transported to `Λ` by the identity above (`AnalyticAt.congr`).

  This does NOT close the obtuse case: steps 2 and 3 remain open (`qou-w3eg`).

  Archimedean (ℝ): `Real.pi`, ordering — §7c.

  -- Ref: [milnor1982] https://doi.org/10.1090/S0273-0979-1982-14958-8
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5 obtuse, step 1), qou-idvt
-/
import QOU.Knot.KummerDilogHalf
import QOU.Archimedean.BlochWignerLobachevsky
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

namespace QOU.Archimedean

open Real Set
open QOU.MathlibExt (cLiTwoExt notCut)

/-- **`Λ` is real-analytic at every interior dihedral angle `t ∈ (0, π)`.**
On `(0, π)`, `Λ t = Im cLiTwoExt(e^{2it}) / 2`, and the right-hand side is
analytic as a composition (entire `exp` ∘ real-analytic linear map, then the
ℂ-analytic `cLiTwoExt` on the open `notCut`, then the ℝ-linear `Im`). -/
theorem analyticAt_Lob {t : ℝ} (h0 : 0 < t) (hπ : t < π) : AnalyticAt ℝ Lob t := by
  -- s ↦ (↑(2·s)) * I  is real-analytic
  have hlin : AnalyticAt ℝ (fun s : ℝ => ((2 * s : ℝ) : ℂ) * Complex.I) t := by
    have hcast : (fun s : ℝ => ((2 * s : ℝ) : ℂ) * Complex.I)
        = fun s : ℝ => (2 : ℂ) * (s : ℂ) * Complex.I := by
      funext s; push_cast; ring
    rw [hcast]
    exact (analyticAt_const.mul (Complex.ofRealCLM.analyticAt t)).mul analyticAt_const
  -- s ↦ exp((↑(2s)) * I).  The `∘`-shaped statement pins the composition
  -- decomposition, which higher-order unification otherwise gets wrong.
  have hexpC : AnalyticAt ℝ
      (Complex.exp ∘ fun s : ℝ => ((2 * s : ℝ) : ℂ) * Complex.I) t :=
    AnalyticAt.comp (g := Complex.exp)
      (f := fun s : ℝ => ((2 * s : ℝ) : ℂ) * Complex.I) (x := t)
      analyticAt_cexp.restrictScalars hlin
  have hexp : AnalyticAt ℝ
      (fun s : ℝ => Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I)) t := hexpC
  -- the point lies in the open cut-complement
  have hmem : Complex.exp (((2 * t : ℝ) : ℂ) * Complex.I) ∈ notCut :=
    QOU.Knot.Kummer.exp_mem_notCut (by linarith) (by linarith [Real.pi_pos])
  -- s ↦ cLiTwoExt (exp((↑(2s)) * I))  is real-analytic
  have hcliC : AnalyticAt ℝ
      (cLiTwoExt ∘ fun s : ℝ => Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I)) t :=
    AnalyticAt.comp (g := cLiTwoExt)
      (f := fun s : ℝ => Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I)) (x := t)
      (QOU.MathlibExt.analyticOnNhd_cLiTwoExt _ hmem).restrictScalars hexp
  have hcli : AnalyticAt ℝ
      (fun s : ℝ => cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))) t := hcliC
  -- take the imaginary part (ℝ-linear)
  have himC : AnalyticAt ℝ
      (⇑Complex.imCLM ∘ fun s : ℝ =>
        cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))) t :=
    AnalyticAt.comp (g := ⇑Complex.imCLM)
      (f := fun s : ℝ => cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))) (x := t)
      (Complex.imCLM.analyticAt _) hcli
  have him : AnalyticAt ℝ
      (fun s : ℝ => (cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))).im) t := by
    simpa [Function.comp, Complex.imCLM_apply] using himC
  -- divide by two
  have hhalf : AnalyticAt ℝ
      (fun s : ℝ => (cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))).im
        * (2 : ℝ)⁻¹) t := him.mul analyticAt_const
  -- Λ agrees with this on the open interval, so Λ is analytic at t
  refine hhalf.congr ?_
  filter_upwards [isOpen_Ioo.mem_nhds (show t ∈ Ioo (0 : ℝ) π from ⟨h0, hπ⟩)] with s hs
  have hk := QOU.Knot.Kummer.im_cLiTwoExt_exp (θ := 2 * s)
    (by linarith [hs.1]) (by linarith [hs.2, Real.pi_pos])
  show (cLiTwoExt (Complex.exp (((2 * s : ℝ) : ℂ) * Complex.I))).im * (2 : ℝ)⁻¹ = Lob s
  rw [show Lob s = Cl_2 (2 * s) / 2 from rfl, div_eq_mul_inv, hk]

/-- **`Λ` is real-analytic on the whole open interval `(0, π)`** — the
`AnalyticOnNhd` form the identity-theorem step (step 3) consumes. -/
theorem analyticOnNhd_Lob : AnalyticOnNhd ℝ Lob (Ioo 0 π) :=
  fun _ ht => analyticAt_Lob ht.1 ht.2

end QOU.Archimedean
