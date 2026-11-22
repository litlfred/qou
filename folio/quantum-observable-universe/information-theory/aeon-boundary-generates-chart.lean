import Mathlib.Tactic

/-!
# Aeon boundary generates a chart (conjectural)

Class-axiomatised stub for `conj:aeon-boundary-generates-chart`:
the composition `Φ_1^q ∘ CMB` lands in `Bun°` — the first Planck
step of the torsion flow, applied to the CMB of an aeon, produces
an object whose degree-0 fibre is non-trivial, i.e. inside `Bun°`.

Per `AGENTS.md §3b-cond`, the conjecture's content is encoded as
an `opaque Prop` and the class instance has that Prop as its sole
field with body `sorry` — the sorry IS the conjecture, not missing
proof.

## References

- `[leitner2026]` `conj:aeon-boundary-generates-chart`
- `[leitner2026]` `def:cmb-functor`
- `[leitner2026]` `def:torsion-knot-flow`
-/

namespace QOU.AeonBoundary

/-- **The aeon-recycling Prop.**

    Opaque proposition asserting the conjecture's content: for the
    given parameter type `V` (the projective fibre over which the
    bundles live), the composition `Φ_1^q ∘ CMB` is well-defined
    on `π₀(Bun°)` and lands back inside `Bun°(ℙ(V))`. -/
opaque AeonRecyclingHolds (V : Type*) : Prop

/-- **Aeon recycling conjecture** (axiomatised as a class per
    AGENTS.md §3b-cond). Downstream theorems may take
    `[AeonRecycling V]` as a class hypothesis and inherit the
    conjectural assumption explicitly. -/
class AeonRecycling (V : Type*) : Prop where
  /-- The aeon-recycling proposition holds. The `sorry` in the
      canonical instance IS the conjecture. -/
  recycling_holds : AeonRecyclingHolds V

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the field(s) below, which is
-- exactly the open conjecture; supplying one asserts the conjecture.
--
-- History: this file previously carried
--     instance aeon_recycling_conjecture (V : Type*) : AeonRecycling V where
--     axiom aeon_recycling_holds : ∀ (V : Type*), AeonRecyclingHolds V
-- i.e. the conjecture was discharged by `axiom` and installed as a global
-- instance, so every downstream `[AeonRecycling]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  Removed, not completed.
-- Downstream results must take `[AeonRecycling]` as an explicit hypothesis.

end QOU.AeonBoundary
