import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.HadronFibreEmbedding — Fibre-compatible hadron embedding

A fibre-compatible embedding places a hadron into a fibre of the
brane tower, satisfying integrability, fibre confinement, Hopf
compatibility, and volume compatibility conditions.

**None of those four conditions is encoded below** (corrected 2026-09-14).
`HadronFibreEmbedding` carries the embedding's *data* only; the two fields
that once named conditions were typed with the universe `Prop`, so an
instance chose the proposition rather than proving it, and both are now
removed as measured-dead. See the structure's docstring.

## References

- [leitner2026] §3 Lifting and Descent

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The **data** of a fibre-compatible hadron embedding: a base point, its
    partner coordinate, and the embedding energy, all over `R_q`.

    LaTeX: `\label{def:hadron-fibre-embedding}`

    **This structure encodes NO conditions, and the docstring now says so.**
    The four the module header names — integrability, fibre confinement, Hopf
    compatibility, volume compatibility — are not fields here and never were
    encoded as propositions; a reader who needs one must state it separately
    against this data.

    **Both universe-`Prop` fields are now gone.** `integrable` was removed
    2026-09-07 as measured-dead. `confined` was KEPT at that time on the
    stated ground that "it is read by four declarations" — and that is a
    **name collision**, not a readership. Re-measured 2026-09-14 across the
    Lean tree:

    - `DownQuark.confined` / `UpQuark.confined` are `Bool` (`= true := rfl`);
    - `ConfinedParticle.confined` and
      `ConfinementPhaseStratification.confined` are applied to a parameter
      (`h.confined q`), so they are functions on a different carrier;
    - `confinedNet` is a different name again.

    There is **no** `.confined` projection on a `HadronFibreEmbedding` and
    **no** `confined :=` construction site anywhere, so the field was exactly
    as dead as `integrable`. Same disposition, same evidence, same file.

    The lesson generalises and is the one AGENTS.md records for `markovZ`:
    **a field name is not an identifier — resolve a "who reads this?" claim to
    the declaration, not to the token.** Consumption is not the test in any
    case; a field typed with the universe `Prop` is chosen by the constructor,
    so reading it constrains nothing even when the reader is genuine. -/
-- Ref: [leitner2026] §3, Definition: Fibre-compatible hadron embedding
structure HadronFibreEmbedding where
  /-- The base point in the projective line. -/
  theta : R_q
  phi : R_q
  /-- The embedding energy (from Möbius energy constraint). -/
  energy : R_q
  -- Energy is non-negative:
  -- energy_nonneg : 0 ≤ energy  -- (archimedean; not meaningful over R_q)

end

end QOU
