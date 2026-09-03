---
# qou-4bef
title: 'GAP: alpha_EM ladder producers hardcode q0 (muon literal = retired pin A), emit float64 ppb fields, and honest_status.not_at_target is stale muon-framed'
status: todo
type: task
created_at: 2026-09-03T05:00:50Z
updated_at: 2026-09-03T05:00:50Z
parent: qou-ggdk
---

Measured 2026-09-03 (session qou-ggdk, compute-precision-auditor). computations/alpha_em_form_ladder_probe.py:63-66 and alpha_em_schwinger_ladder_probe.py:47 hardcode ANCHORS = {muon: 1.10997859555733471 (RETIRED pin A), proton: 1.109978582751380808}; neither imports q_parameter; neither stem is in q0_anchor_manifest.json; invisible to q0_anchor_consistency_audit (filed Q0_ANCHOR_MISSING), hardcoded_literal_audit (keys on codata_constants.py only) and the manifest. At the live CODATA-2022 muon anchor the quadratic residual is 81.0357 ppb, not 80.51 (verdicts unchanged). def ppb(v): return float(...) makes all 11 residual/sigma fields raw float64 (baselined 6+5 in raw-float64-baseline.json, drain owner PR #4677). /data/honest_status/not_at_target still reads 'best ~81 ppb muon = ~537x sigma_a' (f-string on fp_muon, producer line ~154) while the assertion strings are proton-framed. Fix at the producer: read q_at()/q_muon_at() by name (comparison producer → physical_proton + per-process override per AGENTS.md constraint 3), return mpf and serialize via _precision.fmt, regenerate honest_status. FormLadderAnchorDominance.lean:208,211 carry the float64 reprs as exact ℝ literals — update in the same change. Tower status: ORDER-ZERO-ONLY (truncated ladder). Blocked by nothing; touches recorded numbers, so needs owner sign-off before re-pinning.
