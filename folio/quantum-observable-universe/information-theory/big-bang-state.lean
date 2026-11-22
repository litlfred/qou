import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Basic

/-!
# QOU.BigBangState — Big bang state (degree-0 trivial configuration)

A big bang state is a jet horizon used as a reference configuration:
the degree-0 algebra A_0 vanishes, but higher-degree jet data persists.

LaTeX label: `def:big-bang-state`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.BigBangState` in jet-horizon.lean

## References
- [leitner2026] §9/big-bang-state
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

/-- A big bang state: a bundle initial condition where A_0 = 0.
    Algebraically identical to a jet horizon but used as a
    reference configuration rather than a boundary.

    Existence is not assumed: whether any affine chart admits
    a big bang state is a dynamical question. -/
-- Ref: [leitner2026] §9/big-bang-state
-- See: jet-horizon.lean § "Jet horizon" for prerequisite JetHorizon
structure BigBangState extends JetHorizon where
  /-- Number of base points in the initial configuration. -/
  numBasePoints : ℕ
  /-- At least one base point. -/
  nonempty : numBasePoints ≥ 1

end QOU
