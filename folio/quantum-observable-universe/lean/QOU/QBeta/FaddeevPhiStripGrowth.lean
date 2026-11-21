import QOU.MathlibExt.PhiBProd

/-!
# The strip-growth characterization class (growth epic, brick G4)

Route-B brick **G4** of the Faddeev growth-estimate epic (`qou-mz4f`). The shift equations
(the `FaddeevPhi` class) do **not** pin `Φ_b` — the elliptic-freedom obstruction. The
physical `Φ_b` is singled out by a **growth condition** (Faddeev–Kashaev): among all
shift-solutions it is the one with controlled growth. This file formalizes that condition as
a §3b characterization class and discharges its non-vacuity by exhibiting `phiBProd` as an
instance.

* `FaddeevPhiStripGrowth b Φ` — `Φ` is **comparable to `phiBProd`**: `∃ C > 0`,
  `‖Φ z‖ ≤ C‖phiBProd b z‖` and `‖phiBProd b z‖ ≤ C‖Φ z‖` for all `z`. This is the honest
  §3b axiomatization of the physical characterization — it carries the growth **hypothesis**
  (comparability), not the uniqueness conclusion.
* `instPhiBProd` — **`phiBProd` is an instance** (`C = 1`), so the class is non-vacuous by
  construction (anti-laundering §3b-tax: the carrier asserts real content and is realized).
* `ratio_bounded_of_stripGrowth` — the payoff toward G5: two strip-growth solutions have a
  **bounded ratio** off the denominator's zeros (`‖Φ₁/Φ₂‖ ≤ C₁C₂`), the raw-ratio input the
  boundedness capstone consumes.

The strip bound that *witnesses* comparability for a concrete solution is supplied by the
G1–G3 product estimates (`PhiBProdStripBound`, `PhiBProdStripLowerBound`); wiring the raw
ratio bound here into the meromorphic-normal-form `hbdd` of
`FaddeevUniquenessBoundedCapstone` is the remaining G5 step.

Verified `lean`-direct against `PhiBProd`. Sorry-free.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
--        https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md
-/

open Complex
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta

/-- **Strip-growth characterization class.** `Φ` is comparable in modulus to the canonical
product `phiBProd b`: some `C > 0` bounds each by `C` times the other, everywhere. This is
the growth condition that singles out the physical `Φ_b` among the shift-solutions; it
carries the comparability **hypothesis**, not the uniqueness conclusion. -/
class FaddeevPhiStripGrowth (b : ℂ) (Φ : ℂ → ℂ) : Prop where
  comparable : ∃ C : ℝ, 0 < C ∧
    ∀ z, ‖Φ z‖ ≤ C * ‖phiBProd b z‖ ∧ ‖phiBProd b z‖ ≤ C * ‖Φ z‖

/-- **`phiBProd` is a strip-growth instance** (`C = 1`) — the class is non-vacuous, realized
by the canonical product itself. -/
instance instPhiBProd (b : ℂ) : FaddeevPhiStripGrowth b (phiBProd b) :=
  ⟨1, one_pos, fun z => ⟨by rw [one_mul], by rw [one_mul]⟩⟩

/-- **Bounded ratio of two strip-growth solutions.** If `Φ₁` and `Φ₂` are both comparable to
`phiBProd b`, their ratio is bounded off `Φ₂`'s zeros: `‖Φ₁ z / Φ₂ z‖ ≤ C₁·C₂`. This is the
raw-ratio boundedness input the Liouville/boundedness capstone consumes (G5). -/
theorem ratio_bounded_of_stripGrowth (b : ℂ) (Φ₁ Φ₂ : ℂ → ℂ)
    [h₁ : FaddeevPhiStripGrowth b Φ₁] [h₂ : FaddeevPhiStripGrowth b Φ₂] :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ z, Φ₂ z ≠ 0 → ‖Φ₁ z / Φ₂ z‖ ≤ C := by
  obtain ⟨C₁, hC₁, hcomp₁⟩ := h₁.comparable
  obtain ⟨C₂, hC₂, hcomp₂⟩ := h₂.comparable
  refine ⟨C₁ * C₂, by positivity, fun z hz => ?_⟩
  rw [norm_div]
  have hd : 0 < ‖Φ₂ z‖ := norm_pos_iff.mpr hz
  rw [div_le_iff₀ hd]
  calc ‖Φ₁ z‖ ≤ C₁ * ‖phiBProd b z‖ := (hcomp₁ z).1
    _ ≤ C₁ * (C₂ * ‖Φ₂ z‖) := mul_le_mul_of_nonneg_left (hcomp₂ z).2 hC₁.le
    _ = C₁ * C₂ * ‖Φ₂ z‖ := by ring

end QOU.QBeta
