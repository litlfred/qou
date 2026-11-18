---
# qou-8foz
title: 'Registry stale: pyhecke.gram.z migrated to D, registry still records C'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T12:54:16Z
updated_at: 2026-10-04T15:23:21Z
parent: qou-5vkl
---

tools/pyhecke/python/pyhecke/gram.py:175 now reads `z = q0 ** 3 / (q0 ** 2 + 1)` (convention D), migrated 2026-08-15 per its own banner at :15/:52. But docs/coordination/trace-convention-registry.json still carries it as C in evaluators.z (:426) and in blocked_migrations (:360-371, owner_decision_required: true).

The registry's own note at :435 says a D reading there means 'something switched it and G_INV is now silently wrong' — so this needs an OWNER eye, not an agent edit. Either the migration was intended and the registry + blocked_migrations entry should be cleared, or G_INV consumers are now reading a different trace rule than the registry advertises.

Related, same module, same PR-worth of scope: z_mp (:622), tr_m_mp (:637) and :746 are still C, and their docstrings assert 'in lockstep with the module's float64 z' — which the :175 migration made false. So gram.py is a live D/C hybrid.

Found while mapping the Wenzl level family (PR #5229); verified by direct read, not taken on a subagent's report. NOT fixed on that branch.

- **Round 97 (`litlfred/qou#8432`)**: Advanced in `feat/round97-monotone-multbound-ncpart-nonuniform-onebody-43c1` (Commit 1 `e883e42fdde30a6d22e385b72041c6f52899312f`, Commit 2 `56d66b28962228fdc58ad152218bdd3754f7c059`, probe sha256 `e41a92695f7287bc24947a7f23e2cb1aff6e02fcb3b0e34fb76f50f0c076b259`).
