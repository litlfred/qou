---
# qou-gqt5
title: 'DRAIN: 452 float64-padded witness values (fake precision) + source-level mpf(float) detector'
status: todo
type: task
priority: high
created_at: 2026-08-06T23:54:42Z
updated_at: 2026-08-06T23:54:42Z
---

Owner directive: NO FLOAT64. witness_float64_padding_audit.py finds 283 distinct values / 452 occurrences across 61 files (56 live) where a float64 was serialized at 50+ dps, writing 30+ digits of binary-rounding garbage on values with ~8 significant figures. Dominant class: B_AME_MeV / B_target_MeV (AME experimental binding energies). Example: 8.4817962 serialized as 8.4817962000000015621026250300928950309753417968750000000000. DISCRIMINATOR: relative distance to nearest binary64 is ~1e-50 for padded vs ~1e-17 for genuine 50-dps. ROOT CAUSE: mpf(<python float>) instead of mpf('<string literal>') -- the value is binary-rounded before mpmath sees it. Ratchet is in place (baseline 452, --strict blocks new). TWO FOLLOW-UPS: (1) drain by fixing producers to carry values as strings then re-running -- never hand-edit, never --rebaseline to go green; (2) add a SOURCE-level AST detector for mpf(<float literal or float-valued var>) so the anti-pattern is caught at authoring time rather than after it reaches a witness. That second one likely prevents more than the drain fixes.
