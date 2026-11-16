---
# qou-9du2
title: Manifest-vs-witness anchor vocabulary
status: in-progress
type: task
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:22Z
updated_at: 2026-11-16T19:43:00Z
parent: qou-trd0
---

Extracted 2026-10-04 from the prose of session log `qou-9ot5` (work had no bean).


## Round 47 Execution Update (2026-11-16, PR #8152)

- **PR:** https://github.com/litlfred/qou/pull/8152 (`d0d9e522bf023310f599b4d6724b0703e39ccbd4`)
- **Action taken:**
  - Added `Q0_MANIFEST_ANCHOR_ALIASES = {"ideal_muon": "muon", "physical_proton": "proton"}` and `_normalise_q0_anchor_token` in `tools/qou-substrate/python/qou_substrate/witness.py`, normalising manifest-vocabulary tokens to witness-vocabulary tokens across all three `WitnessBuilder` entry paths (`stamp_staleness_metadata`, `wrap_legacy`, and `save(extra)`) and populating `q0Value` when absent.
  - Updated `tools/qou-substrate/tests/test_q0_anchor.py` (`test_bool_True_is_not_a_documented_anchor_and_warns` to assert `ValueError` matching `witness.py:1974`, plus `test_manifest_vocabulary_tokens_normalise_to_witness_tokens` covering all 3 entry paths; `35 passed`).
- **Status:** Kept `in-progress` pending PR #8152 merge and owner review.
