---
# qou-1w90
title: 'env guard: _version_tuple orders opaque hex hashes, so pyhecke_native_build flags a false ''downgrade'''
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:15:47Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

- **Round 92 (`litlfred/qou#8416`)**: Advanced in `feat/round92-jetmono-jetsign-kzratio-kzunit-kappacorr-43c1` (Commit 1 `b85484a2b9309c11a8832becee2e728a03219677`, Commit 2 `de3ca907bd3d3c7bb260ce5aa08259ade30c6cc9`, probe sha256 `7a5dfeb80aacf1b23a7e663221ecc9f97b20abf96256db6ae736e9dd7742c6f9`).

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** On main, `tools/qou-substrate/python/qou_substrate/witness.py` has `_NON_ORDINAL_ENV_KEYS = {pyhecke_native_build, platform, stdlib_only, note}`, and `_environment_delta` skips those keys in both the downgraded and upgraded lists, so a changed build hash is no longer ordered. Read at main `2ae54ab401`.
