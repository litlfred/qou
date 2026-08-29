---
# qou-snh8
title: 'INFRA: lake-cache/qou paper-olean branch has ZERO SchurWeyl oleans — needs clean reseed'
status: todo
type: task
priority: normal
created_at: 2026-08-29T06:37:26Z
updated_at: 2026-08-29T06:38:24Z
---

Found while landing the M1 arc (PR #5960). The whole QOU.SchurWeyl.* cone (66 files: Wenzl/Ocneanu/Markov normalisation incl. the proved general telescope sum_dim_wenzlWeight_eq_one) is ABSENT from lake-cache/qou-v4-24-0, so every agent touching it must rebuild from source (3308-job lake build; cache get 403s in-sandbox). A safe reseed is NOT possible from a verification sandbox: scripts/lean-olean-cache-seed.sh (correctly) refuses a partial/trace-mixed tree -- it needs a clean full 'lake build QOU UGB Fred2005' on a uniformly-traced pinned mathlib, then SEED_PAPER=1. Proper path: run .github/workflows/lake-cache-refresh.yml (service script lake-cache.sh, tars whole .lake) on a machine with working cache-get, OR a full local build where disk+time allow. Do NOT force-override the seed guard (SEED_ALLOW_NO_MATHLIB / bare --push) -- it publishes a mathlib-less branch that makes restores report 'Lean unavailable'.
