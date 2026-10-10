---
# tc36
title: 'Lean drain: NucleusEmpty — 9 errors, synthesize/defeq/type-mismatch (deeper, multi-root)'
status: completed
type: task
priority: normal
tags:
    - verify-needed
created_at: 2026-06-14T17:29:07Z
updated_at: 2026-06-15T23:18:22Z
parent: w5q7
---

User pick (drain thread, opt 2). Deeper than HeckeH3 (varied root causes L105–242). Verify via lake-cache restore + lean-direct.

TRIAGE (build-unverified read, 2026-06-14): file reads as ALREADY compiling; the 9-error baseline looks stale (dep CanonicalKnotIdSDPUniqueness fixed in 2026-06-09 audit). Action: build-verify via lake-cache restore + lean-direct, NOT proof work.

VERIFICATION (2026-06-15): Verified that `content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean` compiles successfully via `lake exe cache get` and `lake env lean`. No proof work required.
