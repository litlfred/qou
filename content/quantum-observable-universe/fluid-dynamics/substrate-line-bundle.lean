/-!
# QOU.FluidDynamics.SubstrateLineBundle — The substrate line bundle and the G_m-family of differentials

The substrate line bundle is the trivial G_m-torsor Q = End(1) ⊗_Z G_m → Spec R
whose fibre at each R-point is G_m(R) = R^x.  A substrate section is a global
section q : Spec R → Q, i.e. an element q ∈ R^x.  When the QOU is fibred over
a space M, the substrate line bundle is Q_M = M × G_m.

LaTeX label: `def:substrate-line-bundle`

## References

- [manuscript] Ch 10 §1

**Ground ring**: `R_q = ℤ[q, q⁻¹]`
-/

import Mathlib.Data.Real.Basic

namespace QOU.FluidDynamics

/-- The substrate line bundle: a trivial G_m-torsor parametrising the
    substrate parameter q.  A substrate section is an invertible element
    q ∈ R^x encoding the deformation parameter of the QOU.

    The G_m-family of differentials consists of the q-parametrised
    differential forms d_q, δ_q varying over the base Spec R. -/
-- Ref: [manuscript] Ch 10 §1
structure SubstrateLineBundle where
  /-- The substrate section q ∈ R^x (invertible element). -/
  q : ℝ
  /-- The substrate parameter is strictly positive. -/
  q_pos : 0 < q
  /-- The q-parametrised family of differentials (abstractly). -/
  -- Ref: [manuscript] Ch 10 §1
  differential_family : Type*

end QOU.FluidDynamics
