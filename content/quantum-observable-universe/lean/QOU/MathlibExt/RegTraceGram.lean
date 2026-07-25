import QOU.MathlibExt.TraceFormSemisimple
import Mathlib.LinearAlgebra.Matrix.BilinearForm

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

end QOU.MathlibExt
