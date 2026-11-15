import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import QOU.Mass.BindingRecurrenceSpectral
import QOU.Mass.Lever1TauClosedForm

/-!
# QOU.Mass.BindingTauAnchorClosure — wired anchors force `τ > 2` ⇒ binding kernel extensive

Companion to `QOU.Mass.Lever1Tau.tau_kernel_closed_form`, which proves the wired-anchor seed
`τ = (a_D^(2) + a_D^(4)) / a_D^(3)` equals the closed form `3(3q⁴ + 8q² + 3)/(4q(q+1)²)` (the three
production-wired prolonged Seiberg–Witten period anchors `a_D^(2)=1`, `a_D^(3)=(q+1)²/(3q)`,
`a_D^(4)=(3q²+4+3q⁻²)/4`). **This file does not re-prove that identity** — it cites it — and adds the
two facts that file does not:

* `tauAnchor_gt_two` — `0 < q ⇒ 2 < τ` throughout the substrate regime, via the sum-of-squares
  positivity `504·(τ·den − 2·den) = 56(9q²−4q)² + (56q−36)² + 3240 > 0`;
* `binding_extensive_at_substrate` — composing with `QOU.Mass.lambdaPlus_gt_one` (the abstract
  `τ>2 ⇒ λ₊>1` spectral bridge), the depth-2 binding kernel `R = x²−τx+1` is **extensive**
  (`λ₊ > 1`) given the anchors — the property the saturating `|χ|` joint trace (`τ=2`, `λ=1`) lacks.

Plus the bar-antisymmetric **odd partner** `a_D^(5) = τ·a_D^(4) − a_D^(3)` and its closed form.

## Scope (honest)

Algebraic half only: the wired anchor *values* force this `τ`, `τ > 2`, hence extensivity. It does
**not** derive the geometric residual `a_D^(n) = ∮ λ_SW^(n) = lw(n−1)` (this `τ` = abelianised
`λ_SW` Gauss–Manin holonomy on color `E_q`) — the owner-gated keystone
(`conj:qdifference-kernel-prolongation-symbol`). The Step-1 geometry probe
`computations/substrate/lever1_color_sigma_geometry_probe.py` shows the bare differential carries
zero residue at the finite branch points, so that identification needs the prolongation operator
`λ_SW^(n) → a_D^(n)`, left "by induction" (the construction gap).

LaTeX label: `prop:binding-tau-anchor-closure` (interprets `prop:binding-genfun-qdifference`).

## References
- [leitner2026] §mass-theory/binding-genfun-qdifference, §mass-theory/sl2-prolongation-recurrence
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4
-/

namespace QOU.Mass

open Real

/-- `a_D^(3) = lw(2) = (q+1)²/(3q)` (Hopf-link anchor, c = 2). -/
noncomputable def aD3 (q : ℝ) : ℝ := (q + 1) ^ 2 / (3 * q)

/-- `a_D^(4) = lw(3) = (3q² + 4 + 3q⁻²)/4` (proton / Family-A anchor, c = 3). -/
noncomputable def aD4 (q : ℝ) : ℝ := (3 * q ^ 2 + 4 + 3 / q ^ 2) / 4

/-- The binding-kernel trace from the `det = 1` depth-2 recurrence
`a_D^(4) = τ·a_D^(3) − a_D^(2)` with `a_D^(2) = 1`: `τ = (1 + a_D^(4)) / a_D^(3)`. -/
noncomputable def tauAnchor (q : ℝ) : ℝ := (1 + aD4 q) / aD3 q

/-- **Closed form of the wired trace** — `τ = 3(3q⁴ + 8q² + 3)/(4q(q+1)²)`. Cites
`Lever1Tau.tau_kernel_closed_form` (no re-proof of the field identity). -/
theorem tauAnchor_closed_form {q : ℝ} (hq : 0 < q) :
    tauAnchor q = 3 * (3 * q ^ 4 + 8 * q ^ 2 + 3) / (4 * q * (q + 1) ^ 2) := by
  unfold tauAnchor aD3 aD4
  exact Lever1Tau.tau_kernel_closed_form q hq.ne' (by positivity)

/-- **The wired trace exceeds `2` throughout the substrate regime.** For every `q > 0`, `2 < τ`.
The obstruction is the sum-of-squares positivity of the numerator `9q⁴ − 8q³ + 8q² − 8q + 9`. -/
theorem tauAnchor_gt_two {q : ℝ} (hq : 0 < q) : 2 < tauAnchor q := by
  rw [tauAnchor_closed_form hq, lt_div_iff₀ (by positivity : (0 : ℝ) < 4 * q * (q + 1) ^ 2)]
  nlinarith [sq_nonneg (9 * q ^ 2 - 4 * q), sq_nonneg (56 * q - 36), hq, sq_nonneg q]

/-- **The binding kernel is extensive at the substrate.** Given the wired anchors, the dominant root
of `R(q,x) = x² − τx + 1` exceeds `1` for every `q > 0` — the extensive (A-scaling) growth a
saturating multiplicative trace (`τ = 2`, `λ = 1`) cannot source. Composes `tauAnchor_gt_two` with
the abstract spectral bridge `lambdaPlus_gt_one`. -/
theorem binding_extensive_at_substrate {q : ℝ} (hq : 0 < q) :
    1 < lambdaPlus (tauAnchor q) :=
  lambdaPlus_gt_one (tauAnchor_gt_two hq)

/-- The depth-2 recurrence's `n=5` term — the bar-antisymmetric **odd partner**
`a_D^(5) = τ·a_D^(4) − a_D^(3)`. -/
noncomputable def aD5 (q : ℝ) : ℝ := tauAnchor q * aD4 q - aD3 q

/-- **Closed form of the odd partner.**
`a_D^(5) = (81q⁸ + 308q⁶ − 64q⁵ + 354q⁴ − 64q³ + 308q² + 81) / (48q³(q+1)²)` (`≈ 5.3556` at `q₀`).

Honest scope: this is the depth-2 kernel's `n=5` *prediction* — exact through the seed `n ≤ 4`, but
the independently-computed selection-rule value `lw(4)` does **not** satisfy the recurrence (it
differs by `≈ 0.4 %`; the windowed-kernel drift now Lean-proved at `q=1` in
`QOU.Mass.Lever1Depth2Exclusion`). So this is the kernel's value, **not** a claim that
`a_D^(5) = lw(4)`. -/
theorem aD5_closed_form {q : ℝ} (hq : 0 < q) :
    aD5 q =
      (81 * q ^ 8 + 308 * q ^ 6 - 64 * q ^ 5 + 354 * q ^ 4 - 64 * q ^ 3
        + 308 * q ^ 2 + 81) / (48 * q ^ 3 * (q + 1) ^ 2) := by
  have hq0 : q ≠ 0 := hq.ne'
  have hq1 : q + 1 ≠ 0 := by positivity
  unfold aD5
  rw [tauAnchor_closed_form hq]
  unfold aD3 aD4
  field_simp
  ring

end QOU.Mass
