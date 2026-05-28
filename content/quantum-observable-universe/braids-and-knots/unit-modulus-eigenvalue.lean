/-!
# `prop:unit-modulus-eigenvalue` — §3b-cond conditional formalization

This content sibling records the §3b-cond conditional-class structure
for `prop:unit-modulus-eigenvalue`. Its `uses[]` cone reaches
`conj:meson-volume-conjecture`, whose content is axiomatised by the
class `MesonDualVolume` (see `meson-volume-conjecture.lean`).

The compiled proof of the eigenvalue statement itself lives in the
`QOU` Lake library at
`QOU.BraidsAndKnots.borromean_eigenvalue_neg_one`
(`lean/QOU/BraidsAndKnots/UnitModulusEigenvalue.lean`). This sibling
only carries the conditional-class marker; it is not part of the
compiled library (`srcDir = lean/`).
-/

namespace QOU.BraidsAndKnots

/-- Marker for the meson dual-volume class hypothesis. The full
    `MesonDualVolume` class lives in `meson-volume-conjecture.lean`. -/
section ConditionalOn_MesonDualVolume
variable (q_vc : ℝ) [MesonDualVolume q_vc]
-- §3b-cond: `prop:unit-modulus-eigenvalue` is conditional on
-- `conj:meson-volume-conjecture` via the class `MesonDualVolume`.
end ConditionalOn_MesonDualVolume

end QOU.BraidsAndKnots
