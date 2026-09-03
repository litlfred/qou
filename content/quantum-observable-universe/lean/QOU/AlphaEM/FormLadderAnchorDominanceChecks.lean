/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.AlphaEM.FormLadderAnchorDominance
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# α_EM form ladder — recorded-witness arithmetic (NOT mathematics)

Companion to `QOU.AlphaEM.FormLadderAnchorDominance`.  Everything in this file
is a **recorded decimal** — witness output or a CODATA reference — and a
`norm_num` check on it.  Nothing here is derived; the mathematics (Part 0–2 of
the companion) is stated there over generic rings with no empirical input, and
this file only instantiates it on the numbers
`computations/alpha-em-form-ladder.witness.json` recorded.

Split out on 2026-09-03 (bean `qou-08zf`) so that the formal statements carry
no empirical literal (owner preference, stricter than AGENTS.md §7c's
"CODATA → `ℝ`" row).  The names are unchanged from their previous location in
the companion, under the `Checks` namespace.

`scripts/check-sidecars.sh` flags this file as "ℝ in type but no archimedean
construct".  That is expected and not a defect: every declaration here is a
recorded decimal, and a decimal literal is the §7c CODATA/experimental row —
`ℝ` is the correct type for it, and generalising to `{R}` would only hide the
fact that these are measured numbers.

**Provenance of every number, so nobody "corrects" one silently:**

| declaration | value | what it is |
|---|---:|---|
| `predProton` | 137.035999313169 | witness fixed point, proton anchor |
| `predMuon` | 137.036010188814 | witness fixed point, muon anchor — at the **live** CODATA-2022 muon derivation (`q_muon_at`), regenerated 2026-09-03 on owner authorisation (bean `qou-4bef`). Until then the witness carried the **retired** frozen pin `A` (`1.1099785955573347…`) and this row read 137.036010116763 / 80.5100 ppb; the retired-pin values are kept here as history, not as data. |
| `refCodata` | 137.035999084 | the CODATA-2018 value the witness scored against (the table now carries 137.035999177; bumping this alone would desynchronise it from the residuals below) |
| `residProtonPpb` | 1.6723270456964245 | witness residual, proton anchor (20-digit `mpf` serialisation; the pre-2026-09-03 witness recorded the float64 repr 1.6723270482102428 from a 19-figure proton literal — moved at the 9th significant digit) |
| `residMuonPpb` | 81.035740382392585 | witness residual, muon anchor, live CODATA-2022 derivation (retired pin `A` gave 80.50996334188073; see `predMuon`) |
| `residLeadingOnlyPpb` | −1552805.3 | residual of the leading term `q[9]_q[10]_q` alone |
-/

namespace QOU.AlphaEM.FormLadder.Checks

/-- Recorded fixed point at the proton anchor (`alpha-em-form-ladder.witness.json`). -/
def predProton : ℝ := 137.035999313169  -- noqa: P31 - RECORDED witness output, not CODATA

/-- Recorded fixed point at the muon anchor — live CODATA-2022 muon derivation,
regenerated 2026-09-03 (owner authorisation, bean `qou-4bef`); the retired pin `A`
value 137.036010116763 is history only.  See the module docstring. -/
def predMuon : ℝ := 137.036010188814  -- noqa: P31 - RECORDED witness output, not CODATA

/-- The reference value the witness scores against (CODATA-2018 Cs-recoil).  It
must track `alpha-em-form-ladder.witness.json`, not the live table. -/
def refCodata : ℝ := 137.035999084  -- noqa: P31

/-- Recorded proton-anchored residual, in ppb (regenerated 2026-09-03 from the
50-digit proton string; the 19-figure literal gave 1.6723270482102428). -/
def residProtonPpb : ℝ := 1.6723270456964245

/-- Recorded muon-anchored residual, in ppb — live CODATA-2022 muon derivation,
regenerated 2026-09-03 (the retired pin `A` gave 80.50996334188073). -/
def residMuonPpb : ℝ := 81.035740382392585

/-- Residual of the leading term `q[9]_q[10]_q` alone, in ppb — the figure that
must **not** be quoted as the form's accuracy. -/
def residLeadingOnlyPpb : ℝ := -1552805.3

/-- The two recorded predictions are distinct, so the generic exclusion applies. -/
theorem predictions_differ : predProton ≠ predMuon := by
  unfold predProton predMuon; norm_num

/-- **The generic exclusion, instantiated on the recorded pair.**  No affine
anchor-blind correction with `s ≠ 0` brings the recorded proton and muon
predictions together — `no_anchor_blind_affine_correction_closes_gap` at
`R = ℝ` on `predictions_differ`. -/
theorem recorded_anchors_not_closed_by_affine (s c : ℝ) (hs : s ≠ 0) :
    s * predProton + c ≠ s * predMuon + c :=
  no_anchor_blind_affine_correction_closes_gap predProton predMuon s c predictions_differ hs

/-- **The anchor gap dominates the proton-anchored residual** — by more than
`40×` on the recorded values (measured ratio ≈ 47).  The quantitative form of
"the pin choice is not bookkeeping". -/
theorem anchor_gap_dominates_proton_residual :
    residMuonPpb - residProtonPpb > 40 * residProtonPpb := by
  unfold residMuonPpb residProtonPpb; norm_num

/-- **The leading term alone misses by more than `5·10⁵×` the full form's
proton-anchored residual** (measured ratio ≈ 9.3·10⁵). -/
theorem leading_term_residual_dwarfs_full_form :
    -residLeadingOnlyPpb > 500000 * residProtonPpb := by
  unfold residLeadingOnlyPpb residProtonPpb; norm_num

end QOU.AlphaEM.FormLadder.Checks
