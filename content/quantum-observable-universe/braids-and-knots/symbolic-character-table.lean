/-
  Symbolic character table for all partitions H₂-H₇.
  Ref: [manuscript] §5.5, prop:symbolic-character-table
-/
namespace QOU.BraidKnot
/-- Character of the self-conjugate partition [3,1,1]. -/
noncomputable def chi_311 (q : ℝ) : ℝ := 3 * (q - 1/q)
/-- Character of [3,2,1] (H₆ dominant). -/
noncomputable def chi_321 (q : ℝ) : ℝ := 8 * (q - 1/q)
end QOU.BraidKnot
