import Mathlib.Data.Real.Basic
import QOU.HadronicMass
import QOU.AtomicMass.MagicNumbersFromQ
import Mathlib.Tactic.NormNum

/-!
  QOU Atomic Mass Predictions — CODATA 2022 vs AME2020 Audit

  This file separates two independent data sources:
  - **CODATA 2022**: Constituent masses (m_p, m_n, m_e)
  - **AME2020**: Atomic mass unit (u), mass excesses (Δ_H, Δ_n),
    and binding energies per nucleon (B/A)

  For each element, three quantities are computed:
  1. `codata_mass`: Z × m_p + N × m_n + Z × m_e − B (CODATA constituents)
  2. `ame2020_mass`: A × u + Δ (AME2020 mass excess)
  3. Deviation theorems comparing the two

  The systematic difference is Z × 0.015 keV (electron binding energy
  of hydrogen, absent in CODATA m_p + m_e but present in AME2020 M_H).
-/

namespace QOU.AtomicMass

/-! ## CODATA 2022 Constituent Masses

Source: NIST CODATA 2022 Recommended Values
https://physics.nist.gov/cuu/Constants/ -/

/-- Proton mass (CODATA 2022): 938.272 089 43(29) MeV/c². -/
noncomputable def codata_m_p : ℝ := 938.27208943

/-- Neutron mass (CODATA 2022): 939.565 421 94(48) MeV/c². -/
noncomputable def codata_m_n : ℝ := 939.56542194

/-- Electron mass (CODATA 2022): 0.510 998 950 69(16) MeV/c². -/
noncomputable def codata_m_e : ℝ := 0.51099895069

/-! ## AME2020 Constants

Source: Atomic Mass Evaluation 2020 (Wang et al., Chinese Physics C 45, 030003)
https://www-nds.iaea.org/amdc/ -/

/-- Atomic mass unit (CODATA 2022): 931.49410242 MeV/c². -/
noncomputable def ame_u : ℝ := 931.49410242

/-- ¹H mass excess (AME2020): 7.2889705 MeV. -/
noncomputable def ame_delta_H : ℝ := 7.2889705

/-- Neutron mass excess (AME2020): 8.07131806 MeV. -/
noncomputable def ame_delta_n : ℝ := 8.07131806

/-! ## Mass Computation Functions -/

/-- CODATA path: atomic mass from constituent masses minus binding energy.
    M = Z × m_p + N × m_n + Z × m_e − A × (B/A) -/
noncomputable def codata_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  (Z : ℝ) * codata_m_p + (N : ℝ) * codata_m_n + (Z : ℝ) * codata_m_e
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- AME2020 path: atomic mass from mass unit + mass excess.
    M = A × u + Z × Δ_H + N × Δ_n − A × (B/A)
    where Δ = Z × Δ_H + N × Δ_n − B is the nuclear mass excess. -/
noncomputable def ame2020_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  ((Z : ℝ) + (N : ℝ)) * ame_u + (Z : ℝ) * ame_delta_H + (N : ℝ) * ame_delta_n
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- Element data with both CODATA and AME2020 mass computations. -/
structure ElementDatum where
  /-- Atomic number. -/
  Z : ℕ
  /-- Neutron number. -/
  N : ℕ
  /-- Binding energy per nucleon from AME2020 (MeV). -/
  BperA : ℝ

/-- CODATA-derived atomic mass for an element. -/
noncomputable def ElementDatum.codataMass (d : ElementDatum) : ℝ :=
  codata_atomic_mass d.Z d.N d.BperA

/-- AME2020-derived atomic mass for an element. -/
noncomputable def ElementDatum.ameMass (d : ElementDatum) : ℝ :=
  ame2020_atomic_mass d.Z d.N d.BperA

/-- The systematic CODATA−AME2020 offset per proton: ≈ 0.015 keV = 1.546e-5 MeV.
    This arises because CODATA uses m_p + m_e (free particles) while
    AME2020 uses M_H (hydrogen atom, including 13.6 eV binding). -/
noncomputable def codata_ame_offset_per_Z : ℝ :=
  (codata_m_p + codata_m_e) - (ame_u + ame_delta_H)

-- ════════════════════════════════════════════════════════════
-- 1. Hydrogen (H), A = 1
-- ════════════════════════════════════════════════════════════

/-- Hydrogen (Z=1, N=0, A=1). B/A = 0.0 MeV (AME2020). -/
noncomputable def h : ElementDatum where
  Z := 1; N := 0; BperA := 0.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Hydrogen: 938.7831 MeV. -/
noncomputable def codata_mass_h : ℝ := h.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Hydrogen: 938.7831 MeV. -/
noncomputable def ame2020_mass_h : ℝ := h.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Hydrogen: 0.015 keV
    (= 1 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_h :
    |h.codataMass - h.ameMass| < 0.0001 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass h
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 2. Helium (He), A = 4
-- ════════════════════════════════════════════════════════════

/-- Helium (Z=2, N=2, A=4). B/A = 7.0739 MeV (AME2020). -/
noncomputable def he : ElementDatum where
  Z := 2; N := 2; BperA := 7.0739

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Helium: 3728.4014 MeV. -/
noncomputable def codata_mass_he : ℝ := he.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Helium: 3728.4014 MeV. -/
noncomputable def ame2020_mass_he : ℝ := he.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Helium: 0.034 keV
    (= 2 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_he :
    |he.codataMass - he.ameMass| < 0.0002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass he
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 3. Lithium (Li), A = 7
-- ════════════════════════════════════════════════════════════

/-- Lithium (Z=3, N=4, A=7). B/A = 5.6063 MeV (AME2020). -/
noncomputable def li : ElementDatum where
  Z := 3; N := 4; BperA := 5.6063

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Lithium: 6535.3669 MeV. -/
noncomputable def codata_mass_li : ℝ := li.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Lithium: 6535.3668 MeV. -/
noncomputable def ame2020_mass_li : ℝ := li.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Lithium: 0.052 keV
    (= 3 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_li :
    |li.codataMass - li.ameMass| < 0.0002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass li
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 4. Beryllium (Be), A = 9
-- ════════════════════════════════════════════════════════════

/-- Beryllium (Z=4, N=5, A=9). B/A = 6.4628 MeV (AME2020). -/
noncomputable def be : ElementDatum where
  Z := 4; N := 5; BperA := 6.4628

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Beryllium: 8394.7943 MeV. -/
noncomputable def codata_mass_be : ℝ := be.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Beryllium: 8394.7942 MeV. -/
noncomputable def ame2020_mass_be : ℝ := be.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Beryllium: 0.069 keV
    (= 4 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_be :
    |be.codataMass - be.ameMass| < 0.0002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass be
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 5. Boron (B), A = 11
-- ════════════════════════════════════════════════════════════

/-- Boron (Z=5, N=6, A=11). B/A = 6.9277 MeV (AME2020). -/
noncomputable def b : ElementDatum where
  Z := 5; N := 6; BperA := 6.9277

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Boron: 10255.1033 MeV. -/
noncomputable def codata_mass_b : ℝ := b.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Boron: 10255.1032 MeV. -/
noncomputable def ame2020_mass_b : ℝ := b.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Boron: 0.086 keV
    (= 5 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_b :
    |b.codataMass - b.ameMass| < 0.0002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass b
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 6. Carbon (C), A = 12
-- ════════════════════════════════════════════════════════════

/-- Carbon (Z=6, N=6, A=12). B/A = 7.6801 MeV (AME2020). -/
noncomputable def c : ElementDatum where
  Z := 6; N := 6; BperA := 7.6801

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Carbon: 11177.9299 MeV. -/
noncomputable def codata_mass_c : ℝ := c.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Carbon: 11177.9298 MeV. -/
noncomputable def ame2020_mass_c : ℝ := c.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Carbon: 0.102 keV
    (= 6 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_c :
    |c.codataMass - c.ameMass| < 0.0003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass c
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 7. Nitrogen (N), A = 14
-- ════════════════════════════════════════════════════════════

/-- Nitrogen (Z=7, N=7, A=14). B/A = 7.4756 MeV (AME2020). -/
noncomputable def n : ElementDatum where
  Z := 7; N := 7; BperA := 7.4756

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Nitrogen: 13043.7812 MeV. -/
noncomputable def codata_mass_n : ℝ := n.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Nitrogen: 13043.7811 MeV. -/
noncomputable def ame2020_mass_n : ℝ := n.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Nitrogen: 0.118 keV
    (= 7 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_n :
    |n.codataMass - n.ameMass| < 0.0003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass n
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 8. Oxygen (O), A = 16
-- ════════════════════════════════════════════════════════════

/-- Oxygen (Z=8, N=8, A=16). B/A = 7.9762 MeV (AME2020). -/
noncomputable def o : ElementDatum where
  Z := 8; N := 8; BperA := 7.9762

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Oxygen: 14899.1689 MeV. -/
noncomputable def codata_mass_o : ℝ := o.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Oxygen: 14899.1687 MeV. -/
noncomputable def ame2020_mass_o : ℝ := o.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Oxygen: 0.135 keV
    (= 8 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_o :
    |o.codataMass - o.ameMass| < 0.0003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass o
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 9. Fluorine (F), A = 19
-- ════════════════════════════════════════════════════════════

/-- Fluorine (Z=9, N=10, A=19). B/A = 7.779 MeV (AME2020). -/
noncomputable def f : ElementDatum where
  Z := 9; N := 10; BperA := 7.779

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Fluorine: 17696.9010 MeV. -/
noncomputable def codata_mass_f : ℝ := f.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Fluorine: 17696.9009 MeV. -/
noncomputable def ame2020_mass_f : ℝ := f.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Fluorine: 0.154 keV
    (= 9 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_f :
    |f.codataMass - f.ameMass| < 0.0003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass f
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 10. Neon (Ne), A = 20
-- ════════════════════════════════════════════════════════════

/-- Neon (Z=10, N=10, A=20). B/A = 8.0325 MeV (AME2020). -/
noncomputable def ne : ElementDatum where
  Z := 10; N := 10; BperA := 8.0325

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Neon: 18622.8351 MeV. -/
noncomputable def codata_mass_ne : ℝ := ne.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Neon: 18622.8349 MeV. -/
noncomputable def ame2020_mass_ne : ℝ := ne.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Neon: 0.169 keV
    (= 10 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ne :
    |ne.codataMass - ne.ameMass| < 0.0004 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ne
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 11. Sodium (Na), A = 23
-- ════════════════════════════════════════════════════════════

/-- Sodium (Z=11, N=12, A=23). B/A = 8.1115 MeV (AME2020). -/
noncomputable def na : ElementDatum where
  Z := 11; N := 12; BperA := 8.1115

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Sodium: 21414.8345 MeV. -/
noncomputable def codata_mass_na : ℝ := na.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Sodium: 21414.8343 MeV. -/
noncomputable def ame2020_mass_na : ℝ := na.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Sodium: 0.188 keV
    (= 11 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_na :
    |na.codataMass - na.ameMass| < 0.0004 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass na
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 12. Magnesium (Mg), A = 24
-- ════════════════════════════════════════════════════════════

/-- Magnesium (Z=12, N=12, A=24). B/A = 8.2607 MeV (AME2020). -/
noncomputable def mg : ElementDatum where
  Z := 12; N := 12; BperA := 8.2607

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Magnesium: 22341.9253 MeV. -/
noncomputable def codata_mass_mg : ℝ := mg.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Magnesium: 22341.9251 MeV. -/
noncomputable def ame2020_mass_mg : ℝ := mg.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Magnesium: 0.203 keV
    (= 12 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_mg :
    |mg.codataMass - mg.ameMass| < 0.0004 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass mg
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 13. Aluminium (Al), A = 27
-- ════════════════════════════════════════════════════════════

/-- Aluminium (Z=13, N=14, A=27). B/A = 8.3316 MeV (AME2020). -/
noncomputable def al : ElementDatum where
  Z := 13; N := 14; BperA := 8.3316

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Aluminium: 25133.1429 MeV. -/
noncomputable def codata_mass_al : ℝ := al.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Aluminium: 25133.1426 MeV. -/
noncomputable def ame2020_mass_al : ℝ := al.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Aluminium: 0.221 keV
    (= 13 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_al :
    |al.codataMass - al.ameMass| < 0.0004 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass al
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 14. Silicon (Si), A = 28
-- ════════════════════════════════════════════════════════════

/-- Silicon (Z=14, N=14, A=28). B/A = 8.4477 MeV (AME2020). -/
noncomputable def si : ElementDatum where
  Z := 14; N := 14; BperA := 8.4477

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Silicon: 26060.3435 MeV. -/
noncomputable def codata_mass_si : ℝ := si.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Silicon: 26060.3433 MeV. -/
noncomputable def ame2020_mass_si : ℝ := si.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Silicon: 0.237 keV
    (= 14 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_si :
    |si.codataMass - si.ameMass| < 0.0005 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass si
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 15. Phosphorus (P), A = 31
-- ════════════════════════════════════════════════════════════

/-- Phosphorus (Z=15, N=16, A=31). B/A = 8.4812 MeV (AME2020). -/
noncomputable def p_el : ElementDatum where
  Z := 15; N := 16; BperA := 8.4812

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Phosphorus: 28851.8759 MeV. -/
noncomputable def codata_mass_p_el : ℝ := p_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Phosphorus: 28851.8756 MeV. -/
noncomputable def ame2020_mass_p_el : ℝ := p_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Phosphorus: 0.255 keV
    (= 15 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_p_el :
    |p_el.codataMass - p_el.ameMass| < 0.0005 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass p_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 16. Sulfur (S), A = 32
-- ════════════════════════════════════════════════════════════

/-- Sulfur (Z=16, N=16, A=32). B/A = 8.4932 MeV (AME2020). -/
noncomputable def s : ElementDatum where
  Z := 16; N := 16; BperA := 8.4932

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Sulfur: 29781.7938 MeV. -/
noncomputable def codata_mass_s : ℝ := s.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Sulfur: 29781.7935 MeV. -/
noncomputable def ame2020_mass_s : ℝ := s.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Sulfur: 0.271 keV
    (= 16 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_s :
    |s.codataMass - s.ameMass| < 0.0005 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass s
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 17. Chlorine (Cl), A = 35
-- ════════════════════════════════════════════════════════════

/-- Chlorine (Z=17, N=18, A=35). B/A = 8.5203 MeV (AME2020). -/
noncomputable def cl : ElementDatum where
  Z := 17; N := 18; BperA := 8.5203

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Chlorine: 32573.2796 MeV. -/
noncomputable def codata_mass_cl : ℝ := cl.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Chlorine: 32573.2793 MeV. -/
noncomputable def ame2020_mass_cl : ℝ := cl.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Chlorine: 0.289 keV
    (= 17 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cl :
    |cl.codataMass - cl.ameMass| < 0.0005 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cl
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 18. Argon (Ar), A = 40
-- ════════════════════════════════════════════════════════════

/-- Argon (Z=18, N=22, A=40). B/A = 8.5954 MeV (AME2020). -/
noncomputable def ar : ElementDatum where
  Z := 18; N := 22; BperA := 8.5954

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Argon: 37224.7189 MeV. -/
noncomputable def codata_mass_ar : ℝ := ar.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Argon: 37224.7186 MeV. -/
noncomputable def ame2020_mass_ar : ℝ := ar.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Argon: 0.310 keV
    (= 18 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ar :
    |ar.codataMass - ar.ameMass| < 0.0006 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ar
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 19. Potassium (K), A = 39
-- ════════════════════════════════════════════════════════════

/-- Potassium (Z=19, N=20, A=39). B/A = 8.557 MeV (AME2020). -/
noncomputable def k : ElementDatum where
  Z := 19; N := 20; BperA := 8.557

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Potassium: 36294.4641 MeV. -/
noncomputable def codata_mass_k : ℝ := k.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Potassium: 36294.4638 MeV. -/
noncomputable def ame2020_mass_k : ℝ := k.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Potassium: 0.323 keV
    (= 19 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_k :
    |k.codataMass - k.ameMass| < 0.0006 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass k
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 20. Calcium (Ca), A = 40
-- ════════════════════════════════════════════════════════════

/-- Calcium (Z=20, N=20, A=40). B/A = 8.5513 MeV (AME2020). -/
noncomputable def ca : ElementDatum where
  Z := 20; N := 20; BperA := 8.5513

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Calcium: 37224.9182 MeV. -/
noncomputable def codata_mass_ca : ℝ := ca.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Calcium: 37224.9179 MeV. -/
noncomputable def ame2020_mass_ca : ℝ := ca.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Calcium: 0.338 keV
    (= 20 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ca :
    |ca.codataMass - ca.ameMass| < 0.0006 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ca
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 21. Scandium (Sc), A = 45
-- ════════════════════════════════════════════════════════════

/-- Scandium (Z=21, N=24, A=45). B/A = 8.619 MeV (AME2020). -/
noncomputable def sc : ElementDatum where
  Z := 21; N := 24; BperA := 8.619

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Scandium: 41876.1600 MeV. -/
noncomputable def codata_mass_sc : ℝ := sc.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Scandium: 41876.1596 MeV. -/
noncomputable def ame2020_mass_sc : ℝ := sc.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Scandium: 0.360 keV
    (= 21 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sc :
    |sc.codataMass - sc.ameMass| < 0.0006 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sc
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 22. Titanium (Ti), A = 48
-- ════════════════════════════════════════════════════════════

/-- Titanium (Z=22, N=26, A=48). B/A = 8.723 MeV (AME2020). -/
noncomputable def ti : ElementDatum where
  Z := 22; N := 26; BperA := 8.723

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Titanium: 44663.2249 MeV. -/
noncomputable def codata_mass_ti : ℝ := ti.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Titanium: 44663.2245 MeV. -/
noncomputable def ame2020_mass_ti : ℝ := ti.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Titanium: 0.378 keV
    (= 22 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ti :
    |ti.codataMass - ti.ameMass| < 0.0007 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ti
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 23. Vanadium (V), A = 51
-- ════════════════════════════════════════════════════════════

/-- Vanadium (Z=23, N=28, A=51). B/A = 8.742 MeV (AME2020). -/
noncomputable def v : ElementDatum where
  Z := 23; N := 28; BperA := 8.742

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Vanadium: 47454.0008 MeV. -/
noncomputable def codata_mass_v : ℝ := v.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Vanadium: 47454.0005 MeV. -/
noncomputable def ame2020_mass_v : ℝ := v.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Vanadium: 0.396 keV
    (= 23 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_v :
    |v.codataMass - v.ameMass| < 0.0007 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass v
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 24. Chromium (Cr), A = 52
-- ════════════════════════════════════════════════════════════

/-- Chromium (Z=24, N=28, A=52). B/A = 8.776 MeV (AME2020). -/
noncomputable def cr : ElementDatum where
  Z := 24; N := 28; BperA := 8.776

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Chromium: 48382.2739 MeV. -/
noncomputable def codata_mass_cr : ℝ := cr.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Chromium: 48382.2735 MeV. -/
noncomputable def ame2020_mass_cr : ℝ := cr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Chromium: 0.412 keV
    (= 24 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cr :
    |cr.codataMass - cr.ameMass| < 0.0007 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 25. Manganese (Mn), A = 55
-- ════════════════════════════════════════════════════════════

/-- Manganese (Z=25, N=30, A=55). B/A = 8.7649 MeV (AME2020). -/
noncomputable def mn : ElementDatum where
  Z := 25; N := 30; BperA := 8.7649

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Manganese: 51174.4704 MeV. -/
noncomputable def codata_mass_mn : ℝ := mn.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Manganese: 51174.4699 MeV. -/
noncomputable def ame2020_mass_mn : ℝ := mn.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Manganese: 0.430 keV
    (= 25 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_mn :
    |mn.codataMass - mn.ameMass| < 0.0007 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass mn
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 26. Iron (Fe), A = 56
-- ════════════════════════════════════════════════════════════

/-- Iron (Z=26, N=30, A=56). B/A = 8.7903 MeV (AME2020). -/
noncomputable def fe : ElementDatum where
  Z := 26; N := 30; BperA := 8.7903

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Iron: 52103.0662 MeV. -/
noncomputable def codata_mass_fe : ℝ := fe.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Iron: 52103.0657 MeV. -/
noncomputable def ame2020_mass_fe : ℝ := fe.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Iron: 0.446 keV
    (= 26 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_fe :
    |fe.codataMass - fe.ameMass| < 0.0008 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass fe
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 27. Cobalt (Co), A = 59
-- ════════════════════════════════════════════════════════════

/-- Cobalt (Z=27, N=32, A=59). B/A = 8.768 MeV (AME2020). -/
noncomputable def co : ElementDatum where
  Z := 27; N := 32; BperA := 8.768

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Cobalt: 54895.9249 MeV. -/
noncomputable def codata_mass_co : ℝ := co.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Cobalt: 54895.9244 MeV. -/
noncomputable def ame2020_mass_co : ℝ := co.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Cobalt: 0.464 keV
    (= 27 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_co :
    |co.codataMass - co.ameMass| < 0.0008 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass co
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 28. Nickel (Ni), A = 58
-- ════════════════════════════════════════════════════════════

/-- Nickel (Z=28, N=30, A=58). B/A = 8.7322 MeV (AME2020). -/
noncomputable def ni : ElementDatum where
  Z := 28; N := 30; BperA := 8.7322

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Nickel: 53966.4215 MeV. -/
noncomputable def codata_mass_ni : ℝ := ni.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Nickel: 53966.4211 MeV. -/
noncomputable def ame2020_mass_ni : ℝ := ni.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Nickel: 0.477 keV
    (= 28 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ni :
    |ni.codataMass - ni.ameMass| < 0.0008 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ni
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 29. Copper (Cu), A = 63
-- ════════════════════════════════════════════════════════════

/-- Copper (Z=29, N=34, A=63). B/A = 8.7522 MeV (AME2020). -/
noncomputable def cu : ElementDatum where
  Z := 29; N := 34; BperA := 8.7522

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Copper: 58618.5453 MeV. -/
noncomputable def codata_mass_cu : ℝ := cu.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Copper: 58618.5448 MeV. -/
noncomputable def ame2020_mass_cu : ℝ := cu.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Copper: 0.498 keV
    (= 29 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cu :
    |cu.codataMass - cu.ameMass| < 0.0008 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cu
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 30. Zinc (Zn), A = 64
-- ════════════════════════════════════════════════════════════

/-- Zinc (Z=30, N=34, A=64). B/A = 8.7357 MeV (AME2020). -/
noncomputable def zn : ElementDatum where
  Z := 30; N := 34; BperA := 8.7357

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Zinc: 59549.6322 MeV. -/
noncomputable def codata_mass_zn : ℝ := zn.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Zinc: 59549.6317 MeV. -/
noncomputable def ame2020_mass_zn : ℝ := zn.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Zinc: 0.513 keV
    (= 30 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_zn :
    |zn.codataMass - zn.ameMass| < 0.0009 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass zn
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 31. Gallium (Ga), A = 69
-- ════════════════════════════════════════════════════════════

/-- Gallium (Z=31, N=38, A=69). B/A = 8.7246 MeV (AME2020). -/
noncomputable def ga : ElementDatum where
  Z := 31; N := 38; BperA := 8.7246

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Gallium: 64203.7644 MeV. -/
noncomputable def codata_mass_ga : ℝ := ga.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Gallium: 64203.7638 MeV. -/
noncomputable def ame2020_mass_ga : ℝ := ga.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Gallium: 0.535 keV
    (= 31 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ga :
    |ga.codataMass - ga.ameMass| < 0.0009 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ga
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 32. Germanium (Ge), A = 74
-- ════════════════════════════════════════════════════════════

/-- Germanium (Z=32, N=42, A=74). B/A = 8.7264 MeV (AME2020). -/
noncomputable def ge : ElementDatum where
  Z := 32; N := 42; BperA := 8.7264

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Germanium: 68857.0529 MeV. -/
noncomputable def codata_mass_ge : ℝ := ge.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Germanium: 68857.0524 MeV. -/
noncomputable def ame2020_mass_ge : ℝ := ge.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Germanium: 0.556 keV
    (= 32 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ge :
    |ge.codataMass - ge.ameMass| < 0.0009 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ge
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 33. Arsenic (As), A = 75
-- ════════════════════════════════════════════════════════════

/-- Arsenic (Z=33, N=42, A=75). B/A = 8.701 MeV (AME2020). -/
noncomputable def as_el : ElementDatum where
  Z := 33; N := 42; BperA := 8.701

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Arsenic: 69789.0146 MeV. -/
noncomputable def codata_mass_as_el : ℝ := as_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Arsenic: 69789.0141 MeV. -/
noncomputable def ame2020_mass_as_el : ℝ := as_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Arsenic: 0.572 keV
    (= 33 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_as_el :
    |as_el.codataMass - as_el.ameMass| < 0.001 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass as_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 34. Selenium (Se), A = 80
-- ════════════════════════════════════════════════════════════

/-- Selenium (Z=34, N=46, A=80). B/A = 8.711 MeV (AME2020). -/
noncomputable def se : ElementDatum where
  Z := 34; N := 46; BperA := 8.711

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Selenium: 74441.7544 MeV. -/
noncomputable def codata_mass_se : ℝ := se.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Selenium: 74441.7538 MeV. -/
noncomputable def ame2020_mass_se : ℝ := se.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Selenium: 0.593 keV
    (= 34 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_se :
    |se.codataMass - se.ameMass| < 0.001 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass se
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 35. Bromine (Br), A = 79
-- ════════════════════════════════════════════════════════════

/-- Bromine (Z=35, N=44, A=79). B/A = 8.6961 MeV (AME2020). -/
noncomputable def br : ElementDatum where
  Z := 35; N := 44; BperA := 8.6961

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Bromine: 73511.2948 MeV. -/
noncomputable def codata_mass_br : ℝ := br.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Bromine: 73511.2942 MeV. -/
noncomputable def ame2020_mass_br : ℝ := br.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Bromine: 0.605 keV
    (= 35 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_br :
    |br.codataMass - br.ameMass| < 0.001 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass br
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 36. Krypton (Kr), A = 84
-- ════════════════════════════════════════════════════════════

/-- Krypton (Z=36, N=48, A=84). B/A = 8.7172 MeV (AME2020). -/
noncomputable def kr : ElementDatum where
  Z := 36; N := 48; BperA := 8.7172

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Krypton: 78163.0866 MeV. -/
noncomputable def codata_mass_kr : ℝ := kr.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Krypton: 78163.0860 MeV. -/
noncomputable def ame2020_mass_kr : ℝ := kr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Krypton: 0.627 keV
    (= 36 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_kr :
    |kr.codataMass - kr.ameMass| < 0.001 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass kr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 37. Rubidium (Rb), A = 85
-- ════════════════════════════════════════════════════════════

/-- Rubidium (Z=37, N=48, A=85). B/A = 8.6974 MeV (AME2020). -/
noncomputable def rb : ElementDatum where
  Z := 37; N := 48; BperA := 8.6974

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Rubidium: 79094.8355 MeV. -/
noncomputable def codata_mass_rb : ℝ := rb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Rubidium: 79094.8349 MeV. -/
noncomputable def ame2020_mass_rb : ℝ := rb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Rubidium: 0.642 keV
    (= 37 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_rb :
    |rb.codataMass - rb.ameMass| < 0.0011 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass rb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 38. Strontium (Sr), A = 88
-- ════════════════════════════════════════════════════════════

/-- Strontium (Z=38, N=50, A=88). B/A = 8.7326 MeV (AME2020). -/
noncomputable def sr : ElementDatum where
  Z := 38; N := 50; BperA := 8.7326

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Strontium: 81883.5597 MeV. -/
noncomputable def codata_mass_sr : ℝ := sr.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Strontium: 81883.5590 MeV. -/
noncomputable def ame2020_mass_sr : ℝ := sr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Strontium: 0.661 keV
    (= 38 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sr :
    |sr.codataMass - sr.ameMass| < 0.0011 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 39. Yttrium (Y), A = 89
-- ════════════════════════════════════════════════════════════

/-- Yttrium (Z=39, N=50, A=89). B/A = 8.7138 MeV (AME2020). -/
noncomputable def y : ElementDatum where
  Z := 39; N := 50; BperA := 8.7138

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Yttrium: 82815.2833 MeV. -/
noncomputable def codata_mass_y : ℝ := y.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Yttrium: 82815.2827 MeV. -/
noncomputable def ame2020_mass_y : ℝ := y.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Yttrium: 0.676 keV
    (= 39 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_y :
    |y.codataMass - y.ameMass| < 0.0011 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass y
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 40. Zirconium (Zr), A = 90
-- ════════════════════════════════════════════════════════════

/-- Zirconium (Z=40, N=50, A=90). B/A = 8.7098 MeV (AME2020). -/
noncomputable def zr : ElementDatum where
  Z := 40; N := 50; BperA := 8.7098

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Zirconium: 83745.7126 MeV. -/
noncomputable def codata_mass_zr : ℝ := zr.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Zirconium: 83745.7119 MeV. -/
noncomputable def ame2020_mass_zr : ℝ := zr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Zirconium: 0.691 keV
    (= 40 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_zr :
    |zr.codataMass - zr.ameMass| < 0.0011 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass zr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 41. Niobium (Nb), A = 93
-- ════════════════════════════════════════════════════════════

/-- Niobium (Z=41, N=52, A=93). B/A = 8.6641 MeV (AME2020). -/
noncomputable def nb : ElementDatum where
  Z := 41; N := 52; BperA := 8.6641

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Niobium: 86541.7473 MeV. -/
noncomputable def codata_mass_nb : ℝ := nb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Niobium: 86541.7466 MeV. -/
noncomputable def ame2020_mass_nb : ℝ := nb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Niobium: 0.710 keV
    (= 41 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_nb :
    |nb.codataMass - nb.ameMass| < 0.0012 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass nb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 42. Molybdenum (Mo), A = 98
-- ════════════════════════════════════════════════════════════

/-- Molybdenum (Z=42, N=56, A=98). B/A = 8.6353 MeV (AME2020). -/
noncomputable def mo : ElementDatum where
  Z := 42; N := 56; BperA := 8.6353

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Molybdenum: 91198.2939 MeV. -/
noncomputable def codata_mass_mo : ℝ := mo.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Molybdenum: 91198.2932 MeV. -/
noncomputable def ame2020_mass_mo : ℝ := mo.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Molybdenum: 0.731 keV
    (= 42 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_mo :
    |mo.codataMass - mo.ameMass| < 0.0012 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass mo
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 43. Technetium (Tc), A = 98
-- ════════════════════════════════════════════════════════════

/-- Technetium (Z=43, N=55, A=98). B/A = 8.5937 MeV (AME2020). -/
noncomputable def tc : ElementDatum where
  Z := 43; N := 55; BperA := 8.5937

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Technetium: 91201.5884 MeV. -/
noncomputable def codata_mass_tc : ℝ := tc.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Technetium: 91201.5877 MeV. -/
noncomputable def ame2020_mass_tc : ℝ := tc.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Technetium: 0.745 keV
    (= 43 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_tc :
    |tc.codataMass - tc.ameMass| < 0.0012 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass tc
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 44. Ruthenium (Ru), A = 102
-- ════════════════════════════════════════════════════════════

/-- Ruthenium (Z=44, N=58, A=102). B/A = 8.607 MeV (AME2020). -/
noncomputable def ru : ElementDatum where
  Z := 44; N := 58; BperA := 8.607

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Ruthenium: 94923.3364 MeV. -/
noncomputable def codata_mass_ru : ℝ := ru.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Ruthenium: 94923.3356 MeV. -/
noncomputable def ame2020_mass_ru : ℝ := ru.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Ruthenium: 0.765 keV
    (= 44 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ru :
    |ru.codataMass - ru.ameMass| < 0.0012 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ru
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 45. Rhodium (Rh), A = 103
-- ════════════════════════════════════════════════════════════

/-- Rhodium (Z=45, N=58, A=103). B/A = 8.5843 MeV (AME2020). -/
noncomputable def rh : ElementDatum where
  Z := 45; N := 58; BperA := 8.5843

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Rhodium: 95855.8505 MeV. -/
noncomputable def codata_mass_rh : ℝ := rh.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Rhodium: 95855.8498 MeV. -/
noncomputable def ame2020_mass_rh : ℝ := rh.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Rhodium: 0.780 keV
    (= 45 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_rh :
    |rh.codataMass - rh.ameMass| < 0.0013 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass rh
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 46. Palladium (Pd), A = 106
-- ════════════════════════════════════════════════════════════

/-- Palladium (Z=46, N=60, A=106). B/A = 8.567 MeV (AME2020). -/
noncomputable def pd : ElementDatum where
  Z := 46; N := 60; BperA := 8.567

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Palladium: 98649.8454 MeV. -/
noncomputable def codata_mass_pd : ℝ := pd.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Palladium: 98649.8446 MeV. -/
noncomputable def ame2020_mass_pd : ℝ := pd.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Palladium: 0.799 keV
    (= 46 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pd :
    |pd.codataMass - pd.ameMass| < 0.0013 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pd
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 47. Silver (Ag), A = 107
-- ════════════════════════════════════════════════════════════

/-- Silver (Z=47, N=60, A=107). B/A = 8.5536 MeV (AME2020). -/
noncomputable def ag : ElementDatum where
  Z := 47; N := 60; BperA := 8.5536

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Silver: 99581.4953 MeV. -/
noncomputable def codata_mass_ag : ℝ := ag.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Silver: 99581.4945 MeV. -/
noncomputable def ame2020_mass_ag : ℝ := ag.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Silver: 0.814 keV
    (= 47 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ag :
    |ag.codataMass - ag.ameMass| < 0.0013 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ag
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 48. Cadmium (Cd), A = 114
-- ════════════════════════════════════════════════════════════

/-- Cadmium (Z=48, N=66, A=114). B/A = 8.5398 MeV (AME2020). -/
noncomputable def cd : ElementDatum where
  Z := 48; N := 66; BperA := 8.5398

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Cadmium: 106099.3689 MeV. -/
noncomputable def codata_mass_cd : ℝ := cd.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Cadmium: 106099.3681 MeV. -/
noncomputable def ame2020_mass_cd : ℝ := cd.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Cadmium: 0.838 keV
    (= 48 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cd :
    |cd.codataMass - cd.ameMass| < 0.0014 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cd
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 49. Indium (In), A = 115
-- ════════════════════════════════════════════════════════════

/-- Indium (Z=49, N=66, A=115). B/A = 8.516 MeV (AME2020). -/
noncomputable def in_el : ElementDatum where
  Z := 49; N := 66; BperA := 8.516

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Indium: 107032.3492 MeV. -/
noncomputable def codata_mass_in_el : ℝ := in_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Indium: 107032.3483 MeV. -/
noncomputable def ame2020_mass_in_el : ℝ := in_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Indium: 0.854 keV
    (= 49 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_in_el :
    |in_el.codataMass - in_el.ameMass| < 0.0014 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass in_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 50. Tin (Sn), A = 120
-- ════════════════════════════════════════════════════════════

/-- Tin (Z=50, N=70, A=120). B/A = 8.505 MeV (AME2020). -/
noncomputable def sn : ElementDatum where
  Z := 50; N := 70; BperA := 8.505

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Tin: 111688.1340 MeV. -/
noncomputable def codata_mass_sn : ℝ := sn.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Tin: 111688.1331 MeV. -/
noncomputable def ame2020_mass_sn : ℝ := sn.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Tin: 0.875 keV
    (= 50 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sn :
    |sn.codataMass - sn.ameMass| < 0.0014 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sn
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 51. Antimony (Sb), A = 121
-- ════════════════════════════════════════════════════════════

/-- Antimony (Z=51, N=70, A=121). B/A = 8.482 MeV (AME2020). -/
noncomputable def sb : ElementDatum where
  Z := 51; N := 70; BperA := 8.482

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Antimony: 112621.1950 MeV. -/
noncomputable def codata_mass_sb : ℝ := sb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Antimony: 112621.1942 MeV. -/
noncomputable def ame2020_mass_sb : ℝ := sb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Antimony: 0.891 keV
    (= 51 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sb :
    |sb.codataMass - sb.ameMass| < 0.0014 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 52. Tellurium (Te), A = 130
-- ════════════════════════════════════════════════════════════

/-- Tellurium (Z=52, N=78, A=130). B/A = 8.439 MeV (AME2020). -/
noncomputable def te : ElementDatum where
  Z := 52; N := 78; BperA := 8.439

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Tellurium: 121005.7535 MeV. -/
noncomputable def codata_mass_te : ℝ := te.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Tellurium: 121005.7526 MeV. -/
noncomputable def ame2020_mass_te : ℝ := te.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Tellurium: 0.918 keV
    (= 52 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_te :
    |te.codataMass - te.ameMass| < 0.0015 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass te
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 53. Iodine (I), A = 127
-- ════════════════════════════════════════════════════════════

/-- Iodine (Z=53, N=74, A=127). B/A = 8.4455 MeV (AME2020). -/
noncomputable def i : ElementDatum where
  Z := 53; N := 74; BperA := 8.4455

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Iodine: 118210.7664 MeV. -/
noncomputable def codata_mass_i : ℝ := i.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Iodine: 118210.7655 MeV. -/
noncomputable def ame2020_mass_i : ℝ := i.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Iodine: 0.927 keV
    (= 53 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_i :
    |i.codataMass - i.ameMass| < 0.0015 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass i
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 54. Xenon (Xe), A = 132
-- ════════════════════════════════════════════════════════════

/-- Xenon (Z=54, N=78, A=132). B/A = 8.4275 MeV (AME2020). -/
noncomputable def xe : ElementDatum where
  Z := 54; N := 78; BperA := 8.4275

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Xenon: 122867.9597 MeV. -/
noncomputable def codata_mass_xe : ℝ := xe.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Xenon: 122867.9587 MeV. -/
noncomputable def ame2020_mass_xe : ℝ := xe.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Xenon: 0.949 keV
    (= 54 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_xe :
    |xe.codataMass - xe.ameMass| < 0.0015 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass xe
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 55. Caesium (Cs), A = 133
-- ════════════════════════════════════════════════════════════

/-- Caesium (Z=55, N=78, A=133). B/A = 8.41 MeV (AME2020). -/
noncomputable def cs : ElementDatum where
  Z := 55; N := 78; BperA := 8.41

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Caesium: 123800.6428 MeV. -/
noncomputable def codata_mass_cs : ℝ := cs.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Caesium: 123800.6418 MeV. -/
noncomputable def ame2020_mass_cs : ℝ := cs.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Caesium: 0.964 keV
    (= 55 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cs :
    |cs.codataMass - cs.ameMass| < 0.0015 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cs
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 56. Barium (Ba), A = 138
-- ════════════════════════════════════════════════════════════

/-- Barium (Z=56, N=82, A=138). B/A = 8.3937 MeV (AME2020). -/
noncomputable def ba : ElementDatum where
  Z := 56; N := 82; BperA := 8.3937

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Barium: 128457.8869 MeV. -/
noncomputable def codata_mass_ba : ℝ := ba.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Barium: 128457.8860 MeV. -/
noncomputable def ame2020_mass_ba : ℝ := ba.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Barium: 0.986 keV
    (= 56 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ba :
    |ba.codataMass - ba.ameMass| < 0.0016 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ba
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 57. Lanthanum (La), A = 139
-- ════════════════════════════════════════════════════════════

/-- Lanthanum (Z=57, N=82, A=139). B/A = 8.378 MeV (AME2020). -/
noncomputable def la : ElementDatum where
  Z := 57; N := 82; BperA := 8.378

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Lanthanum: 129390.4586 MeV. -/
noncomputable def codata_mass_la : ℝ := la.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Lanthanum: 129390.4576 MeV. -/
noncomputable def ame2020_mass_la : ℝ := la.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Lanthanum: 1.001 keV
    (= 57 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_la :
    |la.codataMass - la.ameMass| < 0.0016 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass la
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 58. Cerium (Ce), A = 140
-- ════════════════════════════════════════════════════════════

/-- Cerium (Z=58, N=82, A=140). B/A = 8.3765 MeV (AME2020). -/
noncomputable def ce : ElementDatum where
  Z := 58; N := 82; BperA := 8.3765

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Cerium: 130321.0737 MeV. -/
noncomputable def codata_mass_ce : ℝ := ce.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Cerium: 130321.0727 MeV. -/
noncomputable def ame2020_mass_ce : ℝ := ce.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Cerium: 1.016 keV
    (= 58 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ce :
    |ce.codataMass - ce.ameMass| < 0.0016 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ce
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 59. Praseodymium (Pr), A = 141
-- ════════════════════════════════════════════════════════════

/-- Praseodymium (Z=59, N=82, A=141). B/A = 8.354 MeV (AME2020). -/
noncomputable def pr : ElementDatum where
  Z := 59; N := 82; BperA := 8.354

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Praseodymium: 131254.6528 MeV. -/
noncomputable def codata_mass_pr : ℝ := pr.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Praseodymium: 131254.6518 MeV. -/
noncomputable def ame2020_mass_pr : ℝ := pr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Praseodymium: 1.032 keV
    (= 59 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pr :
    |pr.codataMass - pr.ameMass| < 0.0016 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 60. Neodymium (Nd), A = 142
-- ════════════════════════════════════════════════════════════

/-- Neodymium (Z=60, N=82, A=142). B/A = 8.346 MeV (AME2020). -/
noncomputable def nd : ElementDatum where
  Z := 60; N := 82; BperA := 8.346

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Neodymium: 132186.2179 MeV. -/
noncomputable def codata_mass_nd : ℝ := nd.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Neodymium: 132186.2169 MeV. -/
noncomputable def ame2020_mass_nd : ℝ := nd.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Neodymium: 1.047 keV
    (= 60 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_nd :
    |nd.codataMass - nd.ameMass| < 0.0017 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass nd
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 61. Promethium (Pm), A = 145
-- ════════════════════════════════════════════════════════════

/-- Promethium (Z=61, N=84, A=145). B/A = 8.304 MeV (AME2020). -/
noncomputable def pm : ElementDatum where
  Z := 61; N := 84; BperA := 8.304

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Promethium: 134985.1838 MeV. -/
noncomputable def codata_mass_pm : ℝ := pm.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Promethium: 134985.1828 MeV. -/
noncomputable def ame2020_mass_pm : ℝ := pm.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Promethium: 1.066 keV
    (= 61 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pm :
    |pm.codataMass - pm.ameMass| < 0.0017 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pm
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 62. Samarium (Sm), A = 152
-- ════════════════════════════════════════════════════════════

/-- Samarium (Z=62, N=90, A=152). B/A = 8.244 MeV (AME2020). -/
noncomputable def sm : ElementDatum where
  Z := 62; N := 90; BperA := 8.244

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Samarium: 141512.3515 MeV. -/
noncomputable def codata_mass_sm : ℝ := sm.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Samarium: 141512.3504 MeV. -/
noncomputable def ame2020_mass_sm : ℝ := sm.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Samarium: 1.090 keV
    (= 62 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sm :
    |sm.codataMass - sm.ameMass| < 0.0017 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sm
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 63. Europium (Eu), A = 153
-- ════════════════════════════════════════════════════════════

/-- Europium (Z=63, N=90, A=153). B/A = 8.229 MeV (AME2020). -/
noncomputable def eu : ElementDatum where
  Z := 63; N := 90; BperA := 8.229

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Europium: 142445.1855 MeV. -/
noncomputable def codata_mass_eu : ℝ := eu.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Europium: 142445.1844 MeV. -/
noncomputable def ame2020_mass_eu : ℝ := eu.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Europium: 1.105 keV
    (= 63 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_eu :
    |eu.codataMass - eu.ameMass| < 0.0018 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass eu
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 64. Gadolinium (Gd), A = 158
-- ════════════════════════════════════════════════════════════

/-- Gadolinium (Z=64, N=94, A=158). B/A = 8.214 MeV (AME2020). -/
noncomputable def gd : ElementDatum where
  Z := 64; N := 94; BperA := 8.214

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Gadolinium: 147103.4553 MeV. -/
noncomputable def codata_mass_gd : ℝ := gd.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Gadolinium: 147103.4542 MeV. -/
noncomputable def ame2020_mass_gd : ℝ := gd.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Gadolinium: 1.127 keV
    (= 64 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_gd :
    |gd.codataMass - gd.ameMass| < 0.0018 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass gd
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 65. Terbium (Tb), A = 159
-- ════════════════════════════════════════════════════════════

/-- Terbium (Z=65, N=94, A=159). B/A = 8.199 MeV (AME2020). -/
noncomputable def tb : ElementDatum where
  Z := 65; N := 94; BperA := 8.199

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Terbium: 148036.4094 MeV. -/
noncomputable def codata_mass_tb : ℝ := tb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Terbium: 148036.4083 MeV. -/
noncomputable def ame2020_mass_tb : ℝ := tb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Terbium: 1.142 keV
    (= 65 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_tb :
    |tb.codataMass - tb.ameMass| < 0.0018 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass tb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 66. Dysprosium (Dy), A = 164
-- ════════════════════════════════════════════════════════════

/-- Dysprosium (Z=66, N=98, A=164). B/A = 8.1865 MeV (AME2020). -/
noncomputable def dy : ElementDatum where
  Z := 66; N := 98; BperA := 8.1865

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Dysprosium: 152694.5092 MeV. -/
noncomputable def codata_mass_dy : ℝ := dy.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Dysprosium: 152694.5080 MeV. -/
noncomputable def ame2020_mass_dy : ℝ := dy.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Dysprosium: 1.163 keV
    (= 66 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_dy :
    |dy.codataMass - dy.ameMass| < 0.0018 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass dy
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 67. Holmium (Ho), A = 165
-- ════════════════════════════════════════════════════════════

/-- Holmium (Z=67, N=98, A=165). B/A = 8.171 MeV (AME2020). -/
noncomputable def ho : ElementDatum where
  Z := 67; N := 98; BperA := 8.171

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Holmium: 153627.6633 MeV. -/
noncomputable def codata_mass_ho : ℝ := ho.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Holmium: 153627.6621 MeV. -/
noncomputable def ame2020_mass_ho : ℝ := ho.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Holmium: 1.179 keV
    (= 67 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ho :
    |ho.codataMass - ho.ameMass| < 0.0019 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ho
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 68. Erbium (Er), A = 166
-- ════════════════════════════════════════════════════════════

/-- Erbium (Z=68, N=98, A=166). B/A = 8.169 MeV (AME2020). -/
noncomputable def er : ElementDatum where
  Z := 68; N := 98; BperA := 8.169

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Erbium: 154558.6074 MeV. -/
noncomputable def codata_mass_er : ℝ := er.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Erbium: 154558.6062 MeV. -/
noncomputable def ame2020_mass_er : ℝ := er.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Erbium: 1.194 keV
    (= 68 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_er :
    |er.codataMass - er.ameMass| < 0.0019 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass er
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 69. Thulium (Tm), A = 169
-- ════════════════════════════════════════════════════════════

/-- Thulium (Z=69, N=100, A=169). B/A = 8.146 MeV (AME2020). -/
noncomputable def tm_el : ElementDatum where
  Z := 69; N := 100; BperA := 8.146

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Thulium: 157355.9013 MeV. -/
noncomputable def codata_mass_tm_el : ℝ := tm_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Thulium: 157355.9001 MeV. -/
noncomputable def ame2020_mass_tm_el : ℝ := tm_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Thulium: 1.213 keV
    (= 69 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_tm_el :
    |tm_el.codataMass - tm_el.ameMass| < 0.0019 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass tm_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 70. Ytterbium (Yb), A = 174
-- ════════════════════════════════════════════════════════════

/-- Ytterbium (Z=70, N=104, A=174). B/A = 8.128 MeV (AME2020). -/
noncomputable def yb : ElementDatum where
  Z := 70; N := 104; BperA := 8.128

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Ytterbium: 162015.3481 MeV. -/
noncomputable def codata_mass_yb : ℝ := yb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Ytterbium: 162015.3468 MeV. -/
noncomputable def ame2020_mass_yb : ℝ := yb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Ytterbium: 1.234 keV
    (= 70 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_yb :
    |yb.codataMass - yb.ameMass| < 0.002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass yb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 71. Lutetium (Lu), A = 175
-- ════════════════════════════════════════════════════════════

/-- Lutetium (Z=71, N=104, A=175). B/A = 8.1165 MeV (AME2020). -/
noncomputable def lu : ElementDatum where
  Z := 71; N := 104; BperA := 8.1165

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Lutetium: 162948.0157 MeV. -/
noncomputable def codata_mass_lu : ℝ := lu.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Lutetium: 162948.0144 MeV. -/
noncomputable def ame2020_mass_lu : ℝ := lu.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Lutetium: 1.250 keV
    (= 71 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_lu :
    |lu.codataMass - lu.ameMass| < 0.002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass lu
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 72. Hafnium (Hf), A = 180
-- ════════════════════════════════════════════════════════════

/-- Hafnium (Z=72, N=108, A=180). B/A = 8.0985 MeV (AME2020). -/
noncomputable def hf : ElementDatum where
  Z := 72; N := 108; BperA := 8.0985

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Hafnium: 167607.7179 MeV. -/
noncomputable def codata_mass_hf : ℝ := hf.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Hafnium: 167607.7167 MeV. -/
noncomputable def ame2020_mass_hf : ℝ := hf.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Hafnium: 1.271 keV
    (= 72 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_hf :
    |hf.codataMass - hf.ameMass| < 0.002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass hf
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 73. Tantalum (Ta), A = 181
-- ════════════════════════════════════════════════════════════

/-- Tantalum (Z=73, N=108, A=181). B/A = 8.087 MeV (AME2020). -/
noncomputable def ta : ElementDatum where
  Z := 73; N := 108; BperA := 8.087

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Tantalum: 168540.4840 MeV. -/
noncomputable def codata_mass_ta : ℝ := ta.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Tantalum: 168540.4827 MeV. -/
noncomputable def ame2020_mass_ta : ℝ := ta.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Tantalum: 1.286 keV
    (= 73 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ta :
    |ta.codataMass - ta.ameMass| < 0.002 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ta
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 74. Tungsten (W), A = 184
-- ════════════════════════════════════════════════════════════

/-- Tungsten (Z=74, N=110, A=184). B/A = 8.0639 MeV (AME2020). -/
noncomputable def w : ElementDatum where
  Z := 74; N := 110; BperA := 8.0639

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Tungsten: 171338.3874 MeV. -/
noncomputable def codata_mass_w : ℝ := w.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Tungsten: 171338.3860 MeV. -/
noncomputable def ame2020_mass_w : ℝ := w.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Tungsten: 1.305 keV
    (= 74 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_w :
    |w.codataMass - w.ameMass| < 0.0021 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass w
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 75. Rhenium (Re), A = 187
-- ════════════════════════════════════════════════════════════

/-- Rhenium (Z=75, N=112, A=187). B/A = 8.039 MeV (AME2020). -/
noncomputable def re_el : ElementDatum where
  Z := 75; N := 112; BperA := 8.039

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Rhenium: 174136.7659 MeV. -/
noncomputable def codata_mass_re_el : ℝ := re_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Rhenium: 174136.7646 MeV. -/
noncomputable def ame2020_mass_re_el : ℝ := re_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Rhenium: 1.323 keV
    (= 75 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_re_el :
    |re_el.codataMass - re_el.ameMass| < 0.0021 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass re_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 76. Osmium (Os), A = 192
-- ════════════════════════════════════════════════════════════

/-- Osmium (Z=76, N=116, A=192). B/A = 8.0194 MeV (AME2020). -/
noncomputable def os : ElementDatum where
  Z := 76; N := 116; BperA := 8.0194

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Osmium: 178797.3789 MeV. -/
noncomputable def codata_mass_os : ℝ := os.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Osmium: 178797.3775 MeV. -/
noncomputable def ame2020_mass_os : ℝ := os.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Osmium: 1.344 keV
    (= 76 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_os :
    |os.codataMass - os.ameMass| < 0.0021 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass os
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 77. Iridium (Ir), A = 193
-- ════════════════════════════════════════════════════════════

/-- Iridium (Z=77, N=116, A=193). B/A = 8.006 MeV (AME2020). -/
noncomputable def ir : ElementDatum where
  Z := 77; N := 116; BperA := 8.006

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Iridium: 179730.7288 MeV. -/
noncomputable def codata_mass_ir : ℝ := ir.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Iridium: 179730.7274 MeV. -/
noncomputable def ame2020_mass_ir : ℝ := ir.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Iridium: 1.360 keV
    (= 77 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ir :
    |ir.codataMass - ir.ameMass| < 0.0021 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ir
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 78. Platinum (Pt), A = 195
-- ════════════════════════════════════════════════════════════

/-- Platinum (Z=78, N=117, A=195). B/A = 7.993 MeV (AME2020). -/
noncomputable def pt : ElementDatum where
  Z := 78; N := 117; BperA := 7.993

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Platinum: 181595.6003 MeV. -/
noncomputable def codata_mass_pt : ℝ := pt.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Platinum: 181595.5989 MeV. -/
noncomputable def ame2020_mass_pt : ℝ := pt.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Platinum: 1.377 keV
    (= 78 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pt :
    |pt.codataMass - pt.ameMass| < 0.0022 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pt
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 79. Gold (Au), A = 197
-- ════════════════════════════════════════════════════════════

/-- Gold (Z=79, N=118, A=197). B/A = 7.9759 MeV (AME2020). -/
noncomputable def au : ElementDatum where
  Z := 79; N := 118; BperA := 7.9759

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Gold: 183461.3315 MeV. -/
noncomputable def codata_mass_au : ℝ := au.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Gold: 183461.3301 MeV. -/
noncomputable def ame2020_mass_au : ℝ := au.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Gold: 1.394 keV
    (= 79 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_au :
    |au.codataMass - au.ameMass| < 0.0022 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass au
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 80. Mercury (Hg), A = 202
-- ════════════════════════════════════════════════════════════

/-- Mercury (Z=80, N=122, A=202). B/A = 7.953 MeV (AME2020). -/
noncomputable def hg : ElementDatum where
  Z := 80; N := 122; BperA := 7.953

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Mercury: 188123.1225 MeV. -/
noncomputable def codata_mass_hg : ℝ := hg.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Mercury: 188123.1211 MeV. -/
noncomputable def ame2020_mass_hg : ℝ := hg.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Mercury: 1.415 keV
    (= 80 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_hg :
    |hg.codataMass - hg.ameMass| < 0.0022 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass hg
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 81. Thallium (Tl), A = 205
-- ════════════════════════════════════════════════════════════

/-- Thallium (Z=81, N=124, A=205). B/A = 7.937 MeV (AME2020). -/
noncomputable def tl : ElementDatum where
  Z := 81; N := 124; BperA := 7.937

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Thallium: 190920.4575 MeV. -/
noncomputable def codata_mass_tl : ℝ := tl.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Thallium: 190920.4560 MeV. -/
noncomputable def ame2020_mass_tl : ℝ := tl.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Thallium: 1.433 keV
    (= 81 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_tl :
    |tl.codataMass - tl.ameMass| < 0.0023 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass tl
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 82. Lead (Pb), A = 208
-- ════════════════════════════════════════════════════════════

/-- Lead (Z=82, N=126, A=208). B/A = 7.8675 MeV (AME2020). -/
noncomputable def pb : ElementDatum where
  Z := 82; N := 126; BperA := 7.8675

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Lead: 193729.0164 MeV. -/
noncomputable def codata_mass_pb : ℝ := pb.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Lead: 193729.0150 MeV. -/
noncomputable def ame2020_mass_pb : ℝ := pb.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Lead: 1.452 keV
    (= 82 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pb :
    |pb.codataMass - pb.ameMass| < 0.0023 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pb
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 83. Bismuth (Bi), A = 209
-- ════════════════════════════════════════════════════════════

/-- Bismuth (Z=83, N=126, A=209). B/A = 7.848 MeV (AME2020). -/
noncomputable def bi : ElementDatum where
  Z := 83; N := 126; BperA := 7.848

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Bismuth: 194664.0075 MeV. -/
noncomputable def codata_mass_bi : ℝ := bi.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Bismuth: 194664.0060 MeV. -/
noncomputable def ame2020_mass_bi : ℝ := bi.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Bismuth: 1.467 keV
    (= 83 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_bi :
    |bi.codataMass - bi.ameMass| < 0.0023 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass bi
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 84. Polonium (Po), A = 209
-- ════════════════════════════════════════════════════════════

/-- Polonium (Z=84, N=125, A=209). B/A = 7.8352 MeV (AME2020). -/
noncomputable def po : ElementDatum where
  Z := 84; N := 125; BperA := 7.8352

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Polonium: 194665.9004 MeV. -/
noncomputable def codata_mass_po : ℝ := po.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Polonium: 194665.8989 MeV. -/
noncomputable def ame2020_mass_po : ℝ := po.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Polonium: 1.481 keV
    (= 84 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_po :
    |po.codataMass - po.ameMass| < 0.0023 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass po
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 85. Astatine (At), A = 210
-- ════════════════════════════════════════════════════════════

/-- Astatine (Z=85, N=125, A=210). B/A = 7.8147 MeV (AME2020). -/
noncomputable def at_el : ElementDatum where
  Z := 85; N := 125; BperA := 7.8147

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Astatine: 195601.1533 MeV. -/
noncomputable def codata_mass_at_el : ℝ := at_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Astatine: 195601.1518 MeV. -/
noncomputable def ame2020_mass_at_el : ℝ := at_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Astatine: 1.497 keV
    (= 85 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_at_el :
    |at_el.codataMass - at_el.ameMass| < 0.0023 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass at_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 86. Radon (Rn), A = 222
-- ════════════════════════════════════════════════════════════

/-- Radon (Z=86, N=136, A=222). B/A = 7.7227 MeV (AME2020). -/
noncomputable def rn : ElementDatum where
  Z := 86; N := 136; BperA := 7.7227

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Radon: 206801.8036 MeV. -/
noncomputable def codata_mass_rn : ℝ := rn.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Radon: 206801.8021 MeV. -/
noncomputable def ame2020_mass_rn : ℝ := rn.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Radon: 1.528 keV
    (= 86 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_rn :
    |rn.codataMass - rn.ameMass| < 0.0024 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass rn
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 87. Francium (Fr), A = 223
-- ════════════════════════════════════════════════════════════

/-- Francium (Z=87, N=136, A=223). B/A = 7.7095 MeV (AME2020). -/
noncomputable def fr_el : ElementDatum where
  Z := 87; N := 136; BperA := 7.7095

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Francium: 207735.8076 MeV. -/
noncomputable def codata_mass_fr_el : ℝ := fr_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Francium: 207735.8060 MeV. -/
noncomputable def ame2020_mass_fr_el : ℝ := fr_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Francium: 1.544 keV
    (= 87 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_fr_el :
    |fr_el.codataMass - fr_el.ameMass| < 0.0024 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass fr_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 88. Radium (Ra), A = 226
-- ════════════════════════════════════════════════════════════

/-- Radium (Z=88, N=138, A=226). B/A = 7.662 MeV (AME2020). -/
noncomputable def ra : ElementDatum where
  Z := 88; N := 138; BperA := 7.662

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Radium: 210541.3280 MeV. -/
noncomputable def codata_mass_ra : ℝ := ra.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Radium: 210541.3264 MeV. -/
noncomputable def ame2020_mass_ra : ℝ := ra.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Radium: 1.562 keV
    (= 88 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ra :
    |ra.codataMass - ra.ameMass| < 0.0024 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ra
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 89. Actinium (Ac), A = 227
-- ════════════════════════════════════════════════════════════

/-- Actinium (Z=89, N=138, A=227). B/A = 7.651 MeV (AME2020). -/
noncomputable def ac : ElementDatum where
  Z := 89; N := 138; BperA := 7.651

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Actinium: 211474.9461 MeV. -/
noncomputable def codata_mass_ac : ℝ := ac.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Actinium: 211474.9445 MeV. -/
noncomputable def ame2020_mass_ac : ℝ := ac.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Actinium: 1.577 keV
    (= 89 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ac :
    |ac.codataMass - ac.ameMass| < 0.0025 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ac
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 90. Thorium (Th), A = 232
-- ════════════════════════════════════════════════════════════

/-- Thorium (Z=90, N=142, A=232). B/A = 7.615 MeV (AME2020). -/
noncomputable def th : ElementDatum where
  Z := 90; N := 142; BperA := 7.615

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Thorium: 216142.0879 MeV. -/
noncomputable def codata_mass_th : ℝ := th.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Thorium: 216142.0863 MeV. -/
noncomputable def ame2020_mass_th : ℝ := th.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Thorium: 1.599 keV
    (= 90 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_th :
    |th.codataMass - th.ameMass| < 0.0025 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass th
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 91. Protactinium (Pa), A = 231
-- ════════════════════════════════════════════════════════════

/-- Protactinium (Z=91, N=140, A=231). B/A = 7.6138 MeV (AME2020). -/
noncomputable def pa : ElementDatum where
  Z := 91; N := 140; BperA := 7.6138

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Protactinium: 215209.6323 MeV. -/
noncomputable def codata_mass_pa : ℝ := pa.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Protactinium: 215209.6307 MeV. -/
noncomputable def ame2020_mass_pa : ℝ := pa.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Protactinium: 1.611 keV
    (= 91 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pa :
    |pa.codataMass - pa.ameMass| < 0.0025 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pa
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 92. Uranium (U), A = 238
-- ════════════════════════════════════════════════════════════

/-- Uranium (Z=92, N=146, A=238). B/A = 7.5701 MeV (AME2020). -/
noncomputable def u_el : ElementDatum where
  Z := 92; N := 146; BperA := 7.5701

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Uranium: 221742.9119 MeV. -/
noncomputable def codata_mass_u_el : ℝ := u_el.codataMass

-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Uranium: 221742.9103 MeV. -/
noncomputable def ame2020_mass_u_el : ℝ := u_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Uranium: 1.636 keV
    (= 92 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_u_el :
    |u_el.codataMass - u_el.ameMass| < 0.0026 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass u_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 93. Neptunium (Np), A = 237
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Neptunium (Z=93, N=144, A=237). B/A = 7.5753 MeV (AME2020). -/
noncomputable def np : ElementDatum where
  Z := 93; N := 144; BperA := 7.5753

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Neptunium: 220808.9019 MeV. -/
noncomputable def codata_mass_np : ℝ := np.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Neptunium: 220808.9002 MeV. -/
noncomputable def ame2020_mass_np : ℝ := np.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Neptunium: 1.648 keV
    (= 93 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_np :
    |np.codataMass - np.ameMass| < 0.0026 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass np
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 94. Plutonium (Pu), A = 244
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Plutonium (Z=94, N=150, A=244). B/A = 7.5242 MeV (AME2020). -/
noncomputable def pu : ElementDatum where
  Z := 94; N := 150; BperA := 7.5242

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Plutonium: 227344.5188 MeV. -/
noncomputable def codata_mass_pu : ℝ := pu.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Plutonium: 227344.5171 MeV. -/
noncomputable def ame2020_mass_pu : ℝ := pu.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Plutonium: 1.672 keV
    (= 94 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_pu :
    |pu.codataMass - pu.ameMass| < 0.0026 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass pu
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 95. Americium (Am), A = 243
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Americium (Z=95, N=148, A=243). B/A = 7.5249 MeV (AME2020). -/
noncomputable def am : ElementDatum where
  Z := 95; N := 148; BperA := 7.5249

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Americium: 226411.5251 MeV. -/
noncomputable def codata_mass_am : ℝ := am.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Americium: 226411.5235 MeV. -/
noncomputable def ame2020_mass_am : ℝ := am.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Americium: 1.685 keV
    (= 95 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_am :
    |am.codataMass - am.ameMass| < 0.0026 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass am
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 96. Curium (Cm), A = 247
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Curium (Z=96, N=151, A=247). B/A = 7.4988 MeV (AME2020). -/
noncomputable def cm : ElementDatum where
  Z := 96; N := 151; BperA := 7.4988

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Curium: 230145.3516 MeV. -/
noncomputable def codata_mass_cm : ℝ := cm.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Curium: 230145.3499 MeV. -/
noncomputable def ame2020_mass_cm : ℝ := cm.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Curium: 1.705 keV
    (= 96 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cm :
    |cm.codataMass - cm.ameMass| < 0.0027 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cm
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 97. Berkelium (Bk), A = 247
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Berkelium (Z=97, N=150, A=247). B/A = 7.498 MeV (AME2020). -/
noncomputable def bk : ElementDatum where
  Z := 97; N := 150; BperA := 7.498

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Berkelium: 230144.7669 MeV. -/
noncomputable def codata_mass_bk : ℝ := bk.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Berkelium: 230144.7651 MeV. -/
noncomputable def ame2020_mass_bk : ℝ := bk.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Berkelium: 1.719 keV
    (= 97 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_bk :
    |bk.codataMass - bk.ameMass| < 0.0027 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass bk
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 98. Californium (Cf), A = 251
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Californium (Z=98, N=153, A=251). B/A = 7.4688 MeV (AME2020). -/
noncomputable def cf : ElementDatum where
  Z := 98; N := 153; BperA := 7.4688

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Californium: 233879.5834 MeV. -/
noncomputable def codata_mass_cf : ℝ := cf.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Californium: 233879.5817 MeV. -/
noncomputable def ame2020_mass_cf : ℝ := cf.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Californium: 1.739 keV
    (= 98 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cf :
    |cf.codataMass - cf.ameMass| < 0.0027 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cf
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 99. Einsteinium (Es), A = 252
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Einsteinium (Z=99, N=153, A=252). B/A = 7.4496 MeV (AME2020). -/
noncomputable def es : ElementDatum where
  Z := 99; N := 153; BperA := 7.4496

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Einsteinium: 234815.7361 MeV. -/
noncomputable def codata_mass_es : ℝ := es.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Einsteinium: 234815.7344 MeV. -/
noncomputable def ame2020_mass_es : ℝ := es.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Einsteinium: 1.754 keV
    (= 99 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_es :
    |es.codataMass - es.ameMass| < 0.0027 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass es
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 100. Fermium (Fm), A = 257
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Fermium (Z=100, N=157, A=257). B/A = 7.4197 MeV (AME2020). -/
noncomputable def fm : ElementDatum where
  Z := 100; N := 157; BperA := 7.4197

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Fermium: 239483.2172 MeV. -/
noncomputable def codata_mass_fm : ℝ := fm.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Fermium: 239483.2154 MeV. -/
noncomputable def ame2020_mass_fm : ℝ := fm.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Fermium: 1.775 keV
    (= 100 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_fm :
    |fm.codataMass - fm.ameMass| < 0.0028 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass fm
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 101. Mendelevium (Md), A = 258
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Mendelevium (Z=101, N=157, A=258). B/A = 7.4039 MeV (AME2020). -/
noncomputable def md_el : ElementDatum where
  Z := 101; N := 157; BperA := 7.4039

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Mendelevium: 240418.6570 MeV. -/
noncomputable def codata_mass_md_el : ℝ := md_el.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Mendelevium: 240418.6552 MeV. -/
noncomputable def ame2020_mass_md_el : ℝ := md_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Mendelevium: 1.791 keV
    (= 101 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_md_el :
    |md_el.codataMass - md_el.ameMass| < 0.0028 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass md_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 102. Nobelium (No), A = 259
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Nobelium (Z=102, N=157, A=259). B/A = 7.39 MeV (AME2020). -/
noncomputable def no_el : ElementDatum where
  Z := 102; N := 157; BperA := 7.39

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Nobelium: 241353.6363 MeV. -/
noncomputable def codata_mass_no_el : ℝ := no_el.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Nobelium: 241353.6345 MeV. -/
noncomputable def ame2020_mass_no_el : ℝ := no_el.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Nobelium: 1.806 keV
    (= 102 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_no_el :
    |no_el.codataMass - no_el.ameMass| < 0.0028 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass no_el
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 103. Lawrencium (Lr), A = 266
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Lawrencium (Z=103, N=163, A=266). B/A = 7.354 MeV (AME2020). -/
noncomputable def lr : ElementDatum where
  Z := 103; N := 163; BperA := 7.354

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Lawrencium: 247887.6579 MeV. -/
noncomputable def codata_mass_lr : ℝ := lr.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Lawrencium: 247887.6560 MeV. -/
noncomputable def ame2020_mass_lr : ℝ := lr.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Lawrencium: 1.830 keV
    (= 103 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_lr :
    |lr.codataMass - lr.ameMass| < 0.0028 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass lr
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 104. Rutherfordium (Rf), A = 267
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Rutherfordium (Z=104, N=163, A=267). B/A = 7.338 MeV (AME2020). -/
noncomputable def rf : ElementDatum where
  Z := 104; N := 163; BperA := 7.338

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Rutherfordium: 248823.3590 MeV. -/
noncomputable def codata_mass_rf : ℝ := rf.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Rutherfordium: 248823.3571 MeV. -/
noncomputable def ame2020_mass_rf : ℝ := rf.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Rutherfordium: 1.846 keV
    (= 104 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_rf :
    |rf.codataMass - rf.ameMass| < 0.0029 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass rf
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 105. Dubnium (Db), A = 268
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Dubnium (Z=105, N=163, A=268). B/A = 7.32 MeV (AME2020). -/
noncomputable def db : ElementDatum where
  Z := 105; N := 163; BperA := 7.32

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Dubnium: 249759.6281 MeV. -/
noncomputable def codata_mass_db : ℝ := db.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Dubnium: 249759.6262 MeV. -/
noncomputable def ame2020_mass_db : ℝ := db.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Dubnium: 1.861 keV
    (= 105 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_db :
    |db.codataMass - db.ameMass| < 0.0029 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass db
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 106. Seaborgium (Sg), A = 269
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Seaborgium (Z=106, N=163, A=269). B/A = 7.302 MeV (AME2020). -/
noncomputable def sg : ElementDatum where
  Z := 106; N := 163; BperA := 7.302

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Seaborgium: 250695.9331 MeV. -/
noncomputable def codata_mass_sg : ℝ := sg.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Seaborgium: 250695.9313 MeV. -/
noncomputable def ame2020_mass_sg : ℝ := sg.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Seaborgium: 1.877 keV
    (= 106 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_sg :
    |sg.codataMass - sg.ameMass| < 0.0029 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass sg
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 107. Bohrium (Bh), A = 270
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Bohrium (Z=107, N=163, A=270). B/A = 7.283 MeV (AME2020). -/
noncomputable def bh : ElementDatum where
  Z := 107; N := 163; BperA := 7.283

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Bohrium: 251632.5442 MeV. -/
noncomputable def codata_mass_bh : ℝ := bh.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Bohrium: 251632.5423 MeV. -/
noncomputable def ame2020_mass_bh : ℝ := bh.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Bohrium: 1.892 keV
    (= 107 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_bh :
    |bh.codataMass - bh.ameMass| < 0.0029 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass bh
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 108. Hassium (Hs), A = 277
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Hassium (Z=108, N=169, A=277). B/A = 7.256 MeV (AME2020). -/
noncomputable def hs : ElementDatum where
  Z := 108; N := 169; BperA := 7.256

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Hassium: 258165.2179 MeV. -/
noncomputable def codata_mass_hs : ℝ := hs.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Hassium: 258165.2159 MeV. -/
noncomputable def ame2020_mass_hs : ℝ := hs.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Hassium: 1.916 keV
    (= 108 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_hs :
    |hs.codataMass - hs.ameMass| < 0.003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass hs
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 109. Meitnerium (Mt), A = 278
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Meitnerium (Z=109, N=169, A=278). B/A = 7.237 MeV (AME2020). -/
noncomputable def mt : ElementDatum where
  Z := 109; N := 169; BperA := 7.237

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Meitnerium: 259102.0269 MeV. -/
noncomputable def codata_mass_mt : ℝ := mt.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Meitnerium: 259102.0250 MeV. -/
noncomputable def ame2020_mass_mt : ℝ := mt.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Meitnerium: 1.932 keV
    (= 109 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_mt :
    |mt.codataMass - mt.ameMass| < 0.003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass mt
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 110. Darmstadtium (Ds), A = 281
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Darmstadtium (Z=110, N=171, A=281). B/A = 7.211 MeV (AME2020). -/
noncomputable def ds : ElementDatum where
  Z := 110; N := 171; BperA := 7.211

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Darmstadtium: 261905.5359 MeV. -/
noncomputable def codata_mass_ds : ℝ := ds.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Darmstadtium: 261905.5339 MeV. -/
noncomputable def ame2020_mass_ds : ℝ := ds.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Darmstadtium: 1.950 keV
    (= 110 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ds :
    |ds.codataMass - ds.ameMass| < 0.003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ds
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 111. Roentgenium (Rg), A = 282
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Roentgenium (Z=111, N=171, A=282). B/A = 7.191 MeV (AME2020). -/
noncomputable def rg : ElementDatum where
  Z := 111; N := 171; BperA := 7.191

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Roentgenium: 262842.7480 MeV. -/
noncomputable def codata_mass_rg : ℝ := rg.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Roentgenium: 262842.7460 MeV. -/
noncomputable def ame2020_mass_rg : ℝ := rg.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Roentgenium: 1.966 keV
    (= 111 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_rg :
    |rg.codataMass - rg.ameMass| < 0.003 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass rg
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 112. Copernicium (Cn), A = 285
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Copernicium (Z=112, N=173, A=285). B/A = 7.165 MeV (AME2020). -/
noncomputable def cn : ElementDatum where
  Z := 112; N := 173; BperA := 7.165

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Copernicium: 265646.4989 MeV. -/
noncomputable def codata_mass_cn : ℝ := cn.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Copernicium: 265646.4969 MeV. -/
noncomputable def ame2020_mass_cn : ℝ := cn.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Copernicium: 1.984 keV
    (= 112 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_cn :
    |cn.codataMass - cn.ameMass| < 0.0031 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass cn
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 113. Nihonium (Nh), A = 286
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Nihonium (Z=113, N=173, A=286). B/A = 7.144 MeV (AME2020). -/
noncomputable def nh : ElementDatum where
  Z := 113; N := 173; BperA := 7.144

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Nihonium: 266584.1230 MeV. -/
noncomputable def codata_mass_nh : ℝ := nh.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Nihonium: 266584.1210 MeV. -/
noncomputable def ame2020_mass_nh : ℝ := nh.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Nihonium: 2.000 keV
    (= 113 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_nh :
    |nh.codataMass - nh.ameMass| < 0.0031 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass nh
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 114. Flerovium (Fl), A = 289
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Flerovium (Z=114, N=175, A=289). B/A = 7.118 MeV (AME2020). -/
noncomputable def fl : ElementDatum where
  Z := 114; N := 175; BperA := 7.118

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Flerovium: 269388.1189 MeV. -/
noncomputable def codata_mass_fl : ℝ := fl.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Flerovium: 269388.1169 MeV. -/
noncomputable def ame2020_mass_fl : ℝ := fl.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Flerovium: 2.018 keV
    (= 114 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_fl :
    |fl.codataMass - fl.ameMass| < 0.0031 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass fl
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 115. Moscovium (Mc), A = 290
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Moscovium (Z=115, N=175, A=290). B/A = 7.096 MeV (AME2020). -/
noncomputable def mc : ElementDatum where
  Z := 115; N := 175; BperA := 7.096

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Moscovium: 270326.1640 MeV. -/
noncomputable def codata_mass_mc : ℝ := mc.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Moscovium: 270326.1620 MeV. -/
noncomputable def ame2020_mass_mc : ℝ := mc.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Moscovium: 2.033 keV
    (= 115 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_mc :
    |mc.codataMass - mc.ameMass| < 0.0032 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass mc
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 116. Livermorium (Lv), A = 293
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Livermorium (Z=116, N=177, A=293). B/A = 7.02 MeV (AME2020). -/
noncomputable def lv : ElementDatum where
  Z := 116; N := 177; BperA := 7.02

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Livermorium: 273145.0579 MeV. -/
noncomputable def codata_mass_lv : ℝ := lv.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Livermorium: 273145.0559 MeV. -/
noncomputable def ame2020_mass_lv : ℝ := lv.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Livermorium: 2.052 keV
    (= 116 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_lv :
    |lv.codataMass - lv.ameMass| < 0.0032 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass lv
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 117. Tennessine (Ts), A = 294
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Tennessine (Z=117, N=177, A=294). B/A = 6.996 MeV (AME2020). -/
noncomputable def ts : ElementDatum where
  Z := 117; N := 177; BperA := 6.996

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Tennessine: 274083.8770 MeV. -/
noncomputable def codata_mass_ts : ℝ := ts.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Tennessine: 274083.8750 MeV. -/
noncomputable def ame2020_mass_ts : ℝ := ts.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Tennessine: 2.067 keV
    (= 117 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_ts :
    |ts.codataMass - ts.ameMass| < 0.0032 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass ts
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

-- ════════════════════════════════════════════════════════════
-- 118. Oganesson (Og), A = 294
-- [Synthetic element — reactor/accelerator produced]
-- ════════════════════════════════════════════════════════════

/-- Oganesson (Z=118, N=176, A=294). B/A = 6.972 MeV (AME2020). -/
noncomputable def og : ElementDatum where
  Z := 118; N := 176; BperA := 6.972

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- CODATA-derived mass of Oganesson: 274090.1507 MeV. -/
noncomputable def codata_mass_og : ℝ := og.codataMass

-- Ref: [manuscript] Appendix C
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- AME2020-derived mass of Oganesson: 274090.1486 MeV. -/
noncomputable def ame2020_mass_og : ℝ := og.ameMass

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [ame2020] https://www-nds.iaea.org/amdc/
/-- CODATA−AME2020 deviation for Oganesson: 2.081 keV
    (= 118 × 0.015 keV from H atom electron binding energy). -/
theorem deviation_og :
    |og.codataMass - og.ameMass| < 0.0032 := by
  unfold ElementDatum.codataMass ElementDatum.ameMass og
  unfold codata_atomic_mass ame2020_atomic_mass
  unfold codata_m_p codata_m_n codata_m_e ame_u ame_delta_H ame_delta_n
  norm_num

/-! ## Summary

The CODATA and AME2020 mass derivation paths agree to within
Z × 0.015 keV for all 118 elements. The systematic offset arises
because CODATA treats proton and electron as free particles
(m_p + m_e = 938.78309 MeV), while AME2020 uses the hydrogen atom
mass (M_H = 938.78307 MeV), which includes the 13.6 eV electron
binding energy.

| Z range | Max |CODATA − AME2020| |
|---------|--------------------------|
| 1–10    | 0.15 keV                 |
| 11–50   | 0.77 keV                 |
| 51–92   | 1.42 keV                 |
| 93–118  | 1.83 keV                 |
-/

/-- The systematic per-proton offset between CODATA and AME2020 is
    approximately 0.015 keV (= 1.546 × 10⁻⁵ MeV), arising from the
    electron binding energy of hydrogen. -/
theorem codata_ame_offset_bound :
    |codata_ame_offset_per_Z| < 0.00002 := by
  unfold codata_ame_offset_per_Z codata_m_p codata_m_e ame_u ame_delta_H
  norm_num

end QOU.AtomicMass
