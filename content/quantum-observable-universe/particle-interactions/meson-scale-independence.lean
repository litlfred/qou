/-!
# `prop:meson-scale-independence` — §3b-cond conditional formalization

This content sibling records the §3b-cond conditional-class structure
for `prop:meson-scale-independence`. Its `uses[]` cone reaches
`conj:meson-volume-conjecture`, whose content is axiomatised by the
class `MesonDualVolume` (see `meson-volume-conjecture.lean`). The
proposition is conditional on that class; the meson scale `m_π` is
fixed by the Hopf-link dual-volume datum, independent of
`(m_e, q_0)`.

This file is a narrative formalization stub — it is not part of the
compiled `QOU` Lake library (`srcDir = lean/`).
-/

namespace QOU.ParticleInteractions

/-- Marker for the meson dual-volume class hypothesis. The full
    `MesonDualVolume` class lives in `meson-volume-conjecture.lean`
    (namespace `QOU.ParticleInteractions`). -/
section ConditionalOn_MesonDualVolume
variable (q_vc : ℝ) [MesonDualVolume q_vc]
-- §3b-cond: `prop:meson-scale-independence` is conditional on
-- `conj:meson-volume-conjecture` via the class `MesonDualVolume`.
end ConditionalOn_MesonDualVolume

end QOU.ParticleInteractions
