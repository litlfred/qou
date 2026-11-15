import QOU.Basic

/-!
# QOU.CategoricalReeb.QReebFlowOnColorCoords

Axiomatisation of the $q$-Reeb flow action on the color-sector
coordinates over the exceptional divisor.

The class encodes three pieces of structure:

1. **Additive composition** in the flow parameter.
2. **Per-sector signed rate**: each sector advances at angular
   rate $k\,q$, where $k \in \mathbb{Z}$ is a signed multiplier
   determined by the braid generator and the sector's role in
   the current two-strand subsystem.  Concretely: $k = 0$ for
   spectator sectors; $k = +1$ for the "leading" active sector
   under a positively-oriented generator (e.g. red under
   $\sigma_1$); $k = -1$ for the "partner" active sector whose
   angular coordinate counter-rotates so the two-strand
   centre-of-mass is preserved (e.g. green under $\sigma_1$);
   $k = +1$ uniformly under the positive 3-cycle
   $\sigma_1\sigma_2$; $k = -1$ uniformly under the negative
   3-cycle $\sigma_2\sigma_1$.

The signed-rate dictionary between braid generators and per-sector
multipliers is supplied by the consumer (see
`SixCanonicalKnotOperators`).

LaTeX label: `def:q-reeb-flow-on-color-coords`
-/

namespace QOU.CategoricalReeb

/-- The three color sectors over the exceptional divisor.  Each
sector carries an angular coordinate $\psi$; the latitude
coordinate $\phi$ is shared. -/
inductive ColorSector where
  | red
  | green
  | blue
deriving DecidableEq, Repr

/-- The $q$-Reeb flow on color-sector coordinates.

    `flow q t k ψ` is the angular position $\psi'$ of a sector
    after applying the flow $\phi^q_t$ to the starting position
    $\psi$, given the sector's signed rate multiplier `k : ℤ`
    under the current braid generator.

    Sectors with rate `k` advance at angular rate `k * q`; in
    particular `k = 0` gives the spectator rule and `k = ±1` the
    centre-of-mass-preserving two-strand action.  Composition is
    additive in $t$. -/
class QReebFlowOnColorCoords (q : ℝ) where
  /-- The flow on the angular coordinate.  `k` is the signed
      rate multiplier under the current braid generator. -/
  flow : ℝ → ℤ → ℝ → ℝ
  /-- Identity at $t = 0$ regardless of rate. -/
  flow_zero : ∀ (k : ℤ) (ψ : ℝ), flow 0 k ψ = ψ
  /-- Additive composition in the flow parameter (rate preserved
      across the composition step). -/
  flow_add : ∀ (t₁ t₂ : ℝ) (k : ℤ) (ψ : ℝ),
    flow (t₁ + t₂) k ψ = flow t₂ k (flow t₁ k ψ)
  /-- A sector with rate `k` advances at angular rate $k\,q$. -/
  flow_rate : ∀ (t ψ : ℝ) (k : ℤ),
    flow t k ψ = ψ + (k : ℝ) * q * t

namespace QReebFlowOnColorCoords

variable {q : ℝ} [QReebFlowOnColorCoords q]

/-- Corollary: spectator sectors ($k = 0$) are stationary. -/
theorem flow_spectator (t ψ : ℝ) : flow (q := q) t 0 ψ = ψ := by
  simp [flow_rate]

/-- Corollary: leading active sectors ($k = +1$) advance at rate $+q$. -/
theorem flow_active_pos (t ψ : ℝ) :
    flow (q := q) t 1 ψ = ψ + q * t := by
  simp [flow_rate]

/-- Corollary: partner active sectors ($k = -1$) advance at rate $-q$. -/
theorem flow_active_neg (t ψ : ℝ) :
    flow (q := q) t (-1) ψ = ψ - q * t := by
  simp [flow_rate]; ring

end QReebFlowOnColorCoords

-- Ref: [leitner2026] folio/quantum-observable-universe/braids-and-knots/q-reeb-flow-on-color-coords.md

/-- The color-twist accumulated by a $k = +1$ sector over the full
    divisor traversal of latitude length `T`.  At `T = π` this is
    the substrate-parameter advance of `q π`. -/
def colorTwist (q T : ℝ) : ℝ := q * T

theorem colorTwist_eq (q T : ℝ) : colorTwist q T = q * T := rfl

end QOU.CategoricalReeb
