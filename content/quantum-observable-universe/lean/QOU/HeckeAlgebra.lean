/-!
# QOU.HeckeAlgebra — umbrella module

Imports the Hecke-algebra-at-q₀ infrastructure for downstream
SDP-uniqueness consumers in `QOU.BraidKnot.*`. -/

import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.Hoefsmit
import QOU.HeckeAlgebra.Wedderburn
import QOU.HeckeAlgebra.MarkovTrace
import QOU.HeckeAlgebra.QSubstrate
import QOU.HeckeAlgebra.JonesMarkovWenzl
import QOU.HeckeAlgebra.Formal           -- pre-archimedean (ℤ[q, q⁻¹])
import QOU.HeckeAlgebra.Realification    -- archimedean wall crossing at q_0
