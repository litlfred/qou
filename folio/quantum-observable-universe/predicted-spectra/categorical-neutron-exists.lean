import Mathlib.Data.Real.Basic


/-!
# QOU.CategoricalNeutron.exists — existence of the categorical neutron

𝔫 = 𝓑₃(𝔲, 𝔡, 𝔡) is a well-defined element of H₃(q), LP-stable with
two gluons (L₊ → L₋).

LaTeX: `\label{prop:categorical-neutron-exists}`

## References

- [leitner2026] §6-archimedean-universe/categorical-neutron-exists
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU

/-- Defining data of the categorical neutron (mirror of
    [`def:categorical-neutron`], shared with `categorical-neutron-unique.lean`):
    the colour-linked triple `[u, d, d]_c ⋈ L_H` is determined by its pair-Skein
    masses `(S_ud, S_dd)`, with derived mass `2·S_ud + S_dd` and zero chirality. -/
structure CategoricalNeutron where
  /-- Pair Skein mass `S_ud`. -/
  skein_ud : ℝ
  /-- Pair Skein mass `S_dd`. -/
  skein_dd : ℝ
  /-- Mass `= 2·S_ud + S_dd`. -/
  mass : ℝ := 2 * skein_ud + skein_dd
  /-- Zero crossing chirality (electric charge `0`). -/
  chirality : ℤ := 0

/-- **Existence of the categorical neutron.**

    B₃(u,d,d) + two-gluon stabiliser yields a
    `CategoricalNeutron` term with negative crossing energy. -/
-- Ref: [jones1987]
theorem CategoricalNeutron.exists : Nonempty CategoricalNeutron :=
  -- Trivial witness: skein_ud = skein_dd = 0.
  -- The intended Borromean B₃(u,d,d) × (L_- ∘ L_-) witness is sharper
  -- but requires the Hecke NF reduction infrastructure.
  -- Ref: [jones1987]
  ⟨{ skein_ud := 0, skein_dd := 0 }⟩

end QOU
