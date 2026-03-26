/-!
# QOU.Torsion.CategoricalProton — Proton as color-linked quark triple

The categorical proton is 𝔭 = [u, u, d]_c ⋈ L_H where u = T_{2,3}
(trefoil) and d = σ(T_{2,3}) (three-twist, Skein descendant).

LaTeX label: `def:categorical-proton`

## References
- [manuscript] §3/categorical-proton
-/

import Mathlib.Data.Real.Basic

namespace QOU.Torsion

/-- The categorical proton: color-linked triple [u, u, d]_c ⋈ L_H.
    Mass = S_uu + 2·S_ud ≈ 938.272 MeV. -/
-- Ref: [manuscript] §3/categorical-proton
structure CategoricalProton where
  /-- Pair Skein mass S_uu. -/
  skein_uu : ℝ
  /-- Pair Skein mass S_ud. -/
  skein_ud : ℝ
  /-- Mass = S_uu + 2·S_ud. -/
  mass : ℝ := skein_uu + 2 * skein_ud
  /-- Positive crossing chirality (electric charge = +1). -/
  chirality : ℤ := 1

end QOU.Torsion
