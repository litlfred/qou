import QOU.QuantumObservableUniverse.SubstrateParameter

/-!
# QOU.qLieBracket

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/qLieBracket.lean (monolithic)

The q-deformed Lie bracket is the **archimedean** realisation of the
categorical q-Lie bracket. It is stated over `ℝ` because the substrate
parameter `q = sp.field p : ℝ` (`ArchimedeanSubstrateField.field`) is an
ℝ-valued field with `q(p) ≥ 1`; the coefficient `q⁻¹` and the Planck
constant `1 − q⁻¹` therefore live on the archimedean side of the
substrate→archimedean wall.
-/

namespace QOU

/-- **q-Deformed Lie bracket**:
    `[V, W]_q = q⁻¹ [V, W] + (1 − q⁻¹)(θ(V) ℒ_ξ W − θ(W) ℒ_ξ V)`.

    Here `bracket_VW = [V, W]` is the classical bracket value,
    `thetaV_LxiW = θ(V) ℒ_ξ W` and `thetaW_LxiV = θ(W) ℒ_ξ V`, all
    evaluated pointwise at `p : M`, with `q = sp.field p`.

    LaTeX: `\label{def:q-lie-bracket}` -/
noncomputable def qLieBracket {M : Type*} (sp : ArchimedeanSubstrateField M)
    (bracket_VW : M → ℝ) (thetaV_LxiW : M → ℝ) (thetaW_LxiV : M → ℝ)
    (p : M) : ℝ :=
  (sp.field p)⁻¹ * bracket_VW p +
    (1 - (sp.field p)⁻¹) * (thetaV_LxiW p - thetaW_LxiV p)

/-- The q-deformed Lie bracket recovers the classical bracket at `q = 1`. -/
theorem qLieBracket_classical {M : Type*} (sp : ArchimedeanSubstrateField M)
    (bracket_VW thetaV_LxiW thetaW_LxiV : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qLieBracket sp bracket_VW thetaV_LxiW thetaW_LxiV p = bracket_VW p := by
  simp [qLieBracket, hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

end QOU
