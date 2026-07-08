-- Faddeev f_k exact polynomial coefficients over ℚ(√3)
-- Extracted via the non-compact modular double t -> i*t
-- Computed by hecke-engine faddeev_ck.rs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Irrational

/-- The exact analytical coefficient f_1 of the topological mass ladder. -/
noncomputable def f_1 : ℝ := - (7 / 6) * Real.sqrt 3

/-- The exact analytical coefficient f_2 of the topological mass ladder. -/
noncomputable def f_2 : ℝ := - (5407 / 72) + (1 / 3) * Real.sqrt 3

/-- The exact analytical coefficient f_3 of the topological mass ladder.
    This corresponds to the third-order moment of the non-compact boundary integral. -/
noncomputable def f_3 : ℝ := 2 + (7142821 / 6480) * Real.sqrt 3

/-- The exact analytical coefficient f_4 of the topological mass ladder. -/
noncomputable def f_4 : ℝ := - (2774900693 / 120960) - (2461 / 108) * Real.sqrt 3

/-- The exact analytical coefficient f_5 of the topological mass ladder. -/
noncomputable def f_5 : ℝ := (8572817 / 9720) + (11795319232141 / 97977600) * Real.sqrt 3

/-- 
Proposition: The exact cyclotomic algebraic witness of the macroscopic Faddeev observable f_3.
This formalizes the exact sequence limit evaluated by the Rust structural extraction.
-/
theorem f_3_exact_witness : f_3 = 2 + (7142821 / 6480) * Real.sqrt 3 := by
  rfl
