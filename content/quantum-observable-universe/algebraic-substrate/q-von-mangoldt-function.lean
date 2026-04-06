/-!
# QOU.AlgebraicSubstrate.QVonMangoldtFunction

The q-von Mangoldt function over maximal ideals of the coordinate ring.
LaTeX: `\label{def:q-von-mangoldt-function}`
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- A maximal ideal of the coordinate ring, carrying a norm (residue field
    cardinality) and a predicate marking fundamental defects. -/
structure MaxIdeal where
  /-- The norm N(𝔪) — cardinality of the residue field. -/
  norm : ℝ
  norm_pos : 0 < norm
  /-- Whether this ideal corresponds to a fundamental defect. -/
  isFundamental : Prop

/-- The q-von Mangoldt function.

    For a fundamental defect with norm N(𝔪), returns
    (N(𝔪)^ℏ_q - 1) / ℏ_q where ℏ_q = (q-1)/q is the quantum
    Planck constant. Returns 0 for non-fundamental ideals. -/
noncomputable def QVonMangoldtFunction (hbar_q : ℝ) (hbar_pos : 0 < hbar_q)
    (m : MaxIdeal) : ℝ :=
  if m.isFundamental then
    (m.norm ^ hbar_q - 1) / hbar_q
  else
    0

end QOU.AlgebraicSubstrate
