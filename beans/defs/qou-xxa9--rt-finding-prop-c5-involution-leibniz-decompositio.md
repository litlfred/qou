---
# qou-xxa9
title: 'RT finding: prop:c5-involution-leibniz-decomposition — Lean takes c5 := -b^2 - 1/2 as a definition (rung-5 identification not derived); narrative errors; R-specialised without need'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B01).

- The Lean (`folio/quantum-observable-universe/stochastic-mechanics/c5-involution-leibniz-decomposition.lean`) proves c5Decomposition q = −3/2 + 1/[2]_q² over ℝ with q ≠ 0. This is a correct rational-function identity. RT-1 round-trips faithfully.
- The statement needs no archimedean structure. Per §7c it should be over a generic field (char ≠ 2, q ≠ 0, q²+1 ≠ 0).
- The `.md` claims this is THE ladder coefficient c_5. Both RT-2 and RT-3 found that the narrative never derives c_5 = −b² − 1/2 from the ladder; the c_k table is asserted.
- Internal errors in the narrative proof:
  - Step 2 uses h/2 = 1/2 (that is, h = 1); at the silver ratio, h = 2.
  - B_n is called "two averaged crossings", but its second factor is σ₁ − h = σ₁⁻¹.
  - tr_M(B_n − B_p) = h²/2 − h is asserted, not computed.
- Checked: b² = 7/8 at q = 1+√2 is correct. The ladder is convention-C-frame (qou-cds1).
