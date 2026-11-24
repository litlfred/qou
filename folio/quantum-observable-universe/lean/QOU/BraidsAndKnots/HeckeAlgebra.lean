import HeckeTemperleyLieb.Common
import HeckeTemperleyLieb.HeckeAlgebra.Hoefsmit
import HeckeTemperleyLieb.Wedderburn
import QOU.BraidsAndKnots.MarkovTrace
import QOU.BraidsAndKnots.QSubstrate
import QOU.BraidsAndKnots.JonesMarkovWenzl
import QOU.BraidsAndKnots.Formal           -- pre-archimedean (ℤ[q, q⁻¹])
import QOU.BraidsAndKnots.Realification    -- archimedean wall crossing at q_0
import QOU.BraidsAndKnots.Demazure

/-!
# QOU.HeckeAlgebra — umbrella module

Imports the Hecke-algebra-at-q₀ infrastructure for downstream
SDP-uniqueness consumers in `QOU.BraidKnot.*`. -/
