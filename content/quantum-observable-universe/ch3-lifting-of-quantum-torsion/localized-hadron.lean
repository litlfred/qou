/-!
# QOU.LocalizedHadron — Hadron placed at a categorical point

A localized hadron is a hadron placed at a categorical point p of the
projective line ℙ(V), via a morphism 𝟙 → Sym^n(𝒦_p) ⊗ ℒ_p^bind.

## References

- [leitner2026] §3 Lifting and Descent
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

namespace QOU

/-- A localized hadron: a hadron placed at a specific categorical point.

    LaTeX: `\label{def:localized-hadron}` -/
-- Ref: [leitner2026] §3, Definition: Localized hadron
structure LocalizedHadron extends Hadron where
  /-- The categorical point (base point in the projective line). -/
  point_theta : ℝ
  point_phi : ℝ
  /-- Binding link data. -/
  binding : HadronBinding

end QOU
