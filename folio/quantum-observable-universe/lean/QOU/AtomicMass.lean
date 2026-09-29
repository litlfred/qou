-- ╔═══════════════════════════════════════════════════════════════════╗
-- ║  GENERATED FILE — DO NOT EDIT BY HAND.                              ║
-- ║  Source of truth: scripts/atomic_mass_data.json (data) +           ║
-- ║                   scripts/gen_atomic_mass.py    (template).         ║
-- ║  Regenerate:  python3 scripts/gen_atomic_mass.py                    ║
-- ║  CI drift gate (atomic-mass-gen-check.yml) fails on any divergence. ║
-- ╚═══════════════════════════════════════════════════════════════════╝
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.AtomicMass.MagicNumbersFromQ

/-!
  QOU Atomic Mass Predictions — CODATA 2022 vs AME2020 Audit

  Two independent mass sources are compared for each element:
  - **CODATA 2022** constituent masses (m_p, m_n, m_e)
  - **AME2020** atomic mass unit (u) and mass excesses (Δ_H, Δ_n)

  For an element with `Z` protons and `N` neutrons (`A = Z + N`) the
  CODATA path is `Z·m_p + N·m_n + Z·m_e − A·(B/A)` and the AME path is
  `A·u + Z·Δ_H + N·Δ_n − A·(B/A)`.  Their difference is the *structural
  offset*

      codataMass − ameMass = Z·offset_Z + N·offset_N            (1)

  with
  - `offset_Z = (m_p + m_e) − (u + Δ_H) ≈ 1.546 × 10⁻⁵ MeV` — the
    H-atom electron binding energy, absent from the free `m_p + m_e`
    but present in `M_H`; and
  - `offset_N = m_n − (u + Δ_n) ≈ 1.46 × 10⁻⁶ MeV` — the residual
    CODATA-2022 vs AME2020 neutron-mass discrepancy.

  Both offsets are tiny.  Identity (1) (`codata_minus_ame_offset`) and
  the resulting per-element bound (`deviation_uniform`) are proved
  **generically** for every `ElementDatum`, subsuming what were 118
  copy-pasted per-element theorems.  The curated 118-element AME2020
  dataset (Z = 1…118) is retained as `elements`.

  Correction note: the historical per-Z-only form `… = Z·offset_Z`
  is *false* — the `N·offset_N` term does not cancel against the
  `B/A` binding term (that would require `m_n = u + Δ_n`, which fails
  by ≈ 1.46 eV).  Identity (1) is the corrected statement.
-/

namespace QOU.AtomicMass

/-! ## CODATA 2022 Constituent Masses
Source: NIST CODATA 2022, https://physics.nist.gov/cuu/Constants/ -/

/-- Proton mass (CODATA 2022): 938.272 089 43(29) MeV/c². -/
noncomputable def codata_m_p : ℝ := 938.27208943

/-- Neutron mass (CODATA 2022): 939.565 421 94(48) MeV/c². -/
noncomputable def codata_m_n : ℝ := 939.56542194

/-- Electron mass (CODATA 2022): 0.510 998 950 69(16) MeV/c². -/
noncomputable def codata_m_e : ℝ := 0.51099895069

/-! ## AME2020 Constants
Source: Atomic Mass Evaluation 2020 (Wang et al., Chinese Physics C 45,
030003), https://www-nds.iaea.org/amdc/ -/

/-- Atomic mass unit (CODATA 2022): 931.49410372 MeV/c². -/
noncomputable def ame_u : ℝ := 931.49410372

/-- ¹H mass excess (AME2020): 7.2889705 MeV. -/
noncomputable def ame_delta_H : ℝ := 7.2889705

/-- Neutron mass excess (AME2020): 8.07131806 MeV. -/
noncomputable def ame_delta_n : ℝ := 8.07131806

/-! ## Mass computation functions -/

/-- CODATA path: `M = Z·m_p + N·m_n + Z·m_e − A·(B/A)`. -/
noncomputable def codata_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  (Z : ℝ) * codata_m_p + (N : ℝ) * codata_m_n + (Z : ℝ) * codata_m_e
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- AME2020 path: `M = A·u + Z·Δ_H + N·Δ_n − A·(B/A)`. -/
noncomputable def ame2020_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  ((Z : ℝ) + (N : ℝ)) * ame_u + (Z : ℝ) * ame_delta_H + (N : ℝ) * ame_delta_n
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- Element data: atomic number, neutron number, AME2020 B/A (MeV). -/
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

/-! ## Structural offsets -/

/-- Per-proton CODATA−AME2020 offset: `(m_p + m_e) − (u + Δ_H)`
    ≈ 1.546 × 10⁻⁵ MeV (H-atom electron binding energy). -/
noncomputable def codata_ame_offset_per_Z : ℝ :=
  (codata_m_p + codata_m_e) - (ame_u + ame_delta_H)

/-- Per-neutron CODATA−AME2020 offset: `m_n − (u + Δ_n)`
    ≈ 1.46 × 10⁻⁶ MeV (residual CODATA-2022 vs AME2020 neutron-mass
    discrepancy).  Nonzero — this is the term the historical
    `= Z·offset_Z` lemma wrongly dropped. -/
noncomputable def codata_ame_offset_per_N : ℝ :=
  codata_m_n - (ame_u + ame_delta_n)

/-- **Structural identity.**  For any element datum the CODATA−AME2020
    mass difference is `Z·offset_Z + N·offset_N`.  The `A·(B/A)`
    binding terms cancel; the proton and neutron offsets do not. -/
theorem ElementDatum.codata_minus_ame_offset (e : ElementDatum) :
    e.codataMass - e.ameMass
      = (e.Z : ℝ) * codata_ame_offset_per_Z
        + (e.N : ℝ) * codata_ame_offset_per_N := by
  unfold ElementDatum.codataMass ElementDatum.ameMass
    codata_atomic_mass ame2020_atomic_mass
    codata_ame_offset_per_Z codata_ame_offset_per_N
  ring

/-- The per-proton offset is below 2 × 10⁻⁵ MeV. -/
theorem codata_ame_offset_per_Z_bound : |codata_ame_offset_per_Z| < 0.00002 := by
  unfold codata_ame_offset_per_Z codata_m_p codata_m_e ame_u ame_delta_H
  rw [abs_lt]; constructor <;> norm_num

/-- The per-neutron offset is below 2 × 10⁻⁶ MeV. -/
theorem codata_ame_offset_per_N_bound : |codata_ame_offset_per_N| < 0.000002 := by
  unfold codata_ame_offset_per_N codata_m_n ame_u ame_delta_n
  rw [abs_lt]; constructor <;> norm_num

/-- **Uniform per-element deviation bound.**  For any element datum,
    `|codataMass − ameMass| ≤ Z·|offset_Z| + N·|offset_N|`.  This
    single generic statement subsumes the per-element numerical checks
    (the offsets are bounded by `codata_ame_offset_per_{Z,N}_bound`). -/
theorem deviation_uniform (e : ElementDatum) :
    |e.codataMass - e.ameMass|
      ≤ (e.Z : ℝ) * |codata_ame_offset_per_Z|
        + (e.N : ℝ) * |codata_ame_offset_per_N| := by
  rw [ElementDatum.codata_minus_ame_offset]
  have hZ : (0 : ℝ) ≤ (e.Z : ℝ) := Nat.cast_nonneg _
  have hN : (0 : ℝ) ≤ (e.N : ℝ) := Nat.cast_nonneg _
  calc |(e.Z : ℝ) * codata_ame_offset_per_Z + (e.N : ℝ) * codata_ame_offset_per_N|
      ≤ |(e.Z : ℝ) * codata_ame_offset_per_Z|
          + |(e.N : ℝ) * codata_ame_offset_per_N| := abs_add_le _ _
    _ = (e.Z : ℝ) * |codata_ame_offset_per_Z|
          + (e.N : ℝ) * |codata_ame_offset_per_N| := by
        rw [abs_mul, abs_mul, abs_of_nonneg hZ, abs_of_nonneg hN]

/-! ## Headline numerical checks (concrete instances of the bound) -/

/-- Hydrogen (Z=1, N=0). -/
noncomputable def hydrogen : ElementDatum := ⟨1, 0, 0.0⟩
/-- Iron-56 (Z=26, N=30): peak binding energy per nucleon. -/
noncomputable def iron56 : ElementDatum := ⟨26, 30, 8.7903⟩
/-- Oganesson-294 (Z=118, N=176): heaviest tabulated element. -/
noncomputable def oganesson : ElementDatum := ⟨118, 176, 6.972⟩

example : |hydrogen.codataMass - hydrogen.ameMass| < 0.0001 := by
  simp only [hydrogen, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

example : |iron56.codataMass - iron56.ameMass| < 0.0008 := by
  simp only [iron56, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

example : |oganesson.codataMass - oganesson.ameMass| < 0.0032 := by
  simp only [oganesson, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

/-! ## AME2020 dataset (Z = 1…118)

Curated `(symbol, ⟨Z, N, B/A⟩)` table.  Every entry satisfies
`deviation_uniform`; B/A values are AME2020 binding energy per
nucleon in MeV.  Source: https://www-nds.iaea.org/amdc/ -/

/-- The 118 tabulated elements with their AME2020 binding energies. -/
noncomputable def elements : List (String × ElementDatum) :=
  [
    ("H", ⟨1, 0, 0.0⟩),
    ("He", ⟨2, 2, 7.0739⟩),
    ("Li", ⟨3, 4, 5.6063⟩),
    ("Be", ⟨4, 5, 6.4628⟩),
    ("B", ⟨5, 6, 6.9277⟩),
    ("C", ⟨6, 6, 7.6801⟩),
    ("N", ⟨7, 7, 7.4756⟩),
    ("O", ⟨8, 8, 7.9762⟩),
    ("F", ⟨9, 10, 7.779⟩),
    ("Ne", ⟨10, 10, 8.0325⟩),
    ("Na", ⟨11, 12, 8.1115⟩),
    ("Mg", ⟨12, 12, 8.2607⟩),
    ("Al", ⟨13, 14, 8.3316⟩),
    ("Si", ⟨14, 14, 8.4477⟩),
    ("P", ⟨15, 16, 8.4812⟩),
    ("S", ⟨16, 16, 8.4932⟩),
    ("Cl", ⟨17, 18, 8.5203⟩),
    ("Ar", ⟨18, 22, 8.5954⟩),
    ("K", ⟨19, 20, 8.557⟩),
    ("Ca", ⟨20, 20, 8.5513⟩),
    ("Sc", ⟨21, 24, 8.619⟩),
    ("Ti", ⟨22, 26, 8.723⟩),
    ("V", ⟨23, 28, 8.742⟩),
    ("Cr", ⟨24, 28, 8.776⟩),
    ("Mn", ⟨25, 30, 8.7649⟩),
    ("Fe", ⟨26, 30, 8.7903⟩),
    ("Co", ⟨27, 32, 8.768⟩),
    ("Ni", ⟨28, 30, 8.7322⟩),
    ("Cu", ⟨29, 34, 8.7522⟩),
    ("Zn", ⟨30, 34, 8.7357⟩),
    ("Ga", ⟨31, 38, 8.7246⟩),
    ("Ge", ⟨32, 42, 8.7264⟩),
    ("As", ⟨33, 42, 8.701⟩),
    ("Se", ⟨34, 46, 8.711⟩),
    ("Br", ⟨35, 44, 8.6961⟩),
    ("Kr", ⟨36, 48, 8.7172⟩),
    ("Rb", ⟨37, 48, 8.6974⟩),
    ("Sr", ⟨38, 50, 8.7326⟩),
    ("Y", ⟨39, 50, 8.7138⟩),
    ("Zr", ⟨40, 50, 8.7098⟩),
    ("Nb", ⟨41, 52, 8.6641⟩),
    ("Mo", ⟨42, 56, 8.6353⟩),
    ("Tc", ⟨43, 55, 8.5937⟩),
    ("Ru", ⟨44, 58, 8.607⟩),
    ("Rh", ⟨45, 58, 8.5843⟩),
    ("Pd", ⟨46, 60, 8.567⟩),
    ("Ag", ⟨47, 60, 8.5536⟩),
    ("Cd", ⟨48, 66, 8.5398⟩),
    ("In", ⟨49, 66, 8.516⟩),
    ("Sn", ⟨50, 70, 8.505⟩),
    ("Sb", ⟨51, 70, 8.482⟩),
    ("Te", ⟨52, 78, 8.439⟩),
    ("I", ⟨53, 74, 8.4455⟩),
    ("Xe", ⟨54, 78, 8.4275⟩),
    ("Cs", ⟨55, 78, 8.41⟩),
    ("Ba", ⟨56, 82, 8.3937⟩),
    ("La", ⟨57, 82, 8.378⟩),
    ("Ce", ⟨58, 82, 8.3765⟩),
    ("Pr", ⟨59, 82, 8.354⟩),
    ("Nd", ⟨60, 82, 8.346⟩),
    ("Pm", ⟨61, 84, 8.304⟩),
    ("Sm", ⟨62, 90, 8.244⟩),
    ("Eu", ⟨63, 90, 8.229⟩),
    ("Gd", ⟨64, 94, 8.214⟩),
    ("Tb", ⟨65, 94, 8.199⟩),
    ("Dy", ⟨66, 98, 8.1865⟩),
    ("Ho", ⟨67, 98, 8.171⟩),
    ("Er", ⟨68, 98, 8.169⟩),
    ("Tm", ⟨69, 100, 8.146⟩),
    ("Yb", ⟨70, 104, 8.128⟩),
    ("Lu", ⟨71, 104, 8.1165⟩),
    ("Hf", ⟨72, 108, 8.0985⟩),
    ("Ta", ⟨73, 108, 8.087⟩),
    ("W", ⟨74, 110, 8.0639⟩),
    ("Re", ⟨75, 112, 8.039⟩),
    ("Os", ⟨76, 116, 8.0194⟩),
    ("Ir", ⟨77, 116, 8.006⟩),
    ("Pt", ⟨78, 117, 7.993⟩),
    ("Au", ⟨79, 118, 7.9759⟩),
    ("Hg", ⟨80, 122, 7.953⟩),
    ("Tl", ⟨81, 124, 7.937⟩),
    ("Pb", ⟨82, 126, 7.8675⟩),
    ("Bi", ⟨83, 126, 7.848⟩),
    ("Po", ⟨84, 125, 7.8352⟩),
    ("At", ⟨85, 125, 7.8147⟩),
    ("Rn", ⟨86, 136, 7.7227⟩),
    ("Fr", ⟨87, 136, 7.7095⟩),
    ("Ra", ⟨88, 138, 7.662⟩),
    ("Ac", ⟨89, 138, 7.651⟩),
    ("Th", ⟨90, 142, 7.615⟩),
    ("Pa", ⟨91, 140, 7.6138⟩),
    ("U", ⟨92, 146, 7.5701⟩),
    ("Np", ⟨93, 144, 7.5753⟩),
    ("Pu", ⟨94, 150, 7.5242⟩),
    ("Am", ⟨95, 148, 7.5249⟩),
    ("Cm", ⟨96, 151, 7.4988⟩),
    ("Bk", ⟨97, 150, 7.498⟩),
    ("Cf", ⟨98, 153, 7.4688⟩),
    ("Es", ⟨99, 153, 7.4496⟩),
    ("Fm", ⟨100, 157, 7.4197⟩),
    ("Md", ⟨101, 157, 7.4039⟩),
    ("No", ⟨102, 157, 7.39⟩),
    ("Lr", ⟨103, 163, 7.354⟩),
    ("Rf", ⟨104, 163, 7.338⟩),
    ("Db", ⟨105, 163, 7.32⟩),
    ("Sg", ⟨106, 163, 7.302⟩),
    ("Bh", ⟨107, 163, 7.283⟩),
    ("Hs", ⟨108, 169, 7.256⟩),
    ("Mt", ⟨109, 169, 7.237⟩),
    ("Ds", ⟨110, 171, 7.211⟩),
    ("Rg", ⟨111, 171, 7.191⟩),
    ("Cn", ⟨112, 173, 7.165⟩),
    ("Nh", ⟨113, 173, 7.144⟩),
    ("Fl", ⟨114, 175, 7.118⟩),
    ("Mc", ⟨115, 175, 7.096⟩),
    ("Lv", ⟨116, 177, 7.02⟩),
    ("Ts", ⟨117, 177, 6.996⟩),
    ("Og", ⟨118, 176, 6.972⟩)
  ]

end QOU.AtomicMass
