import QOU.QBeta.FiveTwoDeformedSaddle
import QOU.MathlibExt.ImplicitScalar
import Mathlib.Analysis.Calculus.FDeriv.Pow

/-!
# The GGM curve's roots are locally differentiable in `x`

Bean `qou-trns`. `QOU/MathlibExt/ImplicitScalar.lean` supplies the scalar
implicit function theorem; this file plugs it into the curve, which is the only
thing standing between that brick and the envelope step.

Two pieces:

* `hasStrictFDerivAt_curve` — the curve, as a function of `(x,y) : ℂ × ℂ`, is
  strictly differentiable everywhere, with derivative `∂ₓc • fst + ∂_yc • snd`.
  Mechanical (it is a polynomial), but the partials have to be written down and
  matched against what the `mul`/`pow`/`sub` combinators produce.

* `exists_hasDerivAt_root` — the payoff. Off the discriminant locus, a root of
  the curve is locally a differentiable function of `x`, with the IFT value.

## The partials

    curve x y = x·y³ − (x²+1)·y² + (x²+x+1)·y − x

    ∂ₓcurve = y³ − 2x·y² + (2x+1)·y − 1
    ∂_ycurve = 3x·y² − 2(x²+1)·y + (x²+x+1)

`∂_ycurve ≠ 0` is exactly "`y` is a **simple** root of the cubic", which is what
the IFT needs and what fails on the discriminant locus.

## ⚠ It does not hold on all of the transport arc, and that is expected

`exists_unit_circle_disc_zero` (`FiveTwoDiscriminant.lean`) proves the
discriminant **vanishes** on `|x| = 1`, at `θ = 137.9206708879635°`. There two of
the three branches collide, `∂_ycurve = 0`, and no differentiable labelling of
individual roots exists. So this gives branches on `[0,π] ∖ {φ₀}` only — and
`QOU/Archimedean/ConstantOffOnePoint.lean` is the brick that glues such a
statement into one on the whole interval.

## What the envelope still needs after this

The chain rule for `d/dφ Σⱼ V(x, yⱼ(φ))`, where the `dyⱼ/dx` terms vanish
because `∂V/∂y = 0` — and that is already free, since
`deformed_saddle_iff_curve` says the saddle condition **is** the curve. Note the
envelope never needs the *value* of `dyⱼ/dx`, only that it exists; this file
supplies the value anyway because the IFT gives it for nothing.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. This is one hypothesis
of the envelope step, not the envelope step.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open QOU.MathlibExt

/-- `∂(curve)/∂x` at `(x, y)`. -/
noncomputable def curveDx (x y : ℂ) : ℂ := y ^ 3 - 2 * x * y ^ 2 + (2 * x + 1) * y - 1

/-- `∂(curve)/∂y` at `(x, y)`. Nonvanishing is exactly "`y` is a simple root". -/
noncomputable def curveDy (x y : ℂ) : ℂ := 3 * x * y ^ 2 - 2 * (x ^ 2 + 1) * y + (x ^ 2 + x + 1)

/-- **The curve is strictly differentiable in `(x, y)`**, with the stated partials. -/
theorem hasStrictFDerivAt_curve (x₀ y₀ : ℂ) :
    HasStrictFDerivAt (fun q : ℂ × ℂ => curve q.1 q.2)
      (curveDx x₀ y₀ • ContinuousLinearMap.fst ℂ ℂ ℂ
        + curveDy x₀ y₀ • ContinuousLinearMap.snd ℂ ℂ ℂ) (x₀, y₀) := by
  have hx : HasStrictFDerivAt (fun q : ℂ × ℂ => q.1)
      (ContinuousLinearMap.fst ℂ ℂ ℂ) (x₀, y₀) := hasStrictFDerivAt_fst
  have hy : HasStrictFDerivAt (fun q : ℂ × ℂ => q.2)
      (ContinuousLinearMap.snd ℂ ℂ ℂ) (x₀, y₀) := hasStrictFDerivAt_snd
  -- curve = ((x·y³ − (x²+1)·y²) + (x²+x+1)·y) − x, matching `curve`'s parse
  have h := (((hx.mul (hy.pow 3)).sub (((hx.pow 2).add_const 1).mul (hy.pow 2))).add
      ((((hx.pow 2).add hx).add_const 1).mul hy)).sub hx
  simp only [curve]
  convert h using 1
  refine ContinuousLinearMap.ext fun v => ?_
  simp [curveDx, curveDy]
  ring

/-- **Off the discriminant locus, a root of the GGM curve is locally a
differentiable function of `x`.**

This is `exists_hasDerivAt_implicit` specialised to the curve. The hypothesis
`curveDy x₀ y₀ ≠ 0` is "`y₀` is a simple root"; it is exactly what fails at the
branch point on the transport arc. -/
theorem exists_hasDerivAt_root {x₀ y₀ : ℂ} (hc : curve x₀ y₀ = 0)
    (hdy : curveDy x₀ y₀ ≠ 0) :
    ∃ g : ℂ → ℂ, g x₀ = y₀ ∧ (∀ᶠ x in nhds x₀, curve x (g x) = 0) ∧
      HasDerivAt g (-(curveDx x₀ y₀) / curveDy x₀ y₀) x₀ := by
  set F' : (ℂ × ℂ) →L[ℂ] ℂ :=
    curveDx x₀ y₀ • ContinuousLinearMap.fst ℂ ℂ ℂ
      + curveDy x₀ y₀ • ContinuousLinearMap.snd ℂ ℂ ℂ with hF'
  have hf : HasStrictFDerivAt (fun q : ℂ × ℂ => curve q.1 q.2) F' (x₀, y₀) :=
    hasStrictFDerivAt_curve x₀ y₀
  have hA : F' (1, 0) = curveDx x₀ y₀ := by simp [hF']
  have hB : F' (0, 1) = curveDy x₀ y₀ := by simp [hF']
  obtain ⟨g, hg0, hgeq, hgd⟩ :=
    exists_hasDerivAt_implicit hf (by simpa using hc) (by rw [hB]; exact hdy)
  exact ⟨g, hg0, hgeq, by rwa [hA, hB] at hgd⟩

/-- **Non-vacuity.** `exists_hasDerivAt_root` is an existence theorem, and one
whose hypotheses nothing satisfies proves nothing. They are satisfiable:
`(x, y) = (0, 0)` lies on the curve, and `curveDy 0 0 = 1 ≠ 0`.

The check with real content is numerical and lives in Route 26: along the
transport arc `|curveDy|` is bounded away from zero except at the branch point
`φ₀`, where it vanishes — so the IFT applies on `[0,π] ∖ {φ₀}` and nowhere
fails except exactly where `exists_unit_circle_disc_zero` says it must. -/
theorem exists_hasDerivAt_root_nonvacuous :
    ∃ g : ℂ → ℂ, g 0 = 0 ∧ (∀ᶠ x in nhds (0 : ℂ), curve x (g x) = 0) ∧
      HasDerivAt g (-(curveDx 0 0) / curveDy 0 0) 0 :=
  exists_hasDerivAt_root (by simp [curve]) (by norm_num [curveDy])

end QOU.QBeta.FiveTwoDeformedSaddle
