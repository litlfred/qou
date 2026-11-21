import QOU.Information.SkeinHorizonLowerBound
import Mathlib.Data.Nat.Log

/-!
# QOU.Information.SkeinInfoLowerBound — the rigorous `info(n)` entropy floor

`SkeinHorizonLowerBound` discharged the *sequential-walk* cost: `treeSearch`
must visit all `3^c` leaves (`treeSearch_hcost`), an honest but naive
`O(3^c)`-step bound. This file supplies its **information-theoretic
complement** — the entropy floor: the *optimal-query* decision depth to
distinguish the horizon's `3^c` leaves is exactly

  `info(H) = log₃(numLeaves) = c`  trits,

and no ternary decision process can do better. Each step reveals at most one
trit, so `d` steps separate at most `3^d` outcomes; distinguishing `N`
outcomes therefore needs depth `≥ log₃ N`. Pure counting — no P-vs-NP content,
no conjecture: this is the rigorous lower bound the horizon's `3^c` leaf count
*forces*, unconditionally.

Contents (all sorry-free):

* `horizonInfo` — `info(H) := log₃(numLeaves)`.
* `horizonInfo_eq_filtrationLevel` — `info(H) = c` (exact).
* `numLeaves_eq_three_pow_info` — `numLeaves = 3^{info}` (info is exact, not
  a mere bound).
* `info_depth_lower_bound` — the entropy floor: `N ≤ 3^d ⇒ log₃ N ≤ d`.
* `horizon_depth_ge_info` — its horizon instantiation: covering the horizon's
  leaves needs depth `≥ info(H) = c`.
* `treeSearch_info` — the two ends of the query spectrum: `treeSearch d`
  carries exactly `d` trits (`log₃ 3^d = d`), the filtration level, while its
  sequential cost is `3^d` steps.

-- Ref: [leitner2026] information-theory/skein-turing-machine,
   information-theory/p-vs-np-boundary
-/

namespace QOU.Information

open SkeinObservationSystem

/-- **Information content of the computational horizon, in trits** — the base-3
    logarithm of the leaf count. Since the ternary resolution tree has
    `numLeaves = 3^c`, this is exactly the crossing count `c`: the number of
    independent ternary resolutions the observer must fix. -/
def horizonInfo (H : QOU.ComputationalHorizon) : ℕ := Nat.log 3 H.numLeaves

/-- `info(H) = c` — the trit-information equals the filtration level, exactly. -/
theorem horizonInfo_eq_filtrationLevel (H : QOU.ComputationalHorizon) :
    horizonInfo H = horizonFiltrationLevel H := by
  unfold horizonInfo horizonFiltrationLevel
  rw [H.numLeaves_eq, Nat.log_pow (by norm_num)]

/-- `numLeaves = 3^{info}` — the information count is exact, not merely a bound:
    the horizon has precisely `3^{info(H)}` leaves. -/
theorem numLeaves_eq_three_pow_info (H : QOU.ComputationalHorizon) :
    H.numLeaves = 3 ^ horizonInfo H := by
  rw [horizonInfo_eq_filtrationLevel]; exact H.numLeaves_eq

/-- **Entropy floor — the rigorous `info(n)` lower bound.** A ternary
    decision/branching process that must distinguish `N` outcomes at depth `d`
    — i.e. whose `3^d` reachable leaves cover them (`N ≤ 3^d`) — needs depth at
    least `log₃ N`. Each step reveals at most one trit, so `d` steps separate at
    most `3^d` outcomes. Pure counting; unconditional. -/
theorem info_depth_lower_bound {N d : ℕ} (h : N ≤ 3 ^ d) :
    Nat.log 3 N ≤ d :=
  calc Nat.log 3 N ≤ Nat.log 3 (3 ^ d) := Nat.log_mono_right h
    _ = d := Nat.log_pow (by norm_num) d

/-- **The horizon's decision-depth floor.** Any ternary decision process whose
    reachable leaves cover the horizon (`numLeaves ≤ 3^d`) has depth
    `≥ info(H) = c`. The information-theoretic complement of the sequential-walk
    step bound `treeSearch_hcost`: the *optimal-query* floor is `c` trits, while
    the *sequential-walk* cost is `3^c` leaf visits. -/
theorem horizon_depth_ge_info (H : QOU.ComputationalHorizon) {d : ℕ}
    (h : H.numLeaves ≤ 3 ^ d) : horizonInfo H ≤ d :=
  info_depth_lower_bound h

/-- The depth-`d` ternary search carries exactly `d` trits: its normal form
    `3^d` has `log₃ = d`, the filtration level. So `treeSearch d`'s sequential
    cost `3^d` (`treeSearch_hcost`) and its information depth `d` are the two
    ends of the query spectrum. -/
theorem treeSearch_info (d : ℕ) : Nat.log 3 (treeSearch d).normalForm = d :=
  Nat.log_pow (by norm_num) d

end QOU.Information
