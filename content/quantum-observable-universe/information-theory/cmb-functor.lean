/-!
# QOU.CMBFunctor — CMB functor

The CMB functor extracts degree ≥ 1 jet data surviving a boundary horizon.
Composition of the horizon functor ∂ with the colimit of (A₁/A₀ ⊕ A₂/A₀)
over the boundary.

LaTeX label: `def:cmb-functor`

Formalization: extracted from jet-horizon.lean for content-block co-location.
Source declaration: `QOU.CMBFunctor` in jet-horizon.lean

## References
- [manuscript] §9/cmb-functor
-/

-- Prerequisite types from jet-horizon.lean
-- (not independently compilable; see jet-horizon.lean for full context)

namespace QOU

/-- The CMB functor value: the degree ≥ 1 data surviving a
    boundary horizon. Composition of ∂ with the colimit of
    (A_1/A_0 ⊕ A_2/A_0) over the boundary. -/
-- Ref: [manuscript] §9/cmb-functor
structure CMBFunctorValue where
  /-- The source aeon. -/
  source : Aeon
  /-- The boundary horizon from which CMB data is extracted. -/
  horizon : JetHorizon
  /-- The horizon is in the aeon's boundary. -/
  in_boundary : horizon ∈ source.boundary
  /-- The CMB data at this horizon. -/
  cmb : CMBBoundaryDatum
  /-- The CMB's algebra matches the horizon's algebra. -/
  algebra_match : cmb.source.algebra = horizon.algebra

end QOU
