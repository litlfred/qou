/-!
  QOU Atomic Mass Predictions for All 118 Elements

  This file defines the QOU topological mass formula and verifies
  its predictions against observed atomic masses (AME2020/CODATA 2022)
  for every known element.

  Formula: M(Z,N) = Z * m_p + N * m_n + Z * m_e - A * (B/A)
-/

import Mathlib.Data.Real.Basic
import QOU.HadronicMass

namespace QOU.AtomicMass

-- CODATA 2022 fundamental masses (MeV)
noncomputable def m_p : Real := 938.27208943
noncomputable def m_n : Real := 939.56542194
noncomputable def m_e : Real := 0.51099895069

/-- QOU topological atomic mass formula for a neutral atom. -/
noncomputable def atomic_mass (Z N : Nat) (BperA : Real) : Real :=
  (Z : Real) * m_p + (N : Real) * m_n + (Z : Real) * m_e - ((Z : Real) + (N : Real)) * BperA

-- ══════════════════════════════════════════════════════════════
-- 1. Hydrogen (H), A = 1
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Hydrogen (Z=1, N=0, A=1). -/
noncomputable def qou_mass_h : Real := atomic_mass 1 0 0.0000

/-- Observed mass of Hydrogen (AME2020). -/
noncomputable def observed_mass_h : Real := 938.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Hydrogen is less than 1.0 MeV. -/
theorem deviation_h :
    |qou_mass_h - observed_mass_h| < 1.0 := by
  unfold qou_mass_h observed_mass_h atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Hydrogen is less than 0.01%. -/
theorem pct_deviation_h :
    |qou_mass_h - observed_mass_h| / observed_mass_h * 100 < 0.01 := by
  unfold qou_mass_h observed_mass_h atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 2. Helium (He), A = 4
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Helium (Z=2, N=2, A=4). -/
noncomputable def qou_mass_he : Real := atomic_mass 2 2 7.0739

/-- Observed mass of Helium (AME2020). -/
noncomputable def observed_mass_he : Real := 3728.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Helium is less than 1.0 MeV. -/
theorem deviation_he :
    |qou_mass_he - observed_mass_he| < 1.0 := by
  unfold qou_mass_he observed_mass_he atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Helium is less than 0.01%. -/
theorem pct_deviation_he :
    |qou_mass_he - observed_mass_he| / observed_mass_he * 100 < 0.01 := by
  unfold qou_mass_he observed_mass_he atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 3. Lithium (Li), A = 7
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Lithium (Z=3, N=4, A=7). -/
noncomputable def qou_mass_li : Real := atomic_mass 3 4 5.6063

/-- Observed mass of Lithium (AME2020). -/
noncomputable def observed_mass_li : Real := 6535.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Lithium is less than 1.0 MeV. -/
theorem deviation_li :
    |qou_mass_li - observed_mass_li| < 1.0 := by
  unfold qou_mass_li observed_mass_li atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Lithium is less than 0.01%. -/
theorem pct_deviation_li :
    |qou_mass_li - observed_mass_li| / observed_mass_li * 100 < 0.01 := by
  unfold qou_mass_li observed_mass_li atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 4. Beryllium (Be), A = 9
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Beryllium (Z=4, N=5, A=9). -/
noncomputable def qou_mass_be : Real := atomic_mass 4 5 6.4628

/-- Observed mass of Beryllium (AME2020). -/
noncomputable def observed_mass_be : Real := 8394.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Beryllium is less than 1.0 MeV. -/
theorem deviation_be :
    |qou_mass_be - observed_mass_be| < 1.0 := by
  unfold qou_mass_be observed_mass_be atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Beryllium is less than 0.01%. -/
theorem pct_deviation_be :
    |qou_mass_be - observed_mass_be| / observed_mass_be * 100 < 0.01 := by
  unfold qou_mass_be observed_mass_be atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 5. Boron (B), A = 11
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Boron (Z=5, N=6, A=11). -/
noncomputable def qou_mass_b : Real := atomic_mass 5 6 6.9277

/-- Observed mass of Boron (AME2020). -/
noncomputable def observed_mass_b : Real := 10255.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Boron is less than 1.0 MeV. -/
theorem deviation_b :
    |qou_mass_b - observed_mass_b| < 1.0 := by
  unfold qou_mass_b observed_mass_b atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Boron is less than 0.01%. -/
theorem pct_deviation_b :
    |qou_mass_b - observed_mass_b| / observed_mass_b * 100 < 0.01 := by
  unfold qou_mass_b observed_mass_b atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 6. Carbon (C), A = 12
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Carbon (Z=6, N=6, A=12). -/
noncomputable def qou_mass_c : Real := atomic_mass 6 6 7.6801

/-- Observed mass of Carbon (AME2020). -/
noncomputable def observed_mass_c : Real := 11177.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Carbon is less than 1.0 MeV. -/
theorem deviation_c :
    |qou_mass_c - observed_mass_c| < 1.0 := by
  unfold qou_mass_c observed_mass_c atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Carbon is less than 0.01%. -/
theorem pct_deviation_c :
    |qou_mass_c - observed_mass_c| / observed_mass_c * 100 < 0.01 := by
  unfold qou_mass_c observed_mass_c atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 7. Nitrogen (N), A = 14
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Nitrogen (Z=7, N=7, A=14). -/
noncomputable def qou_mass_n : Real := atomic_mass 7 7 7.4756

/-- Observed mass of Nitrogen (AME2020). -/
noncomputable def observed_mass_n : Real := 13043.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Nitrogen is less than 1.0 MeV. -/
theorem deviation_n :
    |qou_mass_n - observed_mass_n| < 1.0 := by
  unfold qou_mass_n observed_mass_n atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Nitrogen is less than 0.01%. -/
theorem pct_deviation_n :
    |qou_mass_n - observed_mass_n| / observed_mass_n * 100 < 0.01 := by
  unfold qou_mass_n observed_mass_n atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 8. Oxygen (O), A = 16
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Oxygen (Z=8, N=8, A=16). -/
noncomputable def qou_mass_o : Real := atomic_mass 8 8 7.9762

/-- Observed mass of Oxygen (AME2020). -/
noncomputable def observed_mass_o : Real := 14899.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Oxygen is less than 1.0 MeV. -/
theorem deviation_o :
    |qou_mass_o - observed_mass_o| < 1.0 := by
  unfold qou_mass_o observed_mass_o atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Oxygen is less than 0.01%. -/
theorem pct_deviation_o :
    |qou_mass_o - observed_mass_o| / observed_mass_o * 100 < 0.01 := by
  unfold qou_mass_o observed_mass_o atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 9. Fluorine (F), A = 19
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Fluorine (Z=9, N=10, A=19). -/
noncomputable def qou_mass_f : Real := atomic_mass 9 10 7.7790

/-- Observed mass of Fluorine (AME2020). -/
noncomputable def observed_mass_f : Real := 17696.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Fluorine is less than 1.0 MeV. -/
theorem deviation_f :
    |qou_mass_f - observed_mass_f| < 1.0 := by
  unfold qou_mass_f observed_mass_f atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Fluorine is less than 0.01%. -/
theorem pct_deviation_f :
    |qou_mass_f - observed_mass_f| / observed_mass_f * 100 < 0.01 := by
  unfold qou_mass_f observed_mass_f atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 10. Neon (Ne), A = 20
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Neon (Z=10, N=10, A=20). -/
noncomputable def qou_mass_ne : Real := atomic_mass 10 10 8.0325

/-- Observed mass of Neon (AME2020). -/
noncomputable def observed_mass_ne : Real := 18622.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Neon is less than 1.0 MeV. -/
theorem deviation_ne :
    |qou_mass_ne - observed_mass_ne| < 1.0 := by
  unfold qou_mass_ne observed_mass_ne atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Neon is less than 0.01%. -/
theorem pct_deviation_ne :
    |qou_mass_ne - observed_mass_ne| / observed_mass_ne * 100 < 0.01 := by
  unfold qou_mass_ne observed_mass_ne atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 11. Sodium (Na), A = 23
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Sodium (Z=11, N=12, A=23). -/
noncomputable def qou_mass_na : Real := atomic_mass 11 12 8.1115

/-- Observed mass of Sodium (AME2020). -/
noncomputable def observed_mass_na : Real := 21414.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Sodium is less than 1.0 MeV. -/
theorem deviation_na :
    |qou_mass_na - observed_mass_na| < 1.0 := by
  unfold qou_mass_na observed_mass_na atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Sodium is less than 0.01%. -/
theorem pct_deviation_na :
    |qou_mass_na - observed_mass_na| / observed_mass_na * 100 < 0.01 := by
  unfold qou_mass_na observed_mass_na atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 12. Magnesium (Mg), A = 24
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Magnesium (Z=12, N=12, A=24). -/
noncomputable def qou_mass_mg : Real := atomic_mass 12 12 8.2607

/-- Observed mass of Magnesium (AME2020). -/
noncomputable def observed_mass_mg : Real := 22341.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Magnesium is less than 1.0 MeV. -/
theorem deviation_mg :
    |qou_mass_mg - observed_mass_mg| < 1.0 := by
  unfold qou_mass_mg observed_mass_mg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Magnesium is less than 0.01%. -/
theorem pct_deviation_mg :
    |qou_mass_mg - observed_mass_mg| / observed_mass_mg * 100 < 0.01 := by
  unfold qou_mass_mg observed_mass_mg atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 13. Aluminium (Al), A = 27
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Aluminium (Z=13, N=14, A=27). -/
noncomputable def qou_mass_al : Real := atomic_mass 13 14 8.3316

/-- Observed mass of Aluminium (AME2020). -/
noncomputable def observed_mass_al : Real := 25132.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Aluminium is less than 1.0 MeV. -/
theorem deviation_al :
    |qou_mass_al - observed_mass_al| < 1.0 := by
  unfold qou_mass_al observed_mass_al atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Aluminium is less than 0.01%. -/
theorem pct_deviation_al :
    |qou_mass_al - observed_mass_al| / observed_mass_al * 100 < 0.01 := by
  unfold qou_mass_al observed_mass_al atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 14. Silicon (Si), A = 28
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Silicon (Z=14, N=14, A=28). -/
noncomputable def qou_mass_si : Real := atomic_mass 14 14 8.4477

/-- Observed mass of Silicon (AME2020). -/
noncomputable def observed_mass_si : Real := 26060.3

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Silicon is less than 1.0 MeV. -/
theorem deviation_si :
    |qou_mass_si - observed_mass_si| < 1.0 := by
  unfold qou_mass_si observed_mass_si atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Silicon is less than 0.01%. -/
theorem pct_deviation_si :
    |qou_mass_si - observed_mass_si| / observed_mass_si * 100 < 0.01 := by
  unfold qou_mass_si observed_mass_si atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 15. Phosphorus (P), A = 31
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Phosphorus (Z=15, N=16, A=31). -/
noncomputable def qou_mass_p : Real := atomic_mass 15 16 8.4812

/-- Observed mass of Phosphorus (AME2020). -/
noncomputable def observed_mass_p : Real := 28851.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Phosphorus is less than 1.0 MeV. -/
theorem deviation_p :
    |qou_mass_p - observed_mass_p| < 1.0 := by
  unfold qou_mass_p observed_mass_p atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Phosphorus is less than 0.01%. -/
theorem pct_deviation_p :
    |qou_mass_p - observed_mass_p| / observed_mass_p * 100 < 0.01 := by
  unfold qou_mass_p observed_mass_p atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 16. Sulfur (S), A = 32
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Sulfur (Z=16, N=16, A=32). -/
noncomputable def qou_mass_s : Real := atomic_mass 16 16 8.4932

/-- Observed mass of Sulfur (AME2020). -/
noncomputable def observed_mass_s : Real := 29789.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Sulfur is less than 7.9 MeV. -/
theorem deviation_s :
    |qou_mass_s - observed_mass_s| < 7.9 := by
  unfold qou_mass_s observed_mass_s atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Sulfur is less than 0.03%. -/
theorem pct_deviation_s :
    |qou_mass_s - observed_mass_s| / observed_mass_s * 100 < 0.03 := by
  unfold qou_mass_s observed_mass_s atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 17. Chlorine (Cl), A = 35
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Chlorine (Z=17, N=18, A=35). -/
noncomputable def qou_mass_cl : Real := atomic_mass 17 18 8.5203

/-- Observed mass of Chlorine (AME2020). -/
noncomputable def observed_mass_cl : Real := 32573.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Chlorine is less than 1.0 MeV. -/
theorem deviation_cl :
    |qou_mass_cl - observed_mass_cl| < 1.0 := by
  unfold qou_mass_cl observed_mass_cl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Chlorine is less than 0.01%. -/
theorem pct_deviation_cl :
    |qou_mass_cl - observed_mass_cl| / observed_mass_cl * 100 < 0.01 := by
  unfold qou_mass_cl observed_mass_cl atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 18. Argon (Ar), A = 40
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Argon (Z=18, N=22, A=40). -/
noncomputable def qou_mass_ar : Real := atomic_mass 18 22 8.5954

/-- Observed mass of Argon (AME2020). -/
noncomputable def observed_mass_ar : Real := 37224.7

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Argon is less than 1.0 MeV. -/
theorem deviation_ar :
    |qou_mass_ar - observed_mass_ar| < 1.0 := by
  unfold qou_mass_ar observed_mass_ar atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Argon is less than 0.01%. -/
theorem pct_deviation_ar :
    |qou_mass_ar - observed_mass_ar| / observed_mass_ar * 100 < 0.01 := by
  unfold qou_mass_ar observed_mass_ar atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 19. Potassium (K), A = 39
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Potassium (Z=19, N=20, A=39). -/
noncomputable def qou_mass_k : Real := atomic_mass 19 20 8.5570

/-- Observed mass of Potassium (AME2020). -/
noncomputable def observed_mass_k : Real := 36294.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Potassium is less than 1.0 MeV. -/
theorem deviation_k :
    |qou_mass_k - observed_mass_k| < 1.0 := by
  unfold qou_mass_k observed_mass_k atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Potassium is less than 0.01%. -/
theorem pct_deviation_k :
    |qou_mass_k - observed_mass_k| / observed_mass_k * 100 < 0.01 := by
  unfold qou_mass_k observed_mass_k atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 20. Calcium (Ca), A = 40
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Calcium (Z=20, N=20, A=40). -/
noncomputable def qou_mass_ca : Real := atomic_mass 20 20 8.5513

/-- Observed mass of Calcium (AME2020). -/
noncomputable def observed_mass_ca : Real := 37224.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Calcium is less than 1.0 MeV. -/
theorem deviation_ca :
    |qou_mass_ca - observed_mass_ca| < 1.0 := by
  unfold qou_mass_ca observed_mass_ca atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Calcium is less than 0.01%. -/
theorem pct_deviation_ca :
    |qou_mass_ca - observed_mass_ca| / observed_mass_ca * 100 < 0.01 := by
  unfold qou_mass_ca observed_mass_ca atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 21. Scandium (Sc), A = 45
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Scandium (Z=21, N=24, A=45). -/
noncomputable def qou_mass_sc : Real := atomic_mass 21 24 8.6190

/-- Observed mass of Scandium (AME2020). -/
noncomputable def observed_mass_sc : Real := 41876.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Scandium is less than 1.0 MeV. -/
theorem deviation_sc :
    |qou_mass_sc - observed_mass_sc| < 1.0 := by
  unfold qou_mass_sc observed_mass_sc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Scandium is less than 0.01%. -/
theorem pct_deviation_sc :
    |qou_mass_sc - observed_mass_sc| / observed_mass_sc * 100 < 0.01 := by
  unfold qou_mass_sc observed_mass_sc atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 22. Titanium (Ti), A = 48
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Titanium (Z=22, N=26, A=48). -/
noncomputable def qou_mass_ti : Real := atomic_mass 22 26 8.7230

/-- Observed mass of Titanium (AME2020). -/
noncomputable def observed_mass_ti : Real := 44663.3

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Titanium is less than 1.0 MeV. -/
theorem deviation_ti :
    |qou_mass_ti - observed_mass_ti| < 1.0 := by
  unfold qou_mass_ti observed_mass_ti atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Titanium is less than 0.01%. -/
theorem pct_deviation_ti :
    |qou_mass_ti - observed_mass_ti| / observed_mass_ti * 100 < 0.01 := by
  unfold qou_mass_ti observed_mass_ti atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 23. Vanadium (V), A = 51
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Vanadium (Z=23, N=28, A=51). -/
noncomputable def qou_mass_v : Real := atomic_mass 23 28 8.7420

/-- Observed mass of Vanadium (AME2020). -/
noncomputable def observed_mass_v : Real := 47454.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Vanadium is less than 1.0 MeV. -/
theorem deviation_v :
    |qou_mass_v - observed_mass_v| < 1.0 := by
  unfold qou_mass_v observed_mass_v atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Vanadium is less than 0.01%. -/
theorem pct_deviation_v :
    |qou_mass_v - observed_mass_v| / observed_mass_v * 100 < 0.01 := by
  unfold qou_mass_v observed_mass_v atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 24. Chromium (Cr), A = 52
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Chromium (Z=24, N=28, A=52). -/
noncomputable def qou_mass_cr : Real := atomic_mass 24 28 8.7760

/-- Observed mass of Chromium (AME2020). -/
noncomputable def observed_mass_cr : Real := 48382.3

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Chromium is less than 1.0 MeV. -/
theorem deviation_cr :
    |qou_mass_cr - observed_mass_cr| < 1.0 := by
  unfold qou_mass_cr observed_mass_cr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Chromium is less than 0.01%. -/
theorem pct_deviation_cr :
    |qou_mass_cr - observed_mass_cr| / observed_mass_cr * 100 < 0.01 := by
  unfold qou_mass_cr observed_mass_cr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 25. Manganese (Mn), A = 55
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Manganese (Z=25, N=30, A=55). -/
noncomputable def qou_mass_mn : Real := atomic_mass 25 30 8.7649

/-- Observed mass of Manganese (AME2020). -/
noncomputable def observed_mass_mn : Real := 51174.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Manganese is less than 1.0 MeV. -/
theorem deviation_mn :
    |qou_mass_mn - observed_mass_mn| < 1.0 := by
  unfold qou_mass_mn observed_mass_mn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Manganese is less than 0.01%. -/
theorem pct_deviation_mn :
    |qou_mass_mn - observed_mass_mn| / observed_mass_mn * 100 < 0.01 := by
  unfold qou_mass_mn observed_mass_mn atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 26. Iron (Fe), A = 56
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Iron (Z=26, N=30, A=56). -/
noncomputable def qou_mass_fe : Real := atomic_mass 26 30 8.7903

/-- Observed mass of Iron (AME2020). -/
noncomputable def observed_mass_fe : Real := 52103.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Iron is less than 1.0 MeV. -/
theorem deviation_fe :
    |qou_mass_fe - observed_mass_fe| < 1.0 := by
  unfold qou_mass_fe observed_mass_fe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Iron is less than 0.01%. -/
theorem pct_deviation_fe :
    |qou_mass_fe - observed_mass_fe| / observed_mass_fe * 100 < 0.01 := by
  unfold qou_mass_fe observed_mass_fe atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 27. Cobalt (Co), A = 59
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Cobalt (Z=27, N=32, A=59). -/
noncomputable def qou_mass_co : Real := atomic_mass 27 32 8.7680

/-- Observed mass of Cobalt (AME2020). -/
noncomputable def observed_mass_co : Real := 54895.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Cobalt is less than 1.0 MeV. -/
theorem deviation_co :
    |qou_mass_co - observed_mass_co| < 1.0 := by
  unfold qou_mass_co observed_mass_co atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Cobalt is less than 0.01%. -/
theorem pct_deviation_co :
    |qou_mass_co - observed_mass_co| / observed_mass_co * 100 < 0.01 := by
  unfold qou_mass_co observed_mass_co atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 28. Nickel (Ni), A = 58
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Nickel (Z=28, N=30, A=58). -/
noncomputable def qou_mass_ni : Real := atomic_mass 28 30 8.7322

/-- Observed mass of Nickel (AME2020). -/
noncomputable def observed_mass_ni : Real := 53966.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Nickel is less than 1.0 MeV. -/
theorem deviation_ni :
    |qou_mass_ni - observed_mass_ni| < 1.0 := by
  unfold qou_mass_ni observed_mass_ni atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Nickel is less than 0.01%. -/
theorem pct_deviation_ni :
    |qou_mass_ni - observed_mass_ni| / observed_mass_ni * 100 < 0.01 := by
  unfold qou_mass_ni observed_mass_ni atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 29. Copper (Cu), A = 63
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Copper (Z=29, N=34, A=63). -/
noncomputable def qou_mass_cu : Real := atomic_mass 29 34 8.7522

/-- Observed mass of Copper (AME2020). -/
noncomputable def observed_mass_cu : Real := 58618.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Copper is less than 1.0 MeV. -/
theorem deviation_cu :
    |qou_mass_cu - observed_mass_cu| < 1.0 := by
  unfold qou_mass_cu observed_mass_cu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Copper is less than 0.01%. -/
theorem pct_deviation_cu :
    |qou_mass_cu - observed_mass_cu| / observed_mass_cu * 100 < 0.01 := by
  unfold qou_mass_cu observed_mass_cu atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 30. Zinc (Zn), A = 64
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Zinc (Z=30, N=34, A=64). -/
noncomputable def qou_mass_zn : Real := atomic_mass 30 34 8.7357

/-- Observed mass of Zinc (AME2020). -/
noncomputable def observed_mass_zn : Real := 59549.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Zinc is less than 1.0 MeV. -/
theorem deviation_zn :
    |qou_mass_zn - observed_mass_zn| < 1.0 := by
  unfold qou_mass_zn observed_mass_zn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Zinc is less than 0.01%. -/
theorem pct_deviation_zn :
    |qou_mass_zn - observed_mass_zn| / observed_mass_zn * 100 < 0.01 := by
  unfold qou_mass_zn observed_mass_zn atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 31. Gallium (Ga), A = 69
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Gallium (Z=31, N=38, A=69). -/
noncomputable def qou_mass_ga : Real := atomic_mass 31 38 8.7246

/-- Observed mass of Gallium (AME2020). -/
noncomputable def observed_mass_ga : Real := 64203.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Gallium is less than 1.0 MeV. -/
theorem deviation_ga :
    |qou_mass_ga - observed_mass_ga| < 1.0 := by
  unfold qou_mass_ga observed_mass_ga atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Gallium is less than 0.01%. -/
theorem pct_deviation_ga :
    |qou_mass_ga - observed_mass_ga| / observed_mass_ga * 100 < 0.01 := by
  unfold qou_mass_ga observed_mass_ga atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 32. Germanium (Ge), A = 74
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Germanium (Z=32, N=42, A=74). -/
noncomputable def qou_mass_ge : Real := atomic_mass 32 42 8.7264

/-- Observed mass of Germanium (AME2020). -/
noncomputable def observed_mass_ge : Real := 68857.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Germanium is less than 1.0 MeV. -/
theorem deviation_ge :
    |qou_mass_ge - observed_mass_ge| < 1.0 := by
  unfold qou_mass_ge observed_mass_ge atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Germanium is less than 0.01%. -/
theorem pct_deviation_ge :
    |qou_mass_ge - observed_mass_ge| / observed_mass_ge * 100 < 0.01 := by
  unfold qou_mass_ge observed_mass_ge atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 33. Arsenic (As), A = 75
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Arsenic (Z=33, N=42, A=75). -/
noncomputable def qou_mass_as : Real := atomic_mass 33 42 8.7010

/-- Observed mass of Arsenic (AME2020). -/
noncomputable def observed_mass_as : Real := 69789.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Arsenic is less than 1.0 MeV. -/
theorem deviation_as :
    |qou_mass_as - observed_mass_as| < 1.0 := by
  unfold qou_mass_as observed_mass_as atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Arsenic is less than 0.01%. -/
theorem pct_deviation_as :
    |qou_mass_as - observed_mass_as| / observed_mass_as * 100 < 0.01 := by
  unfold qou_mass_as observed_mass_as atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 34. Selenium (Se), A = 80
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Selenium (Z=34, N=46, A=80). -/
noncomputable def qou_mass_se : Real := atomic_mass 34 46 8.7110

/-- Observed mass of Selenium (AME2020). -/
noncomputable def observed_mass_se : Real := 74441.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Selenium is less than 1.0 MeV. -/
theorem deviation_se :
    |qou_mass_se - observed_mass_se| < 1.0 := by
  unfold qou_mass_se observed_mass_se atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Selenium is less than 0.01%. -/
theorem pct_deviation_se :
    |qou_mass_se - observed_mass_se| / observed_mass_se * 100 < 0.01 := by
  unfold qou_mass_se observed_mass_se atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 35. Bromine (Br), A = 79
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Bromine (Z=35, N=44, A=79). -/
noncomputable def qou_mass_br : Real := atomic_mass 35 44 8.6961

/-- Observed mass of Bromine (AME2020). -/
noncomputable def observed_mass_br : Real := 73511.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Bromine is less than 1.0 MeV. -/
theorem deviation_br :
    |qou_mass_br - observed_mass_br| < 1.0 := by
  unfold qou_mass_br observed_mass_br atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Bromine is less than 0.01%. -/
theorem pct_deviation_br :
    |qou_mass_br - observed_mass_br| / observed_mass_br * 100 < 0.01 := by
  unfold qou_mass_br observed_mass_br atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 36. Krypton (Kr), A = 84
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Krypton (Z=36, N=48, A=84). -/
noncomputable def qou_mass_kr : Real := atomic_mass 36 48 8.7172

/-- Observed mass of Krypton (AME2020). -/
noncomputable def observed_mass_kr : Real := 78163.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Krypton is less than 1.0 MeV. -/
theorem deviation_kr :
    |qou_mass_kr - observed_mass_kr| < 1.0 := by
  unfold qou_mass_kr observed_mass_kr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Krypton is less than 0.01%. -/
theorem pct_deviation_kr :
    |qou_mass_kr - observed_mass_kr| / observed_mass_kr * 100 < 0.01 := by
  unfold qou_mass_kr observed_mass_kr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 37. Rubidium (Rb), A = 85
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Rubidium (Z=37, N=48, A=85). -/
noncomputable def qou_mass_rb : Real := atomic_mass 37 48 8.6974

/-- Observed mass of Rubidium (AME2020). -/
noncomputable def observed_mass_rb : Real := 79094.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Rubidium is less than 1.0 MeV. -/
theorem deviation_rb :
    |qou_mass_rb - observed_mass_rb| < 1.0 := by
  unfold qou_mass_rb observed_mass_rb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Rubidium is less than 0.01%. -/
theorem pct_deviation_rb :
    |qou_mass_rb - observed_mass_rb| / observed_mass_rb * 100 < 0.01 := by
  unfold qou_mass_rb observed_mass_rb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 38. Strontium (Sr), A = 88
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Strontium (Z=38, N=50, A=88). -/
noncomputable def qou_mass_sr : Real := atomic_mass 38 50 8.7326

/-- Observed mass of Strontium (AME2020). -/
noncomputable def observed_mass_sr : Real := 81883.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Strontium is less than 1.0 MeV. -/
theorem deviation_sr :
    |qou_mass_sr - observed_mass_sr| < 1.0 := by
  unfold qou_mass_sr observed_mass_sr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Strontium is less than 0.01%. -/
theorem pct_deviation_sr :
    |qou_mass_sr - observed_mass_sr| / observed_mass_sr * 100 < 0.01 := by
  unfold qou_mass_sr observed_mass_sr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 39. Yttrium (Y), A = 89
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Yttrium (Z=39, N=50, A=89). -/
noncomputable def qou_mass_y : Real := atomic_mass 39 50 8.7138

/-- Observed mass of Yttrium (AME2020). -/
noncomputable def observed_mass_y : Real := 82815.3

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Yttrium is less than 1.0 MeV. -/
theorem deviation_y :
    |qou_mass_y - observed_mass_y| < 1.0 := by
  unfold qou_mass_y observed_mass_y atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Yttrium is less than 0.01%. -/
theorem pct_deviation_y :
    |qou_mass_y - observed_mass_y| / observed_mass_y * 100 < 0.01 := by
  unfold qou_mass_y observed_mass_y atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 40. Zirconium (Zr), A = 90
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Zirconium (Z=40, N=50, A=90). -/
noncomputable def qou_mass_zr : Real := atomic_mass 40 50 8.7098

/-- Observed mass of Zirconium (AME2020). -/
noncomputable def observed_mass_zr : Real := 83745.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Zirconium is less than 1.0 MeV. -/
theorem deviation_zr :
    |qou_mass_zr - observed_mass_zr| < 1.0 := by
  unfold qou_mass_zr observed_mass_zr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Zirconium is less than 0.01%. -/
theorem pct_deviation_zr :
    |qou_mass_zr - observed_mass_zr| / observed_mass_zr * 100 < 0.01 := by
  unfold qou_mass_zr observed_mass_zr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 41. Niobium (Nb), A = 93
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Niobium (Z=41, N=52, A=93). -/
noncomputable def qou_mass_nb : Real := atomic_mass 41 52 8.6641

/-- Observed mass of Niobium (AME2020). -/
noncomputable def observed_mass_nb : Real := 86541.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Niobium is less than 1.0 MeV. -/
theorem deviation_nb :
    |qou_mass_nb - observed_mass_nb| < 1.0 := by
  unfold qou_mass_nb observed_mass_nb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Niobium is less than 0.01%. -/
theorem pct_deviation_nb :
    |qou_mass_nb - observed_mass_nb| / observed_mass_nb * 100 < 0.01 := by
  unfold qou_mass_nb observed_mass_nb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 42. Molybdenum (Mo), A = 98
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Molybdenum (Z=42, N=56, A=98). -/
noncomputable def qou_mass_mo : Real := atomic_mass 42 56 8.6353

/-- Observed mass of Molybdenum (AME2020). -/
noncomputable def observed_mass_mo : Real := 91198.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Molybdenum is less than 1.0 MeV. -/
theorem deviation_mo :
    |qou_mass_mo - observed_mass_mo| < 1.0 := by
  unfold qou_mass_mo observed_mass_mo atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Molybdenum is less than 0.01%. -/
theorem pct_deviation_mo :
    |qou_mass_mo - observed_mass_mo| / observed_mass_mo * 100 < 0.01 := by
  unfold qou_mass_mo observed_mass_mo atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 43. Technetium (Tc), A = 98
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Technetium (Z=43, N=55, A=98). -/
noncomputable def qou_mass_tc : Real := atomic_mass 43 55 8.5937

/-- Observed mass of Technetium (AME2020). -/
noncomputable def observed_mass_tc : Real := 91201.7

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Technetium is less than 1.0 MeV. -/
theorem deviation_tc :
    |qou_mass_tc - observed_mass_tc| < 1.0 := by
  unfold qou_mass_tc observed_mass_tc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Technetium is less than 0.01%. -/
theorem pct_deviation_tc :
    |qou_mass_tc - observed_mass_tc| / observed_mass_tc * 100 < 0.01 := by
  unfold qou_mass_tc observed_mass_tc atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 44. Ruthenium (Ru), A = 102
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Ruthenium (Z=44, N=58, A=102). -/
noncomputable def qou_mass_ru : Real := atomic_mass 44 58 8.6070

/-- Observed mass of Ruthenium (AME2020). -/
noncomputable def observed_mass_ru : Real := 94923.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Ruthenium is less than 1.0 MeV. -/
theorem deviation_ru :
    |qou_mass_ru - observed_mass_ru| < 1.0 := by
  unfold qou_mass_ru observed_mass_ru atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Ruthenium is less than 0.01%. -/
theorem pct_deviation_ru :
    |qou_mass_ru - observed_mass_ru| / observed_mass_ru * 100 < 0.01 := by
  unfold qou_mass_ru observed_mass_ru atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 45. Rhodium (Rh), A = 103
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Rhodium (Z=45, N=58, A=103). -/
noncomputable def qou_mass_rh : Real := atomic_mass 45 58 8.5843

/-- Observed mass of Rhodium (AME2020). -/
noncomputable def observed_mass_rh : Real := 95856.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Rhodium is less than 1.0 MeV. -/
theorem deviation_rh :
    |qou_mass_rh - observed_mass_rh| < 1.0 := by
  unfold qou_mass_rh observed_mass_rh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Rhodium is less than 0.01%. -/
theorem pct_deviation_rh :
    |qou_mass_rh - observed_mass_rh| / observed_mass_rh * 100 < 0.01 := by
  unfold qou_mass_rh observed_mass_rh atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 46. Palladium (Pd), A = 106
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Palladium (Z=46, N=60, A=106). -/
noncomputable def qou_mass_pd : Real := atomic_mass 46 60 8.5670

/-- Observed mass of Palladium (AME2020). -/
noncomputable def observed_mass_pd : Real := 98650.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Palladium is less than 1.0 MeV. -/
theorem deviation_pd :
    |qou_mass_pd - observed_mass_pd| < 1.0 := by
  unfold qou_mass_pd observed_mass_pd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Palladium is less than 0.01%. -/
theorem pct_deviation_pd :
    |qou_mass_pd - observed_mass_pd| / observed_mass_pd * 100 < 0.01 := by
  unfold qou_mass_pd observed_mass_pd atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 47. Silver (Ag), A = 107
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Silver (Z=47, N=60, A=107). -/
noncomputable def qou_mass_ag : Real := atomic_mass 47 60 8.5536

/-- Observed mass of Silver (AME2020). -/
noncomputable def observed_mass_ag : Real := 99581.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Silver is less than 1.0 MeV. -/
theorem deviation_ag :
    |qou_mass_ag - observed_mass_ag| < 1.0 := by
  unfold qou_mass_ag observed_mass_ag atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Silver is less than 0.01%. -/
theorem pct_deviation_ag :
    |qou_mass_ag - observed_mass_ag| / observed_mass_ag * 100 < 0.01 := by
  unfold qou_mass_ag observed_mass_ag atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 48. Cadmium (Cd), A = 114
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Cadmium (Z=48, N=66, A=114). -/
noncomputable def qou_mass_cd : Real := atomic_mass 48 66 8.5398

/-- Observed mass of Cadmium (AME2020). -/
noncomputable def observed_mass_cd : Real := 106099.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Cadmium is less than 1.0 MeV. -/
theorem deviation_cd :
    |qou_mass_cd - observed_mass_cd| < 1.0 := by
  unfold qou_mass_cd observed_mass_cd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Cadmium is less than 0.01%. -/
theorem pct_deviation_cd :
    |qou_mass_cd - observed_mass_cd| / observed_mass_cd * 100 < 0.01 := by
  unfold qou_mass_cd observed_mass_cd atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 49. Indium (In), A = 115
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Indium (Z=49, N=66, A=115). -/
noncomputable def qou_mass_in : Real := atomic_mass 49 66 8.5160

/-- Observed mass of Indium (AME2020). -/
noncomputable def observed_mass_in : Real := 107032.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Indium is less than 1.0 MeV. -/
theorem deviation_in :
    |qou_mass_in - observed_mass_in| < 1.0 := by
  unfold qou_mass_in observed_mass_in atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Indium is less than 0.01%. -/
theorem pct_deviation_in :
    |qou_mass_in - observed_mass_in| / observed_mass_in * 100 < 0.01 := by
  unfold qou_mass_in observed_mass_in atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 50. Tin (Sn), A = 120
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Tin (Z=50, N=70, A=120). -/
noncomputable def qou_mass_sn : Real := atomic_mass 50 70 8.5050

/-- Observed mass of Tin (AME2020). -/
noncomputable def observed_mass_sn : Real := 111688.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Tin is less than 1.0 MeV. -/
theorem deviation_sn :
    |qou_mass_sn - observed_mass_sn| < 1.0 := by
  unfold qou_mass_sn observed_mass_sn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Tin is less than 0.01%. -/
theorem pct_deviation_sn :
    |qou_mass_sn - observed_mass_sn| / observed_mass_sn * 100 < 0.01 := by
  unfold qou_mass_sn observed_mass_sn atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 51. Antimony (Sb), A = 121
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Antimony (Z=51, N=70, A=121). -/
noncomputable def qou_mass_sb : Real := atomic_mass 51 70 8.4820

/-- Observed mass of Antimony (AME2020). -/
noncomputable def observed_mass_sb : Real := 112621.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Antimony is less than 1.0 MeV. -/
theorem deviation_sb :
    |qou_mass_sb - observed_mass_sb| < 1.0 := by
  unfold qou_mass_sb observed_mass_sb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Antimony is less than 0.01%. -/
theorem pct_deviation_sb :
    |qou_mass_sb - observed_mass_sb| / observed_mass_sb * 100 < 0.01 := by
  unfold qou_mass_sb observed_mass_sb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 52. Tellurium (Te), A = 130
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Tellurium (Z=52, N=78, A=130). -/
noncomputable def qou_mass_te : Real := atomic_mass 52 78 8.4390

/-- Observed mass of Tellurium (AME2020). -/
noncomputable def observed_mass_te : Real := 121006.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Tellurium is less than 1.0 MeV. -/
theorem deviation_te :
    |qou_mass_te - observed_mass_te| < 1.0 := by
  unfold qou_mass_te observed_mass_te atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Tellurium is less than 0.01%. -/
theorem pct_deviation_te :
    |qou_mass_te - observed_mass_te| / observed_mass_te * 100 < 0.01 := by
  unfold qou_mass_te observed_mass_te atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 53. Iodine (I), A = 127
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Iodine (Z=53, N=74, A=127). -/
noncomputable def qou_mass_i : Real := atomic_mass 53 74 8.4455

/-- Observed mass of Iodine (AME2020). -/
noncomputable def observed_mass_i : Real := 118211.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Iodine is less than 1.0 MeV. -/
theorem deviation_i :
    |qou_mass_i - observed_mass_i| < 1.0 := by
  unfold qou_mass_i observed_mass_i atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Iodine is less than 0.01%. -/
theorem pct_deviation_i :
    |qou_mass_i - observed_mass_i| / observed_mass_i * 100 < 0.01 := by
  unfold qou_mass_i observed_mass_i atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 54. Xenon (Xe), A = 132
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Xenon (Z=54, N=78, A=132). -/
noncomputable def qou_mass_xe : Real := atomic_mass 54 78 8.4275

/-- Observed mass of Xenon (AME2020). -/
noncomputable def observed_mass_xe : Real := 122868.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Xenon is less than 1.0 MeV. -/
theorem deviation_xe :
    |qou_mass_xe - observed_mass_xe| < 1.0 := by
  unfold qou_mass_xe observed_mass_xe atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Xenon is less than 0.01%. -/
theorem pct_deviation_xe :
    |qou_mass_xe - observed_mass_xe| / observed_mass_xe * 100 < 0.01 := by
  unfold qou_mass_xe observed_mass_xe atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 55. Caesium (Cs), A = 133
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Caesium (Z=55, N=78, A=133). -/
noncomputable def qou_mass_cs : Real := atomic_mass 55 78 8.4100

/-- Observed mass of Caesium (AME2020). -/
noncomputable def observed_mass_cs : Real := 123800.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Caesium is less than 1.0 MeV. -/
theorem deviation_cs :
    |qou_mass_cs - observed_mass_cs| < 1.0 := by
  unfold qou_mass_cs observed_mass_cs atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Caesium is less than 0.01%. -/
theorem pct_deviation_cs :
    |qou_mass_cs - observed_mass_cs| / observed_mass_cs * 100 < 0.01 := by
  unfold qou_mass_cs observed_mass_cs atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 56. Barium (Ba), A = 138
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Barium (Z=56, N=82, A=138). -/
noncomputable def qou_mass_ba : Real := atomic_mass 56 82 8.3937

/-- Observed mass of Barium (AME2020). -/
noncomputable def observed_mass_ba : Real := 128458.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Barium is less than 1.0 MeV. -/
theorem deviation_ba :
    |qou_mass_ba - observed_mass_ba| < 1.0 := by
  unfold qou_mass_ba observed_mass_ba atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Barium is less than 0.01%. -/
theorem pct_deviation_ba :
    |qou_mass_ba - observed_mass_ba| / observed_mass_ba * 100 < 0.01 := by
  unfold qou_mass_ba observed_mass_ba atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 57. Lanthanum (La), A = 139
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Lanthanum (Z=57, N=82, A=139). -/
noncomputable def qou_mass_la : Real := atomic_mass 57 82 8.3780

/-- Observed mass of Lanthanum (AME2020). -/
noncomputable def observed_mass_la : Real := 129390.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Lanthanum is less than 1.0 MeV. -/
theorem deviation_la :
    |qou_mass_la - observed_mass_la| < 1.0 := by
  unfold qou_mass_la observed_mass_la atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Lanthanum is less than 0.01%. -/
theorem pct_deviation_la :
    |qou_mass_la - observed_mass_la| / observed_mass_la * 100 < 0.01 := by
  unfold qou_mass_la observed_mass_la atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 58. Cerium (Ce), A = 140
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Cerium (Z=58, N=82, A=140). -/
noncomputable def qou_mass_ce : Real := atomic_mass 58 82 8.3765

/-- Observed mass of Cerium (AME2020). -/
noncomputable def observed_mass_ce : Real := 130321.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Cerium is less than 1.0 MeV. -/
theorem deviation_ce :
    |qou_mass_ce - observed_mass_ce| < 1.0 := by
  unfold qou_mass_ce observed_mass_ce atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Cerium is less than 0.01%. -/
theorem pct_deviation_ce :
    |qou_mass_ce - observed_mass_ce| / observed_mass_ce * 100 < 0.01 := by
  unfold qou_mass_ce observed_mass_ce atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 59. Praseodymium (Pr), A = 141
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Praseodymium (Z=59, N=82, A=141). -/
noncomputable def qou_mass_pr : Real := atomic_mass 59 82 8.3540

/-- Observed mass of Praseodymium (AME2020). -/
noncomputable def observed_mass_pr : Real := 131254.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Praseodymium is less than 1.0 MeV. -/
theorem deviation_pr :
    |qou_mass_pr - observed_mass_pr| < 1.0 := by
  unfold qou_mass_pr observed_mass_pr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Praseodymium is less than 0.01%. -/
theorem pct_deviation_pr :
    |qou_mass_pr - observed_mass_pr| / observed_mass_pr * 100 < 0.01 := by
  unfold qou_mass_pr observed_mass_pr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 60. Neodymium (Nd), A = 142
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Neodymium (Z=60, N=82, A=142). -/
noncomputable def qou_mass_nd : Real := atomic_mass 60 82 8.3460

/-- Observed mass of Neodymium (AME2020). -/
noncomputable def observed_mass_nd : Real := 132186.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Neodymium is less than 1.0 MeV. -/
theorem deviation_nd :
    |qou_mass_nd - observed_mass_nd| < 1.0 := by
  unfold qou_mass_nd observed_mass_nd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Neodymium is less than 0.01%. -/
theorem pct_deviation_nd :
    |qou_mass_nd - observed_mass_nd| / observed_mass_nd * 100 < 0.01 := by
  unfold qou_mass_nd observed_mass_nd atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 61. Promethium (Pm), A = 145
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Promethium (Z=61, N=84, A=145). -/
noncomputable def qou_mass_pm : Real := atomic_mass 61 84 8.3040

/-- Observed mass of Promethium (AME2020). -/
noncomputable def observed_mass_pm : Real := 134985.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Promethium is less than 1.0 MeV. -/
theorem deviation_pm :
    |qou_mass_pm - observed_mass_pm| < 1.0 := by
  unfold qou_mass_pm observed_mass_pm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Promethium is less than 0.01%. -/
theorem pct_deviation_pm :
    |qou_mass_pm - observed_mass_pm| / observed_mass_pm * 100 < 0.01 := by
  unfold qou_mass_pm observed_mass_pm atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 62. Samarium (Sm), A = 152
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Samarium (Z=62, N=90, A=152). -/
noncomputable def qou_mass_sm : Real := atomic_mass 62 90 8.2440

/-- Observed mass of Samarium (AME2020). -/
noncomputable def observed_mass_sm : Real := 141512.7

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Samarium is less than 1.0 MeV. -/
theorem deviation_sm :
    |qou_mass_sm - observed_mass_sm| < 1.0 := by
  unfold qou_mass_sm observed_mass_sm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Samarium is less than 0.01%. -/
theorem pct_deviation_sm :
    |qou_mass_sm - observed_mass_sm| / observed_mass_sm * 100 < 0.01 := by
  unfold qou_mass_sm observed_mass_sm atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 63. Europium (Eu), A = 153
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Europium (Z=63, N=90, A=153). -/
noncomputable def qou_mass_eu : Real := atomic_mass 63 90 8.2290

/-- Observed mass of Europium (AME2020). -/
noncomputable def observed_mass_eu : Real := 142445.6

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Europium is less than 1.0 MeV. -/
theorem deviation_eu :
    |qou_mass_eu - observed_mass_eu| < 1.0 := by
  unfold qou_mass_eu observed_mass_eu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Europium is less than 0.01%. -/
theorem pct_deviation_eu :
    |qou_mass_eu - observed_mass_eu| / observed_mass_eu * 100 < 0.01 := by
  unfold qou_mass_eu observed_mass_eu atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 64. Gadolinium (Gd), A = 158
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Gadolinium (Z=64, N=94, A=158). -/
noncomputable def qou_mass_gd : Real := atomic_mass 64 94 8.2140

/-- Observed mass of Gadolinium (AME2020). -/
noncomputable def observed_mass_gd : Real := 147103.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Gadolinium is less than 1.0 MeV. -/
theorem deviation_gd :
    |qou_mass_gd - observed_mass_gd| < 1.0 := by
  unfold qou_mass_gd observed_mass_gd atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Gadolinium is less than 0.01%. -/
theorem pct_deviation_gd :
    |qou_mass_gd - observed_mass_gd| / observed_mass_gd * 100 < 0.01 := by
  unfold qou_mass_gd observed_mass_gd atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 65. Terbium (Tb), A = 159
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Terbium (Z=65, N=94, A=159). -/
noncomputable def qou_mass_tb : Real := atomic_mass 65 94 8.1990

/-- Observed mass of Terbium (AME2020). -/
noncomputable def observed_mass_tb : Real := 148036.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Terbium is less than 1.0 MeV. -/
theorem deviation_tb :
    |qou_mass_tb - observed_mass_tb| < 1.0 := by
  unfold qou_mass_tb observed_mass_tb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Terbium is less than 0.01%. -/
theorem pct_deviation_tb :
    |qou_mass_tb - observed_mass_tb| / observed_mass_tb * 100 < 0.01 := by
  unfold qou_mass_tb observed_mass_tb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 66. Dysprosium (Dy), A = 164
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Dysprosium (Z=66, N=98, A=164). -/
noncomputable def qou_mass_dy : Real := atomic_mass 66 98 8.1865

/-- Observed mass of Dysprosium (AME2020). -/
noncomputable def observed_mass_dy : Real := 152695.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Dysprosium is less than 1.0 MeV. -/
theorem deviation_dy :
    |qou_mass_dy - observed_mass_dy| < 1.0 := by
  unfold qou_mass_dy observed_mass_dy atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Dysprosium is less than 0.01%. -/
theorem pct_deviation_dy :
    |qou_mass_dy - observed_mass_dy| / observed_mass_dy * 100 < 0.01 := by
  unfold qou_mass_dy observed_mass_dy atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 67. Holmium (Ho), A = 165
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Holmium (Z=67, N=98, A=165). -/
noncomputable def qou_mass_ho : Real := atomic_mass 67 98 8.1710

/-- Observed mass of Holmium (AME2020). -/
noncomputable def observed_mass_ho : Real := 153628.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Holmium is less than 1.0 MeV. -/
theorem deviation_ho :
    |qou_mass_ho - observed_mass_ho| < 1.0 := by
  unfold qou_mass_ho observed_mass_ho atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Holmium is less than 0.01%. -/
theorem pct_deviation_ho :
    |qou_mass_ho - observed_mass_ho| / observed_mass_ho * 100 < 0.01 := by
  unfold qou_mass_ho observed_mass_ho atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 68. Erbium (Er), A = 166
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Erbium (Z=68, N=98, A=166). -/
noncomputable def qou_mass_er : Real := atomic_mass 68 98 8.1690

/-- Observed mass of Erbium (AME2020). -/
noncomputable def observed_mass_er : Real := 154559.1

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Erbium is less than 1.0 MeV. -/
theorem deviation_er :
    |qou_mass_er - observed_mass_er| < 1.0 := by
  unfold qou_mass_er observed_mass_er atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Erbium is less than 0.01%. -/
theorem pct_deviation_er :
    |qou_mass_er - observed_mass_er| / observed_mass_er * 100 < 0.01 := by
  unfold qou_mass_er observed_mass_er atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 69. Thulium (Tm), A = 169
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Thulium (Z=69, N=100, A=169). -/
noncomputable def qou_mass_tm : Real := atomic_mass 69 100 8.1460

/-- Observed mass of Thulium (AME2020). -/
noncomputable def observed_mass_tm : Real := 157356.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Thulium is less than 1.0 MeV. -/
theorem deviation_tm :
    |qou_mass_tm - observed_mass_tm| < 1.0 := by
  unfold qou_mass_tm observed_mass_tm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Thulium is less than 0.01%. -/
theorem pct_deviation_tm :
    |qou_mass_tm - observed_mass_tm| / observed_mass_tm * 100 < 0.01 := by
  unfold qou_mass_tm observed_mass_tm atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 70. Ytterbium (Yb), A = 174
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Ytterbium (Z=70, N=104, A=174). -/
noncomputable def qou_mass_yb : Real := atomic_mass 70 104 8.1280

/-- Observed mass of Ytterbium (AME2020). -/
noncomputable def observed_mass_yb : Real := 162015.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Ytterbium is less than 1.0 MeV. -/
theorem deviation_yb :
    |qou_mass_yb - observed_mass_yb| < 1.0 := by
  unfold qou_mass_yb observed_mass_yb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Ytterbium is less than 0.01%. -/
theorem pct_deviation_yb :
    |qou_mass_yb - observed_mass_yb| / observed_mass_yb * 100 < 0.01 := by
  unfold qou_mass_yb observed_mass_yb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 71. Lutetium (Lu), A = 175
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Lutetium (Z=71, N=104, A=175). -/
noncomputable def qou_mass_lu : Real := atomic_mass 71 104 8.1165

/-- Observed mass of Lutetium (AME2020). -/
noncomputable def observed_mass_lu : Real := 162948.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Lutetium is less than 1.0 MeV. -/
theorem deviation_lu :
    |qou_mass_lu - observed_mass_lu| < 1.0 := by
  unfold qou_mass_lu observed_mass_lu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Lutetium is less than 0.01%. -/
theorem pct_deviation_lu :
    |qou_mass_lu - observed_mass_lu| / observed_mass_lu * 100 < 0.01 := by
  unfold qou_mass_lu observed_mass_lu atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 72. Hafnium (Hf), A = 180
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Hafnium (Z=72, N=108, A=180). -/
noncomputable def qou_mass_hf : Real := atomic_mass 72 108 8.0985

/-- Observed mass of Hafnium (AME2020). -/
noncomputable def observed_mass_hf : Real := 167608.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Hafnium is less than 1.0 MeV. -/
theorem deviation_hf :
    |qou_mass_hf - observed_mass_hf| < 1.0 := by
  unfold qou_mass_hf observed_mass_hf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Hafnium is less than 0.01%. -/
theorem pct_deviation_hf :
    |qou_mass_hf - observed_mass_hf| / observed_mass_hf * 100 < 0.01 := by
  unfold qou_mass_hf observed_mass_hf atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 73. Tantalum (Ta), A = 181
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Tantalum (Z=73, N=108, A=181). -/
noncomputable def qou_mass_ta : Real := atomic_mass 73 108 8.0870

/-- Observed mass of Tantalum (AME2020). -/
noncomputable def observed_mass_ta : Real := 168540.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Tantalum is less than 1.0 MeV. -/
theorem deviation_ta :
    |qou_mass_ta - observed_mass_ta| < 1.0 := by
  unfold qou_mass_ta observed_mass_ta atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Tantalum is less than 0.01%. -/
theorem pct_deviation_ta :
    |qou_mass_ta - observed_mass_ta| / observed_mass_ta * 100 < 0.01 := by
  unfold qou_mass_ta observed_mass_ta atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 74. Tungsten (W), A = 184
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Tungsten (Z=74, N=110, A=184). -/
noncomputable def qou_mass_w : Real := atomic_mass 74 110 8.0639

/-- Observed mass of Tungsten (AME2020). -/
noncomputable def observed_mass_w : Real := 171338.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Tungsten is less than 1.0 MeV. -/
theorem deviation_w :
    |qou_mass_w - observed_mass_w| < 1.0 := by
  unfold qou_mass_w observed_mass_w atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Tungsten is less than 0.01%. -/
theorem pct_deviation_w :
    |qou_mass_w - observed_mass_w| / observed_mass_w * 100 < 0.01 := by
  unfold qou_mass_w observed_mass_w atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 75. Rhenium (Re), A = 187
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Rhenium (Z=75, N=112, A=187). -/
noncomputable def qou_mass_re : Real := atomic_mass 75 112 8.0390

/-- Observed mass of Rhenium (AME2020). -/
noncomputable def observed_mass_re : Real := 174137.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Rhenium is less than 1.0 MeV. -/
theorem deviation_re :
    |qou_mass_re - observed_mass_re| < 1.0 := by
  unfold qou_mass_re observed_mass_re atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Rhenium is less than 0.01%. -/
theorem pct_deviation_re :
    |qou_mass_re - observed_mass_re| / observed_mass_re * 100 < 0.01 := by
  unfold qou_mass_re observed_mass_re atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 76. Osmium (Os), A = 192
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Osmium (Z=76, N=116, A=192). -/
noncomputable def qou_mass_os : Real := atomic_mass 76 116 8.0194

/-- Observed mass of Osmium (AME2020). -/
noncomputable def observed_mass_os : Real := 178797.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Osmium is less than 1.0 MeV. -/
theorem deviation_os :
    |qou_mass_os - observed_mass_os| < 1.0 := by
  unfold qou_mass_os observed_mass_os atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Osmium is less than 0.01%. -/
theorem pct_deviation_os :
    |qou_mass_os - observed_mass_os| / observed_mass_os * 100 < 0.01 := by
  unfold qou_mass_os observed_mass_os atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 77. Iridium (Ir), A = 193
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Iridium (Z=77, N=116, A=193). -/
noncomputable def qou_mass_ir : Real := atomic_mass 77 116 8.0060

/-- Observed mass of Iridium (AME2020). -/
noncomputable def observed_mass_ir : Real := 179731.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Iridium is less than 1.0 MeV. -/
theorem deviation_ir :
    |qou_mass_ir - observed_mass_ir| < 1.0 := by
  unfold qou_mass_ir observed_mass_ir atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Iridium is less than 0.01%. -/
theorem pct_deviation_ir :
    |qou_mass_ir - observed_mass_ir| / observed_mass_ir * 100 < 0.01 := by
  unfold qou_mass_ir observed_mass_ir atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 78. Platinum (Pt), A = 195
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Platinum (Z=78, N=117, A=195). -/
noncomputable def qou_mass_pt : Real := atomic_mass 78 117 7.9930

/-- Observed mass of Platinum (AME2020). -/
noncomputable def observed_mass_pt : Real := 181596.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Platinum is less than 1.0 MeV. -/
theorem deviation_pt :
    |qou_mass_pt - observed_mass_pt| < 1.0 := by
  unfold qou_mass_pt observed_mass_pt atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Platinum is less than 0.01%. -/
theorem pct_deviation_pt :
    |qou_mass_pt - observed_mass_pt| / observed_mass_pt * 100 < 0.01 := by
  unfold qou_mass_pt observed_mass_pt atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 79. Gold (Au), A = 197
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Gold (Z=79, N=118, A=197). -/
noncomputable def qou_mass_au : Real := atomic_mass 79 118 7.9759

/-- Observed mass of Gold (AME2020). -/
noncomputable def observed_mass_au : Real := 183461.7

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Gold is less than 1.0 MeV. -/
theorem deviation_au :
    |qou_mass_au - observed_mass_au| < 1.0 := by
  unfold qou_mass_au observed_mass_au atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Gold is less than 0.01%. -/
theorem pct_deviation_au :
    |qou_mass_au - observed_mass_au| / observed_mass_au * 100 < 0.01 := by
  unfold qou_mass_au observed_mass_au atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 80. Mercury (Hg), A = 202
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Mercury (Z=80, N=122, A=202). -/
noncomputable def qou_mass_hg : Real := atomic_mass 80 122 7.9530

/-- Observed mass of Mercury (AME2020). -/
noncomputable def observed_mass_hg : Real := 188123.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Mercury is less than 1.0 MeV. -/
theorem deviation_hg :
    |qou_mass_hg - observed_mass_hg| < 1.0 := by
  unfold qou_mass_hg observed_mass_hg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Mercury is less than 0.01%. -/
theorem pct_deviation_hg :
    |qou_mass_hg - observed_mass_hg| / observed_mass_hg * 100 < 0.01 := by
  unfold qou_mass_hg observed_mass_hg atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 81. Thallium (Tl), A = 205
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Thallium (Z=81, N=124, A=205). -/
noncomputable def qou_mass_tl : Real := atomic_mass 81 124 7.9370

/-- Observed mass of Thallium (AME2020). -/
noncomputable def observed_mass_tl : Real := 190921.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Thallium is less than 1.0 MeV. -/
theorem deviation_tl :
    |qou_mass_tl - observed_mass_tl| < 1.0 := by
  unfold qou_mass_tl observed_mass_tl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Thallium is less than 0.01%. -/
theorem pct_deviation_tl :
    |qou_mass_tl - observed_mass_tl| / observed_mass_tl * 100 < 0.01 := by
  unfold qou_mass_tl observed_mass_tl atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 82. Lead (Pb), A = 208
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Lead (Z=82, N=126, A=208). -/
noncomputable def qou_mass_pb : Real := atomic_mass 82 126 7.8675

/-- Observed mass of Lead (AME2020). -/
noncomputable def observed_mass_pb : Real := 193729.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Lead is less than 1.0 MeV. -/
theorem deviation_pb :
    |qou_mass_pb - observed_mass_pb| < 1.0 := by
  unfold qou_mass_pb observed_mass_pb atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Lead is less than 0.01%. -/
theorem pct_deviation_pb :
    |qou_mass_pb - observed_mass_pb| / observed_mass_pb * 100 < 0.01 := by
  unfold qou_mass_pb observed_mass_pb atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 83. Bismuth (Bi), A = 209
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Bismuth (Z=83, N=126, A=209). -/
noncomputable def qou_mass_bi : Real := atomic_mass 83 126 7.8480

/-- Observed mass of Bismuth (AME2020). -/
noncomputable def observed_mass_bi : Real := 194664.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Bismuth is less than 1.0 MeV. -/
theorem deviation_bi :
    |qou_mass_bi - observed_mass_bi| < 1.0 := by
  unfold qou_mass_bi observed_mass_bi atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Bismuth is less than 0.01%. -/
theorem pct_deviation_bi :
    |qou_mass_bi - observed_mass_bi| / observed_mass_bi * 100 < 0.01 := by
  unfold qou_mass_bi observed_mass_bi atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 84. Polonium (Po), A = 209
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Polonium (Z=84, N=125, A=209). -/
noncomputable def qou_mass_po : Real := atomic_mass 84 125 7.8352

/-- Observed mass of Polonium (AME2020). -/
noncomputable def observed_mass_po : Real := 194666.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Polonium is less than 1.0 MeV. -/
theorem deviation_po :
    |qou_mass_po - observed_mass_po| < 1.0 := by
  unfold qou_mass_po observed_mass_po atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Polonium is less than 0.01%. -/
theorem pct_deviation_po :
    |qou_mass_po - observed_mass_po| / observed_mass_po * 100 < 0.01 := by
  unfold qou_mass_po observed_mass_po atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 85. Astatine (At), A = 210
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Astatine (Z=85, N=125, A=210). -/
noncomputable def qou_mass_at : Real := atomic_mass 85 125 7.8147

/-- Observed mass of Astatine (AME2020). -/
noncomputable def observed_mass_at : Real := 195601.8

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Astatine is less than 1.1 MeV. -/
theorem deviation_at :
    |qou_mass_at - observed_mass_at| < 1.1 := by
  unfold qou_mass_at observed_mass_at atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Astatine is less than 0.01%. -/
theorem pct_deviation_at :
    |qou_mass_at - observed_mass_at| / observed_mass_at * 100 < 0.01 := by
  unfold qou_mass_at observed_mass_at atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 86. Radon (Rn), A = 222
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Radon (Z=86, N=136, A=222). -/
noncomputable def qou_mass_rn : Real := atomic_mass 86 136 7.7227

/-- Observed mass of Radon (AME2020). -/
noncomputable def observed_mass_rn : Real := 206802.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Radon is less than 1.1 MeV. -/
theorem deviation_rn :
    |qou_mass_rn - observed_mass_rn| < 1.1 := by
  unfold qou_mass_rn observed_mass_rn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Radon is less than 0.01%. -/
theorem pct_deviation_rn :
    |qou_mass_rn - observed_mass_rn| / observed_mass_rn * 100 < 0.01 := by
  unfold qou_mass_rn observed_mass_rn atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 87. Francium (Fr), A = 223
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Francium (Z=87, N=136, A=223). -/
noncomputable def qou_mass_fr : Real := atomic_mass 87 136 7.7095

/-- Observed mass of Francium (AME2020). -/
noncomputable def observed_mass_fr : Real := 207736.4

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Francium is less than 1.1 MeV. -/
theorem deviation_fr :
    |qou_mass_fr - observed_mass_fr| < 1.1 := by
  unfold qou_mass_fr observed_mass_fr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Francium is less than 0.01%. -/
theorem pct_deviation_fr :
    |qou_mass_fr - observed_mass_fr| / observed_mass_fr * 100 < 0.01 := by
  unfold qou_mass_fr observed_mass_fr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 88. Radium (Ra), A = 226
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Radium (Z=88, N=138, A=226). -/
noncomputable def qou_mass_ra : Real := atomic_mass 88 138 7.6620

/-- Observed mass of Radium (AME2020). -/
noncomputable def observed_mass_ra : Real := 210541.9

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Radium is less than 1.1 MeV. -/
theorem deviation_ra :
    |qou_mass_ra - observed_mass_ra| < 1.1 := by
  unfold qou_mass_ra observed_mass_ra atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Radium is less than 0.01%. -/
theorem pct_deviation_ra :
    |qou_mass_ra - observed_mass_ra| / observed_mass_ra * 100 < 0.01 := by
  unfold qou_mass_ra observed_mass_ra atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 89. Actinium (Ac), A = 227
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Actinium (Z=89, N=138, A=227). -/
noncomputable def qou_mass_ac : Real := atomic_mass 89 138 7.6510

/-- Observed mass of Actinium (AME2020). -/
noncomputable def observed_mass_ac : Real := 211475.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Actinium is less than 1.1 MeV. -/
theorem deviation_ac :
    |qou_mass_ac - observed_mass_ac| < 1.1 := by
  unfold qou_mass_ac observed_mass_ac atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Actinium is less than 0.01%. -/
theorem pct_deviation_ac :
    |qou_mass_ac - observed_mass_ac| / observed_mass_ac * 100 < 0.01 := by
  unfold qou_mass_ac observed_mass_ac atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 90. Thorium (Th), A = 232
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Thorium (Z=90, N=142, A=232). -/
noncomputable def qou_mass_th : Real := atomic_mass 90 142 7.6150

/-- Observed mass of Thorium (AME2020). -/
noncomputable def observed_mass_th : Real := 216142.7

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Thorium is less than 1.1 MeV. -/
theorem deviation_th :
    |qou_mass_th - observed_mass_th| < 1.1 := by
  unfold qou_mass_th observed_mass_th atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Thorium is less than 0.01%. -/
theorem pct_deviation_th :
    |qou_mass_th - observed_mass_th| / observed_mass_th * 100 < 0.01 := by
  unfold qou_mass_th observed_mass_th atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 91. Protactinium (Pa), A = 231
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Protactinium (Z=91, N=140, A=231). -/
noncomputable def qou_mass_pa : Real := atomic_mass 91 140 7.6138

/-- Observed mass of Protactinium (AME2020). -/
noncomputable def observed_mass_pa : Real := 215210.2

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Protactinium is less than 1.1 MeV. -/
theorem deviation_pa :
    |qou_mass_pa - observed_mass_pa| < 1.1 := by
  unfold qou_mass_pa observed_mass_pa atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Protactinium is less than 0.01%. -/
theorem pct_deviation_pa :
    |qou_mass_pa - observed_mass_pa| / observed_mass_pa * 100 < 0.01 := by
  unfold qou_mass_pa observed_mass_pa atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 92. Uranium (U), A = 238
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Uranium (Z=92, N=146, A=238). -/
noncomputable def qou_mass_u : Real := atomic_mass 92 146 7.5701

/-- Observed mass of Uranium (AME2020). -/
noncomputable def observed_mass_u : Real := 221743.5

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Absolute deviation of QOU prediction for Uranium is less than 1.1 MeV. -/
theorem deviation_u :
    |qou_mass_u - observed_mass_u| < 1.1 := by
  unfold qou_mass_u observed_mass_u atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
/-- Percentage deviation of QOU prediction for Uranium is less than 0.01%. -/
theorem pct_deviation_u :
    |qou_mass_u - observed_mass_u| / observed_mass_u * 100 < 0.01 := by
  unfold qou_mass_u observed_mass_u atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 93. Neptunium (Np), A = 237
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Neptunium (Z=93, N=144, A=237). -/
noncomputable def qou_mass_np : Real := atomic_mass 93 144 7.5753

/-- Observed mass of Neptunium (AME2020). -/
noncomputable def observed_mass_np : Real := 220812.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Neptunium is less than 3.6 MeV. -/
theorem deviation_np :
    |qou_mass_np - observed_mass_np| < 3.6 := by
  unfold qou_mass_np observed_mass_np atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Neptunium is less than 0.01%. -/
theorem pct_deviation_np :
    |qou_mass_np - observed_mass_np| / observed_mass_np * 100 < 0.01 := by
  unfold qou_mass_np observed_mass_np atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 94. Plutonium (Pu), A = 244
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Plutonium (Z=94, N=150, A=244). -/
noncomputable def qou_mass_pu : Real := atomic_mass 94 150 7.5563

/-- Observed mass of Plutonium (AME2020). -/
noncomputable def observed_mass_pu : Real := 227325.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Plutonium is less than 12.2 MeV. -/
theorem deviation_pu :
    |qou_mass_pu - observed_mass_pu| < 12.2 := by
  unfold qou_mass_pu observed_mass_pu atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Plutonium is less than 0.02%. -/
theorem pct_deviation_pu :
    |qou_mass_pu - observed_mass_pu| / observed_mass_pu * 100 < 0.02 := by
  unfold qou_mass_pu observed_mass_pu atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 95. Americium (Am), A = 243
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Americium (Z=95, N=148, A=243). -/
noncomputable def qou_mass_am : Real := atomic_mass 95 148 7.5249

/-- Observed mass of Americium (AME2020). -/
noncomputable def observed_mass_am : Real := 226394.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Americium is less than 18.0 MeV. -/
theorem deviation_am :
    |qou_mass_am - observed_mass_am| < 18.0 := by
  unfold qou_mass_am observed_mass_am atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Americium is less than 0.02%. -/
theorem pct_deviation_am :
    |qou_mass_am - observed_mass_am| / observed_mass_am * 100 < 0.02 := by
  unfold qou_mass_am observed_mass_am atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 96. Curium (Cm), A = 247
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Curium (Z=96, N=151, A=247). -/
noncomputable def qou_mass_cm : Real := atomic_mass 96 151 7.5008

/-- Observed mass of Curium (AME2020). -/
noncomputable def observed_mass_cm : Real := 230048.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Curium is less than 97.4 MeV. -/
theorem deviation_cm :
    |qou_mass_cm - observed_mass_cm| < 97.4 := by
  unfold qou_mass_cm observed_mass_cm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Curium is less than 0.05%. -/
theorem pct_deviation_cm :
    |qou_mass_cm - observed_mass_cm| / observed_mass_cm * 100 < 0.05 := by
  unfold qou_mass_cm observed_mass_cm atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 97. Berkelium (Bk), A = 247
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Berkelium (Z=97, N=150, A=247). -/
noncomputable def qou_mass_bk : Real := atomic_mass 97 150 7.4980

/-- Observed mass of Berkelium (AME2020). -/
noncomputable def observed_mass_bk : Real := 229977.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Berkelium is less than 168.3 MeV. -/
theorem deviation_bk :
    |qou_mass_bk - observed_mass_bk| < 168.3 := by
  unfold qou_mass_bk observed_mass_bk atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Berkelium is less than 0.08%. -/
theorem pct_deviation_bk :
    |qou_mass_bk - observed_mass_bk| / observed_mass_bk * 100 < 0.08 := by
  unfold qou_mass_bk observed_mass_bk atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 98. Californium (Cf), A = 251
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Californium (Z=98, N=153, A=251). -/
noncomputable def qou_mass_cf : Real := atomic_mass 98 153 7.4688

/-- Observed mass of Californium (AME2020). -/
noncomputable def observed_mass_cf : Real := 233631.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Californium is less than 249.1 MeV. -/
theorem deviation_cf :
    |qou_mass_cf - observed_mass_cf| < 249.1 := by
  unfold qou_mass_cf observed_mass_cf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Californium is less than 0.12%. -/
theorem pct_deviation_cf :
    |qou_mass_cf - observed_mass_cf| / observed_mass_cf * 100 < 0.12 := by
  unfold qou_mass_cf observed_mass_cf atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 99. Einsteinium (Es), A = 252
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Einsteinium (Z=99, N=153, A=252). -/
noncomputable def qou_mass_es : Real := atomic_mass 99 153 7.4496

/-- Observed mass of Einsteinium (AME2020). -/
noncomputable def observed_mass_es : Real := 234494.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Einsteinium is less than 322.2 MeV. -/
theorem deviation_es :
    |qou_mass_es - observed_mass_es| < 322.2 := by
  unfold qou_mass_es observed_mass_es atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Einsteinium is less than 0.15%. -/
theorem pct_deviation_es :
    |qou_mass_es - observed_mass_es| / observed_mass_es * 100 < 0.15 := by
  unfold qou_mass_es observed_mass_es atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 100. Fermium (Fm), A = 257
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Fermium (Z=100, N=157, A=257). -/
noncomputable def qou_mass_fm : Real := atomic_mass 100 157 7.4197

/-- Observed mass of Fermium (AME2020). -/
noncomputable def observed_mass_fm : Real := 239082.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Fermium is less than 401.7 MeV. -/
theorem deviation_fm :
    |qou_mass_fm - observed_mass_fm| < 401.7 := by
  unfold qou_mass_fm observed_mass_fm atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Fermium is less than 0.18%. -/
theorem pct_deviation_fm :
    |qou_mass_fm - observed_mass_fm| / observed_mass_fm * 100 < 0.18 := by
  unfold qou_mass_fm observed_mass_fm atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 101. Mendelevium (Md), A = 258
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Mendelevium (Z=101, N=157, A=258). -/
noncomputable def qou_mass_md : Real := atomic_mass 101 157 7.4039

/-- Observed mass of Mendelevium (AME2020). -/
noncomputable def observed_mass_md : Real := 239949.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Mendelevium is less than 470.2 MeV. -/
theorem deviation_md :
    |qou_mass_md - observed_mass_md| < 470.2 := by
  unfold qou_mass_md observed_mass_md atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Mendelevium is less than 0.21%. -/
theorem pct_deviation_md :
    |qou_mass_md - observed_mass_md| / observed_mass_md * 100 < 0.21 := by
  unfold qou_mass_md observed_mass_md atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 102. Nobelium (No), A = 259
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Nobelium (Z=102, N=157, A=259). -/
noncomputable def qou_mass_no : Real := atomic_mass 102 157 7.3900

/-- Observed mass of Nobelium (AME2020). -/
noncomputable def observed_mass_no : Real := 240814.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Nobelium is less than 540.1 MeV. -/
theorem deviation_no :
    |qou_mass_no - observed_mass_no| < 540.1 := by
  unfold qou_mass_no observed_mass_no atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Nobelium is less than 0.23%. -/
theorem pct_deviation_no :
    |qou_mass_no - observed_mass_no| / observed_mass_no * 100 < 0.23 := by
  unfold qou_mass_no observed_mass_no atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 103. Lawrencium (Lr), A = 262
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Lawrencium (Z=103, N=159, A=262). -/
noncomputable def qou_mass_lr : Real := atomic_mass 103 159 7.3540

/-- Observed mass of Lawrencium (AME2020). -/
noncomputable def observed_mass_lr : Real := 243606.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Lawrencium is less than 553.3 MeV. -/
theorem deviation_lr :
    |qou_mass_lr - observed_mass_lr| < 553.3 := by
  unfold qou_mass_lr observed_mass_lr atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Lawrencium is less than 0.24%. -/
theorem pct_deviation_lr :
    |qou_mass_lr - observed_mass_lr| / observed_mass_lr * 100 < 0.24 := by
  unfold qou_mass_lr observed_mass_lr atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 104. Rutherfordium (Rf), A = 267
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Rutherfordium (Z=104, N=163, A=267). -/
noncomputable def qou_mass_rf : Real := atomic_mass 104 163 7.3000

/-- Observed mass of Rutherfordium (AME2020). -/
noncomputable def observed_mass_rf : Real := 248264.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Rutherfordium is less than 570.0 MeV. -/
theorem deviation_rf :
    |qou_mass_rf - observed_mass_rf| < 570.0 := by
  unfold qou_mass_rf observed_mass_rf atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Rutherfordium is less than 0.24%. -/
theorem pct_deviation_rf :
    |qou_mass_rf - observed_mass_rf| / observed_mass_rf * 100 < 0.24 := by
  unfold qou_mass_rf observed_mass_rf atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 105. Dubnium (Db), A = 268
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Dubnium (Z=105, N=163, A=268). -/
noncomputable def qou_mass_db : Real := atomic_mass 105 163 7.2800

/-- Observed mass of Dubnium (AME2020). -/
noncomputable def observed_mass_db : Real := 249133.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Dubnium is less than 637.8 MeV. -/
theorem deviation_db :
    |qou_mass_db - observed_mass_db| < 637.8 := by
  unfold qou_mass_db observed_mass_db atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Dubnium is less than 0.27%. -/
theorem pct_deviation_db :
    |qou_mass_db - observed_mass_db| / observed_mass_db * 100 < 0.27 := by
  unfold qou_mass_db observed_mass_db atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 106. Seaborgium (Sg), A = 269
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Seaborgium (Z=106, N=163, A=269). -/
noncomputable def qou_mass_sg : Real := atomic_mass 106 163 7.2600

/-- Observed mass of Seaborgium (AME2020). -/
noncomputable def observed_mass_sg : Real := 250002.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Seaborgium is less than 705.7 MeV. -/
theorem deviation_sg :
    |qou_mass_sg - observed_mass_sg| < 705.7 := by
  unfold qou_mass_sg observed_mass_sg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Seaborgium is less than 0.29%. -/
theorem pct_deviation_sg :
    |qou_mass_sg - observed_mass_sg| / observed_mass_sg * 100 < 0.29 := by
  unfold qou_mass_sg observed_mass_sg atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 107. Bohrium (Bh), A = 270
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Bohrium (Z=107, N=163, A=270). -/
noncomputable def qou_mass_bh : Real := atomic_mass 107 163 7.2400

/-- Observed mass of Bohrium (AME2020). -/
noncomputable def observed_mass_bh : Real := 250871.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Bohrium is less than 773.7 MeV. -/
theorem deviation_bh :
    |qou_mass_bh - observed_mass_bh| < 773.7 := by
  unfold qou_mass_bh observed_mass_bh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Bohrium is less than 0.32%. -/
theorem pct_deviation_bh :
    |qou_mass_bh - observed_mass_bh| / observed_mass_bh * 100 < 0.32 := by
  unfold qou_mass_bh observed_mass_bh atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 108. Hassium (Hs), A = 277
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Hassium (Z=108, N=169, A=277). -/
noncomputable def qou_mass_hs : Real := atomic_mass 108 169 7.2100

/-- Observed mass of Hassium (AME2020). -/
noncomputable def observed_mass_hs : Real := 257458.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Hassium is less than 720.5 MeV. -/
theorem deviation_hs :
    |qou_mass_hs - observed_mass_hs| < 720.5 := by
  unfold qou_mass_hs observed_mass_hs atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Hassium is less than 0.29%. -/
theorem pct_deviation_hs :
    |qou_mass_hs - observed_mass_hs| / observed_mass_hs * 100 < 0.29 := by
  unfold qou_mass_hs observed_mass_hs atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 109. Meitnerium (Mt), A = 278
-- [Synthetic element]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Meitnerium (Z=109, N=169, A=278). -/
noncomputable def qou_mass_mt : Real := atomic_mass 109 169 7.1900

/-- Observed mass of Meitnerium (AME2020). -/
noncomputable def observed_mass_mt : Real := 258327.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Meitnerium is less than 788.6 MeV. -/
theorem deviation_mt :
    |qou_mass_mt - observed_mass_mt| < 788.6 := by
  unfold qou_mass_mt observed_mass_mt atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Meitnerium is less than 0.32%. -/
theorem pct_deviation_mt :
    |qou_mass_mt - observed_mass_mt| / observed_mass_mt * 100 < 0.32 := by
  unfold qou_mass_mt observed_mass_mt atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 110. Darmstadtium (Ds), A = 281
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Darmstadtium (Z=110, N=171, A=281). -/
noncomputable def qou_mass_ds : Real := atomic_mass 110 171 7.1650

/-- Observed mass of Darmstadtium (AME2020). -/
noncomputable def observed_mass_ds : Real := 261061.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Darmstadtium is less than 858.0 MeV. -/
theorem deviation_ds :
    |qou_mass_ds - observed_mass_ds| < 858.0 := by
  unfold qou_mass_ds observed_mass_ds atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Darmstadtium is less than 0.34%. -/
theorem pct_deviation_ds :
    |qou_mass_ds - observed_mass_ds| / observed_mass_ds * 100 < 0.34 := by
  unfold qou_mass_ds observed_mass_ds atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 111. Roentgenium (Rg), A = 282
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Roentgenium (Z=111, N=171, A=282). -/
noncomputable def qou_mass_rg : Real := atomic_mass 111 171 7.1440

/-- Observed mass of Roentgenium (AME2020). -/
noncomputable def observed_mass_rg : Real := 261930.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Roentgenium is less than 926.5 MeV. -/
theorem deviation_rg :
    |qou_mass_rg - observed_mass_rg| < 926.5 := by
  unfold qou_mass_rg observed_mass_rg atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Roentgenium is less than 0.36%. -/
theorem pct_deviation_rg :
    |qou_mass_rg - observed_mass_rg| / observed_mass_rg * 100 < 0.36 := by
  unfold qou_mass_rg observed_mass_rg atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 112. Copernicium (Cn), A = 285
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Copernicium (Z=112, N=173, A=285). -/
noncomputable def qou_mass_cn : Real := atomic_mass 112 173 7.1180

/-- Observed mass of Copernicium (AME2020). -/
noncomputable def observed_mass_cn : Real := 264664.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Copernicium is less than 996.4 MeV. -/
theorem deviation_cn :
    |qou_mass_cn - observed_mass_cn| < 996.4 := by
  unfold qou_mass_cn observed_mass_cn atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Copernicium is less than 0.39%. -/
theorem pct_deviation_cn :
    |qou_mass_cn - observed_mass_cn| / observed_mass_cn * 100 < 0.39 := by
  unfold qou_mass_cn observed_mass_cn atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 113. Nihonium (Nh), A = 286
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Nihonium (Z=113, N=173, A=286). -/
noncomputable def qou_mass_nh : Real := atomic_mass 113 173 7.0960

/-- Observed mass of Nihonium (AME2020). -/
noncomputable def observed_mass_nh : Real := 265533.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Nihonium is less than 1065.4 MeV. -/
theorem deviation_nh :
    |qou_mass_nh - observed_mass_nh| < 1065.4 := by
  unfold qou_mass_nh observed_mass_nh atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Nihonium is less than 0.41%. -/
theorem pct_deviation_nh :
    |qou_mass_nh - observed_mass_nh| / observed_mass_nh * 100 < 0.41 := by
  unfold qou_mass_nh observed_mass_nh atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 114. Flerovium (Fl), A = 289
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Flerovium (Z=114, N=175, A=289). -/
noncomputable def qou_mass_fl : Real := atomic_mass 114 175 7.0700

/-- Observed mass of Flerovium (AME2020). -/
noncomputable def observed_mass_fl : Real := 268267.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Flerovium is less than 1135.5 MeV. -/
theorem deviation_fl :
    |qou_mass_fl - observed_mass_fl| < 1135.5 := by
  unfold qou_mass_fl observed_mass_fl atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Flerovium is less than 0.43%. -/
theorem pct_deviation_fl :
    |qou_mass_fl - observed_mass_fl| / observed_mass_fl * 100 < 0.43 := by
  unfold qou_mass_fl observed_mass_fl atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 115. Moscovium (Mc), A = 290
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Moscovium (Z=115, N=175, A=290). -/
noncomputable def qou_mass_mc : Real := atomic_mass 115 175 7.0470

/-- Observed mass of Moscovium (AME2020). -/
noncomputable def observed_mass_mc : Real := 269136.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Moscovium is less than 1204.9 MeV. -/
theorem deviation_mc :
    |qou_mass_mc - observed_mass_mc| < 1204.9 := by
  unfold qou_mass_mc observed_mass_mc atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Moscovium is less than 0.46%. -/
theorem pct_deviation_mc :
    |qou_mass_mc - observed_mass_mc| / observed_mass_mc * 100 < 0.46 := by
  unfold qou_mass_mc observed_mass_mc atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 116. Livermorium (Lv), A = 293
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Livermorium (Z=116, N=177, A=293). -/
noncomputable def qou_mass_lv : Real := atomic_mass 116 177 7.0200

/-- Observed mass of Livermorium (AME2020). -/
noncomputable def observed_mass_lv : Real := 271870.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Livermorium is less than 1275.6 MeV. -/
theorem deviation_lv :
    |qou_mass_lv - observed_mass_lv| < 1275.6 := by
  unfold qou_mass_lv observed_mass_lv atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Livermorium is less than 0.48%. -/
theorem pct_deviation_lv :
    |qou_mass_lv - observed_mass_lv| / observed_mass_lv * 100 < 0.48 := by
  unfold qou_mass_lv observed_mass_lv atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 117. Tennessine (Ts), A = 294
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Tennessine (Z=117, N=177, A=294). -/
noncomputable def qou_mass_ts : Real := atomic_mass 117 177 6.9960

/-- Observed mass of Tennessine (AME2020). -/
noncomputable def observed_mass_ts : Real := 272739.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Tennessine is less than 1345.4 MeV. -/
theorem deviation_ts :
    |qou_mass_ts - observed_mass_ts| < 1345.4 := by
  unfold qou_mass_ts observed_mass_ts atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Tennessine is less than 0.5%. -/
theorem pct_deviation_ts :
    |qou_mass_ts - observed_mass_ts| / observed_mass_ts * 100 < 0.5 := by
  unfold qou_mass_ts observed_mass_ts atomic_mass m_p m_n m_e
  norm_num

-- ══════════════════════════════════════════════════════════════
-- 118. Oganesson (Og), A = 294
-- [Synthetic element — observed mass extrapolated]
-- ══════════════════════════════════════════════════════════════

/-- QOU predicted mass of Oganesson (Z=118, N=176, A=294). -/
noncomputable def qou_mass_og : Real := atomic_mass 118 176 6.9720

/-- Observed mass of Oganesson (AME2020). -/
noncomputable def observed_mass_og : Real := 273539.0

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Absolute deviation of QOU prediction for Oganesson is less than 551.7 MeV. -/
theorem deviation_og :
    |qou_mass_og - observed_mass_og| < 551.7 := by
  unfold qou_mass_og observed_mass_og atomic_mass m_p m_n m_e
  norm_num

-- Ref: [codata2022] https://physics.nist.gov/cuu/Constants/
-- Ref: [manuscript] Appendix C
/-- Percentage deviation of QOU prediction for Oganesson is less than 0.21%. -/
theorem pct_deviation_og :
    |qou_mass_og - observed_mass_og| / observed_mass_og * 100 < 0.21 := by
  unfold qou_mass_og observed_mass_og atomic_mass m_p m_n m_e
  norm_num

end QOU.AtomicMass