import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring


/-!
# QOU.qConnection

Extracted from folio/quantum-observable-universe/lean/ for content-block co-location.
Source: folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Particles.lean

**Archimedean realisation**: the substrate parameter `q : M → ℝ` is the
`field` of a `ArchimedeanSubstrateField`. The categorical `q`-connection specialises
to `A_q = q⁻¹ A + (1 − q⁻¹) ι_ξ A · θ`. At `q = 1` this recovers the full
instanton connection `A`.
-/

namespace QOU

/-- **q-Deformed connection**: `A_q = q⁻¹ A + (1 − q⁻¹) ι_ξ A · θ`.

    LaTeX: `\label{def:q-connection}` -/
noncomputable def qConnection {M : Type*} (sp : ArchimedeanSubstrateField M)
    (connA : M → ℝ) (iotaXiA : M → ℝ) (theta : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * connA p +
    (1 - (sp.field p)⁻¹) * (iotaXiA p * theta p)

/-- The q-deformed connection recovers the classical connection at `q = 1`. -/
theorem qConnection_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (connA iotaXiA theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qConnection sp connA iotaXiA theta p = connA p := by
  unfold qConnection
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
