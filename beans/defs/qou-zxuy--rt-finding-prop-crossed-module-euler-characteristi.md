---
# qou-zxuy
title: 'RT finding: prop:crossed-module-euler-characteristic — ''−12 = dim V·χ(Σ₄)'' is a decide-checked coincidence presented as an identity; Φ₀ direction reversed in statement'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B09).

- The Lean (`folio/quantum-observable-universe/lean/QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean`) is `by decide` on a concrete Gaussian-integer computation. Its right-hand side is the named constant `dim_V * euler_bring`. Nothing links the matrix sum to the topology. All three independent legs (RT-1A, RT-2B, RT-3) flagged the identification as numerical only.
- In the `.md` statement, Φ₀: Q₈ → H₃(q) is written with domain Q₈ but defined on σ's, mapping to Q₈ units. The direction is reversed.
- The narrative asserts the intermediate matrix [[−6,3i],[3i,−6]] without computing it. The "Bring bridge" table (−8G, 3/16) is unproved.
- Rescope to "trace = −12, which numerically equals dim V·χ(Σ₄)", or supply a structural argument. See also qou-zmuu, qou-vfy1.
