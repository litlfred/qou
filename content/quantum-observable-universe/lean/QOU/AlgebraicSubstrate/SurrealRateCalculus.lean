import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.AlgebraicSubstrate.SurrealRateCalculus — rate table

Records the four classical-limit scaling laws of the QOU framework
as surreal-order inequalities:

- Mass gap `Δ_q ≍ ε^3` — positive infinitesimal of order 3.
- Reeb period `Ω_q ≍ ε⁻¹` — positive transfinite of order 1.
- Enstrophy ceiling `Z_q ≍ ε^(-4/3)` — transfinite of order 4/3.
- Rogue-zero cost `E(δ) ≍ δ² · ε⁻¹` — transfinite scaled by `δ²`.

Each is stated as a leading-coefficient equation on an abstract
field carrier `F`; downstream instances discharge by specialising
to `𝐍𝐨` via `QOU.AppendixSurreals.StandardPart`.  The class
requires only `[Field F]` — no ordering or positivity hypothesis;
those are added by downstream interpretations that need them
(e.g.\ to compare `Ow`-orders).

LaTeX label: `prop:surreal-rate-calculus`.

## References

- [conway1976] Conway, *On Numbers and Games*.
- [gonshor1986] Gonshor, *Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- The rate-table *shape*: a class recording the four
    classical-limit rates as data over an abstract field carrier `F`.

    An instance of this class fixes the leading-coefficient equations
    `Δ = ε³`, `Ω·ε = 1`, `Z³·ε⁴ = 1`, `E(δ)·ε = δ²` (each up to a
    positive scalar absorbed into the named quantity) and entails
    the rate table [`prop:surreal-rate-calculus`].  Under the surreal
    embedding `ε ↦ 1/ω`, these equations specialise to the
    `Ow`-valuations `Ow(Δ) = -3`, `Ow(Ω) = 1`, `Ow(Z) = 4/3`,
    `Ow(E(δ)) = 1` whenever `δ ≠ 0` (the rogue-zero equation
    `E(δ)·ε = δ²` holds for every `δ : F`; the `Ow = 1`
    interpretation requires `δ ≠ 0`). -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [manuscript] Chapter 8 §5 (Surreal rate calculus)
class SurrealRateCalculus (F : Type u) [Field F] where
  /-- The Reeb infinitesimal embedded in `F`.  Non-zero (forced
      by `reebPeriod_order : reebPeriod · epsilon = 1` below). -/
  epsilon : F
  /-- The mass gap. -/
  massGap : F
  /-- The Reeb period. -/
  reebPeriod : F
  /-- The enstrophy ceiling. -/
  enstrophyCeiling : F
  /-- Rogue-zero energy cost, parametrised by a standard-real drift. -/
  roguePartCost : F → F
  /-- Mass-gap leading-coefficient equation: `Δ = ε³`. -/
  massGap_order : massGap = epsilon ^ 3
  /-- Reeb-period leading-coefficient equation: `Ω · ε = 1`. -/
  reebPeriod_order : reebPeriod * epsilon = 1
  /-- Enstrophy leading-coefficient equation: `Z³ · ε⁴ = 1`
      (the cubic form of `Z = ε^(-4/3)`, avoiding fractional
      exponents at the type level). -/
  enstrophy_order : enstrophyCeiling ^ 3 * epsilon ^ 4 = 1
  /-- Rogue-zero leading-coefficient equation:
      `E(δ) · ε = δ²` for every drift `δ`. -/
  rogueZero_order : ∀ δ : F, roguePartCost δ * epsilon = δ ^ 2

/-- **Classical-limit instance** (ε = 1).
    At the classical limit, the Reeb infinitesimal collapses to 1
    and every rate equation becomes trivial:
    - `Δ = 1 = 1³` ✓
    - `Ω · 1 = 1 · 1 = 1` ✓
    - `Z³ · 1⁴ = 1 · 1 = 1` ✓
    - `E(δ) · 1 = δ² · 1 = δ²` ✓
    This is the "no infinitesimal" baseline; the substantive
    surreal content arises when ε is genuinely infinitesimal in
    `𝐍𝐨` via the standard-part embedding. -/
instance surrealRateCalculus_classicalLimit (F : Type u) [Field F] :
    SurrealRateCalculus F where
  epsilon := 1
  massGap := 1
  reebPeriod := 1
  enstrophyCeiling := 1
  roguePartCost := fun δ => δ ^ 2
  massGap_order := by norm_num
  reebPeriod_order := by norm_num
  enstrophy_order := by norm_num
  rogueZero_order := fun δ => by ring

end QOU.AlgebraicSubstrate
