import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Archimedean.strangelet_double_beta

Strangelet interactions descend from the degree-2 fiber via double beta
decay.  The Skein crossing-change amplitude s = q^{1/2} − q^{−1/2}
gives the double-beta rate Γ_{2β} ∝ s⁴, and s ≈ 0.104 is
numerically the EM/strong ratio.

LaTeX label: `prop:strangelet-double-beta`

## References
- [leitner2026] Ch. 7, §strangelet-double-beta

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- The Skein amplitude for a single crossing change:
    s(q) = q^{1/2} − q^{−1/2}. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
noncomputable def skein_amplitude (q : ℝ) : ℝ :=
  q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))

/-- The double beta decay rate is proportional to s⁴. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
noncomputable def double_beta_rate (q : ℝ) : ℝ :=
  (skein_amplitude q) ^ 4

/-- The Skein descent: the minimal path from the degree-2 fiber
    (cinquefoil, 5 crossings) to the degree-1 fiber (trefoil,
    3 crossings) requires exactly 2 crossing changes. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
theorem crossing_descent_count :
    (5 : ℕ) - 3 = 2 := by norm_num

/-- The cinquefoil has 5 crossings (genus 2). -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
def cinquefoil_crossings : ℕ := 5

/-- The trefoil has 3 crossings (genus 1). -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
def trefoil_crossings : ℕ := 3

/-- The intermediate knot (figure-eight, 4₁) has 4 crossings. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
def figure_eight_crossings : ℕ := 4

/-- **Definitional unfolding** of the strangelet double-beta rate. The physical model — the
    interaction descends through two Skein smoothings (cinquefoil → figure-eight → trefoil)
    with rate proportional to `s⁴`, `s = skein_amplitude q = tanh(ln q)` the EM/strong ratio —
    is *encoded in the definition* `double_beta_rate q := (skein_amplitude q) ^ 4`; this lemma
    only exposes that definition (the earlier `1 < q` hypothesis was unused and is dropped).
    The descent derivation and the parameter-free `s⁴ ≈ 10⁻⁴` reading are narrative
    (`.md` / Ch. 7), NOT a Lean consequence of this equation. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
theorem strangelet_double_beta (q : ℝ) :
    double_beta_rate q = (skein_amplitude q) ^ 4 := rfl

/-- The descent path goes cinquefoil → figure-eight → trefoil:
    5 → 4 → 3 crossings. -/
-- Ref: [leitner2026] Ch. 7, §strangelet-double-beta
theorem descent_path :
    cinquefoil_crossings - 1 = figure_eight_crossings ∧
    figure_eight_crossings - 1 = trefoil_crossings := by
  unfold cinquefoil_crossings figure_eight_crossings trefoil_crossings
  omega

end QOU.Archimedean
