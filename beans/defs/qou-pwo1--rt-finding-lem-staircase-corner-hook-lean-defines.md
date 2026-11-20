---
# qou-pwo1
title: 'RT finding: lem:staircase-corner-hook — Lean defines hCorner as the arithmetic (k-1)+(k-1)+1; no partition is formalised; rho_k convention unstated in .md'
status: todo
type: bug
priority: low
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B10).

- The Lean (`folio/quantum-observable-universe/lean/QOU/StaircaseCornerHook.lean`) has `hCorner k := (k-1)+(k-1)+1` and proves `= 2k−1` by omega. The statement is pure ℕ arithmetic. The staircase partition, arm and leg never appear, so the Lean does not formalise "the hook of cell (0,0) of ρ_k".
- The `.md` does not fix ρ_k = (k, …, 1). With (k−1, …, 1) the hook would be 2k−3.
- The narrative does prove exactly the stated claim under the (k, …, 1) convention. The fix is cheap: define ρ_k and the hook via Mathlib `YoungDiagram`, or state the convention.
