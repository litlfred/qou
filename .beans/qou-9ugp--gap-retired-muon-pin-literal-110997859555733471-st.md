---
# qou-9ugp
title: 'GAP: retired muon pin literal 1.10997859555733471 still hardcoded in ~180 computations/ producers outside the alpha cluster — all unstamped, invisible to the qou-3f7a anchor drain'
status: todo
type: task
tags:
    - sm-26
created_at: 2026-09-03T16:32:23Z
updated_at: 2026-09-03T16:32:23Z
---

Measured 2026-09-03 (session qou-ggdk) after the alpha-cluster tranche (PR #6519, commits 577367a41b f3bafde098 9218877589). Method: grep -rlF '1.10997859555733471' computations --include=*.py. The literal is the self-certified muon pin A, retired 2026-08-22/28 (fca08de7d2, 83bab99730); the live muon anchor is q_muon_at() over the CODATA-2022 lepton ratio (…56427390…) and the proton default is Q_50_DIGIT_STR. These producers are UNSTAMPED, so q0_anchor_consistency_audit files them under Q0_ANCHOR_MISSING and the corpus-wide drain qou-3f7a (which keys on stamps) cannot see them. Recipe that worked on the 14 alpha producers, in three shapes: (A) dead fallback 'q_at(50) if the substrate imports else the literal' → hard refusal, import q_at from q_parameter (NOT qou_substrate.constants, or the witness gets no stamp), declare the stem under physical_proton; (B) explicit proton-vs-muon comparison (E1) → both pins by name, mpf residuals via _precision.fmt, assertion booleans as strings, wb.save(q0_comparison(muon=…, proton=…, reason=…)); (C) muon-only with no comparison purpose → proton default (2026-08-30 rule), stamp proton. Per-producer: run, diff the witness with volatile keys masked, expect proton legs unchanged past the 9th digit and muon legs shifted by the −0.0769 ppb pin migration; precision-gates.sh --changed must show zero NEW-dirty and only drained entries. Never re-pin an anchor-DEFINING witness (q-pinning-50-digit). Land manifest + witnesses together (constraint 4). Scope by subdirectory (deltalambda/, qbeta/, …) — a tranche per directory keeps each PR reviewable.
