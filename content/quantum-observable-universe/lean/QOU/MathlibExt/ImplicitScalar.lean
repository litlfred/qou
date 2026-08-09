import Mathlib.Analysis.Calculus.InverseFunctionTheorem.FDeriv
import Mathlib.Analysis.Calculus.FDeriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.Calculus.FDeriv.Pow
import Mathlib.Analysis.Calculus.FDeriv.Add
import Mathlib.Analysis.Complex.Basic

/-!
# Scalar implicit function theorem — solving `f x y = 0` for `y`

Bean `qou-trns`. The envelope step `dS/dφ = 2φ` needs the roots `yⱼ(x)` of the
GGM curve to be **differentiable in `x`**, and that is the implicit function
theorem for one equation in one unknown with one parameter.

## Why this is a Mathlib gap

Mathlib has an implicit function theorem — `Mathlib/Analysis/Calculus/Implicit.lean`
— but it is the general Banach-space version built on `ImplicitFunctionData`,
which presents the solution set through a complemented-subspace splitting
(`leftFun`/`rightFun`, and `implicitFunction : F → G → E` taking a point of
`ker f'`). That is the right shape for a submanifold and the wrong shape for
"solve for `y` as a function of `x`". It is also, as of this writing, imported by
nothing else in Mathlib.

What is missing is the scalar case in the form everyone actually uses:

    f x₀ y₀ = 0,  ∂f/∂y ≠ 0   ⟹   ∃ g,  g x₀ = y₀,  f x (g x) = 0 near x₀,
                                        g' x₀ = −(∂f/∂x)/(∂f/∂y)

`exists_hasDerivAt_implicit` below is that statement, over any complete
nontrivially-normed field — so `ℂ` for this application, and `ℝ` for free.

## The construction

The standard one, done concretely rather than through `ImplicitFunctionData`:
straighten the graph with `Φ(x,y) = (x, f x y)`, whose derivative

    L (a,b) = (a, A·a + B·b),      A = ∂f/∂x,  B = ∂f/∂y

is invertible exactly when `B ≠ 0`, with `L⁻¹(a,b) = (a, (b − A·a)/B)` written
down explicitly (`ContinuousLinearEquiv.equivOfInverse`). Then Mathlib's inverse
function theorem applies to `Φ`, and

    g x := (Φ.localInverse (x, 0)).2

is the branch. `eventually_right_inverse` gives `Φ(Ψ(x,0)) = (x,0)`, whose first
component says `Ψ(x,0) = (x, g x)` and whose second says `f x (g x) = 0`. The
derivative falls out of `to_localInverse` composed with `a ↦ (a,0)`, and
`L⁻¹(1,0) = (1, −A/B)` is where the IFT formula comes from.

## ⚠ Where this does NOT apply on the transport arc, and why that is expected

`∂curve/∂y ≠ 0` is exactly "`y` is a **simple** root", i.e. the discriminant does
not vanish. On the 5₂ transport arc the discriminant **does** vanish, at
`θ = 137.9206708879635°` — that is `exists_unit_circle_disc_zero`, proved in
`QOU/QBeta/FiveTwoDiscriminant.lean`. Two of the three branches collide there and
no differentiable labelling of individual roots survives it.

So this theorem gives the branches on `[0,π] ∖ {φ₀}` and cannot give them at
`φ₀`. That is not a defect: it is why
`QOU/Archimedean/ConstantOffOnePoint.lean` exists —
`constant_of_hasDerivWithinAt_zero_off_point` glues a derivative identity that
holds off one point into a statement on the whole interval, using continuity
there. The two bricks are built for each other.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms. This is one hypothesis
of the envelope step, not the envelope step, and certainly not the sum rule.
-/

namespace QOU.MathlibExt

open Filter Topology

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]

/-! ### The straightening map's derivative -/

/-- `L A B (a,b) = (a, A·a + B·b)` — the derivative of `(x,y) ↦ (x, f x y)`. -/
noncomputable def straighten (A B : 𝕜) : (𝕜 × 𝕜) →L[𝕜] (𝕜 × 𝕜) :=
  (ContinuousLinearMap.fst 𝕜 𝕜 𝕜).prod
    (A • ContinuousLinearMap.fst 𝕜 𝕜 𝕜 + B • ContinuousLinearMap.snd 𝕜 𝕜 𝕜)

@[simp] theorem straighten_apply (A B : 𝕜) (v : 𝕜 × 𝕜) :
    straighten A B v = (v.1, A * v.1 + B * v.2) := by
  simp [straighten, smul_eq_mul]

/-- The inverse: `(a,b) ↦ (a, (b − A·a)/B)`. -/
noncomputable def unstraighten (A B : 𝕜) : (𝕜 × 𝕜) →L[𝕜] (𝕜 × 𝕜) :=
  (ContinuousLinearMap.fst 𝕜 𝕜 𝕜).prod
    (B⁻¹ • (ContinuousLinearMap.snd 𝕜 𝕜 𝕜 - A • ContinuousLinearMap.fst 𝕜 𝕜 𝕜))

@[simp] theorem unstraighten_apply (A B : 𝕜) (v : 𝕜 × 𝕜) :
    unstraighten A B v = (v.1, B⁻¹ * (v.2 - A * v.1)) := by
  simp [unstraighten, smul_eq_mul]

/-- **The straightening map is a linear equivalence exactly when `∂f/∂y ≠ 0`.** -/
noncomputable def straightenEquiv (A : 𝕜) {B : 𝕜} (hB : B ≠ 0) : (𝕜 × 𝕜) ≃L[𝕜] (𝕜 × 𝕜) :=
  ContinuousLinearEquiv.equivOfInverse (straighten A B) (unstraighten A B)
    (fun v => by
      simp only [straighten_apply, unstraighten_apply]
      ext <;> (field_simp; try ring))
    (fun v => by
      simp only [straighten_apply, unstraighten_apply]
      ext <;> (field_simp; try ring))

@[simp] theorem straightenEquiv_apply (A : 𝕜) {B : 𝕜} (hB : B ≠ 0) (v : 𝕜 × 𝕜) :
    straightenEquiv A hB v = (v.1, A * v.1 + B * v.2) := straighten_apply A B v

@[simp] theorem straightenEquiv_symm_apply (A : 𝕜) {B : 𝕜} (hB : B ≠ 0) (v : 𝕜 × 𝕜) :
    (straightenEquiv A hB).symm v = (v.1, B⁻¹ * (v.2 - A * v.1)) :=
  unstraighten_apply A B v

/-! ### The theorem -/

/-- **Scalar implicit function theorem.**

If `f : 𝕜 × 𝕜 → 𝕜` is strictly differentiable at `(x₀, y₀)`, vanishes there, and
its `y`-partial `B := f' (0,1)` is nonzero, then there is a function `g` with
`g x₀ = y₀`, solving `f (x, g x) = 0` near `x₀`, and

    g' x₀ = −A / B,     A := f' (1,0).

Proved by straightening the graph with `(x,y) ↦ (x, f (x,y))` and applying
Mathlib's inverse function theorem, rather than through `ImplicitFunctionData`. -/
theorem exists_hasDerivAt_implicit [CompleteSpace 𝕜]
    {f : 𝕜 × 𝕜 → 𝕜} {f' : (𝕜 × 𝕜) →L[𝕜] 𝕜} {x₀ y₀ : 𝕜}
    (hf : HasStrictFDerivAt f f' (x₀, y₀)) (h0 : f (x₀, y₀) = 0)
    (hB : f' (0, 1) ≠ 0) :
    ∃ g : 𝕜 → 𝕜, g x₀ = y₀ ∧ (∀ᶠ x in 𝓝 x₀, f (x, g x) = 0) ∧
      HasDerivAt g (-(f' (1, 0)) / f' (0, 1)) x₀ := by
  set A := f' (1, 0) with hA
  set B := f' (0, 1) with hBdef
  -- `f'` acts as `v ↦ A·v.1 + B·v.2`
  have hf'apply : ∀ v : 𝕜 × 𝕜, f' v = A * v.1 + B * v.2 := by
    intro v
    have hv : v = v.1 • ((1 : 𝕜), (0 : 𝕜)) + v.2 • ((0 : 𝕜), (1 : 𝕜)) := by
      ext <;> simp
    rw [hv, map_add, f'.map_smul, f'.map_smul, ← hA, ← hBdef]
    simp [smul_eq_mul]
    ring
  -- the straightened map and its strict derivative
  set Φ : 𝕜 × 𝕜 → 𝕜 × 𝕜 := fun q => (q.1, f q) with hΦ
  have hderiv : HasStrictFDerivAt Φ ((straightenEquiv A hB : (𝕜 × 𝕜) →L[𝕜] (𝕜 × 𝕜)))
      (x₀, y₀) := by
    have h1 : HasStrictFDerivAt (fun q : 𝕜 × 𝕜 => q.1)
        (ContinuousLinearMap.fst 𝕜 𝕜 𝕜) (x₀, y₀) := hasStrictFDerivAt_fst
    have h2 := h1.prodMk hf
    convert h2 using 1
    refine ContinuousLinearMap.ext fun v => ?_
    simp [straightenEquiv, straighten, hf'apply v]
  set Ψ := hderiv.localInverse Φ _ (x₀, y₀) with hΨ
  have hΦp : Φ (x₀, y₀) = (x₀, 0) := by simp [hΦ, h0]
  refine ⟨fun x => (Ψ (x, 0)).2, ?_, ?_, ?_⟩
  · -- `g x₀ = y₀`
    have := hderiv.localInverse_apply_image
    rw [hΦp] at this
    simp [hΨ, this]
  · -- `f (x, g x) = 0` near `x₀`
    have hri := hderiv.eventually_right_inverse
    rw [hΦp] at hri
    have hmap : Tendsto (fun x : 𝕜 => (x, (0 : 𝕜))) (𝓝 x₀) (𝓝 (x₀, 0)) :=
      (Continuous.prodMk continuous_id continuous_const).tendsto x₀
    filter_upwards [hmap.eventually hri] with x hx
    have h1 : (Ψ (x, 0)).1 = x := congrArg Prod.fst hx
    have h2 : f (Ψ (x, 0)) = 0 := congrArg Prod.snd hx
    have h3 : (x, (Ψ (x, 0)).2) = Ψ (x, 0) := Prod.ext h1.symm rfl
    rw [h3]; exact h2
  · -- the derivative
    have hinv : HasStrictFDerivAt Ψ
        ((straightenEquiv A hB).symm : (𝕜 × 𝕜) →L[𝕜] (𝕜 × 𝕜)) (Φ (x₀, y₀)) :=
      hderiv.to_localInverse
    rw [hΦp] at hinv
    have hincl : HasDerivAt (fun x : 𝕜 => (x, (0 : 𝕜))) ((1 : 𝕜), (0 : 𝕜)) x₀ := by
      simpa using (hasDerivAt_id x₀).prodMk (hasDerivAt_const x₀ (0 : 𝕜))
    have hcomp := hinv.hasFDerivAt.comp_hasDerivAt x₀ hincl
    have hsnd : HasDerivAt (fun x : 𝕜 => (Ψ (x, 0)).2)
        (((straightenEquiv A hB).symm ((1 : 𝕜), (0 : 𝕜))).2) x₀ := by
      simpa using (ContinuousLinearMap.snd 𝕜 𝕜 𝕜).hasFDerivAt.comp_hasDerivAt x₀ hcomp
    rw [straightenEquiv_symm_apply] at hsnd
    convert hsnd using 1
    field_simp
    ring

/-! ### Non-vacuity: the hypotheses are satisfiable and the formula is right -/

/-- **Usability check.** An existence theorem whose hypotheses nothing satisfies
is worthless, so here it is instantiated end to end on `f (x,y) = y² − x` at
`(1,1)`: `∂f/∂y = 2 ≠ 0`, `∂f/∂x = −1`, and the theorem returns a branch of
`√x` through `1` with `g′(1) = −(−1)/2 = 1/2` — the derivative of `√x` at `1`,
as it must be. -/
theorem exists_sqrt_branch :
    ∃ g : ℂ → ℂ, g 1 = 1 ∧ (∀ᶠ x in 𝓝 (1 : ℂ), (g x) ^ 2 - x = 0) ∧
      HasDerivAt g (1 / 2) 1 := by
  set F' : (ℂ × ℂ) →L[ℂ] ℂ :=
    (2 : ℂ) • ContinuousLinearMap.snd ℂ ℂ ℂ - ContinuousLinearMap.fst ℂ ℂ ℂ with hF'
  have hf : HasStrictFDerivAt (fun q : ℂ × ℂ => q.2 ^ 2 - q.1) F' ((1 : ℂ), (1 : ℂ)) := by
    have h2 : HasStrictFDerivAt (fun q : ℂ × ℂ => q.2 ^ 2)
        ((2 : ℂ) • ContinuousLinearMap.snd ℂ ℂ ℂ) ((1 : ℂ), (1 : ℂ)) := by
      simpa using (hasStrictFDerivAt_snd (𝕜 := ℂ) (p := ((1 : ℂ), (1 : ℂ)))).pow 2
    simpa [hF'] using h2.sub hasStrictFDerivAt_fst
  have hB : F' (0, 1) ≠ 0 := by simp [hF']
  obtain ⟨g, hg0, hgeq, hgd⟩ :=
    exists_hasDerivAt_implicit hf (by norm_num) hB
  refine ⟨g, hg0, hgeq, ?_⟩
  have : -(F' (1, 0)) / F' (0, 1) = 1 / 2 := by simp [hF']
  rwa [this] at hgd

end QOU.MathlibExt
