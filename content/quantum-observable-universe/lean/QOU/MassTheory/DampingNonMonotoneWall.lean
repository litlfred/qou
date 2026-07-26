/-
# The A-dependent DAMPING route is walled: the required correction is NON-monotone in A

`QOU.MassTheory.JetFiltrationTwoAnchorNoGo` (#4300) proved the single-knob
`q`-scaled coinvariant graded dimension `[A]_q!` cannot land both light-nucleus
anchors, and read §4 of the jet-filtration audit as calling for a **damped**
graded dimension (grow slower than `[A]_q!`).  Both routes the follow-up proposed
are *dampings* — a factor `D(A) ≤ 1` applied to `ρ_grad(A) = [A]_q!/[2]_q!`:

* route (a) an A-locked **parabolic/skew quotient** of `[A]_q!` (a quotient of a
  positively-graded coinvariant algebra has graded dimension `≤` the full one);
* route (b) a **Demazure sub-crystal** (a Bruhat-prefix *sub-sum* of `[A]_q!`,
  `≤` the full sum — already `demazure_A3_family_le_full` in
  `DemazureSubcrystalGradedDim.lean`).

This file proves, sorry-free, that **no damping `D(A) ≤ 1` can close the A=3
anchor at the fixed canonical substrate** — extending the Demazure-only A=3
obstruction to the *entire* pure-damping class — and that at the SAME substrate
window the A=4 ratio *over*shoots.  Hence the residual
`ρ_strong(A) − ρ_grad(A)` **changes sign** between A=3 (`> 0`, graded undershoots)
and A=4 (`< 0`, graded overshoots), so the correction the data requires is
**not sign-definite in A** — it cannot be a multiplicative damping (which only ever
*subtracts*).  This is a scope-(b) structural exclusion of the damping class, with
the cited invariant being the monotone-`≤ 1` action of a damping together with the
q₀-window undershoot at A=3.

## The two proved facts (canonical-substrate window `q ∈ [1.109, 1.11]`)

* **(U) A=3 undershoot / damping wall.** For `1 ≤ q ≤ 111/100` and any damping
  `0 ≤ d ≤ 1`, `d · [3]_q < ρ_strong(3) = 3.8128` (indeed `[3]_{1.11} = 3.3421`).
  A damping only *decreases* `[3]_q`, which already undershoots — so **no** damping
  reaches the A=3 target.  This is the reason route (a) and route (b) both fail.
* **(O) A=4 overshoot.** For `1109/1000 ≤ q ≤ 111/100`,
  `[3]_q·[4]_q > ρ_strong(4) = 13.0316` (indeed `[3][4]_{1.109} = 15.702`).
  At the substrate the A=4 ratio *over*shoots — the direction a damping *would*
  correctly help, in the opposite sign to A=3.

Together (U) + (O): the required correction is `+` at A=3 and `−` at A=4.  A
damping supplies `≤ 0` at both — it structurally cannot produce a sign change.

## Anchor robustness

The conclusion does not depend on the isospin/Coulomb correction: the undershoot
(U) needs only `ρ_strong(3) > [3]_{1.11} = 3.3421`, true for the *raw* AME ratio
`B(³H)/B(²H) = 3.814` as well as the corrected `3.8128`; the overshoot (O) needs
only `ρ_strong(4) < [3][4]_{1.109} = 15.702`, true for the raw
`B(⁴He)/B(²H) = 12.72` as well as the corrected `13.0316`.  The sign change is
therefore robust to the exact anchor values (used only as one-sided bounds).

**Anti-fit (STRICT).** `ρ_strong(3) = 3.8128`, `ρ_strong(4) = 13.0316` are
DERIVED-ELSEWHERE comparison constants (#3986/#3990 isospin/Coulomb-corrected AME)
and appear ONLY as bounds.  No `q` and no `d` are solved from them; nothing is
wired.  Base ring `ℝ` per §7c (ordering inequalities on `1 ≤ q`).

Companion probe: `computations/deltalambda/deltalambda_damping_nonmonotone_wall_probe.py`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-- `ρ_grad(3) = W_3/W_2 = [3]_q = 1 + q + q²`. -/
def dampGradRatio3 (q : ℝ) : ℝ := 1 + q + q ^ 2

/-- `[4]_q = 1 + q + q² + q³`, the A=3→A=4 graded step (`ρ_grad(4) = [3]_q·[4]_q`). -/
def dampGradStep4 (q : ℝ) : ℝ := 1 + q + q ^ 2 + q ^ 3

/-- `[3]_q` is monotone increasing on `[1,∞)` (used for the substrate upper bound). -/
theorem dampGradRatio3_mono {a b : ℝ} (ha : 1 ≤ a) (hab : a ≤ b) :
    dampGradRatio3 a ≤ dampGradRatio3 b := by
  unfold dampGradRatio3
  nlinarith [sq_nonneg (b - a), mul_nonneg (by linarith : (0:ℝ) ≤ a) (by linarith : (0:ℝ) ≤ b - a)]

/-- `[3]_q ≥ 0` on `q ≥ 1`. -/
theorem dampGradRatio3_nonneg (q : ℝ) (hq : 1 ≤ q) : 0 ≤ dampGradRatio3 q := by
  unfold dampGradRatio3; positivity

/-- **(U) A=3 undershoot / damping wall.** For the canonical substrate window
`1 ≤ q ≤ 1.11` and ANY damping factor `0 ≤ d ≤ 1`, the damped A=3 ratio stays
strictly below the A=3 strong target: `d · [3]_q < 3.8128`.

`[3]_q ≤ [3]_{1.11} = 3.3421 < 3.8128` (monotonicity + the substrate upper bound),
and a damping only decreases it (`d · [3]_q ≤ [3]_q` since `d ≤ 1`, `[3]_q ≥ 0`).
Hence NO damping `D(A) ≤ 1` — parabolic/skew quotient (route a) or Demazure
sub-crystal (route b) alike — reaches the A=3 anchor at the physical substrate. -/
theorem damping_cannot_close_A3 (q : ℝ) (hq : 1 ≤ q) (hq' : q ≤ 111 / 100)
    (d : ℝ) (hd0 : 0 ≤ d) (hd1 : d ≤ 1) :
    d * dampGradRatio3 q < 3.8128 := by
  have hmono : dampGradRatio3 q ≤ dampGradRatio3 (111 / 100) :=
    dampGradRatio3_mono hq hq'
  have hval : dampGradRatio3 (111 / 100) < 3.8128 := by unfold dampGradRatio3; norm_num
  have hpos : 0 ≤ dampGradRatio3 q := dampGradRatio3_nonneg q hq
  -- d · [3]_q ≤ 1 · [3]_q = [3]_q ≤ [3]_{1.11} < 3.8128
  have hdamp : d * dampGradRatio3 q ≤ dampGradRatio3 q := by
    nlinarith [mul_le_mul_of_nonneg_right hd1 hpos]
  linarith

/-- **(O) A=4 overshoot.** For the canonical substrate window
`1.109 ≤ q ≤ 1.11`, the (undamped) A=4 graded ratio strictly *exceeds* the A=4
strong target: `[3]_q·[4]_q > 13.0316` (`[3][4]_{1.109} = 15.702`).  At the same
substrate where A=3 undershoots, A=4 overshoots — the correction the data wants is
`+` at A=3 but `−` at A=4. -/
theorem substrate_A4_overshoots (q : ℝ) (hlo : 1109 / 1000 ≤ q) (hhi : q ≤ 111 / 100) :
    (13.0316 : ℝ) < dampGradRatio3 q * dampGradStep4 q := by
  unfold dampGradRatio3 dampGradStep4
  have hq0 : (0 : ℝ) ≤ q := by linarith
  -- q ≥ 1.109 ⇒ q² ≥ 1.109², q³ ≥ 1.109³, hence each factor is bounded below by its
  -- value at the substrate lower endpoint (all quantities non-negative).
  have hsq : (1109 / 1000 : ℝ) ^ 2 ≤ q ^ 2 := by nlinarith [hlo, hq0]
  have hcube : (1109 / 1000 : ℝ) ^ 3 ≤ q ^ 3 := by nlinarith [hlo, hsq, hq0]
  have h3 : (1 : ℝ) + 1109 / 1000 + (1109 / 1000) ^ 2 ≤ 1 + q + q ^ 2 := by linarith
  have h4 : (1 : ℝ) + 1109 / 1000 + (1109 / 1000) ^ 2 + (1109 / 1000) ^ 3
      ≤ 1 + q + q ^ 2 + q ^ 3 := by linarith
  have hp3 : (0 : ℝ) ≤ 1 + 1109 / 1000 + (1109 / 1000) ^ 2 := by norm_num
  have hp4 : (0 : ℝ) ≤ 1 + 1109 / 1000 + (1109 / 1000) ^ 2 + (1109 / 1000) ^ 3 := by norm_num
  have hprod : ((1 : ℝ) + 1109 / 1000 + (1109 / 1000) ^ 2)
        * (1 + 1109 / 1000 + (1109 / 1000) ^ 2 + (1109 / 1000) ^ 3)
      ≤ (1 + q + q ^ 2) * (1 + q + q ^ 2 + q ^ 3) :=
    mul_le_mul h3 h4 hp4 (by linarith)
  have hval : (13.0316 : ℝ) < ((1 : ℝ) + 1109 / 1000 + (1109 / 1000) ^ 2)
        * (1 + 1109 / 1000 + (1109 / 1000) ^ 2 + (1109 / 1000) ^ 3) := by norm_num
  linarith

/-- **The damping route is walled — the required correction is non-monotone in A.**
On the canonical substrate window `[1.109, 1.11]`, the graded dimension undershoots
A=3 (so a damping, which only subtracts, cannot close it — `damping_cannot_close_A3`)
yet overshoots A=4 (`substrate_A4_overshoots`).  The residual therefore changes
sign between A=3 (`+`) and A=4 (`−`); a multiplicative damping `D(A) ≤ 1` supplies a
non-positive correction at every A and cannot realise a sign change.

The statement packages the two directions as one certificate: at any substrate
`q` in the window there is a damped-below A=3 value and an over-target A=4 value,
so `damped A=3 < target(3)` while `target(4) < undamped A=4`. -/
theorem damping_route_walled (q : ℝ) (hlo : 1109 / 1000 ≤ q) (hhi : q ≤ 111 / 100)
    (d : ℝ) (hd0 : 0 ≤ d) (hd1 : d ≤ 1) :
    d * dampGradRatio3 q < 3.8128 ∧
      (13.0316 : ℝ) < dampGradRatio3 q * dampGradStep4 q := by
  have hq : (1 : ℝ) ≤ q := by linarith
  exact ⟨damping_cannot_close_A3 q hq hhi d hd0 hd1, substrate_A4_overshoots q hlo hhi⟩

end QOU.MassTheory
