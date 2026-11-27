/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLMoiseGap
import BraidKnotOctonion.PLScaling

set_option autoImplicit false

/-!
# Assembly of the Moise–Bing comparison (#8902)

`MoiseBing E` follows from a **relative Moise approximation**: topologically ambient isotopic
polygonal links are carried onto one another, component by component and with orientation, by a
PL homeomorphism of bounded displacement. A PL homeomorphism of bounded displacement is PL
isotopic to the identity (`PLAmbientIsotopic.of_bounded`, `PLScaling.lean`), which closes the
argument with no further gap.

The bound is necessary, not a convenience: the track of a PL isotopy is Lipschitz, so its end map
has bounded displacement, and `x ↦ 2 • x` is not PL isotopic to the identity
(`not_plIsotopicToId_two_smul`). The approximation is therefore asked to produce, e.g., a
compactly supported homeomorphism.

The approximation is a hypothesis here. This file proves only that it suffices.
-/

namespace QOU.MathlibExt.PL

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **Moise–Bing from relative Moise approximation with bounded displacement.** -/
theorem moiseBing_of_relMoise [FiniteDimensional ℝ E]
    (hB : ∀ L L' : PolygonalLink E, AmbientIsotopic L L' →
      ∃ (g : E ≃ₜ E) (e : Fin L.k ≃ Fin L'.k) (B : ℝ), IsPL g ∧ (∀ x, ‖g x - x‖ ≤ B) ∧
        ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
          ∀ t, g ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    MoiseBing E := by
  intro L L' h
  obtain ⟨g, e, B, hPL, hb, hfin⟩ := hB L L' h
  exact PLAmbientIsotopic.of_bounded g hPL hb e hfin

end QOU.MathlibExt.PL
