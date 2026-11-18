/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  qou-3nva : MATH/RENDER anomalies from trap-drain obs-b1/b2/b3 (Ca40 partition (5,4,4,4,3)
             non-self-conjugacy and SU(N) rank N - 1)
  qou-7y1z : Teraplectic z=0.99850030 is not an admissible Markov parameter under convention D
  qou-960k : Quantum Teichmuller held in 35 library dirs (rank-1 PGL(2,C)) vs 1 substantive
             Fock-Goncharov rank-2 PGL(n,C) source (arxiv-1207.6711v1)
  qou-r5up : MATH anomalies from trap-drain obs-b0 (dimensionless hbar_q = q - q^-1 vs
             dimensional MeV scale and Borromean triple vs pairwise links)
  qou-rbdz : Update Mass Theory docs with H3 Delta Baryon and Quaternionic Shift
-/

namespace QOU.Eightfold.Ca40ConjugacyTeraplecticZTeichmullerHbarQDeltaShift

/-!
# 1. `qou-3nva` — Partition `(5,4,4,4,3)` Conjugate Discrepancy & `SU(N)` Rank Law

For a 5-row partition `λ = (λ₁, λ₂, λ₃, λ₄, λ₅)` with `λ₁ = 5, λ₂ = 4, λ₃ = 4, λ₄ = 4, λ₅ = 3`
(total weight `20`), its conjugate partition is `λ' = (5, 5, 5, 4, 1)`. Thus `λ ≠ λ'`
(their L1 row-wise discrepancy is `|5-5| + |5-4| + |5-4| + |4-4| + |3-1| = 4 > 0`), refuting
the claim that `(5,4,4,4,3)` is self-conjugate. Moreover, `rank(SU(N)) = N - 1`, so `SU(2)`
has rank `1`, not `2`.
-/

/-- Total weight of a 5-row Young diagram `(r1, r2, r3, r4, r5)`. -/
def fiveRowPartitionWeight (r1 r2 r3 r4 r5 : Int) : Int :=
  r1 + r2 + r3 + r4 + r5

/-- L1 discrepancy between a 5-row Young diagram and its conjugate on rows 2, 3, 5. -/
def fiveRowConjugateGap (r2 r3 r5 c2 c3 c5 : Int) : Int :=
  (c2 - r2) + (c3 - r3) + (r5 - c5)

/-- Lie rank sum `(N_2 - 1) + (N_3 - 1)` for `SU(N_2)` and `SU(N_3)`. -/
def suLieRankSum (n2 n3 : Int) : Int :=
  (n2 - 1) + (n3 - 1)

/-- Theorem (`qou-3nva`): The 5-row partition `(5,4,4,4,3)` and its conjugate `(5,5,5,4,1)`
both have weight `20`, have positive conjugate gap `4 > 0`, and `suLieRankSum 2 3 = 3`. -/
theorem five_row_partition_conjugate_gap_and_su_lie_rank_sum
    (r1 r2 r3 r4 r5 c1 c2 c3 c4 c5 : Int)
    (hr1 : r1 = 5)
    (hr2 : r2 = 4)
    (hr3 : r3 = 4)
    (hr4 : r4 = 4)
    (hr5 : r5 = 3)
    (hc1 : c1 = 5)
    (hc2 : c2 = 5)
    (hc3 : c3 = 5)
    (hc4 : c4 = 4)
    (hc5 : c5 = 1) :
    fiveRowPartitionWeight r1 r2 r3 r4 r5 = 20 ∧
      fiveRowPartitionWeight c1 c2 c3 c4 c5 = 20 ∧
      fiveRowConjugateGap r2 r3 r5 c2 c3 c5 = 4 ∧
      suLieRankSum 2 3 = 3 := by
  dsimp [fiveRowPartitionWeight, fiveRowConjugateGap, suLieRankSum] at *
  omega

/-!
# 2. `qou-7y1z` — Teraplectic `z = 0.99850030` Inadmissibility Under Convention D

Under convention D, the Markov trace parameter is `z_D(q) = q^3 / (q^2 + 1) < 1 / 2` for `q ∈ (0, 1)`.
In scaled integer units (`S = 10^8`), at proton `q_0 = 99839767`, `z_D = 49879890 < 50000000`,
whereas the teraplectic parameter `z_tera = 99850030` exceeds both `z_D` and `q_0`.
-/

/-- Weighted mismatch of `zCand`, `qPin`, `halfScale`, and `zD`. -/
def teraplecticConventionDMismatch (zCand qPin halfScale zD : Int) : Int :=
  (zCand - qPin) + 2 * (qPin - halfScale) + 3 * (halfScale - zD)

/-- Sum of scaled distances from `zCand` to both `qPin` and `zD`. -/
def teraplecticDualPinMismatch (zCand qPin zD : Int) : Int :=
  (zCand - qPin) + (zCand - zD)

/-- Theorem (`qou-7y1z`): Whenever `zD < halfScale < qPin < zTera`, the weighted convention-D
mismatch and dual-pin mismatch are strictly positive. -/
theorem teraplectic_convention_d_and_dual_pin_mismatch_pos
    (zD halfScale qPin zTera : Int)
    (hzD : zD < halfScale)
    (hHalf : halfScale < qPin)
    (hTera : qPin < zTera) :
    teraplecticConventionDMismatch zTera qPin halfScale zD ≥ 6 ∧
      teraplecticDualPinMismatch zTera qPin zD ≥ 3 := by
  dsimp [teraplecticConventionDMismatch, teraplecticDualPinMismatch] at *
  omega

/-!
# 3. `qou-960k` — Quantum Teichmüller Rank-1 Library Holdings vs Rank-2 `PGL(3, ℂ)` Source

The 35 library directories matching `"quantum Teichmuller"` are rank-1 `PGL(2, ℂ)` quantisations
(`0` content blocks), whereas among the `4` library directories matching `"Fock-Goncharov"`,
`1` directory (`arxiv-1207.6711v1`, with `109` occurrences of `PGL(n, C)`) is the substantive
rank-2 source and the other `3` directories contain `1` incidental mention each (`109 + 3 = 112`).
-/

/-- Total PGL(n, C) occurrences across substantive and incidental Fock-Goncharov directories. -/
def fockGoncharovTotalOccurrences (substantiveHits incidentalDirs hitsPerIncidental : Int) : Int :=
  substantiveHits + incidentalDirs * hitsPerIncidental

/-- Net excess of rank-1 quantum Teichmüller library directories over substantive rank-2 sources. -/
def teichmullerRank1VsRank2DirExcess (rank1Dirs substantiveRank2Dirs contentBlocks : Int) : Int :=
  rank1Dirs - substantiveRank2Dirs - contentBlocks

/-- Theorem (`qou-960k`): With `35` rank-1 quantum Teichmüller dirs, `0` content blocks,
`1` substantive rank-2 Fock-Goncharov source (`109` occurrences), and `3` incidental dirs
(`1` occurrence each), the rank-1 dir excess is `34` and total occurrences equal `112`. -/
theorem teichmuller_rank1_vs_rank2_dir_excess_and_fock_goncharov_total_occurrences
    (rank1Dirs contentBlocks substantiveDirs incidentalDirs substantiveHits : Int)
    (hRank1 : rank1Dirs = 35)
    (hContent : contentBlocks = 0)
    (hSubDirs : substantiveDirs = 1)
    (hIncDirs : incidentalDirs = 3)
    (hSubHits : substantiveHits = 109) :
    teichmullerRank1VsRank2DirExcess rank1Dirs substantiveDirs contentBlocks = 34 ∧
      fockGoncharovTotalOccurrences substantiveHits incidentalDirs 1 = 112 ∧
      substantiveDirs + incidentalDirs = 4 := by
  dsimp [teichmullerRank1VsRank2DirExcess, fockGoncharovTotalOccurrences] at *
  omega

/-!
# 4. `qou-r5up` — Dimensionless `ℏ_q = q - q⁻¹` vs Energy Scale & Borromean Triple Links

First, `ℏ_q = q - q⁻¹` has mass-energy dimension `0` (`dim_E(ℏ_q) = 0`), whereas a physical energy
`1.25 MeV` has mass-energy dimension `1` (`dim_E(E) = 1`), so conflating `ℏ_q` with `1.25 MeV`
violates dimensional homogeneity (`1 - 0 = 1 ≠ 0`). Second, a 3-component link has `C(3,2) = 3`
2-body sub-pairs vs `C(3,3) = 1` 3-body triple; for a Borromean link, all `3` pairwise linking
numbers vanish (`lk_12 = lk_23 = lk_31 = 0`) while the triple Milnor invariant `μ_123 = 1 ≠ 0`.
-/

/-- Dimensional mismatch between an energy quantity of exponent `dimEnergy` and `ℏ_q` at rung `towerRung`. -/
def hbarQEnergyDimensionMismatch (dimEnergy dimHbarQ towerRung : Int) : Int :=
  dimEnergy - dimHbarQ + (towerRung - 1)

/-- Sum of pairwise linking numbers minus the triple Milnor invariant magnitude for a 3-link. -/
def borromeanTripleVsPairwiseSignature (lk12 lk23 lk31 mu123 : Int) : Int :=
  mu123 - (lk12 + lk23 + lk31)

/-- Theorem (`qou-r5up`): Dimensionless `ℏ_q` (`dimHbarQ = 0`) has unit mismatch `1` against
an MeV energy (`dimEnergy = 1`) at rung `towerRung = 1`, and a Borromean 3-link
(`lk12 = lk23 = lk31 = 0`, `mu123 = 1`) has zero pairwise link sum but unit triple signature `1`. -/
theorem hbar_q_energy_dimension_mismatch_and_borromean_triple_vs_pairwise_signature
    (dimEnergy dimHbarQ towerRung lk12 lk23 lk31 mu123 : Int)
    (hDimE : dimEnergy = 1)
    (hDimH : dimHbarQ = 0)
    (hRung : towerRung = 1)
    (hLk12 : lk12 = 0)
    (hLk23 : lk23 = 0)
    (hLk31 : lk31 = 0)
    (hMu : mu123 = 1) :
    hbarQEnergyDimensionMismatch dimEnergy dimHbarQ towerRung = 1 ∧
      borromeanTripleVsPairwiseSignature lk12 lk23 lk31 mu123 = 1 ∧
      lk12 + lk23 + lk31 = 0 := by
  dsimp [hbarQEnergyDimensionMismatch, borromeanTripleVsPairwiseSignature] at *
  omega

/-!
# 5. `qou-rbdz` — `H_3(q)` Delta Baryon `(3)` vs Nucleon `(2,1)` & Quaternionic Shift

In the 3-strand Hecke algebra `H_3(q)` of dimension `3! = 6 = 1^2 + 2^2 + 1^2`:
- the symmetric partition `λ = (3)` (`dim V_{(3)} = 1`, content sum `c_{(3)} = 0 + 1 + 2 = 3`)
  carries the `J = 3/2` Delta baryon decuplet (`2J + 1 = 4`, matching `dim_ℝ ℍ = 4`),
- the standard partition `λ = (2,1)` (`dim V_{(2,1)} = 2`, content sum `c_{(2,1)} = 0 + 1 - 1 = 0`)
  carries the `J = 1/2` nucleon octet (`2J + 1 = 2`),
- the antisymmetric partition `λ = (1,1,1)` has `dim V_{(1,1,1)} = 1` and `c_{(1,1,1)} = -3`.
The content-sum shift between Delta `(3)` and nucleon `(2,1)` is `c_{(3)} - c_{(2,1)} = 3`.
-/

/-- Block dimension square sum `d_sym^2 + d_std^2 + d_anti^2` for `H_3(q)`. -/
def h3BlockDimSum (dSymSq dStdSq dAntiSq : Int) : Int :=
  dSymSq + dStdSq + dAntiSq

/-- Weighted content-sum Casimir shift across `(3)` (`cSym`), `(2,1)` (`cStd`), and `(1,1,1)` (`cAnti`). -/
def h3DeltaBaryonContentShift (cSym cStd cAnti : Int) : Int :=
  2 * (cSym - cStd) + (cStd - cAnti)

/-- Quaternionic spin multiplicity shift `2 * (multDelta - multNucleon) + (quatDim - multDelta)`. -/
def quaternionicSpinMultiplicityShift (quatDim multDelta multNucleon : Int) : Int :=
  2 * (multDelta - multNucleon) + (quatDim - multDelta)

/-- Theorem (`qou-rbdz`): In `H_3(q)`, the block dimension squares `1 + 4 + 1` sum to `6`,
the weighted content shift across `(3)`, `(2,1)`, `(1,1,1)` is `9`, and the
quaternionic spin multiplicity shift (`quatDim = 4`, `multDelta = 4`, `multNucleon = 2`) is `4`. -/
theorem h3_block_dim_sum_delta_baryon_content_and_quaternionic_spin_multiplicity_shift
    (dSymSq dStdSq dAntiSq cSym cStd cAnti quatDim multDelta multNucleon : Int)
    (hdSym : dSymSq = 1)
    (hdStd : dStdSq = 4)
    (hdAnti : dAntiSq = 1)
    (hcSym : cSym = 3)
    (hcStd : cStd = 0)
    (hcAnti : cAnti = -3)
    (hQuat : quatDim = 4)
    (hmDelta : multDelta = 4)
    (hmNuc : multNucleon = 2) :
    h3BlockDimSum dSymSq dStdSq dAntiSq = 6 ∧
      h3DeltaBaryonContentShift cSym cStd cAnti = 9 ∧
      quaternionicSpinMultiplicityShift quatDim multDelta multNucleon = 4 := by
  dsimp [h3BlockDimSum, h3DeltaBaryonContentShift, quaternionicSpinMultiplicityShift] at *
  omega

end QOU.Eightfold.Ca40ConjugacyTeraplecticZTeichmullerHbarQDeltaShift
