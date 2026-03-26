/-!
# QOU.HadronicMass.terminal_resolution_hadronic_mass

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/HadronicMass.lean (monolithic)
-/

import QOU.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic

namespace QOU.HadronicMass

/-- **Proposition (Terminal Resolution of Hadronic Mass).**
    Using the derived substrate parameter `q = 1.1097`, all four rows
    of the hadronic mass table match NIST CODATA 2022 values:
    1. Proton:  `|m_p^{QOU} − 938.27208943| < 0.001`
    2. Neutron: `|m_n^{QOU} − 939.56542194| < 0.001`
    3. Deuteron: `|m_D^{QOU} − 1875.61294500| < 0.001`
    4. Binding: `|ΔE^{QOU} − 2.22456637| < 0.001`

    LaTeX: `\label{prop:terminal-resolution}` -/
theorem terminal_resolution_hadronic_mass :
    |proton_topological - proton_mass_MeV| < 1e-3 ∧
    |neutron_topological - neutron_mass_MeV| < 1e-3 ∧
    |deuteron_topological - deuteron_mass_MeV| < 1e-3 ∧
    |binding_energy_QOU - binding_energy_CODATA| < 0.001 :=
  ⟨row1_proton_matches_CODATA,
   row2_neutron_matches_CODATA,
   row3_deuteron_matches_CODATA,
   row4_binding_CODATA_comparison⟩

end QOU.HadronicMass
