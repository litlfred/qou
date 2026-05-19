import QOU.Basic

/-!
# QOU.CategoricalReeb.QReebFlowOnCoralCoords

Axiomatisation of the $q$-Reeb flow action on the coral-sector
coordinates over the exceptional divisor.

The class encodes three pieces of structure:

1. **Additive composition** in the flow parameter.
2. **Active sector rate**: when a sector participates in the
   current two-strand subsystem (e.g. red and green under
   $\sigma_1$), its angular coordinate advances at rate $q$.
3. **Spectator rule**: when a sector is not participating
   (e.g. blue under $\sigma_1$), its angular coordinate is
   stationary.

The active / spectator status is encoded by a `Bool` argument
to `flow`, leaving the dictionary between braid generators and
active sectors to be supplied by the consumer (see
`SixCanonicalKnotOperators`).

LaTeX label: `def:q-reeb-flow-on-coral-coords`
-/

namespace QOU.CategoricalReeb

/-- The three coral sectors over the exceptional divisor.  Each
sector carries an angular coordinate $\psi$; the latitude
coordinate $\phi$ is shared. -/
inductive CoralSector where
  | red
  | green
  | blue
deriving DecidableEq, Repr

/-- The $q$-Reeb flow on coral-sector coordinates.

    `flow q t active ψ` is the angular position $\psi'$ of a
    sector after applying the flow $\phi^q_t$ to the starting
    position $\psi$, given the sector's active/spectator status
    `active : Bool` under the current braid generator.

    Active sectors rotate at rate $q$; spectator sectors are
    stationary.  Composition is additive in $t$. -/
class QReebFlowOnCoralCoords (q : ℝ) where
  /-- The flow on the angular coordinate.  `active = true` means
      the sector participates in the current braid generator's
      two-strand subsystem; `active = false` means it is a
      spectator. -/
  flow : ℝ → Bool → ℝ → ℝ
  /-- Identity at $t = 0$. -/
  flow_zero : ∀ (active : Bool) (ψ : ℝ), flow 0 active ψ = ψ
  /-- Additive composition in the flow parameter (active state
      preserved across the composition step). -/
  flow_add : ∀ (t₁ t₂ : ℝ) (active : Bool) (ψ : ℝ),
    flow (t₁ + t₂) active ψ = flow t₂ active (flow t₁ active ψ)
  /-- Active sectors advance at angular rate $q$. -/
  flow_active : ∀ (t ψ : ℝ), flow t true ψ = ψ + q * t
  /-- Spectator sectors are stationary. -/
  flow_spectator : ∀ (t ψ : ℝ), flow t false ψ = ψ

-- Ref: [manuscript] content/quantum-observable-universe/braids-and-knots/q-reeb-flow-on-coral-coords.md

/-- The coral-twist accumulated by an active sector over the full
    divisor traversal of latitude length `T`.  At `T = π` this is
    the substrate-parameter advance of `q π`. -/
def coralTwist (q T : ℝ) : ℝ := q * T

theorem coralTwist_eq (q T : ℝ) : coralTwist q T = q * T := rfl

end QOU.CategoricalReeb
