import Mathlib.Tactic
import QOU.Torsion.HeckeMassElement

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

## De-axiomatisation (bean `2g2u`)

The carrier's two fields `Φ` and `φ` are no longer *free* data. Given the real
`HeckeMassElement Φ_mass(β)` (`QOU.Torsion.HeckeMassElement`, which already
carries the genuine `Φ_mass = Φ^desc + Φ^trans` decomposition and its
Markov-trace mass), `ofHecke` **derives** both:

- `Φ` is *left multiplication by the mass element* `a ↦ Φ_mass · a` — a genuine
  `AddMonoidHom` (additivity is `mul_add`, not a posited field), so the "mass
  endomorphism is additive" is a theorem about a concrete map, not an axiom;
- `φ_n` is the *Φ-orbit* of the mass element `Φ^[n](Φ_mass)` — the level-`n`
  global sections realised as brane-level iterates, with `φ_0 = Φ_mass` and
  `φ_{n+1} = Φ(φ_n)` both proved.

This is an honest cross-wire to the existing formalisation, not illustrative
inhabitation (a dummy `Φ := id`, `φ := 0` would compile but carry no content).
The open *closed-form* of `Φ_mass` itself is the separate research conjecture
`conj:mass-endomorphism` (see `QOU.MassEndomorphism.VolumeBridge`), not this
intro carrier.
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

/-- **De-axiomatisation (bean `2g2u`): cross-wire to the real Hecke mass
    element.** From `Φ_mass(β) ∈ H_n(R,q)` (a `HeckeMassElement`), build the
    categorical-mass carrier with:

    - `Φ := (Φ_mass · —)`, left multiplication by the mass element — a genuine
      `AddMonoidHom` whose additivity is `mul_add`, so `Φ` is *derived*, not
      a posited field;
    - `φ n := Φ^[n](Φ_mass)`, the Φ-orbit of the mass element (the level-`n`
      brane sections closing the arc).

    Requires `[CommRing A]` (the ground ring of the Hecke mass element); the
    carrier itself stays over generic `[Ring A]`. -/
def CategoricalMassMarkov.ofHecke {A : Type*} [CommRing A]
    (Φmass : QOU.Braiding.HeckeMassElement A) : CategoricalMassMarkov A where
  Φ :=
    { toFun := fun a => Φmass.massElement * a
      map_zero' := mul_zero _
      map_add' := fun a b => mul_add _ a b }
  φ n := (fun a => Φmass.massElement * a)^[n] Φmass.massElement

/-- The derived mass endomorphism is genuine left multiplication by the mass
    element — not a free field. -/
theorem CategoricalMassMarkov.ofHecke_Φ_apply {A : Type*} [CommRing A]
    (Φmass : QOU.Braiding.HeckeMassElement A) (a : A) :
    (CategoricalMassMarkov.ofHecke Φmass).Φ a = Φmass.massElement * a := rfl

/-- The level-`0` global section is the mass element itself. -/
theorem CategoricalMassMarkov.ofHecke_φ_zero {A : Type*} [CommRing A]
    (Φmass : QOU.Braiding.HeckeMassElement A) :
    (CategoricalMassMarkov.ofHecke Φmass).φ 0 = Φmass.massElement := rfl

/-- The global sections form the Φ-orbit: `φ_{n+1} = Φ(φ_n)`. The `φ_n` are
    genuinely closed under the mass endomorphism, not an independent family. -/
theorem CategoricalMassMarkov.ofHecke_φ_succ {A : Type*} [CommRing A]
    (Φmass : QOU.Braiding.HeckeMassElement A) (n : ℕ) :
    (CategoricalMassMarkov.ofHecke Φmass).φ (n + 1)
      = (CategoricalMassMarkov.ofHecke Φmass).Φ ((CategoricalMassMarkov.ofHecke Φmass).φ n) := by
  show (fun a => Φmass.massElement * a)^[n + 1] Φmass.massElement
      = Φmass.massElement * (fun a => Φmass.massElement * a)^[n] Φmass.massElement
  rw [Function.iterate_succ_apply']

-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/categorical-mass-markov-trace-endomorphism-intro.ts

end QOU
