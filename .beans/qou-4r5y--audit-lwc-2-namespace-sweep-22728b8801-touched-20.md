---
# qou-4r5y
title: 'AUDIT: LWC-2 namespace sweep (22728b8801) touched 20+ Lean files; 2 confirmed breaks (ext_toSsyt, Partition.*) — audit the rest for stripped type-name prefixes'
status: todo
type: task
created_at: 2026-08-07T17:38:02Z
updated_at: 2026-08-07T17:38:02Z
---


## 2026-08-07 — a THIRD break found; raise the priority

PR #4698 repaired two known breaks (`SYTEnumerationFintype` `ext_toSsyt`,
`DeltaLambdaSignRule` 9 × `Partition.`) and, once the second was fixed,
immediately surfaced a **third** in `PartitionNatBridge.lean:52`: a call to
`Partition.ext'`, a declaration that exists nowhere in the file's history.

The pattern to note for this audit: **breaks mask each other.** Because
`DeltaLambdaSignRule` did not compile, nothing downstream of it was ever
reached, so `PartitionNatBridge`'s own error was invisible. Auditing the
remaining ~20 sweep-touched files by eye is therefore not enough — each
repair can expose a new error behind it. The audit must **build the full
dependents cone after each fix**, not just re-read the diffs.

Verified-clean so far (41-module cone, lean-direct, `FAILED: none`): the
`SYTHookFormula` / `IdentityIHLFBridge` / `SytSmallShapeCountsLarger` /
`PartitionNatBridge` / `SYTCornerListConnection` / `PartitionHookProductBridge`
cones. The rest of the sweep's 20+ files remain unaudited.
