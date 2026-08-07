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

## 2026-08-08 — root-cause map after a second pass; 11 casualties found, 1 unresolved

Follow-up PR (branch `claude/agent-4685-phase0-collision-itnixj`) found **two more**
LWC-2 casualties beyond the three fixed in #4698, confirming the masking pattern
above. Running total of stripped **type**-prefix regressions: **11**.

| # | File | Decl | State |
|---|---|---|---|
| 1 | `Mathlib/SYTEnumerationFintype.lean:710` | `ext_toSsyt` call site | fixed #4698 |
| 2–10 | `BraidKnot/DeltaLambdaSignRule.lean` | 9 × `Partition.*` | fixed #4698 |
| 11 | `BraidKnot/PartitionNatBridge.lean:34` | `Partition.ext'` | **fixed here** |
| 12 | `BraidKnot/SpechtStandardBasisCore.lean:325` | `Triangular.linearIndependent` | **fixed here (partial — see below)** |

**#4698 mis-diagnosed #11.** Its commit `8149c611` asserted `Partition.ext'` "exists
nowhere in the file's history" and worked around it by declaring a new
`Partition.ext`. The declaration existed at `PartitionNatBridge.lean:34` the whole
time with its `Partition.` prefix stripped. The error came from grepping
`DeltaLambdaSignRule.lean` — the wrong file — and treating the null result as proof
of absence. **Lesson for the rest of this audit: locate the declaration before
concluding it is missing; a null grep is only as good as the file you ran it on.**

Because `PartitionReindex` (which calls it by the full name
`PartitionNatBridge.Partition.ext'`) was not in #4698's verified cone, the miss
survived the merge. **The verification cone must be the full dependents set, not
just the modules under edit.**

### Still open — the Specht cluster (NOT a namespace strip)

Restoring `Triangular.linearIndependent` cleared the field error but
`SpechtStandardBasis` still fails:

```
SpechtStandardBasis.lean:125:85: error: unsolved goals
SpechtStandardBasis.lean:126:40: error: failed to synthesize
```

in `specht_finrank_eq_numSYT` (`Module.finrank_eq_nat_card_basis … ; rfl`). This is a
**proof-level / Mathlib-API break**, a different bug class from the sweep. Four more
modules fail only transitively behind it: `JucysMurphy`,
`SnWedderburnPartitionBridge`, `OVTopAssembly`, `RSKBurnsideDischarge`.

`RSKBurnsideDischarge` failing matters for the burnside roadmap — it is the RSK side
of the discharge. Fixing `specht_finrank_eq_numSYT` is the next unit of work here.

### Verified green (42-module cone, lean-direct, `FAILED: none`)

`PartitionHookProductBridge`, `PartitionReindex`, `PartitionNatBridge`,
`SYTHookFormula`, `IdentityIHLFBridge`, `SytSmallShapeCountsLarger`,
`StandardYoungTableau` (now sorry-free) and their full cones.
