/-
# Jet-filtration graded dimension: the single-knob TWO-ANCHOR NO-GO

`QOU.MassTheory.JetFiltrationGradedDimEscape` proved the NON-determinant
coinvariant graded dimension `W_A(q) = ∏_{k=1}^{A}[k]_q` **escapes** the
exchange-determinant cap (`ρ_grad(4) = [3]_q·[4]_q ≥ 12 > 6`), placing the
true binding magnitude in the **two-sided bracket**

    −ln det  (capped ρ_A ≤ C(A,2); too flat)  <  true  <  [A]_q!  (too steep).

This file closes the *other* side of that bracket: it proves, sorry-free, that
the single-parameter `q`-scaled graded dimension **cannot land both** light-nucleus
anchors `{ρ_strong(3) ≈ 3.8128, ρ_strong(4) ≈ 13.0316}` — the "one knob cannot do
both" observation the jet-filtration probe recorded only as Python assertions
(W5 of the 2026-07-24 binding-mass workplan, formalize-first). Three facts:

* **(S) step-lock** — for every `q ≥ 1`, `[4]_q ≥ 4`. The A=3→A=4 graded step is
  bounded below by its classical value at *every* admissible substrate `q`; since
  the data step `ρ_strong(4)/ρ_strong(3) ≈ 3.418 < 4`, the graded step overshoots
  the data step for all `q ≥ 1` (a `q`-independent, AME-independent invariant).
* **(M) single-knob monotonicity** — both `q ↦ [3]_q` and `q ↦ [3]_q·[4]_q` are
  monotone increasing on `[1,∞)`. The one knob `q` moves the (under-shot) A=3 ratio
  and the (over-shot) A=4 ratio in the *same* direction — it cannot raise one while
  lowering the other.
* **(N) two-anchor no-go** — for every `q ≥ 1`, if `[3]_q ≥ ρ_strong(3)` then
  `[3]_q·[4]_q > ρ_strong(4)`: reaching the A=3 target *forces* an A=4 overshoot
  (`ρ_strong(3)·4 = 15.2512 > 13.0316`). No single parameter-free `q` lands both.

**Anti-fit (STRICT).** `ρ_strong(3)=3.8128`, `ρ_strong(4)=13.0316` are consumed as
DERIVED-ELSEWHERE comparison constants (isospin/Coulomb-corrected AME, #3986/#3990;
the committed jet-filtration witness) and appear ONLY as bounds in (N). No `q` is
solved from them; nothing is wired. (S)/(M) are AME-independent scope-(b) invariants.
Base ring `ℝ` per §7c (ordering inequalities on `1 ≤ q`).

Companion probe: `computations/deltalambda/deltalambda_graded_two_anchor_nogo_probe.py`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-- `ρ_grad(3) = W_3/W_2 = [3]_q = 1 + q + q²` (the A=3 coinvariant graded ratio). -/
def gradedRatio3 (q : ℝ) : ℝ := 1 + q + q ^ 2

/-- `[4]_q = 1 + q + q² + q³`, the multiplicative A=3→A=4 graded step
(`ρ_grad(4) = gradedRatio3 · gradedStep4`). -/
def gradedStep4 (q : ℝ) : ℝ := 1 + q + q ^ 2 + q ^ 3

/-- **(S) step-lock.** For `q ≥ 1`, the graded A=3→A=4 step `[4]_q ≥ 4`.
Exact factorisation `[4]_q − 4 = (q−1)(q² + 2q + 3)`, non-negative on `q ≥ 1`. -/
theorem gradedStep4_ge_four (q : ℝ) (hq : 1 ≤ q) : 4 ≤ gradedStep4 q := by
  have h0 : 0 ≤ q - 1 := by linarith
  have key : gradedStep4 q - 4 = (q - 1) * (q ^ 2 + 2 * q + 3) := by
    unfold gradedStep4; ring
  nlinarith [mul_nonneg h0 (by positivity : (0 : ℝ) ≤ q ^ 2 + 2 * q + 3), key]

/-- **(S′) graded step strictly exceeds the data step for every `q ≥ 1`.**
The isospin-corrected data step `ρ_strong(4)/ρ_strong(3) = 13.0316/3.8128 ≈ 3.418`
is `< 4 ≤ [4]_q`, so no `q ≥ 1` flattens the graded step to the observed growth. -/
theorem gradedStep4_gt_data_step (q : ℝ) (hq : 1 ≤ q) :
    (13.0316 / 3.8128 : ℝ) < gradedStep4 q := by
  have h := gradedStep4_ge_four q hq
  have : (13.0316 / 3.8128 : ℝ) < 4 := by norm_num
  linarith

/-- **(M) single-knob monotonicity, A=3.** `q ↦ [3]_q` is monotone on `[1,∞)`. -/
theorem gradedRatio3_mono {a b : ℝ} (ha : 1 ≤ a) (hab : a ≤ b) :
    gradedRatio3 a ≤ gradedRatio3 b := by
  unfold gradedRatio3
  have hb : 1 ≤ b := le_trans ha hab
  nlinarith [sq_nonneg (b - a), mul_nonneg (by linarith : (0:ℝ) ≤ a) (by linarith : (0:ℝ) ≤ b - a)]

/-- Positivity of `[3]_q` on `q ≥ 1` (used for the product monotonicity). -/
theorem gradedRatio3_pos (q : ℝ) (hq : 1 ≤ q) : 0 < gradedRatio3 q := by
  unfold gradedRatio3; positivity

/-- Positivity of `[4]_q` on `q ≥ 1`. -/
theorem gradedStep4_pos (q : ℝ) (hq : 1 ≤ q) : 0 < gradedStep4 q := by
  unfold gradedStep4; positivity

/-- **(M) single-knob monotonicity, A=4.** `q ↦ ρ_grad(4) = [3]_q·[4]_q` is monotone
on `[1,∞)`. Together with `gradedRatio3_mono`, the single knob `q` moves BOTH the
A=3 and A=4 ratios upward — it cannot push one up and the other down. -/
theorem gradedRatio4_mono {a b : ℝ} (ha : 1 ≤ a) (hab : a ≤ b) :
    gradedRatio3 a * gradedStep4 a ≤ gradedRatio3 b * gradedStep4 b := by
  have hb : 1 ≤ b := le_trans ha hab
  have h3 : gradedRatio3 a ≤ gradedRatio3 b := gradedRatio3_mono ha hab
  have h4 : gradedStep4 a ≤ gradedStep4 b := by
    unfold gradedStep4
    nlinarith [sq_nonneg (b - a), mul_nonneg (by linarith : (0:ℝ) ≤ a) (by linarith : (0:ℝ) ≤ b - a),
      mul_nonneg (by positivity : (0:ℝ) ≤ a ^ 2) (by linarith : (0:ℝ) ≤ b - a),
      mul_nonneg (by linarith : (0:ℝ) ≤ b) (sq_nonneg (b - a))]
  have h3a : 0 ≤ gradedRatio3 a := le_of_lt (gradedRatio3_pos a ha)
  have h4b : 0 ≤ gradedStep4 b := le_of_lt (gradedStep4_pos b hb)
  calc gradedRatio3 a * gradedStep4 a
      ≤ gradedRatio3 b * gradedStep4 a := by
        apply mul_le_mul_of_nonneg_right h3 (le_of_lt (gradedStep4_pos a ha))
    _ ≤ gradedRatio3 b * gradedStep4 b := by
        apply mul_le_mul_of_nonneg_left h4 (le_of_lt (gradedRatio3_pos b hb))

/-- **(N) the two-anchor NO-GO.** For every `q ≥ 1`, if the graded dimension reaches
the A=3 strong target (`[3]_q ≥ ρ_strong(3) = 3.8128`), then it strictly overshoots
the A=4 strong target: `ρ_grad(4) = [3]_q·[4]_q > ρ_strong(4) = 13.0316`, because
`[4]_q ≥ 4` (step-lock) and `3.8128 · 4 = 15.2512 > 13.0316`.

Hence **no single parameter-free `q` lands both light-nucleus anchors**: the
one-parameter `q`-scaled coinvariant graded dimension `[A]_q!` cannot close the
Δ_λ magnitude wall. The `2.2196` MeV-ratio no-go margin certifies that closing the
bracket requires a genuinely `A`-dependent (non-single-knob) damping — the `q`-knob
alone cannot tighten the two-sided bracket to the observed magnitudes. -/
theorem graded_two_anchor_nogo (q : ℝ) (hq : 1 ≤ q)
    (hreach3 : (3.8128 : ℝ) ≤ gradedRatio3 q) :
    (13.0316 : ℝ) < gradedRatio3 q * gradedStep4 q := by
  have hstep : 4 ≤ gradedStep4 q := gradedStep4_ge_four q hq
  have h3pos : (0 : ℝ) < gradedRatio3 q := gradedRatio3_pos q hq
  -- [3]_q·[4]_q ≥ [3]_q·4 ≥ 3.8128·4 = 15.2512 > 13.0316
  nlinarith [hreach3, hstep, h3pos,
    mul_le_mul_of_nonneg_left hstep (le_of_lt h3pos)]

end QOU.MassTheory
