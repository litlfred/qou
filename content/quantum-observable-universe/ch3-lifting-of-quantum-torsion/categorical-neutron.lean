/-!
# QOU.Torsion.CategoricalNeutron — Neutron as color-linked quark triple

The categorical neutron is 𝔫 = [u, d, d]_c ⋈ L_H.

LaTeX label: `def:categorical-neutron`

## References
- [manuscript] §3/categorical-neutron
-/

import Mathlib.Data.Real.Basic

namespace QOU.Torsion

/-- The categorical neutron: color-linked triple [u, d, d]_c ⋈ L_H.
    Mass = 2·S_ud + S_dd ≈ 939.565 MeV. -/
-- Ref: [manuscript] §3/categorical-neutron
structure CategoricalNeutron where
  /-- Pair Skein mass S_ud. -/
  skein_ud : ℝ
  /-- Pair Skein mass S_dd. -/
  skein_dd : ℝ
  /-- Mass = 2·S_ud + S_dd. -/
  mass : ℝ := 2 * skein_ud + skein_dd
  /-- Zero crossing chirality (electric charge = 0). -/
  chirality : ℤ := 0

end QOU.Torsion
