/-!
# Compatibility re-export for YekutielijTriple (typo variant)

This file provides backward-compatible aliases for the typo spelling
"Yekutielij". The canonical definitions live in `YekutieliTriple.lean`.
-/

import QOU.Torsion.YekutieliTriple

namespace QOU.Torsion

/-- Backward-compatible alias for `YekutieliTriple`. -/
abbrev YekutielijTriple := YekutieliTriple

/-- Backward-compatible alias for `YekutieliLiftingCondition`. -/
abbrev YekutielijLiftingCondition := YekutieliLiftingCondition

end QOU.Torsion
