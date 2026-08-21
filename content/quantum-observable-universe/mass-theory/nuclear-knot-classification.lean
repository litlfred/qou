/-
  Nuclear knot classification: braid closure type determines binding scale.

  The closure of the nuclear braid 𝒩(Z,N) falls into one of four knot
  types. Each type determines the geometric invariant (Vol or CS) that
  sets the binding scale.

  Ref: [manuscript] §5.8, prop:nuclear-knot-classification
-/

import QOU.Torsion.HeckeMassElement
import QOU.Torsion.TopologicalMass

namespace QOU.BraidKnot

/-- Classification of nuclear braid closures by knot type. -/
inductive NuclearKnotType where
  | unknot      : NuclearKnotType   -- A = 1, trivial
  | satellite   : NuclearKnotType   -- A = 2, mixed topology
  | figureEight : NuclearKnotType   -- A = 3, Vol(4₁) = 2.030
  | borromean   : NuclearKnotType   -- A ≥ 4, Vol(B₃) = 7.328
  deriving DecidableEq, Repr

/-- The binding scale α depends on the knot type through its volume. -/
noncomputable def bindingScale (K : NuclearKnotType) (m_e : ℝ) : ℝ :=
  match K with
  | .unknot      => 0
  | .satellite   => m_e * 7.327724753846269  -- default Borromean
  | .figureEight => m_e * 2.029883212819307  -- Vol(4₁)
  | .borromean   => m_e * 7.327724753846269  -- Vol(B₃) = 8G

/-- The classification map itself: the mass number `A = Z + N` selects
    the closure type, exactly per the table annotated on
    `NuclearKnotType` above.

    **2026-08-21 (bean `qou/q407`).** This function did not exist. The
    table lived only in end-of-line comments on the constructors, so
    nothing in Lean connected `(Z, N)` to a knot type, and the theorem
    below could not be about the classification. -/
def nuclearKnotType (Z N : ℕ) : NuclearKnotType :=
  if Z + N ≤ 1 then .unknot
  else if Z + N = 2 then .satellite
  else if Z + N = 3 then .figureEight
  else .borromean

/-- **For A ≥ 4, the nuclear braid closure is Borromean.**

    **2026-08-21 (bean `qou/q407`).** The previous version was

    ```lean
    theorem nuclear_knot_classification (Z N : ℕ) (hA : Z + N ≥ 4) :
        ∃ K : NuclearKnotType, K = .borromean := ⟨.borromean, rfl⟩
    ```

    which says the constructor `.borromean` exists. `Z`, `N` and `hA`
    were all unused, so it held just as well for `A = 0`, and it would
    have survived any change to the classification it was named for.
    The claim needed a classification *map* to be about; the map is now
    `nuclearKnotType`, transcribed from the comments that already
    carried the table. -/
-- Ref: [manuscript] §5.8, prop:nuclear-knot-classification
theorem nuclear_knot_classification (Z N : ℕ) (hA : Z + N ≥ 4) :
    nuclearKnotType Z N = .borromean := by
  unfold nuclearKnotType
  rw [if_neg (by omega), if_neg (by omega), if_neg (by omega)]

/-- **Closure type determines the binding scale** — the proposition's
    own title, now derivable: at `A ≥ 4` the scale is the Borromean
    volume `Vol(B₃) = 8G`. -/
-- Ref: [manuscript] §5.8, prop:nuclear-knot-classification
theorem bindingScale_of_borromean (Z N : ℕ) (m_e : ℝ) (hA : Z + N ≥ 4) :
    bindingScale (nuclearKnotType Z N) m_e = m_e * 7.327724753846269 := by
  rw [nuclear_knot_classification Z N hA]
  simp [bindingScale]

end QOU.BraidKnot
