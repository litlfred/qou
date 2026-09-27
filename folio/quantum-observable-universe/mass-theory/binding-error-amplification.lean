import Mathlib.Tactic

/-!
# Binding-energy error amplification

Binding is a mass defect `B = M_free − M_atom` with `B ≪ M_atom`. A relative
error `δ` in the predicted bound-state mass is amplified by the factor
`M_atom / B` in the predicted binding energy. For light nuclei this factor is
of order 10²–10³, so a sub-percent error in the bound-state mass (the
step-9a per-knot mass-prediction error) becomes a tens-of-percent error in
the binding energy (the step-9b gap). The two are one error, not two.

This is a pure error-propagation identity over `ℝ` — no q-deformation, no
calibration input, no fit. It quantifies why per-knot mass accuracy gates
binding accuracy.

-- Ref: [manuscript] prop:binding-error-amplification
-/

namespace QOU.MassTheory.BindingErrorAmplification

/-- The amplification factor: bound-state mass over binding energy. -/
noncomputable def amplification (M_atom B : ℝ) : ℝ := M_atom / B

/-- **Binding-energy error amplification.**  With binding defined as the mass
    defect `B = M_free − M_atom`, and the predicted bound mass carrying
    relative error `δ` (`M_atom_pred = M_atom·(1 + δ)`, exact `M_free`), the
    predicted binding `B_pred = M_free − M_atom_pred` has relative error

      `(B_pred − B) / B = −δ · (M_atom / B)`.

    The amplification factor is the mass-to-binding ratio `M_atom / B`. -/
theorem binding_rel_error
    (M_free M_atom B δ : ℝ)
    (hB : B = M_free - M_atom) :
    (M_free - M_atom * (1 + δ) - B) / B = -δ * (M_atom / B) := by
  rw [hB]; ring

/-- The amplification factor `M_atom / B` for ⁴He exceeds 130, in the
    cross-multiplied form `130 · B_AME < M_atom` with bound mass
    `M_atom ≈ 3727.379 MeV` and `B_AME ≈ 28.296 MeV` (CODATA / AME-2020).
    A `0.7 %` bound-mass error therefore becomes a `~90 %` binding error.
    The ratio itself carries no framework assumption. -/
theorem helium4_amplification_gt_130 :
    (130 : ℝ) * 28.295673 < 3727.379 := by norm_num

end QOU.MassTheory.BindingErrorAmplification
