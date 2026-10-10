import QOU.SchurWeyl.SeminormalParam
import QOU.SchurWeyl.HoefsmitRep

/-!
# QOU.SchurWeyl.SeminormalParamAnchorReal — the `S1` anchor, at `ℝ`

Split out of `QOU/SchurWeyl/SeminormalParam.lean` (bean `qou-j377`).

That file's five other results are now generic over `[Field K]`.  This one cannot be: it
identifies the hand-built `(2,1)` matrix `S1` from `HoefsmitRep.lean`, which is `ℝ`-valued,
with `seminormalBlock` at the predicted parameter — and its proof of `1 - q ^ 4 ≠ 0` runs
through `positivity` on `q ^ 2 + 1`, an order step.  §7c therefore puts it in its own file.

**It is off the general-field path**, which is why generalising it is not on the critical
list: `scripts/lean-general-field-tranche-scope.py` reports `HoefsmitRep`'s twelve
`ℝ`-carrying declarations as unreachable from `heckeWedderburn`, reaching the chain only
through `QJucysMurphy.qJM_seminormalRep21_one`, a rank-2 sanity check with zero consumers.
The anchor is a genuine cross-check of the axial-distance formula against a hand-built
matrix and is kept as such; it is simply not load-bearing for the Wedderburn theorem.

Were it wanted over a general field, the order step is not the obstacle it looks like:
`GenericParameter.sq_add_one_ne_zero` supplies `q ^ 2 + 1 ≠ 0` from `NotRootOfUnity`, and
under that hypothesis the `1 - q ^ 4 ≠ 0` case split disappears rather than being replaced.
-/

namespace QOU.SchurWeyl

open Hecke Matrix

namespace Seminormal

variable (q : ℝ)

/-- **Anchor.**  The hand-built `(2,1)` matrix `S1` — constructed in `HoefsmitRep.lean` to
satisfy the braid relation with `S0`, independently of any axial-distance formula — is the
generic block at the parameter this file predicts.  In `[[1,2],[3]]` the entry `2` has
content `1` and `3` has content `-1`, so `σ_1` acts with axial distance `-2`.

The hypothesis `q² ≠ 1` is necessary, not cosmetic: at `q = ±1` the numerator `q - q⁻¹`
and the denominator `1 - q⁴` both vanish, so `seminormalParam q (-2)` evaluates to `0`
(Lean's `0 / 0`), while `S1`'s `(0,0)` entry is `-1 / (2q) ≠ 0`.  That is the Hecke
algebra degenerating to the group algebra, where the seminormal form is not given by this
formula. -/
theorem S1_eq_seminormalParam (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    S1 q = seminormalBlock q (seminormalParam q (-2)) := by
  have h4 : (1 : ℝ) - q ^ (-2 * (-2 : ℤ)) = 1 - q ^ 4 := by
    norm_num [← zpow_natCast]
  have hne4 : (1 : ℝ) - q ^ 4 ≠ 0 := by
    intro hcon
    apply hq2
    have h2 : (q ^ 2 - 1) * (q ^ 2 + 1) = 0 := by nlinarith [hcon]
    rcases mul_eq_zero.mp h2 with h | h
    · linarith
    · nlinarith [sq_nonneg q]
  have hden : q ^ 3 + q ≠ 0 := by
    have hfac : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [hfac]
    exact mul_ne_zero hq (by positivity)
  have hparam : seminormalParam q (-2) = -1 / (q ^ 3 + q) := by
    rw [seminormalParam, h4]
    field_simp
    ring
  rw [hparam]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [S1, seminormalBlock]; try field_simp; try ring)

end Seminormal

end QOU.SchurWeyl
