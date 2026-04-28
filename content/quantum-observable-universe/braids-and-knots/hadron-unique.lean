/-!
# QOU.Hadron.unique_up_to_isotopy — uniqueness of hadrons up to isotopy

Hecke normal form is unique in H_n(q); Markov trace is isotopy-invariant.

LaTeX: `\label{prop:hadron-unique}`

## References

- [manuscript] §4-braids-and-knots/hadron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of hadrons up to braid isotopy — open statement.**

    The intended uniqueness fact is: two hadrons with the same
    crossing partition, localisation point, and Hecke normal form
    coincide *up to braid isotopy* (Markov-trace-equivalence).

    The `Subsingleton Hadron` claim originally written here is
    **strictly false** because the `Hadron` structure has free fields:

      `theta : R_q`     (no constraint)
      `phi   : R_q`     (no constraint)
      `constituents : List PlanarDiagram` (only `length ≥ 2` required)

    Distinct values for any of these give distinct `Hadron` terms
    that are equally valid. `Subsingleton` therefore cannot hold.

    To make this theorem provable, the conclusion must be sharpened
    to one of:

    1. A binary equivalence-up-to-isotopy relation `≈_isotopy` on
       `Hadron`, with an `Equivalence` proof + a `Subsingleton`-style
       statement at the *quotient* level.
    2. A coercion to a Markov-class invariant (e.g. the Jones
       polynomial of the closure) plus injectivity of that invariant
       under specified hypotheses (Jones 1987 + Reshetikhin-Turaev).

    Closing-as-written would let a false claim through; the
    `sorry` is retained with this diagnosis. -/
-- Ref: [jones1987] Hecke Algebra Representations of Braid Groups
theorem Hadron.unique_up_to_isotopy : Subsingleton Hadron := by
  -- Subsingleton claim is too strong (see docstring); Hadron's free
  -- fields admit distinct terms.
  sorry  -- Ref: [jones1987] — but theorem statement needs revision; see docstring

end QOU
