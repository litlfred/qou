import QOU.MathlibExt.NormalizedSumClosure
import QOU.MathlibExt.HconvConventionBridge

/-!
# QOU.MathlibExt.NormalizedSumUnconditional — `normalizedSum n q = 1`, unconditionally

The general-`n` fake-degree residual `normalizedSum n q = 1` (bean `qou-3quc`) is now proved
**unconditionally** (no hypotheses beyond the substrate regime `1 < q`), by discharging the last
hypothesis of the telescope-closure assembly
`NormalizedSumClosure.normalizedSum_eq_one_of_convBridge` (#6011) with the now-proved convention
bridge `HconvConventionBridge.hconv` (piece 3). The three inputs of the assembly are supplied from
`1 < q`:

* `hq2 : 1 < q²` (`nlinarith`);
* `hgen : ∀ k ≠ 0, (q²)^k ≠ 1` (`zpow` injectivity, `q² > 1`);
* `hconv` per partition `p`, from `HconvConventionBridge.hconv` on the sorted carrier `toList p`
  (`toList_sorted`, `toList_sum`).

This closes the Lean side of `qou-3quc`: `normalizedSum n q = 1` for every `n` and every `1 < q`,
with axioms `[propext, Classical.choice, Quot.sound]` (no `sorryAx`).
-/

namespace QOU.MathlibExt.NormalizedSumUnconditional

open QOU.MathlibExt.MolienFakeDegreeGeneralN
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Mathlib.PartitionListBridge

/-- **`normalizedSum n q = 1`, unconditionally** (for `1 < q`). The general-`n` q-analogue fake-degree
identity, closed via the corpus general-X Macdonald telescope at `X = 0` and the convention bridge
`hconv` — the whole of `qou-3quc`. -/
theorem normalizedSum_eq_one (n : ℕ) (q : ℝ) (hq : 1 < q) :
    normalizedSum n q = 1 := by
  have hq2 : 1 < q ^ 2 := by nlinarith
  refine NormalizedSumClosure.normalizedSum_eq_one_of_convBridge n q hq2 ?_ ?_
  · -- genericity of the (Q = q²) specialisation
    intro k hk h
    apply hk
    have h0 : (q ^ 2) ^ k = (q ^ 2) ^ (0 : ℤ) := by rw [h, zpow_zero]
    exact zpow_right_injective₀ (by linarith) (ne_of_gt hq2) h0
  · -- the convention bridge on the sorted carrier
    intro p
    rw [HconvConventionBridge.hconv q (toList p) (toList_sorted p) hq, toList_sum p]

/-- **The general-`n` Molien / fake-degree identity** `molienSum n q = [n]_q!`, unconditionally
(for `1 < q`) — i.e. `Σ_{λ⊢n} f^λ · q^{−κ_λ} · qDim_q(λ) = [n]_q!`. The headline consequence of
`normalizedSum_eq_one` via `molienSum_eq_qFactorial_iff`, whose docstring records this as the open
content of `qou-3quc` that it "does not close, it locates". Now closed. -/
theorem molienSum_eq_qFactorial (n : ℕ) (q : ℝ) (hq : 1 < q) :
    molienSum n q = qFactorial q n :=
  (molienSum_eq_qFactorial_iff n q hq).mpr (normalizedSum_eq_one n q hq)

end QOU.MathlibExt.NormalizedSumUnconditional
