import Mathlib.Data.Real.Basic

/-!
# QOU.ArchimedeanUniverse.mi_sw_cartan_reduction

Content block
[`lem:mi-sw-abelianisation-cartan`](../../../quantum-observable-universe/archimedean-universe/mi-sw-abelianisation-cartan.md): *Cartan reduction recovers the Seiberg--Witten differential*.

## Lean structure

The claim is the geometric identification, on the exceptional divisor
`𝒮_c ≅ ℙ¹(ℂ)`, of the Cartan component `A⁰` of the reduced connection
with the local coordinate `1`-form `X · dz` and the Seiberg–Witten
differential `λ_SW`:

```
A⁰ = X · dz = λ_SW.
```

These three real quantities are opaque outputs of the abelianisation /
Cartan-reduction construction; there is no faithful Mathlib structure
that *forces* their equality, so neither pattern A (compute) nor
pattern B (Mathlib derive) applies.  Per the vacuity-fix playbook
(pattern C) the honest disposition is to **name** the conditional
conjecture as a `def : Prop` over the three quantities, rather than to
fake a proof by projecting a `claim_*` field that already asserts it.
Naming a construction is not a logical claim (AGENTS.md §3b).

## References

- [manuscript] quantum-observable-universe/archimedean-universe/mi-sw-abelianisation-cartan.md.
-/

namespace QOU.ArchimedeanUniverse

/-- **Statement** ([`lem:mi-sw-abelianisation-cartan`]):
    Cartan reduction recovers the Seiberg–Witten differential.

    On the exceptional divisor `𝒮_c ≅ ℙ¹(ℂ)` the principal
    `SU(2)`-bundle trivialises, the connection `∇_A` reduces to a
    `𝔰𝔲(2)`-valued `1`-form, and its Cartan component `A⁰` satisfies

    `A⁰ = X · dz = λ_SW`,

    recovering the Seiberg–Witten differential.

    This `def : Prop` **names** the conjectural identification over the
    three geometric quantities (the Cartan component `A_0`, the local
    coordinate form `X_dz`, and the SW differential `lambda_SW`); it is
    an open categorical fact, carried honestly rather than projected
    from a self-asserting class field. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/mi-sw-abelianisation-cartan.md
def mi_sw_cartan_reduction (A_0 X_dz lambda_SW : ℝ) : Prop :=
  A_0 = X_dz ∧ X_dz = lambda_SW

end QOU.ArchimedeanUniverse
