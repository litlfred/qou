import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic


/-!
# QOU.qExtDeriv

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qExtDeriv.lean (monolithic).
That file no longer exists — the library was split, and `qExtDeriv` now lives at
  content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Particles.lean

**Archimedean realisation.** This is the archimedean specialisation of the
categorical `d_q` (cf. `def:categorical-q-ext-deriv`): the differential
forms and the substrate field are evaluated over `ℝ` at the substrate
point `q(p) = sp.field p`. The substrate parameter
(`QOU.ArchimedeanSubstrateField`) carries `field : M → ℝ`, so the per-point
evaluation lives in `ℝ`.
-/

namespace QOU

universe u v

/-- **q-Deformed exterior derivative** (archimedean realisation):
    `d_q α = q⁻¹ dα + (1 − q⁻¹) θ ∧ L_ξ α`, evaluated at the substrate
    point `q(p) = sp.field p`.

    LaTeX: `\label{def:q-ext-deriv}` -/
noncomputable def qExtDeriv {M : Type*} (sp : ArchimedeanSubstrateField M)
    (d_alpha : M → ℝ) (lieDerivReeb : M → ℝ) (theta : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * d_alpha p +
    (1 - (sp.field p)⁻¹) * (theta p * lieDerivReeb p)

/-- The q-deformed exterior derivative recovers the classical `d` at `q = 1`. -/
theorem qExtDeriv_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (d_alpha lieDerivReeb theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qExtDeriv sp d_alpha lieDerivReeb theta p = d_alpha p := by
  simp [qExtDeriv, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
