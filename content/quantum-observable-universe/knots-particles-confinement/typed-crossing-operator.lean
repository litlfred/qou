-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Typed crossing operator C(fᵢ, fⱼ; σₖ) ∈ H₃(q)

/-- Quark flavor type. -/
inductive QuarkFlavor where
  | up   : QuarkFlavor
  | down : QuarkFlavor
  deriving DecidableEq, Repr

/-- Crossing type determined by the two quark flavors. -/
inductive CrossingType where
  | sameUp   : CrossingType  -- up-up: bare generator σₖ
  | sameDown : CrossingType  -- down-down: inverse σₖ⁻¹ = σₖ − HA
  | mixed    : CrossingType  -- up-down or down-up: mean ½(σₖ + σₖ⁻¹)
  deriving DecidableEq, Repr

/-- Classify a quark flavor pair into a crossing type. -/
def crossingTypeOf (f₁ f₂ : QuarkFlavor) : CrossingType :=
  match f₁, f₂ with
  | .up, .up     => .sameUp
  | .down, .down => .sameDown
  | _, _         => .mixed

/-- The **typed crossing operator** `C(fᵢ, fⱼ; σₖ)`.
    Three cases from the Hecke relation:
    - Up-up: eigenvalue `q`
    - Down-down: eigenvalue `−q⁻¹`
    - Mixed: arithmetic mean, eigenvalue `½(q − q⁻¹)` -/
structure TypedCrossingOperator where
  crossType : CrossingType
  generatorIndex : Nat  -- 0 or 1 for H₃(q)
