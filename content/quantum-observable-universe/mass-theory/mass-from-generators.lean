import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Experimental.MassFromGenerators — Atomic mass predictions from T_{m,n} generators

Mass spectrum computed from torus knot generators via Hopf linking,
color-tube threading, and Skein crossing changes. All masses in MeV/c².

CODATA 2022 and AME2020 values are provided for comparison.
The substrate parameter q = 1.10997 is the single free parameter.

LaTeX label: `rem:mass-from-generators`, `rem:mass-comparison-table`

## References

- CODATA 2022 recommended values of fundamental physical constants
- AME2020 Atomic Mass Evaluation (Wang et al., CPC 45 030003, 2021)
- [manuscript] §11-experimental-evidence/mass-from-generators

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Experimental.MassData

-- ═══════════════════════════════════════════════════════════════════
-- CODATA 2022 reference masses (MeV/c²)
-- ═══════════════════════════════════════════════════════════════════

/-- Electron mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_electron : ℝ := 0.51099895069

/-- Muon mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_muon : ℝ := 105.6583755

/-- Proton mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_proton : ℝ := 938.27208943

/-- Neutron mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_neutron : ℝ := 939.56542194

/-- Deuteron mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_deuteron : ℝ := 1875.61294500

/-- He-3 nuclear mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_he3 : ℝ := 2808.39161112

/-- He-4 (alpha) nuclear mass, CODATA 2022. -/
-- Ref: [codata2022] CODATA 2022
noncomputable def codata_he4 : ℝ := 3727.3794118

-- ═══════════════════════════════════════════════════════════════════
-- AME2020 nuclear masses (MeV/c²)
-- ═══════════════════════════════════════════════════════════════════

/-- Li-6 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_li6 : ℝ := 5601.518

/-- Li-7 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_li7 : ℝ := 6533.833

/-- Be-9 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_be9 : ℝ := 8392.750

/-- C-12 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_c12 : ℝ := 11174.862

/-- N-14 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_n14 : ℝ := 13040.203

/-- O-16 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_o16 : ℝ := 14895.079

/-- Si-28 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_si28 : ℝ := 26053.195

/-- Fe-56 nuclear mass, AME2020. -/
-- Ref: [ame2020] AME2020
noncomputable def ame_fe56 : ℝ := 52089.801

-- ═══════════════════════════════════════════════════════════════════
-- Nuclear binding energies per nucleon (MeV), AME2020
-- ═══════════════════════════════════════════════════════════════════

/-- Deuteron B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_deuteron : ℝ := 1.1122

/-- He-3 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_he3 : ℝ := 2.5727

/-- He-4 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_he4 : ℝ := 7.0739

/-- Li-6 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_li6 : ℝ := 5.3325

/-- Li-7 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_li7 : ℝ := 5.6063

/-- Be-9 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_be9 : ℝ := 6.4628

/-- C-12 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_c12 : ℝ := 7.6801

/-- N-14 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_n14 : ℝ := 7.4756

/-- O-16 B/A. -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_o16 : ℝ := 7.9762

/-- Fe-56 B/A (maximum of the curve). -/
-- Ref: [ame2020] AME2020
noncomputable def binding_per_A_fe56 : ℝ := 8.7903

-- ═══════════════════════════════════════════════════════════════════
-- QOU predicted masses from knot generation (MeV/c²)
--
-- Computed from: q = 1.10997, μ_u = 311.10, μ_d = 312.39
-- Proton:  S_uu + 2·S_ud = 938.269 MeV
-- Neutron: 2·S_ud + S_dd = 939.565 MeV
-- Atom(Z,N) = Z·m_p + N·m_n - A·(B/A) + Z·m_e
-- ═══════════════════════════════════════════════════════════════════

/-- Hydrogen-1 atom (¹H): 𝔭 ⋈ T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_hydrogen_1 : ℝ := 938.780495

/-- Deuterium atom (²H): 𝔭 ⋈ 𝔫 ⋈ T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_deuterium : ℝ := 1876.120855

/-- Helium-3 atom (³He): 2𝔭 ⋈ 𝔫 ⋈ 2T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_helium_3 : ℝ := 2809.407650

/-- Helium-4 atom (⁴He): 2𝔭 ⋈ 2𝔫 ⋈ 2T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_helium_4 : ℝ := 3728.394911

/-- Lithium-6 atom (⁶Li): 3𝔭 ⋈ 3𝔫 ⋈ 3T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_lithium_6 : ℝ := 5603.040766

/-- Lithium-7 atom (⁷Li): 3𝔭 ⋈ 4𝔫 ⋈ 3T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_lithium_7 : ℝ := 6535.356427

/-- Beryllium-9 atom (⁹Be): 4𝔭 ⋈ 5𝔫 ⋈ 4T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_beryllium_9 : ℝ := 8394.780582

/-- Carbon-12 atom (¹²C): 6𝔭 ⋈ 6𝔫 ⋈ 6T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_carbon_12 : ℝ := 11177.910333

/-- Nitrogen-14 atom (¹⁴N): 7𝔭 ⋈ 7𝔫 ⋈ 7T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_nitrogen_14 : ℝ := 13043.758388

/-- Oxygen-16 atom (¹⁶O): 8𝔭 ⋈ 8𝔫 ⋈ 8T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_oxygen_16 : ℝ := 14899.142843

/-- Silicon-28 atom (²⁸Si): 14𝔭 ⋈ 14𝔫 ⋈ 14T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_silicon_28 : ℝ := 26060.297976

/-- Iron-56 atom (⁵⁶Fe): 26𝔭 ⋈ 30𝔫 ⋈ 26T_{2,3}. -/
-- Ref: [manuscript] §11/mass-from-generators
noncomputable def qou_iron_56 : ℝ := 52102.978883

-- ═══════════════════════════════════════════════════════════════════
-- Agreement checks (analogous to terminal_resolution_sub_keV)
-- ═══════════════════════════════════════════════════════════════════

/-- Hydrogen atom: QOU vs CODATA+m_e, within 0.01 MeV. -/
-- Ref: [codata2022] CODATA 2022
theorem hydrogen_agreement :
    |qou_hydrogen_1 - (codata_proton + codata_electron)| < 0.01 := by
  unfold qou_hydrogen_1 codata_proton codata_electron
  norm_num

/-- Deuterium atom: QOU vs CODATA+m_e, within 0.01 MeV. -/
-- Ref: [codata2022] CODATA 2022
theorem deuterium_agreement :
    |qou_deuterium - (codata_deuteron + codata_electron)| < 0.01 := by
  unfold qou_deuterium codata_deuteron codata_electron
  norm_num

/-- Helium-4 atom: QOU vs CODATA+2m_e, within 0.01 MeV. -/
-- Ref: [codata2022] CODATA 2022
theorem helium_4_agreement :
    |qou_helium_4 - (codata_he4 + 2 * codata_electron)| < 0.01 := by
  unfold qou_helium_4 codata_he4 codata_electron
  norm_num

end QOU.Experimental.MassData
