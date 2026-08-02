import Mathlib.Tactic

/-!
# QOU.BraidKnot.six_term_mass_formula_complete — six-term unified mass formula

**Proposition** ([`prop:six-term-mass-formula-complete`](../../../quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md)).

*The categorical mass of a vortex `ϱ` decomposes as a sum of six
terms:*

```
  𝔪(ϱ) = |tr_M(T_w)|                                  (Term 1)
       + Σ_i Φ_q(|V̂_i^full|)                         (Term 2)
       + z² Σ_{i<j} Φ_q(|V̂_i^full V̂_j^full|)        (Term 3)
       + ... + Terms 4, 5, 6
```

Lean encoding records the six addends as fields of an abstract
context plus a sum identity.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the six-term mass formula.  The decomposition is a
    pure additive identity, so the base ring need only be a commutative
    additive monoid `[AddCommMonoid R]` (§7c) — the six-term sum uses `+` and
    the additive identity `0`, with no ordering or multiplication; the archimedean
    specialisation `R := ℝ` is a downstream instantiation, not baked in here. -/
class SixTermMassFormulaContext (R : Type*) [AddCommMonoid R] where
  /-- The six addends (in the generic base ring `R`). -/
  term1 : R
  term2 : R
  term3 : R
  term4 : R
  term5 : R
  term6 : R
  /-- The categorical mass `𝔪(ϱ)`. -/
  cat_mass : R
  /-- Manuscript six-term decomposition: `𝔪(ϱ) = Σ_{i=1}^{6} term_i`. -/
  claim_six_term_sum :
    cat_mass = term1 + term2 + term3 + term4 + term5 + term6

/-- **Six-term unified mass formula** ([`prop:six-term-mass-formula-complete`]).

    `𝔪(ϱ) = term1 + term2 + term3 + term4 + term5 + term6`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md
def six_term_mass_formula_complete {R : Type*} [AddCommMonoid R]
    [ctx : SixTermMassFormulaContext R] :
    ctx.cat_mass = ctx.term1 + ctx.term2 + ctx.term3
                 + ctx.term4 + ctx.term5 + ctx.term6 :=
  ctx.claim_six_term_sum

end QOU.BraidKnot
