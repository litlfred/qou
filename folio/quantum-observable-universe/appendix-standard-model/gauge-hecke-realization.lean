import Mathlib.CategoryTheory.Endomorphism
import Mathlib.Algebra.Group.Hom.Defs

/-!
# Conjecture: Hecke realization of the gauge groupoid

The QOU derivation chain evaluates braid words through the Hecke
algebra `H_n(q)` (Markov trace, Wedderburn blocks). The conjecture
formalised here is the *gauge* reading of that chain: the gauge
transformations of the knot-state groupoid — its automorphism
monoids — realise faithfully inside the multiplicative monoid of the
Hecke algebra, so that gauge structure and Hecke structure are two
presentations of the same symmetry.

This is a **primary conjecture** (no other conjecture class appears
as a hypothesis; the classification is derived from the signature,
AGENTS.md §3b-tax). The class carries the conjecture's content as a
quantified existence-of-embedding field; no instance is provided —
the open state is represented by a content-bearing class with no
instance.

What is *not* conjectural: that the braid group maps onto `H_n(q)`
(standard, [kasselTuraev2008]); that gauge equivalence in a groupoid
is an equivalence relation (proved in `gauge-action-groupoid.lean`).
What *is* conjectural: that the physically-relevant gauge
automorphism monoids inject, i.e. that no gauge symmetry is lost in
the Hecke quotient.

## References

- [kassel2008] Kassel–Turaev, Braid Groups
- [leitner2026] Appendix: Toward the Standard Model
-/

namespace QOU.StandardModel

open CategoryTheory

universe u v

/-- **Conjecture (Hecke realization of gauge symmetry).** For the
groupoid `S` of topological states and a monoid `H` (intended: the
multiplicative monoid of the Hecke algebra `H_n(q)`), every state's
automorphism monoid embeds in `H` via a monoid homomorphism. The
content field asserts the embedding for *every* state — faithfulness
means no gauge transformation is collapsed in the Hecke image.

Intended instantiation: `S` = knot-state groupoid of the QOU
substrate, `H` = `H_n(q)` under multiplication. Open: no instance
for that instantiation is known; providing one requires exhibiting
the injective homs, which is precisely the open derivation. -/
class GaugeHeckeRealization (S : Type u) [Groupoid.{v} S]
    (H : Type*) [Monoid H] : Prop where
  /-- Every state's gauge automorphism monoid embeds in `H`. -/
  aut_embeds : ∀ X : S, ∃ Φ : End X →* H, Function.Injective Φ

/-- The conjecture class has falsifiable content: it fails whenever
`H` is too small. If any state carries two distinct gauge
automorphisms, no realization into a subsingleton monoid exists. -/
theorem not_gaugeHeckeRealization_of_subsingleton
    (S : Type u) [Groupoid.{v} S] (H : Type*) [Monoid H] [Subsingleton H]
    (X : S) (f g : End X) (hfg : f ≠ g) :
    ¬GaugeHeckeRealization S H := by
  rintro ⟨aut⟩
  obtain ⟨Φ, hΦ⟩ := aut X
  exact hfg (hΦ (Subsingleton.elim _ _))

/-- Monotonicity: a realization survives enlarging the target along
any injective monoid homomorphism (e.g. `H_n(q) ↪ H_{n+1}(q)` under
a tower inclusion). -/
theorem GaugeHeckeRealization.of_injective_comp
    (S : Type u) [Groupoid.{v} S] {H H' : Type*} [Monoid H] [Monoid H']
    (ψ : H →* H') (hψ : Function.Injective ψ)
    [inst : GaugeHeckeRealization S H] : GaugeHeckeRealization S H' := by
  refine ⟨fun X => ?_⟩
  obtain ⟨Φ, hΦ⟩ := inst.aut_embeds X
  exact ⟨ψ.comp Φ, hψ.comp hΦ⟩

end QOU.StandardModel
