---
# qou-h1h5
title: 'GAP: qbeta_cos_resummation_d_probe fails its own assertion after refresh'
status: completed
type: task
priority: normal
created_at: 2026-11-24T20:49:38Z
updated_at: 2026-11-25T01:04:07Z
---

Found by the 2026-11-24 paper-compute refresh (PR #9395, branch `claude/compute-refresh-2026-11-24`, main `dd5f163edbd`). `computations/qbeta/qbeta-cos-resummation-d.witness.json` was self-stale. Re-running the current producer `computations/qbeta/qbeta_cos_resummation_d_probe.py` **exits 1** and writes `allPassed: false` ("5 assertions, FAILURES"). The refreshed witness was **NOT committed** (owner decision 2026-11-24, "D2 commit all 42": hold producers that fail their own assertion).

Before (committed) → after (fresh run):

- assertion 1 `reproduces_block_published_ppm` (expected 0, tolerance 0.051; "residuals quoted to 0.1 ppm in the block"): computed `0.04662413485460241588` → `0.23497564896469417239`, **passed True → False**
- assertion 4 computed: `0.0` → `1.77e-74` (precision floor, still passes)
- cell residuals moved by ~0.1–0.2 ppm, e.g. `cells/0/eps_Q_ppm` `-431571.753375865` → `-431571.861861588`; `cells/2/eps_Q_ppm` `1677.567847475` → `1677.376675211`; `cells/4/eps_Q_ppm` `306.048717722` → `305.857807215`

The movement (~0.19 ppm in `eps_Q` on every cell) matches the shift a muon-anchor re-pin produces. That is consistent with the probe's inputs having moved under it while its content block still quotes the old ppm figures. Not established: whether the block or the producer is the one to correct. Related: `qou-zuva` (M6 redo of the q-beta cos-resummation family in convention D).

Log: `/tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/logs/qbeta_cos_resummation_d_probe.py.log`. It is in session scratchpad and may not survive; re-run with `PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python python3 -u computations/qbeta/qbeta_cos_resummation_d_probe.py`.

Next honest step: identify which input moved (anchor vs `E₀`), then update the block's quoted ppm from the producer. Do not widen the 0.051 tolerance to fit.

## 2026-11-24 root cause (agent, session 01Eucf, claimed)
Not the anchor (proton pin unchanged) and not E0: every Q value is identical (max |value-published| = 4.65e-11). Only the reference moved: Q_BETA_MEV went from 0.78233341 (AME2020) to 0.78233355931 (CODATA 2022) in a887b738d50 (owner ruling 2026-11-20, cal-3-q-beta.witness.json), which is +0.19 ppm on every eps_Q. Corpus-derived fix (exemption 2): update the block's published ppm and its stated 'CODATA 0.78233341' to the producer output. Do not widen the 0.051 tolerance.

## 2026-11-24 fixed in PR https://github.com/litlfred/qou/pull/9401 (cf53560dce3)
The block, its table-data and the probe's PUBLISHED_PPM now carry the producer's output against CODATA 2022: -431571.9 / -432037.7 / +1677.4 / +856.6 ppm; current-pin C cell +305.86. Tolerance 0.051 unchanged; the probe passes 5/5 (max offset 0.047). Complete when merged.

Merged in #9401 (2026-11-25).
