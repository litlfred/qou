/-
# The bracket family over ℂ — archimedean vertical edges of the ζ-indexed picture

Continuation of the Habiro ζ₄ bridge (bean qou-vegn), after
`HabiroZeta4Bracket.lean`. The classical Habiro element `[2]_q` has a
global archimedean realization `z ↦ z + z⁻¹`; this file names that
family and proves its two archimedean vertical-edge facts:

* **`bracketFamily_conj`** — Galois (complex-conjugation)
  equivariance: `[2]_{z̄} = conj [2]_z`. On the unit circle
  conjugation IS the bar involution `q ↦ q⁻¹`, so this single
  statement is the archimedean form of the bar edge at EVERY fibre at
  once — the global version of the ζ₄ instance already tied to
  `rho_compat`.
* **`bracketFamily_zeta8_eq_sqrt2`** — the ζ₈ fibre value
  `[2]_{ζ₈} = √2`: the evaluation point of the corpus Q_β ζ₈
  categorical witness
  (`docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md`),
  companion to the ζ₄ modular zero. The p = 2 gluing edge between
  these two fibres is verified computationally in
  `computations/probes/zeta4_zeta8_habiro_gluing_probe.py`; the p-adic
  Frobenius action itself is verified against GSWZ printed data in
  `computations/probes/gswz_frobenius_teichmuller_probe.py`.

Honest scope: these are the ARCHIMEDEAN shadows of the GSWZ vertical
edges (arXiv:2412.04241, `library/arxiv-2412.04241v2/2412.04241v2.pdf`) — conjugation is
the only continuous Galois automorphism of ℂ, and the p-adic Frobenius
edges live compute-side, not in this Lean layer. The ζ-indexed FAMILY
structure for the τ-assignment tower (fibre data beyond the bracket)
remains the open half of bean qou-vegn.

HONESTY (STRICT): sorry-free, no axioms, no `decide`. Nothing wired;
`1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

namespace QOU.Machinery.CoxeterParabolic

open Complex

/-- The global archimedean realization of the classical Habiro element
`[2]_q`. -/
noncomputable def bracketFamily (z : ℂ) : ℂ := z + z⁻¹

/-- **Galois-conjugation equivariance** — the archimedean vertical-edge
class: on the unit circle conjugation is the bar involution, so this is
the bar edge at every fibre at once. -/
theorem bracketFamily_conj (z : ℂ) :
    bracketFamily ((starRingEnd ℂ) z) = (starRingEnd ℂ) (bracketFamily z) := by
  unfold bracketFamily
  rw [map_add, map_inv₀]

/-- **The ζ₈ fibre value**: `[2]_{ζ₈} = √2` — the corpus Q_β ζ₈
witness point, companion of the ζ₄ modular zero. -/
theorem bracketFamily_zeta8_eq_sqrt2 :
    bracketFamily (Complex.exp (Real.pi / 4 * I)) = Real.sqrt 2 := by
  unfold bracketFamily
  rw [← Complex.exp_neg]
  have h : (Real.pi / 4 : ℂ) * I = (Real.pi / 4 : ℝ) * I := by
    push_cast
    ring
  rw [h, ← Complex.cos_add_sin_I, ← neg_mul, ← Complex.cos_sub_sin_I]
  rw [← Complex.ofReal_cos, ← Complex.ofReal_sin,
    Real.cos_pi_div_four, Real.sin_pi_div_four]
  push_cast
  ring

end QOU.Machinery.CoxeterParabolic
