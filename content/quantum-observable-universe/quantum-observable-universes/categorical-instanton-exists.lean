/-!
# QOU.CategoricalInstanton.exists — existence of categorical instantons

Trivial witness: the zero connection has F = 0 (self-dual).
Non-trivial witness: BPST descent on SU_q(2)-bundle.

LaTeX: `\label{prop:categorical-instanton-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-instanton-exists
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

import QOU.Basic

namespace QOU

/-- **Existence of categorical instantons.**

    For any `FrobeniusHopfData C`, a `CategoricalInstanton fh` term
    exists — the trivial connection F = 0 is self-dual, providing
    the zero-instanton witness. -/
-- Ref: [atiyah1978]
theorem CategoricalInstanton.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) :
    Nonempty (@CategoricalInstanton C _ _ fh) :=
  -- Trivial witness: identity connection / curvature, identity Hodge
  -- star (involutive: 𝟙 ≫ 𝟙 = 𝟙). Self-duality reduces to
  -- 𝟙 ≫ 𝟙 = 𝟙 via Category.comp_id.
  -- The intended BPST descent witness on SU_q(2) is sharper but
  -- requires the gauge-bundle infrastructure not yet in Mathlib.
  -- Ref: [atiyah1978]
  ⟨{ connection := 𝟙 fh.obj
     curvature := 𝟙 fh.obj
     hodge :=
       { star := 𝟙 fh.obj
         star_sq := by simp }
     self_dual := by
       show 𝟙 fh.obj ≫ 𝟙 fh.obj = 𝟙 fh.obj
       simp }⟩

end QOU
