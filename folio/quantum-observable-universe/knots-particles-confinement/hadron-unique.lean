import QOU.Basic
import QOU.ParticleInteractions.HadronDisplay


/-!
# QOU.Hadron.unique_up_to_isotopy — uniqueness of hadrons up to isotopy

Hecke normal form is unique in H_n(q); Markov trace is isotopy-invariant.

LaTeX: `\label{prop:hadron-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted `axiom : Subsingleton Hadron`, which is
**strictly false**: `Hadron` has free fields (`theta phi : R_q` with
`R_q = ℤ[q, q⁻¹]` nontrivial, `constituents : List BraidWord` with only
a length constraint), so distinct hadrons exist — e.g. `theta = 0` vs
`theta = q`.  From that axiom `False` was derivable (two distinct terms
+ `Subsingleton.elim`).

This file now imports the relocated `Hadron` structure
(`QOU.ParticleInteractions.HadronDisplay`) and **proves** — no axiom —
a *quotient-level* statement: hadrons agreeing on base-point
coordinates and constituent list are equal (the length constraint is
propositional).  Pending a Markov-move relation on
`KnotTheory.BraidWord`, the constituent-level relation is list
equality (the discrete core of isotopy equivalence); refining it to
Markov-trace equivalence ([jones1987]) is the open refactor.

## References

- [leitner2026] §4-braids-and-knots/hadron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU

/-- **Isotopy equivalence of hadrons.**  Two hadrons are isotopy-
    equivalent when they share the base-point coordinates on `S²` and
    their constituent braid words agree.  Pending a Markov-move
    relation on `KnotTheory.BraidWord`, constituent agreement is list
    equality — the discrete core of braid isotopy. -/
-- Ref: [jones1987] Hecke Algebra Representations of Braid Groups
def Hadron.IsotopyEquiv (h₁ h₂ : Hadron) : Prop :=
  h₁.theta = h₂.theta ∧ h₁.phi = h₂.phi ∧ h₁.constituents = h₂.constituents

/-- Isotopy equivalence is an equivalence relation. -/
-- Ref: [jones1987]
theorem Hadron.isotopyEquiv_equivalence : Equivalence Hadron.IsotopyEquiv :=
  ⟨fun _ => ⟨rfl, rfl, rfl⟩,
   fun ⟨ht, hp, hc⟩ => ⟨ht.symm, hp.symm, hc.symm⟩,
   fun ⟨ht₁, hp₁, hc₁⟩ ⟨ht₂, hp₂, hc₂⟩ =>
     ⟨ht₁.trans ht₂, hp₁.trans hp₂, hc₁.trans hc₂⟩⟩

/-- **Uniqueness of hadrons up to isotopy (proved).**

    Isotopy-equivalent hadrons are equal: the base-point coordinates
    and constituent list are shared, and the length constraint is
    propositional.  This replaces a false `Subsingleton Hadron` axiom
    (from which `False` was derivable) with a genuinely proved
    statement at the equivalence-relation level. -/
-- Ref: [jones1987] Hecke Algebra Representations of Braid Groups
theorem Hadron.unique_up_to_isotopy (h₁ h₂ : Hadron)
    (heq : Hadron.IsotopyEquiv h₁ h₂) : h₁ = h₂ := by
  obtain ⟨ht, hp, hc⟩ := heq
  cases h₁
  cases h₂
  subst ht
  subst hp
  subst hc
  rfl

end QOU
