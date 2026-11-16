/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of the 5-bean cluster under `qou-2002`:
1. `qou-9ugp`: Retired muon pin literal `1.10997859555733471` dual-detector discovery
   partition (`137 = 48 + 89` live vs prose across 5 subdirectories), per-producer
   `Q_50_DIGIT_STR` anchor-resolution law, and import-cone staleness vs re-pin shift
   decomposition (`delta_total = delta_preexisting + delta_repin`).
2. `qou-bypn`: Triage of the 35 `ideal_muon` manifest entries (`35 = 7 + 15 + 13`,
   with the 13 no-source-rationale producers split `13 = 5 + 7 + 1` by `q0` acquisition
   route: Group A via `q_parameter`, Group B direct `q-pinning-50-digit.witness.json`
   read, Group C via `load_q_50dps`), and the E1/E2 exception indicator law.
3. `qou-c4kv`: Class-(a) `q0` literal transcription three-way split (`45 = 8 + 32 + 5`
   and ratchet drop `71 - 10 = 61`), two-step `B -> A -> C` vs direct `B -> C` migration
   additivity, and frozen-companion straddle residual when `tr_M(q_B)` is held fixed.
4. `qou-9idb`: `rho_f_categorical_probe` mirror anchor-straddle (`ideal_muon` consumer
   reading proton `markov-peel-atomic-tr-m.witness.json`) coupled behind the `17 -> 44`
   raw-float64 drain (`27 = 9 * 3` additional `(true_rho, delta, err_pct)` fields),
   and exact percentage-error scoring identity.
5. `qou-515v`: Root vendored `ame2020.json` float64 binding energy conversion law
   (`B_MeV(B_keV) = B_keV / 1000`), linear propagation of JSON float64 artifact tails
   (`eps_MeV = eps_keV / 1000`), and the `3558 = 640 + 2918` visible-tail vs clean-decimal
   partition with the exact `6Li` (`31993.9872 - 31993.987199999996 = 4e-12 keV`) witness.
-/
import Mathlib.Tactic

namespace QOU.MassTheory.AnchorManifestTriageAndAmeFloatDrain

/-! ### 1. `qou-9ugp`: Retired Muon Pin Discovery Partition, `Q_50_DIGIT_STR` Resolution & Drift Split -/

/-- Dual-detector discovery sum across a five-tranche partition (`qou-9ugp`). -/
def fiveTrancheCountSum (c1 c2 c3 c4 c5 : ℚ) : ℚ :=
  c1 + c2 + c3 + c4 + c5

/-- Exact live vs prose grep decomposition across `deltalambda`, `qbeta`, `audits`,
`substrate`, and `probes`:
live `0 + 31 + 11 + 6 + 0 = 48`, prose `39 + 14 + 6 + 4 + 26 = 89`, total `48 + 89 = 137` (`qou-9ugp`). -/
theorem retired_muon_pin_live_vs_prose_partition :
    fiveTrancheCountSum 0 31 11 6 0 = 48 ∧
    fiveTrancheCountSum 39 14 6 4 26 = 89 ∧
    fiveTrancheCountSum 0 31 11 6 0 + fiveTrancheCountSum 39 14 6 4 26 = 137 := by
  unfold fiveTrancheCountSum
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- Per-producer anchor resolution of `Q_50_DIGIT_STR` (`qou-9ugp` Correction 2):
`q_parameter` binds `Q_50_DIGIT_STR` to `q_muon` when `m = 1` (stem in `ideal_muon`)
and to `q_proton` when `m = 0` (stem not in `ideal_muon`). -/
def q50DigitResolved (m qMuon qProton : ℚ) : ℚ :=
  m * qMuon + (1 - m) * qProton

/-- Exact difference between the `ideal_muon`-listed (`m = 1`) and unlisted (`m = 0`)
bindings of `Q_50_DIGIT_STR`, and exact specialization at `m = 1` and `m = 0` (`qou-9ugp`). -/
theorem q50DigitResolved_branch_law (qMuon qProton : ℚ) :
    q50DigitResolved 1 qMuon qProton = qMuon ∧
    q50DigitResolved 0 qMuon qProton = qProton ∧
    q50DigitResolved 1 qMuon qProton - q50DigitResolved 0 qMuon qProton = qMuon - qProton := by
  unfold q50DigitResolved
  refine ⟨by ring, by ring, by ring⟩

/-- Total witness drift between a committed witness (`cpCommitted`), the unmodified
HEAD producer re-run (`cpHead`), and the re-pinned run (`cpRepinned`) (`qou-9ugp`). -/
def witnessDriftDecomposition (cpCommitted cpHead cpRepinned : ℚ) : ℚ :=
  (cpHead - cpCommitted) + (cpRepinned - cpHead)

/-- Exact additive decomposition of total witness change into pre-existing import-cone
staleness (`cpHead - cpCommitted`) plus the isolated pin shift (`cpRepinned - cpHead`),
together with the pin sensitivity identity (`qou-9ugp`). -/
theorem witness_drift_and_pin_sensitivity_identity
    (cpCommitted cpHead cpRepinned qMuon qProton : ℚ)
    (hq : qMuon - qProton ≠ 0) :
    witnessDriftDecomposition cpCommitted cpHead cpRepinned = cpRepinned - cpCommitted ∧
    ((cpRepinned - cpHead) / (qMuon - qProton)) * (qMuon - qProton) = cpRepinned - cpHead := by
  unfold witnessDriftDecomposition
  refine ⟨by ring, ?_⟩
  field_simp [hq]

/-! ### 2. `qou-bypn`: `ideal_muon` 35-Stem Triage Partition & E1/E2 Ruling Indicator Law -/

/-- Three-way partition of the `ideal_muon` manifest (`qou-bypn`):
justified in `qou-1c4y` (`j`), source-documented rationale (`s`), and no-source-rationale
triage set (`u`). -/
def idealMuonManifestTotal (j s u : ℚ) : ℚ :=
  j + s + u

/-- Exact numerical partition of the 35 `ideal_muon` stems:
`7 = 3 + 2 + 1 + 1` justified in `qou-1c4y`, `15` carrying in-source rationale, and
`13 = 5 + 7 + 1` carrying no in-source rationale split into Group A (`5` via `q_parameter`),
Group B (`7` direct witness read), and Group C (`1` via `load_q_50dps`) (`qou-bypn`). -/
theorem ideal_muon_manifest_triage_partition :
    (3 : ℚ) + 2 + 1 + 1 = 7 ∧
    (5 : ℚ) + 7 + 1 = 13 ∧
    idealMuonManifestTotal 7 15 13 = 35 := by
  unfold idealMuonManifestTotal
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- Effective anchor resolved for a producer given routing indicator `r` (`r = 1` when
routed through `q_parameter`, `r = 0` when reading `q-pinning-50-digit.witness.json`
directly as in Group B) and manifest membership `m` (`qou-bypn`). -/
def groupABEffectiveAnchor (r m qMuon qProton : ℚ) : ℚ :=
  r * (m * qMuon + (1 - m) * qProton) + (1 - r) * qMuon

/-- Removing a stem from `ideal_muon` (`m : 1 -> 0`) shifts a Group A producer (`r = 1`)
by `qProton - qMuon`, whereas a Group B producer (`r = 0`, direct witness read) has zero
shift until routed through `q_parameter` (`qou-bypn`). -/
theorem groupA_vs_groupB_manifest_removal_shift (m qMuon qProton : ℚ) :
    groupABEffectiveAnchor 1 0 qMuon qProton - groupABEffectiveAnchor 1 1 qMuon qProton =
      qProton - qMuon ∧
    groupABEffectiveAnchor 0 m qMuon qProton = qMuon := by
  unfold groupABEffectiveAnchor
  refine ⟨by ring, by ring⟩

/-- Exception indicator law for the 2026-08-30 owner ruling (`qou-bypn`):
a producer is assigned `qMuon` iff at least one of exception E1 (`e1 = 1`, explicit
muon-vs-proton comparison) or exception E2 (`e2 = 1`, ideal CAL-1/2/3 mathematics) holds,
and `qProton` when neither holds (`e1 = 0, e2 = 0`). -/
def rulingAnchorFromExceptions (e1 e2 qMuon qProton : ℚ) : ℚ :=
  (1 - (1 - e1) * (1 - e2)) * qMuon + (1 - e1) * (1 - e2) * qProton

/-- When neither E1 nor E2 applies (`e1 = 0, e2 = 0`, as in `hadron_knot_table.py`),
the ruling assigns `qProton`; when either E1 or E2 holds (`e1 = 1` or `e2 = 1`),
it assigns `qMuon` (`qou-bypn`). -/
theorem ruling_anchor_exception_cases (e1 e2 qMuon qProton : ℚ) :
    rulingAnchorFromExceptions 0 0 qMuon qProton = qProton ∧
    rulingAnchorFromExceptions 1 e2 qMuon qProton = qMuon ∧
    rulingAnchorFromExceptions e1 1 qMuon qProton = qMuon := by
  unfold rulingAnchorFromExceptions
  refine ⟨by ring, by ring, by ring⟩

/-! ### 3. `qou-c4kv`: Class-(a) Literal Transcription Split, Two-Step Re-Pin & Frozen Straddle -/

/-- Linearized observable response `f(q, trM) = f0 + sQ * q + sTr * trM` depending on both
the direct `q0` parameter and a companion trace input `trM` (`qou-c4kv`). -/
def coupledAnchorObservable (f0 sQ sTr q trM : ℚ) : ℚ :=
  f0 + sQ * q + sTr * trM

/-- Exact class-(a) literal transcription ledger counts:
`8` migrated no-witness producers + `32` cost-deferred witness-emitting producers +
`5` correctness-blocked frozen-companion producers = `45` (and `32 + 5 = 37` remaining;
ratchet `71 - 10 = 61`) (`qou-c4kv`). -/
theorem class_a_literal_transcription_partition :
    (8 : ℚ) + 32 + 5 = 45 ∧
    (32 : ℚ) + 5 = 37 ∧
    (71 : ℚ) - 10 = 61 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩

/-- Two-step migration `B -> A -> C` equals the direct migration `B -> C` on any
coupled observable when both `q` and `trM` move together, whereas moving `q` from `qB`
to `qC` while holding `trM = trMB` frozen (the 5 correctness cases in `qou-c4kv`) leaves
an exact straddle residual `-sTr * (trMC - trMB)`. -/
theorem two_step_migration_and_frozen_companion_straddle
    (f0 sQ sTr qB qA qC trMB trMA trMC : ℚ) :
    (coupledAnchorObservable f0 sQ sTr qA trMA - coupledAnchorObservable f0 sQ sTr qB trMB) +
      (coupledAnchorObservable f0 sQ sTr qC trMC - coupledAnchorObservable f0 sQ sTr qA trMA) =
      coupledAnchorObservable f0 sQ sTr qC trMC - coupledAnchorObservable f0 sQ sTr qB trMB ∧
    (coupledAnchorObservable f0 sQ sTr qC trMB - coupledAnchorObservable f0 sQ sTr qB trMB) -
      (coupledAnchorObservable f0 sQ sTr qC trMC - coupledAnchorObservable f0 sQ sTr qB trMB) =
      -sTr * (trMC - trMB) := by
  unfold coupledAnchorObservable
  refine ⟨by ring, by ring⟩

/-! ### 4. `qou-9idb`: `rho_f_categorical_probe` Mirror Straddle & `17 -> 44` Float64 Drain Gate -/

/-- Percentage error scoring formula `err_pct = (rhoPred - trueRho) / trueRho * 100`
in `rho_f_categorical_probe.py` (`qou-9idb`). -/
def rhoScoreErrPct (rhoPred trueRho : ℚ) : ℚ :=
  (rhoPred - trueRho) / trueRho * 100

/-- Raw-float64 field count on re-running `rho_f_categorical_probe.py` before draining:
`baseFields + kEntries * 3` where each scored entry emits `3` float fields
(`true_rho`, `delta`, `err_pct`) (`qou-9idb`). -/
def rhoProbeRawFloatCount (baseFields kEntries : ℚ) : ℚ :=
  baseFields + 3 * kEntries

/-- Exact `17 -> 44` raw-float64 ratchet expansion (`17 + 3 * 9 = 44`, difference `27`),
exact proton-to-muon `tr_M_proton` shift (`1.06530622861 - 1.06530614425 = 8436 / 10^11`),
and percentage-error shift identity between the muon twin (`rhoMuon`) and proton reference
(`rhoProton`) (`qou-9idb`). -/
theorem rho_f_categorical_straddle_and_float_drain_identity
    (rhoMuon rhoProton trueRho : ℚ) (ht : trueRho ≠ 0) :
    rhoProbeRawFloatCount 17 9 = 44 ∧
    rhoProbeRawFloatCount 17 9 - 17 = 27 ∧
    (106530622861 : ℚ) / 100000000000 - 106530614425 / 100000000000 = 8436 / 100000000000 ∧
    rhoScoreErrPct rhoMuon trueRho - rhoScoreErrPct rhoProton trueRho =
      (rhoMuon - rhoProton) / trueRho * 100 := by
  unfold rhoProbeRawFloatCount rhoScoreErrPct
  refine ⟨by norm_num, by norm_num, by norm_num, ?_⟩
  field_simp [ht]
  ring

/-! ### 5. `qou-515v`: Vendored `ame2020.json` Float64 Artifact Tail Propagation & `6Li` Witness -/

/-- Conversion from total binding energy in keV (`bKeV`) to MeV (`bKeV / 1000`) in
`codata_constants._ame_binding_mev` (`qou-515v`). -/
def ameBindingMeVFromKeV (bKeV : ℚ) : ℚ :=
  bKeV / 1000

/-- Linear propagation of a JSON float64 serialization artifact tail `epsKeV` from
`ame2020.json` into downstream MeV validation constants (`qou-515v`). -/
theorem ame_binding_mev_artifact_tail_propagation (bKeVExact epsKeV : ℚ) :
    ameBindingMeVFromKeV (bKeVExact + epsKeV) - ameBindingMeVFromKeV bKeVExact =
      epsKeV / 1000 := by
  unfold ameBindingMeVFromKeV
  ring

/-- Exact `ame2020.json` corpus partition (`3558 = 640 + 2918`, with `640` entries carrying
visible float64 artifact tails) and exact `6Li` (`Z = 3, A = 6`) artifact tail identity:
`31993.9872 - 31993.987199999996 = 4 * 10⁻¹² keV`, producing a `4 * 10⁻¹⁵ MeV` shift in
`AME_B_LI6_MEV_VALIDATION` (`qou-515v`). -/
theorem ame2020_corpus_and_li6_artifact_tail_exact :
    (640 : ℚ) + 2918 = 3558 ∧
    (31993987200000000 : ℚ) / 1000000000000 - 31993987199999996 / 1000000000000 =
      4 / 1000000000000 ∧
    ameBindingMeVFromKeV (31993987200000000 / 1000000000000) -
      ameBindingMeVFromKeV (31993987199999996 / 1000000000000) =
      4 / 1000000000000000 := by
  unfold ameBindingMeVFromKeV
  refine ⟨by norm_num, by norm_num, by norm_num⟩

end QOU.MassTheory.AnchorManifestTriageAndAmeFloatDrain
