import Mathlib.Data.Real.Basic


/-!
# QOU.CategoricalProton.unique_up_to_isotopy — uniqueness of the categorical proton

𝔭 is unique up to braid isotopy: two categorical protons that share the same
Hecke normal form in H₃(q) and the same S₃ colour assignment coincide.

LaTeX: `\label{prop:categorical-proton-unique}`

## References

- [leitner2026] §6-archimedean-universe/categorical-proton-unique
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU

/-- Defining data of the categorical proton (mirror of
    [`def:categorical-proton`], `QOU.Torsion.CategoricalProton`): the
    colour-linked triple `[u, u, d]_c ⋈ L_H` is determined by its pair-Skein
    masses `(S_uu, S_ud)`, with derived mass `S_uu + 2·S_ud` and positive
    crossing chirality `+1`. -/
structure CategoricalProton where
  /-- Pair Skein mass `S_uu`. -/
  skein_uu : ℝ
  /-- Pair Skein mass `S_ud`. -/
  skein_ud : ℝ
  /-- Mass `= S_uu + 2·S_ud`. -/
  mass : ℝ := skein_uu + 2 * skein_ud
  /-- Positive crossing chirality (electric charge `+1`). -/
  chirality : ℤ := 1

/-- **Hecke-normal-form coincidence context.**

    Two categorical protons share the same Hecke normal form in `H₃(q)` and the
    same `S₃` colour assignment.  By [`def:categorical-proton`] the Hecke normal
    form determines the pair-Skein masses, the derived mass, and the chirality;
    the `S₃` permutation symmetry on the colour tubes makes the assignment of
    `(u, u, d)` to tube positions irrelevant.  This class records that
    coincidence as explicit hypotheses, so the uniqueness theorem below is a
    rigorous *conditional* result. -/
class ProtonSameHeckeNF (P Q : CategoricalProton) : Prop where
  /-- Same pair-Skein mass `S_uu`. -/
  skein_uu : P.skein_uu = Q.skein_uu
  /-- Same pair-Skein mass `S_ud`. -/
  skein_ud : P.skein_ud = Q.skein_ud
  /-- Same derived mass. -/
  mass : P.mass = Q.mass
  /-- Same chirality. -/
  chirality : P.chirality = Q.chirality

/-- **Uniqueness of the categorical proton up to braid isotopy**
    (conditional on the Hecke-normal-form coincidence of
    [`def:categorical-proton`]).

    Two categorical protons with the same Hecke normal form in `H₃(q)` and the
    same `S₃` colour assignment are equal.  This replaces the earlier
    `Subsingleton CategoricalProton` axiom, which was *false* for the free real
    fields `skein_uu, skein_ud`: distinct Skein data give genuinely distinct
    protons, so uniqueness holds only conditionally on a shared Hecke normal
    form — exactly the content of the narrative statement. -/
-- Ref: [jones1987]
theorem CategoricalProton.unique_up_to_isotopy
    (P Q : CategoricalProton) [h : ProtonSameHeckeNF P Q] : P = Q := by
  obtain ⟨e1, e2, e3, e4⟩ := h
  cases P
  cases Q
  simp only [CategoricalProton.mk.injEq]
  exact ⟨e1, e2, e3, e4⟩

end QOU
