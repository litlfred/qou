/-
# What the two carrier fields force at the classical point

Bean `qou-pdix`. Computed in
`computations/qbeta/qbeta_eigenphase_carrier_classical_limit_probe.py` (5/5).

`qou-pdix`'s remaining job is to produce `M` from the Hecke seminormal
representation on `V_(2,1)` satisfying

    QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum (q) (M) :
        M.trace = 2 * cos (eigenphase q)   ∧   M.det = 1

and prove those two fields. Entry 6 of that bean expands `α` about `q = 1 + t`
and tests it against a holonomy ansatz; what had not been asked is what the two
fields force about **`M` itself** at `q = 1`. Three things, and none of them
mentions which convention is right.

**`α(1) = 0`** — its `t¹` coefficient is `z(1) − 1 = −1/2` under *both*
conventions — so `tr M(1) = 2 cos 0 = 2` while `det M(1) = 1`. The
characteristic polynomial is then `x² − 2x + 1 = (x−1)²`
(`charpoly_of_trace_two_det_one`), both eigenvalues are `1`, and **`M(1)` is
unipotent**. Not `I`: at `q = 1` the algebra is `ℂ[S₃]` whose `(2,1)` block is
all of `M₂(ℂ)`, so a nontrivial Jordan block is permitted.

**Unless `M` normalises a single braid word's image** — then `M(1)` lies in the
`S₃` image, semisimple by Maschke, hence diagonalisable; unipotent **and**
diagonalisable forces `M(1) = I`, so the word must degenerate to the identity
permutation. A second and simpler reason for that bean's route-1 closure, needing
only the classical point.

## The exclusion this file records

Step 26 established `Δ_L = NF(neutron) − NF(proton)` as the corpus's **only
elliptic** operator — the only one clearing `qou-pdix`'s TIER-0 condition `D0`
(`det A > 0`, spectrum `±iθ`). Its classical eigenphase is **exactly `2π/3`**,
because every NF coordinate carries `(q−1)(q+1)` and the leading direction is
`−(1 + T₁T₀)` with `T₁T₀` the `S₃` three-cycle.

`carrier_trace_at_classical_point` gives the requirement, `two_cos_two_pi_div_three`
the value `Δ_L` actually supplies, and `delta_L_is_not_a_carrier` the mismatch.
It is **structural, not a near-miss**: `χ^{(2,1)}` of a three-cycle is `−1`, and
trace `2` identifies the identity class uniquely in that character table.

## What is deliberately not here

The `t`-series coefficients (`tr M = 2 − t²/4 + O(t³)` identically for both
conventions, first differing at `t³` — `1/4` vs `5/4`) are **measurements** and
live in the witness. So does the consequence that the bean's acceptance-test
part 1, read on the trace, is convention-blind through `t²`.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.QBeta

/-- With `tr M = 2` and `det M = 1` the characteristic polynomial is `(x−1)²`,
so both eigenvalues are `1` and `M` is **unipotent**. -/
theorem charpoly_of_trace_two_det_one (x : ℝ) :
    x ^ 2 - 2 * x + 1 = (x - 1) ^ 2 := by ring

/-- The carrier's trace at the classical point. `α(1) = 0` because `α`'s `t¹`
coefficient is `z(1) − 1 = −1/2` in both conventions, so `tr M(1) = 2 cos 0`. -/
theorem carrier_trace_at_classical_point : 2 * Real.cos 0 = 2 := by
  rw [Real.cos_zero]; norm_num

/-- What `Δ_L` supplies instead: its classical eigenphase is exactly `2π/3`, and
`2 cos (2π/3) = −1` — the `S₃` three-cycle's character. -/
theorem two_cos_two_pi_div_three : 2 * Real.cos (2 * Real.pi / 3) = -1 := by
  have h : 2 * Real.pi / 3 = Real.pi - Real.pi / 3 := by ring
  rw [h, Real.cos_pi_sub, Real.cos_pi_div_three]
  norm_num

/-- **`Δ_L` is not a carrier**, and fails at order zero. A carrier needs
`tr M(1) = 2`; the corpus's only elliptic operator — the only one clearing
TIER-0 `D0` — gives `−1`. -/
theorem delta_L_is_not_a_carrier :
    2 * Real.cos (2 * Real.pi / 3) ≠ 2 * Real.cos 0 := by
  rw [two_cos_two_pi_div_three, carrier_trace_at_classical_point]
  norm_num

/-- The gap is exactly `3`, the distance between the identity's character and a
three-cycle's in `χ^{(2,1)}` — so the exclusion is a character-table fact. -/
theorem carrier_gap_is_three :
    2 * Real.cos 0 - 2 * Real.cos (2 * Real.pi / 3) = 3 := by
  rw [two_cos_two_pi_div_three, carrier_trace_at_classical_point]
  norm_num

end QOU.QBeta
