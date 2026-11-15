import QOU.MathlibExt.TraceFormSemisimple
import Mathlib.LinearAlgebra.Matrix.BilinearForm
import Mathlib.LinearAlgebra.Basis.Basic

/-!
# QOU.MathlibExt.RegTraceGram — the Gram-determinant criterion

Brick B2f-core (epic `qou-hnhg`).  Packages the regular trace form
`regTraceForm` as a genuine `LinearMap.BilinForm`, so all of Mathlib's
Gram-determinant machinery applies to it.  In particular
`LinearMap.BilinForm.nondegenerate_iff_det_ne_zero` gives, for any finite
basis `b`,

  `(regTraceBilin).Nondegenerate  ↔  det (Gram matrix of regTraceBilin in b) ≠ 0`,

so the abstract semisimplicity keystone (B3d) becomes a **determinant
condition**:

> `H` is semisimple ⟸ the Gram matrix of the regular trace form has
> nonzero determinant.

For the Iwahori–Hecke algebra `H_n(q)` in its `T_w` basis that
determinant is `[n]_q!` (up to a unit) — the Schur-element / Poincaré
identity.  Supplying that value (which needs the `n!`-dim `T_w` basis,
brick `qou-lrz1`) is the only remaining step to discharge
`WenzlCriterion`; the packaging + the `nondegenerate ⇒ semisimple`
direction are proven here, sorry-free.
-/

namespace QOU.MathlibExt

open Algebra LinearMap

variable (K A : Type*) [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]

/-- The **regular trace form as a bilinear form**:
    `B(x, y) = trace(L_{xy})`.  Being a genuine `LinearMap.BilinForm`,
    it plugs into Mathlib's Gram-matrix / determinant API. -/
noncomputable def regTraceBilin : LinearMap.BilinForm K A :=
  LinearMap.compr₂ (LinearMap.mul K A)
    ((LinearMap.trace K A).comp (Algebra.lmul K A).toLinearMap)

variable {K A}

@[simp] theorem regTraceBilin_apply (x y : A) :
    regTraceBilin K A x y = regTraceForm K A x y := rfl

/-- **Abstract semisimplicity from the bilinear form's nondegeneracy
    (sorry-free).**  Restates the B3d keystone through `regTraceBilin`,
    so that Mathlib's `nondegenerate_iff_det_ne_zero` — applied to
    `regTraceBilin` — turns semisimplicity into a Gram-determinant
    condition on any chosen basis. -/
theorem isSemisimpleRing_of_regTraceBilin_nondegenerate
    (h : (regTraceBilin K A).Nondegenerate) : IsSemisimpleRing A :=
  isSemisimpleRing_of_regTraceForm_nondegenerate fun x hx =>
    h x fun y => (regTraceBilin_apply x y).trans (hx y)

/-- **Gram-determinant ⟹ semisimple, explicit-matrix form (sorry-free).**
    For any finite basis `b` of `A`, a nonzero determinant of the regular
    trace form's Gram matrix `BilinForm.toMatrix b (regTraceBilin K A)`
    forces semisimplicity.  The Gram entries are the observable traces
    `toMatrix b (regTraceBilin) i j = regTraceForm K A (b i) (b j)
    = tr(L_{b_i b_j})` (`BilinForm.toMatrix_apply` ∘ `regTraceBilin_apply`).

    This is the exact hook a `T_w`-basis Gram computation plugs into:
    supply the basis `b` (brick `qou-lrz1`) and the determinant value
    `det = [n]_q!` (brick `qou-twwf`), and semisimplicity of `H_n(q)`
    follows — no further Hecke input.  The `n = 2` value is already
    computed concretely in `QOU.Hecke.H2CompanionRep`. -/
theorem isSemisimpleRing_of_regTraceGram_det_ne_zero
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A)
    (h : (BilinForm.toMatrix b (regTraceBilin K A)).det ≠ 0) :
    IsSemisimpleRing A :=
  isSemisimpleRing_of_regTraceBilin_nondegenerate
    ((BilinForm.nondegenerate_iff_det_ne_zero b).mpr h)

/-- **Gram entries are the observable regular-trace values (sorry-free).**
    Records that the `(i, j)` entry of the Gram matrix in a basis `b` is
    `tr(L_{b_i b_j})`, so a `T_w`-basis Gram computation is literally a
    table of Markov-trace observables. -/
@[simp] theorem regTraceGram_toMatrix_apply
    {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Module.Basis ι K A) (i j : ι) :
    BilinForm.toMatrix b (regTraceBilin K A) i j = regTraceForm K A (b i) (b j) := by
  rw [BilinForm.toMatrix_apply, regTraceBilin_apply]

end QOU.MathlibExt
