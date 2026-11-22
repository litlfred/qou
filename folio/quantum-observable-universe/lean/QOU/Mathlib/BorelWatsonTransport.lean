/-
  Watson-uniqueness brick 4a — the `z ↦ 1/z` interior transport
  (bean el8w tranche 5).

  The last piece of Watson uniqueness is the change of variables mapping the
  sector-at-0 (where the Gevrey-1 asymptotic lives) to the half-plane-at-∞
  (where brick 3's `watson_uniqueness_rhp` applies). This file proves the
  INTERIOR core of that transport, sorry-free:

    * `Complex.inv_re_pos` — the open right half-plane `{re > 0}` is invariant
      under inversion `z ↦ z⁻¹` (immediate from `Complex.inv_re`,
      `z⁻¹.re = z.re / normSq z`). So inversion carries the domain to itself,
      the point `0` at one end to `∞` at the other.
    * `differentiableOn_comp_inv` — precomposition with inversion preserves
      holomorphy on the open half-plane: if `g` is `DifferentiableOn ℂ` on
      `{re > 0}` then so is `w ↦ g w⁻¹`. This is the analyticity half of the
      change of variables (`DifferentiableOn.comp` + `differentiableOn_inv`,
      with the `MapsTo` supplied by `inv_re_pos`).

  HONEST REMAINING GAP (the reason full Watson is multi-session, NOT faked):

    1. **Boundary continuity.** `watson_uniqueness_rhp` needs `DiffContOnCl`
       (continuity up to the closure `{re ≥ 0}`), and the closure contains `0`,
       where `g ∘ inv` is NOT continuous. The genuine Watson statement uses a
       sector strictly inside the half-plane and a limiting argument, avoiding
       the boundary point `0`/`∞`. That boundary handling is the missing piece.
    2. **Opening `> π` (the fractional power).** A half-plane is opening `= π`
       and, under inversion, an `exp(−c/|z|)` bound maps only to `exp(−c|w|)` —
       exponential, insufficient (brick 3's note). Watson's opening `> π`
       requires an additional fractional-power map `z ↦ z^{1/β}` (β > 1) to
       reach a half-plane while amplifying the bound to the stretched
       exponential `exp(−b|w|^β)` that brick 3 consumes. The `cpow`
       branch-cut analyticity for that map is the second missing piece.

  Both are scoped in the el8w tranche 5 bean; neither is axiomatized.

  Archimedean (ℂ): genuinely archimedean — complex holomorphy, inversion.

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4a
-/

import Mathlib.Analysis.Complex.PhragmenLindelof

namespace QOU.Mathlib.Borel

open Complex

/-- **The open right half-plane is invariant under inversion.**
    `z⁻¹.re = z.re / normSq z`, so `0 < z.re ⇒ 0 < z⁻¹.re`. Inversion carries
    the Watson domain to itself, swapping the ends `0 ↔ ∞`. -/
theorem inv_re_pos {z : ℂ} (hz : 0 < z.re) : 0 < z⁻¹.re := by
  have hz0 : z ≠ 0 := fun h => by rw [h] at hz; simp at hz
  rw [Complex.inv_re]
  exact div_pos hz (Complex.normSq_pos.mpr hz0)

/-- **Inversion preserves holomorphy on the open half-plane.** If `g` is
    holomorphic on `{re > 0}`, so is its precomposition with inversion
    `w ↦ g w⁻¹`. The analyticity half of the Watson `z ↦ 1/z` change of
    variables. -/
theorem differentiableOn_comp_inv {E : Type*} [NormedAddCommGroup E]
    [NormedSpace ℂ E] {g : ℂ → E}
    (hg : DifferentiableOn ℂ g {z : ℂ | 0 < z.re}) :
    DifferentiableOn ℂ (fun w => g w⁻¹) {z : ℂ | 0 < z.re} := by
  have hinv : DifferentiableOn ℂ (fun w : ℂ => w⁻¹) {z : ℂ | 0 < z.re} := by
    intro w hw
    have hw0 : w ≠ 0 := fun h => by rw [h] at hw; simp at hw
    exact (differentiableAt_id.inv hw0).differentiableWithinAt
  exact hg.comp hinv (fun z hz => inv_re_pos hz)

end QOU.Mathlib.Borel
