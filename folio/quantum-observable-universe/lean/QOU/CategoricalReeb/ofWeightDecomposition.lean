import Mathlib.Data.Real.Basic

/-!
# QOU.CategoricalReeb.ofWeightDecomposition

Canonical Lean declaration for content block at
[`quantum-observable-universe/quantum-observable-universes/categorical-reeb-exists.ts`](quantum-observable-universe/quantum-observable-universes/categorical-reeb-exists.ts).

Given a quantum observable universe `(C, A, τ)` with maximal torus `T`
and weight decomposition `(π_H, π_V)`, there exists a categorical Reeb
derivation `(ξ, Θ_A)` on `A` satisfying the **normalisation** condition
`Θ_A(ξ x) = 1` for every element `x`.

The normalisation condition is irreducibly abstract over the opaque
categorical object `A` and its endomorphism `ξ` / contact form `Θ_A`; no
Mathlib structure makes it tautologous.  We therefore **name** the
conditional conjecture as a `Prop` (pattern C of the vacuity-fix
playbook): for a categorical object equipped with `ξ` and `Θ_A`,
`ofWeightDecomposition` is the proposition that the Reeb-normalisation
holds.  The self-assuming `claim_ofWeightDecomposition` carrier field of
the old encoding is removed; inhabiting the proposition is the open
conditional claim, not faked by a projection.
-/

namespace QOU.CategoricalReeb

/-- **Categorical Reeb normalisation** (named conditional conjecture).

For a categorical object `A` equipped with a Reeb endomorphism
`ξ : A → A` and a contact 1-form `Θ_A : A → ℝ` (the scalar evaluation of
`Θ_A : A → 𝟙`), `ofWeightDecomposition ξ Θ_A` is the proposition that the
**normalisation** condition

`∀ x, Θ_A (ξ x) = 1`     (categorically `Θ_A ∘ ξ = id_𝟙`)

holds.  This names the conditional claim of the categorical-Reeb
existence proposition (pattern C); it is *not* asserted — an inhabitant
witnesses the Reeb-derivation normalisation. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/categorical-reeb-exists.ts
def ofWeightDecomposition {A : Type*} (ξ : A → A) (Θ_A : A → ℝ) : Prop :=
    ∀ x : A, Θ_A (ξ x) = 1

end QOU.CategoricalReeb
