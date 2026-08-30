import QOU.MathlibExt.QPlancherel

/-!
# `HasQPlancherelCLT` was uninhabitable; the fixed shape is inhabited

Run:  `LEAN_PATH=<mathlib + QOU oleans> lean <this file>`  ->  exit 0.

Found by `scripts/limit-claim-encoding-audit.py`, which flagged the field
for a *different* reason (a docstring promising a limit).  That triage
called it a false positive, correctly for the limit question and blindly
for this one: the bound was not merely unlocalised, it was false.

The defect shape was named by a sibling branch on PR #6041 -- *an
external theorem asserted for every inhabitant of a structure that does
not carry the theorem's hypotheses*.  [feray2010] Theorem 1.1 is about
the q-Plancherel branching fractions; the old field asserted it for
every real sequence and every real limit, against a constant `Cq` the
instance had already fixed.
-/

namespace QOU.Audits.QPlancherelProbe

open QOU.MathlibExt.QPlancherel

/-- **The old shape refuted.**  Verbatim the pre-2026-08-29 field, with
    `Cq` fixed first, as an instance would fix it.  No inhabitant exists. -/
theorem old_bound_shape_is_refutable :
    ¬ ∃ Cq : ℝ, 0 < Cq ∧
        ∀ (f : ℕ → ℝ) (f_inf : ℝ) (k : ℕ), k ≥ 4 →
          |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ) := by
  rintro ⟨Cq, hpos, hb⟩
  have h := hb (fun _ => (0 : ℝ)) (Cq + 1) 4 (by norm_num)
  have hs : Real.sqrt (((4 : ℕ) : ℝ) - 3) = 1 := by norm_num
  rw [hs, div_one] at h
  rw [abs_of_nonpos (by simp; linarith)] at h
  simp at h
  linarith

/-- **The fixed shape is inhabited**, so the repair is not merely a
    weakening that trades one unusable class for another: a constant
    sequence at its own limit satisfies it for any `Cq > 0`. -/
example : ∃ (Cq : ℝ) (f : ℕ → ℝ) (f_inf : ℝ), 0 < Cq ∧
    ∀ k : ℕ, k ≥ 4 → |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ) := by
  refine ⟨1, fun _ => 0, 0, one_pos, fun k _ => ?_⟩
  simp only [sub_self, abs_zero]
  exact div_nonneg zero_le_one (Real.sqrt_nonneg _)

end QOU.Audits.QPlancherelProbe
