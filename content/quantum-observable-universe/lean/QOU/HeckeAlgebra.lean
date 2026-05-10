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
-- Per Copilot review: `QOU.HeckeAlgebra.Realification` is kept
-- OUT of this umbrella while it still has `sorry` placeholders
-- (specifically `realifyAtRealQ0`, pending Mathlib
-- `LaurentPolynomial.evalRingHom` API verification).  Downstream
-- code that needs it can import it directly:
--   `import QOU.HeckeAlgebra.Realification`
-- This keeps the umbrella's baseline dependency surface stable.
