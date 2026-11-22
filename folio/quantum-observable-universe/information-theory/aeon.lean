import Mathlib.Data.List.Basic
import Mathlib.Tactic.Basic

/-!
# QOU.Aeon — Aeon (connected component of the observable subcategory)

An aeon is a connected component of the observable subcategory
Bun°(P(V)), where A_0 ≠ 0.  Maximal collection of observable
configurations connected by flow maps without crossing a jet horizon.

LaTeX label: `def:aeon`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.Aeon` in jet-horizon.lean

## References
- [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
- [leitner2026] §9/aeon
-/

namespace QOU

/-- Prerequisite type — the canonical declaration is `QOU.JetHorizon`
    in `folio/quantum-observable-universe/lean/QOU/JetHorizon.lean`
    (Lake-built under the `qou` package).  Re-declared here as an
    opaque carrier so this co-located content-block sibling is
    independently checkable by `lean`-direct without importing the
    full `qou` library cone. -/
-- Ref: [leitner2026] def:jet-horizon
structure JetHorizon where
  /-- Opaque carrier of the jet-horizon datum. -/
  carrier : Type*

/-- Prerequisite type — the canonical declaration is
    `QOU.ObservableConfig` in `QOU/JetHorizon.lean`.  Re-declared
    here as an opaque carrier for the same co-location reason as
    `JetHorizon` above. -/
-- Ref: [leitner2026] def:observable-subcategory
structure ObservableConfig where
  /-- Opaque carrier of the observable configuration. -/
  carrier : Type*

/-- An aeon: a connected component of the observable subcategory
    Bun°(P(V)).  Maximal collection of observable configurations
    connected by flow maps without crossing a jet horizon. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [leitner2026] §9/aeon
structure Aeon where
  /-- The observable configurations in this aeon. -/
  configs : Type*
  /-- Each configuration is observable. -/
  observable : configs → ObservableConfig
  /-- A relation witnessing that two configs are connected by a
      flow map (one Planck step) within Bun°. -/
  flow_step : configs → configs → Prop
  /-- The flow relation is symmetric (reversible computation). -/
  flow_symm : ∀ x y, flow_step x y → flow_step y x
  /-- Connectedness: any two configs are related by a chain of
      flow steps. -/
  connected : ∀ (x y : configs),
    ∃ (path : List configs),
      path.head? = some x ∧ path.getLast? = some y ∧
      ∀ i : Fin (path.length - 1),
        flow_step (path.get ⟨i, by omega⟩) (path.get ⟨i + 1, by omega⟩)
  /-- Boundary: jet horizons reachable as limits of directed
      diagrams in the aeon. -/
  boundary : List JetHorizon

/-- Two aeons are adjacent if their boundaries share a common
    jet horizon: ∂𝒜₁ ∩ ∂𝒜₂ ≠ ∅. -/
def Aeon.adjacent (a₁ a₂ : Aeon) : Prop :=
  ∃ h, h ∈ a₁.boundary ∧ h ∈ a₂.boundary

end QOU
