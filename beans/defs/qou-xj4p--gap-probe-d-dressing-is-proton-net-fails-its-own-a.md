---
# qou-xj4p
title: 'GAP: probe_d_dressing_is_proton_net fails its own assertion after refresh'
status: todo
type: task
created_at: 2026-11-24T20:49:37Z
updated_at: 2026-11-24T20:49:37Z
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
