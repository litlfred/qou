/-
  The channel's `u` is not the anchor's own NZ deformation (bean `qou-8vt2`, AV2).

  WHERE THIS COMES FROM.  PR #4513 and #4725 proved that both corpus anchors sit
  at the REGULAR IDEAL CELL of their triangulation:

    * m004 (4₁, muon):  the Casson-Rivin optimum on the symmetry-fixed line is
      the regular ideal TETRAHEDRON, every angle `1/3` in π-units
      (`M004AngleStructure.regular_unique_on_fixed_locus`);
    * L6a4 (Borromean, proton): the unique symmetric point is the regular ideal
      OCTAHEDRON, angles `1/4, 1/4, 1/2`
      (`L6a4AngleStructure.unique_symmetric_point`).

  The regular ideal cell decomposition IS the complete hyperbolic structure, and
  in Neumann-Zagier coordinates the complete structure sits at `u = 0` — which is
  exactly the normalisation `FigureEightComplexVolume` already uses, since
  `V₄₁ 0 = Vol(4₁)` is real (`V₄₁_zero_re`).

  THAT NORMALISATION IS NOT AN INFERENCE — IT IS NEUMANN-ZAGIER'S OWN DEFINITION,
  checked against the paper (Topology 24 (1985) 307-332, §1):

    "Let `u_i = ½ log(λ(m_i))` where `m_i` is the chosen meridian at the i-th
     cusp.  Since `λ(m_i) = 1` for the complete hyperbolic structure on M, we may
     choose the branch of logarithm so `(u_1, …, u_h) = 0` for this structure."

    "The hyperbolic structure `M_u` is complete at the i-th end of M (i.e. this
     end is still a true cusp) IF AND ONLY IF `u_i = 0`."

  So `u = 0 ⟺ complete structure` is an *iff* in the source, stronger than this
  file needs.  Two further points from the same section corroborate the corpus's
  surrounding machinery: the cusp shape `τ_i(u)` is an EVEN function of each `u_i`
  (the origin of `V₄₁_even` / `no_cubic_rung`), and `u` is a local coordinate
  valid only "in a neighborhood of `0 ∈ ℂ^h`" — which is why the Murakami
  substrate-matched meridian, at `|u| ≥ 2π`, is off the controlled neighbourhood
  (`FigureEightDeformedMeridianWinding`).

  The half-factor is worth carrying: `u = ½ log λ(m)` means the T5 hypothesis
  `hRe : Re u = ln q₀` is the condition `|λ(meridian)| = q₀²`, not `= q₀`.  Any
  candidate bridge owes that factor.

  THE CONSEQUENCE, PROVED BELOW.  `Im V₄₁` is the harmonic form
  `κ·(Re²u − Im²u)`, so it VANISHES at `u = 0`.  Hence a channel whose
  deformation map sends the substrate to `u = 0` has `S = 0` identically
  (`S_eq_zero_of_u_eq_zero`).  Contrapositively, the MEASURED nonzero leaks
  `S_μ = +0.00968298` and `S_p = −0.03945936` force `u(q₀) ≠ 0`
  (`u_ne_zero_of_S_ne_zero`).

  SO: if `u` were the Neumann-Zagier deformation of the anchor's OWN hyperbolic
  structure, it would be `0` — because that structure is the complete one — and
  the leak would vanish.  It does not.  **The channel's `u` is not the anchor's
  own geometric deformation parameter.**

  WHY THIS IS WORTH RECORDING.  It is the second independent exclusion of a
  "geometric reading" of `u`.  The first (#4513,
  `ChannelMeridianIdentification`) excluded the substrate-matched Murakami
  meridian.  Together they box the geometric readings in hard, and the remaining
  space should be ENUMERATED before any new candidate is proposed — that is the
  discipline `qou-8vt2` exists to enforce.

  HONESTY BOUNDARY — read this before citing the file.

  * What is PROVED here is the implication `u = 0 → S = 0` and its
    contrapositive.  That is genuine but easy; its weight is in what it rules
    out, not in its difficulty.
  * "The anchors sit at the complete structure" is NOT proved here.  The
    angle-structure half is (see the two files above); the step from "regular
    ideal cell" to "complete hyperbolic structure" is standard hyperbolic
    geometry that Mathlib cannot express (bean `qou-idvt`), and is used as
    CONTEXT, not as a hypothesis of any theorem below.  What IS now sourced
    rather than inferred is the other half — `u = 0 ⟺ complete` — quoted from
    Neumann-Zagier above.
  * `u = 0` therefore appears as an explicit HYPOTHESIS `hu`, never as an
    established fact about the anchors.  Nothing here silently assumes the
    geometric reading it is testing.
  * The measured `S` values are inputs, quoted for the contrapositive's
    interpretation only; no theorem below depends on their numerical values.

  Scope (a) per AGENTS.md: nothing here refutes the channel or the NZ complex
  volume.  What is excluded is one IDENTIFICATION of the channel's free field
  `u` with a particular geometric object.

  -- Ref: [leitner2026] bean qou-8vt2; conj:binding-qbeta-complex-volume
  -- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
  --      Topology 24 (1985) 307-332.  DOI corrected 2026-08-08: this file first
  --      carried 10.1016/0040-9383(85)90050-3, typed from memory rather than read
  --      off `folio/schema/references.ts`, which had the correct one all along.
-/

import QOU.Knot.FigureEightComplexVolume
import QOU.QBeta.PhiBSArgumentIdentification

namespace QOU.QBeta.CompleteStructureExclusion

open QOU.Knot.FigureEightComplexVolume
open QOU.QBeta.PhiBSArgumentIdentification

/-- **The Chern-Simons part vanishes at the complete structure.**
`Im V₄₁ 0 = κ·(0² − 0²) = 0` — immediate from the harmonic form, recorded
separately because it is the hinge of everything below. -/
theorem imV₄₁_zero : (V₄₁ 0).im = 0 := by
  rw [imV₄₁]; simp

/-- **A channel sitting at the complete structure has no leak.**
If the deformation map sends the substrate point to `u = 0`, the S-leak is
identically zero, whatever the Stokes constant. -/
theorem S_eq_zero_of_u_eq_zero {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀) (hu : ch.u q₀ = 0) :
    S q₀ = 0 := by
  rw [ch.S_eq q₀ hq, hV, hu, imV₄₁_zero, mul_zero]

/-- **The measured leak forces a nonzero deformation.**  Contrapositive of the
above: since `S ≠ 0` is measured at both anchors, `u(q₀) ≠ 0` there.

This is the exclusion.  The anchors' own hyperbolic structures ARE the complete
ones (regular ideal cell, proved in the angle-structure files), and the complete
structure is `u = 0`; so `u` cannot be the anchor's own NZ deformation. -/
theorem u_ne_zero_of_S_ne_zero {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀) (hS : S q₀ ≠ 0) :
    ch.u q₀ ≠ 0 :=
  fun hu => hS (S_eq_zero_of_u_eq_zero hV hq hu)

/-- **Both anchors at once.**  Two channels — the muon and proton anchors — with
nonzero measured leaks both have nonzero deformation.  Stated because the
exclusion is about the PAIR: a single anchor could be argued away as a
normalisation choice, both cannot. -/
theorem both_anchors_deformed {S₁ S₂ : ℝ → ℝ}
    [ch₁ : SDeformedVolumeChannel S₁] [ch₂ : SDeformedVolumeChannel S₂]
    (hV₁ : ch₁.V = V₄₁) (hV₂ : ch₂.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hS₁ : S₁ q₀ ≠ 0) (hS₂ : S₂ q₀ ≠ 0) :
    ch₁.u q₀ ≠ 0 ∧ ch₂.u q₀ ≠ 0 :=
  ⟨u_ne_zero_of_S_ne_zero hV₁ hq hS₁, u_ne_zero_of_S_ne_zero hV₂ hq hS₂⟩

/-- **The sign flip needs more than nonvanishing.**  `Im V₄₁` is positive inside
the cone `|Im u| < |Re u|` and negative outside it, so two anchors of OPPOSITE
leak sign must lie on opposite sides of the diagonal `|Re u| = |Im u|` — not
merely away from `0`.

Recorded as the sharper A_ω-free filter that `qou-8vt2` AV4 and `qou-qmnb` AV1
tell candidates to apply BEFORE computing any magnitude.

**Statement note.**  An earlier version of this claimed the stronger ordering
`Im₂² − Re₂² < Re₁² − Im₁²`, and `linarith` rejected it — correctly.  Both
quantities are positive, but opposite SIGNS of the leak give no ORDERING between
their magnitudes.  What is true, and all that is true, is the sidedness below. -/
theorem opposite_sides_of_diagonal {S₁ S₂ : ℝ → ℝ}
    [ch₁ : SDeformedVolumeChannel S₁] [ch₂ : SDeformedVolumeChannel S₂]
    (hV₁ : ch₁.V = V₄₁) (hV₂ : ch₂.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hA₁ : 0 < ch₁.A_ω) (hA₂ : 0 < ch₂.A_ω)
    (hpos : 0 < S₁ q₀) (hneg : S₂ q₀ < 0) :
    0 < (ch₁.u q₀).re ^ 2 - (ch₁.u q₀).im ^ 2 ∧
      (ch₂.u q₀).re ^ 2 - (ch₂.u q₀).im ^ 2 < 0 := by
  have h1 := ch₁.S_eq q₀ hq
  have h2 := ch₂.S_eq q₀ hq
  rw [hV₁, imV₄₁] at h1
  rw [hV₂, imV₄₁] at h2
  have hk : (0 : ℝ) < cuspModulus := cuspModulus_pos
  -- S₁ > 0 forces Re² > Im² at anchor 1; S₂ < 0 forces Re² < Im² at anchor 2
  constructor
  · by_contra hc
    push_neg at hc
    nlinarith [hpos, h1, mul_pos hA₁ hk]
  · by_contra hc
    push_neg at hc
    nlinarith [hneg, h2, mul_pos hA₂ hk]

end QOU.QBeta.CompleteStructureExclusion
