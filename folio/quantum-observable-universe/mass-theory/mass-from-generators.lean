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
- [leitner2026] §11-experimental-evidence/mass-from-generators

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
-- Atom rows and agreement checks: removed 2026-11-28
--
-- Twelve atom masses `qou_hydrogen_1` … `qou_iron_56` and the theorems
-- `hydrogen_agreement`, `deuterium_agreement`, `helium_4_agreement` stood
-- here. The rows were computed from dressed quark masses μ_u = 311.10,
-- μ_d = 312.39 MeV chosen under the retired convention-C pair formula to
-- reproduce m_p and m_n, so they were fitted, and the theorems compared
-- them with measured values inside Lean. Both are removed (owner rules
-- 2026-11-27: no fitting, no empirical values in formal proofs). Record:
-- docs/audits/2026-11-28-dressed-mass-fit-removal.md.
-- ═══════════════════════════════════════════════════════════════════

end QOU.Experimental.MassData
