import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import QOU.Mass.ColorSpectralCubicGeometry

/-!
# QOU.Mass.DilationBranchLocusRigidity — no nontrivial dilation preserves the branch locus

The colour spectral curve `Σ : P(X,z) = 0` of the Lever-1 binding kernel is a
3-sheeted cover of the `z`-line whose branch locus is the zero set of the
**branch sextic**

  `D(z) = 16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16`

(`= −disc_X P`, `QOU.Mass.ColorSpectralCubicGeometry.color_cubic_discriminant`).

This file proves that `D` is **rigid under scaling**: if precomposing `D` with a
dilation `z ↦ l·z` returns a constant multiple of `D`, then `l = 1` (and the
constant is `1`). Two coefficients do all the work — the constant term forces
`c = 1`, and the linear term then forces `l = 1`.

## Why this closes a route (bean `qou-lmnq`; wall W1, `qou-d8de`)

The W1 wall asks for a q-difference prolongation `D_q` built from `Σ`, and its
first named route is a **q-shift on the base**, `z ↦ q²z`. Two prior tranches
excluded that route by the *coefficient field*: no rational q-connection on the
`z`-line has the sheets as flat sections (`QOU.Mass.ColorCubicIrreducible`, PR
#6695), and the same exclusion survives passage to the ramified local chart
(`QOU.Mass.IrreducibleCubicNoQuadraticRoot`, PR #6738). What those left open was
an operator living on `Σ` itself rather than on a coordinate.

This file closes that, and it needs no rationality theorem. **The geometric step
is stated here in prose and is not formalised**: an automorphism `σ : Σ → Σ`
covering `z ↦ l·z` is an isomorphism of coverings up to the base automorphism, so
it carries ramification points to ramification points and therefore permutes the
finite branch locus `B`. Because `D` is squarefree (exactly checked in the
companion probe) and `D(0) = 16 ≠ 0`, "`l·B = B`" says precisely that `D(l·z)`
and `D(z)` have the same root multiset, i.e. `D ∘ (l·) = c·D` for a constant `c`.
That hypothesis is where this file starts, and from it `l = 1` — so **the only
dilation admitting a lift to `Σ` is the identity**, for every `l`, root of unity
or not, at every `q`.

The complementary half — that `Σ → P¹` has full `S₃` monodromy, hence no
single-valued algebraic branch — is **already held in the corpus** and is cited
rather than re-derived: `computations/qbeta/c3_w1_cover_monodromy.py`.

> **Currency note (2026-09-12).** The paragraph above says "the geometric step is
> stated here in prose and is not formalised". That step is **two** halves, and only
> one is still prose. *An automorphism of `Σ` permutes `B`* remains prose — genuinely
> geometric, about coverings and ramification. *A map sending a finite set of nonzero
> points into itself has finite order* is now proved:
> `QOU.Mass.BranchLocusFiniteOrder.exists_pow_eq_one_of_stabilizes`, with the
> substrate corollaries `not_stabilizes_of_one_lt_real` / `..._complex` ruling out
> every real `l > 1`. The general-Möbius determinacy behind `Stab(B) ↪ Sym(B)` is
> also proved, in `QOU.Mass.MoebiusThreePointRigidity`. So the prose chain from here
> to the conclusion is **one link long, not two**.

Ground ring: `[Field K] [CharZero K]` (§7c). Characteristic zero is used exactly
to invert `16` and `24`; nothing archimedean appears.
-/

namespace QOU.Mass.DilationBranchLocusRigidity

open Polynomial

variable {K : Type*}

section CommRing

variable [CommRing K]

/-- The **branch-locus sextic as a polynomial**, `16X⁶+24X⁵+35X⁴+50X³+35X²+24X+16`.
The polynomial avatar of `QOU.Mass.ColorSpectralCubicGeometry.branchSextic`; see
`eval_branchSexticPoly`. -/
noncomputable def branchSexticPoly : K[X] :=
  C 16 * X ^ 6 + C 24 * X ^ 5 + C 35 * X ^ 4 + C 50 * X ^ 3 + C 35 * X ^ 2 + C 24 * X + C 16

/-- The polynomial avatar evaluates to the corpus's branch sextic. -/
theorem eval_branchSexticPoly (z : K) :
    (branchSexticPoly : K[X]).eval z = ColorSpectralCubicGeometry.branchSextic z := by
  unfold branchSexticPoly ColorSpectralCubicGeometry.branchSextic
  simp only [eval_add, eval_mul, eval_pow, eval_C, eval_X]

/-- Precomposition with the dilation `z ↦ l·z`, coefficients read off. -/
theorem branchSexticPoly_comp_scale (l : K) :
    (branchSexticPoly : K[X]).comp (C l * X)
      = C (16 * l ^ 6) * X ^ 6 + C (24 * l ^ 5) * X ^ 5 + C (35 * l ^ 4) * X ^ 4
        + C (50 * l ^ 3) * X ^ 3 + C (35 * l ^ 2) * X ^ 2 + C (24 * l) * X + C 16 := by
  unfold branchSexticPoly
  simp only [add_comp, mul_comp, pow_comp, C_comp, X_comp, map_mul, map_pow, mul_pow]
  ring

/-- A constant multiple of the sextic, in the same normal form. -/
theorem C_mul_branchSexticPoly (c : K) :
    C c * (branchSexticPoly : K[X])
      = C (c * 16) * X ^ 6 + C (c * 24) * X ^ 5 + C (c * 35) * X ^ 4
        + C (c * 50) * X ^ 3 + C (c * 35) * X ^ 2 + C (c * 24) * X + C (c * 16) := by
  unfold branchSexticPoly
  simp only [map_mul]
  ring

end CommRing

variable [Field K] [CharZero K]

/-- **Scaling rigidity of the branch locus.** If the branch sextic precomposed
with a dilation `z ↦ l·z` is a constant multiple of itself, then `l = 1` and the
constant is `1`.

The constant term gives `16 = c·16`, hence `c = 1`; the linear term then gives
`24·l = 24`, hence `l = 1`. Characteristic zero is used only to invert those two
integers. -/
theorem dilation_scaling_rigid (l c : K)
    (h : (branchSexticPoly : K[X]).comp (C l * X) = C c * branchSexticPoly) :
    l = 1 ∧ c = 1 := by
  rw [branchSexticPoly_comp_scale, C_mul_branchSexticPoly] at h
  have h0 := congrArg (fun p : K[X] => p.coeff 0) h
  have h1 := congrArg (fun p : K[X] => p.coeff 1) h
  simp only [coeff_add, coeff_C_mul_X_pow, coeff_C_mul_X, coeff_C] at h0 h1
  norm_num at h0 h1
  -- `h0` is the constant term `16 = c * 16`, which `norm_num` already solves for `c`;
  -- `h1` is the linear term `24 * l = c * 24`.
  refine ⟨?_, h0⟩
  linear_combination (1 / 24 : K) * h1 + h0

/-- **No nontrivial dilation preserves the branch locus.** Contrapositive form:
a dilation by `l ≠ 1` cannot send the branch sextic to a multiple of itself, so
(by the covering argument in this file's header) it admits no lift to `Σ`. -/
theorem no_scaling_of_ne_one (l c : K) (hl : l ≠ 1) :
    (branchSexticPoly : K[X]).comp (C l * X) ≠ C c * branchSexticPoly :=
  fun h => hl (dilation_scaling_rigid l c h).1

/-- **The substrate case.** The dilation the W1 route asks for is `z ↦ q₀²z` with
`q₀ ≈ 1.10998`, so `l = q₀² > 1`; no such `l` preserves the branch locus. Stated
for any real `l > 1` so that no numerical value enters the Lean. -/
theorem no_scaling_of_one_lt (l c : ℝ) (hl : 1 < l)
    (h : (branchSexticPoly : ℝ[X]).comp (C l * X) = C c * branchSexticPoly) : False := by
  have := (dilation_scaling_rigid l c h).1
  linarith

end QOU.Mass.DilationBranchLocusRigidity
