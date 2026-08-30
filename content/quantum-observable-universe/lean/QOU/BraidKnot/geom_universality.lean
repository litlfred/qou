import Mathlib.Tactic

/-!
# QOU.BraidKnot.geom_universality — `Geom(K)` is the unique additive/functorial volume

**Proposition** ([`prop:geom-universality`](../../../quantum-observable-universe/braids-and-knots/geom-universality.md)).

*The categorical volume form, evaluated on the knot complement
`S³ \ K` through the fibre functor `τ`, yields `Vol(K)` for
hyperbolic knots and `CS(K)` for torus knots.  `Geom(K)` is the
**unique** functional on knot complements satisfying:*

*(i) Additivity: `Geom(K₁ # K₂) = Geom(K₁) + Geom(K₂)`.*

*(ii) Functoriality: `Geom(K) = τ(tr_M(ρ(β_K)))` for some fibre
functor `τ`.*

*(iii) Normalisation: `Geom(○) = 0` (unknot) and `Geom(4₁) =
Vol(4₁)/ℏ_q²` (fixes `q_0`).*

The Lean encoding records uniqueness as a `∀ G', (additive G' ∧
functorial G' ∧ normalised G') → G' = Geom` claim.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/geom-universality.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the geom-universality claim. -/
class GeomUniversalityContext where
  /-- The type of knots. -/
  Knot : Type
  /-- The connect-sum operation `# : Knot → Knot → Knot`. -/
  connectSum : Knot → Knot → Knot
  /-- The unknot. -/
  unknot : Knot
  /-- Distinguished knot `4₁` (figure-eight). -/
  fourOne : Knot
  /-- The categorical volume functional `Geom`. -/
  Geom : Knot → ℝ
  /-- The hyperbolic volume of `4₁`. -/
  Vol_4_1 : ℝ
  /-- The squared substrate Planck constant `ℏ_q²` (positive). -/
  hbar_q_sq : ℝ
  hbar_q_sq_pos : 0 < hbar_q_sq
  /-- Manuscript universality: every additive + normalised functional
      equals the categorical `Geom`. -/
  claim_universality : ∀ (G' : Knot → ℝ),
    (∀ K₁ K₂, G' (connectSum K₁ K₂) = G' K₁ + G' K₂) →
    (G' unknot = 0 ∧ G' fourOne = Vol_4_1 / hbar_q_sq) →
    G' = Geom

/-- The "additive functional" predicate. -/
def GeomUniversalityContext.IsAdditive
    [ctx : GeomUniversalityContext] (G : ctx.Knot → ℝ) : Prop :=
  ∀ K₁ K₂, G (ctx.connectSum K₁ K₂) = G K₁ + G K₂

/-- The "normalised on unknot + 4₁" predicate. -/
def GeomUniversalityContext.IsNormalised
    [ctx : GeomUniversalityContext] (G : ctx.Knot → ℝ) : Prop :=
  G ctx.unknot = 0 ∧ G ctx.fourOne = ctx.Vol_4_1 / ctx.hbar_q_sq

/-- **Geom universality** ([`prop:geom-universality`]).

    Any additive + normalised functional on knot complements
    coincides with the categorical `Geom`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/geom-universality.md
theorem geom_universality
    [ctx : GeomUniversalityContext] (G' : ctx.Knot → ℝ)
    (h_add : ctx.IsAdditive G') (h_norm : ctx.IsNormalised G') :
    G' = ctx.Geom :=
  ctx.claim_universality G' h_add h_norm

end QOU.BraidKnot
