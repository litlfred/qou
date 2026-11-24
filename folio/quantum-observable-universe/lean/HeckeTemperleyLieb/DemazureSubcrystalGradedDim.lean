/-
# Demazure sub-crystal graded dimension — the DAMPED `[A]_q!` (bracket + A=3 obstruction)

Scope-(b) certificate accompanying `deltalambda_demazure_subcrystal_magnitude_probe.py`
(this branch) and the follow-on to #4012 (`JetFiltrationGradedDimEscape.lean`).

#4012 proved the FULL coinvariant graded dimension ratio
`ρ_grad(A) = W_A(q)/W_2(q)` (with `W_A(q) = [A]_q! = ∏[k]_q = Σ_{w∈S_A} q^{ℓ(w)}`,
a NON-determinant object) ESCAPES the `SaturationRhoCap` determinant ceiling
`ρ_A ≤ C(A,2)` — but it OVERSHOOTS A=4 (`ρ_grad(4) = [3]_q·[4]_q`).

AGENTS.md §7b's interpolator is a **Demazure sub-crystal** graded dimension — a
Bruhat-prefix sub-sum of `[A]_q!`.  Concretely `[A]_q! = ∏_{k} [k]_q` and `[k]_q`
is the length-gen function of the `S_k/S_{k-1}` minimal coset reps; a coset-chain
Demazure sub-crystal truncates each coset at a prefix `[t_k+1]_q`, `t_k ≤ k−1`.
Full `t_k = k−1` recovers `[k]_q`.

This file records the two q-independent structural facts the probe rests on:

1. **Monotonicity (the A=3 obstruction).** A Bruhat sub-sum is `≤` the full sum
   (`1 ≤ [2]_q ≤ [3]_q` for `q ≥ 1`): the maximum of the A=3 Demazure family is
   the FULL ratio `[3]_q`.  Since `[3]_q` itself undershoots the A=3 strong target
   at the substrate `q₀` (`[3]_{q₀} ≈ 3.34 < 3.81`, a q₀-numeric fact in the
   probe), NO Demazure sub-crystal reaches A=3 — pure damping is monotone the
   WRONG way for the A=3 undershoot.

2. **The A=4 bracket, and that its lower end still escapes the cap.** The A=4
   target is bracketed between the drop-top truncation `[3]_q·[3]_q` and the full
   `[3]_q·[4]_q`; the endpoints are ordered (`[3]²_q ≤ [3]_q·[4]_q`), and the
   LOWER endpoint still exceeds the determinant cap `6 = C(4,2)`
   (`[3]²_q ≥ 9 > 6`).  So the tightening of #4012's window `{6, [3][4]}` to
   `{[3]², [3][4]}` is real and q-independent — the damped object stays above the
   cap the determinant provably cannot clear.

Base ring `ℝ` per §7c (ordering inequalities on `1 ≤ q`).  Nothing wired: this
proves the bracket and the obstruction; the probe is a scope-(a) honest negative
(the object does not LAND both targets).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.DemazureSubcrystal

/-- `[2]_q = 1 + q` — the `S_2/S_1` coset length-gen function (deuteron reference). -/
def q2 (q : ℝ) : ℝ := 1 + q

/-- `[3]_q = 1 + q + q²` — full `A=3` coset factor / `ρ_grad(3)`. -/
def q3 (q : ℝ) : ℝ := 1 + q + q ^ 2

/-- `[4]_q = 1 + q + q² + q³` — full `A=4` top-coset factor. -/
def q4 (q : ℝ) : ℝ := 1 + q + q ^ 2 + q ^ 3

/-- Full `A=3` coset factor is `≥ 3` for `q ≥ 1` (equality at the classical
`q = 1`, `3!/2! = 3`); the A=3 strong target `3.81` needs `q > 1`. -/
theorem q3_ge_three (q : ℝ) (hq : 1 ≤ q) : 3 ≤ q3 q := by
  have h0 : 0 ≤ q - 1 := by linarith
  have : q3 q - 3 = (q - 1) * (q + 2) := by unfold q3; ring
  nlinarith [mul_nonneg h0 (by linarith : (0 : ℝ) ≤ q + 2), this]

/-- **A=3 Demazure family is monotone in the truncation level: `1 ≤ [2]_q ≤ [3]_q`.**
The three A=3 truncations `{[1]_q, [2]_q, [3]_q} = {1, 1+q, 1+q+q²}` are ordered
for `q ≥ 1`, so the family MAXIMUM is the full ratio `[3]_q = ρ_grad(3)`.  A
Bruhat sub-sum cannot exceed the full sum — this is the A=3 obstruction: damping
only DECREASES `ρ(3)`, while the A=3 target sits ABOVE the full ratio. -/
theorem demazure_A3_family_le_full (q : ℝ) (hq : 1 ≤ q) :
    1 ≤ q2 q ∧ q2 q ≤ q3 q := by
  constructor
  · unfold q2; nlinarith
  · have : q3 q - q2 q = q ^ 2 := by unfold q2 q3; ring
    nlinarith [sq_nonneg q, this]

/-- Full A=4 top-coset factor dominates the drop-top truncation: `[3]_q ≤ [4]_q`
for `q ≥ 1` (indeed `q ≥ 0`), since `[4]_q − [3]_q = q³ ≥ 0`. -/
theorem q3_le_q4 (q : ℝ) (hq : 1 ≤ q) : q3 q ≤ q4 q := by
  have hq0 : 0 ≤ q := by linarith
  have : q4 q - q3 q = q ^ 3 := by unfold q3 q4; ring
  nlinarith [pow_nonneg hq0 3, this]

/-- **A=4 bracket ordering: drop-top `[3]²_q ≤ [3]_q·[4]_q` = full.**
The two endpoints of the A=4 Demazure bracket (keep 3 vs 4 reps of the A3→A4
coset, holding A2→A3 full) are ordered for `q ≥ 1`.  The strong target `13.03`
sits between them at the substrate `q₀` (`[3]²_{q₀} ≈ 11.17 < 13.03 < 15.74 ≈
[3][4]_{q₀}`, the q₀-numeric bracket in the probe). -/
theorem demazure_A4_droptop_le_full (q : ℝ) (hq : 1 ≤ q) :
    q3 q * q3 q ≤ q3 q * q4 q := by
  have hq3 : (0 : ℝ) ≤ q3 q := by nlinarith [q3_ge_three q hq]
  exact mul_le_mul_of_nonneg_left (q3_le_q4 q hq) hq3

/-- **The tightening is real and q-independent: the drop-top lower bracket still
escapes the determinant cap.** For `q ≥ 1`, `[3]²_q ≥ 9 > 6 = C(4,2)`.  So the
DAMPED Demazure A=4 object `[3]²_q` (lower bracket ≈ 11.17 at `q₀`) stays strictly
above the `SaturationRhoCap` ceiling `6` that the `−ln det` cumulant provably
cannot clear — #4012's window `{6, [3][4]}` tightens to `{[3]², [3][4]}` with both
ends above the cap. -/
theorem demazure_droptop_exceeds_det_cap (q : ℝ) (hq : 1 ≤ q) :
    (6 : ℝ) < q3 q * q3 q := by
  nlinarith [q3_ge_three q hq]

end QOU.MassTheory.DemazureSubcrystal
