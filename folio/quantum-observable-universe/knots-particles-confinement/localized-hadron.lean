import QOU.ParticleInteractions.HadronDisplay


/-!
# QOU.LocalizedHadron — Hadron placed at a categorical point

A localized hadron is a hadron placed at a categorical point p of the
projective line ℙ(V), via a morphism 𝟙 → Sym^n(𝒦_p) ⊗ ℒ_p^bind.

## References

- [leitner2026] §3 Lifting and Descent

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ), taken
from `QOU.Archimedean.GroundRing` (the library home reused by the
`Hadron` structure this file extends).  The parameter `q` is the
canonical indeterminate of `R_q`.  Specialise via `ι : R_q → ℝ, q ↦ q₀`
for numerical evaluation.
-/

namespace QOU

open Archimedean (R_q)

/-- Binding structure: the Hopf link and its Skein polynomial
    contribution to the hadronic binding energy. -/
-- Ref: [leitner2026] §3, Definition: Hadron mass
structure HadronBinding where
  /-- The q-deformation parameter. -/
  q : R_q
  /-- The binding link (Hopf link braid word). -/
  bindingLink : KnotTheory.BraidWord
  /-- The Skein polynomial evaluation Q(q) · M(L_Hopf). -/
  bindingMass : R_q

/-- A localized hadron: a hadron (`QOU.Hadron`) placed at a specific
    categorical point `p = (θ, φ)` of the projective line, together with
    its binding-link data.

    LaTeX: `\label{def:localized-hadron}` -/
-- Ref: [leitner2026] §3, Definition: Localized hadron
structure LocalizedHadron extends Hadron where
  /-- The categorical point: coordinate `θ` of the base point. -/
  point_theta : R_q
  /-- The categorical point: coordinate `φ` of the base point. -/
  point_phi : R_q
  /-- Binding link data. -/
  binding : HadronBinding

/-- The categorical point `(θ, φ)` at which the hadron is localized. -/
def LocalizedHadron.point (H : LocalizedHadron) : R_q × R_q :=
  (H.point_theta, H.point_phi)

end QOU
