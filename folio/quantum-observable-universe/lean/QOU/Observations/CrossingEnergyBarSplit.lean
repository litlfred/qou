/-
# The crossing energy's bar-split: writhe is bar-even, crossing number bar-odd

Beans `qou-fi93` and `qou-hjs8`; probe
`computations/barparity/crossing_energy_bar_split_probe.py`.

`qou-fi93` establishes that every counting object the framework defines is
*exactly* bar-even — `[n]_q`, `d_q(λ)`, the Plancherel measure, `Σ y_λ` — and
concludes, as a scope-(b) exclusion, that the colour-curve asymmetry cannot
reach a number density.  Its constructive consequence is that a counting
measure **not** built from q-integers would be needed.

This file formalises two facts that bear on that, both about *shape* rather
than about physics:

1. The crossing energy `E = n₊·q − n₋·q⁻¹` (`def:crossing-energy`, a SUM of
   degree-`±1` terms) splits under the bar involution into a bar-even part
   carrying the **writhe** `n₊ − n₋` and a bar-odd part carrying the
   **crossing number** `n₊ + n₋`.  Two topological counting integers, on
   opposite bar-parities.

2. A ratio of two bar-odd quantities is bar-even.  That is *why* `[n]_q =
   (qⁿ − q⁻ⁿ)/(q − q⁻¹)` has no bar-odd content: numerator and denominator
   are each bar-odd and the signs cancel.  The framework's bar-odd content is
   **divided out**, not absent — and the crossing energy is the object that
   keeps the factor `q − q⁻¹` undivided.

Nothing here derives a baryon asymmetry, an `η`, or any number density, and
nothing here selects `qⁿ − q⁻ⁿ` as the right object.  It proves the mechanism
by which division destroys bar-odd content, which is what makes `qou-fi93`'s
observation a mechanism rather than a coincidence.

Generic over a `Field`; no anchor, no `ℝ`, per §7c.  The evaluation at `q₀`
lives in the probe.

-- Ref: [leitner2026] `def:crossing-energy`,
--      `prop:antiparticle-crossing-reversal`, beans `qou-fi93` / `qou-hjs8`
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Observations.CrossingEnergyBarSplit

variable {K : Type*} [Field K]

/-- The crossing energy of a braid with `np` positive and `nm` negative
crossings: `def:crossing-energy` weights `L₊` by `q` and `L₋` by `−q⁻¹`, and
SUMS them.  The sum, rather than a product, is what makes this inhomogeneous
in `q` and hence not bar-even. -/
def crossingEnergy (np nm q : K) : K := np * q - nm * q⁻¹

/-- The bar involution `q ↦ q⁻¹` applied to the crossing energy. -/
def crossingEnergyBar (np nm q : K) : K := np * q⁻¹ - nm * q

/-- `crossingEnergyBar` really is `crossingEnergy` at `q⁻¹` — stated so the
name is not taken on trust. -/
theorem crossingEnergyBar_eq (np nm q : K) :
    crossingEnergyBar np nm q = crossingEnergy np nm q⁻¹ := by
  unfold crossingEnergyBar crossingEnergy
  rw [inv_inv]

/-- **The bar-EVEN part carries the WRITHE.** -/
theorem bar_even_eq_writhe (np nm q : K) :
    crossingEnergy np nm q + crossingEnergyBar np nm q
      = (np - nm) * (q + q⁻¹) := by
  unfold crossingEnergy crossingEnergyBar
  ring

/-- **The bar-ODD part carries the CROSSING NUMBER.** -/
theorem bar_odd_eq_crossing_number (np nm q : K) :
    crossingEnergy np nm q - crossingEnergyBar np nm q
      = (np + nm) * (q - q⁻¹) := by
  unfold crossingEnergy crossingEnergyBar
  ring

/-- **The mirror swaps `n₊` and `n₋`** (`prop:antiparticle-crossing-reversal`
item 2: negate, then `q ↔ q⁻¹`).  So the writhe is negated and the crossing
number is preserved: the bar-ODD part is the mirror-invariant one. -/
theorem mirror_swaps (np nm q : K) :
    -crossingEnergyBar np nm q = crossingEnergy nm np q := by
  unfold crossingEnergy crossingEnergyBar
  ring

/-- **A ratio of two bar-ODD quantities is bar-EVEN.**  This is the mechanism:
`[n]_q`'s numerator and denominator are each bar-odd, so the bar acts on the
ratio as `(−f)/(−g) = f/g` and the bar-odd content cancels.  Stated
abstractly — `fb`/`gb` are the barred values, and the hypotheses say each is
the negation of its unbarred partner — so it applies to any such ratio, not
only to `[n]_q`. -/
theorem bar_odd_ratio_is_bar_even {f g fb gb : K}
    (hf : fb = -f) (hg : gb = -g) :
    fb / gb = f / g := by
  rw [hf, hg, neg_div_neg_eq]

/-- The q-integer's numerator and denominator, related by the identity that
makes the constructive candidate explicit: `qⁿ − q⁻ⁿ = [n]_q · (q − q⁻¹)`.
Stated for an arbitrary `num`, so it is the *algebra* of not-dividing rather
than a claim about any particular `n`. -/
theorem undivided_eq (num q : K) (h : q - q⁻¹ ≠ 0) :
    (num / (q - q⁻¹)) * (q - q⁻¹) = num :=
  div_mul_cancel₀ num h

end QOU.Observations.CrossingEnergyBarSplit
