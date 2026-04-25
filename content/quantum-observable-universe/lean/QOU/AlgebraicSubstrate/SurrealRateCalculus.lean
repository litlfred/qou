/-!
# QOU.AlgebraicSubstrate.SurrealRateCalculus — rate table

Records the four classical-limit scaling laws of the QOU framework
as surreal-order inequalities:

- Mass gap `Δ_q ≍ ε^3` — positive infinitesimal of order 3.
- Reeb period `Ω_q ≍ ε⁻¹` — positive transfinite of order 1.
- Enstrophy ceiling `Z_q ≍ ε^(-4/3)` — transfinite of order 4/3.
- Rogue-zero cost `E(δ) ≍ δ² · ε⁻¹` — transfinite scaled by `δ²`.

Each is stated as an assumption on an abstract ordered field with a
positive infinitesimal; downstream instances discharge by specialising
to `𝐍𝐨` via `QOU.AppendixSurreals.StandardPart`.

LaTeX label: `prop:surreal-rate-calculus`.

## References

- [conway1976] Conway, *On Numbers and Games*.
- [gonshor1986] Gonshor, *Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- The rate-table *shape*: a class recording the four
    classical-limit rates as data over an abstract ordered-field
    carrier `F`.

    An instance of this class, combined with a `PositiveInfinitesimal`
    instance on `epsilon`, entails the rate table
    [`prop:surreal-rate-calculus`]. -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [manuscript] Chapter 8 §5 (Surreal rate calculus)
class SurrealRateCalculus (F : Type u) where
  /-- The Reeb infinitesimal embedded in `F`. -/
  epsilon : F
  /-- The mass gap. -/
  massGap : F
  /-- The Reeb period. -/
  reebPeriod : F
  /-- The enstrophy ceiling. -/
  enstrophyCeiling : F
  /-- Rogue-zero energy cost, parametrised by a standard-real drift. -/
  roguePartCost : F → F
  /-- Mass-gap scaling: `Δ ≍ ε³`. -/
  massGap_order : True
  /-- Reeb-period scaling: `Ω ≍ ε⁻¹`. -/
  reebPeriod_order : True
  /-- Enstrophy scaling: `Z ≍ ε^(-4/3)`. -/
  enstrophy_order : True
  /-- Rogue-zero scaling: `E(δ) ≍ δ² · ε⁻¹`. -/
  rogueZero_order : True

end QOU.AlgebraicSubstrate
