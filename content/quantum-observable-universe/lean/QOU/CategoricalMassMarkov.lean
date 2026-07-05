import Mathlib.Tactic

/-!
# QOU.CategoricalMassMarkov

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-endomorphism/categorical-mass-markov-trace-endomorphism-intro.ts`](quantum-observable-universe/mass-endomorphism/categorical-mass-markov-trace-endomorphism-intro.ts).

Formalises the introductory structural datum of the Markov-trace mass-
endomorphism arc: the categorical mass is pinned by a Markov-trace
endomorphism `Φ` on the substrate algebra, together with the global sections
`φ_n` that close the foundations arc. This is an overview block; the carrier
names the endomorphism as an additive map (its content is developed in the
downstream blocks). Generic ring (§7c-clean).
-/

namespace QOU

/-- Data for the categorical-mass Markov-trace endomorphism.

    A `definition` carrier: the substrate algebra `A`, the Markov-trace mass
    endomorphism `Φ` (an additive map), and the family of global sections
    `φ : ℕ → A` (the `φ_n` closing the arc). -/
structure CategoricalMassMarkov (A : Type*) [Ring A] where
  /-- The Markov-trace mass endomorphism `Φ`. -/
  Φ : A →+ A
  /-- The global sections `φ_n`. -/
  φ : ℕ → A

namespace CategoricalMassMarkov

variable {A : Type*} [Ring A] (M : CategoricalMassMarkov A)

/-- The mass endomorphism preserves the zero state (it is additive). -/
theorem Phi_zero : M.Φ 0 = 0 := map_zero M.Φ

/-- The mass endomorphism is additive on the substrate. -/
theorem Phi_add (a b : A) : M.Φ (a + b) = M.Φ a + M.Φ b := map_add M.Φ a b

end CategoricalMassMarkov

-- Ref: [manuscript] quantum-observable-universe/mass-endomorphism/categorical-mass-markov-trace-endomorphism-intro.ts

end QOU
