/-
  Watson-uniqueness brick 4b-ii (boundary) — the ε-reduction (bean el8w
  tranche 5).

  The composed transport `Φ_t(z) = (z^t)⁻¹` (brick 4b-ii interior) carries the
  sector-at-0 to the half-plane-at-∞, but the pulled-back function `F = f ∘ Φ⁻¹`
  is NOT continuous at the single boundary point `w = 0` (the image of the
  sector tip at `∞`). Brick 3's `watson_uniqueness_rhp` needs `DiffContOnCl` —
  continuity on ALL of the closed half-plane `{re ≥ 0}`, `0` included — so it
  cannot be applied to `F` directly.

  The standard Watson fix is the ε-limiting argument: prove equality on each
  shifted closed half-plane `{re ≥ ε}` (ε > 0, which stays away from the `w = 0`
  puncture) and take `ε → 0`. This file proves the LOAD-BEARING REDUCTION step of
  that argument, sorry-free:

      (∀ ε > 0, EqOn f g {re ≥ ε})  ⟹  EqOn f g {re > 0}.

  It is exactly the `ε → 0` collapse: any point of the OPEN half-plane already
  lies in some closed shifted half-plane (take `ε = re z > 0`), so equality on
  all of them gives equality on the open half-plane — no puncture touched.

  Remaining for full Watson (the honest final hypothesis-engineering): the
  shifted instance `EqOn f g {re ≥ ε}` from a TRANSLATED `watson_uniqueness_rhp`
  (apply brick 3 to `w ↦ f (w + ε)` on `{re > 0}`; the six hypotheses transport
  under the shift, with imaginary-axis boundedness becoming boundedness on the
  vertical line `{re = ε}`). Scoped in the el8w tranche 5 bean; NOT axiomatized.

  Archimedean (ℂ): the ambient objects are complex-analytic; this reduction
  itself is pure order/set logic on `re`.

  -- Ref: [leitner2026] bean el8w tranche 5 — Watson uniqueness brick 4b-ii boundary
-/

import Mathlib.Analysis.Complex.Basic

namespace QOU.Mathlib.Borel

open Set

/-- **The ε-reduction (boundary argument, load-bearing step).** If two functions
    agree on every shifted closed half-plane `{re ≥ ε}` for `ε > 0`, they agree
    on the open half-plane `{re > 0}`. This is the `ε → 0` collapse of the
    Watson boundary limiting argument: it reduces uniqueness on `{re > 0}` (whose
    boundary point `0` breaks `DiffContOnCl` after transport) to uniqueness on
    the shifted half-planes (which avoid that puncture). Pure `re`-order logic —
    take `ε = re z`. -/
theorem eqOn_rhp_of_eqOn_shifted {E : Type*} {f g : ℂ → E}
    (h : ∀ ε > (0 : ℝ), EqOn f g {z : ℂ | ε ≤ z.re}) :
    EqOn f g {z : ℂ | 0 < z.re} :=
  fun z hz => h z.re hz (le_refl z.re)

/-- The open right half-plane is the union of the shifted closed half-planes
    `{re ≥ ε}` over `ε > 0` — the set-level content of the ε-reduction. -/
theorem rhp_eq_iUnion_shifted :
    {z : ℂ | 0 < z.re} = ⋃ ε > (0 : ℝ), {z : ℂ | ε ≤ z.re} := by
  ext z
  simp only [mem_setOf_eq, mem_iUnion, exists_prop]
  constructor
  · exact fun hz => ⟨z.re, hz, le_refl _⟩
  · rintro ⟨ε, hε, hz⟩
    exact lt_of_lt_of_le hε hz

end QOU.Mathlib.Borel
