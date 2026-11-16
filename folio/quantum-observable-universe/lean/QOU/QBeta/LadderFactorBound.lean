/-
# The Q_β ladder's correction factor is bounded by 1 — for every phase

Beans `qou-cds1` (re-derive the `c_k` ladder under convention D) and `qou-pdix`
(derive the eigenphase `α`). Companion to
`computations/qbeta/qbeta_ladder_form_cannot_reach_ruled_base_probe.py` (7/7),
which supplies the numbers these lemmas make structural.

## What this settles

The ladder's correction factor is

    F(α) = cos(α − u/2) · (1 − u²) · ∏_{k≥3} (1 + c_k u^k)

and what it must supply is `F_required = Q_codata / Q_base`. On the base the
owner ruled on 2026-09-08 (`ε := tr_M` at `z_D`), `F_required` **exceeds 1** —
`1.75923699418` at the order-zero `E₀`, `1.20016236389` on the dashboard's
scored cell — where on the *retired* `z = 1` cell it was `0.998325241673`,
below 1.

`ladderN2_lt_of_one_le` says no phase reaches a required factor at or above 1,
and `ladder_lt_of_one_le` extends that through any further rungs whose product
lies in `(0, 1]`. `rung_lt_one` is why that hypothesis is met by this corpus's
ladder: every `c_k` it records or derives is negative (`c_2 = −1` structural,
`c_3 = −2.0693425771` recorded, `c_5 = −(b²+½)` derived), so every factor is
below 1.

**Consequence.** `qou-cds1`'s standing blocker — *"the blocker is still the N=1
phase (qou-pdix)"* — was written for the retired base and does not survive the
base change recorded in the same entry. Deriving `α` cannot unblock this ladder
on the ruled base, because **no** `α` does.

## Scope

These are statements about the ladder's *functional form*, nothing else. They
do **not** retire `α` (`qou-pdix` stays open on its own terms), do **not**
refute the ladder or the forced bar-odd projection `a_odd = a − h²/4` (C-frame,
sorry-free, untouched), and do **not** choose a base — per AGENTS.md §NO FITTING
a base is never selected by which obstruction it removes, so `F_required < 1` on
the retired cell is not a reason to prefer it.

The hypotheses are the honest ones: `P` is a *hypothesis*, not a claim about the
rungs, and the numeric fact that this corpus's rungs satisfy it is measured in
the probe rather than asserted here.

Verified `lean`-direct with `-DautoImplicit=false -s 65536`: exit 0, no
diagnostics, no `sorry`, no `axiom`. (A bare `lean` is a weaker check and the
exit code must not be read after a pipe — both traps are documented in
AGENTS.md and both were hit while producing this file.)
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.QBeta.LadderFactorBound

theorem ladderN2_le (u a : ℝ) (hu2 : u ^ 2 ≤ 1) :
    Real.cos (a - u / 2) * (1 - u ^ 2) ≤ 1 - u ^ 2 := by
  nlinarith [Real.cos_le_one (a - u / 2), Real.neg_one_le_cos (a - u / 2)]

theorem ladderN2_lt_of_one_le (u a F : ℝ) (hu : 0 < u) (hu2 : u ^ 2 < 1)
    (hF : 1 ≤ F) : Real.cos (a - u / 2) * (1 - u ^ 2) < F := by
  have h := ladderN2_le u a (le_of_lt hu2)
  nlinarith [pow_pos hu 2]

theorem rung_lt_one (u c : ℝ) (k : ℕ) (hu : 0 < u) (hc : c < 0) :
    1 + c * u ^ k < 1 := by
  have hp : 0 < u ^ k := pow_pos hu k
  nlinarith

theorem ladder_lt_of_one_le (u a F P : ℝ) (hu : 0 < u) (hu2 : u ^ 2 < 1)
    (hP0 : 0 < P) (hP1 : P ≤ 1) (hF : 1 ≤ F) :
    Real.cos (a - u / 2) * (1 - u ^ 2) * P < F := by
  have hu2p : (0:ℝ) < u ^ 2 := pow_pos hu 2
  have hq : (0:ℝ) < 1 - u ^ 2 := by linarith
  have hqP : (0:ℝ) < (1 - u ^ 2) * P := mul_pos hq hP0
  have step1 : Real.cos (a - u / 2) * ((1 - u ^ 2) * P) ≤ 1 * ((1 - u ^ 2) * P) :=
    mul_le_mul_of_nonneg_right (Real.cos_le_one _) (le_of_lt hqP)
  have step2 : (1 - u ^ 2) * P ≤ (1 - u ^ 2) * 1 :=
    mul_le_mul_of_nonneg_left hP1 (le_of_lt hq)
  have : Real.cos (a - u / 2) * (1 - u ^ 2) * P
      = Real.cos (a - u / 2) * ((1 - u ^ 2) * P) := by ring
  rw [this]
  linarith

/-! ## The `P` hypothesis, discharged for an arbitrary truncation order

`ladder_lt_of_one_le` takes `P ∈ (0, 1]` as a *hypothesis*, and `rung_lt_one`
shows this corpus's rungs are each below 1 — which left the join between the
two to be made numerically, per truncation order. #7276 asked whether the
product bound was formalized or discharged by measurement; it was the latter.
It is now the former.

`prod_pos_le_one` is the induction: a finite list of reals each in `(0, 1]` has
its product in `(0, 1]`. `ladder_lt_of_rungs` composes it with the cap, so the
exclusion holds at **every** truncation order with no numerical step at all —
the measured half of the argument is now only about *which* `c_k` the corpus
records, never about what their product does. -/

/-- A finite product of factors each in `(0, 1]` lies in `(0, 1]`. -/
theorem prod_pos_le_one (l : List ℝ) (h : ∀ x ∈ l, 0 < x ∧ x ≤ 1) :
    0 < l.prod ∧ l.prod ≤ 1 := by
  induction l with
  | nil => simp
  | cons a t ih =>
      have ha := h a (by simp)
      have ht : ∀ x ∈ t, 0 < x ∧ x ≤ 1 := fun x hx => h x (by simp [hx])
      obtain ⟨hp, hle⟩ := ih ht
      rw [List.prod_cons]
      exact ⟨mul_pos ha.1 hp, by nlinarith [ha.1, ha.2, hp, hle]⟩

/-- The ladder is below any requirement `≥ 1` at EVERY truncation order, given
only that each rung lies in `(0, 1]`. No per-order numerical discharge. -/
theorem ladder_lt_of_rungs (u a F : ℝ) (hu : 0 < u) (hu2 : u ^ 2 < 1) (hF : 1 ≤ F)
    (l : List ℝ) (hl : ∀ x ∈ l, 0 < x ∧ x ≤ 1) :
    Real.cos (a - u / 2) * (1 - u ^ 2) * l.prod < F := by
  obtain ⟨hP0, hP1⟩ := prod_pos_le_one l hl
  have hu2p : (0:ℝ) < u ^ 2 := pow_pos hu 2
  have hq : (0:ℝ) < 1 - u ^ 2 := by linarith
  have hqP : (0:ℝ) < (1 - u ^ 2) * l.prod := mul_pos hq hP0
  have s1 : Real.cos (a - u / 2) * ((1 - u ^ 2) * l.prod)
      ≤ 1 * ((1 - u ^ 2) * l.prod) :=
    mul_le_mul_of_nonneg_right (Real.cos_le_one _) (le_of_lt hqP)
  have s2 : (1 - u ^ 2) * l.prod ≤ (1 - u ^ 2) * 1 :=
    mul_le_mul_of_nonneg_left hP1 (le_of_lt hq)
  have e : Real.cos (a - u / 2) * (1 - u ^ 2) * l.prod
      = Real.cos (a - u / 2) * ((1 - u ^ 2) * l.prod) := by ring
  rw [e]; linarith

/-- **Quantitative deficit lower bound**: for any target `F` and rung list `l` with
entries in `(0, 1]`, the gap `F − cos(α − u/2)(1 − u²) ∏ l` is at least
`(F − 1) + u² · ∏ l`. -/
theorem ladder_deficit_ge_of_rungs (u a F : ℝ) (hu : 0 < u) (hu2 : u ^ 2 < 1)
    (l : List ℝ) (hl : ∀ x ∈ l, 0 < x ∧ x ≤ 1) :
    (F - 1) + u ^ 2 * l.prod ≤ F - Real.cos (a - u / 2) * (1 - u ^ 2) * l.prod := by
  obtain ⟨hP0, hP1⟩ := prod_pos_le_one l hl
  have hq : (0 : ℝ) < 1 - u ^ 2 := by linarith
  have hqP : (0 : ℝ) < (1 - u ^ 2) * l.prod := mul_pos hq hP0
  have s1 : Real.cos (a - u / 2) * ((1 - u ^ 2) * l.prod)
      ≤ 1 * ((1 - u ^ 2) * l.prod) :=
    mul_le_mul_of_nonneg_right (Real.cos_le_one _) (le_of_lt hqP)
  have e : Real.cos (a - u / 2) * (1 - u ^ 2) * l.prod
      = Real.cos (a - u / 2) * ((1 - u ^ 2) * l.prod) := by ring
  rw [e]
  linarith

/-- **Rung membership in `(0, 1]`**: any negative coefficient `c < 0` with
`-1 < c · u^k` places the rung `1 + c · u^k` in `(0, 1]`. -/
theorem rung_mem_unit_interval (u c : ℝ) (k : ℕ) (hu : 0 < u) (hc : c < 0)
    (hlow : -1 < c * u ^ k) :
    0 < 1 + c * u ^ k ∧ 1 + c * u ^ k ≤ 1 := by
  have hlt := rung_lt_one u c k hu hc
  exact ⟨by linarith, le_of_lt hlt⟩

end QOU.QBeta.LadderFactorBound
