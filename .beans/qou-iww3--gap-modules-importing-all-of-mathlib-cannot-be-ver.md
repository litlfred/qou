---
# qou-iww3
title: 'GAP: modules importing all of Mathlib cannot be verified from the olean cache'
status: todo
type: task
created_at: 2026-08-08T09:07:47Z
updated_at: 2026-08-08T09:07:47Z
---


## Finding

`QOU.Information.DispersionSuppressionScale` and
`QOU.Molecular.ElectronShellCapacity` fail lean-direct with:

    object file '.lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean'
    of module Mathlib does not exist

Both `import Mathlib` wholesale. The restored cache carries per-module oleans
but not the aggregate `Mathlib.olean`, so these two cannot be verified in this
sandbox.

**This is an environment artifact, not a code defect** — recorded so a later
agent does not mistake it for breakage and "fix" working files. (Compare
`qou-gdc1`, where exactly that mistake was made in the other direction.)

## Next honest step

Either build/obtain the aggregate `Mathlib.olean` for the cache branch, or
narrow these two modules' imports to the specific `Mathlib.*` modules they
use — which is preferable anyway per AGENTS.md §8 ("keep imports minimal").
