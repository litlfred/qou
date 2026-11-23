import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Observations.gravity_spectral_prefactor

The universal curvature-rank tail of the unified mass formula carries the
prefactor `α = m_e · 8G`, where `G` is **Catalan's constant**, so that
`8G = Vol(𝓑₃) ≈ 7.3277` is the hyperbolic volume of the Borromean
complement — two regular ideal octahedra of volume `4G` each.

## The Newton reading is withdrawn (2026-09-14)

This file previously named the quantity `newtonG` and its header read
"Newton's gravitational constant `G`".  That was a glyph collision with
`conj:binding-scale-catalan`, which asserts the *same* formula
`α = m_e · 8G` with `G` Catalan's.  The two readings differ numerically —
`m_e · 8 · G_Catalan = 3.744459659941610 MeV` against
`m_e · 8 · 1 = 4.087991605520000 MeV` for `G_Planck = 1` — and the corpus's
own quoted value is `3.7445 MeV`, so Catalan's is the reading every
consuming block uses.  Newton's constant appears nowhere in this
repository: no witness, no producer, no CODATA comparison.

`[verlinde2011]` was cited here in support of the Newton reading and is
therefore no longer a reference for this statement; it is recorded in this
docstring rather than on the theorem.

## What the theorem below does and does not say

`tailSpectralRatio` is a **definition**, `G_q := α / (8 · m_e)`, and
`gravity_spectral_prefactor` is its unfolding: `α = m_e · 8 · (α / (8 · m_e))`.
It establishes that the extraction is well-posed for `m_e > 0`, nothing more.
It is **not** a derivation of the prefactor, and `G_q` carries no
`[length]³[mass]⁻¹[time]⁻²` content.

LaTeX label: `prop:gravity-spectral-prefactor`

## References

- [leitner2026] §6/gravity-spectral-prefactor
-/

namespace QOU.Observations

/-- The universal-residue prefactor of the unified mass formula. -/
structure UniversalResidue where
  /-- Prefactor on the deep-tower stratum. -/
  α : ℝ
  /-- Electron mass (the ruler fixed by CAL-1). -/
  m_e : ℝ
  /-- The ruler is a positive scale. -/
  m_e_pos : 0 < m_e

/-- The dimensionless tail spectral ratio extracted from the prefactor:
    `G_q = α / (8 · m_e)`.

    Under the Catalan reading this equals Catalan's constant exactly when
    `α = m_e · Vol(𝓑₃)`; see `tailSpectralRatio_eq_of_borromean`. -/
noncomputable def tailSpectralRatio (U : UniversalResidue) : ℝ :=
  U.α / (8 * U.m_e)

/-- **Proposition (prefactor extraction is well-posed).**

    `α = m_e · 8 · G_q` for the ratio `G_q` defined above.  This is the
    unfolding of `tailSpectralRatio`; it says the extraction inverts
    cleanly for a positive ruler, and does not derive `α`. -/
-- Ref: [leitner2026] §6/gravity-spectral-prefactor
theorem gravity_spectral_prefactor (U : UniversalResidue) :
    U.α = U.m_e * 8 * tailSpectralRatio U := by
  unfold tailSpectralRatio
  field_simp [ne_of_gt U.m_e_pos]

/-- The ratio recovers whatever constant the prefactor was built from: if
    `α = m_e · 8 · c` then `G_q = c`.  With `c` Catalan's constant this is
    the link to `conj:binding-scale-catalan`, and it is what makes the
    coefficient `8` a statement about `Vol(𝓑₃)` rather than a free choice. -/
-- Ref: [leitner2026] §6/gravity-spectral-prefactor
theorem tailSpectralRatio_eq_of_borromean (U : UniversalResidue) (c : ℝ)
    (h : U.α = U.m_e * 8 * c) : tailSpectralRatio U = c := by
  unfold tailSpectralRatio
  rw [h]
  field_simp [ne_of_gt U.m_e_pos]

end QOU.Observations
