/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLMoiseGap
import QOU.MathlibExt.PLHomeo

set_option autoImplicit false

/-!
# Assembly of the Moise–Bing comparison (#8902)

`MoiseBing E` follows from two inputs:

* `PLIsotopyToId E`: an orientation-preserving PL homeomorphism with PL inverse is PL isotopic to
  the identity (`PLHomeo.lean`);
* a relative Moise approximation: topologically ambient isotopic polygonal links are carried onto
  one another, component by component and with orientation, by an orientation-preserving PL
  homeomorphism with PL inverse.

Both are hypotheses here. This file proves only that they combine.
-/

namespace QOU.MathlibExt.PL

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **Moise–Bing from its two parts**, the PL isotopy theorem and relative Moise approximation. -/
theorem moiseBing_of_parts (hiso : PLIsotopyToId E)
    (hB : ∀ L L' : PolygonalLink E, AmbientIsotopic L L' →
      ∃ (g : E ≃ₜ E) (e : Fin L.k ≃ Fin L'.k), IsPL g ∧ IsPL g.symm ∧
        IsPL.OrientationPreserving g ∧ ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
          ∀ t, g ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    MoiseBing E := by
  intro L L' h
  obtain ⟨g, e, _, hinv, hor, hfin⟩ := hB L L' h
  exact PLAmbientIsotopic.of_plHomeo hiso g hor hinv e hfin

end QOU.MathlibExt.PL
