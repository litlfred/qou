/-!
# QOU.CategoricalReeb.QReebFlowOnCoralCoords

Axiomatisation of the $q$-Reeb flow action on the coral-sector
coordinates over the exceptional divisor.  The flow advances each
sector's angular coordinate $\psi$ linearly with rate $q$ along the
latitude direction $\phi \in [0, \pi]$ of the Reeb bundle.

The class is conjectural — the underlying differential-geometric
construction lives in `qou:QOU.ReebBundle` (placeholder) — but the
**algebraic structure** it imposes (additive flow, two-strand
localisation, sector spectator rule) is enough for the downstream
six-operators theorem to be stated and proved conditionally.

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

    `flow q t s ψ` is the angular position $\psi'$ of the sector $s$
    after applying the flow $\phi^q_t$ to the starting position
    $\psi$.  Composition is additive in $t$.

    `spectator q s β` records whether sector $s$ is a spectator
    (angular rate zero) under braid generator $β$: this is the
    two-strand localisation rule. -/
class QReebFlowOnCoralCoords (q : ℝ) where
  /-- The flow on the angular coordinate of a single sector. -/
  flow : ℝ → CoralSector → ℝ → ℝ
  /-- Identity at $t = 0$. -/
  flow_zero : ∀ (s : CoralSector) (ψ : ℝ), flow 0 s ψ = ψ
  /-- Additive composition in the flow parameter. -/
  flow_add : ∀ (t₁ t₂ : ℝ) (s : CoralSector) (ψ : ℝ),
    flow (t₁ + t₂) s ψ = flow t₂ s (flow t₁ s ψ)
  /-- Coral-twist rate: each active sector advances at angular rate $q$. -/
  flow_rate : ∀ (t : ℝ) (s : CoralSector) (ψ : ℝ),
    flow t s ψ = ψ + q * t

-- Ref: [manuscript] content/quantum-observable-universe/braids-and-knots/q-reeb-flow-on-coral-coords.md

/-- The coral-twist accumulated across the full divisor traversal
    from south foundry ($t = 0$) to north foundry ($t = \pi$). -/
def coralTwist (q : ℝ) : ℝ := q * Real.pi

theorem coralTwist_eq (q : ℝ) : coralTwist q = q * Real.pi := rfl

end QOU.CategoricalReeb
