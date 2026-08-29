---
# qou-tk8a
title: 'Rebase PR #5500 onto origin/main and regenerate the 4 corpus-wide audit witnesses'
status: completed
type: task
priority: normal
created_at: 2026-08-28T15:07:52Z
updated_at: 2026-08-28T15:48:33Z
parent: qou-jeb1
---

Done on branch claude/muon-anchor-codata-2022-2026-08-22 (PR #5500), rebased onto cdbdc84af1. 2 conflicts, both witness JSON, resolved by taking main + re-running the producer. mergeable_state dirty -> clean. Found an 11th guard the PR inventory missed: q0_value_drift_audit.py:68 held Q_CANONICAL as a transcribed A literal, so the drift detector could not see its own reference drift and was already reporting the re-derived anchor as its single NEW stale entry. Both pins now resolve via _q0_value_for_anchor; verified an exact no-op on pristine main (NEW 0). Also delivered tests/test_muon_anchor_codata_2022.py, which q_parameter.py claimed existed and did not.
