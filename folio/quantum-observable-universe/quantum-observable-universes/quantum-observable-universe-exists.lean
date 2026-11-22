import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumObservableUniverse.exists_instance — existence of QOU

A QOU structure exists: Rep(SU_q(2)) is a witness with Haar integration,
vanishing Chern classes on Ad, and the quantum determinant as the
volume constraint.

## The hypotheses are ring conditions, not a field

This statement asked for `[Field k]` and quantified over **every** field until
2026-08-16.  Both halves were wrong, in opposite directions.

*Too strong*, because the field is not load-bearing.  Reading the corpus for
what the cited construction actually needs:

| ingredient | condition | source |
|---|---|---|
| `U_q(sl₂)` Hopf algebra | `q − q⁻¹` invertible in `R` | `prop:q-casimir-exists` |
| `H_n(q)` semisimple | `6 ∈ R^×`, `q` not a root of unity | `descartes-knot-eigenbasis-derivation` (Jimbo) |
| the same, formally | `WenzlGeneric q n` | `QOU.Information.WenzlGeneric` |
| the algebra's home | Lusztig integral form over `ℤ[q,q⁻¹]` | `substrate-parameter-limits-and-lusztig` |

Every one is a **unit or genericity condition on a commutative ring**.  None
asks for a field.  Only complete reducibility of *every* `R`-module would, and
`QuantumUniverse` never requires that — its axiom 4 constrains the blocks of
`A`, not the ambient category.

*Too weak*, because `∀ k, [Field k]` is false where no generic `q` exists —
`𝔽₂` has no `q ∉ {0, 1}` at all, so the cited witness cannot be built there.
Quantifying over all fields asserted more than the citation supports while
excluding `ℤ[q,q⁻¹]`, the framework's own ground ring.

The hypotheses below are the honest replacement: narrower than "every field",
broader than "some field".

## What is still open

The `sorry` is unchanged and this is **not** progress toward discharging it —
only a correction of what must be proved.  The remaining work is the Drinfeld–
Jimbo representation category itself.

Note this does **not** follow from `QOU.TrivialWitness`: at `A = 𝟙` the
augmentation ideal vanishes, so `adjoint_nontrivial` fails and the trivial
witness gives a `QuantumUniverse` only.  A genuinely non-trivial `A` is required
here, which is what the `[kassel1995]` citation was always about.

LaTeX: `\label{prop:quantum-observable-universe-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/quantum-observable-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §IX (quantum SU(2))
- [wenzl1988] https://doi.org/10.1007/BF01404457
-/

namespace QOU

universe w

/-- **Existence of a quantum observable universe over a commutative ring.**

    `R` is a commutative ring carrying a substrate parameter `q` with named
    inverse `qinv`, subject to the three conditions the cited construction
    needs: `q − qinv` invertible (for the `q`-Casimir), `6` invertible and `q`
    Wenzl-generic at every rank (for semisimplicity of `H_n(q)` via Jimbo).

    `hgeneric` is `∀ n, WenzlGeneric q n` written out — that definition
    (`QOU.Information.WenzlGeneric`, `∀ k, 2 ≤ k → k ≤ n → q ^ k ≠ 1`) is
    already stated over a generic monoid, so it applies to `R` unchanged.  It
    is spelled inline rather than imported: `PNeqNpEquivalence` is a heavy
    Information-chapter module and this is a content-block sibling, so pulling
    it in for one `Prop` would bloat the import cone.  Restating it as a
    *definition* here was the other option and is worse — a second
    `WenzlGeneric` is exactly the symbol collision the notation register warns
    about.  Quantified over all `k` since `∀ n` makes the rank bound vacuous.

    Witnessed by Rep(SU_q(2)) with Haar integration, vanishing Chern classes on
    the adjoint, and the quantum determinant volume constraint. -/

-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IX (quantum SU(2))
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Stated, not proved (bean qou-6qbv): until 2026-11-20 this was discharged by
-- projecting a context-class field `exists_instance : Nonempty …`, i.e. the
-- conclusion was assumed. The honest state is a cited sorry; the obstruction
-- `QOU.WitnessObstruction.qou_needs_nongenerating_unit` prunes where a witness
-- can live (not in a module category) and does not discharge it.
theorem QuantumObservableUniverse.exists_instance
    (R : Type w) [CommRing R] (q qinv : R)
    (hq : q * qinv = 1)
    (hcasimir : IsUnit (q - qinv))
    (hsix : IsUnit (6 : R))
    (hgeneric : ∀ k : ℕ, 2 ≤ k → q ^ k ≠ 1) :
    Nonempty (QuantumObservableUniverse.{w + 1, w, w, w} R) := by
  sorry

end QOU
