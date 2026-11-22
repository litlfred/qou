import QOU.QBeta.OneSidedNonlinearMaps

/-!
# A non-product final-state trace: which window it must land in

Thread "Find where the n–p mass error comes from", 2026-11-21. Audit §14. Owner, 2026-11-21: the
final-state trace may not be a product, because of the flavour/colour terms. So `ε(p e⁻ ν̄) = x`
is left free here (the product `ε_p·f` plus whatever cross terms the flavour/colour structure
gives). The energy of a state is `g(ε)`.

## What is proved (on `1 < q ≤ 23/20`, for every `x`)

1. `increasing_excluded`: for a monotone `g`, no `x` gives both a positive lepton pair
   `g(x) − g(ε_p)` and a positive `Q_β = g(ε_n) − g(x)`. Reason: it would need
   `ε_p < x < ε_n`, and `ε_n < ε_p`. This holds whatever the cross terms are.
2. `decreasing_window`: for a strictly antitone `g` (e.g. `−log`, `ℏ/𝔇 = 1/x`), both are positive
   **iff** `ε_n < x < ε_p`, i.e. `ε_p/q² < x < ε_p`.
3. `product_outside_window`: the plain product `x = ε_p·f` is below the window. So the cross
   terms must lift the final-state trace by more than `ε_n − ε_p·f > 0`.

No value of the cross terms is assumed or claimed here.
-/

namespace QOU.QBeta.NonProductFinalState

open QOU.QBeta.FlavourWeightSplit
open QOU.QBeta.OneSidedLeptonFactor
open QOU.QBeta.OneSidedNonlinearMaps
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-- **Increasing maps are excluded for every final-state trace `x`.** -/
theorem increasing_excluded {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) (g : ℝ → ℝ)
    (hg : Monotone g) (x : ℝ) :
    ¬ (g (epsP q (borromeanV3A q)) < g x ∧ g x < g (epsN q (borromeanV3B q))) := by
  obtain ⟨_, h2⟩ := ordering hq1 hq2
  rintro ⟨a, b⟩
  have := hg h2.le
  linarith

/-- **Decreasing maps work exactly on the window `ε_n < x < ε_p`.** -/
theorem decreasing_window {q : ℝ} (g : ℝ → ℝ) (hg : StrictAnti g) (x : ℝ) :
    (g (epsP q (borromeanV3A q)) < g x ∧ g x < g (epsN q (borromeanV3B q))) ↔
      (epsN q (borromeanV3B q) < x ∧ x < epsP q (borromeanV3A q)) := by
  constructor
  · rintro ⟨a, b⟩
    exact ⟨hg.lt_iff_lt.mp b, hg.lt_iff_lt.mp a⟩
  · rintro ⟨a, b⟩
    exact ⟨hg.lt_iff_lt.mpr b, hg.lt_iff_lt.mpr a⟩

/-- **The plain product lies below the window.** -/
theorem product_outside_window {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsP q (borromeanV3A q) * leptonFactor q < epsN q (borromeanV3B q) :=
  (ordering hq1 hq2).1

end QOU.QBeta.NonProductFinalState
