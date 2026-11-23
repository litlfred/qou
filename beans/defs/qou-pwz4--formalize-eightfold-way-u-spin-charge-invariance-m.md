---
# qou-pwz4
title: Formalize Eightfold Way U-Spin Charge Invariance, Microscopic Coleman-Glashow Borromean V3 QED Identity, & Lambda-Sigma0 e_{(2,1)} Sub-Projector Resolution
status: in-progress
type: task
priority: high
created_at: 2026-11-18T22:15:53Z
updated_at: 2026-11-23T23:06:44Z
parent: qou-rgj8
---

Formalize QOU/Eightfold/USpinColemanGlashowLambdaSigma.lean (0 sorry, 0 axiom): (1) 3-flavor quark charges (q_u = +2/3, q_d = -1/3, q_s = -1/3) and exact U-spin charge invariance q_d = q_s across the three U-spin doublets (p <-> Sigma^+ = uud <-> uus, n <-> Xi^0 = udd <-> uss, Sigma^- <-> Xi^- = dds <-> dss); (2) Microscopic 3-strand adjacent-charge matrices Q_{12}+Q_{23} on all 6 outer baryon-octet states, proving Q_{Adj}(Sigma^+) = Q_{Adj}(p), Q_{Adj}(Xi^0) = Q_{Adj}(n), Q_{Adj}(Sigma^-) = Q_{Adj}(Xi^-) = (2/9)I_3, and proving that the connected 4th-order Borromean V^3 QED trace satisfies the Coleman-Glashow identity (Delta m_QED(p-n) - Delta m_QED(Sigma^+-Sigma^-) + Delta m_QED(Xi^0-Xi^-) = 0) at the concrete 3x3 matrix operator level while each individual doublet splitting is non-zero for q != +-1; (3) Operator resolution of the Lambda-Sigma^0 (0,0) weight degeneracy (OctetWeightDegeneracy.lean) via orthogonal rank-1 I=1 (Sigma^0) and I=0 (Lambda) sub-idempotents inside the 2D mixed-symmetry projector e_{(2,1)}.

## 2026-11-23 — Worker 20 (qou-8fw2) claimed on branch claude/sm8w-eightfold-wire-clasp-lambda-sigma-20261123 (under parent package qou-8fw2).



---
**Worker 20 () Delivery — 2026-11-23 (, Issue #9222, PR #9223):**
- Commits: `3c6d1b9dc71` (pre-registration), `39a4158b03b` (`HyperbolicMesonClaspAndDiquarkSplit.lean`, `QOU.lean` 22-module wiring, Ch. 10 content sync, 80-dps probe), `e28c1294e44` (witness stamp `allPassed: True`, `stale: False`, `q0Anchor: proton`).
- Lean 4 (`QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean`): 0 errors, 0 warnings, 0 placeholders, standard axioms `[propext, Classical.choice, Quot.sound]` only.
- 80-dps Probe & Witness (`computations/probes/sm8w_eightfold_clasp_diquark_gmo/`): passed `probe-float64-guard --diff`, `witness_raw_float64_audit --strict`, `mpf_context_dps_audit --strict`, and `lean-orphan-audit --diff`.
- Proved `projDiquark_complete_orthogonal_idempotents`, `jm2_jm3_comm_and_diquark_split`, and `trace_projDiquark_V_and_V3_split` on `S^{(2,1)}` (agreeing with 3D weight-space `eLambda`, `eSigma0`), breaking `m_Lambda = m_{Sigma^0}` weight-only degeneracy without free parameters: `tr(P_Lambda V^3) - tr(P_{Sigma^0} V^3) = (q - q^{-1})^3 (q^2 + q^{-2})[3]_q / [2]_q = +0.02826481` at `q_0`. Kept `in-progress` on the honest quantitative gap (`31.535 MeV`, `-59.0%` vs PDG `76.959 MeV`; single-crossing `q_0` gives `122.701 MeV`, `+59.4%`).
