import Mathlib.Analysis.MeanInequalities
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
# QOU.MassTheory.PnBalancePointSpectralGap

**The p-n interface letter sits at the spectral balance point, and AM-GM puts its
growth rate strictly below both like-pair letters — at every crossing
multiplicity.**

Bean `qou-brng`, escape class B.

## What this is for

`QOU.MassTheory.PnBetweennessBlocksSignMixed.pn_betweenness_blocks_signMixed`
rules out the sign-mixed pattern using two hypotheses, and the 2026-09-12 entry
on `qou-brng` named them as class B's whole remaining escape: the **averaging**
of the p-n letter, and the **affineness** of the interface law `μ = z + d`.

Affineness is an `m = 1` fact.  The interface letter `σ_g + d·I` has two-strand
trace `z + d` (`QOU.Mass.ChainTraceFactor.twoStrandTrace_eq`), but at crossing
multiplicity `m` the letter is `(σ_g + d·I)^m`, whose trace is degree `m` in `d`
— already `(d² + 1) + (2d + h)·z` at `m = 2`.  So the hypothesis is genuinely
breakable, and measured, betweenness itself fails from `m = 12`
(`computations/probes/multiplicity_breaks_affineness_but_not_the_pattern_probe.py`).

**It breaks the wrong way.**  Diagonalising, `σ_g` has Hecke eigenvalues `q` and
`-q⁻¹`, so the multiplicity-`m` trace is `w₊(d+q)^m + w₋(d-q⁻¹)^m`.  The growth
rate of each letter is therefore its spectral radius `max |d+q| |d-q⁻¹|`:

| letter | `d` | spectral radius |
|---|---|---|
| pp | `0` | `q` |
| nn | `-h` | `q` |
| pn | `≈ -h/2` | `≈ (q + q⁻¹)/2` |

This file proves the three facts that make the last column decide the question:
`balance_eigen_neg` (at `d = -h/2` the two eigenvalues are exact negatives, both
of magnitude `(q+q⁻¹)/2`), `one_lt_balance` (AM-GM), and `balance_lt_self`
(`(q+q⁻¹)/2 < q` for `q > 1`).  Hence `pn_spectralRadius_lt_pp`: the p-n channel
grows strictly slower than either like-pair channel, at every `q > 1`.

The gap is `growth_gap_eq`: `q / ((q+q⁻¹)/2) = 2q²/(q²+1)`, which is
`1 + tanh(log q)` — the crossing discriminant `QOU.Braiding.em_strong_ratio_tanh`
already carries in that form, and the one `qou-hjs8` proved θ-free.

## Scope

**Scope (b)** for the asymptotic statement; invariant = AM-GM on the two Hecke
eigenvalues, and it mentions no numerical value.  The small-`m` statement is
measured, not proved.

It does **not** exclude class B: a derived p-n letter that is *not* at the
balance point is untouched, and that is now the whole of class B's remaining
room.  It says nothing about **magnitude**, which is `qou-brng`'s real target.
-/

namespace QOU.MassTheory.PnBalancePointSpectralGap

variable {q : ℝ}

/-- The Hecke `h = q - q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- The spectral balance offset `d = -h/2`. -/
noncomputable def balanceOffset (q : ℝ) : ℝ := -(heckeH q) / 2

/-- Half the quantum dimension of the fundamental, `[2]_q/2 = (q + q⁻¹)/2`. -/
noncomputable def halfQuantumDim (q : ℝ) : ℝ := (q + q⁻¹) / 2

/-- **The balance point is where the two Hecke eigenvalues become exact
negatives.**  At `d = -h/2`, `(d + q) + (d - q⁻¹) = 0`. -/
theorem balance_eigen_neg (q : ℝ) :
    (balanceOffset q + q) + (balanceOffset q - q⁻¹) = 0 := by
  unfold balanceOffset heckeH
  ring

/-- **and both have magnitude `[2]_q/2`.** -/
theorem balance_eigen_pos (q : ℝ) : balanceOffset q + q = halfQuantumDim q := by
  unfold balanceOffset heckeH halfQuantumDim
  ring

theorem balance_eigen_neg' (q : ℝ) : balanceOffset q - q⁻¹ = -halfQuantumDim q := by
  unfold balanceOffset heckeH halfQuantumDim
  ring

/-- **AM-GM.**  For `q > 1` the arithmetic mean of `q` and `q⁻¹` exceeds their
geometric mean `1`. -/
theorem one_lt_balance (hq : 1 < q) : 1 < halfQuantumDim q := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  unfold halfQuantumDim
  rw [lt_div_iff₀ (by norm_num : (0:ℝ) < 2)]
  have hq1 : (0 : ℝ) < q - 1 := by linarith
  have key : 0 < (q - 1) ^ 2 / q := div_pos (pow_pos hq1 2) hq0
  have hexp : q + q⁻¹ - 1 * 2 = (q - 1) ^ 2 / q := by
    field_simp
    ring
  linarith [hexp ▸ key]

/-- **The balance rate is strictly below `q`.**  `(q + q⁻¹)/2 < q` for `q > 1`. -/
theorem balance_lt_self (hq : 1 < q) : halfQuantumDim q < q := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  unfold halfQuantumDim
  rw [div_lt_iff₀ (by norm_num : (0:ℝ) < 2)]
  have key : 0 < (q ^ 2 - 1) / q := by
    apply div_pos _ hq0
    nlinarith
  have hexp : q * 2 - (q + q⁻¹) = (q ^ 2 - 1) / q := by
    field_simp
    ring
  linarith [hexp ▸ key]

/-- **The p-n channel grows strictly slower than either like-pair channel.**

`pp` and `nn` have spectral radius `q`; the balance-point p-n letter has
`(q + q⁻¹)/2`, and AM-GM sandwiches it strictly between `1` and `q`. -/
theorem pn_spectralRadius_lt_pp (hq : 1 < q) :
    1 < halfQuantumDim q ∧ halfQuantumDim q < q :=
  ⟨one_lt_balance hq, balance_lt_self hq⟩

/-- **The growth gap in closed form:** `q / ((q+q⁻¹)/2) = 2q²/(q²+1)`.

This is `1 + tanh (log q)`, the crossing discriminant carried by
`QOU.Braiding.em_strong_ratio_tanh` — so the amount by which the like-pair
channels outgrow the p-n channel is `1 + δ_CP`. -/
theorem growth_gap_eq (hq : 1 < q) :
    q / halfQuantumDim q = 2 * q ^ 2 / (q ^ 2 + 1) := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold halfQuantumDim
  rw [div_div_eq_mul_div]
  field_simp

end QOU.MassTheory.PnBalancePointSpectralGap
