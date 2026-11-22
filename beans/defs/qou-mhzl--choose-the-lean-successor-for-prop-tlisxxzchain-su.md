---
# qou-mhzl
title: Choose the Lean successor for prop TLIsXXZChain (substrate-massive-regime)
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:30Z
updated_at: 2026-11-22T09:50:00Z
parent: qou-uwyf
---

braids-and-knots/substrate-massive-regime.ts refs QOU.OneDim.TLIsXXZChain, a module name. The module declares xxzAnisotropy_eq, tlLoop_add_heckeH, one_lt_anisotropy and others; none is obviously the block's statement. Read the block, pick or write the theorem.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.

## 2026-11-22 finding (thread "Pick Lean refs for TLIsXXZChain and remark")

The block states: q ∈ ℝ, q > 0, q ≠ 1 ⇒ Δ(q) = (q + q⁻¹)/2 > 1. `QOU.OneDim.one_lt_anisotropy {q : ℝ} (hpos : 0 < q) (hne : q ≠ 1) : 1 < xxzAnisotropy q` (TLIsXXZChain.lean:126) is that statement with the same hypotheses; `xxzAnisotropy_eq` unfolds the definition. The contrapositive the prose mentions is `eq_one_of_anisotropy_le`, the scalar identities are `twoMul_eq` / `twoInv_eq`. Proposed ref: `qou:QOU.OneDim.one_lt_anisotropy`. No Lean change. Awaiting owner pick.
