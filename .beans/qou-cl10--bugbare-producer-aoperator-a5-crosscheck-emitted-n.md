---
# qou-cl10
title: 'BUG(bare producer): aoperator_a5_crosscheck emitted no scriptFile/scriptHash and re-running would DELETE the backfilled q0Anchor/q0Value'
status: completed
type: task
priority: normal
created_at: 2026-08-23T08:49:51Z
updated_at: 2026-08-23T08:50:15Z
---

RESOLVED. Producer now emits scriptFile + scriptHash and DERIVES q0Anchor from the q0 the run used (never asserts it). Verified without the full run: scriptFile resolves, scriptHash = a2a639853345 via the canonical file_content_hash helper, derived anchor reproduces the committed 'muon'. Follow-up not taken here: its trM_combiner/trM_transfer payload is float64 via float(), against the STRICT no-float64 probe rule.
