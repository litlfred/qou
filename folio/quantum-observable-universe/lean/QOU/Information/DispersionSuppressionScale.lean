import Mathlib.Data.Real.Basic

/-!
# QOU.Information.DispersionSuppressionScale

Canonical Lean for content block
[`conj:dispersion-suppression-scale`](../../../quantum-observable-universe/information-theory/dispersion-suppression-scale.md).

## Why this is a `def` and not a `theorem`

An earlier revision read

```lean
theorem dispersion_suppression_scale (q : ℝ) (E_QG : ℝ) : Prop :=
  ∃ fractional_variation : ℝ → ℝ, ∀ E : ℝ, E > 0 → fractional_variation E ≤ E / E_QG
```

which had two independent problems:

1. **It proved nothing.** Its *type* is `Prop`, so the declaration is a term of
   type `Prop` — a proposition — not a proof of one. Labelling it `theorem`
   claimed a proof that does not exist (AGENTS.md §1a).
2. **The proposition it named was content-free.** The existential is witnessed
   by any sufficiently negative function (`fun _ => -1`), so it asserts nothing
   about the physical dispersion. `q` was unused.

The honest form is a *named predicate* on a given fractional-variation
function — which is what the docstring's "Pattern C — named proposition"
intends. Quantifying the variation function existentially is what destroyed the
content; taking it as a parameter restores it.

The block is a `conjecture`, so no proof or instance is offered here: the open
claim is that the QOU's archimedean projection *satisfies* this predicate for a
suppression scale at or above the Planck energy.

-- Ref: [abdo2009] https://doi.org/10.1038/nature08574
-/

namespace QOU.Information.DispersionSuppressionScale

/-- **Archimedean suppression of the substrate `q`-dispersion.**

    `dispersion_suppression_scale v E_QG` holds when the residual fractional
    variation `v` of the archimedean photon group velocity is bounded by
    `𝔈 / 𝔈_QG` at every positive photon energy `𝔈`.

    A predicate on the variation function, not an existential over it: the
    existential form is satisfied by any negative constant and so says nothing
    (see the module docstring). -/
def dispersion_suppression_scale (fractionalVariation : ℝ → ℝ) (E_QG : ℝ) : Prop :=
  ∀ E : ℝ, 0 < E → fractionalVariation E ≤ E / E_QG

end QOU.Information.DispersionSuppressionScale
