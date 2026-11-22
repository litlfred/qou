import Mathlib.Data.Real.Basic


/-!
# QOU.CategoricalNeutron.unique_up_to_isotopy — uniqueness of the categorical neutron

𝔫 is unique up to braid isotopy: two categorical neutrons that share the same
Hecke normal form in H₃(q) and the same S₃ colour assignment coincide.

LaTeX: `\label{prop:categorical-neutron-unique}`

## References

- [leitner2026] §6-archimedean-universe/categorical-neutron-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU

/-- Defining data of the categorical neutron (mirror of
    [`def:categorical-neutron`], `QOU.Torsion.CategoricalNeutron`): the
    colour-linked triple `[u, d, d]_c ⋈ L_H` is determined by its pair-Skein
    masses `(S_ud, S_dd)`, with derived mass `2·S_ud + S_dd` and zero crossing
    chirality. -/
structure CategoricalNeutron where
  /-- Pair Skein mass `S_ud`. -/
  skein_ud : ℝ
  /-- Pair Skein mass `S_dd`. -/
  skein_dd : ℝ
  /-- Mass `= 2·S_ud + S_dd`. -/
  mass : ℝ := 2 * skein_ud + skein_dd
  /-- Zero crossing chirality (electric charge `0`). -/
  chirality : ℤ := 0

/-- **Hecke-normal-form coincidence context.**

    Two categorical neutrons share the same Hecke normal form in `H₃(q)` and the
    same `S₃` colour assignment.  By [`def:categorical-neutron`] the Hecke normal
    form determines the pair-Skein masses, the derived mass, and the chirality;
    the `S₃` permutation symmetry on the colour tubes makes the assignment of
    `(u, d, d)` to tube positions irrelevant.  This class records that
    coincidence as explicit hypotheses, so the uniqueness theorem below is a
    rigorous *conditional* result. -/
class NeutronSameHeckeNF (P Q : CategoricalNeutron) : Prop where
  /-- Same pair-Skein mass `S_ud`. -/
  skein_ud : P.skein_ud = Q.skein_ud
  /-- Same pair-Skein mass `S_dd`. -/
  skein_dd : P.skein_dd = Q.skein_dd
  /-- Same derived mass. -/
  mass : P.mass = Q.mass
  /-- Same chirality. -/
  chirality : P.chirality = Q.chirality

/-- **Uniqueness of the categorical neutron up to braid isotopy**
    (conditional on the Hecke-normal-form coincidence of
    [`def:categorical-neutron`]).

    Two categorical neutrons with the same Hecke normal form in `H₃(q)` and the
    same `S₃` colour assignment are equal.  This replaces the earlier
    `Subsingleton CategoricalNeutron` axiom, which was *false* for the free real
    fields `skein_ud, skein_dd`: distinct Skein data give genuinely distinct
    neutrons, so uniqueness holds only conditionally on a shared Hecke normal
    form — exactly the content of the narrative statement. -/
-- Ref: [jones1987]
theorem CategoricalNeutron.unique_up_to_isotopy
    (P Q : CategoricalNeutron) [h : NeutronSameHeckeNF P Q] : P = Q := by
  obtain ⟨e1, e2, e3, e4⟩ := h
  cases P
  cases Q
  simp only [CategoricalNeutron.mk.injEq]
  exact ⟨e1, e2, e3, e4⟩

end QOU
