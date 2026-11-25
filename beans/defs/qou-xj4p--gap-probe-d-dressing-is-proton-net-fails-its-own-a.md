---
# qou-xj4p
title: 'GAP: probe_d_dressing_is_proton_net fails its own assertion after refresh'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T20:49:37Z
updated_at: 2026-11-25T10:15:40Z
---

Found by the 2026-11-24 paper-compute refresh (PR #9395, branch `claude/compute-refresh-2026-11-24`, main `dd5f163edbd`). `computations/probes/probe-d-dressing-is-proton-net.witness.json` was self-stale. Re-running the current producer `computations/probes/probe_d_dressing_is_proton_net.py` (exit 0) writes `allPassed: false`. The refreshed witness was **NOT committed** (owner decision 2026-11-24, "D2 commit all 42": hold producers that fail their own assertion). Main still carries the old passing witness.

Before (committed) → after (fresh run):

- assertion 1 `binding_candidate_subpercent` (`B_D = E₀·net(p)·Δtr` vs AME2020): **True → False**
- `data/numerical/B_cand_E0_netp_dtr_MeV`: `2.23094304357897479` → `0.55119272426415506`
- `data/numerical/B_cand_err_vs_AME_pct`: `0.28665559959396997` → `-75.22246250688538`
- `data/numerical/Delta_tr`: `0.59516889262234348652` → `0.14704667798040846911` (factor ~4.05)
- `data/numerical/B_via_kashiwara_qbeta_MeV`: `2.2272095331670547` → `0.550601110315296747`
- `data/numerical/Qbeta_kashiwara_MeV`: `0.782334386518171885` → `0.782804713582601608`

The deuteron candidate falls from a 0.29 % hit to a 75 % miss. The driver is `Delta_tr`, which shrank by about 4x, so an upstream trace or word changed. Which one is not established here. Under the anti-fit rule the earlier 0.29 % should not be treated as evidence that the old input was right.

Log: `/tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/logs/probe_d_dressing_is_proton_net.py.log`. It is in session scratchpad and may not survive; re-run with `PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python python3 -u computations/probes/probe_d_dressing_is_proton_net.py`.

Next honest step: trace where `Delta_tr` comes from and which upstream change moved it, then decide whether the probe's conclusion is withdrawn or its input is wrong.

## 2026-11-24 root cause (agent, session 01Eucf, claimed)
Delta_tr = tr_free - tr_atom from tr_m_atom_zn(1,1). Live (borromean word) gives 0.147046678; with atom_braid_word_3A(intra_order='grouped') it gives 0.556544660, against the old witness value 0.5952. About 93% of the move is the 2026-09-05 word ruling (7db032fb482, qou-hu1f); the remaining ~7% is unattributed (the old witness, 2026-07-04, predates the convention-D cascade). The input is correct per the corpus, so the 0.29% deuteron hit was a property of the superseded word: an honest negative, and the probe's conclusion should be withdrawn.


## 2026-11-25 attribution COMPLETE (agent, session 01Eucf, branch claude/xj4p-delta-tr-attribution-20261125)
Reproduced the old Delta_tr 0.59516889262234348652 exactly in a worktree at 581c176f480 (the witness's rewritten commitSha 4dfe838c398). E0 and net(p) did not move (B/(net_p*Dtr) = 4.18598136329447589 in both witnesses). Path old -> live, each step measured, mpmath 70 dps:
- (c) float64-built interface d -> 70-digit: -1.35e-20.
- (b) y_lambda pin retired muon -> proton: -1.415e-9. The old run read y_lambda from the muon-built y-lambda-at-q0 cache through the trivially satisfied |q - Q| < 1e-12 gate: a layer straddle (y at muon, chi at proton). CODATA-2018 and CODATA-2022 muon pins also move Dtr only in the 10th digit.
- (a) Markov convention C -> D (2026-08-09): -0.0386242308025191344 (8.62% of the total move; 4.80% in log terms). THIS is the previously unattributed ~7%.
- word ruling grouped -> alternating (2026-09-05): -0.409497982424029743 (91.38%; 95.20% log).
Not additive: in the other order, the word step under C is -0.49643 and C->D on the alternating word is +0.04830 (opposite sign). Shares are path-dependent.
B_cand vs AME by configuration: C+grouped +0.287% (old); D+grouped -6.22%; C+alternating -83.36%; D+alternating (canonical) -75.22%. The sub-percent hit holds only on the superseded word under the excised convention.
Script + RESULTS: computations/probes/probe_d_dressing_is_proton_net/attribution/. Next step is an owner decision: withdraw the probe's conclusion, or re-scope it. Kept in-progress until then.
