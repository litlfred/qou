/-!
# QOU.HorizonFunctor — Horizon functor

The horizon functor sends an aeon to its boundary (a list of jet horizons).

LaTeX label: `def:horizon-functor`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.HorizonFunctor` in jet-horizon.lean

## References
- [manuscript] §9/horizon-functor
-/

-- Prerequisite types from jet-horizon.lean
-- (not independently compilable; see jet-horizon.lean for full context)

namespace QOU

/-- The horizon functor: sends an aeon to its boundary. -/
-- Ref: [manuscript] §9/horizon-functor
def horizonFunctor (a : Aeon) : List JetHorizon := a.boundary


/-- **def:horizon-functor** — placeholder stub; full definition TBD. -/
structure HorizonFunctor where
  witness : ℝ
  witness_pos : 0 < witness
end QOU
