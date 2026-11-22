import Mathlib.Data.List.Basic
import Mathlib.Tactic.Basic

/-!
# QOU.HorizonFunctor — Horizon functor

The horizon functor sends an aeon to its boundary (a list of jet horizons).

LaTeX label: `def:horizon-functor`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.HorizonFunctor` in jet-horizon.lean

## References
- [leitner2026] §9/horizon-functor
-/

-- Prerequisite types mirrored from the `QOU.JetHorizon` library module so this
-- co-location extract compiles standalone. The canonical definitions live in
-- `folio/quantum-observable-universe/lean/QOU/JetHorizon.lean` (Lake-built
-- under the `qou` package); these copies keep the file independently checkable
-- by `lean`-direct without depending on the (uncached) library olean.

namespace QOU

/-- Prerequisite type — canonical decl: `QOU.JetHorizon` in `QOU/JetHorizon.lean`.
    Re-declared here as an opaque carrier for co-location. -/
-- Ref: [leitner2026] def:jet-horizon
structure JetHorizon where
  /-- Opaque carrier of the jet-horizon datum. -/
  carrier : Type*

/-- Prerequisite type — canonical decl: `QOU.Aeon` in `QOU/JetHorizon.lean`.
    Re-declared here with the single `boundary` field this extract uses. -/
-- Ref: [leitner2026] def:aeon
structure Aeon where
  /-- Boundary: jet horizons reachable as limits of directed
      diagrams in the aeon. -/
  boundary : List JetHorizon

/-- The horizon functor: sends an aeon to its boundary. -/
-- Ref: [leitner2026] §9/horizon-functor
def horizonFunctor (a : Aeon) : List JetHorizon := a.boundary

end QOU
