/-!
# QOU.QHeckeEigensheaf

q-Hecke eigensheaf: eigenvalue under q-Hecke operators, with
tensor compatibility and factorisation.

Co-located sibling for content block `def:q-hecke-eigensheaf`.
Full formalization: `QOU/QGeometricLanglands.lean`
-/

import QOU.QGeometricLanglands

-- Re-export: QOU.QGeometricLanglands.QHeckeEigensheaf

namespace QOU

/-- **def:q-hecke-eigensheaf** — placeholder stub; full definition TBD. -/
structure QHeckeEigensheaf where
  witness : ℝ
  witness_pos : 0 < witness
end QOU
